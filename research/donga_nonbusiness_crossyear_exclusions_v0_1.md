# 동아일보 2010↔2011 비경제 repeat — cross-year exclusion audit v0.1

**작성일:** 2026-08-17  
**목적:** 2011 공식 roster와 2012 공식 roster, 그리고 2012 명예의 전당 20/20 완전 복원본을 교차해 2010 membership이 논리적으로 불가능한 비경제 후보를 제거한다.

## 1. 적용 규칙

동아일보 2012 명예의 전당 20인은 2010·2011·2012 세 해 모두 선정된 사람들이다. 따라서 어떤 인물이:

1. 2011 공식 roster에 있고,
2. 2012 공식 roster에도 있으며,
3. 완전 복원된 2012 Hall 20에는 없다면,

그 인물은 **2010에는 선정되지 않았다.** 만약 2010에도 선정됐다면 3년 연속 선정자가 되어 Hall 20에 반드시 포함되어야 하기 때문이다.

2012 Hall 20은 원지면 판독으로 20/20 이름 복원이 완료돼 있다.

## 2. 문화·예술·스포츠에서 제외 5명

2011 official `자유로운 창조인` roster에도 있고 2012 official `자유로운 창조인` roster에도 있지만 2012 Hall 20에는 없는 사람:

- 김애란
- 이수만
- 이자람
- 장미란
- 하정우

따라서 이 5명은 **2010 membership excluded_by_crossyear**이며 2010↔2011 repeat 후보에서도 제거한다.

## 3. 행동하는 지성인에서 제외 1명

### 최재경
- 2011 official `행동하는 지성인`: 포함
- 2012 official `행동하는 지성인`: 포함
- 2012 Hall 20 complete roster: 부재

따라서 **최재경은 2010 선정자가 아니다.**

## 4. 지도자 영역

2011 unresolved 지도자 후보는:
- 김부겸
- 김태효
- 박근혜
- 이정희
- 임성남

2012 official `미래를 여는 지도자` 10명은:
권영진, 김두관, 김세연, 남경필, 문재인, 박영선, 백지아, 안희정, 이근, 정재호.

교집합이 없으므로 이번 2011+2012+Hall 규칙으로 추가 exclusion은 발생하지 않는다.

## 5. 현재 비경제 repeat 구조

기존 row-resolved 비경제 repeat: **14/16**

확정된 14명:
- 문화: 김연아, 박진영, 봉준호, 장한나
- 지도자: 김문수, 오세훈, 원희룡, 유시민, 나경원
- 지성인: 김해성, 안철수, 조국, 박원순, 김준영

남은 repeat: **정확히 2명**.

이번 audit은 positive membership을 추가하지 않으므로 repeat count는 14/16 그대로지만, false-positive 후보 6명을 제거한다.

## 6. Sources

1. 동아일보 2011 official 100-person roster — `https://www.donga.com/news/100people/2011/text_list.html`
2. 동아일보 2012 official roster — `https://www.donga.com/news/100people/2012/index.html`
3. 동아일보 2012 자유로운 창조인 — `https://www.donga.com/news/100people/2012/sub02.html`
4. 동아일보 2012 행동하는 지성인 — official 2012 roster / person pages
5. `research/donga_2012_hall_of_fame_image_resolution_v0_1.md` — 2012 Hall 20/20 original-page reconstruction

## 분석 gate

**100/100 T0 roster freeze, identity resolution, baseline/provenance 저장, category reconciliation 전에는 2020 target-year prediction metric을 계산하지 않는다.**
