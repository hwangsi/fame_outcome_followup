# Dong-A 2010 Baseline & Post-T0 Peak Protocol v1.0

**Generated:** 2026-08-18  
**Cohort:** 동아일보 2010 「2020년 한국을 빛낼 100인」  
**Parent rules:** `state/coding_rules_typeA_v0_1.md`, `state/coding_rules_typeA_sector_scope_v0_1.md`

## 1. 목적

2020 target-year scope가 높다는 사실만으로 2010년의 미래예측이 성공했다고 판단하지 않는다.

선정 당시 이미 장관·광역단체장·대기업 회장·세계적 교수·올림픽 챔피언이었던 사람과, 2010 이후 새롭게 그 수준에 오른 사람을 분리해야 한다.

따라서 각 인물에 세 개의 서로 다른 scope를 둔다.

1. `t0_snapshot_scope_score`
2. `baseline_peak_through_t0`
3. `post_t0_peak_score`

2020 target-year score는 네 번째 별도 축으로 유지한다.

## 2. T0 snapshot

`t0_snapshot_scope_score` = 동아일보 선정 시점인 2010년 5월 전후에 실제로 맡고 있던 역할의 scope.

원칙:

- 원지면 캡처의 역할/소속을 primary source로 사용한다.
- `전 장관`, `전 의원`처럼 과거직이 명시된 경우 과거 peak 자체를 T0 snapshot으로 넣지 않는다.
- 당시 현역 선수/창작자/연구자의 실적은 선정시점까지 발생한 것만 사용한다.
- 2010년 후반의 승진·수상은 T0 snapshot에 소급하지 않는다.

## 3. Baseline peak through T0

`baseline_peak_through_t0` = 선정일까지 평생 이미 도달했던 최고 scope.

예:

- 유시민: T0에는 `전 보건복지부 장관`이므로 T0 snapshot과 별개로 prior minister peak를 baseline peak에 반영한다.
- 세계 1위/올림픽 우승을 이미 달성한 선수는 현재 직함이 단순 `선수`여도 해당 성취가 선정일 전에 발생했다면 baseline peak에 포함한다.

필드:

- `baseline_peak_through_t0.score`
- `baseline_peak_through_t0.role_or_achievement`
- `baseline_peak_through_t0.date`
- `baseline_peak_through_t0.evidence_urls`
- `baseline_peak_through_t0.confidence`

## 4. Post-T0 peak

`post_t0_peak_score` = 선정일 이후 새롭게 관찰된 최고 scope.

- 시작: 2010년 선정일 이후
- 종료: 현재 데이터 cutoff(2026-08)까지
- 2020 target snapshot과 분리
- 일시적 최고직도 peak로 기록하되 날짜와 duration/temporary 여부를 보존
- 사망 전 peak는 기록 가능하지만 사망 자체는 실패로 취급하지 않음

필드:

- `post_t0_peak.score`
- `post_t0_peak.role_or_achievement`
- `post_t0_peak.start_date`
- `post_t0_peak.end_date`
- `post_t0_peak.evidence_urls`
- `post_t0_peak.confidence`

## 5. Advancement

`advancement_delta = post_t0_peak_score - baseline_peak_through_t0.score`

분류는 기존 Type A 규칙을 따른다.

- `advanced`: delta > 0
- `sustained_high`: delta = 0 and post peak >= 3
- `no_clear_advancement`: delta = 0 and post peak < 3
- `lower_than_baseline`: delta < 0
- `not_assessable`: evidence 부족/competing event 등으로 비교 불가

단, `lower_than_baseline`은 도덕적·직업적 실패를 뜻하지 않는다. 선정 이전 peak보다 이후 peak가 낮았다는 기술적 분류다.

## 6. Explicit-target cohort의 추가 질문

이 코호트는 2020이라는 목표연도를 명시했으므로 일반 Type A보다 한 축을 더 가진다.

### A. Target-year attainment
`target2020.scope_score`

### B. Long-run selection quality
`post_t0_peak_score`

### C. True advancement
`post_t0_peak_score - baseline_peak_through_t0`

즉, 한 사람은:

- 2020 exact snapshot은 낮지만 2021에 큰 peak를 기록할 수 있고,
- post-T0 peak는 높지만 이미 2010 전에 같은 수준에 도달했을 수 있으며,
- 반대로 2020 시점에는 안정적 중견 역할이지만 장기적으로 큰 상승을 기록할 수 있다.

이 셋을 섞지 않는다.

## 7. Baseline coding workflow

### Pass 1 — T0 snapshot 100/100
원지면 role과 당시까지 직접 확인된 성취를 이용해 전원 코딩한다.

### Pass 2 — prior-peak exception audit
T0 snapshot보다 이전 peak가 더 높을 가능성이 있는 사람만 집중 검색한다.

우선 audit 대상:

- `전` 장관/의원/고위직 표기
- 은퇴/전직 선수
- 2010 이전 올림픽·세계선수권·세계랭킹 1위
- 창업 후 이미 회장/CEO를 역임하고 T0 역할이 낮아진 경우
- 대학/기관 전임 수장을 거친 경우

### Pass 3 — baseline freeze
100명 baseline peak가 완료되면 별도 freeze를 만든다.

## 8. Post-T0 peak workflow

분야별로 검색한다.

- 정치/공공: 대통령·총리·장관·정당대표·광역단체장·주요 국제기구
- 경제: 그룹 회장·CEO·산업 apex·글로벌 창업 성취
- 과학/의학: 세계 최고급 학술상, 대형 연구기관/국가 연구단 리더십, field-defining achievement
- 문화예술: 세계 최고급 영화제/아카데미/국제 예술 성취
- 스포츠: 올림픽/세계선수권 우승, 세계랭킹 1위, 세계 최상위 리그 peak
- 시민사회/교육: 주요 전국기관·국제기구 최고 리더십

## 9. 분석 Gate

Target-2020 v1.0 freeze는 이미 target-year descriptive analysis를 허용한다.

다음 항목은 baseline + post-T0 peak freeze 전에는 계산하지 않는다.

- Type A `major_leadership_precision`
- Type A `apex_precision`
- baseline-adjusted advancement rate
- `advanced / sustained_high / no_clear_advancement` 분포

또한 동아일보 2010 명단은 category 안에서 가나다순이므로 원문에 별도 순위가 없는 한 Spearman ranking accuracy는 계산하지 않는다.
