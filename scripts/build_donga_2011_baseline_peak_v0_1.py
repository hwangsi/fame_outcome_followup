#!/usr/bin/env python3
import csv,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];TYPEA=ROOT/'data/typeA'
T0=TYPEA/'donga_2011_t0_snapshot_scope_v0_3.json'
BASE10=TYPEA/'donga_2010_baseline_peak_through_t0_v1_4.json'
OUTJ=TYPEA/'donga_2011_baseline_peak_through_t0_v0_1.json';OUTC=TYPEA/'donga_2011_baseline_peak_through_t0_v0_1.csv'

def main():
 t0=json.loads(T0.read_text(encoding='utf-8'));b10=json.loads(BASE10.read_text(encoding='utf-8'))
 old={p['name']:p for p in b10['people']};people=[];repeat_checked=0;repeat_carried_higher=[]
 for p in t0['people']:
  p=dict(p);n=p['name'];t=p['t0_snapshot_scope_score'];baseline=t;basis='2011_audited_t0_no_prior_peak_above_t0_yet_identified';prior=None
  if p['repeat_2010_2011']:
   assert n in old,n;repeat_checked+=1;prior=old[n]['baseline_peak_through_t0']
   if prior>baseline:
    baseline=prior;basis='carried_forward_higher_frozen_2010_lifetime_peak';repeat_carried_higher.append(n)
   else:
    basis='2011_t0_at_or_above_frozen_2010_lifetime_peak'
  p['baseline_peak_through_t0']=baseline
  p['baseline_peak_role']=p['t0_role'] if baseline==t else old[n]['baseline_peak_role']
  p['baseline_peak_year']=2011 if baseline==t else old[n]['baseline_peak_year']
  p['baseline_basis_v0_1']=basis
  p['prior_2010_frozen_baseline']=prior
  p['needs_new_person_prior_career_audit']=not p['repeat_2010_2011']
  people.append(p)
 assert repeat_checked==38
 cnt=Counter(p['baseline_peak_through_t0'] for p in people)
 assert cnt==Counter({2:44,3:51,4:5}),cnt
 assert len(repeat_carried_higher)==0,repeat_carried_higher
 out={'schema_version':'donga_2011_baseline_peak_through_t0_v0.1','generated':'2026-08-18','status':'pass1_repeat_history_checked_new62_prior_career_audit_pending','selection_cutoff':'2011-04-01','t0_ref':'data/typeA/donga_2011_t0_snapshot_scope_v0_3.json','prior_repeat_baseline_ref':'data/typeA/donga_2010_baseline_peak_through_t0_v1_4.json','method':{'repeat_38':'baseline is max(audited 2011 T0, frozen 2010 lifetime peak); this prevents losing pre-2010 achievements','new_62':'audited 2011 T0 is provisional baseline until a dedicated prior-career audit checks for a higher pre-2011 peak'},'qa':{'total':100,'unique_names':100,'repeat_checked_n':repeat_checked,'new_person_prior_audit_pending_n':62,'repeat_carried_higher_n':len(repeat_carried_higher),'repeat_carried_higher_names':repeat_carried_higher,'score_counts':{str(k):v for k,v in sorted(cnt.items())},'mean_baseline':sum(p['baseline_peak_through_t0'] for p in people)/100},'people':people}
 OUTJ.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 fields=['name','category','repeat_2010_2011','t0_snapshot_scope_score','baseline_peak_through_t0','baseline_peak_role','baseline_peak_year','prior_2010_frozen_baseline','needs_new_person_prior_career_audit']
 with OUTC.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:p.get(k) for k in fields} for p in people)
 print(json.dumps(out['qa'],ensure_ascii=False,indent=2))
if __name__=='__main__':main()
