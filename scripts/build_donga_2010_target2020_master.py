#!/usr/bin/env python3
"""Build canonical Dong-A 2010 -> target-2020 master dataset from base files + audit patches."""
from __future__ import annotations
import csv, json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TYPEA = ROOT / "data" / "typeA"

BASE_FILES = [
    "donga_2010_target2020_outcomes_v0_1.json",
    "donga_2010_target2020_outcomes_creators_v0_1.json",
    "donga_2010_target2020_outcomes_pioneers_v0_1.json",
    "donga_2010_target2020_outcomes_intellectuals_v0_1.json",
    "donga_2010_target2020_outcomes_economy_v0_1.json",
]
PATCH_FILES = [
    "donga_2010_target2020_pending_audit_round1_academic_v0_1.json",
    "donga_2010_target2020_pending_audit_round2_public_civic_v0_1.json",
    "donga_2010_target2020_pending_audit_round3_resolved_v0_1.json",
]
UNRESOLVED_FILES = [
    "donga_2010_target2020_round3_unresolved_a_v0_1.json",
    "donga_2010_target2020_round3_unresolved_b_v0_1.json",
]
ALIASES = {"한승희": "한숭희"}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def norm(name: str) -> str:
    return ALIASES.get(name, name)


def main():
    roster = load(TYPEA / "donga_2010_canonical_roster_v2_1.json")
    baseline = load(TYPEA / "donga_2010_baseline_from_capture_v1_0.json")

    category_by_name = {}
    for category, names in roster["categories"].items():
        for name in names:
            if name in category_by_name:
                raise ValueError(f"duplicate roster name: {name}")
            category_by_name[name] = category
    if len(category_by_name) != 100:
        raise ValueError(f"roster size != 100: {len(category_by_name)}")

    rows = {}
    for category, persons in baseline["categories"].items():
        for p in persons:
            name = norm(p["name"])
            rows[name] = {
                "name": name,
                "category": category_by_name[name],
                "t0_role": p.get("role"),
                "t0_age": p.get("age"),
                "t0_sex": p.get("sex"),
                "target2020": None,
                "within_window_followup": None,
                "final_state": None,
                "resolution_state": None,
                "resolution_reason": None,
                "provenance_layers": [],
            }

    if set(rows) != set(category_by_name):
        raise ValueError(f"baseline/roster mismatch: missing={set(category_by_name)-set(rows)}, extra={set(rows)-set(category_by_name)}")

    for filename in BASE_FILES:
        data = load(TYPEA / filename)
        for p in data["people"]:
            name = norm(p["name"])
            r = rows[name]
            r["target2020"] = p.get("target2020")
            r["within_window_followup"] = p.get("within_window_followup")
            r["provenance_layers"].append(filename)

    for filename in PATCH_FILES:
        data = load(TYPEA / filename)
        for p in data.get("changes", []):
            name = norm(p["name"])
            r = rows[name]
            r["target2020"] = p.get("target2020", r["target2020"])
            r["resolution_state"] = None
            r["resolution_reason"] = None
            r["provenance_layers"].append(filename)

    for filename in UNRESOLVED_FILES:
        data = load(TYPEA / filename)
        for p in data["rows"]:
            name = norm(p["name"])
            r = rows[name]
            r["resolution_state"] = p["resolution_state"]
            r["resolution_reason"] = p.get("reason")
            r["target2020"] = r["target2020"] or {}
            r["target2020"]["scope_score"] = None
            r["provenance_layers"].append(filename)

    for r in rows.values():
        t = r.get("target2020") or {}
        if r["resolution_state"]:
            r["final_state"] = "unresolved"
        elif t.get("competing_event") or t.get("match", "").startswith("competing_event"):
            r["final_state"] = "competing_event"
        elif t.get("scope_score") is not None:
            r["final_state"] = "resolved"
        else:
            r["final_state"] = "ERROR_unclassified"

    ordered = []
    for category, names in roster["categories"].items():
        ordered.extend(rows[name] for name in names)

    states = Counter(r["final_state"] for r in ordered)
    scores = Counter((r.get("target2020") or {}).get("scope_score") for r in ordered if r["final_state"] == "resolved")
    by_category = {}
    for category in roster["categories"]:
        rr = [r for r in ordered if r["category"] == category]
        by_category[category] = {
            "n": len(rr),
            "resolved": sum(r["final_state"] == "resolved" for r in rr),
            "competing_event": sum(r["final_state"] == "competing_event" for r in rr),
            "unresolved": sum(r["final_state"] == "unresolved" for r in rr),
        }

    expected_states = Counter({"resolved": 87, "competing_event": 3, "unresolved": 10})
    expected_scores = Counter({1: 2, 2: 43, 3: 37, 4: 5})
    if states != expected_states:
        raise ValueError(f"state QA failed: {states} != {expected_states}")
    if scores != expected_scores:
        raise ValueError(f"score QA failed: {scores} != {expected_scores}")

    out = {
        "schema_version": "donga_2010_target2020_master_v1.0",
        "generated_from": {
            "roster": "donga_2010_canonical_roster_v2_1.json",
            "baseline": "donga_2010_baseline_from_capture_v1_0.json",
            "base_files": BASE_FILES,
            "patch_files": PATCH_FILES,
            "unresolved_files": UNRESOLVED_FILES,
        },
        "qa": {
            "total": len(ordered),
            "states": dict(states),
            "resolved_score_counts": {str(k): v for k, v in sorted(scores.items())},
            "by_category": by_category,
        },
        "people": ordered,
    }
    json_path = TYPEA / "donga_2010_target2020_master_v1_0.json"
    csv_path = TYPEA / "donga_2010_target2020_master_v1_0.csv"
    json_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    fields = ["name","category","t0_role","t0_age","t0_sex","final_state","resolution_state","target_role","scope_score","sector","evidence_date","match","confidence"]
    with csv_path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in ordered:
            t = r.get("target2020") or {}
            w.writerow({
                "name": r["name"], "category": r["category"], "t0_role": r["t0_role"], "t0_age": r["t0_age"], "t0_sex": r["t0_sex"],
                "final_state": r["final_state"], "resolution_state": r["resolution_state"], "target_role": t.get("role"), "scope_score": t.get("scope_score"),
                "sector": t.get("sector"), "evidence_date": t.get("evidence_date"), "match": t.get("match"), "confidence": t.get("confidence")
            })
    print(json.dumps(out["qa"], ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
