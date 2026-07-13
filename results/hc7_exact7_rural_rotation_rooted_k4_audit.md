# Independent audit: rural rotation gives a rooted `K_4`

Audited file: `results/hc7_exact7_rural_rotation_rooted_k4.md`.

## Verdict

**GREEN.**  Lemma 1.1 now uses the single selected cell-free
block-terminal rib, exactly as required below.

The common-face statement is correct in the stated **cell-free
block-terminal rib** setting.  No family of separately chosen pairwise
webs is used.  The selected rib contains the augmented graph
`K+alpha Q+beta P` literally; deleting its artificial terminals gives one
face of `K` containing every marked vertex.  Three-connectivity makes that
face boundary a cycle, and set-terminal crosslessness puts `Q` and `P` on
opposite `x-y` arcs.

The pole-rotation order, repeated-occurrence handling, and literal
rooted-`K_4` subdivision also audit GREEN.  The repeated-end outcome
remains deliberately only a collision certificate.

## 1. Why the fixed web is essential

The source correctly uses the one selected cell-free block-terminal web.
A separately chosen pairwise web for `(x,q,y,p)` could contain actual
carrier vertices in clique cells, so deleting completion edges from such
a certificate would not prove cofaciality.  The patched proof avoids that
invalid route entirely.

## 2. Exact fixed-rib proof of Lemma 1.1

Use the single cell-free web/rib embedding already supplied by the planar-
rib outcome of the block-terminal theorem.  In that selected plane rib,

\[
                     K^+=K+\alpha Q+\beta P
\]

is a literal subgraph, and `(x,alpha,y,beta)` is the outer frame.  There
are no actual carrier vertices in clique cells.

Delete `alpha,beta` and every completion-only edge.  Deleting edges only
merges faces.  Since both artificial terminals lie on the outer frame,
all faces incident with either terminal merge with the outer face.  Hence
the resulting embedding of literal `K` has one face incident with

\[
                         \{x,y\}\cup Q\cup P.
\]

The carrier is three-connected, so every facial boundary is a cycle; call
this one `C`.  Whitney's theorem makes the embedding, and hence `C`, unique
up to reflection.  Uniqueness is useful here but is not needed to
synchronize separately selected webs.

Finally, all of `Q` lies on one open `x-y` arc of `C` and all of `P` on
the other.  If some `q in Q` and `p in P` lay on the same open arc, the
`q-p` subpath of that arc avoiding `x,y` and the opposite `x-y` arc would
be vertex-disjoint.  This would be a set-terminal cross in `K`, contrary
to hypothesis.  Since both sets are nonempty, this argument puts the two
entire sets on opposite arcs.

This proves Lemma 1.1 from one fixed literal embedding and uses no
completion edge as a host edge.

The exact pair-carrier application also has the literal nonedge `xy`.
Although the fixed-rib proof above does not need it, Section 1 should
retain that inherited fact to avoid suggesting a more general theorem
than the proof spine supplies.

## 3. Pole rotation versus facial order

Retain every literal pole--carrier edge as an occurrence before using the
tree-pole theorem.  Start with the planar **simple** quotient furnished by
the spanning-rural theorem, and reinsert parallel copies in a thin band
around their common simple edge.  Copies with the same carrier end are
consecutive in that band; their internal order may be fixed arbitrarily.
This is legitimate because contraction supplies no pre-existing plane
rotation inside the unembedded pole.

For a fixed pole `z`, all its distinct simple neighbours lie on `C`, and
`z` is drawn in the face bounded by `C`.  Noncrossing spokes from one
vertex to distinct vertices of a facial cycle have the same cyclic order
at the centre as their ends have on the cycle, up to reversal.  Otherwise
two spokes would cross in the disk.  Deleting other spokes does not alter
the relative order of the four selected distinct ends.

Therefore, when `u(a),u(b),u(c),u(d)` are distinct, their cyclic pole order
is exactly their order on `C`, up to reversal.  When two ends coincide,
this order comparison is intentionally not used; the theorem returns the
repeated-end collision.

An occurrence is a literal pole edge end, not merely a simple neighbour.
Two different occurrences may have both the same carrier end and the same
pole base, but they are still two different literal edges.  The
occurrence-leaf expansion in the tree-pole theorem records them separately.

## 4. Literal rooted `K_4` subdivision

Assume the four carrier ends are distinct.  The tree-pole theorem gives
two vertex-disjoint paths inside the pole connector tree, one joining the
bases of `a,c` and the other the bases of `b,d`.  Add the four selected
literal pole--carrier edges.  This gives paths

\[
 D_{ac}:u(a)\leadsto u(c),\qquad
 D_{bd}:u(b)\leadsto u(d).
\]

Their interiors lie in `X`, while `C` lies in disjoint `K`.  Their pole
portions are vertex-disjoint, and their four endpoints on `C` are distinct;
hence the two paths are mutually internally disjoint and meet `C` only at
their named ends.

The four ends occur alternately on `C`.  The four arcs of `C` between
successive ends, together with `D_ac,D_bd`, are six pairwise internally
disjoint paths realizing all six edges of a subdivision of `K_4`.  Its
branch vertices are exactly

\[
                         u(a),u(b),u(c),u(d).

Every path edge is literal.  Completion edges are used only to select the
plane order in the fixed rib.

If the two occurrences in one tree path have the same pole base, that path
may have a one-vertex pole portion; after adding its two distinct
attachment edges it is still a valid carrier-end path.  The two pole
portions remain disjoint because they lie in opposite components of the
tree edge witnessing the noncircular split.

Thus Theorem 2.1 is GREEN with the fixed-rib proof now in the source.

## 5. Exact scope

The distinct-end branch produces a genuine rooted `K_4` subdivision in
`G[K union X]`.  It does not itself provide the other three pairwise
adjacent branch sets required for `K_7`.

The collision branch likewise records only two distinct literal pole
edges sharing a carrier end, together with their separate occurrence
data.  Such a collision does not supply four rooted branch vertices and
does not by itself justify splitting the pole while preserving labels.

Accordingly the file's final conversion target is correctly stated as
remaining work: the rooted duty object or collision must still be combined
with the untouched frame traces, opposite pole, and attained decorated
state to yield a literal `K_7`, a supported rank promotion, or a bilateral
state.
