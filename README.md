# 언론사 선정 인재 추적 — Fame Outcome Follow-up

> 과거 언론이 선정한 **“미래 인재 / 차세대 리더 / 영향력 인물”**은 10년, 20년 뒤 실제로 어떻게 되었는가?

**기준일:** 2026-08-18  
**현재 주력 코호트:** 동아일보 2011 「10년 뒤 한국을 빛낼 100인」  
**현재 단계:** **2011 post-selection outcome audit 58/100 완료, 42/100 진행 예정**

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

- **Major-leadership precision**  
  선정 이후 관찰된 최고 역할/성과가 `scope ≥ 3`인가?

- **Apex precision**  
  국가·세계 최고 수준인 `scope = 4`에 도달했는가?

- **Baseline-adjusted advancement**  
  선정 이전 lifetime peak보다 실제로 더 높은 층위에 도달했는가?

- **Sustained high**  
  이미 높은 사람이 이후에도 높은 수준을 유지했는가?

- **Ranking accuracy**  
  순위가 있는 리스트에서 상위 순위가 더 큰 후속 상승을 예측했는가?

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

---

## 3. 현재까지의 연구 현황

| 코호트 | 유형 | 상태 | 핵심 결과 |
|---|---|---:|---|
| 동아일보 과학기술 역할모델 2002–2005 | Type B | 39/39 | longitudinal pilot 완료 |
| 뉴스메이커 2003 정치 Top10 | Type A | 10/10 | major 100%, apex 20%, advanced 70% |
| 뉴스메이커 2003 경제 Top5 | Type A | 5/5 | major 100%, apex 80%, advanced 80% |
| 한겨레21 2004 정치 Top10 | Type A | 10/10 | major 100%, apex 50%, advanced 40% |
| 동아일보 2010 「2020년 한국을 빛낼 100인」 | Type A | **100/100** | major 71%, apex 12%, advanced 28% |
| 동아일보 2011 「10년 뒤 한국을 빛낼 100인」 | Type A | **58/100 post-T0** | 진행 중 — 전체 rate는 아직 보고하지 않음 |

---

## 4. Type B pilot — 동아일보 과학기술 역할모델

**코호트:** 동아일보 「닮고 싶고 되고 싶은 과학기술인」 2002–2005, n=39

추적축:

`T0 → T+10(±1년) → T+20(±1년) → Current`

결과:

- Current verified: **29/39 = 74%**
- T+10 strict: **37/39 = 95%**
- T+20 strict: **34/39 = 87%**
- High-status lifetime trajectory: **26/39 = 67%**
- T+10 elite 생존자 중 T+20 elite 유지: **14/19 = 74%**

---

## 5. 초기 Type A ranked cohorts

### 뉴스메이커 2003 정치 Top10

- major leadership: **10/10 (100%)**
- apex: **2/10 (20%)**
- baseline-adjusted advanced: **7/10 (70%)**
- rank vs advancement Δ: **ρ=-0.094, p=0.796**

### 뉴스메이커 2003 경제 Top5

- major leadership: **5/5 (100%)**
- apex: **4/5 (80%)**
- baseline-adjusted advanced: **4/5 (80%)**
- rank vs advancement Δ: **ρ=-0.224, p=0.718**

### 한겨레21 2004 정치 Top10

- major leadership: **10/10 (100%)**
- apex: **5/10 (50%)**
- baseline-adjusted advanced: **4/10 (40%)**
- rank vs advancement Δ: **ρ=+0.402, p=0.249**

뉴스메이커 정치 Top10과 한겨레21 Top10의 20 placements는 16 unique persons이며 강금실·권영길·정동영·추미애가 중복된다. 따라서 naïve independent-sample test는 사용하지 않는다.

---

## 6. 동아일보 2010 「2020년 한국을 빛낼 100인」 — 완료

### 데이터 상태

- canonical roster: **100/100**
- T0 snapshot: **100/100**
- pre-selection lifetime peak: **100/100**
- lifetime post-T0 peak through 2026-08-18: **100/100**
- final unresolved: **0**

### 최종 Type A 결과

- post-T0 scope ≥3: **71/100 = 71%**
- post-T0 scope =4: **12/100 = 12%**
- baseline-adjusted advanced: **28/100 = 28%**
- sustained high: **44/100 = 44%**
- no clear advancement: **28/100 = 28%**
- lower than baseline: **0/100**

사망으로 관찰기간이 단축된 3명을 제외한 sensitivity:

- major scope ≥3: **68/97 = 70.1%**
- apex: **12/97 = 12.4%**
- advanced: **26/97 = 26.8%**

### 핵심 해석

> **선정 이후 major 수준에 도달한 사람은 71%였지만, 선정 이전 lifetime peak까지 보정하면 실제로 더 높은 층위로 상승한 사람은 28%였다.**

따라서 raw future attainment를 그대로 “예측 성공률”로 읽으면 안 된다. 이 리스트의 성과는 **이미 강한 사람을 골라내는 screening 능력 + 일부 인물의 실제 후속 상승**으로 분해해서 해석하는 것이 적절하다.

분야별 `major / advancement`:

- 자유로운 창조인: **80% / 40%**
- 꿈꾸는 개척가: **88% / 12%**
- 행동하는 지성인: **35% / 35%**
- 도전하는 경제인: **68% / 24%**
- 미래를 여는 지도자: **100% / 44.4%**
- 독자선정: **0% / 0%**

---

## 7. 동아일보 2010↔2011 반복선정 분석

2010과 2011 리스트에 **38명**이 반복 선정됐다.

2010 선정 이후 전체 peak를 나중에 관찰된 repeat/non-repeat로 나누면:

- raw major: **repeat 92.1% vs single 58.1%**
- raw apex: **repeat 23.7% vs single 4.8%**
- baseline-exceeding advancement: **repeat 28.9% vs single 27.4%**
- baseline-stratified CMH OR: **≈2.43, p≈0.107**

중요한 해석:

- 반복선정자는 raw future attainment가 훨씬 높다.
- 그러나 **실제 baseline 초과 성장률은 거의 같다.**
- 동일 baseline 층에서 repeat signal은 반복선정 쪽으로 남지만 현재 표본에서는 확증적이지 않다.
- 2011 재선정 여부는 2010 시점에서는 미래 정보이므로 이 분석은 **prospective prediction이 아니라 association**으로 해석한다.

---

## 8. 동아일보 2011 「10년 뒤 한국을 빛낼 100인」 — 진행 중

### 8.1 Baseline

2011 코호트는 다음을 이미 동결했다.

- roster: **100/100**
- T0 scope: **100/100**
- pre-selection lifetime peak through 2011-04-01: **100/100**
- 2010↔2011 repeat: **38명**
- new 2011 entrants: **62명**

### 8.2 Observation window

2011 post-T0 outcome은 반드시 다음 window로 제한한다.

- **start:** 2011-04-01
- **end:** 2026-08-18

2010 자료를 단순 승계하지 않고 cutoff를 다시 적용해 look-ahead/reverse-causation 문제를 방지한다.

### 8.3 Repeat 38명

- 34명: 기존 2010 post-T0 peak가 2012년 이후로 명확하여 안전하게 승계
- 4명: 강덕수·박원순·유시민·이주호를 cutoff 기준으로 직접 재감사
- 결과: **38/38 resolved**

### 8.4 New entrants

현재 신규 62명 중 **20명**의 post-2011 outcome audit를 완료했다.

따라서 현재 partial master는:

- total: **100**
- assessed: **58**
  - repeat: **38/38**
  - new entrants: **20/62**
- pending: **42**

**2011 cohort-wide major precision / apex precision / advancement rate는 100/100 완료 전에는 계산·보고하지 않는다.**

현재 partial master:

`analysis/donga_2011_post_t0_partial_master_v0_2.json`

---

## 9. Coding guardrails

### Baseline을 반드시 분리한다

`post_t0_peak - contemporaneous T0 title`이 아니라:

`post_t0_peak - pre-selection lifetime peak`

으로 advancement를 계산한다.

### Peak와 adverse outcome을 분리한다

형사사건, 직 상실, 경영 실패, 사망 등은 이미 관찰된 prominence peak를 소급해 낮추지 않는다.

- `post_t0_peak_score` = 관찰된 최대 prominence/leadership
- adverse event = 별도 차원
- death truncation = 관찰기간 단축 표시

### Broad screening과 ranked Top-N을 직접 같은 precision으로 비교하지 않는다

동아 100인과 정치 Top10은 cohort design이 다르다.

### 중복 인물은 독립 표본으로 취급하지 않는다

향후 cross-cohort 모델에서는 canonical `person_id`와 person-clustered analysis를 사용한다.

---

## 10. 현재 핵심 파일

```text
state/
  coding_rules_typeA_v0_1.md
  coding_rules_typeA_sector_scope_v0_1.md
  donga_2010_post_t0_peak_protocol_v1_0.md
  donga_2010_post_t0_peak_freeze_v1_2.json
  donga_2010_typeA_result_v1_0.md
  donga_2011_t0_baseline_freeze_v1_0.json

data/typeA/
  newsmaker_2003_outcomes_v0_3.json
  h21_2004_outcomes_v0_1.json
  donga_2010_post_t0_peak_metrics_v1_2.json
  donga_2011_t0_roles_v0_1.json

research/
  donga_2011_post_t0_repeat_cutoff_audit_v0_1.json
  donga_2011_post_t0_new_audit_batch1_v0_1.json
  donga_2011_post_t0_new_audit_batch2_v0_1.json

analysis/
  typeA_cross_cohort_comparison_v0_1.md
  donga_2011_post_t0_seed_v0_2.json
  donga_2011_post_t0_partial_master_v0_2.json

scripts/
  build_donga_2010_post_t0_peak_master.py
  analyze_donga_2010_post_t0_peak.py
  build_donga_2011_post_t0_seed.py
  build_donga_2011_post_t0_partial_master.py

.github/workflows/
  donga-2011-postt0-seed-qa.yml
```

상세 handoff는 `progress_2026-08-18_v8.md` 참고.

---

## 11. QA / reproducibility

동아 2011 파이프라인은 GitHub Actions에서 다음을 재검증한다.

- 2010 frozen T0/baseline 재생성
- 2010 final post-T0 master 재생성
- 2011 audited T0/baseline 재생성
- repeat 38/38 cutoff resolution
- 신규 audit batch의 roster/repeat/중복 검증
- partial master assessed/pending count 검증
- death truncation field 전달 검증
- 주요 apex coding assertion 검증

최신 확인된 성공 run:

- workflow: `Dong-A 2011 Post-T0 Seed QA`
- run ID: `32072437143`
- conclusion: **success**

---

## 12. 현재 우선순위

1. **동아일보 2011 pending 42명 post-T0 audit 완료**
2. 2011 final post-T0 master 100/100 동결
3. 2011 major / apex / advancement / sustained-high 계산
4. 2010 vs 2011 cohort 비교 및 repeat-selection 분석 정교화
5. Type-A common master 구축 — cohort / placement / canonical person_id 통합
6. 한겨레21 2004 31명 전체표 복원
7. 한겨레21 1999, 신동아 1998 및 조선·중앙·경향 계열 archive retrieval
8. 코호트가 충분히 누적되면 person-clustered / mixed-effects model 및 matched-control 설계 도입

### 바로 다음 작업점

현재 2011 pending은 **42명**이다. 다음 batch는 출처가 명확하고 score 경계가 낮은 인물부터 처리한다.

우선 후보:

`김선욱 · 김승환 · 박형주 · 석지영 · 이국종 · 변대규 · 남민우 · 황철주 · 장하석 · 함돈희`

---

## 13. 현재까지 보이는 연구 가설

현재 데이터에서 반복적으로 보이는 신호는 다음과 같다.

1. **Selection과 ranking은 다른 능력일 수 있다.**  
   좋은 후보군을 고르는 능력과 그 안에서 미래 상승 순서를 맞히는 능력은 동일하지 않다.

2. **Raw future attainment는 baseline prestige에 크게 좌우된다.**  
   이미 강한 사람을 고르면 이후 major rate는 자연스럽게 높아진다.

3. **Baseline-adjusted advancement가 미래예측 평가의 핵심이다.**  
   “나중에도 유명했다”와 “선정 뒤 실제로 더 올라갔다”를 분리해야 한다.

4. **Repeated selection은 추가 정보일 가능성이 있으나 아직 확정적이지 않다.**  
   반복선정자의 raw outcome은 강하지만 baseline을 보정하면 차이가 크게 줄어든다.

이 가설들은 향후 더 많은 매체·연도 코호트가 확보되면 정식 통계모형으로 검증한다.
