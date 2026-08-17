# 언론사 선정 인재 추적 — Fame Outcome Follow-up

**기준일:** 2026-08-18  
**현재 단계:** Type B longitudinal pilot 완료 + Type A 3계열/125 placements 분석 기반 확보 + 동아일보 2010 100인 전수 Type-A 추적 완료

## 1. 프로젝트 질문

언론·전문가가 과거에 선정한 “차세대 리더 / 미래 인재 / 영향력 인물”은 실제로 장기적으로 어떻게 되었는가?

Type A(미래예측형)에서는 반드시 다음을 분리한다.

1. **Major-leadership precision** — 선정 뒤 높은 수준의 역할/성과(scope ≥3)에 도달했는가?
2. **Apex precision** — global/national apex(scope 4)에 도달했는가?
3. **Baseline-adjusted advancement** — 선정 전에 이미 달성한 lifetime peak보다 실제로 더 올라갔는가?
4. **Sustained high** — 이미 높은 사람이 이후에도 높은 수준을 유지했는가?
5. **Ranking accuracy** — 순위가 있는 리스트에서 상위 순위가 더 큰 상승폭을 예측했는가?

Type B(이미 성취한 역할모델형)는 prediction accuracy가 아니라 persistence/trajectory로 해석한다.

---

## 2. Type B — 동아일보 과학기술 역할모델 Pilot

**코호트:** 동아일보 「닮고 싶고 되고 싶은 과학기술인」 2002–2005, n=39

- `T0 → T+10(±1년) → T+20(±1년) → Current`
- Current verified: **29/39 = 74%**
- T+10 strict: **37/39 = 95%**
- T+20 strict: **34/39 = 87%**
- High-status lifetime trajectory: **26/39 = 67%**
- T+10 elite 생존자 중 T+20 elite 유지: **14/19 = 74%**

---

## 3. Type A — 완료된 분석 단위

### 3.1 뉴스메이커 2003 정치 Top10

- major leadership: **10/10 (100%)**
- apex: **2/10 (20%)**
- baseline-adjusted advanced: **7/10 (70%)**
- rank vs advancement Δ: **ρ=-0.094, p=0.796**

### 3.2 뉴스메이커 2003 경제 Top5

- major leadership: **5/5 (100%)**
- apex: **4/5 (80%)**
- baseline-adjusted advanced: **4/5 (80%)**
- rank vs advancement Δ: **ρ=-0.224, p=0.718**

### 3.3 한겨레21 2004 정치 Top10

- major leadership: **10/10 (100%)**
- apex: **5/10 (50%)**
- baseline-adjusted advanced: **4/10 (40%)**
- rank vs advancement Δ: **ρ=+0.402, p=0.249**

뉴스메이커 정치 Top10과 한겨레21 Top10의 20 placements는 16 unique persons이며 강금실·권영길·정동영·추미애가 중복된다. 따라서 naïve independent-sample test를 사용하지 않는다.

---

## 4. 동아일보 2010 「2020년 한국을 빛낼 100인」 — 100/100 완료

### 4.1 복원·코딩 상태

- canonical roster: **100/100**
- T0 snapshot: **100/100**
- pre-selection lifetime peak: **100/100**
- target-year 2020 snapshot: resolved 87 / competing-event 3 / unresolved 10
- lifetime post-T0 peak through 2026-08-18: **100/100**
- final unresolved: **0**

### 4.2 최종 Type-A 결과

- post-T0 scope ≥3: **71/100 = 71%**
- post-T0 scope =4: **12/100 = 12%**
- baseline-adjusted advanced: **28/100 = 28%**
- sustained high: **44/100 = 44%**
- no clear advancement: **28/100 = 28%**
- lower than baseline: **0/100**

사망으로 관찰기간이 단축된 최은석·서동철·박원순 3명을 제외한 sensitivity:

- major scope ≥3: **68/97 = 70.1%**
- apex: **12/97 = 12.4%**
- advanced: **26/97 = 26.8%**

### 4.3 가장 중요한 해석

> **71%가 선정 이후 major 수준에 도달했지만, 2010 이전의 lifetime peak까지 보정하면 실제로 더 높은 층위로 상승한 사람은 28%다.**

즉 이 리스트의 성과는 “미래 스타 71% 예측”이라기보다 **이미 강한 사람을 골라낸 screening + 일부의 실제 후속 상승**으로 분해해서 해석해야 한다.

분야별 major / advancement:

- 자유로운 창조인: **80% / 40%**
- 꿈꾸는 개척가: **88% / 12%**
- 행동하는 지성인: **35% / 35%**
- 도전하는 경제인: **68% / 24%**
- 미래를 여는 지도자: **100% / 44.4%**
- 독자선정: **0% / 0%**

---

## 5. 현재 교차 코호트 신호

현재까지 반복되는 가장 강한 패턴은 다음과 같다.

1. **Selection과 ranking은 다른 능력이다.** Top10 코호트들은 후보 자체는 강했지만 순위와 실제 상승폭의 상관은 약했다.
2. **Raw future attainment는 baseline 수준에 크게 좌우된다.** 이미 장관·세계적 과학자·대기업 경영자였던 사람을 고르면 post-T0 major rate는 높아진다.
3. **Broad list와 Top10은 직접 같은 precision으로 비교하면 안 된다.** 동아 2010은 100명·5개 분야의 broad screening이고, 뉴스메이커/한겨레21은 정치·경제 상위 rank 리스트다.
4. 앞으로 outlet 비교의 핵심 outcome은 `post_t0_peak`, `baseline_peak`, `advancement_delta`의 세 축을 함께 보는 것이다.

---

## 6. 현재 핵심 파일

```text
analysis/
  analysis_v3_1.md
  typeA_newsmaker_2003_v0_3.md
  typeA_h21_2004_v0_1.md
  typeA_cross_cohort_comparison_v0_1.md

data/typeA/
  newsmaker_2003_outcomes_v0_3.json
  h21_2004_outcomes_v0_1.json
  donga_2010_canonical_roster_v2_1.json
  donga_2010_post_t0_peak_audit_patch_v1_2.json
  donga_2010_post_t0_peak_metrics_v1_2.json

state/
  coding_rules_typeA_v0_1.md
  coding_rules_typeA_sector_scope_v0_1.md
  donga_2010_t0_baseline_freeze_v1_4.json
  donga_2010_post_t0_peak_protocol_v1_0.md
  donga_2010_post_t0_peak_freeze_v1_2.json
  donga_2010_typeA_result_v1_0.md

scripts/
  build_donga_2010_post_t0_peak_master.py
  analyze_donga_2010_post_t0_peak.py
```

---

## 7. 다음 우선순위

1. **Type-A common master v0.1 구축** — 뉴스메이커 2003 정치10+경제5, 한겨레21 2004 Top10, 동아 2010 100인을 동일 placement schema로 통합.
2. person overlap을 canonical `person_id`로 묶어 repeated-selection 구조를 명시.
3. cohort design을 `ranked_topN / broad_screening / explicit_horizon`으로 분리하여 naïve pooled precision을 금지.
4. 교차 코호트 비교 v0.2 작성 — baseline 분포, major, apex, advancement, sustained-high를 design-aware descriptive comparison.
5. **한겨레21 2004 31명 전체표** 복원 — Top10 selection bias 완화.
6. 한겨레21 1999, 신동아 1998 archive retrieval 지속.
7. 이후 조선·중앙·동아·한겨레·경향 계열의 Type-A 코호트를 동일 protocol로 확장.
8. 충분한 코호트가 쌓이면 person-clustered / mixed-effects 모델과 matched control cohort를 도입해 editorial selection의 incremental predictive value를 평가.
