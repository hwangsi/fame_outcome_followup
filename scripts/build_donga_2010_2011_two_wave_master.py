#!/usr/bin/env python3
import hashlib, json, os
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
M10=ROOT/'data/typeA/donga_2010_post_t0_peak_master_v1_2.json'
M11=ROOT/'analysis/donga_2011_post_t0_master_v1_0.json'
OUT=ROOT/'analysis/donga_2010_2011_two_wave_master_v0_1.json'
FREEZE_OUT=ROOT/'state/donga_2010_2011_two_wave_freeze_v0_1.json'
RESULT_OUT=ROOT/'state/donga_2010_2011_two_wave_result_v0_1.md'


def pid(name):
    return 'donga-' + hashlib.sha256(name.encode('utf-8')).hexdigest()[:12]


def placement_2010(r):
    return {
      'person_id':pid(r['name']),'name':r['name'],'selection_year':2010,'selection_cutoff':'2010-05-10',
      'category':r['category'],'repeat_next_wave':None,
      'baseline_peak_score':r['baseline_peak_through_t0'],
      'post_selection_peak_score':r['post_t0_peak_score'],'post_selection_peak_year':r['post_t0_peak_year'],
      'advancement_delta':r['advancement_delta'],'advancement_class':r['advancement_class'],
      'outcome_assessable':r['post_t0_peak_score'] is not None,
      'death_truncated':r['exposure_truncated_by_death'],'death_year':r['death_year'],
      'source_master':str(M10.relative_to(ROOT))
    }


def placement_2011(r):
    return {
      'person_id':pid(r['name']),'name':r['name'],'selection_year':2011,'selection_cutoff':'2011-04-01',
      'category':r['category'],'repeat_previous_wave':r['repeat_2010_2011'],
      'baseline_peak_score':r['baseline_2011'],
      'post_selection_peak_score':r['post2011_peak_score'],'post_selection_peak_year':r['post2011_peak_year'],
      'advancement_delta':r['advancement_delta'],'advancement_class':r['advancement_class'],
      'outcome_assessable':r['post2011_peak_score'] is not None,
      'death_truncated':r['exposure_truncated_by_death'],'death_year':r['death_year'],
      'source_master':str(M11.relative_to(ROOT))
    }


def main():
    d10=json.loads(M10.read_text(encoding='utf-8'))
    d11=json.loads(M11.read_text(encoding='utf-8'))
    p10={r['name']:r for r in d10['people']}; p11={r['name']:r for r in d11['people']}
    assert len(p10)==100 and len(p11)==100
    repeat11={r['name'] for r in d11['people'] if r['repeat_2010_2011']}
    intersection=set(p10)&set(p11)
    assert len(repeat11)==38
    assert intersection==repeat11, {'intersection_only':sorted(intersection-repeat11),'repeat_only':sorted(repeat11-intersection)}

    placements=[]
    for name,r in p10.items():
        x=placement_2010(r); x['repeat_next_wave']=name in repeat11; placements.append(x)
    for name,r in p11.items(): placements.append(placement_2011(r))
    assert len(placements)==200

    names=sorted(set(p10)|set(p11)); assert len(names)==162
    people=[]
    for name in names:
        in10=name in p10; in11=name in p11
        if in10 and in11: group='repeat_2010_2011'
        elif in10: group='2010_only'
        else: group='2011_new'
        pp=sorted([x for x in placements if x['name']==name],key=lambda x:x['selection_year'])
        first=pp[0]; last=pp[-1]
        first_peak=first['post_selection_peak_score']
        person={
          'person_id':pid(name),'name':name,'group':group,'placement_count':len(pp),
          'selection_years':[x['selection_year'] for x in pp],
          'first_selection_year':first['selection_year'],'last_selection_year':last['selection_year'],
          'baseline_at_first_selection':first['baseline_peak_score'],
          'first_selection_post_peak_score':first_peak,
          'first_selection_advancement_delta':first['advancement_delta'],
          'first_selection_advancement_class':first['advancement_class'],
          'first_selection_outcome_assessable':first['outcome_assessable'],
          'ever_major_after_first_selection':bool(first_peak is not None and first_peak>=3),
          'ever_apex_after_first_selection':bool(first_peak==4),
          'death_truncated_any':any(x['death_truncated'] for x in pp),
          'placements':pp,
        }
        if group=='repeat_2010_2011':
            a,b=pp
            person.update({
              'baseline_2010':a['baseline_peak_score'],'baseline_2011':b['baseline_peak_score'],
              'baseline_change_2010_to_2011':b['baseline_peak_score']-a['baseline_peak_score'],
              'category_2010':a['category'],'category_2011':b['category'],
              'category_same':a['category']==b['category'],
              'post2010_peak_score':a['post_selection_peak_score'],
              'post2011_peak_score':b['post_selection_peak_score'],
              'post_peak_score_change_between_windows':None if b['post_selection_peak_score'] is None else b['post_selection_peak_score']-a['post_selection_peak_score'],
              'advancement_class_2010':a['advancement_class'],'advancement_class_2011':b['advancement_class'],
            })
        people.append(person)

    groups=Counter(p['group'] for p in people)
    assert groups==Counter({'2010_only':62,'repeat_2010_2011':38,'2011_new':62}), groups
    repeats=[p for p in people if p['group']=='repeat_2010_2011']
    baseline_changes=Counter('up' if p['baseline_change_2010_to_2011']>0 else 'same' if p['baseline_change_2010_to_2011']==0 else 'down' for p in repeats)
    category_changes=Counter('same' if p['category_same'] else 'changed' for p in repeats)
    transition=Counter((p['advancement_class_2010'],p['advancement_class_2011']) for p in repeats)

    def group_summary(g):
        rr=[p for p in people if p['group']==g]
        ass=[p for p in rr if p['first_selection_outcome_assessable']]
        return {
          'n':len(rr),'first_selection_assessable_n':len(ass),
          'first_selection_major_n':sum(p['ever_major_after_first_selection'] for p in rr),
          'first_selection_major_rate_full':sum(p['ever_major_after_first_selection'] for p in rr)/len(rr),
          'first_selection_apex_n':sum(p['ever_apex_after_first_selection'] for p in rr),
          'first_selection_apex_rate_full':sum(p['ever_apex_after_first_selection'] for p in rr)/len(rr),
          'first_selection_advanced_n':sum(p['first_selection_advancement_class']=='advanced' for p in rr),
          'first_selection_advanced_rate_full':sum(p['first_selection_advancement_class']=='advanced' for p in rr)/len(rr),
          'first_selection_baseline_counts':dict(Counter(str(p['baseline_at_first_selection']) for p in rr)),
        }

    summaries={g:group_summary(g) for g in ['2010_only','repeat_2010_2011','2011_new']}
    qa={
      'placements_n':200,'unique_persons_n':162,'2010_placements_n':100,'2011_placements_n':100,
      'groups':dict(groups),'repeat_intersection_n':len(intersection),
      'repeat_baseline_change_counts':dict(baseline_changes),
      'repeat_category_change_counts':dict(category_changes),
      'repeat_advancement_transition_counts':{f'{a} -> {b}':n for (a,b),n in sorted(transition.items())},
    }
    out={
      'schema_version':'donga_2010_2011_two_wave_master_v0.1','generated':'2026-08-18',
      'status':'complete_two_wave_200_placements_162_persons',
      'source_masters':[str(M10.relative_to(ROOT)),str(M11.relative_to(ROOT))],
      'unit_definitions':{
        'placement':'one person appearing in one editorial selection wave; 200 rows total',
        'person':'one canonical individual across waves; 162 rows total',
        'repeat':'same frozen identity selected in both 2010 and 2011; 38 persons'
      },
      'qa':qa,'person_group_first_selection_summary':summaries,
      'guardrails':[
        'The 200 placements are not 200 independent people; 38 repeat persons contribute two placements each.',
        'Person-level first-selection outcomes use the post-selection window beginning at the person’s first wave: 2010 for 2010-only/repeat, 2011 for 2011-new.',
        'For repeat persons, post-2010 and post-2011 peak windows overlap in calendar time and their difference is descriptive, not a causal trajectory estimator.',
        'The name intersection between 2010 and 2011 must exactly equal the frozen 38-person repeat set; otherwise the build fails.'
      ],
      'placements':placements,'people':people,
    }
    OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

    freeze={
      'schema_version':'donga_2010_2011_two_wave_freeze_v0.1','generated':'2026-08-18',
      'status':'complete_two_wave_200_placements_162_persons',
      'source_master_ref':str(OUT.relative_to(ROOT)),
      'population':{'placements':200,'unique_persons':162,'groups':dict(groups)},
      'repeat_38':{
        'baseline_change_counts':dict(baseline_changes),
        'category_change_counts':dict(category_changes),
        'advancement_transition_counts':{f'{a} -> {b}':n for (a,b),n in sorted(transition.items())},
      },
      'person_group_first_selection_summary':summaries,
      'runtime_context':{'github_run_id':os.getenv('GITHUB_RUN_ID'),'github_sha':os.getenv('GITHUB_SHA')},
      'guardrails':out['guardrails'],
    }
    FREEZE_OUT.write_text(json.dumps(freeze,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

    def pct(x): return f'{100*x:.1f}%'
    lines=[
      '# 동아일보 2010–2011 two-wave longitudinal summary v0.1','',
      '- placements: **200**','- unique persons: **162**',
      '- 2010-only: **62**','- repeat 2010+2011: **38**','- 2011-new: **62**','',
      '## Person-level first-selection outcomes','',
      '| Group | N | Major | Apex | Advanced |','|---|---:|---:|---:|---:|'
    ]
    labels={'2010_only':'2010-only','repeat_2010_2011':'Repeat','2011_new':'2011-new'}
    for g in ['2010_only','repeat_2010_2011','2011_new']:
        s=summaries[g]
        lines.append(f"| {labels[g]} | {s['n']} | {s['first_selection_major_n']}/{s['n']} = {pct(s['first_selection_major_rate_full'])} | {s['first_selection_apex_n']}/{s['n']} = {pct(s['first_selection_apex_rate_full'])} | {s['first_selection_advanced_n']}/{s['n']} = {pct(s['first_selection_advanced_rate_full'])} |")
    lines += ['', '## Repeat 38 — 2010→2011 baseline change','', f"`{dict(baseline_changes)}`",'',
              '## Repeat 38 — category continuity','', f"`{dict(category_changes)}`",'',
              '## Repeat 38 — advancement-class transition','']
    for (a,b),n in sorted(transition.items()): lines.append(f'- `{a} → {b}`: **{n}**')
    lines += ['', '## Guardrails','',
              '- 200 placements are not 200 independent people; repeat 38 contribute two placements.',
              '- First-selection person outcomes start at 2010 for 2010-only/repeat and 2011 for 2011-new.',
              '- Repeat post-2010 and post-2011 outcome windows overlap, so their difference is descriptive rather than causal.','']
    RESULT_OUT.write_text('\n'.join(lines),encoding='utf-8')
    print(json.dumps({'qa':qa,'group_summary':summaries},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
