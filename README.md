# 언론사 선정 인재 추적 — Fame Outcome Follow-up

> 과거 언론이 선정한 **“미래 인재 / 차세대 리더 / 영향력 인물”**은 10년, 20년 뒤 실제로 어떻게 되었는가?

**기준일:** 2026-08-18  
**현재 단계:** **Type-A common metrics v0.4 + 경향 2004/2005 longitudinal reference 완료 + common longitudinal schema v0.1 정의 → Dong-A 2010 target2020/T+10 harmonization 진행**

---

## 1. 연구 질문

이 프로젝트는 언론·전문가가 특정 시점에 선정한 유망 인물을 장기 추적해 다음을 분리해 평가한다.

1. 선정 뒤 높은 수준의 역할·성과에 도달했는가?
2. 이미 선정 전에 높았던 사람과 **선정 뒤 실제로 더 성장한 사람**을 구분할 수 있는가?
3. 특정 T+10/T+20 시점에도 높은 역할을 점유하고 있었는가?
4. 반복 선정은 단년도 선정보다 추가적인 미래 정보를 주는가?
5. 원 기사에 explicit target year가 있을 때 실제 해당 시점 예측은 맞았는가?
6. 매체·시대·분야·리스트 설계에 따라 신호가 달라지는가?

최종 목표는 조선·중앙·동아·한겨레·경향 등 여러 매체의 과거 인재 선정 기획을 동일한 placement/person schema와 코딩 규칙으로 복원·비교하는 것이다.

---

## 2. 핵심 outcome architecture

Type-A는 이제 최소 네 층을 분리한다.

### A. Baseline

선정 시점의 지위·역할.

### B. Lifetime post-selection peak

선정 뒤 관찰기간 전체에서 도달한 최고 수준.

- **Major**: post-selection peak `scope ≥3`
- **Apex**: `scope =4`
- **Advanced**: `post_selection_peak > baseline_scope`
- **Sustained high**: delta=0 and peak≥3
- **No clear advancement**: delta=0 and peak<3
- **Lower than baseline**: delta<0

### C. Fixed-window snapshot

정확한 T+10/T+20 시점에 실제로 어떤 역할을 점유했는지 평가한다.

- `scope ≥2 at window`
- `Major at window = scope ≥3`
- `Apex at window = scope =4`

Lifetime peak와 fixed-window snapshot은 서로 다른 outcome이다.

### D. Explicit article target

기사 자체가 “2020년에 빛날 사람”처럼 특정 미래 연도를 명시한 경우 별도 prediction layer로 저장한다.

같은 관측연도가 generic T+10/T+20과 정확히 겹치면 독립 관측으로 두 번 세지 않는다. 한 개 canonical snapshot에 semantic alias만 여러 개 부여한다.

세부 규칙:

- `state/coding_rules_typeA_v0_1.md`
- `state/coding_rules_typeA_sector_scope_v0_1.md`
- `state/coding_rules_typeA_longitudinal_v0_1.md`
- `state/typeA_common_longitudinal_schema_v0_1.json`

---

## 3. Scope score

| score | 의미 |
|---:|---|
| 0 | meaningful role/achievement 미확인 또는 직접 자료 부족 |
| 1 | 제한적·지역적·간헐적 활동 |
| 2 | 전국 단위에서 확립된 전문직·창작자·선수·기관 리더 |
| 3 | 국내 최상위권 또는 뚜렷한 국제적 리더십/성과 |
| 4 | 국가·세계적 apex 또는 field-defining achievement |

---

## 4. 주요 완료 Type-A cohort

| cohort | n | Lifetime Major | Lifetime Apex | Advanced |
|---|---:|---:|---:|---:|
| 뉴스메이커 2003 정치 Top10 | 10 | 100% | 20% | 70% |
| 뉴스메이커 2003 경제 Top5 | 5 | 100% | 80% | 80% |
| 한겨레21 2004 정치 Top10 | 10 | 100% | 50% | 40% |
| 경향신문 2004 「17대국회 이끌 뉴리더」 | 20 | 100% | 20% | 95% |
| 경향신문 2005 「한국을 이끌 60인」 정치10 | 10 | 100% | 50% | 80% |
| 동아일보 2010 「2020년 한국을 빛낼 100인」 | 100 | **71%** | **12%** | **28%** |
| 동아일보 2011 「10년 뒤 한국을 빛낼 100인」 | 100 | **90%** | **12%** | **36%** |

동아 2011은 100/100 adjudication 완료, 99 scored, `신준호` 1명만 `not_assessable`, pending 0이다.

---

## 5. 경향 2005 full longitudinal freeze

경향신문 2005 「한국을 이끌 60인」은 현재 Type-A mixed-unit longitudinal reference cohort다.

- original selected units = **60**
- persons = **57**
- organizations = **3**
- T+10 outcome paths = **60/60**
- T+20 outcome paths = **60/60**

### Person57 lifetime peak

- Major = **53/57 = 93.0%**
- Apex = **24/57 = 42.1%**
- Advanced = **24/57 = 42.1%**

### T+10

- assessable = 54
- competing event = 3
- Scope ≥2 = **50/54 = 92.6%**
- Major = **27/54 = 50.0%**
- Apex = **3/54 = 5.6%**

### T+20

- assessable = 52
- competing event = 5
- Scope ≥2 = **44/52 = 84.6%**
- Major = **27/52 = 51.9%**
- Apex = **10/52 = 19.2%**

핵심:

> **eventual high achievement, baseline-adjusted rise, fixed-window persistence는 서로 다른 outcome이다.**

관련 파일:

- `data/typeA/khan_2005_korea_leaders60_longitudinal_completion_v1_0.json`
- `state/khan_2005_korea_leaders60_longitudinal_freeze_v1_0.json`

---

## 6. 경향 2004–2005 정치 longitudinal 비교

비교 cohort:

- 경향 2004 「17대국회 이끌 뉴리더」 20명
- 경향 2005 「한국을 이끌 60인」 정치10

중복 인물:

- 김부겸
- 노회찬
- 박진
- 원희룡

따라서 30 placements이지만 unique persons는 26이며 독립 표본이 아니다.

### Lifetime peak

| metric | 경향 2004 | 경향 2005 정치10 |
|---|---:|---:|
| n | 20 | 10 |
| baseline mean | 2.15 | 2.60 |
| post peak mean | 3.20 | 3.50 |
| Major | 100% | 100% |
| Apex | 20% | 50% |
| Advanced | **95%** | **80%** |

### T+10

| metric | 경향 2004 | 경향 2005 정치10 |
|---|---:|---:|
| assessable | 20 | 9 |
| Scope ≥2 | 95.0% | 77.8% |
| Major | **35.0%** | **33.3%** |
| Apex | 0% | 11.1% |

### T+20

| metric | 경향 2004 | 경향 2005 정치10 |
|---|---:|---:|
| assessable | 18 | 8 |
| Scope ≥2 | 66.7% | 62.5% |
| Major | **33.3%** | **50.0%** |
| Apex | 0% | 0% |

두 cohort 모두 lifetime Major는 100%지만 특정 T+10/T+20 시점의 Major-role occupancy는 훨씬 낮다.

상세:

`analysis/khan_2004_2005_politics_longitudinal_comparison_v0_1.md`

---

## 7. Competing-event 규칙

v0.1 longitudinal schema에서는 **death를 표준 competing event**로 처리한다.

- original cohort denominator에는 유지
- window `status = competing_event`
- `scope_score = null`
- window-specific assessable denominator에서는 제외
- 0점, 실패, exit로 강제 변환하지 않음

따라서 T+10/T+20 결과는 항상 original N과 assessable N을 함께 보고한다.

---

## 8. Dong-A 2010: target2020과 T+10 harmonization

동아일보 2010 cohort는 선정 시점이 2010이고 기사 자체가 「2020년 한국을 빛낼 100인」이므로:

- explicit target year = **2020**
- generic T+10 center = **2020**

같은 시간창이면 두 개의 독립 outcome을 만들지 않는다.

한 개의 canonical snapshot을 만들고:

`aliases = ["explicit_target_2020", "t10"]`

로 연결한다.

즉 같은 2020 관측을:

- article prediction 분석에서는 explicit-target outcome으로 사용 가능
- longitudinal persistence 분석에서는 T+10 outcome으로 사용 가능
- pooled denominator에서는 **한 번만 계산**

현재 semantic adapter:

`data/typeA/donga_2010_common_longitudinal_adapter_v0_1.json`

다음 QA는 기존 target2020 layer가 실제로 사용한 exact time tolerance가 common T+10 default `2020 ±1 year`와 같은지 확인하는 것이다.

---

## 9. 동아일보 2011 핵심 결과

Full-cohort conservative:

- Major: **90/100 = 90.0%**
- Apex: **12/100 = 12.0%**
- Advanced: **36/100 = 36.0%**
- Sustained high: **53**

> **90% major attainment와 36% actual advancement는 같은 지표가 아니다.**

2011 리스트는 강한 screening/persistence를 보였지만, 선정 이전 baseline을 실제로 넘어선 비율은 그보다 훨씬 낮았다.

### Repeat 38 vs new 62 — prospective from 2011 selection time

| Outcome | Repeat | New | baseline-stratified exact p |
|---|---:|---:|---:|
| Major ≥3 | 92.1% | 88.7% | 0.691 |
| Apex =4 | **23.7%** | **4.8%** | **0.0268** |
| Advanced | 28.9% | 40.3% | 0.339 |

반복선정은 major persistence나 actual advancement보다 **후속 apex identification**에서 더 강한 sparse-data signal을 보였다. 이는 observational association이며 causal effect가 아니다.

상세: `state/donga_2011_repeat_predictive_value_v1_0.md`

---

## 10. 동아 2010–2011 two-wave master

두 연도를 200명의 독립 표본으로 세지 않고 placement와 person을 분리했다.

- placements: **200**
- unique persons: **162**
- 2010-only: **62**
- repeat: **38**
- 2011-new: **62**

Person-level first-selection outcomes:

| Group | N | Major | Apex | Advanced |
|---|---:|---:|---:|---:|
| 2010-only | 62 | 58.1% | 4.8% | 27.4% |
| Repeat | 38 | 92.1% | 23.7% | 28.9% |
| 2011-new | 62 | 88.7% | 4.8% | 40.3% |

Repeat 38의 2010→2011 advancement class가 동일한 것은 독립적인 안정성 증거가 아니다. 두 observation window가 겹치고 안전한 post-2011 peak inheritance가 포함되므로 부분적으로 구조적이다.

Files:

- `state/donga_2010_2011_two_wave_freeze_v0_1.json`
- `state/donga_2010_2011_two_wave_result_v0_1.md`

---

## 11. Type-A common layer

현재 stable full placement master는 **v0.3**이며, metrics layer는 **v0.4**까지 진행되어 있다.

### Stable full placement master v0.3

- `data/typeA/typeA_common_master_v0_3.json`
- `data/typeA/typeA_common_master_v0_3.csv`

### Metrics layer v0.4

- `data/typeA/typeA_common_metrics_v0_4.json`

v0.4 full master materialization은 아직 pending이다.

Pending:

- `data/typeA/typeA_common_master_v0_4.json`
- `data/typeA/typeA_common_master_v0_4.csv`

---

## 12. Identity QA

이름만 같다고 동일인으로 merge하지 않는다.

실제 audit에서 발견된 위험 사례:

- 김선욱: 대학 총장 동명이인 ≠ **피아니스트 김선욱**
- 김승환: 교육감 동명이인 ≠ **POSTECH 물리학자 김승환**
- 김가영: 당구선수 동명이인 ≠ **농업유통 창업가 김가영**
- 전혜경: 농업계 동명이인 ≠ **UNICEF Senior Advisor 전혜경**

Common master에서는 frozen Dong-A repeat set 또는 별도 verified overlap에 속하지 않는 새로운 same-name collision이 나타나면 builder가 fail한다.

---

## 13. 현재까지 가장 안정적인 해석

1. **Selection quality** — 확보된 코호트에서 언론/전문가가 장기적으로 높은 위치에 도달할 후보군을 고르는 능력은 상당히 보인다.
2. **Future rise** — raw lifetime Major rate는 이미 높은 사람의 persistence를 포함하므로 미래 성장 예측력을 과대평가할 수 있다.
3. **Elite persistence** — lifetime peak와 정확한 T+10/T+20 role occupancy는 크게 다를 수 있다.
4. **Ranking** — 현재 확보된 ranked cohorts에서는 순위와 이후 advancement의 관계가 약하다.
5. **Re-selection** — baseline-adjusted growth보다 elite persistence/apex identification에 더 가까운 신호다.
6. **Comparison unit** — outlet comparison보다 list design, year, domain, depth와 follow-up window를 먼저 분리해야 한다.

> **현재 자료에서 언론은 ‘누가 강한 후보인가’를 고르는 능력은 꽤 보이지만, ‘비슷한 출발점에서 누가 더 크게 성장할 것인가’와 ‘정확히 10년·20년 뒤에도 누가 높은 역할에 있을 것인가’는 별개의 예측 문제다.**

---

## 14. Reproducibility

Main QA workflow:

`.github/workflows/donga-2011-postt0-seed-qa.yml`

기존 workflow는 2010/2011 baseline → 2011 final master → repeat exact analysis → two-wave master → common master 계열을 재생성·검증한다.

Longitudinal common schema는 현재 별도 reference layer로 추가되었으며 이후 workflow 통합 예정이다.

---

## 15. 현재 우선순위

### 1. Dong-A 2010 target2020 exact-window QA

기존 `target2020` outcome layer가 실제로 사용한 시간 tolerance를 확인한다.

- common T+10 default = `2020 ±1 year`
- 동일하면 기존 2020 outcome을 canonical T+10 snapshot으로 alias
- 다르면 explicit-target과 generic T+10 window를 분리하고 overlap을 명시

### 2. Dong-A 2011 generic T+10 longitudinal layer

2011 selection 기준 T+10 = **2021 ±1 year** snapshot을 구축한다.

### 3. 경향 2004/2005 common-schema adapters

기존 frozen longitudinal data를 변경하지 않고 common schema reference adapter로 정리한다.

### 4. Type-A common master v0.4 materialization

metrics v0.4와 일치하는 full placement JSON/CSV를 생성한다.

### 5. 추가 comparable Type-A cohort 확보

조선·중앙·한겨레·경향 등에서 같은 시기·분야·list depth를 가진 cohort를 우선 복원한다.

---

## 16. 최근 진행 리포

현재 checkpoint:

`progress_2026-08-18_v26.md`

v26에서 완료:

- Type-A common longitudinal schema v0.1
- machine-readable schema
- Dong-A 2010 target2020/T+10 semantic adapter

다음 deterministic 작업은 **Dong-A 2010 exact-window QA**다.
