#!/usr/bin/env python3
import json
from pathlib import Path
from statistics import mean

ROOT=Path(__file__).resolve().parents[1]
AUDIT=ROOT/'research/khan_2005_socialedu_person9_peak_audit_v0_1.json'
REC=ROOT/'research/khan_2005_korea_leaders60_recovery_v0_1.json'
OUT=ROOT/'data/typeA/khan_2005_socialedu_person9_peak_master_v1_0.json'
METRICS=ROOT/'data/typeA/khan_2005_socialedu_person9_metrics_v1_0.json'
FREEZE=ROOT/'state/khan_2005_socialedu_person9_freeze_v1_0.json'


def main():
    a=json.loads(AUDIT.read_text(encoding='utf-8'))
    r=json.loads(REC.read_text(encoding='utf-8'))
    people=a['people']
    field=[u for u in r['units'] if u['field']=='사회교육']
    persons=[u for u in field if u['unit_type']=='person']
    orgs=[u for u in field if u['unit_type']=='organization']
    assert len(field)==10 and len(persons)==9 and len(orgs)==1
    assert orgs[0]['canonical_name']=='경제정의실천시민연합'
    assert {u['canonical_name'] for u in persons}=={p['name'] for p in people}
    assert len(people)==9 and len({p['name'] for p in people})==9
    q=a['qa']
    assert q['baseline_distribution']=={'2':3,'3':5,'4':1}
    assert abs(mean(p['baseline_peak_through_t0'] for p in people)-25/9)<1e-12
    assert q['post_peak_distribution']=={'3':4,'4':5}
    assert abs(mean(p['post_t0_peak_score'] for p in people)-32/9)<1e-12
    assert sum(p['post_t0_peak_score']>=3 for p in people)==9
    assert sum(p['post_t0_peak_score']==4 for p in people)==5
    assert sum(p['advancement_class']=='advanced' for p in people)==4
    assert sum(p['advancement_class']=='sustained_high' for p in people)==5

    rows=[]
    for p in people:
        x=dict(p)
        x.update({
          'outlet':'경향신문','selection_date':'2005-12-15','publication_date':'2005-12-30',
          'cohort_unit':'khan_2005_korea_leaders60_socialedu_person9','list_title':'한국을 이끌 60인 — 사회교육 person9',
          'domain':'social_education_public','design':'multistage_public_awareness_expert_final_field10_mixed_unit',
          'selection_mechanism':'1168_initial_to_185_expert_recommendation_to_public1266_to_final_expert12',
          'parent_selection':'khan_2005_korea_leaders60','parent_selected_units':60,'field_selected_units':10,
          'field_person_units':9,'field_organization_units':1,'excluded_other_unit_type':'경제정의실천시민연합',
          'field_specific_secondary':True,'unit_type_secondary':'person',
          'major_ge3':p['post_t0_peak_score']>=3,'apex_eq4':p['post_t0_peak_score']==4
        })
        rows.append(x)

    metrics={
      'schema_version':'khan_2005_socialedu_person9_metrics_v1.0','generated':'2026-08-18',
      'population':{'person_n':9,'assessable_person_n':9,'field_selected_units':10,'field_person_units':9,
                    'field_organization_units':1,'organization_unit':'경제정의실천시민연합','parent_selected_units':60,
                    'field_specific_secondary':True,'unit_type_secondary':'person'},
      'baseline':{'mean':25/9,'distribution':{'2':3,'3':5,'4':1}},
      'post_peak':{'mean':32/9,'distribution':{'3':4,'4':5}},
      'outcomes':{'major_n':9,'major_rate':1.0,'apex_n':5,'apex_rate':5/9,'advanced_n':4,'advanced_rate':4/9,
                  'sustained_high_n':5,'sustained_high_rate':5/9,'no_clear_advancement_n':0,
                  'lower_than_baseline_n':0,'not_assessable_n':0},
      'apex_names':['김상조','이종욱','정운찬','조국','하승창'],
      'advanced_names':['김상조','정운찬','조국','하승창'],
      'sustained_high_names':['김영란','김영무','박원순','안재규','이종욱'],
      'death_truncated_names':['박원순','이종욱'],
      'guardrails':a['interpretation_guardrails']
    }
    master={'schema_version':'khan_2005_socialedu_person9_peak_master_v1.0','generated':'2026-08-18',
      'status':'field_mixed_unit_person_subset_peak_audited_9_of_9',
      'cohort':{'publication':'경향신문','selection_cutoff':'2005-12-15','publication_date':'2005-12-30',
                'title':'한국을 이끌 60인 — 사회교육 person9','cohort_type':'A','domain':'social_education_public',
                'person_n':9,'field_selected_units':10,'field_organization_unit':'경제정의실천시민연합',
                'parent_selection':'khan_2005_korea_leaders60','parent_selected_units':60,
                'field_specific_secondary':True,'unit_type_secondary':'person',
                'design':'multistage_public_awareness_expert_final_field10_mixed_unit'},
      'metrics':metrics,'people':rows,'source_audit':str(AUDIT.relative_to(ROOT))}
    freeze={'schema_version':'khan_2005_socialedu_person9_freeze_v1.0','generated':'2026-08-18',
      'population':metrics['population'],'baseline':metrics['baseline'],'post_peak':metrics['post_peak'],
      'outcomes':metrics['outcomes'],'apex_names':metrics['apex_names'],'advanced_names':metrics['advanced_names'],
      'sustained_high_names':metrics['sustained_high_names'],'death_truncated_names':metrics['death_truncated_names'],
      'guardrails':metrics['guardrails']}
    OUT.write_text(json.dumps(master,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    METRICS.write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    FREEZE.write_text(json.dumps(freeze,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(freeze,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
