# Type-A 교차 코호트 비교 v0.5

**작성일:** 2026-08-18  
**수치층:** `typeA_common_metrics_v0.4`  
**분석단위:** **255 placements / 195 canonical persons / 7 cohort units**  
**상태:** metrics layer freeze 완료. `typeA_common_master_v0.4.json` 255-row full placement materialization은 아직 pending.

## 1. v0.5 변화

경향신문 2005 「한국을 이끌 60인」의 **정치 분야 10명**을 field-specific secondary cohort로 추가했다.

원 기획은 **60 selected units = 57 persons + 3 organizations**이므로 전체 60인을 person-only master에 넣지 않았다. 정치 분야는 10개 모두 person이라 기존 Type-A 정치 scope로 독립 분석했다.

## 2. 일곱 cohort unit

| cohort | n | baseline | post-peak | Major ≥3 | Apex=4 | Advanced |
|---|---:|---:|---:|---:|---:|---:|
| 뉴스메이커 2003 정치 Top10 | 10 | 2.40 | 3.20 | 10/10 (100.0%) | 2/10 (20.0%) | 7/10 (70.0%) |
| 뉴스메이커 2003 경제 Top5 | 5 | 2.40 | 3.80 | 5/5 (100.0%) | 4/5 (80.0%) | 4/5 (80.0%) |
| 한겨레21 2004 정치 Top10 | 10 | 3.30 | 3.50 | 10/10 (100.0%) | 5/10 (50.0%) | 4/10 (40.0%) |
| 경향 2004 국회 뉴리더20 | 20 | 2.15 | 3.20 | 20/20 (100.0%) | 4/20 (20.0%) | 19/20 (95.0%) |
| 경향 2005 한국을 이끌 60인 — 정치10* | 10 | 2.60 | 3.50 | 10/10 (100.0%) | 5/10 (50.0%) | 8/10 (80.0%) |
| 동아 2010 미래100 | 100 | 2.55 | 2.83 | 71/100 (71.0%) | 12/100 (12.0%) | 28/100 (28.0%) |
| 동아 2011 미래100 | 100 | 2.67 | 3.03 | 90/100 (90.0%) | 12/100 (12.0%) | 36/100 (36.0%) |

\* 경향 2005 정치10은 전체 60-unit 프로젝트의 정치 field-specific secondary analysis다.

## 3. 2004–2005 정치 세 코호트

| | 한겨레21 2004 | 경향 2004 | 경향 2005 정치10* |
|---|---:|---:|---:|
| n | 10 | 20 | 10 |
| baseline mean | **3.30** | **2.15** | **2.60** |
| Major | 100.0% | 100.0% | 100.0% |
| Apex | 50.0% | 20.0% | 50.0% |
| Advanced | **40.0%** | **95.0%** | **80.0%** |

경향 2005 정치10은 baseline 2.60, Advanced 80%로 한겨레21 2004(3.30, 40%)와 경향 2004(2.15, 95%) 사이에 놓인다.

이 패턴은 **baseline ceiling + selection design** 가설과 방향이 맞는다. 이미 전국 최고위권이 많은 리스트는 raw Major가 높아도 추가 상승 여지가 작고, 미래 잠재력을 명시적으로 선별한 후보군은 baseline-adjusted advancement가 더 높을 수 있다.

다만 표본이 작고 동일 인물이 반복되므로 매체 효과로 해석하지 않는다.

## 4. 경향 2005 정치10 결과

- Major: **10/10 = 100%**
- Apex: **5/10 = 50%**
- Advanced: **8/10 = 80%**
- Sustained high: **2/10 = 20% — 강금실, 김근태**
- Apex: **김부겸, 박근혜, 손학규, 이명박, 정동영**

selection cutoff는 원 방법론이 작업 종료일로 밝힌 **2005-12-15**를 사용한다. 발표일 2005-12-30 사이의 15일을 no-lookahead buffer로 둔다.

## 5. Mixed-unit guardrail

경향 2005 전체 기획에는 조직 3개가 포함된다.

- NHN
- 한국공학교육인증원
- 경제정의실천시민연합

따라서 전체 프로젝트를 “57명”으로 재정의하면 안 된다. primary denominator는 **60 units**다. 조직 outcome schema가 별도로 freeze되기 전에는 전체 60-unit hit rate를 계산하지 않는다.

## 6. Common metrics v0.4

- placements: **255**
- canonical persons: **195**
- unique display names: **194**
- cohort units: **7**
- repeated persons: **50**
- placement distribution: **1회 145 / 2회 42 / 3회 6 / 4회 2**
- max placement count: **4**
- 4회 선정: **원희룡, 유시민**

Naïve pooled descriptive:

- Major: **216/255 = 84.7%**
- Apex: **44/255 = 17.3%**
- Advanced: **106/255 = 41.6%**

Person-level first selection:

- persons: **195**
- Major: **159/195 = 81.5%**
- Apex: **24/195 = 12.3%**
- Advanced: **79/195 = 40.5%**

## 7. 현재 결론

현재 자료는 다음을 가장 강하게 지지한다.

> **장기 성과는 ‘어느 언론사인가’보다 후보군의 baseline과 selection design에 크게 좌우될 가능성이 있다.**

특히 같은 2004–2005 정치 분야에서 baseline mean과 Advanced가 반대 방향으로 움직이는 양상이 보인다. 이것은 아직 인과적 증거가 아니라, 더 comparable한 코호트를 모아 검정해야 할 구조적 가설이다.

## 8. Materialization status

수치층은 frozen v0.3에 검증 완료된 정치10을 정확히 더한 additive update로 고정했다.

- frozen base: `data/typeA/typeA_common_master_v0_3.json`
- added cohort: `data/typeA/khan_2005_politics10_peak_master_v1_0.json`
- metrics: `data/typeA/typeA_common_metrics_v0_4.json`
- metrics freeze: `state/typeA_common_metrics_freeze_v0_4.json`

아직 생성하지 않은 것:

- `data/typeA/typeA_common_master_v0_4.json`
- `data/typeA/typeA_common_master_v0_4.csv`

따라서 **full placement master v0.4는 아직 frozen이라고 부르지 않는다.**

## 9. Reproducibility

- parent recovery: `research/khan_2005_korea_leaders60_recovery_v0_1.json`
- mixed-unit policy: `state/coding_rules_typeA_mixed_unit_v0_1.md`
- politics audit: `research/khan_2005_politics10_peak_audit_v0_1.json`
- politics master: `data/typeA/khan_2005_politics10_peak_master_v1_0.json`
- politics metrics: `data/typeA/khan_2005_politics10_metrics_v1_0.json`
- common metrics: `data/typeA/typeA_common_metrics_v0_4.json`
- metrics freeze: `state/typeA_common_metrics_freeze_v0_4.json`
- full-master builder: `scripts/build_typeA_common_master_v0_4.py`
