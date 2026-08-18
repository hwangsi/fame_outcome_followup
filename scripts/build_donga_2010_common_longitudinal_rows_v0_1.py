#!/usr/bin/env python3
import hashlib, json
from collections import Counter
from pathlib import Path

from identity_resolution import resolve_identity_key, person_id_from_identity_key

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'data/typeA/donga_2010_target2020_master_v1_0.json'
OUT=ROOT/'data/typeA/donga_2010_common_longitudinal_rows_v0_1.json'
FREEZE=ROOT/'state/donga_2010_common_longitudinal_rows_freeze_v0_1.json'
OUTLET='동아일보'; COHORT_UNIT='donga_2010_2020_100'; TARGET_YEAR=2020


def snapshot_id(name):
    s=f'{OUTLET}|{COHORT_UNIT}|{name}|{TARGET_YEAR}'
    return 'snap-'+hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


def main():
    d=json.loads(SRC.read_text(encoding='utf-8'))
    q=d['qa']
    assert q['total']==100
    assert q['states']=={'resolved':87,'unresolved':10,'competing_event':3}
    rows=[]
    for p in d['people']:
        name=p['name']; fs=p['final_state']; t=p.get('target2020') or {}
        status={'resolved':'assessable','unresolved':'untraceable','competing_event':'competing_event'}[fs]
        score=t.get('scope_score')
        if status=='assessable':
            assert isinstance(score,int) and 0<=score<=4,(name,score)
        else:
            assert score is None,(name,status,score)
        ik=resolve_identity_key(name,OUTLET,COHORT_UNIT)
        refs=t.get('source_urls') or t.get('evidence_refs') or []
        if not refs:
            refs=t.get('timeline_support_urls') or []
        rows.append({
          'snapshot_id':snapshot_id(name),
          'person_id':person_id_from_identity_key(ik),
          'identity_key':ik,
          'name':name,
          'outlet':OUTLET,
          'cohort_unit':COHORT_UNIT,
          'selection_year':2010,
          'window_id':'t10',
          'semantic_alias':'explicit_target_2020',
          'target_year':2020,
          'window_start':'2019-01-01',
          'window_end':'2021-12-31',
          'status':status,
          'scope_score':score,
          'scope_ge2':(score>=2) if score is not None else None,
          'major_ge3':(score>=3) if score is not None else None,
          'apex_eq4':(score==4) if score is not None else None,
          'role_at_window':t.get('role'),
          'evidence_date':t.get('evidence_date'),
          'match':t.get('match'),
          'confidence':t.get('confidence'),
          'evidence_refs':refs,
          'category':p.get('category'),
          'source_ref':'data/typeA/donga_2010_target2020_master_v1_0.json',
          'provenance_layers':p.get('provenance_layers') or []
        })
    assert len(rows)==100 and len({r['name'] for r in rows})==100 and len({r['snapshot_id'] for r in rows})==100
    sc=Counter(r['status'] for r in rows)
    assert sc=={'assessable':87,'untraceable':10,'competing_event':3},sc
    assessed=[r for r in rows if r['status']=='assessable']
    scorec=Counter(r['scope_score'] for r in assessed)
    assert scorec=={1:2,2:43,3:37,4:5},scorec
    assert sum(r['scope_ge2'] for r in assessed)==85
    assert sum(r['major_ge3'] for r in assessed)==42
    assert sum(r['apex_eq4'] for r in assessed)==5
    rows.sort(key=lambda r:r['name'])
    qa={'rows':100,'unique_names':100,'unique_snapshot_ids':100,'assessable_n':87,'competing_event_n':3,'untraceable_n':10,'score_counts_assessable':{str(k):scorec.get(k,0) for k in range(5)},'scope_ge2_n':85,'major_ge3_n':42,'apex_eq4_n':5}
    payload={'schema_version':'donga_2010_common_longitudinal_rows_v0.1','generated':'2026-08-18','status':'materialized_100_of_100_canonical_t10_rows','semantic_adapter_ref':'data/typeA/donga_2010_common_longitudinal_adapter_v0_1.json','qa':qa,'rows':rows}
    freeze={'schema_version':'donga_2010_common_longitudinal_rows_freeze_v0.1','generated':'2026-08-18','qa':qa,'source_ref':'data/typeA/donga_2010_target2020_master_v1_0.json','guardrails':['one canonical snapshot row per selected unit','explicit target 2020 and T+10 are semantic aliases, not duplicate observations','competing event and unresolved remain null rather than score 0','exact 2020 evidence remains preferred over higher 2021 within-window events']}
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    FREEZE.write_text(json.dumps(freeze,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(freeze,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
