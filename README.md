# 언론사 선정 인재 추적 — Fame Outcome Follow-up

**기준일:** 2026-08-17  
**현재 단계:** Type B longitudinal Pilot 완료 + Type A 2개 코호트 비교 + 동아일보 2010 explicit-horizon calibration cohort 재구축

## 1. Type B — 동아일보 과학기술 역할모델 Pilot

**코호트:** 동아일보 「닮고 싶고 되고 싶은 과학기술인」 2002–2005, n=39

- 추적축: `T0 → T+10(±1년) → T+20(±1년) → Current`
- Current verified: **29/39 = 74%**
- T+10 strict: **37/39 = 95%**
- T+20 strict: **34/39 = 87%**
- High-status lifetime trajectory: **26/39 = 67%**
- T+10 elite 생존자 중 T+20 elite 유지: **14/19 = 74%**

Type B는 이미 성취한 역할모델 선정이므로 prediction accuracy가 아니라 **persistence / trajectory**로 해석한다.

## 2. Type A — 미래예측형

Type A에서는 세 축을 분리한다.

1. **Selection precision** — 후보군을 잘 골랐는가?
2. **Ranking accuracy** — 순위가 미래 성취 순서를 맞혔는가?
3. **Baseline-adjusted advancement** — 선정 당시 지위를 빼고도 실제 상승했는가?

### A. 뉴스메이커 2003 정치 Top10

- post-T0 major leadership: **10/10**
- post-T0 apex: **2/10**
- baseline-adjusted advanced: **7/10**
- Rank vs post-T0 peak: ρ=-0.306, p=0.389
- **Rank vs advancement Δ: ρ=-0.094, p=0.796**

경제 Top5는 major **5/5**, apex **4/5**, advanced **4/5**이며 rank vs Δ는 ρ=-0.224, p=0.718이다.

### B. 한겨레21 2004 차세대 리더 Top10

복원 순위:
1. 고건 60.0
2. 강금실 47.3
3. 박근혜 46.5
4. 이회창 33.8
5. 정몽준 32.4
6. 정동영 31.0
7. 권영길 26.2
8. 이명박
9. 추미애
10. 이해찬

결과:
- post-T0 major leadership: **10/10**
- apex: **5/10**
- baseline-adjusted advanced: **4/10**
- Rank vs post-T0 peak: ρ=+0.035, p=0.924
- **Rank vs advancement Δ: ρ=+0.402, p=0.249**

### 두 Type A 코호트의 현재 공통 신호

> **후보군 자체는 매우 잘 골랐지만, 후보군 내부의 순위는 누가 더 크게 성장할지를 잘 예측하지 못했다.**

뉴스메이커와 한겨레21 정치 Top10의 20개 placement에는 **16명 unique person**만 있다. 강금실·권영길·정동영·추미애가 중복되므로 outlet 간 비교에서 단순 독립표본 검정은 사용하지 않는다.

| 지표 | 뉴스메이커 2003 | 한겨레21 2004 |
|---|---:|---:|
| T0 baseline mean | 2.4 | 3.3 |
| baseline-adjusted advanced | 7/10 | 4/10 |
| Rank vs Δ ρ | -0.094 | +0.402 |

한겨레21은 T0부터 대통령 권한대행 경험자·대선후보·총리·장관·서울시장 등이 많아, raw future success보다 **baseline adjustment의 필요성**이 특히 크다.

## 3. Explicit-horizon calibration — 동아일보 2010 「2020년 한국을 빛낼 100인」

2010년에 목표연도를 **2020년으로 명시**한 미래예측형 기획이다.

- 총 100명: 편집부 99 + 독자선정 1
- 최초 후보 355명
- 자문위원 8명
- 추천위원 205명
- 평균나이 44.9세
- 여성 16명
- 대학 교수 36명
- 1차 추천 상위: **김빛내리 23표 / 이재용 19표 / 안철수 18표**

카테고리 목표:
- 자유로운 창조인 20
- 꿈꾸는 개척가 25
- 행동하는 지성인 20
- 도전하는 경제인 25
- 미래를 여는 지도자 10

현재 **58/100명**을 직접 확인했다.
- 자유로운 창조인 **20/20**
- 꿈꾸는 개척가 10/25
- 행동하는 지성인 7/20
- 도전하는 경제인 15/25
- 미래를 여는 지도자 6/10

전체 100명 복원 전에는 성공률을 계산하지 않는다. 이 코호트는 완성 후 **2010의 예측을 정확히 목표시점 2020에서 calibration**할 수 있다는 점이 가장 큰 장점이다.

## 4. Repository structure

```text
analysis/
  analysis_v3_1.md
  typeA_newsmaker_2003_v0_3.md
  typeA_h21_2004_v0_1.md
  typeA_cross_cohort_comparison_v0_1.md
  typeA_cross_cohort_metrics_v0_1.json

data/typeA/
  newsmaker_2003_t0_partial.json
  newsmaker_2003_outcomes_v0_3.json
  h21_2004_t0_partial.json
  h21_2004_outcomes_v0_1.json
  donga_2010_2020_100_seed_v0_1.json

research/
  phase2_typeA_candidates.md
  donga_2010_explicit_horizon_discovery_v0_1.md

state/
  coding_rules_v3.md
  coding_rules_typeA_v0_1.md

scripts/
  analyze_v3_1.py
  analyze_typeA_newsmaker_2003.py
  analyze_typeA_cross_cohort.py
  gen_report_v3.py
```

## 5. 다음 우선순위

1. **동아일보 2010 나머지 42명 복원** → 전체 100명 완성
2. 전체 100명에 대해 **target year 2020 outcome** 코딩
3. 1차 추천표 추가 복원 시 vote-count calibration 분석
4. 한겨레21 2004 31명 전체표 복원
5. 한겨레21 1999 및 신동아 1998 원순위 archive retrieval
6. Type A가 3개 이상 완성되면 person-clustered 공통 master dataset 구축
