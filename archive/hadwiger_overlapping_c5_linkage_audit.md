# Overlapping nested C5s: extraction is false, pumping still works

## 1. Verdict

The proposed clean-subchain statement is false, even in its strongest
intended setting.

There are arbitrarily large 5-connected planar triangulations with an
arbitrarily long nested family of chordless separating 5-cycles such
that

* every cycle contains one common public vertex;
* after taking alternate layers, the four-vertex private parts are
  pairwise non-touching;
* no two cycles are vertex-disjoint; and
* there is no separator of order at most four.

Thus shared public vertices do not force a small separator, and no
function `f(m)` of the proposed kind exists for `m=2`.

Fortunately, vertex-disjoint cycles are unnecessary for the pumping
theorem.  Two overlapping nested 5-cycles in the HC7 planar society
still have a five-path linkage; every shared vertex is represented by
a trivial path.  Adding the two fixed protected roots gives the clean
seven-root linkage required by extension-family pumping.  Consequently
the 1024-annulus bound applies directly to noncrossing nested cycles,
including cycles with shared public vertices.

## 2. Counterexample construction

Begin with the depth-`L` pentagonal sphere triangulation `H_L` from the
uniform web construction.  It consists of two pentagonal disks glued
along their common boundary

\[
 C_0=a_0a_1a_2a_3a_4a_0.
\]

On the positive side, write the concentric rings as

\[
 R_j=r^j_0r^j_1r^j_2r^j_3r^j_4r^j_0
 \qquad(1\le j\le L).
\]

Consecutive rings have the standard triangulated-annulus edges

\[
 r^{j-1}_i r^j_i,qquad r^{j-1}_i r^j_{i-1}
 \quad(i\in\mathbb Z_5),                           \tag{2.1}
\]

where `R_0=C_0`.  A hub is adjacent to all vertices of `R_L`.

Contract the radial path

\[
 a_0r^1_0r^2_0\cdots r^{L-1}_0                  \tag{2.2}
\]

to one vertex `v`, but do not contract the last edge from
`r^(L-1)_0` to `r^L_0`.  Let the resulting simple plane graph be
`H_L^*`.

For `0<=j<=L-1`, the image of `R_j` is a chordless 5-cycle

\[
 C_j=v,r^j_1r^j_2r^j_3r^j_4v,                  \tag{2.3}
\]

with the evident interpretation at `j=0`.  These cycles are nested and
all contain `v`.

### Lemma 2.1 (the contracted web remains 5-connected)

For every `L>=2`, `H_L^*` is a simple 5-connected planar
triangulation.

#### Proof

Contract the edges of (2.2) from the outside inward.  At each step the
contracted radial edge has exactly the two common neighbours belonging
to its incident triangular faces.  Suppressing the resulting parallel
copies therefore decreases the vertex count by one and the edge count
by three, so the resulting simple plane graph remains a triangulation.

The last ring `R_L` was deliberately left uncontracted.  A vertex which
loses a neighbour because two consecutive column-zero vertices merge
had degree six before the loss, and hence has degree at least five
afterwards.  Vertices of `R_L` retain degree five, all other unmerged
vertices retain degree at least five, and the merged vertex `v` has
larger degree.  Thus

\[
 \delta(H_L^*)\ge5.                               \tag{2.4}
\]

It remains to exclude a separator of order three or four.  The edge
description (2.1) after identifying the column-zero vertices is local:
edges join vertices in one ring or two consecutive rings, except for
edges incident with `v` and the two hubs.  Inspecting two consecutive
layers gives the following two facts.

1. Every 3-cycle is one of the displayed triangular faces.
2. Every 4-cycle has an annular or ring edge as a chord.

For clarity, away from `v` these are the usual two triangles in each
quadrilateral cell of (2.1).  At `v`, the only new triangles are

\[
 v r^{j-1}_1 r^j_1 v,qquad
 v r^{j-1}_4 r^j_4 v,
\]

which are precisely the two faces produced by the contraction.  Any
four-cycle through `v` either lies in one such pair of adjacent cells,
where its annular diagonal is a chord, or would require an edge
skipping a layer, which does not exist.

In a plane triangulation, every minimal cut of order three is a
separating triangle, and every minimal cut of order four contains a
separating chordless 4-cycle (a chord would give a separating
triangle).  The two inspected facts and (2.4) therefore exclude all
cuts of order below five. \(\square\)

The uniform local inspection can also be checked from the counts.  If
the original graph has `10L+7` vertices, then `H_L^*` has

\[
 9L+8
\]

vertices and exactly

\[
 3(9L+8)-6
\]

edges, as required for a sphere triangulation.

### Lemma 2.2 (arbitrarily many non-touching private parts)

The subfamily

\[
 C_0,C_2,C_4,\ldots
\]

consists of nested chordless separating 5-cycles with common public
part `{v}` and pairwise non-touching private parts

\[
 V(C_{2j})-\{v\}.
\]

Every member is obstructing: it has at least two vertices on either
side.  No two members are vertex-disjoint, while Lemma 2.1 says that no
separator of order at most four exists.

#### Proof

The private vertices lie in distinct rings.  Edges of the positive
disk join only equal or consecutive ring levels, so levels differing
by at least two have neither a common private vertex nor an edge
between their private parts.  All cycles contain `v`, proving the
failure of disjointness.  The uncontracted final ring and hub provide
at least six vertices inside the last selected cycle; the negative
disk and earlier rings provide at least two outside every selected
cycle. \(\square\)

This proves that clean vertex-disjoint subchain extraction is the wrong
target.

## 3. Set-to-set linkage with overlapping cycles

The correct replacement is a linkage lemma which permits trivial
paths.

### Lemma 3.1 (overlapping cycle linkage)

Let `C,D` be two nested, noncrossing 5-cycles in a plane graph `Q`.
Assume no set of at most four vertices separates `C` from `D`.  Then
there are five pairwise vertex-disjoint `C-D` paths whose initial
vertices are all five vertices of `C` and whose terminal vertices are
all five vertices of `D`.

Every vertex in `C intersect D` is the unique vertex of a trivial path.
The nontrivial paths can be chosen with interiors in the closed annular
region between the cycles and disjoint from both cycles.  Their endpoint
bijection preserves cyclic order, up to reversal.

#### Proof

By the set version of Menger's theorem, the maximum number of disjoint
`C-D` paths equals the minimum order of a vertex set meeting every such
path.  The hypothesis makes this minimum at least five, while each
terminal set has order five.  Hence five paths exist and use every
vertex of both cycles as an endpoint.

If `x` belongs to both cycles, the path using `x` as its initial vertex
must also use `x` as its terminal vertex: otherwise a different path
would have to end at `x`, contradicting disjointness.  Replace that path
by the trivial path at `x`.

For each remaining path, keep the segment after its last visit to `C`
and before its first subsequent visit to `D`.  A simple arc cannot
leave the annular region without meeting one of its boundary cycles,
so the retained segment lies in the annulus and has no other cycle
vertex internally.  Finally, disjoint arcs across an annulus cannot
have alternating ends.  After a small isotopy separating any common
boundary arcs, their endpoint map is cyclic, up to reflection.
\(\square\)

## 4. Why HC7 supplies the linkage

Let the HC7 planar side be attached through

\[
 S=A\mathbin{\dot\cup}V(C),qquad A=K_2.
\]

Let `C_i,C_j` be nested obstructing 5-cycles in that side.  If a set
`X` of at most four vertices met every `C_i-C_j` path, then deleting

\[
 A\cup X
\]

would separate the nonempty region inside the inner cycle from the
nonempty region outside the outer cycle in the ambient graph.  This is
a cut of order at most six, contrary to 7-connectivity.  Lemma 3.1
therefore supplies five annular paths.

Together with the two trivial paths at the fixed vertices of `A`, this
is a clean seven-root linkage.  Shared public vertices of the two
cycles simply give further trivial paths; they cause no difficulty in
the pumping construction.

## 5. Operational pumping without extraction

Order any noncrossing nested chain of obstructing pentagons by
inclusion of their inside disks.  Apply Lemma 3.1 between consecutive
cycles and propagate the cyclic labels inward along the linkage.
Consecutive annuli have disjoint interiors, so concatenating paths of
the same label gives a clean linkage between any two members of the
chain.  Trivial paths concatenate trivially.

For the adhesion `K_2 join C_5` with six colours, there are exactly ten
proper equality states on the seven roots, and therefore at most

\[
 2^{10}=1024
\]

inward extension families.  If a chain had at least 1024 annuli, two
families would repeat.  The linked-annulus pumping theorem would then
produce a proper non-6-colourable minor, contradicting
minor-criticality.

### Theorem 5.1 (overlap-robust HC7 depth bound)

Every noncrossing nested chain of obstructing 5-cycles in the residual
HC7 planar society has fewer than 1024 annuli, whether or not the
cycles share public vertices or public edges.

Thus the pumping bound is already operational on the intersecting
cycle outcome.  The remaining structural issue is not clean-subchain
extraction; it is handling branching rather than nested chains, and
bounding the complexity of a single annular torso.
