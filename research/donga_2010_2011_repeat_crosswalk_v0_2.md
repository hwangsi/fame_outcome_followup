# 동아일보 2010↔2011 repeat crosswalk v0.2

**작성일:** 2026-08-17  
**목적:** 2011 동아일보가 명시한 `2010·2011 2년 연속 선정 38명`을 row-level evidence로 재구축한다.

## v0.2 핵심 변경

2013 동아일보의 `명예의 전당 21인`은 본문에서 **통산 세 차례 선정된 사람**으로 정의된다. 따라서 2011 roster에는 있으나 2012 roster에는 없고, 2013 Hall-of-Fame에는 포함된 사람은 가능한 세 번의 선정연도가 **2010·2011·2013**으로 강제된다.

이 규칙으로 다음 2명을 새로 2010↔2011 repeat로 확정한다.

### 나경원
- 2011 official roster: `미래를 여는 지도자`
- 2012 official leader roster: 없음
- 2013 Hall-of-Fame 21: 포함
- 2013 Hall 정의: 통산 3회 선정
- 결론: 2010·2011·2013 세 번 선정 → **2010 membership H**, **2010↔2011 repeat confirmed**
- 주의: 2010 category는 직접 자료가 없으므로 미확정 유지

### 김준영
- 2011 official roster: `행동하는 지성인`
- 2012 official intellectual roster: 없음
- 2013 Hall-of-Fame 21: 포함
- 2013 Hall 정의: 통산 3회 선정
- 결론: 2010·2011·2013 세 번 선정 → **2010 membership H**, **2010↔2011 repeat confirmed**
- 주의: 2010 category는 직접 자료가 없으므로 미확정 유지

## 2013 Hall inference 사용 규칙

헤드라인의 표현보다 본문 정의인 `통산 세 차례`를 우선한다. 박원순처럼 2010·2011 선정 후 2012에는 빠졌어도 2013 Hall에 들어가는 사례가 있으므로, Hall은 반드시 `3년 연속`을 뜻하지 않는다.

따라서 Hall inference는 다음 조건을 모두 만족할 때만 쓴다.

1. 2011 official roster membership 확인
2. 2012 official roster 전체에서 부재 확인
3. 2013 Hall-of-Fame membership 확인
4. Hall이 통산 3회 선정자를 뜻한다는 first-party 정의 확인

이 네 조건을 만족하면 2013까지 가능한 세 번의 선정연도는 2010·2011·2013으로 유일하다.

## 반복선정 재구축 현황

v0.1 row-resolved repeat: **33/38**

v0.2 신규:
- 나경원
- 김준영

따라서:
- **row-resolved repeat = 35/38**
- **remaining = 3**

### 분야별
- 과학: **8/8 complete**
- 경제: **13/14**, remaining 1
- 문화·지도자·지성인 합계: **14/16**, remaining 2

## 2010 row-resolved membership 현황

- v0.2 evidence-cleaned base: 67
- 이후 별도 row evidence로 추가: 김정범, 박원순, 이창용, 신현송, 현택환, 나경원, 김준영 = 7
- **row-resolved confirmed minimum = 74/100**

legacy v0.5에는 aggregate 78/100이 기록돼 있으므로 현재 상태는:
- `legacy_aggregate_confirmed_n = 78`
- `row_resolved_confirmed_min_n = 74`
- `legacy_vs_row_resolved_gap = 4`

78을 폐기하는 것이 아니라, 남은 4개 row의 provenance를 재연결할 때까지 canonical 분석 수치로 사용하지 않는다.

## 2013 Hall로 동시에 가능한 exclusion

2011·2012·2013 모두 선정되어 2013 Hall에 들어간 것이 확인되는 사람은 2010 repeat가 될 수 없다.

예:
- 경제: 김정주, 변대규, 이미경, 이서현
- 문화: 김애란, 이자람, 하정우

이들은 2010↔2011 repeat 잔여 후보에서 제외한다.

## 남은 검색 공간

### 경제 1명
2011 경제 roster에서 아직 row-resolved되지 않았고 2011–2013 3회로 배제되지 않은 후보를 exact-year evidence로 확인한다.

### 비경제 2명
2011 문화·지도자·지성인 roster 중 아직 unresolved인 사람에 대해 2010 당해 기사, 공식기관 공지, 정확한 연도 retrospective evidence를 우선 검색한다.

## 분석 gate

**100/100 T0 roster freeze 이전에는 2020 target-year prediction metric을 계산하지 않는다.**
