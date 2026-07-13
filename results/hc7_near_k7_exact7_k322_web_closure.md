# Complete unbounded closure of the sharp `K3+2K2` full-shore core

## Theorem

### Theorem 1 (full `K_{3,2,2}` web closure)

Let `G` be a seven-connected graph and let

\[
 S=\{0,1,2,3,4,5,6\},
 \qquad
 E(\overline{G[S]})=\{01,02,12,34,56\}.             \tag{1}
\]

Thus `G[S]=K_{3,2,2}`, with independent parts
`{0,1,2}`, `{3,4}`, and `{5,6}`.  Suppose `G-S` has exactly two
components `D_1,D_2` and

\[
 N(D_1)=N(D_2)=S.                                   \tag{2}
\]

Then `G` contains a `K_7` minor or `G` is six-colourable.  Consequently
this sharp full-shore core cannot occur in a proper-minor-minimal
counterexample to `HC_7`.

## Proof

For `j in {1,2}` and `i in {1,2,3,4}`, put

\[
 P_i^j=N_{D_j}(i).
\]

Every portal set is nonempty by (2).  Form an auxiliary graph `A_j`
from `G[D_j]` by adding four independent terminals, with `t_i` adjacent
precisely to `P_i^j`.  Order them as

\[
 T=(t_1,t_3,t_2,t_4).                               \tag{3}
\]

### Claim 1: a crossed terminal tuple gives a `K_7` minor

A crossing of the four-term tuple (3) consists of vertex-disjoint paths
from `t_1` to `t_2` and from `t_3` to `t_4`.  Delete their artificial
terminal ends.  Their remaining vertex sets are disjoint connected sets
`X,Y subseteq D_j`, where `X` meets both `P_1^j,P_2^j` and `Y` meets
both `P_3^j,P_4^j`.

Let `k=3-j`.  The following seven sets are pairwise disjoint branch
sets:

\[
 \{1\},\quad \{3\},\quad \{5\},\quad D_k,\quad
 \{0,6\},\quad X\cup\{2\},\quad Y\cup\{4\}.        \tag{4}
\]

They are connected: `06` is an edge of `G[S]`, and the last two sets
are joined to their roots through their corresponding portal contacts.
The four sets

\[
 \{1\},\quad\{3\},\quad\{5\},\quad\{0,6\}
\]

are pairwise adjacent.  For the last of them, use respectively the
edges `61`, `03`, and `05`.  The `X cup {2}` bag sees `{1}` through its
`P_1^j` contact, and sees `{3}`, `{5}`, and `{0,6}` through the boundary
edges `23`, `25`, and `26`.  Symmetrically, the `Y cup {4}` bag sees
`{3}` through its `P_3^j` contact, and sees `{1}`, `{5}`, and `{0,6}`
through `41`, `45`, and `40`.  The two bags see one another through the
boundary edge `24`.  Finally the full connected shore `D_k` sees every
other bag through its boundary vertex.  Hence (4) is a `K_7` model.

### Claim 2: in the crossless case each shore is a bare planar rib

Assume that `G` has no `K_7` minor.  By Claim 1, (3) is crossless in
both auxiliary graphs.  Add edges on the fixed vertex set of `A_j`
until the tuple is maximally crossless.  The generalized Two Paths
Theorem (Humeau--Pous, Theorem 1.5) says that the resulting same-vertex
edge-supergraph is a `4`-web `W_j` with frame (3).  Let `R_j` be its
planar rib.

Suppose a nonempty clique `X subseteq D_j` is inserted in a facial
triangle `F` of `R_j`.  Every neighbour of `X` represented in `A_j`
lies in `F`.  Replace a terminal `t_i` in `F` by the corresponding
boundary vertex `i`, and fix every shore vertex of `F`; the image
`\widehat F` has order at most three and accounts for all neighbours of
`X` in `D_j cup {1,2,3,4}`.  The two shores are anticomplete, so the only
other possible neighbours in the original graph are the three omitted
boundary vertices `0,5,6`.  Therefore

\[
 N_G(X)\subseteq \widehat F\cup\{0,5,6\},
 \qquad |N_G(X)|\le6.                               \tag{5}
\]

This set separates `X` from the nonempty opposite shore, contradicting
seven-connectivity.  Thus every shore vertex is a rib vertex.  Since
`A_j` is an edge-subgraph of `W_j`, all its edges between shore and frame
vertices lie in the planar rib.

Replace the four artificial terminals by `1,3,2,4` and include the frame
edges

\[
 13,32,24,41.
\]

These are precisely the four edges of `G[{1,2,3,4}]`.  Hence

\[
 G[D_j\cup\{1,2,3,4\}]
\]

has a plane embedding in a closed disk whose boundary is the cycle
`1-3-2-4-1`.

### Completion of the proof

Embed the two shore disks on opposite sides of their common boundary
cycle.  There are no edges between the shores, so they glue without
crossings.  Consequently

\[
 P:=G-\{0,5,6\}                                    \tag{6}
\]

is planar.  Give `P` four colours by the Four Color Theorem.  Give
vertex `0` a fifth colour and give both `5` and `6` a sixth colour.
The latter two vertices are nonadjacent by (1), while `0` has the other
new colour; both new colours are absent from `P`.  This is a
proper six-colouring of `G`.

Thus the crossless case is six-colourable, while Claim 1 supplies a
`K_7` minor in the crossed case.  This proves the theorem. \(\square\)

## Audit summary

The proof uses only a fixed four-terminal instance of the classical
Two Paths web theorem.  The terminal order was chosen so that its two
crossing pairs are exactly the missing pairs `12` and `34`; the unused
boundary pair `56` is repaired in the explicit model by the connected
bag `{0,6}`.  In the web alternative the three unused boundary vertices
are exactly the extra vertices in the cut bound (5), giving the sharp
order six contradiction to seven-connectivity.
