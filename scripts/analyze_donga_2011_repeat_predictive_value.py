#!/usr/bin/env python3
import json, math
from collections import Counter, defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MASTER=ROOT/'analysis/donga_2011_post_t0_master_v1_0.json'
OUT_JSON=ROOT/'analysis/donga_2011_repeat_predictive_value_v1_0.json'
OUT_MD=ROOT/'analysis/donga_2011_repeat_predictive_value_v1_0.md'


def prop(n,d):
    return n/d if d else None


def raw_or(a,b,c,d):
    # a=repeat hit, b=repeat nonhit, c=new hit, d=new nonhit
    if b*c==0:
        return math.inf if a*d>0 else None
    return a*d/(b*c)


def logcomb(n,k):
    if k<0 or k>n: return -math.inf
    return math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1)


def fisher_two_sided(a,b,c,d):
    r1=a+b; r2=c+d; c1=a+c; n=r1+r2
    lo=max(0,c1-r2); hi=min(r1,c1)
    def lp(x):
        return logcomb(c1,x)+logcomb(n-c1,r1-x)-logcomb(n,r1)
    obs=lp(a); probs=[]
    for x in range(lo,hi+1):
        z=lp(x)
        if z <= obs + 1e-12: probs.append(math.exp(z))
    return min(1.0,sum(probs))


def cmh(strata, outcome_key):
    # assessable rows only. Exposure = repeat.
    num_or=0.0; den_or=0.0; sum_ae=0.0; sum_var=0.0; used=[]
    for baseline,rows in sorted(strata.items()):
        rows=[r for r in rows if r['post2011_peak_score'] is not None]
        if not rows: continue
        rep=[r for r in rows if r['repeat_2010_2011']]
        new=[r for r in rows if not r['repeat_2010_2011']]
        a=sum(bool(outcome_key(r)) for r in rep); b=len(rep)-a
        c=sum(bool(outcome_key(r)) for r in new); d=len(new)-c
        n=a+b+c+d
        if n<2: continue
        num_or += a*d/n
        den_or += b*c/n
        n1=a+b; n0=c+d; m1=a+c; m0=b+d
        ea=n1*m1/n
        va=(n1*n0*m1*m0)/(n*n*(n-1)) if n>1 else 0
        sum_ae += a-ea; sum_var += va
        used.append({'baseline':baseline,'repeat_hit':a,'repeat_nonhit':b,'new_hit':c,'new_nonhit':d,'n':n})
    mh_or=(num_or/den_or) if den_or>0 else math.inf
    chi2=(sum_ae*sum_ae/sum_var) if sum_var>0 else None
    p=math.erfc(math.sqrt(chi2/2)) if chi2 is not None else None
    chi2_cc=((max(0,abs(sum_ae)-0.5)**2)/sum_var) if sum_var>0 else None
    p_cc=math.erfc(math.sqrt(chi2_cc/2)) if chi2_cc is not None else None
    return {'mh_common_or':mh_or,'cmh_chi2':chi2,'cmh_p':p,'cmh_chi2_continuity_corrected':chi2_cc,'cmh_p_continuity_corrected':p_cc,'strata':used}


def group_metrics(rows, full_denominator=True):
    scored=[r for r in rows if r['post2011_peak_score'] is not None]
    denom=len(rows) if full_denominator else len(scored)
    major=sum((r['post2011_peak_score'] or -1)>=3 for r in rows)
    apex=sum(r['post2011_peak_score']==4 for r in rows)
    adv=sum(r['advancement_class']=='advanced' for r in rows)
    return {
        'n_total':len(rows),'n_scored':len(scored),'denominator':denom,
        'major_n':major,'major_rate':prop(major,denom),
        'apex_n':apex,'apex_rate':prop(apex,denom),
        'advanced_n':adv,'advanced_rate':prop(adv,denom),
        'baseline_counts':dict(Counter(str(r['baseline_2011']) for r in rows)),
        'advancement_classes':dict(Counter(r['advancement_class'] for r in rows)),
    }


def main():
    d=json.loads(MASTER.read_text(encoding='utf-8'))
    rows=d['people']; assert len(rows)==100
    rep=[r for r in rows if r['repeat_2010_2011']]
    new=[r for r in rows if not r['repeat_2010_2011']]
    assert len(rep)==38 and len(new)==62
    assert sum(r['post2011_peak_score'] is None for r in rows)==1

    metrics={}
    for label,fn in {
        'major':lambda r:r['post2011_peak_score'] is not None and r['post2011_peak_score']>=3,
        'apex':lambda r:r['post2011_peak_score']==4,
        'advanced':lambda r:r['advancement_class']=='advanced',
    }.items():
        a=sum(fn(r) for r in rep); b=len(rep)-a
        c=sum(fn(r) for r in new); dd=len(new)-c
        metrics[label]={
            'primary_full_cohort':{
                'repeat_hit':a,'repeat_nonhit':b,'new_hit':c,'new_nonhit':dd,
                'repeat_rate':a/len(rep),'new_rate':c/len(new),
                'risk_difference_repeat_minus_new':a/len(rep)-c/len(new),
                'raw_odds_ratio':raw_or(a,b,c,dd),
                'fisher_two_sided_p':fisher_two_sided(a,b,c,dd),
            }
        }
        # assessable sensitivity (only differs for new because Shin Jun-ho is NA)
        repa=[r for r in rep if r['post2011_peak_score'] is not None]
        newa=[r for r in new if r['post2011_peak_score'] is not None]
        aa=sum(fn(r) for r in repa); bb=len(repa)-aa; cc=sum(fn(r) for r in newa); ddd=len(newa)-cc
        metrics[label]['assessable_only']={
            'repeat_hit':aa,'repeat_nonhit':bb,'repeat_n':len(repa),
            'new_hit':cc,'new_nonhit':ddd,'new_n':len(newa),
            'repeat_rate':aa/len(repa),'new_rate':cc/len(newa),
            'risk_difference_repeat_minus_new':aa/len(repa)-cc/len(newa),
            'raw_odds_ratio':raw_or(aa,bb,cc,ddd),
            'fisher_two_sided_p':fisher_two_sided(aa,bb,cc,ddd),
        }

    strata=defaultdict(list)
    for r in rows: strata[r['baseline_2011']].append(r)
    adjusted={
        'major':cmh(strata,lambda r:r['post2011_peak_score']>=3),
        'apex':cmh(strata,lambda r:r['post2011_peak_score']==4),
        'advanced':cmh(strata,lambda r:r['advancement_class']=='advanced'),
    }

    out={
      'schema_version':'donga_2011_repeat_predictive_value_v1.0','generated':'2026-08-18',
      'question':'At the 2011 selection time, did prior selection in 2010 add prospective information about post-2011 outcomes beyond baseline prestige?',
      'design':'prospective_from_2011_selection_time_observational_repeat_vs_new',
      'master_ref':str(MASTER.relative_to(ROOT)),
      'population':{'total':100,'repeat':38,'new':62,'assessable':99,'new_assessable':61},
      'baseline_distribution':{
        'repeat':dict(Counter(str(r['baseline_2011']) for r in rep)),
        'new':dict(Counter(str(r['baseline_2011']) for r in new)),
      },
      'group_summary':{
        'repeat_full':group_metrics(rep,True),'new_full':group_metrics(new,True),
        'repeat_assessable':group_metrics(rep,False),'new_assessable':group_metrics(new,False),
      },
      'outcome_comparisons':metrics,
      'baseline_stratified_cmh_assessable_only':adjusted,
      'guardrails':[
        'Repeat status is known at the 2011 selection time, so this avoids the look-ahead problem of classifying the 2010 cohort by a future 2011 event.',
        'Repeat status is observational, not randomized; association is not causation.',
        'CMH analyses use assessable rows only and stratify by frozen 2011 pre-selection lifetime baseline score.',
        'The one not-assessable new entrant is conservatively a non-hit in primary raw rates and excluded from assessable-only/CMH analyses.'
      ]
    }
    OUT_JSON.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

    def pct(x): return f'{100*x:.1f}%'
    md=['# 동아일보 2011 반복선정의 prospective 추가 예측력 v1.0','',
        '- repeat 2010→2011: **38명**','- new 2011 entrants: **62명** (61 assessable)','',
        '## Raw outcomes','',
        '| Outcome | Repeat | New | Difference | Fisher p |','|---|---:|---:|---:|---:|']
    for key,title in [('major','Major ≥3'),('apex','Apex =4'),('advanced','Advanced')]:
        x=metrics[key]['primary_full_cohort']
        md.append(f"| {title} | {x['repeat_hit']}/38 = {pct(x['repeat_rate'])} | {x['new_hit']}/62 = {pct(x['new_rate'])} | {100*x['risk_difference_repeat_minus_new']:+.1f} pp | {x['fisher_two_sided_p']:.4g} |")
    md += ['', '## Baseline distribution','',f"- repeat: `{out['baseline_distribution']['repeat']}`",f"- new: `{out['baseline_distribution']['new']}`",'',
           '## Baseline-stratified CMH (assessable only)','',
           '| Outcome | MH common OR | CMH p | continuity-corrected p |','|---|---:|---:|---:|']
    for key,title in [('major','Major ≥3'),('apex','Apex =4'),('advanced','Advanced')]:
        x=adjusted[key]
        md.append(f"| {title} | {x['mh_common_or']:.3f} | {x['cmh_p']:.4g} | {x['cmh_p_continuity_corrected']:.4g} |")
    md += ['', '## Interpretation guardrail','',
           '이 분석은 2011 선정 시점에서 이미 알려진 `2010에도 선정됨` 정보를 사용하므로 2010 cohort를 미래 정보로 나누던 기존 association 분석보다 prospective 질문에 가깝다. 그러나 repeat 여부는 무작위가 아니며 baseline prestige와 강하게 연관될 수 있으므로, raw rate보다 baseline-stratified 결과를 함께 해석해야 한다.','']
    OUT_MD.write_text('\n'.join(md),encoding='utf-8')
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
