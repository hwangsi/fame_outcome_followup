# Type-A mixed person / organization selection policy v0.1

**작성일:** 2026-08-18  
**최초 적용 사례:** 경향신문 2005 「한국을 이끌 60인」

## 1. 문제

일부 언론 선정 기획은 개인만 뽑지 않는다. 경향신문 2005 「한국을 이끌 60인」은 6개 분야별 10개, 총 60개 선정 단위 가운데:

- person: **57**
- organization: **3**

을 포함한다.

조직 3개:

- NHN
- 한국공학교육인증원
- 경제정의실천시민연합

기존 Type-A common master는 개인의 career scope를 추적하는 person/placement schema이므로 조직을 같은 점수 규칙으로 넣을 수 없다.

## 2. 원 설계 보존 원칙

원 선정의 primary denominator는 반드시 **60 selected units**로 보존한다.

다음은 금지한다.

- 조직 3개를 조용히 제거하고 “57명 선정”이라고 재정의
- person career scope를 조직에 적용
- 조직의 존속만으로 개인의 Major/Advanced와 동일한 hit를 부여
- person-only 분석 결과를 원 60-unit 전체의 성과로 표현

## 3. unit_type

모든 mixed selection row는 최소 다음을 가진다.

```text
unit_type = person | organization
printed_name
canonical_name
field
source
```

개인은 기존 identity architecture를 사용한다.

조직은 향후 별도 `entity_key` / `organization_id`를 사용한다.

## 4. Person secondary analysis

57명의 개인 subset은 **사전에 명시된 secondary analysis**로 추적할 수 있다.

표현 예:

> “원 기획은 60 selected units(57 persons + 3 organizations)이었다. 아래 결과는 person-only 57-unit secondary analysis다.”

원 분모 60을 숨기지 않는다.

## 5. Field-specific analysis

각 분야는 원 설계에서 정확히 10개씩 선정된 완결된 stratum이다.

따라서 다음 조건에서는 field-specific secondary cohort로 분석할 수 있다.

1. 해당 field의 10개 unit가 모두 동일 unit_type이거나,
2. mixed field라면 unit type을 분리한 결과임을 명시하고 primary field denominator 10을 보존한다.

### 경향 2005 정치10

정치 분야 10개는 모두 person이므로 기존 Type-A person scope로 별도 분석 가능하다.

cohort unit 후보:

`khan_2005_korea_leaders60_politics10`

단, 이는 전체 60인의 결과가 아니라 **정치 field-specific secondary analysis**다.

## 6. Organization outcome architecture — 향후 별도 정의

조직은 최소 다음 축으로 추적해야 한다.

- survival / continuity
- scale / reach
- field leadership
- institutional influence
- merger / renaming / successor status
- dissolution / absorption

개인의 `pre-selection lifetime peak → post-selection career peak`와 동일한 score 0–4를 그대로 재사용하지 않는다.

조직용 scope rule이 freeze되기 전에는 세 조직을 `outcome_pending_schema`로 둔다.

## 7. Identity

person unit는 `identity_key → person_id`를 사용한다.

특히:

- 경향 2005 대중문화 `이미경/CJ부회장`은 `이미경|cj_enm_business`
- 경향 2004 정치인 이미경은 `이미경|politician`

으로 구분한다.

`비`는 printed name을 보존하되 canonical person name은 `정지훈`, identity anchor는 `가수 비(Rain)`로 둔다.

## 8. QA

경향 2005 recovery가 통과하려면:

- selected units = 60
- fields = 6
- each field = 10
- person = 57
- organization = 3
- organization set = NHN / 경제정의실천시민연합 / 한국공학교육인증원
- politics = 10 persons

이어야 한다.

## 9. 버전 정책

기존 Type-A common master v0.3은 person-only freeze 상태로 유지한다.

경향 2005 전체 60-unit를 common architecture에 넣으려면 person master와 별개인 mixed-unit layer를 새로 설계한다.

정치10처럼 완결된 all-person field를 추가하는 경우에는 기존 person-only common master의 다음 버전에 placement로 추가할 수 있지만 `parent_selection = khan_2005_korea_leaders60`와 `field_secondary = true`를 반드시 보존한다.
