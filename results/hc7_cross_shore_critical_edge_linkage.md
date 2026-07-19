# Opposite-shore critical edges give a rooted four-vertex model or an exact seven-separation

**Status:** written proof; separate internal audit GREEN in
[`hc7_cross_shore_critical_edge_linkage_audit.md`](hc7_cross_shore_critical_edge_linkage_audit.md).
This theorem is
uniform and unbounded.  It uses one critical edge from each open shore of a
separation and replaces the boundary-colouring drift between their two
proper-minor responses by literal host geometry.  It does not yet preserve a
selected five-label minor model across the returned separation, synchronize a
complete boundary partition, or prove `HC_7`.

## 1. Setting

Let `G` be a seven-connected graph such that

\[
 \chi(G)=7
 \quad\text{and}\quad
 \chi(M)\le 6\text{ for every proper minor }M\text{ of }G.       \tag{1.1}
\]

Let

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}D,
 \qquad E_G(A,D)=\varnothing,                                  \tag{1.2}
\]

where `A,D` are nonempty.  Choose edges

\[
                    h=ab\in E(G[A]),
             \qquad e=cd\in E(G[D]).                            \tag{1.3}
\]

The four ends in (1.3) are distinct.  Put

\[
                         H=G-\{h,e\}.                            \tag{1.4}
\]

Thus the braces in (1.4) mean edge deletion.

## 2. Exact chromatic and connectivity compression

### Lemma 2.1

The graph `H` satisfies

\[
                         \chi(H)=6,
                  \qquad \kappa(H)\ge5.                         \tag{2.1}
\]

Moreover, for each nonempty subset `C` of `{h,e}`, `H` has a proper
six-colouring in which the ends of precisely the edges in `C` receive the
same colour.  No proper six-colouring of `H` makes both pairs proper.

#### Proof

The graph `H` is a proper minor of `G`, so `chi(H)<=6`.  Suppose that `H`
had a proper colouring with at most five colours.  Recolour `a` and `c`
with one new sixth colour.  The vertices `a,c` are nonadjacent by (1.2),
and the new colour was previously absent.  The recolouring makes both
deleted edges proper: their other ends `b,d` retain old colours.  It is
therefore a proper six-colouring of `G`, a contradiction.  Hence
`chi(H)=6`.

The two deleted edges form a matching.  For a separation `(L,T,R)` of
`H` with both open sides nonempty, every `L`--`R` path in `G` either meets
`T` or uses one of `h,e` from one open side to the other.  Seven internally
disjoint paths between fixed vertices of `L,R` therefore give

\[
       |T|+|\{g\in\{h,e\}:g\text{ has one end in each open side}\}|
       \ge7.                                                   \tag{2.2}
\]

The second term is at most two, so `|T|>=5`.  This proves the connectivity
bound.

For a nonempty `C subseteq {h,e}`, contract every edge in `C`, take a
six-colouring of the resulting proper minor, expand the contracted
vertices, and delete both edges.  The ends of the edges in `C` are equal.
Every edge outside `C` was still present after the contractions (the two
edges are vertex-disjoint), so its ends are different.  This gives the
three asserted signatures.  An all-proper colouring of `H` would already
colour `G`.  \(\square\)

The equality `chi(H)=6` is where the placement in opposite shores is used:
one endpoint of each failed edge can be recoloured with the same fresh
colour.  For two arbitrary critical edges, the common deletion can be
five-colourable.

## 3. Rooted model or exact seven-separation

### Theorem 3.1

At least one of the following holds.

1. The graph `H` contains a `K_4`-minor model rooted at `a,b,c,d`: four
   pairwise disjoint connected branch sets, one containing each of these
   four specified vertices.
2. The graph `G` has an actual separation of order seven obtained from an
   order-five separation of `H`.  Both deleted edges cross the two open
   sides of the order-five separation.  For **every** choice of one end of
   each edge, adjoining the two chosen ends to its five-vertex boundary
   leaves both open sides nonempty and gives an actual order-seven
   separation of `G`.

In outcome 2 the endpoint choice may therefore be made to retain any
preassigned side placement which is achieved by choosing one end of `h`
and one end of `e`.  In particular, a two-vertex branch set supported by
either deleted edge can be kept in either desired closed side whenever its
other named branch sets already lie there.

#### Proof

By Lemma 2.1, `H` is five-connected.  If it is six-connected, Jung's
two-linkage theorem says that it is two-linked.  Hence each of the three
pairings of the four nominated vertices `a,b,c,d` has two vertex-disjoint
linking paths in `H`.  The rooted-`K_4` characterization for a
three-connected graph (Fabila-Monroy--Wood, Theorem 8) now gives a
`K_4`-minor rooted at the four vertices.  This is outcome 1.

It remains that `kappa(H)=5`.  Choose an order-five separation
`(L,T,R)` of `H`.  Inequality (2.2) forces both deleted edges to cross its
open sides.  Select one end of each crossing edge and adjoin the selected
vertices to `T`.  Deleting this seven-set removes every edge of `G` from
the residual left shore to the residual right shore.

We show that neither residual shore can be empty, for any of the four
endpoint choices.  Suppose, by symmetry, that the selected ends exhaust
`L`.  Then `L` consists of two vertices, one end of each deleted edge.  A
vertex of `L` can have neighbours only among the other vertex of `L`, the
five vertices of `T`, and its mate across the deleted edge.  Since
seven-connectivity gives minimum degree at least seven, all seven possible
neighbours occur.  Thus `L` is a clique complete to `T`.

Use the simultaneous-contraction colouring from Lemma 2.1 in which the
ends of both deleted edges are equal.  In `H`, the two vertices of `L`
have distinct colours because they are adjacent; their two mates have the
corresponding colours, while no vertex of `T` has either colour because
`L` is complete to `T`.  Interchange the two colours on the two vertices
of `L`, leaving every other vertex fixed.  Edges inside `L` and from `L`
to `T` remain proper, and both deleted crossing edges become proper.
There are no other edges between the two open sides.  This produces a
proper six-colouring of `G`, a contradiction.

Therefore every endpoint choice leaves two nonempty open sides.  The
chosen seven-set is the boundary of an actual separation of `G`, proving
outcome 2 and the side-placement assertion.  \(\square\)

The proof of the second outcome is the two-edge specialization of the
matching-deletion separator and derangement argument.  It is included here
because the universal quantifier over endpoint choices is what permits a
later label-preserving lift.

## 4. Two repeated critical contacts on the opposite shore

Let `e,f` be two distinct persistent critical edges in `G[D]`, and keep
the edge `h` in `G[A]`.  Applying Theorem 3.1 separately to `(h,e)` and
`(h,f)` gives the following exact fork.

### Corollary 4.1

For each `g in {e,f}`, either

1. `G-{h,g}` contains a `K_4`-minor rooted at the four ends of `h,g`; or
2. `G` has an actual order-seven separation obtained by a universally
   valid endpoint lift of an order-five separation of `G-{h,g}`.

Thus an operation on the opposite shore cannot be represented only by a
new boundary equality partition: it yields either a rooted model through
the two critical edges or an exact literal boundary.  If the exact
separation preserves the five inherited branch-set labels and one selected
boundary partition on one closed side, the selected-response preservation
theorem reduces its remaining colouring obligation precisely to a
partition-specific connected-subgraph system on that same side.

#### Proof

The edge `h` is vertex-disjoint from each of `e,f` by (1.2), so Theorem
3.1 applies twice.  The last sentence invokes only the stated hypotheses
of the selected-response preservation theorem; it is not an assertion that
the endpoint lift supplies those hypotheses automatically.  \(\square\)

The three edges can also be kept on one common deletion host.  This gives a
sharper distinction between the independent and incident repeated-contact
configurations.

### Theorem 4.2 (joint three-edge chromatic fork)

Put

\[
                         J=G-\{h,e,f\}.                          \tag{4.1}
\]

1. If `e,f` are vertex-disjoint, then

   \[
                           \chi(J)\in\{5,6\}.                    \tag{4.2}
   \]

   If `chi(J)=5`, every end of `e` is adjacent to every end of `f`.
   Consequently the four ends of `e,f` induce a `K_4` in `G`.

2. If `e=sw` and `f=st` are incident, then

   \[
                           \chi(J)=6.                             \tag{4.3}
   \]

3. If `e,f` are vertex-disjoint, then for every nonempty subset `C` of
   `{h,e,f}`, the graph `J` has a six-colouring in which the ends of
   precisely the edges in `C` are equal.  If `e=sw,f=st` are incident, the
   same assertion holds for every nonempty `C` which does not contain both
   `e,f`; it also holds for sets containing both `e,f` when `wt` is not an
   edge of `G`.  The all-proper signature is absent in either case.

4. In the vertex-disjoint case, `kappa(J)>=4`.  If equality holds, every
   order-four separation of `J` is crossed by all three deleted edges, and
   every choice of one endpoint on each edge lifts it to an actual
   order-seven separation of `G`.

#### Proof

First suppose that all three edges are vertex-disjoint.  If `J` were
four-colourable, recolour one end of `h` and one end of `e` with a new
fifth colour and one end of `f` with a new sixth colour.  The chosen end of
`h` is anticomplete to both chosen ends in `D`; using separate fresh colours
on the latter two also handles a possible edge between them.  This restores
all three deleted edges and six-colours `G`.  Hence `chi(J)>=5`, while
minor-minimality gives the reverse upper bound six.

Suppose `chi(J)=5`.  If some end `c` of `e` and some end `s` of `f` were
nonadjacent, choose either end `a` of `h`.  The set `{a,c,s}` is independent
because of (1.2).  Recolour its three vertices with one fresh sixth colour.
This restores all three deleted edges and again six-colours `G`.  Therefore
all four edges between the two endpoint pairs occur.  Together with `e,f`,
they induce the asserted `K_4`.

Now let `e=sw,f=st`.  A five-colouring of `J` can be extended to a
six-colouring of `G` by recolouring one end `a` of `h` and the common end
`s` with one fresh colour.  The vertices `a,s` are nonadjacent by (1.2),
and changing `s` repairs both incident deleted edges.  This contradiction
proves (4.3).

For item 3, contract the edges of any permitted nonempty set `C`, six-colour
the proper minor, expand the contracted vertices, and delete all three
edges.  In the matching case, no uncontracted edge has its ends identified
by the contractions.  In the incident case the only additional possible
edge internal to the component formed by contracting both `e,f` is `wt`;
this is why a set containing both incident edges is permitted only when
`wt` is absent.  The resulting signature is therefore exact.  An
all-proper colouring restores all three edges and is impossible.

Finally, in the vertex-disjoint case the three edges form a matching.
The matching-deletion separator budget gives `kappa(J)>=4`; at equality all
three edges cross.  Item 3 is the exact matching-signature property, so the
derangement-lift theorem makes every endpoint selection an actual
order-seven lift.  \(\square\)

The incident conclusion is useful precisely because it rules out the
five-chromatic common-deletion branch.  In the independent case that branch
survives only with a literal `K_4` on the four repeated-contact endpoints;
the boundary trace is no longer its only structure.

## 5. Relation to a fixed paired boundary trace

Suppose now that `|S|=7` and a paired boundary partition `Pi` is induced
by a proper six-colouring of `G[A union S]`.  Let `e,f` lie in `D` and
suppose their common deletion attains `Pi` **with the fixed equality
trace**: there is a proper six-colouring of
`G[D union S]-{e,f}` which induces `Pi` on `S` and gives equal colours to
the two ends of each of `e,f`.  This is the common-equality branch supplied
by the repeated-exposure argument when neither single deletion attains the
selected trace; it is stronger than mere extendability of `Pi` through the
common deletion.  If `e=sw,f=st` are incident, the equality assumption
itself forces `wt` to be absent.  Choose any edge `h in E(G[A])`.

The common graph

\[
                        G-\{h,e,f\}                              \tag{5.1}
\]

then has both of the following literal colouring chambers:

* a colouring inducing `Pi` on `S`, with `e,f` monochromatic and `h`
  proper; and
* a colouring obtained from `G/h`, with `h` monochromatic and `e,f`
  proper.

The second colouring induces a partition extending through the original
closed `D`-shore, and therefore its partition is different from `Pi`.
This is the exact cross-shore drift.  Corollary 4.1 shows that the drift is
accompanied, for each persistent edge, by either an endpoint-rooted `K_4`
model or a universally orientable exact seven-separation.

#### Justification

For the first chamber, glue the fixed `Pi` colouring of the `A`-closed
shore to the fixed-trace colouring of `G[D union S]-\{e,f\}`.  The edge
`h` is present and proper.  For the second, colour the proper minor `G/h`,
expand its contraction vertex, and then delete `e,f`; those two edges were
present in `G/h` and hence are proper.  The restriction to the unchanged
`D`-closed shore is a proper colouring.  If its boundary partition were
`Pi`, it would glue to the original `Pi` colouring of the `A`-closed shore
and six-colour `G`, contrary to (1.1).

### Proposition 5.1 (the universal lift is a mixed-response interface)

Assume outcome 2 of Theorem 3.1 for the pair `h,e`, and orient the crossing
edges so that

\[
                 a,c\in L,\qquad b,d\in R.                 \tag{5.2}
\]

Let `C_eq` be the family of fixed-equality colourings in which `h` is
proper and `e,f` are monochromatic, and let `C_h` be the family obtained by
expanding six-colourings of `G/h`, in which `h` is monochromatic and `e,f`
are proper.  Both are nonempty by the preceding argument.  If `f` has a vertex in
`L-T`, put

\[
                       S^*=T\mathbin{\dot\cup}\{a,d\}.     \tag{5.3}
\]

Then the fixed-equality chamber is proper on the `R`-closed shore of the
lifted order-seven separation, while the `h`-contraction chamber is proper
on its `L`-closed shore.  If instead `f` has a vertex in `R-T`, the same
conclusion holds after putting

\[
                       S^*=T\mathbin{\dot\cup}\{b,c\}      \tag{5.4}
\]

and interchanging left and right.  In either case the sets of boundary
partitions induced on `S^*` by the two legal chamber families are disjoint.
If `V(f) subseteq T`, the fixed-equality chamber is not proper on the lifted
boundary, so it induces no legal boundary partition there.

#### Proof

The edge `f` belongs to `G-\{h,e\}`.  Hence it cannot have one endpoint in
`L-T` and the other in `R-T`.  In the first case it is contained in
`G[L union T]`.  With the endpoint choice (5.3), the edges `e,f` occur only
in the `L`-closed shore, whereas `h` occurs only in the `R`-closed shore.
The fixed-equality chamber is therefore proper on the latter, because `h`
is proper there; the `h`-contraction chamber is proper on the former,
because `e,f` are proper there.  The second case is symmetric.

Suppose that the same equality partition occurred in both legal chamber
families.  Permute one closed-shore colouring so that
the two restrictions agree on `S^*`, then glue the `L`-closed restriction
of the `h`-contraction chamber to the `R`-closed restriction of the
fixed-equality chamber.  Every edge of `G` is proper: the only deleted edges
which occur in a retained closed shore are precisely those declared proper
above.  This gives a six-colouring of `G`, contrary to (1.1).  The two
partition families are therefore disjoint.

Finally, if `V(f) subseteq T`, both endpoints of `f` belong to every lifted
boundary.  They have equal colours in the fixed-equality chamber, so its
restriction to that boundary is not proper.  \(\square\)

Thus endpoint orientation supplies two opposite legal colourings, not a
common boundary partition.  The relevant object on the new boundary is a
transported partition induced by one legal chamber; the old partition `Pi`
is not literally a partition of `S^*`.  To close the separation, that
transported partition must be realized on the other shore by its own named
connected contraction supports.

## 6. Exact gain and remaining obstruction

The theorem uses a proper-minor response from the opposite shore in a way
which is absent from the fixed-trace edge-rotation barriers.  It proves a
host-measured dichotomy and never identifies a palette colour with a
minor-model label.

It does **not** complete the direct-entry exchange.  In the rooted-model
outcome, the four branch sets can traverse the old boundary or inherited
model bags, so they are not automatically disjoint from the three branch
sets which would complete a `K_7` model.  In the separation outcome, the
universal endpoint lift preserves endpoint side choices but does not by
itself preserve the complete five-label tuple or make one equality
partition extend through both closed shores.

The remaining cross-shore theorem has therefore been narrowed to one of
two label-faithful assertions:

1. route the endpoint-rooted `K_4` model while reserving the three named
   completing branch sets, or use its unavoidable intersections to obtain
   a partition-specific connected-subgraph system; or
2. for one legal transported partition on the universally valid endpoint
   lift, preserve five inherited labels as connected contraction supports
   on the opposite shore, then apply exact response preservation on the
   returned order-seven boundary.

Proposition 5.1 shows that the two automatically transported chamber
partitions are incompatible.  A common partition therefore requires new
same-shore connected-support geometry; it cannot be obtained merely by
choosing another orientation of the two deleted edges.

## 7. Dependencies

* the two-edge specialization of the
  [matching-deletion separator budget and derangement lift](../results/hc7_matching_deletion_separator_lift.md);
* H. A. Jung's theorem that every six-connected graph is two-linked,
  quoted as Theorem 1.1 in Stephens--Ye,
  *Connectivity for Kite-Linked Graphs*, arXiv:1912.02873; and
* the rooted-`K_4` characterization for three-connected graphs,
  Fabila-Monroy--Wood, Theorem 8.
