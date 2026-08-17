#!/usr/bin/env python3
import csv,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];TYPEA=ROOT/'data/typeA'
SRC=TYPEA/'donga_2011_t0_snapshot_scope_v0_2.json';OUTJ=TYPEA/'donga_2011_t0_snapshot_scope_v0_3.json';OUTC=TYPEA/'donga_2011_t0_snapshot_scope_v0_3.csv'
CORR={
'김영달':{'old_score':2,'new_score':3,'reason':'Before the 2011 cutoff, IDIS was reported as having risen past GE and Sony to No.1 in the global DVR industry, with >50% Korean market share and substantial overseas business; this meets major/global industry-leader scope.','source_urls':['https://biz.chosun.com/site/data/html_dir/2010/10/08/2010100800451.html','https://www.mk.co.kr/news/stock/4800821']},
'김철영':{'old_score':2,'new_score':3,'reason':'Before cutoff, Mirae Nanotech had broken into a formerly 3M-dominated global optical-film market, was reported near/at global No.1 territory with strong overseas customers and multi-thousand-billion-won revenue scale; Kim as founder-CEO meets major industry leader scope.','source_urls':['https://www.mk.co.kr/news/business/4730373','https://view.asiae.co.kr/article/2010032214213709737','https://www.etnews.com/201006250114']},
'황철주':{'old_score':2,'new_score':3,'reason':'Before cutoff, Jusung Engineering ranked 11th globally in solar equipment and had signed a KRW 160 billion China solar-equipment export contract described as the largest single domestic-equipment export at that time; Hwang was a major equipment-industry leader.','source_urls':['https://www.etnews.com/201101260156','https://www.etnews.com/201004040100']}
}
NO_CHANGE_NOTES={
'남민우':'Domestic wired-network equipment leader with expanding exports, but at cutoff the firm was still explicitly targeting future global top-five status; retain score 2 under conservative large/global-industry threshold.',
'남광희':'Strong global component supplier and distinctive technology, but available cutoff evidence does not establish company/CEO as a broad major-industry leader; retain 2.',
'박상일':'World-class AFM technology and national core technology designation, but small firm scale and limited global share at the period support conservative score 2.',
'정준':'International technology-pioneer recognition is notable, but available evidence supports innovative specialist-company leadership rather than major-industry scope; retain 2.'
}
def main():
 d=json.loads(SRC.read_text(encoding='utf-8'));people=[]
 for p in d['people']:
  p=dict(p);n=p['name'];c=CORR.get(n)
  if c:
   assert p['t0_snapshot_scope_score']==c['old_score'];p['t0_snapshot_scope_score']=c['new_score'];p['score_basis']='business_scale_and_global_industry_audit';p['coding_confidence']='H';p['t0_correction_v0_3']=c
  if n in NO_CHANGE_NOTES:p['business_scope_no_change_v0_3']=NO_CHANGE_NOTES[n]
  people.append(p)
 cnt=Counter(x['t0_snapshot_scope_score'] for x in people);assert cnt==Counter({2:44,3:51,4:5}),cnt
 out={'schema_version':'donga_2011_t0_snapshot_scope_v0.3','generated':'2026-08-18','status':'audited_t0_snapshot_ready_for_freeze_candidate','supersedes':'data/typeA/donga_2011_t0_snapshot_scope_v0_2.json','corrections':CORR,'business_no_change_notes':NO_CHANGE_NOTES,'qa':{'total':100,'unique_names':100,'repeat_n':sum(x['repeat_2010_2011'] for x in people),'score_counts':{str(k):v for k,v in sorted(cnt.items())},'mean_scope':sum(x['t0_snapshot_scope_score'] for x in people)/100,'review_flagged_n':0},'people':people}
 OUTJ.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 fields=['name','category','t0_role','repeat_2010_2011','t0_snapshot_scope_score','sector','score_basis','coding_confidence']
 with OUTC.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:p.get(k) for k in fields} for p in people)
 print(json.dumps(out['qa'],ensure_ascii=False,indent=2))
if __name__=='__main__':main()
