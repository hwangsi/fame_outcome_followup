# 언론사 선정 인재 추적 — Fame Outcome Follow-up

**기준일:** 2026-08-17  
**현재 단계:** 동아일보 Type B Pilot v3.1 완료 + 뉴스메이커 2003 Type A v0.3 분석

## 1. 동아일보 Pilot — Type B 역할모델형

**코호트:** 동아일보 「닮고 싶고 되고 싶은 과학기술인」 2002–2005, n=39

- 추적축: `T0 → T+10(±1년) → T+20(±1년) → Current`
- Current verified: **29/39 = 74%**
- T+10 strict: **37/39 = 95%**
- T+20 strict: **34/39 = 87%**
- High-status lifetime trajectory: **26/39 = 67%**

이 코호트는 당시 이미 성취한 역할모델을 선정한 Type B이므로 이 비율은 “언론 예측 성공률”이 아니다.

### v3.1 longitudinal analysis

- T+10 `elite_high`였고 T+20까지 평가 가능한 생존자: **14/19 = 74%가 elite 유지**
- T+10 `established` → T+20 `elite_high`: **1/11 = 9%**
- 산업계 lifetime high-status: **10/12 = 83%**
- 학술연구: **11/19 = 58%**
- 사회문화: **5/8 = 62%**
- 산업계 vs 비산업계 Fisher exact: **OR 3.44, p=0.269** → 탐색적 가설 수준

연령이 확인된 23명 분석에서는 T0 고연령군일수록 lifetime high-status는 높지만 T+20 현역 elite 비율은 낮아, 향후 언론사 간 비교에 **age/career-stage adjustment가 필수**임을 확인했다.

## 2. Phase 2 — Type A 미래예측형

### 뉴스메이커 2003 「차세대 리더 정치·경제」 v0.3

- 발행: **2003-05-30**
- 질문: “앞으로 정치·경제 분야를 이끌어갈 차세대 리더”
- 한길리서치, 오피니언 리더 100명
- 교수 50 / 기자 30 / 시민단체 간부 20
- 3명 중복 선택

### T0 복원

**정치 Top10**
1. 정동영 43%
2. 김근태 33%
3. 손학규 28%
4. 유시민 20%
5. 강금실 18%
6. 추미애·권영길 공동
8. 이부영
9. 천정배·강재섭 공동

**경제 Top5**
1. 안철수 39%
2. 장하성 32%
3. 강철규 29%
4. 정운찬 28%
5. 이재용 19%

경제 원문에는 조학국·변양호·이재웅·진대제·장하준도 등장하지만 정확한 6–10위 원순위/지목률은 공개 텍스트에서 복원하지 못했다. 정치 6–10위 지목률도 미복원 상태로 유지하며 임의 추정하지 않는다.

### v0.3 핵심 결과

Type A는 세 가지를 분리한다.

1. **Selection precision** — 후보군을 잘 골랐는가?
2. **Ranking accuracy** — 순위가 미래 성취 순서를 맞혔는가?
3. **Baseline-adjusted advancement** — 선정 당시 이미 높았던 지위를 감안해도 더 상승했는가?

현재 ranked sample:

| 지표 | 정치 Top10 | 경제 Top5 |
|---|---:|---:|
| post-T0 major leadership | **10/10 (100%)** | **5/5 (100%)** |
| post-T0 apex | 2/10 (20%) | 4/5 (80%) |
| baseline-adjusted advanced | **7/10 (70%)** | **4/5 (80%)** |

**Ranking accuracy**
- Rank vs post-T0 peak: 정치 ρ=-0.306 (p=0.389), 경제 ρ=0.000 (p=1.000)
- Rank vs 실제 상승폭 `advancement_delta`: **정치 ρ=-0.094 (p=0.796), 경제 ρ=-0.224 (p=0.718)**

> **현재의 핵심 해석: 후보군 자체는 매우 잘 골랐지만, 후보군 내부의 순위가 누가 더 크게 성장할지를 예측하지는 못했다.**

raw 100%를 “언론 예측 성공률 100%”라고 부르지 않는다. 손학규·강금실·권영길·강철규·정운찬 등은 T0에서 이미 높은 직위에 있었으므로, 미래예측에는 baseline-adjusted advancement가 더 중요하다.

## 3. Repository structure

```text
README.md
report_2026-08-17_v3.md

analysis/
  analysis_v3_1.md
  typeA_newsmaker_2003_v0_2.md
  typeA_newsmaker_2003_v0_3.md

research/
  phase2_typeA_candidates.md

state/
  coding_rules_v3.md
  coding_rules_typeA_v0_1.md

scripts/
  gen_report_v3.py
  analyze_v3_1.py
  analyze_typeA_newsmaker_2003.py

data/
  typeA/
    newsmaker_2003_t0_partial.json
    newsmaker_2003_outcomes_v0_2.json
    newsmaker_2003_outcomes_v0_3.json

artifacts/
  v3_bundle.tar.xz
```

## 4. 다음 작업

1. 뉴스메이커 정치 6–10위 T0 profile을 동시대 자료로 추가 검증해 baseline confidence 승격
2. 경제 6–10위 원지면/표 확보 시 Top10으로 확장
3. **한겨레21 1999 차세대 리더** 전체 31명 원표 확보 시도
4. 신동아 1998 ‘정치부 기자가 뽑은 차세대 정치인’ 전체 순위 복원 시도
5. 두 번째 Type A 코호트 확보 후 outlet 간 `selection precision / ranking accuracy / baseline-adjusted advancement` 비교
