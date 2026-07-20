# Component-aware off-path bridges in a pentagonal-bipyramid column

**Status:** active unpromoted research draft.  The proved claims have received
a GREEN [separate internal cold audit](hc7_pentagonal_bipyramid_off_path_bridge_draft_audit.md),
which is not external peer review.  Section 5 applies the cited Two Paths
Theorem and records its exact host-level limit.  No bridge-chain theorem is
asserted.  This file does not change the authoritative status of Conjectural
Theorem 3.1.

## 1. Exact setting

Let `F` be five-connected and have a vertex partition into nonempty connected
columns

\[
 C_a,C_b,C_0,C_1,C_2,C_3,C_4
\]

whose contact graph is the pentagonal bipyramid: `a,b` are nonadjacent and
each is adjacent to every rim label, while the rim labels form the cycle
`0,1,2,3,4,0`.  Rim subscripts are read modulo five.  Let
\(A,B\subseteq V(F)\) meet every column, and suppose every column contains an
`A`--`B` path.  (The latter follows already from connectedness and the two
nonempty intersections, but it is retained as a literal target hypothesis.)
A `K_5`-minor model is paired-rooted at `(A,B)` when its five disjoint,
connected and pairwise adjacent branch sets each meet both `A` and `B`.

For a rim index `i`, put

\[
\begin{aligned}
 U_i&=N_F(V(C_a))\cap V(C_i),&
 W_i&=N_F(V(C_b))\cap V(C_i),\\
 L_i&=N_F(V(C_{i-1}))\cap V(C_i),&
 P_i&=N_F(V(C_{i+1}))\cap V(C_i).
\end{aligned}                                                    \tag{1.1}
\]

All four sets are nonempty.  A path may have one vertex; thus a shortest
`U_i`--`W_i` path has order one when the two sets intersect.  The symbols
`U_i,W_i` are pole-column portal sets and are unrelated to the root sets
`A,B`.

## 2. Any-path off-component transfer

### Lemma 2.1 (two-sided off-component transfer)

Fix `i`.  Let `R` be any path in `F[C_i]` meeting both `U_i` and `W_i`.
Suppose a component `H` of `F[C_i]-V(R)` meets both external rim portal
sets:

\[
        V(H)\cap L_i\ne\varnothing,
        \qquad V(H)\cap P_i\ne\varnothing.                      \tag{2.1}
\]

Then `F` contains a `K_5`-minor model paired-rooted at `(A,B)`.

### Proof

Let \(\mathcal H\) be the set of components of `F[C_i]-V(R)` and define the
following vertex sets:

\[
\begin{aligned}
 D_1&=V(C_a)\cup V(R)\cup
       \bigcup_{K\in\mathcal H-\{H\}}V(K),\\
 D_2&=V(C_b),\\
 D_3&=V(H)\cup V(C_{i+1}),\\
 D_4&=V(C_{i+2}),\\
 D_5&=V(C_{i+3})\cup V(C_{i+4}).
\end{aligned}                                                    \tag{2.2}
\]

The five sets are nonempty and pairwise disjoint.  Every component of
`F[C_i]-V(R)` has an edge to `R`, because `F[C_i]` is connected.  Hence
`F[D_1]` is connected: `R` meets `U_i` and therefore attaches to `C_a`,
and every retained component attaches to `R`.  The graph `F[D_3]` is
connected by the `H`--`C_{i+1}` contact in (2.1).  The graph `F[D_5]` is
connected because `C_{i+3},C_{i+4}` are consecutive rim columns.  The
other two sets are whole connected columns.

All ten pairwise adjacencies have literal witnesses:

| pair | witness |
|---|---|
| \(D_1D_2\) | a vertex of \(R\cap W_i\) and its neighbour in `C_b` |
| \(D_1D_3\) | an edge from `H` to `R` |
| \(D_1D_4\) | the quotient contact \(C_aC_{i+2}\) |
| \(D_1D_5\) | the quotient contact \(C_aC_{i+3}\) |
| \(D_2D_3\) | the quotient contact \(C_bC_{i+1}\) |
| \(D_2D_4\) | the quotient contact \(C_bC_{i+2}\) |
| \(D_2D_5\) | the quotient contact \(C_bC_{i+3}\) |
| \(D_3D_4\) | the rim contact \(C_{i+1}C_{i+2}\) |
| \(D_3D_5\) | the assumed contact \(HC_{i-1}=HC_{i+4}\) |
| \(D_4D_5\) | the rim contact \(C_{i+2}C_{i+3}\) |

Thus `F[D_1],...,F[D_5]` are branch sets of a `K_5` model.  They contain,
respectively, the whole columns

\[
                C_a,C_b,C_{i+1},C_{i+2},C_{i+3}.
\]

Each of those columns meets both literal sets `A` and `B`.  Every branch
set is therefore paired-rooted at `(A,B)`.  \(\square\)

The proof uses neither five-connectivity, shortestness of `R`, nor an
internal `A`--`B` path.  Those stronger hypotheses belong to the global
target, not to this transfer.

### Relation to the audited alternating-split theorem

The set

\[
 V(C_i)-V(H)=V(R)\cup
       \bigcup_{K\in\mathcal H-\{H\}}V(K)                       \tag{2.3}
\]

is connected.  It contacts both pole columns, while `H` contacts both rim
neighbours.  Hence `H` and its complement form the alternating connected
split in Corollary 2.2 of
[`hc7_pentagonal_bipyramid_adjacent_rim_linkage.md`](../results/hc7_pentagonal_bipyramid_adjacent_rim_linkage.md).
Lemma 2.1 records the direct paired-rooted five-bag lift.

## 3. The complete one-column Two Paths certificate

Bridge intervals are only a representation of a whole linkage instance.
The exact positive object is the following.

### Lemma 3.1 (connected bipartition extension)

Let `G` be connected and let `X,Y` be disjoint nonempty connected vertex
sets.  There is a partition \(V(G)=X'\mathbin{\dot\cup}Y'\) such that
\(X\subseteq X'\), \(Y\subseteq Y'\), and both `G[X']` and `G[Y']` are
connected.

### Proof

Contract `X` and `Y`, take a spanning tree, and delete any edge on the
unique path between the two contracted vertices.  The two resulting tree
components give the required partition after the contractions are
expanded.  \(\square\)

### Lemma 3.2 (one-column Two Paths transfer)

Fix `i`.  Suppose `F[C_i]` contains vertex-disjoint connected subgraphs
`X,Y` such that

\[
\begin{aligned}
 X\cap U_i&\ne\varnothing,& X\cap W_i&\ne\varnothing,\\
 Y\cap L_i&\ne\varnothing,& Y\cap P_i&\ne\varnothing.
\end{aligned}                                                    \tag{3.1}
\]

Then `F` contains a `K_5`-minor model paired-rooted at `(A,B)`.

### Proof

Apply Lemma 3.1 inside `F[C_i]` to extend `X,Y` to a connected bipartition
`X',Y'`.  The four portal classes in (3.1) alternate in the cyclic neighbour
order at the rim label `i`.  Corollary 2.2 of the audited adjacent-rim
linkage theorem gives an explicit five-bag model in which each bag contains
a whole nonsplit column.  Since every whole column meets both `A` and `B`,
that model is paired-rooted.  \(\square\)

Equivalently, form `J_i` by adding four terminal vertices
`t_a,t_b,t_-,t_+` to `F[C_i]`, adjacent respectively to
`U_i,W_i,L_i,P_i`.  The positive case is a pair of vertex-disjoint paths
joining `t_a` to `t_b` and `t_-` to `t_+`.  Any negative structural theorem
must concern this complete Two Paths instance, not each off-path component
separately.

### Corollary 3.3 (exact one-column formulation)

The auxiliary four-terminal graph has the two prescribed vertex-disjoint
paths if and only if `C_i` has an alternating connected bipartition in
which one side contacts `C_a,C_b` and the other contacts
`C_{i-1},C_{i+1}`.

The forward implication is Lemmas 3.1--3.2.  Conversely, paths inside the
two connected sides between their respective portal sets give the two
prescribed paths.  Thus component-aware bridge analysis is a way of solving
the complete one-column Two Paths instance, not a weaker replacement for
it.

### Corollary 3.4 (off-component transfer is the whole positive case)

For a fixed `i`, the following are equivalent.

1. Some `U_i`--`W_i` path `R` has a component of
   `F[C_i]-V(R)` meeting both `L_i` and `P_i`.
2. The four-terminal auxiliary graph has the two prescribed
   vertex-disjoint paths.
3. `C_i` has the alternating connected bipartition in Corollary 3.3.

For item 1, connectedness of `H` supplies an `L_i`--`P_i` path inside
`H`, disjoint from `R`, proving item 2.  Conversely, for item 2 take the
`U_i`--`W_i` path as `R`; the disjoint `L_i`--`P_i` path lies in one
component of `F[C_i]-V(R)`, proving item 1.  Corollary 3.3 gives the
equivalence of items 2 and 3.

Consequently, after the alternating-split outcome has been excluded, the
off-component condition is negative for **every** `U_i`--`W_i` path, not
only for every shortest one.  Shortest paths remain useful canonical
objects for representing that complete negative instance.

## 4. Typed bridges of a shortest pole path

Orient a shortest `U_i`--`W_i` path as

\[
                         R=r_0r_1\cdots r_k.                    \tag{4.1}
\]

The path is induced in `F[C_i]`: a chord between nonconsecutive path
vertices would shorten it.  When `k>0`, `r_0` is the only path vertex in
`U_i` and `r_k` is the only path vertex in `W_i`, since either additional
portal would give a shorter suffix or prefix.  Consequently its nontrivial
`R`-bridges inside the column are precisely the components `H` of
`F[C_i]-V(R)`, together with their incident edges to `R`.

For such a component define

\[
\begin{aligned}
 \operatorname{Att}_R(H)&=N_{F[C_i]}(V(H))\cap V(R),\\
 \ell_R(H)&=\min\{j:r_j\in\operatorname{Att}_R(H)\},\\
 r_R(H)&=\max\{j:r_j\in\operatorname{Att}_R(H)\},\\
 I_R(H)&=[\ell_R(H),r_R(H)],\\
 \sigma(H)&=\{x\in\{a,b,i-1,i+1\}:E_F(H,C_x)\ne\varnothing\}.
\end{aligned}                                                    \tag{4.2}
\]

The attachment set is nonempty, but it need not contain every path vertex
in its convex hull.  Two bridges genuinely cross when there are four
distinct indices `p<q<r<s` such that `r_p,r_r` attach to one bridge and
`r_q,r_s` attach to the other.  Overlap of `I_R(H)` and `I_R(K)` alone is
not a crossing certificate.  Repeated intercolumn contacts at a single path
vertex and external contacts owned by path vertices must be retained as
literal data.

The exact residual hypothesis after the equivalent positive outcomes in
Corollary 3.4 have been excluded is

\[
 \begin{gathered}
 \text{for every }i\in\mathbb Z/5\mathbb Z,\text{ every }
 U_i\text{--}W_i\text{ path }R,\text{ and every component }H
 \text{ of }F[C_i]-V(R),\\
                         \{i-1,i+1\}\nsubseteq\sigma(H).           \tag{4.3}
 \end{gathered}
\]

Components may therefore be left-typed, right-typed, or neutral with
respect to the rim neighbours.  Components of different types may still
compose into the positive linkage of Lemma 3.2.

### Proposition 4.1 (alternating attachments alone do not link)

Genuine crossing of two component-bridge attachment sets does not by itself
give the Two Paths certificate in Lemma 3.2, even when `R` is shortest.

Indeed, let `R=r_0r_1r_2r_3r_4r_5`, add vertices `x,y`, and add precisely
the four edges

\[
                    xr_1,xr_3,yr_2,yr_4.                       \tag{4.4}
\]

Take `U={r_0}`, `W={r_5}`, `L={x}`, and `P={y}`.  The path `R` is a
shortest `U`--`W` path.  The two off-path components have genuinely
alternating attachments

\[
                         r_1,r_2,r_3,r_4,
\]

and each meets one of `L,P`.  Nevertheless there are no disjoint connected
sets joining `U` to `W` and `L` to `P`.  Any `r_0`--`r_5` path contains
`r_1` and `r_4`, since they are the only neighbours of the two ends.  An
`x`--`y` path disjoint from it must therefore start `x r_3` and end
`r_2 y`.  Its only possible route is `x r_3 r_2 y`.  After deleting those
four vertices, the remaining graph has `r_0,r_1` and `r_4,r_5` in different
components, so it contains no path joining `r_0` to `r_5`.

The shortest `U`--`W` paths are the base path and the two equal-length
single-bridge detours.  For each, every off-path component remains
one-sided.  Thus even the universal-shortest residual condition does not
make crossing attachment order a positive certificate.

Thus a crossing theorem needs additional disjoint routing inside the
bridges or a global consequence of five-connectivity; the cyclic order of
four attachment vertices is insufficient.

### Lemma 4.2 (one bridge releases a two-sided open segment)

Let a component bridge `H` have distinct attachments `r_p,r_q`, with
`p<q`, and let `Q` be an `r_p`--`r_q` path whose internal vertices lie in
`H`.  If the open segment \(R(r_p,r_q)\) meets both `L_i` and `P_i`, then
`F` has a paired-rooted `K_5` model.

Replace the closed `r_p`--`r_q` segment of `R` by `Q`.  This gives a new
`U_i`--`W_i` path disjoint from the old open segment.  The open segment is
connected and meets both rim portal sets, so the two subgraphs satisfy
Lemma 3.2.  This is a valid individual bridge-span exchange.  Its converse
is false by the audited single-bridge span-inference barrier: several
bridges may compose the positive linkage even when no individual span does.

## 5. What the complete negative Two Paths instance gives

The appropriate structural theorem applies both to one rim column and to the
adjacent-rim carrier in the audited linkage theorem.  In the first case put
`Q=C_i` and take the external owner columns, in cyclic order, to be

\[
                  C_a,C_{i-1},C_b,C_{i+1}.                    \tag{5.1}
\]

In the second case put `Q=C_i\cup C_{i+1}` and use

\[
                  C_a,C_{i-1},C_b,C_{i+2}.                    \tag{5.2}
\]

In either case add four artificial terminals `t_1,t_2,t_3,t_4`, with
`t_j` adjacent precisely to the vertices of `Q` having a literal neighbour
in the corresponding owner column.  The carrier `Q` is connected and all
four terminal neighbourhoods are nonempty.  A crossing of the cyclic terminal
tuple is exactly a pair of disjoint paths joining `t_1` to `t_3` and `t_2`
to `t_4`.  For (5.1) this is the alternating split in Section 3; for (5.2)
it is the audited adjacent-rim linkage.

### Theorem 5.1 (external Two Paths/web alternative)

If the two prescribed paths do not exist, the auxiliary graph `J` is a
spanning subgraph of a `4`-web with frame
`t_1t_2t_3t_4t_1`.  Concretely, there is an edge set `E^+` such that
`J+E^+` consists of a plane rib with that outer four-cycle, all inner faces
triangular and every triangle facial, together with a possibly empty clique
inside each facial triangle and adjacent to exactly the three vertices of
that triangle.

This is the web-completion formulation of the Two Paths Theorem: Humeau and
Pous, Theorem 1.5 and Definition 1.2, give a current constructive proof of
the vertex-disjoint result originally proved independently by Seymour and
Thomassen.  The completion edges in `E^+` are generally not edges of `F`.

### Lemma 5.2 (literal boundary of a web cell)

Assume `F` is five-connected and the negative outcome of Theorem 5.1 holds.
Let `Delta` be a facial triangle of the rib, let `K_Delta` be its inserted
clique-vertex set, and let `X` be a component of the **literal** graph
`F[K_Delta]`.  Put

\[
 T=\{t_1,t_2,t_3,t_4\},\qquad
 S=V(Delta)\cap T,\qquad D=V(Delta)\cap V(Q),                 \tag{5.3}
\]

and let `E(X)` be the set of terminals whose artificial terminal edge to
`X` is already in `J`, not merely in the completion.  Then:

1. `E(X)` is a subset of `S`;
2. every neighbour of `X` in `F` lies in `D` or in an external owner column
   named by `E(X)`;
3. if `Z_X=N_F(X)-V(Q)`, then

   \[
                           |Z_X|\ge 2+|S|;                    \tag{5.4}
   \]

4. `|S|` is one or two, and in the latter case its two terminals are
   consecutive on the frame; and
5. when `|S|=2`, `D={z}` for one literal carrier vertex and `Q-X` is
   connected.

### Proof

A clique vertex of a web has no neighbour outside its own clique and the
three vertices of its facial triangle.  Because `J` is a spanning subgraph
of the completed web, a literal terminal edge from `X` can therefore end only
at a terminal in `Delta`, proving item 1.  The same observation, translated
back through the definition of the artificial terminals, proves item 2.

There is a nonempty far rim column with no quotient edge to `Q`: one may use
either non-neighbouring rim column for (5.1), and `C_{i+3}` for (5.2).
Consequently `N_F(X)` separates `X` from a literal far-side vertex.  By
five-connectivity it has order at least five.  Since
`|D|=3-|S|`, item 2 gives

\[
             5\le |N_F(X)|\le |D|+|Z_X|=3-|S|+|Z_X|,
\]

which is (5.4).  If `S` is empty, item 1 gives `Z_X` empty and contradicts
(5.4).

No facial triangle contains two opposite frame terminals.  If, for example,
it contained `t_1,t_3`, the rib edge `t_1t_3` would separate `t_2` from
`t_4` in the plane rib.  Filling facial triangles with cliques does not join
the two sides of such a separator.  But connectedness of `Q` and the two
nonempty portal sets gives a literal `t_2`--`t_4` path in `J` avoiding
`t_1,t_3`, a contradiction.  Thus the `|S|=3` case and opposite
two-terminal gates are impossible, proving item 4.

Finally suppose `|S|=2`.  Then `D={z}` and item 2 gives
`N_Q(X)\subseteq\{z\}`.  For any `y` in `Q-X`, take a `y`--`X` path in the
literal connected graph `Q`.  The predecessor of its first vertex in `X`
must be `z`, so the prefix is a `y`--`z` path in `Q-X`.  Every vertex of
`Q-X` therefore lies in the component of `z`, proving item 5.  \(\square\)

### Corollary 5.3 (the irreducible local cells)

After the alternating split and adjacent-rim linkage have been excluded, a
nonempty web cell has exactly one of the following literal signatures.

1. Its facial gate contains one terminal and two carrier vertices.  All its
   external neighbours lie in one owner column, with at least three distinct
   such neighbours.
2. Its facial gate contains two consecutive terminals and one carrier vertex.
   Its external neighbours lie in the corresponding pole column and outer
   rim column, or in just one of them, with at least four distinct external
   neighbours in total.  Its carrier complement is connected.

The lower bounds are multiplicity statements, not new owner labels.  Gate
membership is not literal contact, because both cell-to-gate edges and rib
edges may have been added by the web completion.  Even if no cell has carrier
vertices, deleting the completion edges proves only that this one- or
two-column auxiliary is a planar disc society.  It neither embeds the other
columns nor couples the repeated edge orders at the two ends of an
intercolumn bundle.

### Proposition 5.4 (both surviving cells occur in unbounded
five-connected expansions)

For every `m>=5`, both signatures in Corollary 5.3 occur in a
five-connected graph with the exact pentagonal-bipyramid column quotient.
These examples are local guardrails, not counterexamples to Conjectural
Theorem 3.1.

Take `i=0`.  Make `C_a,C_b,C_2,C_3,C_4` copies of `K_m`, and put all edges
between those five columns that their pentagonal-bipyramid labels permit.
For the singleton-terminal cell, take

\[
 C_0=F[\{h,z_1\}]=hz_1,\qquad C_1=\{z_2\},\qquad z_1z_2\in E(F),
\]

make `h,z_1` complete to `C_a`, make `z_1` complete to `C_b,C_4`, and make
`z_2` complete to `C_a,C_b,C_2`.  In the adjacent-carrier auxiliary, the
literal terminal neighbourhoods are

\[
 N(t_a)=\{h,z_1,z_2\},\quad N(t_-)=\{z_1\},\quad
 N(t_b)=\{z_1,z_2\},\quad N(t_+)=\{z_2\}.
\]

The six vertices other than `h` have a rib with facial triangles

\[
 t_at_-z_1,\ t_-t_bz_1,\ t_bz_1z_2,\ t_bt_+z_2,
 t_+t_az_2,\ t_az_1z_2.
\]

The vertex `h` is in the cell behind `t_az_1z_2`; the edge `hz_2` is a
completion edge and is not literal.  Its whole external boundary is
`{z_1}` together with all `m` vertices of `C_a`.

For the consecutive-terminal cell, instead take

\[
 C_0=F[\{h,z\}]=hz,\qquad C_1=\{q\},\qquad zq\in E(F),
\]

make `h,z` complete to `C_a,C_4`, make `z` complete to `C_b`, and make `q`
complete to `C_a,C_b,C_2`.  The analogous rib has facial triangles

\[
 t_at_-z,\ t_-t_bz,\ t_bzq,\ t_bt_+q,\ t_+t_aq,\ t_azq,
\]

and `h` fills `t_at_-z`, with literal contacts to both consecutive terminal
owners.

In either construction, deleting at most four vertices leaves every `K_m`
column nonempty.  Those five surviving large columns have a connected
quotient, and every surviving carrier vertex is adjacent to a large column.
Thus the whole graph remains connected and is five-connected.  The displayed
web completions prove that the adjacent-carrier linkage is negative.  Hence
five-connectivity does not convert either surviving cell into a separator of
bounded order.

## 6. Exact tests of the strict-reduction gate

Let `H` be a one-sided component of `C_i-V(R)`.  Three natural operations can
be stated exactly, but none is automatic from bridge intervals.

1. **Deletion.**  The donor `C_i-H` is connected: it consists of `R` and the
   other components, each attached to `R`.  The two pole contacts survive on
   `R`, and the rim contact missed by `H` survives elsewhere.  A strict
   deletion still requires the other rim contact, an `A`--`B` path in the
   donor, five-connectivity of `F-H`, and the universal implication
   “`F-H` four-colourable only if `F` is four-colourable.”  Paired models
   lift automatically because `F-H` is a subgraph.
2. **Contraction.**  Contracting a nontrivial connected set `S` inside one
   column preserves connected columns, the quotient contacts, mapped root
   paths and the lift of a paired model.  Provided the contracted graph still
   has at least six vertices, it is five-connected precisely when there is no
   set `T` of at most three vertices outside `S` for which `F-(S\cup T)` is
   disconnected.  It additionally needs a four-colouring pullback over `S`.
3. **Reassignment.**  If `H` meets `C_{i-1}` and misses `C_{i+1}`, moving it
   from `C_i` to `C_{i-1}` preserves the exact quotient and connectedness of
   both columns.  It may destroy the donor's literal `A`--`B` path.  Even when
   it does not, the host graph, `A`, and `B` are unchanged, so no host-level
   parameter decreases; the reverse move can be equally legal.

### Proposition 6.1 (same form and model lifting do not pull back colour)

There is a five-connected one-sided bridge configuration for which deletion
and contraction both give the same five-connected, four-colourable
pentagonal-bipyramid expansion, while the original graph is not
four-colourable.

Give vertices subscripts in `{0,1,2,3}` and take

\[
\begin{array}{c|ccccccc}
\text{column}&C_a&C_b&C_0&C_1&C_2&C_3&C_4\\ \hline
\text{vertices}&\{a_1\}&\{b_0,b_1\}&\{r_0\}&
\{u_1,u_2,u_3\}&\{c_0\}&\{d_2\}&\{e_3\}.
\end{array}                                                    \tag{6.1}
\]

Form `D` by joining two vertices in the same column, or in columns adjacent
in the pentagonal bipyramid, exactly when their subscripts differ.  The
subscripts give a proper four-colouring.  The complement of `D` has maximum
degree four; its only vertex pair with three common complement-neighbours is
`{d_2,e_3}`, with common set `{u_1,u_2,u_3}`, and every other pair with at
least two has both vertices among `{u_1,u_2,u_3}` and common set contained in
`{d_2,e_3}`.  Hence every complete bipartite subgraph of the complement has
at most five vertices.  A cut of `D` of order at most four would partition
at least six remaining vertices into two anticomplete shores, giving a larger
complete bipartite subgraph of the complement.  Thus `D` is five-connected;
its minimum degree is five, so its connectivity is exactly five.

Add `h` to `C_0` adjacent exactly to

\[
                         r_0,u_1,u_2,u_3,a_1.                 \tag{6.2}
\]

Adding a vertex with at least five neighbours to a five-connected graph
preserves five-connectivity.  The graph `F` still has the exact column
quotient.  Moreover `F-h=D` and `F/r_0h=D`, because the four other neighbours
of `h` are already neighbours of `r_0`.  Taking

\[
 A=B=\{a_1,b_0,r_0,u_1,c_0,d_2,e_3\}
\]

preserves a singleton `A`--`B` path in every column under both operations,
and every paired model in the reduced graph lifts literally.  Nevertheless
`F` contains the `K_5` subgraph on `{r_0,h,u_1,u_2,u_3}`, so it is not
four-colourable.  Here `R={r_0}` is a shortest pole path and `{h}` is
one-sided.  The example is not a target counterexample: for the displayed
roots, one paired `K_5` model is

\[
 \{r_0\},\quad \{u_1\},\quad \{u_2,a_1\},\quad
 \{u_3,b_0\},\quad \{b_1,c_0\}.
\]

It proves that a valid strict reduction needs a new colour-extension
implication, not merely the structural and model-lifting invariants.

### Proposition 6.2 (five-connectivity is not inherited)

There is also a five-connected one-sided bridge configuration in which both
deletion and contraction destroy five-connectivity.

Take clique columns of orders

\[
 |C_a|=2,\ |C_b|=1,\ |C_0|=2,\ |C_1|=1,\ |C_2|=1,
 |C_3|=2,\ |C_4|=2
\]

with complete joins on every pentagonal-bipyramid edge.  Write
`C_a=\{a,a'\}`, `C_b=\{b\}`, `C_0=\{r,h\}`, `C_1=\{x\}`,
`C_2=\{y\}`, `C_3=\{p,p'\}` and `C_4=\{q,q'\}`.  Delete
`hq,hq'` and `xa'`.  Then `R=\{r\}` is a shortest pole path and
`H=\{h\}` meets `C_1` but misses `C_4`.

Put `K=F-\{h,x\}`.  The graph `K` is the join of (i) the disjoint union of
the edge `aa'` and isolated vertex `b`, and (ii) the two-connected clique path

\[
                  \{r\}-\{q,q'\}-\{p,p'\}-\{y\}.
\]

Deleting at most four vertices leaves this join connected.  Indeed, a
surviving pole vertex joins all surviving clique-path vertices; if all three
pole vertices are deleted, at most one clique-path vertex is deleted and
two-connectivity applies.  Thus `K` is five-connected.  Moreover

\[
 N_K(h)=\{r,a,a',b\},\qquad N_K(x)=\{r,a,b,y\},
\]

their union has order five, and `hx` is an edge.  These facts and
five-connectivity of `K` show directly that deleting at most four vertices
from `F` leaves it connected.  But in `F-h` the vertex `x` has degree four,
and the same is true after contracting `rh`.  Hence bridge geometry alone
does not imply five-contractibility or five-connectivity after deletion.
Taking `A=B` to contain one retained vertex of every column shows that all
seven literal root paths can survive while this condition fails.

Under a paired-negative hypothesis, the still-sufficient colour statement
would have to be: every nonextendible boundary colouring constructs a
paired-rooted model.  Without a proof from literal bridge data, that statement
is the original global allocation problem in another form.

## 7. Targeted finite evidence and its limit

The retained script
[`hc7_pb_bridge_mechanism_probe.py`](hc7_pb_bridge_mechanism_probe.py) uses
only the two already retained finite campaigns and two audited PB barriers.
Its invocation is

```text
.venv/bin/python active/hc7_pb_bridge_mechanism_probe.py
```

It verifies dependency hashes, all exact graph hypotheses at their stated
scope, and every positive five-bag certificate.  The fixed run covers 2,920
labelled PB frames and 15,320 shortest paths.  It finds 3,020 transfer paths,
2,300 alternating-split frames, 1,540 adjacent-linkage frames and 802
two-column-absorption frames.  It also finds 2,480 cases where the complete
adjacent-carrier Two Paths instance is positive although every tested
individual bridge/span rule is negative: 2,380 split one carrier bridge and
100 compose multiple carrier bridges.  In 6,320 laminar cases, deleting the
complete owner-column attachment set does not disconnect `F`.

Every frozen owner-column shortest path has at most one off-path component.
The run therefore examines no pair of owner-bridge intervals and has no power
to confirm or refute a crossing-versus-laminar pair theorem.  All counts are
computer-assisted finite evidence only; none is used as an unbounded premise.

## 8. Exact remaining proof gates

The desired bridge-chain theorem is not asserted here.  A proof must close
all of the following gates.

1. **Crossing gate.**  Decode a complete chain of typed bridges into the
   one-column Two Paths certificate, the audited adjacent-rim linkage, the
   audited two-column absorption, or another explicit paired-rooted `K_5`.
   Alternating convex hulls without distinct literal attachments and the
   needed disjoint routes do not suffice.
2. **Noncrossing gate.**  From failure of the complete linkage instance,
   obtain either a literal separation of `F` or a compatible collection of
   column societies whose composition embeds all of `F`.  A web confined
   to one column does not imply that `F` is planar.
3. **Colouring gate.**  A web outcome is terminal only after an embedding of
   all of `F`, and hence a four-colouring, or after verification of the exact
   hypotheses of a cited colour-extension theorem.
4. **Reduction gate.**  Any smaller instance must preserve
   five-connectivity, seven nonempty connected columns with the exact
   pentagonal-bipyramid contact graph, all seven literal `A`--`B` paths, a
   proved pullback of the four-colourable conclusion, and a lift of every
   paired model.  It
   must declare base cases and a strict well-founded parameter on `F`.

The audited
[`single-bridge span-inference barrier`](../barriers/hc7_single_bridge_span_inference_barrier.md)
shows why individual negative bridge tests do not establish the noncrossing
gate: several bridges can compose a positive Two Paths linkage even though
no bridge passes the proposed local test.  The audited
[`split/linkage/planarity barrier`](../barriers/hc7_pentagonal_bipyramid_split_linkage_planarity_barrier.md)
likewise shows that alternating splits and adjacent-rim linkages alone are
not exhaustive; its positive model uses the separately audited two-column
absorption mechanism.

Five-connectivity belongs to the whole graph `F`.  It does not turn two
endpoints of an interval in one column into a separator of `F`, because an
off-path component may have arbitrarily many literal neighbours in the four
adjacent columns.  Establishing the global consequence of (4.3), rather than
another local bridge taxonomy, is the theorem-strength unresolved step.
Sections 5 and 6 make it precise: one must couple the five negative
adjacent-carrier webs so that every surviving one- or two-owner cell is
either allocated in an explicit multi-column paired model, embedded together
with all literal edge bundles, or replaced by a smaller same-form host with a
proved universal colouring pullback.  None of the local web completion edges
supplies that operation.

The first irreducible case already has a precise form: a web cell behind
`{t_x,z_1,z_2}` whose literal external boundary contains at least three
vertices of the single owner column `C_x`.  The artificial terminal has
collapsed an unbounded recipient-column boundary.  Turning that boundary
into a label-preserving split, linkage, two-piece absorption, compatible
whole-`F` embedding, or strict colour-extending reduction is the remaining
theorem-strength inference.  The unbounded construction in Proposition 5.4
shows that five-connectivity and the local web order alone do not prove it.

## External structural source

- S. Humeau and D. Pous, *On the Two Paths Theorem and the Two Disjoint
  Paths Problem*, [arXiv:2505.16431](https://arxiv.org/abs/2505.16431),
  Definition 1.2 and Theorem 1.5.
- P. D. Seymour, *Disjoint paths in graphs*, *Discrete Mathematics* 29
  (1980), 293--309,
  [doi:10.1016/0012-365X(80)90158-2](https://doi.org/10.1016/0012-365X(80)90158-2).
