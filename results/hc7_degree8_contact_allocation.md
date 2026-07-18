# Contact allocation at a degree-eight vertex

**Status:** written proof; separate internal audit.

This note isolates a local branch-set construction used in the
degree-eight equality case.  The construction is unbounded: the component
outside the closed neighbourhood may have arbitrary order.  It uses only
its literal neighbourhood, not a quotient graph or a virtual edge of a
plane completion.

## 1. Setup

Let `G` be a graph, let `v` be a vertex of degree eight, and write

\[
             N_G(v)=B\mathbin{\dot\cup}C,
             \qquad |B|=3,\quad |C|=5.                 \tag{1.1}
\]

Let `D` be a connected component of `G-N_G[v]`, and put

\[
                         S=N_G(D)\subseteq B\cup C.      \tag{1.2}
\]

Assume

\[
       |S|\ge 7,
       \qquad \alpha\bigl(G[B\cup C]\bigr)\le 3.       \tag{1.3}
\]

When `G` is seven-connected and `D` is nonempty, the first inequality in
(1.3) is automatic.  The proof below needs only the literal hypotheses
(1.1)--(1.3).

## 2. Complete adjacency between the two parts

### Theorem 2.1

Under the setup of Section 1, suppose every vertex of `B` is adjacent to
every vertex of `C`.  Then `G` contains a `K_7` minor.

### Proof

Since `|B|=3` and `|S|>=7`, at least four vertices of `C` belong to `S`.
The independence bound in (1.3) therefore gives an edge

\[
                         xy\in E\bigl(G[C\cap S]\bigr). \tag{2.1}
\]

Choose `b in B cap S` and write `B-{b}={b_0,b_1}`.  Of the three
vertices in `C-{x,y}`, at least one belongs to `S`; call one such vertex
`z` and call the other two `r_0,r_1`.  Relabel `r_0,r_1` arbitrarily.

Consider the six sets

\[
 \{x\},\quad \{y\},\quad \{b\},\quad
 \{v,z\},\quad \{b_0,r_0\},\quad \{b_1,r_1\}.          \tag{2.2}
\]

They are pairwise disjoint.  Each is connected: `v` is adjacent to `z`,
and `b_i` is adjacent to `r_i`.  They are pairwise adjacent.  Indeed,
`xy` supplies the only adjacency between the first two singleton sets;
all adjacencies involving one vertex in `B` and one in `C` are present;
`v` is adjacent to every member of `B union C`; and the two last sets are
adjacent through, for example, the edge `b_0r_1`.

Every set in (2.2) meets `S`.  This is explicit for the first four.  Each
of the last two has order two, while at most one vertex of `B union C` is
outside `S`, so neither last set can avoid `S`.

The component `D` is connected and is adjacent to every set in (2.2),
because each of those sets meets `N_G(D)=S`.  Thus `D` together with the
six sets in (2.2) is an explicit `K_7`-minor model.  \(\square\)

Theorem 2.1 does not require a cycle or any other prescribed edge in
`G[C]`; the independence bound supplies the only edge of `G[C]` used by
the construction.

## 3. One missing adjacency

### Theorem 3.1

Retain the setup of Section 1.  Suppose there are vertices `b_0 in B` and
`c_0 in C` such that every `B`--`C` edge is present except possibly
`b_0c_0`.  If

\[
            G\bigl[(C\cap S)-\{c_0\}\bigr]
            \text{ contains an edge},                  \tag{3.1}
\]

then `G` contains a `K_7` minor.

### Proof

Choose an edge `xy` in (3.1).  At most one vertex of `B union C` is
outside `S`, so one may choose

\[
                 b\in (B-\{b_0\})\cap S.               \tag{3.2}
\]

Write `B-{b}={b_0,b_1}`.  The set `C-{x,y}` consists of `c_0` and two
other vertices.  Choose distinct names `z,r_0,r_1` for these three
vertices so that

\[
                         z\in S,
              \qquad    r_0\ne c_0.                    \tag{3.3}
\]

Such a choice always exists.  If `c_0` is the unique vertex missed by
`S`, both other vertices are available, one for `z` and one for `r_0`.
Otherwise `c_0` belongs to `S`; choose it as `z` if necessary, and choose
`r_0` among the two other vertices.

Use the six sets displayed in (2.2), with these choices.  The set
`{b_0,r_0}` is connected because `r_0!=c_0`.  Both `x` and `y` avoid
`c_0`, so they are adjacent to `b_0`.  The vertices `b` and `b_1` are
adjacent to every vertex of `C`, and the two last sets are adjacent through
`b_1r_0`.  These observations, together with the universal adjacency of
`v` inside its closed neighbourhood and the edge `xy`, verify every
pairwise adjacency among the six sets.

They all meet `S` for the same reason as in Theorem 2.1: the four
designated sets contain `x,y,b,z in S`, and at most one vertex of the whole
neighbourhood lies outside `S`.  Appending `D` again gives an explicit
`K_7`-minor model.  \(\square\)

### Corollary 3.2

Under the hypotheses of Theorem 3.1, condition (3.1) is automatic if
`G[C]` contains a cycle through all five vertices of `C`.  Consequently,
the conclusion holds when `C` contains a spanning `5`-cycle and at most
one `B`--`C` edge is absent.

### Proof

Deleting `c_0` from the spanning `5`-cycle leaves a path on four vertices.
At most one further vertex of that path is outside `S`.  Removing at most
one vertex from a four-vertex path leaves an edge, which proves (3.1).
\(\square\)

## 4. A spanning five-cycle and two independent missing adjacencies

The one-missing-edge argument extends to two missing adjacencies provided
that they do not share an endpoint.  No edge inside `B` is required.

### Theorem 4.1

Retain the setup of Section 1, but do not assume the independence bound in
(1.3).  Suppose that `G[C]` contains a spanning cycle and that the set

\[
       (B\times C)-E(G)
\]

is a matching of order at most two.  Then `G` contains a `K_7` minor.

### Proof

Fix a literal spanning cycle and write it as

\[
                         c_0c_1c_2c_3c_4c_0.           \tag{4.1}
\]

Since `|S|>=7`, either every vertex of `B union C` belongs to `S`, or
there is a unique vertex `o` outside `S`.

It is enough to treat exactly two missing `B`--`C` edges.  Indeed, a
matching of order zero or one can be extended to a matching of order two
by deleting one or two additional `B`--`C` edges.  A minor model in the
resulting spanning subgraph is also a minor model in `G`.

Relabel `B={b_0,b_1,b_2}`.  Up to a permutation of `B` and a dihedral
symmetry of the cycle, the two absent edges have one of the forms

\[
 \begin{split}
   M_A&=\{b_0c_0,b_1c_1\},\\
   M_D&=\{b_0c_0,b_1c_2\}.
 \end{split}                                             \tag{4.2}
\]

These are the cases in which the two endpoints in `C` are adjacent or at
distance two, respectively.

For compactness, write

\[
 [h;x;yz;pr,qt]                                           \tag{4.3}
\]

for the following six branch sets:

\[
 \{b_h\},\quad \{v,c_x\},\quad \{c_y\},\quad \{c_z\},
 \quad \{b_p,c_r\},\quad \{b_q,c_t\}.                  \tag{4.4}
\]

The table gives a choice for every orbit of the possible omitted vertex.
An entry containing several choices of `o` applies to each of them.
Choices not displayed separately are obtained by the symmetry of the
corresponding line of (4.2).

\[
\begin{array}{c|c|c}
\text{missing edges}&o&\text{choice in the notation (4.3)}\\ \hline
M_A&\varnothing\ \text{or }b_2 &[0;0;23;14,21]\\
   &b_0\ \text{or }c_0 &[1;1;23;04,20]\\
   &c_2 &[0;0;34;12,21]\\
   &c_3 &[2;2;04;01,13]\\ \hline
M_D&\varnothing,\ b_2,\ c_3,\ \text{or }c_4
       &[0;0;12;13,24]\\
   &b_0 &[1;2;01;04,23]\\
   &c_0 &[1;2;34;01,20]\\
   &c_1 &[0;0;23;11,24]
\end{array}                                               \tag{4.5}
\]

For `M_A`, the unlisted vertices `b_1,c_1,c_4` are symmetric to
`b_0,c_0,c_2`, respectively.  For `M_D`, the unlisted vertices `b_1,c_2`
are symmetric to `b_0,c_0`, respectively, and `c_3,c_4` form one orbit.
Thus (4.5) is exhaustive.

We verify what the table records.  In every entry, `c_yc_z` is an edge of
the cycle, both two-vertex sets in (4.4) use present `B`--`C` edges, and
the six sets are pairwise adjacent using only the cycle edges and the
present `B`--`C` edges.  This is a direct check against the two edges in
(4.2); in particular, no adjacency inside `B` is used.  The set
`{v,c_x}` is connected and adjacent to all five other sets through `v`.

The six sets partition `\{v\}\cup B\cup C`.  When `o` exists, the table
places it in one of the two-vertex `B`--`C` branch sets, never in
`\{b_h\}`, `\{v,c_x\}`, `\{c_y\}`, or `\{c_z\}`.  Consequently every
set in (4.4) meets `S`.

Finally, `D` is connected and is adjacent to every set in (4.4), because
each of them meets `S=N_G(D)`.  Appending `D` therefore gives seven
pairwise adjacent connected branch sets, and hence a `K_7` minor in `G`.
\(\square\)

Extra edges inside `B`, chords of the cycle, and additional `B`--`C`
edges only preserve the displayed models.

The same table applies when the five cyclic vertices are replaced by five
connected branch sets.  This is the form needed when consecutive neighbours
of `v` are joined by arcs of a facial boundary rather than by edges.

### Theorem 4.2 (cyclic connected-set form)

Let the singleton `\{v\}` and the following nine sets be pairwise disjoint:

\[
             \{b_0\},\{b_1\},\{b_2\},
             C_0,C_1,C_2,C_3,C_4,\quad D.               \tag{4.6}
\]

Assume:

1. `D` and every `C_i` are connected;
2. each `C_i` contains a specified vertex `c_i` adjacent to `v`, and
   each `b_j` is adjacent to `v`;
3. `C_i` is adjacent to `C_{i+1}` for every index modulo five;
4. among the fifteen pairs `(b_j,C_i)`, at most two are nonadjacent, and
   those nonadjacent pairs have distinct `b_j`- and `C_i`-indices.

Record the contacts of `D` on the eight labels by

\[
 S^*=\{b_j:N_G(D)\cap\{b_j\}\ne\varnothing\}
      \mathbin{\cup}
      \{c_i:N_G(D)\cap C_i\ne\varnothing\}.             \tag{4.7}
\]

If `|S^*|>=7`, then `G` contains a `K_7` minor.

### Proof

Apply the table (4.5) to the abstract cycle with vertices
`c_0,...,c_4`, interpreting adjacency between `b_j` and `c_i` as
adjacency between `b_j` and `C_i`.  In every displayed branch set, replace
`c_i` by the whole connected set `C_i`.  Thus, for example,

\[
       \{v,c_x\}\longmapsto \{v\}\cup C_x,
       \qquad
       \{b_p,c_r\}\longmapsto \{b_p\}\cup C_r.          \tag{4.8}
\]

The six resulting sets are pairwise disjoint and connected.  Every
adjacency checked in Theorem 4.1 remains valid: a cycle edge is replaced
by an edge between consecutive `C_i`, and a cross-edge is replaced by an
edge from `b_j` to `C_i`.  The branch set containing `v` is adjacent to
every other branch set because each contains either a neighbour `b_j` or
one of the specified neighbours `c_i` of `v`.

If one label is absent from `S^*`, the table places that label in a branch
set with a second label that belongs to `S^*`.  By (4.7), the corresponding
expanded branch set is therefore adjacent to `D`.  Every one of the six
expanded branch sets is adjacent to `D`, so appending `D` gives a
`K_7`-minor model.  \(\square\)

### Corollary 4.3 (a genuine facial boundary supplies the cyclic sets)

Let `H` be a three-connected plane graph and let `v` have degree five in
`H`, with neighbours `c_0,...,c_4` in their cyclic order around `v`.
Then `H-v` is two-connected.  The face created by deleting `v` has a
boundary cycle containing `c_0,...,c_4` in this order, and the vertices of
that cycle can be partitioned into five connected sets
`C_0,...,C_4` such that `c_i in C_i` and consecutive sets are adjacent.

Consequently, Theorem 4.2 applies whenever this boundary cycle is disjoint
from the chosen set `D` and from `B={b_0,b_1,b_2}`, and its remaining
incidence and contact hypotheses hold.

### Proof

For every vertex `x` of `H-v`, the graph

\[
                         H-\{v,x\}
\]

is connected by three-connectivity.  Hence `H-v` is two-connected.  Every
face boundary in a two-connected plane graph is a cycle.  Deleting `v`
merges the faces incident with `v`, and the boundary of the resulting face
contains the five neighbours in their cyclic order.

For each `i`, take the boundary arc from `c_i` towards `c_{i+1}`, include
`c_i` and all its internal vertices in `C_i`, and leave `c_{i+1}` for
`C_{i+1}`.  These five sets partition the boundary cycle, are connected,
and consecutive sets share a boundary edge.  The last assertion is now
Theorem 4.2.  \(\square\)

The disjointness condition in Corollary 4.3 is essential to this deduction.
The facial boundary in `H-v` may contain vertices outside `N_H[v]`; in a
host application some of them could lie in the proposed seventh branch set
`D`.  The corollary does not assert that such an overlap can be removed.  It
applies only when this facial cycle avoids `D`, or when another connected
set supplying the contacts in (4.7) remains disjoint from it.

## 5. The allocation criterion and trust boundary

The proofs use the following small matching principle.  First choose an
edge `xy` of `G[C]` with both endpoints in `S` and a vertex
`b in B cap S`.  Of the three remaining vertices of `C`, assign one vertex
`z in S` to the branch set containing `v`, and assign the other two
injectively to the two
vertices of `B-{b}`.  The assignment is valid when its two assigned pairs
are edges, the two resulting pair-bags are adjacent, both are adjacent to
`x` and `y`, and `b` is adjacent to `x`, to `y`, and to both pair-bags.
The six sets in (2.2) then give the required local model.
Theorems 2.1, 3.1, 4.1, and 4.2 give hypotheses under which this compatible
assignment is forced.  Theorem 4.1 is the sharpest of them for a literal
spanning five-cycle: two missing cross-edges are allowed when their set is
a matching.  Theorem 4.2 permits the cycle vertices to be expanded into
disjoint connected sets while retaining the same labelled incidence data.

The result does **not** prove that the missing `B`--`C` edges form a matching
of order at most two from curvature, contraction-criticality, or
seven-connectivity.  Corollary 4.3 uses a genuine facial boundary cycle,
not a virtual edge of a plane completion, and it requires that cycle to be
disjoint from the seventh branch set.  A sharp local obstruction to a
stronger inference is recorded in
[`hc7_degree8_contact_allocation_barrier.md`](../barriers/hc7_degree8_contact_allocation_barrier.md).

The next host-level problem is therefore to show that the degree-eight
equality case supplies a compatible allocation of this kind, or else that
failure exposes an order-seven separation whose two closed sides have
compatible six-colourings.
