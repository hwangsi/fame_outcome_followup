# 동아일보 2011 「10년 뒤 한국을 빛낼 100인」 T+10 결과 v1.0

**Freeze date:** 2026-08-18  
**Target year:** 2021  
**Admissible window:** 2020-01-01 ~ 2022-12-31  
**Primary rule:** 2021 direct evidence > nearest 2020/2022 evidence

## 1. Coverage

- original N = **100**
- final outcome paths = **100/100**
- assessable = **90**
- competing event = **1** — 박원순
- untraceable = **9** — 강덕수, 김준영, 김해성, 박지영, 김영준, 신준호, 하상백, 김상우, 최재경

Untraceable rows are not assigned zero scores.

## 2. Final T+10 metrics

Primary denominator is the 90 assessable persons.

| metric | n / assessable | rate |
|---|---:|---:|
| Scope ≥2 | 87 / 90 | **96.7%** |
| Major ≥3 | 63 / 90 | **70.0%** |
| Apex =4 | 4 / 90 | **4.4%** |

Score distribution among assessable persons:

- score 0: 1
- score 1: 2
- score 2: 24
- score 3: 59
- score 4: 4

Evidence provenance:

- exact 2021 / tenure explicitly spanning 2021: **81**
- nearest 2020: **8**
- nearest 2022: **1**

## 3. Lifetime peak와 T+10은 다르다

같은 2011 cohort의 lifetime post-selection layer에서는:

- Major = **90%**
- Apex = **12%**
- Advanced = **36%**

그러나 2021±1 fixed-window에서는:

- Major = **70.0% of assessable**
- Apex = **4.4% of assessable**

이는 언론의 선정이 훗날 한 번이라도 높은 peak에 도달할 사람을 잘 포함했는지와, 정확히 10년 뒤에도 높은 역할을 점유하고 있었는지가 전혀 다른 질문임을 보여준다. 두 수치는 denominator도 다르므로 단순 percentage-point paired estimate로 해석하지 않는다.

## 4. 2021-first rule이 실제로 바꾼 사례

- **이주호**: 2022 부총리·교육부장관 score 3 대신 2021 KDI 교수 **score 2**
- **봉준호**: 2020 Academy apex score 4 대신 2021 영화감독 활동 **score 3**
- **손흥민**: 2022 Premier League Golden Boot score 4 대신 2021 PFA Team of the Year·토트넘 핵심선수 **score 3**
- **유범재**: 2020 한국로봇학회장 score 3 대신 2021 KIST 연구자·학회 명예회장 **score 2**
- **이서현**: 과거 삼성물산 패션부문장 score 3 대신 2021 삼성복지재단 이사장 **score 2**
- **박근혜**: 과거 대통령 apex를 유지하지 않고 2021 active leadership role 부재 **score 0**

즉 fixed-window layer는 lifetime peak를 단순 재포장한 결과가 아니다.

## 5. Repeat 38 vs new 62 — T+10 descriptive comparison

### Repeat-selected

- original N = 38
- assessable = 33
- competing event = 1
- untraceable = 4
- Scope ≥2 = **32/33 = 97.0%**
- Major = **25/33 = 75.8%**
- Apex = **3/33 = 9.1%**

### New 2011 entrants

- original N = 62
- assessable = 57
- untraceable = 5
- Scope ≥2 = **55/57 = 96.5%**
- Major = **38/57 = 66.7%**
- Apex = **1/57 = 1.8%**

Exploratory Fisher exact two-sided:

- Scope ≥2: p = **1.000**
- Major: p = **0.475**
- Apex: p = **0.138**

따라서 lifetime layer에서 보였던 repeat group의 apex signal은 T+10 snapshot에서도 방향은 같지만, 이 표본에서는 통계적으로 명확하지 않다. 반복선정은 randomized exposure가 아니므로 causal interpretation은 금지한다.

## 6. Methodological conclusion

동아 2011은 세 층을 동시에 보여준다.

1. **Lifetime selection quality:** Major 90% — 선정자 대부분이 이후 어느 시점엔 높은 수준에 도달하거나 유지했다.
2. **Baseline-adjusted rise:** Advanced 36% — 이미 높았던 사람을 제외하면 실제 상승은 훨씬 적다.
3. **T+10 persistence:** Major 70.0% among assessable — 정확히 10년 뒤 major role을 점유한 비율은 lifetime peak보다 낮다.

따라서 향후 매체 비교에서는 `Lifetime Major/Apex`, `Advanced`, `T+10/T+20 occupancy`를 반드시 독립 outcome으로 보고해야 한다.

## 7. Canonical files

- `data/typeA/donga_2011_t10_final_master_v1_0.json`
- `data/typeA/donga_2011_t10_metrics_v1_0.json`
- `state/donga_2011_t10_freeze_v1_0.json`

Remaining-30 audit layers:

- `research/donga_2011_t10_remaining30_creative_sports_v1_0.json`
- `research/donga_2011_t10_remaining30_public_legal_v1_0.json`
- `research/donga_2011_t10_remaining30_hard_academic_business_v1_0.json`

## 8. Next

동아 2010 canonical target2020/T+10과 동아 2011 T+10을 동일 denominator semantics로 비교한다. Placement-level 결과를 먼저 제시하고, 38명 반복선정으로 인한 dependence를 처리하기 위해 162 unique-person two-wave sensitivity analysis를 별도로 수행한다.
