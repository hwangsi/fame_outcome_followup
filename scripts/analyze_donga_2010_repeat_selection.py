#!/usr/bin/env python3
import json, math
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean

ROOT=Path(__file__).resolve().parents[1]
TYPEA=ROOT/'data/typeA'
MASTER=TYPEA/'donga_2010_post_t0_peak_master_v1_2.json'
ROSTER11=TYPEA/'donga_2011_100_roster_v0_1.json'
OUT_JSON=ROOT/'analysis/donga_2010_repeat_selection_metrics_v0_1.json'
OUT_MD=ROOT/'analysis/donga_2010_repeat_selection_analysis_v0_1.md'


def fisher_two_sided(a,b,c,d):
    # table [[a,b],[c,d]], fixed margins
    n=a+b+c+d; r1=a+b; c1=a+c
    lo=max(0, r1-(n-c1)); hi=min(r1,c1)
    def prob(x):
        return math.comb(c1,x)*math.comb(n-c1,r1-x)/math.comb(n,r1)
    p0=prob(a)
    return min(1.0, sum(prob(x) for x in range(lo,hi+1) if prob(x) <= p0 + 1e-15))


def effect(hit_r,n_r,hit_s,n_s):
    rr=(hit_r/n_r)/(hit_s/n_s) if hit_s else None
    rd=hit_r/n_r-hit_s/n_s
    a=hit_r; b=n_r-hit_r; c=hit_s; d=n_s-hit_s
    if b*c:
        odds=(a*d)/(b*c)
    elif a*d and not b*c:
        odds=float('inf')
    else:
        odds=None
    return {
        'repeat_rate':hit_r/n_r,'single_rate':hit_s/n_s,
        'rate_difference':rd,'risk_ratio':rr,'odds_ratio':odds,
        'fisher_two_sided_p':fisher_two_sided(a,b,c,d)
    }


def summarize(rows):
    n=len(rows)
    return {
        'n':n,
        'baseline_score_counts':{str(k):v for k,v in sorted(Counter(r['baseline_peak_through_t0'] for r in rows).items())},
        'mean_baseline_peak':mean(r['baseline_peak_through_t0'] for r in rows),
        'mean_t0_scope':mean(r['t0_snapshot_scope_score'] for r in rows),
        'post_t0_score_counts':{str(k):v for k,v in sorted(Counter(r['post_t0_peak_score'] for r in rows).items())},
        'major_ge3_n':sum(r['post_t0_peak_score']>=3 for r in rows),
        'major_ge3_rate':sum(r['post_t0_peak_score']>=3 for r in rows)/n,
        'apex_eq4_n':sum(r['post_t0_peak_score']==4 for r in rows),
        'apex_eq4_rate':sum(r['post_t0_peak_score']==4 for r in rows)/n,
        'advanced_n':sum(r['advancement_class']=='advanced' for r in rows),
        'advanced_rate':sum(r['advancement_class']=='advanced' for r in rows)/n,
        'sustained_high_n':sum(r['advancement_class']=='sustained_high' for r in rows),
        'no_clear_advancement_n':sum(r['advancement_class']=='no_clear_advancement' for r in rows),
        'death_truncated_n':sum(bool(r['exposure_truncated_by_death']) for r in rows)
    }


def pct(x): return f'{100*x:.1f}%'

def f3(x): return f'{x:.3f}' if x is not None and math.isfinite(x) else ('inf' if x==float('inf') else 'NA')


def main():
    master=json.loads(MASTER.read_text(encoding='utf-8'))
    rows=master['people']
    assert len(rows)==100 and master['qa']['unresolved']==0
    r11=json.loads(ROSTER11.read_text(encoding='utf-8'))
    names11=set(sum(r11['categories'].values(),[]))
    names10={r['name'] for r in rows}
    repeat=names10 & names11
    assert len(repeat)==38, len(repeat)

    for r in rows:
        r['repeat_2011']=r['name'] in repeat
    rr=[r for r in rows if r['repeat_2011']]
    ss=[r for r in rows if not r['repeat_2011']]
    assert len(rr)==38 and len(ss)==62

    sr=summarize(rr); ssumm=summarize(ss)
    effects={}
    for key,label in [('major_ge3_n','major_ge3'),('apex_eq4_n','apex_eq4'),('advanced_n','advanced')]:
        effects[label]=effect(sr[key],sr['n'],ssumm[key],ssumm['n'])

    baseline_strata={}
    for score in [1,2,3,4]:
        a=[r for r in rr if r['baseline_peak_through_t0']==score]
        b=[r for r in ss if r['baseline_peak_through_t0']==score]
        baseline_strata[str(score)]={
            'repeat':summarize(a) if a else {'n':0},
            'single':summarize(b) if b else {'n':0}
        }
        if a and b:
            baseline_strata[str(score)]['effects']={
                'major_ge3':effect(sum(r['post_t0_peak_score']>=3 for r in a),len(a),sum(r['post_t0_peak_score']>=3 for r in b),len(b)),
                'advanced':effect(sum(r['advancement_class']=='advanced' for r in a),len(a),sum(r['advancement_class']=='advanced' for r in b),len(b))
            }

    category={}
    cats=list(dict.fromkeys(r['category'] for r in rows))
    for cat in cats:
        a=[r for r in rr if r['category']==cat]; b=[r for r in ss if r['category']==cat]
        category[cat]={'repeat':summarize(a) if a else {'n':0},'single':summarize(b) if b else {'n':0}}
        if a and b:
            category[cat]['effects']={
                'major_ge3':effect(sum(r['post_t0_peak_score']>=3 for r in a),len(a),sum(r['post_t0_peak_score']>=3 for r in b),len(b)),
                'advanced':effect(sum(r['advancement_class']=='advanced' for r in a),len(a),sum(r['advancement_class']=='advanced' for r in b),len(b))
            }

    # Baseline >=3 is an important confounding signal.
    baseline_high_r=sum(r['baseline_peak_through_t0']>=3 for r in rr)
    baseline_high_s=sum(r['baseline_peak_through_t0']>=3 for r in ss)
    baseline_effect=effect(baseline_high_r,len(rr),baseline_high_s,len(ss))

    out={
        'schema_version':'donga_2010_2011_repeat_selection_metrics_v0.1',
        'generated':'2026-08-18',
        'cohort':'Dong-A 2010 100-person cohort; exposure = selected again in official 2011 100-person roster',
        'repeat_definition':'exact name intersection of canonical 2010 roster and official 2011 roster',
        'repeat_n':38,'single_2010_only_n':62,
        'repeat_names':sorted(repeat),
        'groups':{'repeat_2010_2011':sr,'selected_2010_only':ssumm},
        'unadjusted_effects':effects,
        'baseline_high_ge3_comparison':{
            'repeat_n':baseline_high_r,'single_n':baseline_high_s,
            **baseline_effect
        },
        'by_baseline_score':baseline_strata,
        'by_editorial_category':category,
        'guardrails':[
            'Repeat selection is an observational editorial exposure, not randomized treatment.',
            'Repeat-selected people may already have higher baseline scope; unadjusted post-T0 attainment differences therefore are not pure forecasting effects.',
            'Advancement above preselection lifetime peak is less mechanically driven by baseline status than absolute major attainment, but remains observational.',
            'The 2011 selection occurs about one year after the 2010 selection, so some early post-2010 achievements may influence repeat selection; reverse causation is possible.'
        ]
    }
    OUT_JSON.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

    lines=[]
    lines += ['# 동아일보 2010↔2011 반복선정 효과 분석 v0.1','',
              '**분석일:** 2026-08-18  ',
              '**Exposure:** 2010 선정자 중 2011에도 다시 선정되었는가  ',
              '**Repeat:** 38명 / **2010-only:** 62명','',
              '## 1. Unadjusted comparison','',
              '| 지표 | 2년 연속 38명 | 2010-only 62명 | 차이 | RR | Fisher p |','|---|---:|---:|---:|---:|---:|']
    labels=[('major_ge3','Post-T0 scope≥3','major_ge3_n'),('apex_eq4','Apex=4','apex_eq4_n'),('advanced','Baseline 초과 상승','advanced_n')]
    for ek,lab,nkey in labels:
        e=effects[ek]
        lines.append(f"| {lab} | {sr[nkey]}/{sr['n']} ({pct(e['repeat_rate'])}) | {ssumm[nkey]}/{ssumm['n']} ({pct(e['single_rate'])}) | {100*e['rate_difference']:+.1f}%p | {f3(e['risk_ratio'])} | {f3(e['fisher_two_sided_p'])} |")
    lines += ['', '## 2. Baseline imbalance', '',
              f"반복선정군에서 선정 이전 baseline scope≥3는 **{baseline_high_r}/{len(rr)} ({pct(baseline_high_r/len(rr))})**, 2010-only군은 **{baseline_high_s}/{len(ss)} ({pct(baseline_high_s/len(ss))})**이다.",
              '', f"Baseline-high risk ratio = **{f3(baseline_effect['risk_ratio'])}**, Fisher p = **{f3(baseline_effect['fisher_two_sided_p'])}**.",
              '', '따라서 반복선정군의 절대 major-attainment가 높더라도 이를 곧바로 “두 번 뽑은 것이 더 정확했다”로 해석하면 안 된다. 반복선정 자체가 이미 높은 baseline을 가진 사람을 다시 고른 결과일 수 있다.',
              '', '## 3. Baseline score별 비교','',
              '| baseline | repeat n | repeat major | repeat advanced | single n | single major | single advanced |','|---:|---:|---:|---:|---:|---:|---:|']
    for score in ['1','2','3','4']:
        x=baseline_strata[score]; a=x['repeat']; b=x['single']
        def cell(s,k): return f"{s.get(k,0)}/{s.get('n',0)}" if s.get('n',0) else '-'
        lines.append(f"| {score} | {a.get('n',0)} | {cell(a,'major_ge3_n')} | {cell(a,'advanced_n')} | {b.get('n',0)} | {cell(b,'major_ge3_n')} | {cell(b,'advanced_n')} |")
    lines += ['', '## 4. 분야별 exploratory comparison','',
              '| category | repeat n | repeat major | repeat advanced | single n | single major | single advanced |','|---|---:|---:|---:|---:|---:|---:|']
    for cat,x in category.items():
        a=x['repeat']; b=x['single']
        lines.append(f"| {cat} | {a.get('n',0)} | {cell(a,'major_ge3_n')} | {cell(a,'advanced_n')} | {b.get('n',0)} | {cell(b,'major_ge3_n')} | {cell(b,'advanced_n')} |")
    lines += ['', '## 5. Interpretation guardrails','',
              '- 2011 반복선정은 무작위 exposure가 아니다.',
              '- 2010 선정 후 약 1년 동안의 초기 성취가 2011 재선정에 영향을 줄 수 있으므로 reverse causation이 가능하다.',
              '- 따라서 unadjusted repeat vs single 차이는 editorial persistence와 baseline strength가 섞인 값이다.',
              '- 진짜 추가 예측정보를 보려면 baseline score 및 분야를 통제하거나 matched analysis가 필요하다.',
              '', '## 6. Reproducibility','',
              '- 2010 final master: `data/typeA/donga_2010_post_t0_peak_master_v1_2.json` (builder runtime)',
              '- 2011 official roster: `data/typeA/donga_2011_100_roster_v0_1.json`',
              '- analyzer: `scripts/analyze_donga_2010_repeat_selection.py`',
              '- metrics output: `analysis/donga_2010_repeat_selection_metrics_v0_1.json`']
    OUT_MD.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps({
        'repeat_n':38,'single_n':62,
        'repeat':sr,'single':ssumm,
        'effects':effects,'baseline_high_ge3':{'repeat_n':baseline_high_r,'single_n':baseline_high_s,**baseline_effect}
    },ensure_ascii=False,indent=2))

if __name__=='__main__': main()
