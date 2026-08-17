#!/usr/bin/env python3
import json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SEED=ROOT/'analysis/donga_2011_post_t0_seed_v0_2.json'
BATCH_FILES=[
    ROOT/'research/donga_2011_post_t0_new_audit_batch1_v0_1.json',
    ROOT/'research/donga_2011_post_t0_new_audit_batch2_v0_1.json',
]
OUT=ROOT/'analysis/donga_2011_post_t0_partial_master_v0_2.json'

def adv_class(delta,peak):
    if delta is None or peak is None: return 'not_assessed'
    if delta>0: return 'advanced'
    if delta==0 and peak>=3: return 'sustained_high'
    if delta==0: return 'no_clear_advancement'
    return 'lower_than_baseline'

def main():
    seed=json.loads(SEED.read_text(encoding='utf-8'))
    audited={}; audit_source={}; batch_names={}
    for bf in BATCH_FILES:
        b=json.loads(bf.read_text(encoding='utf-8'))
        assert b['qa']['resolved_n']==b['qa']['batch_n']==len(b['people'])
        names=[]
        for p in b['people']:
            n=p['name']
            assert n not in audited, f'duplicate across new audit batches: {n}'
            audited[n]=p; audit_source[n]=str(bf.relative_to(ROOT)); names.append(n)
        batch_names[bf.stem]=sorted(names)
    assert len(audited)==20

    seed_by={p['name']:p for p in seed['people']}
    assert set(audited) <= set(seed_by)
    bad=[n for n in audited if seed_by[n]['repeat_2010_2011']]
    assert not bad, f'new audit batches contain repeat entrants: {bad}'

    rows=[]
    for s in seed['people']:
        n=s['name']; baseline=s['baseline_2011']
        if s['repeat_2010_2011']:
            peak=s['candidate_post2011_peak_score']
            assert peak is not None
            r={
              'name':n,'category':s['category'],'repeat_2010_2011':True,'baseline_2011':baseline,
              'post2011_peak_role':s['candidate_post2011_peak_role'],'post2011_peak_score':peak,
              'post2011_peak_year':s['candidate_post2011_peak_year'],'evidence_confidence':s.get('evidence_confidence'),
              'source_urls':s.get('source_urls',[]),'exposure_truncated_by_death':s.get('exposure_truncated_by_death',False),
              'death_year':s.get('death_year'),'coding_status':'assessed_repeat_seed',
              'audit_source':seed['cutoff_audit_ref'] if s['seed_status']=='repeat_cutoff_reaudit_resolved' else seed['repeat_source_ref']
            }
        elif n in audited:
            a=audited[n]; peak=a['post2011_peak_score']
            r={
              'name':n,'category':s['category'],'repeat_2010_2011':False,'baseline_2011':baseline,
              'post2011_peak_role':a['post2011_peak_role'],'post2011_peak_score':peak,
              'post2011_peak_year':a['post2011_peak_year'],'evidence_confidence':a['evidence_confidence'],
              'source_urls':a['source_urls'],
              'exposure_truncated_by_death':bool(a.get('exposure_truncated_by_death',False)),
              'death_year':a.get('death_year'),
              'coding_status':a['coding_status'],'audit_source':audit_source[n]
            }
        else:
            r={
              'name':n,'category':s['category'],'repeat_2010_2011':False,'baseline_2011':baseline,
              'post2011_peak_role':None,'post2011_peak_score':None,'post2011_peak_year':None,
              'evidence_confidence':None,'source_urls':[],'exposure_truncated_by_death':False,'death_year':None,
              'coding_status':'pending_new_entrant_audit','audit_source':None
            }
            peak=None
        delta=None if peak is None else peak-baseline
        r['advancement_delta']=delta
        r['advancement_class']=adv_class(delta,peak)
        rows.append(r)

    assessed=[r for r in rows if r['post2011_peak_score'] is not None]
    pending=[r for r in rows if r['post2011_peak_score'] is None]
    repeats=[r for r in rows if r['repeat_2010_2011']]
    new_assessed=[r for r in assessed if not r['repeat_2010_2011']]
    death_truncated=[r for r in assessed if r['exposure_truncated_by_death']]
    score_counts=Counter(str(r['post2011_peak_score']) for r in assessed)
    class_counts=Counter(r['advancement_class'] for r in assessed)

    assert len(rows)==100 and len(repeats)==38
    assert len(assessed)==58 and len(new_assessed)==20 and len(pending)==42
    assert all(r['post2011_peak_score'] is not None for r in repeats)
    assert any(r['name']=='김정주' and r['exposure_truncated_by_death'] and r['death_year']==2022 for r in rows)

    out={
      'schema_version':'donga_2011_post_t0_partial_master_v0.2','generated':'2026-08-18',
      'status':'partial_58_of_100_assessed','selection_cutoff':'2011-04-01',
      'baseline_ref':seed['baseline_ref'],'repeat_seed_ref':str(SEED.relative_to(ROOT)),
      'new_audit_refs':[str(x.relative_to(ROOT)) for x in BATCH_FILES],
      'qa':{
        'total':100,'assessed_n':58,'pending_n':42,'repeat_assessed_n':38,'new_assessed_n':20,
        'death_truncated_assessed_n':len(death_truncated),
        'score_counts_assessed':dict(score_counts),'advancement_class_counts_assessed':dict(class_counts),
        'pending_names':sorted(r['name'] for r in pending),
        'new_audit_batch_names':batch_names
      },
      'guardrails':[
        'Partial master only; do not report 2011 cohort-wide rates until pending_n reaches zero.',
        'All repeat-selected cases are post-cutoff resolved; remaining pending cases are new 2011 entrants only.',
        'Adverse events and death truncation are separate dimensions and do not retroactively lower a maximum prominence score.',
        'A score-4 sports apex requires an explicit apex title/achievement; top-league participation alone remains score 3.'
      ],
      'people':rows
    }
    OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out['qa'],ensure_ascii=False,indent=2))

if __name__=='__main__': main()
