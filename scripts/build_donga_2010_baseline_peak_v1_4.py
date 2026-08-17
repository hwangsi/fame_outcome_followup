#!/usr/bin/env python3
import csv,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];TYPEA=ROOT/'data/typeA'
T0=TYPEA/'donga_2010_t0_snapshot_scope_v1_3.json';OUTJ=TYPEA/'donga_2010_baseline_peak_through_t0_v1_4.json';OUTC=TYPEA/'donga_2010_baseline_peak_through_t0_v1_4.csv'
PRIOR={
'이소연':(3,'한국 최초 우주인·소유즈 TMA-12/국제우주정거장 우주실험전문가',2008,['https://www.kari.re.kr/kor/article/ATCL87374b48c/9969']),
'유시민':(3,'보건복지부 장관',2006,[]),
'안철수':(3,'안철수연구소 창업자·대표이사/이사회 의장',2005,['https://company.ahnlab.com/kr/company/founder.do']),
'홍명보':(3,'대한민국 축구 국가대표 주장·2002 월드컵 핵심 선수',2002,[]),
'김병국':(3,'대통령실 외교안보수석비서관',2008,['https://www.yna.co.kr/view/AKR20120224170500043'])
}
def main():
 d=json.loads(T0.read_text(encoding='utf-8'));people=[]
 for p in d['people']:
  t=p['t0_snapshot_scope_score'];e=PRIOR.get(p['name'])
  if e and e[0]>=t: peak,role,year,urls=e;basis='explicit_prior_peak_audit'
  else: peak,role,year,urls=t,p['t0_role'],2010,[];basis='t0_snapshot_is_highest_identified_through_selection'
  people.append({'name':p['name'],'category':p['category'],'sector':p['sector'],'age':p.get('age'),'sex':p.get('sex'),'t0_snapshot_scope_score':t,'baseline_peak_through_t0':peak,'baseline_peak_role':role,'baseline_peak_year':year,'baseline_minus_t0':peak-t,'baseline_basis':basis,'source_urls':urls})
 c=Counter(x['baseline_peak_through_t0'] for x in people);assert c==Counter({2:46,3:50,4:3,1:1}),c
 greater=[x['name'] for x in people if x['baseline_minus_t0']>0];assert set(greater)=={'이소연','김병국'},greater
 out={'schema_version':'donga_2010_baseline_peak_through_t0_v1.4','generated':'2026-08-18','t0_ref':'data/typeA/donga_2010_t0_snapshot_scope_v1_3.json','supersedes':'data/typeA/donga_2010_baseline_peak_through_t0_v1_3.json','correction':{'name':'김병국','t0_unchanged':2,'baseline_old':2,'baseline_new':3,'reason':'He had already served as presidential senior secretary for foreign affairs and national security in 2008, before the 2010 selection.'},'qa':{'total':100,'unique_names':100,'score_counts':{str(k):v for k,v in sorted(c.items())},'mean_baseline_peak':sum(x['baseline_peak_through_t0'] for x in people)/100,'baseline_greater_than_t0_n':len(greater),'baseline_greater_than_t0_names':greater},'people':people}
 OUTJ.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 fields=['name','category','sector','t0_snapshot_scope_score','baseline_peak_through_t0','baseline_peak_role','baseline_peak_year','baseline_minus_t0','baseline_basis']
 with OUTC.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:p.get(k) for k in fields} for p in people)
 print(json.dumps(out['qa'],ensure_ascii=False,indent=2))
if __name__=='__main__':main()
