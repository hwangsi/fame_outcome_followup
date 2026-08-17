#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROSTER = ROOT / 'research/khan_2004_17th_assembly_newleaders_roster_v0_1.json'
COMMON = ROOT / 'data/typeA/typeA_common_master_v0_2.json'
OUT = ROOT / 'analysis/khan_2004_common_overlap_v0_1.json'


def main():
    r = json.loads(ROSTER.read_text(encoding='utf-8'))
    c = json.loads(COMMON.read_text(encoding='utf-8'))

    new_names = {p['name'] for p in r['people']}
    assert len(new_names) == 20

    by_name = {}
    for p in c['people']:
        by_name[p['name']] = p

    placements_by_name = {}
    for p in c['placements']:
        placements_by_name.setdefault(p['name'], []).append(p)

    overlaps = []
    for name in sorted(new_names & set(by_name)):
        old = by_name[name]
        placements = sorted(
            placements_by_name.get(name, []),
            key=lambda x: (x['selection_date'], x['outlet'], x['cohort_unit'])
        )
        overlaps.append({
            'name': name,
            'existing_person_id': old['person_id'],
            'existing_placement_count': old['placement_count'],
            'existing_outlets': old['outlets'],
            'existing_selection_years': old['selection_years'],
            'existing_cohort_units': old['cohort_units'],
            'existing_placements': [
                {
                    'placement_id': x['placement_id'],
                    'outlet': x['outlet'],
                    'selection_date': x['selection_date'],
                    'cohort_unit': x['cohort_unit'],
                    'domain': x['domain'],
                    'baseline_peak_through_t0': x['baseline_peak_through_t0'],
                    'post_t0_peak_score': x['post_t0_peak_score'],
                    'advancement_class': x['advancement_class']
                }
                for x in placements
            ],
            'identity_status': 'requires_cross_cohort_identity_confirmation_before_merge'
        })

    out = {
        'schema_version': 'khan_2004_common_overlap_v0.1',
        'generated': '2026-08-18',
        'new_cohort_n': 20,
        'existing_common_person_n': c['qa']['unique_people'],
        'overlap_name_n': len(overlaps),
        'overlap_names': [x['name'] for x in overlaps],
        'overlaps': overlaps,
        'guardrails': [
            'Name intersection is only a candidate identity match, not proof of identity.',
            'Political names should be verified against 2004 party/office and existing cohort contemporaneous role before merge.',
            'No new placement may be added to the common master until each overlap is identity-confirmed.',
            'Non-overlap names receive new person IDs only when the Kyunghyang cohort is promoted from recovery to audited outcome master.'
        ]
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
