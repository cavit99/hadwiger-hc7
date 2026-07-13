# Pair-mode normalization for core-coloured adhesion vertices

## 1. Setting and the target quotient

Use the two-shore exact antipodal gate cut

\[
 L=\{v\}\mathbin{\dot\cup}X\mathbin{\dot\cup}\{p,q\},
 \qquad X=\{x_1,x_2,x_3,x_4\},                  \tag{1.1}
\]

where (G[X]) consists of the two edges (x_1x_2,x_3x_4).  The roots
(x_i) have four distinct core colours.  The two other colours are the
gate colours (\alpha,\beta).  The cut has exactly two shores, denoted
(C_0) and (C_1), and every cut vertex has a neighbour in each shore.

A mode

\[
                    B_0\mid B_1\mid B_2\mid\{r\},
                    \qquad |B_i|=2,              \tag{1.2}
\]

is useful only when every (B_i) is independent and the three pair
blocks are pairwise adjacent in the boundary quotient.  Every mode
constructed below has this property.  One pair contains (v), so it sees
both core pairs.  The edge of (G[X]) incident with the fixed core-colour
mate joins the other two pair blocks.

All Kempe switches below are performed in the (H=G-v) part of the
(C_0)-side, including the other cut vertices but omitting (v) and the far
shore.  The vertex (v) is coloured only after the switch, with the gate
colour opposite to the resulting colour of (0).  Thus the switches prove
extension of a boundary state by (C_0); they are not asserted to be
global switches.

## 2. Exactly one adhesion vertex has a gate colour

### Theorem 2.1 (one-gate normalization)

Suppose (p) has a gate colour and (q) has the core colour of (x_i).
Then either

1. the (C_0)-side accepts a proper mode
   \[
       \{v,p\}\mid\{q,x_i\}\mid\{x_j,x_k\}\mid\{x_\ell\},
                                                               \tag{2.1}
   \]
   where (x_jx_k) is a missing edge of (G[X]); or
2. the three roots (X-\{x_i\}) have a rooted (K_3)-model whose centre
   bag has interior in (C_0) and whose two leaf bags are singleton roots.

#### Proof

Use the (K_0)-switch to choose (c(v)=c(p)).  Properness gives the two
independent pair blocks (\{v,p\}) and (\{q,x_i\}).

On the other three roots, the two missing edges form a two-edge star and
its leaves form the other literal edge of (G[X]).  A global bichromatic
path for each missing edge exists by four-saturation.  Its interior lies
in one shore: the only cut vertices in its two colours are its ends.

If one candidate edge has no path on the (C_0)-side, its ends lie in
different components of the corresponding two-colour side graph.
Switching one endpoint component merges those ends and changes no other
boundary block, giving (2.1).  If both candidate edges have side-local
paths, join their interiors to their common root.  This is the centre bag
of a rooted triangle; the two arms give its leaf contacts and the literal
edge of (G[X]) joins the singleton leaves. \(\square\)

The pair-block quotient in (2.1) is a triangle: (v) joins the first block
to both core blocks, and the literal matching edge from (x_i) to the
centre of the missing-edge star joins the latter two.

## 3. Pure core with two distinct core colours

Suppose now

\[
                    c(p)=c(x_a),\qquad c(q)=c(x_b),qquad a\ne b.
                                                               \tag{3.1}
\]

Fix one gate colour (\gamma) which is safe at (v) on the (C_0)-side.
For (r\in\{p,q\}), call (r) **(\gamma)-isolatable** when it and its
same-colour root mate lie in different components of the side graph
induced by their core colour and (\gamma).

### Theorem 3.1 (isolation, capacity, or a four-terminal web)

At least one of the following holds.

1. The (C_0)-side accepts a proper mode of the form
   \[
      \{v,p\}\mid\{q,x_b\}\mid\{x_j,x_k\}\mid\{x_\ell\},
                                                               \tag{3.2}
   \]
   or its version with (p,q) interchanged.
2. For one of the two choices of fixed pair, the remaining three core
   roots have the shore-local rooted triangle described in Theorem 2.1.
3. There are disjoint connected carriers in (C_0), one joining the
   portal sets of (p,x_a) and one joining those of (q,x_b).
4. The four portal sets of (p,x_a,q,x_b) lie on the outer face of a
   bare set-terminal Two Paths web in (C_0).

#### Proof

If (p) is (\gamma)-isolatable, switch the component containing (p).
No other cut vertex has either of the two involved colours: (x_a) is in
the other component, (q,x_b) use the distinct core colour (b), and all
other roots have their own core colours.  Thus only (p) changes on the
boundary, and it now has colour (\gamma).  Give (v) colour (\gamma),
obtaining the pair (\{v,p\}) while retaining (\{q,x_b\}).

Among the three roots (X-\{x_b\}), the two missing edges form a star.
If either missing pair is disconnected in its two-colour side graph,
switching one endpoint component gives (3.2).  The switch does not touch
(p), which now has a gate colour, or (q,x_b), whose core colour was
removed from the three-root set.  If neither pair is disconnected, the
two paths give outcome 2 exactly as in Theorem 2.1.  The same argument
applies with (p,q) interchanged.

It remains that neither (p) nor (q) is (\gamma)-isolatable.  Hence there
is a side-local two-colour path from (p) to (x_a), and one from (q) to
(x_b).  Apply the set-terminal Two Paths/Web Theorem to the four full
portal sets in (C_0).  Its linkage outcome gives two disjoint carriers,
which is outcome 3.  In its crossless outcome an edge-maximal completion
is a web.  Any nonempty clique part inserted behind a facial triangle has
relative boundary consisting of at most its three rib vertices together
with the three omitted cut labels.  Its boundary therefore has order at
most six, contrary to the relative seven-connectivity inequality.  Hence
the web is bare, giving outcome 4. \(\square\)

No unknown (pX)- or (qX)-edge is used in this proof.  In particular, the
pair (\{q,x_b\}) is independent because its vertices had one colour in
the original proper colouring; the third pair is explicitly chosen from
the missing edges of (G[X]).

## 4. Pure core with one repeated core colour

It remains that

\[
                         c(p)=c(q)=c(x_a).        \tag{4.1}
\]

Thus (p,q,x_a) are pairwise nonadjacent.  Pair-mode normalization must
split this three-vertex equality block; merely finding a perfect matching
of boundary nonedges is not enough.

For a gate colour (\gamma), inspect the components of the side graph on
the core colour (a) and (\gamma).

### Theorem 4.1 (triple split or exact triple lock)

Either Theorem 2.1's mode/rooted-triangle alternative holds after
interchanging the roles of (p) and (q), or, for each safe gate colour
(\gamma\in\{\alpha,\beta\}), the component partition induced on
(\{p,q,x_a\}) is one of

\[
                         pqx_a,qquad pq\mid x_a. \tag{4.2}
\]

In other words, the sole remaining obstruction is the **triple lock**:
for neither gate colour is (p) or (q) alone in a component separated
from the other two vertices.

#### Proof

Suppose, for some safe gate colour, the component containing (p) contains
neither (q) nor (x_a).  Switch that component and give (v) the new colour
of (p).  The boundary now has the two independent pairs
(\{v,p\}) and (\{q,x_a\}).  The normalization on the remaining three
roots is exactly Theorem 2.1: a disconnected candidate support gives the
third pair, while two connected supports give its rooted-triangle outcome.
The argument is symmetric in (p,q).

If neither switch is possible, neither (p) nor (q) is a singleton block
of the component partition on these three same-colour vertices.  The only
set partitions of three labelled vertices with that property are the one
block partition and (pq\mid x_a), proving (4.2). \(\square\)

The triple lock is a minimal genuine state obstruction.  It does not
follow from the boundary graph: the boundary always has many matchings of
nonedges.  What fails is the ability to split one member of a repeated
three-vertex colour block by a shore-local Kempe switch.  Eliminating it
requires a component-splitting minor transition, a portal peel, or a
three-terminal web theorem; none of those follows from abstract colour
saturation alone.

## 5. Boundary-only sanity check

For completeness, the six vertices (X\cup\{p,q\}) can fail to have a
perfect matching of nonedges in only one maximal boundary pattern, up to
the automorphisms of (2K_2) and interchange of (p,q):

* (p,q) have the distinct colours of the endpoints of one literal edge
  of (G[X]);
* (pq) is an edge; and
* both (p) and (q) are adjacent to both endpoints of the other literal
  edge.

Every no-matching subpattern is contained in this pattern.  The
dependency-free verifier is `gate_core_boundary_matching_probe.py`.
This is not an obstruction to a mode on all seven cut vertices, because
(v) may be paired with (p) or (q).  It is recorded to prevent an invalid
argument which keeps (v) singleton and assumes a perfect nonedge matching
on the other six vertices.

## 6. Net reduction

The adhesion placements are now reduced as follows.

* Both (p,q) gate-coloured: normalized by
  `hadwiger_gate_pairmode_all_gate_placements.md`.
* Exactly one gate-coloured: a proper pair mode or one shore-local rooted
  triangle.
* Pure core, distinct colours: a proper pair mode, a rooted triangle, two
  disjoint carriers, or a bare four-terminal web.
* Pure core, one colour: the same outcomes or the explicit triple lock
  (4.2).

The remaining objects are structural and label-free: a triangle frame, a
two-demand web, or a three-terminal component lock.  No further raw
boundary adjacency enumeration is needed.

## 7. Atomic descent forces the pure, distinct-colour placement

The unique-portal descent in
`hadwiger_two_path_capacity_state_web_exchange.md` makes the preceding
classification substantially sharper at an atomic gate.

### Theorem 7.1 (singleton gate shore is pure-core and split-colour)

If the (K_0)-shore is the singleton (C_0=\{0\}), then

\[
 p,q\in J,\qquad pq\in E(G),\qquad c(p)\ne c(q). \tag{7.1}
\]

Consequently the same-core-colour triple lock of Theorem 4.1 cannot occur
at the terminal singleton of the exact-cut descent.

#### Proof

Fullness at the exact cut gives

\[
                         N_G(0)=L.
\]

In particular (0p,0q\in E(G)).  Since (c(0)=\alpha), properness excludes
colour (\alpha) at (p,q).  If, say, (p) had the other gate colour
(\beta), then the bichromatic edge (0p) would put (p) in the same
(\alpha,\beta)-component as (0), namely (K_0).  This contradicts the
Menger construction, in which (p,q\notin K_0\cup K_{56}).  Thus both
(p,q) use core colours, proving (p,q\in J).

The re-rooted vertex (0) has degree seven.  Dirac's neighbourhood bound
for the seven-contraction-critical graph gives

\[
                         \alpha(G[N(0)])\le2.
\]

The vertices (v,p,q) all lie in (N(0)), while (vp,vq\notin E(G)).  Hence
(pq) must be an edge, or these three vertices would be independent.
Finally two equally coloured vertices cannot be adjacent in the proper
colouring (c), so (c(p)\ne c(q)). \(\square\)

Thus repeated descent does not leave all four placement families alive.
At its singleton endpoint only the distinct-colour branch of Theorem 3.1
survives.  The remaining finite datum is whether those two core colours
are the endpoints of a literal edge (12 or 34) or a missing cross-edge;
the gate-colour and triple-lock branches disappear automatically.

### Corollary 7.2 (clique frame or crossed frame)

Let (M_a) be the one of the two literal edges (x_1x_2,x_3x_4)
containing the core-colour mate (x_a) of (p), and define (M_b)
similarly for (q).  Then

\[
 N_X^c(p)\subseteq V(M_a),\qquad
 N_X^c(q)\subseteq V(M_b).                        \tag{7.2}
\]

Consequently:

1. if (M_a=M_b), the four vertices consisting of (p,q) and the
   endpoints of the other literal edge induce a (K_4); and
2. if (M_a\ne M_b), each of (p,q) is complete to the literal edge
   opposite its own colour mate.  This is exactly the crossed-frame
   geometry.

#### Proof

Suppose (p) missed both endpoints of one of the missing cross-edges of
(G[X]).  Those two endpoints and (p) would be an independent triple in
(N(0)), contradicting (\alpha(G[N(0)])\le2).  Thus the set of roots
missed by (p) is a clique in (G[X]).  It contains (x_a), because they
have one colour.  The only cliques of (2K_2) containing (x_a) lie in
the literal edge (M_a), proving the first inclusion; the argument for
(q) is identical.

If (M_a=M_b), both vertices are complete to the opposite literal edge,
and they are adjacent to one another by Theorem 7.1.  Together with that
opposite edge they induce (K_4).  If the mate edges differ, (7.2) says
precisely that each of (p,q) is complete to the edge not containing its
mate. \(\square\)

Thus the terminal exact-cut recursion has only two local geometries, not
an arbitrary pure-core placement: a literal boundary (K_4), or the
crossed frame already isolated in the sole-exterior programme.
