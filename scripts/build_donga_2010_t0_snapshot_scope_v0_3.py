#!/usr/bin/env python3
import csv,json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; TYPEA=ROOT/'data/typeA'
SRC=TYPEA/'donga_2010_t0_snapshot_scope_v0_2.json'
OUTJ=TYPEA/'donga_2010_t0_snapshot_scope_v0_3.json'; OUTC=TYPEA/'donga_2010_t0_snapshot_scope_v0_3.csv'

CORR={
'김광수':('Harvard/McLean team led by Kwang-Soo Kim reported a 2009 protein-based, transgene-free iPS reprogramming advance with direct therapeutic relevance.',['https://news.harvard.edu/gazette/story/2009/06/safer-stem-cells-for-therapy/']),
'김기문':('POSTECH selected Kim as a 2009 POSTECH Fellow for outstanding research achievements attracting worldwide attention.',['https://chem.postech.ac.kr/sub1_3.php']),
'김필립':('By selection he had the 2008 Ho-Am Science Prize, 2009 IBM Faculty Award, APS Fellowship and internationally leading graphene work including Nature/Nature Physics publications.',['https://philipkim.scholars.harvard.edu/bio','https://philipkim.scholars.harvard.edu/publications-0']),
'남홍길':('Before selection he had achieved corresponding-author publications across Science, Cell and Nature, was described by POSTECH as having established a world-leading position in plant research, and received the 2009 National Academy of Sciences award.',['https://www.postech.ac.kr/kor/research-industry-academia/research-results.do?articleNo=6700&mode=view','https://postech.ac.kr/kor/newscenter/university-news.do?articleNo=4150&mode=view']),
'박홍근':('Before selection Hongkun Park was a tenured Harvard professor with major international research awards including the 2008 NIH Director’s Pioneer Award and prior Ho-Am Science Prize.',['https://www.chemistry.harvard.edu/people/hongkun-park']),
'임지순':('Before selection SNU described Ihm as a world authority in carbon nanomaterials; he received an international ACCMS award in 2009 and was appointed SNU endowed professor effective 2009-11-01.',['https://physics.snu.ac.kr/boards/news?page=55','https://www.snu.ac.kr/research/highlights?bbsidx=74738&md=v']),
'정하웅':('KAIST described Jeong as an international expert who pioneered complex-network science, with Nature, PNAS and PRL papers and >5,000 citations already documented around the selection era.',['https://news.kaist.ac.kr/site/news/html/news/?skey=prof&sval=%EC%A0%95%ED%95%98%EC%9B%85']),
'찰스 리':('His discovery of widespread copy-number variation opened a new field of human genetics and earned the 2008 Ho-Am Prize in Medicine before selection.',['https://news.harvard.edu/gazette/story/2008/04/ho-am-prize-koreas-nobel-is-awarded-to-bwhs-charles-lee/'])
}

def main():
 d=json.loads(SRC.read_text(encoding='utf-8')); people=[]
 for p in d['people']:
  p=dict(p); n=p['name']
  if n in CORR:
   assert p['t0_snapshot_scope_score']==2,(n,p['t0_snapshot_scope_score'])
   reason,urls=CORR[n]; p['t0_snapshot_scope_score']=3; p['score_basis']='preselection_world_leading_research_achievement_correction'; p['coding_confidence']='H'
   p['review_flags']=[]
   p['t0_correction_v0_3']={'reason':reason,'source_urls':urls}
  people.append(p)
 counts=Counter(x['t0_snapshot_scope_score'] for x in people)
 assert counts==Counter({2:53,3:43,4:3,1:1}),counts
 bycat={}
 for cat in dict.fromkeys(x['category'] for x in people):
  s=[x for x in people if x['category']==cat]
  bycat[cat]={'n':len(s),'score_counts':{str(k):v for k,v in sorted(Counter(x['t0_snapshot_scope_score'] for x in s).items())},'mean_scope':sum(x['t0_snapshot_scope_score'] for x in s)/len(s),'review_flagged':sum(bool(x.get('review_flags')) for x in s)}
 out={'schema_version':'donga_2010_t0_snapshot_scope_v0.3','generated':'2026-08-18','supersedes':'data/typeA/donga_2010_t0_snapshot_scope_v0_2.json','status':'pass1_research_audit_corrected_provisional_not_baseline_peak','corrections':{n:{'new_score':3,'reason':v[0],'source_urls':v[1]} for n,v in CORR.items()},'qa':{'total':100,'unique_names':100,'score_counts':{str(k):v for k,v in sorted(counts.items())},'review_flagged_n':sum(bool(x.get('review_flags')) for x in people),'by_category':bycat},'people':people}
 OUTJ.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 fields=['name','category','t0_role','age','sex','t0_snapshot_scope_score','sector','score_basis','coding_confidence','review_flags']
 with OUTC.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
  for p in people:
   r={k:p.get(k) for k in fields};r['review_flags']=';'.join(p.get('review_flags',[]));w.writerow(r)
 print(json.dumps(out['qa'],ensure_ascii=False,indent=2))

if __name__=='__main__':main()
