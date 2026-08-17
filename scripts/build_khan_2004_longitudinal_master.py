#!/usr/bin/env python3
import json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PEAK=ROOT/'data/typeA/khan_2004_17th_assembly_newleaders_peak_master_v1_0.json'
B1=ROOT/'research/khan_2004_longitudinal_uri_batch1_v0_1.json'
B2=ROOT/'research/khan_2004_longitudinal_gnp_dlp_batch2_v0_1.json'
OUT=ROOT/'data/typeA/khan_2004_17th_assembly_newleaders_longitudinal_master_v1_0.json'
METRICS=ROOT/'data/typeA/khan_2004_17th_assembly_newleaders_longitudinal_metrics_v1_0.json'
FREEZE=ROOT/'state/khan_2004_17th_assembly_newleaders_longitudinal_freeze_v1_0.json'
RESULT=ROOT/'state/khan_2004_17th_assembly_newleaders_longitudinal_result_v1_0.md'


def dist(rows, field):
    c=Counter()
    for p in rows:
        s=p[field]['scope_score']
        c['null' if s is None else str(s)] += 1
    return {k:c.get(k,0) for k in ['0','1','2','3','4','null']}


def snap_metrics(rows, field):
    assess=[p for p in rows if p[field]['scope_score'] is not None]
    return {
      'assessable_n':len(assess),
      'competing_event_n':len(rows)-len(assess),
      'score_distribution':dist(rows,field),
      'scope_ge2_n':sum(p[field]['scope_score'] is not None and p[field]['scope_score']>=2 for p in rows),
      'scope_ge2_rate_assessable':sum(p[field]['scope_score'] is not None and p[field]['scope_score']>=2 for p in rows)/len(assess),
      'major_ge3_n':sum(p[field]['scope_score'] is not None and p[field]['scope_score']>=3 for p in rows),
      'major_ge3_rate_assessable':sum(p[field]['scope_score'] is not None and p[field]['scope_score']>=3 for p in rows)/len(assess)
    }


def main():
    peak=json.loads(PEAK.read_text(encoding='utf-8'))
    b1=json.loads(B1.read_text(encoding='utf-8'))
    b2=json.loads(B2.read_text(encoding='utf-8'))
    snap=b1['people']+b2['people']
    assert len(snap)==20 and len({p['name'] for p in snap})==20
    peaks={p['name']:p for p in peak['people']}
    assert set(peaks)=={p['name'] for p in snap}

    # Recompute and validate batch QA rather than trusting manually entered summary counts.
    assert b1['qa']['t10_score_distribution']=={'1':0,'2':7,'3':3,'4':0}
    assert b1['qa']['t20_score_distribution']=={'1':5,'2':3,'3':2,'4':0}
    assert b1['qa']['current_score_distribution']=={'1':4,'2':5,'3':1,'4':0}
    assert b2['qa']['t10_score_distribution']=={'1':1,'2':5,'3':4,'4':0,'null':0}
    assert b2['qa']['t20_score_distribution']=={'1':1,'2':3,'3':4,'4':0,'null':2}
    assert b2['qa']['current_score_distribution']=={'1':3,'2':4,'3':1,'4':0,'null':2}

    people=[]
    for s in snap:
        p=peaks[s['name']]
        x={
          'name':s['name'],'party_t0':p['party_t0'],'selection_date':'2004-05-05',
          'baseline_peak_through_t0':p['baseline_peak_through_t0'],
          'post_t0_peak_score':p['post_t0_peak_score'],'post_t0_peak_role':p['post_t0_peak_role'],
          'post_t0_peak_year':p['post_t0_peak_year'],'advancement_delta':p['advancement_delta'],
          'advancement_class':p['advancement_class'],'t10':s['t10'],'t20':s['t20'],'current':s['current'],
          'death_truncated':bool(s.get('death_truncated',False)),
          'identity_key':s.get('identity_key')
        }
        x['t10_major_ge3']=s['t10']['scope_score'] is not None and s['t10']['scope_score']>=3
        x['t20_major_ge3']=s['t20']['scope_score'] is not None and s['t20']['scope_score']>=3
        x['current_major_ge3']=s['current']['scope_score'] is not None and s['current']['scope_score']>=3
        people.append(x)
    people.sort(key=lambda p:p['name'])

    sm={k:snap_metrics(people,k) for k in ['t10','t20','current']}
    assert sm['t10']['score_distribution']=={'0':0,'1':1,'2':12,'3':7,'4':0,'null':0}
    assert sm['t20']['score_distribution']=={'0':0,'1':6,'2':6,'3':6,'4':0,'null':2}
    assert sm['current']['score_distribution']=={'0':0,'1':7,'2':9,'3':2,'4':0,'null':2}
    assert (sm['t10']['major_ge3_n'],sm['t20']['major_ge3_n'],sm['current']['major_ge3_n'])==(7,6,2)

    alive_current=[p for p in people if p['current']['scope_score'] is not None]
    assert len(alive_current)==18
    ever_advanced_alive=sum(p['advancement_class']=='advanced' for p in alive_current)
    assert ever_advanced_alive==18
    advanced_but_current_below3=sum(p['advancement_class']=='advanced' and p['current']['scope_score']<3 for p in alive_current)
    assert advanced_but_current_below3==16
    advanced_but_current_scope1=sum(p['advancement_class']=='advanced' and p['current']['scope_score']==1 for p in alive_current)
    assert advanced_but_current_scope1==7

    death_names=sorted(p['name'] for p in people if p['death_truncated'])
    assert death_names==['노회찬','박세일']
    low_current=sorted(p['name'] for p in people if p['current']['confidence']=='L')
    assert low_current==['신기남','심재철','전재희','천정배']

    metrics={
      'schema_version':'khan_2004_17th_assembly_newleaders_longitudinal_metrics_v1.0',
      'generated':'2026-08-18','population':{'n':20,'death_truncated_n':2,'current_assessable_n':18},
      'peak_outcomes':peak['metrics']['outcomes'],
      'snapshots':sm,
      'trajectory_contrast':{
        'ever_advanced_n_full':sum(p['advancement_class']=='advanced' for p in people),
        'ever_advanced_rate_full':sum(p['advancement_class']=='advanced' for p in people)/20,
        'ever_advanced_alive_current_n':ever_advanced_alive,
        'alive_current_n':len(alive_current),
        'advanced_alive_but_current_below_major_n':advanced_but_current_below3,
        'advanced_alive_but_current_scope1_n':advanced_but_current_scope1,
        't20_major_among_assessable':{'n':sm['t20']['major_ge3_n'],'denominator':sm['t20']['assessable_n'],'rate':sm['t20']['major_ge3_rate_assessable']},
        'current_major_among_assessable':{'n':sm['current']['major_ge3_n'],'denominator':sm['current']['assessable_n'],'rate':sm['current']['major_ge3_rate_assessable']},
        'interpretation':'Ever-advancement and fixed-time persistence answer different questions: most selected people rose above baseline at some point, but far fewer occupied scope>=3 roles at T+20 or current.'
      },
      'death_truncated_names':death_names,
      'current_low_confidence_names':low_current,
      'guardrails':[
        'Do not replace lifetime peak with target-year snapshot or vice versa.',
        'Death after selection is a competing event; post-death snapshots are null rather than failures.',
        'Current former-officeholder status does not inherit an earlier minister/governor/presidential-candidate score.',
        'Fixed-time scope>=3 persistence is descriptive and sensitive to retirement, election cycles, career switching and age.',
        'Four current rows have low confidence and should be sensitivity-audited if current-status inference becomes primary.'
      ]
    }
    master={
      'schema_version':'khan_2004_17th_assembly_newleaders_longitudinal_master_v1.0',
      'generated':'2026-08-18','status':'t10_t20_current_complete_20_of_20',
      'target_windows':{'t10':'2014 ±1 year','t20':'2024 ±1 year','current':'2026-08-18'},
      'metrics':metrics,'people':people,
      'source_batches':[str(B1.relative_to(ROOT)),str(B2.relative_to(ROOT))]
    }
    freeze={
      'schema_version':'khan_2004_17th_assembly_newleaders_longitudinal_freeze_v1.0','generated':'2026-08-18',
      'population':metrics['population'],'peak_outcomes':metrics['peak_outcomes'],'snapshots':metrics['snapshots'],
      'trajectory_contrast':metrics['trajectory_contrast'],'death_truncated_names':death_names,
      'current_low_confidence_names':low_current,'guardrails':metrics['guardrails']
    }
    result=f'''# 경향신문 2004 「17代국회 이끌 뉴리더」 longitudinal result v1.0\n\n- 기준일: **2026-08-18**\n- 선정자: **20명**\n- peak outcome 완료: **20/20**\n- T+10 / T+20 / current snapshot: **20/20**\n- death competing events: **2명 — 노회찬, 박세일**\n\n## 1. Ever-peak outcome\n\n- Major: **20/20 = 100%**\n- Apex: **4/20 = 20%**\n- Advanced: **19/20 = 95%**\n\n## 2. Fixed-time snapshots\n\n| window | assessable | scope1 | scope2 | scope>=3 | competing event |\n|---|---:|---:|---:|---:|---:|\n| T+10 (2014±1) | 20 | 1 | 12 | **7 (35.0%)** | 0 |\n| T+20 (2024±1) | 18 | 6 | 6 | **6 (33.3%)** | 2 |\n| Current (2026) | 18 | 7 | 9 | **2 (11.1%)** | 2 |\n\n## 3. 핵심 해석\n\n**19/20이 언젠가 baseline을 넘어섰다는 사실과, 20년 뒤에도 최고위 정치 역할을 유지한다는 것은 전혀 다른 질문이다.**\n\n현재 살아 있는 18명은 모두 선정 이후 한 번 이상 baseline을 넘어섰지만, 2026 현재 scope≥3 역할은 2명뿐이다. 16명은 과거 상승 peak 이후 현재는 scope<3이며, 그중 7명은 scope1이다.\n\n따라서 경향 2004의 높은 95% advancement는 “eventual rise identification”의 강한 신호로 읽을 수 있지만 **persistent elite occupancy 20년 예측**으로 읽으면 안 된다.\n\n## 4. Competing event\n\n박세일(2017)과 노회찬(2018)은 T+20/current 이전에 별세했다. 두 사람의 이후 snapshot은 `null`이며 실패로 세지 않는다.\n\n## 5. Guardrail\n\npeak, T+10, T+20, current를 별도 축으로 유지한다. 전직 장관·도지사·대통령 후보라는 과거 peak를 현재 snapshot에 자동 승계하지 않는다.\n'''
    OUT.write_text(json.dumps(master,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    METRICS.write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    FREEZE.write_text(json.dumps(freeze,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    RESULT.write_text(result,encoding='utf-8')
    print(json.dumps(freeze,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
