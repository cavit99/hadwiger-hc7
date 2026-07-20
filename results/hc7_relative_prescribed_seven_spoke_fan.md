# A prescribed seven-spoke fan inside one side of an eight-separation

**Status:** written proof; [separate internal audit](hc7_relative_prescribed_seven_spoke_fan_audit.md)
GREEN.  This is an unbounded host-level reduction for the two-component
order-eight response problem.  It does not prove `HC_7`.

## 1. A relative prescribed-fan theorem

### Theorem 1.1

Let `G` be a seven-connected graph, let `S` be a set of eight vertices,
and let `C` be a component of `G-S`.  Assume that `G-S` has another
component.  Fix `v in C` and seven distinct edges

\[
                         vv_1,\ldots,vv_7.             \tag{1.1}
\]

Then at least one of the following holds.

1. There are seven paths `P_1,...,P_7` in `G[C union S]` such that

   - `P_i` begins with the prescribed edge `vv_i`;
   - the paths are pairwise vertex-disjoint outside `v`;
   - their other ends are seven distinct vertices of `S`; and
   - no path contains another vertex of `S`.

2. There is a nonempty connected proper subset `A` of `C` such that

   \[
                              |N_G(A)|=7.              \tag{1.2}
   \]

   Its full neighbourhood is the boundary of an actual separation with
   two nonempty open sides.

#### Proof

The first neighbours in (1.1) all belong to `C union S`, because `C` is a
component of `G-S`.  Put

\[
 D=\{v_i:v_i\in S\},\qquad
 U=\{v_i:v_i\in C\}.                                  \tag{1.3}
\]

Thus `D,U` are disjoint and `|D|+|U|=7`.  In the graph

\[
                     H=G[(C-\{v\})\cup(S-D)]           \tag{1.4}
\]

apply the vertex-set form of Menger's theorem between `U` and `S-D`.

If `U` is empty, all seven prescribed edges end in `S` and are already
the required paths.  Assume therefore that `U` is nonempty.

Suppose first that there are `|U|` pairwise vertex-disjoint paths between
these two sets.  Since the source set has order `|U|`, every source is an
end of one path, and the other ends are distinct.  Truncate each path at
its first vertex of `S-D` and prepend its corresponding edge from `v`.
Together with the direct paths `vv_i` for `v_i in D`, these are the seven
paths in outcome 1.  Their ends are distinct because `D` and `S-D` are
disjoint, and truncation makes each end its path's only boundary vertex.

Otherwise Menger's theorem gives a set `Z subseteq V(H)` with

\[
                              |Z|\le |U|-1              \tag{1.5}
\]

which separates `U` from `S-D`; terminals are allowed to belong to `Z`.
Choose `u in U-Z`, and let `A` be the component of `H-Z` containing `u`.
No surviving member of `S-D` belongs to `A`, while members of `Z` have
been deleted, so `A subseteq C-\{v\}`.
Componenthood in `H-Z`, together with the fact that `C` is a component of
`G-S`, gives

\[
                    N_G(A)\subseteq \{v\}\cup D\cup Z. \tag{1.6}
\]

Consequently

\[
 |N_G(A)|\le1+|D|+|Z|
          \le1+|D|+(|U|-1)=7.                         \tag{1.7}
\]

The set `A` is nonempty and connected.  A different component of `G-S`
lies outside `A union N_G(A)`, so `N_G(A)` is the boundary of a genuine
separation.  Seven-connectivity forces equality in (1.7), proving (1.2).
Since `v notin A`, the set `A` is a proper subset of `C`.  This is outcome
2. \(\square\)

### Corollary 1.2 (generic exact-seven restart)

In outcome 2, choose any edge `xy` with `x in A` and
`y in N_G(A)`.  If every proper minor of `G` is six-colourable and `G`
itself is not, then every proper six-colouring of `G-xy` gives `x,y` one
colour.  Its boundary equality partition extends through the edge-deleted
closed `A`-side and through the opposite closed side, but not through the
intact closed `A`-side.  Hence `A,N_G(A);xy` is a generic exact-seven
selected-response interface.

#### Proof

The proper minor `G-xy` is six-colourable.  Its ends must have one colour,
or the edge could be restored.  The colouring restricts properly to both
edge-deleted closed shores.  If its equality partition on `N_G(A)` also
extended through the intact `A`-side, align the at most six colour names on
the boundary and glue the two closed-shore colourings.  This would
six-colour `G`, a contradiction. \(\square\)

The restart is strictly smaller than `C`.  It is a strict step in a
generic exact-seven recursion only when `C` itself is known to lie inside
the previously ranked operated shore; that provenance is not part of
Theorem 1.1.

## 2. Application to a crossing-edge response

Assume now that `G` is not six-colourable and every proper minor is
six-colourable.  Let

\[
                         e=pv,\qquad p\in S,quad v\in C,          \tag{2.1}
\]

and let `c` be a proper six-colouring of `G-e`.  Put

\[
                         c(p)=c(v)=\alpha.                         \tag{2.2}
\]

For every alternate colour `beta`, the `alpha`--`beta` component of
`G-e` containing `v` also contains `p`.  Otherwise an interchange on the
component containing `v` would give `p,v` different colours and allow
`e` to be restored.  Choose an `alpha`--`beta` path from `v` to `p`.
Its first edge at `v` has a `beta`-coloured other end.  The five alternate
colours therefore give five distinct first edges, all different from
`e`.

Seven-connectivity gives `d_G(v)>=7`, so choose any seventh incident edge
different from these six.  Theorem 1.1 gives the following exact
alternative.

### Corollary 2.1

Every crossing-edge response at a component behind an order-eight boundary
gives either

1. a generic exact-seven selected-response interface on a connected
   proper subset of the operated component; or
2. seven paths inside that component together with the boundary, beginning
   respectively with the deleted edge, the five colour-indexed first
   edges, and one further incident edge, and ending at seven distinct
   literal boundary vertices.

The rerouted paths in outcome 2 retain the six operation-specific first
edges.  Except for the direct deleted edge, they need not remain
bichromatic.

## 3. A minor decoder for the relative fan

Retain outcome 2 of Corollary 2.1, and suppose `G-S` has a second component
`C'` which is adjacent to every vertex of `S`.  The path beginning with
`vp` is the direct edge `vp`, because `p` is already a boundary vertex.
Delete `v` from each of the other six paths and call the resulting
connected paths

\[
                              L_1,\ldots,L_6.           \tag{3.1}
\]

They are pairwise vertex-disjoint, avoid `p`, and have six distinct ends
in `S-\{p\}`.  Define their **contact graph** `J` on vertex set `[6]` by

\[
 ij\in E(J)
 \quad\Longleftrightarrow\quad
 E_G(V(L_i),V(L_j))\ne\varnothing.                    \tag{3.2}
\]

### Theorem 3.1 (contact-minor decoder)

If `J` contains a `K_5` minor, then `G` contains an explicit `K_7`-minor
model.

#### Proof

Let `M_1,...,M_5` be the five branch sets of a `K_5`-minor model in `J`.
For each `j`, put

\[
                     B_j=\bigcup_{i\in M_j}V(L_i).     \tag{3.3}
\]

Connectivity of `M_j` in the contact graph and the literal contact edges
from (3.2) make `G[B_j]` connected.  The five sets are pairwise disjoint
and pairwise adjacent.

The following seven sets are pairwise disjoint:

\[
                 \{v\},\qquad C'\cup\{p\},\qquad
                 B_1,\ldots,B_5.                      \tag{3.4}
\]

The second set is connected because `C'` is connected and is adjacent to
`p`.  It is adjacent to `{v}` through the edge `vp`.  Every `B_j` contains
a limb with a boundary end `s`; fullness of `C'` supplies an edge from
`C'` to `s`, so the second set is adjacent to every `B_j`.  Finally `{v}`
is adjacent to every `B_j` through the prescribed first edge of any limb
in that branch set.  Thus the seven sets in (3.4) are pairwise adjacent
connected branch sets, proving the theorem. \(\square\)

### Corollary 3.2

In a `K_7`-minor-free host, every relative seven-spoke response fan has a
six-vertex `K_5`-minor-free contact graph.  In particular that contact
graph is four-colourable by the known case `HC_5`.

## 4. Coupling one response fan from each component

Let `S` be an eight-set and let `C,D` be two distinct components of `G-S`.
Fix
`p in S`, neighbours `v in C`, `w in D`, and relative seven-spoke fans
as in Theorem 1.1, with direct prescribed spokes `vp` and `wp`.  Each fan
ends at seven distinct vertices of `S`; let `r_C,r_D` be its unique
omitted boundary vertex.

Put

\[
                 T=S-\{p,r_C,r_D\}.                  \tag{4.1}
\]

Thus `|T|` is six when `r_C=r_D` and five otherwise.  For `s in T`, let
`P_s^C,P_s^D` be the two fan paths ending at `s`, and define the
**common-endpoint column**

\[
                 L_s=(P_s^C-v)\cup(P_s^D-w).          \tag{4.2}
\]

Each `L_s` is connected through its common boundary vertex `s`.  The
columns are pairwise vertex-disjoint: the two fan systems are separately
disjoint outside their roots, the open components are disjoint, and the
boundary ends are distinct.  They avoid `p`, since each relative fan path
contains no boundary vertex other than its end.

Define the **coupled contact graph** `J` on vertex set `T` by

\[
 st\in E(J)
 \quad\Longleftrightarrow\quad
 E_G(V(L_s),V(L_t))\ne\varnothing.                   \tag{4.3}
\]

### Theorem 4.1 (paired-fan contact decoder)

If `J` contains a `K_5` minor, then `G` contains an explicit
`K_7`-minor model.

#### Proof

Let `M_1,...,M_5` be the branch sets of a `K_5` model in `J` and put

\[
                       B_i=\bigcup_{s\in M_i}V(L_s).   \tag{4.4}
\]

Contact edges make the five sets connected and pairwise adjacent.  They
are disjoint from the two connected sets

\[
                              \{v,p\},\qquad\{w\}.     \tag{4.5}
\]

The sets in (4.5) are adjacent through `pw`.  For every column, `v` is
adjacent to its `C`-side first vertex and `w` to its `D`-side first vertex.
Consequently each set in (4.5) is adjacent to every `B_i`.  Thus the five
sets in (4.4), together with (4.5), are seven pairwise adjacent connected
branch sets. \(\square\)

### Corollary 4.2 (coupled response normal form)

Suppose `G` is seven-connected, every proper minor of `G` is
six-colourable, and `G` itself is not.  For crossing edges `pv,pw`, apply
Corollary 2.1 separately in `C` and `D`.  Then either

1. one application returns a generic exact-seven selected-response
   interface on a proper connected subset of its component; or
2. the two response fans form the common-endpoint columns (4.2), and their
   coupled contact graph is `K_5`-minor-free whenever `G` is
   `K_7`-minor-free.

The two fan colourings may be different.  Only their literal boundary ends
and paths are coupled; no palette colour is identified with a column or a
minor-model label.

## 5. Exact contribution and trust boundary

Theorem 1.1 strengthens the previous component-internal five-path
alternative in two ways: all seven selected first edges are retained, and
the boundary ends are distinct.  Theorems 3.1 and 4.1 remove every single
fan or paired common-endpoint system whose literal contact graph contains a
`K_5` minor.  All statements hold for arbitrarily large components.

The surviving contact graph can nevertheless be `K_5`-minor-free, and its
four-colourability does not by itself synchronize the two closed-shore
colourings.  The theorem does not identify palette colours with old
minor-model labels, preserve bichromaticity after rerouting, or prove that
the complete family of crossing-edge responses cannot keep producing
`K_5`-minor-free coupled contact graphs.  Contact graphs from separately
chosen, nonaligned limb systems may not be united; Theorem 4.1 works only
because its columns form one common literal system.  The remaining
response-coupling implication remains open.

## 6. Dependencies

- vertex Menger's theorem;
- seven-connectivity and proper-minor six-colourability; and
- the known case `HC_5`, only for the final four-colourability observation.
