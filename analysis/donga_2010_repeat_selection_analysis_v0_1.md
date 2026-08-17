# 동아일보 2010↔2011 반복선정 효과 분석 v0.1

**작성일:** 2026-08-18  
**분석대상:** 2010년 선정자 100명  
**Exposure:** 2011년 공식 100인 명단에 다시 선정되었는가  
**반복선정:** 38명 / **2010 단회선정:** 62명

## 1. 핵심 결과

2010년에 선정된 뒤 2011년에도 다시 선정된 38명은 장기 career peak만 놓고 보면 단회선정 62명보다 매우 강한 성과를 보였다.

| 지표 | 2년 연속 38명 | 2010-only 62명 | 차이 | RR | Fisher p |
|---|---:|---:|---:|---:|---:|
| Post-T0 scope≥3 | **35/38 (92.1%)** | **36/62 (58.1%)** | **+34.0%p** | 1.586 | 0.000223 |
| Apex=4 | **9/38 (23.7%)** | **3/62 (4.8%)** | **+18.8%p** | 4.895 | 0.00885 |
| Baseline 초과 상승 | **11/38 (28.9%)** | **17/62 (27.4%)** | **+1.5%p** | 1.056 | 1.000 |

표면적으로는 반복선정이 매우 강한 신호다. 2년 연속 선정자의 92.1%가 이후 scope 3 이상에 도달 또는 유지했고, apex 비율도 23.7%로 단회선정자의 4.8%보다 훨씬 높다.

하지만 **실제로 선정 당시까지의 개인 최고 career scope를 넘어선 비율은 28.9% vs 27.4%로 거의 동일하다.**

## 2. 왜 이런 차이가 생겼는가: baseline imbalance

반복선정군은 애초에 2010 시점 이전부터 훨씬 높은 수준에 있던 사람들이었다.

- 반복선정군 baseline scope≥3: **30/38 = 78.9%**
- 단회선정군 baseline scope≥3: **23/62 = 37.1%**
- 차이: **+41.9%p**
- RR: **2.13**
- Fisher p: **6.84×10⁻⁵**

평균 baseline peak 역시:

- 반복선정: **2.87**
- 단회선정: **2.35**

이었다.

따라서 반복선정군의 높은 장기 major/apex 성과는 상당 부분 **이미 2010년에 검증된 강자를 2011년에 다시 고른 효과**로 설명될 가능성이 크다.

## 3. 가장 중요한 해석

이 결과는 반복선정을 두 종류의 신호로 분리해야 함을 보여준다.

### Absolute attainment signal

> “두 번 선정된 사람은 이후에도 큰 인물이 되는가?”

그렇다. 92.1%가 post-T0 scope≥3이고, 23.7%가 apex에 도달했다. 반복선정은 장기적으로 높은 위치를 유지하거나 도달할 사람을 식별하는 데 매우 강한 **status/quality marker**다.

### Incremental growth signal

> “두 번 선정하면, 한 번 선정된 사람보다 그 이후 더 크게 성장할 사람을 추가로 골라내는가?”

현재 coarse 0–4 scale에서는 거의 그렇지 않다. baseline을 넘어선 상승은 **28.9% vs 27.4%**로 사실상 같다.

따라서 현재 가장 적절한 표현은 다음과 같다.

> **2년 연속 선정은 미래의 추가 상승을 예측하는 신호라기보다, 이미 높은 수준에 도달한 인물을 편집진이 다시 확인하는 강한 elite-persistence signal로 보인다.**

## 4. 이 분석이 중요한 이유

2010 단일 코호트에서 이미 `major attainment 71%`와 `baseline-adjusted advancement 28%` 사이에 큰 차이가 있었다. 반복선정 분석은 그 차이의 원인을 더 명확하게 보여준다.

반복선정자들은:

- baseline부터 훨씬 높았고,
- 이후 major/apex 비율도 훨씬 높았지만,
- **자신의 선정 전 최고 수준을 넘어서는 추가 상승률은 단회선정자와 거의 같았다.**

즉 언론의 반복선정은 “앞으로 더 성장할 사람”보다 **“이미 강하고 앞으로도 강할 가능성이 높은 사람”**에 더 민감했을 가능성이 있다.

## 5. 중요한 제한점

첫째, 2011 재선정은 2010 선정 약 1년 뒤에 일어난다. 따라서 2010년 5월 이후 2011년 재선정 전까지 발생한 초기 성취가 재선정에 반영됐을 수 있다. 즉 repeat status는 완전히 ex-ante인 예측변수가 아니며 **reverse causation** 가능성이 있다.

둘째, 반복선정군과 단회선정군은 baseline이 크게 다르므로 단순 비율 비교는 인과적으로 해석할 수 없다.

셋째, 0–4 scope는 coarse ordinal scale이므로 같은 score 3 안에서도 실제로 큰 성장이나 영향력 차이가 존재할 수 있다.

넷째, 표본이 38 vs 62로 크지 않으며 분야별로 나누면 더 작아진다. p-value는 exploratory descriptive statistic으로만 사용한다.

## 6. 다음 분석

이제 가장 중요한 다음 질문은 **같은 baseline stratum 안에서도 반복선정 효과가 남는가**이다.

예를 들어 baseline=2인 사람끼리 비교해:

- repeat-selected가 더 자주 scope≥3으로 올라가는지
- advancement>0이 더 높은지

를 봐야 한다.

마찬가지로 baseline=3 안에서는:

- apex=4 진입률이 반복선정에서 더 높은지

를 비교하는 것이 의미 있다.

그 다음에는 분야(category)를 동시에 고려한 stratified analysis 또는 matched analysis로 넘어가야 한다.

## 7. Reproducibility

- 2010 final outcome: `data/typeA/donga_2010_post_t0_peak_master_v1_2.json` (builder-generated)
- 2011 official roster: `data/typeA/donga_2011_100_roster_v0_1.json`
- exact repeat crosswalk: `research/donga_2010_2011_repeat_crosswalk_v1_0.md`
- analyzer: `scripts/analyze_donga_2010_repeat_selection.py`
- committed metrics: `analysis/donga_2010_repeat_selection_metrics_v0_1.json`
- GitHub Actions validation commit: `be47c2310f4212f06a6cc0924fbbe612df0af471`
- Actions run: `32067838483`
- analysis + QA steps: **success**
