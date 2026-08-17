#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Analyze NewsMaker 2003 Type A cohort v0.3.

Reports raw selection precision, apex precision, baseline-adjusted advancement,
and rank correlations with both post-T0 peak scope and advancement delta.
"""
from pathlib import Path
import json
from scipy.stats import spearmanr


def main(root=Path(".")):
    p=root/"data"/"typeA"/"newsmaker_2003_outcomes_v0_3.json"
    d=json.loads(p.read_text(encoding="utf-8"))
    for domain in ("politics","economy"):
        rows=[x for x in d["people"] if x["domain"]==domain]
        ranks=[x["rank"] for x in rows]
        peaks=[x["post_t0_peak_score"] for x in rows]
        deltas=[x["advancement_delta"] for x in rows]
        rho_peak,p_peak=spearmanr(ranks,peaks)
        rho_delta,p_delta=spearmanr(ranks,deltas)
        major=sum(x["post_t0_peak_score"]>=3 for x in rows)
        apex=sum(x["post_t0_peak_score"]==4 for x in rows)
        advanced=sum(x["baseline_adjusted_class"]=="advanced" for x in rows)
        print(domain, "n=",len(rows))
        print(" major precision:",major,"/",len(rows))
        print(" apex precision:",apex,"/",len(rows))
        print(" baseline-adjusted advanced:",advanced,"/",len(rows))
        print(" Spearman rank vs peak:",rho_peak,p_peak)
        print(" Spearman rank vs advancement delta:",rho_delta,p_delta)


if __name__=="__main__":
    main()
