# 언론사 선정 인재 추적 — Fame Outcome Follow-up

> 과거 언론이 선정한 **“미래 인재 / 차세대 리더 / 영향력 인물”**은 10년, 20년 뒤 실제로 어떻게 되었는가?

**기준일:** 2026-08-18  
**현재 단계:** **동아 2010/2011 lifetime + T+10 완료, 2010–2011 harmonized comparison 완료, Type-A common longitudinal metrics v0.1 freeze 완료**

---

## 1. 연구 질문

언론·전문가가 특정 시점에 선정한 유망 인물을 장기 추적해 다음을 분리한다.

1. 선정 뒤 높은 수준의 역할·성과에 도달했는가?
2. 선정 시점보다 실제로 더 성장했는가?
3. 정확한 T+10/T+20 시점에도 높은 역할을 점유했는가?
4. 반복 선정은 추가적인 미래 신호를 주는가?
5. 기사에 explicit target year가 있을 때 실제 해당 시점 결과는 어떠했는가?
6. 매체·시대·분야·list design에 따라 신호가 어떻게 달라지는가?

최종 목표는 조선·중앙·동아·한겨레·경향 등 여러 매체의 과거 인재 선정 기획을 동일한 placement/person schema와 코딩 규칙으로 복원·비교하는 것이다.

---

## 2. Outcome architecture

### A. Baseline
선정 시점의 실제 지위·역할.

### B. Lifetime post-selection peak
선정 뒤 관찰기간 전체에서 도달한 최고 수준.

- **Major** = peak `scope ≥3`
- **Apex** = `scope =4`
- **Advanced** = `post_selection_peak > baseline_scope`
- **Sustained high** = delta=0 and peak≥3

### C. Fixed-window snapshot
T+10/T+20 시점에 실제로 점유한 역할.

- `scope ≥2 at window`
- `Major at window = scope ≥3`
- `Apex at window = scope =4`

**Lifetime peak와 fixed-window snapshot은 다른 outcome이다.**

### D. Explicit article target
기사 자체가 특정 미래 연도를 명시하면 별도 prediction semantic layer로 저장한다. Generic T+10/T+20과 calendar window가 완전히 같으면 한 canonical snapshot에 semantic alias만 여러 개 부여하고 두 번 세지 않는다.

Core rules:

- `state/coding_rules_typeA_v0_1.md`
- `state/coding_rules_typeA_sector_scope_v0_1.md`
- `state/coding_rules_typeA_longitudinal_v0_1.md`
- `state/typeA_common_longitudinal_schema_v0_1.json`

---

## 3. Scope score

| score | 의미 |
|---:|---|
| 0 | target 시점 meaningful active role 미확인 |
| 1 | 제한적·지역적·간헐적 활동 |
| 2 | 전국 단위에서 확립된 전문직·창작자·선수·기관 리더 |
| 3 | 국내 최상위권 또는 뚜렷한 국제적 리더십/성과 |
| 4 | 국가·세계적 apex 또는 field-defining achievement |

직접 근거가 부족하거나 동일인 연결이 불안정하면 억지로 0점을 주지 않고 `untraceable/unresolved`로 남긴다.

---

## 4. 주요 lifetime 결과

| cohort | n | Lifetime Major | Lifetime Apex | Advanced |
|---|---:|---:|---:|---:|
| 뉴스메이커 2003 정치 Top10 | 10 | 100% | 20% | 70% |
| 뉴스메이커 2003 경제 Top5 | 5 | 100% | 80% | 80% |
| 한겨레21 2004 정치 Top10 | 10 | 100% | 50% | 40% |
| 경향 2004 「17대국회 이끌 뉴리더」 | 20 | 100% | 20% | 95% |
| 경향 2005 「한국을 이끌 60인」 person57 | 57 | 93.0% | 42.1% | 42.1% |
| 동아 2010 「2020년 한국을 빛낼 100인」 | 100 | **71%** | **12%** | **28%** |
| 동아 2011 「10년 뒤 한국을 빛낼 100인」 | 100 | **90%** | **12%** | **36%** |

---

## 5. Type-A common longitudinal metrics v0.1

Files:

- `data/typeA/typeA_common_longitudinal_metrics_v0_1.json`
- `state/typeA_common_longitudinal_metrics_freeze_v0_1.json`

### T+10

| cohort | assessable | Scope ≥2 | Major ≥3 | Apex =4 |
|---|---:|---:|---:|---:|
| 경향 2004 정치20 | 20 | **95.0%** | **35.0%** | 0% |
| 경향 2005 person57 | 54 | **92.6%** | **50.0%** | 5.6% |
| 동아 2010 | 87 | **97.7%** | **48.3%** | 5.7% |
| 동아 2011 | 90 | **96.7%** | **70.0%** | 4.4% |

현재 완료된 네 longitudinal unit에서:

- Scope ≥2 = **92.6–97.7%**
- Major = **35.0–70.0%**
- Apex = **0–5.7%**

즉 broad establishment는 T+10에서 거의 포화되어 있지만, **Major-role occupancy가 더 변별력 있는 fixed-window outcome**이다.

### 현재 확보된 T+20

| cohort | assessable | Scope ≥2 | Major ≥3 | Apex =4 |
|---|---:|---:|---:|---:|
| 경향 2004 정치20 | 18 | 66.7% | 33.3% | 0% |
| 경향 2005 person57 | 52 | 84.6% | 51.9% | 19.2% |

---

## 6. Competing event

v0.1에서는 **death를 표준 competing event**로 처리한다.

- original denominator에는 유지
- snapshot `status = competing_event`
- `scope_score = null`
- primary assessable denominator에서는 제외
- 0점/실패로 강제 변환하지 않음

모든 fixed-window 결과는 original N, assessable N, competing event N, unresolved/untraceable N을 함께 보고한다.

---

## 7. Dong-A 2010: explicit target2020 = T+10

선정연도 2010, explicit target year 2020.

- target window = **2019–2021**
- generic T+10 window = **2019–2021**
- canonical aliases = `["explicit_target_2020", "t10"]`

Freeze:

- `state/donga_2010_target2020_freeze_v1_0.json`
- `state/donga_2010_target2020_t10_harmonization_freeze_v1_0.json`

T+10/target2020:

- original N = **100**
- assessable = **87**
- competing event = **3**
- unresolved = **10**
- Scope ≥2 = **85/87 = 97.7%**
- Major = **42/87 = 48.3%**
- Apex = **5/87 = 5.7%**

---

## 8. Dong-A 2011 lifetime + T+10

### Lifetime

- Major = **90/100 = 90.0%**
- Apex = **12/100 = 12.0%**
- Advanced = **36/100 = 36.0%**

Repeat38 vs new62 lifetime:

| Outcome | Repeat | New | baseline-stratified exact p |
|---|---:|---:|---:|
| Major ≥3 | 92.1% | 88.7% | 0.691 |
| Apex =4 | **23.7%** | **4.8%** | **0.0268** |
| Advanced | 28.9% | 40.3% | 0.339 |

### T+10

- target = **2021**
- admissible window = **2020–2022**
- exact 2021 evidence 우선
- lifetime peak 복사 금지

Files:

- `data/typeA/donga_2011_t10_final_master_v1_0.json`
- `data/typeA/donga_2011_t10_metrics_v1_0.json`
- `state/donga_2011_t10_freeze_v1_0.json`
- `analysis/donga_2011_t10_result_v1_0.md`

Final coverage/results:

- original N = **100**
- assessable = **90**
- competing event = **1**
- untraceable = **9**
- exact 2021 / explicit 2021-tenure evidence = **81/90**
- Scope ≥2 = **87/90 = 96.7%**
- Major = **63/90 = 70.0%**
- Apex = **4/90 = 4.4%**

Fixed-window가 lifetime peak와 달라진 예:

- 이주호: 2022 부총리 3 → **2021 KDI 교수 2**
- 봉준호: 2020 Academy apex 4 → **2021 감독 역할 3**
- 손흥민: 2022 Golden Boot 4 → **2021 역할 3**
- 유범재: 2020 학회장 3 → **2021 KIST 연구자·명예회장 2**
- 오세훈: 2020 총선후보 2 → **2021 서울시장 3**

---

## 9. Dong-A 2010 vs 2011 harmonized T+10

Files:

- `analysis/donga_2010_2011_t10_harmonized_comparison_v1_0.json`
- `analysis/donga_2010_2011_t10_harmonized_comparison_v1_0.md`
- `state/donga_2010_2011_t10_comparison_freeze_v1_0.json`

| metric | 2010 | 2011 | 2011 − 2010 |
|---|---:|---:|---:|
| Scope ≥2 | 97.7% | 96.7% | −1.0 pp |
| Major ≥3 | **48.3%** | **70.0%** | **+21.7 pp** |
| Apex =4 | 5.7% | 4.4% | −1.3 pp |

100 vs 100을 독립표본처럼 검정하지 않는다.

- placements = **200**
- unique persons = **162**
- repeat = **38**
- 2010-only = **62**
- 2011-new = **62**
- 두 T+10 window는 2020–2021을 공통 포함

따라서 +21.7 pp Major 차이는 **descriptive cohort contrast**이며 causal estimate가 아니다.

### 162 unique-person first-selection sensitivity

- unique N = **162**
- assessable = **144**
- competing event = **3**
- unresolved/untraceable = **15**
- Scope ≥2 = **140/144 = 97.2%**
- Major = **80/144 = 55.6%**
- Apex = **6/144 = 4.2%**

Repeat 38명은 첫 선정인 2010에 한 번만 귀속한다. 이것은 common-calendar snapshot이 아니라 **first-selection 기준 person-specific T+10**이다.

---

## 10. Two-wave identity layer

- placements = **200**
- unique persons = **162**
- 2010-only = **62**
- repeat = **38**
- 2011-new = **62**

Lifetime first-selection groups:

| Group | N | Major | Apex | Advanced |
|---|---:|---:|---:|---:|
| 2010-only | 62 | 58.1% | 4.8% | 27.4% |
| Repeat | 38 | 92.1% | 23.7% | 28.9% |
| 2011-new | 62 | 88.7% | 4.8% | 40.3% |

Files:

- `state/donga_2010_2011_two_wave_freeze_v0_1.json`
- `state/donga_2010_2011_two_wave_result_v0_1.md`

---

## 11. Type-A common layers

### Lifetime layer

Stable committed full placement master:

- `data/typeA/typeA_common_master_v0_3.json`
- `data/typeA/typeA_common_master_v0_3.csv`

Committed metrics:

- `data/typeA/typeA_common_metrics_v0_4.json`

v0.4 builder:

- `scripts/build_typeA_common_master_v0_4.py`

**현재 repo에는 다음 generated v0.4 artifacts가 아직 materialize되어 있지 않다:**

- `data/typeA/typeA_common_master_v0_4.json`
- `data/typeA/typeA_common_master_v0_4.csv`
- `state/typeA_common_master_freeze_v0_4.json`

이 gap은 다음 파일에 명시한다.

- `state/typeA_common_v0_4_materialization_gap_v0_1.json`

즉 v0.4 분석 정의와 builder는 존재하고 metrics도 commit되어 있지만, full row-level generated artifact/freeze의 repo materialization은 아직 pending이다.

### Longitudinal layer

- `data/typeA/typeA_common_longitudinal_metrics_v0_1.json`
- `state/typeA_common_longitudinal_metrics_freeze_v0_1.json`

Lifetime namespace와 fixed-window namespace는 분리 유지한다.

---

## 12. Identity QA

이름만 같다고 동일인으로 merge하지 않는다.

실제 위험 사례:

- 김선욱: 대학 총장 동명이인 ≠ **피아니스트 김선욱**
- 김승환: 교육감 동명이인 ≠ **POSTECH 물리학자 김승환**
- 김가영: 당구선수 동명이인 ≠ **농업유통 창업가 김가영**
- 전혜경: 농업계 동명이인 ≠ **국제기구 경력 전혜경**
- 하상백: 금융회사 대표 동명이인 ≠ **패션디자이너 하상백**

안전한 동일인 연결이 없으면 `untraceable`로 유지한다.

---

## 13. 현재까지 가장 안정적인 해석

1. **Selection quality** — 확보된 코호트에서 장기적으로 강한 후보군을 고르는 능력은 상당히 보인다.
2. **Future rise** — raw lifetime Major는 baseline persistence를 포함하므로 성장 예측력을 과대평가할 수 있다.
3. **Elite persistence** — lifetime peak와 정확한 T+10/T+20 occupancy는 크게 다를 수 있다.
4. **Fixed-window discrimination** — T+10 Scope≥2는 거의 포화되고, **Major≥3가 더 변별력 있다.**
5. **Re-selection** — baseline-adjusted growth보다 elite persistence/apex identification에 가까운 신호다.
6. **Comparison unit** — outlet보다 list design, year, domain, depth, baseline, follow-up window를 먼저 분리해야 한다.
7. **Dependence** — 반복 등장 placement를 독립표본으로 처리하면 안 된다.

> **언론은 ‘누가 강한 후보인가’를 고르는 능력은 꽤 보이지만, ‘비슷한 출발점에서 누가 더 크게 성장할 것인가’와 ‘정확히 10년·20년 뒤에도 누가 높은 역할에 있을 것인가’는 별개의 예측 문제다.**

---

## 14. Reproducibility

주요 deterministic/frozen references:

- `scripts/build_donga_2010_target2020_master.py`
- `scripts/build_typeA_common_master_v0_4.py`
- `state/donga_2010_target2020_freeze_v1_0.json`
- `state/donga_2011_post_t0_peak_freeze_v1_0.json`
- `state/donga_2011_t10_freeze_v1_0.json`
- `state/typeA_common_longitudinal_metrics_freeze_v0_1.json`

Generated artifact가 repo에 없으면 이를 존재한다고 가정하지 않고 별도 materialization status로 기록한다.

---

## 15. 현재 우선순위

1. **Type-A common master v0.4 generated artifact materialization**  
   기존 builder를 실제 checkout/CI에서 실행해 JSON/CSV/freeze를 생성하고 assertions를 통과시킨 뒤 commit한다.

2. **Common longitudinal row-level adapters**  
   경향 2004/2005와 동아 2010/2011 frozen snapshot을 common schema row observations로 변환한다.

3. **추가 comparable Type-A cohort 복원**  
   조선·중앙·한겨레·경향 등에서 비슷한 시기·분야·list depth의 cohort를 우선 확보한다.

4. **T+20 확대**  
   follow-up calendar가 가능한 cohort에 T+20 snapshot을 추가한다.

5. **Cross-cohort model**  
   충분한 코호트가 모이면 baseline, sector, age, list design, repeated person을 반영한 cluster-aware/hierarchical model을 설계한다.

---

## 16. 최근 진행 리포

현재 checkpoint:

`progress_2026-08-18_v32.md`

v32 완료:

- Dong-A 2010 vs 2011 harmonized T+10 comparison
- 162 unique-person first-selection sensitivity
- Type-A common longitudinal metrics v0.1 + freeze
- README status synchronization
- Type-A common v0.4 materialization gap 확인 및 문서화
