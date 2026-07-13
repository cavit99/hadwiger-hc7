# Two missing cliques: exact boundary polarities and the synchronized Kempe lock

## Status

This note analyzes the sharp nonrural missing graph

\[
                  F=K_X\mathbin{\dot\cup}K_Y
                         \mathbin{\dot\cup}K_{\{r\}},
                  \qquad |X|=|Y|=3,                            \tag{0.1}
\]

from `hadwiger_two_shore_missing_graph_characterization.md`.  Thus the
boundary graph is `K_1 vee K_{3,3}`: `X` and `Y` are independent,
all `X`--`Y` edges are present, and `r` is universal.

The results are uniform in the labels inside `X,Y`.

1. The 24 exact six-colour states are classified without enumeration.
2. Every inclusion-minimal pair of disjoint full-shore private-block
   polarities is classified as a pair of edge-minimal covers in one
   five-by-five state graph.
3. Two such polarities always have a common coordinate which is unique on
   both sides.  The corresponding proper-minor witnesses force a
   synchronized Kempe carrier on the opposite triangle.

The last conclusion is a genuine graph-theoretic transition, but it is
not yet a `K_7` model: the two Kempe carriers live in different closed
sides and share their three boundary roots.  Turning the double page into
protected disjoint columns is the remaining step.

## 1. The complete state space

For a three-set `Z`, write

* `O_Z` for the one-block partition `{Z}`;
* `P_Z^z` for the two-block partition
  `{Z-{z},{z}}`, for `z in Z`; and
* `D_Z` for the discrete three-block partition.

Put

\[
              mathcal T_Z=\{O_Z\}\cup
                  \{P_Z^z:z\in Z\}\cup\{D_Z\}.                 \tag{1.1}
\]

### Proposition 1.1 (24-state classification)

Up to palette permutation, every proper six-colour equality state on the
boundary is a pair

\[
                         (pi_X,pi_Y)\in
                         mathcal T_X\times mathcal T_Y,          \tag{1.2}
\]

together with the singleton block `{r}`, except that
`(D_X,D_Y)` is forbidden.  Hence there are `5*5-1=24` labelled states.

#### Proof

Every colour block lies wholly in `X`, wholly in `Y`, or is `{r}`:
all cross-edges and all edges incident with `r` are present.  Conversely,
every pair of partitions of `X,Y` is proper on the boundary.  The number
of blocks is

\[
                         |pi_X|+|pi_Y|+1.                        \tag{1.3}
\]

It exceeds six only when both three-set partitions are discrete.  This
proves the assertion.  \(\square\)

Contracting a full shore alone produces a boundary state with at most
five blocks, because the contracted universal image uses a sixth colour
absent from the boundary.  In (1.2), this is the inequality

\[
                         |pi_X|+|pi_Y|\le4.                      \tag{1.4}
\]

## 2. Private blocks are a required-vertex edge cover

Make a bipartite **state graph** `Sigma` with parts `mathcal T_X` and
`mathcal T_Y`; its edges are all pairs except `D_XD_Y`.  Thus edges of
`Sigma` are exactly the 24 states.

Call

\[
 mathcal R_Z=mathcal T_Z-\{D_Z\}
     =\{O_Z\}\cup\{P_Z^z:z\in Z\}                              \tag{2.1}
\]

the four required coordinate types.

### Lemma 2.1 (private completeness)

A state family `mathcal E subseteq E(Sigma)` contains a private-block
witness for every nonempty independent boundary set contained in `X` or
in `Y` if and only if every vertex of

\[
                         mathcal R_X\cup mathcal R_Y             \tag{2.2}
\]

is incident with an edge of `mathcal E`.

Moreover any such family automatically contains a state satisfying
(1.4), so the shore-alone contraction imposes no additional abstract
condition.

#### Proof

For `Z=X` or `Y`, the whole three-set is an exact block precisely in
coordinate `O_Z`.  A two-set `Z-{z}` is an exact block precisely in
coordinate `P_Z^z`.  The same coordinate also has `{z}` as its singleton
block.  As `z` ranges over `Z`, these three pair partitions witness all
three singleton blocks.  Thus the four required coordinate vertices are
equivalent to all seven nonempty private-block demands.

Finally, covering `O_X` supplies a state `(O_X,pi_Y)`.  Its boundary has
at most

\[
                           1+3+1=5
\]

blocks, proving the last assertion.  \(\square\)

### Theorem 2.2 (all inclusion-minimal polarities)

A family `mathcal E` is inclusion-minimal subject to Lemma 2.1 if and
only if

1. it covers all eight required vertices in (2.2); and
2. every selected state edge has at least one endpoint which is a
   required vertex of degree one in `mathcal E`.

Consequently a pair `(mathcal E_A,mathcal E_B)` is an
inclusion-minimal disjoint full-shore polarity exactly when the two edge
sets are disjoint and each satisfies conditions 1--2.

Every such family has between four and eight states.

#### Proof

Deleting an edge preserves the required-vertex cover exactly when both
of its required endpoints, if any, still have another incident edge.
Thus an edge is indispensable precisely when at least one of its required
endpoints has degree one.  This proves the equivalence.

One state covers at most two required vertices, so at least four states
are needed.  Assign to every selected edge one of its degree-one required
endpoints.  Distinct edges receive distinct endpoints, because a
degree-one vertex lies on only one edge.  There are eight required
vertices, giving the upper bound eight.  \(\square\)

This characterization includes states with one discrete coordinate; it
does not silently restrict to the simpler four-by-four non-discrete core.

## 3. A common private coordinate is unavoidable

For a minimal family `mathcal E`, let `L(mathcal E)` be its required
vertices of degree one.

### Lemma 3.1 (common-leaf synchronization)

If `mathcal E_A,mathcal E_B` are disjoint minimal polarities, then

\[
                 L(mathcal E_A)\cap L(mathcal E_B)\ne emptyset. \tag{3.1}
\]

Thus, after possibly interchanging `X,Y`, there is a required coordinate
`pi_X in mathcal R_X` and distinct coordinates `sigma_A,sigma_B` such
that

\[
 \begin{aligned}
  \{sigma:(pi_X,sigma)in mathcal E_A\}&=\{sigma_A\},\\
  \{sigma:(pi_X,sigma)in mathcal E_B\}&=\{sigma_B\}.
 \end{aligned}                                                  \tag{3.2}
\]

#### Proof

The injection in the proof of Theorem 2.2 gives

\[
                         |L(mathcal E)|\ge|mathcal E|.          \tag{3.3}
\]

If a minimal family has four edges, those edges must cover all eight
required vertices twice endpoint-by-endpoint: no edge can waste an
endpoint on a discrete coordinate.  Hence every required vertex has
degree one and `|L(mathcal E)|=8`.

If either family has four edges, (3.1) follows immediately.  Otherwise
both have at least five edges, and (3.3) plus inclusion-exclusion in the
eight-element set of required vertices gives an intersection of order at
least two.  This proves (3.1).

At a common leaf, each family has exactly one incident state.  The two
opposite endpoints are distinct because the state families are disjoint,
giving (3.2).  \(\square\)

## 4. The singleton-fibre Kempe theorem

The following lemma is independent of criticality and of the sizes of the
two open shores.

### Theorem 4.1 (one coordinate forces a Kempe carrier)

Let `K` be a graph containing the boundary `K_1 vee K_{3,3}`, and let
`c` be a proper six-colouring of `K`.  Fix the equality coordinate on
`X`, and suppose that among all colourings of `K` with that same
`X`-coordinate, the `Y`-coordinate has only one possible value `sigma`.
Then:

1. If `sigma=O_Y`, write `alpha` for the common colour on `Y`.  For
   every colour `beta` absent from the boundary, all three vertices of
   `Y` lie in one `{alpha,beta}`-component.
2. If `sigma=P_Y^y`, write `alpha` for the colour on `Y-{y}` and
   `beta` for the colour on `y`.  All three vertices of `Y` lie in one
   `{alpha,beta}`-component.
3. If `sigma=D_Y`, then every two vertices of `Y` lie in one component
   induced by their two colours.

Every component asserted above avoids `X union {r}`.

#### Proof

All colours used on `Y` are absent from `X union {r}`, because every
`X`--`Y` edge and every edge from `r` to the boundary is present.

Suppose first that `sigma=O_Y`.  At most five colours occur on the
boundary, even if the fixed `X`-coordinate is discrete, so a colour
`beta` absent from the boundary exists.  If the three `Y` vertices do not
lie in one `{alpha,beta}`-component, switch one component meeting a
nonempty proper subset of `Y`.  The switched subset has colour `beta`
and its complement colour `alpha`; since `Y` has order three, the new
coordinate is one of the `P_Y^y`.  The switch does not affect `X` or
`r`, contradicting uniqueness of `sigma`.

Now let `sigma=P_Y^y`.  Consider the `{alpha,beta}`-component containing
the singleton `y`.  If it contains no member of `Y-{y}`, switching it
makes all of `Y` monochromatic.  If it contains exactly one member of
`Y-{y}`, switching it produces a different pair partition.  Either
outcome contradicts uniqueness.  Hence it contains all three roots.

Finally let `sigma=D_Y`, and take two roots having colours
`alpha,beta`.  If they lie in different `{alpha,beta}`-components,
switch the component containing one of them.  Those two roots then share
a colour while the third retains its different colour, producing a pair
partition and again preserving the `X`-coordinate.  This proves item 3.

The asserted components use only colours absent from `X union {r}`, so
they avoid those boundary vertices.  \(\square\)

### Corollary 4.2 (synchronized double-page lock)

Assume the two closed-side extension families themselves form an
inclusion-minimal disjoint polarity.  Choose the common coordinate from
Lemma 3.1.  The full-shore contraction which creates its corresponding
private block selects the unique state on each side.  In the two witness
colourings, Theorem 4.1 produces a Kempe carrier on the opposite triangle
on both sides (or the pairwise family in the discrete case).  The two
carrier interiors lie in opposite open sides and are disjoint; their only
common vertices are their named boundary roots.

#### Proof

The private-block contraction theorem gives a state incident with the
chosen required coordinate on each side.  Equation (3.2) makes that state
unique.  Apply Theorem 4.1 separately to the two closed-side colourings.
The separation ensures that interiors belonging to opposite open sides
are disjoint.  \(\square\)

This is the first synchronized graph object forced by the abstract
polarity: two rooted Kempe pages, not merely two equality partitions.

## 5. Exact one-step novelty and the remaining gap

Let the two closed-side extension families be `mathcal E_A,mathcal E_B`.
For every vertex deletion, edge deletion, or edge contraction wholly
inside the open `A`-side, a six-colouring of the resulting proper minor
induces a state

\[
                         pi_mu in mathcal E_B
                             \setminus mathcal E_A,              \tag{5.1}
\]

which extends the operated `A`-side.  For an edge deletion the operated
ends have one colour, see every other colour, and lie in a common
bichromatic component for every other colour.  The symmetric assertion
holds on the `B`-side.

Equation (5.1) is immediate from minor-criticality: membership in the
unchanged opposite family comes from restriction, while membership in the
original operated-side family would colour-glue the unmodified graph.

What is not yet proved is that an internal operation can be chosen whose
state has the synchronized coordinate of Lemma 3.1.  Without that
alignment, its saturated equal-endpoint Kempe components need not attach
to the two pages in Corollary 4.2.  This is the exact remaining exchange:

> **Synchronized-operation lemma.**  In the two-triangle exact-cut cell,
> some internal one-step operation realizes an opposite-side state at a
> common private coordinate, or the two locked Kempe pages have four
> protected disjoint columns.

The first outcome would align the equal-endpoint saturation with the
boundary carrier; the second enters the audited rooted-page completion.
No graph-realizable seven-connected counterarchitecture to this statement
is presently established.

## 6. Audit boundary

Corollary 4.2 assumes that the **actual** extension families are
inclusion-minimal polarities.  Choosing inclusion-minimal subfamilies of
larger extension families does not justify uniqueness of a coordinate
fibre, because omitted states may still extend the same side.  Thus the
corollary cannot yet be applied to arbitrary sides by merely selecting a
minimal cover.

Likewise, the two Kempe pages share their three boundary roots.  They are
not two disjoint branch sets and do not by themselves form a clique minor.
Any lift must split them into protected columns or use an actual rooted
model theorem; contracting both pages independently would identify the
same boundary vertices and is invalid.

