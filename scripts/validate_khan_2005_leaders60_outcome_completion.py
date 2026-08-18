#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
P57=ROOT/'data/typeA/khan_2005_korea_leaders60_person57_metrics_v1_0.json'
COMP=ROOT/'research/khan_2005_korea_leaders60_outcome_completion_v1_0.json'
ORG=ROOT/'research/khan_2005_organizations_outcome_audit_v0_1.json'
CORR=ROOT/'research/khan_2005_recovery_identity_correction_v0_1.json'
FIELD_METRICS=[
    ROOT/'data/typeA/khan_2005_politics10_metrics_v1_0.json',
    ROOT/'data/typeA/khan_2005_economy_person9_metrics_v1_0.json',
    ROOT/'data/typeA/khan_2005_scitech_person9_metrics_v1_0.json',
    ROOT/'data/typeA/khan_2005_socialedu_person9_metrics_v1_0.json',
    ROOT/'data/typeA/khan_2005_popculture10_metrics_v1_0.json',
    ROOT/'data/typeA/khan_2005_cultureart10_metrics_v1_0.json',
]


def main():
    p=json.loads(P57.read_text(encoding='utf-8'))
    c=json.loads(COMP.read_text(encoding='utf-8'))
    o=json.loads(ORG.read_text(encoding='utf-8'))
    x=json.loads(CORR.read_text(encoding='utf-8'))
    fm=[json.loads(q.read_text(encoding='utf-8')) for q in FIELD_METRICS]

    assert c['status']=='all_60_selected_units_outcome_resolved_by_unit_type'
    assert c['original_selected_units']==60
    assert c['unit_composition']=={'persons':57,'organizations':3}
    assert c['qa']['resolved_total']==60 and c['qa']['completion_rate']==1.0
    assert c['qa']['single_cross_unit_type_success_rate_generated'] is False

    # Field composition: 10 each, total 60.
    assert len(c['field_status'])==6
    assert all(v['selected_units']==10 and v['resolved_units']==10 for v in c['field_status'].values())
    assert sum(v['persons'] for v in c['field_status'].values())==57
    assert sum(v['organizations'] for v in c['field_status'].values())==3

    # Person-only field metrics must add exactly to person57 secondary.
    def pop_n(m):
        z=m['population']
        return z.get('n',z.get('person_n'))
    n=sum(pop_n(m) for m in fm)
    major=sum(m['outcomes']['major_n'] for m in fm)
    apex=sum(m['outcomes']['apex_n'] for m in fm)
    adv=sum(m['outcomes']['advanced_n'] for m in fm)
    sustained=sum(m['outcomes']['sustained_high_n'] for m in fm)
    no_clear=sum(m['outcomes'].get('no_clear_advancement_n',0) for m in fm)
    lower=sum(m['outcomes'].get('lower_than_baseline_n',0) for m in fm)
    assert (n,major,apex,adv,sustained,no_clear,lower)==(57,53,24,24,29,3,1)
    assert adv+sustained+no_clear+lower==57
    assert p['analysis_denominator']==57 and p['original_selected_units']==60
    assert (p['outcomes']['major_n'],p['outcomes']['apex_n'],p['outcomes']['advanced_n'])==(53,24,24)
    assert abs(p['baseline']['mean']-162/57)<1e-12
    assert abs(p['post_peak']['mean']-191/57)<1e-12

    # Organizations are complete but remain on their own trajectory schema.
    assert set(c['organization3'])=={'outcome_ref','NHN','한국공학교육인증원','경제정의실천시민연합'}
    assert c['organization3']['NHN']['continuity_class']=='branched_continuity'
    assert c['organization3']['한국공학교육인증원']['t20_trajectory']=='expanded'
    assert c['organization3']['경제정의실천시민연합']['t20_trajectory']=='sustained_high'
    assert o['qa']['audited_organization_n']==3

    # Identity correction must remain explicit.
    assert x['affected_printed_name']=='임지선'
    assert x['incorrect_prior_anchor']=='바이올리니스트'
    assert x['correct_identity']['identity_anchor']=='작곡가/연세대학교 작곡과 교수'
    assert c['identity_corrections'][0]['correct_anchor']=='작곡가/연세대학교 작곡과 교수'

    print(json.dumps({
        'status':'PASS',
        'selected_units':60,
        'person_units':57,
        'organization_units':3,
        'person_major_n':53,
        'person_apex_n':24,
        'person_advanced_n':24,
        'single_cross_unit_type_success_rate':False
    },ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
