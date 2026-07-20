# Independent audit: compound-separator terminal-edge response barrier

**Verdict:** GREEN.

**Audited source:**
`barriers/hc7_order8_compound_separator_terminal_edge_barrier.md`

**Source SHA-256:**
`2fd4db50ed50143cc92731e69f65e39157adcc5f937d06429338669036cd0eba`

The only source change after the mathematical audit added the link to this
GREEN audit; the refuted statement and certificate are unchanged.

**Audited verifier:**
`barriers/hc7_order8_compound_separator_terminal_edge_barrier_verify.py`

**Verifier SHA-256:**
`1b8c05806045e5d8c82330ef4c021cb1f14e15e524c589aa71d9c3e7b2b473fc`

## Construction and colouring

The edge list in the source agrees with the verifier.  The displayed
split-root assignment is proper.  Under the merged-root trace, the four
vertices `8,9,10,11` induce a clique and each sees all three boundary
colours used on `X`, `Y`, and `{d,e}`.  They consequently have only the
three remaining palette colours available, which cannot colour their
`K_4`.  Deleting the terminal edge `8-12` changes none of those adjacencies,
so the merged trace remains nonextendible.  Exhaustive backtracking in the
verifier independently checks both nonextensions and the split extension.

## Support geometry

The two parts

```text
Q0={8,9,12}, Q1={10,11}
```

are connected and adjacent, and each is adjacent to every literal boundary
vertex.  Exhaustive subset enumeration gives exactly the displayed
inclusion-minimal root, `X`, and `Y` support families.  It verifies all
three pairwise cross-intersection statements inside each part and verifies
that there is no globally disjoint root/`X`/`Y` triple.

The set `A={8,9,12}` is an inclusion-minimal connected `X`-support, and
`B={11}` is an inclusion-minimal connected `Y`-support.  Their union meets
every root connector.  Vertex `12` is a leaf of `G[A]`, with unique
`A`-neighbour `8`, so `8-12` is genuinely a terminal support edge.

## Minor certificates

The verifier checks vertex and edge coverage, the tree property, and the
running-intersection axiom for both displayed tree decompositions.  Their
widths are five for the whole boundaried graph and two for the boundary.
Treewidth minor-monotonicity therefore excludes a `K_7` minor in the whole
graph and a `K_5` minor in the boundary.

The verifier was run independently and printed exactly:

```text
GREEN compound-separator terminal-edge response barrier
two S-full connected parts; all three local support families cross-intersect
minimal compound root separator A_X union B_Y has terminal edge 8-12
merged trace rejected before and after deleting 8-12
treewidth upper bounds: tw(G[S union R])<=5, tw(G[S])<=2
scope: no opposite shore, seven-connectivity, or contraction-critical host
```

## Scope

The source correctly limits the conclusion.  The construction has no
opposite shore and is not asserted to be seven-connected, seven-chromatic,
or contraction-critical.  It therefore does not refute the active
host-level disjunction.  It refutes the narrower inference that
minimal compound-separator geometry, pairwise cross-intersection and
`K_7`-minor exclusion force a terminal support edge to retain the selected
merged-root response.

No unresolved defect remains in the stated barrier.
