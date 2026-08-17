#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Analyze v3 outcomes: T+10→T+20 transitions, sector and age-known subset.

Reads either:
- data/outcomes_v3.json
- data/outcomes_v3.json.xz
"""
from pathlib import Path
import json, lzma
import pandas as pd
import numpy as np
from scipy.stats import fisher_exact

STRICT={"exact_year","within_window","timeline_covers_target"}
HIGH={"upward_expansion","sustained_high"}

def load_data(root: Path):
    raw=root/"data/outcomes_v3.json"
    if raw.exists():
        return json.loads(raw.read_text(encoding="utf-8"))
    packed=root/"data/outcomes_v3.json.xz"
    if packed.exists():
        return json.loads(lzma.decompress(packed.read_bytes()).decode("utf-8"))
    raise FileNotFoundError("Expected data/outcomes_v3.json or data/outcomes_v3.json.xz")

def main(root=Path(".")):
    d=load_data(root)
    rows=[]
    for p in d["people"]:
        rows.append({
            "name":p["name"],"year":p["year"],"dept":p["dept_t0"],"birth":p.get("birth"),
            "t10_level":p["t10"]["level"],"t10_match":p["t10"]["match"],
            "t20_level":p["t20"]["level"],"t20_match":p["t20"]["match"],
            "status":p["status_trajectory"],"sector_transition":p["sector_transition"],
        })
    df=pd.DataFrame(rows)
    df["age_t0"]=df.apply(lambda r:r["year"]-r["birth"] if pd.notna(r["birth"]) else np.nan,axis=1)
    strict_both=df[df.t10_match.isin(STRICT)&df.t20_match.isin(STRICT)]
    print("Strict at both T+10/T+20:",len(strict_both))
    print(pd.crosstab(strict_both.t10_level,strict_both.t20_level))
    print("\nLifetime high-status by T0 sector")
    print(pd.crosstab(df.dept,df.status.isin(HIGH)))
    ind=df.dept=="산업계"
    tab=np.array([
      [(ind & df.status.isin(HIGH)).sum(),(ind & ~df.status.isin(HIGH)).sum()],
      [((~ind)&df.status.isin(HIGH)).sum(),((~ind)&~df.status.isin(HIGH)).sum()]
    ])
    print("Industry vs others Fisher:",fisher_exact(tab))
    print("\nBirth year coverage:",df.birth.notna().sum(),"/",len(df))

if __name__=="__main__":
    main()
