# Type-A 교차 코호트 비교 v0.2

**작성일:** 2026-08-18  
**분석단위:** 4 cohort units, 125 placements, 118 unique persons  
**중복 인물:** 7명 — 강금실, 권영길, 안철수, 유시민, 이재용, 정동영, 추미애

## 1. 이번 버전의 핵심 변화

v0.1의 뉴스메이커 2003·한겨레21 2004 TopN 비교에 **동아일보 2010 「2020년 한국을 빛낼 100인」 전수 100명**을 추가했다.

이로써 처음으로 서로 성격이 다른 두 list design을 동시에 볼 수 있다.

- `ranked_topN`: 정치·경제 분야에서 상위 5~10명만 뽑은 얕은 ranked list
- `explicit_horizon_broad_screening`: 문화·과학·시민사회·경제·정치를 아우른 100명 broad list

따라서 이번 버전부터는 **언론사별 적중률을 단순 비교하지 않고 list design을 분석의 일부로 취급**한다.

---

## 2. 네 분석 단위

| cohort unit | design | n | baseline mean | post-T0 mean | major ≥3 | apex=4 | baseline 초과 상승 |
|---|---|---:|---:|---:|---:|---:|---:|
| 뉴스메이커 2003 정치 Top10 | ranked expert survey | 10 | 2.40 | 3.20 | **10/10 (100%)** | 2/10 (20%) | **7/10 (70%)** |
| 뉴스메이커 2003 경제 Top5 | ranked expert survey | 5 | 2.40 | 3.80 | **5/5 (100%)** | **4/5 (80%)** | **4/5 (80%)** |
| 한겨레21 2004 정치 Top10 | ranked public survey | 10 | **3.30** | 3.50 | **10/10 (100%)** | 5/10 (50%) | 4/10 (40%) |
| 동아일보 2010 미래100 | broad explicit-horizon | 100 | 2.55 | 2.83 | **71/100 (71%)** | 12/100 (12%) | **28/100 (28%)** |

### 즉시 보이는 것

TopN 세 단위는 모두 major attainment가 100%다. 그러나 이것만으로 “TopN 언론이 동아일보보다 예측을 잘했다”고 말할 수 없다.

TopN은:

- 정치·경제에 집중되어 있고,
- 5~10명만 남기는 매우 얕은 selection이며,
- 이미 높은 baseline 인물이 많이 포함되고,
- 실제 순위를 제공한다.

반면 동아 2010은 100명을 다섯 분야 이상에서 넓게 뽑은 broad screening이다.

즉 **list depth와 selection mechanism 자체가 outcome rate를 크게 바꿀 수 있다.**

---

## 3. Major attainment와 advancement는 다른 질문이다

현재 네 코호트를 한 문장으로 요약할 때 가장 중요한 구분은 다음이다.

### Major attainment

> 선정된 사람이 이후 높은 위치(scope ≥3)에 적어도 한 번 도달했는가?

- 뉴스메이커 정치: 100%
- 뉴스메이커 경제: 100%
- 한겨레21 정치: 100%
- 동아 2010 broad100: 71%

이 값은 **후속 career quality**에는 좋은 지표지만, 미래 성장 예측과 동일하지 않다.

### Baseline-adjusted advancement

> 선정 시점까지 이미 달성한 lifetime peak보다 이후 더 높은 층위에 실제로 올라갔는가?

- 뉴스메이커 정치: 70%
- 뉴스메이커 경제: 80%
- 한겨레21 정치: 40%
- 동아 2010 broad100: 28%

이 지표가 “그 사람이 이미 잘나가서 뽑힌 것인지, 이후 실제로 더 성장한 것인지”를 가장 직접적으로 분리한다.

---

## 4. Design별 descriptive summary

### Ranked TopN 25 placements

- 25 placements / 21 unique people
- major ≥3: **25/25 = 100%**
- apex=4: **11/25 = 44%**
- baseline 초과 상승: **15/25 = 60%**

### Broad explicit-horizon 100 placements

- 100 placements / 100 unique people
- major ≥3: **71/100 = 71%**
- apex=4: **12/100 = 12%**
- baseline 초과 상승: **28/100 = 28%**

이 차이는 상당히 크지만 **design effect와 outlet effect가 완전히 confounded**되어 있다. 현재 자료로는 원인을 분리할 수 없다.

따라서 올바른 표현은:

> “현재 확보된 얕은 ranked TopN 코호트는 broad 100-person screening보다 높은 후속 major/apex/advancement 비율을 보였다.”

이지,

> “뉴스메이커나 한겨레21이 동아일보보다 미래예측을 잘했다.”

가 아니다.

---

## 5. Naïve pooling은 참고값일 뿐이다

125 placements를 그대로 합치면:

- major ≥3: **96/125 = 76.8%**
- apex=4: **23/125 = 18.4%**
- advanced: **43/125 = 34.4%**

그러나 이 값은 inferential metric으로 쓰면 안 된다.

이유는:

1. 7명이 두 번 등장하여 observations가 독립이 아니다.
2. list depth가 5, 10, 100으로 크게 다르다.
3. 정치·경제 중심 TopN과 다분야 broad list가 섞여 있다.
4. selection year가 2003, 2004, 2010으로 다르다.
5. expert survey, public-opinion survey, editorial broad screening이 섞여 있다.

따라서 pooled 76.8%는 **현재 데이터셋 전체의 기술적 요약**일 뿐 “한국 언론의 평균 예측정확도”가 아니다.

---

## 6. Baseline 수준이 얼마나 중요한가

한겨레21 정치 Top10의 baseline mean은 **3.30**으로 네 단위 중 가장 높다. 이 그룹은 10명 전원이 이후 major scope에 있었지만 실제 baseline 초과 상승은 40%에 불과하다.

반면 뉴스메이커 정치·경제의 baseline mean은 각각 2.40으로 더 낮고 advancement가 70%, 80%였다.

동아 2010은 baseline mean 2.55, advancement 28%다. 여기서는 broad screening의 긴 꼬리와 분야 이질성이 함께 작용한다.

현재 자료가 반복적으로 보여주는 것은:

> **Raw major-attainment는 선정 시점 baseline에 매우 민감하고, 따라서 미래 선구안을 평가하려면 baseline-adjusted outcome이 필수다.**

---

## 7. Ranking signal은 여전히 약하다

기존 ranked cohort 분석:

- 뉴스메이커 정치 Top10: rank vs advancement Δ, **ρ=-0.094, p=0.796**
- 뉴스메이커 경제 Top5: **ρ=-0.224, p=0.718**
- 한겨레21 정치 Top10: **ρ=+0.402, p=0.249**

어느 단위에서도 순위가 이후 실제 상승폭을 유의하게 예측하지 못했다.

현재까지 가장 일관된 신호는:

> **언론은 강한 후보군을 고르는 selection에는 꽤 성공하지만, 그 후보들 안에서 누가 더 크게 성장할지를 순위화하는 ranking 정보는 약하다.**

단, 표본이 작으므로 ranking signal 부재를 확정적으로 주장하기에는 이르다.

---

## 8. 반복선정 결과가 이 해석을 강화한다

동아일보 2010 선정자 중 2011년에도 다시 선정된 38명은 단회선정 62명보다 장기 major/apex 성과가 훨씬 높았다.

- major: **92.1% vs 58.1%**
- apex: **23.7% vs 4.8%**

하지만 baseline 초과 상승은:

- **28.9% vs 27.4%**

로 거의 같았다.

게다가 baseline scope≥3 비율은:

- 반복선정 **78.9%**
- 단회선정 **37.1%**

이었다.

따라서 반복선정은 현재 자료에서는 **future-rise marker라기보다 already-elite / elite-persistence marker**에 더 가깝다.

이 패턴은 cross-cohort 분석의 핵심 교훈과 일치한다: **baseline을 통제하지 않은 high later-attainment는 언론의 미래예측력보다 이미 높은 후보를 골랐다는 사실을 반영할 수 있다.**

---

## 9. 현재 단계에서 주장 가능한 것 / 아직 불가능한 것

### 주장 가능한 것

1. 확보된 모든 Type-A 코호트에서 많은 선정자가 장기적으로 높은 career scope를 보였다.
2. 그러나 major attainment와 genuine advancement 사이에는 큰 차이가 있다.
3. shallow ranked TopN은 broad screening보다 훨씬 높은 outcome rate를 보였다.
4. 순위와 이후 성장폭의 상관은 현재 세 ranked cohort에서 약하다.
5. 반복선정은 absolute later status에는 강한 신호지만 baseline-adjusted growth에는 거의 추가 신호가 없다.

### 아직 주장하면 안 되는 것

1. 어느 언론사가 가장 선구안이 좋았다는 순위.
2. 76.8%를 “한국 언론 평균 적중률”로 부르는 것.
3. 반복선정이 이후 성공을 인과적으로 예측한다고 말하는 것.
4. 선정자들이 비선정 유사인물보다 실제로 더 잘 성장했다고 말하는 것 — 아직 control cohort가 없다.

---

## 10. 다음 분석 설계

### A. Repeat-selection baseline-stratified analysis

동아 2010↔2011의 반복선정 효과를 baseline score와 분야 안에서 비교한다. 특히:

- baseline=2에서 repeat vs single의 score≥3 진입
- baseline=3에서 repeat vs single의 apex=4 진입
- baseline/category strata를 이용한 standardized 또는 Mantel–Haenszel-style comparison

을 계산한다.

### B. 한겨레21 2004 전체 31명 복원

현재 Top10만 분석한 selection truncation 문제를 완화한다. 31명 전체가 확보되면 Top10 vs lower-ranked 21명의 gradient를 직접 볼 수 있다.

### C. 동일 design의 여러 outlet 코호트 확보

언론사 effect를 보려면 **같은 시기·같은 분야·비슷한 list depth**의 코호트가 필요하다. 조선·중앙·동아·한겨레·경향의 유사 Type-A 리스트를 반복 수집해야 한다.

### D. Matched control cohort

최종적으로는 선정 당시 나이·분야·baseline scope가 유사한 비선정자를 matching하여 editorial selection의 incremental predictive value를 검정한다.

---

## 11. Reproducibility

- common builder: `scripts/build_typeA_common_master_v0_1.py`
- committed common metrics: `data/typeA/typeA_common_metrics_v0_1.json`
- 뉴스메이커 2003: `data/typeA/newsmaker_2003_outcomes_v0_3.json`
- 한겨레21 2004: `data/typeA/h21_2004_outcomes_v0_1.json`
- 동아일보 2010 final: `data/typeA/donga_2010_post_t0_peak_master_v1_2.json` (builder runtime)
- 동아 2010 metrics: `data/typeA/donga_2010_post_t0_peak_metrics_v1_2.json`
- 반복선정 metrics: `analysis/donga_2010_repeat_selection_metrics_v0_1.json`
- CI validation: GitHub Actions run `32067990921`, job `95504444792`, **success**

## 12. 현재 가장 압축된 결론

> **지금까지의 자료는 언론이 “누가 이미 강한가 / 앞으로도 높은 위치에 있을 가능성이 큰가”를 골라내는 능력은 상당히 보여주지만, “비슷한 출발점에서 누가 더 크게 성장할 것인가”를 추가로 예측하는 능력은 훨씬 약하게 보인다.**

이 차이를 분리하는 핵심 변수는 `baseline_peak_through_t0`와 `advancement_delta`다.
