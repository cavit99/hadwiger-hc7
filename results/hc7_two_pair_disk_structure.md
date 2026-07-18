# Structural alternatives for an exact seven-separation with two paired traces

**Status:** written proof; separate internal audit.  The results are
unbounded and use literal branch sets and vertices.  They do not prove
`HC_7`: a full-neighbourhood separation returned below need not have order
seven or carry compatible colourings of its two closed sides.

## 1. Setup

Let `G` be a seven-connected graph and let

\[
       V(G)=L\mathbin{\dot\cup}T\mathbin{\dot\cup}R,
       \qquad E_G(L,R)=\varnothing,
       \qquad |T|=7,                                      \tag{1.1}
\]

where `L` and `R` are nonempty, `L` is connected, and

\[
                              N_G(L)=T.                  \tag{1.2}
\]

Let

\[
       I=\{i_0,i_1\},\qquad J=\{j_0,j_1\}                 \tag{1.3}
\]

be disjoint subsets of `T`.  Assume that

\[
                         H=G[L\cup I\cup J]               \tag{1.4}
\]

has a drawing in a closed disk in which the four nominated vertices occur
on the boundary in the cyclic order

\[
                         i_0,j_0,i_1,j_1,                 \tag{1.5}
\]

and every other vertex lies in the open disk.  This is the literal,
cell-free outcome of the Two Paths theorem; no auxiliary completion edge is
an edge of `G` unless it was already present.

Suppose also that `G[R\cup T]` contains five pairwise vertex-disjoint,
connected, pairwise adjacent subgraphs

\[
                         Q_I,Q_J,Q_1,Q_2,Q_3              \tag{1.6}
\]

such that

\[
                         Q_I\cap T=I,
             \qquad      Q_J\cap T=J.                    \tag{1.7}
\]

The three residual subgraphs may meet the remaining three boundary
vertices in any way allowed by their disjointness.  In the active
five-subgraph reflection application, two of those traces are singletons
and one is empty.

## 2. A rooted-model split gives a complete minor or a separation

### Theorem 2.1

Assume `|L|>=2`.  Then at least one of the following holds.

1. `G` contains a `K_7` minor.
2. For some `W in {Q_I,Q_J}` there is a nonempty proper connected set
   `A proper subset V(W)`, one of the rooted branch sets `B_r` in (2.4),
   and an index `k in {1,2,3}` such that

   \[
          X=B_r\cup A,\qquad X\cap T=\{r\},
          \qquad E_G(X,Q_k)=\varnothing.                 \tag{2.1}
   \]

   Both `A` and the label-preserving expanded set `X` are connected, and
   each gives a nontrivial full-neighbourhood separation

   \[
       (Y\cup N_G(Y),\;V(G)-Y),\qquad Y\in\{A,X\},        \tag{2.2}
   \]

   whose boundary has order at least seven.

### Proof

The closed-shore rooted-connectivity lemma says that

\[
                         (H,I\cup J)                       \tag{2.3}
\]

is internally four-connected.  Since `|L|>=2`, the graph `H` has at least
six vertices.  Jorgensen's rooted-minor lemma therefore gives four disjoint
connected branch sets

\[
               B_{i_0},B_{j_0},B_{i_1},B_{j_1}           \tag{2.4}
\]

rooted at the indicated vertices and having at least five of the six
possible pairwise adjacencies.

A rooted `K_4` model is impossible in the disk drawing: its adjacencies
between the two `I`-bags and between the two `J`-bags would contain two
vertex-disjoint paths joining alternating points of the boundary.  The
same argument shows that the unique nonrequired adjacency in (2.4) cannot
join consecutive vertices of (1.5).  If, for example, the
`B_{i_0}`--`B_{j_0}` adjacency were nonrequired, the required
`B_{i_0}`--`B_{i_1}` and `B_{j_0}`--`B_{j_1}` adjacencies would again give
two disjoint crossing paths.  Hence the nonrequired pair is either
`i_0i_1` or `j_0j_1`.  In particular, all four `I`--`J` branch-set
adjacencies are present.

Choose a spanning tree of `G[Q_I]`.  Delete an edge on its
`i_0`--`i_1` path and let `A_0,A_1` be the vertex sets of the two resulting
tree components, indexed by their roots.  They are nonempty, connected,
adjacent, disjoint, and partition `V(Q_I)`.  Apply the same construction to
`Q_J`, obtaining connected adjacent parts `D_0,D_1` rooted at `j_0,j_1`.

Form the four expanded rooted sets

\[
       B_{i_0}\cup A_0,\quad B_{i_1}\cup A_1,\quad
       B_{j_0}\cup D_0,\quad B_{j_1}\cup D_1.            \tag{2.5}
\]

They are pairwise disjoint: the four rooted bags lie in `H`, each tree part
meets `H` exactly in its nominated root, and the rooted bags are disjoint.
Each is connected and contains exactly its nominated vertex of `T`.

Suppose one expanded set `X=B_r\cup A` is anticomplete to some residual
subgraph `Q_k`, where `A` is the corresponding tree part.  Then `A` is
also anticomplete to `Q_k`.  For either `Y=A` or `Y=X`, the nonempty
subgraph `Q_k` lies in

\[
                         V(G)-(Y\cup N_G(Y)).             \tag{2.6}
\]

Both sets are nonempty and connected, and neither is all of `G`; hence
(2.2) gives two genuine nontrivial separations.  Seven-connectivity gives
`|N_G(Y)|>=7`, proving outcome 2.

It remains that every expanded set in (2.5) is adjacent to every residual
subgraph.  Use those four sets together with `Q_1,Q_2,Q_3`.  The two
tree-cut edges supply the within-`I` and within-`J` adjacencies, the rooted
model supplies all four cross adjacencies, the present assumption supplies
all adjacencies to a residual subgraph, and the residual subgraphs are
pairwise adjacent.  These seven sets are therefore an explicit
`K_7`-minor model.  \(\square\)

### Trust boundary for Theorem 2.1

The tree part `A` is strictly smaller than its old far-side subgraph, while
the expanded set `X` retains one nominated root and one missed residual
subgraph.  Neither certificate is yet an induction: its full neighbourhood
can have order greater than seven, can cut the old branch sets in new ways,
and need not retain both paired traces or a common boundary-colouring
partition.

## 3. Curvature forces a degree-seven or degree-eight vertex

### Theorem 3.1

Under the setup of Section 1, some vertex `v in L` satisfies

\[
                              7\le d_G(v)\le8.             \tag{3.1}
\]

If `d_G(v)=8`, then

\[
                d_H(v)=5,
       \qquad   T-(I\cup J)\subseteq N_G(v).              \tag{3.2}
\]

More precisely, either the disk has an interior vertex of completed degree
at most four, which has host degree seven, or it has at least two interior
vertices of completed degree five.  Every one of the latter having host
degree eight satisfies (3.2).

### Proof

Temporarily delete every literal edge of `H` joining consecutive roots in
(1.5).  This deletes no edge incident with `L`.  Draw four pairwise
internally disjoint arcs in the exterior of the remaining disk drawing,
one between each consecutive pair in (1.5), so that the arcs form a new
outer `4`-cycle through the roots and enclose the old drawing.  Regard
these arcs as virtual edges and triangulate every bounded face by adding
noncrossing edges between existing vertices.  No vertex is added.  Call
the resulting simple plane graph `H^+`.  Every vertex outside the four
roots lies inside its outer `4`-cycle, and every edge of `H` incident with
`L` remains an edge of `H^+`.

Each root has its two virtual cycle neighbours and, by `N_G(L)=T`, an
actual neighbour in `L`.
Thus every outer vertex has degree at least three in `H^+`.

Euler's formula for a triangulated disk with outer boundary of order four
gives

\[
 \sum_{x\in L}(6-d_{H^+}(x))
 +\sum_{x\in I\cup J}(4-d_{H^+}(x))=6.                  \tag{3.3}
\]

The second sum is at most four, so the first is at least two.  Hence some
interior vertex `v`, necessarily in `L`, has
`d_{H^+}(v)<=5`.  Since no edge incident with `L` was deleted,
`d_H(v)<=5`.  A vertex of `L` has no neighbour in `R`, and the only
vertices outside `H` to which it can be adjacent are the three vertices of
`T-(I\cup J)`.  Consequently

\[
                     d_G(v)\le d_H(v)+3\le8.             \tag{3.4}
\]

Seven-connectivity gives the other inequality in (3.1).  Equality at
eight in (3.4) forces every intermediate inequality to be equality, proving
(3.2).

Finally, an interior contribution to (3.3) is at least two if its degree is
at most four, and is one if its degree is five.  Thus either one such vertex
has degree at most four, or at least two have degree five.  In the former
case (3.4) and minimum degree seven force host degree seven and adjacency to
all three omitted boundary vertices.  \(\square\)

### Consequence for the active programme

If the first vertex in Theorem 3.1 has degree seven, its neighbourhood is
an actual order-seven separation boundary: the original far side `R`
survives outside its closed neighbourhood.  In the active hypothetical
minor-minimal counterexample, the degree-seven matching language can
therefore be regenerated at this vertex.  The only other
curvature equality is a degree-eight vertex with five neighbours in the
four-root disk and all three omitted boundary vertices as neighbours.
This is a bounded-degree re-entry, not a trace-preserving descent.

### Corollary 3.2 (the complete five-ring equality closes)

Let `v in L` have degree eight as in (3.2), put `B=T-(I union J)`,
and let `C={c_0,...,c_4}` be its five neighbours in `H`, indexed cyclically.
If

\[
        c_ic_{i+1}\in E(G)\quad(i\bmod 5),
        \qquad E_G(B,C)=B\times C,                        \tag{3.5}
\]

then `G` contains a `K_7` minor.

#### Proof

Let `D` be the component of `G-N_G[v]` containing a vertex of the old far
side `R`.  Its external neighbourhood is contained in

\[
                         N_G(v)=B\mathbin{\dot\cup}C.
\]

Seven-connectivity gives `|N_G(D)|>=7`, so at most one of these eight
vertices is missed by `D`.

Write `B={b_0,b_1,b_2}`.  Unless the missed vertex is one of
`b_2,c_2,c_3,c_4`, use the following six branch sets:

\[
 \{c_0,b_0\},\ \{c_1,b_1\},\ \{b_2\},\
 \{c_2,v\},\ \{c_3\},\ \{c_4\}.                        \tag{3.6}
\]

For the four exceptional missed vertices, respectively use

\[
\begin{array}{c|l}
b_2&\{c_0,b_0\},\{b_1\},\{c_1,b_2\},\{c_2,v\},\{c_3\},\{c_4\};\\
c_2&\{c_0,b_0\},\{b_1,c_2\},\{b_2\},\{c_1,v\},\{c_3\},\{c_4\};\\
c_3&\{c_0,b_0\},\{b_1,c_3\},\{b_2\},\{c_1\},\{c_2\},\{v,c_4\};\\
c_4&\{c_0,b_0\},\{b_1,c_4\},\{b_2\},\{c_1,v\},\{c_2\},\{c_3\}.
\end{array}                                               \tag{3.7}
\]

In every line, the six displayed sets are connected and pairwise adjacent
by the five-cycle, the edges from `v` to `C`, and the complete `B`--`C`
adjacency.  Each set contains a vertex of `N_G(D)`: the only possibly
missed vertex was paired with another contacted vertex.  Appending `D` as
the seventh branch set gives the required explicit `K_7`-minor model.
\(\square\)

Thus a `K_7`-minor-free degree-eight equality must lose a literal rim edge
or have nonuniform contacts between the five disk neighbours and the three
omitted boundary vertices.  The virtual rim edges of the triangulated
completion cannot be used in (3.5).

## 4. A far-side colouring forces a literal double-colour contact

Put

\[
                         U=I\cup J,
             \qquad      B=T-U.                           \tag{4.1}
\]

### Theorem 4.1

Let `phi` be a proper six-colouring of the unchanged closed shore
`G[R\cup T]`, and suppose that its restriction to `U` is nonconstant.  Then
at least one of the following holds.

1. `phi` extends to a proper six-colouring of `G`.
2. Some literal vertex `v in L` has neighbours in `B` of at least two
   distinct `phi`-colours:

   \[
                         |\phi(N_G(v)\cap B)|\ge2.         \tag{4.2}
   \]

In particular, outcome 2 holds for every such far-side colouring when `G`
is not six-colourable.

### Proof

Assume that (4.2) fails.  As in the proof of Theorem 3.1, temporarily
delete every literal edge joining consecutive roots and enclose the
remaining drawing with a virtual `4`-cycle.  If the ends of one virtual
side have distinct
`phi`-colours, retain that side.  If they have the same colour, subdivide
the side once with a new artificial vertex and precolour that vertex with
any different colour.  The resulting outer cycle `C` is properly
precoloured.  A nonconstant colouring of a `4`-cycle has at most two
monochromatic sides, so

\[
                              4\le |C|\le6.               \tag{4.3}
\]

For every literal vertex `v in L`, choose a five-element list contained in

\[
                         [6]-\phi(N_G(v)\cap B).           \tag{4.4}
\]

Such a list exists because (4.2) fails.  Give the roots and artificial
vertices arbitrary five-element lists containing their prescribed colours.

Apply Theorem 7 of Bohme--Mohar--Stiebitz to the plane graph inside `C`.
That theorem extends a precolouring of a facial cycle of order at most six
from lists of order at least five, apart from three explicit configurations.
None can occur here.  When `|C|=5`, the exceptional vertex adjacent to five
cycle vertices would have to be adjacent to the artificial vertex.  When
`|C|=6`, the same obstruction again meets an artificial vertex; the two
four-vertex windows in the second exception together cover `C`; and the
three three-vertex windows in the third exception together cover `C`.
Every exception would therefore require an interior literal vertex to be
adjacent to an artificial vertex, but artificial vertices have no interior
neighbours.

The outer precolouring consequently extends.  Restrict the resulting
colouring to the literal graph `H`, restoring the temporarily deleted
root--root edges.  Each restored edge is proper because both ends retain
their colours from the proper colouring `phi` of `G[R\cup T]`.  The lists
(4.4) make every edge from `L` to `B` proper, the colouring agrees with
`phi` on `U`, and there is no edge from `L` to `R`.  It therefore glues to
`phi` and six-colours `G`, proving outcome 1.  \(\square\)

### Corollary 4.2 (three omitted boundary vertices)

Let `F_B` be the graph on the three vertices of `B` in which two vertices
are adjacent when they have a common neighbour in `L`.  In every
nonextendable far-side colouring which is nonconstant on `U`, some edge of
`F_B` is bichromatic.

Suppose additionally that `G` is not six-colourable, every proper minor of
`G` is six-colourable, and that `b_ib_j` is an edge of `F_B` but not an
edge of `G[T]`.  Contract a
two-edge star through a common neighbour in `L`.  In a six-colouring of the
proper minor, pull the representative colour back to `b_i,b_j` on the
unchanged far shore.  This pullback is proper because `b_ib_j` is absent
and every edge incident with either boundary vertex survives at the
contraction representative.  The pulled-back far-side colouring cannot
extend to `G`, because `G` is not six-colourable.  If its restriction to
`U` is nonconstant, Theorem 4.1 forces a different edge of `F_B`,
necessarily incident with the third vertex of `B`, to be bichromatic.
Thus, under these hypotheses, an isolated contractible common-neighbour
pair cannot be the only double-contact witness.

## 5. Trust boundary and dependencies

Theorem 2.1 converts the whole non-singleton disk family into an explicit
complete minor or a genuine full-neighbourhood separation, but does not
bound the latter.  Theorem 3.1 makes the same family re-enter at degree
seven or eight, but does not preserve the five named far-side subgraphs.
Theorem 4.1 turns every nonextendable colouring into a literal common
neighbour of two differently coloured omitted boundary vertices, but that
vertex can depend on the colouring.  The remaining theorem must use
proper-minor responses and `K_7`-minor exclusion to bound or synchronize
the returned separation, or to make these response-dependent contacts
label-preserving.

Dependencies and external inputs:

- [closed-shore rooted connectivity](hc7_closed_shore_rooted_connectivity.md);
- Jørgensen's rooted `K_4^-` lemma as restated in Lemma 10 of S. Norin and
  A. Totschnig, *Every graph with no `K_7^vee`-minor is 6-colorable*,
  <https://arxiv.org/abs/2507.03244>;
- Theorem 7 of T. Böhme, B. Mohar and M. Stiebitz, *Dirac's Map-Color
  Theorem for Choosability*, Journal of Graph Theory 32 (1999), 327--339,
  <https://doi.org/10.1002/(SICI)1097-0118(199912)32:4%3C327::AID-JGT2%3E3.0.CO;2-B>.
