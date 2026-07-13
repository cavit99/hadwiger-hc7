# Independent audit: exact-seven two-lobe gate exchange

## Verdict

**GREEN after two local clarifications.**  The forbidden-label Hall
separator, the endpoint-inclusive lobe-to-gate linkages, the small-shore
rooted lift, and both four-carrier constructions are valid.  The two
clarifications now incorporated in the theorem file are:

1. `|A(K)|>=4` is proved directly from the separator `T union A(K)` when
   `|K|<4`; it does not follow from the matching lower bound alone in
   those small lobes.
2. In the path-gate proof the two portal/linkage indices may be interchanged
   so that the path beginning at `x_i` terminates at the intended leaf
   `t_i`.

No contraction-criticality, colour-state identification, virtual web edge,
or connectivity stronger than the stated seven-connectivity of `G` and
three-connectivity of `G[L]` is used.

## 1. Preliminary gate fact

Every component `K` of `G[L]-T` has a neighbour at each literal member of
`T`.  Otherwise, if `t in T` had no neighbour in `K`, then `T-{t}` would
separate `K` from the other lobe, contradicting three-connectivity of
`G[L]`.  This justifies every later assertion that a whole lobe is adjacent
to each bag containing a different gate vertex.

## 2. Forbidden-label Hall separator

Let `f=|F|` and let `m` be the maximum matching order in the bipartite
portal graph with sides `S-F` and `V(K)`.  The deficiency identity on the
`S-F` side is exactly

\[
 m=\min_{U\subseteq S-F}
       \bigl((7-f)-|U|+|N_K(U)|\bigr).
\]

For a minimizing `U`, the proposed deletion set

\[
 X=T\cup F\cup((S-F)-U)\cup N_K(U)
\]

has order `3+f+m`; all four displayed pieces are disjoint.  If
`m<min{4-f,|K|}`, then this order is below seven.  Moreover
`K-N_K(U)` is nonempty: equality `N_K(U)=K` would imply
`m=(7-f)-|U|+|K|>=|K|`.  A vertex in `K-N_K(U)` cannot leave through
`U`, while every other boundary label, every gate vertex, and every
internal exit through `N_K(U)` is deleted.  The other lobe and the
opposite open shore remain.  Hence `X` is a genuine separator of order
below seven.

The separate deletion `T union A(K)` proves `3+|A(K)|>=7`.  Thus the
claimed four-label lower bound also covers singleton, two-vertex, and
three-vertex lobes.  The two stated matching consequences then follow by
taking respectively `F=emptyset, |K|>=3` and `|F|=1, |K|>=2`.

## 3. Endpoint-inclusive set Menger

For three starts `X subseteq K`, failure of three disjoint `X`--`T` paths
in `G[K union T]` produces an endpoint-inclusive hitting set `Z` of order
at most two.  Since both terminal sets have order three, a start and a
gate vertex survive.  The component of a surviving start in
`G[L]-Z` cannot reach `T-Z`: any route from `K` first reaches `T` and
would yield an `X`--`T` path avoiding `Z`.  The other lobe remains and
meets every surviving gate vertex, so `G[L]-Z` is disconnected, contrary
to three-connectivity.

For two starts and the two leaves `U=T-{w}`, the same argument in
`G[K union U]` gives a hitting set `Z` of order at most one.  Now
`Z union {w}` has order at most two.  A start and a leaf survive, the
start component has no exit from `K` except through deleted `w` or an
unreachable surviving member of `U`, and the other lobe remains on the
far side.  This again contradicts three-connectivity.  Thus the proof
does not silently require internally disjoint paths with common endpoints:
the endpoints themselves are distinct, because the paths are
vertex-disjoint in the endpoint-inclusive version of Menger.

Truncation at each first gate hit keeps the `K`-parts disjoint and prevents
a path from wandering through another gate vertex.

## 4. Small-shore rooted lift

Because `G[L]` is three-connected, `L` is one connected open-shore
component.  The actual-adhesion portal theorem therefore supplies an
`S`--`L` matching of order `min{7,|L|}`.  For `|L|<=7` it saturates all
of `L`.  Every three-connected graph contains a `K_4` minor.  Select one
actual vertex from each of its four branch sets; their matching partners
are four distinct literal vertices of `S`.  The selected vertices root
the already chosen `K_4` bags, so the audited four-portal lift with the
three disjoint `S`-full packets produces seven literal branch sets.  No
claim that an arbitrary four prescribed vertices root a `K_4` is being
made.

## 5. Triangle-gate carrier construction

After the small-shore case, `|C|+|D|>=5`, so one lobe has at least three
vertices.  The matching lemma chooses three distinct portal vertices with
three distinct labels in that lobe, and the order-three linkage gives
three disjoint path bags ending at the three distinct gate vertices.

The other lobe is adjacent to every path bag through its literal contact
with that bag's gate vertex.  The three path bags are pairwise adjacent
through the three **literal** edges of `G[T]`.  Their labels are distinct,
and the other lobe has at least four labels, so it has a fourth label
outside those three.  The four-carrier lift is therefore exact.  No edge
of a completed web triangle is substituted for a literal gate edge.

## 6. Path gate with a labelled middle

After choosing two portals in `D` while forbidding the middle label `q`,
the order-two linkage in `G[D union {t_1,t_3}]` gives disjoint initial
path trees from the portal vertices to distinct leaves.  Relabeling the
two portal pairs if necessary aligns `x_i` with `t_i`.

The two disjoint path trees can be joined by a shortest path in `D` whose
internal vertices avoid both.  Their union is a tree and hence extends to
a spanning tree of connected `G[D]`.  Deleting an edge on the unique
connector divides `D` into nonempty connected sets `X_1,X_3`, retains the
respective portal and leaf contact in each part, and leaves a literal
`X_1X_3` edge.

The six pairwise adjacencies among

\[
 X_1\cup\{t_1\},\quad X_3\cup\{t_3\},\quad C,\quad\{t_2\}
\]

are exactly: the deleted tree edge; the three contacts of `C` with
`t_1,t_2,t_3`; and the two literal path edges `t_1t_2,t_2t_3`.
The first, second, and fourth bags have the distinct labels
`s_1,s_3,q`; `A(C)` has size at least four and supplies a fourth.
Thus this also gives a literal four-carrier lift.

## 7. Exact trust boundary

The proved residue is only the one stated in Section 6 of the theorem:
a target-free two-lobe gate has `|L|>=8`, no literal gate triangle, and
an unlabelled middle whenever its literal gate graph is a two-edge path.
Together with the previously audited edge exchange, each literal gate
edge has endpoint portal rank at most one.  The proof does **not** close
zero-edge, one-edge, or unlabelled-middle path gates, and it does not
produce a rooted triangle after deleting either lobe.
