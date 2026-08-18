#!/usr/bin/env python3
import csv, hashlib, json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean

from identity_resolution import resolve_identity_key, person_id_from_identity_key

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'data/typeA/typeA_common_master_v0_3.json'
KH=ROOT/'data/typeA/khan_2005_politics10_peak_master_v1_0.json'
AUDIT=ROOT/'research/khan_2005_politics10_identity_audit_v0_2.json'
OUTJ=ROOT/'data/typeA/typeA_common_master_v0_4.json'
OUTC=ROOT/'data/typeA/typeA_common_master_v0_4.csv'
OUTM=ROOT/'data/typeA/typeA_common_metrics_v0_4.json'
FREEZE=ROOT/'state/typeA_common_master_freeze_v0_4.json'


def placement_id(outlet,unit,name):
    return 'pl-'+hashlib.sha256(f'{outlet}|{unit}|{name}'.encode()).hexdigest()[:14]

def khrow(p):
    outlet='경향신문'; unit='khan_2005_korea_leaders60_politics10'
    ik=resolve_identity_key(p['name'],outlet,unit)
    return {'placement_id':placement_id(outlet,unit,p['name']),'person_id':person_id_from_identity_key(ik),'identity_key':ik,'legacy_person_id_v0_2':None,'name':p['name'],'outlet':outlet,'selection_date':'2005-12-15','selection_year':2005,'cohort_unit':unit,'list_title':'한국을 이끌 60인 — 정치10','design':'multistage_public_awareness_expert_final_field10','selection_mechanism':'1168_initial_to_185_expert_recommendation_to_public1266_to_final_expert12','domain':'politics','rank':None,'rank_known':False,'target_horizon':'2006-2020','selection_score':None,'selection_score_type':None,'series_order':None,'baseline_peak_through_t0':p['baseline_peak_through_t0'],'post_t0_peak_score':p['post_t0_peak_score'],'outcome_assessable':True,'advancement_delta':p['advancement_delta'],'advancement_class':p['advancement_class'],'major_ge3':p['post_t0_peak_score']>=3,'apex_eq4':p['post_t0_peak_score']==4,'death_truncated':bool(p.get('death_truncated',False)),'source_schema':'khan_2005_politics10_peak_master_v1_0','parent_selection':'khan_2005_korea_leaders60','parent_selected_units':60,'field_specific_secondary':True}

def summarize(rr):
    ass=[r for r in rr if r['outcome_assessable']]
    return {'n':len(rr),'assessable_n':len(ass),'unique_people':len({r['person_id'] for r in rr}),'design':rr[0]['design'],'selection_mechanism':rr[0]['selection_mechanism'],'outlet':rr[0]['outlet'],'baseline_mean':mean(r['baseline_peak_through_t0'] for r in rr),'post_peak_mean_assessable':mean(r['post_t0_peak_score'] for r in ass),'major_n':sum(r['major_ge3'] for r in rr),'major_rate_full':sum(r['major_ge3'] for r in rr)/len(rr),'apex_n':sum(r['apex_eq4'] for r in rr),'apex_rate_full':sum(r['apex_eq4'] for r in rr)/len(rr),'advanced_n':sum(r['advancement_class']=='advanced' for r in rr),'advanced_rate_full':sum(r['advancement_class']=='advanced' for r in rr)/len(rr),'not_assessable_n':sum(not r['outcome_assessable'] for r in rr),'field_specific_secondary':bool(rr[0].get('field_specific_secondary',False)),'parent_selection':rr[0].get('parent_selection')}

def main():
    base=json.loads(BASE.read_text(encoding='utf-8')); kh=json.loads(KH.read_text(encoding='utf-8')); audit=json.loads(AUDIT.read_text(encoding='utf-8'))
    assert base['qa']['placements']==245 and base['qa']['unique_people']==193 and base['qa']['unique_display_names']==192
    assert audit['qa']['same_existing_n']==10 and audit['qa']['new_person_n']==0
    base_by_name=defaultdict(list)
    for r in base['placements']: base_by_name[r['name']].append(r)
    expected={x['name'] for x in audit['same_person_existing']}
    assert expected=={p['name'] for p in kh['people']}
    # Every K05 politics person already exists as a canonical person in v0.3.
    for p in kh['people']:
        assert base_by_name[p['name']],p['name']
        k=khrow(p)
        assert any(r['person_id']==k['person_id'] and r['identity_key']==k['identity_key'] for r in base_by_name[p['name']]),p['name']
    rows=[dict(r) for r in base['placements']]+[khrow(p) for p in kh['people']]
    assert len(rows)==255 and len({r['placement_id'] for r in rows})==255
    assert len({r['person_id'] for r in rows})==193
    assert len({r['identity_key'] for r in rows})==193
    assert len({r['name'] for r in rows})==192
    lee=[r for r in rows if r['name']=='이미경']
    assert len(lee)==2 and {r['identity_key'] for r in lee}=={'이미경|cj_enm_business','이미경|politician'}
    by_pid=defaultdict(list)
    for r in rows: by_pid[r['person_id']].append(r)
    people=[]
    for pid,pp0 in by_pid.items():
        pp=sorted(pp0,key=lambda r:(r['selection_date'],r['outlet'],r['cohort_unit']))
        names={r['name'] for r in pp}; iks={r['identity_key'] for r in pp}; assert len(names)==1 and len(iks)==1
        ass=[r for r in pp if r['outcome_assessable']]
        people.append({'person_id':pid,'identity_key':next(iter(iks)),'name':next(iter(names)),'placement_count':len(pp),'outlets':sorted({r['outlet'] for r in pp}),'selection_years':[r['selection_year'] for r in pp],'cohort_units':[r['cohort_unit'] for r in pp],'designs':sorted({r['design'] for r in pp}),'first_selection_year':pp[0]['selection_year'],'last_selection_year':pp[-1]['selection_year'],'first_selection_baseline':pp[0]['baseline_peak_through_t0'],'first_selection_post_peak':pp[0]['post_t0_peak_score'],'first_selection_advancement_class':pp[0]['advancement_class'],'assessable_placement_n':len(ass),'ever_major_across_placements':any(r['major_ge3'] for r in ass),'ever_apex_across_placements':any(r['apex_eq4'] for r in ass),'ever_advanced_across_placements':any(r['advancement_class']=='advanced' for r in ass),'placements':[r['placement_id'] for r in pp]})
    people.sort(key=lambda p:(p['name'],p['identity_key']))
    dist=Counter(p['placement_count'] for p in people); repeated=[p for p in people if p['placement_count']>1]
    units={}
    for unit in dict.fromkeys(r['cohort_unit'] for r in rows): units[unit]=summarize([r for r in rows if r['cohort_unit']==unit])
    assert len(units)==7
    k5=units['khan_2005_korea_leaders60_politics10']; assert (k5['n'],k5['major_n'],k5['apex_n'],k5['advanced_n'])==(10,10,5,8)
    designs={}
    for design in sorted({r['design'] for r in rows}):
        rr=[r for r in rows if r['design']==design]
        designs[design]={'placements':len(rr),'unique_people':len({r['person_id'] for r in rr}),'major_n':sum(r['major_ge3'] for r in rr),'major_rate_full':sum(r['major_ge3'] for r in rr)/len(rr),'apex_n':sum(r['apex_eq4'] for r in rr),'apex_rate_full':sum(r['apex_eq4'] for r in rr)/len(rr),'advanced_n':sum(r['advancement_class']=='advanced' for r in rr),'advanced_rate_full':sum(r['advancement_class']=='advanced' for r in rr)/len(rr),'warning':'Descriptive only; year, domain, list depth and selection mechanism remain confounded.'}
    naive={'placements':255,'unique_people':193,'major_n':sum(r['major_ge3'] for r in rows),'major_rate':sum(r['major_ge3'] for r in rows)/255,'apex_n':sum(r['apex_eq4'] for r in rows),'apex_rate':sum(r['apex_eq4'] for r in rows)/255,'advanced_n':sum(r['advancement_class']=='advanced' for r in rows),'advanced_rate':sum(r['advancement_class']=='advanced' for r in rows)/255,'warning':'Descriptive only. Placements are not independent; Kyunghyang 2005 politics10 is a secondary field stratum of a mixed 60-unit selection.'}
    assert (naive['major_n'],naive['apex_n'],naive['advanced_n'])==(216,44,106)
    pf={'persons':193,'first_selection_major_n':sum((p['first_selection_post_peak'] or -1)>=3 for p in people),'first_selection_apex_n':sum(p['first_selection_post_peak']==4 for p in people),'first_selection_advanced_n':sum(p['first_selection_advancement_class']=='advanced' for p in people),'warning':'Person-level first-selection description; observation windows and cohort designs differ.'}
    qa={'placements':255,'unique_people':193,'unique_display_names':192,'true_homonym_split_n':1,'repeated_person_n':len(repeated),'placement_count_distribution':{str(k):v for k,v in sorted(dist.items())},'max_placement_count':max(dist),'max_selected_names':sorted(p['name'] for p in people if p['placement_count']==max(dist)),'cohort_units':7,'not_assessable_placements':sum(not r['outcome_assessable'] for r in rows),'mixed_parent_selections_excluded_from_person_master':['khan_2005_korea_leaders60'],'field_specific_secondary_units':['khan_2005_korea_leaders60_politics10'],'identity_override_registry':'data/typeA/canonical_identity_overrides_v0_1.json','identity_overlap_audit':'research/khan_2005_politics10_identity_audit_v0_2.json'}
    guards=['person_id is derived from canonical identity_key, not display name alone.','The two people named 이미경 remain distinct canonical persons.','All ten Kyunghyang 2005 politics10 persons already existed in the v0.3 canonical person set; adding the cohort creates ten placements and zero new canonical people.','The original Kyunghyang 2005 project selected 60 units: 57 persons and 3 organizations.','Only its all-person politics10 field is included here as a field-specific secondary cohort.','Do not treat 255 placements as independent observations.']
    master={'schema_version':'typeA_common_master_v0.4','generated':'2026-08-18','status':'corrected_identity_overlap_plus_khan_2005_politics10','qa':qa,'identity_policy':base['identity_policy'],'placements':rows,'people':people}
    metrics={'schema_version':'typeA_common_metrics_v0.4','generated':'2026-08-18','status':'corrected_identity_overlap','qa':qa,'by_cohort_unit':units,'by_design':designs,'naive_placement_pooled_descriptive':naive,'person_first_selection_descriptive':pf,'interpretation_guardrails':guards,'correction_note':'Earlier unmaterialized v0.4 design incorrectly expected 195 persons because 김근태 and 손학규 were misclassified as new; v0.3 already contains both in NewsMaker 2003.'}
    freeze={'schema_version':'typeA_common_master_freeze_v0.4','generated':'2026-08-18','qa':qa,'by_cohort_unit':units,'by_design':designs,'naive_placement_pooled_descriptive':naive,'person_first_selection_descriptive':pf,'guardrails':guards,'supersedes_unmaterialized_expectation':{'unique_people':195,'unique_display_names':194}}
    OUTJ.write_text(json.dumps(master,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); OUTM.write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); FREEZE.write_text(json.dumps(freeze,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    fields=['placement_id','person_id','identity_key','legacy_person_id_v0_2','name','outlet','selection_date','selection_year','cohort_unit','list_title','design','selection_mechanism','domain','rank','rank_known','selection_score','selection_score_type','series_order','target_horizon','baseline_peak_through_t0','post_t0_peak_score','outcome_assessable','advancement_delta','advancement_class','major_ge3','apex_eq4','death_truncated','source_schema','parent_selection','parent_selected_units','field_specific_secondary']
    with OUTC.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows({k:r.get(k) for k in fields} for r in rows)
    print(json.dumps(freeze,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
