# Binary transition trees: a full-bag collapse without a list core

## 1. Purpose

The matched-list analysis gives named colours and local saturation, but it
requires the selected transit tree to be the whole minimal expansion core.
The following theorem removes that hypothesis from the geometric part of
the argument.  It uses only the two possible marked states on a singleton
adhesion.

For an arbitrary spanning tree of a branch bag, every edge-deletion witness
has one bit: its defect colour is either the apex colour or it is not.  Two
incident lobes with the same bit either splice to colour the original graph,
or have an ambient bypass.  Consequently every rotation-rigid,
foreign-transit-free branch tree is a path and its bits alternate.

This does not by itself give the portal saturation of a matched list core.
Its value is that portal-bearing parts outside a minimal core no longer
create arbitrary tree geometry: they are absorbed into one binary owner
corridor.

## 2. Setup and the edge bit

Let (r\ge2).  Let (G) be non-(r)-colourable and suppose that every
proper minor of (G) is (r)-colourable.  Fix (v\in V(G)), put

\[
                              H=G-v,
\]

and let (T) be a tree subgraph of (H).  In the model application (T)
is a spanning tree of one branch bag of a fixed clique model.

For each edge (e=xy\in E(T)), choose an (r)-colouring (c_e) of
(G-e).  Necessarily

\[
                              c_e(x)=c_e(y),             \tag{2.1}
\]

since otherwise (c_e) would already colour (G).  Define

\[
 \tau(e)=
 \begin{cases}
  1,&c_e(x)=c_e(v),\\
  0,&c_e(x)\ne c_e(v).
 \end{cases}                                             \tag{2.2}
\]

The choice of (c_e) need not be canonical.  The theorem below holds for
every independent choice of one witness per edge.

## 3. The binary lobe theorem

### Lemma 3.1 (equal-bit incident lobes bypass)

Let (e=qx) and (f=qy) be distinct edges of (T) incident with (q).
Let (T_x,T_y) be the corresponding components of (T-q).  If

\[
                              \tau(e)=\tau(f),           \tag{3.1}
\]

then (T_x) and (T_y) lie in the same component of (H-q).

#### Proof

Suppose they lie in different components of (H-q).  Group the component
containing (T_x) on one side of a separation of (H) with adhesion
(\{q\}), and the component containing (T_y) on the other.  The edge
deletions (e,f) are supported on opposite boundary-anchored shores.

On the singleton adhesion there is only one equality partition.  Its
marked apex block is (\{q\}) exactly when the corresponding edge bit is
one, and is empty exactly when the bit is zero.  Equation (3.1) therefore
says that (c_e,c_f) induce the same marked state on (\{q\}).

Use (c_f) on the closed shore containing (e), and (c_e), after one
palette permutation, on the opposite closed shore.  The restrictions agree
at (q); the first colouring restores (e), the second restores (f),
and every other edge lies in an untouched closed shore.  This is a proper
(r)-colouring of (G), a contradiction.  Hence the two lobes lie in one
component of (H-q). \(\square\)

The proof is exactly the boundary-faithful crossed-minor theorem.  The fact
that each deleted edge is incident with the adhesion is harmless: deleting
(qx) does not delete any edge of the opposite closed shore.

### Lemma 3.2 (bypass, clean rotation, or named transit)

Under the hypotheses of Lemma 3.1, an (H-q) path joins the two lobes.
Relative to a fixed clique model containing (T) in one bag, a shortest
such path gives one of the following.

1. A (T)-path whose interior avoids every other branch bag.  Adding it to
   the transit bag and deleting an edge of the old tree interval is a clean
   label-preserving rotation.
2. A first hit in a named foreign branch bag.

#### Proof

Take a shortest lobe-to-lobe path in (H-q), and then a subpath between
two consecutive visits to (T).  Its interior avoids (T).  If it avoids
all foreign bags, its union with (T) has one cycle; delete an old tree
edge on that cycle.  The vertex set of every old portal and all old
interbag edges are retained.  Otherwise truncate at the first foreign-bag
vertex. \(\square\)

### Theorem 3.3 (global binary collapse)

For every choice of the edge witnesses (c_e), at least one of the
following holds.

1. The transit tree has a clean label-preserving rotation.
2. There is a named foreign-bag transit.
3. (T) is a path and its edge bits alternate:

   \[
                         0,1,0,1,\ldots
   \quad\hbox{or}\quad
                         1,0,1,0,\ldots .               \tag{3.2}
   \]

#### Proof

If a vertex (q) of (T) has degree at least three, two incident edges
have the same bit.  Lemmas 3.1 and 3.2 give outcome 1 or 2.  In their
absence, (\Delta(T)\le2), so the connected tree (T) is a path.

At an internal path vertex, two consecutive edges with the same bit again
invoke Lemmas 3.1 and 3.2.  Thus, in the absence of the first two outcomes,
every consecutive pair has different bits, which is (3.2). \(\square\)

## 4. Relation to the matched-core theorem

When (T) is the whole matched list core, the named edge labels refine the
binary bit.  The old alpha/delta theorem identifies the alternating residue
as

\[
                         \alpha,\delta,\alpha,\delta,
                         \ldots,\alpha,
\]

and supplies exact expansion lists.  Theorem 3.3 is weaker in colour
content but stronger in scope: (T) may be an arbitrary spanning tree of
the whole branch bag, including every portal-bearing lobe outside a
minimal list core.

Thus the former **core exchange** problem splits into two precise tasks.

1. The geometric tree cannot branch or have a nonalternating edge-state
   sequence without producing a rotation/transit.
2. On the surviving binary path, one must recover enough colour/portal
   capacity from the pinned and unpinned edge witnesses to build the rooted
   model or a colour-gluable adhesion.

The second task is still open.  In particular, the bit sequence alone does
not imply the matched expansion lists, and no such implication is used
here.

## 5. Audit boundaries

* The theorem uses one colouring of (G-e) for every tree edge; it does
  not assume those colourings agree away from (T).
* Equality of bits is enough only because the adhesion is a singleton.
  For a larger adhesion, the full equality partition must be compared.
* A clean rotation is an actual model move, but a global potential is still
  needed to prove that repeated rotations terminate inside a class where
  the desired colour-capacity information is retained.
* A named foreign transit is not silently absorbed through another branch
  bag.  It is the input to the Hall collision-carrier descent.

