#!/usr/bin/env python3
import glob, json
from collections import Counter
from pathlib import Path
from statistics import mean

ROOT=Path(__file__).resolve().parents[1]
TYPEA=ROOT/'data/typeA'
BASE=TYPEA/'donga_2010_baseline_peak_through_t0_v1_4.json'
PATCH=TYPEA/'donga_2010_post_t0_peak_audit_patch_v1_2.json'
OUT=TYPEA/'donga_2010_post_t0_peak_analysis_working.json'
PATTERN=str(TYPEA/'donga_2010_post_t0_peak_*_v0_1.json')

def cls(delta, peak):
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
            if n not in b: raise AssertionError(f'noncanonical post-T0 row: {n}')
            merged[n]=dict(p,category=b[n]['category'])
    patch=json.loads(PATCH.read_text(encoding='utf-8'))
    for p in patch['patches']:
        n=p['name']; merged[n].update(p); merged[n]['category']=b[n]['category']
    source_files.append(str(PATCH.relative_to(ROOT)))

    rows=[]
    for n,p in merged.items():
        br=b[n]; peak=p.get('post_t0_peak_score')
        if peak is None:
            rows.append({'name':n,'category':br['category'],'baseline_peak_through_t0':br['baseline_peak_through_t0'],'post_t0_peak_score':None,'advancement_delta':None,'advancement_class':'not_assessable','coding_status':p.get('coding_status'),'exposure_truncated_by_death':p.get('exposure_truncated_by_death',False)}); continue
        delta=peak-br['baseline_peak_through_t0']
        rows.append({'name':n,'category':br['category'],'baseline_peak_through_t0':br['baseline_peak_through_t0'],'post_t0_peak_score':peak,'advancement_delta':delta,'advancement_class':cls(delta,peak),'post_t0_peak_role':p.get('post_t0_peak_role'),'post_t0_peak_year':p.get('post_t0_peak_year'),'coding_status':p.get('coding_status'),'exposure_truncated_by_death':p.get('exposure_truncated_by_death',False)})
    assessed=[r for r in rows if r['post_t0_peak_score'] is not None]; classes=Counter(r['advancement_class'] for r in rows)
    bycat={}
    for cat in dict.fromkeys(r['category'] for r in rows):
        a=[r for r in rows if r['category']==cat and r['post_t0_peak_score'] is not None]
        bycat[cat]={'rows':len(a),'assessed':len(a),'unresolved':0,'major_ge3_n':sum(r['post_t0_peak_score']>=3 for r in a),'major_ge3_rate':sum(r['post_t0_peak_score']>=3 for r in a)/len(a) if a else None,'apex_eq4_n':sum(r['post_t0_peak_score']==4 for r in a),'advanced_n':sum(r['advancement_class']=='advanced' for r in a),'sustained_high_n':sum(r['advancement_class']=='sustained_high' for r in a),'no_clear_advancement_n':sum(r['advancement_class']=='no_clear_advancement' for r in a),'lower_than_baseline_n':sum(r['advancement_class']=='lower_than_baseline' for r in a),'mean_advancement_delta':mean(r['advancement_delta'] for r in a) if a else None,'truncated_by_death_n':sum(r['exposure_truncated_by_death'] for r in a)}
    out={'schema_version':'donga_2010_post_t0_peak_analysis_working_v0.6','generated':'2026-08-18','status':'complete_100_rows_pre_freeze','baseline_ref':'data/typeA/donga_2010_baseline_peak_through_t0_v1_4.json','audit_patch_ref':'data/typeA/donga_2010_post_t0_peak_audit_patch_v1_2.json','source_files':source_files,'coverage':{'rows':len(rows),'assessed':len(assessed),'unresolved':len(rows)-len(assessed),'remaining_uncreated':100-len(rows)},'assessed_only':{'major_leadership_precision_ge3':sum(r['post_t0_peak_score']>=3 for r in assessed)/len(assessed),'major_ge3_n':sum(r['post_t0_peak_score']>=3 for r in assessed),'apex_precision_eq4':sum(r['post_t0_peak_score']==4 for r in assessed)/len(assessed),'apex_eq4_n':sum(r['post_t0_peak_score']==4 for r in assessed),'mean_advancement_delta':mean(r['advancement_delta'] for r in assessed),'advancement_classes':{k:classes.get(k,0) for k in ['advanced','sustained_high','no_clear_advancement','lower_than_baseline','not_assessable']}},'by_category':bycat,'rows':rows}
    assert len(rows)==100 and len(assessed)==100
    assert out['assessed_only']['major_ge3_n']==71 and out['assessed_only']['apex_eq4_n']==12
    OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
