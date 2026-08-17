#!/usr/bin/env python3
from pathlib import Path
import json
from scipy.stats import spearmanr

def stats(rows):
    rho_peak,p_peak=spearmanr([x["rank"] for x in rows],[x["post_t0_peak_score"] for x in rows])
    rho_delta,p_delta=spearmanr([x["rank"] for x in rows],[x["advancement_delta"] for x in rows])
    return {
      "n":len(rows),
      "major":sum(x["post_t0_peak_score"]>=3 for x in rows),
      "apex":sum(x["post_t0_peak_score"]==4 for x in rows),
      "advanced":sum(x["advancement_delta"]>0 for x in rows),
      "rho_peak":(rho_peak,p_peak),
      "rho_delta":(rho_delta,p_delta),
    }

def main(root=Path(".")):
    nm=json.loads((root/"data/typeA/newsmaker_2003_outcomes_v0_3.json").read_text(encoding="utf-8"))
    h=json.loads((root/"data/typeA/h21_2004_outcomes_v0_1.json").read_text(encoding="utf-8"))
    nm_p=[x for x in nm["people"] if x["domain"]=="politics"]
    h_p=h["people"]
    print("NewsMaker:",stats(nm_p))
    print("H21:",stats(h_p))
    shared=sorted({x["name"] for x in nm_p}&{x["name"] for x in h_p})
    print("Shared persons:",shared)

if __name__=="__main__":
    main()
