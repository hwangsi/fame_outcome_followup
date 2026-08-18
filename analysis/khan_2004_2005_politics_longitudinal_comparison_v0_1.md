# 경향신문 2004–2005 정치 선정 longitudinal comparison v0.1

- 작성일: 2026-08-18
- 분석 성격: **descriptive within-domain comparison**
- 비교 대상:
  1. 경향신문 2004 「17대국회 이끌 뉴리더」 20명
  2. 경향신문 2005 「한국을 이끌 60인」 중 정치 field 10명

## 1. 왜 이 비교가 유용한가

두 cohort는 같은 언론사이고 모두 정치 분야이지만 selection design이 다르다.

### 2004 뉴리더20

- universe: 제17대 국회의원 299명
- initial pool 45명
- expert panel 40명
- party quota를 둔 국회 내부 차세대 리더 선발
- party leaders excluded
- baseline mean: **2.15**

### 2005 정치10

- parent project: 6 fields × 10 = 60 selected units
- initial candidates 1,168 → 185 → public survey n=1,266 → expert final panel
- 2006–2020 향후 15년 활동 가능성을 강조
- 정치 field는 10명 모두 person
- baseline mean: **2.60**

따라서 2004는 비교적 낮은 baseline의 국회의원 내부 신흥 리더를 적극적으로 찾은 설계이고, 2005는 이미 전국적으로 알려진 고위 정치인/대권주자까지 포함한 더 높은-baseline 설계다.

## 2. 중복 인물

두 cohort에 모두 들어간 사람은 4명이다.

- 김부겸
- 노회찬
- 박진
- 원희룡

따라서 두 cohort는 독립 표본이 아니다.

- placements: 30
- unique persons: 26
- overlap: 4

이 때문에 단순한 두 비율 차이의 독립표본 검정이나 매체/연도 우열 inference는 primary analysis로 사용하지 않는다.

## 3. Peak outcome 비교

| metric | 경향 2004 뉴리더20 | 경향 2005 정치10 |
|---|---:|---:|
| n | 20 | 10 |
| baseline mean | **2.15** | **2.60** |
| post-selection peak mean | **3.20** | **3.50** |
| Major | **20/20 = 100%** | **10/10 = 100%** |
| Apex | **4/20 = 20%** | **5/10 = 50%** |
| Advanced | **19/20 = 95%** | **8/10 = 80%** |
| Sustained high | 0 | **2/10 = 20%** |

### 해석

두 cohort 모두 결국 scope≥3의 major political leadership에 도달한 비율은 100%다.

그러나 `Advanced`는:

- 2004: 95%
- 2005: 80%

이다.

2005에서 raw Apex가 더 높은데 Advanced가 더 낮은 것은 모순이 아니다.

2005 cohort는 선정 시점부터:

- 전 장관
- 현 장관
- 광역단체장
- 전국정당 대표
- 유력 대권주자

등이 더 많이 포함되어 baseline이 높다.

따라서 이후 최고점이 높더라도 **T0보다 더 올라갈 여지가 작다.**

이 결과는 기존의 `baseline ceiling` 가설과 방향이 일관된다.

## 4. T+10 fixed-window comparison

각 cohort는 자기 selection year를 기준으로 정확히 +10년 ±1년 window를 사용한다.

- 2004 cohort: T+10 = 2014 ±1
- 2005 cohort: T+10 = 2015 ±1

| metric | 2004 T+10 | 2005 T+10 |
|---|---:|---:|
| original n | 20 | 10 |
| assessable | 20 | 9 |
| competing event | 0 | 1 |
| scope≥2 | **19/20 = 95.0%** | **7/9 = 77.8%** |
| Major ≥3 | **7/20 = 35.0%** | **3/9 = 33.3%** |
| Apex =4 | **0/20 = 0%** | **1/9 = 11.1%** |

### 핵심

Peak Major는 양쪽 모두 100%였지만, 정확히 10년 뒤 Major-role occupancy는 약 1/3이다.

- 2004: 35.0%
- 2005: 33.3%

즉 후보들의 eventual career peak가 매우 높았다는 사실은 **10년 뒤에도 장관·도지사·당대표·대통령 같은 높은 역할에 있을 것**을 의미하지 않는다.

이것이 peak와 persistence를 분리해야 하는 가장 직접적인 근거다.

## 5. T+20 fixed-window comparison

- 2004 cohort: T+20 = 2024 ±1
- 2005 cohort: T+20 = 2025 ±1

| metric | 2004 T+20 | 2005 T+20 |
|---|---:|---:|
| original n | 20 | 10 |
| assessable | 18 | 8 |
| competing event | 2 | 2 |
| scope≥2 | **12/18 = 66.7%** | **5/8 = 62.5%** |
| Major ≥3 | **6/18 = 33.3%** | **4/8 = 50.0%** |
| Apex =4 | **0/18 = 0%** | **0/8 = 0%** |

T+20 Major는 수치상 2005 정치10이 높지만 이를 연도/선정법 superiority로 해석하지 않는다.

이유:

1. assessable denominator가 18 vs 8로 매우 작다.
2. 두 cohort에 4명이 중복되어 독립 표본이 아니다.
3. 정치 역할은 선거·내각 교체 주기에 매우 민감하다.
4. target windows가 정확히 같은 달력이 아니라 1년 차이다.
5. 2005는 baseline이 더 높고 selection mechanism도 다르다.

따라서 이 차이는 **descriptive pattern**으로만 보존한다.

## 6. Peak와 persistence의 gap

### 2004

- Advanced ever: **95%**
- T+10 Major: **35%**
- T+20 Major: **33.3%**

### 2005

- Advanced ever: **80%**
- T+10 Major: **33.3%**
- T+20 Major: **50%**

두 cohort 모두 `ever rose`와 `occupied a major role at a later fixed window` 사이에 큰 gap이 있다.

이 gap은 예측 실패라기보다 outcome definition의 차이다.

예:

- 한때 총리/장관/도지사/당대표가 되었더라도 10년 또는 20년 snapshot에서는 이미 퇴임했을 수 있다.
- 전직 최고직 타이틀은 fixed-window current scope에 자동 상속하지 않는다.
- 사망은 competing event이며 실패가 아니다.

## 7. 동일 언론사 내 selection-design hypothesis

현재 관찰되는 구조는 다음 가설과 일관된다.

### 낮은 baseline의 emerging-leader selection

경향 2004:

- baseline 2.15
- Advanced 95%

### 더 높은 baseline의 broad future-leader selection

경향 2005 정치10:

- baseline 2.60
- Advanced 80%
- Apex 50%

즉 더 유명하고 높은 자리에 이미 있던 사람을 선발할수록:

- raw eventual peak/apex는 높을 수 있지만
- baseline-adjusted rise는 낮아질 수 있다.

반대로 국회의원 중 상대적으로 덜 완성된 신흥 인물을 골랐던 2004 설계에서는 future rise가 더 크게 관찰된다.

이것을 현재 단계에서 causal selection-design effect라고 부르지는 않는다.

권장 표현:

> “Within Kyunghyang's 2004–2005 political selections, the lower-baseline emerging-leader cohort showed greater baseline-adjusted advancement, whereas the higher-baseline 2005 cohort showed more apex attainment. Fixed-window major-role persistence was much lower than eventual major attainment in both cohorts. This pattern is consistent with baseline ceiling and selection-design differences, but the small, overlapping samples preclude causal or superiority claims.”

## 8. 연구 프레임에 주는 의미

이 비교를 통해 Type-A outcome은 최소 세 층으로 계속 분리해야 한다.

### 1. Selection quality

나중에 한 번이라도 major leadership에 도달했는가?

- 두 cohort 모두 100%

### 2. Future rise

T0 baseline보다 실제로 올라갔는가?

- 2004: 95%
- 2005: 80%

### 3. Elite persistence

정확한 미래 시점에도 major role에 있었는가?

- T+10: 약 1/3
- T+20: 약 1/3~1/2

이 세 질문은 서로 대체할 수 없다.

## 9. Sources

- 2004 peak / longitudinal:
  - `data/typeA/khan_2004_17th_assembly_newleaders_peak_master_v1_0.json`
  - `data/typeA/khan_2004_17th_assembly_newleaders_longitudinal_master_v1_0.json`
- 2005 politics10 peak:
  - `data/typeA/khan_2005_politics10_metrics_v1_0.json`
- 2005 politics10 longitudinal:
  - `data/typeA/khan_2005_politics10_longitudinal_metrics_v1_0.json`

## 10. Guardrails

- descriptive comparison only
- overlapping people → observations not independent
- no causal effect of selection design
- no outlet/year superiority claim
- target windows differ by one calendar year because selection years differ
- fixed-window scores do not inherit former office
- death is a competing event
- peak and snapshot remain separate outcomes
