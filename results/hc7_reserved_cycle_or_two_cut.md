# Reserved cycles at a degree-eight vertex

**Status:** written proof; separate internal audit.  This note proves
the cycle-reservation part of the active degree-eight problem and identifies
the exact low-connectivity residue.  It does not prove that the three
boundary vertices have the contact pattern required by the degree-eight
allocation theorem, and it does not synchronize the two colourings at the
order-seven separation returned below.

## 1. Literal setup

Use the notation of the exact two-pair disk configuration.  Thus

\[
 V(G)=L\mathbin{\dot\cup}T\mathbin{\dot\cup}R,
 \qquad |T|=7,
 \qquad E_G(L,R)=\varnothing,
\]

where `G` is seven-connected, `L,R` are nonempty, and

\[
 U=\{i_0,j_0,i_1,j_1\}\subseteq T,
 \qquad B=T-U.
\]

Put `H=G[L union U]`, with its disk drawing, and let `v in L` be a
degree-eight vertex supplied by the curvature equality.  Write

\[
 C=N_H(v),\qquad |C|=5,
 \qquad N_G(v)=B\mathbin{\dot\cup}C.                 \tag{1.1}
\]

Let `D` be a component of `G-N_G[v]` containing a component of the old
open shore `G[R]`.  In particular, `D` is nonempty and

\[
                         N_G(D)\subseteq B\cup C.      \tag{1.2}
\]

Define the literal component-deleted host residue

\[
                         K=G-(D\cup B\cup\{v\}).       \tag{1.3}
\]

Every member of `C` belongs to `K`.  In the contraction-critical
application, Dirac's neighbourhood inequality gives

\[
                         \alpha(G[C])\le3.             \tag{1.4}
\]

## 2. A connected reserved subgraph or a low-order cut

### Theorem 2.1 (reserved-cycle reduction)

Under the setup above, at least one of the following holds.

1. There is a cycle `W subseteq K` containing all five vertices of `C`.
   The cycle can be partitioned into five pairwise disjoint connected sets

   \[
                         C_0,C_1,C_2,C_3,C_4           \tag{2.1}
   \]

   such that each set contains a distinct member of `C`, and consecutive
   sets are adjacent cyclically.  The six sets

   \[
                 D,C_0,C_1,C_2,C_3,C_4                \tag{2.2}
   \]

   are literal and pairwise disjoint, and `D` is adjacent to at least
   seven of the eight labels consisting of `B` and the five sets in
   (2.1).

2. The graph `K` has a separator `Z` of order at most two.  Put
   `z=|Z|`.  For every component `A` of `K-Z`, put

   \[
                         C_A=A\cap C.                  \tag{2.3}
   \]

   If `A-C_A` is nonempty and `|C_A|<=4-z`, then `G` has an actual
   order-seven full-neighbourhood separation.  More precisely, some
   component `X` of `G[A-C_A]` satisfies

   \[
       N_G(X)=Z\mathbin{\dot\cup}B
                 \mathbin{\dot\cup}C_A,
       \qquad |N_G(X)|=7.                              \tag{2.4}
   \]

   If `|X|>=2` and every proper minor of `G` is six-colourable, this
   boundary has an explicitly attained one-sided partition into at most
   five independent sets: contract a spanning tree of `X` and restrict a
   six-colouring of the resulting minor to `G-X`.  Every boundary vertex
   avoids the colour of the contraction representative.

   Consequently, if no such order-seven separation occurs, every
   component `A` of `K-Z` containing a vertex outside `C` satisfies

   \[
                         |A\cap C|\ge5-z.              \tag{2.5}
   \]

   In that case at most one component of `K-Z` contains a vertex outside
   `C`; every other component is contained in the five-set `C`.

In particular, if `K` is three-connected, outcome 1 holds.  More
generally, outcome 1 holds whenever `K` is `k`-connected for some `k>=2`
with `alpha(G[C])<=k`.

Hence failure of outcome 1 can occur only when `K` is disconnected, has a
cutvertex, or is two-connected with `alpha(G[C])=3`.  In every case a
separator of order at most two is available for outcome 2.

### Proof

Suppose first that `K` is `k`-connected for some `k>=2` and
`alpha(G[C])<=k`.  Fournier's cyclability theorem says that a set `X` in
a `k`-connected graph lies on a cycle whenever `alpha(G[X])<=k`.
Apply it to `X=C`.  This gives a literal cycle `W subseteq K` containing
all five members of `C`.

List those five vertices in their cyclic order on `W`.  Delete one edge
from each of the five intervening arcs.  The five resulting vertex sets
are nonempty disjoint paths, each contains exactly one nominated member of
`C`, and consecutive paths are adjacent through the five deleted cycle
edges.  These are the sets in (2.1).

The cycle lies in `K`, so it avoids `D`, `v`, and `B`.  Since `D` is a
component of `G-N_G[v]`, its whole external neighbourhood is contained in
the eight-set `B union C`.  Seven-connectivity and the nonempty opposite
side containing `v` give

\[
                         7\le |N_G(D)|\le8.             \tag{2.6}
\]

Every contacted member of `B` is one contacted singleton label.  Every
contacted vertex `c in C` lies in one set `C_i`, which is therefore
adjacent to `D`.  Thus `D` meets at least seven of the eight labels.  This
proves outcome 1.

It remains to prove the lift asserted in outcome 2.  Let `Z` separate
`K`, let `A` be a component of `K-Z`, and suppose `A-C_A` is nonempty.
Choose a component `X` of `G[A-C_A]`.  Every vertex of `X` lies outside
`N_G[v]`: all five neighbours of `v` in `H` are precisely the vertices of
`C`, while the three other neighbours of `v` are in `B`.

There is no edge from `X` to `D`.  Indeed, `X` contains no member of
`C=N_H(v)`, so both `X` and `D` lie in `G-N_G[v]`; the set `D` is one
component of that graph.  Every host vertex outside
`D union B union {v}` was retained in `K`.  The choice of the component
`A` of `K-Z` therefore accounts for every other possible host neighbour,
and gives

\[
                         N_G(X)
       \subseteq Z\cup B\cup C_A.                      \tag{2.7}
\]

The three displayed parts are disjoint.  If `|C_A|<=4-z`, the right-hand
side of (2.7) has order at most seven.  Seven-connectivity gives the
opposite inequality.  Equality must therefore hold throughout: necessarily
`|C_A|=4-z`, every displayed candidate is an actual neighbour of `X`, and
(2.4) follows.  The set `D` survives in the opposite open side, so this is
a genuine nontrivial order-seven separation.

The contrapositive gives (2.5).  Finally, (1.4) lets one take `k=3` in
the first part whenever `K` is three-connected.  If two components of
`K-Z` both contained vertices outside `C`, (2.5) would put at least
`2(5-z)>5` distinct members of `C` in their union, since `z<=2`.  This is
impossible.  The last assertion of outcome 2 follows.  \(\square\)

## 3. The exact consequence for contact allocation

In outcome 1, retain the singleton sets `\{b\}` for `b in B`.  Form the
bipartite nonadjacency graph between `B` and the five cyclic connected
sets `C_i`.  If this graph is a matching of order at most two, all the
hypotheses of the audited degree-eight connected-set allocation theorem
hold: `D` supplies the connected seventh branch set and (2.6) supplies its
seven contacts.  Hence `G` has an explicit `K_7`-minor model.

Thus the unclosed residue has exactly two independent parts.

1. **Low connectivity after reserving `D`.**  A separator `Z` of order at
   most two has the concentrated distribution (2.5).  If its lower
   threshold fails, the proof already returns an order-seven boundary.
   Otherwise precisely one component of `K-Z` can contain vertices outside
   `C`; all remaining components are subgraphs induced by subsets of `C`.
   The missing operation is a label-preserving split of `D` (or of a
   connected subgraph attached through `D`) which reconnects those separated
   `C`-classes while leaving a connected subgraph with seven contacts.
2. **Concentrated boundary contacts.**  Even with the reserved cycle, the
   nonadjacencies from `B` to its five sectors need not form a matching.
   A proper-minor response must either enlarge the three `B`-branch sets
   by disjoint first-hit subgraphs until the matching condition holds, or
   return an exact order-seven boundary with a common equality partition.

In the contraction-critical application, the order-seven separation in
(2.4) has a canonical one-sided target partition.  If `|X|>=2`, contract a
spanning tree of `X`.  In a six-colouring of the resulting proper minor,
the contracted representative is adjacent to all seven vertices of
`N_G(X)`, so its colour is absent from that boundary.  The induced boundary
partition has at most five blocks and extends through the unchanged closed
opposite shore.  If `X` is a singleton, it is a degree-seven vertex.  In
the intended minor-minimal counterexample, `chi(G)=7` and Dirac's
neighbourhood bound gives `alpha(N_G(X))<=2`; deleting the vertex therefore
gives the promoted degree-seven matching partition on its neighbourhood.
What remains to be proved in either case is
that a suitable target partition extends through `G[X union N_G(X)]`, or
that its failure gives the required labelled split.  The present theorem
does not assert that synchronization.

## 4. Dependencies and trust boundary

- The local allocation used in Section 3 is
  [the degree-eight connected-set allocation theorem](hc7_degree8_contact_allocation.md).
- Fournier's cyclability theorem is restated as Theorem 7 in R. Gould,
  *A look at cycles containing specified elements of a graph*, Discrete
  Mathematics 309 (2009), 6299--6311, and as Theorem D in A. Saito and
  T. Yamashita, *Cycles within specified distance from each vertex*,
  Discrete Mathematics 278 (2004), 219--226,
  <https://doi.org/10.1016/j.disc.2003.05.004>.

The reduction uses literal vertices, components, cycles, and
full-neighbourhood separators.  It does not use an edge added in a planar
completion.  It does not prove the matching condition on the three
boundary-contact rows, a split of the concentrated low-cut residue, or a
common equality partition on the returned order-seven boundary.
