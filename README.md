# 언론사 선정 인재 추적 — Fame Outcome Follow-up

> 과거 언론이 선정한 **“미래 인재 / 차세대 리더 / 영향력 인물”**은 10년, 20년 뒤 실제로 어떻게 되었는가?

**기준일:** 2026-08-18  
**완료된 주력 코호트:** 동아일보 2010·2011 「한국을 빛낼 100인」  
**현재 단계:** **2011 outcome + repeat-selection 분석 + 2010–2011 two-wave person/placement master 완료 → Type-A common master 통합 단계**

---

## 1. 연구 질문

이 프로젝트는 언론·전문가가 특정 시점에 선정한 유망 인물들을 장기 추적해 다음을 구분해 평가한다.

1. 선정 뒤 높은 수준의 역할·성과에 도달했는가?
2. 이미 선정 전에 높았던 사람과 **선정 뒤 실제로 더 성장한 사람**을 구분할 수 있는가?
3. 반복 선정은 단년도 선정보다 추가적인 미래 정보를 주는가?
4. 순위형 리스트에서는 높은 순위가 더 큰 후속 상승을 예측하는가?
5. 매체·시대·분야·리스트 설계에 따라 신호가 달라지는가?

최종 목표는 조선·중앙·동아·한겨레·경향 등 여러 매체의 과거 인재 선정 기획을 동일한 placement/person schema와 코딩 규칙으로 복원·비교하는 것이다.

---

## 2. 핵심 방법론

### Type A — 미래예측형

- **Major**: post-selection peak `scope ≥3`
- **Apex**: `scope =4`
- **Advanced**: `post_selection_peak - pre_selection_lifetime_peak > 0`
- **Sustained high**: delta=0 and peak≥3
- **No clear advancement**: delta=0 and peak<3
- **Lower than baseline**: delta<0
- **Not assessable**: 동일인 후속자료가 충분하지 않아 강제 low score를 주지 않음

### Type B — 이미 성취한 역할모델형

Prediction accuracy보다 `T0 → T+10 → T+20 → current`의 **persistence / trajectory**를 본다.

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

## 3. 완료 코호트 요약

| 코호트 | 유형 | 상태 | Major | Apex | Advanced |
|---|---|---:|---:|---:|---:|
| 뉴스메이커 2003 정치 Top10 | Type A | 10/10 | 100% | 20% | 70% |
| 뉴스메이커 2003 경제 Top5 | Type A | 5/5 | 100% | 80% | 80% |
| 한겨레21 2004 정치 Top10 | Type A | 10/10 | 100% | 50% | 40% |
| 동아일보 2010 「2020년 한국을 빛낼 100인」 | Type A | **100/100** | **71%** | **12%** | **28%** |
| 동아일보 2011 「10년 뒤 한국을 빛낼 100인」 | Type A | **100/100 adjudicated** | **90%** | **12%** | **36%** |

Type B pilot인 동아일보 「닮고 싶고 되고 싶은 과학기술인」 2002–2005(n=39)는 longitudinal follow-up을 완료했다.

---

## 4. 동아일보 2010 — 최종

- roster / T0 / baseline / post-T0 peak: **100/100**
- unresolved: **0**
- Major: **71/100 = 71%**
- Apex: **12/100 = 12%**
- Advanced: **28/100 = 28%**
- Sustained high: **44/100 = 44%**

> **71% major attainment와 28% actual advancement는 같은 지표가 아니다.**

2010 리스트는 이미 강한 사람을 골라내는 screening과 일부의 실제 후속 상승이 섞인 구조로 해석한다.

---

## 5. 동아일보 2011 — 최종

### 데이터 완결성

- selection cutoff: **2011-04-01**
- observation end: **2026-08-18**
- adjudicated: **100/100**
- scored: **99/100**
- not assessable: **1명 — 신준호**
- pending: **0**
- repeat 2010→2011: **38명**
- new entrants: **62명**

신준호는 선정 당시 `호텔신라 조리팀 차장` identity는 확실하지만 post-T0 동일인 경력을 재현 가능하게 직접 연결할 자료가 부족해 `not_assessable`로 처리했다.

### Full-cohort conservative 결과

- Major: **90/100 = 90.0%**
- Apex: **12/100 = 12.0%**
- Advanced: **36/100 = 36.0%**
- Sustained high: **53**
- No clear advancement: **7**
- Lower than baseline: **3**
- Not assessable: **1**

Assessable-only 99명에서는 major 90.9%, apex 12.1%, advanced 36.4%다.

> **2011의 90% major attainment는 매우 강한 screening/persistence를 뜻하지만, 실제 baseline 초과 상승은 36%였다.**

---

## 6. 2011 반복선정의 prospective 추가 예측력 — 완료

2011 선정 시점에서 `2010에도 선정되었음`은 이미 알려진 정보이므로, repeat 38명과 new 62명의 이후 성과를 look-ahead 없이 비교했다.

Baseline 분포는 repeat가 훨씬 높았다.

| baseline | Repeat | New |
|---:|---:|---:|
| 2 | 8 | 30 |
| 3 | 27 | 30 |
| 4 | 3 | 2 |

### Raw outcome

| Outcome | Repeat | New | Fisher p |
|---|---:|---:|---:|
| Major ≥3 | 35/38 = **92.1%** | 55/62 = **88.7%** | 0.738 |
| Apex =4 | 9/38 = **23.7%** | 3/62 = **4.8%** | **0.00885** |
| Advanced | 11/38 = **28.9%** | 25/62 = **40.3%** | 0.288 |

### Frozen-baseline stratified

| Outcome | MH common OR | Exact conditional p |
|---|---:|---:|
| Major ≥3 | 0.734 | 0.691 |
| Apex =4 | **8.690** | **0.0268** |
| Advanced | 1.825 | 0.339 |

해석:

- **Major:** repeat의 추가 신호 거의 없음 — 양쪽 모두 ceiling에 가까움.
- **Apex:** repeat에서 강한 sparse-data association이 남음.
- **Advanced:** repeat가 실제로 더 성장할 사람을 추가로 골라냈다는 명확한 근거는 없음.

따라서 현재 데이터에서 반복선정은 **“더 성장할 사람”보다 “장차 극소수 apex까지 갈 사람을 재차 포착하는 editorial consensus signal”**에 더 가깝다. 단, observational exposure이며 apex 사건은 12건뿐이므로 causal effect로 해석하지 않는다.

상세: `state/donga_2011_repeat_predictive_value_v1_0.md`

---

## 7. 동아 2010–2011 two-wave master — 완료

두 연도를 단순히 200명의 독립 표본으로 세지 않고 placement와 person을 분리했다.

- placements: **200**
- unique persons: **162**
- 2010-only: **62**
- repeat 2010+2011: **38**
- 2011-new: **62**

### Person-level first-selection outcome

| Group | N | Major | Apex | Advanced |
|---|---:|---:|---:|---:|
| 2010-only | 62 | 58.1% | 4.8% | 27.4% |
| Repeat | 38 | **92.1%** | **23.7%** | 28.9% |
| 2011-new | 62 | **88.7%** | 4.8% | **40.3%** |

Repeat 38명에서는:

- frozen baseline: **38/38 동일**
- editorial category: **37/38 동일**, 변경 1명 = **안철수**
- advancement class: 11 advanced→advanced, 24 sustained-high→sustained-high, 3 no-clear→no-clear

**중요:** 이 38/38 class 동일을 독립적인 “1년 안정성” 증거로 해석하지 않는다. 2010·2011 post-selection window가 겹치고, 2011 repeat outcome 상당수가 2011 cutoff 이후임이 명확한 기존 post-2010 peak를 안전 승계하도록 설계되었기 때문에 class identity는 부분적으로 구조적이다.

상세:

- `state/donga_2010_2011_two_wave_freeze_v0_1.json`
- `state/donga_2010_2011_two_wave_result_v0_1.md`

---

## 8. Identity QA

이름만으로 경력을 연결하지 않는다. 실제 audit에서 발견된 위험 사례:

- 김선욱: 대학 총장 동명이인 ≠ **피아니스트 김선욱**
- 김승환: 교육감 동명이인 ≠ **POSTECH 물리학자 김승환**
- 김가영: 당구선수 동명이인 ≠ **농업유통 창업가 김가영**
- 전혜경: 농업계 동명이인 ≠ **UNICEF Senior Advisor 전혜경**

2011 신규 audit batch 3–6의 42명은 frozen T0 `category + t0_role_official_2011`을 자동 대조한다. 불일치하면 CI가 실패한다.

---

## 9. Coding / analysis guardrails

- advancement는 contemporaneous title이 아니라 **pre-selection lifetime peak** 대비 계산한다.
- adverse event는 이미 관찰된 peak를 소급해 낮추지 않는다.
- death는 failure가 아니라 exposure truncation이다.
- nomination/내정만으로 achieved peak를 올리지 않는다.
- 자료 부족은 강제 low score 대신 `not_assessable`로 남길 수 있다.
- broad screening과 ranked Top-N은 같은 precision으로 단순 비교하지 않는다.
- 중복 인물은 독립 표본으로 취급하지 않는다.
- repeat status는 observational exposure이며 causal effect가 아니다.

---

## 10. 핵심 파일

```text
state/
  coding_rules_typeA_v0_1.md
  coding_rules_typeA_sector_scope_v0_1.md
  donga_2010_post_t0_peak_freeze_v1_2.json
  donga_2010_typeA_result_v1_0.md
  donga_2011_baseline_freeze_v1_0.json
  donga_2011_post_t0_peak_freeze_v1_0.json
  donga_2011_typeA_result_v1_0.md
  donga_2011_repeat_predictive_value_freeze_v1_0.json
  donga_2011_repeat_predictive_value_v1_0.md
  donga_2010_2011_two_wave_freeze_v0_1.json
  donga_2010_2011_two_wave_result_v0_1.md

scripts/
  build_donga_2010_post_t0_peak_master.py
  build_donga_2011_post_t0_master.py
  analyze_donga_2011_repeat_predictive_value.py
  build_donga_2010_2011_two_wave_master.py

analysis/  # runtime-generated
  donga_2011_post_t0_master_v1_0.json
  donga_2011_post_t0_metrics_v1_0.json
  donga_2011_repeat_predictive_value_v1_0.json
  donga_2010_2011_two_wave_master_v0_1.json
```

---

## 11. QA / reproducibility

Workflow:

`/.github/workflows/donga-2011-postt0-seed-qa.yml`

최신 two-wave QA run:

- run ID: **32075435387**
- head: `7fcbe80456b6be1d1c8804ebd29208327917604f`
- conclusion: **success**

이 workflow는 2010/2011 baseline부터 final 2011 master, repeat exact analysis, two-wave placement/person master까지 재생성·검증한다.

---

## 12. 다음 우선순위

1. **Type-A common placement/person master v0.1** 구축
   - 뉴스메이커 2003 정치10 + 경제5
   - 한겨레21 2004 정치10
   - 동아 2010 100
   - 동아 2011 100
2. cohort design을 `ranked_topN / broad_screening / explicit_horizon`으로 명시
3. 모든 placement를 canonical person에 연결하고 cross-cohort overlap을 검증
4. placement-level과 person-level 결과를 분리한 cross-cohort comparison v0.3 작성
5. 한겨레21 full31 / 1999 archive recovery 및 다른 신문사로 확장
6. 충분한 표본이 쌓이면 person-clustered / mixed-effects model과 matched control을 도입

현재 가장 중요한 다음 작업은 **“225 placements를 독립 225명으로 오해하지 않도록 common placement/person schema를 만드는 것”**이다.
