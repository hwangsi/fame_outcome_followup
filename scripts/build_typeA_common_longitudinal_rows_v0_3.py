#!/usr/bin/env python3
import json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'data/typeA/typeA_common_longitudinal_rows_v0_2.json'
K05=ROOT/'data/typeA/khan_2005_korea_leaders60_person57_common_longitudinal_rows_v0_1.json'
OUT=ROOT/'data/typeA/typeA_common_longitudinal_rows_v0_3.json'
FREEZE=ROOT/'state/typeA_common_longitudinal_rows_freeze_v0_3.json'


def main():
    b=json.loads(BASE.read_text(encoding='utf-8'))
    k=json.loads(K05.read_text(encoding='utf-8'))
    assert b['qa']['snapshot_rows']==260 and b['qa']['row_ready_selected_placements']==220
    assert k['qa']['persons']==57 and k['qa']['snapshot_rows']==114
    rows=[dict(r) for r in b['rows']]+[dict(r) for r in k['rows']]
    assert len(rows)==374
    assert len({r['snapshot_id'] for r in rows})==374
    cells=Counter((r['cohort_unit'],r['window_id']) for r in rows)
    expected={
      ('khan_2004_17th_assembly_newleaders_20','t10'):20,
      ('khan_2004_17th_assembly_newleaders_20','t20'):20,
      ('khan_2004_17th_assembly_newleaders_20','current'):20,
      ('khan_2005_korea_leaders60_person57','t10'):57,
      ('khan_2005_korea_leaders60_person57','t20'):57,
      ('donga_2010_2020_100','t10'):100,
      ('donga_2011_10yr_100','t10'):100,
    }
    assert cells==expected,cells
    def rr(unit,w): return [r for r in rows if r['cohort_unit']==unit and r['window_id']==w]
    k10=rr('khan_2005_korea_leaders60_person57','t10')
    k20=rr('khan_2005_korea_leaders60_person57','t20')
    assert sum(r['status']=='assessable' for r in k10)==54
    assert sum(r['major_ge3'] is True for r in k10)==27
    assert sum(r['apex_eq4'] is True for r in k10)==3
    assert sum(r['status']=='assessable' for r in k20)==52
    assert sum(r['scope_ge2'] is True for r in k20)==43
    assert sum(r['major_ge3'] is True for r in k20)==26
    assert sum(r['apex_eq4'] is True for r in k20)==10
    rows.sort(key=lambda r:(r['selection_year'],r['cohort_unit'],r['window_id'],r['name']))
    qa={
      'snapshot_rows':374,'unique_snapshot_ids':374,'cohort_units':4,'cohort_window_cells':7,
      'row_ready_selected_placements':277,
      'by_cohort':{
        'khan_2004_17th_assembly_newleaders_20':{'selected_person_placements':20,'snapshot_rows':60,'windows':['t10','t20','current']},
        'khan_2005_korea_leaders60_person57':{'selected_person_placements':57,'snapshot_rows':114,'windows':['t10','t20'],'secondary_of_mixed_60_unit_selection':True},
        'donga_2010_2020_100':{'selected_person_placements':100,'snapshot_rows':100,'windows':['t10']},
        'donga_2011_10yr_100':{'selected_person_placements':100,'snapshot_rows':100,'windows':['t10']}
      },
      'khan_2005_corrected_t20':{'assessable_n':52,'scope_ge2_n':43,'major_ge3_n':26,'apex_eq4_n':10},
      'remaining_completed_metric_only_cohorts':[]
    }
    payload={'schema_version':'typeA_common_longitudinal_rows_v0.3','generated':'2026-08-18','status':'flat_row_master_4_cohorts_7_windows_corrected_khan2005','qa':qa,'rows':rows}
    freeze={'schema_version':'typeA_common_longitudinal_rows_freeze_v0.3','generated':'2026-08-18','qa':qa,'sources':[str(BASE.relative_to(ROOT)),str(K05.relative_to(ROOT))],'supersedes':'state/typeA_common_longitudinal_rows_freeze_v0_2.json','guardrails':['one row equals one cohort-placement x fixed-window snapshot','Kyunghyang 2005 person57 is a secondary person-only analysis of a mixed 60-unit selection','organization units remain excluded from person-scope row master','same person selected in different cohorts remains separate placement exposure','competing events and untraceable rows remain null rather than failure scores','Kyunghyang 2005 T20 uses corrected Shin Hee-sup retirement coding']}
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    FREEZE.write_text(json.dumps(freeze,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(freeze,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
