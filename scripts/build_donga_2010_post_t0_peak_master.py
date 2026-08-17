#!/usr/bin/env python3
import csv, glob, json
from collections import Counter
from pathlib import Path
from statistics import mean

ROOT=Path(__file__).resolve().parents[1]
TYPEA=ROOT/'data/typeA'
BASE=TYPEA/'donga_2010_baseline_peak_through_t0_v1_4.json'
PATCH=TYPEA/'donga_2010_post_t0_peak_audit_patch_v1_2.json'
MASTER_JSON=TYPEA/'donga_2010_post_t0_peak_master_v1_2.json'
MASTER_CSV=TYPEA/'donga_2010_post_t0_peak_master_v1_2.csv'
METRICS_JSON=TYPEA/'donga_2010_post_t0_peak_metrics_v1_2.json'
PATTERN=str(TYPEA/'donga_2010_post_t0_peak_*_v0_1.json')

def adv_class(delta, peak):
    if delta>0: return 'advanced'
    if delta==0 and peak>=3: return 'sustained_high'
    if delta==0: return 'no_clear_advancement'
    return 'lower_than_baseline'

def main():
    baseline=json.loads(BASE.read_text(encoding='utf-8'))
    b={p['name']:p for p in baseline['people']}
    merged={}; source_files=[]
    for fn in sorted(glob.glob(PATTERN)):
        d=json.load(open(fn,encoding='utf-8'))
        if not isinstance(d.get('people'),list): continue
        source_files.append(str(Path(fn).relative_to(ROOT)))
        for p in d['people']:
            n=p['name']
            if n in merged: raise AssertionError(f'duplicate post-T0 row: {n}')
            if n not in b: raise AssertionError(f'noncanonical name: {n}')
            merged[n]=dict(p)
    assert len(merged)==100

    patch=json.loads(PATCH.read_text(encoding='utf-8'))
    for pp in patch['patches']:
        n=pp['name']
        if n not in merged: raise AssertionError(f'patch noncanonical name: {n}')
        merged[n].update(pp)
    assert {p['name'] for p in patch['patches']}=={'김숙정','박성훈'}
    source_files.append(str(PATCH.relative_to(ROOT)))

    rows=[]
    for n,br in b.items():
        p=merged[n]; peak=p.get('post_t0_peak_score')
        row={
            'name':n,'category':br['category'],'sector_t0':br['sector'],
            't0_snapshot_scope_score':br['t0_snapshot_scope_score'],
            'baseline_peak_through_t0':br['baseline_peak_through_t0'],
            'baseline_peak_role':br['baseline_peak_role'],'baseline_peak_year':br['baseline_peak_year'],
            'post_t0_peak_role':p.get('post_t0_peak_role'),'post_t0_peak_score':peak,
            'post_t0_peak_year':p.get('post_t0_peak_year'),'sector_at_peak':p.get('sector_at_peak'),
            'evidence_confidence':p.get('evidence_confidence'),'coding_status':p.get('coding_status'),
            'exposure_truncated_by_death':bool(p.get('exposure_truncated_by_death',False)),
            'death_year':p.get('death_year'),'source_urls':p.get('source_urls',[]),'peak_reason':p.get('peak_reason')
        }
        if peak is None:
            row['advancement_delta']=None; row['advancement_class']='not_assessable'
        else:
            d=peak-br['baseline_peak_through_t0']; row['advancement_delta']=d; row['advancement_class']=adv_class(d,peak)
        rows.append(row)

    assessed=[r for r in rows if r['post_t0_peak_score'] is not None]
    unresolved=[r for r in rows if r['post_t0_peak_score'] is None]
    truncated=[r for r in assessed if r['exposure_truncated_by_death']]
    nontrunc=[r for r in assessed if not r['exposure_truncated_by_death']]
    score_counts=Counter(r['post_t0_peak_score'] for r in assessed)
    classes=Counter(r['advancement_class'] for r in rows)

    assert len(rows)==100 and len(assessed)==100 and not unresolved
    assert len(truncated)==3 and {r['name'] for r in truncated}=={'최은석','서동철','박원순'}
    assert score_counts==Counter({2:29,3:59,4:12}), score_counts
    assert classes==Counter({'sustained_high':44,'advanced':28,'no_clear_advancement':28}), classes

    major=sum(r['post_t0_peak_score']>=3 for r in assessed)
    apex=sum(r['post_t0_peak_score']==4 for r in assessed)
    adv=sum(r['advancement_class']=='advanced' for r in assessed)
    nm=sum(r['post_t0_peak_score']>=3 for r in nontrunc)
    na=sum(r['post_t0_peak_score']==4 for r in nontrunc)
    nd=sum(r['advancement_class']=='advanced' for r in nontrunc)
    assert (major,apex,adv)==(71,12,28)
    assert len(nontrunc)==97 and (nm,na,nd)==(68,12,26)

    bycat={}
    for cat in dict.fromkeys(r['category'] for r in rows):
        rr=[r for r in rows if r['category']==cat]
        bycat[cat]={
            'n':len(rr),'assessed':len(rr),'unresolved':0,
            'major_ge3_n':sum(r['post_t0_peak_score']>=3 for r in rr),
            'major_ge3_rate':sum(r['post_t0_peak_score']>=3 for r in rr)/len(rr),
            'apex_eq4_n':sum(r['post_t0_peak_score']==4 for r in rr),
            'apex_eq4_rate':sum(r['post_t0_peak_score']==4 for r in rr)/len(rr),
            'advanced_n':sum(r['advancement_class']=='advanced' for r in rr),
            'advanced_rate':sum(r['advancement_class']=='advanced' for r in rr)/len(rr),
            'sustained_high_n':sum(r['advancement_class']=='sustained_high' for r in rr),
            'no_clear_advancement_n':sum(r['advancement_class']=='no_clear_advancement' for r in rr),
            'mean_advancement_delta':mean(r['advancement_delta'] for r in rr),
            'truncated_by_death_n':sum(r['exposure_truncated_by_death'] for r in rr)
        }

    master={
        'schema_version':'donga_2010_post_t0_peak_master_v1.2','generated':'2026-08-18','status':'complete_100_of_100',
        'observation_end':'2026-08-18','selection_cutoff':'2010-05-10',
        'protocol_ref':'state/donga_2010_post_t0_peak_protocol_v1_0.md',
        'baseline_ref':'data/typeA/donga_2010_baseline_peak_through_t0_v1_4.json',
        'audit_patch_ref':'data/typeA/donga_2010_post_t0_peak_audit_patch_v1_2.json',
        'supersedes_runtime':'data/typeA/donga_2010_post_t0_peak_master_v1_1.json',
        'source_files':source_files,
        'qa':{'total':100,'assessed':100,'unresolved':0,'truncated_by_death':3,'post_t0_score_counts':{str(k):v for k,v in sorted(score_counts.items())},'advancement_classes':{k:classes.get(k,0) for k in ['advanced','sustained_high','no_clear_advancement','lower_than_baseline','not_assessable']},'unresolved_names':[],'truncated_names':[r['name'] for r in truncated]},
        'people':rows
    }
    MASTER_JSON.write_text(json.dumps(master,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    fields=['name','category','sector_t0','t0_snapshot_scope_score','baseline_peak_through_t0','baseline_peak_role','baseline_peak_year','post_t0_peak_role','post_t0_peak_score','post_t0_peak_year','sector_at_peak','advancement_delta','advancement_class','evidence_confidence','coding_status','exposure_truncated_by_death','death_year']
    with MASTER_CSV.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows({k:r.get(k) for k in fields} for r in rows)

    metrics={
        'schema_version':'donga_2010_post_t0_peak_metrics_v1.2','generated':'2026-08-18',
        'metric_scope':'lifetime_post_selection_peak_through_2026-08-18_with_preselection_peak_adjustment',
        'population':{'total':100,'assessed':100,'unresolved':0,'death_truncated_assessed':3,'assessed_nontruncated':97},
        'primary_full_cohort':{
            'denominator':100,'major_leadership_ge3_n':major,'major_leadership_precision':major/100,
            'apex_eq4_n':apex,'apex_precision':apex/100,'advanced_n':adv,'advanced_rate':adv/100,
            'mean_advancement_delta':mean(r['advancement_delta'] for r in assessed),
            'advancement_classes':{k:classes.get(k,0) for k in ['advanced','sustained_high','no_clear_advancement','lower_than_baseline','not_assessable']},
            'post_t0_score_counts':{str(k):v for k,v in sorted(score_counts.items())}
        },
        'sensitivity_excluding_death_truncated':{
            'denominator':97,'major_ge3_n':nm,'major_ge3_rate':nm/97,
            'apex_eq4_n':na,'apex_eq4_rate':na/97,'advanced_n':nd,'advanced_rate':nd/97,
            'mean_advancement_delta':mean(r['advancement_delta'] for r in nontrunc)
        },
        'by_category':bycat,
        'interpretation_guardrails':[
            'Primary precision uses all 100 roster members and is not equivalent to the 2020 target-year snapshot metric.',
            'Death-truncated rows remain in the primary cohort because a post-selection peak was observed before death; a sensitivity analysis excluding them is also reported.',
            'Advancement uses post-T0 peak minus baseline lifetime peak through selection, not post-T0 peak minus contemporaneous title alone.',
            'A major-leadership hit can be sustained_high rather than an editorially predicted rise; major precision and advancement rate answer different questions.',
            'The roster is alphabetical within editorial categories, so ranking accuracy is not estimable.'
        ]
    }
    METRICS_JSON.write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(master['qa'],ensure_ascii=False,indent=2))
    print(json.dumps(metrics,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
