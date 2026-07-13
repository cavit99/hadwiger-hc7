# Four-connectivity, rooted diamonds, and the nested Moser carrier

## 1. The exact vertex-rooted theorem

For four distinct vertices \(x_1,x_2,x_3,x_4\), an
\(X\)-rooted \(K_4^-\)-model *missing* \(x_ix_j\) means four disjoint
connected bags \(B_1,B_2,B_3,B_4\), with \(x_k\in B_k\), such that
every two bags are adjacent except that adjacency between \(B_i\) and
\(B_j\) is not required.  The model is allowed to have that sixth
adjacency as well.

The following is a sharp corollary of the rooted-\(K_4\) theorem of
Fabila-Monroy and Wood.

### Theorem 1.1 (prescribed missing edge in a four-connected graph)

Let \(H\) be four-connected and let \(X=\{x_1,x_2,x_3,x_4\}\).
Exactly one of the following structural alternatives holds.

1. \(H\) has an \(X\)-rooted \(K_4\)-model.  In this case it has an
   \(X\)-rooted \(K_4^-\)-model with any prescribed missing pair.
2. \(H\) is planar and the four roots occur on one face.  Write their
   cyclic order as
   \[
                         x_1,x_2,x_3,x_4.                 \tag{1.1}
   \]
   Then \(H\) has a rooted \(K_4^-\)-model missing either prescribed
   opposite pair \(x_1x_3\) or \(x_2x_4\), and it has no rooted
   \(K_4^-\)-model missing any prescribed consecutive pair.

#### Proof

The rooted-\(K_4\) theorem says that a four-connected graph has an
\(X\)-rooted \(K_4\), unless it is planar with all four roots on one
face.  This gives alternative 1 and reduces the proof to alternative 2.

The planar embedding is unique up to reflection because \(H\) is
three-connected.  Add the edge \(x_1x_3\) through the common face.
The resulting graph is still four-connected and planar, but the added
edge separates \(x_2\) from \(x_4\) on that face; by uniqueness it has
no embedding with all four roots on one face.  The rooted-\(K_4\)
theorem therefore gives a rooted \(K_4\)-model in
\(H+x_1x_3\).  Since \(x_1,x_3\) lie in distinct rooted bags, the
new edge is either unused or is an edge between precisely those two
bags.  Delete it.  What remains in \(H\) is a rooted \(K_4^-\)-model
missing \(x_1x_3\).  The proof for \(x_2x_4\) is identical.

Suppose instead that a model missing the consecutive pair \(x_1x_2\)
existed.  The required \(B_1B_3\)-edge, together with connectedness of
the two bags, contains an \(x_1\)-\(x_3\) path in \(B_1\cup B_3\).
Similarly \(B_2\cup B_4\) contains an \(x_2\)-\(x_4\) path.  These two
paths are disjoint.  This is impossible in a plane graph when
\(x_1,x_2,x_3,x_4\) occur in alternating order on one face.  The other
three consecutive pairs are symmetric. \(\square\)

Thus the statement “every four-connected graph has a rooted diamond at
four prescribed vertices” is true only when the missing edge is allowed
to be chosen.  If the missing pair itself is prescribed, facial order is
the exact obstruction.

## 2. Sharpness examples

### Example 2.1 (the missing pair cannot be arbitrary)

Let \(A=C_8^2\), the square of the eight-cycle, and take the four even
vertices \(0,2,4,6\).  The graph \(A\) is the square-antiprism graph.
It is four-connected: deleting at most three cyclic positions cannot
create two gaps each containing two consecutive deleted vertices, which
would be necessary to disconnect a graph having all distance-one and
distance-two cycle edges.  Its four even vertices bound a square face.
Theorem 1.1 therefore gives diamonds missing either opposite pair and
forbids diamonds missing a consecutive pair.  This is a concrete
four-connected counterexample to arbitrary prescription of the missing
edge.

### Example 2.2 (a connected path cannot be prescribed as one bag)

Let
\[
                              A=P_4\vee I_3,                \tag{2.1}
\]
the join of a four-vertex path \(P\) and three independent vertices
\(a,b,c\).  The graph \(A\) is four-connected.  Indeed, after deleting
at most three vertices, either an independent vertex and a path vertex
both remain, in which case the join edges connect everything, or all
three independent vertices were deleted, in which case the surviving
\(P_4\) is connected.  Its minimum degree is four, so the connectivity
is exactly four.

Require one rooted bag to contain the whole path \(P\), and the other
three bags to contain \(a,b,c\), respectively.  There are no unused
vertices.  The only bag adjacencies are the three adjacencies from
\(P\) to \(a,b,c\); the latter are pairwise nonadjacent.  Hence there
is not even a rooted \(K_4^-\)-model.

Consequently one cannot contract a prescribed connected carrier and
silently reapply Theorem 1.1.  Edge contraction need not preserve
four-connectivity, and the connected-root version is false even when the
prescribed set induces a path.

## 3. The safe connected-carrier dichotomy

There is nevertheless an exact statement which records what can go
wrong under the contraction.

### Theorem 3.1 (rooted clique or carrier-centred adhesion)

Let \(F\) be four-connected, let \(P\subseteq F\) be connected, and
let \(a,b,c\notin P\) be distinct.  Put \(Q=F/P\), and let \(p\) be
the contraction vertex.  Assume \(|Q|\ge5\).  Then one of the following
holds.

1. \(Q\) is four-connected and has a rooted \(K_4\)-model at
   \(p,a,b,c\); this lifts to four pairwise adjacent connected bags in
   \(F\), one containing all of \(P\).
2. \(Q\) is four-connected and planar with \(p,a,b,c\) on one face.
   The precise rooted-diamond conclusions of Theorem 1.1 hold, in the
   facial cyclic order.
3. There is a set \(Y\subseteq V(F)-P\), with \(|Y|\le2\), such that
   \(F-(P\cup Y)\) is disconnected.  Moreover every component \(C\)
   of \(F-(P\cup Y)\) satisfies
   \[
                         |N_F(C)\cap P|\ge4-|Y|.            \tag{3.1}
   \]

#### Proof

If \(Q\) is four-connected, Theorem 1.1 (or, for the full-clique
dichotomy, the rooted-\(K_4\) theorem) gives outcomes 1 and 2.  A model
in \(Q\) lifts by replacing \(p\) in its bag with \(P\): all components
of that bag minus \(p\) attach to the connected set \(P\), so the
expanded bag is connected.

Suppose \(Q\) is not four-connected and let \(X\) be a separator of
order at most three.  Necessarily \(p\in X\).  Otherwise \(F-X\) is
connected by four-connectivity, and contracting the still-present set
\(P\) would show that \(Q-X\) is connected.  Put
\(Y=X-\{p\}\).  Then \(|Y|\le2\), and
\[
                         Q-X=F-(P\cup Y)
\]
is disconnected.  For any component \(C\) of this graph, all its
neighbours lie in \(P\cup Y\).  Since another component remains,
\(N_F(C)\) separates \(F\); four-connectivity gives
\(|N_F(C)|\ge4\), and (3.1) follows. \(\square\)

Outcome 3 is the exact information lost on contracting \(P\).  For a
path carrier, it is a two-shore (or multi-shore) portal state: after at
most two exceptional vertices are removed, every shore has at least
\(4-|Y|\) distinct attachments on the path.

## 4. Application to the nested degree-nine Moser shore

Use the notation of `hadwiger_degree9_terminal_root_swap.md`.  Thus
\(G\) is seven-connected, \(F=G-\{h,1,2\}\) is four-connected,
\(e_6\in Z\), \(e_0\in J\), and \(U=Z\cup J\) is connected.  Let
\(r_5\) be the prescribed exterior root in \(R_5\), and choose any path
\[
                 P\subseteq D\cup R_5\quad\hbox{from }6
                 \hbox{ to }r_5.                            \tag{4.1}
\]
Such a path exists because \(D\) is connected and contains \(6\),
\(R_5\) is connected and contains both \(5,r_5\), and \(65\) is an
edge.  Put \(Q=F/P\), with contraction vertex \(p\).

### Corollary 4.1 (every carrier exposes an adhesion)

If \(G\) has no \(K_7\)-minor, then, for **every** choice of \(P\) in
(4.1), there is a set
\[
             Y_P\subseteq V(F)-P,\qquad |Y_P|\le2,          \tag{4.2}
\]
such that \(F-(P\cup Y_P)\) is disconnected.  Every component \(C\)
of that graph has
\[
                         |N_F(C)\cap P|\ge4-|Y_P|.           \tag{4.3}
\]

#### Proof

Apply Theorem 3.1 to \(P,e_6,e_0,v\).  If outcome 1 there gives a
rooted \(K_4\), lift it to \(F\).  The four lifted bags are each
adjacent to all of \(h,1,2\): the \(e_6\)- and \(e_0\)-bags use their
exterior roots; the \(v\)-bag uses \(v\); and the \(P\)-bag uses
\(r_5\) for its \(h\)-edge and \(6\) for its edges to \(1,2\).
Together with the triangle \(\{h\},\{1\},\{2\}\), they form a
\(K_7\)-model, contrary to hypothesis.

The planar outcome of Theorem 3.1 is impossible here as well.  In the
quotient \(Q\), the four vertices
\[
                              p,v,3,4                        \tag{4.4}
\]
induce a \(K_4\): use \(6v\), the two edges from the right exterior
root \(r_5\) to \(3,4\), and the Moser triangle edges
\(v3,v4,34\).  A four-connected planar graph with more than four
vertices cannot contain a \(K_4\) subgraph.  Indeed, in a plane
embedding of that \(K_4\), any additional vertex lies in one of its
four triangular regions, whose boundary separates it from the fourth
\(K_4\)-vertex.  That boundary is a three-vertex cut.  The distinct
vertices \(e_6,e_0\) show that \(|Q|>4\).  Thus \(Q\) cannot be both
four-connected and planar.

Only outcome 3 of Theorem 3.1 remains, and it gives (4.2)--(4.3).
\(\square\)

This is stronger than a crossed-frame dichotomy: the fixed Moser
triangle kills the crossed-frame branch before any rotation analysis is
needed.  It is genuinely structural and applies to carriers of arbitrary
length.  The remaining work is now concentrated in one exact object:
for every \(6\)-to-\(r_5\) carrier path, a set of at most two exceptional
vertices separates at least two shores, each with the forced portal load
(4.3).  This is precisely the setting for a two-shore capacity-state
exchange along an ordered path.

### Lemma 4.2 (first-failure exact prefix state)

Orient a path in (4.1) as
\[
                         P=x_0x_1\cdots x_m,\qquad
                         x_0=6,\quad x_m=r_5.               \tag{4.5}
\]
In a \(K_7\)-minor-free nested state there is an index
\(i\in\{1,\ldots,m\}\) and two vertices \(y_i,z_i\notin
P[0,i]\) such that
\[
                  F-\bigl(P[0,i]\cup\{y_i,z_i\}\bigr)     \tag{4.6}
\]
is disconnected.  Moreover:

1. \(F/P[0,i-1]\) is four-connected;
2. after contracting \(P[0,i-1]\) to \(p_{i-1}\), the set
   \[
                         \{p_{i-1},x_i,y_i,z_i\}            \tag{4.7}
   \]
   is an exact four-vertex separator; and
3. every component \(C\) of (4.6) has at least two distinct neighbours
   in \(P[0,i]\).  More precisely, if
   \[
             \lambda(C)=|N_G(C)\cap\{h,1,2\}|,
   \]
   then
   \[
             |N_F(C)\cap P[0,i]|\ge5-\lambda(C).          \tag{4.7a}
   \]

The same assertion holds after orienting \(P\) from \(r_5\) to \(6\).

#### Proof

Put \(P_i=P[0,i]\) and \(F_i=F/P_i\).  The graph \(F_0=F\) is
four-connected, whereas \(F_m=F/P\) is not four-connected by
Corollary 4.1.  Let \(i\) be the first index for which \(F_i\) is not
four-connected.  In the four-connected graph \(F_{i-1}\), the graph
\(F_i\) is obtained by contracting the edge
\(p_{i-1}x_i\).

We use the elementary contractible-edge criterion.  If an edge \(ab\)
of a four-connected graph \(L\) has \(L/ab\) not four-connected, take
a separator \(X\) of \(L/ab\) of order at most three.  The contraction
vertex belongs to \(X\), since otherwise lifting \(X\) would contradict
four-connectivity of \(L\).  Replacing that vertex by \(a,b\) gives a
separator of \(L\) of order at most four.  Four-connectivity forces its
order to be exactly four.  Thus \(|X|=3\), and the lifted separator is
\(\{a,b,y,z\}\) for two vertices \(y,z\).

Apply this criterion in \(F_{i-1}\).  It gives (4.7), and lifting the
contracted prefix gives (4.6).  If \(C\) is a component of (4.6), then
\(N_F(C)\subseteq P_i\cup\{y_i,z_i\}\).  Its neighbourhood separates
the four-connected graph \(F\), so it has order at least four.  At most
two of its members are \(y_i,z_i\); hence \(C\) has at least two
distinct neighbours in \(P_i\).  In the original graph,
\[
             N_G(C)\subseteq P_i\cup\{y_i,z_i,h,1,2\}.
\]
Seven-connectivity of \(G\) therefore gives
\(|N_F(C)\cap P_i|+2+\lambda(C)\ge7\), which is (4.7a).
Reversing the path proves the final assertion. \(\square\)

Lemma 4.2 is the ordered form of the carrier adhesion.  It does not say
that the whole prefix is a bounded separator; rather, after the prefix
is contracted, the obstruction is an exact four-cut containing the next
carrier edge.  This is precisely the state on which a prefix exchange or
a port-order argument can act without assuming that contraction
preserves connectivity.

### Lemma 4.3 (prefix near-\(K_7\) and a dirty suffix)

Retain the first-failure index \(i\) of Lemma 4.2, and put
\[
             L=F/P[0,i-1],\qquad p=P[0,i-1]/P[0,i-1].      \tag{4.8}
\]
Then \(L\) has a rooted \(K_4\)-model at
\(p,e_6,e_0,v\).  On lifting to \(G\), this model together with
\(\{h\},\{1\},\{2\}\) is a \(K_7^-\)-model whose only possibly
missing adjacency is the edge from \(h\) to the bag containing the
contracted prefix.

Let
\[
                         R=x_i x_{i+1}\cdots x_m            \tag{4.9}
\]
be the uncontracted suffix.  In a \(K_7\)-minor-free graph, every such
rooted \(K_4\)-model has
\[
        V(R)\cap(B_{e_6}\cup B_{e_0}\cup B_v)\ne\varnothing. \tag{4.10}
\]
Moreover, if \(x_j\) is the first vertex of \(R\) in one of those three
bags, the model can be normalized so that
\[
                 x_i,\ldots,x_{j-1}\in B_p,\qquad
                 x_j\in B_{e_6}\cup B_{e_0}\cup B_v.      \tag{4.11}
\]
Thus the edge \(x_{j-1}x_j\) (or \(px_i\) when \(j=i\)) is a literal
first dirty transition from the prefix bag into another rooted bag.

#### Proof

The graph \(L\) is four-connected by choice of \(i\).  It is nonplanar.
Indeed, before the prefix reaches \(5\), the vertices \(v,3,4,5\)
induce a \(K_4\).  Once \(5\) belongs to the contracted prefix, the
vertices \(p,v,3,4\) induce a \(K_4\), using the edges from \(5\) to
\(3,4\) and from \(6\) to \(v\).  In either case \(L\) has vertices
outside this \(K_4\), including \(e_6,e_0\); as in Corollary 4.1, a
four-connected planar graph of order greater than four cannot contain a
\(K_4\) subgraph.

The rooted-\(K_4\) theorem now gives a rooted model
\((B_p,B_{e_6},B_{e_0},B_v)\).  Expand \(p\) back to the prefix.
The last three bags see all of \(h,1,2\) at their roots, while the
prefix bag sees \(1,2\) through \(6\).  Hence the seven displayed bags
form the asserted \(K_7^-\).  If the prefix bag already sees \(h\), it
is a \(K_7\)-model.

Suppose (4.10) fails.  Add the whole suffix \(R\) to the prefix bag.
It remains connected through \(x_{i-1}x_i\), stays disjoint from the
other three rooted bags, and now contains \(r_5\), which is adjacent to
\(h\).  This repairs the only missing adjacency and gives \(K_7\), a
contradiction.  Finally, before the first hit \(x_j\), all suffix
vertices are either unused or already in \(B_p\).  Absorbing all of
them into \(B_p\) preserves connectedness and disjointness and gives
(4.11). \(\square\)

The exact four-cut of Lemma 4.2 contains \(p,x_i\).  Thus (4.11) has
two sharply different forms: either the dirty hit occurs immediately at
the uncontractible cut edge, or both endpoints of that cut edge can be
put in the prefix bag and the first dirty transition occurs farther down
the suffix.  This is the precise point at which the four-cut state and
the rooted-minor state have to be synchronized.

### Lemma 4.4 (four-cut component localization)

Let
\[
                         T=\{p,x_i,y_i,z_i\}                \tag{4.12}
\]
be the exact four-cut in \(L\).  Every component of \(L-T\) is adjacent
to every vertex of \(T\).

Suppose the three roots \(e_6,e_0,v\) lie in three distinct components
of \(L-T\), and none lies in \(T\).  In a \(K_7\)-minor-free state,
\(r_5\) either lies in \(T\) or lies in one of those three rooted
components.  Equivalently, a fourth, root-free \(T\)-component cannot
contain \(r_5\).

#### Proof

If a component \(C\) of \(L-T\) missed a member of \(T\), then
\(N_L(C)\) would have order at most three and would separate the
four-connected graph \(L\).  Hence every component is full to \(T\).

Let \(C_6,C_0,C_v\) be the three rooted components, and suppose a
fourth component \(C_5\) contains \(r_5\).  The following four sets are
pairwise adjacent and connected:
\[
 \{p,x_i\}\cup C_5,\qquad
 C_6\cup\{y_i\},\qquad
 C_0\cup\{z_i\},\qquad
 C_v.                                                       \tag{4.13}
\]
Fullness to \(T\) supplies every cross-adjacency: the first set sees all
three rooted components through \(p\) or \(x_i\); the second and third
are adjacent through a \(C_6z_i\)- or \(C_0y_i\)-edge; and the unanchored
component \(C_v\) sees both \(y_i,z_i\).  The first set contains the
prefix (hence \(6\)) and \(r_5\), while the other three contain
\(e_6,e_0,v\).  Therefore all four sets see each of \(h,1,2\), and
adjoining the singleton triangle gives a \(K_7\)-model. \(\square\)

The qualifications in Lemma 4.4 are necessary bookkeeping, not cosmetic.
If a protected root equals \(y_i\) or \(z_i\), or if two protected roots
lie in one \(T\)-component, (4.13) is not a four-root packing.  The exact
remaining localization alternatives are therefore:

* a protected root lies in \(\{y_i,z_i\}\);
* two protected roots share a \(T\)-component;
* \(r_5\in\{x_i,y_i,z_i\}\); or
* \(r_5\) shares a \(T\)-component with one of \(e_6,e_0,v\).

This finite list is the correct interface for the dirty-suffix theorem;
claiming unconditionally that \(r_5\) shares a component with a root
would silently omit the cut-vertex cases.

### Theorem 4.5 (central edge: dirty routing or a full seven-adhesion)

Put \(P_{65}=\{6,5\}\) and \(Q_{65}=F/65\), with contraction vertex
\(p\).  In a \(K_7\)-minor-free nested state, exactly one of the
following two structural outcomes occurs.

1. There are vertices \(y,z\notin\{h,1,2,5,6\}\) such that
   \[
                    S=\{h,1,2,5,6,y,z\}                   \tag{4.15}
   \]
   is a seven-vertex cut of \(G\).  Every component of \(G-S\) is
   adjacent to every vertex of \(S\).
2. The graph \(Q_{65}\) is four-connected and has a rooted
   \(K_4\)-model at \(p,e_6,e_0,v\).  For every such model and every
   \(5\)-\(r_5\) path \(R\subseteq R_5\), the part
   \(R-5\) meets at least one of the three bags rooted at
   \(e_6,e_0,v\).  Equivalently, there is no rooted model with a
   reserved clean \(5\)-\(r_5\)-\(h\) connector.

#### Proof

Apply Theorem 3.1 to the connected set \(\{6,5\}\).  If \(Q_{65}\)
is not four-connected, outcome 3 gives a set \(Y\) of order at most
two such that \(F-(\{6,5\}\cup Y)\) is disconnected, and every
component has at least \(4-|Y|\) distinct neighbours in
\(\{6,5\}\).  Since the latter set has only two vertices, this forces
\(|Y|=2\); write \(Y=\{y,z\}\).  Deleting (4.15) from \(G\) leaves
the same disconnected graph.  Seven-connectivity makes \(S\) an exact
minimum cut.  If a component of \(G-S\) missed one member of \(S\),
its neighbourhood would have order at most six, a contradiction.
This proves outcome 1.

Suppose \(Q_{65}\) is four-connected.  Its vertices \(p,v,3,4\)
induce a \(K_4\), and it has the additional vertices \(e_6,e_0\).
Thus it is nonplanar by the triangular-region argument of Corollary
4.1.  The rooted-\(K_4\) theorem gives the model in outcome 2.  On
lifting it to \(F\), the bag rooted at \(p\) contains \(5,6\), so it
sees \(1,2\), while the other three rooted bags see all of \(h,1,2\).
Together with the singleton triangle this is a \(K_7^-\), with only
the \(h\)-to-\(p\)-bag adjacency possibly absent.

If a path \(R\subseteq R_5\) from \(5\) to \(r_5\) avoided the other
three rooted bags, absorb \(R-5\) into the \(p\)-bag.  This preserves
connectedness and disjointness and supplies the missing edge through
\(r_5h\), producing a \(K_7\)-model.  Hence every such path is dirty,
as claimed. \(\square\)

Outcome 1 is substantially stronger than the generic carrier adhesion:
the carrier has collapsed to the actual Moser edge \(56\), the two
exceptional vertices are forced, and lifting restores a full exact
seven-adhesion in \(G\).  Outcome 2 is the complementary rooted-minor
state.  Since \(56\) is an actual edge of the contraction-critical
graph, its one-step colouring transition can now be synchronized with
either a full seven-boundary state or a first dirty hit in \(R_5\).

### Corollary 4.6 (the full adhesion has at most three shores)

In outcome 1 of Theorem 4.5, \(G-S\) has at most three components.

#### Proof

If \(C_1,C_2,C_3,C_4\) were four components, use the seven bags
\[
 \{1\},\quad\{2\},\quad\{6\},\quad
 C_1\cup\{h\},\quad C_2\cup\{5\},\quad
 C_3\cup\{y\},\quad C_4\cup\{z\}.                         \tag{4.16}
\]
The first three form a triangle through \(12,16,26\).  Each of the
last four bags is connected because its component is full to \(S\).
Any two of those four bags are adjacent: the component in either bag
has a neighbour at the boundary vertex in the other.  Each is also
adjacent to \(1,2,6\), again by fullness.  Thus (4.16) is a
\(K_7\)-model. \(\square\)

So the exact-boundary branch is not an unbounded component enumeration:
it consists of two or three full shores (one shore is impossible because
\(S\) is a cut), together with the one-step \(56\)-transition.

## 5. Path deletion and the exact portal ladder

The contraction condition has a clean path-deletion formulation.

### Lemma 5.1 (contraction/deletion equivalence)

Let \(F\) be four-connected and \(P\subseteq F\) connected, with enough
vertices remaining for the stated connectivities.  Then
\[
             F/P\text{ is four-connected}
             \quad\Longleftrightarrow\quad
             F-V(P)\text{ is three-connected}.             \tag{5.1}
\]

#### Proof

If \(F/P\) is four-connected, deleting its contraction vertex leaves a
three-connected graph, namely \(F-V(P)\).

Conversely, put \(Q=F/P\), with contraction vertex \(p\), and suppose
\(F-V(P)\) is three-connected.  A separator \(X\) of \(Q\) of order at
most three cannot avoid \(p\), since then \(F-X\) is connected and its
contraction is \(Q-X\).  If \(p\in X\), write
\(X=\{p\}\cup Y\), where \(|Y|\le2\).  Then
\[
                         Q-X=(F-V(P))-Y
\]
is connected by three-connectivity.  Thus no such separator exists.
\(\square\)

### Corollary 5.2 (no three-connected carrier remainder)

In a \(K_7\)-minor-free nested Moser state, for every path \(P\) in
(4.1),
\[
                              F-V(P)\text{ is not
                              three-connected}.             \tag{5.2}
\]

Indeed, otherwise Lemma 5.1 and Corollary 4.1 would give a
four-connected quotient, hence the rooted \(K_4\) and a \(K_7\)-model.

The failure in (5.2) has a precise connectivity hierarchy.  Put
\(H=F-V(P)\).

### Lemma 5.3 (loaded \(0/1/2\)-cut hierarchy)

Let \(C\) be one of the following shores.

* If \(H\) is disconnected, let \(C\) be a component of \(H\), and put
  \(k=0\).
* If \(H\) is connected but not two-connected, let \(t\) be a cutvertex
  and let \(C\) be a component of \(H-t\); put \(T=\{t\}\) and \(k=1\).
* If \(H\) is two-connected but not three-connected, let
  \(T=\{y,z\}\) be a two-cut and let \(C\) be a component of \(H-T\);
  put \(k=2\).

Then \(C\) is adjacent to every vertex of \(T\), and, writing
\[
                      \lambda(C)=|N_G(C)\cap\{h,1,2\}|,
\]
one has
\[
                   |N_F(C)\cap V(P)|
                      \ge 7-k-\lambda(C)\ge4-k.             \tag{5.3}
\]

#### Proof

For \(k=1\), connectedness of \(H\) makes every component of \(H-t\)
adjacent to \(t\).  For \(k=2\), if a component of \(H-\{y,z\}\)
missed \(y\) or \(z\), the other vertex would be a cutvertex of the
two-connected graph \(H\).  The assertion is empty for \(k=0\).

All neighbours of \(C\) lie in
\[
                       V(P)\cup T\cup\{h,1,2\}.
\]
Since another shore remains, this neighbourhood separates the
seven-connected graph \(G\), and hence has order at least seven.
This gives the first inequality in (5.3); the second uses
\(\lambda(C)\le3\). \(\square\)

The cuts in Lemma 5.3 have a standard laminar packaging.  In the
connected, non-two-connected case they are organized by the block-cut
tree, every leaf lobe carrying at least three \(P\)-portals (and more
when \(\lambda<3\)).  In the two-connected, non-three-connected case,
the two-separations are organized by the SPQR tree; every displayed
two-shore bridge is full to its two gate vertices and carries at least
two \(P\)-portals.  Thus (5.2) is not an unstructured failure: every
carrier produces a loaded \(0/1/2\)-cut tree.

Kawarabayashi--Lee--Yu, *Non-Separating Paths in 4-Connected Graphs*,
Theorem 1.2, prove that, for prescribed vertices \(u,v\) in a
four-connected graph, there is a \(u\)-\(v\) path whose deletion
leaves a two-connected graph, unless the graph is a double wheel with
centre \(\{u,v\}\).  (Their Theorem 2.3 is only an intermediate,
weaker induced-path statement; Theorem 3.5 supplies the upgrade used
in Theorem 1.2.)  Their path is unrestricted: it need not lie in
\(D\cup R_5\), nor avoid \(e_6,e_0,v,3,4\).  Consequently it cannot
yet be substituted for the carrier in Corollary 4.1.  A
carrier-confinement (or protected-avoidance) lemma would, however,
eliminate the \(0\)- and \(1\)-cut rows and leave only the loaded SPQR
two-cut tree.

Demanding a three-connected remainder is not a legitimate use of the
known nonseparating-path theorem.  Four-connectivity does not suffice:
if \(u,v\) are the centres of a double wheel, deletion of every
\(u\)-\(v\) path leaves a subgraph of the ring and never a
three-connected graph.  More generally, the Lovasz path-removal
conjecture is unresolved for three-connected remainders.  The rigorous
next target on this route is therefore a carrier-confined
two-connected remainder or an exchange that shortens the loaded
\(0/1/2\)-cut tree.

## 6. The important bookkeeping correction

A rooted diamond in \(F\), joined to the three singleton bags
\(h,1,2\), is only \(K_3\vee K_4^-=K_7^-\).  It is not by itself a
\(K_7\)-model.  It yields \(K_7\) only when the nominally missing pair
has an independently guaranteed edge (for example the \(pv\)-edge in
the opposite-pair facial order).  The full rooted \(K_4\) in
Corollary 4.1 is what lifts directly.
