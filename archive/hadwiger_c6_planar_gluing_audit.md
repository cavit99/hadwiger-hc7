# Audit of the proposed planar-gluing colouring alternative

## 1. The literal planar conclusion is impossible

Retain the degree-seven configuration with apex (v), universal
boundary vertex (z), triangular-prism boundary (W), and connected
full shores (D_1,D_2).  Put

[
 J=G-{v,z}=G[Wcup D_1cup D_2].
]

If (J) were planar, the Four Colour Theorem followed by two fresh
colours on (z,v) would indeed give a six-colouring of (G).  The
premise, however, cannot occur.

### Lemma 1.1

For either shore (D), the graph (G[Wcup D]) is nonplanar.

### Proof

The triangular prism (W) is three-connected and planar, so its plane
embedding is unique up to reflection.  Its faces are two triangles and
three quadrilaterals; no face contains all six vertices of (W).

In a planar supergraph of (W), a connected component of the graph
outside (W), together with all its incident edges to (W), is a
single (W)-bridge.  The interior of a connected bridge lies in one
face of the embedded (W), so all of its attachments must occur on the
boundary of that face.  But (D) is connected and full to (W): its
attachment set is all six vertices of (W).  No face of the prism has
that boundary.  This is impossible. (square)

Consequently (J) contains the nonplanar subgraph (G[Wcup D_1]),
regardless of the relative orientation chosen for disk embeddings of
the two shores.

## 2. What synchronization does and does not mean

The bare-web theorem embeds a shore (D) with four selected portal
classes on one face.  It does **not** embed the full graph
(G[Wcup D]).  Even a common face containing all six portal sets of
(D) does not cure this: adding the six boundary vertices and all nine
edges of the triangular prism is a separate rooted-planarity problem,
and Lemma 1.1 rules it out.

One can expose the obstruction by choosing a Hamiltonian cycle of the
prism.  The three remaining prism edges must be assigned to the two
sides of that cycle in its planar embedding.  A full connected shore
already uses attachment data on all six cycle vertices.  Merely
reversing its disk order says nothing about whether those three chords
can be inserted without crossing the shore.  The circular frame index
records part of precisely this missing chord-side information.

Thus the holonomy has two levels:

1. **embedding holonomy:** SPQR flips change the circular frame state;
2. **colour holonomy:** proper-minor colourings induce boundary
   permutations that must compose trivially along a rope.

Trivial embedding holonomy does not imply that the union is planar.

## 3. Correct colouring target

A legitimate replacement for the failed shortcut is an extension-state
theorem:

> Decorate each bounded-adhesion rung or SPQR torso by the set of
> four-colourings of its boundary that extend across it.  If the product
> of these transfer relations contains a common boundary state for the
> two shores and the prism, then colour the shores with four colours and
> use fresh colours on (z) and (v).

The Four Colour Theorem may justify individual planar-torso extension
relations, but it cannot be applied once to (J).  Moreover ordinary
4-colourability of a planar torso does not automatically give extension
for a prescribed adhesion colouring; Kempe permutations or an explicit
finite boundary-state calculation are still required.

This audit therefore rejects only the global-planarity shortcut.  It
leaves colour-state gluing as a viable, genuinely stronger alternative
to a rooted-minor construction.
