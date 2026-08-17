# 동아일보 2010 legacy 78 reconciliation v0.2

**작성일:** 2026-08-17  
**상태:** v0.1 superseded — 독립적인 두 복원 트랙의 합집합을 반영

## 핵심 정정

`row-resolved confirmed` 수치는 하나의 순차적인 72→74 경로가 아니라, 서로 독립적인 두 복원 트랙을 합쳐 계산해야 한다.

### 기준점
- v0.7 canonical row-resolved: **72/100**

### 트랙 A — 2013 Hall 논리로 2010 membership 복원
- **나경원**
- **김준영**

두 사람은 2011 공식 roster에 있고 2012 roster에는 없으며, 2013 동아일보의 `통산 세 차례 선정` 명예의 전당에 포함됐다. 따라서 가능한 선정연도는 2010·2011·2013으로 유일하다.

→ **+2, 74/100**

### 트랙 B — 2010 first-party evidence로 legacy row 복원
- **김용** — 2010-07-28 동아일보 Donga NewsBook 2 기사에서 100인 선정자로 직접 취급
- **이상훈** — 2010-05-10 동아일보 최초 기획 기사에서 선정된 100인의 다짐 사례로 직접 인용

→ **+2, union canonical = 76/100**

## 현재 authoritative count

- **canonical row-resolved membership: 76/100**
- **full-roster remaining slots: 24**

과거 `legacy aggregate 78`은 그대로 historical audit value로 보존하지만 canonical count가 아니다.

## legacy 78에서 아직 provenance가 재연결되지 않은 4 records

v0.5 category delta를 이용한 구조적 reconciliation상 남은 것은 다음 4개다.

1. **윤명철** — category unknown; secondary biography에서는 선정 사실이 반복되지만 first-party corroboration 대기
2. **도전하는 경제인 1명** — 이름/근거 미연결
3. **행동하는 지성인 1명** — 이름/근거 미연결
4. **행동하는 지성인 1명** — 이름/근거 미연결

주의: 나경원·김준영은 이 legacy 4개와 별개의 2011/2013 repeat reconstruction 트랙에서 복원된 행이다. 따라서 `78-76=2`처럼 단순 차감해 legacy unresolved 수를 계산하면 안 된다.

## 2011 repeat reconstruction과의 관계

현재 2010↔2011 repeat는 **35/38** row-resolved.
- 경제: 13/14 → **1명 남음**
- 과학: 8/8 complete
- 문화·지도자·지성 합계: 14/16 → **2명 남음**

legacy의 `경제 1 + 지성 2`와 repeat 잔여 `경제 1 + 비경제 2`가 겹칠 가능성이 높아, 두 문제를 교차 검증하는 것이 가장 효율적이다. 단, 동일인이라고 추정해서는 안 되고 exact-year evidence로 확인해야 한다.

## 다음 우선순위

1. 2011 repeat 남은 3명 exact-year evidence 확인
2. 신지애 등 2010 secondary-copy + 2011 official roster 교집합 후보의 first-party/official 2010 근거 확보
3. 윤명철 first-party corroboration
4. 2010 A1/A4 원지면 또는 DNB 2 full roster 복원
5. membership 100/100 이후 category reconciliation

## Gate

**100/100 T0 roster freeze 및 category 합계 20/25/20/25/10 reconciliation 이전에는 2020 target-year prediction metric을 계산하지 않는다.**
