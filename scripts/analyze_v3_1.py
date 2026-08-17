#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Analyze outcomes_v3.json: T+10→T+20 transitions, sector and age-known subset."""
from pathlib import Path
import json, pandas as pd, numpy as np
from scipy.stats import fisher_exact

STRICT={"exact_year","within_window","timeline_covers_target"}
HIGH={"upward_expansion","sustained_high"}

def main(root=Path(".")):
    d=json.loads((root/"data/outcomes_v3.json").read_text(encoding="utf-8"))
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
