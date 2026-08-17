# 동아일보 2010↔2011 반복선정 효과 분석 v0.2

**작성일:** 2026-08-18  
**2010 선정자:** 100명  
**2011 재선정:** 38명  
**2010-only:** 62명

## 결론부터

2011년에 다시 선정된 38명은 장기적으로 훨씬 높은 절대 성취를 보였다.

- post-T0 scope≥3: **92.1% vs 58.1%**
- apex=4: **23.7% vs 4.8%**

하지만 반복선정군은 선정 전부터 훨씬 강한 집단이었다.

- baseline scope≥3: **78.9% vs 37.1%**
- mean baseline peak: **2.87 vs 2.35**

따라서 위의 큰 major/apex 차이는 상당 부분 **이미 검증된 고성과자를 2011년에 다시 선정한 효과**와 섞여 있다.

단순 baseline 초과 상승률은 28.9% vs 27.4%로 거의 같지만, 이 비교 역시 반복선정군에 baseline=4의 ceiling case 3명이 있고 단회선정군에 baseline=1 case 1명이 있어 완전히 공정하지 않다.

같은 upward-capable baseline끼리 비교하면 반복선정에 유리한 방향이 다시 나타난다.

| 선정 전 baseline | 반복선정 상승 | 단회선정 상승 | RR | Fisher p |
|---:|---:|---:|---:|---:|
| 2 | **5/8 (62.5%)** | **13/38 (34.2%)** | 1.83 | 0.232 |
| 3 | **6/27 (22.2%)** | **3/23 (13.0%)** | 1.70 | 0.479 |

baseline 2와 3을 층화한 Mantel–Haenszel 분석에서는:

- common OR: **2.43**
- CMH χ²: **2.60**
- p: **0.107**

이다.

따라서 현재 가장 적절한 해석은 다음과 같다.

> **반복선정은 확실히 이미 높은 수준에 있는 사람을 다시 포착하는 강한 elite-persistence signal이다. 같은 baseline 안에서도 이후 추가 상승이 더 많아지는 방향성은 보이지만, 38명이라는 작은 반복선정 표본에서는 그 incremental signal을 통계적으로 확정하기 어렵다.**

즉 “반복선정은 미래 상승을 전혀 예측하지 못한다”도 과도하고, “두 번 선정하면 독립적으로 미래를 더 잘 맞힌다”도 과도하다.

## 1. Unadjusted comparison

| outcome | repeat 38 | 2010-only 62 | 차이 | RR | Fisher p |
|---|---:|---:|---:|---:|---:|
| post-T0 scope≥3 | 35/38 (92.1%) | 36/62 (58.1%) | +34.0%p | 1.59 | 0.000223 |
| apex=4 | 9/38 (23.7%) | 3/62 (4.8%) | +18.8%p | 4.89 | 0.00885 |
| baseline 초과 상승 | 11/38 (28.9%) | 17/62 (27.4%) | +1.5%p | 1.06 | 1.000 |

## 2. Baseline confounding

2011 반복선정은 무작위가 아니다. 2010 시점에 이미 높은 status/career capital을 가진 사람에게 훨씬 집중되어 있다.

| baseline | repeat 38 | single 62 |
|---|---:|---:|
| 1 | 0 | 1 |
| 2 | 8 | 38 |
| 3 | 27 | 23 |
| 4 | 3 | 0 |

baseline≥3 비율 차이는 **+41.9%p**이며 Fisher p는 **6.84×10⁻⁵**다.

따라서 major attainment 92.1%는 반복선정의 순수한 forecasting value로 볼 수 없다.

## 3. Transition-specific interpretation

### Baseline 2 → major level

반복선정자는 8명 중 5명(62.5%)이 이후 scope≥3으로 올라갔다. 단회선정자는 38명 중 13명(34.2%)이었다.

효과크기는 RR 1.83, OR 3.21로 반복선정 방향이지만 표본이 8명으로 매우 작아 Fisher p=0.232다.

### Baseline 3 → apex

반복선정자는 27명 중 6명(22.2%)이 이후 apex=4에 도달했고, 단회선정자는 23명 중 3명(13.0%)이었다.

RR 1.70, OR 1.90이나 Fisher p=0.479다.

두 strata가 모두 같은 방향이라는 점은 흥미롭지만, 독립적으로는 불확실하다.

## 4. Mantel–Haenszel baseline-stratified estimate

baseline=2와 3만 사용해 upward transition을 비교했다. baseline=4는 0–4 척도상 더 상승할 공간이 없고, baseline=1은 repeat comparator가 없어 제외했다.

공통 OR은 **2.43**, CMH p는 **0.107**이었다.

이는 단순 overall advancement 28.9% vs 27.4%보다 반복선정의 incremental signal을 더 공정하게 보여준다. 결과는 **suggestive but inconclusive**로 분류하는 것이 적절하다.

## 5. 분야별 결과는 exploratory로만 본다

분야별 표본은 너무 작고 baseline composition도 다르다. 일부 category에서는 큰 차이가 나오지만 이를 그대로 editorial forecasting effect로 해석하면 안 된다.

예를 들어 `행동하는 지성인`에서 repeat major가 4/5, single major가 3/15로 차이가 크지만, category 안에서도 baseline과 인물구성이 다르다. `자유로운 창조인`에서는 repeat apex가 3/5, single 1/15로 높지만 반복군 자체가 baseline 3–4에 집중되어 있다.

따라서 category-specific p-value는 hypothesis-generating 용도로만 보존한다.

## 6. 연구적으로 의미하는 것

이번 결과는 언론의 반복선정을 세 층으로 나눠 볼 필요가 있음을 보여준다.

1. **Recognition:** 이미 높은 사람을 다시 알아보는가? → 매우 강함.
2. **Persistence:** 다시 뽑힌 사람이 이후에도 major/apex로 남는가? → 매우 강함.
3. **Incremental foresight:** 같은 출발선에서 다시 뽑힌 사람이 더 많이 상승하는가? → 방향성은 있으나 현재 표본으로 확정 불가.

앞으로 다른 언론·다른 연도의 반복선정 사례가 누적되면 세 번째 질문을 pooled stratified analysis로 검증할 수 있다.

## 7. 제한점

- 2011 재선정은 2010 선정 약 1년 후라 초기 post-2010 성취가 재선정에 반영될 수 있다. 따라서 reverse causation이 가능하다.
- baseline score는 0–4 coarse ordinal scale이다.
- CMH는 baseline score만 통제하며 분야, 나이, 기관, 당시 언론노출 등은 통제하지 않는다.
- 반복선정군이 38명이라 strata별 검정력이 낮다.
- p-value는 exploratory descriptive evidence로 취급한다.

## 8. Reproducibility

- 2010 outcome master: `data/typeA/donga_2010_post_t0_peak_master_v1_2.json` (runtime)
- 2011 roster: `data/typeA/donga_2011_100_roster_v0_1.json`
- repeat crosswalk: `research/donga_2010_2011_repeat_crosswalk_v1_0.md`
- basic analyzer: `scripts/analyze_donga_2010_repeat_selection.py`
- stratified analyzer: `scripts/analyze_donga_2010_repeat_stratified.py`
- committed basic metrics: `analysis/donga_2010_repeat_selection_metrics_v0_1.json`
- committed stratified metrics: `analysis/donga_2010_repeat_selection_stratified_v0_2.json`
- validation commit: `345a6ea410837bbf526daca1074d767f5b315e91`
- Actions run: `32068258774`
- analysis and QA: **success**
