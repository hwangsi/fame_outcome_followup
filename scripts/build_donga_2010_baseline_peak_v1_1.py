#!/usr/bin/env python3
import csv,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; TYPEA=ROOT/'data/typeA'
T0=TYPEA/'donga_2010_t0_snapshot_scope_v1_1.json'; OUTJ=TYPEA/'donga_2010_baseline_peak_through_t0_v1_1.json'; OUTC=TYPEA/'donga_2010_baseline_peak_through_t0_v1_1.csv'
PRIOR={
'이소연':{'score':3,'role':'한국 최초 우주인·소유즈 TMA-12/국제우주정거장 우주실험전문가','year':2008,'urls':['https://www.kari.re.kr/kor/article/ATCL87374b48c/9969','https://www.kari.re.kr/kor/article/ATCL87374b48c/9976']},
'유시민':{'score':3,'role':'보건복지부 장관','year':2006,'urls':[]},
'안철수':{'score':3,'role':'안철수연구소 창업자·대표이사/이사회 의장','year':2005,'urls':['https://company.ahnlab.com/kr/company/founder.do']},
'홍명보':{'score':3,'role':'대한민국 축구 국가대표 주장·2002 월드컵 핵심 선수','year':2002,'urls':[]}
}
def main():
 d=json.loads(T0.read_text(encoding='utf-8'));people=[]
 for p in d['people']:
  t=p['t0_snapshot_scope_score'];e=PRIOR.get(p['name'])
  if e and e['score']>=t: peak=e['score'];role=e['role'];year=e['year'];basis='explicit_prior_peak_audit';urls=e['urls']
  else: peak=t;role=p['t0_role'];year=2010;basis='t0_snapshot_is_highest_identified_through_selection';urls=[]
  people.append({'name':p['name'],'category':p['category'],'sector':p['sector'],'age':p.get('age'),'sex':p.get('sex'),'t0_snapshot_scope_score':t,'baseline_peak_through_t0':peak,'baseline_peak_role':role,'baseline_peak_year':year,'baseline_minus_t0':peak-t,'baseline_basis':basis,'source_urls':urls})
 c=Counter(x['baseline_peak_through_t0'] for x in people);assert c==Counter({2:50,3:46,4:3,1:1}),c
 out={'schema_version':'donga_2010_baseline_peak_through_t0_v1.1','generated':'2026-08-18','t0_ref':'data/typeA/donga_2010_t0_snapshot_scope_v1_1.json','supersedes':'data/typeA/donga_2010_baseline_peak_through_t0_v0_1.json','qa':{'total':100,'unique_names':100,'score_counts':{str(k):v for k,v in sorted(c.items())},'mean_baseline_peak':sum(x['baseline_peak_through_t0'] for x in people)/100,'baseline_greater_than_t0_n':sum(x['baseline_minus_t0']>0 for x in people)},'people':people}
 assert out['qa']['baseline_greater_than_t0_n']==1
 OUTJ.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 fields=['name','category','sector','t0_snapshot_scope_score','baseline_peak_through_t0','baseline_peak_role','baseline_peak_year','baseline_minus_t0','baseline_basis']
 with OUTC.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:p.get(k) for k in fields} for p in people)
 print(json.dumps(out['qa'],ensure_ascii=False,indent=2))
if __name__=='__main__':main()
