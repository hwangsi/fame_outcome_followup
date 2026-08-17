#!/usr/bin/env python3
import csv, json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TYPEA = ROOT / 'data/typeA'
BASE = TYPEA / 'donga_2011_baseline_peak_through_t0_v0_5.json'
AUDIT = ROOT / 'research/donga_2011_prior_career_audit_v0_5.json'
OUTJ = TYPEA / 'donga_2011_baseline_peak_through_t0_v1_0.json'
OUTC = TYPEA / 'donga_2011_baseline_peak_through_t0_v1_0.csv'

EXPECTED_CORRECTED = {'백승헌','이창준','이연희','이상이','이국종','이자람'}


def main():
    base = json.loads(BASE.read_text(encoding='utf-8'))
    audit = json.loads(AUDIT.read_text(encoding='utf-8'))
    corrections = {x['name']: x for x in audit['corrections']}
    nochange = {x['name']: x for x in audit['audited_no_change']}
    audited_names = set(corrections) | set(nochange)
    assert len(audited_names) == audit['qa']['audited_n'] == 15

    people = []
    newly_audited = 0
    corrected_this_pass = []
    for p0 in base['people']:
        p = dict(p0)
        n = p['name']
        if n in audited_names:
            assert not p['repeat_2010_2011']
            assert p.get('needs_new_person_prior_career_audit') is True, f'already audited: {n}'
            assert p['t0_snapshot_scope_score'] == 2, (n, p['t0_snapshot_scope_score'])
            newly_audited += 1
            rec = corrections.get(n)
            if rec:
                assert rec['baseline_score'] > p['baseline_peak_through_t0']
                p['baseline_peak_through_t0'] = rec['baseline_score']
                p['baseline_peak_role'] = rec['baseline_peak_role']
                p['baseline_peak_year'] = rec['baseline_peak_year']
                corrected_this_pass.append(n)
                ev = rec
                p['baseline_basis_v1_0'] = 'final_prior_career_audit_higher_peak'
            else:
                ev = nochange[n]
                assert ev['baseline_score'] == p['baseline_peak_through_t0'] == 2
                p['baseline_basis_v1_0'] = 'final_prior_career_audit_no_higher_peak_identified'
            p['needs_new_person_prior_career_audit'] = False
            p['prior_career_audit_status'] = 'audited_v0_5_final'
            p['prior_career_audit_confidence'] = ev['confidence']
            p['prior_career_audit_source_urls'] = ev['source_urls']
            p['prior_career_audit_reason'] = ev['reason']
        people.append(p)

    assert newly_audited == 15
    assert set(corrected_this_pass) == {'이상이','이국종','이자람'}, corrected_this_pass
    pending = [p['name'] for p in people if p.get('needs_new_person_prior_career_audit')]
    assert pending == [], pending
    cnt = Counter(p['baseline_peak_through_t0'] for p in people)
    assert cnt == Counter({2: 38, 3: 57, 4: 5}), cnt

    corrected_all = {p['name'] for p in people if p['baseline_peak_through_t0'] > p['t0_snapshot_scope_score']}
    assert corrected_all == EXPECTED_CORRECTED, corrected_all
    assert sum(p['repeat_2010_2011'] for p in people) == 38
    assert len(people) == 100 and len({p['name'] for p in people}) == 100

    out = {
        'schema_version': 'donga_2011_baseline_peak_through_t0_v1.0',
        'generated': '2026-08-18',
        'status': 'freeze_candidate_100_of_100_prior_career_audited',
        'selection_cutoff': '2011-04-01',
        'supersedes': 'data/typeA/donga_2011_baseline_peak_through_t0_v0_5.json',
        't0_ref': base['t0_ref'],
        'rules_ref': 'state/coding_rules_typeA_sector_scope_v0_1.md',
        'audit_refs': [
            'research/donga_2011_prior_career_audit_v0_1.json',
            'research/donga_2011_prior_career_audit_v0_2.json',
            'research/donga_2011_prior_career_audit_v0_3.json',
            'research/donga_2011_prior_career_audit_v0_4.json',
            'research/donga_2011_prior_career_audit_v0_5.json'
        ],
        'method': {
            'repeat_38': 'Compared against frozen 2010 lifetime baseline so pre-2010 achievements cannot be lost.',
            'new_62': 'All 62 new entrants received dedicated pre-2011 career audit in five risk-prioritized passes.',
            'baseline_definition': 'Maximum sector-normalized scope reached at any time through 2011-04-01; T0 snapshot remains a separate field.'
        },
        'qa': {
            'total': 100,
            'unique_names': 100,
            'repeat_checked_n': 38,
            'new_person_total_n': 62,
            'new_person_prior_audited_n': 62,
            'new_person_prior_audit_pending_n': 0,
            'all_prior_career_audits_complete': True,
            'baseline_greater_than_t0_n': len(corrected_all),
            'baseline_greater_than_t0_names': sorted(corrected_all),
            'this_pass_corrected_n': len(corrected_this_pass),
            'this_pass_corrected_names': sorted(corrected_this_pass),
            'score_counts': {str(k): v for k, v in sorted(cnt.items())},
            'mean_baseline': sum(p['baseline_peak_through_t0'] for p in people) / 100
        },
        'people': people
    }
    assert abs(out['qa']['mean_baseline'] - 2.67) < 1e-12
    OUTJ.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    fields = [
        'name','category','repeat_2010_2011','t0_snapshot_scope_score',
        'baseline_peak_through_t0','baseline_peak_role','baseline_peak_year',
        'prior_career_audit_status','prior_career_audit_confidence'
    ]
    with OUTC.open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for p in people:
            w.writerow({k: p.get(k) for k in fields})

    print(json.dumps(out['qa'], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
