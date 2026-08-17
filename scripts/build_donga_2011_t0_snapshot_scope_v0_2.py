#!/usr/bin/env python3
import csv,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];TYPEA=ROOT/'data/typeA'
SRC=TYPEA/'donga_2011_t0_snapshot_scope_v0_1.json';OUTJ=TYPEA/'donga_2011_t0_snapshot_scope_v0_2.json';OUTC=TYPEA/'donga_2011_t0_snapshot_scope_v0_2.csv'
CORR={
'김상욱':{'old_score':2,'new_score':3,'reason':'Before 2011-04-01 he had already received the 2010 KAIST Academic Award and Korea Young Scientist Award, with internationally leading molecular-assembly nanomaterials work including Nature-level research; this meets international-leading science scope.','source_urls':['https://www.kaist.ac.kr/newsen/html/news/?skey=prof&sval=Kim+Sang+Ouk']},
'김은성':{'old_score':2,'new_score':3,'reason':'Before selection, KAIST described Eunseong Kim as co-discoverer of supersolidity and reported his 2010 Nature Physics and Science work providing major new evidence; this is international-leading/field-shaping research, not generic professor scope.','source_urls':['https://kaist.ac.kr/newsen/html/news/?GotoPage=189&list_e_date=&list_s_date=&mng_no=3711&mode=V&skey=&sval=','https://news.kaist.ac.kr/site/news/html/news/index.php?GotoPage=1&list_e_date=&list_s_date=&mng_no=2696&mode=V&skey=keyword&sval=%EC%9D%BC%EB%B3%B8','https://pubmed.ncbi.nlm.nih.gov/21097904/']},
'함돈희':{'old_score':2,'new_score':3,'reason':'By 2009-2011 Donhee Ham was Harvard Gordon McKay Professor of Electrical Engineering and Applied Physics and had been named an MIT Technology Review TR35 global young innovator in 2008; this exceeds generic professor scope.','source_urls':['https://people.seas.harvard.edu/~donhee/donheeham.htm']},
'박근혜':{'old_score':2,'new_score':4,'reason':'Although the official roster title is MP, immediately before selection she was the overwhelming nationwide presidential frontrunner: a Jan 2011 poll put her at 42.3%, with all other contenders in single digits. Locked politics rubric assigns score 4 to a viable national presidential contender.','source_urls':['https://www.yna.co.kr/view/AKR20110102037700001','https://imnews.imbc.com/replay/2011/nwdesk/article/2770686_30473.html']},
'변대규':{'old_score':2,'new_score':3,'reason':'By Jan 2011 Humax, founded and led by Byun Dae-gyu, had passed KRW 1 trillion annual revenue, 98% overseas sales, and was reported as fourth in the global set-top-box market. This meets major/global industry-leader scope rather than ordinary mid-sized CEO scope.','source_urls':['https://www.hankyung.com/article/2011012664651']}
}
RESOLVED_NO_CHANGE={
'김정범':'Center/direct laboratory leadership plus assistant-professor role remains score 2 absent stronger evidence of field-leading international stature by cutoff.',
'김영하':'Established national novelist with international translation activity; current evidence does not require score 3 under locked creator rubric.',
'손흥민':'Top-European-league debut/early first-team stage by cutoff but not yet an established meaningful starter career sufficient for score 3.',
'나경원':'Major-party supreme council member remains below party leader/minister/metropolitan-governor score-3 threshold.',
'김태효':'Presidential secretary is nationally important but below minister/major national-institution head threshold in locked rubric.',
'황철주':'Successful technology entrepreneur, but current pre-cutoff evidence does not require large-industry/global-leader score 3.',
'김상우':'ICC senior investigator is an important international professional role, but not high executive leadership of a major multilateral institution.',
'최재경':'Judicial Research and Training Institute deputy director remains below head/minister-level national leadership threshold.'
}
def main():
 d=json.loads(SRC.read_text(encoding='utf-8'));people=[]
 for p in d['people']:
  p=dict(p);n=p['name'];c=CORR.get(n)
  if c:
   assert p['t0_snapshot_scope_score']==c['old_score'],(n,p['t0_snapshot_scope_score'])
   p['t0_snapshot_scope_score']=c['new_score'];p['score_basis']='preselection_achievement_or_status_audit';p['coding_confidence']='H';p['t0_correction_v0_2']=c;p['review_flags']=[]
  elif n in RESOLVED_NO_CHANGE:
   p['review_resolution_v0_2']=RESOLVED_NO_CHANGE[n];p['coding_confidence']='H';p['review_flags']=[]
  people.append(p)
 cnt=Counter(x['t0_snapshot_scope_score'] for x in people);assert cnt==Counter({2:47,3:48,4:5}),cnt
 assert sum(bool(x.get('review_flags')) for x in people)==0
 out={'schema_version':'donga_2011_t0_snapshot_scope_v0.2','generated':'2026-08-18','status':'audited_t0_snapshot_candidate_for_freeze','supersedes':'data/typeA/donga_2011_t0_snapshot_scope_v0_1.json','corrections':CORR,'resolved_no_change':RESOLVED_NO_CHANGE,'qa':{'total':100,'unique_names':100,'repeat_n':sum(x['repeat_2010_2011'] for x in people),'score_counts':{str(k):v for k,v in sorted(cnt.items())},'mean_scope':sum(x['t0_snapshot_scope_score'] for x in people)/100,'review_flagged_n':0},'people':people}
 OUTJ.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 fields=['name','category','t0_role','repeat_2010_2011','t0_snapshot_scope_score','sector','score_basis','coding_confidence']
 with OUTC.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows({k:p.get(k) for k in fields} for p in people)
 print(json.dumps(out['qa'],ensure_ascii=False,indent=2))
if __name__=='__main__':main()
