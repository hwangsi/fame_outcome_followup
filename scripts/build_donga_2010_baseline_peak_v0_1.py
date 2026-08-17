#!/usr/bin/env python3
import csv,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; TYPEA=ROOT/'data/typeA'
T0=TYPEA/'donga_2010_t0_snapshot_scope_v0_4.json'
OUTJ=TYPEA/'donga_2010_baseline_peak_through_t0_v0_1.json'; OUTC=TYPEA/'donga_2010_baseline_peak_through_t0_v0_1.csv'

PRIOR_PEAK={
'이소연':{
 'baseline_peak_score':3,
 'baseline_peak_role':'한국 최초 우주인·소유즈 TMA-12/국제우주정거장 우주실험전문가',
 'baseline_peak_year':2008,
 'reason':'KARI officially selected Lee as Korea’s first astronaut; she launched aboard Soyuz TMA-12 on 2008-04-08. This prior national-historic aerospace role exceeds her May-2010 snapshot as a senior researcher.',
 'source_urls':['https://www.kari.re.kr/kor/article/ATCL87374b48c/9969','https://www.kari.re.kr/kor/article/ATCL87374b48c/9976']
},
'유시민':{
 'baseline_peak_score':3,'baseline_peak_role':'보건복지부 장관','baseline_peak_year':2006,
 'reason':'The original 2010 capture itself identifies him as former Minister of Health and Welfare. The score equals, rather than exceeds, the corrected T0 governor-candidate scope.',
 'source_urls':[]
},
'안철수':{
 'baseline_peak_score':3,'baseline_peak_role':'안철수연구소 창업자·대표이사/이사회 의장','baseline_peak_year':2005,
 'reason':'AhnLab official founder history documents founder/CEO through 2005 and board chair from 2005; this peak equals the corrected 2010 multi-role scope.',
 'source_urls':['https://company.ahnlab.com/kr/company/founder.do']
},
'홍명보':{
 'baseline_peak_score':3,'baseline_peak_role':'대한민국 축구 국가대표 주장·2002 월드컵 핵심 선수','baseline_peak_year':2002,
 'reason':'Prior elite international playing career is retained as a same-stratum peak; it does not exceed his score-3 2010 Olympic-team head-coach snapshot.',
 'source_urls':[]
}
}

def main():
 d=json.loads(T0.read_text(encoding='utf-8')); people=[]
 for p in d['people']:
  p=dict(p); n=p['name']; t0=p['t0_snapshot_scope_score']
  if n in PRIOR_PEAK:
   e=PRIOR_PEAK[n]; peak=e['baseline_peak_score']; assert peak>=t0,(n,peak,t0)
   role=e['baseline_peak_role']; year=e['baseline_peak_year']; basis='explicit_prior_peak_audit'
   evidence=e
  else:
   peak=t0; role=p['t0_role']; year=2010; basis='t0_snapshot_is_highest_identified_through_selection'; evidence=None
  people.append({
   'name':n,'category':p['category'],'sector':p['sector'],'age':p.get('age'),'sex':p.get('sex'),
   't0_snapshot_scope_score':t0,'baseline_peak_through_t0':peak,'baseline_peak_role':role,'baseline_peak_year':year,
   'baseline_minus_t0':peak-t0,'baseline_basis':basis,'baseline_exception_evidence':evidence
  })
 counts=Counter(x['baseline_peak_through_t0'] for x in people); assert counts==Counter({2:52,3:44,4:3,1:1}),counts
 assert sum(x['baseline_minus_t0']>0 for x in people)==1
 out={'schema_version':'donga_2010_baseline_peak_through_t0_v0.1','generated':'2026-08-18','t0_ref':'data/typeA/donga_2010_t0_snapshot_scope_v0_4.json','protocol_ref':'state/donga_2010_baseline_peak_protocol_v1_0.md','status':'baseline_peak_pass1_complete_ready_for_freeze','definition':'highest verified scope reached on or before the May 2010 selection; defaults to audited T0 snapshot unless a higher prior episode is directly identified','qa':{'total':100,'unique_names':100,'score_counts':{str(k):v for k,v in sorted(counts.items())},'mean_baseline_peak':sum(x['baseline_peak_through_t0'] for x in people)/100,'prior_peak_explicit_n':len(PRIOR_PEAK),'baseline_greater_than_t0_n':sum(x['baseline_minus_t0']>0 for x in people)},'people':people}
 OUTJ.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 fields=['name','category','sector','age','sex','t0_snapshot_scope_score','baseline_peak_through_t0','baseline_peak_role','baseline_peak_year','baseline_minus_t0','baseline_basis']
 with OUTC.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:p.get(k) for k in fields} for p in people)
 print(json.dumps(out['qa'],ensure_ascii=False,indent=2))
if __name__=='__main__':main()
