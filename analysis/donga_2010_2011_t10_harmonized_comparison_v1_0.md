# Dong-A 2010–2011 T+10 harmonized comparison v1.0

- Date: 2026-08-18
- Status: **final descriptive comparison**
- Outcome: fixed-window role occupancy at T+10
- Common scope thresholds: `scope>=2`, `Major=scope>=3`, `Apex=scope=4`

## 1. Why these two cohorts can be compared

Dong-A 2010 「2020년 한국을 빛낼 100인」 has an explicit 2020 prediction. Its frozen admissible window is 2019–2021, which is exactly the generic T+10 window centered on 2020. Therefore the explicit-target and T+10 labels reuse one canonical observation.

Dong-A 2011 「10년 뒤 한국을 빛낼 100인」 uses a T+10 window centered on 2021, with admissible evidence from 2020–2022 and direct 2021 evidence preferred.

The same 0–4 scope architecture is used for the comparison.

## 2. Placement-level descriptive comparison

| Metric | Dong-A 2010 T+10 | Dong-A 2011 T+10 | 2011 − 2010 |
|---|---:|---:|---:|
| Original N | 100 | 100 | — |
| Assessable | 87 | 90 | — |
| Competing event | 3 | 1 | — |
| Unresolved / untraceable | 10 | 9 | — |
| Scope ≥2 | **85/87 = 97.7%** | **87/90 = 96.7%** | **−1.0 pp** |
| Major ≥3 | **42/87 = 48.3%** | **63/90 = 70.0%** | **+21.7 pp** |
| Apex =4 | **5/87 = 5.7%** | **4/90 = 4.4%** | **−1.3 pp** |

The strongest descriptive result is not a difference in whether selected people remained established at all. Both waves are essentially saturated at scope≥2 about ten years later.

The difference appears at the **Major threshold**: 2011-selected people were much more often occupying a domestic top-tier or clear international-leadership role at T+10 than the 2010 cohort.

Apex occupancy is rare in both snapshots and does not show the same increase.

## 3. Why a naive 100-vs-100 significance test is not used

The two placement cohorts are not independent.

- total placements = 200
- unique persons = 162
- repeat-selected in both 2010 and 2011 = 38
- 2010-only = 62
- 2011-new = 62

The admissible windows also overlap substantially:

- 2010 T+10: 2019–2021
- 2011 T+10: 2020–2022
- common calendar overlap: **2020–2021**

Therefore a conventional independent two-sample test treating all 200 placements as unrelated observations would overstate independence. The +21.7 percentage-point Major difference is retained as a **descriptive cohort contrast**, not a causal or independent-sample estimate.

## 4. 162 unique-person first-selection sensitivity analysis

To remove duplicate people, define each person's follow-up from the **first Dong-A selection**:

- all 100 people selected in 2010 use the canonical 2020/T+10 observation;
- the 38 repeat people are counted only once, under their 2010 first selection;
- the 62 people newly appearing in 2011 use the 2021 T+10 observation.

This yields **162 unique persons**.

### Coverage

- original unique-person N = **162**
- assessable = **144**
- competing event = **3**
- unresolved/untraceable = **15**

### Scope distribution among assessable 144

- score 0 = 1
- score 1 = 3
- score 2 = 60
- score 3 = 74
- score 4 = 6

### First-selection T+10 outcomes

| Metric | N / assessable | Rate |
|---|---:|---:|
| Scope ≥2 | 140/144 | **97.2%** |
| Major ≥3 | 80/144 | **55.6%** |
| Apex =4 | 6/144 | **4.2%** |

Using original N=162 as a conservative descriptive denominator gives scope≥2 86.4%, Major 49.4%, and Apex 3.7%. Competing events and unresolved/untraceable cases are **not** reclassified as failures in the primary analysis.

Important: this sensitivity analysis is **person-specific T+10 from first selection**, not a common-calendar-year snapshot. The 2010-first group centers on 2020, while 2011-new entrants center on 2021.

## 5. Interpretation

### Finding 1 — selection strongly predicts continued establishment

About 97% of assessable people in both waves still occupied at least an established national professional/creative/athletic/institutional role at T+10. At this threshold, the lists have little discriminatory room left.

### Finding 2 — Major is the more informative fixed-window threshold

The 2011 cohort has substantially higher Major occupancy at T+10: 70.0% versus 48.3% in 2010. This suggests that the two lists differ more in **level of later elite-role occupancy** than in basic career continuity.

This should not be interpreted as evidence that the 2011 editorial process was causally or intrinsically superior. Baseline prestige, age, sector composition, selection mechanism, and the exact list concept can differ.

### Finding 3 — Apex is a sparse outcome

Apex occupancy is 5.7% in 2010 and 4.4% in 2011. Even among heavily pre-screened prominent people, occupying a national/world-apex role at one fixed follow-up window is uncommon.

This is consistent with the broader project architecture: **lifetime Apex attainment and fixed-window Apex occupancy are different outcomes**.

### Finding 4 — deduplication materially changes what the denominator means

The 200 placements correspond to only 162 people. For cross-wave person-level summaries, the first-selection sensitivity should accompany placement-level results so repeat-selected people are not silently double-weighted.

## 6. What not to conclude

Do not conclude that:

- Dong-A became 21.7 percentage points “better at prediction” in 2011;
- the two 100-person cohorts are independent samples;
- repeat selection causes later success;
- unresolved/untraceable people are failures;
- a fixed-window score is interchangeable with lifetime peak.

## 7. Source freezes

- `state/donga_2010_target2020_freeze_v1_0.json`
- `state/donga_2010_target2020_t10_harmonization_freeze_v1_0.json`
- `data/typeA/donga_2011_t10_metrics_v1_0.json`
- `state/donga_2011_t10_freeze_v1_0.json`
- `state/donga_2010_2011_two_wave_freeze_v0_1.json`
- machine-readable comparison: `analysis/donga_2010_2011_t10_harmonized_comparison_v1_0.json`

## Bottom line

> **Ten years later, almost everyone who was assessable remained professionally established in both waves (~97%). The meaningful separation is at the Major threshold: 48.3% for the 2010 cohort versus 70.0% for the 2011 cohort, while Apex occupancy remains rare (~4–6%). Because 38 people appear in both lists and the windows overlap, this is a descriptive cohort contrast rather than an independent-sample causal comparison.**
