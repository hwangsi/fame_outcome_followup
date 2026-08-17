# 언론사 선정 인재 추적 — Fame Outcome Follow-up

**기준일:** 2026-08-17  
**현재 단계:** 동아일보 Type B Pilot v3.1 분석 완료 + Phase 2 Type A 코호트 착수

## 1. 동아일보 Pilot v3

**코호트:** 동아일보 「닮고 싶고 되고 싶은 과학기술인」 2002–2005, n=39

- 추적축: `T0 → T+10(±1년) → T+20(±1년) → Current`
- Current verified: **29/39 = 74%**
- T+10 strict: **37/39 = 95%**
- T+20 strict: **34/39 = 87%**
- High-status lifetime trajectory: **26/39 = 67%**

이 코호트는 당시 이미 성취한 역할모델을 선정한 Type B이므로 이 비율은 “언론 예측 성공률”이 아니다.

### v3.1 longitudinal analysis

T+10과 T+20 모두 strict evidence가 있는 33명의 전이행렬을 추가 분석했다.

- T+10 `elite_high`였고 T+20까지 평가 가능한 생존자: **14/19 = 74%가 elite 유지**
- T+10 `established` → T+20 `elite_high`: **1/11 = 9%**
- 산업계 lifetime high-status: **10/12 = 83%**
- 학술연구: **11/19 = 58%**
- 사회문화: **5/8 = 62%**
- 산업계 vs 비산업계 Fisher exact: **OR 3.44, p=0.269** → 탐색적 가설 수준

연령이 확인된 23명 분석에서는 T0 고연령군일수록 lifetime high-status는 높지만 T+20 현역 elite 비율은 낮아, 향후 언론사 간 비교에 **age/career-stage adjustment가 필수**임을 확인했다.

## 2. Phase 2 — Type A 미래예측형 코호트

실제 prediction accuracy를 평가할 수 있는 미래예측형 기획을 별도 코호트로 구축한다.

### 첫 구축 대상: 뉴스메이커 2003 「차세대 리더 정치·경제」

- 발행: **2003-05-30**
- 질문: “앞으로 정치·경제 분야를 이끌어갈 차세대 리더”
- 한길리서치, 오피니언 리더 100명
- 교수 50 / 기자 30 / 시민단체 간부 20
- 3명 중복 선택

현재 복원:

**정치 Top 10 순위**
1. 정동영 43%
2. 김근태 33%
3. 손학규 28%
4. 유시민 20%
5. 강금실 18%
6. 추미애·권영길 공동
8. 이부영
9. 천정배·강재섭 공동

**경제 Top 5 순위·점수**
1. 안철수 39%
2. 장하성 32%
3. 강철규 29%
4. 정운찬 28%
5. 이재용 19%

경제 분야는 조학국·변양호·이재웅·진대제·장하준도 원문에서 언급되지만, 정확한 전체 순위가 복원될 때까지 임의 순위를 부여하지 않는다.

### 다른 Type A 후보

- 한겨레21 1999 차세대 리더 조사 — 전체 31명 원표 확보 필요
- 신동아 1998 정치부 기자 100명 ‘차세대 정치인’ — 전체 순위 원문 확보 필요
- 시사저널 차세대 리더 시리즈 — 방법론 benchmark

## 3. Repository structure

```text
README.md
report_2026-08-17_v3.md

analysis/
  analysis_v3_1.md

phase2/
  phase2_typeA_candidates.md
  typeA_newsmaker_2003_t0_partial.md
  typeA_newsmaker_2003_t0_partial.json

data/
  outcomes_v3.json.xz

state/
  coding_rules_v3.md

scripts/
  gen_report_v3.py
  analyze_v3_1.py

artifacts/
  v3_bundle.tar.xz
```

`data/outcomes_v3.json.xz`는 전체 39명 v3 JSON의 xz 압축본이다. `scripts/analyze_v3_1.py`는 raw JSON 또는 이 압축본을 직접 읽는다.

전체 v3 원본 스냅샷은 `artifacts/v3_bundle.tar.xz`에도 보존되어 있다.

```bash
tar -xJf artifacts/v3_bundle.tar.xz
```

## 4. 다음 작업

1. 뉴스메이커 2003 정치/경제 ranked core의 **T+10(2013), T+20(2023), Current(2026)** outcome 코딩
2. 경제 전체 Top10 정확 순위/score 복원
3. 정치 6~10위 score 복원
4. Type A `Top-k precision`, rank–outcome association 계산
5. 동아일보 2002–2003 코호트의 누락 birth year 보완 → age-adjusted analysis 완성
