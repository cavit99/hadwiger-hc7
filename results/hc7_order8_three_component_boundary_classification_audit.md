# Independent audit: three-component order-eight boundary classification

**Verdict:** **GREEN** for the written host reductions and the stated finite
classification, within the trust boundary below.  This is a separate internal
audit, not external peer review.  The result does not close the
three-component interface.

## Audited revisions

- theorem note:
  `results/hc7_order8_three_component_boundary_classification.md`
- theorem SHA-256:
  `1d976b6ece78b66c08a87df36cfc3f31a3e8511d57aa6990aeaa28c7c67c76b3`
- verifier:
  `results/hc7_order8_three_component_boundary_verify.py`
- verifier SHA-256:
  `d4677fcd39be4e4411176b8c916ae637057d34a70758ba3bbde70ed16badd68e`

The revision change since the original audit is metadata-only promotion from
`active/` to `results/`, together with the corresponding invocation-path
update.  The theorem statements, proofs, classification predicates, and
verification algorithms are unchanged.  The promoted revisions were
rechecked at the new paths before this audit was repinned.

## Written reductions

Lemma 2.1 is correct.  A `K_4` model in `H-Z`, together with three full
components and the two vertices of `Z`, gives the seven disjoint connected
sets displayed in (2.2).  Fullness supplies every adjacency involving the
first three sets, including all three pairwise adjacencies between them.
Thus the absence of a `K_7` minor is exactly enough to exclude every `K_4`
model of `H` supported on at most six boundary vertices.

Lemma 3.1 is also correct.  A clique odd-cycle transversal `U` gives at most
two nonempty independent sets `P,Q`; the absence of a boundary `K_4` gives
`|U|<=3`.  For each component `C` of `G-X`, two other full components can be
contracted with `P` and `Q`.  Their images and the vertices of `U` form a
clique in a proper minor, so a six-colouring pulls back to `G[C\cup X]` with
the exact boundary partition (3.2).  These component-side colourings can be
permuted to agree on the literal boundary and then glued because distinct
components of `G-X` are anticomplete.

The demand identity used after Lemma 3.1 is valid.  A boundary partition of
demand at most two leaves at most two independent blocks after deleting a
maximum clique of singleton blocks; conversely a clique odd-cycle
transversal and a bipartition of its complement give demand at most two.

## Verifier audit

The graph6 decoder and encoder use the standard upper-triangle bit order and
round-trip the complete input catalogue.  The colouring recursion is an
exhaustive DSATUR-ordered backtracking search.  Clique odd-cycle transversals
are checked over every vertex subset, with exact clique and bipartiteness
tests.

The `K_4`-minor routine is complete: a clique minor can be obtained using
vertex deletions and contractions of branch-set trees, without needing an
explicit edge-deletion branch.  Testing every two-vertex deletion therefore
is exactly the stated condition that no `K_4` model is supported on at most
six boundary vertices.  The odd-cycle routine enumerates induced cycles;
this is sufficient because every odd cycle contains an induced odd cycle.
The three-colour partition recursion is a restricted-growth enumeration, so
it counts each unlabelled equality partition exactly once.  The edge-minimal
test checks every single-edge deletion against the same three residual
conditions.

The prescribed normal and optimized runs both reproduced the displayed
output, including 12,346 input graphs, 82 survivors, five edge-minimal codes,
and digest
`f415269d09d9b0673b030a2125cd20a15b46a20c202463bf20d70864179e68fc`.
The normal run enforces the detailed expected spectrum through assertions.
Under `python -O` those assertions are disabled, so that run is a
reproducibility check rather than an independently self-checking certificate.

The post-promotion commands were

```text
geng -q 8 | python3 results/hc7_order8_three_component_boundary_verify.py
geng -q 8 | python3 -O results/hc7_order8_three_component_boundary_verify.py
```

and both again produced the exact displayed output and digest.

As an additional independent check, the central census was recomputed with
set-partition colouring and direct enumeration of four pairwise adjacent
connected branch sets on each six-vertex induced subgraph, rather than
DSATUR and contraction recursion.  It independently returned

```text
three-chromatic without clique OCT: 746
four-chromatic without clique OCT: 953
three-chromatic compact-K4-free survivors: 82
four-chromatic compact-K4-free survivors: 0
survivor-code sha256: f415269d09d9b0673b030a2125cd20a15b46a20c202463bf20d70864179e68fc
```

## Trust boundary and exact scope

The finite result trusts the standard completeness of `nauty`'s
`geng -q 8` unlabelled catalogue, the graph6 specification, the Python
runtime, and the audited verifier.  It enumerates only boundary graphs; it
does not replace an unbounded argument about component interiors.

The result proves that the surviving boundary graph is one of 82
three-colourable types with the listed finite properties.  It does **not**
force a proper-minor colouring to return a three-colour boundary partition,
does not synchronize the two shores, and does not itself produce either a
`K_7` minor or a six-colouring of the host graph.
