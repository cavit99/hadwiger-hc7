# Protected tree carriers: the exact order-four threshold

## 1. Inverse size of a contracted Menger certificate

Let `H` be four-connected, let `T` contain four vertices, and let
`C_1,...,C_4` be pairwise disjoint connected protected carriers disjoint
from `T`.  Contract `C_i` to `c_i`, and suppose the contracted graph has
no four-linkage from `{c_1,...,c_4}` to `T`.

Menger supplies a separator `Z` of order at most three in the contracted
graph.  Put

\[
 I=\{i:c_i in Z\},\qquad r=|Z-\{c_1,c_2,c_3,c_4\}|.             \tag{1.1}
\]

### Lemma 1.1 (warehouse-size identity)

The full inverse image

\[
 Z^uparrow=(Z-\{c_1,c_2,c_3,c_4\})
             union\bigcup_{i in I}C_i                           \tag{1.2}
\]

is a separator of `H` of order

\[
                  |Z^uparrow|=r+\sum_{i in I}|C_i|.             \tag{1.3}
\]

Consequently `|Z^uparrow|>=4`.  It gives an exact order-four adhesion
precisely when the right side of (1.3) is four; after restoring a
disjoint neutral triangle `Q`, precisely this case gives an exact
order-seven adhesion.

#### Proof

Every path in `H-Z^uparrow` contracts to a path avoiding `Z`, so the two
Menger sides remain separated.  The carriers are pairwise disjoint and
disjoint from the ordinary vertices of `Z`, giving (1.3).
Four-connectivity excludes a separator of order at most three.  If the
order is four, no proper subset separates, again by four-connectivity,
so the cut is exact.  Restoring `Q` adds three vertices.  QED.

Nothing in (1.3) depends on whether the protected carriers are paths,
trees, or highly connected graphs.  Tree structure helps only if it
permits a state-preserving split of a carrier; minimality of the tree by
itself does not do so.

## 2. The path threshold is sharp

For `ell>=4`, let `C=c_1...c_ell` be a path and let

\[
               X=\{a_1,a_2,a_3,t_1,t_2,t_3,t_4\}
\]

be an independent set.  Join every vertex of `C` to every vertex of
`X`, and add no other edges.  Write

\[
                         H_ell=P_ell vee \overline{K_7}.         \tag{2.1}
\]

Use protected carriers

\[
 C_i=\{a_i\}\quad(1<=i<=3),\qquad C_4=C,                       \tag{2.2}
\]

and target set `T={t_1,t_2,t_3,t_4}`.

### Proposition 2.1 (minimal-path warehouse)

For `ell=5`, the graph `H_5` has all of the following properties.

1. It is five-connected and `K_7`-minor-free.
2. The four unprotected source representatives have a four-linkage to
   `T`.
3. There is no protected column system containing the four sets in
   (2.2).
4. It has no separator of order four.
5. The path `C` can be made the unique inclusion-minimal carrier of four
   named portal rows.

#### Proof

The set `C` is a five-vertex cut.  Deleting fewer than five vertices
leaves at least one vertex of `C` and at least one vertex of `X`; the
surviving outside vertex joins all surviving path vertices, while a
surviving path vertex joins every surviving outside vertex.  Hence the
remainder is connected and `kappa(H_5)=5`.

There is a tree decomposition with central bag `C` and, for every
`x in X`, one leaf bag `C union {x}`.  Its width is five.  Since
`tw(K_7)=6` and treewidth is minor-monotone, `H_5` has no `K_7` minor.

If only one representative of the protected path is retained, the four
paths

\[
 a_1c_1t_1,\quad a_2c_2t_2,\quad a_3c_3t_3,\quad c_4t_4          \tag{2.3}
\]

are pairwise disjoint.  Thus the ordinary/gammoid linkage rank is four.

But a protected bag containing `C_4` contains every vertex of `C`.
Every path from an `a_i` to any target meets `C`, because `X` is
independent.  No other protected bag can therefore reach a target
disjointly from the `C_4` bag.  This proves item 3.  Item 4 follows from
five-connectivity.

Finally prescribe four portal rows with their occurrences

\[
                         {c_1},\ {c_2},\ {c_4},\ {c_5}.          \tag{2.4}
\]

Any connected subgraph meeting all four rows contains the unique
`c_1`--`c_5` path, namely all of `C`.  Hence `C` is the unique minimal
state carrier for these rows.  QED.

For comparison, the same construction with `ell=4` has `C=P_4` as an
exact order-four cut.  It therefore lands in the exact-seven adhesion
after adding `Q`, exactly at the equality case of Lemma 1.1.  Increasing
the minimal path by one vertex is enough to leave that equality cell.

### Proposition 2.2 (a nontrivial exterior edge closes the full join)

Let `C` and `X` be disjoint sets of orders `m` and `m+2`, with every
`C`--`X` edge present.  If `G[X]` has an edge, then `G[C union X]`
contains a `K_{m+2}` minor.

#### Proof

Let `uv` be an edge of `G[X]`, write

\[
                  X-{u,v}=\{x_1,\ldots,x_m\},
       \qquad C=\{c_1,\ldots,c_m\},
\]

and use the seven bags

\[
                    \{c_i,x_i\}\ (1<=i<=m),\qquad
                    \{u\},\ \{v\}.                              \tag{2.5}
\]

Every two-vertex bag is connected.  Two such bags are adjacent through
either cross edge `c_ix_j`; each sees `u` and `v` through `c_i`; and the
last two bags see one another through `uv`.  QED.

Thus, at `m=5`, the independent exterior in Proposition 2.1 is forced in
the complete-contact version of any target-free five-vertex warehouse.  In
a vertex-critical host, identical exterior neighbourhoods are then
impossible.  Private distinguishing neighbours must leave the displayed
full join, locating exactly where an operation-sensitive bypass has to
start.

### Theorem 2.3 (connected exterior closes the complete warehouse)

Let `C` and `X` be disjoint sets of orders `m` and `m+2`, with every
`C`--`X` edge present.  If one component of `G-C` contains two vertices
of `X`, then `G` contains a `K_{m+2}` minor.  Consequently every
`(m+1)`-connected graph containing `K_{m,m+2}` as a subgraph contains a
`K_{m+2}` minor.

#### Proof

Inside a component of `G-C` containing at least two vertices of `X`,
choose an `X`--`X` path `P` with the fewest edges.  Its ends, say `u,v`,
belong to `X`, while its internal vertices avoid `X`; otherwise a
subpath between consecutive occurrences of `X` would be shorter.

Write `X-{u,v}={x_1,...,x_m}` and `C={c_1,...,c_m}`.  The `m` sets

\[
                             D_i=\{c_i,x_i\}
\]

are connected and pairwise adjacent: `c_ix_j` joins `D_i` to `D_j`.
Split the path `P` at any one of its edges into two nonempty connected
adjacent sets `R,S`, with `u in R` and `v in S`.  Both are disjoint from
all `D_i`.  The endpoint `u` is adjacent to every `c_i`, so `R` sees
every `D_i`; the endpoint `v` gives the same statement for `S`.
Therefore

\[
                         D_1,\ldots,D_m,R,S
\]

are `m+2` disjoint connected pairwise adjacent bags.

If `G` is `(m+1)`-connected, deletion of the `m` vertices of `C` leaves
`G-C` connected, so the first assertion applies.  QED.

At `m=5`, this eliminates the complete-contact five-vertex warehouse in
the actual seven-connected host outright.  The five-connected example
`H_5` survives only because deleting its path leaves seven isolated
targets.  The remaining HC7 warehouse problem can therefore involve
only **collective** carrier-to-target contacts, not complete bipartite
contact.

## 3. Consequence for the state-forcing programme

The following implication is false, even with stronger connectivity
than currently available and with target-minor exclusion:

\[
 \begin{array}{c}
 H\text{ four-connected and }K_7\text{-minor-free},\\
 \text{every protected state carrier is a tree}
 \end{array}
 \quad\Longrightarrow\quad
 \begin{array}{c}
 \text{four protected columns, or}\\
 \text{an exact order-four cut.}
 \end{array}                                                     \tag{3.1}
\]

The obstruction in `H_5` is still static: the seven outside vertices
are false twins, so it cannot occur unchanged in a vertex-critical host.
Critical anti-domination forces private distinguishing contacts.  What
must now be proved is not a tree-splitting lemma, but an
**operation-sensitive warehouse bypass**: those private contacts either
leave the large minimal tree on four disjoint routes, or their failure
has one common exact boundary extension state.  Path/tree minimality
alone supplies neither conclusion.
