#!/usr/bin/env python3
import csv, hashlib, json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean

from identity_resolution import resolve_identity_key, person_id_from_identity_key

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'data/typeA/typeA_common_master_v0_3.json'
KHAN05=ROOT/'data/typeA/khan_2005_politics10_peak_master_v1_0.json'
IDAUDIT=ROOT/'research/khan_2005_politics10_identity_audit_v0_1.json'
OUTJ=ROOT/'data/typeA/typeA_common_master_v0_4.json'
OUTC=ROOT/'data/typeA/typeA_common_master_v0_4.csv'
OUTM=ROOT/'data/typeA/typeA_common_metrics_v0_4.json'
FREEZE=ROOT/'state/typeA_common_master_freeze_v0_4.json'


def placement_id(outlet,cohort_unit,name):
    return 'pl-' + hashlib.sha256(f'{outlet}|{cohort_unit}|{name}'.encode('utf-8')).hexdigest()[:14]


def khan05_row(p):
    outlet='경향신문'; unit='khan_2005_korea_leaders60_politics10'
    ik=resolve_identity_key(p['name'],outlet,unit)
    return {
      'placement_id':placement_id(outlet,unit,p['name']),
      'person_id':person_id_from_identity_key(ik),'identity_key':ik,'legacy_person_id_v0_2':None,
      'name':p['name'],'outlet':outlet,'selection_date':'2005-12-15','selection_year':2005,
      'cohort_unit':unit,'list_title':'한국을 이끌 60인 — 정치10',
      'design':'multistage_public_awareness_expert_final_field10',
      'selection_mechanism':'1168_initial_to_185_expert_recommendation_to_public1266_to_final_expert12',
      'domain':'politics','rank':None,'rank_known':False,'target_horizon':'2006-2020',
      'selection_score':None,'selection_score_type':None,'series_order':None,
      'baseline_peak_through_t0':p['baseline_peak_through_t0'],'post_t0_peak_score':p['post_t0_peak_score'],
      'outcome_assessable':True,'advancement_delta':p['advancement_delta'],'advancement_class':p['advancement_class'],
      'major_ge3':p['post_t0_peak_score']>=3,'apex_eq4':p['post_t0_peak_score']==4,
      'death_truncated':bool(p.get('death_truncated',False)),'source_schema':'khan_2005_politics10_peak_master_v1_0',
      'parent_selection':'khan_2005_korea_leaders60','parent_selected_units':60,'field_specific_secondary':True
    }


def summarize_unit(rr):
    assessed=[r for r in rr if r['outcome_assessable']]
    return {
      'n':len(rr),'assessable_n':len(assessed),'unique_people':len({r['person_id'] for r in rr}),
      'design':rr[0]['design'],'selection_mechanism':rr[0]['selection_mechanism'],'outlet':rr[0]['outlet'],
      'baseline_mean':mean(r['baseline_peak_through_t0'] for r in rr),
      'post_peak_mean_assessable':mean(r['post_t0_peak_score'] for r in assessed),
      'major_n':sum(r['major_ge3'] for r in rr),'major_rate_full':sum(r['major_ge3'] for r in rr)/len(rr),
      'apex_n':sum(r['apex_eq4'] for r in rr),'apex_rate_full':sum(r['apex_eq4'] for r in rr)/len(rr),
      'advanced_n':sum(r['advancement_class']=='advanced' for r in rr),'advanced_rate_full':sum(r['advancement_class']=='advanced' for r in rr)/len(rr),
      'not_assessable_n':sum(not r['outcome_assessable'] for r in rr),
      'field_specific_secondary':bool(rr[0].get('field_specific_secondary',False)),
      'parent_selection':rr[0].get('parent_selection')
    }


def main():
    base=json.loads(BASE.read_text(encoding='utf-8'))
    kh=json.loads(KHAN05.read_text(encoding='utf-8'))
    audit=json.loads(IDAUDIT.read_text(encoding='utf-8'))
    assert base['qa']['placements']==245 and base['qa']['unique_people']==193
    assert kh['metrics']['population']=={'n':10,'assessable_n':10,'parent_selected_units':60,'field_specific_secondary':True}
    assert audit['qa']['same_existing_n']==8 and audit['qa']['new_person_n']==2 and audit['qa']['pending_n']==0

    rows=[dict(r) for r in base['placements']]
    rows += [khan05_row(p) for p in kh['people']]
    assert len(rows)==255
    assert len({r['placement_id'] for r in rows})==255

    # Parent mixed selection guardrail: only the all-person politics field enters this person-only master.
    assert all(r.get('parent_selection')!='khan_2005_korea_leaders60' or r['cohort_unit']=='khan_2005_korea_leaders60_politics10' for r in rows)
    assert len([r for r in rows if r['cohort_unit']=='khan_2005_korea_leaders60_politics10'])==10

    same8={x['name'] for x in audit['same_person_existing']}
    assert same8=={'강금실','김부겸','노회찬','박근혜','박진','원희룡','이명박','정동영'}
    for n in same8:
        rr=[r for r in rows if r['name']==n]
        assert len({r['identity_key'] for r in rr})==1, n
        assert len({r['person_id'] for r in rr})==1, n

    new2={x['name'] for x in audit['new_canonical_people']}
    assert new2=={'김근태','손학규'}
    for n in new2:
        rr=[r for r in rows if r['name']==n]
        assert len(rr)==1 and rr[0]['cohort_unit']=='khan_2005_korea_leaders60_politics10'

    # Existing true homonym split must remain intact.
    lee=[r for r in rows if r['name']=='이미경']
    assert len(lee)==2 and len({r['person_id'] for r in lee})==2
    assert {r['identity_key'] for r in lee}=={'이미경|cj_enm_business','이미경|politician'}

    by_pid=defaultdict(list)
    for r in rows: by_pid[r['person_id']].append(r)
    assert len(by_pid)==195
    assert len({r['identity_key'] for r in rows})==195
    assert len({r['name'] for r in rows})==194

    person_rows=[]
    for pid,pp0 in by_pid.items():
        pp=sorted(pp0,key=lambda r:(r['selection_date'],r['outlet'],r['cohort_unit']))
        assessed=[r for r in pp if r['outcome_assessable']]
        names=sorted({r['name'] for r in pp}); iks=sorted({r['identity_key'] for r in pp})
        assert len(names)==1 and len(iks)==1
        person_rows.append({
          'person_id':pid,'identity_key':iks[0],'name':names[0],'placement_count':len(pp),
          'outlets':sorted({r['outlet'] for r in pp}),'selection_years':[r['selection_year'] for r in pp],
          'cohort_units':[r['cohort_unit'] for r in pp],'designs':sorted({r['design'] for r in pp}),
          'first_selection_year':pp[0]['selection_year'],'last_selection_year':pp[-1]['selection_year'],
          'first_selection_baseline':pp[0]['baseline_peak_through_t0'],
          'first_selection_post_peak':pp[0]['post_t0_peak_score'],
          'first_selection_advancement_class':pp[0]['advancement_class'],
          'assessable_placement_n':len(assessed),
          'ever_major_across_placements':any(r['major_ge3'] for r in assessed),
          'ever_apex_across_placements':any(r['apex_eq4'] for r in assessed),
          'ever_advanced_across_placements':any(r['advancement_class']=='advanced' for r in assessed),
          'placements':[r['placement_id'] for r in pp]
        })
    person_rows.sort(key=lambda p:(p['name'],p['identity_key']))

    dist=Counter(p['placement_count'] for p in person_rows)
    repeated=[p for p in person_rows if p['placement_count']>1]

    units={}
    for unit in dict.fromkeys(r['cohort_unit'] for r in rows):
        units[unit]=summarize_unit([r for r in rows if r['cohort_unit']==unit])
    assert len(units)==7
    k5=units['khan_2005_korea_leaders60_politics10']
    assert (k5['n'],k5['major_n'],k5['apex_n'],k5['advanced_n'])==(10,10,5,8)
    assert abs(k5['baseline_mean']-2.6)<1e-12 and abs(k5['post_peak_mean_assessable']-3.5)<1e-12
    assert k5['field_specific_secondary'] is True and k5['parent_selection']=='khan_2005_korea_leaders60'

    designs={}
    for design in sorted({r['design'] for r in rows}):
        rr=[r for r in rows if r['design']==design]
        designs[design]={
          'placements':len(rr),'unique_people':len({r['person_id'] for r in rr}),
          'major_n':sum(r['major_ge3'] for r in rr),'major_rate_full':sum(r['major_ge3'] for r in rr)/len(rr),
          'apex_n':sum(r['apex_eq4'] for r in rr),'apex_rate_full':sum(r['apex_eq4'] for r in rr)/len(rr),
          'advanced_n':sum(r['advancement_class']=='advanced' for r in rr),'advanced_rate_full':sum(r['advancement_class']=='advanced' for r in rr)/len(rr),
          'warning':'Descriptive only; year, domain, list depth and selection mechanism remain confounded.'
        }

    naive={
      'placements':255,'unique_people':195,
      'major_n':sum(r['major_ge3'] for r in rows),'major_rate':sum(r['major_ge3'] for r in rows)/255,
      'apex_n':sum(r['apex_eq4'] for r in rows),'apex_rate':sum(r['apex_eq4'] for r in rows)/255,
      'advanced_n':sum(r['advancement_class']=='advanced' for r in rows),'advanced_rate':sum(r['advancement_class']=='advanced' for r in rows)/255,
      'warning':'Descriptive only. Placements are not independent; the 2005 Kyunghyang politics10 is a secondary field stratum of a 60-unit mixed selection.'
    }
    assert (naive['major_n'],naive['apex_n'],naive['advanced_n'])==(216,44,106)

    pf={
      'persons':195,
      'first_selection_major_n':sum((p['first_selection_post_peak'] or -1)>=3 for p in person_rows),
      'first_selection_apex_n':sum(p['first_selection_post_peak']==4 for p in person_rows),
      'first_selection_advanced_n':sum(p['first_selection_advancement_class']=='advanced' for p in person_rows),
      'warning':'Person-level first-selection description; observation windows and cohort designs differ.'
    }
    assert pf['first_selection_major_n']==159
    assert pf['first_selection_apex_n']==24
    assert pf['first_selection_advanced_n']==79

    qa={
      'placements':255,'unique_people':195,'unique_display_names':194,'true_homonym_split_n':1,
      'repeated_person_n':len(repeated),'placement_count_distribution':{str(k):v for k,v in sorted(dist.items())},
      'max_placement_count':max(dist),
      'max_selected_names':sorted(p['name'] for p in person_rows if p['placement_count']==max(dist)),
      'cohort_units':7,'not_assessable_placements':sum(not r['outcome_assessable'] for r in rows),
      'mixed_parent_selections_excluded_from_person_master':['khan_2005_korea_leaders60'],
      'field_specific_secondary_units':['khan_2005_korea_leaders60_politics10'],
      'identity_override_registry':'data/typeA/canonical_identity_overrides_v0_1.json'
    }
    guardrails=[
      'person_id is derived from canonical identity_key, not display name alone.',
      'The two people named 이미경 remain distinct canonical persons.',
      'The original Kyunghyang 2005 project selected 60 units: 57 persons and 3 organizations.',
      'Only its all-person politics10 field is included here as a prespecified field-specific secondary cohort.',
      'Do not report politics10 metrics as performance of the full 60-unit project.',
      'Do not treat 255 placements as independent observations.',
      'Baseline-adjusted advancement is preferred for future-rise claims; raw major attainment includes persistence.'
    ]
    master={'schema_version':'typeA_common_master_v0.4','generated':'2026-08-18','status':'plus_khan_2005_politics10_field_secondary',
      'qa':qa,'identity_policy':base['identity_policy'],'placements':rows,'people':person_rows}
    metrics={'schema_version':'typeA_common_metrics_v0.4','generated':'2026-08-18','qa':qa,
      'by_cohort_unit':units,'by_design':designs,'naive_placement_pooled_descriptive':naive,
      'person_first_selection_descriptive':pf,'interpretation_guardrails':guardrails}
    freeze={'schema_version':'typeA_common_master_freeze_v0.4','generated':'2026-08-18','qa':qa,
      'by_cohort_unit':units,'by_design':designs,'naive_placement_pooled_descriptive':naive,
      'person_first_selection_descriptive':pf,'guardrails':guardrails}

    OUTJ.write_text(json.dumps(master,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    OUTM.write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    FREEZE.write_text(json.dumps(freeze,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    fields=['placement_id','person_id','identity_key','legacy_person_id_v0_2','name','outlet','selection_date','selection_year','cohort_unit','list_title','design','selection_mechanism','domain','rank','rank_known','selection_score','selection_score_type','series_order','target_horizon','baseline_peak_through_t0','post_t0_peak_score','outcome_assessable','advancement_delta','advancement_class','major_ge3','apex_eq4','death_truncated','source_schema','parent_selection','parent_selected_units','field_specific_secondary']
    with OUTC.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows({k:r.get(k) for k in fields} for r in rows)
    print(json.dumps(freeze,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
