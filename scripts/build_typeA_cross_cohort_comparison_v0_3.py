#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
METRICS = ROOT / 'data/typeA/typeA_common_metrics_v0_2.json'
OUT = ROOT / 'analysis/typeA_cross_cohort_comparison_v0_3.md'


def pct(n, d):
    return f'{100*n/d:.1f}%'


def main():
    m = json.loads(METRICS.read_text(encoding='utf-8'))
    q = m['qa']
    units = m['by_cohort_unit']
    designs = m['by_design']
    naive = m['naive_placement_pooled_descriptive']
    pf = m['person_first_selection_descriptive']

    order = [
        ('newsmaker_2003_politics_top10', '뉴스메이커 2003 정치 Top10'),
        ('newsmaker_2003_economy_top5', '뉴스메이커 2003 경제 Top5'),
        ('h21_2004_politics_top10', '한겨레21 2004 정치 Top10'),
        ('donga_2010_2020_100', '동아일보 2010 미래100'),
        ('donga_2011_10yr_100', '동아일보 2011 미래100'),
    ]

    rows = []
    for key, label in order:
        x = units[key]
        rows.append(
            f"| {label} | {x['design']} | {x['n']} | {x['baseline_mean']:.2f} | "
            f"{x['post_peak_mean_assessable']:.2f} | {x['major_n']}/{x['n']} ({pct(x['major_n'],x['n'])}) | "
            f"{x['apex_n']}/{x['n']} ({pct(x['apex_n'],x['n'])}) | "
            f"{x['advanced_n']}/{x['n']} ({pct(x['advanced_n'],x['n'])}) |"
        )

    ranked = designs['ranked_topN']
    broad = designs['broad_screening_explicit_horizon']
    persons = pf['persons']

    text = f"""# Type-A 교차 코호트 비교 v0.3

**작성일:** 2026-08-18  
**공통 master:** `typeA_common_master_v0.2`  
**분석단위:** **{q['placements']} placements / {q['unique_people']} unique persons / 5 cohort units**  
**반복 인물:** **{q['repeated_person_n']}명** — 2회 선정 40명, 3회 선정 3명  
**3회 선정:** {', '.join(q['triple_selected_names'])}

## 1. v0.3의 핵심 변화

v0.2의 125 placements(뉴스메이커 2003, 한겨레21 2004, 동아 2010)에 **동아일보 2011 100 placements**를 추가했다. 동시에 단순 이름 매칭을 버리고 identity-guarded common master를 사용한다.

따라서 이제 데이터는 **225 placements이지만 179명의 독립 인물**이다. 같은 사람이 여러 번 선정된 경우를 독립 표본처럼 세지 않는 것이 이번 버전의 가장 중요한 구조적 변화다.

또한 동아 2011에는 1명의 `not_assessable`이 있으므로 full-placement rate에서는 보수적으로 non-hit로 유지한다.

---

## 2. 다섯 cohort unit의 placement-level descriptive

| cohort unit | design | n | baseline mean | post-T0 mean* | major ≥3 | apex=4 | baseline 초과 상승 |
|---|---|---:|---:|---:|---:|---:|---:|
{chr(10).join(rows)}

\* post-T0 mean은 assessable placement 기준이다.

가장 눈에 띄는 점은 여전히 **Major attainment와 genuine advancement의 간극**이다. 특히 broad 100-person screening에서는 선정 이후 높은 위치에 있었던 사람의 비율과 선정 전 lifetime peak를 실제로 넘어선 사람의 비율이 크게 다르다.

---

## 3. Design별 기술적 비교

### Ranked TopN

- placements: **{ranked['placements']}**
- unique people: **{ranked['unique_people']}**
- major: **{ranked['major_n']}/{ranked['placements']} = {pct(ranked['major_n'], ranked['placements'])}**
- apex: **{ranked['apex_n']}/{ranked['placements']} = {pct(ranked['apex_n'], ranked['placements'])}**
- advanced: **{ranked['advanced_n']}/{ranked['placements']} = {pct(ranked['advanced_n'], ranked['placements'])}**

### Broad screening + explicit horizon

- placements: **{broad['placements']}**
- unique people: **{broad['unique_people']}**
- major: **{broad['major_n']}/{broad['placements']} = {pct(broad['major_n'], broad['placements'])}**
- apex: **{broad['apex_n']}/{broad['placements']} = {pct(broad['apex_n'], broad['placements'])}**
- advanced: **{broad['advanced_n']}/{broad['placements']} = {pct(broad['advanced_n'], broad['placements'])}**

이 차이를 **언론사 효과**로 해석하면 안 된다. ranked TopN과 broad screening은 selection year, 분야, list depth, selection mechanism이 동시에 다르다. 현재 단계에서는 design-stratified descriptive만 허용한다.

---

## 4. Naïve placement pooling

225 placements를 그대로 합친 기술적 요약은 다음과 같다.

- major: **{naive['major_n']}/225 = {pct(naive['major_n'],225)}**
- apex: **{naive['apex_n']}/225 = {pct(naive['apex_n'],225)}**
- advanced: **{naive['advanced_n']}/225 = {pct(naive['advanced_n'],225)}**

그러나 이 수치는 inferential metric이 아니다. **43명이 반복 등장하고, 3명은 세 번 등장**하므로 observations가 독립이 아니다. 또한 연도·분야·리스트 깊이·선정 방식이 서로 confounded되어 있다.

---

## 5. Person-level first-selection descriptive

placement 중복을 제거하고 각 인물의 **첫 선정 시점**만 사용하면:

- persons: **{persons}**
- first-selection major: **{pf['first_selection_major_n']}/{persons} = {pct(pf['first_selection_major_n'], persons)}**
- first-selection apex: **{pf['first_selection_apex_n']}/{persons} = {pct(pf['first_selection_apex_n'], persons)}**
- first-selection advanced: **{pf['first_selection_advanced_n']}/{persons} = {pct(pf['first_selection_advanced_n'], persons)}**

이 person-level 요약은 placement 중복 문제는 줄이지만, **첫 선정 연도에 따라 observation window가 다르다**는 한계가 남는다. 따라서 이것도 기술통계로만 사용한다.

---

## 6. 반복선정에서 얻은 추가 정보

동아 2011에서 2010 repeat 38명과 new 62명을 prospective하게 비교한 별도 분석의 결론은 common master 해석과 일치한다.

- repeat는 **major persistence**에는 추가 신호가 거의 없었다.
- repeat는 **apex identification**에서 강한 sparse-data association을 보였다.
- repeat는 **baseline-adjusted advancement**에서 명확한 추가 신호가 없었다.

즉 반복선정은 현재 자료에서 “누가 더 성장할 것인가”보다는 “이미 강한 후보 중 누가 극소수 apex까지 갈 가능성이 있는가”에 가까운 editorial consensus signal이다. causal effect로 표현하지 않는다.

상세: `state/donga_2011_repeat_predictive_value_v1_0.md`

---

## 7. 현재까지 가장 안정적인 해석

1. **선정(selection)**: 확보된 코호트에서 언론/전문가가 장기적으로 높은 위치에 남는 후보군을 골라내는 능력은 상당히 보인다.
2. **상승(advancement)**: 그러나 이미 선정 전에 높은 사람이 많기 때문에 raw major rate는 미래 성장 예측력을 과대평가할 수 있다.
3. **순위(ranking)**: 기존 ranked cohort에서 rank와 이후 advancement의 상관은 약했다.
4. **반복선정(re-selection)**: 반복선정은 baseline-adjusted growth보다 elite persistence/apex identification에 더 가까운 신호다.
5. **비교단위**: outlet comparison보다 먼저 list design, year, domain, depth를 분리해야 한다.

가장 압축하면:

> **현재 자료에서 언론은 ‘누가 강한 후보인가’를 고르는 능력은 꽤 보이지만, ‘비슷한 출발점에서 누가 더 크게 성장할 것인가’를 추가로 맞히는 능력은 훨씬 약하게 보인다.**

---

## 8. Identity QA

common master는 이름만 같다고 merge하지 않는다.

- 동아 2010↔2011 repeat 38명은 frozen repeat set으로 검증한다.
- 초기 cross-cohort overlap은 별도 verified set으로만 merge한다.
- 새 same-name collision이 생기면 builder가 **fail**하고 manual identity audit을 요구한다.

현재 QA:

- placements: **{q['placements']}**
- unique people: **{q['unique_people']}**
- repeated persons: **{q['repeated_person_n']}**
- placement count distribution: **1회 {q['placement_count_distribution']['1']}명 / 2회 {q['placement_count_distribution']['2']}명 / 3회 {q['placement_count_distribution']['3']}명**
- same-name verified candidates: **{q['same_name_candidates_n']}명**
- not assessable placements: **{q['not_assessable_placements']}**

---

## 9. 다음 분석 단계

### A. 한겨레21 2004 full31 복원

Top10 truncation을 줄이고 rank gradient를 직접 본다.

### B. 조선·중앙·경향 등 동일 설계 코호트 추가

outlet effect를 보려면 같은 시기·분야·list depth의 비교 가능한 코호트가 필요하다.

### C. Person-clustered / mixed-effects model

표본이 더 쌓인 뒤 repeated placement를 person cluster로 처리하고 year/domain/design을 함께 모델링한다.

### D. Matched control

선정 당시 age/domain/baseline이 유사한 비선정 인물을 매칭해 editorial selection의 incremental predictive value를 검정한다.

---

## 10. Reproducibility

- common builder: `scripts/build_typeA_common_master_v0_2.py`
- common master: `data/typeA/typeA_common_master_v0_2.json`
- common CSV: `data/typeA/typeA_common_master_v0_2.csv`
- common metrics: `data/typeA/typeA_common_metrics_v0_2.json`
- frozen summary: `state/typeA_common_master_freeze_v0_2.json`
- comparison builder: `scripts/build_typeA_cross_cohort_comparison_v0_3.py`
- this report: `analysis/typeA_cross_cohort_comparison_v0_3.md`

All claims in this report are descriptive unless a separately frozen inferential analysis is explicitly referenced.
"""

    OUT.write_text(text, encoding='utf-8')
    print(OUT)


if __name__ == '__main__':
    main()
