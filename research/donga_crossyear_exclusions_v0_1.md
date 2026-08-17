# 동아일보 2010 cohort — cross-year exclusion audit v0.1

**작성일:** 2026-08-17  
**목적:** 2011–2014 동아일보 공식 선정/명예의전당 기록을 조합해 2010 membership이 논리적으로 불가능한 후보를 제거한다.

## 원칙

이 audit은 이름을 2010 roster에 **추가**하기 위한 것이 아니라, 후대 연도별 기록이 만들어내는 조합 제약을 이용해 false-positive 후보를 **제외**하기 위한 것이다.

- 2011 official roster membership만으로 2010을 소급하지 않는다.
- 2014 명예의전당은 동아일보 본문이 `통산 3번 선정`된 사람이라고 정의한다.
- 연도 조합이 유일할 때만 exclusion/inference를 허용한다.

## 1. 양윤선 — 2010 membership 제외

### 확인된 연도
- **2011:** 동아일보 공식 100인 roster `도전하는 경제인`에 양윤선 포함.
- **2012:** 동아일보 공식 `도전하는 경제인` 25명 전체 roster에 양윤선 없음.
- **2013:** 동아일보 본문이 양윤선을 그해 선정된 100인의 대표 사례로 직접 소개.
- **2014:** 동아일보가 `통산 3번 선정`되어 명예의전당에 오른 10명 중 양윤선을 직접 열거.

### 논리
2014 시점의 총 선정 횟수는 정확히 3회다. 이미 2011과 2013이 확정되고, 2012는 공식 전체 roster에서 제외되어 있으므로 세 번째 선정은 2014다.

따라서 양윤선의 선정연도는 **2011, 2013, 2014**로 강제되며, **2010에는 선정되지 않았다.**

### 결과
- `2010 membership = excluded_by_crossyear`
- 2010↔2011 경제 repeat 후보에서 제거.
- 기존 경제 마지막-1 후보군: 8명 → **7명**

잔여 후보:
`권구훈, 김가영, 김남구, 손병두, 정용진, 최태원, 황철주`

## 2. 손열음 — 2010 membership 제외

### 확인된 연도/제약
- **2011:** 저장소에 고정된 동아일보 공식 2011 roster 100명 전체에 손열음 없음.
- **2012:** 동아일보 공식 `자유로운 창조인` roster에 손열음 포함.
- **2014:** 동아일보가 `통산 3번 선정`되어 명예의전당에 오른 10명 중 손열음을 직접 열거.
- **2016 동아일보:** 손열음이 동아일보 선정 `한국을 빛낼 100인`에 **3년 연속** 선정됐다고 명시.

### 논리
이 기획은 2010년에 시작됐고, 손열음은 2011 roster에 없다. 2012에는 선정됐으며 2014 시점까지 통산 3회, 후대 동아일보는 이 세 번이 연속이었다고 명시한다.

따라서 가능한 연속 3개년은 **2012, 2013, 2014**뿐이다. 즉 **2010 선정자는 아니다.**

### 결과
- `2010 membership = excluded_by_crossyear`
- 과거 `pending_secondary_2010` 후보에서 제거.
- 2010 자유로운 창조인 secondary reconstruction에 손열음이 없다는 사실과도 일치.

## 3. 현 상태에 미치는 영향

- canonical confirmed roster: **77/100 유지**
- remaining to exact 100: **23 유지**
- 2010↔2011 repeat row-resolved: **35/38 유지**
- 경제 repeat 미해결 후보: **8 → 7**
- pending candidate-generation list에서 손열음 제거

숫자가 늘어난 것은 아니지만, 두 false-positive 경로를 닫아 이후 검색공간을 줄였다.

## 4. Sources

1. 동아일보 2011 official roster: `https://www.donga.com/news/100people/2011/text_list.html`
2. 동아일보 2012 official roster: `https://www.donga.com/news/100people/2012/index.html`
3. 동아일보 2012 business roster: `https://www.donga.com/news/100people/2012/sub04.html`
4. 동아일보 2012 creative roster: `https://www.donga.com/news/100people/2012/sub02.html`
5. 동아일보 2013-04-02 「“한계는 없다”… 실패도 즐기며 달려온 100개의 꿈」
6. 동아일보 2014-04-03 「카리스마는 가라… 미래 리더는 소통-공감하는 양치기형」
7. 동아일보 2016-11-10 「‘단짝’ 주미 강-손열음, 듀오앨범 내고 콘서트」

## 분석 gate

**100/100 T0 roster freeze와 category reconciliation 전에는 2020 target-year prediction metric을 계산하지 않는다.**
