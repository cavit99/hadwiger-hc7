# Independent audit: concentrated missing-colour rotation normal form

**Audited source:** `hc7_concentrated_rotation_normalization.md`
**Frozen proof SHA-256:**
`ec3b95124205b01f02c804f123dd07d31102ce63eb62c845254654e2985bf9d5`
**Promoted theorem SHA-256:**
`c60dd0c95f38bb39cf6922987861be83c66e6f85dc9cbf7a452df307d2eef37f`
**Verdict:** **GREEN.**

The promoted theorem differs from the frozen audited proof only in its
status line.  The statement and proof are unchanged.

The normalization identity, the inactive-component separation, and the
fixed-object invariance claims are correct.  The hypothesis in Corollary 3.1
must remain orbit-wide: checking the initial colouring alone would not
control support components after a genuinely nontrivial normalized
transition.  The source states the required orbit-wide hypothesis.

## 1. Exact normalization identity

Let `K_beta` be the unique pole-support component.  The direct transition
interchanges `alpha,beta` on `K_beta`; the subsequent global renaming makes
the same interchange on every vertex in the two colour classes.  Hence the
two operations cancel on `K_beta` and act once on every other
`alpha`--`beta` component.  Vertices of the other four colours are unchanged.
This is exactly the identity asserted in Theorem 2.1.

No pole neighbour can lie in an inactive component.  There are no
`alpha`-coloured pole neighbours by the buffer-colour hypothesis.  Every
`beta`-coloured pole neighbour lies in `K_beta` because concentrated support
means that `K_beta` is the only two-colour component containing a neighbour
of either pole.  Pole neighbours in the other four colours are outside the
two-colour subgraph.  Thus every pole neighbour keeps both its vertex and its
original colour after normalization.

If there is an inactive component, each of its vertices changes colour under
normalization.  Conversely, if there is no inactive component, `K_beta` is
the entire induced two-colour subgraph.  This verifies the stated
fixed-point criterion.

## 2. Inactive-component separator

For an inactive component `L`, inactivity excludes edges from `L` to either
pole.  Component maximality in the induced `alpha`--`beta` subgraph excludes
edges from `L` to an `alpha`- or `beta`-coloured vertex outside `L`.
Consequently

\[
   N_G(L)=N_H(L),
\]

and every vertex of this open neighbourhood has one of the other four
colours.  Deleting it separates the nonempty set `L` from the component
containing the adjacent poles `z,u`.  It is therefore an actual vertex
separator, not merely a relative separator.  Seven-connectivity gives
`|N_H(L)| >= 7`; equality gives an actual order-seven separation with both
open sides nonempty.

The boundary being four-coloured means "using colours from a specified set
of four"; it need not use all four.  As the source correctly warns, neither
an upper bound on the separator order nor compatible colourings of both
closed sides follows.

## 3. Orbit statement and its quantifiers

A direct missing-colour transition is reversible.  After the swap, the same
component is the unique support component for the reverse pair, so repeated
direct transitions define a legitimate orbit.

If, at every colouring reached in that orbit, every available concentrated
transition has its support component equal to the full induced two-colour
subgraph, then that transition is literally a global transposition of the
two colour names.  Induction on the transition sequence shows that every
orbit colouring is only a global relabelling of the original six colour
classes.  This proves Corollary 3.1.

The orbit-wide quantifier is essential.  A nontrivial normalized transition
swaps the colours on inactive components and can change later two-colour
component structure, so an initial-colouring-only version is unjustified.

Two wording points do not affect the theorem but should be read narrowly:

1. the "five possible moves" are five candidate missing-colour exchanges;
   a candidate is an available *direct* transition only when its support is
   concentrated; and
2. the sentence that star transpositions generate all permutations is the
   abstract group-theoretic fact.  Unless all five candidate transitions are
   available at every required stage, it must not be read as saying that the
   actual orbit contains every global permutation.  The proved and used
   conclusion is only that the actual orbit is contained in the set of
   global relabellings.

Diffuse support is already a separator outcome of the preceding audited
bichromatic-support theorem; it is not a missing third kind of direct
rotation.  Thus the final two-way fork is valid for the concentrated
rotation part of the argument, after the diffuse alternative has been
handled.

## 4. Fixed model, selected endpoints, and paths

Normalization changes only colour labels on inactive components.  It does
not change the graph, the six fixed branch sets, pole--branch-set
adjacencies, selected vertices, or the fixed paths.  By Section 1, the
selected pole-neighbours also retain their colours.  Therefore the number
of common-contact branch sets, the total contacted branch sets, every fixed
path's branch-set interval sequence, and every fixed path length are all
unchanged.

This verifies the precise negative conclusion: rotation alone cannot
strictly improve the displayed joint score.  A later improvement must make
an additional model or path choice.  The theorem does not say that such a
regeneration is impossible.

## 5. Guardrail scope

The complete-join planar family is used only to show that separator and
fixed-pair outcomes are structurally necessary.  It is not asserted to be a
seven-chromatic counterexample.  The repository's audited
`K_2`-plus-planar construction realizes the relevant static setup, including
an eligible adjacent pair, concentrated support with an inactive component,
and an order-seven separator, while remaining six-colourable.  This is
consistent with, and does not strengthen, the theorem under audit.

## 6. Trust boundary

This audit promotes only the colouring identity and its separator/invariance
consequences.  It does not promote any of the following:

- a colour-compatible gluing across `N_H(L)`;
- an order bound above the equality case;
- a rooted or label-preserving `K_6`-model regeneration theorem; or
- a Kempe-colouring of order six.

In particular, the star of two-colour connections from the current missing
colour does not imply connectivity of every pair of nonbuffer colour
classes.
