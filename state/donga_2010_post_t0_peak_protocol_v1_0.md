# Dong-A 2010 post-T0 peak protocol v1.0

**Cohort:** 동아일보 2010 「2020년 한국을 빛낼 100인」  
**Selection cutoff:** 2010-05-10 launch date  
**Observation end:** 2026-08-18

## 1. Definition

`post_t0_peak_score` is the highest verified scope reached **after the 2010 selection cutoff** through the observation end.

It is distinct from:
- `t0_snapshot_scope_score`: contemporaneous May-2010 scope
- `baseline_peak_through_t0`: lifetime peak on or before selection
- `target2020_scope_score`: scope specifically around the explicit target year 2020
- `current_scope_score`: current snapshot

## 2. Time boundary

- Events/roles beginning on or before 2010-05-10 belong to baseline/T0, not post-T0.
- If a role spans the cutoff and continues afterward, it can count as post-T0 persistence at the same score, but not as a new advancement unless a higher stratum is subsequently reached.
- A higher role achieved after the cutoff defines the post-T0 peak even if later lost.

## 3. Competing events

Death is **not** coded as prediction failure.

For a person who dies after selection:
- record the highest verified post-T0 peak reached before death;
- set `exposure_truncated_by_death=true`;
- retain death date/year separately;
- advancement can be described, but cohort-level sensitivity should also report results excluding truncated exposure.

## 4. Scoring

Use `state/coding_rules_typeA_sector_scope_v0_1.md` unchanged (0–4 coarse ordinal scope).

The score captures social/organizational/professional reach, not moral worth, wealth, fame alone, or scientific citation counts alone.

## 5. Evidence hierarchy

Prefer:
1. official institution/government/company/sports body/award body;
2. primary professional biography or official event archive;
3. high-quality contemporaneous news for dated transitions;
4. secondary sources only when stronger sources are unavailable.

For score 4, require especially strong direct evidence of apex status.

## 6. Output fields

For every person:
- `post_t0_peak_role`
- `post_t0_peak_score`
- `post_t0_peak_year`
- `sector_at_peak`
- `evidence_confidence`
- `source_urls`
- `peak_reason`
- `exposure_truncated_by_death`
- `death_year` if applicable
- `coding_status`

## 7. Final Type-A metrics after freeze

Once all rows are audited/frozen:
- `major_leadership_precision = post_t0_peak_score >= 3`
- `apex_precision = post_t0_peak_score == 4`
- `advancement_delta = post_t0_peak_score - baseline_peak_through_t0`
- classes:
  - `advanced`: delta > 0
  - `sustained_high`: delta = 0 and post peak >= 3
  - `no_clear_advancement`: delta = 0 and post peak < 3
  - `lower_than_baseline`: delta < 0
  - `not_assessable`: insufficient evidence

Because this 2010 roster is alphabetical within editorial categories, **ranking correlation is not estimable** from row order.

## 8. Guardrails

- Do not use 2026 office alone if an earlier higher office existed.
- Do not substitute target2020 snapshot for lifetime post-T0 peak without checking later/earlier post-selection years.
- Do not turn unresolved evidence into score 0.
- Do not raise a score solely because the person is famous.
- Freeze by version; corrections require a superseding version.
