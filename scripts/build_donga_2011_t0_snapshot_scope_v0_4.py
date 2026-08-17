#!/usr/bin/env python3
import csv,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];TYPEA=ROOT/'data/typeA'
SRC=TYPEA/'donga_2011_t0_snapshot_scope_v0_3.json';OUTJ=TYPEA/'donga_2011_t0_snapshot_scope_v0_4.json';OUTC=TYPEA/'donga_2011_t0_snapshot_scope_v0_4.csv'
CORR={'이자람':{'old_score':2,'new_score':3,'reason':'Before the 2011 cutoff, Lee Jaram had already won Best Actress at the 2010 Kontakt International Theatre Festival in Poland for Sacheonga, with her troupe the only Asian participant. This is a direct international performing-arts achievement meeting score-3 scope.','source_urls':['https://sports.donga.com/ent/article/all/20100531/28742678/1','https://www.playdb.co.kr/productiondb/detail.asp?BizNo=3780']}}
def main():
 d=json.loads(SRC.read_text(encoding='utf-8'));people=[]
 for p in d['people']:
  p=dict(p);n=p['name']
  if n in CORR:
   c=CORR[n];assert p['t0_snapshot_scope_score']==c['old_score'];p['t0_snapshot_scope_score']=c['new_score'];p['score_basis']='preselection_international_performing_arts_achievement_audit';p['coding_confidence']='H';p['t0_correction_v0_4']=c
  people.append(p)
 cnt=Counter(x['t0_snapshot_scope_score'] for x in people);assert cnt==Counter({2:43,3:52,4:5}),cnt
 out={'schema_version':'donga_2011_t0_snapshot_scope_v0.4','generated':'2026-08-18','status':'audited_t0_snapshot_freeze_candidate','supersedes':'data/typeA/donga_2011_t0_snapshot_scope_v0_3.json','corrections':CORR,'qa':{'total':100,'unique_names':100,'repeat_n':sum(x['repeat_2010_2011'] for x in people),'score_counts':{str(k):v for k,v in sorted(cnt.items())},'mean_scope':sum(x['t0_snapshot_scope_score'] for x in people)/100,'review_flagged_n':0},'people':people}
 OUTJ.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 fields=['name','category','t0_role','repeat_2010_2011','t0_snapshot_scope_score','sector','score_basis','coding_confidence']
 with OUTC.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:p.get(k) for k in fields} for p in people)
 print(json.dumps(out['qa'],ensure_ascii=False,indent=2))
if __name__=='__main__':main()
