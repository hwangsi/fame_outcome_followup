#!/usr/bin/env python3
import csv,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; TYPEA=ROOT/'data/typeA'
SRC=TYPEA/'donga_2010_t0_snapshot_scope_v0_3.json'; OUTJ=TYPEA/'donga_2010_t0_snapshot_scope_v0_4.json'; OUTC=TYPEA/'donga_2010_t0_snapshot_scope_v0_4.csv'
AUDIT={
'김윤진':{'decision':'keep_3','reason':'ABC biography confirms worldwide recognition from Lost and major Korean acting awards, supporting international major-professional scope but not a pre-selection global-apex award.','source_urls':['https://abc.com/cast/de2008f9-abf7-43a9-b445-17769bfdfbaa']},
'박진영':{'decision':'keep_3','reason':'The primary 2010 capture identifies a nationally major singer-producer role; no pre-selection evidence meeting the locked score-4 global-apex threshold is required or supported.'},
'봉준호':{'decision':'keep_3','reason':'Cannes documents international renown and 2009 Un Certain Regard selection before T0; Palme d’Or came in 2019, so 2010 remains score 3 rather than global-apex 4.','source_urls':['https://www.festival-cannes.com/en/2009/bong-joon-ho-returns-to-certain-regard-with-mother/','https://www.festival-cannes.com/en/p/joon-ho-bong-2/']},
'서도호':{'decision':'keep_3','reason':'Smithsonian documents worldwide exhibitions including the 2001 Venice Biennale and multiple solo shows before the selection era, supporting international-major artist scope without a score-4 apex event.','source_urls':['https://asia-archive.si.edu/press-release/perspectives-do-ho-suh/']},
'장한나':{'decision':'keep_3','reason':'Warner Classics documents early Rostropovich Competition first prize, Grammy-nominated recordings and major classical awards; this supports international-major musician scope while remaining below the deliberately rare score-4 global-apex threshold.','source_urls':['https://www.warnerclassics.com/release/the-swan']},
'장하준':{'decision':'keep_3','reason':'The 2010 primary role is Cambridge economics professor with established international scholarly influence; no Nobel-equivalent or analogous score-4 apex achievement existed before selection.'},
'강덕수':{'decision':'keep_3','reason':'The 2010 primary role is STX Group chair, a major national conglomerate leadership role. The locked business rubric reserves score 4 for top-chaebol/global-industry apex, so no upward change is made.'},
'박현주':{'decision':'keep_3','reason':'Mirae Asset documents chairmanship since 2001, a 2009 Ernst & Young master entrepreneur award and a 2010 Harvard Business School case; major national/globalizing finance leadership fits score 3, while score 4 remains reserved for top-conglomerate/global-industry apex.','source_urls':['https://securities.miraeasset.com/newir/view/mobile/kr/about/founderGISO.jsp']}
}
def main():
 d=json.loads(SRC.read_text(encoding='utf-8')); people=[]
 for p in d['people']:
  p=dict(p); n=p['name']
  if n in AUDIT:
   assert p['t0_snapshot_scope_score']==3,(n,p['t0_snapshot_scope_score'])
   p['review_flags']=[]; p['t0_review_closure_v0_4']=AUDIT[n]
  people.append(p)
 counts=Counter(x['t0_snapshot_scope_score'] for x in people); assert counts==Counter({2:53,3:43,4:3,1:1})
 assert sum(bool(x.get('review_flags')) for x in people)==0
 bycat={}
 for cat in dict.fromkeys(x['category'] for x in people):
  s=[x for x in people if x['category']==cat]
  bycat[cat]={'n':len(s),'score_counts':{str(k):v for k,v in sorted(Counter(x['t0_snapshot_scope_score'] for x in s).items())},'mean_scope':sum(x['t0_snapshot_scope_score'] for x in s)/len(s),'review_flagged':0}
 out={'schema_version':'donga_2010_t0_snapshot_scope_v0.4','generated':'2026-08-18','supersedes':'data/typeA/donga_2010_t0_snapshot_scope_v0_3.json','status':'t0_snapshot_audit_complete_ready_to_freeze','review_closures':AUDIT,'qa':{'total':100,'unique_names':100,'score_counts':{str(k):v for k,v in sorted(counts.items())},'review_flagged_n':0,'by_category':bycat},'people':people}
 OUTJ.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 fields=['name','category','t0_role','age','sex','t0_snapshot_scope_score','sector','score_basis','coding_confidence','review_flags']
 with OUTC.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
  for p in people:
   r={k:p.get(k) for k in fields};r['review_flags']='';w.writerow(r)
 print(json.dumps(out['qa'],ensure_ascii=False,indent=2))
if __name__=='__main__':main()
