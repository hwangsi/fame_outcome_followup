# Type-A organization outcome architecture v0.1

**작성일:** 2026-08-18  
**최초 적용:** 경향신문 2005 「한국을 이끌 60인」의 organization 3 units

## 1. 목적

Type-A 선정 기획이 사람과 조직을 함께 포함할 때 조직을 개인 career scope 0–4로 점수화하지 않는다.

경향신문 2005 원 기획은 60 selected units = 57 persons + 3 organizations 이므로 primary denominator 60은 그대로 보존한다.

조직 3개:

- NHN — 경제
- 한국공학교육인증원 — 과학기술
- 경제정의실천시민연합 — 사회교육

이 문서는 `state/coding_rules_typeA_mixed_unit_v0_1.md`의 organization 부분을 구체화한다.

## 2. 핵심 원칙

1. **person score 재사용 금지**: 개인의 baseline/post-peak scope 0–4와 organization outcome은 직접 비교하지 않는다.
2. **원 unit 보존**: 선정 당시 조직명을 원 unit로 보존하고, 이후 사명변경·합병·분할은 lineage event로 기록한다.
3. **분할 조직은 복수 successor 허용**: 하나의 조직이 둘 이상으로 분할되면 단일 후계자로 강제하지 않는다.
4. **존속만으로 성공 판정 금지**: 생존/존속과 영향력/범위는 별도 축이다.
5. **self-description 단독으로 최고등급 부여 금지**: 공식 인정, 법적 지위, 국제협약, 외부 지표 등 독립적인 구조적 근거가 없는 경우 field leadership은 보수적으로 기록한다.
6. **composite score는 v0.1에서 생성하지 않음**: 서로 다른 조직 유형(기업/시민단체/인증기관)을 하나의 숫자로 합치지 않는다.

## 3. 조직 identity와 lineage

각 organization unit는 최소 다음 필드를 가진다.

```text
organization_id
entity_key_t0
printed_name
canonical_name_t0
field
selection_date
lineage_events[]
continuity_class
successor_entities[]
```

### continuity_class

- `direct_continuity`: 동일 조직이 핵심 법적/조직적 정체성을 유지
- `renamed_continuity`: 동일 조직이 사명만 변경
- `branched_continuity`: 분할 후 둘 이상의 명확한 successor lineage 존재
- `absorbed_successor`: 원 조직은 소멸했으나 합병·흡수로 명확한 successor 존재
- `dissolved`: 활동 종료, successor 없음
- `unresolved`: 공개 근거로 판정 불가

`branched_continuity`에서는 반드시 successor를 2개 이상 기록할 수 있다.

## 4. Outcome axes

### A. survival / continuity

위 `continuity_class`로 기록한다. 이 값은 성공 점수가 아니라 조직 계보 상태다.

### B. scale / reach

선정 분야에 맞춰 다음 범주 중 하나를 기록한다.

- `local_or_niche`
- `national_specialized`
- `national_broad`
- `international_reach`
- `branched_multi_entity`
- `unclear`

기업의 매출/시가총액과 시민단체의 회원·지역조직, 인증기관의 국제협약 지위를 직접 같은 척도로 비교하지 않는다.

### C. field leadership

- `limited`
- `significant`
- `leading`
- `unclear`

`leading`은 공식 지정·국제 정회원 지위·지배적 시장/제도 역할 등 강한 근거가 있을 때만 사용한다.

### D. institutional influence

- `low_or_unclear`
- `moderate`
- `high`

근거 예:

- 정부/법정 인정기관 지정
- 국제 상호인정 협약 정회원
- 정책·산업 표준 형성 역할
- 전국적 정책 의제 설정·지속적 제도 개입
- 후계기업이 산업 인프라/플랫폼에 미치는 구조적 영향

### E. post-selection trajectory

개인 advancement와 구분되는 organization 전용 범주다.

- `expanded`: 선정 이후 범위 또는 제도적 권한/영향력이 명확히 확대
- `sustained_high`: 높은 분야 관련성을 장기간 유지하되 명확한 확장 판정은 보수적으로 유보
- `transformed_branched`: 분할·재편으로 단일 trajectory가 아닌 복수 successor로 발전
- `contracted`: 존속하나 범위/영향력이 뚜렷하게 축소
- `ceased`: successor 없이 종료
- `not_assessable`: 근거 부족

## 5. Fixed-time snapshots

가능한 경우 다음 시점을 별도로 기록한다.

- T+10: 2015 ± 1 year
- T+20: 2025 ± 1 year
- current: 2026-08-18 기준

각 snapshot에는 다음을 기록한다.

```text
snapshot_date_or_window
operational_status
continuity_class
reach
field_leadership
institutional_influence
evidence[]
confidence
```

분할 조직은 snapshot별로 successor entity를 복수 기록할 수 있다.

## 6. 2005 NHN 특수 규칙

2005 선정 unit `NHN`은 당시 네이버 포털과 한게임 등을 함께 포함한 기업이었다.

2013년 NHN은 포털사업의 네이버 주식회사와 게임사업의 NHN엔터테인먼트로 분할되었다. 네이버 측 공식 자료는 네이버를 존속법인으로 설명하며, NHN엔터테인먼트는 분할 신설법인이다. NHN엔터테인먼트는 2019년 `NHN`으로 사명을 변경했다.

따라서:

```text
continuity_class = branched_continuity
successor_entities = [NAVER Corp., NHN Corp. (former NHN Entertainment)]
```

으로 기록한다.

`2005 NHN → 현재 NAVER` 또는 `2005 NHN → 현재 NHN` 중 하나만을 유일 successor로 고정하지 않는다.

## 7. Composite outcome 금지

v0.1에서는 다음을 만들지 않는다.

- organization Major
- organization Apex
- person+organization 합산 Advanced rate
- 60-unit 전체에 대한 단일 성공률

향후 충분한 organization cohort가 쌓이면 축별 결과를 바탕으로 별도 composite의 타당성을 검토할 수 있다.

## 8. Reporting language

권장 표현:

> “경향신문 2005의 60 selected units 가운데 3개 조직은 person career scope와 다른 organization outcome architecture로 추적했다. 조직 결과는 존속·계승, 범위, 분야 리더십, 제도적 영향력, post-selection trajectory를 별도로 보고하며 개인의 Major/Apex/Advanced와 합산하지 않았다.”

## 9. 최초 QA 조건

경향 2005 organization audit v0.1은 다음을 만족해야 한다.

- organization_n = 3
- fields = 경제 / 과학기술 / 사회교육
- NHN continuity = `branched_continuity`
- 한국공학교육인증원 continuity = `direct_continuity`
- 경제정의실천시민연합 continuity = `direct_continuity`
- composite numeric score 없음
- original denominator 60 보존
