# 동아일보 Pilot v3.1 — Longitudinal transition analysis

**기준 데이터:** `outcomes_v3.json`  
**분석일:** 2026-08-17  
**대상:** 동아일보 「닮고 싶고 되고 싶은 과학기술인」 2002–2005, n=39

## 1. 핵심 결론

1. **T+10의 위상은 T+20을 강하게 예고한다.**
   - T+10 strict에서 `elite_high`였고 T+20까지 strict 추적된 인물은 20명.
   - 이 중 T+20 전 사망 1명을 제외한 19명 가운데 **14명(74%)이 `elite_high` 유지**.
   - 5명은 `established`로 내려왔으나 경력 실패라기보다 정년·명예직·활동축소가 포함된다.
   - T+10 `established` 11명 중 T+20 `elite_high`로 상승한 인물은 **1명(채연석, 9%)**.

2. **산업계는 높은 lifetime high-status 비율을 보이지만 통계적으로 확정할 수준은 아니다.**
   - 산업계: **10/12 = 83%**
   - 학술연구: **11/19 = 58%**
   - 사회문화: **5/8 = 62%**
   - 산업계 vs 비산업계 Fisher exact test: **odds ratio=3.44, p=0.269**.
   - 따라서 “산업계가 더 잘 남는다”는 **탐색적 가설**로 유지한다.

3. **분야 이동 자체는 실패 신호가 아니다.**
   - `same_field`: 16/27 high-status
   - `adjacent_field`: 6/7 high-status
   - `major_pivot`: 4/5 high-status
   - 안철수처럼 분야를 크게 옮겼어도 높은 사회적 영향력을 유지할 수 있다. `sector_transition`과 `status_trajectory`를 분리한 v3 설계가 타당하다.

4. **연령은 T+20 해석을 크게 바꾼다.**
   - birth year가 확보된 23명만의 탐색 분석이다.
   - T0 나이가 높을수록 lifetime high-status는 오히려 높지만, **T+20 시점에 `elite_high`로 남는 비율은 낮다**.
   - 이는 “선정 당시 이미 정점에 가까운 고연령 인물” + “20년 뒤 정년/은퇴”가 동시에 작동하기 때문이다.
   - 따라서 향후 언론사 간 비교에서는 **T0 age adjustment가 필수**다.

---

## 2. T+10 → T+20 strict transition matrix

두 시점 모두 strict evidence(`exact_year`, `within_window`, `timeline_covers_target`)가 있는 **33명**.

| T+10 \ T+20 | elite_high | established | adverse_reversal | deceased | 합계 |
|---|---:|---:|---:|---:|---:|
| elite_high | 14 | 5 | 0 | 1 | 20 |
| established | 1 | 10 | 0 | 0 | 11 |
| adverse_reversal | 0 | 1 | 0 | 1 | 2 |
| deceased | 0 | 0 | 0 | 0 | 0 |

### 해석
- `elite_high → elite_high`: **14명**
- `elite_high → established`: **5명**
- `elite_high → deceased`: **1명(김희준)**
- `established → elite_high`: **1명(채연석)**
- `established → established`: **10명**
- `adverse_reversal → established`: **1명(황우석)**
- `adverse_reversal → deceased`: **1명(양덕준)**

T+10 elite 생존/평가가능자에서 elite 유지율 = **14/19 = 74%**.  
T+10 established에서 T+20 elite 상승률 = **1/11 = 9%**.

---

## 3. T0 부문별 궤적

| 부문 | n | lifetime high-status | T+10 elite/strict assessable | T+20 elite/strict assessable |
|---|---:|---:|---:|---:|
| 사회문화 | 8 | 5/8 (62%) | 4/7 (57%) | 4/7 (57%) |
| 산업계 | 12 | 10/12 (83%) | 8/11 (73%) | 5/9 (56%) |
| 학술연구 | 19 | 11/19 (58%) | 9/19 (47%) | 6/16 (38%) |

### 통계적 주의
산업계 lifetime high-status를 비산업계와 비교한 2×2 Fisher exact test:
- 산업계: 10 high / 2 non-high
- 비산업계: 16 high / 11 non-high
- OR = **3.44**
- p = **0.269**

표본이 작으므로 유의한 sector effect를 주장하지 않는다.

---

## 4. 분야 이동과 lifetime status

| sector_transition | n | high-status | 비율 |
|---|---:|---:|---:|
| adjacent_field | 7 | 6 | 86% |
| major_pivot | 5 | 4 | 80% |
| same_field | 27 | 16 | 59% |

`major_pivot`이 자동으로 career decline을 의미하지 않는다는 점이 명확하다.  
향후 Type A 코호트에서도 **“무슨 분야로 이동했는가”와 “사회적/전문적 지위가 어떻게 변했는가”를 독립 변수로 유지**한다.

---

## 5. T0 age exploratory analysis

**주의: birth year가 현재 확보된 23/39명(59%)만 포함.**  
따라서 아래 수치는 완성된 age analysis가 아니라, age adjustment 필요성을 확인하기 위한 탐색 결과다.

| T0 age group | n | lifetime high-status | T+20 elite/strict career-assessable |
|---|---:|---:|---:|
| ≤51 | 10 | 5/10 (50%) | 5/8 (62%) |
| 52–55 | 6 | 4/6 (67%) | 1/4 (25%) |
| ≥56 | 7 | 6/7 (86%) | 1/5 (20%) |

### 핵심 해석
- 고연령군의 lifetime high-status가 높게 보이는 것은 **T0에서 이미 매우 높은 직위를 가진 사람을 선정**했기 때문일 가능성이 크다.
- 반대로 T+20 `elite_high`는 고연령군에서 낮아진다. 이는 20년 뒤 정년·은퇴가 구조적으로 증가하기 때문이다.
- 따라서 단순한 “20년 뒤 현직 elite 여부”만 비교하면 젊은 후보에게 유리하고 고령 후보에게 불리한 지표가 된다.
- 후속 분석에서는 `age_at_selection`, `career_stage_at_T0`, `vital_status`를 함께 모델링해야 한다.

---

## 6. v3.1에서 권장하는 다음 통계 단위

### Primary descriptive outcomes
1. T+10 level
2. T+20 level
3. T+10→T+20 transition
4. lifetime `status_trajectory`
5. `sector_transition`
6. competing event = death

### 언론사/코호트 간 비교 시
- age at T0
- T0 sector
- T0 baseline role level
- prediction-type(Type A/B/C)
를 최소 조정변수로 둔다.

---

## 7. 다음 데이터 작업

1. **2002–2003 코호트 16명의 birth year/T0 age 보완** → age-known 23/39를 39/39로 완성.
2. T+20 strict gap 5명 재탐색.
3. Type A 코호트를 별도 dataset으로 구축.
4. Type A에서는 rank/score 자체를 predictor로 보존해 `rank → future outcome` 연관을 평가.
