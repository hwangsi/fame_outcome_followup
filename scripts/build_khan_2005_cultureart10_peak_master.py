#!/usr/bin/env python3
import json
from pathlib import Path
from statistics import mean

ROOT=Path(__file__).resolve().parents[1]
AUDIT=ROOT/'research/khan_2005_cultureart10_peak_audit_v0_1.json'
REC=ROOT/'research/khan_2005_korea_leaders60_recovery_v0_1.json'
CORR=ROOT/'research/khan_2005_recovery_identity_correction_v0_1.json'
OUT=ROOT/'data/typeA/khan_2005_cultureart10_peak_master_v1_0.json'
METRICS=ROOT/'data/typeA/khan_2005_cultureart10_metrics_v1_0.json'
FREEZE=ROOT/'state/khan_2005_cultureart10_freeze_v1_0.json'


def main():
    a=json.loads(AUDIT.read_text(encoding='utf-8'))
    r=json.loads(REC.read_text(encoding='utf-8'))
    c=json.loads(CORR.read_text(encoding='utf-8'))
    people=a['people']
    field=[u for u in r['units'] if u['field']=='문화예술']
    assert len(field)==10 and all(u['unit_type']=='person' for u in field)
    assert {u['canonical_name'] for u in field}=={p['name'] for p in people}
    assert c['affected_printed_name']=='임지선'
    assert c['correct_identity']['identity_anchor']=='작곡가/연세대학교 작곡과 교수'
    lim=[p for p in people if p['name']=='임지선'][0]
    assert lim['identity_key']=='임지선|composer' and '작곡가' in lim['identity_anchor']
    q=a['qa']
    assert q['baseline_distribution']=={'2':3,'3':6,'4':1}
    assert abs(mean(p['baseline_peak_through_t0'] for p in people)-2.8)<1e-12
    assert q['post_peak_distribution']=={'2':1,'3':7,'4':2}
    assert abs(mean(p['post_t0_peak_score'] for p in people)-3.1)<1e-12
    assert sum(p['post_t0_peak_score']>=3 for p in people)==9
    assert sum(p['post_t0_peak_score']==4 for p in people)==2
    assert sum(p['advancement_class']=='advanced' for p in people)==3
    assert sum(p['advancement_class']=='sustained_high' for p in people)==6
    assert sum(p['advancement_class']=='no_clear_advancement' for p in people)==1

    rows=[]
    for p in people:
        x=dict(p)
        x.update({'outlet':'경향신문','selection_date':'2005-12-15','publication_date':'2005-12-30',
          'cohort_unit':'khan_2005_korea_leaders60_cultureart10','list_title':'한국을 이끌 60인 — 문화예술10',
          'domain':'culture_arts','design':'multistage_public_awareness_expert_final_field10',
          'selection_mechanism':'1168_initial_to_185_expert_recommendation_to_public1266_to_final_expert12',
          'parent_selection':'khan_2005_korea_leaders60','parent_selected_units':60,'field_selected_units':10,
          'field_person_units':10,'field_organization_units':0,'field_specific_secondary':True,
          'major_ge3':p['post_t0_peak_score']>=3,'apex_eq4':p['post_t0_peak_score']==4})
        rows.append(x)
    metrics={'schema_version':'khan_2005_cultureart10_metrics_v1.0','generated':'2026-08-18',
      'population':{'n':10,'assessable_n':10,'parent_selected_units':60,'field_selected_units':10,'field_specific_secondary':True},
      'baseline':{'mean':2.8,'distribution':{'2':3,'3':6,'4':1}},
      'post_peak':{'mean':3.1,'distribution':{'2':1,'3':7,'4':2}},
      'outcomes':{'major_n':9,'major_rate':0.9,'apex_n':2,'apex_rate':0.2,'advanced_n':3,'advanced_rate':0.3,
                  'sustained_high_n':6,'sustained_high_rate':0.6,'no_clear_advancement_n':1,'lower_than_baseline_n':0,'not_assessable_n':0},
      'apex_names':['이불','조수미'],'advanced_names':['이불','김연수','서재형'],
      'sustained_high_names':['강충모','남경주','전광영','조수미','김홍희','윤호진'],
      'no_clear_advancement_names':['임지선'],'identity_correction_ref':a['identity_correction_ref'],
      'guardrails':a['interpretation_guardrails']}
    master={'schema_version':'khan_2005_cultureart10_peak_master_v1.0','generated':'2026-08-18','status':'field_peak_audited_10_of_10',
      'cohort':{'publication':'경향신문','selection_cutoff':'2005-12-15','publication_date':'2005-12-30','title':'한국을 이끌 60인 — 문화예술10',
                'cohort_type':'A','domain':'culture_arts','n':10,'parent_selection':'khan_2005_korea_leaders60','parent_selected_units':60,
                'field_specific_secondary':True,'design':'multistage_public_awareness_expert_final_field10'},
      'metrics':metrics,'people':rows,'source_audit':str(AUDIT.relative_to(ROOT)),'identity_correction_ref':a['identity_correction_ref']}
    freeze={'schema_version':'khan_2005_cultureart10_freeze_v1.0','generated':'2026-08-18','population':metrics['population'],
      'baseline':metrics['baseline'],'post_peak':metrics['post_peak'],'outcomes':metrics['outcomes'],'apex_names':metrics['apex_names'],
      'advanced_names':metrics['advanced_names'],'sustained_high_names':metrics['sustained_high_names'],
      'no_clear_advancement_names':metrics['no_clear_advancement_names'],'identity_correction_ref':metrics['identity_correction_ref'],
      'guardrails':metrics['guardrails']}
    OUT.write_text(json.dumps(master,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    METRICS.write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    FREEZE.write_text(json.dumps(freeze,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(freeze,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
