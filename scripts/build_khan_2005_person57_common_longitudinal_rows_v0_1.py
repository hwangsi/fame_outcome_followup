#!/usr/bin/env python3
import hashlib, json
from collections import Counter, defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
FILES=[
 ('정치',ROOT/'research/khan_2005_politics10_longitudinal_audit_v0_1.json'),
 ('경제',ROOT/'research/khan_2005_economy_person9_longitudinal_audit_v0_1.json'),
 ('과학기술',ROOT/'research/khan_2005_scitech_person9_longitudinal_audit_v0_1.json'),
 ('사회교육',ROOT/'research/khan_2005_socialedu_person9_longitudinal_audit_v0_1.json'),
 ('대중문화',ROOT/'research/khan_2005_popculture10_longitudinal_audit_v0_1.json'),
 ('문화예술',ROOT/'research/khan_2005_cultureart10_longitudinal_audit_v0_1.json'),
]
OUT=ROOT/'data/typeA/khan_2005_korea_leaders60_person57_common_longitudinal_rows_v0_1.json'
MET=ROOT/'data/typeA/khan_2005_korea_leaders60_person57_longitudinal_metrics_v1_1.json'
FREEZE=ROOT/'state/khan_2005_korea_leaders60_person57_longitudinal_freeze_v1_1.json'


def pid(identity_key):
    return 'ko-'+hashlib.sha256(identity_key.encode('utf-8')).hexdigest()[:12]

def sid(name,identity_key,w):
    return 'snap-'+hashlib.sha256(f'경향신문|khan_2005_korea_leaders60_person57|{identity_key}|{w}'.encode()).hexdigest()[:16]

def main():
    people=[]; seen=set(); rows=[]; by_field={}
    for field,path in FILES:
        d=json.loads(path.read_text(encoding='utf-8'))
        pp=d['people']; by_field[field]={'person_n':len(pp),'source_ref':str(path.relative_to(ROOT))}
        for p in pp:
            name=p['name']; ik=p.get('identity_key') or name
            assert (name,ik) not in seen,(field,name,ik)
            seen.add((name,ik)); people.append((name,ik,field))
            for w,target,start,end in [('t10',2015,'2014-01-01','2016-12-31'),('t20',2025,'2024-01-01','2026-12-31')]:
                s=p[w]; score=s.get('scope_score')
                if score is None:
                    status='competing_event' if s.get('match')=='competing_event' or p.get('death_truncated') else 'untraceable'
                else:
                    status='assessable'
                rows.append({
                  'snapshot_id':sid(name,ik,w),'person_id':pid(ik),'identity_key':ik,'name':name,'outlet':'경향신문',
                  'cohort_unit':'khan_2005_korea_leaders60_person57','parent_selection':'khan_2005_korea_leaders60',
                  'field':field,'selection_year':2005,'window_id':w,'target_year':target,'window_start':start,'window_end':end,
                  'status':status,'scope_score':score,'scope_ge2':(score>=2) if score is not None else None,
                  'major_ge3':(score>=3) if score is not None else None,'apex_eq4':(score==4) if score is not None else None,
                  'role_at_window':s.get('role'),'evidence_date':s.get('evidence_date'),'match':s.get('match'),
                  'confidence':s.get('confidence'),'evidence_refs':s.get('sources') or [],'source_ref':str(path.relative_to(ROOT))
                })
    assert len(people)==57 and len(rows)==114
    assert len({r['snapshot_id'] for r in rows})==114
    assert any(r['identity_key']=='이미경|cj_enm_business' for r in rows), 'CJ 이미경 identity key lost'
    snaps={}
    for w in ['t10','t20']:
        rr=[r for r in rows if r['window_id']==w]; assessed=[r for r in rr if r['status']=='assessable']
        sc=Counter(r['scope_score'] for r in assessed); ce=sum(r['status']=='competing_event' for r in rr)
        snaps[w]={
          'person_n':57,'assessable_n':len(assessed),'competing_event_n':ce,'untraceable_n':sum(r['status']=='untraceable' for r in rr),
          'score_distribution':{str(k):sc.get(k,0) for k in range(5)}|{'null':57-len(assessed)},
          'scope_ge2_n':sum(r['scope_ge2'] is True for r in rr),'major_ge3_n':sum(r['major_ge3'] is True for r in rr),
          'apex_eq4_n':sum(r['apex_eq4'] is True for r in rr)
        }
    assert snaps['t10']=={'person_n':57,'assessable_n':54,'competing_event_n':3,'untraceable_n':0,'score_distribution':{'0':0,'1':4,'2':23,'3':24,'4':3,'null':3},'scope_ge2_n':50,'major_ge3_n':27,'apex_eq4_n':3},snaps['t10']
    assert snaps['t20']=={'person_n':57,'assessable_n':52,'competing_event_n':5,'untraceable_n':0,'score_distribution':{'0':0,'1':9,'2':17,'3':16,'4':10,'null':5},'scope_ge2_n':43,'major_ge3_n':26,'apex_eq4_n':10},snaps['t20']
    # field reconciliation from current audits
    for field in by_field:
        fr=[r for r in rows if r['field']==field]
        by_field[field]['t10']={'assessable_n':sum(r['window_id']=='t10' and r['status']=='assessable' for r in fr),'major_ge3_n':sum(r['window_id']=='t10' and r['major_ge3'] is True for r in fr),'apex_eq4_n':sum(r['window_id']=='t10' and r['apex_eq4'] is True for r in fr)}
        by_field[field]['t20']={'assessable_n':sum(r['window_id']=='t20' and r['status']=='assessable' for r in fr),'major_ge3_n':sum(r['window_id']=='t20' and r['major_ge3'] is True for r in fr),'apex_eq4_n':sum(r['window_id']=='t20' and r['apex_eq4'] is True for r in fr)}
    rows.sort(key=lambda r:(r['window_id'],r['field'],r['name']))
    qa={'persons':57,'snapshot_rows':114,'unique_snapshot_ids':114,'t10':snaps['t10'],'t20':snaps['t20'],'identity_key_cj_lee_preserved':True,'source_field_audits':6}
    payload={'schema_version':'khan_2005_korea_leaders60_person57_common_longitudinal_rows_v0.1','generated':'2026-08-18','status':'row_normalized_from_current_six_field_audits','qa':qa,'rows':rows}
    metrics={'schema_version':'khan_2005_korea_leaders60_person57_longitudinal_metrics_v1.1','generated':'2026-08-18','status':'corrected_after_scitech_shin_heesup_t20_retirement','parent_selection':'khan_2005_korea_leaders60','original_selected_units':60,'person_units':57,'organization_units':3,'analysis_type':'prespecified_person_only_secondary','snapshots':snaps,'by_field':by_field,'correction_from_v1_0':{'t20_score1':{'old':8,'new':9},'t20_score3':{'old':17,'new':16},'t20_scope_ge2_n':{'old':44,'new':43},'t20_major_ge3_n':{'old':27,'new':26},'reason':'Shin Hee-sup T20 corrected from scope3 to scope1 after official IBS retirement evidence; v1.0 aggregate was not regenerated after the field correction.'},'guardrails':['Person57 is a secondary person-only analysis of a mixed 60-unit selection.','Organizations remain outside person scope scores.','Deaths are competing events.','Current six field audits are authoritative over stale pre-correction aggregate.']}
    freeze={'schema_version':'khan_2005_korea_leaders60_person57_longitudinal_freeze_v1.1','generated':'2026-08-18','qa':qa,'metrics_ref':str(MET.relative_to(ROOT)),'rows_ref':str(OUT.relative_to(ROOT)),'supersedes':'data/typeA/khan_2005_korea_leaders60_person57_longitudinal_metrics_v1_0.json','reason':'reconciled to corrected science-tech audit'}
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    MET.write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    FREEZE.write_text(json.dumps(freeze,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(freeze,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
