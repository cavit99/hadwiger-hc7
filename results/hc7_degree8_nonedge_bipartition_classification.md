# Degree-eight boundary alignment outside the odd wheel

**Status:** computer-assisted finite result; separate internal audit
**GREEN** in
[`hc7_degree8_nonedge_bipartition_classification_audit.md`](hc7_degree8_nonedge_bipartition_classification_audit.md).
This result does not prove `HC_7`.

## Theorem 1 (nonedge bipartition classification)

Let `H` be a simple graph on eight vertices such that

\[
                         \alpha(H)\le 3,                         \tag{1.1}
\]

and, for every two-set `Z subseteq V(H)`,

\[
                         K_4\not\preccurlyeq H-Z.                \tag{1.2}
\]

Then exactly one of the following holds.

1. There is a nonedge `pq` such that `H-{p,q}` is bipartite.
2. `H` is the odd wheel `K_1 vee C_7`.

In outcome 1, every bipartition

\[
                         V(H)-\{p,q\}=I\mathbin{\dot\cup}T       \tag{1.3}
\]

has

\[
 |I|=|T|=3,\qquad I,T\text{ independent},                       \tag{1.4}
\]

each of `p,q` has a neighbour in each of `I,T`, and there is an
`I`--`T` edge.

### Proof of the structural strengthening

The two sides in (1.3) are independent.  Condition (1.1) gives
`|I|,|T|<=3`; since their orders sum to six, both have order three.  If,
for example, `p` had no neighbour in `I`, then `I union {p}` would be an
independent four-set.  This proves all four root-to-block contacts, and an
`I`--`T` edge must exist because `I union T` is not independent.  \(\square\)

### Computer-assisted classification

The verifier
[`hc7_degree8_nonedge_bipartition_classification_verify.py`](hc7_degree8_nonedge_bipartition_classification_verify.py)
reads the complete unlabelled order-eight graph catalogue from nauty
`geng`.  It applies exact checks for (1.1), for a `K_4` minor in every
six-vertex induced subgraph, and for bipartiteness after deleting each
nonedge pair.

Of the `12,346` unlabelled graphs, exactly `185` satisfy (1.1)--(1.2).
Exactly `184` have a nonedge with bipartite remainder.  The sole exception
has graph6 code

```text
GCp`f{
```

and the verifier checks directly that it has one universal vertex and an
induced seven-cycle on the remaining vertices.  Hence it is
`K_1 vee C_7`.

Run from the repository root with

```text
geng -q 8 | python3 results/hc7_degree8_nonedge_bipartition_classification_verify.py
```

The expected output is

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

This completes the finite part of the proof.  \(\square\)

## Corollary 2 (the full two-component common-root boundary)

Assume the degree-eight full-component common-root outcome of the audited
[common-root exchange theorem](hc7_full_exterior_component_common_root_exchange.md):
`X=N_G(u)` has order eight and the two components `E,F` of `G-N[u]` are
both adjacent to every vertex of `X`.  Put `H=G[X]`.

Then either `H=K_1 vee C_7`, or there are `p,q,I,T` satisfying every
boundary hypothesis in Sections 1--2 of the audited
[concentrated-reserve response theorem](hc7_low_degree_concentrated_reserve_elimination.md):

\[
 X=I\mathbin{\dot\cup}T\mathbin{\dot\cup}\{p,q\},
 \qquad |I|=|T|=3,                                      \tag{2.1}
\]

where `I,T` are independent, `pq` is a nonedge, both roots contact both
blocks, and an `I`--`T` edge exists.

### Proof

The audited low-degree independence bound gives `alpha(H)<=3`.  Section 2
of the common-root exchange theorem proves (1.2): a `K_4` model in
`H-{z_1,z_2}`, together with the three full connected sets

\[
                         \{u\},\quad E,\quad F,
\]

and the two unused anchors `z_1,z_2`, lifts to an explicit `K_7`-minor
model.  Theorem 1 and its structural strengthening now apply.  \(\square\)

## Exact gain and limitation

The classification removes static endpoint/block alignment as a generic
degree-eight boundary obstruction: outside one explicit boundary graph, an
aligned nonedge and two independent triples always exist.  It does **not**
show that this nonedge is the endpoint pair of a normalized common-root
trace connector, that either shore supplies such a connector with the
required colouring-operation provenance, or that a carrier disjoint from
that connector exists.  The odd-wheel case also remains open at host level.

Consequently the next host theorem must couple one aligned pair to an
actual failed-lift sector, or close the odd wheel separately.  An arbitrary
choice of a normalized sector is insufficient: its two endpoints need not
be one of the aligned pairs supplied here.

## Computational trust boundary

The finite claim trusts nauty's complete unlabelled order-eight catalogue,
CPython, the graph6 parser, and the exact deletion/contraction search for
`K_4` minors imported from the separately retained order-eight boundary
census.  The verifier identifies counts and the unique exception; it is not
a proof-assistant certificate.  The elementary strengthening and the host
reduction are written arguments independent of the enumeration.

## Inputs

- [full exterior components force a common-root exchange](hc7_full_exterior_component_common_root_exchange.md)
- [low-degree exterior-component bounds](hc7_low_degree_exterior_component_bounds.md)
- [dual response from a connector and independent-block carrier](hc7_low_degree_concentrated_reserve_elimination.md)
