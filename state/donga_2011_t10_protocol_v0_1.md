# 동아일보 2011 T+10 longitudinal protocol v0.1

**작성일:** 2026-08-18  
**적용 코호트:** 동아일보 2011 「10년 뒤 한국을 빛낼 100인」  
**상위 규칙:** `state/coding_rules_typeA_longitudinal_v0_1.md`

## 1. 목적

2011 선정 시점에서 일반적 T+10 fixed-window persistence를 평가한다.

- center year: **2021**
- admissible window: **2020-01-01 ~ 2022-12-31**
- primary question: 2021±1년에 실제로 어떤 역할을 점유했는가?

이 outcome은 lifetime post-selection peak와 분리한다.

## 2. Snapshot priority

1. 2021 직접 증거가 있으면 `exact_year`
2. 2021 직접 증거가 없을 때만 2020 또는 2022의 가장 가까운 증거를 `nearest_within_window`로 사용
3. window 밖의 더 높은 직위는 snapshot score를 대체하지 않는다
4. window 내 여러 증거가 있을 때는 가장 직접적이고 contemporaneous한 역할 증거를 우선한다

## 3. Required fields

각 person/unit snapshot은 최소 다음을 가진다.

- `snapshot_id`
- `window_id = t10`
- `target_year = 2021`
- `window_start = 2020-01-01`
- `window_end = 2022-12-31`
- `status`
- `role_at_window`
- `scope_score`
- `scope_label`
- `evidence_date`
- `match`
- `confidence`
- `evidence_refs`
- `coding_note`

## 4. Allowed status

- `assessable`
- `competing_event`
- `untraceable`
- `not_applicable`

Death before/during the window is `competing_event` and is not coded as ordinary failure.

## 5. Derived metrics

Among assessable persons:

- Scope ≥2
- Major at T+10 = scope ≥3
- Apex at T+10 = scope =4

Always report original N, assessable N, competing-event N, and untraceable N.

## 6. Guardrails

- do not copy lifetime peak into T+10 score
- do not use post-2022 roles to raise a 2021±1 snapshot
- preserve identity resolution from the frozen 2011 cohort
- preserve repeat/new placement identity but do not treat repeated persons as independent in person-level pooled analyses
- do not compare numerically with Dong-A 2010 until both cohorts use harmonized window semantics and denominator rules

## 7. Source priority

Prefer, in order:

1. government/parliament/court/university/company/institution official records
2. major contemporaneous news reports
3. authoritative professional or organizational biographies tied to the target window

Later retrospective biographies may support identity/timeline continuity but should not override stronger contemporaneous window evidence.

## 8. Next implementation step

Create a 100-row T+10 master from the frozen Dong-A 2011 roster and T0 identity layer, then calculate window-specific metrics after coverage QA reaches 100/100 outcome paths.
