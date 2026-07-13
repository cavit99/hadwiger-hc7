# The exact boundary-state family in the sole-exterior equality cell

## 1. Complete state classification

Let (G) be a graph which is not six-colourable but whose proper minors
are six-colourable.  Let (v) have degree seven, put

\[
                         N=N_G(v),
\]

and suppose (G-N[v]) has the unique component (C).  Assume
(alpha(G[N])\le2), as is forced in the degree-seven critical cell.
Write

\[
                         H=G-v=G[N\cup C].
\]

For a six-colouring of (H), its **boundary state** is the equality
partition which it induces on (N).

### Theorem 1.1 (exact one-pair family)

The boundary states extending over (H) are exactly

\[
 \bigl\{,P\mid\{x\}:x\in N-P:
             P\text{ is a nonedge of }G[N],\bigr\}.       \tag{1.1}
\]

In particular, every six-colouring of (H) uses all six colours on
(N), with exactly one repeated independent pair.  Conversely every
nonedge (P\subseteq N) occurs as that exact repeated pair.

#### Proof

If a six-colouring of (H) used at most five colours on (N), the
sixth colour could be assigned to (v), producing a six-colouring of
(G).  Hence (N) uses all six colours.  It has seven vertices, so
one colour is repeated.  No colour occurs three times because each
colour class is independent and (alpha(G[N])\le2).  Thus the state
has exactly one two-vertex block (P), and (P) is a nonedge.  This
proves containment in the family (1.1).

Conversely fix a nonedge (P=\{a,b\}).  Contract the connected star
(G[\{v,a,b\}]) to one vertex.  A six-colouring of the resulting
proper minor expands, after deleting (v), to a six-colouring of
(H) in which (a,b) have one colour and no other vertex of (N)
has that colour: every vertex of (N-P) was adjacent to the contracted
star vertex.  The first paragraph now forces the other five boundary
vertices to have five distinct colours.  Hence the resulting state is
exactly the member of (1.1) indexed by (P). \(\square\)

For the pure Moser spindle, the missing-edge graph has ten edges, so
(1.1) consists of exactly ten states.  This is a complete equality, not
merely a list of states known to occur.

## 2. Every internal minor crosses the palette wall

### Corollary 2.1

Perform any proper minor operation wholly inside (C), leaving (N[v])
untouched.  Some six-colouring of the resulting graph induces on (N)
a state with at most five blocks.  That state did not extend the original
(H).

For an internal edge deletion (e=xy), its ends have the same colour in
every six-colouring of (G-e).

#### Proof

The operated graph is a proper minor of (G), and hence has a
six-colouring.  The colour on (v) is absent from its complete
neighbourhood (N), so (N) uses at most five colours.  Theorem 1.1
says that no such state extended the original (H).  If a colouring of
(G-e) gave (x,y) different colours, restoring (e) would colour
(G). \(\square\)

Thus the sole-exterior component is a rooted state-critical object with
an unusually explicit interface: its original extension family is the
ten one-pair states, while every internal operation unlocks the opposite
side of the six-colour palette wall.

## 3. Simultaneous Kempe supports

Fix a colouring from Theorem 1.1 with repeated pair (P), and let
(R=N-P) be the five rainbow roots.

### Theorem 3.1 (rainbow nonedges are Kempe-connected)

If (xy) is a nonedge of (G[R]), the two-colour component containing
(x) also contains (y).  Consequently there is an (x)-(y) path
whose interior lies in (C).

If (xy) and (zw) are vertex-disjoint nonedges of (G[R]), their
two paths can be chosen vertex-disjoint in the same colouring.

#### Proof

The colours of (x,y) occur nowhere else on (N).  If the two roots
were in different bichromatic components, interchange their colours on
the component containing (x).  This would make (x,y) a second
two-vertex boundary block while leaving (P) unchanged.  The boundary
would then use at most five colours, and the missing sixth colour could
be assigned to (v), contradicting the choice of (G).

A shortest bichromatic (x)-(y) path has no internal boundary vertex,
because no other boundary vertex has either endpoint colour.  It avoids
(v), whose deletion defined (H), so its interior lies in the unique
exterior component (C).

For two vertex-disjoint nonedges the four endpoint colours are distinct.
Their two bichromatic subgraphs therefore have disjoint vertex sets, and
the corresponding paths are vertex-disjoint. \(\square\)

In the favourable pure-Moser trace (P=\{1,3\}), the missing-edge graph
on (R) is a (C_5).  Hence every two-edge matching of that cycle has
simultaneous disjoint exterior supports.  The unresolved issue is not
the existence of these paths; it is reserving a (1)-(3) connector
disjoint from a set of supports large enough to package the rooted
(K_5).

## 4. Structural target exposed by the theorem

The ten-state equality suggests a finite-state invariant which is
stronger than one fixed trace.  A prospective closure may use the Kempe
reconfiguration graph on the ten nonedges of the Moser boundary:

* vertices are the exact one-pair states in (1.1);
* an edge records a boundary-changing Kempe switch which preserves six
  colours on (N);
* an internal minor transition necessarily exits this ten-vertex state
  set by Corollary 2.1.

A useful next theorem would show that, in a seven-connected
(K_7)-minor-free host, this state graph cannot realize all ten states
while every missing-(C_5) support meets every reserved connector.  Such
a theorem would turn the protected-connector problem into holonomy of the
complete boundary-state family rather than another list of individual
paths.
