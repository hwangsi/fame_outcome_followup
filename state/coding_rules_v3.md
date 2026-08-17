# Coding Rules v3 — 언론사 선정 인재 장기추적

**버전:** 3.0  
**기준일:** 2026-08-17  
**적용 코호트:** 동아일보 「닮고 싶고 되고 싶은 과학기술인」 2002–2005 (n=39)

## 1. 분석 단위

기본 단위는 `selection cohort → person → time point`이다.

각 인물은 다음 네 시점으로 추적한다.

- **T0:** 선정 당시
- **T+10:** `selection_year + 10`, 허용 창(window) ±1년
- **T+20:** `selection_year + 20`, 허용 창(window) ±1년
- **Current:** 2026-08 현재 또는 가장 최근 검증 가능한 상태

T+10/T+20은 단순히 가장 가까운 아무 자료를 끼워 넣지 않는다. 목표 시점과 자료의 관계를 `match`로 명시한다.

## 2. milestone match

- `exact_year` — 목표 연도와 동일
- `within_window` — 목표 연도 ±1년
- `timeline_covers_target` — 출처가 명시한 임기/재직기간이 목표연도를 실제로 포함
- `nearest_outside_window` — 가장 가까운 자료이지만 ±1년 밖. 보조(broad) 근거로만 사용
- `not_observed` — 신뢰할 만한 해당 시점 자료를 확보하지 못함

### Strict coverage

`exact_year | within_window | timeline_covers_target`만 포함한다.

### Broad coverage

Strict coverage + `nearest_outside_window`.

`nearest_outside_window` 자료는 시점별 핵심 비율의 분모에 넣지 않는다.

## 3. point-specific career level

T+10/T+20 각 시점은 다음 중 하나로 코딩한다.

### `elite_high`
당시에도 국가·분야·대형기관/기업 차원의 상위 리더십 또는 이에 준하는 학술·사회적 영향력이 확인됨.

예:
- 대학 총장/국가 연구기관장
- 대기업·주요 기술기업 최고경영자
- 국회의원·장관급 역할
- 해당 분야에서 국제·국가급 최고 수준 연구자/리더십

### `established`
전문직·연구·경영·명예직 활동은 안정적으로 지속되지만, 해당 시점의 자료만으로 `elite_high`를 부여할 수준의 상위 리더십을 확인하지 못함.

은퇴·명예교수 자체는 하락을 뜻하지 않는다.

### `adverse_reversal`
중대한 연구윤리/법적 사건, 건강 사건, 사업 붕괴 등으로 T0 대비 현저한 경력 반전이 해당 시점에 관찰됨.

원인은 별도 note에 기록한다. 건강 문제와 비위는 동일 의미로 취급하지 않는다.

### `deceased`
목표 시점 이전에 사망. **경력 실패가 아닌 competing event**다.

### `unknown`
시점 판정에 필요한 자료가 부족함.

## 4. sector

시점별 활동 분야는 다음으로 기록한다.

- `same_field`
- `adjacent_field`
- `major_pivot`
- `unknown`
- `not_applicable`

분야 이동은 성공/실패 또는 지위 상승/하락과 독립적으로 취급한다.

## 5. Current의 변수

Current는 기존 v2.1 구조를 유지한다.

- `vital_status`
- `current_status`
- `status_trajectory`
- `sector_transition`
- `trace_status`
- `confidence`

`status_trajectory`와 `sector_transition`을 다시 하나의 outcome으로 합치지 않는다.

## 6. 날짜

- `checked_at` = 조사/감사 수행일
- `evidence_date` = Current 판정에 사용한 가장 최근 핵심 근거의 실제 시점
- `t10.evidence_date`, `t20.evidence_date` = 각 milestone의 근거 시점

`checked_at`을 `evidence_date`처럼 사용하지 않는다.

## 7. confidence

### H
- 공식 기관/공시/학회 등 강한 출처가 직접 지위를 확인하거나,
- 독립적인 신뢰 가능한 출처가 다수 일치하고 identity가 명확

### M
- 동일인·경력선은 충분히 확실하나,
- 출처가 단일 언론/참고자료이거나 시점이 다소 간접적

### L
- 가장 가까운 자료만 존재하거나,
- 시점/역할을 완전히 확정하지 못함

## 8. longitudinal aggregate

### 8.1 Current verification coverage
`trace_status == verified_current` 비율.

### 8.2 Lifetime high-status trajectory
T0/T+10/T+20/Current를 종합하여 기존 `status_trajectory`가
`upward_expansion | sustained_high`인 비율.

이는 **“2026년 현재 엘리트 비율”도, “언론 예측 성공률”도 아니다.**

### 8.3 T+10 / T+20 point elite-high proportion
Strict coverage 중 `deceased`와 `unknown`을 제외하고,
해당 시점 `level == elite_high`의 비율.

이 지표는 연령·은퇴·사망의 영향을 받기 때문에 T+10과 T+20의 단순 차이를 ‘쇠퇴율’로 해석하지 않는다.

## 9. 사망

사망은 다음 두 정보를 동시에 유지한다.

- `vital_status = deceased`
- 생전 `status_trajectory`

T+20 이전 사망자는 T+20 point-status에서 `deceased`로 코딩하고 career-level 비율 분모에서 제외한다.

## 10. 검색 실패

- 기사 없음 ≠ 은퇴
- 부고 없음 ≠ 생존
- 현직 페이지 없음 ≠ 실패
- 과거의 높은 직함 ≠ 현재의 높은 직함

찾지 못한 것은 `unknown/not_observed`로 남긴다.

## 11. 동명이인/identity resolution

최소 2–3개의 식별자가 이어져야 확정한다.

- 생년/나이
- T0 기관
- 전공
- 학력
- 대표 업적
- 직무 경력의 연속성
- 한자명

v3에서 이조원은 2004 T0 원문과 2019 KAIST 공식 경력(테라급나노소자개발사업단장 → 한양대 나노융합과학과 → 나노종합기술원장)이 연속되어 `confirmed`로 승격한다.

## 12. 해석 원칙

이 코호트는 **Type B 역할모델형**이다. 선정 당시 이미 성취한 인물을 고른 것이므로:

- “언론 예측 성공률”을 산출하지 않는다.
- 핵심 질문은 **장기 지위 유지, 역할 변화, 분야 전환, 평판 내구성**이다.
- 향후 Type A 미래예측형 코호트와 비교할 때만 prediction accuracy를 별도로 설계한다.
