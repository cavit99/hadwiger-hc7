# Cross-trace linkage in the sole-exterior Moser cell

## 1. Setting

Let `G` be a hypothetical proper-minor-minimal counterexample to
`HC_7`, let `v` have degree seven, and suppose that

\[
 G-N[v]=C
\]

is connected.  Put `S=N(v)` and suppose that `G[S]` is the pure Moser
spindle

\[
 E(M)=\{01,02,03,04,12,16,26,34,35,45,56\}.
\]

The exact-state theorem says that every nonedge `P` of `M` occurs as
the unique repeated pair in a six-colouring of `G-v`.  In that colouring
the other five boundary vertices are rainbow.

For a nonedge `A={x,y}` of `M`, an **A-carrier** is a connected set in
`C` meeting both portal sets `N_C(x)` and `N_C(y)`.

## 2. Every two disjoint demands have a packet

### Theorem 2.1 (cross-trace two-linkage)

If `A` and `B` are vertex-disjoint nonedges of the pure Moser spindle,
then `C` contains vertex-disjoint `A`- and `B`-carriers.

### Proof

The three boundary vertices outside `A union B` contain a nonedge `P`.
For completeness, this finite property has a four-line hand check.  If
those three vertices were independent in `complement(M)`, they would be
one of the four triangles of `M`, namely

\[
012,\quad034,\quad126,\quad345.
\]

Their respective four-vertex complements are

\[
3456,\quad1256,\quad0345,\quad0126,
\]

and direct inspection of the displayed Moser edge list shows that none
has a perfect matching in `complement(M)`.  This contradicts the two
disjoint edges `A,B`.  Equivalently, every matching of order two in
`complement(M)` extends to a matching of order three.

Use the exact six-colouring whose repeated pair is `P`.  The four ends
of `A` and `B` now receive four distinct colours.  Since the state family
of the unmodified sole shore contains no state with at most five blocks,
the two ends of each of `A,B` lie in one bichromatic component: otherwise
a Kempe switch merges them and leaves a colour absent from `S`, allowing
`v` to be coloured.

Choose a shortest bichromatic path for each pair.  Its internal vertices
avoid `S` and hence lie in `C`.  The two paths use disjoint pairs of
colours, so they are vertex-disjoint.  Their interiors are the required
carriers.  \(\square\)

### Corollary 2.2 (reserved support, one edge at a time)

Fix `I={1,3}`.  On

\[
 U=\{0,5,2,4,6\}
\]

the missing edges form the cycle

\[
 05,52,24,46,60.
\]

For every edge `e` of this cycle there is an `I`-connector and an
`e`-carrier which are vertex-disjoint.

Thus no surviving sole-exterior obstruction can have one individually
unavoidable missing-cycle support.  The obstruction is necessarily a
failure of **simultaneous** choice: every `I`-connector meets every
five-edge rooted certificate even though, for each individual demand,
another `I`-connector avoids a carrier for that demand.

### Corollary 2.3 (the seven boundary terminals are 2-linked)

For every four distinct vertices of `S` and every pairing of them, there
are two vertex-disjoint paths in `H=G-v` joining the prescribed pairs.

Indeed, if both prescribed pairs are Moser nonedges, apply Theorem 2.1
and append their boundary ends.  If one pair is a Moser edge, use that
edge itself; it is disjoint from the other pair's boundary ends and from
the interior of its exterior carrier.  If both are edges, use the two
boundary edges.

Thus the output of the ten-state family is not merely five separate
Kempe supports: the Moser boundary is a fully 2-linked terminal set in
`H`.  The remaining synchronization lemma may therefore be sought as a
rooted-minor theorem for a 2-linked seven-terminal set, with the
palette-wall/minor-transition axiom distinguishing it from ordinary
rooted linkage.

## 3. Why the result does not yet give the reserved model

Theorem 2.1 is a two-demand statement.  The desired `K_7` model requires
one `I`-connector disjoint from a rooted certificate for all five edges
of the missing `C_5`.  Pairwise disjoint realizability does not imply this
six-demand synchronization.

The accompanying verifier
`moser_sole_exterior_trace_witness_probe.py` gives a sharp warning.  It
constructs a graph with all of the following properties:

1. the Moser boundary and a sole connected exterior;
2. vertex-connectivity and minimum degree equal to seven;
3. all ten exact one-pair boundary states are realizable;
4. for the fixed trace `13`, all five Rolek--Song paths occur in one
   colouring, with the required disjointness for nonincident cycle edges;
5. for **every** internal exterior edge `xy`, `H-xy` has a six-colouring
   with exact trace `13` and `x,y` equal;
6. the rooted `K_5` certificate confined to the five unique colour
   classes uses every one of the ten subdivision vertices, so no
   `13`-connector avoids that fixed colour-preserving certificate.

This is not a counterexample to the desired uncoloured conclusion.  It is
five-colourable, hence it fails the palette-wall nonextension axiom, and
it has a different rooted `K_5` model disjoint from a `13`-connector.
The point is exact: existence of all ten traces and of all aligned
one-edge witnesses does not by itself synchronize the fixed Kempe model.
A valid closure must use that no at-most-five-block state extends the
original shore (or use `K_7`-minor exclusion to switch to a different
rooted model).

## 4. Exact remaining structural lemma

The finite labels have now been removed from the live geometric step.
The needed statement can be phrased as follows.

> **Palette-wall synchronization lemma.**  Let a seven-connected graph
> have a pure-Moser seven-boundary with a sole full shore `C`.  Assume
> (i) all ten one-pair states and their cross-trace two-linkages from
> Theorem 2.1, and (ii) no boundary state with at most five blocks extends
> `C`, while every proper internal minor of `C` unlocks such a state.
> Then either there is a `13`-connector disjoint from a rooted `K_5` on
> the other five roots, or `C` exposes an exact seven-adhesion.

Unlike the earlier fixed-trace reserved-connector assertion, this target
explicitly includes the global axiom missing from the sharp witness.  A
minimal-connector proof may now use Theorem 2.1 to replace every single
blocked support; failure of two replacements must be converted into an
internal operation unlocking a forbidden five-block state, or into the
exact adhesion.
