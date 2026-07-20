# A clique decoder for components behind a centre vertex

**Status:** written proof; [separate internal audit](hc7_order8_center_component_clique_decoder_audit.md)
GREEN.  This is an unbounded host-level reduction for the two-component
order-eight response problem.  It does not prove `HC_7`.

## 1. A representative lemma

### Lemma 1.1

Let `N` be a finite set with `|N| >= m+1`, and let
`F_1,...,F_m` be subsets of `N`, each of order at most one.  There are
distinct elements

\[
                         x_i\in N-F_i\qquad(1\le i\le m)             \tag{1.1}
\]

such that no two indices `i != j` satisfy both

\[
                         x_i\in F_j\quad\hbox{and}\quad x_j\in F_i. \tag{1.2}
\]

#### Proof

Choose the representatives in the order `1,...,m`.  Suppose
`x_1,...,x_{i-1}` have been chosen.  Since these representatives are
distinct and `|F_i| <= 1`, at most one earlier representative belongs to
`F_i`.  Let

\[
 J_i=\{j<i:x_j\in F_i\}
\]

and forbid

\[
 P_i=\{x_1,\ldots,x_{i-1}\}\cup F_i
       \cup\bigcup_{j\in J_i}F_j.                                \tag{1.3}
\]

If `J_i` is empty, then `|P_i| <= i`.  If `J_i={j}`, then
`F_i={x_j}` is already contained among the previous representatives, so
again `|P_i| <= i`.  As `i <= m < |N|`, choose `x_i in N-P_i`.
It is distinct from the earlier representatives and avoids `F_i`.  If an
earlier `x_j` belongs to `F_i`, then `j in J_i` and the choice also gives
`x_i notin F_j`.  Thus no mutual pair in (1.2) is created.  Induction
proves the lemma. \(\square\)

## 2. The minor-model construction

### Theorem 2.1 (centre-component clique decoder)

Let `S` be an eight-vertex set in a graph `G`.  Let `v notin S`, let `D`
be a connected subgraph disjoint from `S union {v}`, and let
`A_1,...,A_m`, where `1 <= m <= 5`, be pairwise vertex-disjoint connected
subgraphs disjoint from `S union D union {v}`.  Assume that

1. `D` is adjacent to every vertex of `S`;
2. every `A_i` is adjacent to `v` and is adjacent to all but at most one
   vertex of `S`;
3. `Q subseteq S` is a clique of order `5-m`, every member of `Q` is
   adjacent to `v`, and every `A_i` is adjacent to every member of `Q`;
4. there is a vertex `p in N_G(v) intersect (S-Q)`.

Then `G` contains an explicit `K_7`-minor model.

#### Proof

Put

\[
                        N=S-(Q\cup\{p\}).                           \tag{2.1}
\]

Its order is

\[
                        |N|=8-(5-m)-1=m+2.                          \tag{2.2}
\]

For each `i`, let

\[
                        F_i=N-N_G(A_i).                             \tag{2.3}
\]

The second hypothesis gives `|F_i| <= 1`.  Apply Lemma 1.1 and choose
distinct representatives `x_i in N-F_i` without a mutual defect pair.
Set

\[
                        B_i=A_i\cup\{x_i\}.                         \tag{2.4}
\]

Every `B_i` is connected.  If `i != j` and `A_i` is not adjacent to
`x_j`, then `x_j in F_i`.  The absence of a mutual defect pair gives
`x_i notin F_j`, so `A_j` is adjacent to `x_i`.  Hence the sets `B_i`
are pairwise adjacent.

The following seven sets are pairwise disjoint connected subgraphs:

\[
 B_1,\ldots,B_m,\qquad \{v\},\qquad D\cup\{p\},
       \qquad \{q\}\quad(q\in Q).                                \tag{2.5}
\]

The vertex `v` is adjacent to every `B_i`, to `D union {p}` through
`vp`, and to every singleton in `Q`.  The set `D union {p}` is connected,
is adjacent to every `B_i` through the boundary representative `x_i`, and
is adjacent to every singleton in `Q`, because `D` is adjacent to every
vertex of `S`.  Each `B_i` is adjacent to every singleton in `Q` by the
third hypothesis, and those singletons are pairwise adjacent because `Q`
is a clique.  Together with the pairwise adjacencies among the `B_i`,
these are all pairs in (2.5).  Thus (2.5) is a `K_7`-minor model.
\(\square\)

### Theorem 2.2 (paired-centre component decoder)

Let `S` be an eight-vertex set in a graph `G`, let `p in S`, and let `H`
be a connected subgraph with

\[
                              V(H)\cap S=\{p\}.         \tag{2.6}
\]

Let `A_1,...,A_k`, where `1 <= k <= 6`, be pairwise vertex-disjoint
connected subgraphs disjoint from `H union S`.  Assume that

1. every `A_i` is adjacent to `H` and to all but at most one vertex of
   `S`; and
2. `Q subseteq S-{p}` is a clique of order `6-k`, every member of `Q` is
   adjacent to `H`, and every `A_i` is adjacent to every member of `Q`.

Then `G` contains an explicit `K_7`-minor model.

#### Proof

The set

\[
                              N=S-(Q\cup\{p\})          \tag{2.7}
\]

has order `k+1`.  Apply Lemma 1.1 to the at-most-singleton sets
`F_i=N-N_G(A_i)` and obtain distinct representatives `x_i in N`
without a mutual defect pair.  As in Theorem 2.1, the connected sets
`B_i=A_i union {x_i}` are pairwise adjacent.

The seven branch sets are

\[
                  H,\qquad B_1,\ldots,B_k,
                  \qquad \{q\}\quad(q\in Q).          \tag{2.8}
\]

The first is adjacent to every `B_i` and every singleton in `Q` by
hypothesis.  Each `B_i` is adjacent to every singleton in `Q`, and `Q` is
a clique.  Together with the pairwise adjacency of the `B_i`, this checks
all pairs in (2.8).  The sets are disjoint and connected, so they form a
`K_7`-minor model. \(\square\)

## 3. Application to an eight-separation

### Corollary 3.1

Let `G` be seven-connected and `K_7`-minor-free.  Let `S` be an
eight-vertex set such that `G-S` has two components `C,D`, each adjacent
to every vertex of `S`.  Let `v in C` have a neighbour `p in S`.
Then either

1. some component `A` of `C-v` has `|N_G(A)|=7`, and its full
   neighbourhood is the boundary of an actual separation; or
2. `C-v` has at most four components.

#### Proof

Every component of `C-v` is adjacent to `v`, since `C` is connected.
If a component `A` of `C-v` is adjacent to at most six vertices of `S`,
then

\[
                         N_G(A)\subseteq \{v\}\cup S
\]

has order at most seven.  The other component `D` lies outside
`A union N_G(A)`, so this is the boundary of an actual separation.
Seven-connectivity forces `|N_G(A)|=7`, and in particular `A` is adjacent
to exactly six vertices of `S`.

This is the first outcome.  If that outcome is excluded, every component
of `C-v` is adjacent to all but at most one vertex of `S`.
If there were at least five components, choose any five and apply Theorem
2.1 with `m=5`, `Q` empty, and the given vertex `p`.  This gives a
`K_7` minor, a contradiction.  Hence at most four components remain.
\(\square\)

The first paragraph uses no ranked response programme: it gives the actual
order-seven separation directly whenever a component misses at least two
boundary vertices.

### Corollary 3.2 (clique restriction for the remaining components)

In the setting of Corollary 3.1, exclude the actual order-seven separation.
Let `A_1,...,A_m`, where `1 <= m <= 4`, be components of `C-v`.  Their
common boundary neighbourhood, restricted to neighbours of `v`, contains
no clique `Q` of order `5-m` for which `v` has another neighbour in
`S-Q`.

#### Proof

Otherwise Theorem 2.1 applies to `A_1,...,A_m`, the other component `D`,
the clique `Q`, and that additional neighbour of `v`, and yields a
`K_7` minor. \(\square\)

### Corollary 3.3 (two centres have at most five components in total)

Let `G` be seven-connected and `K_7`-minor-free.  Let `S` be an
eight-vertex set such that `G-S` has two components `C,D`, each adjacent
to every vertex of `S`.  Choose `p in S`,

\[
                         v\in N_G(p)\cap C,
                         \qquad w\in N_G(p)\cap D.     \tag{3.1}
\]

Then either a component of `C-v` or `D-w` has an actual order-seven full
neighbourhood, or the total number of components of these two graphs is at
most five.

#### Proof

Let `A` be a component of `C-v`.  It has no neighbours outside
`S union {v}`.  If it misses at least two vertices of `S`, then
`|N_G(A)|<=7`; the opposite component `D` witnesses a genuine separation,
so seven-connectivity forces equality.  The same argument applies to a
component of `D-w`.

Exclude this order-seven outcome.  Every component of both graphs is then
adjacent to all but at most one vertex of `S`.  If there were at least six
in total, select six and apply Theorem 2.2 with

\[
                             H=G[\{v,p,w\}],
                             \qquad Q=\varnothing.
\]

The graph `H` is connected through `vp,pw`, and every selected component
is adjacent to `v` or `w`.  The theorem gives a `K_7` minor, a
contradiction. \(\square\)

More generally, if the total component count is `1<=k<=5`, Theorem 2.2
forbids every `(6-k)`-clique in their common boundary neighbourhood whose
vertices are adjacent to `G[{v,p,w}]`.

## 4. Exact contribution and trust boundary

The theorems eliminate, for arbitrarily large components, the entire case
in which deleting one centre leaves at least five connected pieces, and
the paired case in which deleting one centre in each shore leaves at least
six pieces in total.  For the smaller counts they convert nearly complete
boundary contact into explicit clique restrictions.  They use literal
boundary vertices and produce all seven branch sets explicitly.

It does not prove that one of the remaining components can be split into
two suitably adjacent connected subgraphs, align a boundary colouring with
the selected representatives, or close the cases in which `C-v` has at
most four components and the common-neighbour clique is absent.  Those are
the remaining host-level response-coupling questions.

## 5. Dependencies

- seven-connectivity, only in Corollaries 3.1--3.3;
- elementary representative selection; and
- the definition of a minor model.
