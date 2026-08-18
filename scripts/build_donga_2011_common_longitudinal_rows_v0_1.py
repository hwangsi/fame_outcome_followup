#!/usr/bin/env python3
import hashlib
import json
from collections import Counter
from pathlib import Path

from identity_resolution import resolve_identity_key, person_id_from_identity_key

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'data/typeA/donga_2011_common_longitudinal_rows_v0_1.json'
FREEZE = ROOT / 'state/donga_2011_common_longitudinal_rows_freeze_v0_1.json'

COHORT_UNIT = 'donga_2011_10yr_100'
OUTLET = '동아일보'
TARGET_YEAR = 2021
WINDOW_START = '2020-01-01'
WINDOW_END = '2022-12-31'

SOURCES = [
    'research/donga_2011_t10_repeat_economy_audit_v0_1.json',
    'research/donga_2011_t10_repeat_public_politics_audit_v0_1.json',
    'research/donga_2011_t10_repeat_creators_audit_v0_1.json',
    'research/donga_2011_t10_repeat_science_pioneers_audit_v0_1.json',
    'research/donga_2011_t10_newentrant_inwindow18_audit_v0_1.json',
    'research/donga_2011_t10_pending44_batch1_institutional_v0_1.json',
    'research/donga_2011_t10_pending36_batch2_continuity_v0_1.json',
    'research/donga_2011_t10_remaining30_creative_sports_v1_0.json',
    'research/donga_2011_t10_remaining30_public_legal_v1_0.json',
    'research/donga_2011_t10_remaining30_hard_academic_business_v1_0.json',
]


def stable_snapshot_id(name):
    s = f'{OUTLET}|{COHORT_UNIT}|{name}|{TARGET_YEAR}'
    return 'snap-' + hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


def extract_rows(d, source_ref):
    for key in ('people', 'rows', 'outcomes'):
        v = d.get(key)
        if isinstance(v, list):
            return v
    raise AssertionError(f'no row list in {source_ref}; keys={sorted(d.keys())}')


def normalize_status(r):
    raw = r.get('status') or r.get('outcome_status') or r.get('assessment_status')
    if raw in ('assessable', 'resolved', 'observed'):
        return 'assessable'
    if raw in ('competing_event', 'death_competing_event', 'death'):
        return 'competing_event'
    if raw in ('untraceable', 'unresolved', 'not_traceable'):
        return 'untraceable'
    if raw is None and r.get('scope_score') is not None:
        return 'assessable'
    return raw


def normalized_match(r):
    return r.get('match') or r.get('evidence_match') or r.get('provenance')


def main():
    normalized = []
    for rel in SOURCES:
        p = ROOT / rel
        assert p.exists(), rel
        d = json.loads(p.read_text(encoding='utf-8'))
        rows = extract_rows(d, rel)
        for r in rows:
            name = r['name']
            status = normalize_status(r)
            score = r.get('scope_score')
            if status == 'assessable':
                assert isinstance(score, int) and 0 <= score <= 4, (rel, name, score)
            else:
                assert score is None, (rel, name, status, score)
            ik = resolve_identity_key(name, OUTLET, COHORT_UNIT)
            normalized.append({
                'snapshot_id': stable_snapshot_id(name),
                'person_id': person_id_from_identity_key(ik),
                'identity_key': ik,
                'name': name,
                'outlet': OUTLET,
                'cohort_unit': COHORT_UNIT,
                'selection_year': 2011,
                'window_id': 't10',
                'target_year': TARGET_YEAR,
                'window_start': WINDOW_START,
                'window_end': WINDOW_END,
                'status': status,
                'scope_score': score,
                'scope_ge2': (score >= 2) if score is not None else None,
                'major_ge3': (score >= 3) if score is not None else None,
                'apex_eq4': (score == 4) if score is not None else None,
                'role_at_window': r.get('role_at_window') or r.get('role') or r.get('snapshot_role'),
                'evidence_date': r.get('evidence_date'),
                'match': normalized_match(r),
                'confidence': r.get('confidence'),
                'evidence_refs': r.get('evidence_refs') or r.get('sources') or [],
                'source_ref': rel,
                'source_schema': d.get('schema_version'),
            })

    names = [r['name'] for r in normalized]
    assert len(normalized) == 100, len(normalized)
    assert len(set(names)) == 100, [n for n, c in Counter(names).items() if c != 1]
    assert len({r['snapshot_id'] for r in normalized}) == 100

    status_counts = Counter(r['status'] for r in normalized)
    assert status_counts == {'assessable': 90, 'competing_event': 1, 'untraceable': 9}, status_counts
    assessed = [r for r in normalized if r['status'] == 'assessable']
    score_counts = Counter(r['scope_score'] for r in assessed)
    assert score_counts == {0: 1, 1: 2, 2: 24, 3: 59, 4: 4}, score_counts
    assert sum(r['scope_ge2'] for r in assessed) == 87
    assert sum(r['major_ge3'] for r in assessed) == 63
    assert sum(r['apex_eq4'] for r in assessed) == 4

    exact_n = sum(
        1 for r in assessed
        if r['match'] in ('exact_year', 'exact_year_by_official_tenure', 'exact_2021', 'exact_2021_or_tenure')
        or (r['evidence_date'] is not None and str(r['evidence_date']).startswith('2021') and not str(r['match'] or '').startswith('nearest'))
    )
    nearest_2020_n = sum(1 for r in assessed if str(r['evidence_date'] or '').startswith('2020') and str(r['match'] or '').startswith('nearest'))
    nearest_2022_n = sum(1 for r in assessed if str(r['evidence_date'] or '').startswith('2022') and str(r['match'] or '').startswith('nearest'))
    assert exact_n == 81, exact_n
    assert nearest_2020_n == 8, nearest_2020_n
    assert nearest_2022_n == 1, nearest_2022_n

    normalized.sort(key=lambda r: r['name'])
    qa = {
        'rows': 100,
        'unique_names': 100,
        'unique_snapshot_ids': 100,
        'assessable_n': 90,
        'competing_event_n': 1,
        'untraceable_n': 9,
        'score_counts_assessable': {str(k): score_counts[k] for k in range(5)},
        'scope_ge2_n': 87,
        'major_ge3_n': 63,
        'apex_eq4_n': 4,
        'exact_2021_or_tenure_n': 81,
        'nearest_2020_n': 8,
        'nearest_2022_n': 1,
        'source_batch_n': len(SOURCES),
    }
    payload = {
        'schema_version': 'donga_2011_common_longitudinal_rows_v0.1',
        'generated': '2026-08-18',
        'status': 'materialized_100_of_100_canonical_t10_rows',
        'semantic_adapter_ref': 'data/typeA/donga_2011_common_longitudinal_adapter_v0_1.json',
        'qa': qa,
        'rows': normalized,
    }
    freeze = {
        'schema_version': 'donga_2011_common_longitudinal_rows_freeze_v0.1',
        'generated': '2026-08-18',
        'qa': qa,
        'source_refs': SOURCES,
        'guardrails': [
            'one canonical snapshot row per 2011 selected unit',
            'explicit-target-2021 and T+10 are semantic aliases, not duplicate observations',
            'competing event and untraceable remain null rather than score 0',
            'direct 2021 evidence has priority over nearest 2020/2022 evidence',
            'repeat-selected people remain placements here; dependence is handled in person-level analyses',
        ],
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    FREEZE.write_text(json.dumps(freeze, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(freeze, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
