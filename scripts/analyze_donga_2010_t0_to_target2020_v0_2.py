#!/usr/bin/env python3
import json
from collections import Counter
from pathlib import Path
from statistics import mean, median

ROOT=Path(__file__).resolve().parents[1]
TYPEA=ROOT/'data/typeA'
T0=TYPEA/'donga_2010_t0_snapshot_scope_v0_2.json'
TARGET=TYPEA/'donga_2010_target2020_master_v1_0.json'
OUT=TYPEA/'donga_2010_t0_to_target2020_snapshot_change_v0_2.json'

def main():
    t0=json.loads(T0.read_text(encoding='utf-8'))
    target=json.loads(TARGET.read_text(encoding='utf-8'))
    t0by={p['name']:p for p in t0['people']}
    rows=[]
    for p in target['people']:
        if p['final_state']!='resolved': continue
        x=t0by[p['name']]
        a=x['t0_snapshot_scope_score']; b=(p.get('target2020') or {}).get('scope_score')
        assert b is not None
        rows.append({
          'name':p['name'],'category':p['category'],
          't0_snapshot_scope_score':a,'target2020_scope_score':b,'snapshot_delta':b-a,
          't0_role':x.get('t0_role'),'target2020_role':(p.get('target2020') or {}).get('role'),
          't0_review_flags':x.get('review_flags',[])
        })
    assert len(rows)==87
    d=Counter(r['snapshot_delta'] for r in rows)
    cats={}
    for cat in dict.fromkeys(r['category'] for r in rows):
        s=[r for r in rows if r['category']==cat]
        cats[cat]={
          'n':len(s),'t0_mean':mean(r['t0_snapshot_scope_score'] for r in s),
          'target2020_mean':mean(r['target2020_scope_score'] for r in s),
          'mean_snapshot_delta':mean(r['snapshot_delta'] for r in s),
          'up_n':sum(r['snapshot_delta']>0 for r in s),
          'same_n':sum(r['snapshot_delta']==0 for r in s),
          'down_n':sum(r['snapshot_delta']<0 for r in s)
        }
    overall={
      't0_mean_same87':mean(r['t0_snapshot_scope_score'] for r in rows),
      'target2020_mean_same87':mean(r['target2020_scope_score'] for r in rows),
      'mean_snapshot_delta':mean(r['snapshot_delta'] for r in rows),
      'median_snapshot_delta':median(r['snapshot_delta'] for r in rows),
      'delta_counts':{str(k):v for k,v in sorted(d.items())},
      'up_n':sum(r['snapshot_delta']>0 for r in rows),
      'same_n':sum(r['snapshot_delta']==0 for r in rows),
      'down_n':sum(r['snapshot_delta']<0 for r in rows)
    }
    out={
      'schema_version':'donga_2010_t0_to_target2020_snapshot_change_v0.2',
      'generated':'2026-08-18',
      't0_ref':'data/typeA/donga_2010_t0_snapshot_scope_v0_2.json',
      'warning':'Descriptive target2020 minus corrected provisional T0 snapshot; NOT baseline-adjusted advancement.',
      'population':{'resolved_target_rows':87,'excluded_target_unresolved':10,'excluded_competing_event':3},
      'overall':overall,'by_category':cats,
      'largest_positive':[r for r in rows if r['snapshot_delta']==max(x['snapshot_delta'] for x in rows)],
      'largest_negative':[r for r in rows if r['snapshot_delta']==min(x['snapshot_delta'] for x in rows)],
      'rows':rows
    }
    OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    assert overall['up_n']+overall['same_n']+overall['down_n']==87
    print(json.dumps(overall,ensure_ascii=False,indent=2))
    print(json.dumps(cats,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
