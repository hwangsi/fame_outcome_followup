#!/usr/bin/env python3
import json
from pathlib import Path

# QA trigger revision: 1
ROOT=Path(__file__).resolve().parents[1]
REC=ROOT/'research/khan_2005_korea_leaders60_recovery_v0_1.json'
COMMON=ROOT/'data/typeA/typeA_common_master_v0_3.json'
OUT=ROOT/'analysis/khan_2005_leaders60_person_overlap_v0_1.json'


def main():
    r=json.loads(REC.read_text(encoding='utf-8'))
    c=json.loads(COMMON.read_text(encoding='utf-8'))
    units=r['units']
    assert len(units)==60
    assert sum(u['unit_type']=='person' for u in units)==57
    assert sum(u['unit_type']=='organization' for u in units)==3

    fields={}
    for u in units: fields.setdefault(u['field'],[]).append(u)
    assert set(fields)=={'정치','경제','과학기술','사회교육','대중문화','문화예술'}
    assert all(len(v)==10 for v in fields.values())
    assert all(u['unit_type']=='person' for u in fields['정치'])

    common_by_name={}
    for p in c['people']:
        common_by_name.setdefault(p['name'],[]).append(p)

    overlaps=[]
    new_people=[]
    for u in [x for x in units if x['unit_type']=='person']:
        name=u['canonical_name']
        hits=common_by_name.get(name,[])
        if hits:
            overlaps.append({
              'field':u['field'],'printed_name':u['printed_name'],'canonical_name':name,
              'identity_key_hint':u.get('identity_key_hint'),
              'existing_matches':[
                {'person_id':p['person_id'],'identity_key':p.get('identity_key',p['name']),
                 'name':p['name'],'outlets':p['outlets'],'selection_years':p['selection_years'],
                 'cohort_units':p['cohort_units'],'placement_count':p['placement_count']}
                for p in hits
              ],
              'identity_status':'requires_confirmation_before_merge'
            })
        else:
            new_people.append({'field':u['field'],'printed_name':u['printed_name'],'canonical_name':name})

    pol_names={u['canonical_name'] for u in fields['정치']}
    pol_overlap=sorted(pol_names & set(common_by_name))
    assert pol_overlap==['강금실','김부겸','노회찬','박근혜','박진','원희룡','이명박','정동영'], pol_overlap
    assert sorted(pol_names-set(common_by_name))==['김근태','손학규']

    out={
      'schema_version':'khan_2005_leaders60_person_overlap_v0.1','generated':'2026-08-18',
      'source_recovery':'research/khan_2005_korea_leaders60_recovery_v0_1.json',
      'existing_common':'typeA_common_master_v0.3',
      'population':{'selected_units':60,'person_units':57,'organization_units':3,'existing_common_persons':193},
      'person_name_overlap_n':len(overlaps),'person_name_new_n':len(new_people),
      'overlap_names':sorted({x['canonical_name'] for x in overlaps}),
      'overlaps':sorted(overlaps,key=lambda x:(x['field'],x['canonical_name'])),
      'new_people':sorted(new_people,key=lambda x:(x['field'],x['canonical_name'])),
      'politics10':{
        'n':10,'all_person':True,'overlap_n':8,'new_n':2,
        'overlap_names':pol_overlap,'new_names':['김근태','손학규'],
        'eligible_for_field_specific_outcome_audit':True
      },
      'guardrails':[
        'Name overlap is an identity candidate only; same-person merge requires contemporaneous-role confirmation.',
        'CJ vice-chair 이미경 should resolve to the existing business identity rather than the politician identity.',
        'Organizations are excluded from this person-overlap audit but remain in the original 60-unit denominator.',
        'The politics10 field can proceed to Type-A person outcome audit independently, labeled as a field-specific secondary analysis.'
      ]
    }
    OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
