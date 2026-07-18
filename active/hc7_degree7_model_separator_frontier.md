# Degree-seven boundary-labelled near-clique composition

**Status:** active conjectural target.  The input theorems in Sections 1--4
are separately audited.  Section 5 is open.  Nothing here proves `HC_7`.

## 1. The degree-seven interface is a single connected exterior

Let `G` be a hypothetical minor-minimal counterexample to `HC_7`, and let
`u` have degree seven.  Put

\[
 S=N(u),\qquad H=G[S],\qquad F=\overline H.
\]

The anti-neighbourhood is one nonempty connected graph

\[
                         C=G-N[u].                     \tag{1.1}
\]

Thus the two closed sides of the order-seven separation at `S` are

\[
                 A=G-u=G[C\cup S],\qquad B=G[N[u]].    \tag{1.2}
\]

## 2. Exact boundary languages and one-colouring path systems

Dirac's inequality gives `alpha(H)<=2`, so a boundary equality partition
is encoded by a matching of `F`: its matching edges are the two-vertex
colour classes.  The two extension languages are exactly

\[
 \begin{aligned}
  \mathcal M(A)&=\{\{e\}:e\in E(F)\},\\
  \mathcal M(B)&=\{M:M\text{ is a matching of }F, |M|\ge2\}.
 \end{aligned}                                         \tag{2.1}
\]

Fix a nonedge `e_0=ab` of `H` and a six-colouring of `A` whose sole
repeated boundary pair is `ab`.  The five vertices

\[
                         U=S-\{a,b\}
\]

have five distinct colours.  Every edge of `F[U]` is realized by a
bichromatic path through `C` in this one fixed colouring, and paths for
vertex-disjoint edges of `F[U]` are vertex-disjoint.  Since `F[U]` is
triangle-free, it has at most six edges.  Kriesell--Mohr's Theorem 7,
applied after restricting to the five colour classes meeting `U`, packages
these paths into a `U`-rooted `K_5` model in `A-{a,b}`.

This is the required common-colouring provenance.  It is stronger than an
existential collection of paths obtained from unrelated edge deletions.

## 3. The model-carried obstruction

For every `ab in E(F)`, either `G` already has a `K_7` minor or the union
of the five rooted branch sets contains an inclusion-minimal `a-b`
separator `Z` of `A` with

\[
                              |Z|\ge6.                  \tag{3.1}
\]

The components containing `a` and `b` are each adjacent to every vertex
of `Z`, and some rooted branch set contains at least two vertices of `Z`.
The set `Z union {u}` is therefore an actual full separation boundary in
`G`.

More sharply, for each `ab` one obtains one of:

1. an explicit `K_7`-minor model;
2. a full order-seven separation `Q union {u}`, where `|Q|=6`; or
3. seven internally vertex-disjoint `a-b` paths, all meeting the union of
   the five named rooted branch sets.

The third alternative forces at least one branch set to meet two of the
paths.  Connectivity and rooted-model data alone do not split that branch
set: complete multipartite examples and `overline(K_2) join` planar
examples show that the proper-minor colouring response is indispensable.

## 4. Uniform boundary-labelled near-`K_7` model

The boundary complement and rooted models now give a stronger normal form.
There are seven disjoint connected branch sets, including `{u}` and a
singleton boundary vertex `{c}`, with every adjacency present except one or
two pairs incident with `{c}`.  Thus every degree-seven survivor has a
boundary-labelled model of `K_7^-` or of `K_7` with two adjacent edges
deleted.

This eliminates the earlier boundary-by-boundary split.  The nonisolated
part of `F` is one two-connected component on six or seven vertices.  A
degree-two complement vertex gives the one-missing-edge model directly; if
there is no such vertex, then

\[
                 F\cong K_{3,4}
        \quad\hbox{or}\quad
                 F\cong K_{3,3}\mathbin{\dot\cup}K_1,
\]

and explicit rooted bags give the two-adjacent-edge model.

## 5. Primary open theorem

### Boundary-labelled centre-repair theorem

For the aligned one-/two-missing-edge model in Section 4, use the exact
matching-language transition and literal first hits in the five named bags
to obtain at least one of:

1. an explicit `K_7`-minor model in `G`;
2. vertices `p,q` such that `G-{p,q}` has no `K_5` minor; or
3. one equality partition on an actual order-seven boundary induced by
   six-colourings of both closed sides.

Outcome 2 is terminal: the established `t=5` case makes `G-{p,q}`
four-colourable, and two fresh colours extend to `p,q`.  Outcome 3 is also
terminal after a permutation of colour names and gluing.

The model is not an arbitrary `K_7`-minus-two-edges minor.  Its deficient
centre is a literal boundary singleton, its other bags contain specified
boundary roots, and it comes from a six-colouring with one prescribed
repeated boundary pair.  These labels must be retained.

If a clean path from the centre to every deficient bag exists outside the
other five branch sets, absorption gives the missing adjacencies.  Failure
returns the model-carried separator of Section 3.  A proper-minor operation
on an internal edge then induces a boundary matching of size two or three
and locks the edge endpoints in all five bichromatic colour graphs.  The
proof must convert one such palette-labelled bypass into a first hit in a
prescribed deficient bag, or transfer the resulting equality partition to
the actual separator.

Matching data alone cannot select the required bag: on a seven-cycle the
legal size-three matchings admit a cyclic static rebasing.  Consequently a
valid proof must use the literal operation endpoints, first-hit bag labels,
or the full neighbourhood of a failed bypass.  Merely regenerating another
near-clique model is not a decrease.

## 6. Immediate milestone

First prove the theorem for the one-missing-edge model.  Normalize the five
protected bags and choose the centre-to-deficient-bag obstruction
extremally.  If the obstruction is carried by a separator, use the
seven-path linkage and select either a triple-hit bag or two double-hit
bags.  Apply the proper-minor colouring to an internal first-entry edge.  A
successful proof must track:

- the two endpoints of that edge;
- the matching of `F` returned by the proper-minor colouring;
- the first literal contacts with all five named branch sets; and
- the complete neighbourhood of any connected component exposed by a
  failed rerouting.

Then treat the two-missing-edge models from the two exceptional complement
graphs.  Both missing pairs share the same singleton centre, so a connected
centre fan repairing both is sufficient; two unrelated pairwise paths are
not.

The standard seven-connected counterexamples fail exactly (2.1): they have
a common boundary partition or noncritical internal edges.  They therefore
guard the proof against dropping the matching-language hypothesis, but do
not refute this target.

## Dependencies

- [connected degree-seven anti-neighbourhood](../results/hc7_degree7_anti_neighbourhood_connectivity.md)
- [exact matching languages and simultaneous Kempe paths](../results/hc7_degree7_matching_bridge_bundle.md)
- [boundary-labelled one-/two-edge-deficient `K_7` model](../results/hc7_degree7_aligned_near_k7_model.md)
- [rooted `K_5`: reserved connector or full separator](../results/hc7_exact7_rooted_k5_connector_separator.md)
- [exact-block bounded-interface reduction](../results/hc7_bounded_interface_exact_block_kempe_reduction.md)
