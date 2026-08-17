#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
METRICS=ROOT/'data/typeA/typeA_common_metrics_v0_4.json'
OUT=ROOT/'analysis/typeA_cross_cohort_comparison_v0_5.md'


def pct(n,d): return f'{100*n/d:.1f}%'


def main():
    m=json.loads(METRICS.read_text(encoding='utf-8'))
    q=m['qa']; u=m['by_cohort_unit']; naive=m['naive_placement_pooled_descriptive']; pf=m['person_first_selection_descriptive']
    order=[
      ('newsmaker_2003_politics_top10','뉴스메이커 2003 정치 Top10'),
      ('newsmaker_2003_economy_top5','뉴스메이커 2003 경제 Top5'),
      ('h21_2004_politics_top10','한겨레21 2004 정치 Top10'),
      ('khan_2004_17th_assembly_newleaders_20','경향 2004 국회 뉴리더20'),
      ('khan_2005_korea_leaders60_politics10','경향 2005 한국을 이끌 60인 — 정치10*'),
      ('donga_2010_2020_100','동아 2010 미래100'),
      ('donga_2011_10yr_100','동아 2011 미래100')]
    rows=[]
    for key,label in order:
        x=u[key]
        rows.append(f"| {label} | {x['n']} | {x['baseline_mean']:.2f} | {x['post_peak_mean_assessable']:.2f} | {x['major_n']}/{x['n']} ({pct(x['major_n'],x['n'])}) | {x['apex_n']}/{x['n']} ({pct(x['apex_n'],x['n'])}) | {x['advanced_n']}/{x['n']} ({pct(x['advanced_n'],x['n'])}) |")

    h=u['h21_2004_politics_top10']; k04=u['khan_2004_17th_assembly_newleaders_20']; k05=u['khan_2005_korea_leaders60_politics10']
    text=f"""# Type-A 교차 코호트 비교 v0.5

**작성일:** 2026-08-18  
**공통 master:** `typeA_common_master_v0.4`  
**분석단위:** **{q['placements']} placements / {q['unique_people']} canonical persons / {q['cohort_units']} cohort units**

## 1. v0.5 변화

경향신문 2005 「한국을 이끌 60인」의 **정치 분야 10명**을 field-specific secondary cohort로 추가했다.

원 기획은 **60 selected units = 57 persons + 3 organizations**이므로 전체 60인을 person-only master에 넣지 않았다. 정치 분야는 10개 모두 person이라 기존 Type-A 정치 scope로 독립 분석했다.

## 2. 일곱 cohort unit

| cohort | n | baseline | post-peak | Major ≥3 | Apex=4 | Advanced |
|---|---:|---:|---:|---:|---:|---:|
{chr(10).join(rows)}

\* 경향 2005 정치10은 전체 60-unit 프로젝트의 정치 field-specific secondary analysis다.

## 3. 2004–2005 정치 세 코호트

| | 한겨레21 2004 | 경향 2004 | 경향 2005 정치10* |
|---|---:|---:|---:|
| n | {h['n']} | {k04['n']} | {k05['n']} |
| baseline mean | **{h['baseline_mean']:.2f}** | **{k04['baseline_mean']:.2f}** | **{k05['baseline_mean']:.2f}** |
| Major | {pct(h['major_n'],h['n'])} | {pct(k04['major_n'],k04['n'])} | {pct(k05['major_n'],k05['n'])} |
| Apex | {pct(h['apex_n'],h['n'])} | {pct(k04['apex_n'],k04['n'])} | {pct(k05['apex_n'],k05['n'])} |
| Advanced | **{pct(h['advanced_n'],h['n'])}** | **{pct(k04['advanced_n'],k04['n'])}** | **{pct(k05['advanced_n'],k05['n'])}** |

경향 2005 정치10은 baseline 2.60, Advanced 80%로 한겨레21 2004(3.30, 40%)와 경향 2004(2.15, 95%) 사이에 놓인다.

이 패턴은 **baseline ceiling + selection design** 가설과 방향이 맞는다. 이미 전국 최고위권이 많은 리스트는 raw Major가 높아도 추가 상승 여지가 작고, 미래 잠재력을 명시적으로 선별한 후보군은 baseline-adjusted advancement가 더 높을 수 있다.

다만 표본이 작고 동일 인물이 반복되므로 매체 효과로 해석하지 않는다.

## 4. 경향 2005 정치10 결과

- Major: **10/10 = 100%**
- Apex: **5/10 = 50%**
- Advanced: **8/10 = 80%**
- Sustained high: **2/10 = 20% — 강금실, 김근태**
- Apex: **김부겸, 박근혜, 손학규, 이명박, 정동영**

selection cutoff는 원 방법론이 작업 종료일로 밝힌 **2005-12-15**를 사용한다. 발표일 2005-12-30 사이의 15일을 no-lookahead buffer로 둔다.

## 5. Mixed-unit guardrail

경향 2005 전체 기획에는 조직 3개가 포함된다.

- NHN
- 한국공학교육인증원
- 경제정의실천시민연합

따라서 전체 프로젝트를 “57명”으로 재정의하면 안 된다. primary denominator는 **60 units**다. 조직 outcome schema가 별도로 freeze되기 전에는 전체 60-unit hit rate를 계산하지 않는다.

## 6. Common master v0.4

- placements: **{q['placements']}**
- canonical persons: **{q['unique_people']}**
- unique display names: **{q['unique_display_names']}**
- cohort units: **{q['cohort_units']}**
- repeated persons: **{q['repeated_person_n']}**
- max placement count: **{q['max_placement_count']}**
- most-selected person(s): **{', '.join(q['max_selected_names'])}**

Naïve pooled descriptive:

- Major: **{naive['major_n']}/255 = {pct(naive['major_n'],255)}**
- Apex: **{naive['apex_n']}/255 = {pct(naive['apex_n'],255)}**
- Advanced: **{naive['advanced_n']}/255 = {pct(naive['advanced_n'],255)}**

Person-level first selection:

- persons: **{pf['persons']}**
- Major: **{pf['first_selection_major_n']}/{pf['persons']} = {pct(pf['first_selection_major_n'],pf['persons'])}**
- Apex: **{pf['first_selection_apex_n']}/{pf['persons']} = {pct(pf['first_selection_apex_n'],pf['persons'])}**
- Advanced: **{pf['first_selection_advanced_n']}/{pf['persons']} = {pct(pf['first_selection_advanced_n'],pf['persons'])}**

## 7. 현재 결론

현재 자료는 다음을 가장 강하게 지지한다.

> **장기 성과는 ‘어느 언론사인가’보다 후보군의 baseline과 selection design에 크게 좌우될 가능성이 있다.**

따라서 다음 단계의 우선순위는 새 리스트를 무작정 늘리는 것이 아니라, **비슷한 시기·같은 분야·다른 selection mechanism**의 comparable cohort를 확보하는 것이다.

## 8. Reproducibility

- parent recovery: `research/khan_2005_korea_leaders60_recovery_v0_1.json`
- mixed-unit policy: `state/coding_rules_typeA_mixed_unit_v0_1.md`
- politics audit: `research/khan_2005_politics10_peak_audit_v0_1.json`
- politics master: `data/typeA/khan_2005_politics10_peak_master_v1_0.json`
- common master: `data/typeA/typeA_common_master_v0_4.json`
- common metrics: `data/typeA/typeA_common_metrics_v0_4.json`
"""
    OUT.write_text(text,encoding='utf-8')
    print(OUT)

if __name__=='__main__': main()
