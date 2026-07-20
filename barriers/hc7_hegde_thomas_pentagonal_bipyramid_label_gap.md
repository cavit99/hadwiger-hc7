# Hegde--Thomas enlargements do not close the selected-column gap

## Status

Barrier to an intermediate inference.  The literature audit is exact.  The
finite calculation and paired-portal search received an independent GREEN
audit at script SHA-256
`d53e66678231eca6afc5d298a522f6cddd370b137feb974ee3cd756f7bbbadd3`.

## Setting

Let `PB` be the pentagonal bipyramid

\[
PB=\overline {K_2}\vee C_5,
\]

with poles `a,b` and cyclic rim `c_0,\ldots,c_4`.  Suppose a host graph
`F` has a *selected* spanning `PB`-minor model with connected branch sets

\[
L_a,L_b,L_{c_0},\ldots,L_{c_4}.
\]

In the current `HC_7` application, two vertices outside `F` have specified
neighbours in each of these seven selected branch sets.  Consequently an
unrooted clique minor in `F` is insufficient: the clique branch sets have to
retain the selected contacts.

## What the published theorem gives

Hegde and Thomas, *Non-Embeddable Extensions of Embedded Minors*, JCTB 131
(2018), Theorem 1.2, prove that if a weakly four-connected nonplanar graph
`H` has `PB` as a minor, then `H` has a minor isomorphic to an
`i`-enlargement of `PB` for some `i` from 1 through 7.

This conclusion is not relative to a prescribed `PB`-minor model.  The
theorem's hypotheses name only the two abstract graphs.  More importantly,
the proof begins by choosing an expansion of the base graph whose subdivision
is a subgraph of the host, and its subdivision theorem may replace that
subdivision by another one.  It does not assert that the branch vertices or
the resulting enlargement branch sets lie in prescribed branch sets
`L_x`.  See Theorem 3.1 and the proof outline immediately following it in
the primary source:

<https://arxiv.org/abs/1401.2973>

Thus Theorem 1.2 supplies an abstract enlargement minor, but no conclusion
about the two outside vertices meeting its branch sets.

## The enlargement list does not repair the labels automatically

Every peripheral cycle of `PB` is a triangle.  Therefore enlargement types
2, 4, 6 and 7 are impossible.  Only the following can occur:

1. add an edge between nonconfluent vertices;
2. make one nonconforming vertex split; or
3. make the two conforming splits and added edge of operation 5.

The first two families do have a `K_5`-minor rooted at five unsplit vertices
of the old `PB`.  Operation 5 does not always have this property.

Here is one explicit operation-5 instance.  Split the adjacent vertices
`b,c_0`.  Write the two new vertices replacing `b` as `b_0,b_1` and those
replacing `c_0` as `x_0,x_1`.  Assign the old neighbours by

\[
\begin{aligned}
N(b_0)-\{b_1,x_0\}&=\{c_4\},&
N(b_1)-\{b_0,x_1\}&=\{c_1,c_2,c_3\},\\
N(x_0)-\{x_1,b_0\}&=\{c_1\},&
N(x_1)-\{x_0,b_1\}&=\{a,c_4\}.
\end{aligned}
\]

Thus the retained old edge is `b_0x_0` and the operation-5 added edge is
`b_1x_1`.  The split at `b` is conforming along the face `bc_0c_1`, and the
split at `c_0` is conforming along the other face `bc_0c_4`, so this is a
genuine Hegde--Thomas 5-enlargement.

There is no `K_5`-minor whose five branch sets are rooted at all five unsplit
old vertices

\[
a,c_1,c_2,c_3,c_4.
\]

There is also no `K_5`-minor in which five branch sets contain the complete
split fibres of five old `PB` labels.  (For a split label, its complete fibre
is the two-vertex set consisting of both replacement vertices.)

The enlargement nevertheless has an ordinary `K_5`-minor, for example with
branch sets

\[
\{a\},\quad
\{b_0,c_1,x_0\},\quad
\{b_1,c_2\},\quad
\{c_3,c_4\},\quad
\{x_1\}.
\]

The last singleton uses only one half of the split `c_0` fibre.  This is
exactly the distinction between an unlabelled clique minor and the
selected-column conclusion required by the application.

The failure persists for the actual two-root contact condition.  Add two
outside vertices `r,s`.  In each of the five unsplit singleton fibres let
both `r` and `s` contact that singleton.  In the two split fibres let both
outside vertices contact `b_0` and `x_0`, respectively.  Thus the two portal
sets in the enlargement are equal to

\[
P=\{a,c_1,c_2,c_3,c_4,b_0,x_0\}.
\]

Every old `PB` fibre is connected and contains a portal for each outside
vertex.  Nevertheless there is no `K_5`-minor in the enlargement whose five
branch sets each meet `P`.  Equivalently, this abstract enlargement does not
yield five disjoint clique-minor branch sets all adjacent to both outside
vertices.

The deterministic script

`active/hc7_pentagonal_bipyramid_enlargement_probe.py`

checks this by assigning each nonroot vertex either to one of the five rooted
branch sets or to the unused set, and testing connectedness and all ten
pairwise adjacencies.  It generates all labelled enlargements of the possible
types and reports:

```text
type-1: instances=6 unsplit-root failures=0 whole-fibre-root failures=0 ordinary-K5 failures=0
type-3: instances=15 unsplit-root failures=0 whole-fibre-root failures=0 ordinary-K5 failures=0
type-5: instances=50 unsplit-root failures=20 whole-fibre-root failures=20 ordinary-K5 failures=0
```

With the optional `--paired` flag, the script also checks every choice of a
left and right portal in each of the two split fibres (the five unsplit
fibres are portals for both sides):

```text
paired-endpoint tests=800 failures=140
```

The search is exhaustive on each generated graph: there are at most nine
vertices, and after five root sets have been fixed every remaining vertex is
assigned to one of five bags or left unused.

## Exact consequence

The Hegde--Thomas theorem is useful as an **unlabelled nonplanarity normal
form**.  In fact, the finite probe finds an ordinary `K_5`-minor in every
possible `PB` enlargement.  It does not provide the selected-column or
paired-portal conclusion needed in the `HC_7` application, even if one
optimistically couples the abstract split fibres to the old columns.

To use this route one still needs a new statement that is relative to the
chosen spanning `PB` model and preserves the two outside vertices' literal
contacts.  Five-connectivity of the host may make such a strengthening true;
the example above has order nine, 18 edges, minimum degree three, vertex
connectivity three, and chromatic number three.  It is therefore far from the
five-connected core, and it carries none of the operation-specific
six-colour responses forced by seven-contraction-criticality.  It does not
refute a strengthening that uses either of those host-level hypotheses.
