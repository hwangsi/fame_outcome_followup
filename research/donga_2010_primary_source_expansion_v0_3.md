# 동아일보 2010 primary-source expansion audit v0.3

**작성일:** 2026-08-18  
**Supersedes:** `research/donga_2010_primary_source_expansion_v0_2.md`  
**목적:** 2010 「2020년 한국을 빛낼 100인」 exact roster 78→100 복원을 위한 원지면·DNB·개인별 provenance 회수 경로를 고정한다.

## 1. 현재 canonical 상태

- canonical membership: **78/100**
- remaining: **22**
- canonical change in this audit: **0**
- 2020 target-year outcome coding gate: 유지

근거 규칙은 그대로 유지한다. secondary copied list나 후대 profile만으로 canonical membership을 올리지 않는다.

## 2. 2010-05-10 A1/A4 원지면 asset endpoint 확보

동아디지털아카이브의 2010-05-10 지면 페이지에서 A1 및 A4의 `지면보기` 링크를 추적해 실제 이미지 asset endpoint를 확인했다.

Archive date page:
- https://www.donga.com/archive/newslibrary/view?ymd=20100510

A1 500px derivative:
- https://dimg.donga.com/a/500/0/90/5/PDF_EXT/NEWS/2010/05/10/2010051045A01010101.jpg

A4 500px derivative:
- https://dimg.donga.com/a/500/0/90/5/PDF_EXT/NEWS/2010/05/10/2010051045A04040101.jpg

의미:
- 원지면의 파일명/경로 패턴까지 확보됨.
- 500px 파생본은 roster 표 판독에 충분하지 않다.
- 다음 단계는 동일 source object의 고해상도 derivative 또는 원본 PDF/JPEG variant를 회수하는 것이다.

이 경로는 2010-05-12 동아일보 정정기사에서 A1/A4의 100인 표 존재가 독립적으로 확인된다는 기존 audit과 일치한다.

## 3. Donga NewsBook 2 구조 확인

동아일보 first-party 보도에서 두 번째 `동아뉴스북(DNB)`의 주제가 **「2020년을 빛낼 대한민국 100인」**임을 확인했다.

확인된 구조:
- 총 **146쪽**
- 선정자 100명의 성장과정·역할모델·삶의 원칙 등을 수록
- category main screen에서 인물 사진을 클릭해 individual profile page로 이동하는 구조
- 선정자 심층 인터뷰 동영상 포함
- 당시 `dnb.donga.com`, `dongabiz.com`을 통한 배포 경로 존재

따라서 DNB2는 100인 exact roster와 category mapping을 한 번에 복원할 수 있는 최우선 primary-source target이다.

검색상 현재 공개된 원파일/미러는 아직 회수하지 못했다.

## 4. 자유로운 창조인 missing 3 — 상태 재확인

2011년 secondary copied transcription의 자유로운 창조인 20명과 canonical 78을 비교하면 missing은 정확히:

- **김윤진**
- **신지애**
- **이청용**

이다.

이 secondary list는 후보 생성에만 사용한다.

### 신지애
- 2011 동아일보 공식 선정 코호트 membership은 first-party confirmed.
- 2010 copied list에도 존재.
- 따라서 2010↔2011 unresolved nonbusiness repeat의 강한 후보지만, 2010 qualifying evidence는 아직 확보되지 않음.

### 김윤진 / 이청용
- 2010 copied list에 존재.
- 이번 검색에서도 2010 동아 원문 또는 당시 소속기관의 direct selection notice는 아직 찾지 못함.
- canonical 승격 보류.

## 5. 윤명철 secondary corroboration 강화

윤명철은 여러 후대 저자/기관 프로필에서 동아일보 창간 90주년 `2020년 한국을 빛낼 100인` 선정 경력이 반복 확인된다.

추가 확인된 명시적 연도 자료:
- OMI Global 저자 프로필: 수상내역에 `2010 동아일보 2020년 한국을 빛낼 100인 선정`이라고 연도를 직접 기재.
- 교보/YES24 등 저자 프로필에서도 동아일보 창간 90주년 선정 경력을 반복 기재.

대표 source:
- https://www.omiglobal.net/entry/오미글로벌-저자-윤명철

판정:
- `strong_secondary_corroboration` 유지
- predefined evidence hierarchy상 2010 동아 first-party 또는 2010 당시 소속기관 공식 공지가 아니므로 canonical 승격은 아직 하지 않음.

## 6. Official methodology 재검증

2010-05-10 동아일보 A4 원문에서 다음을 다시 확인했다.

- 99명 편집부 선정 + 독자선정 1명
- 후보 355명
- 추천위원 205명
- 5대 category: 20/25/20/25/10
- 추천 상위: 김빛내리 23, 이재용 19, 안철수 18
- 최종 명단에 오세훈·김문수·유시민·송영길 등 당시 지방선거 출마자 포함

Source:
- https://www.donga.com/news/article/all/20100510/28213739/1

## 7. 이번 라운드 검색에서 얻은 것과 얻지 못한 것

### 얻은 것
1. A1/A4 **exact image asset filenames/endpoints**
2. DNB2 **146-page primary-source 구조**와 배포 경로
3. 윤명철의 **2010 year-explicit secondary corroboration** 추가
4. 신지애·김윤진·이청용 direct 2010 evidence가 아직 검색 인덱스에서 노출되지 않는다는 사실 재확인

### 아직 못 얻은 것
1. A1/A4 고해상도 원지면
2. DNB2 원파일 또는 살아 있는 profile archive
3. 김윤진·신지애·이청용의 qualifying 2010 row evidence
4. 윤명철의 qualifying 2010 first-party/institutional evidence
5. 2010↔2011 repeat 잔여 3명 확정

## 8. 다음 공격 순서

1. A1/A4 asset의 고해상도 derivative/original endpoint 변형 탐색
2. DNB2 파일명·CDN·old dnb.donga.com/dongabiz.com mirror/archive 탐색
3. 신지애 2010 exact-year marker 집중 검색
4. 김윤진·이청용 2010 당시 소속기관/에이전시/협회 자료 검색
5. 윤명철 2010 동국대 또는 당시 공식 프로필 검색
6. 경제 repeat 후보 6명에 대해 2010 exact selection marker 검색

## 9. Acceptance rule

> No person enters the canonical frozen roster without row-level evidence guaranteeing 2010 selection under the predefined hierarchy.

따라서 현재 canonical은 **78/100**으로 유지한다.
