# 박인출 2010 membership recovery v0.1

**작성일:** 2026-08-17  
**결론:** 2010 동아일보 「2020년 대한민국을 빛낼 100인」 membership을 **M-confirmed**로 복귀시키고, 2010 category는 **도전하는 경제인**으로 확정.

## 1. 왜 다시 검증했나

v0.2 evidence-cleaned 단계에서 박인출은 secondary/pending으로 남아 있었다. 이후 legacy v0.5에서는 pending 명단에서 박인출이 빠졌고, 동시에 `도전하는 경제인` confirmed count가 16→17로 1 증가했으나 row-level provenance가 보존되지 않았다.

따라서 legacy aggregate의 `경제인 +1` 슬롯을 재검증했다.

## 2. 동시대 근거

### 의학신문 — 2010-05-11
박인출 메디파트너 대표를 동아일보가 기획한 `2020년 대한민국을 빛낼 100인`에 선정했다고 직접 보도. 의료계 인사로는 유일하며, **도전하는 경제인 25인 중 한 명**이라고 구체적으로 명시한다.

Source: https://www.bosa.co.kr/news/articleView.html?idxno=152582

### 덴탈투데이 — 2010-05-10
메디파트너 측 발표를 인용해 박인출 대표가 동아일보 100인에 선정됐고 **도전하는 경제인 25인 중 한 명**이라고 동시대에 보도.

Source: https://www.dttoday.com/news/articleView.html?idxno=47876

### 의약뉴스 — 2010-05-11
동일 선정 사실과 category를 별도 전문매체가 동시대에 보도.

Source: https://www.newsmp.com/news/articleView.html?idxno=69250

## 3. Evidence coding

- membership: **confirmed**
- confidence: **M**
- evidence class: `contemporaneous_specialist_media`
- category_2010: **도전하는 경제인**
- T0 role: 메디파트너㈜ 대표 / 예치과 네트워크 대표의사

현재 evidence hierarchy에서 동시대 전문매체가 선정 사실과 category를 구체적으로 보도한 경우 M으로 인정한다. 이 자료들은 현재 유명세나 후대 biography가 아니라 2010년 5월 당시의 동시대 보도다.

## 4. Legacy reconciliation

v0.2 → v0.5 변화:
- `도전하는 경제인`: 16 → 17 (**+1**)
- v0.2 pending에 있던 박인출은 v0.5 pending에서 제외됨

따라서 provenance가 소실됐던 legacy `경제인 1명`은 박인출 행으로 reconciliation하는 것이 version history와 새 근거 모두에 일치한다.

## 5. Count impact

이전 canonical union: **76/100**  
박인출 복귀: **+1**  
새 canonical row-resolved: **77/100**

legacy unresolved records는 4 → **3**:
- 윤명철 1
- 행동하는 지성인 2

## 6. 분석 gate

아직 roster freeze 아님. 100/100 membership 및 category totals reconciliation 이전에는 2020 target-year prediction metric을 계산하지 않는다.
