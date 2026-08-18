#!/usr/bin/env python3
import json
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / 'research/khan_2005_economy_person9_peak_audit_v0_1.json'
REC = ROOT / 'research/khan_2005_korea_leaders60_recovery_v0_1.json'
OUT = ROOT / 'data/typeA/khan_2005_economy_person9_peak_master_v1_0.json'
METRICS = ROOT / 'data/typeA/khan_2005_economy_person9_metrics_v1_0.json'
FREEZE = ROOT / 'state/khan_2005_economy_person9_freeze_v1_0.json'


def main():
    a = json.loads(AUDIT.read_text(encoding='utf-8'))
    r = json.loads(REC.read_text(encoding='utf-8'))

    people = a['people']
    econ = [u for u in r['units'] if u['field'] == '경제']
    econ_people = [u for u in econ if u['unit_type'] == 'person']
    econ_orgs = [u for u in econ if u['unit_type'] == 'organization']

    assert len(econ) == 10
    assert len(econ_people) == 9
    assert len(econ_orgs) == 1
    assert econ_orgs[0]['canonical_name'] == 'NHN'
    assert {u['canonical_name'] for u in econ_people} == {p['name'] for p in people}
    assert len(people) == 9 and len({p['name'] for p in people}) == 9

    q = a['qa']
    assert q['baseline_distribution'] == {'2': 2, '3': 4, '4': 3}
    assert abs(mean(p['baseline_peak_through_t0'] for p in people) - 28/9) < 1e-12
    assert q['post_peak_distribution'] == {'3': 3, '4': 6}
    assert abs(mean(p['post_t0_peak_score'] for p in people) - 33/9) < 1e-12
    assert sum(p['post_t0_peak_score'] >= 3 for p in people) == 9
    assert sum(p['post_t0_peak_score'] == 4 for p in people) == 6
    assert sum(p['advancement_class'] == 'advanced' for p in people) == 4
    assert sum(p['advancement_class'] == 'sustained_high' for p in people) == 5

    rows = []
    for p in people:
        x = dict(p)
        x.update({
            'outlet': '경향신문',
            'selection_date': '2005-12-15',
            'publication_date': '2005-12-30',
            'cohort_unit': 'khan_2005_korea_leaders60_economy_person9',
            'list_title': '한국을 이끌 60인 — 경제 person9',
            'domain': 'economy',
            'design': 'multistage_public_awareness_expert_final_field10_mixed_unit',
            'selection_mechanism': '1168_initial_to_185_expert_recommendation_to_public1266_to_final_expert12',
            'parent_selection': 'khan_2005_korea_leaders60',
            'parent_selected_units': 60,
            'field_selected_units': 10,
            'field_person_units': 9,
            'field_organization_units': 1,
            'excluded_other_unit_type': 'NHN',
            'field_specific_secondary': True,
            'unit_type_secondary': 'person',
            'major_ge3': p['post_t0_peak_score'] >= 3,
            'apex_eq4': p['post_t0_peak_score'] == 4
        })
        rows.append(x)

    metrics = {
        'schema_version': 'khan_2005_economy_person9_metrics_v1.0',
        'generated': '2026-08-18',
        'population': {
            'person_n': 9,
            'assessable_person_n': 9,
            'field_selected_units': 10,
            'field_person_units': 9,
            'field_organization_units': 1,
            'organization_unit': 'NHN',
            'parent_selected_units': 60,
            'field_specific_secondary': True,
            'unit_type_secondary': 'person'
        },
        'baseline': {'mean': 28/9, 'distribution': {'2': 2, '3': 4, '4': 3}},
        'post_peak': {'mean': 33/9, 'distribution': {'3': 3, '4': 6}},
        'outcomes': {
            'major_n': 9, 'major_rate': 1.0,
            'apex_n': 6, 'apex_rate': 6/9,
            'advanced_n': 4, 'advanced_rate': 4/9,
            'sustained_high_n': 5, 'sustained_high_rate': 5/9,
            'lower_than_baseline_n': 0,
            'not_assessable_n': 0
        },
        'apex_names': ['박현주', '이구택', '이재용', '이재현', '정의선', '최태원'],
        'advanced_names': ['김석동', '박현주', '이재용', '정의선'],
        'sustained_high_names': ['이구택', '이재현', '장하준', '최태원', '황창규'],
        'guardrails': a['interpretation_guardrails']
    }

    master = {
        'schema_version': 'khan_2005_economy_person9_peak_master_v1.0',
        'generated': '2026-08-18',
        'status': 'field_mixed_unit_person_subset_peak_audited_9_of_9',
        'cohort': {
            'publication': '경향신문',
            'selection_cutoff': '2005-12-15',
            'publication_date': '2005-12-30',
            'title': '한국을 이끌 60인 — 경제 person9',
            'cohort_type': 'A',
            'domain': 'economy',
            'person_n': 9,
            'field_selected_units': 10,
            'field_organization_unit': 'NHN',
            'parent_selection': 'khan_2005_korea_leaders60',
            'parent_selected_units': 60,
            'field_specific_secondary': True,
            'unit_type_secondary': 'person',
            'design': 'multistage_public_awareness_expert_final_field10_mixed_unit'
        },
        'metrics': metrics,
        'people': rows,
        'source_audit': str(AUDIT.relative_to(ROOT))
    }

    freeze = {
        'schema_version': 'khan_2005_economy_person9_freeze_v1.0',
        'generated': '2026-08-18',
        'population': metrics['population'],
        'baseline': metrics['baseline'],
        'post_peak': metrics['post_peak'],
        'outcomes': metrics['outcomes'],
        'apex_names': metrics['apex_names'],
        'advanced_names': metrics['advanced_names'],
        'sustained_high_names': metrics['sustained_high_names'],
        'guardrails': metrics['guardrails']
    }

    OUT.write_text(json.dumps(master, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    METRICS.write_text(json.dumps(metrics, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    FREEZE.write_text(json.dumps(freeze, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(freeze, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
