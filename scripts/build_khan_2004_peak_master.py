#!/usr/bin/env python3
import json
from pathlib import Path
from statistics import mean

ROOT=Path(__file__).resolve().parents[1]
ROSTER=ROOT/'research/khan_2004_17th_assembly_newleaders_roster_v0_1.json'
B1=ROOT/'research/khan_2004_peak_audit_uri_batch1_v0_1.json'
B2=ROOT/'research/khan_2004_peak_audit_gnp_dlp_batch2_v0_1.json'
OUT=ROOT/'data/typeA/khan_2004_17th_assembly_newleaders_peak_master_v1_0.json'
METRICS=ROOT/'data/typeA/khan_2004_17th_assembly_newleaders_metrics_v1_0.json'
FREEZE=ROOT/'state/khan_2004_17th_assembly_newleaders_freeze_v1_0.json'


def main():
    r=json.loads(ROSTER.read_text(encoding='utf-8'))
    b1=json.loads(B1.read_text(encoding='utf-8'))
    b2=json.loads(B2.read_text(encoding='utf-8'))
    roster={p['name']:p for p in r['people']}
    audit=b1['people']+b2['people']
    assert len(roster)==20 and len(audit)==20
    assert set(roster)=={p['name'] for p in audit}

    people=[]
    for p in audit:
        rr=roster[p['name']]
        x=dict(p)
        x['selection_date']='2004-05-05'
        x['outlet']='경향신문'
        x['cohort_unit']='khan_2004_17th_assembly_newleaders_20'
        x['list_title']='17代국회 이끌 뉴리더'
        x['design']='expert_vote_party_quota_top20'
        x['selection_mechanism']='expert_panel_vote_party_quota'
        x['domain']='politics'
        x['vote_count']=rr.get('vote_count')
        x['series_order']=rr.get('series_order')
        x['major_ge3']=x['post_t0_peak_score']>=3
        x['apex_eq4']=x['post_t0_peak_score']==4
        people.append(x)

    assert len({p['name'] for p in people})==20
    assert sum(p['advancement_class']=='advanced' for p in people)==19
    assert [p['name'] for p in people if p['advancement_class']=='lower_than_baseline']==['박세일']
    assert sum(p['apex_eq4'] for p in people)==4
    assert sorted(p['name'] for p in people if p['apex_eq4'])==['김부겸','김문수','임종석','한명숙']

    metrics={
      'schema_version':'khan_2004_17th_assembly_newleaders_metrics_v1.0',
      'generated':'2026-08-18',
      'population':{'n':20,'assessable_n':20},
      'baseline':{
        'mean':mean(p['baseline_peak_through_t0'] for p in people),
        'distribution':{str(s):sum(p['baseline_peak_through_t0']==s for p in people) for s in range(5)}
      },
      'post_peak':{
        'mean':mean(p['post_t0_peak_score'] for p in people),
        'distribution':{str(s):sum(p['post_t0_peak_score']==s for p in people) for s in range(5)}
      },
      'outcomes':{
        'major_n':sum(p['major_ge3'] for p in people),'major_rate':sum(p['major_ge3'] for p in people)/20,
        'apex_n':sum(p['apex_eq4'] for p in people),'apex_rate':sum(p['apex_eq4'] for p in people)/20,
        'advanced_n':sum(p['advancement_class']=='advanced' for p in people),'advanced_rate':sum(p['advancement_class']=='advanced' for p in people)/20,
        'sustained_high_n':sum(p['advancement_class']=='sustained_high' for p in people),
        'no_clear_advancement_n':sum(p['advancement_class']=='no_clear_advancement' for p in people),
        'lower_than_baseline_n':sum(p['advancement_class']=='lower_than_baseline' for p in people)
      },
      'apex_names':sorted(p['name'] for p in people if p['apex_eq4']),
      'non_advanced_names':sorted(p['name'] for p in people if p['advancement_class']!='advanced'),
      'near_immediate_advancement_flags':['신기남'],
      'guardrails':[
        'All 20 were already elected to the 17th National Assembly; raw major attainment has severe baseline ceiling and is not the primary future-rise metric.',
        'The selection explicitly targeted future political leaders, so baseline-adjusted advancement is the primary descriptive outcome.',
        'Party quotas (10 Uri, 8 GNP, 2 DLP) are part of the selection design and must be retained in any comparison.',
        '신기남 reached national party chair 12 days after selection; count it after the frozen cutoff but flag likely imminence/short-horizon editorial information.',
        '박세일 baseline uses lifetime pre-selection presidential policy-chief peak (scope4), not his contemporaneous MP title.'
      ]
    }
    master={
      'schema_version':'khan_2004_17th_assembly_newleaders_peak_master_v1.0',
      'generated':'2026-08-18','status':'peak_audited_20_of_20',
      'cohort':{
        'publication':'경향신문','selection_date':'2004-05-05','title':'17代국회 이끌 뉴리더',
        'cohort_type':'A','domain':'politics','n':20,
        'design':'expert_vote_party_quota_top20','selection_mechanism':'expert_panel_vote_party_quota',
        'party_quota':{'열린우리당':10,'한나라당':8,'민주노동당':2},
        'expert_panel_n':40
      },
      'metrics':metrics,'people':people,
      'source_audits':[str(B1.relative_to(ROOT)),str(B2.relative_to(ROOT))]
    }
    freeze={
      'schema_version':'khan_2004_17th_assembly_newleaders_freeze_v1.0','generated':'2026-08-18',
      'population':metrics['population'],'baseline':metrics['baseline'],'post_peak':metrics['post_peak'],
      'outcomes':metrics['outcomes'],'apex_names':metrics['apex_names'],
      'non_advanced_names':metrics['non_advanced_names'],'near_immediate_advancement_flags':metrics['near_immediate_advancement_flags'],
      'guardrails':metrics['guardrails']
    }
    OUT.write_text(json.dumps(master,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    METRICS.write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    FREEZE.write_text(json.dumps(freeze,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(freeze,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
