# 언론사 선정 인재 추적 — Fame Outcome Follow-up

**기준일:** 2026-08-17  
**현재 단계:** Type B longitudinal Pilot 완료 + Type A 2개 코호트 비교 + 동아일보 2010 explicit-horizon roster 재구축/정화

## 1. Type B — 동아일보 과학기술 역할모델 Pilot

**코호트:** 동아일보 「닮고 싶고 되고 싶은 과학기술인」 2002–2005, n=39

- `T0 → T+10(±1년) → T+20(±1년) → Current`
- Current verified: **29/39 = 74%**
- T+10 strict: **37/39 = 95%**
- T+20 strict: **34/39 = 87%**
- High-status lifetime trajectory: **26/39 = 67%**
- T+10 elite 생존자 중 T+20 elite 유지: **14/19 = 74%**

Type B는 이미 성취한 역할모델 선정이므로 prediction accuracy가 아니라 persistence/trajectory로 해석한다.

## 2. Type A — 미래예측형

Type A에서는 `selection precision`, `ranking accuracy`, `baseline-adjusted advancement`를 분리한다.

### 뉴스메이커 2003 정치 Top10
- major leadership **10/10**
- apex **2/10**
- baseline-adjusted advanced **7/10**
- Rank vs advancement Δ: **ρ=-0.094, p=0.796**

경제 Top5: major **5/5**, apex **4/5**, advanced **4/5**, rank vs Δ **ρ=-0.224, p=0.718**.

### 한겨레21 2004 Top10
1 고건, 2 강금실, 3 박근혜, 4 이회창, 5 정몽준, 6 정동영, 7 권영길, 8 이명박, 9 추미애, 10 이해찬.

- major leadership **10/10**
- apex **5/10**
- baseline-adjusted advanced **4/10**
- Rank vs advancement Δ: **ρ=+0.402, p=0.249**

### 교차 코호트 신호
> **후보군 자체는 잘 골랐지만, 후보군 내부 순위는 누가 더 크게 성장할지를 잘 예측하지 못했다.**

두 정치 Top10의 20개 placement는 16명 unique person이며 강금실·권영길·정동영·추미애가 중복된다. 따라서 outlet 간 naïve independent-sample test는 사용하지 않는다.

## 3. Explicit-horizon — 동아일보 2010 「2020년 한국을 빛낼 100인」

2010년에 목표연도 **2020년**을 명시한 calibration cohort.

- 총 100명: 편집부 99 + 독자선정 1
- 최초 후보 355명
- 자문위원 8명 / 추천위원 205명
- 평균나이 44.9세 / 여성 16명 / 대학 교수 36명
- 추천 상위: **김빛내리 23 / 이재용 19 / 안철수 18표**
- category 목표: 자유로운 창조인20 / 꿈꾸는 개척가25 / 행동하는 지성인20 / 도전하는 경제인25 / 미래를 여는 지도자10

### Evidence-cleaned reconstruction v0.2

v0.1에서 secondary copied list를 근거로 일부 category를 `complete`라고 한 주장은 철회했다. v0.2부터 분석 roster는 다음 evidence만 인정한다.

1. **2010 동아일보 원문**이 selected 100으로 직접 명시/인용
2. **2010 당시 소속기관 공식 공지**가 선정 사실 명시
3. 후대 동아/공식자료가 **2010을 포함하는 정확한 반복선정 범위**를 보장

현재 candidate records 73명 중:
- **analysis-eligible membership confirmed: 67명**
- pending: **6명** — 김윤진, 박인출, 서도호, 손열음, 신지애, 이청용
- category 미확정 confirmed member: 11명
- **어느 category도 아직 complete라고 선언하지 않음**

손열음의 후대 `3년 연속 선정` 문구는 정확한 3개 연도가 특정되지 않아 2010 membership 근거로 쓰지 않는다.

**2020 적중률은 roster 100/100 freeze 전에는 계산하지 않는다.** 목표시점 outcome은 strict 2019–2021 근거로 먼저 평가하고 Current 2026과 분리한다.

## 4. 주요 파일

```text
analysis/
  analysis_v3_1.md
  typeA_newsmaker_2003_v0_3.md
  typeA_h21_2004_v0_1.md
  typeA_cross_cohort_comparison_v0_1.md
  typeA_cross_cohort_metrics_v0_1.json

data/typeA/
  newsmaker_2003_outcomes_v0_3.json
  h21_2004_outcomes_v0_1.json
  donga_2010_2020_100_seed_v0_2_cleaned.json

research/
  phase2_typeA_candidates.md
  donga_2010_explicit_horizon_discovery_v0_1.md
  donga_2010_reconstruction_log_v0_2.md

state/
  coding_rules_v3.md
  coding_rules_typeA_v0_1.md
  coding_rules_explicit_horizon_v0_1.md

artifacts/
  donga_2010_v0_2_full.json.xz
```

## 5. 다음 우선순위

1. 동아일보 2010 exact roster **100/100 membership evidence** 복원
2. category totals 20/25/20/25/10 reconciliation 및 2010 baseline 저장
3. roster를 freeze/tag한 뒤에만 **target year 2020 outcome** 코딩
4. 한겨레21 2004 31명 전체표, 한겨레21 1999, 신동아 1998 archive retrieval 지속
5. Type A 3개 이상 완성 후 person-clustered common master dataset 구축
