# 중앙일보 2003–2006 comparable Type-A cohort — archive packet v0.1

- 기준일: **2026-08-18**
- 상태: **web 검색에서 아직 승격 가능한 cohort 미발견 / BIG Kinds 직접검색 우선**
- 목적: 정치·경제 분야의 `차세대 / 미래 / 뉴리더` 선정 기획 중 roster와 selection mechanism이 모두 복원되는 cohort 탐색

## 1. 왜 중앙일보는 BIG Kinds가 우선인가

BIG Kinds 공식 수집정보에 따르면 중앙일보는:

- **1990-01-01 ~ 현재**
- 수집 누락기간: **없음**

으로 제공된다.

따라서 2003–2006 중앙일보 검색은 일반 웹 색인보다 BIG Kinds 내부 DB가 훨씬 유리하다.

공식 coverage:

`https://www.bigkinds.or.kr/v2/intro/news.do`

## 2. 1차 검색 기간

`2003-01-01 ~ 2006-12-31`

## 3. Query groups

### Group A — 정치 future-potential

- `차세대 리더`
- `차세대 지도자`
- `미래 지도자`
- `미래 리더`
- `뉴리더`
- `젊은 리더`

보조어:

- 정치
- 국회
- 당선자
- 전문가
- 선정
- 설문
- 투표
- 후보

### Group B — 경제/전문경영인

- `차세대 CEO`
- `차세대 경영인`
- `차세대 리더 전문경영인`
- `미래 CEO`
- `젊은 경영인`
- `뉴리더 기업`

보조어:

- 전문가 선정
- CEO 설문
- 경영인 설문
- 후보군
- 순위

## 4. 승격 기준

검색 결과가 다음을 만족해야 recovery cohort로 승격한다.

1. selection date가 고정 가능
2. 선정된 이름 roster를 finite denominator로 복원 가능
3. 미래/차세대/잠재력 질문이 명확
4. candidate frame 또는 selector를 파악 가능
5. 가능하면 rank/vote/score 존재

## 5. 제외 기준

다음은 Type-A comparable cohort로 넣지 않는다.

- 단순 대선후보 지지도·당선가능성 조사
- WEF 등 외부기관이 선정하고 중앙일보가 보도만 한 리스트
- 기업 내부 인사에서 회사가 자체적으로 '차세대 리더'라고 부른 사례
- 특정 인물 한 명을 '차세대 리더'라고 묘사한 프로필
- roster denominator가 없는 연재형 소개기사

## 6. 현재 일반 웹검색 결과

현재까지 2003–2005 정치 분야에서 경향신문 2004처럼:

- 명단
- 선정법
- 미래리더 질문

세 가지가 동시에 확인되는 중앙일보 기획은 일반 웹 인덱스에서 찾지 못했다.

이는 `없음`을 의미하지 않는다. 중앙일보가 BIG Kinds에서 1990년부터 완전 수록되므로 **archive-search problem**으로 분류한다.

## 7. 다음 처리

BIG Kinds 검색 결과에서 후보 기사가 나오면:

```text
article_date
article_title
selection_question
candidate_pool
selector
selected_n
names
rank/score
source_record_id
```

를 recovery JSON으로 만들고, 원문 확인 후에만 Type-A common master 후보로 승격한다.
