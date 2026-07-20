# Opposite-shore consequences of a single boundary-vertex recolouring

**Status:** written proof; separate internal audit GREEN in
[`hc7_order9_opposite_single_vertex_flip_audit.md`](hc7_order9_opposite_single_vertex_flip_audit.md).

This note treats the elementary transition that occurs when two boundary
colourings differ only at one literal boundary vertex and extend through
opposite closed shores.  It gives exact shore ownership of two colour
neighbourhoods, forced bichromatic paths through both open shores, and an
order-seven/eight/full-boundary alternative at a nine-vertex boundary.  It
does not identify colours with minor-model branch sets or prove `HC_7`.

## 1. Setting

Let `q>=2`, let `G` be a graph which is not `q`-colourable, and let

\[
 V(G)=A\mathbin{\dot\cup}B\mathbin{\dot\cup}D,
 \qquad A,D\ne\varnothing,
 \qquad E_G(A,D)=\varnothing .                         \tag{1.1}
\]

Let `phi,psi` be proper `q`-colourings of `G[B]` which agree on
`B-{b}` and satisfy

\[
 \phi(b)=i,\qquad \psi(b)=j,\qquad
 j\notin\phi(B),\qquad i\ne j.                        \tag{1.2}
\]

Assume that `phi` extends to a proper colouring `alpha` of `G[D union B]`
but does not extend through `G[A union B]`, while `psi` extends to a proper
colouring `beta` of `G[A union B]` but does not extend through
`G[D union B]`.

Put

\[
                     C=\phi^{-1}(i)-\{b\}.             \tag{1.3}
\]

In the order-nine application both boundary colourings are exact at the
same singleton `{d}`.  The proof below does not use that additional fact.

## 2. The opposite-flip theorem

### Theorem 2.1

Under the hypotheses of Section 1 the following statements hold.

1. The two closed-shore colourings glue after deleting `b` to a proper
   `q`-colouring `c` of `G-b`:

   \[
    c|A=\beta|A,\qquad c|D=\alpha|D,
    \qquad c|_{B-\{b\}}=\phi|_{B-\{b\}}.
                                                               \tag{2.1}
   \]

2. Every colour occurs on a neighbour of `b` under `c`.  More precisely,

   \[
      N_G(b)\cap c^{-1}(i)\subseteq A,
      \qquad
      N_G(b)\cap c^{-1}(j)\subseteq D,                 \tag{2.2}
   \]

   and both sets in (2.2) are nonempty.
   Thus the old-shore extension `alpha` has a literal neighbour of `b` in
   `D` with the newly introduced colour `j`, while the new-shore extension
   `beta` has a literal neighbour of `b` in `A` with the old colour `i`.

3. The set `C` is nonempty.  There are bichromatic paths `P_A,P_D` such
   that

   \[
   \begin{array}{c|c|c|c}
        &\text{ends}&\text{internal vertices}&\text{colours}\cr\hline
    P_A&b,\ x_A\in C&A&i,j\text{ under }\beta\cr
    P_D&b,\ x_D\in C&D&i,j\text{ under }\alpha,
   \end{array}                                                   \tag{2.3}
   \]

   and both paths have nonempty interiors.  The interiors of `P_A,P_D`
   are vertex-disjoint.  The path `P_A` has odd length and `P_D` has even
   length.

4. For every two colours `r,s`, some `r`--`s` component of `G-b` contains
   a neighbour of `b` of each colour.  In particular, some `i`--`j`
   component contains both an `i`-coloured neighbour of `b` in `A` and a
   `j`-coloured neighbour of `b` in `D`.  Consequently `G` contains an odd
   cycle through `b` whose two neighbours of `b` on the cycle lie
   respectively in `A` and `D`, and whose boundary vertices other than
   `b` all belong to `C`.

If `C={x}`, then `x_A=x_D=x`, and `P_A union P_D` is itself an odd cycle
meeting `B` exactly in `{b,x}`.

### Proof

The assignments in (2.1) agree on `B-{b}`.  There are no `A-D` edges, so
they give a proper colouring `c` of `G-b`.

If some colour were absent from `N_G(b)` under `c`, assigning that colour
to `b` would produce a proper `q`-colouring of `G`.  Hence every colour
appears on `N_G(b)`.  In the colouring `alpha`, the vertex `b` has colour
`i`; therefore no neighbour of `b` in `D union (B-{b})` has colour `i`.
Likewise `b` has colour `j` under `beta`, so no neighbour in
`A union (B-{b})` has colour `j`.  This proves (2.2), including
nonemptiness.

Consider in `G[D union B]` the full `i`--`j` component under `alpha`
which contains `b`.  In the boundary two-colour graph, `{b}` is a component:
the colour `j` is absent from the boundary under `phi`, and the other
vertices of colour `i` are nonadjacent to `b` because `phi` is proper.  If
the full component met the boundary only at `b`, interchanging `i,j` on it
would change the boundary colouring from `phi` to exactly `psi`.  This
would extend `psi` through the `D`-shore, contrary to the hypothesis.
Thus the component meets `C`.  A shortest path from `b` to `C`, stopped at
its first boundary vertex after `b`, has all internal vertices in `D`.
This is `P_D`.

The reverse argument in `G[A union B]` starts from `beta`.  The singleton
`{b}` is again a boundary `i`--`j` component, now with `b` coloured `j`.
If its full component met no member of `C`, an interchange would extend
`phi` through the `A`-shore.  A shortest path to `C` therefore gives
`P_A` with all internal vertices in `A`.  This also proves `C` is nonempty.
Both interiors are nonempty because `b` is nonadjacent to every member of
`C`.  They are disjoint because they lie in the disjoint open shores.
The ends of `P_A` have different colours `j,i`, whereas the ends of `P_D`
both have colour `i`; their respective lengths are therefore odd and even.

It remains to prove the common-host statement.  In any `q`-colouring of
`G-b`, and for any two colours `r,s`, some `r`--`s` component contains a
neighbour of `b` of each colour.  Otherwise interchange `r,s` on the union
of all `r`--`s` components which contain an `r`-coloured neighbour of `b`.
By assumption none contains an `s`-coloured neighbour of `b`; after the
interchanges colour `r` is absent from `N_G(b)`, so `b` can receive `r`, a
contradiction.

Apply this observation to `r=i,s=j` and use (2.2).  A simple path in the
resulting component from an `i`-neighbour in `A` to a `j`-neighbour in `D`
must meet `B-{b}`, because the two open shores are anticomplete.  Every
boundary vertex on the path has colour `i` or `j`; by (1.2) it therefore
belongs to `C`.  Adding `b` and the two incident edges closes the path to a
cycle.  The path has odd length, so the cycle is odd.  Finally, when
`C={x}`, both paths in (2.3) have endpoint `x`; their internally disjoint
union is a cycle, and the parity calculation above makes it odd.  This
proves the theorem. \(\square\)

## 3. The order-nine separator consequence

### Corollary 3.1

Assume in addition that `G` is seven-connected and `|B|=9`.  For
`Z in {A,D}`, let `Q_Z` be the component of `G-B` containing the internal
vertices of `P_Z`.  Then

\[
                         7\le |N_G(Q_Z)|\le9.            \tag{3.1}
\]

Thus each shore gives exactly one of the following:

1. an actual order-seven separation;
2. an actual order-eight separation; or
3. a connected subgraph adjacent to every literal vertex of `B`.

The conclusions for `A` and `D` are supported in distinct components of
`G-B`.

### Proof

The component `Q_Z` is nonempty and its neighbourhood is contained in
`B`.  The opposite open shore is nonempty and lies outside
`Q_Z union N_G(Q_Z)`, so `N_G(Q_Z)` is the boundary of an actual
separation.  Seven-connectivity gives the lower bound in (3.1), and
`|B|=9` gives the upper bound.  Equality nine says precisely that `Q_Z` is
adjacent to every boundary vertex.  The two components are distinct
because they lie in different open shores. \(\square\)

### Corollary 3.2 (palette-drop normalization)

Let `theta` be a proper boundary colouring using all `q` colours, and let
`theta'` be obtained from it by interchanging colours `i,j` on one
component `K` of the boundary `i`--`j` graph.  If `theta'` uses fewer than
`q` colours, then, after interchanging `i,j` if necessary,

\[
             K=\{b\},\qquad \theta^{-1}(j)=\{b\},
             \qquad |\theta^{-1}(i)|\ge1,               \tag{3.2}
\]

and `theta'` is obtained simply by recolouring `b` from `j` to `i`.
Equivalently, reversing the move has exactly the form (1.2): it recolours
one vertex from `i` to a previously unused colour `j`.

Consequently, in the residual in which every full boundary trace extends
through exactly one shore, any palette-dropping boundary Kempe step between
oppositely owned traces enters Theorem 2.1.  It therefore has literal direct
entries of the two colours in opposite shores and gives Corollary 3.1.

#### Proof

A Kempe interchange can make only one of its two colours disappear.  Say
`j` disappears.  Then every old `j`-coloured boundary vertex belongs to
`K`, while `K` contains no old `i`-coloured vertex (such a vertex would
receive colour `j`).  Since a colour class is independent and `K` is
connected, `K` consists of one vertex `b`; it is the entire old `j` colour
class.  The colour `i` occurred in the full colouring and no `i`-vertex
belonged to `K`, so at least one `i`-vertex remains outside it.  This proves
(3.2).  Reversing the interchange gives (1.2), and the final assertion is
Theorem 2.1 and Corollary 3.1. \(\square\)

## 4. Relation to existing results and exact limitation

The recolouring `phi -> psi` is an `i`--`j` Kempe interchange on the
singleton component `{b}` of the boundary two-colour graph.  The two paths
in Theorem 2.1 are therefore the singleton specialization of the audited
[opposite-shore single Kempe-transition theorem](../results/hc7_opposite_shore_single_kempe_transition.md).
The present formulation adds the glued colouring of `G-b`, the exact shore
ownership (2.2), the common-host odd cycle, and the order-nine
seven/eight/full-boundary trichotomy.

An order-seven outcome in Corollary 3.1 is not yet a compatible-colouring
outcome: the two selected traces differ at `b`, and the forced path shows
why the singleton interchange is obstructed on that shore.  In the
order-nine alternative the two boundary-full components are anticomplete,
so they do not by themselves give two adjacent branch sets.  Finally, the
two forced edges at `b` share an endpoint; the audited two-edge
direct-entry theorem requires two vertex-disjoint crossing edges and does
not apply without an additional literal split.  No `K_7`-minor model or
state-preserving descent follows from the hypotheses above alone.
