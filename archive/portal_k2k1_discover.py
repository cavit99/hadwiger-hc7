#!/usr/bin/env python3
"""Discover K6 models for a two-vertex shore opposite one contracted shore."""

import itertools
import json

from portal_oneone_small_probe import U, W, nmeeting_k6, pair_single_graph


def main():
    options = (None,) + U + (W,)
    records = []
    for defects in itertools.product(options, repeat=2):
        bags = nmeeting_k6(pair_single_graph(defects))
        if bags is None:
            raise AssertionError(f"uncovered defect tuple {defects}")
        records.append({
            "defects": [-1 if x is None else x for x in defects],
            "bags": bags,
        })
    with open("portal_k2k1_certificate.json", "w", encoding="utf-8") as out:
        json.dump({"format": 1, "records": records}, out, indent=2)
    print(f"wrote {len(records)} K2/K1 model certificates")


if __name__ == "__main__":
    main()
