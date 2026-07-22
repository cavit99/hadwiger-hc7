# Two adjacent bag pairs with at most two boundary defects force a `K_7` minor

**Status:** written proof; separate internal audit; computer-assisted finite
result.  This result does not prove `HC_7`.

## 1. Boundary and four-bag setting

Let `H` be a simple graph on a set `S` of order eight.  Assume

\[
 \alpha(H)\le3,
 \qquad K_4\not\preccurlyeq H-Z
       \quad\text{for every two-set }Z\subseteq S.       \tag{1.1}
\]

For \(j\in\{E,F\}\), choose an arbitrary set

\[
                         M_j\subseteq S,
                         \qquad |M_j|\le2.               \tag{1.2}
\]

Suppose a graph induces `H` on `S` and contains pairwise disjoint connected
sets

\[
                         A_E^0,A_E^1,A_F^0,A_F^1         \tag{1.3}
\]

disjoint from \(S\cup\{u\}\) such that:

1. `A_E^0` is adjacent to `A_E^1`, and `A_F^0` is adjacent to `A_F^1`;
2. each `A_E^k` is adjacent to every vertex of `S-M_E`, and each `A_F^k`
   is adjacent to every vertex of `S-M_F`; and
3. `u` is adjacent to every vertex of `S`.

No adjacency between an `E`-set and an `F`-set is assumed.

## 2. Finite four-anchor allocation

### Theorem 2.1 (four-bag completion)

Every graph satisfying Section 1 contains a `K_7` minor.

### Computer-assisted finite proof

The verifier
[`hc7_degree8_two_defect_component_closure_verify.py`](hc7_degree8_two_defect_component_closure_verify.py)
reads the complete unlabelled order-eight graph catalogue from nauty
`geng`.  It retains exactly the graphs satisfying (1.1), including the
odd wheel, and ranges over all 37 subsets of order at most two for each of
`M_E,M_F`.  An arbitrary labelled instance is isomorphic to one of these
catalogue instances, and the isomorphism carries its missed sets and any
resulting minor model with it.

For each retained graph and ordered missed-set pair it finds six distinct
boundary vertices

\[
                    a_E^0,a_E^1,a_F^0,a_F^1,r,s          \tag{2.1}
\]

such that the seven sets

\[
 A_E^0\cup\{a_E^0\},\quad A_E^1\cup\{a_E^1\},\quad
 A_F^0\cup\{a_F^0\},\quad A_F^1\cup\{a_F^1\},\quad
 \{r\},\quad\{s\},\quad\{u\}                          \tag{2.2}
\]

are connected and pairwise adjacent under only the assumptions of
Section 1.  Concretely, the checker requires each anchor to avoid the
missed set of its own connected set.  For every cross-shore pair it then
checks that one connected set sees the other anchor, or that the two
anchors are adjacent in `H`.  It checks \(rs\in E(H)\) and, for each of the
four connected sets, that it sees each singleton directly or through its
anchor.  These conditions are exactly the 21 branch-set adjacencies in
(2.2).

The exhaustive counts are:

```text
order8_graphs 12346
compact_boundaries 185
missed_sets 37
tested_missed_set_orientations 253265
anchor_certificates 253265
anchor_certificate_sha256 882a558c46dfc7a6b68008a598dd0e30aed3d51b8b05f5e15bca1554ea863d44
failures 0
PASS degree8_two_defect_component_closure
```

Thus a certificate exists in every case.  The sets in (2.2) give the
claimed explicit `K_7`-minor model. \(\square\)

Run the verifier from the repository root with

```text
geng -q 8 | python3 results/hc7_degree8_two_defect_component_closure_verify.py
```

## 3. Universal connector--carrier entanglement and incidence coherence

Retain the setup of the audited
[aligned bilateral response-cycle theorem](hc7_degree8_aligned_pair_bilateral_cycle.md),
including its paths `P_E,P_F`.  Assume additionally that `G` is
seven-connected and has no `K_7` minor.  For \(Q\in\{E,F\}\), let
\(\mathcal D_Q\) be the components of

\[
                          G[Q-V(P_Q^\circ)],             \tag{3.1}
\]

and, for \(D\in\mathcal D_Q\), put

\[
                          m_D=|S-N_G(D)|.                \tag{3.2}
\]

The fixed closed-shore colourings induce, in opposite orders, the exact
partitions

\[
             I\mid T\mid\{p,q\},
 \qquad      I\mid T\mid\{p\}\mid\{q\}.               \tag{3.3}
\]

Call a nonempty connected set \(R\subseteq Q\) a **root connector** when
it has a neighbour at both `p,q`.  For \(B\in\{I,T\}\), a **`B`-carrier** is
a set \(K\subseteq Q\) for which \(G[B\cup K]\) is connected and contains
an edge.

### Theorem 3.1 (every root connector meets every block carrier)

For either shore `Q`, every root connector `R` intersects every `I`-carrier
and every `T`-carrier in `Q`.

### Proof

Suppose that `R` is disjoint from a `B`-carrier `K`, where `B` is one of
`I,T`, and let `A` be the other block.  We construct both partitions in
(3.3) on the closed shore opposite `Q`.

For the merged partition, simultaneously contract spanning trees in

\[
             A\cup\{u\},\qquad B\cup K,
             \qquad R\cup\{p,q\}.                     \tag{3.4}
\]

These are pairwise disjoint connected sets, each containing an edge.  Their
images form a triangle: edges from `u` give two adjacencies and a
root-to-`B` edge gives the third.  Six-colour the proper minor, retain the
colouring on the opposite open shore, and expand the three image colours
over `A,B,{p,q}`.  This gives the exact merged partition.

For the split partition, apply the audited
[root-connector reflection theorem](hc7_order8_root_connector_reflection.md)
with root connector `R`, carrier `K` for `B`, and carrier `{u}` for `A`.
It gives the exact split partition on the same opposite closed shore.
Choose the one matching the fixed response on the closed `Q`-shore.  The
two shore colourings glue to a six-colouring of `G-u`, and a colour absent
from the at most four boundary blocks extends to `u`.  This contradicts
`chi(G)=7`. \(\square\)

This strengthens the four incidence splits from the selected paths to
every literal root connector in either shore.

### Corollary 3.2 (every block carrier is a root separator)

For \(B\in\{I,T\}\), the vertex set of every `B`-carrier in `Q` separates
`p` from `q` in \(G[Q\cup\{p,q\}]\).  Consequently, if that graph contains
`k` internally vertex-disjoint `p`--`q` paths, every `I`-carrier and every
`T`-carrier has at least `k` vertices in `Q`.

### Proof

The open interior of every `p`--`q` path is a root connector, so
Theorem 3.1 says that a fixed block carrier meets every such path.  It is
therefore a `p`--`q` vertex separator.  Its intersections with internally
vertex-disjoint paths are distinct, proving the size bound. \(\square\)

This separator--carrier duality retains both the colouring role of the
independent block and the literal root-path geometry; it is stronger than
an attachment interval or an untagged path family.

### Lemma 3.3 (coherent missed pair)

Every \(D\in\mathcal D_Q\) misses at least one vertex of `I` and at least
one vertex of `T`.  If `m_D=2`, there is a pair

\[
                          M_Q=\{i_Q,t_Q\},
              \qquad i_Q\in I,\quad t_Q\in T,           \tag{3.5}
\]

such that \(N_G(D)\cap S=S-M_Q\).  Moreover the same pair `M_Q` works for
every member of \(\mathcal D_Q\) with `m_D=2`.

### Proof

The audited four-incidence-split corollary says that no component of
`G[Q-V(P_Q^\circ)]` can be adjacent to all of `I`, and likewise for `T`.
This proves the first assertion.  A component with `m_D=2` therefore
misses exactly one vertex from each triple and no other boundary vertex.

The split incidence graph on `I` induces a nontrivial partition of the
three vertices.  A component adjacent to two vertices of `I` puts those
two in one part.  If a second component were adjacent to a different
two-set, the two overlapping pairs would put all three vertices in one
incidence component, contrary to the split.  Hence all components with
`m_D=2` miss the same vertex of `I`.  The identical argument on `T`
proves (3.5). \(\square\)

### Lemma 3.4 (two components give two adjacent connected sets)

If \(\mathcal D_Q\) has two members `D_0,D_1` with
`m_{D_0}=m_{D_1}=2`,
then `Q` contains disjoint connected adjacent sets `A_Q^0,A_Q^1`, each
adjacent to every vertex of `S-M_Q`.

### Proof

Every component of `Q-V(P_Q^\circ)` has a neighbour on `P_Q^\circ`,
because `Q` is connected.  Choose such attachment vertices `x_0,x_1` for
`D_0,D_1`.

If `x_0=x_1`, put that vertex into the first connected set and leave
`D_1` as the second; the edge from `x_0` to `D_1` makes the sets adjacent.
If `x_0` and `x_1` are distinct, take the `x_0`--`x_1` subpath of `P_Q`
and split it across one of its edges.  Add the side containing `x_k` to
`D_k`.  The two resulting sets are disjoint, connected, and adjacent
across the split edge.  Each contains its original component and therefore
remains adjacent to every vertex of `S-M_Q` by Lemma 3.3. \(\square\)

## 4. Two-defect component closure

### Theorem 4.1

In a hypothetical counterexample, at least one of the two shores has at
most one component `D` of `G[Q-V(P_Q^\circ)]` with `m_D=2`.

### Proof

Suppose instead that both shores have two such components.  Apply
Lemma 3.4 in each shore.  The resulting four connected sets are pairwise
disjoint, the two sets in each shore are adjacent, and they have the
boundary neighbourhoods required in Section 1 with the possibly different
pairs `M_E,M_F`.  The compact boundary hypotheses (1.1) are supplied by
the audited full-component common-root reduction and the degree-eight
boundary classification.  Theorem 2.1 gives an explicit `K_7`-minor model,
contrary to the hypothetical-counterexample assumption. \(\square\)

## 5. Exact gain and limitation

The conclusion is independent of the order of attachments along either
path and does not require the two shores to miss the same pair.  Thus the
fourfold incidence-split residue has a genuine asymmetric survivor: after
orienting the shores, one shore contains at most one component missing
exactly two boundary vertices.  Every other post-path component on that
shore misses at least three boundary vertices.

This is not terminal.  Such components may have arbitrarily many contacts
with the path, and a component of `Q-V(P_Q^\circ)` is not an actual
component of `G-N_G[u]`.  Its neighbourhood therefore cannot be called a
strict same-host restart merely because it has order seven through nine.
The next theorem must use the components with at least three missed
boundary vertices, the one exceptional two-defect component, or the
operation-specific deletion kernels to force a terminal outcome.

## Inputs

- [degree-eight nonedge bipartition outside the odd wheel](hc7_degree8_nonedge_bipartition_classification.md)
- [operation-compatible bilateral paths and four incidence splits](hc7_degree8_aligned_pair_bilateral_cycle.md)
- [parallel-cycle incidence/carrier test](hc7_common_root_parallel_two_cycle_normalization.md)
