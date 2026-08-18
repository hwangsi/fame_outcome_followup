# 언론사 선정 인재 추적 — Fame Outcome Follow-up

> 과거 언론이 선정한 **“미래 인재 / 차세대 리더 / 영향력 인물”**은 10년, 20년 뒤 실제로 어떻게 되었는가?

**기준일:** 2026-08-18  
**현재 단계:** **동아 2010/2011 lifetime + T+10 완료, 2010–2011 harmonized comparison 완료, Type-A common longitudinal metrics v0.1 freeze 완료**

---

## 1. 연구 질문

이 프로젝트는 언론·전문가가 특정 시점에 선정한 유망 인물을 장기 추적해 다음 질문을 분리한다.

1. 선정 뒤 높은 수준의 역할·성과에 도달했는가?
2. 선정 시점보다 실제로 더 성장했는가?
3. 정확한 T+10/T+20 시점에도 높은 역할을 점유했는가?
4. 반복 선정은 단년도 선정에 비해 추가적인 미래 신호를 주는가?
5. 원 기사가 특정 미래 연도를 예측했을 때 실제 해당 시점 결과는 어떠했는가?
6. 매체·시대·분야·리스트 설계에 따라 신호가 어떻게 달라지는가?

최종 목표는 조선·중앙·동아·한겨레·경향 등 여러 매체의 과거 인재 선정 기획을 동일한 placement/person schema와 코딩 규칙으로 복원·비교하는 것이다.

---

## 2. 핵심 outcome architecture

Type-A는 최소 네 층을 분리한다.

### A. Baseline
선정 시점의 실제 지위·역할.

### B. Lifetime post-selection peak
선정 뒤 관찰기간 전체에서 도달한 최고 수준.

- **Major** = post-selection peak `scope ≥3`
- **Apex** = `scope =4`
- **Advanced** = `post_selection_peak > baseline_scope`
- **Sustained high** = delta=0 and peak≥3
- **No clear advancement** = delta=0 and peak<3
- **Lower than baseline** = delta<0

### C. Fixed-window snapshot
정확한 T+10/T+20 시점에 실제로 어떤 역할을 점유했는지 평가한다.

- `scope ≥2 at window`
- `Major at window = scope ≥3`
- `Apex at window = scope =4`

**Lifetime peak와 fixed-window snapshot은 서로 다른 outcome이다.**

### D. Explicit article target
기사 자체가 “2020년에 빛날 사람”처럼 특정 미래 연도를 명시한 경우 별도 prediction semantic layer로 저장한다.

같은 calendar window가 generic T+10/T+20과 정확히 겹치면 두 번 세지 않는다. 한 개 canonical snapshot에 semantic alias를 부여한다.

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

## 4. 주요 완료 Type-A lifetime cohort

| cohort | n | Lifetime Major | Lifetime Apex | Advanced |
|---|---:|---:|---:|---:|
| 뉴스메이커 2003 정치 Top10 | 10 | 100% | 20% | 70% |
| 뉴스메이커 2003 경제 Top5 | 5 | 100% | 80% | 80% |
| 한겨레21 2004 정치 Top10 | 10 | 100% | 50% | 40% |
| 경향신문 2004 「17대국회 이끌 뉴리더」 | 20 | 100% | 20% | 95% |
| 경향신문 2005 「한국을 이끌 60인」 person57 | 57 | 93.0% | 42.1% | 42.1% |
| 동아일보 2010 「2020년 한국을 빛낼 100인」 | 100 | **71%** | **12%** | **28%** |
| 동아일보 2011 「10년 뒤 한국을 빛낼 100인」 | 100 | **90%** | **12%** | **36%** |

동아 2011 lifetime layer는 100/100 adjudication 완료, 99 scored, `신준호` 1명만 not-assessable이다.

---

## 5. Type-A common longitudinal metrics v0.1

첫 cross-cohort fixed-window metrics layer가 freeze되었다.

Files:

- `data/typeA/typeA_common_longitudinal_metrics_v0_1.json`
- `state/typeA_common_longitudinal_metrics_freeze_v0_1.json`

### T+10 comparison

| cohort | assessable | Scope ≥2 | Major ≥3 | Apex =4 |
|---|---:|---:|---:|---:|
| 경향 2004 정치20 | 20 | **95.0%** | **35.0%** | 0% |
| 경향 2005 person57 | 54 | **92.6%** | **50.0%** | 5.6% |
| 동아 2010 | 87 | **97.7%** | **48.3%** | 5.7% |
| 동아 2011 | 90 | **96.7%** | **70.0%** | 4.4% |

현재 완료된 네 longitudinal unit에서:

- Scope ≥2 range = **92.6–97.7%**
- Major range = **35.0–70.0%**
- Apex range = **0–5.7%**

즉 T+10에서 “계속 확립된 인물인가”는 대부분의 코호트에서 거의 포화되어 있지만, **Major-role occupancy는 훨씬 큰 변별력**을 보인다.

### 현재 확보된 T+20

| cohort | assessable | Scope ≥2 | Major ≥3 | Apex =4 |
|---|---:|---:|---:|---:|
| 경향 2004 정치20 | 18 | 66.7% | 33.3% | 0% |
| 경향 2005 person57 | 52 | 84.6% | 51.9% | 19.2% |

코호트 설계·분야·연도·baseline이 다르므로 단순 pooled 비교는 descriptive only이다.

---

## 6. 경향 2005 mixed-unit longitudinal reference

경향신문 2005 「한국을 이끌 60인」은 Type-A mixed-unit longitudinal reference cohort다.

- original units = **60**
- persons = **57**
- organizations = **3**
- T+10 paths = **60/60**
- T+20 paths = **60/60**

Person57:

- Lifetime Major = **53/57 = 93.0%**
- Lifetime Apex = **24/57 = 42.1%**
- Advanced = **24/57 = 42.1%**
- T+10 Major = **27/54 = 50.0%**
- T+20 Major = **27/52 = 51.9%**

조직 3개는 person scope score에 강제로 합치지 않는다.

---

## 7. Competing-event 규칙

v0.1 longitudinal schema에서는 **death를 표준 competing event**로 처리한다.

- original cohort denominator에는 유지
- window `status = competing_event`
- `scope_score = null`
- primary window-specific assessable denominator에서는 제외
- 0점, 실패, exit로 강제 변환하지 않음

모든 fixed-window 결과는 original N, assessable N, competing event N, untraceable/unresolved N을 함께 보고한다.

---

## 8. Dong-A 2010: explicit target2020 = canonical T+10

동아일보 2010 cohort는 기사 제목 자체가 「2020년 한국을 빛낼 100인」이며 선정연도는 2010이다.

- explicit target year = **2020**
- explicit target window = **2019–2021**
- generic T+10 center = **2020**
- generic T+10 window = **2019–2021**

따라서 한 개 canonical snapshot에:

`aliases = ["explicit_target_2020", "t10"]`

을 부여한다.

Freeze:

- `state/donga_2010_target2020_freeze_v1_0.json`
- `state/donga_2010_target2020_t10_harmonization_freeze_v1_0.json`

Final frozen target/T+10 coverage:

- original N = **100**
- assessable/resolved = **87**
- competing event = **3**
- unresolved = **10**
- Scope ≥2 = **85/87 = 97.7%**
- Major = **42/87 = 48.3%**
- Apex = **5/87 = 5.7%**

---

## 9. Dong-A 2011 lifetime result

Full-cohort conservative:

- Major = **90/100 = 90.0%**
- Apex = **12/100 = 12.0%**
- Advanced = **36/100 = 36.0%**
- Sustained high = **53**

> **90% eventual Major attainment와 36% actual advancement는 같은 지표가 아니다.**

### Repeat 38 vs new 62 — lifetime layer

| Outcome | Repeat | New | baseline-stratified exact p |
|---|---:|---:|---:|
| Major ≥3 | 92.1% | 88.7% | 0.691 |
| Apex =4 | **23.7%** | **4.8%** | **0.0268** |
| Advanced | 28.9% | 40.3% | 0.339 |

반복선정은 lifetime layer에서 Major나 advancement보다 **후속 Apex identification**과 더 강하게 연관되었다. 이는 observational association이며 causal effect가 아니다.

---

## 10. Dong-A 2011 T+10 final

2011 selection T+10 protocol:

- target year = **2021**
- admissible window = **2020–2022**
- direct 2021 evidence 우선
- 2021 직접근거가 없을 때만 2020/2022 nearest evidence 사용
- lifetime peak 복사 금지

Final files:

- `data/typeA/donga_2011_t10_final_master_v1_0.json`
- `data/typeA/donga_2011_t10_metrics_v1_0.json`
- `state/donga_2011_t10_freeze_v1_0.json`
- `analysis/donga_2011_t10_result_v1_0.md`

Coverage:

- original N = **100**
- assessable = **90**
- competing event = **1** (`박원순`)
- untraceable = **9**
- direct/exact 2021 or explicit 2021-tenure evidence = **81/90**

Primary T+10 results:

- Scope ≥2 = **87/90 = 96.7%**
- Major = **63/90 = 70.0%**
- Apex = **4/90 = 4.4%**

Fixed-window rule이 실제 결과를 바꾼 예:

- 이주호: 2022 부총리 3 → **2021 KDI 교수 2**
- 봉준호: 2020 Academy apex 4 → **2021 감독 역할 3**
- 손흥민: 2022 Golden Boot 4 → **2021 역할 3**
- 유범재: 2020 학회장 3 → **2021 KIST 연구자·명예회장 2**
- 오세훈: 2020 총선후보 2 → **2021 서울시장 3**
- 이서현: 과거 기업 executive peak를 상속하지 않고 **2021 삼성복지재단 이사장 2**

이 때문에 lifetime Major 90%와 T+10 Major 70%는 서로 다른 연구 질문임이 실증적으로 드러난다.

---

## 11. Dong-A 2010 vs 2011 harmonized T+10 comparison

Files:

- `analysis/donga_2010_2011_t10_harmonized_comparison_v1_0.json`
- `analysis/donga_2010_2011_t10_harmonized_comparison_v1_0.md`
- `state/donga_2010_2011_t10_comparison_freeze_v1_0.json`

### Placement-level descriptive comparison

| metric | Dong-A 2010 | Dong-A 2011 | 2011 − 2010 |
|---|---:|---:|---:|
| Scope ≥2 | 97.7% | 96.7% | −1.0 pp |
| Major ≥3 | **48.3%** | **70.0%** | **+21.7 pp** |
| Apex =4 | 5.7% | 4.4% | −1.3 pp |

가장 큰 차이는 broad establishment가 아니라 **Major threshold**에서 나타난다.

그러나 100 vs 100을 독립표본처럼 검정하지 않는다.

- placements = **200**
- unique persons = **162**
- repeat = **38**
- 2010-only = **62**
- 2011-new = **62**
- 두 fixed window는 2020–2021을 공통으로 포함

따라서 +21.7 pp는 **descriptive cohort contrast**이지 “2011 선정이 21.7%p 더 정확했다”는 causal estimate가 아니다.

### 162 unique-person first-selection sensitivity

중복 38명은 첫 선정인 2010에만 귀속하고, 2011에서는 신규 62명만 추가한다.

- unique-person N = **162**
- assessable = **144**
- competing event = **3**
- unresolved/untraceable = **15**
- Scope ≥2 = **140/144 = 97.2%**
- Major = **80/144 = 55.6%**
- Apex = **6/144 = 4.2%**

이것은 **first-selection 기준 person-specific T+10**이며, 모든 사람이 같은 calendar year에 관찰된 단면 분석은 아니다.

---

## 12. Dong-A 2010–2011 two-wave identity layer

두 연도를 200명의 독립 표본으로 세지 않는다.

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

## 13. Type-A common layers

### Lifetime placement master

Stable full placement master:

- `data/typeA/typeA_common_master_v0_3.json`
- `data/typeA/typeA_common_master_v0_3.csv`

Lifetime metrics:

- `data/typeA/typeA_common_metrics_v0_4.json`
- `state/typeA_common_metrics_freeze_v0_4.json`

`typeA_common_master_v0_4.json/.csv` materialization은 아직 pending이다.

### Longitudinal metrics

- `data/typeA/typeA_common_longitudinal_metrics_v0_1.json`
- `state/typeA_common_longitudinal_metrics_freeze_v0_1.json`

Lifetime namespace와 fixed-window namespace는 분리 유지한다.

---

## 14. Identity QA

이름만 같다고 동일인으로 merge하지 않는다.

실제 audit에서 확인된 위험 사례:

- 김선욱: 대학 총장 동명이인 ≠ **피아니스트 김선욱**
- 김승환: 교육감 동명이인 ≠ **POSTECH 물리학자 김승환**
- 김가영: 당구선수 동명이인 ≠ **농업유통 창업가 김가영**
- 전혜경: 농업계 동명이인 ≠ **국제기구 경력 전혜경**
- 하상백: 금융회사 대표 동명이인 자료를 **패션디자이너 하상백**에게 연결하지 않음

Identity를 안전하게 연결하지 못하면 `untraceable`로 남긴다.

---

## 15. 현재까지 가장 안정적인 해석

1. **Selection quality** — 확보된 코호트에서 언론/전문가가 장기적으로 높은 위치에 도달할 후보군을 고르는 능력은 상당히 보인다.
2. **Future rise** — raw lifetime Major는 이미 높았던 사람의 persistence를 포함하므로 성장 예측력을 과대평가할 수 있다.
3. **Elite persistence** — lifetime peak와 정확한 T+10/T+20 role occupancy는 크게 다르다.
4. **Fixed-window discrimination** — T+10 Scope≥2는 여러 코호트에서 거의 포화되어 있으며, **Major≥3가 더 변별력 있는 outcome**이다.
5. **Re-selection** — baseline-adjusted growth보다 elite persistence/apex identification에 가까운 신호다.
6. **Comparison unit** — outlet 자체보다 list design, year, domain, depth, baseline과 follow-up window를 먼저 분리해야 한다.
7. **Dependence** — 반복 등장 인물을 포함하는 placement 자료를 독립표본으로 취급하면 안 된다.

> **현재 자료에서 언론은 ‘누가 강한 후보인가’를 고르는 능력은 꽤 보이지만, ‘비슷한 출발점에서 누가 더 크게 성장할 것인가’와 ‘정확히 10년·20년 뒤에도 누가 높은 역할에 있을 것인가’는 별개의 예측 문제다.**

---

## 16. Reproducibility

주요 source freeze와 deterministic builder를 유지한다.

예:

- `scripts/build_donga_2010_target2020_master.py`
- `state/donga_2010_target2020_freeze_v1_0.json`
- `state/donga_2011_post_t0_peak_freeze_v1_0.json`
- `state/donga_2011_t10_freeze_v1_0.json`
- `state/typeA_common_longitudinal_metrics_freeze_v0_1.json`

Generated runtime artifact가 Git에 직접 저장되지 않더라도 builder + frozen source layer + QA invariant로 재현 가능하게 유지한다.

---

## 17. 현재 우선순위

1. **Common longitudinal row-level adapters materialization**  
   경향 2004/2005와 동아 2010/2011 frozen snapshot을 common schema의 row-level observation으로 변환한다.

2. **Type-A common master v0.4 materialization**  
   lifetime metrics v0.4와 일치하는 full placement JSON/CSV를 생성한다.

3. **추가 comparable Type-A cohort 복원**  
   조선·중앙·한겨레·경향 등에서 비슷한 시기·분야·list depth의 cohort를 우선 확보한다.

4. **T+20 확대**  
   follow-up calendar가 가능한 기존 cohort에 T+20 snapshot을 추가한다.

5. **Cross-cohort model**  
   충분한 코호트가 모이면 baseline, sector, age, list design과 repeated person을 반영한 hierarchical/cluster-aware model을 설계한다.

---

## 18. 최근 진행 리포

현재 checkpoint:

`progress_2026-08-18_v32.md`

v32 완료:

- Dong-A 2010 vs 2011 harmonized T+10 comparison
- 162 unique-person first-selection sensitivity
- Type-A common longitudinal metrics v0.1
- common longitudinal metrics freeze
- README status synchronization
