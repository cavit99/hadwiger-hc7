# Audit: concentrated two-defect closure

## Verdict

**GREEN.**  The concentration atom is exact, the rooted-`K_4` lift is
literal, all five cycle roots lie on one common face in the target-free
branch, and reinserting the concentrated singleton proves planarity after
deleting the same fixed pair `{h_1,h_2}`.

## 1. Exact atom

The concentrated class cannot be deficient.  If, for example,
`P_s subseteq {x_s,x_t}`, then `x_s` misses `b_s`, so the nonempty portal
set is `{x_t}`.  The vertex `b_s` then has only its four singleton-clique
neighbours and `x_t`, while missing `v`, contradicting minimum degree at
least seven.

For the nonempty set `T` of concentrated ordinary labels, the connected
set `R=B-X` is anticomplete to `T` and

\[
 N(R)\subseteq X\cup\{v\}\cup(S-T).
\]

Any `q in T` lies outside `R union N(R)`, so this is an actual separator.
Seven-connectivity gives `7<=|N(R)|<=8-|T|`, hence `|T|=1` and equality
in every allowed row.  Thus the unique label `q` has `P_q=X`, while `R`
sees `X`, `v`, and every singleton other than `q`.

The five vertices

\[
 b_s,b_t,x_s,v,x_t
\]

induce the asserted `C_5`: the five cycle edges are the singleton edge,
the two witness rows and the two foot edges; the five chords are absent by
the two deficient rows, the two apex nonedges and the same-bipartition
nonedge `x_sx_t`.  The two remaining ordinary labels `h_1,h_2` are
complete to this cycle, and `q` is complete to it and to both hubs.  The
exact separator makes `q` anticomplete to `R`.

## 2. Rooted model and common face

Put `W=G-{q,h_1,h_2}`.  It is 4-connected: a separator of order at most
three in `W`, augmented by the three deleted vertices, would be a cut of
order at most six in `G`.

For any four cycle roots, an `X`-rooted `K_4` in `W` gives four disjoint
connected clique bags, each adjacent to the three literal singleton bags
`q,h_1,h_2` through its root.  Those singleton bags form a triangle, so
the lift is a literal `K_7`.

Otherwise the rooted theorem makes `W` planar and every four-subset of
the five cycle vertices cofacial.  Faces for two four-subsets sharing
three fixed roots coincide because `W` is 3-connected and distinct faces
share at most two vertices.  Hence all five cycle roots lie on one face.

## 3. Fixed global apex pair

In `W`, the complete neighbourhood of `q` is exactly the five cycle
vertices: its only other neighbours are the deleted hubs and it has no
edge to `R`.  Since `W` is 3-connected, the common face has a simple
boundary.  Place `q` in that face and draw its five incident edges as
spokes.  This produces a plane drawing of

\[
 G-\{h_1,h_2\}=W+q.
\]

Thus the rural output uses one literal pair of original vertices selected
once by the unique concentrated label.  It is fully compatible with the
coherence requirement; no local apex choices remain in this cell.

Together with the independently audited disconnected-bag closure, this
discharges every `d=2` outcome of the palette-to-label theorem under its
written two-portal hypothesis.
