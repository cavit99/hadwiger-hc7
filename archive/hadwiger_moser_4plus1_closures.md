# Two rigorous closures in the pure-Moser four-plus-one cell

## 1. Setup

Let \(G\) be a proper-minor-minimal counterexample to \(\mathrm{HC}_7\),
let \(d(v)=7\), and suppose

\[
 G-N[v]=C_1\mathbin{\dot\cup}C_2,
 \qquad G[N(v)]\cong M,
\]

where

\[
 E(M)=\{01,02,03,04,12,16,26,34,35,45,56\}.
\]

We use the standard counterexample consequence that \(G\) is
seven-connected.  Since \(|N|=7\), this implies
\(N_G(C_1)=N_G(C_2)=N\): a smaller boundary neighbourhood would be a
vertex cut of order at most six separating that exterior component from
\(v\).

Use the exact-trace colouring with repeated pair \(13\).  Put

\[
 U=\{0,2,4,5,6\},
 \qquad F=05,52,24,46,60.
\]

Suppose one side, say \(C_1\), supports four edges of \(F\), and write
\(e=xy\) for the omitted edge.  Kriesell--Mohr's pseudoforest theorem,
applied in \(G[U\cup C_1]\) to the path \(F-e\), gives five disjoint
rooted bags

\[
 \mathcal B=(B_u:u\in U)
\]

which are pairwise adjacent except possibly \(B_x,B_y\).  Indeed, the
four certificate adjacencies are the edges of \(F-e\), and the five
edges of \(M[U]=\overline F\) supply all complementary adjacencies.

The arguments below do not assume that \(C_2\) supports only \(e\).
They therefore remain valid when some of the four majority edges are
bi-supported.

## 2. The reserved-linkage certificate

### Lemma 2.1

If \(G[C_2\cup\{1,3,x,y\}]\) contains vertex-disjoint paths \(R,Q\),
where \(R\) has ends \(1,3\), \(Q\) has ends \(x,y\), and both paths
have all internal vertices in \(C_2\), then \(G\) has a \(K_7\)-minor.

### Proof

Split \(Q\) at an edge into two adjacent connected subpaths \(Q_x,Q_y\)
containing \(x,y\), respectively.  Replace

\[
 B_x\longmapsto B_x\cup Q_x,
 \qquad B_y\longmapsto B_y\cup Q_y.
\]

These bags are connected, disjoint, and now adjacent.  All their old
adjacencies remain.  The path \(R\) is disjoint from the five bags.  For
each \(u\in U\), at least one of \(1u,3u\) is an edge of \(M\), since
otherwise \(\{1,3,u\}\) would be independent in \(M\).  Hence \(R\)
is adjacent to every rooted bag.  The five modified rooted bags and
\(R\) are an \(N\)-meeting \(K_6\)-model in \(G-v\); add \(\{v\}\).
\(\square\)

This is the precise reserved-connector statement.  The ordinary
two-linkage, rather than four confined certificate edges alone, is what
repairs the fifth adjacency while preserving a sixth bag.

## 3. Two minority positions close without linkage

### Lemma 3.1 (common-neighbour closure)

If \(e\in\{05,06\}\), then \(G\) has a \(K_7\)-minor.

### Proof

For \(e=05\), vertex \(3\) is adjacent to both \(0,5\).  Absorb \(3\)
into \(B_0\).  This keeps that bag connected and creates its missing
adjacency to \(B_5\).  The set

\[
 D=C_2\cup\{1\}
\]

is connected because \(N(C_2)=N\), and it is adjacent to every rooted
bag because \(C_2\) has a neighbour at every root in \(U\).  Thus the
five rooted bags and \(D\) form an \(N\)-meeting \(K_6\)-model.

For \(e=06\), absorb the common neighbour \(1\) into \(B_0\), and use
\(C_2\cup\{3\}\) as the sixth bag.  Add \(\{v\}\) in both cases.
\(\square\)

Thus only the physical minority positions

\[
 25,\quad24,\quad46                                      \tag{3.1}
\]

survive this lemma.  This statement is about the fixed numerical Moser
labelling.  One must not quotient (3.1) by the full dihedral symmetry of
the abstract five-cycle: only the reflection of the cycle is induced by
an automorphism of \(M\) stabilising the repeated pair \(\{1,3\}\).

## 4. Every cutvertex minority component closes

### Lemma 4.1 (cutvertex closure)

For any \(e\in E(F)\), if \(C_2\) has a cutvertex, then \(G\) has a
\(K_7\)-minor.

### Proof

Let \(z\) be a cutvertex and let \(D\) be one component of \(C_2-z\).
Put \(E=C_2-D\).  Every component of \(C_2-z\) has a neighbour at \(z\),
so \(D,E\) are disjoint connected sets and an edge joins them.  There is
another component of \(C_2-z\) contained in \(E\).

Seven-connectivity gives

\[
 |N_G(D)|\ge7.
\]

But \(N_G(D)\subseteq N\cup\{z\}\), so \(D\) has neighbours at at
least six vertices of \(N\).  Applying the same argument to a component
of \(C_2-z\) contained in \(E\) shows that \(E\) also has neighbours at
at least six vertices of \(N\).  Each of \(D,E\) consequently has either
no boundary defect or one boundary defect.  If both have defects, they
are distinct, because \(D\cup E=C_2\) and \(N(C_2)=N\).

Choose one endpoint \(o\) of \(e\) and retain the four rooted bags

\[
 B_u\quad(u\in R:=U-\{o\}).
\]

They form a rooted \(K_4\), since the only possibly missing adjacency
among the five bags was the edge \(e\), and one end of \(e\) was omitted.
The unused boundary vertices are

\[
 A=\{1,3,o\}.
\]

We next choose distinct anchors \(a_D,a_E\in A\).  An anchor assigned to
a shore must differ from that shore's defect, so that it has a neighbour
in the shore.  If the shore misses a retained root \(u\), its anchor is
also required to be adjacent to \(u\) in \(M\).  The following finite
table proves that the anchors can always be chosen.  An empty entry means
there is no ordered pair of distinct shore defects for which the choice
fails.

\[
\begin{array}{c|c|c|c}
e&o&A&\text{exceptional ordered defect pairs}\\ \hline
05&0&\{0,1,3\}&\varnothing\\
25&5&\{1,3,5\}&\varnothing\\
24&2&\{1,2,3\}&(4,5),(5,4)\\
24&4&\{1,3,4\}&(2,6),(6,2)\\
46&6&\{1,3,6\}&\varnothing\\
06&0&\{0,1,3\}&\varnothing
\end{array}                                               \tag{4.1}
\]

For \(e=24\), use \(o=4\) for either ordered pair in the first
exceptional list and \(o=2\) otherwise; the two exceptional lists are
disjoint.  Table (4.1) is a
direct check from

\[
\begin{aligned}
N_M(0)&=\{1,2,3,4\},&N_M(2)&=\{0,1,6\},\\
N_M(4)&=\{0,3,5\},&N_M(5)&=\{3,4,6\},\\
N_M(6)&=\{1,2,5\}.&&
\end{aligned}
\]

The dependency-free script `moser_cutvertex_assignment_verify.py`
checks all possible defects, including a defect in \(A\) or no defect.

Now put

\[
 J_D=D\cup\{a_D\},\qquad J_E=E\cup\{a_E\}.
\]

Both sets are connected, they are adjacent to one another, and each is
adjacent to all four retained rooted bags.  Moreover, both contain a
vertex of \(N\).  Therefore

\[
 \{B_u:u\in R\}\cup\{J_D,J_E\}
\]

is an \(N\)-meeting \(K_6\)-model in \(G-v\).  Add \(\{v\}\).
\(\square\)

## 5. A finite closure for two-cuts

### Lemma 5.1 (two-cut anchor closure)

Suppose the minority component has no cutvertex but has a two-vertex cut.
Choose one component behind the cut and split the cut vertices between the two
sides in the standard way.  This gives disjoint, connected, adjacent
sets \(J_1,J_2\) whose union is \(C_2\).  Each \(J_i\) has neighbours at
at least five vertices of \(N\).  Consequently its defect set

\[
 \Delta_i=N-N_N(J_i)
\]

has order at most two, and \(\Delta_1\cap\Delta_2=\varnothing\).

For \(f=25,24,46\), retain four root bags by omitting either endpoint
of \(f\), and partition the three unused boundary vertices
\(\{1,3,o\}\) between \(J_1,J_2\), giving each side at least one anchor.
Exactly as in Lemma 4.1, this produces an \(N\)-meeting \(K_6\)-model
unless the unordered pair \(\{\Delta_1,\Delta_2\}\) occurs in the
following table.  A string such as \(12\) denotes the set \(\{1,2\}\).

\[
\begin{array}{c|l}
f&\text{unordered residual defect pairs}\\ \hline
25&
[2|35],[4|12],[5|12],[02|35],[04|12],[05|12],
[12|34],[12|35],[12|45],[12|46],[12|56],
[16|34],[24|35],[24|56],[26|35]\\[2mm]
24&
[2|34],[4|12],[5|12],[6|34],[02|34],[04|12],
[05|12],[06|34],[12|34],[12|35],[12|45],[12|46],
[12|56],[16|34],[16|35],[24|56],[25|34],[25|46],
[26|34],[34|56]\\[2mm]
46&
[2|34],[4|16],[6|34],[02|34],[04|16],[06|34],
[12|34],[12|35],[16|24],[16|34],[16|45],
[24|56],[25|34],[26|34],[34|56].
\end{array}                                               \tag{5.1}
\]

#### Proof

Let the two-cut be \(\{z_1,z_2\}\).  Since \(C_2\) has no cutvertex,
every component of \(C_2-\{z_1,z_2\}\) has a neighbour at both cut
vertices.  Put \(J_1=D\cup\{z_1\}\) for one such component \(D\), and
put \(J_2=C_2-J_1\).  These sets are connected and adjacent.  For \(D\),
seven-connectivity and

\[
 N_G(D)\subseteq N\cup\{z_1,z_2\}
\]

give \(|N_N(D)|\ge5\).  A second component on the other side gives the
same bound for \(J_2\).  Full attachment gives disjoint defect sets.

For any fixed omitted endpoint \(o\), assign each of \(1,3,o\) either
to \(J_1\), to \(J_2\), or leave it unused.  Both shores must receive an
anchor.  An assigned anchor may not lie in that shore's defect set, and
every missed retained root must be adjacent in \(M\) to an anchor
assigned to its shore.  Whenever such an assignment exists, absorbing
the anchors gives two adjacent \(N\)-meeting helper bags, each complete
to the four retained root bags, exactly as in Lemma 4.1.

There are only

\[
 \sum_{i=0}^2\binom7i=29
\]

possible defect sets for either shore.  Checking the two endpoint
choices, both shore orders, and the \(3^3\) anchor assignments gives
precisely (5.1).  The dependency-free exhaustive verifier
moser_2cut_assignment_verify.py records the complete check.  Thus
every two-cut instance outside the displayed 50 physical defect pairs
is eliminated. \(\square\)

This lemma does not yet prove that \(C_2\) is three-connected: the
displayed defect pairs must still be combined with the bi-supported
majority path and the minority path.  It does, however, eliminate the
entire complementary family of two-cut geometries by explicit branch
sets.

### Lemma 5.2 (full quotient-model strengthening)

Allowing the rooted bags and the two shores to be combined more flexibly
eliminates a further seventeen entries of (5.1).  The exact residual is

\[
\begin{array}{c|l}
f&\text{unordered residual defect pairs}\\ \hline
25&
[2|35],[5|12],[02|35],[05|12],[12|35],[12|45],
[12|56],[16|34],[24|35],[24|56],[26|35]\\[2mm]
24&
[2|34],[4|12],[02|34],[04|12],[12|34],[12|45],
[12|46],[16|35],[25|34],[25|46],[26|34]\\[2mm]
46&
[4|16],[6|34],[04|16],[06|34],[12|35],[16|24],
[16|34],[16|45],[24|56],[26|34],[34|56].
\end{array}                                               \tag{5.2}
\]

#### Proof

For a defect pair \((\Delta_1,\Delta_2)\), form the nine-vertex quotient
\(L(f,\Delta_1,\Delta_2)\).  Its vertices are the seven boundary/root
vertices and two vertices \(h_1,h_2\) representing the connected shores.
The five vertices of \(U\) induce \(K_5-f\), the original Moser edges are
retained, \(h_1h_2\) is an edge, and

\[
 N_L(h_i)\cap N=N-\Delta_i.
\]

Every \(N\)-meeting \(K_6\)-model in this quotient lifts to the original
graph: replace \(h_i\) by \(J_i\), and replace each root vertex of \(U\)
by its rooted bag.  Connectivity and every quotient adjacency are
preserved by construction.

There are only nine quotient vertices.  The dependency-free verifier
moser_2cut_quotient_verify.py enumerates every used vertex subset and
every set partition into six nonempty branch bags; it requires every bag
to meet \(N\), verifies connectedness, and verifies all fifteen bag
adjacencies.  Applied to the 50 entries of (5.1), it finds a model in
seventeen and leaves exactly the 33 entries of (5.2).  This is a complete
finite certificate for the stated quotient lemma. \(\square\)

## 6. Exact residual of the four-plus-one mechanism

The purely binary mixed words have independently been eliminated by the
pentagon boundary-state lemma in
`hadwiger_moser_pentagon_boundary_lemma.md`.  Hence, if a selected
four-plus-one family remains genuinely unconfined, some majority edge is
bi-supported.

Combining that result with Lemmas 2.1, 3.1, 4.1, 5.1 and 5.2 leaves exactly the
following geometric residual for this mechanism:

1. the minority edge is one of \(25,24,46\);
2. the majority component supports the other four cycle edges;
3. at least one of those four edges is also supported by the minority
   component;
4. the minority component has no cutvertex or two-cut (and hence is
   3-connected when it has order at least four); and
5. it contains no pair of vertex-disjoint paths joining \(1\) to \(3\)
   and the ends of the minority edge.

At the level of the fourteen support-word orbits, the selected
four-plus-one condition permits the seven residual orbit types

\[
1112B,\ 112BB,\ 11B2B,\ 121BB,\ 12B1B,\ 12BBB,\ 1B2BB.              \tag{6.1}
\]

But (6.1) does not encode the physical position of the unique
minority-only edge.  Lemma 3.1 eliminates precisely those rotations in
which that physical edge is \(05\) or \(06\); Lemma 4.1 eliminates every
rotation whose minority component has a cutvertex; and Lemmas 5.1--5.2
leave the 33-pair table (5.2).  The support-independent global two-cut
theorem leaves only the pairs 13|24 and 14|23; neither occurs in (5.2).
Thus every four-plus-one two-cut is eliminated.

The remaining obstruction is therefore not an arbitrary rooted
\(K_5\) problem.  It is a connected, cutvertex-free minority component
with no one- or two-vertex cut, containing a second bichromatic path
(from bi-support), but forming a
four-terminal two-paths obstruction for \((1,3;x,y)\).  (This wording
deliberately also covers components of order one or two.)  Any further
closure must use that second path together with minor exclusion or one-step
contraction-criticality; seven-connectivity and the four confined paths
alone no longer suffice.
