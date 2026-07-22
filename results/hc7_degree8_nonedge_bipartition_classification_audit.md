# Audit: degree-eight nonedge bipartition classification

**Audit type:** separate internal cold audit with independent finite
cross-check

**Verdict:** **GREEN**

Audited theorem:
[`hc7_degree8_nonedge_bipartition_classification.md`](hc7_degree8_nonedge_bipartition_classification.md)

Theorem SHA-256:

```text
419afe10c231d5f4823702f70b4b28099424eed1d159ac885b2f1aab0178b5e3
```

The status-only promotion after this audit has source SHA-256

```text
e2483c23f73e786ce5a32693ef13810f9e3657511c6b178f5d5a1572e5adad9a
```

and changes no mathematical statement or proof.

Audited verifier:
[`hc7_degree8_nonedge_bipartition_classification_verify.py`](hc7_degree8_nonedge_bipartition_classification_verify.py)

Verifier SHA-256:

```text
c01f145349831eb34f3af0ef772c6fe07d82b4b00f9630cabe9ba557eb0be8a9
```

This is an internal audit, not external peer review or a proof-assistant
certificate.  It does not prove `HC_7`.

## Independent finite check

Running the documented command against nauty's complete unlabelled
order-eight catalogue reproduced the recorded output exactly:

```text
order8_graphs 12346
compact_boundaries 185
compact_boundary_sha256 f01bd67668c56deab10ad02ae9c05fa58b38c1235d3b34bb1129880ccc5a1ff9
aligned_nonedge_boundaries 184
exceptions 1
exception_graph6 GCp`f{
exception_sha256 0637152b1890aa89c1ee354c0036dc0929715fcc94e182deb4b851279f66aab0
exception_structure K1_join_C7
PASS degree8_nonedge_bipartition_classification
```

The verifier's input wrapper was checked in both supported modes.  With
stdin at EOF, running the script directly invokes `geng -q 8`; with the
catalogue piped explicitly, it retains the first input line and streams the
remainder.  Both invocations exited successfully and produced byte-identical
output, including both digests above.  The wrapper waits for the generated
catalogue process and raises an error on a nonzero exit.  It does not alter
any classification predicate.

I also reran the classification with a separate `K_4`-minor test.  Rather
than importing the verifier's deletion/contraction recursion, this check
enumerated every choice of four nonempty pairwise disjoint connected branch
sets in each six-vertex remainder and tested all six required adjacencies.
It independently returned `12,346` input graphs, `185` graphs satisfying
the two hypotheses, `184` aligned graphs, and the sole exception
``GCp`f{``.  Reversing catalogue order and a separate direct structural check
gave the same exception and confirmed that it has one universal vertex and
an induced connected two-regular graph on the other seven vertices, hence
is `K_1` joined to `C_7`.

## Encoding and theorem correspondence

The verifier's predicates match the theorem exactly.

- `has_independent_four` is true precisely when `alpha(H)>=4`, so its
  negation is (1.1).
- `has_compact_k4` examines all 28 two-vertex deletions.  Its cached
  deletion/contraction recursion is exhaustive for a `K_4` minor, so its
  negation is (1.2).
- `aligned_nonedges` ranges over exactly the nonedges `pq` and performs an
  ordinary two-colouring test on `H-{p,q}`.  Nonemptiness is outcome 1.
- The graph6 decoder and encoder round-trip the order-eight catalogue.  The
  imported implementation is the separately retained boundary-census
  verifier at SHA-256
  `d4677fcd39be4e4411176b8c916ae637057d34a70758ba3bbde70ed16badd68e`,
  matching its GREEN audit.
- The exception predicate requires exactly one degree-seven vertex and a
  connected two-regular graph on the other seven vertices.  This is exactly
  `K_1` joined to `C_7`, not merely a graph with the same degree sequence.

The unique exception has no aligned nonedge, so the two stated outcomes are
exclusive as well as exhaustive.

## Written strengthening

If `H-{p,q}` is bipartite, each side of any bipartition is independent.
The two sides have total order six, while `alpha(H)<=3` bounds each by
three; hence both have order three.  If either root missed either side,
that root together with the side would be an independent four-set.  Thus
both roots contact both sides.  Finally, no edge between the two sides
would make their six-vertex union independent.  The strengthening uses no
unstated uniqueness or connectedness of the bipartition.

## Host corollary

The degree-eight full-component common-root outcome supplies an
eight-vertex boundary `H=G[N(u)]` with two connected exterior components
full to the boundary.  The audited low-degree bound gives
`alpha(H)<=3`.  Section 2 of the audited common-root exchange theorem gives
condition (1.2): a `K_4` model in `H-{z_1,z_2}` combines with `{u}` and the
two full components anchored at `z_1,z_2` to form seven disjoint pairwise
adjacent branch sets, contradicting the host's `K_7`-minor exclusion.

Theorem 1 therefore applies.  Outside the odd wheel it supplies a nonedge,
two independent triples, all four root-to-block contacts, and an edge
between the triples.  These are exactly the **boundary** hypotheses claimed
in Corollary 2.  The corollary does not import or assert the separate
connector and carrier existence from Section 2 of the concentrated-reserve
theorem.

## Trust boundary and unresolved scope

The finite conclusion depends on nauty `geng` being a complete unlabelled
order-eight catalogue, CPython executing the verifier, and the exact graph6
and minor predicates checked above.  The retained hashes make the run
reproducible, but the output is not a formal proof certificate.

No internal gap was found.  The theorem supplies static boundary alignment
only.  It does not make the selected nonedge the endpoints of a normalized
trace connector, retain colouring-operation provenance, produce a carrier
disjoint from such a connector, close the odd-wheel host case, construct a
`K_7`-minor model, or prove `HC_7`.
