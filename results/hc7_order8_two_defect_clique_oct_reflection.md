# Reflection across an order-eight boundary with two complementary one-defect supports

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_two_defect_clique_oct_reflection_audit.md`](hc7_order8_two_defect_clique_oct_reflection_audit.md).
This theorem is unbounded in the orders of both open shores.  It
does not prove `HC_7`; its intended use is to eliminate the adjacent
feedback-pair branch of the strict-reversal order-eight configuration.

## 1. Setting

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
 \qquad L,R\ne\varnothing,
 \qquad |S|=8.                                      \tag{1.1}
\]

Assume that every proper minor of `G` is six-colourable.  Let `d,e` be
distinct vertices of `S` such that

\[
 de\in E(G[S])
 \quad\hbox{and}\quad
 G[S-\{d,e\}]\text{ is bipartite}.                  \tag{1.2}
\]

Suppose `L` contains disjoint connected subgraphs `A_d,A_e` satisfying

\[
 N_G(A_d)\cap S=S-\{d\},
 \qquad
 N_G(A_e)\cap S=S-\{e\},                            \tag{1.3}
\]

and `R` contains disjoint connected subgraphs `Q_1,Q_2`, each adjacent to
every literal vertex of `S`.

Finally assume that `G[S]` contains two vertex-disjoint odd cycles.  The
last hypothesis is used only to ensure that `d` and `e` each see both
classes of the bipartition in (1.2).

## 2. Common-partition theorem

### Theorem 2.1

Under the hypotheses above, `G` is six-colourable.

### Proof

Let

\[
                         S-\{d,e\}=X\mathbin{\dot\cup}Y            \tag{2.1}
\]

be a bipartition.  The two disjoint odd cycles must each meet
`\{d,e\}`, because their deletion leaves a bipartite graph.  Disjointness
then permits us to name them so that one contains `d` and not `e`, while
the other contains `e` and not `d`.

Deleting `d` from the first odd cycle leaves a path of odd length between
the two neighbours of `d` on that cycle.  Its ends therefore lie in
opposite classes of (2.1).  Thus `d` has a neighbour in each of `X,Y`.
The same argument on the second cycle shows that `e` has a neighbour in
each class.  In particular `X,Y` are nonempty.

Consider the boundary partition

\[
                         \Pi=X\mid Y\mid\{d\}\mid\{e\}.             \tag{2.2}
\]

Its four blocks are independent by (1.2).

First construct a colouring of the closed `R`-shore.  In the opposite
open shore `L`, contract a spanning tree of each of

\[
                         A_d\cup X,
                         \qquad A_e\cup Y.             \tag{2.3}
\]

Both sets are connected by (1.3), disjoint, and their images together
with the unchanged vertices `d,e` form a clique of order four.  Indeed,
`A_d` is adjacent to every vertex of `Y`, so the two images are adjacent;
each of `d,e` has a boundary neighbour in each of `X,Y`; and `de` is an
edge.  The contractions produce a proper minor.  Six-colour that minor,
restrict to `G[R\cup S]`, and give every vertex of `X` or `Y` the colour
of its contraction image.  This is a proper colouring and induces exactly
`\Pi` on `S`.

For the reverse direction, use the two boundary-full subgraphs in `R`.
Contract spanning trees of

\[
                         Q_1\cup X,
                         \qquad Q_2\cup Y.             \tag{2.4}
\]

The two images are adjacent because `Q_1` has a neighbour in the nonempty
block `Y` (and symmetrically `Q_2` has one in `X`).  Boundary-fullness
makes each image adjacent to `d,e`, while `de` is an edge.  Thus these
images and `d,e` again form a four-clique in a proper minor.  A
six-colouring restricts and expands to a proper colouring of `G[L\cup S]`
which also induces exactly `\Pi`.

Permute the six colour names on one closed shore so that the two
colourings agree on the four blocks of `\Pi`.  Since there is no edge
between `L` and `R`, they glue to a proper six-colouring of `G`. \(\square\)

## 3. A short-cycle allocation and the strict-reversal consequence

### Lemma 3.1 (two full subgraphs, two one-defect subgraphs, and a short cycle)

Let `S` have order eight.  Suppose `Q_1,Q_2,A_d,A_e` are pairwise
disjoint connected subgraphs outside `S`, where `Q_1,Q_2` are adjacent to
every vertex of `S`, `A_d` is adjacent to every vertex of `S-\{d\}`,
`A_e` is adjacent to every vertex of `S-\{e\}`, and `A_d,A_e` are
adjacent.  If `G[S-\{d,e\}]` contains a cycle on at most four vertices,
then `G` contains a `K_7` minor.

#### Proof

Let `O` be such a cycle.  Contract its edges into three nonempty connected
pairwise adjacent branch sets `O_1,O_2,O_3`.  At least two vertices
`x_1,x_2` remain in `S-(V(O)\cup\{d,e\})`.  The seven branch sets

\[
 Q_1\cup\{x_1\},\quad Q_2\cup\{x_2\},\quad
 A_d,\quad A_e,\quad O_1,\quad O_2,\quad O_3           \tag{3.1}
\]

are connected and pairwise disjoint.  The first two are adjacent to each
other because each `Q_i` sees the other anchor.  They are adjacent to
`A_d,A_e` through `x_1,x_2`, and to every `O_j` by boundary-fullness.
The two one-defect subgraphs are adjacent by hypothesis and see every
vertex of `O` because the cycle avoids `d,e`.  Finally the `O_j` are
pairwise adjacent by construction.  Thus (3.1) is a `K_7`-minor model.
\(\square\)

### Corollary 3.2

Assume that `G` is seven-connected, is not six-colourable, has no `K_7`
minor, and every proper minor of `G` is six-colourable.  Let `S` have order
eight and suppose that `G-S` has exactly three components, each adjacent to
every literal vertex of `S`.  Suppose one component is the induced path in
the [overlapping-interval normal form](hc7_order8_overlapping_interval_normal_form.md),
and let `d,e` be the two missed boundary vertices in its strict-reversal
case.  Suppose no actual order-seven separation has already been returned.

If `G` is not six-colourable and has no `K_7` minor, then both of the
following restrictions hold:

\[
 G[S-\{d,e\}]\text{ has no cycle of order at most four},             \tag{3.2}
\]

and, whenever `G[S-\{d,e\}]` is bipartite,

\[
                         de\notin E(G).                              \tag{3.3}
\]

### Proof

Use the notation `b<a` from the strict-reversal normal form.  Choose an
integer `k` with `b<=k<a` and put

\[
                         A=P[0,k],\qquad B=P[k+1,m].
\]

These subpaths are nonempty, disjoint, connected, and adjacent through the
edge `p_kp_{k+1}`.  The first contains the full one-defect tail `P[0,b]`,
and the second contains `P[a,m]`; hence `A` is adjacent to every vertex of
`S-\{d\}` and `B` to every vertex of `S-\{e\}`.  Moreover
`k<a=\ell(d)` and `k>=b=r(e)`, so `A` has no neighbour at `d` and `B` has
no neighbour at `e`.  The other two components of `G-S` are disjoint and
boundary-full by hypothesis.

The audited [three-component boundary classification](hc7_order8_three_component_boundary_classification.md),
Theorem 4.1, applies in this counterexample setting and shows that `G[S]`
contains two vertex-disjoint odd cycles.

Lemma 3.1 excludes every cycle of order at most four, proving (3.2).  If
the remaining boundary graph is bipartite and `de` is an edge, the two
disjoint odd cycles in `G[S]` verify all hypotheses of Theorem 2.1, which
six-colours `G`.  This proves (3.3). \(\square\)

## 4. Trust boundary

Theorem 2.1 is a complete colouring-gluing theorem under its displayed
hypotheses.  It identifies no palette colour with a branch-set label.

Lemma 3.1 uses the short-cycle hypothesis exactly to leave two distinct
anchors outside the cycle and the two defects.  The note makes no claim
for a five- or six-cycle in `S-\{d,e\}`.  It also does not close the
surviving nonadjacent feedback-pair geometry or the case in which
`G[S-\{d,e\}]` remains nonbipartite but has girth at least five.
