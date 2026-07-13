# Near-\(K_7\) with one complex bag: the rooted normalization and the dynamic owner web

## 1. Scope and status

This note gives an unbounded closure and a structural reduction for a
spanning near-\(K_7\) model with one complex bag.  The main point is a
normalization which was not used explicitly in the older near-clique notes.

For a spanning \(K_7^-\)-model with singleton deficient pair \(a,c\), delete
\(a\).  What remains is a spanning \(K_6\)-model consisting of one complex
bag and a five-clique of singleton bags.  Thus the near-clique problem is
literally the sharp one-complex rooted-model problem, with \(a\) as apex.

Three consequences are proved below.

1. No neutral singleton row can be universal on the complex bag.  In
   particular the exact static obstruction \(K_2\vee I\) is not an
   obstruction in a hypothetical minimal counterexample: its two universal
   vertices are forbidden by the already proved \(HC_6\).
2. If the complex bag is a cycle (of arbitrary order), the model upgrades
   to an explicit \(K_7\)-model.  More generally the proof only needs a
   spanning cycle and the displayed row-density condition.
3. For an arbitrary 2-connected complex bag, every bipolar sweep between
   two apex feet has an exact two-owner sandwich.  At a two-cut, four or
   more sufficiently varied lobes already give the target; otherwise all
   but at most one lobe are dark to one common row.  The full proper-minor
   operation spectra of the dark lobes are pairwise disjoint on the actual
   adhesion.

The last outcome is a genuine capacity--state web, not a proof of
\(HC_7\).  A three-connected, entirely nonuniversal owner web remains.

## 2. The rooted normalization

Let \(G\) be seven-connected and suppose that it has a spanning
\(K_7^-\)-model

\[
       \{a\},\{c\},\{q_1\},\{q_2\},\{q_3\},\{q_4\},B,       \tag{2.1}
\]

where \(ac\) is the only non-required adjacency and \(B\) is connected.
If \(G\) is \(K_7\)-minor-free, then \(ac\notin E(G)\).  Put

\[
 H=G-a,\qquad S=\{c,q_1,q_2,q_3,q_4\}.                     \tag{2.2}
\]

Then \(S\) is a five-clique and

\[
             (B,\{c\},\{q_1\},\ldots,\{q_4\})              \tag{2.3}
\]

is a spanning \(K_6\)-model in \(H\).  Define the six portal rows

\[
 F=N_B(a),\qquad C=N_B(c),\qquad Q_i=N_B(q_i).              \tag{2.4}
\]

Here \(F\) is the contact row: a branch set of (2.3) is contacted exactly
when it contains a vertex of \(F\), except for the four already contacted
singleton bags \(q_i\).  The singleton \(c\) is the unique uncontacted old
bag.

### Lemma 2.1 (portal multiplicity)

If \(\delta(G)\ge7\), then

\[
                  |F|,|C|\ge3,\qquad |Q_i|\ge2.             \tag{2.5}
\]

If no \(K_7\)-minor exists, then \(B\) is 2-connected.

#### Proof

The vertex \(a\) has the four neighbours \(q_1,\ldots,q_4\), is
nonadjacent to \(c\), and has no other vertices outside \(B\).  Hence
\(d(a)=4+|F|\).  The same equation holds for \(c\).  Each \(q_i\) has
five singleton neighbours in (2.1), so \(d(q_i)=5+|Q_i|\).  This proves
(2.5).

If \(x\) is a cutvertex of \(B\), every component of \(B-x\) has all six
singleton vertices of (2.1) as neighbours: its neighbourhood is contained
in those six vertices together with \(x\), and seven-connectivity forces
equality.  Splitting off one component therefore gives the seven branch
sets listed in Theorem 2.1 of
`hadwiger_near_k7_one_complex_bag_closure.md`.  Thus absence of the target
forces \(B\) to be 2-connected. \(\square\)

### Lemma 2.2 (the exact rooted split certificate)

Suppose

\[
                         B=P\mathbin{\dot\cup}R              \tag{2.6}
\]

is a partition into nonempty connected sets, and

\[
 P\cap F\ne\varnothing,\quad P\cap C\ne\varnothing,
 \qquad
 R\cap F\ne\varnothing,\quad R\cap Q_i\ne\varnothing
       \ (1\le i\le4).                                     \tag{2.7}
\]

Then \(G\) has a \(K_7\)-minor.

#### Proof

Use

\[
 \{a\},\quad \{c\}\cup P,\quad R,\quad
 \{q_1\},\ldots,\{q_4\}.                                 \tag{2.8}
\]

The second set is connected through the \(cP\)-edge.  The two parts of
the connected graph \(B\) are adjacent.  The two foot conditions make
the first bag adjacent to both new complex bags.  The \(Q_i\)-conditions
give every \(Rq_i\)-edge, while \(c\) gives all four edges from the
second bag to the neutral singleton clique.  All remaining pairs were
already edges of (2.1). \(\square\)

Thus the one-complex near-clique problem is exactly a connected
two-shore packing problem: one shore must meet \(F,C\), and the other must
meet \(F,Q_1,\ldots,Q_4\).

### Corollary 2.3 (contact and deficient portals are disjoint)

If \(G\) has no \(K_7\)-minor, then

\[
                              F\cap C=\varnothing.            \tag{2.9}
\]

#### Proof

If \(x\in F\cap C\), take \(P=\{x\}\) and \(R=B-x\).  The latter is
connected because \(B\) is 2-connected.  Since \(|F|,|C|\ge3\) and
\(|Q_i|\ge2\), deleting the one vertex \(x\) leaves a foot and a portal
of every neutral row in \(R\).  Hence (2.7) holds and Lemma 2.2 gives the
target. \(\square\)

This is a strong polarity constraint: in a target-free model the two
large rows \(F,C\), each of order at least three, are disjoint.

## 3. Universal portal rows are impossible

### Lemma 3.1 (no universal vertex at a least failing parameter)

Let \(t\ge2\), assume \(HC_{t-1}\), and let \(G\) be a
\(t\)-chromatic graph with no \(K_t\)-minor.  Then \(G\) has no universal
vertex.

#### Proof

If \(u\) is universal, then

\[
                         \chi(G-u)=t-1.                     \tag{3.1}
\]

Moreover \(G-u\) has no \(K_{t-1}\)-minor, since adjoining the singleton
bag \(\{u\}\) to such a model would give a \(K_t\)-minor in \(G\).
This contradicts \(HC_{t-1}\), which makes every
\(K_{t-1}\)-minor-free graph \((t-2)\)-colourable. \(\square\)

### Corollary 3.2 (all four neutral rows are proper)

In a hypothetical minimal counterexample to \(HC_7\),

\[
                            Q_i\ne V(B)                       \tag{3.2}
\]

for every \(i\).

#### Proof

The vertex \(q_i\) is adjacent to all other singleton vertices in (2.1),
including \(a\), and to every vertex of \(B\) exactly when
\(Q_i=V(B)\).  It would then be universal in \(G\), contradicting Lemma
3.1 and the established theorem \(HC_6\). \(\square\)

The connectivity-only graph \(K_2\vee I\) from the older notes has two
universal singleton rows.  Corollary 3.2 excludes that exact architecture
from a hypothetical counterexample.  What survives is not an icosahedral
join: all four neutral rows must have genuine holes in the complex bag.

### Lemma 3.3 (a critical vertex cannot have one nonneighbour)

In a \(k\)-vertex-critical graph, no vertex has exactly one nonneighbour.

#### Proof

Suppose \(u\) has unique nonneighbour \(x\).  The graph \(G-x\) has a
\((k-1)\)-colouring.  In it, the universal vertex \(u\) has a colour used
nowhere else, so \(G-\{u,x\}\) uses at most \(k-2\) colours.  Give \(u,x\)
one new common colour.  They are nonadjacent, and this gives a
\((k-1)\)-colouring of \(G\), a contradiction. \(\square\)

### Corollary 3.4 (every neutral row has two holes)

In (2.1),

\[
 |B-Q_i|\ge2\quad(1\le i\le4),\qquad
 B-F\ne\varnothing\ne B-C.                              \tag{3.3}
\]

#### Proof

All nonneighbours of \(q_i\) lie in \(B-Q_i\).  Corollary 3.2 rules out
zero and Lemma 3.3 rules out one.  The vertex \(a\) is already nonadjacent
to \(c\); if \(F=B\), then \(c\) would be its unique nonneighbour.
The argument for \(C\) is symmetric. \(\square\)

For the \(K_7^{\vee}\) normalization (8.1), the same proof gives
\(|B-Q_i|\ge2\) and says that each of the two deficient rows
\(N_B(b),N_B(c)\) has a hole: otherwise \(a\) would be the unique
nonneighbour of the corresponding singleton.

### Theorem 3.5 (exact pinned/unpinned list polarity)

Assume that \(G\) is proper-minor-minimal non-six-colourable and has no
\(K_7\)-minor.  Fix the five colours of the singleton clique
\(S=\{c,q_1,\ldots,q_4\}\), call the colour of \(c\) \(\gamma\), and
call the sixth colour \(\delta\).  For every proper minor operation
\(\mu\) supported in \(B\), every six-colouring of \(G/\mu\) has exactly
one of the following two boundary states.

* **Pinned:** \(a\) has colour \(\gamma\).  The induced expansion lists
  on an unoperated vertex \(z\in B\) are
  \[
    L_0(z)=\{\delta\}
       \cup\bigl(\{\gamma\}:z\notin F\cup C\bigr)
       \cup\{c(q_i):z\notin Q_i\}.                         \tag{3.4}
  \]
* **Unpinned:** \(a\) has colour \(\delta\).  The lists are
  \[
    L_1(z)=\bigl(\{\delta\}:z\notin F\bigr)
       \cup\bigl(\{\gamma\}:z\notin C\bigr)
       \cup\{c(q_i):z\notin Q_i\}.                         \tag{3.5}
  \]

Consequently, using (2.9),

\[
 L_0(z)=L_1(z)\quad(z\notin F),qquad
 L_1(z)=(L_0(z)-\{\delta\})\cup\{\gamma\}\quad(z\in F). \tag{3.6}
\]

Thus the entire all-operation family has a literal two-colour polarity
switch supported only on the apex-foot row.  No assertion is made that
both polarities occur for one operation.

#### Proof

The five-clique \(S\) is rainbow.  Since \(a\) is adjacent to the four
\(q_i\) and nonadjacent to \(c\), it either has colour \(\gamma\) or the
sixth colour \(\delta\).  Deleting from the palette the colours seen at
the singleton neighbours of \(z\), and also the colour of \(a\) when
\(z\in F\), gives (3.4)--(3.5).

Finally (3.6) follows by comparing the two displayed lists and using
\(F\cap C=\varnothing\). \(\square\)

### Corollary 3.6 (no triple-neutral portal vertex)

In a seven-chromatic \(K_7\)-minor-free graph satisfying (2.1), no vertex
of \(B\) belongs to three of the four neutral rows \(Q_i\).  Consequently

\[
                              \delta(B)\ge4.                  \tag{3.7}
\]

In the \(K_7^{\vee}\) normalization (8.1), no vertex of \(B\) belongs to
all three neutral rows.

#### Proof

Choose any neutral triangle \(T=\{q_i,q_j,q_k\}\).  In the
\(K_7^-\) model, its common neighbours already include the three vertices
\(a,c,q_\ell\), where \(q_\ell\) is the fourth neutral singleton.  The
global triangle-common-neighbour cap (Corollary 2.12 of
`hadwiger_near_k7_two_complex_bag_round.md`) says that a triangle in a
seven-connected, seven-chromatic, \(K_7\)-minor-free graph has at most
three common neighbours.  Hence no vertex of \(B\) is complete to \(T\).

A vertex of \(B\) therefore has at most two neighbours among the \(q_i\).
By (2.9) it is adjacent to at most one of \(a,c\).  Hence it has at most
three neighbours outside \(B\) in the whole graph \(G\).  Since
\(\delta(G)\ge7\), this gives \(d_B(z)\ge4\).

For (8.1), the common neighbours of the neutral triangle
\(\{q_1,q_2,q_3\}\) already include \(a,b,c\), so the same cap excludes
every additional common neighbour in \(B\). \(\square\)

Thus the target-free \(K_7^-\) society is automatically beyond the cycle
case: it is 2-connected, has minimum internal degree four, has six genuine
portal holes, and its two large polar rows \(F,C\) are disjoint.

## 4. An unbounded closure: cyclic complex bags

The following lemma is stated in the row language so that it can be reused.

### Lemma 4.1 (row-dense cycle splitter)

Let \(B\) be a cycle.  Let \(F,C,Q_1,\ldots,Q_4\subseteq V(B)\) satisfy

\[
 |F|,|C|\ge3,\qquad |Q_i|\ge2,                              \tag{4.1}
\]

and suppose every vertex of \(B\) belongs to at least four of the five
sets

\[
                         C,Q_1,Q_2,Q_3,Q_4.                  \tag{4.2}
\]

Then \(B\) has a connected bipartition satisfying (2.7).

#### Proof

First choose a connected bipartition \(B=P\dot\cup R\) for which both
parts meet \(F\) and \(C\).  For completeness, choose two distinct feet
as the poles of a bipolar ordering of the cycle and cut between the first
and last occurrence of \(C\).  Equivalently this is the two-class
connected splitter, Lemma 6.1 of
`hadwiger_spanning_singleton_core_exchange_dichotomy.md`.

If one part, say \(R\), meets all four \(Q_i\), then (2.7) holds.  If
\(P\) meets all four, interchange the names of the two parts.  We may
therefore assume, for a contradiction, that

\[
                         P\cap Q_i=\varnothing,qquad
                         R\cap Q_j=\varnothing               \tag{4.3}
\]

for some \(i,j\).

Condition (4.2) says that a vertex misses at most one of the five rows.
Consequently every vertex of \(P\) misses precisely the row \(Q_i\) and
belongs to every other row; every vertex of \(R\) has the analogous
property for \(Q_j\).  We have \(i\ne j\), since otherwise (4.3) would
make \(Q_i\) empty on the whole cycle.

At least one of \(P,R\), say \(P\), contains two feet.  The two parts are
arcs of the cycle.  Remove an endvertex \(x\) of the arc \(P\) and add it
to the adjacent arc \(R\).  The set \(P-x\) is nonempty, connected, and
still contains a foot.  It also still meets \(C\), because every vertex
of \(P\) belongs to \(C\).  The enlarged \(R+x\) is connected and retains
an old foot.  It meets every \(Q_k\): an old vertex of \(R\) belongs to
\(Q_i\), the new vertex \(x\) belongs to \(Q_j\), and both belong to
every row different from their respective missing rows.  Thus
\((P-x,R+x)\) satisfies (2.7), a contradiction.

If \(R\) is the part with two feet, make the symmetric move and then
interchange the roles of the parts. \(\square\)

### Theorem 4.2 (cyclic one-complex cell closes)

Under (2.1), if \(B\) is a cycle, then \(G\) contains a \(K_7\)-minor.
The same conclusion holds if \(B\) has a spanning cycle and every vertex
has at least four singleton neighbours in \(S\).

#### Proof

The graph \(H=G-a\) is six-connected, so every vertex of a cyclic \(B\)
has degree at least six in \(H\).  It has two neighbours on the cycle and
all its other neighbours lie in the five-clique \(S\).  It is therefore
adjacent to at least four vertices of \(S\), which is exactly (4.2).
Lemma 2.1 supplies (4.1), Lemma 4.1 supplies the split, and Lemma 2.2
lists the resulting \(K_7\)-model.

For a spanning cycle, use its arcs for the connected bipartitions; extra
edges do not invalidate any branch-set adjacency. \(\square\)

This eliminates the suspended-octahedron/odd-cycle type of static portal
obstruction once the actual apex-foot row is retained.  It is uniform in
the length of the cycle.

## 5. The two-owner bipolar web

The cyclic proof uses row density.  Without it one still obtains an exact
ordered obstruction.

Let \(f_-,f_+\) be distinct vertices of \(F\).  Since \(B\) is
2-connected, it has a bipolar ordering

\[
                     z_1=f_-,z_2,\ldots,z_n=f_+              \tag{5.1}
\]

whose every prefix and suffix is connected.  For a nonempty row \(X\),
put

\[
 \ell(X)=\min\{k:z_k\in X\},\qquad
 r(X)=\max\{k:z_k\in X\}.                                  \tag{5.2}
\]

### Theorem 5.1 (two-owner sandwich)

If the split of Lemma 2.2 does not exist, then for every choice of the
two feet and every bipolar ordering (5.1), there are distinct indices
\(i,j\in[4]\) such that

\[
                 r(Q_i)\le \ell(C)\le r(C)\le \ell(Q_j).    \tag{5.3}
\]

#### Proof

If

\[
                         \ell(C)<\min_i r(Q_i),              \tag{5.4}
\]

choose an integer \(t\) with
\(\ell(C)\le t<\min_i r(Q_i)\).  The prefix through \(z_t\) is
connected, contains \(f_-\), and meets \(C\).  The complementary suffix
is connected, contains \(f_+\), and meets every \(Q_i\).  This is the
split of Lemma 2.2.  Its absence therefore gives

\[
                         \min_i r(Q_i)\le\ell(C).             \tag{5.5}
\]

The reverse orientation gives the other inequality.  Indeed, if

\[
                         \max_i\ell(Q_i)<r(C),                \tag{5.6}
\]

cut after an integer \(t\) satisfying
\(\max_i\ell(Q_i)\le t<r(C)\), use the suffix as the
\(F,C\)-shore and the prefix as the retained \(F,Q_1,\ldots,Q_4\)-shore.
Thus absence of the split implies

\[
                         r(C)\le\max_i\ell(Q_i).              \tag{5.7}
\]

Choose \(i,j\) attaining (5.5) and (5.7).  They are distinct.  Otherwise
\(r(Q_i)\le\ell(Q_i)\), whereas \(|Q_i|\ge2\) gives the strict inequality
\(\ell(Q_i)<r(Q_i)\). \(\square\)

Thus the general residue is not six arbitrary portal rows.  In every
foot-to-foot sweep, the whole deficient row \(C\) is bracketed by two
different neutral owner rows.  Corollary 3.2 says neither owner row is
universal, so both ends of this interval web are genuine.

### Lemma 5.2 (spanning triangle at three feet)

For any three distinct feet \(f_1,f_2,f_3\in F\), the bag \(B\) has a
partition

\[
                         B=Z_1\dot\cup Z_2\dot\cup Z_3      \tag{5.8}
\]

into three nonempty connected, pairwise adjacent sets with
\(f_i\in Z_i\).

#### Proof

The rooted-triangle lemma for a 2-connected graph gives three disjoint
pairwise adjacent connected sets rooted at the prescribed vertices.  To
make them spanning, contract the three sets, retain one edge between each
pair, and take a spanning forest of all remaining vertices rooted at the
three contracted vertices.  Assign each forest vertex to its root and
expand.  Every enlarged set is connected and the three retained pairwise
edges preserve their mutual adjacency. \(\square\)

For a piece \(Z\), write

\[
                         \Lambda_Q(Z)=\{i:Z\cap Q_i\ne\varnothing\}.
                                                                    \tag{5.9}
\]

### Theorem 5.3 (one-helper rooted-triangle completion)

Let (5.8) be a spanning foot-rooted triangle, and suppose after relabelling
that \(Z_1\cap C\ne\varnothing\).  Among the four neutral labels, call
\(i\) **crossing** when

\[
                         i\in\Lambda_Q(Z_2)\cap\Lambda_Q(Z_3).       \tag{5.10}
\]

Then \(G\) contains a \(K_7\)-minor if either

1. at least three neutral labels are crossing; or
2. exactly two are crossing and the support masks on \(\{Z_2,Z_3\}\)
   of the remaining two labels have union \(\{Z_2,Z_3\}\).

#### Proof

Absorb the singleton \(c\) into \(Z_1\).  This is connected because
\(Z_1\cap C\ne\varnothing\), and it remains contacted through the foot
in \(Z_1\).  We need three further branch sets from the four-vertex
clique \(\{q_1,q_2,q_3,q_4\}\).  Partition its labels into three nonempty
blocks.  The corresponding singleton unions are connected, pairwise
adjacent, and adjacent to \(\{c\}\cup Z_1\) through the edges \(cq_i\).
They are all contacted by the apex \(a\).

It remains only that every block have a label meeting \(Z_2\) and a label
meeting \(Z_3\).  Three blocks on four labels have sizes \(1,1,2\).  The
two singleton blocks must therefore be crossing labels.  The double block
meets both pieces exactly when it contains a third crossing label, or when
the two remaining support masks cover the two pieces collectively.  These
are outcomes 1 and 2.

The six bags

\[
 \{c\}\cup Z_1,\quad Z_2,\quad Z_3,\quad
 Q[J_1],\quad Q[J_2],\quad Q[J_3]                         \tag{5.11}
\]

are pairwise adjacent connected sets in \(H\), every one meeting
\(N_G(a)\).  Adjoin \(\{a\}\) to obtain the \(K_7\)-model. \(\square\)

Here \(Q[J]\) denotes the clique of singleton vertices whose indices lie
in \(J\).  No old model bag is reused.

### Corollary 5.4 (exact two-pole lock)

In a target-free graph, every spanning triangle rooted at three feet has a
piece meeting \(C\); relative to that piece, the other two pieces satisfy
one of the following.

* At most one neutral row crosses the two pieces; or
* exactly two neutral rows cross, and the other two rows both miss one
  common piece (allowing an empty support mask).

#### Proof

The partition is spanning and \(C\ne\varnothing\), so one piece meets
\(C\).  Negate the two sufficient conditions of Theorem 5.3. \(\square\)

This is a model-level strengthening of the bipolar sandwich.  It holds for
every order and every internal geometry of \(B\): after one deficient
singleton is spent as a helper, all remaining failure is carried by two
pole pieces and four neutral support masks.

## 6. Two-cuts: capacity collapse to a common dark row

Let \(X=\{x,y\}\) be a two-cut of \(B\), and let
\(D_1,\ldots,D_m\) be the components of \(B-X\).  For a lobe \(D_h\),
write

\[
 \rho(D_h)=\{F,C,Q_1,Q_2,Q_3,Q_4:\text{the row meets }D_h\}. \tag{6.1}
\]

### Lemma 6.1 (every lobe misses at most one row)

For every \(h\),

\[
                            |\rho(D_h)|\ge5.                  \tag{6.2}
\]

#### Proof

Two-connectivity of \(B\) makes every lobe adjacent to both \(x\) and
\(y\).  Every neighbour of \(D_h\) outside the lobe belongs to

\[
             \{x,y,a,c,q_1,q_2,q_3,q_4\}.                   \tag{6.3}
\]

Another lobe lies beyond this set, so seven-connectivity gives
\(|N_G(D_h)|\ge7\).  Two of these neighbours are \(x,y\); hence at
least five of the six singleton rows meet the lobe. \(\square\)

Call the unique missed row the **type** of a non-full lobe; a full lobe
has no type.

### Theorem 6.2 (four-lobe packing or a common owner)

If \(m\ge4\), then either \(G\) contains a \(K_7\)-minor, or some row
\(L\in\{F,C,Q_1,\ldots,Q_4\}\) is missed by at least \(m-1\) lobes.
Equivalently, all portals of \(L\) outside at most one exceptional lobe
are concentrated at the cut vertices \(x,y\).

#### Proof

Suppose no missed-row type occurs \(m-1\) times.  Then four lobes can be
chosen and paired so that the two lobes in each pair have different
types (a full lobe may be paired with anything).  This is the elementary
two-pair form of the pigeonhole principle: failure would make all but at
most one of the lobes have one common type.

By Lemma 6.1, the union of two differently typed lobes meets all six
rows.  Put one pair together with \(x\), put the other pair together with
\(y\), and assign every remaining lobe arbitrarily to one side.  Each
side is connected, because every lobe has a neighbour at both cut
vertices; the sides are adjacent through any lobe-to-opposite-cut edge.
Both sides meet all six rows.  In particular they satisfy (2.7), and
Lemma 2.2 gives the target. \(\square\)

This is an unbounded lobe theorem.  The only many-lobe residue is a
single common dark row, not an expanding list of quotient geometries.

### Theorem 6.3 (three lobes close unless one lobe owns every foot)

If \(m=3\), then either Lemma 2.2 gives a \(K_7\)-minor, or all vertices
of \(F\) lie in one component of \(B-X\).

#### Proof

Use the missed-row type from Lemma 6.1, treating a full lobe as having
type \(*\).

If the three lobe types are distinct, one lobe has type outside
\(\{F,C\}\).  Use it as the \(F,C\)-shore and put the other two lobes,
together with \(x,y\), on the retained shore.  The retained pair has
different types and therefore meets all six rows.

Suppose two lobes have type \(\lambda\) and the third has a different
type \(\mu\).  If \(\lambda\notin\{F,C\}\), use one
\(\lambda\)-lobe as the \(F,C\)-shore; the other two lobes have different
types and make the retained shore full.  If \(\lambda=C\), use one
\(C\)-dark lobe as the retained shore: it meets \(F,Q_1,\ldots,Q_4\),
while the other two differently typed lobes, joined through a cut vertex,
meet \(F,C\).

It remains that \(\lambda=F\).  The two repeated lobes have no foot and
the exceptional \(\mu\)-lobe has a foot.  If another foot occurs at
\(x\) or \(y\), put that cut vertex and one \(F\)-dark lobe on the
retained side.  Put the exceptional lobe, the other \(F\)-dark lobe, and
the other cut vertex on the absorbed side.  Both sides are connected.
The retained side meets all \(Q_i\) at its \(F\)-dark lobe and meets
\(F\) at the chosen cut vertex.  The absorbed side meets \(F\) in the
exceptional lobe and meets \(C\) either there (if \(\mu\ne C\)) or in
the \(F\)-dark lobe (if \(\mu=C\)).  This is (2.7).  Hence absence of
the target forces every foot into the exceptional lobe.

Finally, if all three types agree, types \(F\) and \(C\) are impossible:
their portal rows would be contained in \(\{x,y\}\), contrary to (2.5).
For a common neutral type \(Q_i\), the row \(Q_i\) is contained in
\(\{x,y\}\); take one lobe as the \(F,C\)-shore and the complement,
which contains both cut vertices, as the retained shore.  A common full
type is easier.  These choices again satisfy (2.7). \(\square\)

Thus a target-free two-cut has only two genuinely small cases: two lobes,
or three lobes with all apex feet owned by one lobe.  Four or more lobes
have the common-dark-row form of Theorem 6.2.

### Theorem 6.4 (the common dark row collapses to the foot owner)

Assume \(m\ge4\) and the common-owner outcome of Theorem 6.2: a row
\(L\) is missed by at least \(m-1\) lobes.  Then either \(G\) contains a
\(K_7\)-minor, or

* \(L=F\);
* there is exactly one exceptional lobe \(D^*\) which meets \(F\); and
* every foot lies in that lobe:
  \[
                              F\subseteq D^*.                  \tag{6.4}
  \]

#### Proof

Call the \(m-1\) common-type lobes dark.

Suppose first that \(L=Q_i\).  Take one dark lobe as \(P\) and its
complement in \(B\) as \(R\).  The lobe \(P\) meets \(F,C\), since it
misses only \(Q_i\).  The complement is connected: it contains \(x,y\)
and at least two further lobes.  Another dark lobe supplies
\(F,Q_j\) for every \(j\ne i\), while every \(Q_i\)-portal lies outside
the chosen dark lobe and hence in \(R\).  Thus (2.7) holds.

If \(L=C\), reverse the allocation.  Use one dark lobe as \(R\).  It
meets \(F,Q_1,\ldots,Q_4\).  Its connected complement \(P\) contains a
second dark lobe, which supplies a foot, and it contains every
\(C\)-portal outside the chosen lobe.  Since the chosen lobe is
\(C\)-dark, all such portals lie in \(P\); hence \(P\) meets \(F,C\).
Again (2.7) holds.

It remains that \(L=F\).  All dark lobes are footless.  At least one
exceptional lobe exists, since otherwise \(F\subseteq\{x,y\}\), contrary
to \(|F|\ge3\).  If a foot occurs at, say, \(x\), put \(x\) and one dark
lobe on the retained side \(R\), and put \(y\), the exceptional lobe,
and every remaining lobe on \(P\).  Both sides are connected and adjacent.
The dark lobe makes \(R\) meet \(C,Q_1,\ldots,Q_4\), while \(x\) supplies
its foot.  The exceptional lobe supplies a foot to \(P\), and any dark
lobe in \(P\) supplies its \(C\)-contact.  This is (2.7).  The argument is
symmetric if \(y\in F\).

Consequently a target-free graph has no foot at either cut vertex.  Since
the dark lobes are footless as well, all feet lie in the unique exceptional
lobe \(D^*\), proving (6.4). \(\square\)

Theorems 6.3--6.4 give a strict **foot-owner descent**: at every two-cut
with at least three lobes, absence of the target identifies one proper
component containing every apex foot.  Its order is strictly smaller than
\(|B|\).  The other lobes are not unresolved geometry; they are complete
carriers for the five nonfoot rows and may be retained as the stabilizing
shore in the next split.

### Corollary 6.5 (reduction to an exact two-lobe core)

In the target-free outcome of Theorem 6.3 or 6.4, choose one footless dark
lobe \(K\), and let \(D^*\) be the unique foot-owner lobe.  Then

\[
                         B^*=D^*\cup\{x,y\}\cup K             \tag{6.5}
\]

is a connected branch set which may replace \(B\) in the near-\(K_7\)
model; all other lobes may be discarded.  The new model has the same six
singleton bags, all apex feet lie in \(D^*\), and \(K\) meets each of
\(C,Q_1,Q_2,Q_3,Q_4\).  Thus every many-lobe owner cut reduces
label-preservingly to a two-lobe owner core.

#### Proof

Both \(D^*\) and \(K\) have neighbours at each of \(x,y\), so (6.5) is
connected.  It contains all feet by Theorems 6.3--6.4.  The dark lobe
\(K\) misses only \(F\), and hence supplies an edge from \(B^*\) to every
one of the five singleton bags in \(S\).  Therefore

\[
                   (B^*,\{c\},\{q_1\},\ldots,\{q_4\})
\]

is again a \(K_6\)-model in \(G-a\), with the same contact pattern.
Minor models need not be spanning, so deleting the unused lobes from the
model is legitimate. \(\square\)

This is a strict owner-core potential which does not rotate a spanning
tree or pass to a quotient graph.  It acts inside the original graph and
retains the two actual shores \(D^*,K\) and their common cut \(\{x,y\}\),
so their proper-minor states remain available for crossed splicing.

## 7. Full operation states on the owner web

Now assume that \(G\) is not six-colourable and every proper minor is
six-colourable.  At the two-cut above put

\[
                     W=\{a,c,q_1,q_2,q_3,q_4,x,y\}.          \tag{7.1}
\]

For a boundary-faithful proper operation \(\mu\) supported in one open
lobe, let \(\Sigma_h(\mu)\) be the equality partitions of \(W\) induced
by six-colourings of \(G/\mu\) (with deletion notation interpreted in the
usual way).

### Theorem 7.1 (dynamic owner-web anti-coincidence)

If \(h\ne k\), and \(\mu,\nu\) are faithful proper operations supported
in \(D_h,D_k\), respectively, then

\[
                         \Sigma_h(\mu)\cap\Sigma_k(\nu)
                         =\varnothing.                        \tag{7.2}
\]

Every lobe has a nonempty state spectrum (deleting the whole open lobe is
an allowed faithful proper operation).  Moreover there are at most

\[
                              2\cdot6^2=72                    \tag{7.3}
\]

possible equality states on \(W\).  Consequently a two-cut has at most
72 lobes.

#### Proof

Distinct lobes are anticomplete and have all their external neighbours in
\(W\).  If two operated colourings agreed up to a palette permutation on
\(W\), use on each lobe the colouring in which that lobe was not operated,
align the common boundary, and splice.  This restores both proper-minor
operations and gives a six-colouring of \(G\), a contradiction.  This is
the boundary-faithful crossed-minor theorem.

For the count, the five-clique
\(\{c,q_1,q_2,q_3,q_4\}\) is rainbow in every six-colouring.  The vertex
\(a\), still adjacent to all four \(q_i\), either has the colour of \(c\)
or the unique sixth colour.  Once these choices are fixed, each of \(x,y\)
has at most six colour classes available.  Thus at most \(2\cdot6^2\)
equality partitions occur.  Disjointness gives the lobe bound. \(\square\)

Combining Theorems 6.2 and 7.1 gives the precise non-three-connected
residue:

\[
\boxed{
 \begin{array}{c}
 \text{explicit label-preserving split and }K_7,\quad\text{or}\\
 \text{one common dark portal row on all but one lobe, with}\\
 \text{pairwise disjoint full proper-minor state spectra.}
 \end{array}}
\tag{7.4}
\]

The 72 is only a capacity bound, not a contradiction.  The missing
operation theorem must transport the common dark row across one of the
lobes, or identify a state with the exceptional/opposite shore.

## 8. The \(K_7^{\vee}\) normalization

For completeness, a spanning one-complex \(K_7^{\vee}\)-model has

\[
       \{a\},\{b\},\{c\},\{q_1\},\{q_2\},\{q_3\},B,         \tag{8.1}
\]

with deficient pairs \(ab,ac\).  Deleting \(a\) again leaves a spanning
one-complex/singleton \(K_6\)-model: the five vertices
\(b,c,q_1,q_2,q_3\) form a clique.  The apex has one foot row \(F\), the
two uncontacted singleton rows are \(N_B(b),N_B(c)\), and the three
neutral rows are \(N_B(q_i)\).  Here

\[
 |F|\ge4,\quad |N_B(b)|,|N_B(c)|\ge3,quad |N_B(q_i)|\ge2,   \tag{8.2}
\]

and none of the three neutral rows is universal, by Lemma 3.1.

An explicit upgrade is obtained from three disjoint connected sets
\(P_b,P_c,R\subseteq B\) such that

* \(P_b\) meets \(F\) and \(N_B(b)\);
* \(P_c\) meets \(F\) and \(N_B(c)\);
* \(R\) meets \(F\) and all three neutral rows; and
* \(R\) is adjacent to both \(\{b\}\cup P_b\) and
  \(\{c\}\cup P_c\).

Indeed

\[
 \{a\},\quad \{b\}\cup P_b,\quad \{c\}\cup P_c,\quad R,
 \quad\{q_1\},\{q_2\},\{q_3\}                              \tag{8.3}
\]

are then the seven branch sets.  This is the three-shore version of the
same rooted normalization.  The results above completely settle the
two-shore \(K_7^-\) cycle cell; the analogous three-shore web is not
closed here.

### Theorem 8.1 (assisted three-shore block packing)

Let \(Z_1,Z_2,Z_3\subseteq B\) be disjoint, pairwise adjacent connected
sets, each meeting the foot row \(F\).  Partition the five singleton
labels

\[
                         \{b,c,q_1,q_2,q_3\}                  \tag{8.4}
\]

into three nonempty **far blocks** \(J_1,J_2,J_3\) and pairwise disjoint
nonempty **helper blocks** \(H_i\), indexed by a set
\(I\subseteq\{1,2,3\}\).  Assume:

1. every far block contains one of \(q_1,q_2,q_3\);
2. for \(i\in I\), the piece \(Z_i\) meets the portal row of at least one
   label in \(H_i\); and
3. for \(i\notin I\), every far block contains a label whose portal row
   meets \(Z_i\).

Then \(G\) has a \(K_7\)-minor.

#### Proof

For \(i\in I\), enlarge \(Z_i\) by the singleton vertices in \(H_i\).
The enlarged set is connected because one helper label contacts \(Z_i\)
and the helper labels form a clique.  It is adjacent to every far block
through the clique on (8.4).  For \(i\notin I\), condition 3 supplies the
direct adjacency to every far block.  The three accessible pieces remain
pairwise adjacent through their old edges, and the three far blocks are
pairwise adjacent clique bags.  Every accessible piece is contacted at its
foot, while every far block is contacted through its neutral \(q\)-vertex.
These are six pairwise adjacent contacted bags in \(G-a\); adjoining
\(\{a\}\) gives \(K_7\). \(\square\)

Because there are exactly three neutral labels and three far blocks, each
far block contains exactly one \(q_i\).  Thus Theorem 8.1 is a finite allocation
test on the support masks of any foot-rooted triangle, not an existential
linkage theorem.  Lemma 5.2 supplies such a spanning triangle from any
three of the at least four feet in (8.2).

Two useful special cases are immediate.

* Spend \(b,c\) as separate helpers on two pieces.  The third piece need
  only meet all three \(Q_i\).
* Spend \(\{b,c\}\) as one helper block on a piece meeting at least one of
  the two deficient rows.  The other two pieces need each meet all three
  neutral rows.

### Lemma 8.2 (three-shore profile allocation)

Let \(m\ge4\), and let \(L_1,\ldots,L_m\) be abstract lobes.  Each lobe
has a support in the six rows

\[
                    F,B_0,C_0,Q_1,Q_2,Q_3                 \tag{8.5}
\]

and misses at most one row.  Call that row its type; a full lobe has type
\(*\).  There are distinct lobes \(L_b,L_c\) such that

\[
 \{F,B_0\}\subseteq\rho(L_b),\qquad
 \{F,C_0\}\subseteq\rho(L_c),                             \tag{8.6}
\]

and the union of all remaining lobes meets
\(F,Q_1,Q_2,Q_3\), unless the multiset of types has one of the following
four forms.

1. At least \(m-2\) lobes have type \(F\).
2. Every lobe has type in \(\{F,B_0\}\).
3. Every lobe has type in \(\{F,C_0\}\).
4. All lobes have the same non-full type.

#### Proof

A lobe is eligible for \(L_b\) unless its type is \(F\) or \(B_0\),
and is eligible for \(L_c\) unless its type is \(F\) or \(C_0\).  Once
two eligible lobes are removed, the remaining union fails one of the four
retained rows exactly when every remaining lobe has one common type in
\(\{F,Q_1,Q_2,Q_3\}\).  Thus failure of (8.6) has the following exhaustive
possibilities.

First, eligible distinct lobes exist unless item 1, 2, or 3 holds.  Indeed,
absence of an \(L_b\)-candidate is exactly item 2, and absence of an
\(L_c\)-candidate is item 3.  If the only candidate for both roles were
one common lobe, every other lobe would have type simultaneously in
\(\{F,B_0\}\) and in \(\{F,C_0\}\), hence would have type \(F\).
There would be at least \(m-1\) such lobes, giving item 1.

Choose eligible distinct \(L_b,L_c\).  If their complement fails the
retained demand, its \(m-2\) lobes all have one common type
\(\lambda\in\{F,Q_1,Q_2,Q_3\}\).  For \(\lambda=F\) this is item 1.
For \(\lambda=Q_i\), the \(m-2\ge2\) lobes of type \(Q_i\) are themselves
eligible for both roles.  Choose two of them as \(L_b,L_c\).  If any lobe
of another type exists, it remains in the complement together with a
\(Q_i\)-lobe, and their union meets every row.  If none exists, all lobes
have the same type \(Q_i\), which is item 4.  This proves the asserted
alternative. \(\square\)

The lemma is only a seven-symbol allocation statement.  Its graph-theoretic
use is label-preserving and gives an actual separator alternative.

### Theorem 8.3 (\(K_7^{\vee}\) split versus exact owner two-cut)

Let \(X=\{x,y\}\) be a two-cut of the complex bag \(B\) in (8.1), and
let \(D_1,\ldots,D_m\) be the components of \(B-X\), where \(m\ge4\).
Then either the seven branch sets in (8.3) exist, or the lobe profiles have
one of the four exact forms in Lemma 8.2.  More explicitly, the four
separator outcomes are:

1. all apex feet outside at most two exceptional lobes lie in \(X\);
2. every lobe is dark to the apex-foot row or to the \(b\)-row;
3. every lobe is dark to the apex-foot row or to the \(c\)-row; or
4. one row has every portal in \(X\).

In outcome 4 the common row can only be a neutral row \(Q_i\), and then
\(Q_i=X\).

#### Proof

Every lobe meets both cut vertices.  Its external neighbourhood is
contained in \(X\) and the six singleton vertices in (8.1).  Since another
lobe lies beyond that neighbourhood, seven-connectivity gives at least
seven neighbours, so every lobe meets at least five of the six rows in
(8.5).  Apply Lemma 8.2.

In its packing outcome, set

\[
 P_b=D_b,\qquad P_c=D_c,\qquad
 R=B-(D_b\cup D_c).                                    \tag{8.7}
\]

The first two sets are connected.  The set \(R\) is connected: it contains
\(x,y\) and at least two remaining lobes, each adjacent to both cut
vertices.  It is adjacent to each of \(P_b,P_c\) through their edges to
\(x\) or \(y\).  The support conclusions in (8.6) are exactly the three
bullet conditions preceding (8.3).  Hence (8.3) is an explicit
\(K_7\)-model.

In item 1 of Lemma 8.2, only two exceptional lobes and the two cut vertices
can contain feet.  Items 2 and 3 are the displayed two-row dark webs.  In
item 4 every portal of the common missed row lies in \(X\).  But (8.2)
gives at least four feet and at least three \(b\)- and \(c\)-portals, so
none of those rows fits in \(X\).  A neutral row has at least two portals,
and hence must equal \(X\). \(\square\)

This theorem gives the requested split-versus-separator output: every
failure is located at the actual two-cut \(X\), and it names the precise
one- or two-row capacity which cannot be distributed through its lobes.

### Theorem 8.4 (all-operation state lock at the \(K_7^{\vee}\) cut)

Assume additionally that \(G\) is proper-minor-minimal non-six-colourable.
Put

\[
                 W=\{a,b,c,q_1,q_2,q_3,x,y\}.             \tag{8.8}
\]

The operation-state spectra on \(W\) of distinct open lobes are pairwise
disjoint.  There are at most

\[
                              3\cdot6^2=108                 \tag{8.9}
\]

such states, and hence at most 108 lobes.

#### Proof

The crossed-splicing proof is identical to Theorem 7.1 and uses the actual
separation with boundary \(W\).  The five-clique
\(\{b,c,q_1,q_2,q_3\}\) is rainbow.  Since \(a\) is adjacent to the three
\(q_i\) and nonadjacent to \(b,c\), its colour is the colour of \(b\), the
colour of \(c\), or the sixth colour absent from that clique.  Each of
\(x,y\) has at most six choices relative to the rainbow clique.  This gives
(8.9), and anti-coincidence gives the lobe bound. \(\square\)

Theorem 8.4 is the dynamic hypothesis absent from a static planar join.
It does not by itself force two spectra to meet; in the owner outcomes of
Theorem 8.3 the next step must transport the named dark row through one
lobe or splice it with an operation on the exceptional shore.

## 9. Three-connected bags: split or an exact seven-adhesion/state

The two-cut theorems do not apply to a three-connected complex bag.  The
label-free contraction splitter nevertheless gives an exact one-step
alternative once the *actual* near-clique split is used as its forbidden
portal pattern.

### Theorem 9.1 (near-clique portal contraction dichotomy)

Assume that \(G\) is proper-minor-minimal non-six-colourable.  In either
one-complex normalization (2.1) or (8.1), suppose \(B\) is
three-connected and \(|B|\ge5\).  Then at least one of the following
holds.

1. The relevant split certificate is realized in \(B\), and the explicit
   branch sets (2.8) or (8.3) give a \(K_7\)-minor.
2. There is an edge \(xy\in E(B)\) whose contraction preserves
   three-connectivity, fullness of every portal row, relative
   seven-connectivity, and nonrealization of the split certificate.  Every
   six-colouring after this contraction creates a genuinely new exact
   equality state on the labelled singleton boundary.
3. There is such a three-connectivity-preserving edge \(xy\) and a
   nonempty proper set \(Y\subseteq B-\{x,y\}\) such that

   \[
      |N_B(Y)|+|N_L(Y)|=7,qquad x,y\in N_B(Y),             \tag{9.1}
   \]

   where \(L\) is the six-vertex singleton boundary.  Thus
   \(N_B(Y)\cup N_L(Y)\) is an actual exact seven-separator in \(G\);
   each component of \(B[Y]\) meets every vertex of that boundary.

#### Proof

For a nonempty proper \(Z\subset B\), every external neighbour of \(Z\)
is either in \(N_B(Z)\) or is one of the six labelled singleton vertices
whose portal row meets \(Z\).  Seven-connectivity therefore gives

\[
                         |N_B(Z)|+|N_L(Z)|\ge7.              \tag{9.2}
\]

If the external neighbourhood exhausts the complement, (9.2) still holds:
the six singleton vertices and at least one vertex of \(B-Z\) occur in
it.  Thus \(B\) is full and relatively seven-connected as a boundaried
graph.

In the \(K_7^-\) case take as the forbidden portal pattern two adjacent
connected sets with demands

\[
                         \{F,C\},\qquad
                         \{F,Q_1,Q_2,Q_3,Q_4\}.              \tag{9.3}
\]

It is exactly Lemma 2.2.  In the \(K_7^{\vee}\) case take three disjoint
connected sets with demands

\[
 \{F,B_0\},\qquad\{F,C_0\},\qquad\{F,Q_1,Q_2,Q_3\},        \tag{9.4}
\]

and require the third set to be adjacent to each of the first two.  This
is exactly the certificate preceding (8.3).  Both are finite
portal-linkage patterns and lift through an edge contraction: expand the
unique branch set containing the contracted vertex to the two ends of the
edge.

Apply the portal splitter theorem to this forbidden pattern.  If the
pattern occurs, outcome 1 and the listed branch sets follow.  Otherwise a
three-connectivity-preserving contraction either preserves relative
seven-connectivity, giving the structural part of outcome 2, or exposes
the tight witness (9.1), giving outcome 3.  In the latter case ambient
seven-connectivity forces every component on the tight shore to meet all
seven boundary vertices.

Finally, for every internal contraction, a boundary colouring which also
extended over the original \(B\) would splice with the unchanged exterior
and six-colour \(G\).  Hence the contraction extension family contains a
state absent from the original side.  This is the exact all-operation
state novelty asserted in outcome 2. \(\square\)

Outcome 2 is deliberately one-step.  Pigeonholing states along a chain of
already-colourable contractions would be invalid.  Outcome 3, by contrast,
is a retained separator in the original graph and can be compared with a
faithful operation on its opposite shore.

### Audit 9.2 (hypotheses and the full-shore assertion)

The invocation in Theorem 9.1 uses every hypothesis of the portal splitter
as follows.

* \(B\) is a simple three-connected graph and \(|B|\ge5\) by assumption.
* The six singleton vertices are the disjoint labelled boundary; spanning
  normalization gives \(N_G(B)\subseteq B\cup L\).
* Every row is nonempty because (2.1) or (8.1) is a minor model, so the
  society is full.
* Equation (9.2), including its complement-exhaustion case, is precisely
  relative seven-connectivity.
* The two patterns (9.3)--(9.4) are finite, connected-support patterns and
  are contraction-closed by expanding the unique branch set containing a
  contraction vertex.

The final sentence of outcome 3 is also literal.  Put

\[
                         Z=N_B(Y)\cup N_L(Y),\qquad |Z|=7.    \tag{9.5}
\]

For a component \(K\) of \(B[Y]\), every neighbour lies in \(Z\).  If
some \(z\in Z\) were not adjacent to \(K\), then
\(|N_G(K)|\le6\), while \(z\) itself remains outside
\(K\cup N_G(K)\).  Deleting \(N_G(K)\) would separate \(K\) from \(z\),
contradicting seven-connectivity.  Hence \(N_G(K)=Z\): every component
meets all seven *actual vertices* of the boundary.  No contracted bag is
counted as one separator vertex.

### Lemma 9.3 (a five-clique in an exact seven-boundary closes)

Let \(Z\) be a seven-vertex separator in a seven-connected graph, and
suppose every component of \(G-Z\) has a neighbour at every vertex of
\(Z\).  If \(G[Z]\) contains a five-clique, then \(G\) contains a
\(K_7\)-minor.

#### Proof

Let \(L\subset Z\) be the five-clique, write \(Z-L=\{x,y\}\), and choose
components \(D_1,D_2\) on opposite sides of the separation.  Use

\[
                  D_1\cup\{x\},\qquad D_2\cup\{y\},
                  \qquad \{z\}\ (z\in L).                    \tag{9.6}
\]

The first two bags are connected.  They are adjacent because
\(D_1\sim y\) and \(D_2\sim x\) (either cross-edge suffices), and each is
adjacent to every singleton in \(L\) through its component.  The five
singletons form a clique.  These are seven pairwise adjacent branch sets.
\(\square\)

Consequently, the exact-adhesion outcome of Theorem 9.1 is already closed
whenever its singleton portion contains a five-clique.  In the
\(K_7^-\) normalization, a five-element singleton portion closes whenever
the omitted singleton is \(a\) or \(c\); the residual five-singleton case
omits one neutral \(q_i\) and contains only \(K_5^-\).  In the
\(K_7^{\vee}\) normalization, the five singletons other than \(a\) form a
clique, so that omitted-apex subcase closes as well.

More generally, if \(G-Z\) has at least three components and \(G[Z]\)
contains a four-clique, the same construction uses three components joined
to the three vertices of \(Z\) outside that clique and again gives seven
bags.  Thus a surviving exact adhesion with a four-clique has exactly two
full components.

## 10. Exact frontier after this note

The one-complex \(K_7^-\) route no longer stops at the connectivity-only
example.

* The exact \(K_2\vee I\) obstruction is excluded by the absence of
  universal vertices.
* All cyclic (and row-dense Hamiltonian) complex bags close explicitly.
* Every target-free 2-connected bag is a two-owner interval web in every
  foot-polar bipolar ordering.
* At a two-cut, varied capacity closes; many lobes collapse to one common
  dark row carrying disjoint all-operation spectra.
* For a one-complex \(K_7^{\vee}\)-model, every four-or-more-lobe two-cut
  gives the explicit three-shore split (8.3), or one of the exact owner
  separators in Theorem 8.3, again with disjoint all-operation spectra.

The live object is therefore a three-connected, all-neutral-rows-proper
portal society, or the common-dark-row lobe of (7.4).  Excluding it requires
one new operation-sensitive theorem: a dark-row transition must yield a
rooted split, a smaller owner core, or the same faithful state on the
opposite shore.  No connectivity-only claim is used for that last step.

## 11. What a large wall can and cannot prove

The first genuinely label-free invariant in a three-connected target-free
bag comes from Tutte's nonseparating-path theorem.

### Lemma 11.1 (every nonseparating deficient path owns a neutral row)

Assume the (K_7^-) normalization (2.1), let (B) be three-connected,
and suppose the split in Lemma 2.2 does not exist.  Choose

\[
        f_0,f_1\in F,\quad f_0\ne f_1,\qquad c_0\in C.       \tag{11.1}
\]

There is an \(f_0\)-\(c_0\) path \(P\subseteq B-f_1\) such
that \(B-P\) is connected.  Every such path satisfies

\[
                         Q_i\subseteq V(P)                    \tag{11.2}
\]

for at least one \(i\in\{1,2,3,4\}\).

#### Proof

Tutte's theorem says that for any three vertices \(x,y,z\) of a
three-connected graph, \(B-z\) has an \(x\)-\(y\) path whose vertex
deletion leaves \(B\) connected.  Apply it to
\((x,y,z)=(f_0,c_0,f_1)\).

Put \(R=B-P\).  Then \(P,R\) are nonempty and connected, and they are
adjacent because \(B\) is connected.  The path \(P\) meets \(F,C\), while
\(R\) meets \(F\) at \(f_1\).  If \(R\) met every \(Q_i\), this would be
exactly the split of Lemma 2.2.  Hence \(R\cap Q_i=\varnothing\) for some
\(i\), which is (11.2). \(\square\)

### Corollary 11.2 (rainbow blocker formulation)

Choose \(f_1\in F\) and representatives \(z_i\in Q_i\), allowing one
vertex to represent two rows.  There is no nonseparating path with one
end in \(F-\{f_1\}\), the other in \(C\), and avoiding

\[
                         \{f_1,z_1,z_2,z_3,z_4\}.             \tag{11.3}
\]

Equivalently, every rainbow transversal of the four neutral rows, together
with a reserved foot, is a blocker for the rooted nonseparating-path
problem.

This is the exact rooted-model principle exposed by the wall route.  A
large wall is useful only if it either routes around every blocker in
(11.3), or canonically orders the blockers in a web.  Merely having large
treewidth does not force the first outcome.

### Proposition 11.3 (static wall counterarchitecture: audited scope)

There is a completely uniform family of seven-connected,
\(K_7\)-minor-free graphs with a spanning one-complex \(K_7^-\)-model
whose complex bags have unbounded treewidth.  In that elementary family
two neutral rows are universal.

There are also explicitly verified strengthened members, at geodesic
frequencies \(3,4,5,6,7\), in which

* \(B\) is four-connected and its wall scale grows with the frequency;
* \(F\cap C=\varnothing\), with \(|F|,|C|\ge3\);
* every \(Q_i\) has at least two portals and at least two holes; and
* every vertex of \(B\) belongs to at most two neutral rows.

The strengthened construction is parametric, but its uniform
four-connectivity proof for every frequency has not yet been independently
audited.  The rigorous conclusions used below are therefore only that a
large wall does not force the rooted split under relative connectivity
alone, and that all additional static row constraints survive the same
architecture through every tested scale.

#### Construction and proof

For the uniform elementary family, let \(P_n\) be any sequence of
five-connected planar triangulations of unbounded treewidth and take
\(K_2\vee P_n\).  It is seven-connected.  It is \(K_7\)-minor-free:
discarding the at most two branch sets containing the join vertices from
a hypothetical \(K_7\)-model leaves a \(K_5\)-model in planar \(P_n\).
A facial diamond supplies (2.1), with the join vertices as two universal
neutral rows.

For the strengthened members, take \(P_n\) to be the frequency-\(n\)
geodesic triangulation of the icosahedron.  In its triangular coordinates
choose an edge \(q_3q_4\), with its two nonadjacent common neighbours
\(a,c\), and put

\[
                         B=P_n-\{a,c,q_3,q_4\}.                \tag{11.4}
\]

Choose the patch so that \(B\) is four-connected.  Add adjacent vertices
\(u,v\).  Initially make both complete to \(P_n\).  Delete the six edges
from \(u\) to

\[
 X=(N_{P_n}(q_3)\cup N_{P_n}(q_4))-\{a,c,q_3,q_4\},          \tag{11.5}
\]

and delete the edges from \(v\) to two degree-six vertices \(Y\) in the
same flat patch, disjoint from \(X\cup\{a,c,q_3,q_4\}\).  Take

\[
 q_1=u,\quad q_2=v,
\]

and keep \(a,c,q_3,q_4\) as the other four singleton bags.  They induce
\(K_6^-\), with \(ac\) missing.  The rows in \(B\) are

\[
\begin{array}{lll}
 F=N_B(a),& C=N_B(c),&Q_1=B-X,\\
 Q_2=B-Y,&Q_3=N_B(q_3),&Q_4=N_B(q_4).
\end{array}                                                \tag{11.6}
\]

The triangular patch gives the four displayed row properties directly.
In particular, a vertex adjacent to \(q_3\) or \(q_4\) has lost its
\(u\)-edge, so it still lies in at most two of
\(Q_1,\ldots,Q_4\).

Each verified strengthened member is seven-connected.  Indeed, if both
\(u,v\) are deleted, the
remaining at most four deletions cannot disconnect the five-connected
\(P_n\).  If only \(v\) is deleted, every component not contained in
\(X\) attaches to \(u\); the local six-vertex boundary of every nonempty
subset of \(X\) prevents a cut of total order six.  The argument with
\(u,Y\) is the same.  If neither is deleted, the disjoint hole sets
\(X,Y\) make every remaining vertex of \(P_n\) adjacent to at least one
of the adjacent vertices \(u,v\).

Finally each strengthened graph is a subgraph of \(K_2\vee P_n\), so the
same planar-minor argument excludes \(K_7\) and hence excludes the split
of Lemma 2.2.  In the uniform elementary family the treewidth is unbounded
because deleting the two join vertices leaves \(P_n\).  This proves the
uniform assertion; the additional strengthened assertions have the
explicitly stated verified scope. \(\square\)

The coordinate construction and the nontrivial connectivity/row checks
for frequencies \(3,4,5\) are independently reproduced by
near_k7_wall_web_counterarchitecture_verify.py; separate runs give the
same result at frequencies \(6,7\).  A uniform planar-coordinate proof
that the selected diamond deletion remains four-connected would promote
the strengthened sequence to a fully parametric theorem.

### Strategic consequence 11.4

The proposed assertion

\[
 \text{large wall + relative seven-connectivity + proper portal rows}
 \Longrightarrow \text{rooted split or a cut of order at most six}
\]

is false if “proper portal rows” is dropped, and the same architecture
survives that clause at every tested frequency.  The counterarchitecture
is deliberately six-colourable: delete \(u,v\) and four-colour \(P_n\).
Thus it does not refute an
operation-sensitive theorem for a hypothetical counterexample.  It shows
what that theorem must say.  The correct infinite-family alternative is

\[
                 \boxed{\text{rooted split, or a coherent two-apex web}},
                                                                    \tag{11.7}
\]

not bounded treewidth.  The web outcome is harmless only after its local
rotations are made globally coherent, because then deleting the two apex
labels leaves a planar graph and six-colourability follows.  Consequently
retained-shell state pumping should be used to synchronize incompatible
web rotations, not to try to bound the size or treewidth of a single
planar torso.

## 12. A rigorous retained-shell theorem for owner webs

The operation-sensitive part of the wall proposal is valid precisely when
the planar web exposes *actual constant-order adhesions*.  The following
form is independent of the Moser labels and of a particular embedding.

### Theorem 12.1 (four-owner triangular-web depth)

Let \(G\) be seven-connected and proper-minor-minimal non-six-colourable.
Let \(R\) be a fixed set of four vertices.  Suppose

\[
  (O_0,I_0),(O_1,I_1),\ldots,(O_m,I_m)                     \tag{12.1}
\]

is a strict nested sequence of separations such that

\[
 O_i\cap I_i=S_i=R\mathbin{\dot\cup}T_i,\qquad |T_i|=3.    \tag{12.2}
\]

Then

\[
                              m<2^{876}.                    \tag{12.3}
\]

The same conclusion holds when the four owner vertices vary, provided
they are transported coherently by seven disjoint paths through every
annulus.

#### Proof

Every adhesion has order seven.  Seven-connectivity gives seven disjoint
\(S_i\)-\(S_{i+1}\) paths through each open annulus; common owner vertices
are taken as trivial paths.  Propagate labels along these linkages.  On an
ordered seven-set there are

\[
 N(6,7)=\sum_{j=1}^{6}{7\brace j}=876
\]

equality partitions into at most six colour classes, hence at most
\(2^{876}\) extension families.  If (12.3) failed, two inward sides would
have the same transported extension family.  Retain the outer side, the
inner side, and the seven linkage strands between them; delete the other
annular material and contract the strands.  Strictness makes a proper
minor, while equality of extension families says that this minor is
six-colourable exactly when \(G\) is.  This contradicts proper-minor
minimality.  This is the minimum-separator state-depth argument, with the
four owner vertices made explicit. \(\square\)

### Lemma 12.2 (when a web triangle is an exact retained shell)

Let \(T\) be a separating triangle of a planar web torso inside \(B\), and
let \(K\) be a component on its inner side.  If precisely four singleton
labels \(R\subseteq L\) have neighbours in \(K\), then

\[
                              N_G(K)=T\cup R.                 \tag{12.4}
\]

In particular \(T\cup R\) is an actual seven-cut, and every component on
either open side is full to it.

#### Proof

The web decomposition gives \(N_B(K)=T\), while the definition of \(R\)
gives \(N_L(K)=R\).  Since the one-complex model is spanning, there are no
other neighbours, proving (12.4).  Its order is seven.  If a component
behind a minimum cut missed one cut vertex, the other six vertices would
still separate it from that missed vertex, contrary to
seven-connectivity. \(\square\)

### Corollary 12.3 (coherent web or bounded owner depth)

In a target-free two-apex web decomposition, any chain of separating
triangles whose inner lobes have one fixed four-label owner set has bounded
depth by (12.3).  If there is no such separating triangle and the two
apex labels are globally consistent, deleting those labels leaves the
compatible rural expansion of the planar torso; the graph is
six-colourable by four-colouring that expansion and assigning two fresh
colours to the deleted labels.

Thus a hypothetical counterexample cannot be an arbitrarily deep owner
web and cannot be a globally coherent two-apex web.  Its exact residual is
a bounded-depth *rotation conflict*: either a lobe sees at least five
labels, a separating triangle changes its four-label owner set, or two
adjacent rural pieces prescribe incompatible rotations.

This does not yet eliminate that residual.  It identifies the correct
dynamic exchange lemma:

> Across the first owner-set change or rotation conflict, either the two
> rural pieces contain the labelled split (9.3), or faithful minor
> operations on the two retained shores induce the same transported
> seven-boundary equality state.

The second outcome would colour \(G\) by crossed splicing.  Unlike a
quotient-contraction chain, both shores and the annulus are retained in
the original graph, so the proposed state comparison is legitimate.

### Corollary 12.4 (owner triangles feed the exact full-shore theorem)

Assume in Lemma 12.2 that \(G-S\) has exactly two components.  Then the
order-seven full-shore theorem applies verbatim: a cyclic hull of
\(\overline{G[S]}\) is crossed in one shore, and that crossing gives
either a \(K_7\)-minor or an actual covering bad split on the seven
labels, carrying the one-step faithful minor-transition condition.

If \(G-S\) has at least three components and \(G[R]\cong K_4\), the
\(K_7\)-minor is immediate: use the four vertices of \(R\) as singleton
bags and merge three distinct full components with the three vertices of
\(T\).  The latter three bags are pairwise adjacent through their
cross-contacts to \(T\), and each is adjacent to all four singleton bags.

If \(G[R]\cong K_4^-\), with missing pair \(a,c\), the same conclusion
holds as soon as \(G-S\) has four components
\(D_0,D_1,D_2,D_3\).  Use

\[
 D_0\cup\{a\},\quad \{c\},\quad\{q\},\quad\{q'\},\quad
 D_i\cup\{t_i\}\ (1\le i\le3),                         \tag{12.5}
\]

where \(R=\{a,c,q,q'\}\) and \(T=\{t_1,t_2,t_3\}\).
Fullness supplies every asserted adjacency, including the repaired
\(a\)-\(c\) pair and all adjacencies among the last three bags.

Consequently a target-free owner triangle has only three exits:

1. exactly two full shores and the already finite covering-bad-split
   state;
2. exactly three full components and the owner set contains the deficient
   pair \(a,c\), so \(G[R]\cong K_4^-\); or
3. the separator belongs to a bounded-depth chain from Theorem 12.1.

This makes the rotation problem narrower than an arbitrary planar-web
compatibility theorem.  The genuinely new local lemma is needed only for
the \(K_4^-\) owner set or for one of the finite covering bad splits.

### Lemma 12.5 (five cross-contacts close the three-component exception)

In outcome 2 of Corollary 12.4, write

\[
 R=\{a,c,q,q'\},\qquad ac\notin E(G),\qquad
 T=\{t_1,t_2,t_3\}.
\]

If

\[
                         e_G(T,R)\ge5,                       \tag{12.6}
\]

then \(G\) has a \(K_7\)-minor.

#### Proof

Contract each of the three full components of \(G-S\) to one vertex and
delete surplus edges.  The resulting ten-vertex quotient consists of

* \(K_4^-\) on \(R\);
* \(K_3\) on \(T\);
* three pairwise nonadjacent vertices complete to \(R\cup T\); and
* the \(3\)-by-\(4\) contact matrix between \(T\) and \(R\).

There are \(2^{12}=4096\) such matrices.  Exhaustive branch-set search
over every seven-block partition of every support of order seven through
ten shows that every matrix with at least five entries has a \(K_7\)
model.  The search is reproduced by
near_k7_owner_triangle_quotient_verify.py.  It checks 11,880 candidate
partitions for each matrix.  As an adversarial completeness check, exactly
226 matrices are negative; their 60 inclusion-maximal members all have at
most four entries.  Every quotient model lifts through the three component
contractions. \(\square\)

Thus the sole three-component triangular owner residue is not an arbitrary
web: every separator vertex in \(T\) collectively has at most four
contacts to the four owner labels.  Any degree or transition argument
which forces a fifth contact closes the whole cell at once.

The same enumeration gives a sharper, human-sized residue.  Up to
interchanging \(a,c\), interchanging \(q,q'\), and permuting
\(t_1,t_2,t_3\), every negative contact matrix is contained in one of

\[
\begin{array}{c|ccc}
 &N_R(t_1)&N_R(t_2)&N_R(t_3)\\ \hline
\mathrm{I}&\{q,q'\}&\{q\}&\varnothing\\
\mathrm{II}&\{c,q\}&\{a,q\}&\varnothing\\
\mathrm{III}&\{a,q\}&\{c\}&\{a\}\\
\mathrm{IV}&\{q'\}&\{q\}&\{a\}.
\end{array}                                                \tag{12.7}
\]

These are the four orbits of the 60 inclusion-maximal negative matrices.
In particular the cross-contact graph is a forest and at least one owner
label is dark to all three triangle vertices.  This is an exact
four-pattern portal theorem, not an unbounded web enumeration.
