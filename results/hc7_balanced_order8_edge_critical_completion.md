# Edge-critical colouring and a two-path completion at the balanced order-eight boundary

**Status:** written conditional lemmas with a separate GREEN internal audit
in
[`hc7_balanced_order8_edge_critical_completion_audit.md`](hc7_balanced_order8_edge_critical_completion_audit.md).
The results below combine the promoted two-path completion with an
edge-critical colouring and isolate the remaining host-level obstruction.
They do not eliminate the balanced order-eight case or prove `HC_7`.

## 1. Setup

Let `G` be seven-connected, seven-chromatic, and `K_7`-minor-free, and
assume every proper minor of `G` is six-colourable.  Use the exact
order-eight configuration from
[`../active/hc7_balanced_order8_frontier.md`](../active/hc7_balanced_order8_frontier.md):

\[
 S=R\mathbin{\dot\cup}V(e)\mathbin{\dot\cup}V(f)
       \mathbin{\dot\cup}\{x\},\qquad |R|=3,
\]

where `R` is a clique, `e` and `f` are anticomplete edges, and each edge is
collectively adjacent to every vertex of `R`.  Let `C,D` be the two
components of `G-S`; each is adjacent to every vertex of `S`.

Write

\[
                         L=R\cup\{\ell_e,\ell_f\}
\]

for the original five-clique.  Thus `ell_e,ell_f in C`, the edge `e` is
anticomplete to `ell_e` and collectively adjacent to
`L-{ell_e}`, while `f` is anticomplete to `ell_f` and collectively
adjacent to `L-{ell_f}`.

Let `Y` be the second five-clique supplied by the star reduction.  The
[promoted rooted-web theorem](hc7_star_order_eight_rooted_web.md)
places every vertex of `Y-S` in `D`; moreover
`Y` is disjoint from `L`, and its boundary vertices lie among
`V(e) union V(f) union {x}`.  Since `e,f` are anticomplete, `Y` meets the
endpoints of at most one of these two edges.

An **actual order-seven separation** below means a separation with both
open sides nonempty and separator order seven.

## 2. The two nontrivial Kempe components

### Lemma 2.1

There is a proper six-colouring `phi` of
`G-ell_e ell_f` with the following properties.

1. `phi(ell_e)=phi(ell_f)=alpha`.
2. The three vertices of `R` receive three distinct colours, none equal to
   `alpha`.
3. Let `gamma,delta` be the two colours absent from `L` in this colouring.
   For each `theta in {gamma,delta}`, the `alpha`--`theta` Kempe component
   containing `ell_e` also contains `ell_f`.

#### Proof

The edge deletion is a proper minor and hence is six-colourable.  Its two
ends must receive the same colour, since otherwise the colouring would be
a six-colouring of `G`.  The remaining assertions about the colours on
`L` follow because `L` is a five-clique in `G`.

Fix a colour `theta!=alpha`.  If the two leaves belonged to different
`alpha`--`theta` components, interchange `alpha` and `theta` on the
component containing `ell_e`.  This remains a proper six-colouring of the
edge-deleted graph, but it gives the two leaves different colours and
therefore extends over the deleted edge.  That would six-colour `G`, a
contradiction.  Apply this to the two colours absent from `L`.  \(\square\)

For the three colours used on `R`, the corresponding connections may be
the two-edge paths through the vertices of `R`.  The components for
`gamma,delta` are the two genuinely new host subgraphs furnished by the
edge-critical colouring.

## 3. The promoted two-path completion

The exact branch-set construction is now proved and audited separately in
[`hc7_star_order_eight_split_edge_completion.md`](hc7_star_order_eight_split_edge_completion.md).
In the notation above it says that a `K_7` minor exists if `C` contains
vertex-disjoint connected subgraphs `P,Q` such that

\[
 \ell_f\in V(P),\quad P\text{ has a neighbour at }x,
 \qquad
 \ell_e\in V(Q),\quad Q\text{ has a neighbour in }V(e).       \tag{3.1}
\]

Its seven branch sets are the three singleton vertices of `R`, the edge
`e`, the subgraph `P` with `x` absorbed, the subgraph `Q` with one endpoint
of `f` absorbed, and `D` with the other endpoint of `f` absorbed.  The
symmetric conclusion holds after interchanging `e,ell_e` with
`f,ell_f`.

## 4. What deleting the two clique leaves forces

### Theorem 4.1 (contact structure after deleting the leaves)

Assume that `G` has neither a `K_7` minor nor an actual order-seven
separation.  Let `A` be a component of

\[
                         C-\{\ell_e,\ell_f\},
\]

and let `t(A)` be the number of the two leaves adjacent to `A`.  Then:

1. `t(A) in {1,2}`;
2. `|N_G(A) cap S| >= 8-t(A)`; and
3. `A` is nonadjacent to at least one vertex of `R union {x}`.

Consequently:

- if `t(A)=1`, then `A` is adjacent to exactly seven vertices of `S` and
  its unique missed boundary vertex lies in `R union {x}`;
- if `t(A)=2`, then `A` is adjacent to six or seven vertices of `S`, and
  its set of missed boundary vertices has order one or two and meets
  `R union {x}`.

#### Proof

The graph `C` is connected, so every component left after deleting its two
leaf vertices is adjacent to at least one of them.  Since `C` is a
component of `G-S`,

\[
 N_G(A)=\bigl(N_G(A)\cap S\bigr)
        \mathbin{\dot\cup}
        \bigl(N_G(A)\cap\{\ell_e,\ell_f\}\bigr).     \tag{4.1}
\]

The set in (4.1) separates `A` from the nonempty opposite component `D`.
Seven-connectivity makes its order at least seven, and exclusion of an
actual order-seven separation makes its order at least eight.  This proves
the first two assertions.

Suppose instead that `A` is adjacent to every vertex of `R union {x}`.
The lower bound just proved implies that `A` has a neighbour in at least
one of the two edges `e,f`; call such an edge `g`, and call the other edge
`h`.  The following seven sets are pairwise disjoint and connected:

\[
 \{r\}\ (r\in R),\qquad
 V(g),\qquad
 V(h)\cup\{\ell_e,\ell_f\},\qquad
 A\cup\{x\},\qquad D.                                \tag{4.2}
\]

The set containing `h` is connected because `h` is adjacent to the leaf
which it does not omit, and the two leaves are adjacent.  The component
`A` is adjacent to at least one leaf, so its branch set is adjacent to the
`h`-and-leaves branch set.  It is adjacent to `g` by the choice of `g`, to
every singleton from `R` by assumption, and to `D` through `x`.  Fullness
of `D`, collective adjacency of `g,h` to `R`, and the clique edges in `L`
supply every remaining adjacency.  Thus (4.2) is a `K_7`-minor model, a
contradiction.  This proves assertion 3.

If `t(A)=1`, the first two assertions give at least seven boundary
neighbours, while assertion 3 rules out all eight.  If `t(A)=2`, they give
at least six boundary neighbours, while assertion 3 again rules out all
eight.  The two displayed consequences follow. \(\square\)

### Corollary 4.2

Under the hypotheses of Theorem 4.1, if either nontrivial Kempe component
from Lemma 2.1 contains an `ell_e`--`ell_f` path wholly inside `C`, the
interior of that path lies in a single component `A` of
`C-{ell_e,ell_f}`.  This component is adjacent to both leaves, is adjacent
to at least six boundary vertices, and misses one or two boundary vertices,
at least one of which belongs to `R union {x}`.

#### Proof

The internal vertices of a path in `C` avoiding its two ends lie in one
component after the ends are deleted.  Apply Theorem 4.1 with `t(A)=2`.
\(\square\)

### Corollary 4.3 (the exact residual linkage)

Continue under the hypotheses of Theorem 4.1.  Let `A` be a component of
`C-{ell_e,ell_f}` adjacent to both leaves and to `x`.  Then `A` has a
neighbour in at least one of `e,f`; say it has a neighbour in `e`.  Form an
auxiliary graph from `G[A union {ell_e,ell_f}]` by adding two terminal
vertices `x^*` and `e^*`, adjacent respectively to the vertices of `A`
which have neighbours at `x` and in `V(e)`.  This auxiliary graph has no
linkage joining

\[
                    (\ell_f,x^*)\quad\hbox{and}\quad
                    (\ell_e,e^*).                    \tag{4.3}
\]

The analogous statement holds with `e,f` interchanged.

#### Proof

Theorem 4.1 gives `|N_G(A) cap S|>=6`.  Since `A` is adjacent to `x` and
there are only three vertices in `R`, it has a neighbour in at least two
of the four endpoints of `e,f`, and hence contacts at least one of those
edges.

A linkage in (4.3), with the two added terminal vertices deleted from its
paths, gives the two vertex-disjoint connected subgraphs in (3.1), both
contained in `C`.  The promoted split-edge completion would then give a
`K_7` minor, contrary to the setup. \(\square\)

## 5. The exact common-colouring exit

Let `Pi_phi` be the partition of `S` into the colour classes induced by the
edge-deletion colouring `phi` from Lemma 2.1.

### Lemma 5.1 (returning the edge-deletion boundary partition)

Let `mu` be any proper minor operation supported entirely in `D` and not
identifying a vertex of `D` with a boundary vertex.  If `G mu` has a
six-colouring whose induced partition of `S` is `Pi_phi`, then `G` is
six-colourable.

#### Proof

The operation `mu` does not alter `G[C union S]`, so the new colouring
restricts to a proper six-colouring of that closed shore, including the
edge `ell_e ell_f`.  The old colouring `phi` restricts to a proper
six-colouring of `G[D union S]`, since its only monochromatic host edge is
`ell_e ell_f`, which lies in `C`.

The two boundary colourings induce the same partition.  A permutation of
the six colour names therefore makes them agree on every vertex of `S`.
Gluing the two closed-shore colourings then gives a proper six-colouring of
`G`, a contradiction. \(\square\)

Thus, in a hypothetical counterexample, the host-realized partition
`Pi_phi` is excluded from every proper-minor response supported internally
in `D`.  This is stronger than disjoint abstract boundary-extension
languages: it couples one fixed colouring of the unmodified `D`-shore to
all proper-minor colourings of the opposite closed shore.

### Lemma 5.2 (opposite internal-edge witnesses have different traces)

More generally, let `uv` be an edge with both ends in `C` and let `yz` be
an edge with both ends in `D`.  No six-colouring of `G-uv` and
six-colouring of `G-yz` induce the same partition of `S`.

#### Proof

Suppose `phi_C` colours `G-uv`, `phi_D` colours `G-yz`, and their boundary
partitions agree.  After permuting colour names, use `phi_D` on
`G[C union S]` and `phi_C` on `G[D union S]`.  The first restriction is
proper on the original `C`-shore because only the edge in `D` was deleted;
the second is proper on the original `D`-shore because only the edge in
`C` was deleted.  They agree on `S` and hence glue to a six-colouring of
`G`, a contradiction. \(\square\)

### Corollary 5.3 (two opposite edge locks)

The second five-clique `Y` contains adjacent vertices `y_1,y_2 in D`.
Consequently the two edge-deleted graphs

\[
              G-\ell_e\ell_f\qquad\hbox{and}\qquad G-y_1y_2
                                                               \tag{5.1}
\]

have six-colourings with different boundary partitions.  In the first
colouring, Lemma 2.1 gives two nontrivial bichromatic components joining
`ell_e,ell_f`.  In the second, the analogous argument gives two
nontrivial bichromatic components joining `y_1,y_2`, for the two colours
absent from `Y`.

#### Proof

The clique `Y` is disjoint from `L`, so it contains no vertex of `R`.
Because `e,f` are anticomplete, `Y` meets the endpoints of at most one of
them; it may additionally contain `x`.  Thus `|Y cap S|<=3`.  The other
at least two vertices of the five-clique lie in the `Y`-side component
`D`, and any two of them are adjacent.  Choose these as `y_1,y_2`.

Both edge deletions in (5.1) are proper minors and hence six-colourable.
Their boundary partitions differ by Lemma 5.2.  Applying the proof of
Lemma 2.1 to the edge `y_1y_2` inside the five-clique `Y` gives the final
Kempe-component assertion. \(\square\)

## 6. Exact remaining obstruction

The positive continuation can now be stated without treating the two
Kempe paths as if they were already a rooted minor model.  One must prove
at least one of the following host-level assertions:

1. the two nontrivial Kempe components from Lemma 2.1 yield one of the
   promoted two-path configurations in Section 3;
2. their failure yields an actual order-seven separation preserving the
   named edges and cliques;
3. a proper-minor operation in `D` returns `Pi_phi`, invoking Lemma 5.1; or
4. the near-full components classified by Theorem 4.1 can be combined into
   the two paths in (3.1).

Corollary 5.3 adds a second, incompatible edge-lock partition on the
opposite shore.  The remaining matching-specific task is to show that the
four exact traces supplied by a perfect matching of
`overline{G[S]}` force a transition between these two host partitions, or
else force the linkage (3.1) or an actual order-seven separation.  Merely
placing both partitions in an abstract boundary language would discard the
edge and shore on which each one is proper.

The quotient-level example in
[`../barriers/hc7_balanced_order8_two_missing_colour_paths.md`](../barriers/hc7_balanced_order8_two_missing_colour_paths.md)
shows that the mere existence of the two leaf-to-leaf Kempe paths does not
force item 1.  In that example the required paths also fail when restricted
to the clique-side component behind the canonical three-vertex cut.  A
positive theorem must therefore use the four literal endpoints of `e,f`,
seven-connectivity, or the proper-minor transition in Lemma 5.1.
