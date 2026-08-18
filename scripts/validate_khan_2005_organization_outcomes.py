#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / 'research/khan_2005_organizations_outcome_audit_v0_1.json'
RULES = ROOT / 'state/coding_rules_typeA_organization_outcome_v0_1.md'


def main():
    d = json.loads(AUDIT.read_text(encoding='utf-8'))
    assert RULES.exists()
    assert d['original_selected_units'] == 60
    assert d['person_units'] == 57
    assert d['organization_units'] == 3

    orgs = d['organizations']
    assert len(orgs) == 3
    by_name = {x['printed_name']: x for x in orgs}
    assert set(by_name) == {'NHN', '한국공학교육인증원', '경제정의실천시민연합'}

    assert by_name['NHN']['continuity_class'] == 'branched_continuity'
    assert len(by_name['NHN']['successor_entities']) == 2
    assert {x['name'] for x in by_name['NHN']['successor_entities']} == {'NAVER Corp.', 'NHN Corp.'}
    assert by_name['NHN']['t20_window_2024_2026']['trajectory'] == 'transformed_branched'

    assert by_name['한국공학교육인증원']['continuity_class'] == 'direct_continuity'
    assert by_name['한국공학교육인증원']['t20_window_2024_2026']['trajectory'] == 'expanded'
    assert by_name['한국공학교육인증원']['t20_window_2024_2026']['field_leadership'] == 'leading'

    assert by_name['경제정의실천시민연합']['continuity_class'] == 'direct_continuity'
    assert by_name['경제정의실천시민연합']['t20_window_2024_2026']['trajectory'] == 'sustained_high'

    qa = d['qa']
    assert qa['organization_n'] == 3
    assert qa['continuity_counts'] == {'branched_continuity': 1, 'direct_continuity': 2}
    assert qa['trajectory_counts'] == {'transformed_branched': 1, 'expanded': 1, 'sustained_high': 1}
    assert qa['composite_numeric_score_present'] is False
    assert qa['person_outcome_terms_used_as_org_score'] is False
    assert qa['original_denominator_preserved'] == 60

    forbidden = {'major_ge3', 'apex_eq4', 'advancement_delta', 'advancement_class'}
    for org in orgs:
        assert not (forbidden & set(org)), org['printed_name']
        assert org['t20_window_2024_2026']['confidence'] in {'H', 'M-H', 'M'}

    print('OK: Kyunghyang 2005 organization outcome audit v0.1 (3/3)')


if __name__ == '__main__':
    main()
