#!/usr/bin/env python3
import json, re
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TYPEA=ROOT/'data/typeA'
BASE11=TYPEA/'donga_2011_baseline_peak_through_t0_v1_0.json'
POST10=TYPEA/'donga_2010_post_t0_peak_master_v1_2.json'
CUTOFF_AUDIT=ROOT/'research/donga_2011_post_t0_repeat_cutoff_audit_v0_1.json'
OUT=ROOT/'analysis/donga_2011_post_t0_seed_v0_2.json'

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
    audit=json.loads(CUTOFF_AUDIT.read_text(encoding='utf-8'))
    by10={p['name']:p for p in p10['people']}
    audited={p['name']:p for p in audit['people']}
    assert set(audited)=={'강덕수','박원순','유시민','이주호'}
    assert audit['qa']['resolved_n']==4 and audit['qa']['unresolved_n']==0

    rows=[]
    for p in b11['people']:
        n=p['name']; repeat=bool(p['repeat_2010_2011'])
        r={'name':n,'category':p['category'],'repeat_2010_2011':repeat,
           'baseline_2011':p['baseline_peak_through_t0'],'seed_status':None,
           'candidate_post2011_peak_score':None,'candidate_post2011_peak_role':None,
           'candidate_post2011_peak_year':None,'candidate_advancement_delta':None,
           'candidate_advancement_class':'not_assessed','evidence_confidence':None,
           'source_urls':[],'exposure_truncated_by_death':False,'death_year':None,'reason':None}
        if not repeat:
            r['seed_status']='new_2011_manual_audit_required'
            r['reason']='No 2010 post-T0 row exists for this new 2011 entrant.'
        elif n in audited:
            a=audited[n]
            peak=a['post2011_peak_score']; delta=peak-p['baseline_peak_through_t0']
            r.update({
                'candidate_post2011_peak_score':peak,
                'candidate_post2011_peak_role':a['post2011_peak_role'],
                'candidate_post2011_peak_year':a['post2011_peak_year'],
                'candidate_advancement_delta':delta,
                'candidate_advancement_class':adv_class(delta,peak),
                'evidence_confidence':a['evidence_confidence'],
                'source_urls':a['source_urls'],
                'exposure_truncated_by_death':bool(a.get('exposure_truncated_by_death',False)),
                'death_year':a.get('death_year'),
                'seed_status':'repeat_cutoff_reaudit_resolved',
                'reason':a['reason']
            })
        else:
            old=by10[n]; y=year_of(old.get('post_t0_peak_year'))
            if y is None or y<2012:
                raise AssertionError(f'unpatched repeat cutoff case remains: {n} / {old.get("post_t0_peak_year")}')
            peak=old['post_t0_peak_score']; delta=peak-p['baseline_peak_through_t0']
            r.update({
                'candidate_post2011_peak_score':peak,
                'candidate_post2011_peak_role':old.get('post_t0_peak_role'),
                'candidate_post2011_peak_year':old.get('post_t0_peak_year'),
                'candidate_advancement_delta':delta,
                'candidate_advancement_class':adv_class(delta,peak),
                'evidence_confidence':old.get('evidence_confidence'),
                'source_urls':old.get('source_urls',[]),
                'exposure_truncated_by_death':bool(old.get('exposure_truncated_by_death',False)),
                'death_year':old.get('death_year'),
                'seed_status':'repeat_safe_post2011_inheritance_candidate',
                'reason':'Locked 2010 post-T0 maximum is explicitly observed in 2012 or later.'
            })
        rows.append(r)

    cnt=Counter(r['seed_status'] for r in rows)
    repeats=[r for r in rows if r['repeat_2010_2011']]
    safe=[r for r in rows if r['seed_status']=='repeat_safe_post2011_inheritance_candidate']
    patched=[r for r in rows if r['seed_status']=='repeat_cutoff_reaudit_resolved']
    pending_repeat=[r for r in repeats if r['candidate_post2011_peak_score'] is None]
    new=[r for r in rows if not r['repeat_2010_2011']]

    assert len(rows)==100 and len({r['name'] for r in rows})==100
    assert len(repeats)==38 and len(new)==62
    assert len(safe)==34 and len(patched)==4 and not pending_repeat
    assert cnt==Counter({'new_2011_manual_audit_required':62,
                         'repeat_safe_post2011_inheritance_candidate':34,
                         'repeat_cutoff_reaudit_resolved':4}), cnt

    out={'schema_version':'donga_2011_post_t0_seed_v0.2','generated':'2026-08-18',
         'status':'repeat_38_resolved_new_62_pending','selection_cutoff':'2011-04-01',
         'baseline_ref':str(BASE11.relative_to(ROOT)),'repeat_source_ref':str(POST10.relative_to(ROOT)),
         'cutoff_audit_ref':str(CUTOFF_AUDIT.relative_to(ROOT)),
         'qa':{'total':100,'repeat_n':38,'new_2011_n':62,'seed_status_counts':dict(cnt),
               'safe_inheritance_candidate_n':34,'cutoff_reaudit_resolved_n':4,
               'repeat_resolved_n':38,'repeat_reaudit_pending_n':0,
               'manual_new_outcome_audit_queue_n':62,
               'safe_inheritance_candidate_names':sorted(r['name'] for r in safe),
               'cutoff_reaudit_resolved_names':sorted(r['name'] for r in patched)},
         'guardrails':['Seed/triage dataset; final 2011 outcomes require dedicated audit of all 62 new entrants.',
                       'The final observation window starts at 2011-04-01 to prevent look-ahead/reverse-causation bias.',
                       'The four ambiguous repeat rows are accepted only after direct post-cutoff evidence audit.',
                       'Final 2011 post-T0 peak is the maximum observed from 2011-04-01 through 2026-08-18.'],
         'people':rows}
    OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out['qa'],ensure_ascii=False,indent=2))

if __name__=='__main__': main()
