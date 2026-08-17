# 동아일보 2010 「2020년 한국을 빛낼 100인」 장기추적 결과 v1.1

**작성일:** 2026-08-18  
**관찰종료:** 2026-08-18  
**선정 기준시점:** 2010-05-10  
**상태:** frozen analytic result  
**freeze:** `state/donga_2010_post_t0_peak_freeze_v1_1.json`

---

## 1. Executive summary

동아일보가 2010년 선정한 「2020년 한국을 빛낼 100인」을 선정 시점의 지위와 이후 경력을 분리해 추적했다.

최종 100명 중 **99명의 post-selection career peak를 평가 가능**했고, 1명(박성훈)은 선정 이후 동일인 경력 연결 근거가 충분하지 않아 unresolved로 남겼다. 사망으로 관찰기간이 단축된 3명(최은석, 서동철, 박원순)은 실패로 처리하지 않고 별도 sensitivity analysis를 실시했다.

### 핵심 결과

| 지표 | 결과 | 의미 |
|---|---:|---|
| 평가 가능 | **99/100** | post-T0 peak를 재현 가능한 근거로 코딩 |
| post-T0 peak scope ≥3 | **72/99 (72.7%)** | 선정 이후 어느 시점에 major national / international leadership·achievement 수준 이상에 도달 또는 유지 |
| post-T0 apex scope =4 | **12/99 (12.1%)** | global/national apex 수준에 도달 |
| preselection peak 초과 | **29/99 (29.3%)** | 선정 당시까지 이미 달성했던 개인 최고 scope를 이후 실제로 넘어섬 |
| high level 지속 | **44/99 (44.4%)** | 선정 전 이미 scope≥3이었고 이후에도 같은 최고 stratum을 유지 |
| 명확한 추가 상승 없음 | **26/99 (26.3%)** | post-T0 peak가 baseline peak를 초과하지 않음 |
| baseline보다 낮은 post-T0 peak | **0/99** | coarse lifetime-peak rubric상 없음 |

**가장 중요한 해석은 72.7%와 29.3%의 차이다.**  
이 명단은 장기적으로 높은 수준에 남을 사람을 상당히 잘 포함했지만, 그중 상당수는 선정 당시 이미 상당한 성취를 이룬 인물이었다. 따라서 **“미래의 거물을 새로 발굴했다”는 의미의 상승률은 약 29%**이고, **“이미 강한 사람을 골라 그들이 이후에도 major level에 도달·유지했다”는 의미의 attainment는 약 73%**다.

---

## 2. 왜 baseline adjustment가 필요한가

단순히 2010년 이후 성공 여부만 보면 hindsight bias가 크다. 예를 들어 2010년에 이미 세계적 선수, 대기업 핵심 경영자, 장관·광역단체장, 국제적 연구자였던 인물은 이후에도 높은 위치에 있을 가능성이 원래 높다.

따라서 세 축을 분리했다.

1. **T0 snapshot scope**: 2010 선정 당시 그 순간의 역할/성취
2. **baseline peak through T0**: 선정일까지 생애에서 이미 달성한 최고 scope
3. **post-T0 peak**: 선정 이후 2026-08-18까지 달성한 최고 scope

최종 T0 분포는 다음과 같다.

- scope 1: 1명
- scope 2: 48명
- scope 3: 48명
- scope 4: 3명
- 평균: **2.53**

preselection lifetime peak를 반영한 baseline v1.4는 다음과 같다.

- scope 1: 1명
- scope 2: 46명
- scope 3: 50명
- scope 4: 3명
- 평균: **2.55**

T0 snapshot보다 과거 최고점이 더 높았던 명확한 사례는 **이소연, 김병국 2명**이었다.

이 baseline을 사용해 다음을 정의했다.

`advancement_delta = post_t0_peak_score - baseline_peak_through_t0`

따라서 단순한 직함 변화가 아니라 **선정 당시까지 이미 확보한 career capital을 넘어섰는가**를 보게 된다.

---

## 3. Post-T0 peak 분포

99명 assessed에서 post-T0 최고 scope는 다음과 같다.

| Post-T0 peak | n | 비율 |
|---:|---:|---:|
| 2 | 27 | 27.3% |
| 3 | 60 | 60.6% |
| 4 | 12 | 12.1% |
| **합계** | **99** | **100%** |

scope≥3는 72명으로 **72.7%**였다.

이는 2020이라는 특정 한 해의 snapshot 결과와는 다른 지표다. 앞서 frozen target-2020 분석에서는 87명 resolved 중 scope≥3가 **42/87 (48.3%)**였다. 장기 career peak를 보면 72.7%까지 올라간다.

즉 **정확히 2020년에 높은 자리에 있었는가**와 **2010 이후 어느 시점엔가 높은 수준까지 갔는가**는 상당히 다른 질문이다.

---

## 4. Advancement: 실제로 더 올라갔는가

| 분류 | n/99 | 비율 | 정의 |
|---|---:|---:|---|
| **advanced** | **29** | **29.3%** | post-T0 peak > baseline peak |
| **sustained high** | **44** | **44.4%** | baseline≥3이고 post-T0 peak가 같은 high stratum 유지 |
| **no clear advancement** | **26** | **26.3%** | post-T0 peak = baseline, high stratum 신규 상승 없음 |
| lower than baseline | 0 | 0% | post-T0 lifetime peak < baseline |

평균 advancement delta는 **+0.293**이었다.

이 결과는 언론 선정의 성격을 두 가지로 분리해 보여준다.

### A. Major-leadership attainment

> “선정한 사람이 이후에도 사회적으로 큰 역할이나 성취를 보였는가?”

→ **72.7%**

### B. True upward discovery

> “선정 당시 이미 달성한 수준보다 이후 실제로 더 높은 stratum에 올라갔는가?”

→ **29.3%**

따라서 이 코호트만 보면 선정은 **future discovery라기보다 high-potential/high-status filtering의 성격이 더 강했다**고 보는 것이 적절하다.

다만 이것만으로 동아일보의 ‘예측 능력’을 단정할 수는 없다. 비선정 대조군의 자연 상승률과 비교하지 않았기 때문이다.

---

## 5. 분야별 결과

| 선정 category | n | assessed | scope≥3 | apex=4 | advanced | mean Δ |
|---|---:|---:|---:|---:|---:|---:|
| 미래를 여는 지도자 | 9 | 9 | **9 (100%)** | 1 | 4 | **+0.444** |
| 꿈꾸는 개척가 | 25 | 25 | **22 (88.0%)** | 1 | 3 | +0.120 |
| 자유로운 창조인 | 20 | 19 | **16 (84.2%)** | 4 | 8 | +0.421 |
| 도전하는 경제인 | 25 | 25 | **17 (68.0%)** | **5** | 6 | +0.240 |
| 행동하는 지성인 | 20 | 20 | **8 (40.0%)** | 1 | **8** | +0.400 |
| 독자선정 | 1 | 1 | 0 | 0 | 0 | 0.000 |

### 관찰되는 패턴

- **미래를 여는 지도자**는 9명 전원이 이후 scope≥3에 도달했지만, 5명은 이미 선정 전 high-level stratum에 있었고 실제 추가 상승은 4명이었다.
- **꿈꾸는 개척가**는 major attainment가 88%로 매우 높지만 advanced는 3/25에 불과하다. 이는 상당수가 2010년에 이미 국제적 연구자였음을 반영한다.
- **자유로운 창조인**은 advanced 8/19로 상승 폭이 가장 큰 그룹 중 하나이며 apex도 4명으로 많다.
- **도전하는 경제인**은 apex 5명으로 가장 많지만, baseline 자체가 높은 인물이 많아 advanced는 6/25다.
- **행동하는 지성인**은 major attainment는 40%로 낮지만 advanced는 8/20이다. 즉 절대 최고 stratum 도달과 상대적 career advancement가 서로 다른 정보를 준다.

분야 간 직접 우열 비교에는 주의가 필요하다. 정치·기업·학술·문화·시민사회는 career ladder의 구조와 apex의 희소성이 다르며, 현재 0–4 score는 이를 sector-normalized coarse ordinal scale로 맞춘 것이다.

---

## 6. 사망 competing event / truncation sensitivity

선정 이후 사망으로 장기 관찰기간이 단축된 사람은 3명이다.

- 최은석
- 서동철
- 박원순

이들은 사망 전까지 도달한 post-T0 peak를 기록했지만, 2026년까지의 동일한 exposure time을 가질 수 없으므로 별도 sensitivity를 계산했다.

### 사망 3명 제외, assessed 96명

- scope≥3: **69/96 = 71.9%**
- apex=4: **12/96 = 12.5%**
- advanced: **27/96 = 28.1%**
- mean advancement delta: **+0.281**

주 분석과 큰 차이가 없다.

---

## 7. Remaining unresolved sensitivity

최종 unresolved는 **박성훈 1명**이다.

2010 선정 당시 identity와 국제기능올림픽 요리 금메달 및 롯데호텔 피에르 가니에르 경력은 확실하지만, 선정 이후 동일인임을 신뢰도 높게 이어주는 career bridge를 확보하지 못했다. 동명이인 자료를 억지로 연결하지 않았다.

사망 3명을 제외하고 박성훈을 분모에 유지한 97명에서, 이 1명을 criterion 미달/달성으로 각각 놓은 bound는 다음과 같다.

| 지표 | lower | upper |
|---|---:|---:|
| scope≥3 | **71.1%** | **72.2%** |
| apex=4 | **12.4%** | **13.4%** |
| advanced | **27.8%** | **28.9%** |

따라서 남은 1명의 uncertainty가 전체 결론을 실질적으로 바꾸지는 않는다.

---

## 8. 이 결과로 말할 수 있는 것 / 없는 것

### 말할 수 있는 것

1. 동아일보 2010 선정자 대부분은 이후에도 상당한 사회적·전문적 수준에 도달했다.
2. assessed 99명 중 72.7%는 post-selection lifetime peak가 scope≥3이었다.
3. 그러나 선정 당시까지의 최고 수준을 넘어선 사람은 29.3%였다.
4. 따라서 명단의 성공은 **새로운 미래 인재의 발굴**과 **이미 강한 인물의 선별**을 반드시 분리해서 평가해야 한다.
5. 정확히 2020년 한 시점의 성취율(48.3%)과 post-T0 lifetime peak(72.7%)는 다른 개념이며 둘 다 보존할 가치가 있다.

### 아직 말할 수 없는 것

1. **“동아일보가 일반인보다 3배 잘 맞혔다”** 같은 예측력 주장은 불가능하다. 대조군이 없다.
2. 다른 언론사보다 우수했는지도 아직 모른다.
3. category 간 비율 차이를 편집진의 예측능력 차이로 바로 해석할 수 없다.
4. 0–4 점수를 interval scale처럼 정밀 수치로 해석하면 안 된다.
5. 명단이 category 내부에서 가나다순이므로 순위 예측 정확도는 계산할 수 없다.

---

## 9. 현재 단계에서의 핵심 결론

이 코호트는 단순히 “2010년에 찍은 100명 중 2020년에 몇 명이 성공했나”로 평가하면 정보가 크게 손실된다.

보다 정확한 결론은 다음과 같다.

> **동아일보의 2010 명단은 장기적으로 major-level 인물이 될/남을 사람을 높은 비율로 포함했다. 그러나 그 성과의 상당 부분은 미래의 무명 인재를 발굴했다기보다, 선정 당시 이미 상당한 career capital을 가진 사람을 선별한 데서 왔다.**

99명의 평가 가능자 중:

- **72.7%**는 이후 major level 이상에 도달 또는 유지했고,
- **12.1%**는 apex에 도달했으며,
- **29.3%**만 선정 전 개인 최고 수준을 실제로 넘어섰다.

즉 이 프로젝트에서 가장 중요한 outcome은 앞으로도 **absolute attainment와 incremental advancement를 동시에 보고하는 것**이다.

---

## 10. 다음 연구 단계

이제 한 코호트 내부의 follow-up coding은 충분히 안정화됐다. 다음 단계부터는 언론의 진짜 forecasting value를 검증해야 한다.

### 우선순위 1 — 다른 선정 코호트에 동일 pipeline 적용

- 동아일보 2011 또는 인접 연도
- 조선일보
- 중앙일보
- 한겨레
- 경향신문

동일한 `T0 → baseline peak → T+10 snapshot → post-T0 peak → advancement` 구조로 코딩한다.

### 우선순위 2 — matched control 구축

가장 강한 연구설계는 선정자와 유사한 T0 수준이지만 명단에 선정되지 않은 인물을 매칭하는 것이다.

예:

- 같은 분야
- 비슷한 나이
- 비슷한 2010 직위/scope
- 유사한 기관 수준
- 가능하면 비슷한 당시 언론 노출량

그 후 비교한다.

- P(post-T0 peak≥3 | selected)
- P(post-T0 peak≥3 | matched non-selected)
- P(advancement>0 | selected)
- P(advancement>0 | matched non-selected)

이 비교가 있어야 비로소 **언론 선정 자체가 추가적인 예측정보를 가졌는가**를 평가할 수 있다.

### 우선순위 3 — 반복 선정 효과

2010·2011 등 여러 해에 반복 선정된 인물의 성과가 단회 선정자보다 높은지 검증한다.

이는 초기 프로젝트에서 확보한 2010↔2011 연속 선정자 자료와 직접 연결된다.

---

## 11. Reproducibility

핵심 입력/규칙:

- `state/donga_2010_post_t0_peak_protocol_v1_0.md`
- `state/donga_2010_t0_baseline_freeze_v1_4.json`
- `data/typeA/donga_2010_post_t0_peak_audit_patch_v1_1.json`

최종 deterministic builder:

- `scripts/build_donga_2010_post_t0_peak_master.py`

builder가 생성하는 runtime outputs:

- `data/typeA/donga_2010_post_t0_peak_master_v1_1.json`
- `data/typeA/donga_2010_post_t0_peak_master_v1_1.csv`
- `data/typeA/donga_2010_post_t0_peak_metrics_v1_1.json`

validation:

- GitHub Actions workflow: `.github/workflows/donga-target2020-qa.yml`
- validation commit: `d592a9a3240550a0e7074f3953cf6f0de696426e`
- Actions run: `32067234779`
- result: **success**

향후 새 증거나 rubric 변경이 생기면 v1.1을 수정하지 않고 v1.2 이상으로 version-up 한다.
