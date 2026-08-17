# 동아일보 2010 「2020년 한국을 빛낼 100인」 — Target-Year 2020 Metrics v1.0

**Freeze:** `state/donga_2010_target2020_freeze_v1_0.json`  
**Canonical roster:** `data/typeA/donga_2010_canonical_roster_v2_1.json`  
**Builder:** `scripts/build_donga_2010_target2020_master.py`  
**Analyzer:** `scripts/analyze_donga_2010_target2020.py`  
**CI validation:** GitHub Actions run `32050797353`, success

## 1. 무엇을 측정하는가

이 문서의 수치는 **2020년 target-year attainment**다.

기존 Type A 규칙의 `selection precision`과 다르다. Type A selection precision은 `post_t0_peak_score`를 사용하므로, 향후 별도 career-peak dataset이 완성된 뒤 계산해야 한다.

또한 원지면 명단은 영역별 가나다순이므로 list order를 예측 순위로 해석하지 않는다.

## 2. 데이터 완결성

| 상태 | n | 전체 100명 대비 |
|---|---:|---:|
| resolved/scored | 87 | 87.0% |
| competing event | 3 | 3.0% |
| classified unresolved | 10 | 10.0% |
| generic pending | 0 | 0% |

Competing events:

- 최은석 — 2012 사망
- 서동철(Charles D. Surh) — 2017 사망
- 박원순 — 2020 서울시장 재임 중 사망

사망은 낮은 scope나 예측 실패로 치환하지 않는다.

비사망 97명 중 outcome을 score까지 확정한 비율은 **87/97 = 89.7%**다.

## 3. 2020 scope 분포 — resolved 87명

| Scope | n | % of resolved |
|---:|---:|---:|
| 1 | 2 | 2.3% |
| 2 | 43 | 49.4% |
| 3 | 37 | 42.5% |
| 4 | 5 | 5.7% |
| **합계** | **87** | **100%** |

- Mean scope: **2.52**
- Median scope: **2**
- Scope ≥2: **85/87 = 97.7%**
- Scope ≥3: **42/87 = 48.3%**
- Scope =4: **5/87 = 5.7%**

Score 4는 2020 snapshot에서 global/industry/national apex 기준을 충족한 경우로 제한했다. 현재 5명은:

- 봉준호
- 신동빈
- 이재용
- 정의선
- 최태원

## 4. Unresolved sensitivity

Unresolved 10명을 score 0으로 채우지 않는다. 대신 competing event 3명을 제외한 **97명**을 target-year risk set으로 보고 극단적 bound를 계산한다.

| 기준 | 확인된 n | unresolved 전원 기준 미달 | unresolved 전원 기준 충족 |
|---|---:|---:|---:|
| Scope ≥2 | 85 | **87.6%** | **97.9%** |
| Scope ≥3 | 42 | **43.3%** | **53.6%** |
| Scope =4 | 5 | **5.2%** | **15.5%** |

따라서 2020 시점의 `major-scope (≥3)` 도달률은 missingness를 어떻게 두어도 대략 **43–54% 범위** 안에 있다.

이것은 prediction success rate가 아니라 target-year role scope에 대한 보수적 sensitivity bound다.

## 5. Category별 descriptive metrics

| Category | n | resolved | unresolved | competing | resolved mean | Scope ≥3 among resolved | Score 4 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 자유로운 창조인 | 20 | 17 | 2 | 1 | **2.53** | **8/17 (47.1%)** | 1 |
| 꿈꾸는 개척가 | 25 | 24 | 0 | 1 | **2.67** | **16/24 (66.7%)** | 0 |
| 행동하는 지성인 | 20 | 16 | 3 | 1 | **2.06** | **3/16 (18.8%)** | 0 |
| 도전하는 경제인 | 25 | 21 | 4 | 0 | **2.81** | **13/21 (61.9%)** | 4 |
| 미래를 여는 지도자 | 9 | 8 | 1 | 0 | **2.25** | **2/8 (25.0%)** | 0 |
| 독자선정 | 1 | 1 | 0 | 0 | **2.00** | **0/1** | 0 |

### 읽을 때 주의할 점

`도전하는 경제인`은 평균 scope가 가장 높고 score 4도 4명이다. `꿈꾸는 개척가`는 비사망 24명을 모두 resolve했고, 3 이상이 2/3에 달한다.

그러나 이 차이를 곧바로 “동아일보가 과학자·경제인을 더 잘 예측했다”라고 해석할 수는 없다.

- 2010 선정 당시 이미 국제적 교수·대기업 임원·고위 공직자였던 사람이 많다.
- 각 분야에서 scope 2/3/4가 나타나는 career structure가 다르다.
- `미래를 여는 지도자`는 선출직의 주기성이 커서 exact 2020 snapshot에 민감하다. 예를 들어 2021의 더 높은 역할은 의도적으로 2020 score에 소급하지 않았다.
- category별 unresolved 비율도 다르다.

따라서 category 표는 **descriptive target-year comparison**으로만 사용한다.

## 6. 현재 단계에서 말할 수 있는 것

가장 안전한 표현은 다음과 같다.

> 동아일보가 2010년에 ‘2020년 한국을 빛낼 100인’으로 선정한 사람 가운데, 목표연도 전 사망 3명을 제외한 97명 중 87명(89.7%)의 2020 역할을 재현 가능한 근거로 평가할 수 있었다. 평가 가능한 87명 중 42명(48.3%)은 2020년에 major national/international leadership 또는 이에 준하는 scope 3 이상에 도달해 있었다. unresolved 10명을 모두 보수적 실패 또는 모두 성공으로 두는 극단적 sensitivity에서도 이 비율은 비사망 전체 기준 약 43.3–53.6% 범위였다.

하지만 이것만으로 ‘예측이 절반 성공했다’고 결론 내리면 안 된다. 이미 2010년에 높은 위치에 있던 인물이 많기 때문에 다음 단계에서 **T0 baseline-adjusted advancement**와 **post-T0 career peak**를 분리해야 한다.

## 7. 다음 분석

1. 100명의 `baseline_peak_through_t0` scope coding
2. 2010 이후 `post_t0_peak_score`와 peak year/role coding
3. `advancement_delta = post_t0_peak_score - baseline_peak_through_t0`
4. Type A `major_leadership_precision`, `apex_precision`
5. target-2020 attainment와 career-peak success를 나란히 비교
6. 2026 Current snapshot은 target2020 및 career peak와 별도 축으로 추가

이 구조를 쓰면 다음 세 질문을 구분할 수 있다.

- **2020 그 시점에 실제로 높은 역할을 하고 있었는가?**
- **2010 이후 한 번이라도 더 높은 peak에 도달했는가?**
- **그 성취는 2010 당시 이미 높은 baseline을 넘어선 상승이었는가?**
