#!/usr/bin/env python3
import json
from pathlib import Path
from statistics import mean

ROOT=Path(__file__).resolve().parents[1]
AUDIT=ROOT/'research/khan_2005_politics10_peak_audit_v0_1.json'
REC=ROOT/'research/khan_2005_korea_leaders60_recovery_v0_1.json'
OUT=ROOT/'data/typeA/khan_2005_politics10_peak_master_v1_0.json'
METRICS=ROOT/'data/typeA/khan_2005_politics10_metrics_v1_0.json'
FREEZE=ROOT/'state/khan_2005_politics10_freeze_v1_0.json'


def main():
    a=json.loads(AUDIT.read_text(encoding='utf-8'))
    r=json.loads(REC.read_text(encoding='utf-8'))
    people=a['people']
    pol=[u for u in r['units'] if u['field']=='정치']
    assert len(pol)==10 and all(u['unit_type']=='person' for u in pol)
    assert {u['canonical_name'] for u in pol}=={p['name'] for p in people}
    assert len(people)==10 and len({p['name'] for p in people})==10

    q=a['qa']
    assert q['baseline_distribution']=={'2':4,'3':6}
    assert abs(mean(p['baseline_peak_through_t0'] for p in people)-2.6)<1e-12
    assert q['post_peak_distribution']=={'3':5,'4':5}
    assert abs(mean(p['post_t0_peak_score'] for p in people)-3.5)<1e-12
    assert sum(p['post_t0_peak_score']>=3 for p in people)==10
    assert sum(p['post_t0_peak_score']==4 for p in people)==5
    assert sum(p['advancement_class']=='advanced' for p in people)==8
    assert sum(p['advancement_class']=='sustained_high' for p in people)==2
    assert sorted(p['name'] for p in people if p['post_t0_peak_score']==4)==['김부겸','박근혜','손학규','이명박','정동영']
    assert sorted(p['name'] for p in people if p['advancement_class']=='sustained_high')==['강금실','김근태']
    assert sorted(p['name'] for p in people if p.get('death_truncated'))==['김근태','노회찬']

    rows=[]
    for p in people:
        x=dict(p)
        x.update({
          'outlet':'경향신문','selection_date':'2005-12-15','publication_date':'2005-12-30',
          'cohort_unit':'khan_2005_korea_leaders60_politics10',
          'list_title':'한국을 이끌 60인 — 정치10','domain':'politics',
          'design':'multistage_public_awareness_expert_final_field10',
          'selection_mechanism':'1168_initial_to_185_expert_recommendation_to_public1266_to_final_expert12',
          'parent_selection':'khan_2005_korea_leaders60','parent_selected_units':60,
          'field_specific_secondary':True,
          'major_ge3':p['post_t0_peak_score']>=3,'apex_eq4':p['post_t0_peak_score']==4
        })
        rows.append(x)

    metrics={
      'schema_version':'khan_2005_politics10_metrics_v1.0','generated':'2026-08-18',
      'population':{'n':10,'assessable_n':10,'parent_selected_units':60,'field_specific_secondary':True},
      'baseline':{'mean':2.6,'distribution':{'2':4,'3':6}},
      'post_peak':{'mean':3.5,'distribution':{'3':5,'4':5}},
      'outcomes':{
        'major_n':10,'major_rate':1.0,'apex_n':5,'apex_rate':0.5,
        'advanced_n':8,'advanced_rate':0.8,'sustained_high_n':2,'sustained_high_rate':0.2,
        'lower_than_baseline_n':0,'not_assessable_n':0
      },
      'apex_names':['김부겸','박근혜','손학규','이명박','정동영'],
      'sustained_high_names':['강금실','김근태'],
      'death_truncated_names':['김근태','노회찬'],
      'guardrails':a['interpretation_guardrails']
    }
    master={
      'schema_version':'khan_2005_politics10_peak_master_v1.0','generated':'2026-08-18',
      'status':'field_specific_peak_audited_10_of_10',
      'cohort':{
        'publication':'경향신문','selection_cutoff':'2005-12-15','publication_date':'2005-12-30',
        'title':'한국을 이끌 60인 — 정치10','cohort_type':'A','domain':'politics',
        'n':10,'parent_selection':'khan_2005_korea_leaders60','parent_selected_units':60,
        'field_specific_secondary':True,
        'design':'multistage_public_awareness_expert_final_field10'
      },
      'metrics':metrics,'people':rows,
      'source_audit':str(AUDIT.relative_to(ROOT))
    }
    freeze={
      'schema_version':'khan_2005_politics10_freeze_v1.0','generated':'2026-08-18',
      'population':metrics['population'],'baseline':metrics['baseline'],'post_peak':metrics['post_peak'],
      'outcomes':metrics['outcomes'],'apex_names':metrics['apex_names'],
      'sustained_high_names':metrics['sustained_high_names'],'death_truncated_names':metrics['death_truncated_names'],
      'guardrails':metrics['guardrails']
    }
    OUT.write_text(json.dumps(master,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    METRICS.write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    FREEZE.write_text(json.dumps(freeze,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(freeze,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
