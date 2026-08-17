# Type-A canonical identity resolution policy v0.2

**작성일:** 2026-08-18  
**적용:** Type-A common master **v0.3 이후**  
**v0.2:** frozen 상태 유지, 소급 변경하지 않음

## 1. 문제

기존 common master v0.2는 `person_id = hash(name)` 방식이었다. 이 방식은 같은 한글 이름을 가진 서로 다른 사람이 새 코호트에서 등장할 때 구분할 수 없다.

실제 경향신문 2004 「17대국회 이끌 뉴리더」를 기존 common master와 대조하면서 `이미경` 충돌이 발견됐다.

- 경향신문 2004 이미경: **열린우리당 정치인·17대 국회의원 당선자**
- 동아일보 2011 이미경: **CJ E&M 총괄 부회장**

두 사람은 명백히 다른 인물이므로 display name만으로 canonical identity를 만들 수 없다.

## 2. 새 원칙

### display name

기사에 인쇄된 이름을 그대로 보존한다.

### identity key

canonical person을 식별하는 내부 키다.

기본값:

```text
identity_key = name
```

단, 동명이인으로 adjudication되면 placement별 explicit override를 사용한다.

예:

```text
이미경|cj_enm_business
이미경|politician
```

### person ID

```text
person_id = SHA256(identity_key) prefix
```

즉 v0.3부터는 이름이 아니라 identity key를 해시한다.

## 3. override selector

override는 최소 다음 세 필드로 placement를 특정한다.

```text
display_name
outlet
cohort_unit
```

현재 registry:

`data/typeA/canonical_identity_overrides_v0_1.json`

## 4. merge 규칙

같은 이름이 여러 코호트에 등장했다고 자동 merge하지 않는다.

1. contemporaneous role/domain/outlet을 대조한다.
2. 같은 사람임이 확인되면 동일 identity key를 사용한다.
3. 다른 사람이면 각 placement에 명시적 identity key override를 부여한다.
4. 판단 불가능하면 common master build를 중단한다.

## 5. 현재 경향 2004 overlap adjudication

7개 name collision 중:

### same person 6

- 김문수
- 김부겸
- 송영길
- 원희룡
- 유시민
- 천정배

### different person 1

- 이미경

근거 freeze:

`research/khan_2004_common_overlap_identity_audit_v0_1.json`

## 6. 버전 정책

`typeA_common_master_v0_2`는 당시 데이터셋에서 발견된 충돌 범위 안에서는 재현 가능한 freeze이므로 수정하지 않는다.

경향 2004를 붙이는 순간부터:

- `typeA_common_master_v0_3`
- `identity_key`
- homonym-safe `person_id`

를 사용한다.

기존 v0.2 person ID와 신규 v0.3 ID가 달라질 수 있는 동명이인 사례에는 필요 시 `legacy_person_id_v0_2`를 보존한다.

## 7. 예상 population 변화

경향신문 2004 20 placements를 추가하고 6명만 기존 person과 동일인으로 merge하면:

- placements: **225 → 245**
- unique persons: **179 → 193**

`이미경` 두 명을 잘못 merge하면 192명이 되어 QA에서 반드시 실패해야 한다.

## 8. 구현

- resolver: `scripts/identity_resolution.py`
- registry: `data/typeA/canonical_identity_overrides_v0_1.json`
- identity audit: `research/khan_2004_common_overlap_identity_audit_v0_1.json`

향후 common master builder v0.3은 이 resolver를 import하고, 모든 placement에 `identity_key`를 저장해야 한다.
