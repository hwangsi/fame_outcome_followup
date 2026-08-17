#!/usr/bin/env python3
import csv, json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TYPEA = ROOT / 'data/typeA'
MASTER10 = TYPEA / 'donga_2010_post_t0_peak_master_v1_2.json'
BASE11 = TYPEA / 'donga_2011_baseline_peak_through_t0_v1_0.json'
OUTJ = TYPEA / 'donga_2011_post_t0_repeat_seed_v0_1.json'
OUTC = TYPEA / 'donga_2011_post_t0_repeat_seed_v0_1.csv'
CUTOFF = '2011-04-01'


def main():
    m10 = json.loads(MASTER10.read_text(encoding='utf-8'))
    b11 = json.loads(BASE11.read_text(encoding='utf-8'))
    old = {p['name']: p for p in m10['people']}
    repeat = [p for p in b11['people'] if p['repeat_2010_2011']]
    assert len(repeat) == 38

    rows = []
    for b in repeat:
        n = b['name']
        assert n in old, n
        o = old[n]
        year = o.get('post_t0_peak_year')
        # A 2010-coded peak dated 2012+ is unquestionably after the 2011-04-01 cutoff.
        # A peak in 2011 is date-ambiguous unless exact event timing is separately checked.
        # A peak <=2010 may have persisted after cutoff, so it is not treated as failure; it requires re-audit.
        if isinstance(year, int) and year >= 2012:
            status = 'safe_reuse_candidate_after_2011_cutoff'
            reason = '2010 master peak year is 2012 or later; event necessarily occurs after 2011-04-01.'
        else:
            status = 'requires_2011_cutoff_reaudit'
            reason = '2010 master peak is dated 2011/earlier or lacks a simple integer year; exact post-2011 exposure/persistence must be re-audited.'
        rows.append({
            'name': n,
            'category_2011': b['category'],
            'baseline_2011': b['baseline_peak_through_t0'],
            't0_2011': b['t0_snapshot_scope_score'],
            'old_2010_post_t0_peak_score': o.get('post_t0_peak_score'),
            'old_2010_post_t0_peak_role': o.get('post_t0_peak_role'),
            'old_2010_post_t0_peak_year': year,
            'old_2010_sector_at_peak': o.get('sector_at_peak'),
            'old_2010_evidence_confidence': o.get('evidence_confidence'),
            'old_2010_source_urls': o.get('source_urls', []),
            'reuse_status': status,
            'reuse_reason': reason,
            'final_2011_post_t0_peak_score': None,
            'final_2011_post_t0_peak_role': None,
            'final_2011_post_t0_peak_year': None,
            'coding_status_2011': 'seed_not_final'
        })

    counts = Counter(r['reuse_status'] for r in rows)
    assert len(rows) == 38 and len({r['name'] for r in rows}) == 38
    out = {
        'schema_version': 'donga_2011_post_t0_repeat_seed_v0.1',
        'generated': '2026-08-18',
        'status': 'repeat_38_triage_seed_not_final_outcomes',
        'selection_cutoff_2011': CUTOFF,
        'source_2010_master': 'data/typeA/donga_2010_post_t0_peak_master_v1_2.json',
        'source_2011_baseline': 'data/typeA/donga_2011_baseline_peak_through_t0_v1_0.json',
        'method': {
            'safe_reuse_candidate': '2010 lifetime peak has integer year >=2012; still subject to evidence carry-forward QA but no cutoff ambiguity.',
            'cutoff_reaudit': '2010 peak year <=2011 or non-integer/missing; role may precede cutoff, persist across cutoff, or have exact-date ambiguity.',
            'guardrail': 'No repeat row is automatically coded as a 2011 failure merely because its 2010 peak occurred earlier.'
        },
        'qa': {
            'repeat_total': len(rows),
            'status_counts': dict(counts),
            'safe_reuse_candidate_n': counts['safe_reuse_candidate_after_2011_cutoff'],
            'requires_cutoff_reaudit_n': counts['requires_2011_cutoff_reaudit']
        },
        'people': rows
    }
    OUTJ.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    fields = [
        'name','category_2011','baseline_2011','t0_2011',
        'old_2010_post_t0_peak_score','old_2010_post_t0_peak_role','old_2010_post_t0_peak_year',
        'reuse_status','coding_status_2011'
    ]
    with OUTC.open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k:r.get(k) for k in fields})

    print(json.dumps(out['qa'], ensure_ascii=False, indent=2))
    print('reaudit_names=', [r['name'] for r in rows if r['reuse_status']=='requires_2011_cutoff_reaudit'])


if __name__ == '__main__':
    main()
