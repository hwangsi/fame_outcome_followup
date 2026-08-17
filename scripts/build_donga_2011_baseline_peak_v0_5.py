#!/usr/bin/env python3
import csv, json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TYPEA = ROOT / 'data/typeA'
BASE = TYPEA / 'donga_2011_baseline_peak_through_t0_v0_4.json'
AUDIT = ROOT / 'research/donga_2011_prior_career_audit_v0_4.json'
OUTJ = TYPEA / 'donga_2011_baseline_peak_through_t0_v0_5.json'
OUTC = TYPEA / 'donga_2011_baseline_peak_through_t0_v0_5.csv'


def main():
    base = json.loads(BASE.read_text(encoding='utf-8'))
    audit = json.loads(AUDIT.read_text(encoding='utf-8'))
    corrections = {x['name']: x for x in audit['corrections']}
    nochange = {x['name']: x for x in audit['audited_no_change']}
    audited_names = set(corrections) | set(nochange)
    assert len(audited_names) == audit['qa']['audited_n'] == 12

    people = []
    newly_audited = 0
    corrected = []
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
                corrected.append(n)
                ev = rec
                p['baseline_basis_v0_5'] = 'prior_career_audit_science_business_higher_peak'
            else:
                ev = nochange[n]
                assert ev['baseline_score'] == p['baseline_peak_through_t0'] == 2
                p['baseline_basis_v0_5'] = 'prior_career_audit_science_business_no_higher_peak_identified'
            p['needs_new_person_prior_career_audit'] = False
            p['prior_career_audit_status'] = 'audited_v0_4'
            p['prior_career_audit_confidence'] = ev['confidence']
            p['prior_career_audit_source_urls'] = ev['source_urls']
            p['prior_career_audit_reason'] = ev['reason']
        people.append(p)

    assert newly_audited == 12
    assert corrected == ['이연희','이창준'] or corrected == ['이창준','이연희'], corrected
    pending = [p['name'] for p in people if p.get('needs_new_person_prior_career_audit')]
    expected_pending = ['김애란','김영준','김영하','김은식','박형준','손영래','손흥민','신준호','윤순진','윤태호','이국종','이상이','이자람','하상백','하정우']
    assert sorted(pending) == sorted(expected_pending), pending
    cnt = Counter(p['baseline_peak_through_t0'] for p in people)
    assert cnt == Counter({2: 41, 3: 54, 4: 5}), cnt
    audited_new = 62 - len(pending)
    assert audited_new == 47

    out = {
        'schema_version': 'donga_2011_baseline_peak_through_t0_v0.5',
        'generated': '2026-08-18',
        'status': '47_of_62_new_people_prior_audited_final_15_culture_public_pending',
        'selection_cutoff': '2011-04-01',
        'supersedes': 'data/typeA/donga_2011_baseline_peak_through_t0_v0_4.json',
        't0_ref': base['t0_ref'],
        'audit_refs': [
            'research/donga_2011_prior_career_audit_v0_1.json',
            'research/donga_2011_prior_career_audit_v0_2.json',
            'research/donga_2011_prior_career_audit_v0_3.json',
            'research/donga_2011_prior_career_audit_v0_4.json'
        ],
        'qa': {
            'total': 100,
            'unique_names': len({p['name'] for p in people}),
            'repeat_checked_n': 38,
            'new_person_total_n': 62,
            'new_person_prior_audited_n': audited_new,
            'new_person_prior_audit_pending_n': len(pending),
            'all_new_t0_score3_or4_audited': True,
            'cumulative_corrected_prior_peak_n': 3,
            'cumulative_corrected_prior_peak_names': ['백승헌','이창준','이연희'],
            'this_pass_corrected_n': len(corrected),
            'this_pass_corrected_names': corrected,
            'score_counts': {str(k): v for k, v in sorted(cnt.items())},
            'mean_baseline': sum(p['baseline_peak_through_t0'] for p in people) / 100,
            'pending_names': pending
        },
        'people': people
    }
    assert out['qa']['unique_names'] == 100
    assert abs(out['qa']['mean_baseline'] - 2.64) < 1e-12
    OUTJ.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    fields = [
        'name','category','repeat_2010_2011','t0_snapshot_scope_score',
        'baseline_peak_through_t0','baseline_peak_role','baseline_peak_year',
        'needs_new_person_prior_career_audit','prior_career_audit_status',
        'prior_career_audit_confidence','baseline_basis_v0_5'
    ]
    with OUTC.open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for p in people:
            w.writerow({k: p.get(k) for k in fields})

    print(json.dumps(out['qa'], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
