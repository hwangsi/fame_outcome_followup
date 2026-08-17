#!/usr/bin/env python3
import csv, json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TYPEA=ROOT/'data/typeA'
SRC=TYPEA/'donga_2010_t0_snapshot_scope_v0_1.json'
OUTJ=TYPEA/'donga_2010_t0_snapshot_scope_v0_2.json'
OUTC=TYPEA/'donga_2010_t0_snapshot_scope_v0_2.csv'

CORRECTIONS={
  '안철수':{
    'old_score':2,'new_score':3,
    'reason':'At selection he simultaneously held KAIST endowed-chair professorship, AhnLab board chairmanship, and POSCO outside-director/board-chair roles; the capture listed only the academic role.',
    'source_urls':['https://company.ahnlab.com/kr/company/founder.do'],
    'basis':'contemporaneous_multi_role_correction'
  },
  '유시민':{
    'old_score':1,'new_score':3,
    'reason':'By 2010-05-03 he was an active Gyeonggi governor preliminary candidate participating in the opposition-unification contest, before the Donga 2010-05-10 selection launch.',
    'source_urls':['https://www.yna.co.kr/view/AKR20100503108200001'],
    'basis':'contemporaneous_campaign_role_correction'
  },
  '조성진':{
    'old_score':2,'new_score':3,
    'reason':'Before selection he had won the 2009 Hamamatsu International Piano Competition as its youngest winner and first Asian champion, after a prior international youth Chopin win.',
    'source_urls':['https://www.yna.co.kr/view/AKR20091123068200005'],
    'basis':'preselection_international_achievement_correction'
  }
}

def main():
    d=json.loads(SRC.read_text(encoding='utf-8'))
    people=[]
    for p in d['people']:
        p=dict(p)
        name=p['name']
        if name in CORRECTIONS:
            c=CORRECTIONS[name]
            assert p['t0_snapshot_scope_score']==c['old_score'], (name,p['t0_snapshot_scope_score'])
            p['t0_snapshot_scope_score']=c['new_score']
            p['score_basis']=c['basis']
            p['coding_confidence']='H'
            p['review_flags']=[x for x in p.get('review_flags',[]) if 'context' not in x]
            p['t0_correction_v0_2']={k:v for k,v in c.items() if k not in ('old_score','new_score')}
        people.append(p)
    counts=Counter(p['t0_snapshot_scope_score'] for p in people)
    assert counts==Counter({2:61,3:35,4:3,1:1}), counts
    assert len(people)==100 and len({p['name'] for p in people})==100
    bycat={}
    for cat in dict.fromkeys(p['category'] for p in people):
        s=[p for p in people if p['category']==cat]
        bycat[cat]={
          'n':len(s),
          'score_counts':{str(k):v for k,v in sorted(Counter(x['t0_snapshot_scope_score'] for x in s).items())},
          'mean_scope':sum(x['t0_snapshot_scope_score'] for x in s)/len(s),
          'review_flagged':sum(bool(x.get('review_flags')) for x in s)
        }
    out={
      'schema_version':'donga_2010_t0_snapshot_scope_v0.2',
      'generated':'2026-08-18',
      'supersedes':'data/typeA/donga_2010_t0_snapshot_scope_v0_1.json',
      'status':'pass1_corrected_provisional_not_baseline_peak',
      'corrections':CORRECTIONS,
      'qa':{
        'total':100,'unique_names':100,
        'score_counts':{str(k):v for k,v in sorted(counts.items())},
        'review_flagged_n':sum(bool(x.get('review_flags')) for x in people),
        'by_category':bycat
      },
      'people':people
    }
    OUTJ.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    fields=['name','category','t0_role','age','sex','t0_snapshot_scope_score','sector','score_basis','coding_confidence','review_flags']
    with OUTC.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
        for p in people:
            r={k:p.get(k) for k in fields}; r['review_flags']=';'.join(p.get('review_flags',[])); w.writerow(r)
    print(json.dumps(out['qa'],ensure_ascii=False,indent=2))

if __name__=='__main__': main()
