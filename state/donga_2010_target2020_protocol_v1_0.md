# 동아일보 2010 → target year 2020 코딩 프로토콜 v1.0

**작성일:** 2026-08-18  
**적용 코호트:** 동아일보 2010 「2020년 한국을 빛낼 100인」  
**상위 규칙:** `state/coding_rules_typeA_v0_1.md`

## 1. 목적

이 코호트는 선정 시점(2010)에 목표연도 **2020년**을 명시한 explicit-horizon 예측 코호트다. 따라서 일반적인 T+10 근사치보다 **2020년 그 시점의 실제 역할**을 우선 평가한다.

## 2. Target snapshot 규칙

- primary target year: **2020**
- admissible evidence window: **2019-01-01 ~ 2021-12-31**
- 우선순위:
  1. 2020년 직접 증거가 있으면 `exact_year`
  2. 2020 직접 증거가 없을 때만 2019 또는 2021의 가장 가까운 증거를 `nearest_within_window`로 사용
  3. ±1년 증거를 2020 exact snapshot으로 둔갑시키지 않는다.
- 2021년에 더 높은 직위에 올랐더라도 2020 direct evidence가 있으면 **2020 score를 2021 peak로 대체하지 않는다.**
- 필요하면 `within_window_followup` 또는 `window_peak`를 별도 필드에 저장한다.

## 3. Outcome score

`scope_score`는 `coding_rules_typeA_v0_1.md`의 0–4 leadership scope를 따른다.

- 0: 자료 부족/의미 있는 역할 미확인
- 1: 지역·제한적 역할 또는 은퇴 후 제한적 활동
- 2: 전국 단위의 안정적 전문·정치·경영 역할
- 3: 주요 국가·정당·대기업 리더십
- 4: 국가·산업 apex급

이 점수는 사회적 가치의 절대척도가 아니라 분야를 가로질러 대략적인 **scope stratum**을 보기 위한 서열척도다.

## 4. T0 baseline과 분리

- T0 membership/category/role/age/sex는 원지면 캡처 전사본을 canonical baseline으로 사용한다.
- 2020 target snapshot은 T0 역할과 별도로 코딩한다.
- `post_T0 career peak`와 `target2020`을 분리한다.
- 목표연도 이전에 이미 더 높은 직위에 올랐다가 2020에 내려온 경우도 2020 snapshot 자체를 기록한다.

## 5. Evidence rule

각 row는 최소 다음을 가진다.

- `target2020.role`
- `target2020.scope_score`
- `target2020.sector`
- `target2020.evidence_date`
- `target2020.match`
- `target2020.confidence`
- `target2020.source_notes`
- `target2020.source_urls`

가능한 경우 정부·국회·대학·기관 공식자료 또는 주요 통신사/신문의 contemporaneous source를 우선한다. 개인 홈페이지, 후대 약력, 검색 스니펫만으로는 exact-year role을 확정하지 않는다.

## 6. Competing events / uncertainty

- 사망은 예측 실패가 아니라 `competing_event`로 기록한다.
- 은퇴·분야 전환은 자동 실패가 아니다.
- 동일 이름 또는 경력 연결이 불명확하면 outcome score를 억지로 채우지 않고 `pending_identity_resolution`로 남긴다.
- 2019–2021 창 밖의 자료는 identity/timeline 보조 증거로만 사용하며 target score의 직접 근거로 쓰지 않는다.

## 7. 분석 Gate

전체 코호트 metric은 다음 조건이 충족된 뒤 계산한다.

1. 100/100 target row 생성
2. identity audit 완료
3. exact/nearest/pending 구분 저장
4. category별 coverage 보고
5. unresolved row를 별도 표기

부분 batch에서는 **coverage와 unresolved 수만 보고**하고 selection precision/평균 score 등 전체 metric을 조기 계산하지 않는다.
