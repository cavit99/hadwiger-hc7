#!/usr/bin/env python3
"""Archive K6 models for every admissible P3/full-helper quotient."""

import itertools
import json

from portal_k3k1_probe import graph, valid
from portal_oneone_small_probe import nmeeting_k6


def main():
    choices = (
        [row for row in range(128) if row.bit_count() >= 6],
        [row for row in range(128) if row.bit_count() >= 5],
        [row for row in range(128) if row.bit_count() >= 6],
    )
    records = []
    for aw in (False, True):
        for rows in itertools.product(*choices):
            if not valid("path", rows, aw):
                continue
            bags = nmeeting_k6(graph("path", rows, aw))
            if bags is None:
                raise AssertionError((aw, rows))
            records.append({"aw": aw, "rows": list(rows), "bags": bags})
    with open("portal_p3k1_certificate.json", "w", encoding="utf-8") as out:
        json.dump({"format": 1, "records": records}, out, indent=2)
    print(f"wrote {len(records)} P3/K1 certificates")


if __name__ == "__main__":
    main()
