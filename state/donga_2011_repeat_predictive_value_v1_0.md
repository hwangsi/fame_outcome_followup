# 동아일보 2011 반복선정의 prospective 추가 예측력 v1.0

**기준일:** 2026-08-18  
**분석 시점:** 2011 선정 시점에서 이미 알려진 `2010에도 선정됨` 여부를 exposure로 사용  
**설계:** observational prospective comparison from the 2011 selection time

## 1. 질문

> **2011년 선정 시점에서, 전년도 2010 리스트에도 반복 선정되었다는 정보가 당시 baseline prestige를 넘어 이후 성과에 추가적인 예측정보를 제공했는가?**

2010 cohort를 나중의 2011 재선정 여부로 나누는 기존 분석은 미래 정보를 사용하므로 association에 그쳤다. 이번 분석에서는 repeat 여부가 2011 시점에 이미 알려져 있으므로 look-ahead 문제를 피할 수 있다. 다만 repeat 여부는 무작위가 아니므로 인과효과로 해석하지 않는다.

## 2. Population과 baseline

- repeat 2010→2011: **38명**
- new 2011 entrants: **62명**
- assessable: **99명**
- not assessable: **신준호 1명** — new entrant

Frozen 2011 pre-selection lifetime baseline 분포:

| baseline score | Repeat | New |
|---:|---:|---:|
| 2 | 8 | 30 |
| 3 | 27 | 30 |
| 4 | 3 | 2 |

repeat 집단이 시작부터 훨씬 높은 baseline에 치우쳐 있으므로 raw outcome만 비교하면 안 된다.

## 3. Raw full-cohort outcomes

| Outcome | Repeat | New | Difference | Raw OR | Fisher p |
|---|---:|---:|---:|---:|---:|
| Major ≥3 | **35/38 = 92.1%** | **55/62 = 88.7%** | +3.4 pp | 1.48 | 0.738 |
| Apex =4 | **9/38 = 23.7%** | **3/62 = 4.8%** | **+18.8 pp** | **6.10** | **0.00885** |
| Advanced | **11/38 = 28.9%** | **25/62 = 40.3%** | -11.4 pp | 0.60 | 0.288 |

### Raw 해석

- **Major:** 두 집단 모두 이미 약 90%라 repeat 여부가 거의 추가 정보를 주지 않는다.
- **Apex:** repeat에서 23.7%, new에서 4.8%로 큰 차이가 난다.
- **Advanced:** raw로는 오히려 new entrant가 높다. 그러나 repeat 집단이 baseline 3–4에 훨씬 많이 몰려 있어 ceiling effect와 baseline imbalance가 크다.

## 4. Baseline-stratified analysis

신준호를 제외한 assessable 99명을 frozen baseline score 2/3/4로 층화했다.

| Outcome | MH common OR | CMH p | continuity-corrected p | Exact conditional p |
|---|---:|---:|---:|---:|
| Major ≥3 | **0.734** | 0.657 | 0.974 | **0.691** |
| Apex =4 | **8.690** | **0.0167** | **0.0421** | **0.0268** |
| Advanced | **1.825** | 0.276 | 0.445 | **0.339** |

희소한 apex 사건 때문에 asymptotic CMH만 의존하지 않고 strata margin을 조건부로 고정한 exact test도 계산했다. Apex association은 exact two-sided p=**0.0268**로 유지됐다.

## 5. Outcome별 해석

### 5.1 Major: 추가 예측력 거의 없음

raw major는 repeat 92.1% vs new 88.7%로 차이가 작고, baseline 층화 후 MH OR=0.73, exact p=0.69였다.

> **반복 선정은 ‘나중에도 major 수준인가?’를 예측하는 데는 거의 추가 정보가 없다.**

이미 2011 리스트 전체가 높은 수준의 선별 집단이라 ceiling effect가 크다.

### 5.2 Apex: 가장 강한 repeat signal

raw apex는 repeat 9/38(23.7%) vs new 3/62(4.8%)였고, baseline 층화 후에도 MH OR≈**8.69**가 남았다. Exact conditional p=**0.0268**이다.

> **2011 시점의 반복 선정은 이후 apex 도달과 강하게 연관되어 있었다.**

다만 전체 apex 사건은 12건뿐이고 baseline score 자체도 3단계의 거친 척도이므로, 이를 확정적 인과효과나 정확한 효과크기로 해석해서는 안 된다. 현재 표현은 **strong sparse-data signal / association**이 적절하다.

### 5.3 Advancement: 명확한 추가 신호 없음

raw에서는 repeat 28.9% < new 40.3%였다. 그러나 repeat 집단이 이미 baseline 3–4에 집중되어 있어 상승할 여지가 작다. 층화하면 OR 방향은 1을 넘어 **1.83**으로 뒤집히지만 exact p=0.339로 확증적이지 않다.

> **반복 선정이 ‘이전 최고점보다 더 성장할 사람’을 명확히 골라냈다는 근거는 현재 없다.**

## 6. 핵심 결론

이번 결과는 repeat selection의 의미를 세 가지로 분리해야 함을 보여준다.

1. **Major persistence:** 추가 정보 거의 없음 — 이미 두 집단 모두 높음.
2. **Apex identification:** 반복 선정에서 강한 신호 — baseline 층화 후에도 유지.
3. **Actual advancement:** 명확한 추가 예측력 없음.

따라서 반복 선정은 단순히 “더 성장할 사람”을 골라냈다기보다, **이미 강한 후보군 가운데 장차 극소수 apex까지 갈 인물을 재차 포착하는 editorial consensus signal**일 가능성이 있다.

## 7. Guardrails

- repeat status는 observational exposure이며 causal effect가 아니다.
- baseline score는 2/3/4의 비교적 거친 척도이므로 residual confounding 가능성이 있다.
- apex는 12건뿐이어서 sparse-data uncertainty가 크다.
- 반복선정자 38명은 2010·2011 두 placement를 가진 동일인이므로 향후 multi-cohort 분석에서 독립 표본처럼 세면 안 된다.
- 다음 단계에서는 2010–2011 **200 placements / 162 unique persons** 구조를 person-level로 명시해야 한다.

## 8. Reproducibility

Runtime:

- `scripts/analyze_donga_2011_repeat_predictive_value.py`
- `analysis/donga_2011_repeat_predictive_value_v1_0.json`
- `analysis/donga_2011_repeat_predictive_value_v1_0.md`

Freeze:

- `state/donga_2011_repeat_predictive_value_freeze_v1_0.json`

Final QA:

- workflow: `.github/workflows/donga-2011-postt0-seed-qa.yml`
- run ID: `32074755458`
- head commit: `f58533302bd85eabd38bcd0e62ee3dead5de27b4`
- conclusion: **success**

## 9. 다음 단계

동아 2010과 2011을 **200 placements / 162 unique persons**의 two-wave longitudinal dataset으로 묶는다.

그 다음 질문은:

- repeat 38명의 두 시점 baseline과 outcome trajectory는 어떻게 변했는가?
- 2010-only 62명, repeat 38명, 2011-new 62명의 person-level 궤적은 어떻게 다른가?
- placement-level 성과와 person-level 성과를 분리하면 언론 선정의 screening/persistence/apex signal이 어떻게 달라지는가?
