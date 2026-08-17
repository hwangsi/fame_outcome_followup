# Explicit-Horizon Type A 코딩 규칙 v0.1
## 목표연도가 명시된 미래예측형 코호트

**작성일:** 2026-08-17  
**첫 적용:** 동아일보 2010 「2020년 한국을 빛낼 대한민국 100인」

## 1. 핵심 질문

선정자가 명시한 목표연도 H에서 실제로 예측된 영향력을 보였는가?

동아 2010:
- T0 = 2010
- Target = **2020**
- Current = 2026

## 2. Roster-first

Outcome 검색 전에 T0 roster를 freeze한다.

필수:
- 100/100 membership evidence
- identity resolution
- 2010 role/affiliation
- category
- source provenance

현재 유명한 사람을 보고 과거 roster에 추가하는 것은 금지한다.

## 3. Target-year evidence window

### strict
- 2019-01-01 ~ 2021-12-31
- 직책 임기가 2020을 포함하면 `timeline_covers_2020`로 strict 인정

### broad context
- 2018 또는 2022 근거는 trajectory 설명에는 사용 가능하나 strict target outcome을 대체하지 않는다.

### 금지
- 2026 Current를 2020에 소급
- 현재 유명하므로 2020에도 성공했을 것이라는 추정

## 4. 저장 구조

```yaml
target_2020:
  active_status:
  role:
  organization:
  sector:
  scope_level:
  achievement_level:
  target_relevance:
  adverse_event:
  vital_status:
  evidence_date:
  match:
  confidence:
  sources:
```

## 5. scope_level 0–4

- 0 = meaningful role 미관찰 / 데이터 부족
- 1 = 제한적·지역적 활동
- 2 = 전국 단위 established 전문/조직 리더
- 3 = 국내 최상위권 분야/대기업/국가급 리더
- 4 = 세계적 또는 국가·산업 apex급

서로 다른 분야의 score가 동일한 사회적 가치를 뜻하지 않으며, coarse scope stratum으로만 쓴다.

## 6. 분야별 achievement 병행

### 과학/기술
world-leading research/major international prize → national research leadership → sustained high-impact scholarship → established career.

### 경제/경영
global/top national company leadership → major entrepreneurship/company scaling → sustained executive role → decline/adverse reversal.

### 문화/예술/스포츠
global top-tier recognition → national top-tier sustained influence → established professional activity → exit/decline.

### 정치/공공
president/PM/national-party apex → minister/governor/major party leadership → legislature/senior public leadership → exit/retirement.

### 사회/교육/법조/NGO
national/international institutional leadership → major policy/social impact → established professional influence.

## 7. Prediction dimensions

A. Target-year active impact  
B. Target-year scope  
C. Baseline-adjusted advancement = `scope_2020 - scope_2010`  
D. Domain achievement  
E. Adverse event  
F. Competing event(death)

## 8. Current 2026의 용도

Current는 2020 적중 여부와 분리한다.

`T0(2010) → Target(2020) → Current(2026)`

질문:
- 2020 success가 2026에도 유지됐나?
- 2020 이후 breakout/decline/reversal이 있었나?

## 9. 추천표(votes)

현재 복원된 1차 추천 상위:
- 김빛내리 23
- 이재용 19
- 안철수 18

추가 vote가 복원되면 votes와 2020 scope, advancement delta, domain achievement, top-k calibration을 분석한다. 3명만으로 ranking accuracy를 일반화하지 않는다.

## 10. Primary metrics

Roster freeze 후:
1. Target-year assessable rate
2. Target-year active-impact rate
3. Baseline-adjusted advancement distribution
4. 분야별 target-year high-impact 비율
5. adverse/reversal rate
6. 2020→2026 persistence
7. 가능한 경우 vote/rank calibration

## 11. Missingness

- `not_found`는 실패가 아니다.
- `unknown`과 `low_outcome` 분리.
- 2020 자료가 없으면 2026 자료로 대체하지 않는다.
- 웹 visibility의 직군 차이를 보고한다.

## 12. 분석 시작 gate

- [ ] T0 roster 100/100 frozen
- [ ] category totals reconcile
- [ ] 2010 baseline role 100/100 또는 explicit missing
- [ ] identity resolution complete
- [ ] source provenance stored
- [ ] outcome coding script independent from roster reconstruction script

> **명시된 미래연도가 있는 코호트에서는 ‘현재 어떻게 됐나’보다 ‘그들이 스스로 찍은 바로 그 미래시점에 실제 어떻게 됐나’를 먼저 평가한다.**
