# Audit of the single-bridge span-inference barrier

**Verdict:** GREEN.

**Audited source:**
`barriers/hc7_single_bridge_span_inference_barrier.md`

**Audited SHA-256:**
`c03a5c52101fbf560d9cd39e2f9ab017dc53216b128dad728eba60967648a58b`

**Promoted source SHA-256:**
`1f9d4adf3900fb9fae3f5c2d8060514c7d564c5139bb6cdf7f9a0f4c619f1343`

**Verifier:**
`barriers/hc7_single_bridge_span_inference_barrier_verify.py`

**Verifier SHA-256:**
`7a3acca4b95bcc6cecb1e61d11950a6f971ca52783480e2103c28551b2fae97e`

The verifier changed only by removal of a trailing blank line; its executable
content is unchanged.

The promoted source revision changes only the status line and adds this
audit link.  The refuted statement, construction, verification command,
and exact scope are unchanged.

**Audit type:** independent internal mathematical and computational audit.
This is not external peer review and does not prove or refute `HC_7`.

## Host and bridge enumeration

The graph `C` consists of the six-cycle

```text
v0-v1-v2-v3-v4-v5-v0
```

and a vertex `a` adjacent to `v0,v1`.  It has seven vertices and nine
edges.  Deleting any one vertex leaves it connected, while deleting
`v0,v1` isolates `a`; hence its vertex-connectivity is exactly two.

Relative to the fixed path

```text
D=v0-v1-v2-v3-v4-v5,
```

the standard `D`-bridges are exactly:

1. the chord bridge `v0v5`; and
2. the component bridge with interior `{a}` and attachments `v0,v1`.

There are no other off-path vertices, chords, or component attachments.

## Failure of every individual test

The chord bridge spans the open segment `{v1,v2,v3,v4}`.  It contains the
`p`-portal `v1` but not the `q`-portal `a`; as a trivial bridge it has no
off-path component.

The component bridge has empty open span because its attachments are
consecutive.  Its interior `{a}` contains the `q`-portal but not the
`p`-portal.  Thus neither standard bridge has an interior or open span
meeting both portal sets, exactly as required by the negated bridge-local
premise.

Nevertheless

```text
d-v0-v5-e
p-v1-a-q
```

are vertex-disjoint paths with the prescribed terminal pairs.  The first
uses the chord bridge, while the second composes a vertex from the chord's
span with the other bridge's interior.  This refutes precisely the claimed
inference from failure of all individual bridge tests to failure of the
whole linkage.

## Computational check

The deterministic verifier was run with the documented command and
returned exactly:

```text
GREEN single-bridge span inference barrier
C: vertices=7 edges=9 connectivity=2
D-bridges: chord span={v1,v2,v3,v4} hits={p}; triangle interior={a} hits={q}
disjoint linkage: d-v0-v5-e ; p-v1-a-q
scope: bridge-local inference only; no HC7 criticality claim
```

Its assertions independently check connectedness, absence of cut vertices,
the existence of a two-vertex cut, both portal-hit sets, and disjointness of
the displayed linkage.

## Trust boundary

The example is neither seven-connected nor embedded in a hypothetical
minor-minimal counterexample.  It does not refute the positive detour lemma,
the whole Two Paths theorem, or any operation-supported colouring result.
It establishes only that several standard `D`-bridges may compose into the
positive linkage even though no individual bridge passes either local
test.  The barrier states this scope exactly.

Within this scope, no gap was found.
