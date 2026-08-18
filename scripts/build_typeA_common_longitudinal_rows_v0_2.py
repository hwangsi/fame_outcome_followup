#!/usr/bin/env python3
import hashlib, json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
K04=ROOT/'data/typeA/khan_2004_17th_assembly_newleaders_longitudinal_master_v1_0.json'
D10=ROOT/'data/typeA/donga_2010_common_longitudinal_rows_v0_1.json'
D11=ROOT/'data/typeA/donga_2011_common_longitudinal_rows_v0_1.json'
OUT=ROOT/'data/typeA/typeA_common_longitudinal_rows_v0_2.json'
FREEZE=ROOT/'state/typeA_common_longitudinal_rows_freeze_v0_2.json'


def sid(outlet,unit,name,window,target):
    return 'snap-'+hashlib.sha256(f'{outlet}|{unit}|{name}|{window}|{target}'.encode()).hexdigest()[:16]


def normalize_khan2004():
    d=json.loads(K04.read_text(encoding='utf-8'))
    rows=[]
    windows=[('t10',2014,'2013-01-01','2015-12-31'),('t20',2024,'2023-01-01','2025-12-31'),('current',2026,None,None)]
    for p in d['people']:
        for w,target,start,end in windows:
            s=p[w]
            score=s.get('scope_score')
            if score is None:
                status='competing_event' if p.get('death_truncated') else 'untraceable'
            else:
                status='assessable'
            rows.append({
              'snapshot_id':sid('경향신문','khan_2004_17th_assembly_newleaders_20',p['name'],w,target),
              'person_id':None,'identity_key':p.get('identity_key') or p['name'],'name':p['name'],'outlet':'경향신문',
              'cohort_unit':'khan_2004_17th_assembly_newleaders_20','selection_year':2004,'window_id':w,'target_year':target,
              'window_start':start,'window_end':end,'status':status,'scope_score':score,
              'scope_ge2':(score>=2) if score is not None else None,'major_ge3':(score>=3) if score is not None else None,
              'apex_eq4':(score==4) if score is not None else None,'role_at_window':s.get('role'),'evidence_date':s.get('evidence_date'),
              'match':s.get('match'),'confidence':s.get('confidence'),'evidence_refs':s.get('sources') or [],
              'source_ref':'data/typeA/khan_2004_17th_assembly_newleaders_longitudinal_master_v1_0.json'
            })
    return rows


def main():
    rows=normalize_khan2004()
    d10=json.loads(D10.read_text(encoding='utf-8')); d11=json.loads(D11.read_text(encoding='utf-8'))
    assert d10['qa']['rows']==100 and d11['qa']['rows']==100
    rows += d10['rows'] + d11['rows']
    assert len(rows)==260
    assert len({r['snapshot_id'] for r in rows})==260
    cw=Counter((r['cohort_unit'],r['window_id']) for r in rows)
    assert cw=={
      ('khan_2004_17th_assembly_newleaders_20','t10'):20,
      ('khan_2004_17th_assembly_newleaders_20','t20'):20,
      ('khan_2004_17th_assembly_newleaders_20','current'):20,
      ('donga_2010_2020_100','t10'):100,
      ('donga_2011_10yr_100','t10'):100,
    },cw
    # frozen cross-checks
    def subset(unit,w): return [r for r in rows if r['cohort_unit']==unit and r['window_id']==w]
    k10=subset('khan_2004_17th_assembly_newleaders_20','t10'); k20=subset('khan_2004_17th_assembly_newleaders_20','t20')
    assert sum(r['major_ge3'] is True for r in k10)==7 and sum(r['apex_eq4'] is True for r in k10)==0
    assert sum(r['major_ge3'] is True for r in k20)==6 and sum(r['status']=='competing_event' for r in k20)==2
    d10r=subset('donga_2010_2020_100','t10'); d11r=subset('donga_2011_10yr_100','t10')
    assert sum(r['status']=='assessable' for r in d10r)==87 and sum(r['major_ge3'] is True for r in d10r)==42
    assert sum(r['status']=='assessable' for r in d11r)==90 and sum(r['major_ge3'] is True for r in d11r)==63
    rows.sort(key=lambda r:(r['selection_year'],r['cohort_unit'],r['window_id'],r['name']))
    qa={
      'snapshot_rows':260,'unique_snapshot_ids':260,'cohort_units':3,'cohort_window_cells':5,
      'khan_2004_persons':20,'khan_2004_snapshot_rows':60,'donga_2010_t10_rows':100,'donga_2011_t10_rows':100,
      'row_ready_selected_placements':220,
      'not_included_yet':['khan_2005_korea_leaders60_person57'],
      'reason_not_included':'Kyunghyang 2005 has complete field/person aggregate longitudinal metrics but no single normalized 57-person row master yet.'
    }
    payload={'schema_version':'typeA_common_longitudinal_rows_v0.2','generated':'2026-08-18','status':'flat_row_master_3_cohorts_5_windows','metrics_ref':'data/typeA/typeA_common_longitudinal_metrics_v0_1.json','qa':qa,'rows':rows}
    freeze={'schema_version':'typeA_common_longitudinal_rows_freeze_v0.2','generated':'2026-08-18','qa':qa,'sources':[str(K04.relative_to(ROOT)),str(D10.relative_to(ROOT)),str(D11.relative_to(ROOT))],'guardrails':['one row equals one cohort-placement x fixed-window snapshot','same person in different cohorts remains separate placement exposure','competing events and untraceable rows are null, not failures','explicit target-year aliases are not duplicated','Kyunghyang 2005 person57 is not silently pooled until row-normalized']}
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    FREEZE.write_text(json.dumps(freeze,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(freeze,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
