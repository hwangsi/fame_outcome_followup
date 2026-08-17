# 언론사 선정 인재 추적 — Fame Outcome Follow-up

> 과거 언론이 선정한 **“미래 인재 / 차세대 리더 / 영향력 인물”**은 10년, 20년 뒤 실제로 어떻게 되었는가?

**기준일:** 2026-08-18  
**현재 완료 코호트:** 동아일보 2010·2011 「한국을 빛낼 100인」  
**현재 단계:** **동아 2011 post-selection outcome 100/100 adjudication 완료 → repeat-selection의 추가 예측력 분석 단계**

---

## 1. 프로젝트 목적

이 프로젝트는 언론·전문가가 특정 시점에 선정한 유망 인물들을 장기 추적해, 단순한 유명인 회고가 아니라 다음 질문을 정량적으로 평가하려는 연구 프로젝트다.

1. 선정된 사람들은 이후 실제로 높은 수준의 리더십·성과에 도달했는가?
2. 이미 선정 당시 높은 위치에 있던 사람과 **선정 뒤 실제로 더 성장한 사람**을 구분할 수 있는가?
3. 같은 언론사가 반복해서 선정한 사람은 단년도 선정자보다 이후 성과가 더 좋은가?
4. 순위형 리스트라면 높은 순위가 더 큰 후속 상승을 예측했는가?
5. 언론사·시대·분야별로 예측 성능에 차이가 있는가?

최종적으로는 조선·중앙·동아·한겨레·경향 등 여러 매체의 과거 인재 선정 기획을 동일한 코딩 규칙으로 복원하고 비교하는 것을 목표로 한다.

---

## 2. 핵심 방법론

### 2.1 Type A — 미래예측형 리스트

예: “10년 뒤 한국을 빛낼 100인”, “차세대 지도자”, “미래 리더”.

Type A에서는 다음 지표를 반드시 분리한다.

- **Major-leadership precision** — 선정 이후 최고 역할/성과가 `scope ≥ 3`인가?
- **Apex precision** — 국가·세계 최고 수준인 `scope = 4`에 도달했는가?
- **Baseline-adjusted advancement** — 선정 이전 lifetime peak보다 실제로 더 높은 층위에 도달했는가?
- **Sustained high** — 이미 높은 사람이 이후에도 높은 수준을 유지했는가?
- **Ranking accuracy** — 순위형 리스트에서 높은 순위가 더 큰 후속 상승을 예측했는가?

### 2.2 Type B — 이미 성취한 역할모델형 리스트

예: “닮고 싶고 되고 싶은 과학기술인”.

이 경우 prediction accuracy보다 **persistence / trajectory**를 본다.

### 2.3 Scope score

| score | 의미 |
|---:|---|
| 0 | 직접 자료 부족 또는 meaningful role/achievement 미확인 |
| 1 | 제한적·지역적·간헐적 활동 |
| 2 | 전국 단위에서 확립된 전문직·창작자·선수·기관 리더 |
| 3 | 국내 최상위권 또는 뚜렷한 국제적 리더십/성과 |
| 4 | 국가·세계적 apex 또는 field-defining achievement |

분야별 세부 기준은 `state/coding_rules_typeA_sector_scope_v0_1.md`를 따른다.

### 2.4 Advancement

핵심 비교는 동시점 직함이 아니라 **선정 전 lifetime peak**다.

```text
advancement_delta = post_selection_peak - pre_selection_lifetime_peak
```

- `advanced`: delta > 0
- `sustained_high`: delta = 0 and peak ≥3
- `no_clear_advancement`: delta = 0 and peak <3
- `lower_than_baseline`: delta <0
- `not_assessable`: 동일인 후속자료 부족 등으로 판정 불가

---

## 3. 현재까지의 연구 현황

| 코호트 | 유형 | 상태 | 핵심 결과 |
|---|---|---:|---|
| 동아일보 과학기술 역할모델 2002–2005 | Type B | 39/39 | longitudinal pilot 완료 |
| 뉴스메이커 2003 정치 Top10 | Type A | 10/10 | major 100%, apex 20%, advanced 70% |
| 뉴스메이커 2003 경제 Top5 | Type A | 5/5 | major 100%, apex 80%, advanced 80% |
| 한겨레21 2004 정치 Top10 | Type A | 10/10 | major 100%, apex 50%, advanced 40% |
| 동아일보 2010 「2020년 한국을 빛낼 100인」 | Type A | **100/100** | major 71%, apex 12%, advanced 28% |
| 동아일보 2011 「10년 뒤 한국을 빛낼 100인」 | Type A | **100/100 adjudicated** | **major 90%, apex 12%, advanced 36%** |

---

## 4. Type B pilot — 동아일보 과학기술 역할모델

**코호트:** 동아일보 「닮고 싶고 되고 싶은 과학기술인」 2002–2005, n=39

`T0 → T+10(±1년) → T+20(±1년) → Current`

- Current verified: **29/39 = 74%**
- T+10 strict: **37/39 = 95%**
- T+20 strict: **34/39 = 87%**
- High-status lifetime trajectory: **26/39 = 67%**
- T+10 elite 생존자 중 T+20 elite 유지: **14/19 = 74%**

---

## 5. 초기 Type A ranked cohorts

### 뉴스메이커 2003 정치 Top10

- major: **10/10 = 100%**
- apex: **2/10 = 20%**
- advanced: **7/10 = 70%**
- rank vs advancement Δ: **ρ=-0.094, p=0.796**

### 뉴스메이커 2003 경제 Top5

- major: **5/5 = 100%**
- apex: **4/5 = 80%**
- advanced: **4/5 = 80%**
- rank vs advancement Δ: **ρ=-0.224, p=0.718**

### 한겨레21 2004 정치 Top10

- major: **10/10 = 100%**
- apex: **5/10 = 50%**
- advanced: **4/10 = 40%**
- rank vs advancement Δ: **ρ=+0.402, p=0.249**

뉴스메이커 정치 Top10과 한겨레21 Top10의 20 placements는 16 unique persons이며 강금실·권영길·정동영·추미애가 중복된다. 따라서 naïve independent-sample test를 사용하지 않는다.

---

## 6. 동아일보 2010 「2020년 한국을 빛낼 100인」 — 완료

### 데이터 상태

- canonical roster: **100/100**
- T0 snapshot: **100/100**
- pre-selection lifetime peak: **100/100**
- lifetime post-T0 peak through 2026-08-18: **100/100**
- final unresolved: **0**

### 최종 결과

- post-T0 scope ≥3: **71/100 = 71%**
- post-T0 scope =4: **12/100 = 12%**
- baseline-adjusted advanced: **28/100 = 28%**
- sustained high: **44/100 = 44%**
- no clear advancement: **28/100 = 28%**
- lower than baseline: **0/100**

핵심은 **71% major attainment와 28% actual advancement를 같은 것으로 읽지 않는 것**이다.

> 이 리스트는 이미 강한 사람을 골라내는 screening 능력과 일부 인물의 실제 후속 상승을 함께 포착했다.

---

## 7. 동아일보 2011 「10년 뒤 한국을 빛낼 100인」 — 완료

### 7.1 Observation window

- selection cutoff: **2011-04-01**
- observation end: **2026-08-18**

2010 자료를 단순 승계하지 않고 2011 cutoff를 다시 적용해 look-ahead를 방지했다.

### 7.2 데이터 완결성

- roster: **100/100**
- T0 scope: **100/100**
- pre-selection lifetime peak: **100/100**
- post-selection adjudication: **100/100**
- scored: **99/100**
- not assessable: **1/100 — 신준호**
- pending: **0**
- repeat 2010↔2011: **38명**
- new 2011 entrants: **62명**
- death-truncated: **김정주, 박원순 2명**

신준호는 선정 당시 동일인은 확실하지만 선정 후 동일인의 경력을 재현 가능하게 직접 연결할 자료가 부족해 임의의 낮은 점수를 주지 않고 `not_assessable`로 처리했다.

### 7.3 Primary — full cohort conservative

not-assessable 1명을 보수적으로 non-hit로 포함한 전체 100명 기준:

- **major scope ≥3: 90/100 = 90.0%**
- **apex scope =4: 12/100 = 12.0%**
- **baseline-adjusted advanced: 36/100 = 36.0%**

Advancement class:

- advanced: **36**
- sustained high: **53**
- no clear advancement: **7**
- lower than baseline: **3**
- not assessable: **1**

Scored 99명의 post-T0 peak:

- score 2: **9**
- score 3: **78**
- score 4: **12**

### 7.4 Assessable-only sensitivity

신준호를 제외한 99명 기준:

- major: **90/99 = 90.9%**
- apex: **12/99 = 12.1%**
- advanced: **36/99 = 36.4%**

### 7.5 핵심 해석

> **2011 리스트는 post-selection major attainment가 90%로 매우 높았지만, 선정 이전 lifetime peak를 넘어 실제로 더 상승한 사람은 36%였다.**

즉 90%를 “예측 성공률”로 그대로 읽으면 과장된다. 특히 `sustained_high = 53명`이 `advanced = 36명`보다 많다는 점은, 이 리스트가 **신인 발굴뿐 아니라 이미 강한 인물의 지속성을 강하게 포착**했음을 보여준다.

---

## 8. 동아 2010 vs 2011 — descriptive comparison

| 지표 | 2010 | 2011 |
|---|---:|---:|
| Major | 71% | **90%** |
| Apex | **12%** | **12%** |
| Advanced | 28% | **36%** |
| Sustained high | 44% | **53%** |
| No clear advancement | 28% | **7%** |
| Lower than baseline | 0% | **3%** |
| Not assessable | 0% | **1%** |

2011의 raw major와 advancement가 더 높지만, 이를 편집진의 우월한 예측력으로 곧바로 해석하지 않는다.

- 두 코호트의 baseline·분야 구성이 다르다.
- **38명이 반복 선정**되어 독립 표본이 아니다.
- 따라서 현재 비교는 design-aware descriptive comparison이다.

---

## 9. 반복선정 분석

### 9.1 2010을 뒤에서 나눈 분석

2011 재선정 여부는 2010 시점에는 미래 정보다. 따라서 2010 outcome을 나중의 repeat/non-repeat로 나눈 기존 분석은 association이다.

- raw major: repeat **92.1%** vs single **58.1%**
- raw apex: repeat **23.7%** vs single **4.8%**
- advanced: repeat **28.9%** vs single **27.4%**
- baseline-stratified CMH OR ≈ **2.43**, p ≈ **0.107**

### 9.2 다음 질문 — prospective repeat signal

반면 2011 시점에는 “2010에도 선정되었는가”가 이미 알려진 baseline 정보다.

따라서 이제 검증할 질문은:

> **2011년에 반복 선정되었다는 정보가 당시 baseline prestige를 넘어 이후 성과에 추가적인 예측정보를 제공했는가?**

다음 분석은 repeat 38명 vs new entrant 62명에 대해:

1. raw major / apex / advancement
2. baseline distribution
3. baseline-stratified comparison
4. CMH 또는 baseline-adjusted logistic model

을 함께 본다.

---

## 10. Identity QA

이 프로젝트에서 이름만으로 경력을 연결하면 치명적인 오류가 생길 수 있다.

실제로 audit 중 발견한 동명이인 위험:

- 김선욱: 대학 총장 동명이인 ≠ **피아니스트 김선욱**
- 김승환: 교육감 동명이인 ≠ **POSTECH 물리학자 김승환**
- 김가영: 당구선수 동명이인 ≠ **농업유통 창업가 김가영**
- 전혜경: 농업계 동명이인 ≠ **UNICEF Senior Advisor 전혜경**

batch 3 이후 신규 42명은 모두 frozen 2011 roster의:

- 이름
- category
- `t0_role_official_2011`

을 자동 대조하는 identity anchor를 사용한다. 불일치하면 CI가 실패한다.

---

## 11. Coding guardrails

- advancement는 contemporaneous title이 아니라 **pre-selection lifetime peak** 대비 계산한다.
- 형사사건·직 상실·경영 실패 등 adverse outcome은 이미 관찰된 peak를 소급해 낮추지 않는다.
- 사망은 failure가 아니라 exposure truncation이다.
- 내정·후보·언론상 후보군만으로 achieved peak를 올리지 않는다.
- 자료 부족은 억지 score 0/1이 아니라 필요하면 `not_assessable`로 남긴다.
- broad screening과 ranked Top-N을 같은 precision으로 직접 비교하지 않는다.
- 중복 인물은 독립 표본으로 취급하지 않는다.

---

## 12. 현재 핵심 파일

```text
state/
  coding_rules_typeA_v0_1.md
  coding_rules_typeA_sector_scope_v0_1.md
  donga_2010_post_t0_peak_freeze_v1_2.json
  donga_2010_typeA_result_v1_0.md
  donga_2011_baseline_freeze_v1_0.json
  donga_2011_post_t0_peak_freeze_v1_0.json
  donga_2011_typeA_result_v1_0.md

data/typeA/
  donga_2010_canonical_roster_v2_1.json
  donga_2010_post_t0_peak_metrics_v1_2.json
  donga_2011_t0_roles_v0_1.json

research/
  donga_2011_post_t0_repeat_cutoff_audit_v0_1.json
  donga_2011_post_t0_new_audit_batch1_v0_1.json
  donga_2011_post_t0_new_audit_batch2_v0_1.json
  donga_2011_post_t0_new_audit_batch3_v0_1.json
  donga_2011_post_t0_new_audit_batch4_v0_1.json
  donga_2011_post_t0_new_audit_batch5_v0_1.json
  donga_2011_post_t0_new_audit_batch6_v0_1.json

scripts/
  build_donga_2010_post_t0_peak_master.py
  build_donga_2011_post_t0_seed.py
  build_donga_2011_post_t0_partial_master.py
  build_donga_2011_post_t0_master.py

analysis/  # runtime-generated
  donga_2011_post_t0_master_v1_0.json
  donga_2011_post_t0_metrics_v1_0.json
```

---

## 13. QA / reproducibility

동아 2011 final workflow:

```text
.github/workflows/donga-2011-postt0-seed-qa.yml
```

최종 동결 run:

- run ID: **32074307890**
- head commit: `82d6dd13122952c2287537f7d12298297e599900`
- conclusion: **success**

이 workflow는 2010/2011 baseline부터 final 2011 master까지 재생성하고 다음을 검증한다.

- repeat 38/38 post-cutoff resolution
- 62명 신규 entrant 6개 batch의 중복·roster 일치
- identity anchor 42명 검증
- final **100 adjudicated / 99 scored / 1 not-assessable / 0 pending**
- primary denominator 100 / sensitivity denominator 99

---

## 14. 다음 우선순위

1. **2011 repeat 38 vs new 62 prospective predictive-value 분석**
2. baseline-stratified / adjusted repeat effect 산출
3. 동아 2010–2011 two-wave longitudinal comparison 문서화
4. Type-A common master에 2011 cohort 통합
5. 한겨레21 2004 full 31 및 1999 archive recovery 보완
6. 조선·중앙·한겨레·경향 계열의 추가 Type-A 코호트 확장
7. 충분한 코호트가 쌓이면 person-clustered / mixed-effects model 및 matched control 도입

현재 가장 중요한 다음 질문은 **“반복 선정 자체가 baseline을 넘어 추가적인 미래 정보인가?”**이다.
