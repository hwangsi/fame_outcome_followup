#!/usr/bin/env python3
import csv, json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TYPEA = ROOT / 'data/typeA'
BASE = TYPEA / 'donga_2011_baseline_peak_through_t0_v0_1.json'
AUDIT = ROOT / 'research/donga_2011_prior_career_audit_v0_1.json'
OUTJ = TYPEA / 'donga_2011_baseline_peak_through_t0_v0_2.json'
OUTC = TYPEA / 'donga_2011_baseline_peak_through_t0_v0_2.csv'


def main():
    base = json.loads(BASE.read_text(encoding='utf-8'))
    audit = json.loads(AUDIT.read_text(encoding='utf-8'))
    corrections = {x['name']: x for x in audit['corrections']}
    nochange = {x['name']: x for x in audit['audited_no_change']}
    audited_names = set(corrections) | set(nochange)
    assert len(audited_names) == audit['qa']['audited_n'] == 9

    people = []
    corrected = []
    audited_new = 0
    for p0 in base['people']:
        p = dict(p0)
        n = p['name']
        if n in audited_names:
            assert not p['repeat_2010_2011'], f'audit pass unexpectedly contains repeat name: {n}'
            audited_new += 1
            rec = corrections.get(n)
            if rec:
                assert p['baseline_peak_through_t0'] == rec['t0_score'], (n, p['baseline_peak_through_t0'])
                assert rec['baseline_score'] > p['baseline_peak_through_t0']
                p['baseline_peak_through_t0'] = rec['baseline_score']
                p['baseline_peak_role'] = rec['baseline_peak_role']
                p['baseline_peak_year'] = rec['baseline_peak_year']
                p['baseline_basis_v0_2'] = 'prior_career_audit_higher_than_2011_t0'
                corrected.append(n)
                ev = rec
            else:
                ev = nochange[n]
                assert ev['baseline_score'] == p['baseline_peak_through_t0']
                p['baseline_basis_v0_2'] = 'prior_career_audit_no_higher_peak_identified'
            p['needs_new_person_prior_career_audit'] = False
            p['prior_career_audit_status'] = 'audited_v0_1'
            p['prior_career_audit_confidence'] = ev['confidence']
            p['prior_career_audit_source_urls'] = ev['source_urls']
            p['prior_career_audit_reason'] = ev['reason']
        people.append(p)

    assert audited_new == 9
    assert corrected == ['백승헌'], corrected
    pending = [p['name'] for p in people if p.get('needs_new_person_prior_career_audit')]
    assert len(pending) == 53, len(pending)
    cnt = Counter(p['baseline_peak_through_t0'] for p in people)
    assert cnt == Counter({2: 43, 3: 52, 4: 5}), cnt

    out = {
        'schema_version': 'donga_2011_baseline_peak_through_t0_v0.2',
        'generated': '2026-08-18',
        'status': 'pass2_high_risk_prior_career_audit_started_53_new_people_pending',
        'selection_cutoff': '2011-04-01',
        'supersedes': 'data/typeA/donga_2011_baseline_peak_through_t0_v0_1.json',
        't0_ref': base['t0_ref'],
        'audit_ref': 'research/donga_2011_prior_career_audit_v0_1.json',
        'method': {
            'repeat_38': 'Already checked against frozen 2010 lifetime baseline in v0.1.',
            'new_62': 'Dedicated pre-2011 career audit is being applied in risk-prioritized passes; T0 snapshot is preserved even when baseline is raised.',
            'this_pass': 'Nine high-risk new people audited; one prior higher peak found (Baek Seung-heon).'
        },
        'qa': {
            'total': 100,
            'unique_names': len({p['name'] for p in people}),
            'repeat_checked_n': 38,
            'new_person_total_n': 62,
            'new_person_prior_audited_n': 9,
            'new_person_prior_audit_pending_n': len(pending),
            'corrected_prior_peak_n': len(corrected),
            'corrected_prior_peak_names': corrected,
            'score_counts': {str(k): v for k, v in sorted(cnt.items())},
            'mean_baseline': sum(p['baseline_peak_through_t0'] for p in people) / 100,
            'pending_names': pending
        },
        'people': people
    }
    assert out['qa']['unique_names'] == 100
    assert out['qa']['mean_baseline'] == 2.62
    OUTJ.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    fields = [
        'name','category','repeat_2010_2011','t0_snapshot_scope_score',
        'baseline_peak_through_t0','baseline_peak_role','baseline_peak_year',
        'needs_new_person_prior_career_audit','prior_career_audit_status',
        'prior_career_audit_confidence','baseline_basis_v0_2'
    ]
    with OUTC.open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for p in people:
            w.writerow({k: p.get(k) for k in fields})

    print(json.dumps(out['qa'], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
