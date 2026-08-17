#!/usr/bin/env python3
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SEED=ROOT/'analysis/donga_2011_post_t0_seed_v0_2.json'
T0_ROLES=ROOT/'data/typeA/donga_2011_t0_roles_v0_1.json'
BATCH_FILES=[ROOT/f'research/donga_2011_post_t0_new_audit_batch{i}_v0_1.json' for i in range(1,7)]
IDENTITY_ANCHOR_REQUIRED={p.name for p in BATCH_FILES[2:]}
MASTER_OUT=ROOT/'analysis/donga_2011_post_t0_master_v1_0.json'
METRICS_OUT=ROOT/'analysis/donga_2011_post_t0_metrics_v1_0.json'

def adv_class(delta,peak,assessable=True):
    if not assessable or peak is None: return 'not_assessable'
    if delta>0: return 'advanced'
    if delta==0 and peak>=3: return 'sustained_high'
    if delta==0: return 'no_clear_advancement'
    return 'lower_than_baseline'

def validate_identity(n,p,t0_by,batch_name):
    anchor=p.get('t0_identity_anchor')
    if batch_name in IDENTITY_ANCHOR_REQUIRED:
        assert anchor is not None, f'{batch_name} missing T0 identity anchor: {n}'
    if anchor is None: return False
    expected=t0_by[n]
    assert anchor['category']==expected['category'], f'category identity mismatch for {n}'
    assert anchor['t0_role_official_2011']==expected['t0_role_official_2011'], f'T0 role identity mismatch for {n}'
    assert expected['repeat_2010_2011'] is False, f'identity anchor points to repeat entrant: {n}'
    return True

def summarize(rows, denominator_mode='full'):
    scored=[r for r in rows if r['post2011_peak_score'] is not None]
    if denominator_mode=='full':
        denom=len(rows)
    elif denominator_mode=='assessable':
        denom=len(scored)
    else:
        raise ValueError(denominator_mode)
    major=sum((r['post2011_peak_score'] or -1)>=3 for r in rows)
    apex=sum(r['post2011_peak_score']==4 for r in rows)
    advanced=sum(r['advancement_class']=='advanced' for r in rows)
    return {
      'denominator':denom,
      'scored_n':len(scored),
      'not_assessable_n':len(rows)-len(scored),
      'major_ge3_n':major,
      'major_ge3_rate':major/denom if denom else None,
      'apex_eq4_n':apex,
      'apex_eq4_rate':apex/denom if denom else None,
      'advanced_n':advanced,
      'advanced_rate':advanced/denom if denom else None,
      'advancement_classes':dict(Counter(r['advancement_class'] for r in rows)),
      'post_t0_score_counts_scored':dict(Counter(str(r['post2011_peak_score']) for r in scored)),
    }

def main():
    seed=json.loads(SEED.read_text(encoding='utf-8'))
    t0=json.loads(T0_ROLES.read_text(encoding='utf-8'))
    t0_by={p['name']:p for p in t0['people']}; assert len(t0_by)==100

    audited={}; audit_source={}; batch_names={}; anchors=[]
    for bf in BATCH_FILES:
        b=json.loads(bf.read_text(encoding='utf-8'))
        people=b['people']
        expected_n=b['qa'].get('resolved_n',b['qa'].get('adjudicated_n'))
        assert expected_n==len(people)
        names=[]
        for p in people:
            n=p['name']; assert n not in audited, f'duplicate new audit row: {n}'; assert n in t0_by
            if validate_identity(n,p,t0_by,bf.name): anchors.append(n)
            audited[n]=p; audit_source[n]=str(bf.relative_to(ROOT)); names.append(n)
        batch_names[bf.stem]=sorted(names)
    assert len(audited)==62, len(audited)
    assert len(anchors)==42, len(anchors)

    seed_by={p['name']:p for p in seed['people']}; assert set(audited)<=set(seed_by)
    assert not [n for n in audited if seed_by[n]['repeat_2010_2011']]

    rows=[]
    for s in seed['people']:
        n=s['name']; baseline=s['baseline_2011']
        if s['repeat_2010_2011']:
            peak=s['candidate_post2011_peak_score']; assert peak is not None
            assessable=True
            r={'name':n,'category':s['category'],'repeat_2010_2011':True,'baseline_2011':baseline,
               'post2011_peak_role':s['candidate_post2011_peak_role'],'post2011_peak_score':peak,
               'post2011_peak_year':s['candidate_post2011_peak_year'],'evidence_confidence':s.get('evidence_confidence'),
               'source_urls':s.get('source_urls',[]),'exposure_truncated_by_death':s.get('exposure_truncated_by_death',False),
               'death_year':s.get('death_year'),'coding_status':'assessed_repeat_seed','advancement_assessable':True,
               'audit_source':seed['cutoff_audit_ref'] if s['seed_status']=='repeat_cutoff_reaudit_resolved' else seed['repeat_source_ref']}
        else:
            a=audited[n]; peak=a.get('post2011_peak_score'); assessable=bool(a.get('advancement_assessable',peak is not None))
            if assessable: assert peak is not None
            else: assert peak is None
            r={'name':n,'category':s['category'],'repeat_2010_2011':False,'baseline_2011':baseline,
               'post2011_peak_role':a.get('post2011_peak_role'),'post2011_peak_score':peak,
               'post2011_peak_year':a.get('post2011_peak_year'),'evidence_confidence':a.get('evidence_confidence'),
               'source_urls':a.get('source_urls',[]),'exposure_truncated_by_death':bool(a.get('exposure_truncated_by_death',False)),
               'death_year':a.get('death_year'),'coding_status':a['coding_status'],'advancement_assessable':assessable,
               'audit_source':audit_source[n]}
            if 't0_identity_anchor' in a: r['t0_identity_anchor']=a['t0_identity_anchor']
        delta=(peak-baseline) if assessable else None
        r['advancement_delta']=delta
        r['advancement_class']=adv_class(delta,peak,assessable)
        rows.append(r)

    assert len(rows)==100 and len({r['name'] for r in rows})==100
    scored=[r for r in rows if r['post2011_peak_score'] is not None]
    not_assessable=[r for r in rows if r['post2011_peak_score'] is None]
    repeats=[r for r in rows if r['repeat_2010_2011']]
    new=[r for r in rows if not r['repeat_2010_2011']]
    assert len(scored)==99 and len(not_assessable)==1 and not_assessable[0]['name']=='신준호'
    assert len(repeats)==38 and len(new)==62
    assert all(r['post2011_peak_score'] is not None for r in repeats)
    assert sum(r['exposure_truncated_by_death'] for r in rows)==2

    qa={
      'total':100,'adjudicated_n':100,'scored_n':99,'not_assessable_n':1,'pending_n':0,
      'repeat_n':38,'new_entrant_n':62,'repeat_scored_n':38,'new_scored_n':61,
      'not_assessable_names':[r['name'] for r in not_assessable],
      'identity_anchor_validated_n':len(anchors),'identity_anchor_validated_names':sorted(anchors),
      'death_truncated_n':sum(r['exposure_truncated_by_death'] for r in rows),
      'death_truncated_names':sorted(r['name'] for r in rows if r['exposure_truncated_by_death']),
      'score_counts_scored':dict(Counter(str(r['post2011_peak_score']) for r in scored)),
      'advancement_class_counts':dict(Counter(r['advancement_class'] for r in rows)),
      'new_audit_batch_names':batch_names,
    }
    master={
      'schema_version':'donga_2011_post_t0_master_v1.0','generated':'2026-08-18','status':'final_adjudicated_100_pending_0',
      'selection_cutoff':'2011-04-01','observation_end':'2026-08-18','baseline_ref':seed['baseline_ref'],
      'repeat_seed_ref':str(SEED.relative_to(ROOT)),'t0_identity_ref':str(T0_ROLES.relative_to(ROOT)),
      'new_audit_refs':[str(x.relative_to(ROOT)) for x in BATCH_FILES],
      'qa':qa,
      'guardrails':[
        'All 100 roster rows have been adjudicated; one row is explicitly not assessable rather than assigned a forced low score.',
        'Primary full-cohort rates use denominator 100 and conservatively count the not-assessable row as a non-hit.',
        'Assessable sensitivity rates use denominator 99.',
        'Advancement is post-selection peak minus pre-selection lifetime peak through 2011-04-01.',
        'Adverse events and death truncation do not retroactively reduce an observed prominence peak.',
        'From batch 3 onward, new-entrant rows require frozen-T0 category and official-role identity anchors.'
      ],
      'people':rows,
    }
    MASTER_OUT.write_text(json.dumps(master,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

    by_category={}
    cats=defaultdict(list)
    for r in rows: cats[r['category']].append(r)
    for c,rs in sorted(cats.items()):
        by_category[c]={'full':summarize(rs,'full'),'assessable':summarize(rs,'assessable')}
    metrics={
      'schema_version':'donga_2011_post_t0_metrics_v1.0','generated':'2026-08-18',
      'metric_scope':'post_selection_peak_2011-04-01_through_2026-08-18_with_preselection_peak_adjustment',
      'population':{'total':100,'scored':99,'not_assessable':1,'not_assessable_names':['신준호']},
      'primary_full_cohort_conservative':summarize(rows,'full'),
      'sensitivity_assessable_only':summarize(rows,'assessable'),
      'repeat_2010_2011':{'full':summarize(repeats,'full'),'assessable':summarize(repeats,'assessable')},
      'new_2011_entrants':{'full':summarize(new,'full'),'assessable':summarize(new,'assessable')},
      'by_category':by_category,
      'interpretation_guardrails':[
        'Major-leadership precision and baseline-adjusted advancement answer different questions.',
        'The one not-assessable row is retained in the primary denominator as a conservative non-hit and excluded in assessable-only sensitivity.',
        'Repeat-selected status is not a randomized exposure and should not be interpreted causally.',
        'The list is alphabetical within editorial categories, so ranking accuracy is not estimable for this broad-screening cohort.'
      ]
    }
    METRICS_OUT.write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'qa':qa,'primary':metrics['primary_full_cohort_conservative'],'sensitivity':metrics['sensitivity_assessable_only']},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
