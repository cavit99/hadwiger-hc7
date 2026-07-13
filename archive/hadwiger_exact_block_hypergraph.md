# Exact-block hypergraphs at a full-shore adhesion

## 1. Setting

Let \(r=t-1\), and let \(G\) be a proper-minor-minimal graph which is not
\(r\)-colourable.  Thus every proper minor of \(G\) is \(r\)-colourable.
Let \((A,B)\) be a separation with

\[
 S=A\cap B,\qquad A-B\ne\varnothing,\qquad B-A\ne\varnothing.
\]

Assume that there are connected sets

\[
 D_A\subseteq A-S,\qquad D_B\subseteq B-S
\]

such that every vertex of \(S\) has a neighbour in each of \(D_A,D_B\).
Call these **full shores**.

Let \(\Omega=\Omega_r(G[S])\) be the set of all partitions of \(S\) into
at most \(r\) nonempty independent blocks.  For a nonempty independent
set \(P\subseteq S\), put

\[
 \Omega(P)=\{\Pi\in\Omega:P\text{ is a block of }\Pi\}.
\]

Let \(\mathcal E_A\) and \(\mathcal E_B\) be the exact boundary states
induced by \(r\)-colourings of \(G[A]\) and \(G[B]\), respectively.

## 2. The exact-block hypergraph theorem

### Theorem 2.1

Under the hypotheses above:

1. \(\mathcal E_A\cap\mathcal E_B=\varnothing\);
2. for every nonempty independent \(P\subseteq S\),
   \(\mathcal E_A\cap\Omega(P)\ne\varnothing\) and
   \(\mathcal E_B\cap\Omega(P)\ne\varnothing\).

Consequently the hypergraph

\[
 \mathcal H_r(S)=\bigl(\Omega,\{\Omega(P):
 P\subseteq S\text{ nonempty and independent}\}\bigr)
\]

has Property B: its vertices can be coloured red and blue so that every
hyperedge contains both colours.

#### Proof

If \(\Pi\in\mathcal E_A\cap\mathcal E_B\), permute the \(r\) colours on
one side so that corresponding blocks of \(\Pi\) have the same colours.
The two colourings then glue, since there is no edge from \(A-S\) to
\(B-S\).  This would \(r\)-colour \(G\), proving item 1.

Fix a nonempty independent \(P\subseteq S\).  The set
\(D_A\cup P\) is connected.  Contract it to a vertex \(z_A\) and delete
all remaining vertices of \(A-S\).  The resulting graph is a proper
minor of \(G\), and therefore has an \(r\)-colouring.  Expand the boundary
on the \(B\)-side by giving every vertex of \(P\) the colour of \(z_A\).
This is proper.  Moreover, no vertex of \(S-P\) has that colour: every
such vertex has a neighbour in \(D_A\), and hence is adjacent to \(z_A\)
after the contraction.  Thus \(P\) is an exact block of the induced
state, proving

\[
 \mathcal E_B\cap\Omega(P)\ne\varnothing.
\]

Contracting \(D_B\cup P\) symmetrically proves the assertion for
\(\mathcal E_A\).  Colour states in \(\mathcal E_A\) red, states in
\(\mathcal E_B\) blue, and all remaining states arbitrarily.  Item 1
makes this well-defined and item 2 makes every edge bichromatic.
\(\square\)

The theorem uses the full-shore condition for every vertex of \(S\), not
only for the vertices of \(P\).  It is exactly this condition which makes
the contracted image of \(P\) different in colour from every vertex of
\(S-P\).

## 3. Unique-state exclusions

For a graph \(F\), let \(\mathcal C_k(F)\) denote its partitions into at
most \(k\) nonempty independent sets, with colour names forgotten.

### Lemma 3.1

For every nonempty independent \(P\subseteq S\), deletion of the block
\(P\) gives a bijection

\[
 \Omega(P)\longleftrightarrow
 \mathcal C_{r-1}(G[S-P]).                         \tag{3.1}
\]

In particular, no such \(P\) can have
\(|\mathcal C_{r-1}(G[S-P])|=1\).

#### Proof

A state containing the exact block \(P\) has at most \(r-1\) other
blocks, and these are precisely a proper partition of \(G[S-P]\).
Conversely any such partition can be adjoined to the independent block
\(P\).  If the set in (3.1) were a singleton, Theorem 2.1 would require
that one state to lie in both disjoint side families. \(\square\)

### Lemma 3.2 (classification of a unique bounded-palette partition)

Assume \(\chi(F)\le k\).  Then

\[
 |\mathcal C_k(F)|=1
\]

if and only if either

1. \(F\) is complete; or
2. \(\chi(F)=k\) and \(F\) is uniquely \(k\)-colourable, up to a
   permutation of the colours.

#### Proof

Both displayed cases plainly give a unique partition.  Conversely, let
\(\Pi\) be the unique partition and put \(h=|\Pi|\).  If \(h=k\), then
\(\chi(F)=k\) and uniqueness is exactly unique \(k\)-colourability.  If
\(h<k\) and a block of \(\Pi\) has at least two vertices, splitting that
block produces a second member of \(\mathcal C_k(F)\).  Hence every block
is a singleton.  If \(F\) were not complete, a nonadjacent pair could be
merged, again producing a second partition.  Therefore \(F\) is
complete. \(\square\)

### Corollary 3.3 (strengthened one-block adhesion theorem)

There is no nonempty independent \(P\subseteq S\) for which either

1. \(G[S-P]\) is complete; or
2. \(G[S-P]\) is uniquely \(r-1\)-colourable and has chromatic number
   \(r-1\).

No completeness assumption between \(P\) and \(S-P\) is needed.

This strictly strengthens the earlier one-block theorem.  The missing
cross edges do not matter: after contracting a full shore together with
\(P\), the shore itself makes the contracted vertex adjacent to every
vertex of \(S-P\).

## 4. The missing-edge graph and split adhesions

Put

\[
 Q=\overline{G[S]}.
\]

The independent blocks of \(G[S]\) are exactly the cliques of \(Q\).

### Corollary 4.1

The graph \(Q\) is not a split graph.  Consequently \(Q\) contains an
induced \(2K_2\), \(C_4\), or \(C_5\).

#### Proof

If \(Q\) were split, write \(S=P\mathbin{\dot\cup}I\), where \(P\) is a
clique and \(I\) is independent in \(Q\).  If \(P=\varnothing\), move any
one vertex of the nonempty separator \(S\) from \(I\) into \(P\).  Thus
we may assume \(P\ne\varnothing\).  Now \(P\) is independent in \(G[S]\)
and \(G[I]=G[S-P]\) is complete, contrary to Corollary 3.3.

The second assertion is the Földes--Hammer characterization of split
graphs. \(\square\)

This conclusion absorbs arbitrary vertices outside the displayed
induced obstruction: one does not need \(Q\) to equal a core plus
isolates in order to conclude that it is nonsplit.

### Lemma 4.2 (the full-shore minor bound)

If \(G\) has no \(K_t\)-minor, then

\[
 \eta(G[S])\le t-2.                                  \tag{4.1}
\]

#### Proof

If \(G[S]\) had a \(K_{t-1}\)-model, use its \(t-1\) branch sets and add
\(D_A\) as one more branch set.  The set \(D_A\) is connected, disjoint
from \(S\), and adjacent to every model branch set because it has a
neighbour at every vertex of \(S\).  This is a \(K_t\)-model in \(G\), a
contradiction. \(\square\)

This elementary inequality is independent of the state-hypergraph
argument and becomes strong when the nonsplit core is nearly complete in
\(G[S]\).

## 5. Exact characterization below the palette wall

The preceding necessary condition is also the exact abstract
Property-B threshold when the palette can separate every boundary
vertex.

### Theorem 5.1

If \(|S|\le r\), then \(\mathcal H_r(S)\) has Property B if and only if
\(Q=\overline{G[S]}\) is nonsplit.

#### Proof

If \(Q\) is split, the proof of Corollary 4.1 supplies a nonempty clique
\(P\) of \(Q\) such that \(Q-P\) is independent.  Equivalently, \(P\) is
independent in \(G[S]\) and \(G[S-P]\) is complete.  Since
\(|S-P|\le r-1\), the edge \(\Omega(P)\) consists of the single state
formed by \(P\) and the singleton vertices of \(S-P\).  Thus Property B
fails.

Conversely, suppose \(Q\) is nonsplit.  Colour a state \(\Pi\in\Omega\)
by the parity of \(|\Pi|\).  Fix a nonempty clique \(P\) of \(Q\).  Since
\(Q\) is nonsplit, \(Q-P\) has an edge \(xy\).  The following are both
valid states because \(|S|\le r\):

\[
 \{P\}\cup\{\{s\}:s\in S-P\},
\]

and the state obtained from it by replacing \(\{x\},\{y\}\) with
\(\{x,y\}\).  They lie in \(\Omega(P)\) and have opposite block-count
parities.  Hence every hyperedge is bichromatic. \(\square\)

Thus, for adhesions of order at most \(r\), the exact-block hypergraph
mechanism by itself proves precisely nonsplitness and no more.  In
particular the induced \(2K_2,C_4,C_5\) alternatives are genuine parity
survivors, not contradictions.  Additional minor-transition, linkage,
or rooted-model data is necessary to eliminate them.

## 6. What remains at the palette wall

For any nonempty independent \(P\subseteq S\), put

\[
 F_P=G[S-P],\qquad k=r-1.
\]

### Lemma 6.1 (block-count parity localizes the difficulty)

If \(F_P\) is not complete and \(\chi(F_P)\le k-1=r-2\), then
\(\Omega(P)\) contains two states with opposite block-count parity.

#### Proof

Take a proper partition of \(F_P\) with
\(h=\chi(F_P)\le k-1\) blocks.  Since \(F_P\) is not complete, not every
block can be a singleton.  Split a nonsingleton block into two nonempty
independent blocks.  This gives proper partitions of \(F_P\) with \(h\)
and \(h+1\le k\) blocks.  Adjoining \(P\) gives two members of
\(\Omega(P)\) of opposite parity. \(\square\)

Therefore the parity colouring can fail only at:

1. the already-excluded complete-complement cells; or
2. the palette-tight cells \(\chi(F_P)=r-1\).

The palette-tight cells admit a useful exact description when their
order is close to \(k=r-1\).  Let

\[
 R_P=\overline{F_P}=Q[S-P].
\]

A proper partition of \(F_P\) is the same thing as a partition of
\(V(R_P)\) into cliques.  Let \(\theta(R_P)\) be the minimum number of
cliques in such a partition.

### Proposition 6.2 (palette-tight complements of excess at most two)

Assume \(\chi(F_P)=k\), and put \(n=|F_P|\).

1. If \(n=k\), then \(R_P\) is empty and \(\Omega(P)\) is a singleton.
2. If \(n=k+1\), then \(R_P\), after deletion of isolated vertices, is a
   nonempty star \(K_{1,d}\).  The \(k\)-block partitions of \(F_P\) are
   in bijection with the \(d\) edges of that star.
3. If \(n=k+2\), then \(R_P\) contains a triangle or a matching of order
   two, but contains none of:
   * a \(K_4\);
   * a triangle disjoint from an edge;
   * a matching of order three.

   Conversely these conditions characterize \(\theta(R_P)=k\).  The
   \(k\)-block partitions are in bijection with

   \[
   \{\text{triangles of }R_P\}
   \mathbin{\dot\cup}
   \{\text{two-edge matchings of }R_P\}.             \tag{6.1}
   \]

#### Proof

A clique block of order \(a\) saves \(a-1\) blocks relative to the
all-singleton partition.  Since \(\theta(R_P)=k=n-(n-k)\), an optimal
clique partition has total saving \(n-k\).

For \(n=k\), positive saving is forbidden, so \(R_P\) has no edge.

For \(n=k+1\), the maximum saving is exactly one.  Thus \(R_P\) has an
edge, but has neither a triangle nor two disjoint edges.  A graph whose
edges are pairwise intersecting is a star or a triangle; the triangle is
excluded.  Every optimal partition chooses exactly one star edge as its
only nonsingleton block.

For \(n=k+2\), maximum saving is exactly two.  Saving two is supplied by
one triangle or by two disjoint edges.  Saving at least three is supplied
by a \(K_4\), a triangle disjoint from an edge, or three disjoint edges.
Conversely, every clique partition with saving at least three contains
one of these three patterns: the block-size contributions to a total of
three include a block of order at least four, a block of order three
together with another nonsingleton block, or three blocks of order two.
This proves the characterization and (6.1). \(\square\)

In case 2, one edge gives the forbidden unique state and two edges give
a two-state constraint.  In case 3 the state-edge size is exactly the
number in (6.1); sizes one and two are therefore completely explicit.

## 7. Two-state constraints and parity cycles

Let \(L\) be the graph whose vertices are the states in \(\Omega\), with
an edge between the two members of \(\Omega(P)\) whenever
\(|\Omega(P)|=2\).  Parallel copies are irrelevant.

### Proposition 7.1

The graph \(L\) is bipartite.  In particular, any odd cycle of two-state
constraints rules out the full-shore separation.

If every hyperedge of \(\mathcal H_r(S)\) has order two, this condition
is also sufficient for Property B.

#### Proof

The Property-B colouring supplied by Theorem 2.1 gives opposite colours
to the two ends of every edge of \(L\), so \(L\) is bipartite.  Conversely,
when all hyperedges have order two, a bipartition of \(L\) is exactly a
Property-B colouring (isolated states may be coloured arbitrarily).
\(\square\)

Thus the palette-tight two-state survivors reduce to explicit parity
components.  Any non-Property-B obstruction not already caught by a
singleton or an odd cycle of doubletons has a genuine higher-order core.
Indeed, choose an edge-minimal non-Property-B subhypergraph.  Every state
which it uses has incidence degree at least two.  Otherwise delete its
sole incident edge, colour the remaining hypergraph, and then recolour
that state, which occurs nowhere else, to split the deleted edge.  If
every edge of the core had order two, it would be an ordinary
nonbipartite graph and hence contain an odd cycle.  Thus some edge has
order at least three.  This is the precise point at which the abstract
boundary state data cease to be a parity problem.

### Proposition 7.2 (the exact \(2K_2\) signature)

Suppose \(|S|\le r\) and

\[
 Q=2K_2\mathbin{\dot\cup} (|S|-4)K_1.
\]

Let the two edges of \(Q\) be \(e,f\), and write

\[
 \Pi_\varnothing,\quad \Pi_e,\quad \Pi_f,\quad \Pi_{ef}
\]

for the four states obtained by using neither, one, or both of \(e,f\)
as nonsingleton clique blocks of \(Q\).  After possibly interchanging
\(A\) and \(B\),

\[
 \begin{aligned}
 \mathcal E_A\cap\Omega&=\{\Pi_\varnothing,\Pi_{ef}\},\\
 \mathcal E_B\cap\Omega&=\{\Pi_e,\Pi_f\}.
 \end{aligned}                                       \tag{7.1}
\]

#### Proof

Every isolated vertex of \(Q\) is forced to be a singleton block.  For
an endpoint \(x\) of \(e\), the edge \(\Omega(\{x\})\) is
\(\{\Pi_\varnothing,\Pi_f\}\); similarly an endpoint of \(f\) gives
\(\{\Pi_\varnothing,\Pi_e\}\).  Moreover,

\[
 \Omega(e)=\{\Pi_e,\Pi_{ef}\},\qquad
 \Omega(f)=\{\Pi_f,\Pi_{ef}\}.
\]

Theorem 2.1 forces opposite side colours at the ends of each of these
four doubletons.  They form a four-cycle with bipartition
\(\{\Pi_\varnothing,\Pi_{ef}\}\),
\(\{\Pi_e,\Pi_f\}\).  Each state is forced to belong to exactly one
side family, proving (7.1). \(\square\)

There is a corresponding exact minor-transition statement.  If an
\(S\)-label-preserving internal edge deletion, edge contraction, or
interior-vertex deletion is performed on side \(A\), an \(r\)-colouring
of the resulting proper minor has a common boundary state on the
operated \(A\)-side and the unchanged \(B\)-side.  That state cannot have
belonged to \(\mathcal E_A\), or it would glue to colour the original
graph.  Hence every internal one-step minor on \(A\) unlocks one of the
two opposite-parity states in \(\mathcal E_B\); symmetrically for \(B\).
This is a concrete finite signature for any attempted boundaried-graph
elimination.

## 8. Exact Földes--Hammer cores in the \(t=7\) case

The full-shore minor bound sharply limits the cases in which the
missing-edge graph is exactly a forbidden split core plus isolated
vertices.

### Proposition 8.1

Let \(n=|S|\).  Then

\[
 \begin{array}{c|c|c}
 Q & G[S] & \eta(G[S])\\ \hline
 2K_2\dot\cup(n-4)K_1 & K_n-E(2K_2) & n-1\\
 C_4\dot\cup(n-4)K_1 & K_{n-4}\vee 2K_2 & n-2\\
 C_5\dot\cup(n-5)K_1 & K_{n-5}\vee C_5 & n-2.
 \end{array}                                          \tag{8.1}
\]

#### Proof

For the first row, one connected branch set using one endpoint of each
missing edge, together with all remaining singleton vertices, gives a
\(K_{n-1}\)-model.  A \(K_n\)-minor in an \(n\)-vertex graph would require
the graph itself to be complete, so the value is \(n-1\).

The complement of \(C_4\) is \(2K_2\), whose Hadwiger number is two; the
complement of \(C_5\) is again \(C_5\), whose Hadwiger number is three.
Finally

\[
 \eta(K_p\vee H)=p+\eta(H).
\]

The lower bound is immediate.  For the upper bound, at most \(p\) branch
sets of a clique model can meet the \(K_p\); deleting those leaves a
clique model in \(H\).  This proves the last two rows. \(\square\)

### Corollary 8.2

For \(t=7\), a full-shore adhesion has \(|S|\ge7\) by seven-connectivity
and \(\eta(G[S])\le5\) by Lemma 4.2.  Consequently:

1. \(Q=2K_2\dot\cup(n-4)K_1\) is impossible for every possible \(n\);
2. \(Q=C_4\dot\cup(n-4)K_1\) or
   \(Q=C_5\dot\cup(n-5)K_1\) is possible only when \(n=7\).

Thus the exact-core branch of the \(t=7\) contact separator reduces to
the two order-seven adhesions

\[
 G[S]\cong K_3\vee2K_2,
 \qquad
 G[S]\cong K_2\vee C_5.                              \tag{8.2}
\]

The first graph in (8.2) is in fact impossible by using both shores.
Write its \(2K_2\) as the two edges \(x_1x_2,y_1y_2\), and write its
\(K_3\) as \(\{z_1,z_2,z_3\}\).  The seven disjoint connected sets

\[
 D_A\cup\{x_1,x_2\},\quad
 \{y_1\},\quad \{y_2\},\quad
 \{z_1\},\quad \{z_2\},\quad \{z_3\},\quad D_B
\]

are pairwise adjacent.  Indeed, \(D_A,D_B\) each touch every boundary
vertex; the only boundary adjacencies needed among the five singleton or
paired core pieces are the edge \(y_1y_2\), the \(K_3\), and all joins
from that \(K_3\), all of which are present.  These sets form a
\(K_7\)-model.

Consequently, among the three exact Földes--Hammer core-plus-isolates
graphs, the only full-shore residual for \(t=7\) is

\[
 G[S]\cong K_2\vee C_5,
 \qquad Q=C_5\dot\cup2K_1.                            \tag{8.2a}
\]

For completeness, before its minor closure the first graph in (8.2) had
six admissible boundary states corresponding to the four one-edge
matchings and two perfect matchings of the \(C_4\).  The doubleton
constraints force its four one-edge states to alternate around the
cycle.  For the residual (8.2a), the ten admissible states are the five
one-edge and five two-edge matchings of \(C_5\); matching-size parity is
a valid Property-B colouring.  Hence static Property B alone does not
remove (8.2a), but it has an explicit finite side-signature target.

### Proposition 8.3 (complete side-signature classification for the
\(C_5\) residual)

Index the edges of the \(C_5\) cyclically as
\(e_0,e_1,\ldots,e_4\).  Let

\[
 s_i=\{e_i\},\qquad d_i=\{e_i,e_{i+2}\}
\]

denote the five one-edge and five two-edge matching states; indices are
modulo five.  Encode membership in \(\mathcal E_A\) by \(0\), membership
in \(\mathcal E_B\) by \(1\), and membership in neither family by a dash.
The families are disjoint by Theorem 2.1.

Every valid pair \((\mathcal E_A,\mathcal E_B)\), restricted to these ten
states, contains one of the following six inclusion-minimal signatures,
up to a dihedral symmetry of the cycle and interchange of \(0,1\):

\[
\begin{array}{c|c}
(s_0s_1s_2s_3s_4)&(d_0d_1d_2d_3d_4)\\ \hline
00000&11111\\
00101&-101-\\
0010-&--011\\
0101-&101-0\\
010--&-0110\\
0-1--&-0011.
\end{array}                                          \tag{8.3}
\]

Conversely every row of (8.3), and every assignment obtained by replacing
any of its dashes arbitrarily by \(0\) or \(1\), meets every exact-block
edge on both sides.  Thus (8.3) classifies all disjoint side families:
they are exactly the supersets of the six displayed minimal types.

#### Proof

For the exact block \(e_i\), the permitted states are

\[
 \Omega(e_i)=\{s_i,d_i,d_{i+3}\}.                   \tag{8.4}
\]

For the exact singleton block given by the cycle vertex incident with
\(e_{i-1},e_i\), the permitted nonempty matchings of the remaining
three-edge path are

\[
 \{s_{i+1},s_{i+2},s_{i+3},d_{i+1}\}.              \tag{8.5}
\]

The two isolated vertices of the missing-edge graph give the full set of
ten states and add no new condition.  Hence a partial \(0,1,-\) word is
valid exactly when every set in (8.4) and (8.5) contains both \(0\) and
\(1\).

Delete assigned symbols one at a time while this condition remains true.
This terminates at an inclusion-minimal word.  The constraints (8.4)
first show that at least two \(s_i\) are assigned: if none is assigned,
they require

\[
 d_i\ne d_{i+3}\quad(0\le i<5),
\]

which is an impossible alternating colouring of a five-cycle; one
assigned \(s_i\) leaves a four-edge alternating path, and its forced end
colours violate the appropriate condition (8.5).  Branching on the
number of assigned \(s_i\), and using a reflection and a rotation, gives

\[
\begin{array}{c|c|c}
\#\{i:s_i\ne-\}&\text{possible minimal }s\text{-words}
 &\text{forced minimal }d\text{-word}\\ \hline
5&00000&11111\\
5&00101&-101-\\
4&0010-&--011\\
4&0101-&101-0\\
3&010--&-0110\\
2&0-1--&-0011.
\end{array}
\]

In each row the \(d\)-entries follow successively from (8.4), and (8.5)
then both verifies the row and shows that every displayed symbol is
essential.  These are exactly the six rows in (8.3).  Adding symbols to
a valid partial word cannot destroy the fact that every constraint
already contains both colours.  This proves both directions. \(\square\)

The last row shows the sharp odd-cycle break: if exactly two one-edge
states are realized, then, up to symmetry, they are \(s_0\in\mathcal E_A\)
and \(s_2\in\mathcal E_B\), while
\(d_1,d_2\in\mathcal E_A\), \(d_3,d_4\in\mathcal E_B\), and only \(d_0\)
is left unspecified.  The first row is the rigid
matching-size polarity, with every single-edge state on one shore and
every double-matching state on the other.

### Corollary 8.4 (forced one-step transition in the \(C_5\) residual)

Let \(\mu\) be any \(S\)-label-preserving one-step deletion or contraction
internal to side \(A\).  Then the operated side \(A^\mu\) realizes at
least one state belonging to \(\mathcal E_B\), and that state did not
belong to \(\mathcal E_A\).  The symmetric statement holds for an
operation internal to \(B\).

Consequently, after selecting a minimal signature from (8.3), every
internal operation on a \(0\)-side must unlock at least one displayed
\(1\)-state, while every operation on a \(1\)-side must unlock at least
one displayed \(0\)-state.

#### Proof

Apply \(\mu\) to the full graph.  The resulting proper minor has an
\(r\)-colouring.  Its restriction gives one common exact state of the
operated \(A\)-side and the unchanged \(B\)-side.  If that state also
extended to the original \(A\)-side, the two original side colourings
could be aligned and glued, contrary to the choice of \(G\).  Thus it is
in \(\mathcal E_B\setminus\mathcal E_A\). \(\square\)

The script `c5_exact_state_signature.py` checks the finite table directly.
There are 202 total two-colour Property-B assignments, in 14 orbits under
the dihedral group and shore interchange.  There are 62 labeled
inclusion-minimal partial signatures, in exactly the six orbits displayed
in (8.3).  The proof above uses only the ten explicit constraints
(8.4)--(8.5); the computation is an independent audit.

### Proposition 8.5 (the second five-edge quotient residual)

The exact five-edge quotient analysis has a second sharp graph which is
not one of the three core-plus-isolates graphs above:

\[
 Q=K_3\dot\cup2K_2,
 \qquad G[S]=K_{3,2,2}.                              \tag{8.6}
\]

After contracting the two full shores, the nine-vertex quotient is the
complete multipartite graph \(K_{3,2,2,2}\), and it has no
\(K_7\)-minor.  Indeed, seven branch sets on nine vertices include at
least five singleton branch sets: if \(q\) branch sets are nonsingleton,
they use at least \(7+q\) vertices, so \(q\le2\).  Pairwise adjacent
singleton branch sets in a complete multipartite graph must lie in
different parts, but (8.6) has only four parts.  This is impossible.

The six-colour boundary states of (8.6) have the following exact
description.  Let \(T\) be the triangle component of \(Q\), and let
\(E,F\) be its two edge components.  A state is a triple

\[
 (\pi_T,\epsilon,\phi),                              \tag{8.7}
\]

where \(\pi_T\) is one of the five set partitions of \(T\), and
\(\epsilon,\phi\in\{0,1\}\) record whether \(E,F\), respectively, are
used as one clique block.  The unique all-singleton triple is omitted,
because it has seven blocks.  Hence there are exactly

\[
 5\cdot2\cdot2-1=19                                  \tag{8.8}
\]

states.  Their exact-block hyperedges have sizes

\[
 4,4,4,4,7,7,7,9,9,10,10.                           \tag{8.9}
\]

More explicitly:

* an exact triple block in \(T\), or any one of its three exact pair
  blocks, leaves four choices of \((\epsilon,\phi)\);
* an exact singleton \(x\in T\) allows either the all-singleton
  partition of \(T\) or the pair on \(T-x\), giving seven admissible
  states after the forbidden all-singleton state is removed;
* an exact edge block \(E\) gives ten states, while an exact singleton
  in \(E\) gives nine; the same holds for \(F\).

Block-count parity is a Property-B colouring.  For a triple or pair
block in \(T\), toggle \(\epsilon\); for a singleton in \(T\), first use
the pair on the other two triangle vertices and then toggle
\(\epsilon\).  For a block contained in \(E\), toggle \(\phi\), using a
pair block in \(T\) if necessary to avoid the forbidden seven-block
state; argue symmetrically for \(F\).  Thus every exact-block hyperedge
contains both parities.

Accordingly (8.6) is a second genuine static survivor, beside
\(C_5\dot\cup2K_1\).  The one-step transition conclusion remains exact:
every internal operation on either shore must unlock a state realized
by the opposite shore.  The state hypergraph here is much less rigid
than the \(C_5\) hypergraph.  The independent script
`k3_2k2_exact_state_signature.py` finds 301 inclusion-minimal one-side
covers and 27,128 ordered disjoint pairs of minimal covers, in 1,513
orbits under \(S_3\times S_2\) and shore interchange.  These counts are
an audit, not an ingredient of any theorem; (8.7)--(8.9) are the exact
rigorous state description.

## 9. Audit and computational evidence

The script `boundary_partition_hypergraph_probe.py` independently builds
\(\mathcal H_r(S)\) for labeled boundary graphs and tests Property B.
It found no non-Property-B example without a singleton edge among:

* every labeled graph on at most six vertices, for every palette cap;
* 5,000 random labeled graphs on seven vertices, for every palette cap.

This finite observation is **not** used as a theorem.  The proved general
statements are Theorems 2.1 and 5.1, the unique-state classification, the
palette-tight excess-two classification, and the two-state odd-cycle
obstruction.  No claim is made here that singleton edges are the only
possible abstract obstruction above the palette wall.

## 10. Strategic consequence

For the inclusion-minimal contact separator in a least Hadwiger
counterexample, the two distinguished components are full shores, so all
results above apply.  They give three concrete advances:

1. the old one-block exclusion no longer needs cross-completeness;
2. uniquely \(t-2\)-colourable palette-tight remainders are excluded;
3. every surviving missing-edge graph is nonsplit, hence has an induced
   \(2K_2,C_4,C_5\), while all two-state transition constraints must form
   a bipartite graph.

For the sharp seven-vertex, five-missing-edge quotient, the direct
two-shore model eliminates \(C_4\dot\cup3K_1\).  The exact residuals are
\(C_5\dot\cup2K_1\), with the six polarity types in (8.3), and
\(K_3\dot\cup2K_2\), with the 19-state description (8.7).  Neither is
eliminated by static state incidence.

They also identify an exact limitation.  When \(|S|\le t-1\), arbitrary
nonsplit extensions of the Földes--Hammer cores admit the explicit
block-parity Property-B colouring.  Therefore no argument using only
the static exact-block incidence hypergraph can eliminate such a
separator.  The next input must constrain which of the two parity
classes each *graph side actually realizes*, using one-step internal
minor transitions, relative linkage, or a label-preserving contact
augmentation.
