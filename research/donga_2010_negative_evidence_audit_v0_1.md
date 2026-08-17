# 동아일보 2010 negative-evidence audit v0.1

**작성일:** 2026-08-17  
**목적:** secondary list나 불완전한 retrospective 문구 때문에 2010 roster 후보로 잘못 재유입될 수 있는 인물을, 연도 구조를 보장하는 first-party evidence로 명시적으로 제외한다.

## 1. 손열음 — 2010 membership에서 제외

### Evidence chain

1. **2011 공식 동아일보 100인 roster에 손열음이 없다.**
2. **2012 공식 동아일보 roster에는 손열음이 `자유로운 창조인`으로 포함된다.**
3. **2014 동아일보는 손열음을 그해 새로 명예의 전당에 오른 10명 중 한 명으로 명시한다.** 같은 기사에서 명예의 전당은 `통산 3번 선정`된 인물이라고 정의한다.
4. 후대 동아일보 프로필은 손열음이 `한국을 빛낼 100인에 3년 연속 선정`됐다고 명시한다.

### Logical resolution

- 2011에는 선정되지 않았고,
- 2012에는 선정됐으며,
- 2014 시점에는 통산 3회 선정 및 `3년 연속` 조건을 만족한다.

따라서 가능한 연속 3개 선정연도는 **2012·2013·2014**로 유일하다.

**결론:** 손열음은 2010 선정자가 아니다.

### Coding

- `membership_2010 = excluded`
- `reason = exact-year sequence contradiction`
- `confidence = H`
- 2010 candidate-generation pending list에서 제거

이 결론은 과거 중간작업에서 연도 미특정 `3년 연속 선정` 문구를 2010–2012로 해석했던 추론을 최종적으로 닫는다.

## 2. 양윤선 — 2010↔2011 repeat 후보에서 제외

### Evidence chain

1. **2011 공식 동아일보 roster에 양윤선이 `도전하는 경제인`으로 포함된다.**
2. **2013 동아일보 100인 기사에서 양윤선은 해당 연도 선정자로 다뤄진다.**
3. **2014 동아일보는 양윤선을 그해 새로 명예의 전당에 오른 인물로 명시하고, 명예의 전당을 통산 3회 선정자로 정의한다.**

### Logical resolution

2014까지 양윤선의 통산 3회 선정은 2011·2013·2014로 이미 채워진다. 따라서 2010까지 선정됐다면 2014 시점 통산 선정 횟수가 4회가 되어 명예의 전당 정의와 모순된다.

**결론:** 양윤선은 2010↔2011 repeat가 아니다.

### Coding

- `repeat_2010_2011 = excluded`
- `confidence = H`
- business repeat unresolved candidate set에서 제거

## 3. 분석상 의미

Negative evidence는 canonical 2010 roster의 confirmed count를 증가시키지 않는다. 대신 후보공간을 줄이고 잘못된 secondary-source contamination을 방지한다.

현재 영향:

- canonical 2010 row-resolved roster: **77/100 유지**
- 2010↔2011 repeat: **35/38 유지**
- business repeat unresolved candidate count: **8 → 7**
- 2010 pending candidate-generation list에서 손열음 제거

## 4. Guardrail

- `absence`만으로 사람을 제외하지 않는다.
- 공식 연도별 roster, 통산 횟수, 연속선정 문구가 함께 연도 조합을 유일하게 만들 때만 negative resolution을 확정한다.
- secondary copied list와 충돌할 경우 first-party exact-year evidence를 우선한다.
- 2020 outcome이나 2026 현재 상태는 T0 membership 추론에 사용하지 않는다.
