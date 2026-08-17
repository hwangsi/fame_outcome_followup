#!/usr/bin/env python3
import csv,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];TYPEA=ROOT/'data/typeA'
SRC=TYPEA/'donga_2010_t0_snapshot_scope_v1_2.json';OUTJ=TYPEA/'donga_2010_t0_snapshot_scope_v1_3.json';OUTC=TYPEA/'donga_2010_t0_snapshot_scope_v1_3.csv'
CORR={
'이상훈':{'old_score':2,'new_score':3,'reason':'The SNU Brain and Cognitive Sciences department history identifies Sang-Hun Lee as PI of the government World Class University grant and chair of the nascent department created in 2009; his lab also had pre-selection landmark Science/Nature visual-neuroscience work. This meets major national-program/international-leading science scope.','source_urls':['https://bcs.snu.ac.kr/sub1_2.php','https://www.snu-csnl.com/team-3']},
'이효철':{'old_score':2,'new_score':3,'reason':'By 2009 Hyotcherl Ihee was already a full KAIST professor leading the Center for Time-Resolved Diffraction and publishing field-defining work/reviews on time-resolved X-ray liquidography, following his pioneering 2005 ultrafast structural-dynamics work. This meets international-leading scientist scope before selection.','source_urls':['https://pure.kaist.ac.kr/en/persons/hyotcherl-ihee/','https://pubmed.ncbi.nlm.nih.gov/19117426/']}
}
def main():
 d=json.loads(SRC.read_text(encoding='utf-8'));people=[]
 for p in d['people']:
  p=dict(p);c=CORR.get(p['name'])
  if c:
   assert p['t0_snapshot_scope_score']==c['old_score'],(p['name'],p['t0_snapshot_scope_score'])
   p['t0_snapshot_scope_score']=c['new_score'];p['score_basis']='freeze_v1_3_preselection_leadership_research_correction';p['coding_confidence']='H';p['t0_correction_v1_3']=c
  people.append(p)
 cnt=Counter(x['t0_snapshot_scope_score'] for x in people);assert cnt==Counter({2:48,3:48,4:3,1:1}),cnt
 out={'schema_version':'donga_2010_t0_snapshot_scope_v1.3','generated':'2026-08-18','supersedes':'data/typeA/donga_2010_t0_snapshot_scope_v1_2.json','corrections':CORR,'qa':{'total':100,'unique_names':100,'score_counts':{str(k):v for k,v in sorted(cnt.items())},'mean_scope':sum(x['t0_snapshot_scope_score'] for x in people)/100},'people':people}
 OUTJ.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 fields=['name','category','t0_role','age','sex','t0_snapshot_scope_score','sector','score_basis','coding_confidence']
 with OUTC.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:p.get(k) for k in fields} for p in people)
 print(json.dumps(out['qa'],ensure_ascii=False,indent=2))
if __name__=='__main__':main()
