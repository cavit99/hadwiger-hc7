# The exact order-eight star boundary: a near-clique model and a trace-parity barrier

**Status:** written proofs plus a computer-assisted finite census, with a
separate GREEN internal audit in
[`hc7_star_order_eight_boundary_state_barrier_audit.md`](hc7_star_order_eight_boundary_state_barrier_audit.md).
The deterministic verifier is
[`hc7_star_order_eight_boundary_state_barrier_verify.py`](hc7_star_order_eight_boundary_state_barrier_verify.py).
This note does not prove the five-support star branch or Hadwiger's
conjecture for `t=7`.

## 1. Exact setup

Let `G` be a seven-connected graph with no `K_7` minor.  Suppose an
eight-vertex separator has the disjoint decomposition

\[
                 S=R\mathbin{\dot\cup}V(e)
                    \mathbin{\dot\cup}V(f)\mathbin{\dot\cup}\{x\},
                 \qquad |R|=3,                         \tag{1.1}
\]

where:

1. `R` is a clique;
2. `e` and `f` are disjoint edges with no edge between them; and
3. each of `e,f` is collectively adjacent to every vertex of `R`.

Assume every component of `G-S` is adjacent to every literal vertex of
`S`.  This is the exact untrimmed order-eight output of Lemma 6.1 in
[`../results/hc7_star_kernel_rooted_four_contraction.md`](../results/hc7_star_kernel_rooted_four_contraction.md).

## 2. Three complementary components are impossible

### Lemma 2.1

The graph `G-S` has at most two components.

#### Proof

Suppose `C_1,C_2,C_3` are distinct components and write `f=uv`.  The seven
sets

\[
 C_1\cup\{u\},\quad C_2\cup\{v\},\quad C_3\cup\{x\},
 \quad e,\quad \{r\}\ (r\in R)                       \tag{2.1}
\]

are disjoint and connected.  The first two are adjacent through `uv`.
The third is adjacent to each of them because `C_3` has a neighbour at
both `u` and `v` (equivalently, each of `C_1,C_2` has a neighbour at
`x`).  Full boundary adjacency makes each of the first three sets adjacent
to `e` and to every singleton in `R`.  Finally `e` is collectively
adjacent to every vertex of `R`, and `R` is a clique.  Thus (2.1) is an
explicit `K_7`-minor model, a contradiction. \(\square\)

This independently confirms the three-component construction in the
active contraction theorem; it uses the two endpoints of `f` as separate
anchors and retains `e` as one branch set.

## 3. The two-component residue is a spanning near-clique model

### Lemma 3.1

Suppose `G-S` has exactly two components `C,D`.  Then

\[
       C\cup\{x\},\quad D,\quad e,\quad f,
       \quad \{r\}\ (r\in R)                           \tag{3.1}
\]

is a spanning seven-branch-set model in which the unique missing
branch-set adjacency is the pair `e,f`.  Equivalently, `G` has a spanning
`K_7`-minus-one-edge minor model whose two nonadjacent branch sets are the
two specified boundary edges.

#### Proof

The seven displayed sets are disjoint, connected, and cover `V(G)`.  The
set `D` is adjacent to `C union {x}` through a neighbour of `x`.  Full
boundary adjacency makes both component-derived sets adjacent to `e`,
`f`, and every singleton in `R`.  Each of `e,f` is collectively adjacent
to all three vertices of `R`, and the singleton sets from `R` are pairwise
adjacent.  The only absent adjacency is between `e` and `f`, which are
anticomplete by hypothesis. \(\square\)

This is the immediate structural re-entry supplied by the order-eight
residue.  Any positive continuation can work directly with one named
missing adjacency in a spanning near-`K_7` model rather than with an
unstructured four-colour boundary.

## 4. Exact independent-set traces always admit a parity split

Let `H=G[S]`.  Let `Omega_6(H)` be the set of partitions of `S` into at
most six nonempty independent blocks.  For each nonempty independent set
`I` of `H`, define its exact trace cylinder

\[
       \mathcal T_I=\{\Pi\in\Omega_6(H): I\text{ is a block of }\Pi\}.
                                                               \tag{4.1}
\]

The hoped-for state-free argument would show that the hypergraph with
vertex set `Omega_6(H)` and hyperedges `T_I` is not two-colourable.  The
opposite is forced.

### Theorem 4.1 (block-count parity splits every trace cylinder)

Assume `H` is four-colourable and

\[
                         I_2\vee H\not\succcurlyeq K_7.          \tag{4.2}
\]

Under the boundary hypotheses in Section 1, colouring each partition in
`Omega_6(H)` by the parity of its number of blocks makes every
`T_I` bichromatic.

#### Proof

Fix a nonempty independent set `I`.  First, `H-I` is not complete.  If
`|I|<=3`, a complete `H-I` has at least five vertices and hence contains a
`K_5` on a proper subset of `S`.  If `a,b` are the two vertices of `I_2`
and `s in I`, the five clique vertices, `{a,s}`, and `{b}` form a `K_7`
minor in `I_2 vee H`, contrary to (4.2).

An independent set contains at most one vertex from each of the four
cliques

\[
                         R,\qquad e,\qquad f,\qquad \{x\}.
\]

Thus `|I|<=4`.  If `|I|=4`, it contains exactly one vertex from each of
these four sets.  The other endpoint of `e` and the other endpoint of `f`
both remain in `H-I`, and they are nonadjacent.  Hence `H-I` is again not
complete.

Put `q=chi(H-I)`.  Since `H` is four-colourable, `q<=4`.  Because `H-I`
is not complete, `q<|V(H-I)|`; an optimal `q`-colouring therefore has a
colour class of order at least two.  Its colour classes give a partition
of `H-I` into `q` independent blocks.  Splitting one nonsingleton colour
class gives another such partition with `q+1` blocks.  Adjoining `I` as
one exact block produces two members of `T_I` having `q+1` and `q+2`
blocks.  They have opposite parity and use at most six blocks because
`q<=4`.  Thus every trace cylinder is bichromatic. \(\square\)

Consequently, exact independent-block responses on both shores cannot by
themselves force a common boundary partition.  If two disjoint shore
extension languages are replaced by the two parity classes, those classes
are disjoint and each meets every exact trace cylinder.  Thus the cylinder
incidence conditions alone are consistent with disjoint languages.  A
positive argument must use coupled proper-minor transitions or the geometry
of the spanning near-clique model from Lemma 3.1.

## 5. Complete fixed-boundary census

Label

\[
 R=\{0,1,2\},\qquad e=34,\qquad f=56,\qquad x=7.
\]

There are `93,312` labelled boundary graphs satisfying exactly the required
and forbidden adjacencies of Section 1.  The natural contact symmetry group
has order 48: it permutes `R`, reverses each of `e,f`, and interchanges the
two edges.  The checker obtains:

```text
labelled candidates                         93312
contact-symmetry orbits                      2568
orbits with I2 join H K7-minor-free           899
ordinary graph-isomorphism types              710
```

The minor test uses the following exact reduction:

\[
 I_2\vee H\succcurlyeq K_7
 \quad\Longleftrightarrow\quad
 \bigl(H\succcurlyeq K_6\bigr)
 \text{ or }
 \bigl(H-v\succcurlyeq K_5\text{ for some }v\in V(H)\bigr).   \tag{5.3}
\]

For the forward direction, inspect a `K_7` model and the two nonadjacent
join vertices.  If at most one belongs to the model, or if both belong to
one branch set, the other six branch sets give a `K_6` model in `H`.  If
they belong to two different branch sets, at least one of those sets
contains a vertex `v` of `H`; the other five branch sets give a `K_5` model
in `H-v`.  Conversely, a `K_6` model in `H` can be augmented by one join
vertex, while a `K_5` model in `H-v` can be augmented by the two branch
sets `{a,v}` and `{b}`.  This proves (5.3), and the checker tests the
smaller clique minors by exhaustive deletion and contraction.

For every one of the 899 surviving contact orbits, the checker verifies
four-colourability and explicitly enumerates all independent-block
partitions to confirm Theorem 4.1.  It also tests two common static target
states:

* a perfect matching in `overline H`, equivalently a proper partition of
  `S` into four pairs; and
* a clique odd-cycle transversal in `H`, equivalently a clique `U` for
  which `H-U` is bipartite.

The exact contact-orbit counts are:

| clique OCT | complement perfect matching | count |
|---|---:|---:|
| yes | yes | 719 |
| yes | no  | 129 |
| no  | yes | 50  |
| no  | no  | 1   |

Thus neither target is uniform, and even their disjunction has one exact
exception.  Its edge set is

\[
\begin{split}
\{&01,02,03,04,05,06,07,12,14,16,23,26,34,37,47,56,57\}.
                                                               \tag{5.1}
\end{split}
\]

It has graph6 string `G|uFKw`; vertex `0` is universal.  The checker
certifies that it is four-chromatic, that `I_2 vee H` has no `K_7` minor,
that `overline H` has no perfect matching, and that deleting any clique
leaves chromatic number at least three.

The census also shows that the quotient alone cannot sharpen the literal
contact distribution in Lemma 3.1.  One surviving graph has only the
eleven edges

\[
 \{01,02,12,03,13,23,05,15,25,34,56\},               \tag{5.2}
\]

with `x=7` isolated.  All three vertices of `R` contact `e` only through
vertex `3` and contact `f` only through vertex `5`.  Hence target exclusion
does not force distinct boundary portals, any edge incident with `x`, or a
more distributed endpoint pattern inside the boundary graph.

## 6. Exact contribution and limitation

The useful positive output is Lemma 3.1: the entire two-component residue
is already a spanning `K_7`-minus-one-edge model with the missing pair
specified by two literal edge branch sets.

The finite census does not align the two shore extension languages, and it
must not be used to infer such alignment.  Theorem 4.1 proves a stronger
negative statement: the natural exact-trace hypergraph is uniformly
two-colourable throughout this boundary class.  The remaining proof must
therefore exploit information not present in the quotient, notably
seven-contraction-critical colour transitions inside the two components or
a label-preserving repair of the unique missing branch-set adjacency.
