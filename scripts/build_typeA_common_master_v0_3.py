#!/usr/bin/env python3
import csv, hashlib, json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean

from identity_resolution import resolve_identity_key, person_id_from_identity_key

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'data/typeA/typeA_common_master_v0_2.json'
KHAN=ROOT/'data/typeA/khan_2004_17th_assembly_newleaders_peak_master_v1_0.json'
IDAUDIT=ROOT/'research/khan_2004_common_overlap_identity_audit_v0_1.json'
OUTJ=ROOT/'data/typeA/typeA_common_master_v0_3.json'
OUTC=ROOT/'data/typeA/typeA_common_master_v0_3.csv'
OUTM=ROOT/'data/typeA/typeA_common_metrics_v0_3.json'
FREEZE=ROOT/'state/typeA_common_master_freeze_v0_3.json'


def placement_id(outlet,cohort_unit,name):
    return 'pl-' + hashlib.sha256(f'{outlet}|{cohort_unit}|{name}'.encode('utf-8')).hexdigest()[:14]


def migrate_base_row(r):
    x=dict(r)
    ik=resolve_identity_key(r['name'],r['outlet'],r['cohort_unit'])
    x['identity_key']=ik
    x['legacy_person_id_v0_2']=r['person_id']
    x['person_id']=person_id_from_identity_key(ik)
    return x


def khan_row(p):
    outlet='경향신문'; unit='khan_2004_17th_assembly_newleaders_20'
    ik=resolve_identity_key(p['name'],outlet,unit)
    return {
      'placement_id':placement_id(outlet,unit,p['name']),
      'person_id':person_id_from_identity_key(ik),'identity_key':ik,'legacy_person_id_v0_2':None,
      'name':p['name'],'outlet':outlet,'selection_date':'2004-05-05','selection_year':2004,
      'cohort_unit':unit,'list_title':'17代국회 이끌 뉴리더','design':'expert_vote_party_quota_top20',
      'selection_mechanism':'expert_panel_vote_party_quota','domain':'politics',
      'rank':None,'rank_known':False,'target_horizon':None,
      'selection_score':p.get('vote_count'),'selection_score_type':'expert_vote_count' if p.get('vote_count') is not None else None,
      'series_order':p.get('series_order'),
      'baseline_peak_through_t0':p['baseline_peak_through_t0'],'post_t0_peak_score':p['post_t0_peak_score'],
      'outcome_assessable':True,'advancement_delta':p['advancement_delta'],'advancement_class':p['advancement_class'],
      'major_ge3':p['post_t0_peak_score']>=3,'apex_eq4':p['post_t0_peak_score']==4,
      'death_truncated':False,'source_schema':'khan_2004_17th_assembly_newleaders_peak_master_v1_0'
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
      'not_assessable_n':sum(not r['outcome_assessable'] for r in rr)
    }


def main():
    base=json.loads(BASE.read_text(encoding='utf-8'))
    kh=json.loads(KHAN.read_text(encoding='utf-8'))
    audit=json.loads(IDAUDIT.read_text(encoding='utf-8'))
    assert base['qa']['placements']==225 and base['qa']['unique_people']==179
    assert kh['metrics']['population']=={'n':20,'assessable_n':20}
    assert audit['summary']=={'name_collisions':7,'same_person':6,'different_person':1,'pending':0}

    rows=[migrate_base_row(r) for r in base['placements']]
    rows += [khan_row(p) for p in kh['people']]
    assert len(rows)==245
    assert len({r['placement_id'] for r in rows})==245

    # Identity migration must split the two different people named 이미경.
    lee=[r for r in rows if r['name']=='이미경']
    assert len(lee)==2
    assert {r['identity_key'] for r in lee}=={'이미경|cj_enm_business','이미경|politician'}
    assert len({r['person_id'] for r in lee})==2

    # Six confirmed cross-cohort political overlaps must merge to one identity each.
    same6={x['name'] for x in audit['adjudications'] if x['decision']=='same_person'}
    assert same6=={'김문수','김부겸','송영길','원희룡','유시민','천정배'}
    for n in same6:
        rr=[r for r in rows if r['name']==n]
        assert len({r['identity_key'] for r in rr})==1, n
        assert len({r['person_id'] for r in rr})==1, n

    by_pid=defaultdict(list)
    for r in rows: by_pid[r['person_id']].append(r)
    assert len(by_pid)==193
    assert len({r['identity_key'] for r in rows})==193
    assert len({r['name'] for r in rows})==192  # one true homonym split: 이미경

    person_rows=[]
    for pid,pp0 in by_pid.items():
        pp=sorted(pp0,key=lambda r:(r['selection_date'],r['outlet'],r['cohort_unit']))
        assessed=[r for r in pp if r['outcome_assessable']]
        names=sorted({r['name'] for r in pp})
        iks=sorted({r['identity_key'] for r in pp})
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
    assert dist==Counter({1:147,2:41,3:4,4:1}), dist
    repeated=[p for p in person_rows if p['placement_count']>1]
    assert len(repeated)==46
    assert [p['name'] for p in person_rows if p['placement_count']==4]==['유시민']
    assert sorted(p['name'] for p in person_rows if p['placement_count']==3)==['김문수','안철수','원희룡','이재용']

    units={}
    for unit in dict.fromkeys(r['cohort_unit'] for r in rows):
        units[unit]=summarize_unit([r for r in rows if r['cohort_unit']==unit])
    assert len(units)==6
    ku=units['khan_2004_17th_assembly_newleaders_20']
    assert (ku['n'],ku['major_n'],ku['apex_n'],ku['advanced_n'])==(20,20,4,19)

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
      'placements':245,'unique_people':193,
      'major_n':sum(r['major_ge3'] for r in rows),'major_rate':sum(r['major_ge3'] for r in rows)/245,
      'apex_n':sum(r['apex_eq4'] for r in rows),'apex_rate':sum(r['apex_eq4'] for r in rows)/245,
      'advanced_n':sum(r['advancement_class']=='advanced' for r in rows),'advanced_rate':sum(r['advancement_class']=='advanced' for r in rows)/245,
      'warning':'Descriptive only. Placements are not independent and the six cohort units have heterogeneous designs, years, domains and selection mechanisms.'
    }
    assert (naive['major_n'],naive['apex_n'],naive['advanced_n'])==(206,39,98)

    pf={
      'persons':193,
      'first_selection_major_n':sum((p['first_selection_post_peak'] or -1)>=3 for p in person_rows),
      'first_selection_apex_n':sum(p['first_selection_post_peak']==4 for p in person_rows),
      'first_selection_advanced_n':sum(p['first_selection_advancement_class']=='advanced' for p in person_rows),
      'warning':'Person-level first-selection description; observation windows and cohort designs differ.'
    }
    assert pf=={
      'persons':193,'first_selection_major_n':157,'first_selection_apex_n':23,'first_selection_advanced_n':78,
      'warning':'Person-level first-selection description; observation windows and cohort designs differ.'
    }

    qa={
      'placements':245,'unique_people':193,'unique_display_names':192,'true_homonym_split_n':1,
      'repeated_person_n':46,'placement_count_distribution':{str(k):v for k,v in sorted(dist.items())},
      'four_time_selected_names':['유시민'],'three_time_selected_names':['김문수','안철수','원희룡','이재용'],
      'cohort_units':6,'not_assessable_placements':sum(not r['outcome_assessable'] for r in rows),
      'identity_override_registry':'data/typeA/canonical_identity_overrides_v0_1.json'
    }
    guardrails=[
      'person_id is derived from canonical identity_key, not display name alone.',
      'The two people named 이미경 remain distinct canonical persons.',
      'Do not treat 245 placements as independent observations; 46 people recur.',
      'Do not infer outlet effects from heterogeneous selection designs.',
      'Baseline-adjusted advancement is preferred for future-rise claims; raw major attainment includes persistence.',
      'Kyunghyang 2004 used party quotas and an expert panel; it is not a published full-rank Top20.',
      '신기남 reached party chair only 12 days after selection; interpret as near-immediate/imminent advancement.'
    ]
    master={'schema_version':'typeA_common_master_v0.3','generated':'2026-08-18','status':'identity_key_migrated_plus_khan_2004',
      'qa':qa,'identity_policy':{'policy_ref':'state/identity_resolution_policy_v0_2.md','homonym_split_names':['이미경']},
      'placements':rows,'people':person_rows}
    metrics={'schema_version':'typeA_common_metrics_v0.3','generated':'2026-08-18','qa':qa,
      'by_cohort_unit':units,'by_design':designs,'naive_placement_pooled_descriptive':naive,
      'person_first_selection_descriptive':pf,'interpretation_guardrails':guardrails}
    freeze={'schema_version':'typeA_common_master_freeze_v0.3','generated':'2026-08-18','qa':qa,
      'by_cohort_unit':units,'by_design':designs,'naive_placement_pooled_descriptive':naive,
      'person_first_selection_descriptive':pf,'guardrails':guardrails}

    OUTJ.write_text(json.dumps(master,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    OUTM.write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    FREEZE.write_text(json.dumps(freeze,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    fields=['placement_id','person_id','identity_key','legacy_person_id_v0_2','name','outlet','selection_date','selection_year','cohort_unit','list_title','design','selection_mechanism','domain','rank','rank_known','selection_score','selection_score_type','series_order','target_horizon','baseline_peak_through_t0','post_t0_peak_score','outcome_assessable','advancement_delta','advancement_class','major_ge3','apex_eq4','death_truncated','source_schema']
    with OUTC.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows({k:r.get(k) for k in fields} for r in rows)
    print(json.dumps(freeze,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
