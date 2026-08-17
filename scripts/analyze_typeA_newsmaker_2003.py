#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import json
from scipy.stats import spearmanr

def main(root=Path(".")):
    p=root/"data"/"typeA"/"newsmaker_2003_outcomes_v0_2.json"
    d=json.loads(p.read_text(encoding="utf-8"))
    for domain in ("politics","economy"):
        rows=[x for x in d["people"] if x["domain"]==domain]
        ranks=[x["rank"] for x in rows]
        peaks=[x["post_t0_peak_score"] for x in rows]
        rho,pval=spearmanr(ranks,peaks)
        major=sum(x["post_t0_peak_score"]>=3 for x in rows)
        apex=sum(x["post_t0_peak_score"]==4 for x in rows)
        advanced=sum(x["baseline_adjusted_class"]=="advanced" for x in rows)
        print(domain, "n=",len(rows))
        print(" major precision:",major,"/",len(rows))
        print(" apex precision:",apex,"/",len(rows))
        print(" baseline-adjusted advanced:",advanced,"/",len(rows))
        print(" Spearman rank vs peak:",rho,pval)

if __name__=="__main__":
    main()
