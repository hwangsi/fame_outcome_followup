# 언론사 선정 인재 추적 — Fame Outcome Follow-up

> 과거 언론이 선정한 **“미래 인재 / 차세대 리더 / 영향력 인물”**은 10년, 20년 뒤 실제로 어떻게 되었는가?

**기준일:** 2026-08-18  
**현재 authoritative checkpoint:** `progress_2026-08-18_v34.md`

현재 저장소는 다음 두 공통 분석 레이어를 분리해 운용한다.

- **Lifetime peak layer:** 선정 이후 관찰기간 전체에서 도달한 최고 역할/성과
- **Fixed-window longitudinal layer:** T+10/T+20/current 시점에 실제로 점유한 역할

두 outcome은 같은 scope rubric을 사용하지만 서로 다른 질문에 답한다.

---

## 1. 연구 질문

언론·전문가가 특정 시점에 선정한 유망 인물을 장기 추적해 다음을 평가한다.

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

- **Major** = peak `scope >=3`
- **Apex** = `scope =4`
- **Advanced** = `post_selection_peak > baseline_scope`
- **Sustained high** = delta=0 and peak>=3

### C. Fixed-window snapshot
T+10/T+20/current 시점에 실제로 점유한 역할.

- `scope >=2 at window`
- `Major at window = scope >=3`
- `Apex at window = scope =4`

### D. Explicit article target
기사 자체가 특정 미래 연도를 명시하면 별도 prediction semantic layer로 저장한다. Generic T+10/T+20과 calendar window가 완전히 같으면 하나의 canonical snapshot에 alias만 여러 개 부여하고 중복 계수하지 않는다.

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

## 4. Type-A lifetime common layer — authoritative v0.4

### Files

- `data/typeA/typeA_common_master_v0_4.json`
- `data/typeA/typeA_common_master_v0_4.csv`
- `data/typeA/typeA_common_metrics_v0_4.json`
- `state/typeA_common_master_freeze_v0_4.json`

### QA

- placements = **255**
- canonical persons = **193**
- unique display names = **192**
- cohort units = **7**
- repeated persons = **51**
- placement count distribution = 1회 142명 / 2회 42명 / 3회 7명 / 4회 2명
- 4회 선정 = **원희룡, 유시민**
- not-assessable placements = 1

중요한 identity correction:

- 경향 2005 정치10을 추가할 때 김근태·손학규를 새 인물로 계산했던 기존 audit은 오류였다.
- 두 사람 모두 이미 뉴스메이커 2003 정치 Top10에 존재한다.
- 따라서 v0.4는 **255 placements / 193 persons**가 맞으며, 과거 195-person 기대치는 superseded다.

관련 파일:

- `research/khan_2005_politics10_identity_audit_v0_2.json`
- `state/typeA_common_v0_4_materialization_debug.md`

---

## 5. 주요 lifetime 결과

| cohort | n | Lifetime Major | Lifetime Apex | Advanced |
|---|---:|---:|---:|---:|
| 뉴스메이커 2003 정치 Top10 | 10 | 100% | 20% | 70% |
| 뉴스메이커 2003 경제 Top5 | 5 | 100% | 80% | 80% |
| 한겨레21 2004 정치 Top10 | 10 | 100% | 50% | 40% |
| 경향 2004 「17대국회 이끌 뉴리더」 | 20 | 100% | 20% | 95% |
| 경향 2005 「한국을 이끌 60인」 person57 | 57 | 93.0% | 42.1% | 42.1% |
| 동아 2010 「2020년 한국을 빛낼 100인」 | 100 | 71% | 12% | 28% |
| 동아 2011 「10년 뒤 한국을 빛낼 100인」 | 100 | 90% | 12% | 36% |

경향 2005 전체 원선정은 60 units이며 57 persons + 3 organizations다. person57은 mixed-unit selection에 대한 prespecified secondary person-only analysis다.

---

## 6. Type-A common longitudinal layer — authoritative v0.3 / metrics v0.2

### Row master

- `data/typeA/typeA_common_longitudinal_rows_v0_3.json`
- `state/typeA_common_longitudinal_rows_freeze_v0_3.json`

QA:

- canonical snapshot rows = **374**
- unique snapshot IDs = **374**
- row-ready selected-person placements = **277**
- cohort units = **4**
- cohort-window cells = **7**

Composition:

1. 경향 2004 정치20: 20 placements / T+10·T+20·current = 60 rows
2. 경향 2005 person57: 57 placements / T+10·T+20 = 114 rows
3. 동아 2010: 100 placements / T+10 = 100 rows
4. 동아 2011: 100 placements / T+10 = 100 rows

완료된 네 longitudinal cohort unit은 모두 row-ready이며 metric-only로 남은 completed cohort는 없다.

### Row-derived metrics

- `data/typeA/typeA_common_longitudinal_metrics_v0_2.json`
- `state/typeA_common_longitudinal_metrics_freeze_v0_2.json`

Aggregate를 field table에서 수기로 복사하지 않고 374-row master에서 재계산한다.

---

## 7. T+10 비교

| cohort | assessable | Scope >=2 | Major >=3 | Apex =4 |
|---|---:|---:|---:|---:|
| 경향 2004 정치20 | 20 | 19/20 = 95.0% | 7/20 = 35.0% | 0% |
| 경향 2005 person57 | 54 | 50/54 = 92.6% | 27/54 = 50.0% | 3/54 = 5.6% |
| 동아 2010 | 87 | 85/87 = 97.7% | 42/87 = 48.3% | 5/87 = 5.7% |
| 동아 2011 | 90 | 87/90 = 96.7% | 63/90 = 70.0% | 4/90 = 4.4% |

현재 완료된 네 longitudinal unit에서 broad establishment(`scope>=2`)는 92.6–97.7%로 높지만 Major occupancy는 35.0–70.0%로 더 넓게 갈린다. 따라서 **Major fixed-window occupancy가 더 변별력 있는 outcome**이다.

---

## 8. T+20 비교 — corrected

| cohort | assessable | Scope >=2 | Major >=3 | Apex =4 |
|---|---:|---:|---:|---:|
| 경향 2004 정치20 | 18 | 12/18 = 66.7% | 6/18 = 33.3% | 0% |
| 경향 2005 person57 | 52 | **43/52 = 82.7%** | **26/52 = 50.0%** | **10/52 = 19.2%** |

### 경향 2005 stale aggregate correction

과학기술 field audit에서 신희섭 T+20은 IBS 공식 은퇴 기록에 따라 scope3에서 scope1로 이미 교정되었으나, 상위 aggregate가 과거 값을 유지하고 있었다.

Corrected T+20 distribution:

- `0:0 / 1:9 / 2:17 / 3:16 / 4:10 / null:5`
- Scope >=2: **44 -> 43**
- Major >=3: **27 -> 26**

Authoritative files:

- `data/typeA/khan_2005_korea_leaders60_person57_common_longitudinal_rows_v0_1.json`
- `data/typeA/khan_2005_korea_leaders60_person57_longitudinal_metrics_v1_1.json`
- `state/khan_2005_korea_leaders60_person57_longitudinal_freeze_v1_1.json`

v1.0 aggregate는 historical artifact로 보존하지만 v1.1이 supersede한다.

---

## 9. Dong-A 2010: explicit target2020 = T+10

선정연도 2010, explicit target year 2020.

- target window = **2019–2021**
- generic T+10 window = **2019–2021**
- aliases = `["explicit_target_2020", "t10"]`

QA:

- original N = 100
- assessable = 87
- competing event = 3
- unresolved/untraceable = 10
- Scope >=2 = 85/87 = 97.7%
- Major = 42/87 = 48.3%
- Apex = 5/87 = 5.7%

Deterministic master는 과거 workflow가 build만 하고 persist하지 않아 repo에서 빠져 있었으나 현재 복구 완료했다.

- `data/typeA/donga_2010_target2020_master_v1_0.json`
- `data/typeA/donga_2010_target2020_master_v1_0.csv`
- `data/typeA/donga_2010_common_longitudinal_rows_v0_1.json`

---

## 10. Dong-A 2011 lifetime + T+10

Lifetime:

- Major = 90/100 = 90.0%
- Apex = 12/100 = 12.0%
- Advanced = 36/100 = 36.0%

T+10:

- target = 2021
- admissible window = 2020–2022
- original N = 100
- assessable = 90
- competing event = 1
- untraceable = 9
- Scope >=2 = 87/90 = 96.7%
- Major = 63/90 = 70.0%
- Apex = 4/90 = 4.4%

Files:

- `data/typeA/donga_2011_t10_final_master_v1_0.json`
- `data/typeA/donga_2011_t10_metrics_v1_0.json`
- `data/typeA/donga_2011_common_longitudinal_rows_v0_1.json`
- `state/donga_2011_t10_freeze_v1_0.json`

---

## 11. Dong-A 2010 vs 2011 harmonized T+10

| metric | 2010 | 2011 | 2011 - 2010 |
|---|---:|---:|---:|
| Scope >=2 | 97.7% | 96.7% | -1.0 pp |
| Major >=3 | 48.3% | 70.0% | +21.7 pp |
| Apex =4 | 5.7% | 4.4% | -1.3 pp |

두 wave를 독립표본처럼 취급하지 않는다.

- placements = 200
- unique persons = 162
- repeat = 38
- 2010-only = 62
- 2011-new = 62

따라서 +21.7 pp Major 차이는 descriptive cohort contrast이지 causal estimate가 아니다.

Files:

- `analysis/donga_2010_2011_t10_harmonized_comparison_v1_0.json`
- `analysis/donga_2010_2011_t10_harmonized_comparison_v1_0.md`
- `state/donga_2010_2011_t10_comparison_freeze_v1_0.json`

---

## 12. Competing event / unresolved policy

Death는 표준 competing event로 처리한다.

- original denominator에는 유지
- snapshot `status = competing_event`
- `scope_score = null`
- primary assessable denominator에서는 제외
- 0점/실패로 강제 변환하지 않음

직접 추적이 불가능한 경우도 `untraceable/unresolved`로 유지하며 임의의 failure score를 부여하지 않는다.

---

## 13. Identity QA

이름만 같다고 동일인으로 merge하지 않는다.

핵심 원칙:

- placement novelty != person novelty
- same-name collision은 identity anchor로 adjudicate
- true homonym은 `identity_key`를 분리
- cohort가 달라도 같은 사람은 같은 canonical person으로 연결

대표 사례:

- 이미경: CJ E&M/Miky Lee vs 정치인 이미경 분리
- 김근태·손학규: 경향 2005 정치10에서 새 placement이지만 기존 canonical person

Registry:

- `data/typeA/canonical_identity_overrides_v0_1.json`
- `state/identity_resolution_policy_v0_2.md`

---

## 14. 현재 authoritative files

### Lifetime common

- `data/typeA/typeA_common_master_v0_4.json`
- `data/typeA/typeA_common_master_v0_4.csv`
- `data/typeA/typeA_common_metrics_v0_4.json`
- `state/typeA_common_master_freeze_v0_4.json`

### Longitudinal common

- `data/typeA/typeA_common_longitudinal_rows_v0_3.json`
- `state/typeA_common_longitudinal_rows_freeze_v0_3.json`
- `data/typeA/typeA_common_longitudinal_metrics_v0_2.json`
- `state/typeA_common_longitudinal_metrics_freeze_v0_2.json`

### Checkpoint

- `progress_2026-08-18_v34.md`

---

## 15. 다음 우선순위

1. **조선일보·중앙일보 comparable cohort recovery**
   - 2003–2006 우선
   - roster denominator와 selection mechanism이 직접 복원되는 리스트만 Type-A 후보로 승격
   - 단일 인물 기사나 후대 회고 명단을 원래 cohort roster로 대체하지 않음
2. common longitudinal 374 rows에서 cohort-window comparison table을 row-derived 방식으로 확장
3. 반복인물 overlap에 대한 clustered sensitivity 설계
4. 그 다음에만 hierarchical/cluster-aware modeling 검토

현재 조선 2006 차세대 전문경영인 후보는 일부 membership evidence만 있어 **아직 cohort로 승격하지 않는다.** 후대 2007년 기사 명단을 2006 roster로 대체해서는 안 된다.
