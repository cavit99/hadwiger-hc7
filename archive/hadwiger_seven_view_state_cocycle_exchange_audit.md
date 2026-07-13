# Adversarial audit: retained-bag state/cocycle exchange

## Verdict

**GREEN AS PATCHED, with sharply limited scope.**

The retained-view collapse, equality-state lists, forced portal rows, the
explicit clique-minor models, the arbitrary-order extension, and the
full-host matching criterion are correct.  The selected-skeleton theorem
does not colour an ambient host with extra wrong-layer contacts, and the
note now says so explicitly.  The operation-sensitive conclusion still
requires canonicalizing proper-minor colourings; nothing in this package
alone closes `HC_7`.

During audit I corrected five points:

1. ordinary cycle holonomy was being conflated with the stronger edgewise
   state alignment `s=delta t`;
2. Proposition 6.1 was phrased as extending one fixed cyclic colouring,
   although a perfect matching may choose a different permutation on the
   `Y` layer;
3. the forced boundary nonedges needed by the later colouring argument
   were implicit rather than recorded;
4. Theorem 6.2 incorrectly appeared to require `T` nonempty, although the
   sharp rectangular case can have `T` empty;
5. the former Theorem 6.4 overlooked that canonical deletion of all
   carrier diagonals makes a nonperfect relation impossible already.  It
   has been replaced by the exact diagonal obstruction, and its useful
   mixed rectangular construction has been retained only as an abstract
   relation statement where diagonals may have been suppressed.

## 1. Views, properness, and equality states

For a fixed retained bag `X`, contracting every other bag to a singleton
does not depend on which three neutral images are subsequently designated
as `Q`.  Hence the sixteen structural normalizations are exactly seven
underlying retained-bag minors.

Because the model is spanning, `V_X` has fewer vertices than `G` exactly
when a nonretained bag has order at least two.  Thus:

* at least two nonsingleton bags make all views proper;
* with one nonsingleton bag `Z`, exactly the views retaining `Z` can equal
  `G`;
* with all bags singleton, no view is proper.

The boundary graphs in Proposition 2.1 are respectively

* `K_6` for retained `A`;
* `K_6-AC` for retained `B`;
* `K_6-AB` for retained `C`;
* `K_6-{AB,AC}` for retained `U_j`.

Their independent-set structure gives exactly the displayed list
`R`, `AB`, `AC`.  In the neutral case both repeated pairs cannot occur
simultaneously because `BC` is an edge.  The dark-class assertion follows
directly from properness.

The private-leaf expansion is a valid sharp equality-only obstruction.
A pendant vertex cannot be a singleton branch set in a clique model of
order at least three, and deleting pendant vertices from their branch sets
reduces any alleged `K_7` model to the seven-vertex `K_7^vee` core.  The
state enumeration in (3.1) is exact.

## 2. Forced rows

Lemma 4.1 is correct under its explicit setup that `ab` and `ac` are
absent and every carrier is a literal edge.

In the failed repeated state, the unique free colour is available at each
endpoint.  Since the endpoints are adjacent, failure to colour the edge
means that each endpoint sees every one of the five boundary colours.  For
type zero this forces both endpoints to see `b`, every other carrier, and
at least one of `a,c`.  Extension of the `AB` state then requires one
endpoint `p_i` to miss `c`; it sees `a`, while collective contact puts the
`c` portal at `q_i`.  Type one is symmetric.

The proof also forces, rather than merely omits from the selected
skeleton,

\[
 p_i c\notin E\quad(t_i=0),\qquad
 p_i b\notin E\quad(t_i=1).
\]

Each endpoint of `D_i` meets every `D_j`; applying this in both directions
makes the `2 by 2` contact graph have no isolated vertex, which indeed
forces a perfect matching.

## 3. Models (5.3) and (5.4)

All branch sets in (5.3) are disjoint and connected.  The merged bag
`{p_i,p_j}` uses the parallel edge; it meets `q_i,q_j` through the two
carrier edges, and `q_iq_j` is the other parallel edge.  Every endpoint
meets each whole remaining carrier through a selected matching.  Opposite
types make the two `p` endpoints collectively see both `b,c`, while every
`q` endpoint and every whole carrier sees both.

For (5.4), with `t_i=t_j=0` and `t_k=1`, connectivity uses

\[
 ap_i,\qquad cq_i,\qquad q_jp_k.
\]

The same-type crossed edges are `p_iq_j,q_ip_j`; the two required
opposite-type crossed matchings give

\[
 p_iq_k,q_ip_k,p_jq_k,q_jp_k.
\]

Together with the carrier edges, row edges, and contacts to the whole
bag `D_l`, these cover every pair of displayed branch sets.  Swapping
`b,c` proves the type-one version.  The strengthened verifier now checks
these exact displayed models on every curved instance, independently of
the exhaustive branch-set search.

## 4. Uniform and connected-shore extensions

For `n>=4`, the seven-bag construction uses four carrier indices.  Every
remaining whole carrier is connected, meets every endpoint used in the
base model through its selected perfect matchings, meets every boundary
singleton used through the row table, and meets every other added
carrier.  Adding those `n-4` bags gives `K_{n+3}`.

When `s=delta t`, switching type-one endpoints turns every selected pair
into two `K_n` layers.  The cyclic shift colours the literal edge skeleton
with `n+2` colours.  This statement is only about the selected skeleton.

The connected-shore version is also valid: replacing each endpoint by a
connected shore preserves every connectivity and adjacency used in
(5.3)--(5.4).  Its flat conclusion is two labelled clique **models**, not
a colouring of the interiors of the shores.

The algebraic language is now precise.  `s=delta t` is edgewise
state alignment.  It is stronger than ordinary zero cycle holonomy: a
different coboundary has zero cycle holonomy but nonzero discrepancy
`s+delta t`, and the theorem correctly gives a clique minor in the mixed
state case.

## 5. Full-host relation

In the flat full edge host, each layer is a `K_n`.  Fixing colour `i` on
`x_i` forces the `Y` layer to use the same palette by a permutation.
Colour `i` may be assigned to `y_j` exactly when `x_i y_j` is absent.
Thus Proposition 6.1 is exactly the perfect-matching criterion for `M_F`.
It permits a new `Y`-permutation and need not preserve the particular
cyclic shift used to colour the minimal skeleton.

The rectangular classification in Theorem 6.2 is correct, including
`T=emptyset`.  If `S` is Hall-deficient and every missing edge repairs
the graph, then `|N(S)|=|S|-1`; maximality fills `T times S` and
`L times (R-S)`, leaving exactly `(L-T) times S` as the obstruction.

The co-rank theorem is also correct.  The carrier core is co-bipartite,
so a maximum matching of its cross-nonedge graph pairs exactly `nu`
two-vertex colour classes, giving

\[
 \chi=2n-\nu.
\]

By Konig, deleting a minimum vertex cover of the nonedge graph leaves an
actual clique of the same order, so `omega=2n-nu`.  If `nu<=n-2`, this
clique has order at least `n+2`; the connected universal-to-the-core bag
`{b,c}` supplies the final branch set of `K_{n+3}`.

The corrected diagonal theorem is stronger than the earlier mixed-state
argument.  Deleting `x_i y_i` adds `i_Li_R` to `M_F`.  If a fixed Hall
defect `S` is repaired by every diagonal, then every `i_R` lies in `S`
and every `i_L` lies outside `N(S)`.  Hence `S=R` and `N(S)=emptyset`,
which one added edge cannot repair for `n>=2`.  Equivalently, under the
stronger all-cross-edge hypothesis, Theorem 6.2's complement rectangle
would have to contain all diagonals, forcing `n=1`.

Proposition 6.5 correctly preserves the old mixed-type construction for
an abstract two-layer relation in which diagonal constraints have first
been removed.  It must not be cited as a nontrivial literal
edge-carrier case.

## 6. Sharp Hall-defect example and verifier audit

For `t=(0,0,0,1)`, adding

\[
 x_0y_3,\quad x_1y_3,\quad x_2y_3
\]

to the flat skeleton leaves `y_3` with no allowed carrier colour, because
the diagonal `x_3y_3` supplies the fourth forbidden pair.  The exact
branch-set search finds no `K_7` model, and the recorded five-colouring is
proper.  This example is static; it does not satisfy diagonal canonical
deletion, exactly as Theorem 6.4 predicts.

Executed checks:

* `near_k7_two_vertex_state_helly_verify.py`: all `896` mixed type/sign
  skeletons; exactly the `14` state-aligned coboundaries are target-free;
  direct validation of (5.3)--(5.4); exact Hall-example minor search and
  five-colouring.
* `near_k7_seven_view_state_counterarchitecture.py`: exact seven-view
  state sets, treewidth five, and pendant-pruned `K_7` search.
* `near_k7_icosahedron_retained_view_states.py`: connectivity seven,
  coherent two-apex deletion, and exact retained state sets.
* `near_k7_state_relation_verify.py`: `66,066` bipartite relations through
  order four for Theorem 6.2; all `57,344` mixed `n=4` full flat hosts,
  with zero nonperfect diagonal-canonical instances; and `784` abstract
  mixed rectangular branches for Proposition 6.5.

All scripts completed successfully under `.venv/bin/python`.

## Exact remaining gap

Minor-criticality gives an `(n+2)`-colouring after deleting a carrier
edge, but does not keep that colouring in the same switched two-layer
frame.  The verified theorem closes the cell **if** those deletion
colourings can be canonicalized.  The remaining step is therefore an
operation theorem: canonicalize a strategically chosen proper-minor
palette, or convert its failure into a labelled rerouting or coherent
two-apex adhesion.

