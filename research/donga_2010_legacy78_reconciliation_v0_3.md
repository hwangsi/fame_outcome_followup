# 동아일보 2010 legacy 78 reconciliation v0.3

**작성일:** 2026-08-17  
**상태:** v0.2 superseded — 박인출 provenance 복구 반영

## 1. 현재 canonical 상태

독립적인 row-level evidence를 합집합으로 계산한 현재 2010 membership은 **77/100**이다.

- v0.7 canonical baseline: 72
- 2011/2013 exact-year logic: 나경원, 김준영 → +2
- 2010 first-party Donga: 김용, 이상훈 → +2
- 2010 contemporaneous specialist media: 박인출 → +1
- **canonical union = 77/100**

과거 v0.5의 `78/100`은 historical aggregate audit value이며 canonical 분석 수치로 사용하지 않는다.

## 2. 박인출이 legacy 경제 +1 슬롯을 설명하는 이유

v0.2 evidence-cleaned 상태에서는 박인출이 pending 6명 중 하나였다. 이후 v0.5에서:

- pending 목록에서 박인출이 제외됐고
- `도전하는 경제인` confirmed count가 16 → 17로 정확히 +1 증가했다.

이번 재검증에서 2010년 5월의 의학신문·덴탈투데이·의약뉴스가 모두 박인출 메디파트너 대표의 동아일보 100인 선정 사실과 `도전하는 경제인 25인 중 한 명`이라는 category를 구체적으로 보도한 것을 확인했다.

따라서 provenance가 저장되지 않았던 legacy `도전하는 경제인 +1` record는 **박인출**로 reconciliation한다.

Evidence coding:
- membership: confirmed
- confidence: M
- evidence class: contemporaneous specialist media
- 2010 category: 도전하는 경제인

## 3. legacy aggregate에서 아직 provenance 미연결인 3 records

v0.5 category delta와 이미 복원된 행을 대조하면 남은 provenance-loss는 정확히 다음 세 슬롯이다.

1. **윤명철** — category unknown; 후대 biography는 존재하나 first-party corroboration 대기
2. **행동하는 지성인 1명** — 이름 미확정
3. **행동하는 지성인 1명** — 이름 미확정

이 세 record는 `legacy aggregate 78`의 내부 감사 문제이며, 숫자 78과 현재 canonical 77의 단순 차이로 해석하지 않는다. 나경원·김준영처럼 별도의 복원 트랙에서 추가된 행이 있기 때문이다.

## 4. 2011 repeat 문제와의 교차점

2010·2011 두 해 연속 선정자는 동아일보가 총 38명으로 명시했다. 현재 row-level로 35/38을 복원했다.

남은 구조:
- 경제: 1명
- 문화·지도자·지성 합계: 2명

legacy에서 미연결인 `행동하는 지성인 2명`과 repeat에서 남은 `비경제 2명`이 동일한 두 사람일 가능성이 있으므로 가장 먼저 교차 검증한다. 단, 구조적 일치만으로 같은 사람이라고 코딩하지 않고 exact-year/contemporaneous evidence가 필요하다.

## 5. 다음 검색

1. legacy 행동하는 지성인 2명 × 2011 nonbusiness repeat 2명 교차검색
2. 2011 경제 repeat 마지막 1명
3. 윤명철 first-party corroboration
4. 신지애 2010 first-party/official evidence
5. 원지면 A1/A4 또는 DNB2 full roster 회수

## 6. Gate

현재 **77/100은 분석 가능한 partial roster일 뿐 frozen cohort가 아니다.** 정확한 100/100 membership, category totals 20/25/20/25/10, identity, baseline, provenance가 모두 확정된 뒤에만 2020 target-year outcome coding을 시작한다.
