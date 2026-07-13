# Six-root triangle-free routing: audited state for `K_{2,4}` and `theta(2,2,3)`

## 1. Scope

This note concerns Kriesell--Mohr property `(*)`.  A target graph `K` has
property `(*)` when every properly coloured graph with one prescribed root in
each colour class and with a bichromatic root-to-root connection for every edge
of `K` contains a rooted `K`-minor.

The two targets here are the maximal triangle-free graphs on six vertices

* `K_{2,4}`; and
* the theta graph consisting of three paths of lengths `2,2,3` with common
  ends.

No complete proof of property `(*)` for either target is claimed below.

## 2. Minimal-witness normal form

Assume that `K` is either target and choose a counterexample `(G,C,T)`
minimising `|V(G)|+|E(G)|`.

1. For each edge `ij` of `K`, the graph on colour classes `C_i,C_j` consists
   of isolated vertices and one induced alternating path `P_ij` from root
   `t_i` to root `t_j`.  For a nonedge there are no edges between the two
   classes.  This follows by deleting every edge not needed by one selected
   root component and then deleting cycles/branches inside that component.
2. Every non-root vertex has degree at least four.  A non-root of degree two
   lies internally on just one path.  If its two neighbours are `y,z`, contract
   the three-vertex path `y-x-z` to one vertex of the opposite colour, apply
   minimality, and expand the unique bag containing the contraction vertex.
   Degrees are even because every occurrence internal to a bichromatic path
   contributes two incident edges.
3. Every proper subgraph of either target has property `(*)`:
   deleting an edge of the theta graph leaves a graph with at most one cycle;
   deleting an edge of `K_{2,4}` leaves a pendant vertex attached to a
   `K_{2,3}`, and both `K_{2,3}` and the pendant extension have property `(*)`.
   Consequently every selected path has at least four vertices.  Otherwise a
   direct edge between its two roots supplies the sole adjacency missing from
   the rooted model for `K-e`.
4. In particular every colour class has at least two vertices.

For `K_{2,4}`, write the hub roots as `a,b` and the other roots as
`x_1,...,x_n` (`n=4`).  The normal form has an additional useful feature:
every non-root vertex of the colour of `x_i` lies on both `P_{a i}` and
`P_{b i}`, because it has degree at least four and these are the only two
target edges incident with that colour.

## 3. A clean uniform root-shift lemma

The following is the rigorous part of the portal-permutation mechanism.

**Portal-permutation lemma.**  In a minimal path witness for `K_{2,n}`, let
`p_i` be the neighbour of `x_i` on `P_{a i}`.  Suppose there are

* pairwise distinct vertices `p_1,...,p_n`;
* a permutation `pi` of `[n]` with `pi(i) != i`; and
* for every `i`, the neighbour `u_i` of `p_i` towards `a` on `P_{a,pi(i)}`,

such that the prefix of `P_{a,pi(i)}` from `a` through `u_i` contains none of
the vertices `p_j`.  Then the witness has a rooted `K_{2,n}`-model.

**Proof.** Delete every `x_i` and every `p_i`.  Use `u_i` as the new root in
colour class `pi(i)`.  The permutation condition makes this a transversal.
The protected prefix gives an `a-u_i` bichromatic path after the deletion.
Since `u_i` is a non-root vertex in a degree-two leaf colour and has degree at
least four, it also lies on `P_{b,pi(i)}`; the `b-u_i` subpath avoids all
deleted vertices.  Thus the smaller graph is again a `K_{2,n}` routing
witness.  By minimality it has a rooted model.  Relabel its mutually symmetric
leaf bags by `i`, and add `p_i,x_i` to the bag containing `u_i`.  These added
two-edge tails are pairwise disjoint and restore the original roots.  This is
the required rooted model.  QED.

This lemma kills every globally matchable, portal-order-compatible state.  It
also identifies the exact structural residue: a counterexample must have a
Hall-deficient portal system, coincident first portals, or an interleaving of
the first portals on the relevant paths.  A merely local directed support
cycle is insufficient: deleting its portals can break unshifted paths, while
retaining them makes the lifting step invalid if a portal belongs to another
model bag.

The same proof is label-free in essence: it is a root-shift along an
automorphism of the routing target, protected by a globally compatible portal
permutation.

## 4. A complementary carrier--shore lemma

The Hall-deficient side has a second, completely constructive closure.

For the `K_{2,n}` notation above, let `p_i` and `q_i` be the neighbours of
`x_i` on `P_{a i}` and `P_{b i}`, respectively.  Let `L` be a nonempty proper
subset of `[n]` and put `M=[n]-L`.  Suppose

1. every `p_i` belongs to at least one path `P_{a l}` with `l in L`; and
2. for every `l in L`, the vertex `q_l` belongs to at least one path
   `P_{b m}` with `m in M`.

Then there is a rooted `K_{2,n}`-model.

Indeed, take

* the `a`-bag to be the union of `P_{a l}-{x_l}` over `l in L`;
* the `b`-bag to be the union of `P_{b m}-{x_m}` over `m in M`; and
* every leaf bag to be the singleton `{x_i}`.

The two hub bags are connected (their constituent paths share their hub
root), and they are disjoint because the first uses only the `a` colour and
leaf colours in `L`, while the second uses only the `b` colour and leaf
colours in `M`.  Hypothesis 1 makes the first hub bag adjacent to every leaf
root.  The second hub bag is adjacent to roots in `M` by the terminal edges
of its paths and to roots in `L` by hypothesis 2.

This includes a useful collision closure: if a single path `P_{a k}` contains
all first portals `p_i`, choose `L={k}`.  The second condition is automatic,
because `q_k` is a non-root vertex of degree at least four and hence lies on
`P_{b m}` for some `m != k`.

The carrier--shore lemma closes a large part of the Hall-deficient regime
without any rerouting.  The residue is now sharper: every carrier set on one
hub side is blocked by a first portal on the other side whose entire support
stays inside that carrier set.  This is an alternating closed-set, or portal
lock, condition rather than an arbitrary failure of matching.

## 5. Exact two-support cycle elimination

There is also a rigorous partial-shift theorem; the support-confinement
hypothesis is essential.

**Exact-support cycle lemma.**  In a minimal path witness for `K_{2,n}`, suppose
that, at the `a` hub,

* the first portals `p_i` are pairwise distinct; and
* each `p_i` lies on exactly two of the paths `P_{a j}`.

Then the witness has a rooted `K_{2,n}`-model.

**Proof.**  Besides its own path `P_{a i}`, let `P_{a f(i)}` be the unique
other path containing `p_i`.  Thus `f(i) != i`.  The functional digraph of
`f` contains a directed cycle `C`.  For `i in C`, let `u_i` be the neighbour
of `p_i` towards `a` on `P_{a f(i)}`.  Delete `x_i,p_i` for `i in C`; keep
the roots outside `C`, and in the colour class `f(i)` use `u_i` as the new
root.  Since `f` cyclically permutes `C`, this is a transversal.

Put `j=f(i)`.  Among deleted portals, the only ones that can occur on
`P_{a j}` are `p_i` and `p_j`: exact support excludes all others.  The former
comes immediately after `u_i` in the chosen direction, while `p_j` is the
unique neighbour of the old endpoint `x_j`, hence occurs after the distinct
vertex `p_i`.  Therefore the `a-u_i` prefix survives.  As before, `u_i` lies
on `P_{b j}`, so its `b-u_i` subpath survives.  If `j` is outside `C`, exact
support implies that neither `P_{a j}` nor `P_{b j}` uses any deleted portal
or root, so every unshifted leaf retains both routes.

The smaller graph is consequently another `K_{2,n}` routing witness.  Apply
minimality, cyclically relabel the leaf bags on `C`, and add the private tail
`u_i-p_i-x_i` to the bag labelled `i`.  This gives the forbidden rooted model.
QED.

Consequently, a minimal `K_{2,4}` obstruction must exhibit, at each hub side,
either coincident first portals or a first portal supported on at least three
hub--leaf paths.  The pure degree-four/distinct-portal state is eliminated in
all orders, not merely computationally.

There is a theta analogue for the two interchangeable short branches.  Label
the theta paths `a-c-b`, `a-d-b`, and `a-e-f-b`.  If the first `a`-side
portals `p_c,p_d` are distinct, `p_c` occurs only on the `a-c` and `a-d`
paths, and `p_d` occurs only on those same two paths, then swapping `c,d` is
the two-cycle in the proof above.  Delete `c,d,p_c,p_d`, use the predecessor
of `p_c` in colour `d` and the predecessor of `p_d` in colour `c`, apply
minimality, swap the two (automorphic) short-branch bags, and restore the two
private tails.  Thus this exact crossed-short-portal state cannot occur in a
minimal theta obstruction.

## 6. Exhaustive small-witness check

`trianglefree_six_property_search.py` now supports random or exhaustive
minimal alternating-path witnesses with arbitrary colour-class sizes.
`trianglefree_six_order14_verify.py` exhausts every automorphism orbit of
class-size vectors of total order at most fourteen that can occur after the
normal-form reductions above.

The verification enumerates every simple alternating root path for every
target edge, takes their union, and then exhaustively searches all rooted bags:
each non-root vertex is assigned to one of the six root bags or left unused;
connectivity, disjointness and every target adjacency are checked exactly.

Result:

> Neither target has a minimal path counterexample on at most fourteen
> vertices.

This extends falsification evidence but is not a proof in unbounded order.
The exhaustive orbit list and a replayable verifier are in the script; no
randomness is used by that verifier.

## 7. Exact remaining gap

To prove property `(*)` for `K_{2,4}`, it is enough to eliminate the
Hall-deficient/interleaved portal lock left jointly by the portal-permutation
and carrier--shore lemmas.
The desired structural statement is a portal Hall dichotomy:

> Either the first-portal incidence admits a protected global permutation, or
> the Hall-deficient shore can be split into two disjoint connected rooted
> pieces whose boundary contacts directly form the two hub bags.

For `theta(2,2,3)`, the equivalent formulation is a rooted `C_4` model on the
two length-two branches together with a reserved connector through the
two-root length-three ear.  A proof must preserve that connector; an arbitrary
rooted `C_4` certificate is not enough.

These two residues are the same uniform issue in different language:
converting a system of individually valid bichromatic paths into a globally
compatible rooted model when the first portals fail Hall matching.
