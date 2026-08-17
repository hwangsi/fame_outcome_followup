#!/usr/bin/env python3
import json, re
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TYPEA=ROOT/'data/typeA'
BASE11=TYPEA/'donga_2011_baseline_peak_through_t0_v1_0.json'
POST10=TYPEA/'donga_2010_post_t0_peak_master_v1_2.json'
OUT=ROOT/'analysis/donga_2011_post_t0_seed_v0_1.json'

def year_of(v):
    if v is None: return None
    if isinstance(v,int): return v
    m=re.search(r'(19|20)\d{2}',str(v))
    return int(m.group(0)) if m else None

def adv_class(delta,peak):
    if delta>0: return 'advanced'
    if delta==0 and peak>=3: return 'sustained_high'
    if delta==0: return 'no_clear_advancement'
    return 'lower_than_baseline'

def main():
    b11=json.loads(BASE11.read_text(encoding='utf-8'))
    p10=json.loads(POST10.read_text(encoding='utf-8'))
    by10={p['name']:p for p in p10['people']}
    rows=[]
    for p in b11['people']:
        n=p['name']; repeat=bool(p['repeat_2010_2011'])
        r={'name':n,'category':p['category'],'repeat_2010_2011':repeat,
           'baseline_2011':p['baseline_peak_through_t0'],'seed_status':None,
           'candidate_post2011_peak_score':None,'candidate_post2011_peak_role':None,
           'candidate_post2011_peak_year':None,'candidate_advancement_delta':None,
           'candidate_advancement_class':'not_assessed','reason':None}
        if not repeat:
            r['seed_status']='new_2011_manual_audit_required'
            r['reason']='No 2010 post-T0 row exists for this new 2011 entrant.'
        else:
            old=by10[n]; y=year_of(old.get('post_t0_peak_year'))
            r['candidate_post2011_peak_score']=old.get('post_t0_peak_score')
            r['candidate_post2011_peak_role']=old.get('post_t0_peak_role')
            r['candidate_post2011_peak_year']=old.get('post_t0_peak_year')
            if y is not None and y>=2012:
                peak=old['post_t0_peak_score']; delta=peak-p['baseline_peak_through_t0']
                r['candidate_advancement_delta']=delta
                r['candidate_advancement_class']=adv_class(delta,peak)
                r['seed_status']='repeat_safe_post2011_inheritance_candidate'
                r['reason']='Locked 2010 post-T0 maximum is explicitly observed in 2012 or later.'
            elif y==2011:
                r['seed_status']='repeat_2011_date_ambiguous_reaudit_required'
                r['reason']='Year-only 2011 evidence must be resolved against the 2011-04-01 cutoff.'
            else:
                r['seed_status']='repeat_pre2011_or_undated_reaudit_required'
                r['reason']='Pre-2011 or undated representative peak cannot be carried across the 2011 cutoff.'
        rows.append(r)
    cnt=Counter(r['seed_status'] for r in rows)
    safe=[r for r in rows if r['seed_status']=='repeat_safe_post2011_inheritance_candidate']
    repeats=[r for r in rows if r['repeat_2010_2011']]
    assert len(rows)==100 and len(repeats)==38 and cnt['new_2011_manual_audit_required']==62
    out={'schema_version':'donga_2011_post_t0_seed_v0.1','generated':'2026-08-18',
         'status':'triage_seed_not_final_outcomes','selection_cutoff':'2011-04-01',
         'baseline_ref':str(BASE11.relative_to(ROOT)),'repeat_source_ref':str(POST10.relative_to(ROOT)),
         'qa':{'total':100,'repeat_n':38,'new_2011_n':62,'seed_status_counts':dict(cnt),
               'safe_inheritance_candidate_n':len(safe),
               'manual_reaudit_queue_n':100-len(safe),
               'safe_inheritance_candidate_names':sorted(r['name'] for r in safe),
               'repeat_reaudit_names':sorted(r['name'] for r in repeats if r not in safe)},
         'guardrails':['Triage seed only; not final 2011 outcomes.',
                       'The final observation window starts at 2011-04-01 to prevent look-ahead/reverse-causation bias.',
                       '2011 year-only or pre-2011 peak evidence requires post-cutoff re-audit.',
                       'Final 2011 post-T0 peak is the maximum observed from 2011-04-01 through 2026-08-18.'],
         'people':rows}
    OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out['qa'],ensure_ascii=False,indent=2))

if __name__=='__main__': main()
