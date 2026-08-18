# Type-A common longitudinal coding rules v0.1

- status: **active draft reference schema**
- date: **2026-08-18**
- scope: Type-A media-selected people/organizations with post-selection longitudinal follow-up
- reference implementations: Kyunghyang 2004, Kyunghyang 2005

## 1. Purpose

This schema separates three questions that must not be collapsed into one outcome:

1. **Selection quality / lifetime peak**: did the selected person later reach a major or apex role at any time after selection?
2. **Future rise**: did the person rise above the baseline level observed at selection?
3. **Elite persistence / fixed-window occupancy**: was the person still occupying a high-scope role at a predefined T+10 or T+20 window?

A target-year claim printed in the original article is a fourth, article-specific prediction layer and is stored separately from generic longitudinal windows.

## 2. Unit of analysis

Every original selected unit receives exactly one `unit_id` and one `unit_type`.

Allowed unit types:

- `person`
- `organization`

Original placement counts are preserved even when the same person appears in multiple cohorts. Cross-cohort analyses may also construct a deduplicated person layer, but must not overwrite placement-level denominators.

## 3. Required top-level cohort fields

- `cohort_id`
- `outlet`
- `article_title`
- `publication_date`
- `selection_cutoff`
- `selected_units_n`
- `person_units_n`
- `organization_units_n`
- `source_refs`
- `schema_version`

Optional article-prediction fields:

- `explicit_target_year`
- `explicit_target_label`
- `explicit_prediction_horizon_years`

## 4. Person baseline layer

Each person should preserve the status at the time of selection independently of later outcomes.

Required fields:

- `baseline_scope_score`
- `baseline_scope_label`
- `baseline_role`
- `baseline_date_or_window`
- `baseline_evidence_refs`

The baseline layer is immutable after freeze except for documented factual correction.

## 5. Lifetime post-selection peak layer

Lifetime peak is cumulative across the entire observed post-selection period and must not be confused with a fixed-window snapshot.

Required fields:

- `post_selection_peak_scope_score`
- `post_selection_peak_scope_label`
- `post_selection_peak_role`
- `post_selection_peak_date_or_window`
- `post_selection_peak_evidence_refs`

Derived person metrics:

- `advanced = post_selection_peak_scope_score > baseline_scope_score`
- `major = post_selection_peak_scope_score >= 3`
- `apex = post_selection_peak_scope_score == 4`

`advanced`, `major`, and `apex` describe lifetime post-selection achievement unless explicitly prefixed with a snapshot label.

## 6. Fixed-window snapshot layer

Generic longitudinal windows are centered on elapsed time from selection, not on lifetime peak.

Default windows:

- `t10`: selection year + 10 years, default tolerance ±1 year
- `t20`: selection year + 20 years, default tolerance ±1 year

Each snapshot must contain:

- `window_id`
- `target_year`
- `window_start`
- `window_end`
- `status`
- `scope_score`
- `scope_label`
- `role_at_window`
- `snapshot_date_or_window`
- `evidence_refs`
- `coding_note`

Allowed `status` values:

- `assessable`
- `competing_event`
- `untraceable`
- `not_applicable`

For `assessable`, score the best-supported role actually occupied within the target window. Do **not** import a historical peak or a title held outside the window.

Derived snapshot metrics are window-specific:

- `scope_ge2_at_window = scope_score >= 2`
- `major_at_window = scope_score >= 3`
- `apex_at_window = scope_score == 4`

T+10 and T+20 are separate cross-sectional snapshots. They are not a monotonic survival curve and need not move in one direction.

## 7. Competing events

Death before or during a fixed follow-up window is a competing event, not an ordinary failure.

Rules:

- preserve the person in the original cohort denominator;
- set snapshot `status = competing_event` when death prevents meaningful role occupancy assessment for that window;
- set `scope_score = null` for that window;
- exclude competing events from the primary assessable denominator for window-specific role-occupancy proportions;
- always report both original cohort N and assessable N;
- do not silently reclassify competing events as `0`, `exit`, or `failure`.

Other irreversible events may only be treated as competing events if a later schema version explicitly defines them. v0.1 uses death as the standard competing event.

## 8. Explicit target-year predictions

Some media selections make an explicit prediction about a calendar year, for example “people who will shine in 2020.” This prediction target is conceptually distinct from the generic T+10 framework.

Store:

- `explicit_target_year`
- `target_prediction_snapshot_ref`
- `target_prediction_metric_namespace`

### Deduplication rule when target year equals T+10 or T+20

If the article's explicit target-year window is identical to a generic longitudinal window, **do not create two independent observations**.

Instead:

1. create one canonical snapshot object;
2. assign one canonical `snapshot_id`;
3. link multiple semantic roles to that same object, e.g. `aliases = ["explicit_target_2020", "t10"]`;
4. count the observation once in pooled analyses;
5. allow reporting under both research questions while stating that both labels reuse the same observation.

This rule is required for Dong-A 2010 when explicit target 2020 coincides with generic T+10 centered on 2020.

If the original target-year tolerance differs from the generic ±1-year window, store both windows separately and document the overlap.

## 9. Organization longitudinal layer

Organizations must not be forced into person scope scores.

Organization snapshots use the separate organization architecture, including as applicable:

- `continuity_class`
- `trajectory`
- `reach`
- `field_leadership`
- `institutional_influence`
- `successors`
- `evidence_refs`

Person Major/Apex/Advanced metrics and organization continuity/influence metrics are non-commensurate. A single pooled numeric success percentage across person and organization units is prohibited in v0.1.

## 10. Aggregation rules

For a person cohort and each window, report at minimum:

- `person_n`
- `assessable_n`
- `competing_event_n`
- `untraceable_n`
- `scope_ge2_n / assessable_n`
- `major_ge3_n / assessable_n`
- `apex_eq4_n / assessable_n`

For lifetime peak, report at minimum:

- `person_n`
- `major_n / person_n`
- `apex_n / person_n`
- `advanced_n / person_n`

When cross-cohort persons overlap, report placement-level results first and provide a separate deduplicated unique-person sensitivity analysis if useful.

## 11. Cross-cohort comparison guardrails

Do not interpret descriptive differences as causal superiority of one newspaper/year/cohort when any of the following differ:

- selection baseline
- age/generation composition
- sector composition
- article selection mechanism
- explicit forecast horizon
- target-window calendar year
- denominator size
- overlapping persons

Baseline-adjusted `Advanced` and fixed-window occupancy should accompany raw lifetime `Major/Apex` whenever feasible.

## 12. QA invariants

A frozen cohort should satisfy:

- original selected-unit denominator preserved;
- every original unit has a unit-type-specific outcome path;
- baseline and lifetime peak fields are distinct;
- each fixed-window observation has one canonical snapshot object;
- no historical peak is copied into a fixed-window role score;
- competing events are explicit and not coded as failures;
- duplicate semantic labels pointing to the same calendar observation reuse the same `snapshot_id`;
- person and organization outcome architectures remain separate;
- evidence references exist for all non-null substantive outcome claims.

## 13. Reference implementations

### Kyunghyang 2004

Use the 2004 political cohort as a reference for person-only baseline, peak, T+10, and T+20 comparison.

### Kyunghyang 2005

Use the 60-unit cohort as the primary mixed-unit reference because it contains:

- 57 persons
- 3 organizations
- complete T+10 paths
- complete T+20 paths
- explicit competing-event accounting
- separate person and organization architectures

## 14. Next schema implementation steps

1. Materialize a machine-readable JSON schema corresponding to this document.
2. Map Kyunghyang 2004 and 2005 frozen datasets into the common schema without changing their source freezes.
3. Map Dong-A 2010 with a single canonical 2020 snapshot aliased to both explicit-target and T+10 semantics when the windows are identical.
4. Extend to Dong-A 2011 and subsequent Type-A cohorts.
