# 언론사 선정 인재 추적 — Fame Outcome Follow-up

> 과거 언론이 선정한 **“미래 인재 / 차세대 리더 / 영향력 인물”**은 10년, 20년 뒤 실제로 어떻게 되었는가?

**기준일:** 2026-08-18  
**현재 단계:** **Type-A common master v0.2 + cross-cohort comparison v0.3 완료 → 한겨레21 2004 full31 복원 진행**

---

## 1. 연구 질문

이 프로젝트는 언론·전문가가 특정 시점에 선정한 유망 인물을 장기 추적해 다음을 분리해 평가한다.

1. 선정 뒤 높은 수준의 역할·성과에 도달했는가?
2. 이미 선정 전에 높았던 사람과 **선정 뒤 실제로 더 성장한 사람**을 구분할 수 있는가?
3. 반복 선정은 단년도 선정보다 추가적인 미래 정보를 주는가?
4. 순위형 리스트에서는 높은 순위가 더 큰 후속 상승을 예측하는가?
5. 매체·시대·분야·리스트 설계에 따라 신호가 달라지는가?

최종 목표는 조선·중앙·동아·한겨레·경향 등 여러 매체의 과거 인재 선정 기획을 동일한 placement/person schema와 코딩 규칙으로 복원·비교하는 것이다.

---

## 2. 핵심 지표

### Type A — 미래예측형

- **Major**: post-selection peak `scope ≥3`
- **Apex**: `scope =4`
- **Advanced**: `post_selection_peak - pre_selection_lifetime_peak > 0`
- **Sustained high**: delta=0 and peak≥3
- **No clear advancement**: delta=0 and peak<3
- **Lower than baseline**: delta<0
- **Not assessable**: 동일인 후속자료가 충분하지 않아 강제 low score를 주지 않음

### Scope score

| score | 의미 |
|---:|---|
| 0 | meaningful role/achievement 미확인 또는 직접 자료 부족 |
| 1 | 제한적·지역적·간헐적 활동 |
| 2 | 전국 단위에서 확립된 전문직·창작자·선수·기관 리더 |
| 3 | 국내 최상위권 또는 뚜렷한 국제적 리더십/성과 |
| 4 | 국가·세계적 apex 또는 field-defining achievement |

세부 기준: `state/coding_rules_typeA_v0_1.md`, `state/coding_rules_typeA_sector_scope_v0_1.md`

---

## 3. 완료된 Type-A cohort units

| cohort | n | Major | Apex | Advanced |
|---|---:|---:|---:|---:|
| 뉴스메이커 2003 정치 Top10 | 10 | 100% | 20% | 70% |
| 뉴스메이커 2003 경제 Top5 | 5 | 100% | 80% | 80% |
| 한겨레21 2004 정치 Top10 | 10 | 100% | 50% | 40% |
| 동아일보 2010 「2020년 한국을 빛낼 100인」 | 100 | **71%** | **12%** | **28%** |
| 동아일보 2011 「10년 뒤 한국을 빛낼 100인」 | 100 | **90%** | **12%** | **36%** |

동아 2011은 100/100 adjudication 완료, 99 scored, `신준호` 1명만 `not_assessable`, pending 0이다.

---

## 4. 동아일보 2011 핵심 결과

Full-cohort conservative:

- Major: **90/100 = 90.0%**
- Apex: **12/100 = 12.0%**
- Advanced: **36/100 = 36.0%**
- Sustained high: **53**

> **90% major attainment와 36% actual advancement는 같은 지표가 아니다.**

2011 리스트는 강한 screening/persistence를 보였지만, 선정 이전 lifetime peak를 실제로 넘어선 비율은 그보다 훨씬 낮았다.

### Repeat 38 vs new 62 — prospective from 2011 selection time

| Outcome | Repeat | New | baseline-stratified exact p |
|---|---:|---:|---:|
| Major ≥3 | 92.1% | 88.7% | 0.691 |
| Apex =4 | **23.7%** | **4.8%** | **0.0268** |
| Advanced | 28.9% | 40.3% | 0.339 |

반복선정은 major persistence나 actual advancement보다 **후속 apex identification**에서 더 강한 sparse-data signal을 보였다. 이는 observational association이며 causal effect가 아니다.

상세: `state/donga_2011_repeat_predictive_value_v1_0.md`

---

## 5. 동아 2010–2011 two-wave master

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

## 6. Type-A common master v0.2 — 완료

현재 공통 데이터셋:

- **225 placements**
- **179 unique persons**
- **43 repeated persons**
- placement count: 1회 136명 / 2회 40명 / 3회 3명
- 3회 선정: **안철수, 유시민, 이재용**
- not-assessable placement: **1**

### Placement-level naïve descriptive

- Major: **186/225 = 82.7%**
- Apex: **35/225 = 15.6%**
- Advanced: **79/225 = 35.1%**

이 수치는 inferential metric이 아니다. 43명이 반복 등장해 observations가 독립이 아니며, year/domain/design/list depth가 서로 confounded되어 있다.

### Person-level first-selection descriptive

중복을 제거하고 179명의 첫 선정만 사용하면:

- Major: **143/179 = 79.9%**
- Apex: **21/179 = 11.7%**
- Advanced: **64/179 = 35.8%**

### Design-level descriptive

| Design | placements | unique persons | Major | Apex | Advanced |
|---|---:|---:|---:|---:|---:|
| ranked TopN | 25 | 21 | 100% | 44% | 60% |
| broad screening + explicit horizon | 200 | 162 | 80.5% | 12% | 32% |

이 차이를 outlet effect로 해석하지 않는다. selection year, domain, list depth, mechanism이 동시에 다르다.

상세:

- `data/typeA/typeA_common_master_v0_2.json`
- `data/typeA/typeA_common_master_v0_2.csv`
- `data/typeA/typeA_common_metrics_v0_2.json`
- `state/typeA_common_master_freeze_v0_2.json`
- `analysis/typeA_cross_cohort_comparison_v0_3.md`

---

## 7. Identity QA

이름만 같다고 동일인으로 merge하지 않는다.

실제 audit에서 발견된 위험 사례:

- 김선욱: 대학 총장 동명이인 ≠ **피아니스트 김선욱**
- 김승환: 교육감 동명이인 ≠ **POSTECH 물리학자 김승환**
- 김가영: 당구선수 동명이인 ≠ **농업유통 창업가 김가영**
- 전혜경: 농업계 동명이인 ≠ **UNICEF Senior Advisor 전혜경**

Common master에서는 frozen Dong-A repeat set 또는 별도 verified overlap에 속하지 않는 새로운 same-name collision이 나타나면 builder가 fail한다.

---

## 8. 현재까지 가장 안정적인 해석

1. **Selection** — 확보된 코호트에서 언론/전문가가 장기적으로 높은 위치에 남는 후보군을 고르는 능력은 상당히 보인다.
2. **Advancement** — raw major rate는 이미 높은 사람의 persistence를 포함하므로 미래 성장 예측력을 과대평가할 수 있다.
3. **Ranking** — 현재 확보된 ranked cohorts에서는 순위와 이후 advancement의 관계가 약하다.
4. **Re-selection** — baseline-adjusted growth보다 elite persistence/apex identification에 더 가까운 신호다.
5. **Comparison unit** — outlet comparison보다 list design, year, domain, depth를 먼저 분리해야 한다.

> **현재 자료에서 언론은 ‘누가 강한 후보인가’를 고르는 능력은 꽤 보이지만, ‘비슷한 출발점에서 누가 더 크게 성장할 것인가’를 추가로 맞히는 능력은 훨씬 약하게 보인다.**

---

## 9. Reproducibility

Main QA workflow:

`.github/workflows/donga-2011-postt0-seed-qa.yml`

이 workflow는 2010/2011 baseline → 2011 final master → repeat exact analysis → two-wave master → common master v0.2 → cross-cohort v0.3까지 재생성·검증한다.

Common master freeze commit:

`f4b305153d28a509a4cae3c4f7c0e41ceb5bf246`

---

## 10. 현재 우선순위

### 1. 한겨레21 2004 full31 복원

현재 31명 중:

- Top10 이름은 모두 복원
- 추가로 `이인제` 22위 확인
- **11–21위, 23–31위 총 20명 미복원**

Top10 truncation을 해소해야 rank gradient와 selection-depth effect를 더 제대로 볼 수 있다.

### 2. 비교 가능한 추가 Type-A cohort 확보

조선·중앙·경향 등에서 같은 시기·분야·list depth를 가진 cohort를 우선 복원한다.

### 3. 이후 inferential model

표본이 충분해지면 person-clustered / mixed-effects model과 matched control을 도입한다.

현재 정확한 다음 작업점은 **한겨레21 2004 후보 31명 전체표의 누락 20명을 원문/스캔에서 복원하는 것**이다.
