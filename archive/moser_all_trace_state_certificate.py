#!/usr/bin/env python3
"""Check an explicit all-ten-trace abstract state certificate for Moser.

The certificate shows that the listed boundary-state/support axioms remain
jointly consistent.  It is NOT a graph and does not claim realizability by
boundaried graphs.  See ``hadwiger_moser_state_certificate.md``.
"""

from itertools import combinations


def edge(text: str) -> tuple[int, int]:
    assert len(text) == 2
    return tuple(sorted(map(int, text)))


def state(text: str) -> frozenset[tuple[int, int]]:
    return frozenset(edge(part) for part in text.split("-"))


E1 = {
    state(x)
    for x in (
        "05-14", "05-24", "05-46", "06-13", "06-14", "06-15",
        "13-25", "14-23", "15-24", "15-46", "23-46", "24-36",
        "05-13-24", "05-14-36", "05-23-46", "06-13-24",
        "06-14-25", "06-15-23", "13-25-46", "14-25-36",
        "15-24-36",
    )
}
E2 = {
    state(x)
    for x in (
        "05-13", "05-23", "05-36", "06-23", "06-24", "06-25",
        "13-24", "13-46", "14-25", "14-36", "15-36", "25-36",
        "25-46", "05-13-46", "05-14-23", "05-24-36",
        "06-13-25", "06-14-23", "06-15-24", "15-23-46",
    )
}

SUPPORT = {
    "05": {"13": "1", "14": "2", "23": "1", "24": "2", "36": "1", "46": "2"},
    "06": {"13": "2", "14": "2", "15": "2", "23": "1", "24": "1", "25": "1"},
    "13": {"05": "1", "06": "2", "24": "B", "25": "B", "46": "B"},
    "14": {"05": "2", "06": "B", "23": "B", "25": "1", "36": "B"},
    "15": {"06": "B", "23": "B", "24": "2", "36": "1", "46": "2"},
    "23": {"05": "1", "06": "1", "14": "2", "15": "B", "46": "2"},
    "24": {"05": "B", "06": "1", "13": "B", "15": "2", "36": "2"},
    "25": {"06": "1", "13": "2", "14": "B", "36": "B", "46": "B"},
    "36": {"05": "1", "14": "B", "15": "B", "24": "2", "25": "B"},
    "46": {"05": "2", "13": "1", "15": "B", "23": "B", "25": "B"},
}


def is_matching(s: frozenset[tuple[int, int]]) -> bool:
    return len(set().union(*map(set, s))) == 2 * len(s)


def main() -> None:
    moser = {
        edge(x)
        for x in ("01", "02", "03", "04", "12", "16", "26", "34", "35", "45", "56")
    }
    q = {
        pair
        for pair in combinations(range(7), 2)
        if pair not in moser
    }
    doubles = {
        frozenset(pair)
        for pair in combinations(q, 2)
        if is_matching(frozenset(pair))
    }
    triples = {
        frozenset(pair)
        for pair in combinations(q, 3)
        if is_matching(frozenset(pair))
    }

    assert E1 <= doubles | triples
    assert E2 <= doubles | triples
    assert not (E1 & E2)                         # higher-state exclusivity

    # Two-anchor coverage for every double state and on both sides.
    for d in doubles:
        extensions = {d} | {t for t in triples if d <= t}
        assert E1 & extensions
        assert E2 & extensions

    assert set(map(edge, SUPPORT)) == q
    for repeated_text, row in SUPPORT.items():
        repeated = edge(repeated_text)
        expected = {e for e in q if set(e).isdisjoint(repeated)}
        assert set(map(edge, row)) == expected
        assert set(row.values()) <= {"1", "2", "B"}
        assert "1" in row.values() and "2" in row.values()  # no confinement

        # Unsupported on side s forces the double state on side s.
        for other_text, symbol in row.items():
            d = frozenset((repeated, edge(other_text)))
            if symbol == "1":
                assert d in E2
            elif symbol == "2":
                assert d in E1

        # Two unsupported disjoint pairs give commuting swaps/triple state.
        entries = list(row.items())
        for (x_text, x_symbol), (y_text, y_symbol) in combinations(entries, 2):
            x, y = edge(x_text), edge(y_text)
            if not set(x).isdisjoint(y):
                continue
            t = frozenset((repeated, x, y))
            if x_symbol == y_symbol == "1":
                assert t in E2
            if x_symbol == y_symbol == "2":
                assert t in E1

    # The two K_{2,3} traces are the exceptional binary patterns.  Every
    # other trace contains at least one bi-supported edge.
    assert "B" not in SUPPORT["05"].values()
    assert "B" not in SUPPORT["06"].values()
    for repeated in set(SUPPORT) - {"05", "06"}:
        assert "B" in SUPPORT[repeated].values()

    print("certificate valid")
    print("higher states:", len(E1), len(E2))
    print("support rows:", len(SUPPORT))


if __name__ == "__main__":
    main()
