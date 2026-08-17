#!/usr/bin/env python3
import json
from collections import Counter
from pathlib import Path
from statistics import mean, median

ROOT = Path(__file__).resolve().parents[1]
TYPEA = ROOT / "data/typeA"
T0 = TYPEA / "donga_2010_t0_snapshot_scope_v0_1.json"
TARGET = TYPEA / "donga_2010_target2020_master_v1_0.json"
OUT = TYPEA / "donga_2010_t0_to_target2020_snapshot_change_v0_1.json"

def main():
    t0 = json.loads(T0.read_text(encoding="utf-8"))
    target = json.loads(TARGET.read_text(encoding="utf-8"))
    t0_by = {p["name"]:p for p in t0["people"]}
    rows=[]
    for p in target["people"]:
        name=p["name"]
        if p["final_state"]!="resolved":
            continue
        t0r=t0_by[name]
        ts=t0r["t0_snapshot_scope_score"]
        ys=(p.get("target2020") or {}).get("scope_score")
        if ys is None:
            raise AssertionError(f"resolved row without score: {name}")
        delta=ys-ts
        rows.append({
            "name":name,
            "category":p["category"],
            "t0_snapshot_scope_score":ts,
            "target2020_scope_score":ys,
            "snapshot_delta":delta,
            "t0_role":t0r["t0_role"],
            "target2020_role":(p.get("target2020") or {}).get("role"),
            "t0_review_flags":t0r.get("review_flags",[])
        })
    if len(rows)!=87:
        raise AssertionError(len(rows))
    deltas=Counter(r["snapshot_delta"] for r in rows)
    cats={}
    for cat in dict.fromkeys(r["category"] for r in rows):
        sub=[r for r in rows if r["category"]==cat]
        cats[cat]={
            "n":len(sub),
            "t0_mean":mean(r["t0_snapshot_scope_score"] for r in sub),
            "target2020_mean":mean(r["target2020_scope_score"] for r in sub),
            "mean_snapshot_delta":mean(r["snapshot_delta"] for r in sub),
            "up_n":sum(r["snapshot_delta"]>0 for r in sub),
            "same_n":sum(r["snapshot_delta"]==0 for r in sub),
            "down_n":sum(r["snapshot_delta"]<0 for r in sub)
        }
    payload={
        "schema_version":"donga_2010_t0_to_target2020_snapshot_change_v0.1",
        "generated":"2026-08-18",
        "warning":"This is descriptive target2020 minus provisional T0 snapshot, NOT baseline-adjusted advancement. baseline_peak_through_t0 is not frozen.",
        "population":{"resolved_target_rows":len(rows),"excluded_target_unresolved":10,"excluded_competing_event":3},
        "overall":{
            "t0_mean_same87":mean(r["t0_snapshot_scope_score"] for r in rows),
            "target2020_mean_same87":mean(r["target2020_scope_score"] for r in rows),
            "mean_snapshot_delta":mean(r["snapshot_delta"] for r in rows),
            "median_snapshot_delta":median(r["snapshot_delta"] for r in rows),
            "delta_counts":{str(k):v for k,v in sorted(deltas.items())},
            "up_n":sum(r["snapshot_delta"]>0 for r in rows),
            "same_n":sum(r["snapshot_delta"]==0 for r in rows),
            "down_n":sum(r["snapshot_delta"]<0 for r in rows)
        },
        "by_category":cats,
        "largest_positive":[r for r in rows if r["snapshot_delta"]==max(x["snapshot_delta"] for x in rows)],
        "largest_negative":[r for r in rows if r["snapshot_delta"]==min(x["snapshot_delta"] for x in rows)],
        "rows":rows
    }
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    assert payload["population"]["resolved_target_rows"]==87
    assert payload["overall"]["up_n"]+payload["overall"]["same_n"]+payload["overall"]["down_n"]==87
    print(json.dumps({k:v for k,v in payload.items() if k not in ("rows","largest_positive","largest_negative")},ensure_ascii=False,indent=2))
    print("largest_positive", [x["name"] for x in payload["largest_positive"]])
    print("largest_negative", [x["name"] for x in payload["largest_negative"]])

if __name__=="__main__":
    main()
