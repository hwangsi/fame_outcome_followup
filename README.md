# 언론사 선정 인재 추적 — 동아일보 Pilot v3

**기준일:** 2026-08-17  
**코호트:** 동아일보 「닮고 싶고 되고 싶은 과학기술인」 2002–2005, n=39  
**버전:** v3.0

## v3 핵심

- 추적축을 `T0 → T+10(±1년) → T+20(±1년) → Current`로 확장.
- 각 T+10/T+20 시점에 `observed_role`, `level`, `sector`, `evidence_date`, `match`, `confidence`, `sources` 저장.
- strict evidence = `exact_year | within_window | timeline_covers_target`.
- Current의 `status_trajectory`와 `sector_transition`을 분리 유지.
- 사망은 career failure가 아니라 competing event로 처리.

## 최종 coverage

- Current verified: **29/39 = 74%**
- T+10 strict: **37/39 = 95%**
- T+10 broad: **39/39 = 100%**
- T+20 strict: **34/39 = 87%**
- T+20 broad: **36/39 = 92%**
- High-status lifetime trajectory: **26/39 = 67%**, Wilson 95% CI **51–79%**

## 시점별 elite-high

- T+10: **21/37 = 57%** (strict career-assessable), Wilson 95% CI **41–71%**
- T+20: **15/32 = 47%** (strict career-assessable; 사망 2 제외), Wilson 95% CI **31–64%**

이 비율은 예측 성공률이 아니다. 이 코호트는 당시 이미 성취한 역할모델을 선정한 Type B 코호트이므로, 시점별 지위의 지속/전환을 기술하는 지표로 사용한다.

## 남은 strict gap

- T+10: 박성래, 백우현
- T+20: 박완철, 문대원, 이조원, 홍지준, 백우현

## 이번 최종 정정

- 유향숙: 유명희의 대통령실 미래전략기획관 경력이 잘못 붙은 오류 제거. 2012·2022 한국생명공학연구원 명예연구원 활동으로 교정.
- 유명희(1954, 분자생물학자): 2013 대통령실 미래전략기획관, 2023 마크로젠 사외이사, 2026 사외이사/감사위원 선임 확인.
- 이재웅: `쏘카 창업자` 표현 제거. 쏘카 원 창업자는 김지만이며, 이재웅은 초기 투자자·후일 대표·2026 이사회 의장/COO로 구분.
- 손욱: 2023 차세대 CTO 초청강연과 2025 공개기고로 T+20 및 Current 보강.
- 문대원: 한국진공학회 공식 임원자료로 T+10 strict window 보강.
- 장순근: 2022 「남극 그리고 네번의 겨울」 자료로 T+20 exact-year 보강.
- 장인순: 2026 연합뉴스 직접 인터뷰를 T+20(2025±1) 근거로 반영.

## 파일

- `scripts/build_v3.py` — v2.1 JSON을 읽어 v3 JSON을 생성
- `scripts/gen_report_v3.py` — v3 JSON에서 상세 MD와 최종 보고서 자동 생성
- `state/coding_rules_v3.md` — milestone 및 longitudinal coding 규칙
- `data/outcomes_v3.json` — 분석용 원데이터
- `state/outcomes_v3.md` — 39명 상세 근거
- `report_2026-08-17_v3.md` — 메인 결과 보고서
- `data/outcomes_v2_1.json` — build 재현에 필요한 source dataset
