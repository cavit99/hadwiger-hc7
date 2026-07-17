# Two colourful sets need not share one rooted `K_4` model

**Status:** barrier to an intermediate claim; written proof; separate
internal audit GREEN.  This is not a counterexample to `HC_7`.

## 1. Claim refuted

The following natural strengthening of Strong Hadwiger for four colours is
false, even with five-connectivity:

> If `J` is a five-connected four-chromatic graph and `S,T` are colourful
> in `J`, then `J` has a `K_4`-minor model each of whose four branch sets
> meets both `S` and `T`.

Here a set is colourful if every proper four-colouring uses all four
colours on it.

## 2. Construction

Let `A=a_0a_1a_2a_3` and `B=b_0b_1b_2b_3` be two vertex-disjoint copies
of `P_4`, and let

\[
                              J=A\vee B
\]

be their join.  Put

\[
 S=\{a_0,a_1,b_0,b_3\},\qquad
 T=\{a_2,a_3,b_0,b_3\}.                              \tag{2.1}
\]

### Proposition 2.1

The graph `J` is five-connected and four-chromatic, both `S,T` are
colourful, and no `K_4`-minor model in `J` has every branch set meeting
both `S` and `T`.

#### Proof

The chromatic number of a join is the sum of the chromatic numbers of its
factors, so `chi(J)=2+2=4`.  To disconnect `J`, one must delete every
vertex of one factor and a cut vertex of the other, or delete at least six
vertices.  Since each `P_4` is connected and has vertex-connectivity one,
`kappa(J)=4+1=5`.

In every four-colouring of `J`, the two join factors use disjoint palettes
of two colours each.  The adjacent pairs `a_0a_1` and `a_2a_3` each use
both colours of `A`.  The vertices `b_0,b_3` lie in opposite bipartition
classes of `B`, so they use both colours of `B`.  Hence each set in (2.1)
uses all four colours and is colourful.

Suppose that four pairwise disjoint branch sets `D_1,...,D_4` formed a
`K_4` model and each met both `S` and `T`.  Since `|S|=|T|=4`, every
branch set contains exactly one vertex of `S` and exactly one vertex of
`T`.  In particular, the two branch sets containing the common vertices
`b_0,b_3 in S cap T` contain no vertex of `A`, because every vertex of `A`
belongs to `S union T`.

Those two branch sets are disjoint connected subpaths of `B`, one
containing `b_0` and one containing `b_3`.  They must be adjacent because
the branch sets form a clique-minor model.  Their union must therefore
contain the whole path `b_0b_1b_2b_3`.  The remaining two branch sets use
no vertex of `B` and hence lie in `A`.

Each of those remaining connected subpaths must meet both
`{a_0,a_1}=S cap V(A)` and `{a_2,a_3}=T cap V(A)`.  Every such subpath
contains both `a_1` and `a_2`, contradicting disjointness.  Thus the paired
rooted model does not exist. \(\square\)

## 3. Why this is not the `HC_7` residue

The graph `J` already has the following `K_6`-minor model:

\[
 \{a_0\},\ \{a_1\},\ \{b_0\},\ \{b_1\},\
 \{a_2,b_2\},\ \{a_3,b_3\}.                          \tag{3.1}
\]

The four singleton branch sets form a clique through the join edges where
needed, each two-vertex set is connected by a join edge, and all six sets
are pairwise adjacent.  Consequently `J` cannot be the four-chromatic core
in the connected-dominating branch of a `K_7`-minor-free host: the
dominating connected branch set would combine with (3.1) to give a
`K_7` minor.

Thus the construction refutes the connectivity-only paired-root theorem,
but it does not refute a theorem retaining the derived `K_6`-minor
exclusion and the full seven-contraction-critical lift.

## 4. A second limitation: no two-vertex `K_4` transversal

For every set `C subseteq V(J)` with `|C|<=2`, the graph `J-C` is
three-connected.  Write `A'=A-C` and `B'=B-C`; both have order at least
two.  A vertex cut in the join `A' vee B'` must delete every vertex of one
factor, since any surviving vertex in each factor joins all remaining
components.  A set of at most two vertices can delete all of `A'` only
when both deleted vertices of `C` already lie in `A`; in that case `B'=B`
is connected.  The symmetric argument applies to `B'`.  Hence no set of
at most two vertices disconnects `J-C`.  The graph has at least six
vertices.  Every three-connected graph on at least four vertices has a
`K_4` minor, so `J-C` still contains a `K_4` minor.

Therefore the failed paired-root conclusion does not, under the abstract
hypotheses alone, force a two-vertex transversal for all `K_4` minors.
This does not rule out the fixed-pair conclusion in the actual lifted
`HC_7` setting.
