#!/usr/bin/env python3
import csv, json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/typeA/donga_2010_baseline_from_capture_v1_0.json"
CANON = ROOT / "data/typeA/donga_2010_canonical_roster_v2_1.json"
OUT_JSON = ROOT / "data/typeA/donga_2010_t0_snapshot_scope_v0_1.json"
OUT_CSV = ROOT / "data/typeA/donga_2010_t0_snapshot_scope_v0_1.csv"

SCORE = {
"김연아":4,"김윤진":3,"김현수":2,"노희경":2,"박민규":2,"박성훈":2,"박진영":3,"봉준호":3,"서도호":3,"신경숙":2,
"신지애":4,"심승현":2,"양성원":2,"이청용":3,"장한나":3,"정연두":2,"정욱준":2,"조성진":2,"최은석":2,"홍명보":3,
"김광수":2,"김기문":2,"김빛내리":3,"김정범":2,"김창진":2,"김필립":2,"김호근":2,"남홍길":2,"박승정":3,"박홍근":2,
"서동철":2,"신재원":3,"안철수":2,"이상엽":3,"이상훈":2,"이소연":2,"이지오":2,"이효철":2,"임지순":2,"정경민":2,
"정하웅":2,"조동호":2,"주영석":2,"찰스 리":2,"현택환":3,
"김강립":2,"김숙정":2,"김용":3,"김준영":2,"김해성":2,"김형태":2,"박원순":2,"송호근":2,"염형국":2,"오충현":2,
"유근배":2,"윤명철":2,"이광형":2,"이명균":2,"이연주":2,"이은영":2,"이주호":3,"임경진":1,"조국":2,"한숭희":2,
"강덕수":3,"강방천":2,"김재하":2,"김택진":3,"남수정":2,"박병엽":2,"박인출":2,"박지영":2,"박현주":3,"서경배":3,
"서정진":3,"성영석":2,"신동빈":3,"신현송":3,"안동현":2,"이근":2,"이부진":3,"이원규":2,"이재용":3,"이창용":3,
"이해진":3,"장하준":3,"정의선":3,"정태영":3,"최태원":4,
"김문수":3,"김병국":2,"김성한":2,"나경원":2,"송영길":3,"오세훈":3,"원희룡":2,"유시민":1,"임태희":3,
"백경학":2
}

SECTOR = {
"김연아":"sports","김현수":"sports","신지애":"sports","이청용":"sports","홍명보":"sports",
"김윤진":"culture_media","노희경":"culture_literature","박민규":"culture_literature","박성훈":"culinary",
"박진영":"culture_music_business","봉준호":"culture_film","서도호":"culture_visual_art","신경숙":"culture_literature",
"심승현":"culture_comics","양성원":"culture_music_academia","장한나":"culture_music","정연두":"culture_visual_art",
"정욱준":"culture_fashion","조성진":"culture_music","최은석":"digital_media_business",
"김광수":"biomedicine","김기문":"chemistry","김빛내리":"molecular_biology","김정범":"biomedicine","김창진":"engineering",
"김필립":"physics","김호근":"medicine","남홍길":"life_science","박승정":"medicine","박홍근":"chemistry","서동철":"immunology",
"신재원":"aerospace_public_research","안철수":"technology_academia","이상엽":"bioengineering","이상훈":"neuroscience","이소연":"aerospace_research",
"이지오":"chemistry","이효철":"chemistry","임지순":"physics","정경민":"industrial_research","정하웅":"physics","조동호":"engineering",
"주영석":"genomics","찰스 리":"genomics","현택환":"chemistry_nanoscience",
"김강립":"public_service","김숙정":"education_public_service","김용":"education_global_leadership","김준영":"labor_civic",
"김해성":"civic_ngo","김형태":"law_civic","박원순":"civic_policy","송호근":"sociology_academia","염형국":"law_civic",
"오충현":"global_health_public_service","유근배":"geography_academia","윤명철":"history_academia","이광형":"technology_academia",
"이명균":"environment_academia","이연주":"civic_politics","이은영":"consumer_civic","이주호":"public_service","임경진":"youth_civic",
"조국":"law_academia","한숭희":"education_academia",
"강덕수":"business","강방천":"finance_business","김재하":"digital_art_academia","김택진":"technology_business","남수정":"food_business",
"박병엽":"technology_business","박인출":"healthcare_business","박지영":"technology_business","박현주":"finance_business","서경배":"consumer_business",
"서정진":"biotech_business","성영석":"digital_media_business","신동빈":"conglomerate_business","신현송":"public_economics","안동현":"economics_academia",
"이근":"economics_academia","이부진":"conglomerate_business","이원규":"agritech_business","이재용":"conglomerate_business","이창용":"public_economics",
"이해진":"technology_business","장하준":"economics_academia","정의선":"conglomerate_business","정태영":"finance_business","최태원":"conglomerate_business",
"김문수":"politics","김병국":"political_science_academia","김성한":"international_relations_academia","나경원":"politics",
"송영길":"politics","오세훈":"politics","원희룡":"politics","유시민":"politics","임태희":"politics","백경학":"civic_ngo"
}

REVIEW_FLAGS = {
"김윤진":["pre_t0_international_achievement_may_raise_or_confirm_scope"],
"박진영":["industry_leadership_scope_review"],
"봉준호":["pre_t0_international_film_achievement_review"],
"서도호":["pre_t0_international_art_achievement_review"],
"장한나":["pre_t0_international_music_achievement_review"],
"김광수":["research_stature_may_exceed_title_only_scope"],
"김기문":["research_stature_may_exceed_title_only_scope"],
"김필립":["research_stature_may_exceed_title_only_scope"],
"남홍길":["research_stature_may_exceed_title_only_scope"],
"박홍근":["research_stature_may_exceed_title_only_scope"],
"임지순":["research_stature_may_exceed_title_only_scope"],
"정하웅":["research_stature_may_exceed_title_only_scope"],
"찰스 리":["research_stature_may_exceed_title_only_scope"],
"장하준":["international_academic_stature_review"],
"유시민":["capture_role_is_former_office; contemporaneous_active_political_context_requires_audit"],
"강덕수":["group_scale_boundary_3_vs_4_review"],
"박현주":["financial_group_scale_boundary_3_vs_4_review"]
}

ACHIEVEMENT_EXCEPTIONS = {
"김연아":{
    "reason":"2010 Vancouver Olympic figure-skating gold occurred before the May 2010 selection, so contemporaneous athlete scope was global apex.",
    "source_urls":["https://newsroom.olympics.com/record/1306/media_id/3968"]
},
"신지애":{
    "reason":"Became women's golf world No.1 on 2010-05-03, before the Donga selection launch on 2010-05-10.",
    "source_urls":["https://www.golfchannel.com/news/article-golftalkcentral-shin-1-womens-golf"]
}
}

def load_rows():
    base = json.load(open(BASE, encoding="utf-8"))
    canon = json.load(open(CANON, encoding="utf-8"))
    canon_cat = {}
    for cat, names in canon["categories"].items():
        for n in names:
            canon_cat[n] = cat

    rows = []
    for cat, people in base["categories"].items():
        for p in people:
            p = dict(p)
            if p["name"] == "한승희":
                p["name"] = "한숭희"
            name = p["name"]
            if name not in canon_cat:
                raise AssertionError(f"baseline name not canonical: {name}")
            p["category"] = canon_cat[name]
            rows.append(p)
    if len(rows) != 100 or len({x["name"] for x in rows}) != 100:
        raise AssertionError("baseline rows are not exact 100 unique people")
    if set(SCORE) != {x["name"] for x in rows}:
        raise AssertionError(f"score mapping mismatch: {set(SCORE) ^ {x['name'] for x in rows}}")
    if set(SECTOR) != {x["name"] for x in rows}:
        raise AssertionError(f"sector mapping mismatch: {set(SECTOR) ^ {x['name'] for x in rows}}")
    return rows

def main():
    source_rows = load_rows()
    out = []
    for p in source_rows:
        name = p["name"]
        score = SCORE[name]
        flags = REVIEW_FLAGS.get(name, [])
        exc = ACHIEVEMENT_EXCEPTIONS.get(name)
        if exc:
            basis = "primary_capture_role_plus_preselection_achievement"
            confidence = "H"
        elif flags:
            basis = "primary_capture_role_conservative_scope_pass1"
            confidence = "M"
        else:
            basis = "primary_capture_role"
            confidence = "H"
        out.append({
            "name": name,
            "category": p["category"],
            "t0_role": p["role"],
            "age": p.get("age"),
            "sex": p.get("sex"),
            "t0_snapshot_scope_score": score,
            "sector": SECTOR[name],
            "score_basis": basis,
            "coding_confidence": confidence,
            "review_flags": flags,
            "achievement_exception": exc
        })

    score_counts = dict(sorted(Counter(x["t0_snapshot_scope_score"] for x in out).items()))
    bycat = {}
    for cat in ["자유로운 창조인","꿈꾸는 개척가","행동하는 지성인","도전하는 경제인","미래를 여는 지도자","독자선정"]:
        subset=[x for x in out if x["category"]==cat]
        bycat[cat]={
            "n":len(subset),
            "score_counts":dict(sorted(Counter(x["t0_snapshot_scope_score"] for x in subset).items())),
            "mean_scope":sum(x["t0_snapshot_scope_score"] for x in subset)/len(subset),
            "review_flagged":sum(bool(x["review_flags"]) for x in subset)
        }

    payload={
        "schema_version":"donga_2010_t0_snapshot_scope_v0.1",
        "generated":"2026-08-18",
        "status":"pass1_complete_provisional_not_baseline_peak",
        "protocol_ref":"state/donga_2010_baseline_peak_protocol_v1_0.md",
        "sector_rules_ref":"state/coding_rules_typeA_sector_scope_v0_1.md",
        "canonical_roster_ref":"data/typeA/donga_2010_canonical_roster_v2_1.json",
        "baseline_capture_ref":"data/typeA/donga_2010_baseline_from_capture_v1_0.json",
        "method":{
            "definition":"scope of the role actually held around the May 2010 selection, using the original capture as primary evidence",
            "conservative_rule":"generic professor/PI, established creator/professional, MP, nationwide NGO/professional role, and mid-sized CEO default to score 2 unless the contemporaneous role itself or strong pre-selection achievement justifies higher",
            "achievement_exceptions":"only directly verified achievements before the May 2010 selection are allowed in pass 1",
            "not_yet_done":"baseline_peak_through_t0 and full prior-achievement audit are separate pass 2"
        },
        "qa":{
            "total":len(out),
            "unique_names":len({x["name"] for x in out}),
            "score_counts":score_counts,
            "review_flagged_n":sum(bool(x["review_flags"]) for x in out),
            "by_category":bycat
        },
        "people":out
    }
    OUT_JSON.write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding="utf-8")
    with OUT_CSV.open("w",encoding="utf-8-sig",newline="") as f:
        fields=["name","category","t0_role","age","sex","t0_snapshot_scope_score","sector","score_basis","coding_confidence","review_flags"]
        w=csv.DictWriter(f,fieldnames=fields)
        w.writeheader()
        for x in out:
            y={k:x.get(k) for k in fields}
            y["review_flags"]=";".join(x["review_flags"])
            w.writerow(y)

    assert len(out)==100 and len({x["name"] for x in out})==100
    assert score_counts == {1:2,2:63,3:32,4:3}
    assert sum(bycat[c]["n"] for c in bycat)==100
    print(json.dumps(payload["qa"],ensure_ascii=False,indent=2))

if __name__ == "__main__":
    main()
