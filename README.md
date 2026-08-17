# 언론사 선정 인재 추적 — Fame Outcome Follow-up

**기준일:** 2026-08-17  
**현재 단계:** Type B longitudinal Pilot 완료 + Type A 2개 코호트 비교 + 동아일보 2010 explicit-horizon exact roster 복원

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

### Canonical roster v1.1 — 이름 집합 기준

과거의 aggregate count를 누적하는 방식은 중복/유실 위험이 있어 폐기하고, **개인별 row evidence가 붙은 unique-person set**을 canonical source로 사용한다.

- evidence-cleaned v0.2 base: **67명**
- 이후 독립적으로 row-resolved된 추가 인물: **11명**
- base/addition overlap: **0명**
- **canonical row-resolved membership: 78/100**
- remaining: **22명**

추가 11명: 김정범, 박원순, 이창용, 신현송, 현택환, 나경원, 김준영, 김용, 이상훈, 박인출, **서도호**.

서도호는 2013 동아일보 `명예의 전당 21인` 원그래픽에서 확인되며, 2013 Hall이 `통산 세 차례 선정`으로 정의되고 2011 공식 전체명단에는 없으므로 선정연도는 **2010·2012·2013**으로 강제된다. 따라서 2010 membership H. 2013의 category는 2010 category로 소급하지 않는다.

박인출은 2010년 동시대 전문매체들이 동아일보 선정과 `도전하는 경제인` 분야를 구체적으로 보도한 근거로 M-confirmed로 복귀했다. 과거 `78/100` aggregate는 historical audit value일 뿐이며, 현재의 78명은 **별도의 unique-person set audit로 재구축된 수치**다.

### 2010↔2011 repeat reconstruction

동아일보는 2011년 선정자 중 **38명이 2010·2011 2년 연속 선정**됐다고 명시했다.

- row-resolved: **35/38**
- 과학: **8/8 complete**
- 경제: **13/14**, remaining 1
- 문화·지도자·지성인 합계: **14/16**, remaining 2

경제 마지막 1명의 후보는 교차연도 배제 후 **권구훈·김가영·김남구·손병두·최태원·황철주 6명**으로 좁혀졌다. 양윤선·정용진은 연도구조상 2010 repeat에서 제외된다.

2012년 `2010–2012 3년 연속` 명예의 전당 20인은 **20/20 이름 복원 완료**. 2013년 `통산 3회` 명예의 전당도 원그래픽에서 **21/21 이름 복원 완료**했다. 이를 포함한 후대 exact-year evidence를 2010 membership backfill에 사용하되, 후대 category는 2010 category로 소급하지 않는다.

### Primary-source recovery

- 2010 전용 microsite `www.donga.com/news/2020_100/` 존재와 콘텐츠 구조 확인
- 2010-05-10 A1/A4가 100인 표를 담은 원지면임을 archive/정정기사로 확인
- A1/A4 원본 asset endpoint 확인, 고해상도 exact roster 회수는 계속 진행
- Donga NewsBook 2호의 100인 profile archive 존재 확인
- 2013 Hall-of-Fame 원그래픽 직접 판독 완료

### Evidence rule

1. **2010 동아일보 원문**이 selected 100으로 직접 명시/인용 → H
2. **2010 당시 소속기관 공식 공지**가 선정 사실 명시 → H
3. 후대 동아/공식자료가 **2010을 포함하는 정확한 선정연도**를 보장 → H
4. 2010 동시대 전문매체가 선정 및 category를 구체적으로 보도 → M
5. copied list / secondary biography / 현재 유명세만으로는 canonical roster에 넣지 않음

현재 secondary/candidate-generation 상태로 남은 주요 이름은 **김윤진·신지애·이청용·윤명철**이다. 손열음은 연도구조상 2010 membership에서 제외되었고, 서도호는 H-confirmed로 승격되었다.

**2020 적중률은 roster 100/100 freeze 전에는 계산하지 않는다.** 목표시점 outcome은 이후 strict 2019–2021 근거로 평가하고 Current 2026과 분리한다.

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
  donga_2010_canonical_roster_v1_1.json
  donga_2011_100_roster_v0_1.json

research/
  donga_2010_recovery_queue_v1_2.json
  donga_2010_legacy78_reconciliation_v0_3.md
  donga_2010_primary_print_recovery_audit_v0_1.md
  donga_2010_2011_repeat_crosswalk_v0_2.md
  donga_2012_hall_of_fame_backfill_audit_v0_1.md
  donga_2013_hall_image_resolution_v0_1.md

state/
  coding_rules_v3.md
  coding_rules_typeA_v0_1.md
  coding_rules_explicit_horizon_v0_1.md

artifacts/
  donga_2010_v0_2_full.json.xz
```

## 5. 다음 우선순위

1. 2010 exact roster **78 → 100/100** row-level evidence 복원
2. 2011 repeat 잔여 **3명**(경제 1 + 비경제 2) exact-year evidence 확인
3. 2010 A1/A4 원지면 또는 legacy microsite/DNB2에서 exact roster 직접 회수
4. 김윤진·신지애·이청용·윤명철의 2010 qualifying evidence 검증
5. category totals 20/25/20/25/10 reconciliation 및 2010 baseline 저장
6. roster freeze/tag 후에만 **target year 2020 outcome** 코딩
7. 한겨레21 2004 31명 전체표, 한겨레21 1999, 신동아 1998 archive retrieval 지속
8. Type A 3개 이상 완성 후 person-clustered common master dataset 구축
