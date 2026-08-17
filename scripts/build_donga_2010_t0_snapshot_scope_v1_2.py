#!/usr/bin/env python3
import csv,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];TYPEA=ROOT/'data/typeA'
SRC=TYPEA/'donga_2010_t0_snapshot_scope_v1_1.json';OUTJ=TYPEA/'donga_2010_t0_snapshot_scope_v1_2.json';OUTC=TYPEA/'donga_2010_t0_snapshot_scope_v1_2.csv'
CORR={'서동철':{'old_score':2,'new_score':3,'reason':'IBS official memorial describes Charles D. Surh as a world-renowned immunologist who, before 2010 at Scripps, published landmark T-cell life-cycle studies in Nature and Science, including a world-first finding on thymic T-cell selection.','source_urls':['https://www.ibs.re.kr/kor/sub02_05_02.do','https://www.ibs.re.kr/cop/bbs/BBSMSTR_000000000739/selectBoardArticle.do?nttId=14946']}}
def main():
 d=json.loads(SRC.read_text(encoding='utf-8'));people=[]
 for p in d['people']:
  p=dict(p);c=CORR.get(p['name'])
  if c:
   assert p['t0_snapshot_scope_score']==c['old_score'];p['t0_snapshot_scope_score']=c['new_score'];p['score_basis']='freeze_v1_2_preselection_world_leading_research_correction';p['coding_confidence']='H';p['t0_correction_v1_2']=c
  people.append(p)
 cnt=Counter(x['t0_snapshot_scope_score'] for x in people);assert cnt==Counter({2:50,3:46,4:3,1:1}),cnt
 out={'schema_version':'donga_2010_t0_snapshot_scope_v1.2','generated':'2026-08-18','supersedes':'data/typeA/donga_2010_t0_snapshot_scope_v1_1.json','corrections':CORR,'qa':{'total':100,'unique_names':100,'score_counts':{str(k):v for k,v in sorted(cnt.items())},'mean_scope':sum(x['t0_snapshot_scope_score'] for x in people)/100},'people':people}
 OUTJ.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 fields=['name','category','t0_role','age','sex','t0_snapshot_scope_score','sector','score_basis','coding_confidence']
 with OUTC.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:p.get(k) for k in fields} for p in people)
 print(json.dumps(out['qa'],ensure_ascii=False,indent=2))
if __name__=='__main__':main()
