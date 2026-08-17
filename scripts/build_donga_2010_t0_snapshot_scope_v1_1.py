#!/usr/bin/env python3
import csv,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; TYPEA=ROOT/'data/typeA'
SRC=TYPEA/'donga_2010_t0_snapshot_scope_v0_4.json'; OUTJ=TYPEA/'donga_2010_t0_snapshot_scope_v1_1.json'; OUTC=TYPEA/'donga_2010_t0_snapshot_scope_v1_1.csv'
CORR={
'이지오':{
 'old_score':2,'new_score':3,
 'reason':'Before the May-2010 selection, KAIST documented a series of Science papers identifying key sepsis-related immune-protein structures, plus 2007 Scientist of the Year and 2008 KAIST Person of the Year recognition. This meets the world-leading/repeated top-research score-3 rule.',
 'source_urls':['https://news.kaist.ac.kr/newsen/html/news/?skey=prof&sval=Jie-Oh+Lee']
},
'조동호':{
 'old_score':2,'new_score':3,
 'reason':'At the selection era he was simultaneously director of the nationally funded OLEV project, director of KAIST Institute for IT Convergence, and KT Chair Professor. KAIST states OLEV was a large multidisciplinary R&D project specially funded through the 2009 supplementary budget, meeting the major national technology-program leader score-3 rule.',
 'source_urls':['https://news.kaist.ac.kr/site/newsen/html/news/?GotoPage=177&list_e_date=&list_s_date=&mng_no=3656&mode=V&skey=ca&sval=']
}
}
def main():
 d=json.loads(SRC.read_text(encoding='utf-8')); people=[]
 for p in d['people']:
  p=dict(p); n=p['name']
  if n in CORR:
   c=CORR[n]; assert p['t0_snapshot_scope_score']==c['old_score'],(n,p['t0_snapshot_scope_score'])
   p['t0_snapshot_scope_score']=c['new_score'];p['score_basis']='freeze_v1_1_preselection_scope_correction';p['coding_confidence']='H';p['t0_correction_v1_1']=c
  people.append(p)
 counts=Counter(x['t0_snapshot_scope_score'] for x in people);assert counts==Counter({2:51,3:45,4:3,1:1}),counts
 out={'schema_version':'donga_2010_t0_snapshot_scope_v1.1','generated':'2026-08-18','supersedes_freeze':'state/donga_2010_t0_baseline_freeze_v1_0.json','source_snapshot':'data/typeA/donga_2010_t0_snapshot_scope_v0_4.json','corrections':CORR,'qa':{'total':100,'unique_names':len({x['name'] for x in people}),'score_counts':{str(k):v for k,v in sorted(counts.items())},'mean_scope':sum(x['t0_snapshot_scope_score'] for x in people)/100},'people':people}
 assert out['qa']['unique_names']==100
 OUTJ.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 fields=['name','category','t0_role','age','sex','t0_snapshot_scope_score','sector','score_basis','coding_confidence']
 with OUTC.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:p.get(k) for k in fields} for p in people)
 print(json.dumps(out['qa'],ensure_ascii=False,indent=2))
if __name__=='__main__':main()
