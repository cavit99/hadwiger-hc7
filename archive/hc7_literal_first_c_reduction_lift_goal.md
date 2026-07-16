# Active goal: literal first `C`-reduction lift

**Status:** geometric portion discharged; state composition transferred to
the twin-seam exchange goal.

## Strategic decision

Keep the atomic four-root decoder as the current `HC_7` milestone.  The
literal gate analysis proposed here has now been completed through the
audited two-gate and three-gate normal forms.  Its only nonterminal geometric
output is the symmetric twin seam.  The active successor is
[the double-lock exchange](hc7_atomic_twin_seam_double_lock_exchange_goal.md).

This choice follows two audited advances.

1. The asymmetric `(5,6)` carrier theorem closes every connected split in
   which the side away from the compulsory root meets five boundary labels
   and the root side meets six.  It eliminates the whole outerplanar rural
   family.
2. A removable nonroot vertex of degree at most three either closes by that
   theorem or exposes an actual order-seven boundary with a named
   contraction attaining a one-sided exact state.

Thus the first genuinely unbounded rural obstruction is a minimum-degree-
four interior torso or a literal lobe behind a two- or three-vertex gate.
The new goal is to lift that gate before any clique-completion edge is used.

Proving the goal closes the remaining rural child of the atomic decoder.
It does not close the separate symmetric `(5,5)` linkage child, and it does
not by itself prove `HC_7`.

## Frozen input

Use the full connected-bipartite atomic separation

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad S=W\mathbin{\dot\cup}\{u\},\qquad |S|=7,
\]

with the following audited data.

1. `G` is seven-connected, strongly seven-contraction-critical,
   `K_7`-minor-free, and not six-colourable.
2. There is no `A-R` edge; `R` contains two disjoint adjacent connected
   `S`-full packets.
3. `zu` is the unique `A-u` edge; `A-z` is connected and `W`-full.
4. `H=G[S]` is connected and bipartite.
5. `A` is two-connected.  Every clean normalized-core edge, every bare
   cycle shore, and every nonroot degree-at-most-two vertex is closed.
6. The four-root rural branch has reached the direct-reserve cell.  After
   one legal root substitution, the literal host is a clean disk with
   roots `z,x,y,r` on one distinguished face.  One nontrivial boundary path
   repairs the rooted diamond and the direct edge `xy` remains reserved.

Let

\[
                         O=W-\{x,y,r\}.
\]

Retain every literal `O-A` portal edge, the edge `uz`, and the fully crossed
normalized path/subdivided-`Y` core.  Completion edges in a web or a
`C`-reduction are not host edges.

The audited entry results are:

* [asymmetric `(5,6)` closure](../results/hc7_atomic_asymmetric_56_carrier_closure.md)
  and [audit](../results/hc7_atomic_asymmetric_56_carrier_closure_audit.md);
* [degree-three receiver peel](../results/hc7_atomic_degree_three_receiver_peel.md)
  and [audit](../results/hc7_atomic_degree_three_receiver_peel_audit.md).

The latter gives only a one-sided receiver state.  It does not prove a
packet vector, reflection, or a well-founded recursive descent.

## Literal reduction object

Use the classical Two Paths theorem in `C`-reduction form.  An elementary
reduction removes a lobe `D` separated from the distinguished frame by a
literal gate

\[
                              Z=N_A(D),\qquad |Z|\le3,
\]

and completes `Z` to a clique in the reduced graph.  Choose the first such
reduction after exposing all literal two- and three-separations of the
clean disk.  When a canonical lobe is needed, take the complement of the
frame-containing component of `A-Z`; equivalently, saturate the off-frame
side.  An inclusion-minimal off-frame lobe is **not** equivalent: its
complement need not be connected, so it cannot be used silently as the
second carrier.

The separation is literal; the clique completion is not.  Relative
seven-connectivity gives

\[
                         |Z|+|N_S(D)|\ge7.                 \tag{1}
\]

Equality in (1) is an actual seven-boundary, but carries no state unless a
named proper-minor operation and an intact-side restriction are supplied.

## Target theorem

### Literal first `C`-reduction lift theorem

Under the frozen input, the first lobe `D` and gate `Z` yield at least one
of the following literal outcomes.

1. **Asymmetric carrier closure.**  There is a partition
   `A=X dotunion Y` into nonempty connected adjacent sets, with `z` on the
   six-contact side and support profile at least `(5,6)`.  The audited
   adaptive return six-colours `G`.
2. **Rooted-five closure.**  The lobe, a literal jump/cross, the normalized
   core and the omitted portals give five pairwise disjoint connected
   pairwise adjacent bags in `G[A union S]`, each containing a different
   literal member of `S`.  The two rich packets complete a literal `K_7`.
3. **Normalized exact receiver.**  Equality holds in (1),

   \[
       \Omega=Z\cup N_S(D)=N_G(D),\qquad |\Omega|=7,
   \]

   and the proof supplies all of:

   * a specified proper-minor deletion or contraction on the opposite
     closed shore;
   * the exact labelled state induced on the intact `D union Omega` shore;
   * the literal old-to-new boundary map;
   * the actual packet vector of the new separation; and
   * either a strictly smaller oriented `(1,2)` receiver or a named `(1,1)`
     handoff accepted by `S4`.

A naked gate, a one-sided state without its packet orientation, a changed
unlabelled partition, or a clique-completion edge is not an outcome.

## Proof programme

### 1. Peel before completing

Expose literal two- and three-separations before passing to any torso.  A
nonroot removable vertex of degree at most three is handled by the audited
peel.  Its exceptional boundary is only an entry certificate; prove the
packet orientation and receiver data required by outcome 3 before
recursing.

### 2. Isolate one literal plane torso

Only after every earlier lobe is discharged may a 3-connected plane torso
be used.  On that torso choose a facial/Tutte path through the prescribed
frame edge.  Its nontrivial bridges have at most three attachments; outer
bridges have at most two.  Apply (1) to the *literal bridge interior*.

A bridge spanning two core segments is a candidate literal jump.  Decode
it immediately into outcome 1 or 2.  If every bridge is confined, take the
first confined bridge and lift its gate into outcome 3.

### 3. Use planar deficiency only after its hypotheses hold

If all omitted-label extensions remain facial, triangulate the literal
torso and use the DeVos--Seymour/Kawarabayashi--Norine--Thomas--Wollan
quilt calculation.  Low internal degree must be charged to actual portals
in `O`; repeated compensation by the same three labels must yield a jump,
two duty carriers, or the exact receiver.  Minimum degree seven in `G`
alone is not a quilt-deficiency hypothesis.

### 4. Keep every return literal

Every asserted adjacency must be an original edge, a path inside one
branch set, or a named contraction.  Every nonterminal move must decrease
the active-shore order together with a declared receiver orientation.  A
root exchange that merely reverses the previous move falsifies the proposed
induction.

## Literature decision from online research, 15 July 2026

No primary source supplies the lift theorem outright.

* The classical Two Paths theorem says that absence of a `C`-cross is
  equivalent to planarity after a sequence of order-at-most-three
  `C`-reductions.  It adds clique edges at the gates; those edges are the
  exact nonliteral lift gap.  See
  [Kawarabayashi--Thomas--Wollan, Theorem 1.3](https://arxiv.org/abs/1207.6927)
  and the modern constructive treatment of
  [Humeau--Pous](https://arxiv.org/abs/2505.16431).
* Tutte-path theory bounds bridge attachments by three, and outer bridge
  attachments by two, but does not attach the seven literal labels or an
  equality state.  See
  [Biedl--Kindermann](https://arxiv.org/abs/1812.04543) and
  [Wigal--Yu](https://doi.org/10.1016/j.jctb.2022.07.006).
* The planar quilt bound requires internal degree at least six, while the
  KNTW extension assumes bounded total deficiency.  The three omitted
  labels may compensate arbitrarily many lower-degree vertices here.  See
  [DeVos--Seymour](https://www.sfu.ca/~mdevos/papers/3color.pdf) and
  [KNTW](https://arxiv.org/abs/1203.2171).
* Stable-bridge, nonplanar-extension and rooted-subdivision theorems need
  genuine 3-/almost-4-connectivity and other terminal hypotheses not
  implied by relative seven-connectivity.  See
  [Norin--Thomas](https://arxiv.org/abs/1402.1999) and
  [Hayashi--Kawarabayashi--Yoo](https://doi.org/10.1137/23M157082X).

The 2023 correction to the KTW flat-wall framework is a further reason not
to import flatness conclusions beyond the classical `C`-reduction theorem:
[Arnon](https://arxiv.org/abs/2304.02701).

## Falsification boundary

Reject each of the following moves.

* `delta(G)>=7` does not imply internal degree six or bounded quilt
  deficiency in the planar torso.
* Relative seven-connectivity of the whole graph does not make `A`
  3-connected or almost 4-connected.
* A completed gate edge is not literal.
* Equality in (1) supplies no state by itself.
* The degree-three peel supplies only a one-sided state and a local order
  decrease; it is not yet a recursive handoff.
* A Tutte path or stable bridge without five labelled bags is not a rooted
  model.

## Success condition

Success is a complete proof of all three outcomes, followed by an
independent audit of every gate, contraction, packet vector, carrier
support, rooted-bag adjacency and strict receiver rank.  A planar torso,
another list of portal orders, or a naked exact-seven cut is not success.
