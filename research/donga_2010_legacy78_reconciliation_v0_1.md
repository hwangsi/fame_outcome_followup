# 동아일보 2010 legacy 78 aggregate → row-level reconciliation v0.1

**작성일:** 2026-08-17  
**목적:** 과거 작업에서 `confirmed 78/100`으로 기록됐으나 개인별 provenance가 완전히 보존되지 않은 6개 membership을 구조적으로 재구성하고, 재검증된 행만 canonical roster로 복귀시킨다.

## 1. 출발점

현재 증거가 행 단위로 확인된 canonical minimum은 **72/100**이다. 과거 v0.5/v0.6에는 aggregate로 **78/100**이 기록되어 있어 6개의 차이가 남아 있었다.

v0.2 evidence-cleaned 67명과 v0.5 category count를 비교하면 추가된 11개 membership의 category delta는 다음과 같다.

- 도전하는 경제인: +1
- 꿈꾸는 개척가: +1
- 행동하는 지성인: +3
- category unknown: +6

이 가운데 이후 row-level provenance가 다시 붙은 5명은:

- 김정범 — 꿈꾸는 개척가
- 박원순 — 행동하는 지성인
- 이창용 — category unknown
- 신현송 — category unknown
- 현택환 — category unknown

따라서 남은 legacy 6개는 구조적으로 정확히 다음과 같이 환원된다.

1. **김용** — category unknown
2. **윤명철** — category unknown
3. **이상훈** — category unknown
4. **도전하는 경제인 1명** — 이름/근거 미연결
5. **행동하는 지성인 2명** — 이름/근거 미연결

## 2. 이번 재검증

### 김용 — canonical 복귀

**근거:** 동아일보 2010-07-28 「동아뉴스북 2호 ‘대한민국 100인’ 출시」.

해당 기사는 DNB 2호가 ‘2020년을 빛낼 대한민국 100인’을 다룬다고 설명하고, `100인으로 선정된 인물`의 콘텐츠를 소개한 뒤 김용 미국 다트머스대 총장의 경우 이메일 답변을 받지 못해 과거 총장 취임 인터뷰 PDF를 삽입했다고 직접 설명한다. 따라서 동아일보 자체 2010 자료가 김용을 cohort member로 명시적으로 다룬 것으로 판정한다.

- evidence class: **H / primary Donga 2010**
- membership: **confirmed**
- 2010 category: **unknown 유지**
- source: https://www.donga.com/news/article/all/20100728/30156411/1

### 이상훈 — canonical 복귀

**근거:** 동아일보 2010-05-10 「10년후 대한민국을 빛낼 100인입니다」.

최초 선정 기획 본문에서 `서울대 이상훈 교수`의 발언을 100인의 다짐 사례로 직접 인용한다. 기사 문맥은 동아일보가 선정한 100인을 소개하는 본문이며, 따라서 membership을 직접 보장한다.

- evidence class: **H / primary Donga 2010**
- membership: **confirmed**
- 2010 category: **unknown 유지**
- source: https://www.donga.com/news/Society/article/all/20100510/28213859/1

### 윤명철 — 아직 canonical 미복귀

후대 서점 저자 프로필과 교육/문화 자료에서 `동아일보 창간 90주년 2020년 한국을 빛낼 100인 선정`이 반복 확인된다. 그러나 현재 evidence policy상 secondary biography만으로 frozen roster에 넣지 않는다.

- status: **probable / pending first-party corroboration**
- examples:
  - https://ebook-product.kyobobook.co.kr/dig/epd/ebook/E000003440598
  - https://www.kcef.kr/19786/

## 3. reconciliation 결과

- 이전 row-resolved canonical minimum: **72/100**
- 이번 신규 row-resolved: **+2**
- 새 canonical minimum: **74/100**
- legacy aggregate 78 중 아직 provenance 미연결: **4명**
  - 윤명철 1명
  - 도전하는 경제인 이름 미확정 1명
  - 행동하는 지성인 이름 미확정 2명

**중요:** legacy `78`이라는 숫자 자체를 canonical denominator로 사용하지 않는다. 78은 historical aggregate이며, 현재 분석에는 evidence-backed row-resolved count인 74만 사용한다.

## 4. 다음 액션

1. 윤명철의 2010 동아 원문/동국대 당시 공지/동아뉴스북 인물 페이지 확보
2. 2011 2년 연속 38명 중 남은 `경제 1명` 확인 — legacy 경제 1명과 동일인일 가능성 우선 검증
3. 2011 repeat의 남은 비경제 4명 중 `행동하는 지성인` 후보를 검증 — legacy 지성인 2명과 교차 가능성 검증
4. 2010 A1/A4 원지면 또는 DNB 2호 원본 회수

## 원칙

현재 유명세나 2020/2026 outcome을 이용해 T0 membership을 역추정하지 않는다. 2010 membership을 직접 보장하는 contemporaneous/official/retrospective-exact evidence만 canonical roster에 반영한다.
