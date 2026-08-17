#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate v3 report + detailed markdown from outcomes_v3.json.

Outputs:
- report_2026-08-17_v3.md
- state/outcomes_v3.md (project layout) or outcomes_v3.md (flat layout)
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

VITAL_KO={"alive_confirmed":"생존 확인","deceased":"사망","unknown":"미확인"}
CURR_KO={
 "active_fulltime":"현직","active_parttime_advisory":"자문급 현역",
 "emeritus_retired_active":"명예/은퇴 후 활동","retired":"은퇴",
 "unknown":"미확인","not_applicable":"해당 없음(사망)"
}
STATUS_KO={
 "upward_expansion":"상승·확장","sustained_high":"상위 유지",
 "sustained_normal":"안정적 유지","decline_or_reversal":"하락·반전",
 "insufficient_data":"데이터 부족"
}
SECTOR_KO={"same_field":"동일 분야","adjacent_field":"인접 분야","major_pivot":"큰 분야 전환","unknown":"미확인"}
TRACE_KO={"verified_current":"현재 검증","verified_but_stale":"과거까지만","stale_no_signal":"신호 없음"}
LEVEL_KO={
 "elite_high":"상위/엘리트","established":"안정적 전문활동",
 "adverse_reversal":"중대한 반전","deceased":"사망","unknown":"미관찰"
}
MATCH_KO={
 "exact_year":"정확 연도","within_window":"±1년 창",
 "timeline_covers_target":"임기가 목표연도 포함",
 "nearest_outside_window":"창 밖 최근접","not_observed":"미관찰"
}
STRICT={"exact_year","within_window","timeline_covers_target"}

def resolve(root:Path):
    p=root/"data"/"outcomes_v3.json"
    if p.exists():
        return p, root/"report_2026-08-17_v3.md", root/"state"/"outcomes_v3.md"
    p=root/"outcomes_v3.json"
    if p.exists():
        return p, root/"report_2026-08-17_v3.md", root/"outcomes_v3.md"
    raise FileNotFoundError(f"outcomes_v3.json not found under {root}")

def pct(n,d,dec=0):
    if not d: return "—"
    return f"{n/d*100:.{dec}f}%"

def short_role(s, n=70):
    s=s.replace("|","/")
    return s if len(s)<=n else s[:n-1]+"…"

def milestone_cell(m):
    mark="" if m["match"] in STRICT else " †"
    yr=m.get("evidence_date") or "?"
    return f"**{LEVEL_KO[m['level']]}**{mark}<br>{short_role(m['observed_role'],52)}<br><sub>{yr} · {MATCH_KO[m['match']]} · {m['confidence']}</sub>"

def current_cell(p):
    ev=p.get("evidence_date") or "?"
    return f"**{STATUS_KO[p['status_trajectory']]}**<br>{CURR_KO[p['current_status']]}<br><sub>{ev} · {TRACE_KO[p['trace_status']]}</sub>"

def dist_table(d, mapping=None):
    total=sum(d.values())
    return "\n".join(f"| {(mapping or {}).get(k,k)} | {v} | {pct(v,total)} |" for k,v in d.items())

def strict_gap(P,key):
    return [p["name"] for p in P if p[key]["match"] not in STRICT]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--root",type=Path,default=Path(__file__).resolve().parent)
    args=ap.parse_args()
    root=args.root.resolve()
    src,report_path,detail_path=resolve(root)
    d=json.loads(src.read_text(encoding="utf-8"))
    P=d["people"]; A=d["aggregates"]
    T10=A["milestones"]["t10"]; T20=A["milestones"]["t20"]
    H=A["high_status_trajectory"]; CV=A["current_verification_coverage"]

    master=[]
    for p in P:
        master.append(
            f"| {p['year']} | **{p['name']}** | {short_role(p['t0_title'],42)} | "
            f"{milestone_cell(p['t10'])} | {milestone_cell(p['t20'])} | "
            f"{current_cell(p)} | {SECTOR_KO.get(p['sector_transition'],p['sector_transition'])} |"
        )
    master_table=(
        "| 선정 | 인물 | T0 | T+10 | T+20 | Current | 전체 분야이동 |\n"
        "|---:|---|---|---|---|---|---|\n"+"\n".join(master)
    )

    by_year=[]
    for y in (2002,2003,2004,2005):
        a=A["milestones_by_year"]["t10"][str(y)]
        b=A["milestones_by_year"]["t20"][str(y)]
        by_year.append(
          f"| {y} | {a['strict_coverage']}/{a['n']} ({pct(a['strict_coverage'],a['n'])}) | "
          f"{a['elite_high']}/{a['career_assessable']} ({pct(a['elite_high'],a['career_assessable'])}) | "
          f"{b['strict_coverage']}/{b['n']} ({pct(b['strict_coverage'],b['n'])}) | "
          f"{b['elite_high']}/{b['career_assessable']} ({pct(b['elite_high'],b['career_assessable'])}) |"
        )
    by_dept=[]
    for dep in ("학술연구","산업계","사회문화"):
        a=A["milestones_by_dept"]["t10"][dep]
        b=A["milestones_by_dept"]["t20"][dep]
        by_dept.append(
          f"| {dep} | {a['strict_coverage']}/{a['n']} ({pct(a['strict_coverage'],a['n'])}) | "
          f"{a['elite_high']}/{a['career_assessable']} ({pct(a['elite_high'],a['career_assessable'])}) | "
          f"{b['strict_coverage']}/{b['n']} ({pct(b['strict_coverage'],b['n'])}) | "
          f"{b['elite_high']}/{b['career_assessable']} ({pct(b['elite_high'],b['career_assessable'])}) |"
        )

    gaps10=", ".join(strict_gap(P,"t10")) or "없음"
    gaps20=", ".join(strict_gap(P,"t20")) or "없음"

    report=f'''# 그때 언론이 찍은 사람들: 20년 후
## Pilot 결과 보고서 v3 — T+10 / T+20 장기궤적 추가
### 동아일보 「닮고 싶고 되고 싶은 과학기술인」 2002–2005 코호트 (n=39)

**작성일:** 2026-08-17 (KST)  
**원데이터:** `data/outcomes_v3.json`  
**코딩 규칙:** `state/coding_rules_v3.md`  
**추적축:** T0 → T+10(±1년) → T+20(±1년) → Current(2026-08)

> v3의 가장 중요한 변화는 Current 한 장면이 아니라 **시간축을 갖는 longitudinal cohort**로 바뀐 것이다.  
> 이 코호트는 미래 유망주 예측(Type A)이 아니라 이미 성취한 역할모델(Type B)이므로, 여전히 “언론 예측 성공률”은 계산하지 않는다.

---

## 1. v2.1 → v3 핵심 변경

1. **39명 전원에 T+10과 T+20 milestone 추가**
   - T+10 = 선정연도 + 10년, 허용 창 ±1년
   - T+20 = 선정연도 + 20년, 허용 창 ±1년
2. **시점 근거의 질을 명시**
   - `exact_year`, `within_window`, `timeline_covers_target`, `nearest_outside_window`, `not_observed`
3. **손욱 추적 완료** — 2025년 공개활동 확인, lifetime trajectory 재평가.
4. **이조원 identity 마무리** — 2004 T0 원문과 KAIST 경력선 연결, confirmed로 승격.
5. **국양·김규원 Current 갱신**.
6. **유향숙/유명희 entity-swap 및 이재웅 쏘카 창업자 표현 정정**, 장순근·손욱·문대원 strict evidence 보강.

---

## 2. 데이터 완성도

### 2.1 Current 검증
- **현재 검증:** **{CV['verified_current']}/{CV['total']} = {pct(CV['verified_current'],CV['total'])}**
- v2.1의 26/39(67%)에서 **{CV['verified_current']}/39({pct(CV['verified_current'],39)})**로 상승.

### 2.2 T+10
- **Strict coverage:** **{T10['strict_coverage']['n']}/39 = {pct(T10['strict_coverage']['n'],39)}**
- Broad coverage: {T10['broad_coverage']['n']}/39 = {pct(T10['broad_coverage']['n'],39)}
- career-level 평가 가능: {T10['career_assessable_strict']}명
- `elite_high`: **{T10['elite_high_strict']['n']}/{T10['elite_high_strict']['denominator']} = {pct(T10['elite_high_strict']['n'],T10['elite_high_strict']['denominator'])}**
- Wilson 95% CI: {T10['elite_high_strict']['wilson_95_ci'][0]*100:.0f}–{T10['elite_high_strict']['wilson_95_ci'][1]*100:.0f}%

Strict gap: **{gaps10}**

### 2.3 T+20
- **Strict coverage:** **{T20['strict_coverage']['n']}/39 = {pct(T20['strict_coverage']['n'],39)}**
- Broad coverage: {T20['broad_coverage']['n']}/39 = {pct(T20['broad_coverage']['n'],39)}
- 사망 2명을 제외한 career-level 평가 가능: {T20['career_assessable_strict']}명
- `elite_high`: **{T20['elite_high_strict']['n']}/{T20['elite_high_strict']['denominator']} = {pct(T20['elite_high_strict']['n'],T20['elite_high_strict']['denominator'])}**
- Wilson 95% CI: {T20['elite_high_strict']['wilson_95_ci'][0]*100:.0f}–{T20['elite_high_strict']['wilson_95_ci'][1]*100:.0f}%

Strict gap: **{gaps20}**

> T+10과 T+20의 elite-high 비율 차이를 곧바로 성공률 하락으로 해석하지 않는다. 20년 추적에서는 정년·사망·명예직 전환이 구조적으로 늘어나며 `established`는 실패가 아니다.

---

## 3. 39명 전체 longitudinal table

{master_table}

---

## 4. 시점별 분포

### T+10 level
| level | 인원 | 비율 |
|---|---:|---:|
{dist_table(T10['level'],LEVEL_KO)}

### T+20 level
| level | 인원 | 비율 |
|---|---:|---:|
{dist_table(T20['level'],LEVEL_KO)}

---

## 5. 코호트 연도별
| 선정연도 | T+10 strict coverage | T+10 elite/assessable | T+20 strict coverage | T+20 elite/assessable |
|---:|---:|---:|---:|---:|
{chr(10).join(by_year)}

---

## 6. T0 부문별
| T0 부문 | T+10 strict coverage | T+10 elite/assessable | T+20 strict coverage | T+20 elite/assessable |
|---|---:|---:|---:|---:|
{chr(10).join(by_dept)}

---

## 7. 생애 궤적 요약
- **high-status lifetime trajectory:** **{H['high']}/{H['assessable']} = {pct(H['high'],H['assessable'])}**
- Wilson 95% CI: {H['wilson_95_ci'][0]*100:.0f}–{H['wilson_95_ci'][1]*100:.0f}%

## 8. 남은 공백
- T+10 strict: **{gaps10}**
- T+20 strict: **{gaps20}**

## 9. 한계
1. n=39 단일 Type B 코호트이며 미래예측 정확도를 뜻하지 않는다.
2. 공개 웹 자료 기반이라 직군별 visibility가 다르다.
3. `elite_high`와 `established` 경계에는 연구자 판단이 들어간다.
4. T+20의 정년·사망 증가 때문에 T+10과 단순 비교하지 않는다.

## 한 줄 결론
> **v3에서 이 Pilot은 ‘39명의 2026년 근황표’가 아니라, T0→T+10→T+20→Current의 장기 경력궤적 데이터셋으로 완성됐다.**
'''

    detail=[
      "# Outcome 상세 근거 v3 — T0 / T+10 / T+20 / Current","",
      f"**기준일:** {d['generated']} · **schema:** {d['schema_version']} · **코딩 규칙:** {d['rules_ref']}","",
      "T+10/T+20의 `match`가 `exact_year | within_window | timeline_covers_target`일 때 strict evidence로 간주한다.",""
    ]
    for y in (2002,2003,2004,2005):
        detail += [f"## {y} 코호트",""]
        for p in [x for x in P if x["year"]==y]:
            detail += [f"### {p['name']}","",f"- **T0:** {p['t0_title']}"]
            for key,label in (("t10","T+10"),("t20","T+20")):
                m=p[key]
                detail += [
                  f"- **{label} target:** {m['target_year']} (window {m['window'][0]}–{m['window'][1]})",
                  f"  - role: {m['observed_role']}",
                  f"  - level / sector: `{m['level']}` / `{m['sector']}`",
                  f"  - evidence: {m.get('evidence_date') or '—'} · `{m['match']}` · confidence {m['confidence']}"
                ]
                if m["sources"]:
                    detail.append("  - sources:")
                    for i,s in enumerate(m["sources"]):
                        u=m.get("source_urls",[])
                        detail.append(f"    - [{s}]({u[i]})" if i<len(u) and u[i] else f"    - {s}")
                if m.get("note"): detail.append(f"  - note: {m['note']}")
            detail += [
              f"- **Current:** vital `{p['vital_status']}` · current `{p['current_status']}` · status `{p['status_trajectory']}` · sector `{p['sector_transition']}`",
              f"  - current evidence: {p.get('evidence_date') or '—'} · trace `{p['trace_status']}` · confidence {p['confidence']}"
            ]
            if p.get("sources"):
                detail.append("  - current sources:")
                detail += [f"    - {s}" for s in p["sources"]]
            if p.get("note"): detail.append(f"  - current note: {p['note']}")
            detail += ["","---",""]

    report_path.parent.mkdir(parents=True,exist_ok=True)
    detail_path.parent.mkdir(parents=True,exist_ok=True)
    report_path.write_text(report,encoding="utf-8")
    detail_path.write_text("\n".join(detail),encoding="utf-8")
    print("written:",report_path)
    print("written:",detail_path)

if __name__=="__main__":
    main()
