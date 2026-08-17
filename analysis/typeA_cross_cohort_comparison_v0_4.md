# Type-A 교차 코호트 비교 v0.4

**작성일:** 2026-08-18  
**공통 master:** `typeA_common_master_v0.3`  
**분석단위:** **245 placements / 193 canonical persons / 6 cohort units**  
**unique display names:** 192 — 동명이인 1쌍(`이미경`)을 별도 canonical person으로 분리

## 1. v0.4 핵심 변화

경향신문 2004 「17代국회 이끌 뉴리더」 20명을 추가했다. 이 코호트는 17대 국회 당선자 299명을 모집단으로 삼고 전문가 40명이 향후 한국정치를 이끌 인물을 골라 당별 quota로 20명을 선정한 Type-A 정치 코호트다.

이번 추가로 가장 중요한 변화는 두 가지다.

1. **2004년 정치 분야에 서로 다른 selection mechanism 두 개**가 생겼다: 한겨레21 public-opinion Top10과 경향신문 expert future-leader Top20.
2. `이미경` 동명이인 충돌을 실제로 발견하면서 common master가 display-name hash에서 **canonical identity_key** 방식으로 이행했다.

---

## 2. 여섯 cohort unit

| cohort unit | design | n | baseline mean | post-T0 mean* | Major ≥3 | Apex=4 | Advanced |
|---|---|---:|---:|---:|---:|---:|---:|
| 뉴스메이커 2003 정치 Top10 | ranked_topN | 10 | 2.40 | 3.20 | 10/10 (100.0%) | 2/10 (20.0%) | 7/10 (70.0%) |
| 뉴스메이커 2003 경제 Top5 | ranked_topN | 5 | 2.40 | 3.80 | 5/5 (100.0%) | 4/5 (80.0%) | 4/5 (80.0%) |
| 한겨레21 2004 정치 Top10 | ranked_topN | 10 | 3.30 | 3.50 | 10/10 (100.0%) | 5/10 (50.0%) | 4/10 (40.0%) |
| 경향신문 2004 국회 뉴리더20 | expert_vote_party_quota_top20 | 20 | 2.15 | 3.20 | 20/20 (100.0%) | 4/20 (20.0%) | 19/20 (95.0%) |
| 동아일보 2010 미래100 | broad_screening_explicit_horizon | 100 | 2.55 | 2.83 | 71/100 (71.0%) | 12/100 (12.0%) | 28/100 (28.0%) |
| 동아일보 2011 미래100 | broad_screening_explicit_horizon | 100 | 2.67 | 3.03 | 90/100 (90.0%) | 12/100 (12.0%) | 36/100 (36.0%) |

\* assessable placement 기준.

경향 2004는 **Major 100%, Apex 20%, Advanced 95%**다. 단순 수치만 보면 지금까지 가장 높은 advancement를 보이지만, 이것을 곧바로 “경향신문의 예측력이 가장 좋았다”로 해석하면 안 된다.

---

## 3. 같은 2004 정치 분야: 한겨레21 vs 경향신문

이 두 코호트가 현재 데이터에서 가장 유익한 비교다.

| | 한겨레21 2004 정치 Top10 | 경향 2004 뉴리더20 |
|---|---:|---:|
| n | 10 | 20 |
| selection | 일반국민 700명 public opinion | 각계 전문가 40명 panel vote |
| candidate frame | 31명의 전국 정치인 후보 | 17대 당선자 299명 → 45명 1차 후보 |
| 최종 선발 | Top10 | 당별 quota 10/8/2, 총20 |
| baseline mean | **3.30** | **2.15** |
| Major | 100.0% | 100.0% |
| Apex | 50.0% | 20.0% |
| Advanced | **40.0%** | **95.0%** |

### 무엇이 보이는가

한겨레21 후보군은 이미 전국급 중진·장관·대선주자급을 많이 포함해 baseline mean이 3.30이었다. 따라서 이후에도 Major는 100%지만 이미 높은 ceiling 때문에 baseline 초과 상승은 40%였다.

경향은 당 대표를 제외하고 새 국회 당선자 중 **향후 리더 잠재력**을 전문가가 고르는 구조여서 baseline mean이 2.15로 훨씬 낮았다. 20명 중 19명이 이후 자신의 pre-selection lifetime peak를 넘어섰다.

따라서 이 비교가 보여주는 핵심은 outlet superiority가 아니라:

> **“누구를 후보군에 넣고 어떤 질문으로 고르느냐”가 장기 outcome metric을 크게 바꾼다.**

특히 baseline-adjusted advancement는 selection design의 차이를 raw Major보다 훨씬 선명하게 드러낸다.

---

## 4. 경향 2004 결과의 강한 신호와 주의점

경향 20명:

- Major: **20/20 = 100.0%**
- Apex: **4/20 = 20.0%**
- Advanced: **19/20 = 95.0%**
- lower than baseline: **박세일 1명**
- Apex: **김문수, 김부겸, 임종석, 한명숙**

### 박세일 — baseline guardrail 사례

선정 당시에는 새 국회의원으로 보이지만 선정 이전에 이미 대통령비서실 정책기획/사회복지 수석이라는 national-apex급 lifetime peak가 있었다. 따라서 이후 정당 대표가 됐다고 해서 상승으로 세지 않는다. 이 사례는 contemporaneous title 대신 **pre-selection lifetime peak**를 baseline으로 써야 하는 이유를 잘 보여준다.

### 신기남 — imminence guardrail

선정 **12일 뒤** 열린우리당 의장이 됐다. frozen cutoff 뒤의 실제 attainment이므로 원칙상 post-selection peak에 포함하지만, 10년·20년 장기 선구안과 같은 의미로 해석하면 안 된다. `near_immediate_advancement`로 별도 표시한다.

신기남을 단순 sensitivity에서 제외해도 나머지 19명 중 18명이 advanced여서 **94.7%**다. 다만 이것도 inferential estimate가 아니라 descriptive sensitivity다.

---

## 5. Identity architecture v0.3

기존 v0.2는 당시 데이터에서 same-name collision이 모두 verified repeat였기 때문에 `hash(name)`으로 person ID를 만들 수 있었다. 경향 코호트 추가에서 처음으로 실제 homonym이 발견됐다.

- 경향 2004 `이미경` = 열린우리당 정치인
- 동아 2011 `이미경` = CJ E&M 총괄 부회장

따라서 v0.3부터:

```text
identity_key -> person_id
```

방식으로 전환했다.

- `이미경|politician`
- `이미경|cj_enm_business`

두 identity가 서로 다른 canonical person으로 유지된다.

현재 QA:

- placements: **245**
- canonical persons: **193**
- unique display names: **192**
- true homonym split: **1**
- repeated canonical persons: **46**
- placement count distribution: **1회 147 / 2회 41 / 3회 4 / 4회 1**
- 4회 선정: **유시민**
- 3회 선정: **김문수, 안철수, 원희룡, 이재용**

---

## 6. Naïve pooled descriptive — 여전히 참고값

245 placements 전체를 그대로 합치면:

- Major: **206/245 = 84.1%**
- Apex: **39/245 = 15.9%**
- Advanced: **98/245 = 40.0%**

이 값은 “한국 언론 평균 적중률”이 아니다. 반복 인물, 시기, 분야, depth, candidate frame, selection mechanism이 모두 섞여 있다.

---

## 7. Person-level first selection

canonical person별 첫 선정만 사용하면:

- persons: **193**
- Major: **157/193 = 81.3%**
- Apex: **23/193 = 11.9%**
- Advanced: **78/193 = 40.4%**

경향 2004 추가로 송영길의 first selection이 동아 2010에서 경향 2004로 앞당겨지면서, 그의 first-selection class도 `sustained_high`에서 `advanced`로 바뀐다. 이것은 person-level 분석에서 **첫 관찰 코호트가 추가될 때 historical left-truncation이 수정될 수 있음**을 보여준다.

---

## 8. 현재 가장 중요한 연구적 해석

이제 기존의 “언론은 강한 사람을 잘 고르지만 누가 더 성장할지는 약하다”는 결론을 조금 더 정교하게 해야 한다.

현재 자료는 두 패턴을 동시에 보인다.

### A. Established-elite 후보군

한겨레21 2004, 동아 일부 코호트처럼 baseline이 이미 높은 후보군에서는:

- later Major는 매우 높지만
- actual advancement는 훨씬 낮다.

### B. Explicit future-potential 후보군

경향 2004처럼 이미 최고위 인물을 일부러 제외하고 새 당선자 중 **미래 리더 잠재력**을 묻는 설계에서는:

- baseline이 낮고
- baseline-adjusted advancement가 매우 높게 나온다.

따라서 현재 더 적절한 가설은:

> **언론의 ‘미래예측력’은 매체 자체의 고정된 속성이라기보다 candidate frame, 질문, selector, list depth가 결합된 selection design의 속성일 가능성이 크다.**

이 가설을 검정하려면 같은 시대·분야에서 서로 다른 매체의 comparable design을 더 확보해야 한다.

---

## 9. 다음 우선순위

1. **한겨레21 2004 full31** — 지면/DB에서 남은 20명 복원.
2. 경향 2004 20명의 **T+10 / T+20 / current milestone** 추가.
3. 조선·중앙의 2003–2005 정치 미래리더/차세대 인물 리스트 탐색.
4. 동일 시기 정치 코호트가 더 모이면 `baseline + design + outlet`을 분리한 model 설계.
5. 충분한 표본 이후 person-clustered / mixed-effects 분석.

---

## 10. Reproducibility

- Kyunghyang roster: `research/khan_2004_17th_assembly_newleaders_roster_v0_1.json`
- peak audits: `research/khan_2004_peak_audit_uri_batch1_v0_1.json`, `research/khan_2004_peak_audit_gnp_dlp_batch2_v0_1.json`
- Kyunghyang master: `data/typeA/khan_2004_17th_assembly_newleaders_peak_master_v1_0.json`
- identity policy: `state/identity_resolution_policy_v0_2.md`
- identity overrides: `data/typeA/canonical_identity_overrides_v0_1.json`
- common master: `data/typeA/typeA_common_master_v0_3.json`
- common metrics: `data/typeA/typeA_common_metrics_v0_3.json`
- this builder: `scripts/build_typeA_cross_cohort_comparison_v0_4.py`
- this report: `analysis/typeA_cross_cohort_comparison_v0_4.md`
