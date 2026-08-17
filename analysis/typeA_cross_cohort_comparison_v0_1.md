# Type A 교차 코호트 비교 v0.1
## 뉴스메이커 2003 정치 Top10 vs 한겨레21 2004 Top10

**작성일:** 2026-08-17  
**목적:** 서로 다른 미래예측형 언론 리스트에서 `selection precision`, `ranking accuracy`, `baseline-adjusted advancement`가 반복되는지 확인.

---

## 1. 가장 중요한 결과

두 코호트 모두 **후보 선별은 매우 강하지만 순위 예측은 약하다.**

| 지표 | 뉴스메이커 2003 정치 Top10 | 한겨레21 2004 Top10 |
|---|---:|---:|
| n | 10 | 10 |
| post-T0 major leadership | 10/10 (100%) | 10/10 (100%) |
| post-T0 apex | 2/10 (20%) | 5/10 (50%) |
| baseline-adjusted advanced | **7/10 (70%)** | **4/10 (40%)** |
| sustained high | 3/10 | 4/10 |
| lower than baseline | 0/10 | 2/10 |
| T0 baseline mean | **2.4** | **3.3** |
| advancement Δ mean | **0.8** | **0.2** |
| Rank vs post-T0 peak ρ | -0.306 (p=0.389) | 0.035 (p=0.924) |
| **Rank vs advancement Δ ρ** | **-0.094 (p=0.796)** | **0.402 (p=0.249)** |

### 해석

> **두 매체 모두 “누가 앞으로 중요할 사람인가”는 잘 골랐지만, “그중 누가 더 크게 성장할 것인가”를 순위로 맞히지는 못했다.**

뉴스메이커의 rank→Δ는 거의 0(ρ=-0.094), 한겨레21은 오히려 양수(ρ=0.402)다. 좋은 ranking predictor라면 1위에 가까울수록 상승폭이 커야 하므로 음의 상관이 기대된다. 어느 코호트도 그 신호가 뚜렷하지 않다.

---

## 2. 한겨레21에서 baseline-adjusted advancement가 낮은 이유

한겨레21 2004는 T0 baseline 평균이 **3.3**, 뉴스메이커 2003은 **2.4**이다.

한겨레21에는 선정 당시 이미 대통령 권한대행 경험자, 전/현 장관, 대통령 후보 경험자, 서울시장, 국무총리 등이 다수 포함돼 있었다. 따라서 raw `major leadership 10/10`은 미래예측만이 아니라 **이미 전국급 엘리트였던 사람을 다시 고른 효과**를 상당히 포함한다.

이 때문에 앞으로 Type A의 primary outcome은 단순 `future peak`보다 **`advancement_delta = post-T0 peak − T0 baseline`**를 우선하는 것이 타당하다.

---

## 3. 중복 인물 때문에 코호트 간 단순 유의성 검정은 하지 않는다

20개 placement 중 실제 unique person은 **16명**이며, 아래 4명은 두 조사에 모두 등장한다.

| 인물 | 뉴스메이커 2003 rank | 한겨레21 2004 rank | 순위변화(H21−NM) | NM Δ | H21 Δ |
|---|---:|---:|---:|---:|---:|
| 강금실 | 5 | 2 | -3 | +0 | +0 |
| 권영길 | 6.5 | 7 | +0.5 | +0 | +0 |
| 정동영 | 1 | 6 | +5 | +2 | +1 |
| 추미애 | 6.5 | 9 | +2.5 | +1 | +1 |

중복 4명의 평균 절대 순위 이동은 **2.75계단**이다.

특히 정동영은 **1위 → 6위**, 강금실은 **5위 → 2위**, 추미애는 **공동 6위 → 9위**로 1년 차이의 다른 조사에서도 평가순위가 상당히 움직인다.

따라서 `outlet A 7/10 vs outlet B 4/10`을 독립된 두 표본처럼 Fisher test하는 것은 적절하지 않다. 향후 여러 코호트를 합칠 때는 **person-clustered / repeated-measures 구조**를 명시적으로 처리해야 한다.

---

## 4. 지금까지 드러난 프로젝트의 핵심 분석 프레임

### A. Candidate selection
> “중요해질 사람을 후보군 안에 넣었는가?”

현재 두 정치 Top10 모두 post-T0 major leadership 10/10.

### B. Ranking discrimination
> “1위가 8위보다 실제로 더 크게 성장했는가?”

현재 두 코호트 모두 거의 신호 없음.

### C. Baseline-adjusted advancement
> “이미 가진 지위를 빼고도 실제로 상승했는가?”

- 뉴스메이커: **7/10**
- 한겨레21: **4/10**

### D. Persistence vs advancement
이미 높은 T0 인물을 고른 리스트에서는 **높은 지위 유지(persistence)**와 **미래 상승(advancement)**을 분리해야 한다.

---

## 5. 현재 단계의 가설

1. **언론/전문가의 강점은 ranking보다 screening** — 두 코호트에서 반복되는 가장 강한 패턴.
2. **“차세대 리더” 리스트는 미래예측과 현직 엘리트 재확인의 혼합물** — baseline이 높은 한겨레21 2004에서 특히 뚜렷.
3. **순위는 시대의 인기/주목도를 더 강하게 반영할 수 있다** — contemporaneous preference와 long-term advancement는 다를 수 있음.

아직 코호트가 2개뿐이므로 검증된 결론이 아니라 **사전가설**로 유지한다.

---

## 6. 다음 분석 설계

두 번째/세 번째 매체를 추가할 때 다음 필드를 공통 schema로 강제한다.

```yaml
person_id:
outlet:
cohort_date:
domain:
rank:
score:
baseline_scope:
post_t0_peak_scope:
advancement_delta:
t10_scope:
t20_scope:
current_scope:
death_competing_event:
sector_transition:
```

동일 인물이 여러 리스트에 등장하므로 최종적으로 person-level clustered standard errors, mixed-effects/ordinal model, 또는 person 단위 요약 후 outlet 비교 중 하나를 사용한다. n이 충분해지기 전까지는 **effect size + descriptive distribution 중심**으로 간다.

---

## 7. 다음 데이터 우선순위

1. **한겨레21 2004 31명 전체표** 복원 — Top10만 보면 selection precision이 구조적으로 높아질 수 있음.
2. **한겨레21 1999 전체 후보표** 복원.
3. **신동아 1998 차세대 정치인 전체 순위** 복원.
4. 3개 이상 Type A가 확보되면 공통 master dataset 구축.
5. 이후 조선·중앙·동아·한겨레·경향 계열을 동일 프레임으로 확장.

---

## 결론

> **언론과 전문가 집단은 미래에 중요한 역할을 맡을 ‘후보군’을 고르는 데는 상당히 강했지만, 후보군 내부의 세밀한 순위는 장기적인 상승폭을 잘 예측하지 못했다.**

이 가설은 앞으로 추가 코호트에서 검증할 프로젝트의 중심 명제가 될 수 있다.
