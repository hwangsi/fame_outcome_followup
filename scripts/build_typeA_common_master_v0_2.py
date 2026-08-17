#!/usr/bin/env python3
import csv, hashlib, json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean

ROOT=Path(__file__).resolve().parents[1]
TYPEA=ROOT/'data/typeA'
NM=TYPEA/'newsmaker_2003_outcomes_v0_3.json'
H21=TYPEA/'h21_2004_outcomes_v0_1.json'
D10=TYPEA/'donga_2010_post_t0_peak_master_v1_2.json'
D11=ROOT/'analysis/donga_2011_post_t0_master_v1_0.json'
TWO=ROOT/'analysis/donga_2010_2011_two_wave_master_v0_1.json'
OUTJ=TYPEA/'typeA_common_master_v0_2.json'
OUTC=TYPEA/'typeA_common_master_v0_2.csv'
OUTM=TYPEA/'typeA_common_metrics_v0_2.json'
FREEZE=ROOT/'state/typeA_common_master_freeze_v0_2.json'

# Cross-cohort same-name identities already verified in the previous common master or during 2011 audit.
EARLY_VERIFIED_OVERLAP={'강금실','권영길','정동영','추미애','유시민','안철수','이재용','박근혜'}

def person_id(name):
    return 'ko-' + hashlib.sha256(name.encode('utf-8')).hexdigest()[:12]

def placement_id(outlet,cohort_unit,name):
    key=f'{outlet}|{cohort_unit}|{name}'
    return 'pl-' + hashlib.sha256(key.encode('utf-8')).hexdigest()[:14]

def classify(delta,post,assessable=True):
    if not assessable or post is None: return 'not_assessable'
    if delta>0: return 'advanced'
    if delta==0 and post>=3: return 'sustained_high'
    if delta==0: return 'no_clear_advancement'
    return 'lower_than_baseline'

def row(**kw):
    assessable=kw.get('assessable',kw.get('post') is not None)
    post=kw.get('post'); delta=kw.get('delta') if assessable else None
    adv=kw.get('adv_class') or classify(delta,post,assessable)
    return {
      'placement_id':placement_id(kw['outlet'],kw['cohort_unit'],kw['name']),
      'person_id':person_id(kw['name']),'name':kw['name'],'outlet':kw['outlet'],
      'selection_date':kw['selection_date'],'selection_year':int(kw['selection_date'][:4]),
      'cohort_unit':kw['cohort_unit'],'list_title':kw['list_title'],'design':kw['design'],
      'selection_mechanism':kw['selection_mechanism'],'domain':kw['domain'],
      'rank':kw.get('rank'),'rank_known':kw.get('rank') is not None,'target_horizon':kw.get('target_horizon'),
      'baseline_peak_through_t0':kw['baseline'],'post_t0_peak_score':post,
      'outcome_assessable':assessable,'advancement_delta':delta,'advancement_class':adv,
      'major_ge3':bool(post is not None and post>=3),'apex_eq4':bool(post==4),
      'death_truncated':bool(kw.get('death_truncated',False)),'source_schema':kw['source_schema']
    }

def main():
    rows=[]
    nm=json.loads(NM.read_text(encoding='utf-8'))
    for p in nm['people']:
        domain=p['domain']; unit=f'newsmaker_2003_{domain}_top{10 if domain=="politics" else 5}'
        rows.append(row(name=p['name'],outlet='뉴스메이커',selection_date='2003-05-30',cohort_unit=unit,
            list_title='차세대 리더 정치·경제',design='ranked_topN',selection_mechanism='expert_survey',domain=domain,
            rank=p.get('rank'),baseline=p['baseline_peak_through_t0'],post=p['post_t0_peak_score'],
            delta=p['advancement_delta'],adv_class=p['baseline_adjusted_class'],source_schema='newsmaker_2003_outcomes_v0_3'))

    h=json.loads(H21.read_text(encoding='utf-8'))
    for p in h['people']:
        rows.append(row(name=p['name'],outlet='한겨레21',selection_date='2004-09-20',cohort_unit='h21_2004_politics_top10',
            list_title='차세대 리더 여론조사 Top10',design='ranked_topN',selection_mechanism='public_opinion_survey',domain='politics',
            rank=p.get('rank'),baseline=p['baseline_peak_through_t0'],post=p['post_t0_peak_score'],
            delta=p['advancement_delta'],adv_class=p['baseline_adjusted_class'],source_schema='h21_2004_outcomes_v0_1'))

    d10=json.loads(D10.read_text(encoding='utf-8'))
    assert d10['qa']['assessed']==100 and d10['qa']['unresolved']==0
    for p in d10['people']:
        rows.append(row(name=p['name'],outlet='동아일보',selection_date='2010-05-10',cohort_unit='donga_2010_2020_100',
            list_title='2020년 한국을 빛낼 100인',design='broad_screening_explicit_horizon',selection_mechanism='editorial_expert_screening',
            domain=p['category'],rank=None,target_horizon='2020',baseline=p['baseline_peak_through_t0'],post=p['post_t0_peak_score'],
            delta=p['advancement_delta'],adv_class=p['advancement_class'],death_truncated=p['exposure_truncated_by_death'],
            source_schema='donga_2010_post_t0_peak_master_v1_2'))

    d11=json.loads(D11.read_text(encoding='utf-8'))
    assert d11['qa']['adjudicated_n']==100 and d11['qa']['pending_n']==0
    for p in d11['people']:
        rows.append(row(name=p['name'],outlet='동아일보',selection_date='2011-04-01',cohort_unit='donga_2011_10yr_100',
            list_title='10년 뒤 한국을 빛낼 100인',design='broad_screening_explicit_horizon',selection_mechanism='editorial_expert_screening',
            domain=p['category'],rank=None,target_horizon='2021',baseline=p['baseline_2011'],post=p['post2011_peak_score'],
            assessable=p['post2011_peak_score'] is not None,delta=p['advancement_delta'],adv_class=p['advancement_class'],
            death_truncated=p['exposure_truncated_by_death'],source_schema='donga_2011_post_t0_master_v1_0'))

    assert len(rows)==225
    assert len({r['placement_id'] for r in rows})==225

    by_name=defaultdict(list)
    for r in rows: by_name[r['name']].append(r)
    same_name_candidates={n for n,v in by_name.items() if len(v)>1}

    two=json.loads(TWO.read_text(encoding='utf-8'))
    donga_repeat={p['name'] for p in two['people'] if p['group']=='repeat_2010_2011'}
    assert len(donga_repeat)==38
    expected_verified=donga_repeat | EARLY_VERIFIED_OVERLAP
    # Any newly appearing same-name collision must be manually identity-audited before the build can pass.
    assert same_name_candidates==expected_verified, {
      'unexpected_same_name_candidates':sorted(same_name_candidates-expected_verified),
      'expected_but_missing':sorted(expected_verified-same_name_candidates)
    }

    # Explicitly verify known early overlaps by contemporaneous roles represented in source schemas.
    expected_counts={'유시민':3,'안철수':3,'이재용':3,'박근혜':2,'강금실':2,'권영길':2,'정동영':2,'추미애':2}
    for n,c in expected_counts.items(): assert len(by_name[n])==c, (n,len(by_name[n]))

    person_rows=[]
    for name in sorted(by_name):
        pp=sorted(by_name[name],key=lambda r:(r['selection_date'],r['outlet'],r['cohort_unit']))
        assessed=[r for r in pp if r['outcome_assessable']]
        person_rows.append({
          'person_id':person_id(name),'name':name,'placement_count':len(pp),
          'outlets':sorted({r['outlet'] for r in pp}),'selection_years':[r['selection_year'] for r in pp],
          'cohort_units':[r['cohort_unit'] for r in pp],
          'designs':sorted({r['design'] for r in pp}),
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

    assert len(person_rows)==179, len(person_rows)
    placement_counts=Counter(p['placement_count'] for p in person_rows)
    assert placement_counts==Counter({1:136,2:40,3:3}), placement_counts
    repeated=[p for p in person_rows if p['placement_count']>1]
    assert len(repeated)==43
    triple=sorted(p['name'] for p in person_rows if p['placement_count']==3)
    assert triple==['안철수','유시민','이재용'], triple

    units={}
    for unit in dict.fromkeys(r['cohort_unit'] for r in rows):
        rr=[r for r in rows if r['cohort_unit']==unit]
        assessed=[r for r in rr if r['outcome_assessable']]
        units[unit]={
          'n':len(rr),'assessable_n':len(assessed),'unique_people':len({r['person_id'] for r in rr}),
          'design':rr[0]['design'],'selection_mechanism':rr[0]['selection_mechanism'],'outlet':rr[0]['outlet'],
          'baseline_mean':mean(r['baseline_peak_through_t0'] for r in rr),
          'post_peak_mean_assessable':mean(r['post_t0_peak_score'] for r in assessed),
          'major_n':sum(r['major_ge3'] for r in rr),'major_rate_full':sum(r['major_ge3'] for r in rr)/len(rr),
          'apex_n':sum(r['apex_eq4'] for r in rr),'apex_rate_full':sum(r['apex_eq4'] for r in rr)/len(rr),
          'advanced_n':sum(r['advancement_class']=='advanced' for r in rr),'advanced_rate_full':sum(r['advancement_class']=='advanced' for r in rr)/len(rr),
          'not_assessable_n':sum(not r['outcome_assessable'] for r in rr)
        }

    assert (units['donga_2011_10yr_100']['major_n'],units['donga_2011_10yr_100']['apex_n'],units['donga_2011_10yr_100']['advanced_n'])==(90,12,36)
    assert units['donga_2011_10yr_100']['not_assessable_n']==1

    design_groups={}
    for design in sorted({r['design'] for r in rows}):
        rr=[r for r in rows if r['design']==design]
        design_groups[design]={
          'placements':len(rr),'unique_people':len({r['person_id'] for r in rr}),
          'major_n':sum(r['major_ge3'] for r in rr),'major_rate_full':sum(r['major_ge3'] for r in rr)/len(rr),
          'apex_n':sum(r['apex_eq4'] for r in rr),'apex_rate_full':sum(r['apex_eq4'] for r in rr)/len(rr),
          'advanced_n':sum(r['advancement_class']=='advanced' for r in rr),'advanced_rate_full':sum(r['advancement_class']=='advanced' for r in rr)/len(rr),
          'warning':'Descriptive only; year, domain, depth and selection mechanism remain confounded.'
        }

    qa={
      'placements':225,'unique_people':179,'repeated_person_n':43,
      'placement_count_distribution':{str(k):v for k,v in sorted(placement_counts.items())},
      'triple_selected_names':triple,'same_name_candidates_n':len(same_name_candidates),
      'same_name_candidates':sorted(same_name_candidates),'cohort_units':5,
      'not_assessable_placements':sum(not r['outcome_assessable'] for r in rows)
    }
    master={'schema_version':'typeA_common_master_v0.2','generated':'2026-08-18',
      'status':'identity_guarded_225_placements_179_persons','qa':qa,
      'identity_policy':{
        'rule':'A repeated Korean name is merged only if it belongs to the frozen Dong-A repeat set or the explicitly verified early-overlap set.',
        'early_verified_overlap_names':sorted(EARLY_VERIFIED_OVERLAP),
        'donga_repeat_names':sorted(donga_repeat),
        'unexpected_same_name_candidate_action':'fail build and require manual identity audit'
      },
      'placements':rows,'people':person_rows}

    naive={
      'placements':225,'unique_people':179,
      'major_n':sum(r['major_ge3'] for r in rows),'major_rate':sum(r['major_ge3'] for r in rows)/225,
      'apex_n':sum(r['apex_eq4'] for r in rows),'apex_rate':sum(r['apex_eq4'] for r in rows)/225,
      'advanced_n':sum(r['advancement_class']=='advanced' for r in rows),'advanced_rate':sum(r['advancement_class']=='advanced' for r in rows)/225,
      'warning':'Descriptive only. 225 placements are not independent: 43 people appear multiple times, including three people with three placements.'
    }
    person_first={
      'persons':179,
      'first_selection_major_n':sum((p['first_selection_post_peak'] or -1)>=3 for p in person_rows),
      'first_selection_apex_n':sum(p['first_selection_post_peak']==4 for p in person_rows),
      'first_selection_advanced_n':sum(p['first_selection_advancement_class']=='advanced' for p in person_rows),
      'warning':'Person-level first-selection description; observation windows differ by first selection year and cohort design.'
    }
    metrics={'schema_version':'typeA_common_metrics_v0.2','generated':'2026-08-18','qa':qa,
      'by_cohort_unit':units,'by_design':design_groups,'naive_placement_pooled_descriptive':naive,
      'person_first_selection_descriptive':person_first,
      'interpretation_guardrails':[
        'Do not treat 225 placements as independent observations; 43 people recur and three people appear three times.',
        'Do not infer outlet effects from design-stratified differences because year, domain, list depth and mechanism are confounded.',
        'Baseline-adjusted advancement is preferred for future-rise claims; major attainment includes already-high persistence.',
        'The single 2011 not-assessable placement remains a conservative non-hit in full-placement rates.',
        'Any future cross-cohort same-name collision not in the verified identity sets must fail the build pending manual identity audit.'
      ]}

    OUTJ.write_text(json.dumps(master,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    OUTM.write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    FREEZE.write_text(json.dumps({'schema_version':'typeA_common_master_freeze_v0.2','generated':'2026-08-18','qa':qa,
      'by_cohort_unit':units,'by_design':design_groups,'naive_placement_pooled_descriptive':naive,
      'person_first_selection_descriptive':person_first,'guardrails':metrics['interpretation_guardrails']},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

    fields=['placement_id','person_id','name','outlet','selection_date','selection_year','cohort_unit','list_title','design','selection_mechanism','domain','rank','rank_known','target_horizon','baseline_peak_through_t0','post_t0_peak_score','outcome_assessable','advancement_delta','advancement_class','major_ge3','apex_eq4','death_truncated','source_schema']
    with OUTC.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows({k:r.get(k) for k in fields} for r in rows)
    print(json.dumps(metrics,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
