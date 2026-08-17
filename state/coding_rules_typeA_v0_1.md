# Type A 미래예측형 코호트 코딩 규칙 v0.1

**작성일:** 2026-08-17  
**적용 시작 코호트:** 뉴스메이커 2003 「차세대 리더 정치·경제」

## 1. Type A의 핵심 질문

Type A는 당시 언론/전문가가 **앞으로 더 큰 역할을 할 사람을 예측**한 리스트다.  
따라서 Type B 역할모델 코호트와 달리 다음 세 축을 분리한다.

1. **Selection precision** — 후보군 자체를 잘 골랐는가?
2. **Ranking accuracy** — 높은 순위가 더 큰 미래 성취와 연결됐는가?
3. **Baseline-adjusted advancement** — 이미 높은 T0 지위를 감안해도 실제로 더 상승했는가?

## 2. 원칙

- T0 rank와 score는 원문 그대로 보존한다.
- 확인되지 않은 순위/점수는 추정하지 않는다.
- 사망은 예측 실패가 아니라 competing event다.
- 은퇴·분야전환은 자동 실패가 아니다.
- `peak_role`과 `T+10/T+20/Current` 스냅샷을 분리한다.
- 서로 다른 분야의 직위를 완전히 동등하다고 주장하지 않는다. 아래 0–4 score는 **조직/사회적 영향력의 거친 scope stratum**이다.

## 3. Leadership scope score (0–4)

| Score | 의미 | 예시 |
|---:|---|---|
| 0 | 자료 부족/의미 있는 역할 미확인 | — |
| 1 | 지역·제한적 역할 또는 은퇴 후 제한적 활동 | 지역단체/개별 자문 |
| 2 | 전국 단위의 안정적 전문·정치·경영 역할 | 국회의원, 저명 교수/연구소장, 중견기업 최고경영진 |
| 3 | 주요 국가/정당/대기업 리더십 | 장관, 전국정당 대표, 광역단체 주요 후보, 대기업 최고경영진/부회장 |
| 4 | 국가·산업 apex급 | 대통령/국무총리, 유력 전국 대선후보, 대통령 핵심정책 책임자, 국내 최상위 대기업 회장 |

> 정치와 경제의 score 4가 동일한 사회적 가치를 뜻하는 것은 아니다. 순위와 미래 scope의 연관을 보기 위한 coarse ordinal score다.

## 4. Baseline

`baseline_peak_through_t0` = 선정일 이전 또는 선정 당시까지 이미 도달한 최고 scope.

이 값이 중요한 이유:
- 강금실은 2003년 선정 당시 이미 법무부 장관이었다.
- 강철규는 이미 공정거래위원장이었다.
- 정운찬은 이미 서울대 총장이었다.
- 권영길은 2002년 대통령선거 후보였다.

따라서 단순히 이후 장관/대선후보가 되었다는 사실만으로 모두 동일한 “예측 성공”으로 세지 않는다.

## 5. Post-T0 peak

`post_t0_peak_score` = 선정 이후 새롭게 관찰된 최고 scope.  
`advancement_delta = post_t0_peak_score - baseline_peak_through_t0`.

분류:
- `advanced`: delta > 0
- `sustained_high`: delta = 0 and post peak >= 3
- `no_clear_advancement`: delta = 0 and post peak < 3
- `lower_than_baseline`: delta < 0
- `not_assessable`: 자료 부족

## 6. 시점

뉴스메이커 2003:
- T+10 target = 2013, strict ±1년
- T+20 target = 2023, strict ±1년
- Current = 2026-08

시점마다:
- `role`
- `scope_score`
- `sector`
- `evidence_date`
- `match`
- `confidence`
- `source_notes`

를 기록한다.

## 7. Prediction metrics

### 7.1 Selection precision
- `major_leadership_precision = post_t0_peak_score >= 3`
- `apex_precision = post_t0_peak_score == 4`

### 7.2 Top-k precision
T0 top 3 / top 5 / top 10에서 위 두 기준의 비율.

### 7.3 Ranking accuracy
- Spearman rank correlation between **T0 rank** and `post_t0_peak_score`.
- 좋은 예측이라면 순위 숫자가 낮을수록 peak score가 높으므로 rho는 음수가 기대된다.
- 동순위는 평균 rank를 사용한다.

### 7.4 Baseline-adjusted advancement
`advancement_delta`의 분포와 `advanced` 비율을 별도로 제시한다.

## 8. 해석 규칙

- Selection precision이 높고 ranking correlation이 낮다면:
  > “후보군은 잘 골랐으나 후보군 내부의 순서는 미래 성취를 잘 구분하지 못했다.”
- Peak score가 높지만 baseline delta=0이면:
  > “미래 상승을 예측했다기보다 이미 높은 지위의 지속성을 포착했다.”
- Type A 코호트끼리 비교할 때는 최소한 T0 baseline level, age/career stage, domain을 고려한다.

## 9. 현재 버전의 한계

- 뉴스메이커 2003 경제 부문은 Top 5만 순위·지목률을 완전 복원했다.
- 정치 6–10위는 순위는 복원했지만 지목률은 아직 미복원이다.
- baseline score는 공개된 T0 경력에 기반한 **provisional coding**이며, 원문 프로필 전수 확보 후 재검토한다.
