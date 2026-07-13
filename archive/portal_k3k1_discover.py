#!/usr/bin/env python3
"""Discover the K3/full-helper dichotomy over canonical attachment rows."""

import itertools
import json

from portal_k3k1_probe import graph, valid
from portal_oneone_small_probe import nmeeting_k6


SURVIVORS = {
    (False, (93, 115, 115)),
    (False, (109, 115, 115)),
    (False, (115, 115, 124)),
    (False, (115, 115, 125)),
}


def main():
    choices = [row for row in range(128) if row.bit_count() >= 5]
    records = []
    for aw in (False, True):
        for rows in itertools.combinations_with_replacement(choices, 3):
            if not valid("triangle", rows, aw):
                continue
            bags = nmeeting_k6(graph("triangle", rows, aw))
            if bags is None:
                if (aw, rows) not in SURVIVORS:
                    raise AssertionError((aw, rows))
                records.append({"aw": aw, "rows": list(rows), "survivor": True})
            else:
                records.append({"aw": aw, "rows": list(rows), "bags": bags})
    with open("portal_k3k1_certificate.json", "w", encoding="utf-8") as out:
        json.dump({"format": 1, "records": records}, out, indent=2)
    print(f"wrote {len(records)} canonical K3/K1 records")


if __name__ == "__main__":
    main()
