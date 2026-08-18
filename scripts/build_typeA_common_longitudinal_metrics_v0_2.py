#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ROWS=ROOT/'data/typeA/typeA_common_longitudinal_rows_v0_3.json'
OUT=ROOT/'data/typeA/typeA_common_longitudinal_metrics_v0_2.json'
FREEZE=ROOT/'state/typeA_common_longitudinal_metrics_freeze_v0_2.json'

META={
 'khan_2004_17th_assembly_newleaders_20':{'outlet':'경향신문','unit_scope':'persons','original_n':20,'source_ref':'data/typeA/khan_2004_17th_assembly_newleaders_longitudinal_master_v1_0.json'},
 'khan_2005_korea_leaders60_person57':{'outlet':'경향신문','unit_scope':'person-only secondary from mixed 60-unit selection','original_parent_units':60,'person_n':57,'organization_n_excluded_from_person_metrics':3,'source_ref':'state/khan_2005_korea_leaders60_person57_longitudinal_freeze_v1_1.json'},
 'donga_2010_2020_100':{'outlet':'동아일보','unit_scope':'persons','original_n':100,'source_ref':'data/typeA/donga_2010_common_longitudinal_rows_v0_1.json','explicit_target_alias':'explicit_target_2020'},
 'donga_2011_10yr_100':{'outlet':'동아일보','unit_scope':'persons','original_n':100,'source_ref':'data/typeA/donga_2011_common_longitudinal_rows_v0_1.json'}
}

def metric(rr):
    ass=[r for r in rr if r['status']=='assessable']; n=len(ass)
    out={'assessable_n':n,'competing_event_n':sum(r['status']=='competing_event' for r in rr),'untraceable_n':sum(r['status']=='untraceable' for r in rr),'scope_ge2_n':sum(r['scope_ge2'] is True for r in rr),'major_ge3_n':sum(r['major_ge3'] is True for r in rr),'apex_eq4_n':sum(r['apex_eq4'] is True for r in rr)}
    for key in ['scope_ge2','major_ge3','apex_eq4']:
        out[key+'_rate']=out[key+'_n']/n if n else None
    return out

def main():
    d=json.loads(ROWS.read_text(encoding='utf-8')); rows=d['rows']
    assert d['qa']['snapshot_rows']==374
    cohorts={}
    for unit,meta in META.items():
        c=dict(meta)
        for w in ['t10','t20']:
            rr=[r for r in rows if r['cohort_unit']==unit and r['window_id']==w]
            if rr: c[w]=metric(rr)
        cohorts[unit]=c
    k05=cohorts['khan_2005_korea_leaders60_person57']
    assert k05['t10']['assessable_n']==54 and k05['t10']['major_ge3_n']==27
    assert k05['t20']['assessable_n']==52 and k05['t20']['scope_ge2_n']==43 and k05['t20']['major_ge3_n']==26 and k05['t20']['apex_eq4_n']==10
    assert cohorts['donga_2010_2020_100']['t10']['major_ge3_n']==42
    assert cohorts['donga_2011_10yr_100']['t10']['major_ge3_n']==63
    keys={'khan_2004_17th_assembly_newleaders_20':'khan_2004','khan_2005_korea_leaders60_person57':'khan_2005_person57','donga_2010_2020_100':'donga_2010','donga_2011_10yr_100':'donga_2011'}
    cross={}
    for metric_name in ['scope_ge2','major_ge3','apex_eq4']:
        cross[metric_name+'_rates']={keys[u]:cohorts[u]['t10'][metric_name+'_rate'] for u in keys}
    cross['warning']='Descriptive only. Cohorts differ in selection year, design, sector mix, baseline prestige, denominator and target calendar year.'
    payload={'schema_version':'typeA_common_longitudinal_metrics_v0.2','generated':'2026-08-18','status':'row_derived_corrected_after_khan2005_scitech_retirement','row_master_ref':str(ROWS.relative_to(ROOT)),'cohorts':cohorts,'cross_cohort_t10_descriptive':cross,'correction_from_v0_1':{'cohort':'khan_2005_korea_leaders60_person57','window':'t20','scope_ge2_n':{'old':44,'new':43},'major_ge3_n':{'old':27,'new':26},'scope_ge2_rate':{'old':0.8461538462,'new':43/52},'major_ge3_rate':{'old':0.5192307692,'new':0.5},'reason':'Shin Hee-sup T20 retirement correction changed science-tech scope3 to scope1; v0.1 common metrics predated aggregate regeneration.'},'key_pattern':'T+10 broad establishment remains high across all four completed row-ready cohorts, while Major occupancy varies substantially; T+20 estimates are available for both Kyunghyang cohorts and must use corrected K05 values.','guardrails':['Metrics are derived from the frozen row-level common master, not manually copied field totals.','Do not pool person and organization snapshot scores.','Do not treat repeated people across cohorts as independent observations.','Competing events and untraceable rows are excluded from assessable denominators.','Lifetime peak and fixed-window occupancy remain separate outcomes.']}
    freeze={'schema_version':'typeA_common_longitudinal_metrics_freeze_v0.2','generated':'2026-08-18','row_master_ref':str(ROWS.relative_to(ROOT)),'qa':{'cohort_units':4,'t10_cohorts':4,'t20_cohorts':2,'khan_2005_t20_scope_ge2_n':43,'khan_2005_t20_major_ge3_n':26},'supersedes':'data/typeA/typeA_common_longitudinal_metrics_v0_1.json','metrics_ref':str(OUT.relative_to(ROOT))}
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    FREEZE.write_text(json.dumps(freeze,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(freeze,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
