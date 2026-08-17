# 뉴스메이커 2003 「차세대 리더」 — Type A 분석 v0.3

**작성일:** 2026-08-17  
**T0:** 뉴스메이커 2003-05-30 「차세대 리더 정치·경제」  
**분석대상:** 정치 Top10 + 경제 Top5  
**핵심 변경:** T0 baseline 검증 + `rank → advancement_delta` 분석

## Executive summary

이 코호트의 가장 중요한 결과는 **“선별(selection)과 순위(ranking)는 완전히 다른 능력”**이라는 점이다.

- 정치 Top10: post-T0 major leadership **10/10**, baseline-adjusted advancement **7/10**
- 경제 Top5: post-T0 major leadership **5/5**, baseline-adjusted advancement **4/5**
- 그러나 T0 rank와 **실제 상승폭**의 Spearman:
  - 정치 **ρ=-0.094, p=0.796**
  - 경제 Top5 **ρ=-0.224, p=0.718**

즉 전문가들은 **후보군 자체는 매우 잘 골랐지만, 그 안에서 누가 더 크게 성장할지를 순서대로 맞히지는 못했다.**

---

## 1. 왜 raw 100%를 “예측 성공률 100%”라고 부르면 안 되는가

정치 Top10과 경제 Top5 모두 이후 major leadership에 도달했지만, T0부터 이미 엘리트가 많이 포함돼 있었다.

- 손학규: 경기도지사
- 강금실: 법무부 장관
- 권영길: 2002 대통령 후보
- 강철규: 공정거래위원장
- 정운찬: 서울대 총장
- 이재용: 삼성전자 상무·후계 경영자

따라서 raw precision은 **elite candidate selection**의 질을 보여주는 지표이고, 순수한 미래 상승 예측에는 `advancement_delta`가 더 적절하다.

---

## 2. 세 가지 지표를 분리

| 지표 | 정치 Top10 | 경제 Top5 | 의미 |
|---|---:|---:|---|
| post-T0 major leadership | 10/10 (100%) | 5/5 (100%) | 후보군 선별 |
| post-T0 apex | 2/10 (20%) | 4/5 (80%) | 최고수준 도달 |
| baseline-adjusted advanced | 7/10 (70%) | 4/5 (80%) | 선정 당시보다 실제 상승 |

---

## 3. Ranking accuracy

### Rank vs post-T0 peak
- 정치: ρ=-0.306, p=0.389
- 경제 Top5: ρ=0.0, p=1.0

### Rank vs baseline-adjusted advancement delta
- 정치: **ρ=-0.094, p=0.796**
- 경제 Top5: **ρ=-0.224, p=0.718**

좋은 ranking predictor라면 낮은 rank number(1위, 2위…)가 더 큰 future delta와 연결되어 음의 상관이 뚜렷해야 한다. 현재는 두 분야 모두 거의 관계가 없다.

> **후보 발굴은 성공적이지만, 후보군 내부의 순위는 미래 성장폭을 예측하지 못했다.**

---

## 4. 개인별 baseline-adjusted 결과

| 분야 | Rank | 인물 | T0 baseline | Post-T0 peak | Δ | 판정 |
|---|---:|---|---:|---:|---:|---|
| politics | 1 | 정동영 | 2 | 4 | +2 | advanced |
| politics | 2 | 김근태 | 2 | 3 | +1 | advanced |
| politics | 3 | 손학규 | 3 | 3 | +0 | sustained_high |
| politics | 4 | 유시민 | 2 | 3 | +1 | advanced |
| politics | 5 | 강금실 | 3 | 3 | +0 | sustained_high |
| politics | 6.5 | 추미애 | 2 | 3 | +1 | advanced |
| politics | 6.5 | 권영길 | 4 | 4 | +0 | sustained_high |
| politics | 8 | 이부영 | 2 | 3 | +1 | advanced |
| politics | 9.5 | 천정배 | 2 | 3 | +1 | advanced |
| politics | 9.5 | 강재섭 | 2 | 3 | +1 | advanced |
| economy | 1 | 안철수 | 2 | 4 | +2 | advanced |
| economy | 2 | 장하성 | 2 | 4 | +2 | advanced |
| economy | 3 | 강철규 | 3 | 3 | +0 | sustained_high |
| economy | 4 | 정운찬 | 3 | 4 | +1 | advanced |
| economy | 5 | 이재용 | 2 | 4 | +2 | advanced |

---

## 5. T0 baseline 근거 상태

- 정치 1–5위와 경제 Top5의 T0 직함은 **2003 원기사에 직접 명시**되어 있다.
- 정치 6–10위의 순서는 2005년 뉴스메이커 후속기사에서 2003 조사 결과를 회고하여 확인했다.
- 권영길의 경우 2002년 대통령 후보였다는 사실이 별도 동시대 자료에서 확인되어 baseline score 4가 특히 중요하다.
- 정치 6–10위의 세부 baseline scope mapping은 현재 M confidence로 두고, 향후 당시 프로필 원문을 더 확보하면 H로 승격한다.

---

## 6. 복원 불가능/미완료 상태를 데이터로 유지

### 현재까지 복원된 것
- 정치 Top10 순위: 완료
- 정치 Top5 지목률: 완료
- 경제 Top5 순위·지목률: 완료
- 경제 기사 내 추가 인물: 조학국, 변양호, 이재웅, 진대제, 장하준

### 아직 복원되지 않은 것
- 정치 6–10위 정확 지목률
- 경제 6–10위 정확 순위·지목률

2003 공개 텍스트는 경제 Top5 수치와 “장하준 10위 내”까지만 제공한다. 확인되지 않은 값을 추정해서 채우지 않는다.

---

## 7. 이 코호트가 주는 방법론적 교훈

향후 모든 Type A 코호트에서 다음을 기본으로 한다.

1. **Selection precision**
2. **Ranking accuracy**
3. **Baseline-adjusted advancement**
4. T+10/T+20/Current trajectory
5. death/retirement/sector pivot 별도 처리

특히 `rank → advancement_delta`를 핵심 ranking 지표로 삼는 것이 적절하다. 단순 future peak는 T0에서 이미 높은 후보를 과대평가하기 때문이다.

---

## 8. 다음 작업

1. 정치 6–10위 T0 프로필을 동시대 기사로 재검증해 baseline H 승격.
2. 경제 6–10위 원지면/표 확보 시 전체 경제 Top10으로 확장.
3. **한겨레21 1999 차세대 리더** 원표 확보를 병행.
4. 두 번째 Type A 코호트가 생기면 outlet 간 selection/ranking 성능 비교.
