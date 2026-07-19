# Low-connectivity reduction for a singleton component at an order-eight boundary

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_singleton_low_connectivity_reduction_audit.md`](hc7_order8_singleton_low_connectivity_reduction_audit.md).
This theorem eliminates every cutvertex or bridge configuration except one
explicit two-piece residue.  It does not prove `HC_7`, and an order-seven
separation returned below is not asserted to carry compatible shore
colourings.

## 1. Setting and terminology

Let `G` be a seven-connected graph such that

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le 6\text{ for every proper minor }M\text{ of }G.
 \tag{1.1}
\]

Let `S` have order eight and suppose that `G-S` has exactly three
components

\[
                         \{v\},\qquad Q_0,\qquad Q_1,                \tag{1.2}
\]

each adjacent to every literal vertex of `S`.  Put `H=G[S]` and assume

1. `H` is three-colourable;
2. `alpha(H)<=3`; and
3. `H` contains two vertex-disjoint odd cycles.

These three boundary hypotheses hold for every graph in the audited
82-type residue of the three-component order-eight classification.  For a
connected subgraph `P` disjoint from `S`, define its **boundary defect** by

\[
                            D(P)=S-N_G(P).                          \tag{1.3}
\]

Thus `P` is boundary-full exactly when `D(P)=emptyset`, and it is
**near-full** when `|D(P)|<=1`.

## 2. Five near-full connected subgraphs force a `K_7` minor

The first lemma is the allocation fact used in every later branch-set
construction.

### Lemma 2.1 (five representatives with no mutual defect)

Let `N` be a six-element set and let `D_0,...,D_4` be subsets of `N`, each
of order at most one.  There are distinct representatives

\[
                 x_i\in N-D_i\qquad(0<=i<=4)                       \tag{2.1}
\]

such that, for all distinct `i,j`, it is not the case that both

\[
                           x_i\in D_j\quad\text{and}\quad x_j\in D_i.
 \tag{2.2}
\]

#### Proof

Choose the representatives greedily in the order `0,1,...,4`.  Having
chosen `x_0,...,x_{i-1}`, forbid

* the `i` previous representatives;
* the at most one vertex of `D_i`; and
* for every `j<i` with `x_j\in D_i`, the at most one vertex of `D_j`.

Since `D_i` has order at most one, at most one index `j<i` satisfies
`x_j\in D_i`.  If no such index exists, at most `i+1<=5` vertices are
forbidden.  If such an index exists, the vertex of `D_i` is already among
the previous representatives, so the last two bullets increase the
`i`-element previous set by at most one vertex; again at most `i+1<=5`
vertices are forbidden.  One of the six vertices of `N` is therefore
available for `x_i`.

The first two bullets give (2.1) and distinctness.  If `j<i` and
`x_j\in D_i`, the third bullet ensures `x_i\notin D_j`; this is exactly
(2.2). \(\square\)

### Lemma 2.2 (five-piece completion)

Let `|S|=8` and `alpha(G[S])<=3`.  Suppose that `P_0,...,P_4` are
pairwise vertex-disjoint connected subgraphs of `G-S`, where `P_0` is
boundary-full and `P_1,...,P_4` are near-full.  Then `G` contains a
`K_7` minor.

#### Proof

Write `D_i=D(P_i)` and put `D=union_i D_i`.  Since `D_0` is empty and
the other four defects have order at most one, `|D|<=4`.  Hence
`|S-D|>=4`; the bound `alpha(G[S])<=3` gives an edge `ab` of `G[S-D]`.
Put `N=S-{a,b}`.  Every `D_i` is a subset of the six-element set `N`.

Apply Lemma 2.1 and choose distinct `x_0,...,x_4` in `N`.  For
`0<=i<=4`, put

\[
                              B_i=P_i\cup\{x_i\}.                   \tag{2.3}
\]

The seven proposed branch sets are

\[
                    B_0,B_1,B_2,B_3,B_4,\{a\},\{b\}.              \tag{2.4}
\]

They are pairwise disjoint.  Each `B_i` is connected because
`x_i\notin D_i`.  Each `B_i` is adjacent to both singleton branch sets,
because `a,b\notin D`, and the singleton branch sets are adjacent through
the edge `ab`.

It remains to check two sets `B_i,B_j`.  If `P_i,P_j` are adjacent, there
is nothing to prove.  Otherwise, (2.2) says that at least one of
`x_j\notin D_i` and `x_i\notin D_j` holds.  In the first case `P_i` is
adjacent to `x_j\in B_j`; in the second, `P_j` is adjacent to
`x_i\in B_i`.  Thus every pair in (2.4) is adjacent, so (2.4) is an
explicit `K_7`-minor model. \(\square\)

No anticompleteness assumption between the five connected subgraphs is
used; extra edges only help.

## 3. The other two components are not singletons

### Lemma 3.1

Under the setting of Section 1, neither `Q_0` nor `Q_1` is a singleton.

#### Proof

Suppose, by symmetry, that `Q_0={q}`.  Since `H` is three-colourable and
`alpha(H)<=3`, any proper three-colouring partitions `S` as

\[
                  S=A\mathbin{\dot\cup}B\mathbin{\dot\cup}C,
                  \qquad |A|=|B|=3,\quad |C|=2.                   \tag{3.1}
\]

Indeed, the three independent colour classes have order at most three and
sum to eight.

In `G`, simultaneously contract spanning trees of the two disjoint
connected stars

\[
                              \{v\}\cup A,\qquad \{q\}\cup B.     \tag{3.2}
\]

This is a proper minor and hence has a proper six-colouring.  The two
contraction images are adjacent: for example, `v` is adjacent to every
vertex of `B`.  Each image is adjacent to both vertices of `C`.  Therefore
the two image colours are distinct, neither occurs on `C`, and the induced
colouring uses at most four colours on the literal boundary `S` after
expanding the two stars.

Restrict this expanded colouring to `G[Q_1\cup S]`.  At least one of the
six colours is absent from `S`; give that colour to both `v` and `q`.
The vertices `v,q` are distinct singleton components of `G-S`, so they are
nonadjacent and have no neighbours in `Q_1`.  Their neighbours all lie in
`S`, where the new colour is absent.  This gives a proper six-colouring of
`G`, contradicting (1.1). \(\square\)

## 4. What a cutvertex or bridge exposes

### Lemma 4.1 (cutvertex lobes)

Let `Q` be one of `Q_0,Q_1`, let `x` be a cutvertex of `G[Q]`, and let
`L` be a component of `G[Q]-x`.  Then either `G` has an actual separation
of order seven or `L` is near-full.  If `G[Q]-x` has at least three
components, then `G` has a `K_7` minor or an actual separation of order
seven.

#### Proof

Because `Q` is a component of `G-S`, connectedness gives

\[
                         N_G(L)=\{x\}\mathbin{\dot\cup}N_S(L).     \tag{4.1}
\]

This is a genuine separation boundary: `L` is nonempty, while another
lobe and the two other components of `G-S` lie on the opposite side.
Seven-connectivity yields `|N_S(L)|>=6`.  Equality gives an actual
order-seven separation.  Otherwise `|N_S(L)|>=7`, so `L` is near-full.

Assume that no lobe has returned an order-seven separation.  If there are
exactly three lobes, use those three lobes, the boundary-full singleton
`{v}`, and the other exterior component as the five connected subgraphs
in Lemma 2.2.  If there are at least four lobes, use any four of them and
`{v}`.  In either case Lemma 2.2 gives a `K_7` minor. \(\square\)

### Lemma 4.2 (bridge sides)

Let `xy` be a bridge of `G[Q]`, and let `A,B` be the vertex sets of the
two components of `G[Q]-xy`, with `x\in A` and `y\in B`.  Then either
`G` has an actual separation of order seven or both `G[A]` and `G[B]`
are connected near-full subgraphs.

#### Proof

The sets `A,B` are nonempty and connected, and the only edge of `G[Q]`
between them is `xy`.  Hence

\[
 N_G(A)=\{y\}\mathbin{\dot\cup}N_S(A),
 \qquad
 N_G(B)=\{x\}\mathbin{\dot\cup}N_S(B).               \tag{4.2}
\]

Each is a genuine separation boundary, so seven-connectivity gives
`|N_S(A)|,|N_S(B)|>=6`.  Equality in either inequality is an actual
order-seven separation; otherwise both sides are near-full. \(\square\)

### Corollary 4.3

If no `K_7` minor and no actual order-seven separation has already been
found, then at most one of `Q_0,Q_1` has a cutvertex or a bridge.

#### Proof

By Lemma 4.1, every cutvertex under consideration has exactly two lobes,
and those lobes are connected and near-full.  A bridge supplies two
disjoint connected near-full sides by Lemma 4.2.  If both exterior
components had one of these structures, choose two such pieces from each
component and add the boundary-full singleton `{v}`.  Lemma 2.2 gives a
`K_7` minor. \(\square\)

## 5. Exact classification of a surviving two-piece split

The next lemma is stated for either a bridge split, or one of the two
orientations of a two-lobe cutvertex split.

### Lemma 5.1 (two-piece residue)

Let `Q` be one of `Q_0,Q_1`, let `R` be the other one, and suppose

\[
                         Q=A\mathbin{\dot\cup}B                      \tag{5.1}
\]

where `G[A],G[B]` are nonempty connected near-full subgraphs and there is
an edge between them.  Then at least one of the following holds.

1. `G` contains a `K_7` minor;
2. `G` is six-colourable;
3. there are distinct nonadjacent vertices `d,e\in S` such that

   \[
        D(A)=\{d\},\qquad D(B)=\{e\},
        \qquad G[S-\{d,e\}]\text{ is bipartite}.                    \tag{5.2}
   \]

#### Proof

The four connected subgraphs `{v}`, `R`, `A`, and `B` are pairwise
disjoint; the first two are boundary-full, while the last two are adjacent
and near-full.

First suppose that at least one of `A,B` is boundary-full.  Choose one of
the two disjoint odd cycles in `H` avoiding the actual defect of the other
subgraph (if it has one); call it `O`.  Its order is three or five.  Treat
the boundary-full subgraph as having an artificial defect `e`, where `e`
is chosen outside `V(O)` and distinct from the other defect `d`.  Such an
`e` exists because `|S|=8`, `|O|<=5`, and `d\notin V(O)`.  Lemma 1.1 of
the promoted strict-reversal completion theorem, applied monotonically to
the extra contacts, gives an explicit `K_7`-minor model.  The same argument
applies if both subgraphs are full, choosing two distinct artificial
defects outside one of the odd cycles.

Thus assume both defects are nonempty.  If they are equal, write
`D(A)=D(B)={d}` and choose one of the two disjoint odd cycles `O` avoiding
`d`.

If `|O|=3`, let the three vertices of `O` be singleton branch sets.  The
five-set `S-V(O)` contains `d` and four other vertices.  Use those four
vertices as distinct anchors for `A`, `B`, `{v}`, and `R`.  The four
anchored connected subgraphs are pairwise adjacent: any one sees the
anchor of any other, except that the assumed edge between `A` and `B`
already supplies their adjacency.  All four see every vertex of `O`.
Together with the three singleton vertices of the triangle, they form an
explicit `K_7`-minor model.

If `|O|=5`, partition the cycle into three nonempty connected pairwise
adjacent branch sets.  Write `S-V(O)={d,r,s}`.  The remaining four branch
sets are

\[
                        A\cup\{r\},\quad B\cup\{s\},
                        \{v,d\},\quad R.                            \tag{5.3}
\]

They are connected and pairwise adjacent: `A,B` are adjacent by
hypothesis; `{v,d}` sees both anchors `r,s`; `R` sees `d,r,s`; and the
two anchored near-full subgraphs are adjacent to `R` through their
anchors.  Every set in (5.3) is adjacent to every cycle branch set because
the cycle avoids `d`.  Thus these four sets and the three cycle sets form
an explicit `K_7`-minor model.

We may therefore write `D(A)={d}` and `D(B)={e}` with `d!=e`.  If
`G[S-{d,e}]` is nonbipartite, a shortest odd cycle in this six-vertex
graph has order three or five.  Lemma 1.1 of the strict-reversal completion
theorem applies to `{v},R,A,B` and gives a `K_7` minor.

Finally suppose `G[S-{d,e}]` is bipartite.  If `de` is an edge, the
promoted adjacent-defect reflection theorem applies with `A,B` on one
open shore and the two disjoint boundary-full connected subgraphs `{v}`
and `R` on the other.  The two vertex-disjoint odd cycles in `H` verify
its remaining boundary hypothesis, so `G` is six-colourable.  The only
remaining case is (5.2). \(\square\)

### Lemma 5.2 (the cutvertex misses both defects)

Let `x` be a cutvertex of `G[Q]`, suppose `G[Q]-x` has exactly two
components `L_1,L_2`, and suppose none of the terminal outcomes in
Lemmas 4.1 and 5.1 occurs.  Then, after naming the two defects `d,e` as in
(5.2),

\[
                         x\notin N_G(d)\cup N_G(e).                 \tag{5.4}
\]

#### Proof

Apply Lemma 5.1 first to the connected adjacent partition

\[
                         (L_1\cup\{x\})\mathbin{\dot\cup}L_2.
\]

The surviving exact defect of the first side shows that `x` misses that
defect, say `d`.  Apply the same lemma to the opposite orientation

\[
                         L_1\mathbin{\dot\cup}(L_2\cup\{x\}).
\]

The surviving exact defect of the second side shows that `x` misses the
other defect `e`.  If an orientation made one side boundary-full, the
first branch of Lemma 5.1 would already be terminal.  Hence (5.4) holds.
\(\square\)

## 6. Main reduction

### Theorem 6.1

Under the setting of Section 1, at least one of the following holds.

1. `G` contains a `K_7` minor.
2. `G` is six-colourable.
3. `G` has an actual separation of order seven.
4. Both `Q_0,Q_1` are non-singleton, at most one of them has a cutvertex
   or bridge, and every such low-connectivity structure has the following
   form:
   * a cutvertex has exactly two lobes;
   * a bridge, or either orientation of a two-lobe cutvertex split, gives
     two adjacent connected subgraphs with distinct exact defects
     `{d},{e}`;
   * `de` is not an edge and `G[S-{d,e}]` is bipartite; and
   * in the cutvertex case, the cutvertex is adjacent to neither `d` nor
     `e`.

Consequently, if one exterior component has such a surviving cutvertex or
bridge, the other is a non-singleton connected graph with no cutvertex and
no bridge (and hence is two-connected in the standard convention).

#### Proof

Lemma 3.1 excludes singleton `Q_i`.  Lemmas 4.1 and 4.2 either give the
first or third outcome, or reduce every cutvertex/bridge to adjacent
near-full pieces.  Corollary 4.3 shows that at most one exterior component
has such a structure.  Lemma 5.1 gives the exact independent-defect
bipartite residue, and Lemma 5.2 supplies the additional cutvertex
restriction.  These are exactly the alternatives displayed above.
\(\square\)

## 7. Exact gain and trust boundary

The new unbounded ingredient is Lemma 2.2: five disjoint connected
subgraphs, one full and four of defect at most one, always complete to an
explicit `K_7`-minor model when `alpha(G[S])<=3`.  It eliminates every
cutvertex with at least three lobes and every configuration in which both
non-singleton exterior components have a cutvertex or bridge.

The surviving two-piece residue is exact: its defects form a nonedge
`de`, deleting them makes the boundary bipartite, and a cutvertex misses
both.  The theorem does **not** eliminate this residue.  It does not prove
that a returned order-seven separation induces the same equality partition
from both shores, and it does not address a two-connected, bridge-free
exterior component.

## 8. Dependencies

- [three-component order-eight boundary classification](hc7_order8_three_component_boundary_classification.md),
  only for the three boundary hypotheses isolated in Section 1;
- [strict-reversal completion](hc7_order8_strict_reversal_completion.md),
  Lemma 1.1; and
- [reflection across adjacent complementary defects](hc7_order8_two_defect_clique_oct_reflection.md),
  Theorem 2.1.
