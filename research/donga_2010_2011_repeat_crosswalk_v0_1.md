# 동아일보 2010↔2011 repeat crosswalk v0.1

**작성일:** 2026-08-17  
**목적:** 2011년 동아일보가 명시한 `2010·2011 2년 연속 선정 38명`을 이용해 2010 roster를 재현 가능한 row-level evidence로 복원한다.

## 1. Primary constraints

2011-04-01 동아일보 「100인 어떻게 뽑았나」의 구조적 제약:

- 2010·2011 **2년 연속 선정: 38명**
- 그중 **경제인 14명**
- **과학자 8명**
- 나머지 문화·정치·지성 영역 합계: **16명**

2011 공식 roster 100명은 `data/typeA/donga_2011_100_roster_v0_1.json`으로 별도 고정했다.

## 2. v0.2의 row-resolved 67명과 2011 roster 교집합

기존 evidence-cleaned 2010 confirmed 67명 가운데 2011 roster에도 있는 사람은 **28명**이다.

### 과학 6
김기문, 김빛내리, 김필립, 이상엽, 임지순, 정하웅

### 문화·스포츠 4
김연아, 박진영, 봉준호, 장한나

### 지도자 4
김문수, 오세훈, 원희룡, 유시민

### 경제 11
강덕수, 김택진, 박지영, 박현주, 서정진, 이부진, 이재용, 이해진, 장하준, 정의선, 정태영

### 행동하는 지성인 3
김해성, 안철수, 조국

합계 **28/38**.

## 3. 기존 67명 밖에서 추가로 row-level 확정 가능한 5명

### 김정범
2010-06-18 동아일보 원문이 김정범 교수를 소개하면서 **지난달 본보의 ‘2020년을 빛낼 대한민국 100인’에 선정**됐다고 직접 명시한다. 2011 공식 roster의 `꿈꾸는 개척가`에도 포함된다.

- 2010 membership: **H**
- 2011 membership: official roster
- repeat status: guaranteed by both annual primary records

### 박원순
2013 동아일보 원문이 박원순에 대해 **2010, 2011년 ‘행동하는 지성인’으로 연속 선정**됐다고 정확한 연도와 category를 직접 명시한다.

- 2010 membership: **H**
- 2010 category: **행동하는 지성인, H**
- 2011 membership: official roster

### 이창용
2012 명예의 전당 20인에서 2010–2012 3년 연속 선정자로 확인된다.

- 2010 membership: **H**
- 2010 category: unresolved

### 신현송
2012 A8 명예의 전당 원지면 및 2011 primary repeat 기사로 2010 membership이 보장된다.

- 2010 membership: **H**
- 2010 category: unresolved

### 현택환
후속 동아 기사에서 김빛내리·김기문·현택환이 **2010년부터 2012년까지 3년 연속 선정**됐다고 명시한다.

- 2010 membership: **H**
- 2010 category: unresolved

## 4. 현재 재현 가능한 최소치

- 기존 row-resolved confirmed: **67**
- 신규 row-resolved outside that 67: **5**
- **row-resolved confirmed minimum: 72/100**

한편 v0.5 research log에는 aggregate confirmed가 **78/100**으로 기록돼 있으나, 67→78 증가분 11명을 모두 재현할 per-person ledger가 저장소에 남아 있지 않다.

따라서 현 시점부터 두 숫자를 분리한다.

- `legacy_aggregate_confirmed_n = 78`
- `row_resolved_confirmed_min_n = 72`
- `legacy_rows_pending_reconciliation_n = 6`

이것은 78을 철회한다는 뜻이 아니다. **78이라는 aggregate를 row-level provenance로 다시 붙이기 전까지 분석용 canonical count로 사용하지 않는다는 뜻**이다.

## 5. 2011 repeat 38명 복원 진척

- v0.2 교집합: 28
- 김정범, 박원순, 이창용, 신현송, 현택환 추가: 5
- **row-resolved repeat = 33/38**
- **remaining repeat identities = 5**

### 분야별 제약

#### 과학
- 기존 6 + 김정범 + 현택환 = **8/8**
- 따라서 **2010↔2011 과학 repeat는 완전히 닫힘**.

#### 경제
- 기존 11 + 이창용 + 신현송 = **13/14**
- 따라서 2011 경제 roster 중 **정확히 1명**이 추가 2010 repeat여야 한다.

#### 문화·지도자·지성인
- 기존 4 + 4 + 3 + 박원순 = **12/16**
- 따라서 이 세 영역에서 **4명**의 추가 repeat를 찾아야 한다.

이 구조적 제약은 후보 검색공간을 크게 줄여준다.

## 6. 코딩 원칙

1. 2011 roster에 있다는 이유만으로 2010 membership을 부여하지 않는다.
2. `2년 연속`, `2010·2011`, 또는 2010 당해 선정 원문/기관 공지가 있어야 한다.
3. 후대의 `2년 연속`이 2011–2012인지 2010–2011인지 불명확하면 사용하지 않는다.
4. 2010 category는 repeat membership보다 더 엄격하게, category까지 직접 특정한 근거가 있을 때만 고정한다.
5. 2020 target-year outcome search는 100/100 T0 roster freeze 뒤에만 시작한다.

## 7. 다음 검색 우선순위

### 경제 — 남은 1명
2011 경제 roster 중 아직 repeat로 row-resolved되지 않은 후보를 exact-year evidence로 검색한다. 후대 자료에서 2011–2012만 반복 선정된 것으로 명시되는 인물은 2010 repeat 후보에서 제외한다.

### 비경제 — 남은 4명
2011 문화·지도자·지성인 roster에서 2010 primary article, 당시 기관 공지, 정확한 연도 retrospective evidence를 우선한다.

### legacy 78 reconciliation
동시에 v0.5 aggregate에 포함됐지만 현재 canonical row ledger에 붙지 않은 **6명**을 commit history와 primary evidence로 재연결한다.

## 8. 분석 gate

현재 계산 가능한 것은 roster reconstruction progress뿐이다.

**2020 prediction precision / hit rate / calibration은 계산하지 않는다.**
