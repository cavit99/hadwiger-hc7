# Capacity ownership excludes the atomic three-shore Moser core

## 1. Setting and atomic hypothesis

Let \(G\) be a seven-connected, six-minor-critical,
\(K_7\)-minor-free graph with \(\delta(G)\ge7\).  Let \(S\) be a
seven-cut such that

\[
 G-S=D_1\mathbin{\dot\cup}D_2\mathbin{\dot\cup}D_3,
 \qquad N(D_i)=S,
\]

and suppose \(G[S]\) is the pure Moser spindle

\[
 E(G[S])=
 \{01,02,03,04,12,16,26,34,35,45,56\}.           \tag{1.1}
\]

Call a shore **atomic** if:

1. it has at least six vertices;
2. it is three-connected; and
3. there do not exist \(s\in S\), a six-set \(X\subseteq V(D)\), and a
   component \(C\) of \(D-X\) such that

   \[
                      N_G(C)=X\cup\{s\}.             \tag{1.2}
   \]

Thus (3) says precisely that no seven-set consisting of six shore
vertices and one boundary vertex cuts off a nested exact seven-fragment.

The third condition is the precise no-descent hypothesis used below.

### Theorem 1.1 (atomic three-shore Moser exclusion)

The three shores cannot all be atomic.

Thus every three-component Moser seven-cut exposes at least one of:

* a shore of order at most five;
* a one- or two-vertex cut inside a shore; or
* a nested exact seven-cut.

This eliminates the entire large three-connected infinite family and
routes the residue to a small shore, a low-order portal decomposition,
or exact-cut descent.  A one- or two-cut does not by itself bound the
orders of its pieces.

## 2. Unique capacity ownership

The complement of (1.1) has edges

\[
 05,06,13,14,15,23,24,25,36,46.                  \tag{2.1}
\]

An optimal four-colouring of the Moser spindle is a matching of three
edges of (2.1), together with its unmatched singleton.  There are
sixteen such partitions.

For every such partition

\[
 \Pi=e_1\mid e_2\mid e_3\mid\{s\},                \tag{2.2}
\]

Corollary 6.2 of `hadwiger_three_shore_block_capacity.md` gives a
unique **owner**: exactly one shore contains disjoint connected carriers
for some two of \(e_1,e_2,e_3\).  Each of the other two shores is a
**non-owner**, and contains no such two-block linkage for any pair of
the three matching edges.

Hence the sixteen partitions create exactly

\[
                    2\cdot16=32                  \tag{2.3}
\]

non-owner incidences among the three shores.

## 3. A non-owner matching is antipodal

### Lemma 3.1 (common-face lemma)

Let \(D\) be an atomic shore and let (2.2) be a partition for which
\(D\) is a non-owner.  Then the six portal classes

\[
 P_x=N_D(x)\qquad(x\in S-\{s\})
\]

lie on one face in the unique plane embedding of \(D\).

#### Proof

Apply the portal-transversal theorem to the six classes, taking the
omitted singleton \(s\) as the seventh boundary vertex.  Seven-
connectivity and \(|D|\ge6\) give distinct representatives

\[
                    p_x\in P_x\qquad(x\in S-\{s\}).       \tag{3.1}
\]

For clarity, the Hall argument is direct.  If a subfamily indexed by
\(I\subseteq S-\{s\}\) had union \(U\) with \(|U|<|I|\), then either
\(D=U\), contrary to \(|D|\ge6\ge |I|\), or a component of \(D-U\)
would have all its neighbours in

\[
                 U\cup(S-I),
\]

a set of order at most six.  The other shores give a nonempty far side,
contrary to seven-connectivity.

For each pair among \(e_1,e_2,e_3\), the corresponding two-linkage is
absent.  To use the same-vertex form of the Two Paths Theorem, add four
artificial terminals, one for each involved boundary root, and join a
terminal to its complete portal set.  A cross is exactly a pair of
disjoint connected carriers, so the resulting tuple is crossless.
Complete it on the same vertex set to a maximal crossless graph.  The
Two Paths Theorem represents that graph as a web with the four
artificial terminals on its frame.

Every nonempty clique inserted behind a facial triangle would contain
an original shore vertex.  Its neighbours in the represented graph are
among the three vertices of that triangle.  Replace an artificial
terminal among those three vertices by its boundary root, and add the
three boundary roots omitted from the four-terminal demand.  This gives
an actual separator in \(G\) of order at most six, with an untouched
shore on the far side, contrary to seven-connectivity.  The web is
therefore bare.  Delete the four frame terminals and all completion
edges.  All four complete portal sets are incident with the one face
created from the frame face.

Thus \(D\) is planar.  Since \(D\) is three-connected, Whitney
uniqueness makes its plane embedding unique up to reflection.  In this
fixed embedding, let \(F_{12},F_{23},F_{31}\) be faces containing
respectively the four complete portal classes belonging to
\(e_1\cup e_2,e_2\cup e_3,e_3\cup e_1\).

If two of these faces coincide, that face contains all six classes.  A
distinct third face would share four distinct portal representatives
with it, impossible because two distinct faces of a three-connected
plane graph intersect in at most one edge.  Thus in this case all three
faces coincide.

Suppose instead that all three faces are distinct.  Each pairwise face
intersection contains the two distinct representatives in (3.1)
belonging to the shared matching edge.  In a three-connected plane
graph two distinct face boundaries meet in at most one edge.  Hence
each of the three intersections is exactly an edge, and these three
edges are pairwise vertex-disjoint.

More is true than the statement about the chosen representatives.  If
\(e_i=xy\), then both complete sets \(P_x,P_y\) lie in each of the two
faces whose indices contain \(i\), and hence lie in their intersection
edge.  The distinct representatives \(p_x,p_y\) occupy its two ends.
Consequently the union of all six portal sets has order exactly six.

Let \(X\) be the union of the six portal sets.  The preceding paragraph
gives \(|X|=6\).  If \(D-X\ne\varnothing\), every component \(C\) of
\(D-X\) has

\[
 N_G(C)\subseteq X\cup\{s\}.                      \tag{3.2}
\]

The other shores lie outside \(C\cup X\cup\{s\}\).  Seven-connectivity
therefore forces equality in (3.2), which is precisely the nested
fragment forbidden by (1.2).

It remains that \(D=X\).  Each of the three faces contains its two
pairwise-intersection edges and cannot contain an end of the third
intersection edge: that would give an additional intersection with one
of the other faces.  Hence each face has exactly four vertices and is a
four-cycle.  Their union is an annulus whose two boundary components
are three-cycles.  There is no place for an additional edge: the three
four-cycles are faces, while each of the two complementary regions is
already bounded by a triangle.  Hence \(D\) is exactly the
unsubdivided triangular prism.

A prism vertex has three neighbours in \(D\).  The complete-portal-set
containment proved above says that it can meet only the two boundary
portal classes assigned to its shared edge, and it may additionally
meet the omitted vertex \(s\).
Thus its degree in \(G\) is at most six, contrary to
\(\delta(G)\ge7\).

The all-distinct-face case is impossible, so the three faces coincide.
\(\square\)

### Lemma 3.2 (antipodal order)

On the common face of Lemma 3.1, the three pairs
\(e_1,e_2,e_3\) are the antipodal pairs of the cyclic order of their six
distinct representatives.

#### Proof

If two of the three pairs did not alternate on the facial cycle, two
disjoint facial arcs would join their respective representative pairs.
Those arcs would be disjoint connected carriers for the two boundary
blocks, contrary to the non-owner property.  Thus every two of the
three chords alternate.  Three disjoint chords on six cyclically
ordered points are pairwise alternating exactly when their endpoints
occur in the word

\[
 e_1,e_2,e_3,e_1,e_2,e_3
\]

up to permutation and reversal.  Equivalently, the three matching edges
are the three antipodal pairs. \(\square\)

## 4. Seven non-owner states per shore

### Lemma 4.1

An atomic shore is a non-owner for at most seven of the sixteen Moser
partitions.

#### Proof

Fix the unmatched singleton \(s\).  Suppose two different perfect
matchings of \(S-\{s\}\) both made \(D\) a non-owner.  Lemma 3.1 puts
the same six full portal classes on a face for each matching.  The two
faces must be equal: otherwise their intersection would contain the six
distinct portal representatives, while distinct faces meet in at most
one edge.

The cyclic order on that face has a unique antipodal perfect matching.
Lemma 3.2 therefore says that at most one partition with singleton
\(s\) can make \(D\) a non-owner.  There are seven choices of \(s\),
proving the bound. \(\square\)

## 5. Counting contradiction

If all three shores were atomic, Lemma 4.1 would bound the total number
of non-owner incidences by

\[
                       3\cdot7=21.
\]

But unique ownership gave exactly \(32\) in (2.3).  This contradiction
proves Theorem 1.1. \(\square\)

For reference, the sixteen matchings can be checked without graph
isomorphism software by grouping them according to the unmatched
singleton:

\[
\begin{array}{c|l}
0&13\,25\,46;\ 14\,25\,36;\ 15\,23\,46;\ 15\,24\,36\\
1&05\,23\,46;\ 05\,24\,36\\
2&05\,13\,46;\ 05\,14\,36\\
3&06\,14\,25;\ 06\,15\,24\\
4&06\,13\,25;\ 06\,15\,23\\
5&06\,13\,24;\ 06\,14\,23\\
6&05\,13\,24;\ 05\,14\,23.
\end{array}
\]

## 6. Structural meaning

The proof does not enumerate exterior graphs.  It turns the Moser
boundary into a capacity-ownership invariant, turns capacity failure
into a common facial order, and then uses the elementary fact that one
cyclic order has only one antipodal matching after a fixed vertex is
deleted.  The numerical contradiction \(32>21\) eliminates all atomic
large shores simultaneously.

The exact remaining local work is now confined to the three outcomes in
Theorem 1.1.  A nested exact cut feeds the already normalized two-/three-
shore recursion.  A one- or two-cut supplies a low-order
portal-distribution decomposition (whose pieces can still be
arbitrarily large), and a shore of order at most five is a finite
kernel.
