# 동아일보 2010 legacy 78 → row-level provenance reconciliation v0.1

**작성일:** 2026-08-17  
**목적:** 과거 v0.5에 aggregate `78/100 confirmed`로만 남은 상태를 이름별 evidence ledger로 다시 연결한다.

## 신규 reconciliation: 박인출

### Evidence
2010-05-11 의학신문은 박인출 메디파트너 대표가 동아일보 창간 90주년 기획 `2020년 대한민국을 빛낼 100인`에 선정됐다고 보도했고, **`도전하는 경제인` 분야 25인 중 한 명**이라고 구체적으로 명시했다.

Source:
- 의학신문, 2010-05-11, 「박인출 대표, '2020년 한국을 빛낼 100인' 선정」
- https://www.bosa.co.kr/news/articleView.html?idxno=152582

### Coding
- 2010 membership: **confirmed**
- evidence type: `contemporaneous_professional_media_2010`
- evidence grade: **M**
- 2010 category: **도전하는 경제인**
- category evidence grade: **M**

이 판단은 v0.5 evidence rule 4, 즉 `동시대 전문매체가 선정 및 카테고리를 구체적으로 보도 → M`에 정확히 해당한다.

## Reproducibility count

직전 row-resolved minimum: **74/100**

박인출 추가 후:
- **row_resolved_confirmed_min_n = 75/100**
- `legacy_aggregate_confirmed_n = 78/100`
- `legacy_vs_row_resolved_gap = 3`

즉 legacy 78 중 이제 **3개 row만 provenance 재연결이 남았다.**

## Pending secondary candidates

박인출은 pending에서 제거한다. 현재 secondary-only/pending 후보는:
- 김윤진
- 서도호
- 손열음
- 신지애
- 이청용

이 명단은 `2010 roster에 없다`는 뜻이 아니라, 현재 canonical freeze 기준을 통과하는 row-level evidence가 아직 저장되지 않았다는 뜻이다.

## 다음 액션

1. 김윤진·서도호·신지애·이청용의 2010 기관/전문매체/동아 원문 exact selection evidence 탐색
2. legacy 78 gap 3명의 identity를 commit history 및 원자료로 재연결
3. 2010 A1/A4 원지면의 고해상도 99인 표 회수 병행
4. 100/100 freeze 전에는 2020 outcome metric 계산 금지
