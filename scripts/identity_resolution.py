#!/usr/bin/env python3
import hashlib
import json
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OVERRIDES_PATH = ROOT / 'data/typeA/canonical_identity_overrides_v0_1.json'


@lru_cache(maxsize=1)
def load_overrides():
    d = json.loads(OVERRIDES_PATH.read_text(encoding='utf-8'))
    rows = d['overrides']
    index = {}
    for r in rows:
        sel = r['placement_selector']
        key = (r['display_name'], sel['outlet'], sel['cohort_unit'])
        assert key not in index, f'duplicate identity override selector: {key}'
        index[key] = r
    return d, index


def resolve_identity_key(name, outlet, cohort_unit):
    _, index = load_overrides()
    r = index.get((name, outlet, cohort_unit))
    return r['identity_key'] if r else name


def person_id_from_identity_key(identity_key):
    return 'ko-' + hashlib.sha256(identity_key.encode('utf-8')).hexdigest()[:12]


def person_id(name, outlet, cohort_unit):
    return person_id_from_identity_key(resolve_identity_key(name, outlet, cohort_unit))


def audit_same_name_rows(rows):
    """Return unresolved homonym risk where one display name maps ambiguously without explicit overrides.

    rows must contain name/outlet/cohort_unit. Same-name rows are allowed to resolve to the same identity_key
    (verified repeat) or to distinct explicit identity_keys (adjudicated homonyms). If a name has a mix of
    default-name identity and explicit alternate identities, that is allowed only when every placement that
    should be distinct is explicitly overridden; callers should freeze expected identity counts separately.
    """
    by_name = {}
    for r in rows:
        by_name.setdefault(r['name'], []).append(r)
    result = {}
    for name, rr in by_name.items():
        if len(rr) < 2:
            continue
        resolved = [resolve_identity_key(x['name'], x['outlet'], x['cohort_unit']) for x in rr]
        result[name] = {
            'placement_n': len(rr),
            'identity_keys': sorted(set(resolved)),
            'identity_n': len(set(resolved))
        }
    return result


if __name__ == '__main__':
    d, _ = load_overrides()
    sample = []
    for r in d['overrides']:
        s = r['placement_selector']
        ik = resolve_identity_key(r['display_name'], s['outlet'], s['cohort_unit'])
        sample.append({
            'name': r['display_name'],
            'outlet': s['outlet'],
            'cohort_unit': s['cohort_unit'],
            'identity_key': ik,
            'person_id': person_id_from_identity_key(ik)
        })
    print(json.dumps(sample, ensure_ascii=False, indent=2))
