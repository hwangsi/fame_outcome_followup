#!/usr/bin/env python3
import json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TYPEA=ROOT/'data/typeA'
MASTER=TYPEA/'donga_2010_post_t0_peak_master_v1_2.json'
ROSTER11=TYPEA/'donga_2011_100_roster_v0_1.json'
OUT=ROOT/'analysis/donga_2010_repeat_selection_stratified_v0_2.json'


def fisher_two_sided(a,b,c,d):
    n=a+b+c+d; r1=a+b; c1=a+c
    lo=max(0,r1-(n-c1)); hi=min(r1,c1)
    def p(x): return math.comb(c1,x)*math.comb(n-c1,r1-x)/math.comb(n,r1)
    p0=p(a)
    return min(1.0,sum(p(x) for x in range(lo,hi+1) if p(x)<=p0+1e-15))


def effect(a,b,c,d):
    nr=a+b; ns=c+d
    rr=(a/nr)/(c/ns) if c else None
    return {
        'repeat_advanced_n':a,'repeat_n':nr,'repeat_rate':a/nr,
        'single_advanced_n':c,'single_n':ns,'single_rate':c/ns,
        'rate_difference':a/nr-c/ns,
        'risk_ratio':rr,
        'odds_ratio':(a*d)/(b*c) if b*c else None,
        'fisher_two_sided_p':fisher_two_sided(a,b,c,d)
    }


def cmh(tables):
    # tables are (a,b,c,d): repeat advanced/not, single advanced/not
    score=0.0; var=0.0; or_num=0.0; or_den=0.0
    for a,b,c,d in tables:
        n=a+b+c+d; r1=a+b; r2=c+d; c1=a+c; c2=b+d
        score += a-r1*c1/n
        var += r1*r2*c1*c2/(n*n*(n-1))
        or_num += a*d/n
        or_den += b*c/n
    stat=score*score/var
    return {
        'mantel_haenszel_common_odds_ratio':or_num/or_den,
        'cmh_chi_square_df1':stat,
        'cmh_p':math.erfc(math.sqrt(stat/2))
    }


def main():
    m=json.loads(MASTER.read_text(encoding='utf-8'))
    rows=m['people']; assert len(rows)==100 and m['qa']['unresolved']==0
    r11=json.loads(ROSTER11.read_text(encoding='utf-8'))
    n11=set(sum(r11['categories'].values(),[]))
    repeat={r['name'] for r in rows}&n11
    assert len(repeat)==38

    tables=[]; strata={}
    for score in (2,3):
        r=[x for x in rows if x['name'] in repeat and x['baseline_peak_through_t0']==score]
        s=[x for x in rows if x['name'] not in repeat and x['baseline_peak_through_t0']==score]
        a=sum(x['advancement_class']=='advanced' for x in r); b=len(r)-a
        c=sum(x['advancement_class']=='advanced' for x in s); d=len(s)-c
        tables.append((a,b,c,d))
        strata[str(score)]=effect(a,b,c,d)

    common_r=[x for x in rows if x['name'] in repeat and x['baseline_peak_through_t0'] in (2,3)]
    common_s=[x for x in rows if x['name'] not in repeat and x['baseline_peak_through_t0'] in (2,3)]
    ar=sum(x['advancement_class']=='advanced' for x in common_r)
    as_=sum(x['advancement_class']=='advanced' for x in common_s)
    pooled=effect(ar,len(common_r)-ar,as_,len(common_s)-as_)
    mh=cmh(tables)

    out={
      'schema_version':'donga_2010_repeat_selection_stratified_v0.2',
      'generated':'2026-08-18',
      'analysis_question':'Within comparable preselection baseline strata, is 2011 repeat selection associated with subsequent advancement above the preselection lifetime peak?',
      'eligible_common_strata':[2,3],
      'strata':strata,
      'pooled_common_strata_unstratified':pooled,
      'mantel_haenszel':mh,
      'interpretation':{
        'baseline2':'Repeat-selected: 5/8 advanced to >=3 versus 13/38 of single-selected; direction favors repeat selection but Fisher p is not significant.',
        'baseline3':'Repeat-selected: 6/27 advanced to apex 4 versus 3/23 of single-selected; direction again favors repeat selection but Fisher p is not significant.',
        'combined':'Both common baseline strata point in the same direction. The Mantel-Haenszel common OR is above 1, but the CMH p-value does not cross conventional significance. This is suggestive, not confirmatory, evidence of incremental repeat-selection signal.',
        'ceiling_floor':'Baseline=4 repeat cases are excluded because they cannot advance on the locked 0-4 scale; baseline=1 has no repeat-selected comparator and is also excluded.'
      },
      'guardrails':[
        'Repeat selection occurs roughly one year after initial selection, so early post-2010 performance may influence the repeat decision.',
        'Small stratum sizes make estimates imprecise.',
        'The 0-4 outcome is coarse and may hide within-stratum career growth.',
        'CMH adjustment controls only the locked baseline score strata, not editorial category, age, domain, media visibility, or other confounders.'
      ]
    }
    assert strata['2']['repeat_advanced_n']==5 and strata['2']['single_advanced_n']==13
    assert strata['3']['repeat_advanced_n']==6 and strata['3']['single_advanced_n']==3
    assert abs(mh['mantel_haenszel_common_odds_ratio']-2.427805280528053)<1e-12
    assert abs(mh['cmh_p']-0.10666393286039269)<1e-12
    OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
