# The (K_{3,3}\vee K_1) boundary: two-piece surgery and portal locality

## 1. Setting

Let (G) be seven-connected and (K_7)-minor-free.  Let

\[
 S=A\mathbin{\dot\cup}B\mathbin{\dot\cup}\{c\},
 \qquad |A|=|B|=3,
\]

with (G[S]=K_{3,3}\vee K_1), where (c) is the universal boundary
vertex.  Suppose (G-S) has exactly two connected full shores (D,D').
For (X\subseteq D), write (L(X)=N_S(X)).  Call a subset of (S)
**triangle-limited** if it is contained in

\[
 \{c,a,b\}\quad\text{for some }a\in A, b\in B.       \tag{1.1}
\]

Equivalently, it contains at most one member of (A) and at most one
member of (B).

## 2. The two-piece surgery lemma

### Lemma 2.1

Suppose (D=X\mathbin{\dot\cup}Y), where (X,Y) are nonempty connected
sets and there is an (X)-(Y) edge.  If neither (L(X)) nor (L(Y))
is triangle-limited, then (G) contains a (K_7)-minor.

### Proof

Since (D) is full, (L(X)\cup L(Y)=S).  Put

\[
 p=|L(X)\cap A|,quad q=|L(X)\cap B|,quad
 r=|L(Y)\cap A|,quad s=|L(Y)\cap B|.
\]

The covering condition gives (p+r\ge3) and (q+s\ge3).  Since neither
contact set is triangle-limited,

\[
 (p\ge2\text{ or }q\ge2),\qquad
 (r\ge2\text{ or }s\ge2).                           \tag{2.1}
\]

If neither (p\ge2,s\ge2) nor (q\ge2,r\ge2) held, then, after
possibly interchanging (A,B), (2.1) would give (p\ge2), (s\le1),
and hence (q\ge2); the second failed alternative would then give
(r\le1).  This makes (L(Y)) triangle-limited, a contradiction.
Thus, up to interchanging (A,B) and (X,Y), there are distinct

\[
 a_1,a_2\in A\cap L(X),\qquad
 b_1,b_2\in B\cap L(Y).
\]

Let (a_3,b_3) be the unused members of (A,B).  The seven bags

\[
 \{a_1\},\quad \{b_1\},\quad \{c\},\quad D',\quad
 \{a_3,b_3\},\quad X\cup\{a_2\},\quad Y\cup\{b_2\}   \tag{2.2}
\]

form a (K_7)-model.  The last two bags are connected by the selected
contacts and are adjacent through the (X)-(Y) edge.  Their contacts
at (a_1,b_1) repair the two same-part nonedges.  The fifth bag is
connected through (a_3b_3), all remaining adjacencies among
boundary-containing bags follow from (G[A,B]) and the universal
vertex (c), and the opposite full shore (D') sees every other bag.

### Corollary 2.2 (exact contact obstruction)

In a (K_7)-minor-free realization, every connected bipartition of a
full shore has a triangle-limited side.

The dependency-free verifier `k331_two_piece_contact_atlas.py` audits a
slightly stronger finite statement.  It checks all (3^7=2187) contact
pairs for two adjacent contracted shore pieces.  The maximal negative
pairs are exactly

\[
 (S,\{c,a,b\})\quad\text{and}\quad
 (\{c,a,b\},S),\qquad a\in A, b\in B.              \tag{2.3}
\]

Thus the hand obstruction in Corollary 2.2 is also exact at the
two-piece quotient level; the proof of Lemma 2.1 itself does not depend
on the enumeration.

## 3. Connectivity forced inside each shore

### Lemma 3.1 (orders at most four)

No full shore has order at most four in the counterexample-derived
setting.

### Proof

A singleton shore is excluded by the exact-block contraction argument:
contract that shore together with (A), colour the proper minor with
six colours, expand (A) as one exact block, and colour the singleton
shore with a colour absent from the at-most-five-colour boundary.

Now let (2\le |D|=n\le4).  For every (x\in D), the set

\[
 N_D(x)\cup L(x)
\]

separates (x) from (D').  Seven-connectivity and
(|N_D(x)|\le n-1) give

\[
 |L(x)|\ge8-n\ge4.                                  \tag{3.1}
\]

Choose a connected bipartition of (D) whose two sides each contain a
vertex (for a connected graph, take the two sides of an edge of a
spanning tree).  If necessary choose a leaf side first and then note
that its complement is connected.  Each side contains a vertex whose
contact set has order at least four, so neither side is
triangle-limited.  Lemma 2.1 gives a (K_7)-minor, a contradiction.

### Lemma 3.2 (shore four-connectivity)

Every full shore is four-connected.

### Proof

Lemma 3.1 handles the small complete-graph conventions.  Suppose first
that (xy) is a bridge of (D), with sides (X,Y).  The set
(L(X)\cup\{y\}) separates (X) from (D'), and symmetrically on the
other side.  Hence seven-connectivity gives

\[
 |L(X)|,|L(Y)|\ge6.
\]

Lemma 2.1 is a contradiction.  Thus (D) has no bridge.

If (z) is a cutvertex and (C_1,C_2) are two components of (D-z),
then (L(C_i)\cup\{z\}) separates (C_i) from (D'), so
(|L(C_i)|\ge6).  The sets (C_1) and (D-C_1) are connected and
adjacent, and each has at least six boundary contacts.  Again Lemma 2.1
is a contradiction.  Thus (D) is two-connected.

Let (Z=\{z_1,z_2\}) be a two-cut.  Every component of (D-Z) meets
both (z_1,z_2), since otherwise one of them is a cutvertex.  Also, for
every such component (C),

\[
 |L(C)|+|Z|\ge7,qquad\text{so }|L(C)|\ge5.          \tag{3.2}
\]

For distinct components (C_1,C_2), the sets
(C_1\cup\{z_1\}) and (D-(C_1\cup\{z_1\})) are connected and
adjacent, and contain (C_1,C_2), respectively.  Both have at least
five contacts, contrary to Lemma 2.1.  Thus (D) is three-connected.

Finally let (Z) be a three-cut.  Three-connectivity implies that every
component of (D-Z) meets all three members of (Z), while global
seven-connectivity gives at least four boundary contacts in every such
component.  If (C_1,C_2) are two components, then (C_1) and
(D-C_1) are connected and adjacent; each contains a component with at
least four contacts.  Lemma 2.1 gives the final contradiction.

## 4. Locality of all portal rows

### Lemma 4.1 (single vertices)

For every (x\in D), (L(x)) is triangle-limited.

### Proof

Four-connectivity makes (D-x) connected.  Apply Corollary 2.2 to the
split \(\{x\},D-x\).  If (L(D-x)) were triangle-limited, then

\[
 N_G(D-x)\subseteq\{x\}\cup L(D-x)
\]

would be a cut of order at most four separating (D-x) from (D'),
contrary to seven-connectivity.  Hence (L(x)) is the
triangle-limited side.

### Lemma 4.2 (edges and connected triples)

If (X\subseteq D) is connected and (1\le |X|\le3), then (L(X))
is triangle-limited.  In particular the union of the contact rows at
the ends of every edge is triangle-limited.

### Proof

Four-connectivity makes (D-X) connected.  Corollary 2.2 says one side
is triangle-limited.  If it were (D-X), then

\[
 N_G(D-X)\subseteq X\cup L(D-X)
\]

would have order at most (3+3=6) and separate (D-X) from (D').
Thus (L(X)) is triangle-limited.

Consequently adjacent vertices cannot have contacts at two distinct
members of (A), nor at two distinct members of (B).  More generally,
the portal sets in (D) belonging to distinct vertices of the same
boundary triple are at distance at least three in (D).

## 5. Strengthening the pendant-portal lock

Suppose a shore fails to contain a rooted triangle on
(T\in\{A,B\}).  The pendant-portal theorem in
`hadwiger_k33_portal_triangle.md` supplies (t\in T), its unique shore
neighbour (z), and a connected set (R=D-z) full to (S-\{t\}),
with (z) adjacent to neither other member of (T).

### Corollary 5.1 (sharp portal row)

There is a vertex (u) of the opposite independent triple such that

\[
 N_S(z)\subseteq\{t,c,u\}.                           \tag{5.1}
\]

In particular, the exceptional portal has at most three boundary
contacts and at most one contact in the opposite triple.

### Proof

This is Lemma 4.1 together with (zt\in E(G)).  Since (z) has no
contact at the other two vertices of (T), its triangle-limited row
must have the displayed form.

The remaining lock is therefore not an arbitrary unique-portal
configuration.  Its core (R) is connected and six-full, its portal
(z) has at least four neighbours in (R) (seven-connectivity applied
to the singleton (z), together with (|N_S(z)|\le3)), and every edge
and connected three-vertex set of the entire shore has a common
one-(A), one-(B) portal triangle.  Any closure of the lock may now
work with this sharply local contact geometry rather than with
unrestricted portal rows.

## 6. Rooted triangles and complete closure

The local portal restriction and shore connectivity actually close the
boundary without any further analysis of the pendant lock.

### Lemma 6.1

Each full shore contains both an (A)-rooted triangle and a
(B)-rooted triangle.

### Proof

Fix one shore (D).  For each (a\in A), fullness supplies a vertex
(x_a\in N_D(a)).  Lemma 4.1 says that a shore vertex has at most one
neighbour in (A), so the three vertices (x_a) are distinct.

By Lemma 3.2, (D) is two-connected (indeed four-connected).  A
two-connected graph has a rooted (K_3)-model at any three prescribed
vertices: take a cycle through two of them and a two-fan from the third
to that cycle, or apply the standard fan lemma.  Let its three branch
sets be rooted at the vertices (x_a).  Adjoin each boundary vertex
(a) to the branch set containing (x_a).  The sets remain disjoint,
connected, and pairwise adjacent, and now form an (A)-rooted triangle
in (G[D\cup A]).

The same argument, using Lemma 4.1 to make three distinct choices in
the (B)-portal sets, gives a (B)-rooted triangle.

### Theorem 6.2 (closure of the (2K_3\dot\cup K_1) six-edge core)

The boundary (G[S]=K_{3,3}\vee K_1) cannot occur at an order-seven
counterexample-derived full-shore adhesion.

### Proof

Apply Lemma 6.1 to obtain an (A)-rooted triangle in (D_1) and a
(B)-rooted triangle in (D_2).  Their six branch sets, together with
the singleton bag \(\{c\}\), are pairwise adjacent: adjacency within
each triple comes from its rooted model, adjacency between triples comes
from (G[A,B]=K_{3,3}), and (c) is adjacent to every boundary root.
They form a (K_7)-model, contrary to the hypothesis.

Thus type 2 in the exact six-edge atlas is closed for shores of arbitrary
order.  The sole remaining exact six-edge complement is
(C_6\dot\cup K_1).
