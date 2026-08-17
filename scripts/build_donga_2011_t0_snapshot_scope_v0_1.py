#!/usr/bin/env python3
import csv,json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TYPEA=ROOT/'data/typeA'
SRC=TYPEA/'donga_2011_t0_roles_v0_1.json'
ROSTER=TYPEA/'donga_2011_100_roster_v0_1.json'
OUTJ=TYPEA/'donga_2011_t0_snapshot_scope_v0_1.json'
OUTC=TYPEA/'donga_2011_t0_snapshot_scope_v0_1.csv'

SCORE={
'김기문':3,'김빛내리':3,'김상욱':2,'김승환':3,'김영달':2,'김은성':2,'김정범':2,'김철영':2,'김필립':3,'남광희':2,'남민우':2,'박상일':2,'박형주':2,'백운규':2,'유범재':3,'이상엽':3,'이연희':2,'이창준':2,'임지순':3,'장하석':3,'정근창':2,'정준':2,'정하웅':3,'함돈희':2,'현택환':3,
'김선욱':3,'김애란':2,'김연아':4,'김영준':2,'김영하':2,'박지성':3,'박진영':3,'박형준':2,'봉준호':3,'손흥민':2,'신준호':2,'신지애':4,'윤태호':2,'이불':3,'이수만':3,'이자람':2,'장미란':4,'장한나':3,'하상백':2,'하정우':2,
'김문수':3,'김부겸':2,'김태효':2,'나경원':2,'박근혜':2,'오세훈':3,'원희룡':2,'유시민':3,'이정희':3,'임성남':2,
'강덕수':3,'권구훈':2,'김가영':2,'김남구':3,'김정주':3,'김택진':3,'박지영':2,'박현주':3,'변대규':2,'서정진':3,'손병두':3,'신현송':3,'양윤선':2,'이미경':3,'이부진':3,'이서현':3,'이재용':3,'이창용':3,'이해진':3,'장하준':3,'정용진':3,'정의선':3,'정태영':3,'최태원':4,'황철주':2,
'강일원':2,'곽노현':3,'김상우':2,'김은식':2,'김준영':2,'김해성':2,'박원순':2,'백승헌':2,'석지영':3,'손영래':2,'안철수':3,'윤순진':2,'이국종':2,'이상이':2,'이주호':3,'전혜경':3,'정일용':2,'조국':2,'조명숙':2,'최재경':2
}

SECTOR_BY_CATEGORY={
'꿈꾸는 개척가':'science_technology_innovation',
'자유로운 창조인':'culture_sports_creative',
'미래를 여는 지도자':'politics_diplomacy',
'도전하는 경제인':'business_economics',
'행동하는 지성인':'public_civic_academia'
}

REVIEW={
'김상욱':['preselection_international_research_stature_review'],
'김은성':['preselection_breakthrough_research_review'],
'김정범':['stem_cell_breakthrough_stature_review'],
'함돈희':['harvard_international_engineering_stature_review'],
'김영하':['international_literary_stature_review'],
'손흥민':['top_european_league_early_career_boundary_review'],
'박근혜':['contemporaneous_presidential_contender_status_not_reflected_by_mp_title'],
'나경원':['major_party_leadership_boundary_review'],
'김태효':['presidential_office_national_policy_scope_boundary_review'],
'변대규':['global_technology_company_scale_boundary_review'],
'황철주':['semiconductor_equipment_industry_leadership_boundary_review'],
'김상우':['international_criminal_court_senior_role_boundary_review'],
'최재경':['major_national_judicial_institution_deputy_leadership_review']
}

def main():
    src=json.loads(SRC.read_text(encoding='utf-8'))
    roster=json.loads(ROSTER.read_text(encoding='utf-8'))
    roster_cat={n:c for c,names in roster['categories'].items() for n in names}
    people=src['people']
    names={p['name'] for p in people}
    assert len(people)==100 and len(names)==100
    assert set(SCORE)==names
    assert set(roster_cat)==names
    assert sum(p['repeat_2010_2011'] for p in people)==38
    out=[]
    for p in people:
        n=p['name']; cat=p['category']
        assert roster_cat[n]==cat
        flags=REVIEW.get(n,[])
        out.append({
          'name':n,'category':cat,'t0_role':p['t0_role_official_2011'],
          'repeat_2010_2011':p['repeat_2010_2011'],
          't0_snapshot_scope_score':SCORE[n],
          'sector':SECTOR_BY_CATEGORY[cat],
          'score_basis':'official_2011_role_conservative_pass1' if flags else 'official_2011_role',
          'coding_confidence':'M' if flags else 'H',
          'review_flags':flags,
          'source_url':p['evidence']['source_url']
        })
    cnt=Counter(x['t0_snapshot_scope_score'] for x in out)
    assert cnt==Counter({2:52,3:44,4:4}),cnt
    bycat={}
    for cat in roster['categories']:
        x=[p for p in out if p['category']==cat]
        bycat[cat]={'n':len(x),'score_counts':{str(k):v for k,v in sorted(Counter(p['t0_snapshot_scope_score'] for p in x).items())},'mean_scope':sum(p['t0_snapshot_scope_score'] for p in x)/len(x),'review_flagged':sum(bool(p['review_flags']) for p in x)}
    payload={
      'schema_version':'donga_2011_t0_snapshot_scope_v0.1',
      'generated':'2026-08-18','status':'pass1_provisional_pending_preselection_achievement_audit',
      'selection_cutoff':'2011-04-01',
      'roles_ref':'data/typeA/donga_2011_t0_roles_v0_1.json',
      'rules_ref':'state/coding_rules_typeA_sector_scope_v0_1.md',
      'method':{
        'definition':'Scope of role actually held at the 2011-04-01 selection snapshot.',
        'conservative_pass1':'Role/title first; pre-selection achievements or prior higher office are deferred to explicit audit unless inherent in the role.',
        'next_pass':'Audit review flags and construct lifetime baseline peak through 2011-04-01.'
      },
      'qa':{'total':100,'unique_names':100,'repeat_n':38,'score_counts':{str(k):v for k,v in sorted(cnt.items())},'mean_scope':sum(p['t0_snapshot_scope_score'] for p in out)/100,'review_flagged_n':sum(bool(p['review_flags']) for p in out),'by_category':bycat},
      'people':out
    }
    OUTJ.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    fields=['name','category','t0_role','repeat_2010_2011','t0_snapshot_scope_score','sector','score_basis','coding_confidence','review_flags']
    with OUTC.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for p in out:
            q={k:p.get(k) for k in fields};q['review_flags']=';'.join(p['review_flags']);w.writerow(q)
    print(json.dumps(payload['qa'],ensure_ascii=False,indent=2))

if __name__=='__main__':main()
