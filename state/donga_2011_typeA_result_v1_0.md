# 동아일보 2011 「10년 뒤 한국을 빛낼 100인」 — Type-A 최종 결과 v1.0

**기준일:** 2026-08-18  
**선정 cutoff:** 2011-04-01  
**관찰 종료:** 2026-08-18

## 1. 데이터 완결성

- canonical roster: **100/100**
- T0 scope: **100/100**
- pre-selection lifetime peak: **100/100**
- post-selection outcome adjudication: **100/100**
- scored: **99/100**
- not assessable: **1/100 — 신준호**
- pending: **0**
- 2010↔2011 repeat selections: **38명**
- new 2011 entrants: **62명**
- death-truncated observation: **김정주, 박원순 2명**

신준호는 2011 당시 `호텔신라 조리팀 차장`이라는 identity는 확실하지만, 2011-04-01 이후 동일인의 경력을 재현 가능하게 직접 연결하는 신뢰 자료가 부족해 임의의 낮은 점수를 부여하지 않고 `not_assessable`로 남겼다.

## 2. Primary result — full cohort conservative

Primary analysis는 전체 roster 100명을 분모로 사용하고, not-assessable 1명은 보수적으로 non-hit로 둔다.

| 지표 | n/N | rate |
|---|---:|---:|
| Major leadership (`post-T0 scope ≥3`) | **90/100** | **90.0%** |
| Apex (`scope =4`) | **12/100** | **12.0%** |
| Baseline-adjusted advanced | **36/100** | **36.0%** |

Advancement class:

- advanced: **36**
- sustained high: **53**
- no clear advancement: **7**
- lower than baseline: **3**
- not assessable: **1**

Scored 99명의 post-T0 peak 분포:

- score 2: **9**
- score 3: **78**
- score 4: **12**

## 3. Sensitivity — assessable only

신준호를 제외한 99명을 분모로 하면:

- major: **90/99 = 90.9%**
- apex: **12/99 = 12.1%**
- advanced: **36/99 = 36.4%**

결론은 full-cohort conservative 분석과 거의 변하지 않는다.

## 4. 핵심 해석

> **2011 리스트는 선정 이후 major 수준에 도달하거나 유지한 비율이 90%로 매우 높았지만, 선정 이전 lifetime peak를 넘어서 실제로 더 높은 층위로 상승한 사람은 36%였다.**

따라서 90%를 그대로 “미래예측 성공률”이라고 부르면 과대해석이다. 이 리스트 역시 두 요소가 섞여 있다.

1. 이미 강한 사람을 다시 골라내는 **screening / persistence signal**
2. 선정 이후 실제로 더 높은 층위에 도달한 **advancement signal**

특히 `sustained_high = 53명`이 `advanced = 36명`보다 많다는 점은, 2011 리스트가 순수한 신인 발굴보다 이미 높은 잠재력·지위를 가진 인물의 지속성을 강하게 포착했다는 해석과 부합한다.

## 5. 2010 vs 2011 — 동일 protocol의 기술적 비교

| 지표 | 동아 2010 | 동아 2011 |
|---|---:|---:|
| Major | 71% | **90%** |
| Apex | **12%** | **12%** |
| Advanced | 28% | **36%** |
| Sustained high | 44% | **53%** |
| No clear advancement | 28% | **7%** |
| Lower than baseline | 0% | **3%** |
| Not assessable | 0% | **1%** |

2011은 2010보다 raw major attainment가 크게 높고 advancement도 다소 높지만 apex는 동일하다.

그러나 이 표를 곧바로 “2011 편집진이 2010보다 예측을 더 잘했다”는 결론으로 읽으면 안 된다. 두 코호트의 baseline 구성과 분야 구성은 다르고, **38명이 반복 선정**되어 독립 표본도 아니다. 현재 단계의 비교는 design-aware descriptive comparison이다.

## 6. 2011 repeat 38명 vs new entrant 62명 — prospective 분석 완료

2010 시점에서 나중의 2011 재선정 여부로 2010 outcome을 나누는 기존 분석은 look-ahead가 포함된다. 반면 2011 선정 시점에는 `2010에도 선정되었는가`가 이미 알려진 baseline 정보다.

따라서 이번 비교는 다음 질문에 답한다.

> **2011년 선정 시점에서 반복 선정되었다는 정보가 당시 baseline prestige를 넘어 이후 성과에 추가적인 예측정보를 제공했는가?**

### 6.1 Baseline imbalance

| baseline score | Repeat | New |
|---:|---:|---:|
| 2 | 8 | 30 |
| 3 | 27 | 30 |
| 4 | 3 | 2 |

repeat 집단은 처음부터 baseline 3–4에 훨씬 많이 몰려 있다. 따라서 raw outcome과 baseline-stratified 결과를 반드시 함께 봐야 한다.

### 6.2 Raw outcomes

| Outcome | Repeat | New | Difference | Fisher p |
|---|---:|---:|---:|---:|
| Major ≥3 | **35/38 = 92.1%** | **55/62 = 88.7%** | +3.4 pp | 0.738 |
| Apex =4 | **9/38 = 23.7%** | **3/62 = 4.8%** | **+18.8 pp** | **0.00885** |
| Advanced | **11/38 = 28.9%** | **25/62 = 40.3%** | -11.4 pp | 0.288 |

### 6.3 Baseline-stratified analysis

신준호를 제외한 assessable 99명을 frozen baseline score로 층화했다.

| Outcome | MH common OR | CMH p | Exact conditional p |
|---|---:|---:|---:|
| Major ≥3 | **0.734** | 0.657 | **0.691** |
| Apex =4 | **8.690** | **0.0167** | **0.0268** |
| Advanced | **1.825** | 0.276 | **0.339** |

### 6.4 해석

- **Major:** repeat 여부의 추가 정보가 거의 없다. 두 집단 모두 약 90%로 이미 ceiling에 가깝다.
- **Apex:** repeat 23.7% vs new 4.8%였고, baseline 층화 후에도 MH OR≈8.69, exact p=0.0268로 강한 association이 남는다.
- **Advanced:** raw로는 new가 더 높지만 repeat가 시작부터 높은 baseline에 몰려 있다. 층화 후 OR 방향은 1보다 커지지만 통계적으로 확증적이지 않다.

> **반복 선정은 ‘더 성장할 사람’을 명확히 골라내는 신호라기보다, 이미 강한 후보군 가운데 장차 극소수 apex까지 갈 인물을 재차 포착하는 editorial consensus signal일 가능성이 있다.**

다만 apex 사건은 전체 12건뿐이고 baseline score도 거친 척도이므로, causal effect나 확정적 효과크기로 해석하지 않는다.

상세 분석:

- `state/donga_2011_repeat_predictive_value_v1_0.md`
- `state/donga_2011_repeat_predictive_value_freeze_v1_0.json`

## 7. Identity QA에서 얻은 교훈

batch 3 이후 frozen T0 identity anchor를 의무화했다. 이름만 검색하면 다음처럼 위험한 동명이인 오류가 생긴다.

- 김선욱: 대학 총장 동명이인 ≠ **피아니스트 김선욱**
- 김승환: 교육감 동명이인 ≠ **POSTECH 물리학자 김승환**
- 김가영: 당구선수 동명이인 ≠ **농업유통 창업가 김가영**
- 전혜경: 농업계 동명이인 ≠ **UNICEF Senior Advisor 전혜경**

최종 신규 audit 중 batch 3–6의 **42명 전원**은 2011 frozen category + 공식 당시 직함을 자동 검증하도록 CI에 묶었다.

## 8. 재현성

최종 outcome builder:

- `scripts/build_donga_2011_post_t0_master.py`

repeat predictive-value analysis:

- `scripts/analyze_donga_2011_repeat_predictive_value.py`

runtime outputs:

- `analysis/donga_2011_post_t0_master_v1_0.json`
- `analysis/donga_2011_post_t0_metrics_v1_0.json`
- `analysis/donga_2011_repeat_predictive_value_v1_0.json`
- `analysis/donga_2011_repeat_predictive_value_v1_0.md`

freeze:

- `state/donga_2011_post_t0_peak_freeze_v1_0.json`
- `state/donga_2011_repeat_predictive_value_freeze_v1_0.json`

최신 repeat-analysis QA:

- workflow: `.github/workflows/donga-2011-postt0-seed-qa.yml`
- run ID: `32074755458`
- head commit: `f58533302bd85eabd38bcd0e62ee3dead5de27b4`
- conclusion: **success**

## 9. 다음 분석

다음 우선순위는 동아 2010과 2011을 **200 placements / 162 unique persons**의 two-wave longitudinal dataset으로 통합하는 것이다.

핵심 질문:

1. 2010-only 62명, repeat 38명, 2011-new 62명의 person-level trajectory는 어떻게 다른가?
2. repeat 38명의 2010→2011 baseline과 이후 peak가 어떻게 이동했는가?
3. placement-level precision과 person-level outcome을 분리하면 screening / persistence / apex signal이 어떻게 달라지는가?
4. 이후 이 구조를 뉴스메이커·한겨레21과 같은 Type-A common master에 연결할 수 있는가?
