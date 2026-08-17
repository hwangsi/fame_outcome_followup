#!/usr/bin/env python3
import json, math
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TYPEA=ROOT/'data/typeA'
MASTER=TYPEA/'donga_2010_post_t0_peak_master_v1_2.json'
ROSTER11=TYPEA/'donga_2011_100_roster_v0_1.json'
OUTJ=ROOT/'analysis/donga_2010_repeat_selection_baseline_adjusted_v0_2.json'
OUTM=ROOT/'analysis/donga_2010_repeat_selection_baseline_adjusted_v0_2.md'

def fisher_two_sided(a,b,c,d):
    n=a+b+c+d; r1=a+b; c1=a+c
    lo=max(0,r1-(n-c1)); hi=min(r1,c1)
    def prob(x):
        return math.comb(c1,x)*math.comb(n-c1,r1-x)/math.comb(n,r1)
    p0=prob(a)
    return min(1.0,sum(prob(x) for x in range(lo,hi+1) if prob(x)<=p0+1e-15))

def rate(rows, pred):
    return sum(pred(r) for r in rows)/len(rows) if rows else None

def effect(rows_r, rows_s, pred):
    ar=sum(pred(r) for r in rows_r); nr=len(rows_r)
    ass=sum(pred(r) for r in rows_s); ns=len(rows_s)
    rr=ar/nr if nr else None; rs=ass/ns if ns else None
    if nr and ns:
        p=fisher_two_sided(ar,nr-ar,ass,ns-ass)
        rd=rr-rs
        risk_ratio=(rr/rs) if rs else (float('inf') if rr else None)
    else:
        p=rd=risk_ratio=None
    return {'repeat_n':nr,'repeat_hit_n':ar,'repeat_rate':rr,'single_n':ns,'single_hit_n':ass,'single_rate':rs,'rate_difference':rd,'risk_ratio':risk_ratio,'fisher_two_sided_p':p}

def main():
    m=json.loads(MASTER.read_text(encoding='utf-8'))
    assert m['qa']['total']==100 and m['qa']['unresolved']==0
    r11=json.loads(ROSTER11.read_text(encoding='utf-8'))
    names11=set(sum(r11['categories'].values(),[]))
    rows=[]
    for x in m['people']:
        r=dict(x); r['repeat_2011']=r['name'] in names11; rows.append(r)
    assert sum(r['repeat_2011'] for r in rows)==38

    strata={}
    for b in [1,2,3,4]:
        rr=[r for r in rows if r['baseline_peak_through_t0']==b and r['repeat_2011']]
        ss=[r for r in rows if r['baseline_peak_through_t0']==b and not r['repeat_2011']]
        strata[str(b)]={
            'repeat_n':len(rr),'single_n':len(ss),
            'major':effect(rr,ss,lambda r:r['post_t0_peak_score']>=3),
            'apex':effect(rr,ss,lambda r:r['post_t0_peak_score']==4),
            'advanced':effect(rr,ss,lambda r:r['advancement_class']=='advanced')
        }

    # Clinically/interpretable transitions by starting point.
    baseline2_major=strata['2']['major']
    baseline2_advanced=strata['2']['advanced']
    baseline3_apex=strata['3']['apex']
    baseline3_advanced=strata['3']['advanced']

    # Direct standardization over common baseline support 2/3 using full-cohort target weights.
    common=[r for r in rows if r['baseline_peak_through_t0'] in (2,3)]
    assert len(common)==96
    weights={b:sum(r['baseline_peak_through_t0']==b for r in common)/len(common) for b in (2,3)}
    standardized={}
    for label,pred in {
        'major':lambda r:r['post_t0_peak_score']>=3,
        'apex':lambda r:r['post_t0_peak_score']==4,
        'advanced':lambda r:r['advancement_class']=='advanced'
    }.items():
        rr_rate=0; ss_rate=0; details={}
        for b,w in weights.items():
            rr=[r for r in rows if r['baseline_peak_through_t0']==b and r['repeat_2011']]
            ss=[r for r in rows if r['baseline_peak_through_t0']==b and not r['repeat_2011']]
            assert rr and ss
            pr=rate(rr,pred); ps=rate(ss,pred)
            rr_rate+=w*pr; ss_rate+=w*ps
            details[str(b)]={'weight':w,'repeat_rate':pr,'single_rate':ps,'repeat_n':len(rr),'single_n':len(ss)}
        standardized[label]={'repeat_standardized_rate':rr_rate,'single_standardized_rate':ss_rate,'standardized_rate_difference':rr_rate-ss_rate,'risk_ratio':(rr_rate/ss_rate if ss_rate else None),'strata':details}

    # Category + baseline exact strata for advancement; standardize only strata with both exposure groups.
    cb=defaultdict(lambda:{'repeat':[],'single':[]})
    for r in rows:
        key=(r['category'],r['baseline_peak_through_t0'])
        cb[key]['repeat' if r['repeat_2011'] else 'single'].append(r)
    usable=[]
    excluded=[]
    for key,g in cb.items():
        if g['repeat'] and g['single']:
            usable.append((key,g))
        else:
            excluded.append((key,len(g['repeat']),len(g['single'])))
    support_n=sum(len(g['repeat'])+len(g['single']) for _,g in usable)
    # Weight by pooled stratum size among common-support observations.
    adv_rep=adv_sin=0
    stratum_details=[]
    for (cat,b),g in usable:
        n=len(g['repeat'])+len(g['single']); w=n/support_n
        pr=rate(g['repeat'],lambda r:r['advancement_class']=='advanced')
        ps=rate(g['single'],lambda r:r['advancement_class']=='advanced')
        adv_rep+=w*pr; adv_sin+=w*ps
        stratum_details.append({'category':cat,'baseline':b,'weight':w,'repeat_n':len(g['repeat']),'single_n':len(g['single']),'repeat_advanced_rate':pr,'single_advanced_rate':ps})
    catbase_std={'support_n':support_n,'usable_strata_n':len(usable),'excluded_strata':excluded,'repeat_standardized_advanced_rate':adv_rep,'single_standardized_advanced_rate':adv_sin,'standardized_rate_difference':adv_rep-adv_sin,'strata':stratum_details}

    out={
      'schema_version':'donga_2010_repeat_selection_baseline_adjusted_v0.2','generated':'2026-08-18',
      'cohort':'Dong-A 2010 100-person cohort; repeat exposure = exact-name selection again in 2011 roster',
      'baseline_strata':strata,
      'key_transition_tests':{
        'baseline2_to_major_ge3':baseline2_major,
        'baseline2_any_advancement':baseline2_advanced,
        'baseline3_to_apex4':baseline3_apex,
        'baseline3_any_advancement':baseline3_advanced
      },
      'baseline_standardized_common_support_2_3':{'support_n':96,'target_weights':{str(k):v for k,v in weights.items()},**standardized},
      'category_plus_baseline_standardized_advancement':catbase_std,
      'guardrails':[
        'Baseline standardization is descriptive adjustment, not causal identification.',
        'Baseline=1 has no repeat-selected person and baseline=4 has no 2010-only person, so the principal standardized comparison is restricted to common support baseline 2/3.',
        'The 2011 repeat decision occurs after roughly one year of post-2010 observation and can reflect early outcomes; reverse causation remains possible.',
        'Category+baseline standardization excludes strata lacking both repeat and single observations and therefore changes the target population.',
        'Small stratum sizes make exact p-values unstable; emphasize effect sizes and direction.'
      ]
    }
    OUTJ.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

    def pct(x): return 'NA' if x is None else f'{100*x:.1f}%'
    def num(x): return 'NA' if x is None else (f'{x:.3f}' if math.isfinite(x) else 'inf')
    lines=[
      '# 동아일보 2010↔2011 반복선정 baseline-adjusted 분석 v0.2','',
      '**작성일:** 2026-08-18  ',
      '**핵심 질문:** 이미 높은 사람이 반복선정된 효과를 줄이고도 repeat selection이 추가 상승 신호를 가지는가?','',
      '## 1. 가장 해석하기 쉬운 baseline별 전이','',
      '| 시작점 | outcome | repeat | 2010-only | 차이 | RR | Fisher p |','|---|---|---:|---:|---:|---:|---:|']
    for label,e in [
        ('baseline=2','scope≥3 진입',baseline2_major),('baseline=2','any advancement',baseline2_advanced),
        ('baseline=3','apex=4 진입',baseline3_apex),('baseline=3','any advancement',baseline3_advanced)]:
        lines.append(f"| {label} | {e['repeat_hit_n']}/{e['repeat_n']} vs {e['single_hit_n']}/{e['single_n']} | {pct(e['repeat_rate'])} | {pct(e['single_rate'])} | {pct(e['rate_difference'])} | {num(e['risk_ratio'])} | {num(e['fisher_two_sided_p'])} |")
    lines += ['', '## 2. Baseline 2/3 공통 support 직접표준화','',
              f"공통 support는 **96명**이다. baseline=2 가중치 {pct(weights[2])}, baseline=3 가중치 {pct(weights[3])}를 전체 common-support 분포에서 가져왔다.", '',
              '| outcome | repeat standardized | single standardized | 차이 | RR |','|---|---:|---:|---:|---:|']
    for k in ['major','apex','advanced']:
        z=standardized[k]
        lines.append(f"| {k} | {pct(z['repeat_standardized_rate'])} | {pct(z['single_standardized_rate'])} | {pct(z['standardized_rate_difference'])} | {num(z['risk_ratio'])} |")
    lines += ['', '## 3. Category + baseline 동시 표준화: advancement','',
              f"양쪽 exposure가 모두 존재하는 category×baseline strata에 한정한 support는 **{support_n}명**, usable strata는 **{len(usable)}개**다.",
              f"- repeat standardized advancement: **{pct(adv_rep)}**",
              f"- single standardized advancement: **{pct(adv_sin)}**",
              f"- difference: **{pct(adv_rep-adv_sin)}**",'',
              '이 비교는 baseline뿐 아니라 편집분야 구성 차이도 일부 줄이지만, 공통 support가 없는 strata를 제외하므로 전체 100명과 다른 target population이다.','',
              '## 4. 해석 원칙','',
              '- 조정 전 major/apex의 큰 repeat advantage는 baseline imbalance의 영향을 강하게 받는다.',
              '- 미래 성장 신호는 baseline=2의 major 진입, baseline=3의 apex 진입, 그리고 baseline-standardized advancement에서 판단한다.',
              '- 어떤 조정 결과도 인과효과로 부르면 안 된다. 2011 재선정 전에 이미 초기 post-2010 성취가 발생했을 수 있다.',
              '- 표본이 작은 strata가 많으므로 p-value보다 effect size와 일관성이 중요하다.','',
              '## 5. Reproducibility','',
              '- final 2010 master: `data/typeA/donga_2010_post_t0_peak_master_v1_2.json` (builder runtime)',
              '- official 2011 roster: `data/typeA/donga_2011_100_roster_v0_1.json`',
              '- analyzer: `scripts/analyze_donga_repeat_baseline_adjusted_v0_2.py`',
              '- JSON output: `analysis/donga_2010_repeat_selection_baseline_adjusted_v0_2.json`']
    OUTM.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
