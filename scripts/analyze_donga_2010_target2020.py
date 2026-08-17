#!/usr/bin/env python3
"""Compute frozen Dong-A 2010 target-year 2020 descriptive metrics.

These are TARGET-YEAR ATTAINMENT metrics, not Type-A post-T0 peak selection precision.
"""
from __future__ import annotations
import json, statistics
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TYPEA = ROOT / "data" / "typeA"
MASTER = TYPEA / "donga_2010_target2020_master_v1_0.json"
OUT = TYPEA / "donga_2010_target2020_metrics_v1_0.json"


def pct(a, b):
    return None if not b else a / b


def main():
    if not MASTER.exists():
        raise SystemExit("master missing; run build_donga_2010_target2020_master.py first")
    data = json.loads(MASTER.read_text(encoding="utf-8"))
    people = data["people"]
    resolved = [p for p in people if p["final_state"] == "resolved"]
    competing = [p for p in people if p["final_state"] == "competing_event"]
    unresolved = [p for p in people if p["final_state"] == "unresolved"]
    scores = [p["target2020"]["scope_score"] for p in resolved]

    n_total = len(people)
    n_resolved = len(resolved)
    n_competing = len(competing)
    n_unresolved = len(unresolved)
    at_risk = n_total - n_competing
    score_counts = Counter(scores)
    ge2 = sum(s >= 2 for s in scores)
    ge3 = sum(s >= 3 for s in scores)
    eq4 = sum(s == 4 for s in scores)

    by_cat = {}
    categories = []
    for p in people:
        if p["category"] not in categories:
            categories.append(p["category"])
    for cat in categories:
        rows = [p for p in people if p["category"] == cat]
        rr = [p for p in rows if p["final_state"] == "resolved"]
        cc = [p for p in rows if p["final_state"] == "competing_event"]
        uu = [p for p in rows if p["final_state"] == "unresolved"]
        ss = [p["target2020"]["scope_score"] for p in rr]
        by_cat[cat] = {
            "n": len(rows),
            "resolved": len(rr),
            "competing_event": len(cc),
            "unresolved": len(uu),
            "non_competing_n": len(rows)-len(cc),
            "resolution_rate_among_non_competing": pct(len(rr), len(rows)-len(cc)),
            "resolved_mean_scope": None if not ss else sum(ss)/len(ss),
            "resolved_median_scope": None if not ss else statistics.median(ss),
            "resolved_ge3_n": sum(s >= 3 for s in ss),
            "resolved_ge3_rate": pct(sum(s >= 3 for s in ss), len(ss)),
            "resolved_eq4_n": sum(s == 4 for s in ss),
            "resolved_eq4_rate": pct(sum(s == 4 for s in ss), len(ss)),
            "resolved_score_counts": {str(k): v for k, v in sorted(Counter(ss).items())},
        }

    result = {
        "schema_version": "donga_2010_target2020_metrics_v1.0",
        "metric_scope": "target_year_2020_attainment_not_post_t0_peak_selection_precision",
        "freeze_ref": "state/donga_2010_target2020_freeze_v1_0.json",
        "population": {
            "total": n_total,
            "resolved": n_resolved,
            "competing_event": n_competing,
            "unresolved": n_unresolved,
            "non_competing": at_risk,
            "resolved_fraction_total": pct(n_resolved, n_total),
            "resolved_fraction_non_competing": pct(n_resolved, at_risk),
        },
        "resolved_only": {
            "score_counts": {str(k): v for k, v in sorted(score_counts.items())},
            "mean_scope": sum(scores)/len(scores),
            "median_scope": statistics.median(scores),
            "scope_ge2_n": ge2,
            "scope_ge2_rate": pct(ge2, n_resolved),
            "scope_ge3_n": ge3,
            "scope_ge3_rate": pct(ge3, n_resolved),
            "scope_eq4_n": eq4,
            "scope_eq4_rate": pct(eq4, n_resolved),
        },
        "sensitivity_non_competing_denominator": {
            "denominator": at_risk,
            "assumption": "unresolved rows are bounded as all below vs all meeting each threshold; competing events excluded",
            "scope_ge2": {"known_n": ge2, "lower_bound": ge2/at_risk, "upper_bound": (ge2+n_unresolved)/at_risk},
            "scope_ge3": {"known_n": ge3, "lower_bound": ge3/at_risk, "upper_bound": (ge3+n_unresolved)/at_risk},
            "scope_eq4": {"known_n": eq4, "lower_bound": eq4/at_risk, "upper_bound": (eq4+n_unresolved)/at_risk},
        },
        "by_category": by_cat,
        "interpretation_guardrails": [
            "Do not call scope>=3 target-year attainment 'selection precision'; Type-A selection precision is defined on post-T0 peak score.",
            "Do not score unresolved rows as zero.",
            "Do not treat competing-event deaths as prediction failures.",
            "Category comparisons are descriptive because editorial categories differ in career structure and unresolved rates.",
            "The printed roster is alphabetic within categories, so ranking accuracy is not estimable from list order."
        ]
    }

    # Fixed QA values from the frozen dataset.
    assert (n_total, n_resolved, n_competing, n_unresolved) == (100, 87, 3, 10)
    assert score_counts == Counter({2: 43, 3: 37, 4: 5, 1: 2})
    assert sum(scores) == 219
    assert (ge2, ge3, eq4) == (85, 42, 5)

    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
