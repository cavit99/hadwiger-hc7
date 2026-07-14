# Independent audit: atomic double-contraction state split

## Verdict

**GREEN through Theorem 3.1, Corollary 3.2 and Corollary 4.1.**  The
double contraction supplies one common colouring from which the two
opposite edge-state colourings are obtained by recolouring literal
vertices outside the boundary.  Their restrictions therefore retain the
same exact partition of the literal seven-boundary and glue.  The rich
branch gives the stated leaf signal.  It does not, by itself, turn colour
saturation into labelled carriers.

Frozen source SHA-256:
`f56e7c58f88fbe97eaf33e60e73d08bc7e7cddd1f435a4370d6ae77c57d196bc`.

## 1. Chamber decomposition

For an edge `h=vw` of a seven-chromatic graph whose proper minors are
six-colourable, every six-colouring of `G-h` gives `v,w` the same colour:
otherwise restoring `h` would six-colour `G`.  Identifying the equal-colour
ends is therefore inverse to lifting a colouring of `G/h`.  Lemma 2.1 is
correct, including the boundary-label convention when one end lies in
`S`.

The four possible equality patterns at the two disjoint missing edges
`e=zu` and `f=xy` then split as claimed.  The three chambers in (2.2) are
nonempty because `G-e`, `G-f`, and `G/e/f` are proper minors; the chamber
with both pairs different would colour `G`.  Disjointness of `e` and `f`
is essential here and throughout the split theorem.

## 2. Boundary-preserving split

Lift a six-colouring `c` of `G/e/f` to `G-{e,f}`.  It has

\[
                     c(z)=c(u),\qquad c(x)=c(y).
\]

If `z` is free relative to `u`, recolouring only literal `z` restores
`e` and gives a colouring of `G-f`.  If `x` is free relative to `y`,
recolouring only literal `x` restores `f` and gives a colouring of `G-e`;
the same argument applies with `y` in place of `x`.  Because

\[
                          z\in A,\qquad x,y\in R,
\]

none of these recolourings changes a literal vertex of `S`.  Thus the
intact restriction of the first colouring to `G[A union S]` and the intact
restriction of the second to `G[R union S]` induce exactly the partition
of `S` induced by `c`.  A global permutation of one palette makes the two
restrictions agree vertex by vertex on `S`.  The absence of `A-R` edges
then makes their union a proper six-colouring of `G`.

Consequently `z` cannot be free simultaneously with either rich endpoint.
The logical negation is exactly

\[
 z\text{ is saturated outside }u
 \quad\text{or}\quad
 x\text{ and }y\text{ are both saturated outside their mate}.
\]

Here **saturated is literal and endpointwise**: each named endpoint has a
literal neighbour in each of the five alternate colours.  This should not
be weakened or silently replaced by a statement about the union of the
neighbourhoods of the contracted image of `xy`.

## 3. Exact chromatic number of the double contraction

Minor-criticality gives `chi(G/e/f)<=6`.  If a colouring used at most five
colours, a globally unused sixth colour would be absent from all three
literal neighbourhoods relevant to the theorem, so `z`, `x`, and `y`
would all be free in the lift.  Theorem 3.1 would then colour `G`.
Therefore `chi(G/e/f)=6`, as stated in Corollary 3.2.

## 4. Leaf signal

Assume `f=xy` is a selected-core edge incident with a leaf `x` and the rich
alternative holds.  The mate `y` has the old colour and witnesses none of
the five alternate colours.  Endpointwise saturation therefore gives five
distinct literal neighbours of `x`, one in each alternate colour.

The selected-core leaf condition excludes every selected-core neighbour
other than `y`, but it does not exclude host-graph chords or attachments
from components of `R-V(B)`.  Since there are no `A-R` edges, if no such
chord or off-core rich attachment exists, all five witnesses lie at five
distinct vertices of `S`.  The three alternatives of Corollary 4.1 are
therefore exhaustive.

This consequence is branch-specific.  In the thin-saturation branch the
theorem gives no rich-core leaf signal.  That branch still requires a
separate `z`-rooted connector/composition mechanism.

## 5. Edgewise fork

The elementary bound

\[
                         5\leq\chi(G-\{x,y\})\leq6
\]

is correct.  The upper bound follows from vertex-criticality.  A
four-colouring of `G-{x,y}` could be extended by assigning two fresh
colours to the adjacent vertices `x,y`, contradicting `chi(G)=7`.

The double-critical consequences quoted for the equality-five branch are
external literature input, not needed for Theorem 3.1 or Corollary 4.1.
The cited primary source is Kawarabayashi--Pedersen--Toft,
[*Double-critical graphs and complete minors*](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v17i1r87/pdf/).
The equality-six branch legitimately regenerates only an unrooted `K_6`
minor by `HC_6`; the note correctly declines to infer labelled contacts.

## Trust boundary

The proof uses all of the following and should not be exported without
them:

* the two edges are literal and vertex-disjoint;
* one common colouring of the double contraction is used;
* `z,x,y` lie outside the literal boundary, so the recolourings preserve
  its exact partition;
* the two closed shores have no open-shore cross-edge;
* every proper minor is six-colourable and `G` itself is not.

The theorem supplies a sharp palette-saturation fork.  Neither branch yet
supplies the disjoint, label-faithful carriers demanded by the active
stateful support-four composition, so this audit is not a closure claim.
