# Exact-seven singleton-propagation completion (superseded draft)

This draft is retained for history.  Its theorem was audited and then
subsumed by `results/hc7_exact7_forced_path_completion.md`, which also gives
the exact forcing certificate and five cut-switch types.

## 1. Statement

Let `F` be a triangle-free graph on a literal seven-vertex set `S`.  Give
each `s in S` a nonempty list

\[
                 \Lambda(s)\subsetneq\{1,2,3\},
\]

and suppose every palette colour has support at least four.  Form the
literal auxiliary graph `Q` by adjoining a triangle `c_1c_2c_3` and the
incidence edge `sc_q` exactly when `q in Lambda(s)`.

An **anchored `K_4`** in `Q` is a `K_4` model with four bags containing
four distinct literal vertices of `S`, one per bag.

### Theorem 1.1 (propagation-or-carrier completion)

If `(F,Lambda)` is uncolourable, then either

1. exhaustive singleton propagation reaches an empty list; or
2. `Q` contains an anchored `K_4`.

The statement is independent of the order of propagation in the following
safe sense: fix any exhaustive sequence of forced singleton assignments.  If
that sequence terminates without a conflict, outcome 2 holds.

## 2. Proof

Fix an exhaustive singleton-propagation sequence which terminates without a
conflict.  Every propagation step preserves colourability in both
directions, so the residual instance `(H,L)` is uncolourable.  It has no
singleton and no full list: propagation only deletes colours and every raw
list had order at most two.  Thus every residual list is an exact pair.

Apply the audited triangle-free seven-boundary critical-core classification.
After deleting residual vertices and edges and enlarging lists, `(H,L)`
contains one of `T1`--`T10`.  At every displayed pair-list vertex the raw
list was that same exact pair.  Indeed,

\[
 \text{displayed pair}\supseteq\text{residual pair}
 =\text{raw pair},
\]

and both ends have order two.  At a displayed full-list vertex the raw list
is one of the three pairs.

We now use exactly the support calculation from the audited pair-bicycle
completion.

* `T1` uses five vertices, all with one common pair.  The omitted palette
  colour can occur on at most the two vertices outside the core, contradicting
  support at least four.
* `T3` uses all seven vertices with one common pair, so the omitted colour has
  support zero.
* `T7,T8,T9` use all seven vertices.  Replacing their displayed full lists by
  arbitrary raw pairs still leaves some palette colour with support at most
  three.
* In `T2,T4,T5,T6`, and in each of the three pair refinements of `T10`, the
  explicit four bags in the pair-bicycle completion form an anchored `K_4`.

These cases are exhaustive.  Every boundary edge used by those bags is a
retained edge of the original `F`, and every carrier incidence used at a
pair-list vertex is an exact raw incidence.  Restoring deleted vertices,
edges, and unused incidences cannot destroy the model.  Hence the anchored
`K_4` occurs in the original auxiliary graph `Q`.  This proves the theorem.
`square`

## 3. Literal `HC_7` consequence

Retain the exact-seven `(1,3)` separation with three disjoint `S`-full
packets on the opposite shore, and let three connected pairwise adjacent
carriers span the thin shore.  Their raw contact lists are `Lambda`.

An anchored `K_4` in `Q` lifts by replacing each `c_q` with its literal
carrier.  Anchor the three full packets at the other three vertices of `S`.
Packet fullness supplies the twelve mixed and three packet--packet
adjacencies, while the anchored model supplies the six carrier--carrier
adjacencies.  The result is a literal `K_7` model.

Consequently, in a hypothetical counterexample, every uncolourable raw
carrier state with no full list and support at least four must reach an
empty list under singleton propagation.  Together with the audited
full-list completion, this applies to every canonical crossed block-chain
state.

## 4. Exact remaining interface

A propagation conflict has a finite literal implication certificate.  Each
newly forced pair-list vertex records an adjacent previously forced vertex
which deleted its alternative colour.  At the conflict, tracing these
predecessors gives two forced implication chains ending in incompatible
assignments (the chains may meet or close into a bicycle).  The next
block-chain theorem must transport or break this certificate when a
cutvertex is moved between the two outer carriers.

The theorem does **not** claim that the raw state already has an edge whose
endpoints carry the same singleton.  That stronger shortcut is false: the
three-vertex path with lists `{1},{1,2},{2}` is already a forced conflict
without such an edge.
