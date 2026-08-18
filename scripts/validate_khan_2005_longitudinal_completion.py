#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

FILES={
 'politics': ROOT/'data/typeA/khan_2005_politics10_longitudinal_metrics_v1_0.json',
 'economy': ROOT/'data/typeA/khan_2005_economy_person9_longitudinal_metrics_v1_0.json',
 'scitech': ROOT/'data/typeA/khan_2005_scitech_person9_longitudinal_metrics_v1_0.json',
 'socialedu': ROOT/'data/typeA/khan_2005_socialedu_person9_longitudinal_metrics_v1_0.json',
 'popculture': ROOT/'data/typeA/khan_2005_popculture10_longitudinal_metrics_v1_0.json',
 'cultureart': ROOT/'data/typeA/khan_2005_cultureart10_longitudinal_metrics_v1_0.json',
 'person57': ROOT/'data/typeA/khan_2005_korea_leaders60_person57_longitudinal_metrics_v1_0.json',
 'completion60': ROOT/'data/typeA/khan_2005_korea_leaders60_longitudinal_completion_v1_0.json',
 'orgs': ROOT/'research/khan_2005_organizations_outcome_audit_v0_1.json',
 'nhn_t10': ROOT/'research/khan_2005_nhn_t10_longitudinal_patch_v0_1.json',
 'abeek_t10': ROOT/'research/khan_2005_abeek_t10_longitudinal_patch_v0_1.json',
 'ccej_t10': ROOT/'research/khan_2005_ccej_t10_longitudinal_patch_v0_1.json'
}

def load(path):
    return json.loads(path.read_text(encoding='utf-8'))

def main():
    d={k:load(v) for k,v in FILES.items()}

    # Original mixed-unit design is immutable.
    c=d['completion60']
    assert c['selection']['selected_units']==60
    assert c['selection']['person_units']==57
    assert c['selection']['organization_units']==3
    assert len(c['by_field'])==6
    assert all(v['selected_units']==10 for v in c['by_field'].values())

    # Field person denominators: 10 + 9 + 9 + 9 + 10 + 10 = 57.
    expected_person_n={'politics':10,'economy':9,'scitech':9,'socialedu':9,'popculture':10,'cultureart':10}
    for k,n in expected_person_n.items():
        m=d[k]
        pop=m['population']
        actual=pop.get('n',pop.get('person_n'))
        assert actual==n,(k,actual,n)

    # Aggregate fixed-window person distributions from field metrics.
    aggregate={w:{'0':0,'1':0,'2':0,'3':0,'4':0,'null':0} for w in ('t10','t20')}
    for k in expected_person_n:
        for w in ('t10','t20'):
            dist=d[k]['snapshots'][w]['score_distribution']
            for score in aggregate[w]:
                aggregate[w][score]+=dist.get(score,0)

    assert aggregate['t10']=={'0':0,'1':4,'2':23,'3':24,'4':3,'null':3},aggregate['t10']
    assert aggregate['t20']=={'0':0,'1':8,'2':17,'3':17,'4':10,'null':5},aggregate['t20']

    p=d['person57']
    assert p['snapshots']['t10']['score_distribution']==aggregate['t10']
    assert p['snapshots']['t20']['score_distribution']==aggregate['t20']
    assert p['snapshots']['t10']['assessable_n']==54
    assert p['snapshots']['t10']['competing_event_n']==3
    assert p['snapshots']['t10']['major_ge3_n']==27
    assert p['snapshots']['t10']['apex_eq4_n']==3
    assert p['snapshots']['t20']['assessable_n']==52
    assert p['snapshots']['t20']['competing_event_n']==5
    assert p['snapshots']['t20']['major_ge3_n']==27
    assert p['snapshots']['t20']['apex_eq4_n']==10
    assert p['death_truncated_names']==['김근태','노회찬','박원순','이종욱','김종학']

    # Organization architecture stays separate at both windows.
    assert d['orgs']['qa']['organization_n']==3
    assert d['nhn_t10']['t10']['continuity_class']=='branched_continuity'
    assert d['abeek_t10']['t10']['continuity_class']=='direct_continuity'
    assert d['ccej_t10']['t10']['continuity_class']=='direct_continuity'
    assert d['abeek_t10']['t10']['trajectory']=='expanded'
    assert d['ccej_t10']['t10']['trajectory']=='sustained_high'
    assert c['qa']['t10_total_unit_outcome_paths']==60
    assert c['qa']['t20_total_unit_outcome_paths']==60
    assert c['qa']['single_60_unit_numeric_success_rate_created'] is False
    assert c['qa']['person_and_organization_architectures_separate'] is True

    print('PASS: Kyunghyang 2005 longitudinal completion QA')
    print('T+10 person57:', aggregate['t10'])
    print('T+20 person57:', aggregate['t20'])
    print('60/60 unit-type outcome paths complete at both windows')

if __name__=='__main__':
    main()
