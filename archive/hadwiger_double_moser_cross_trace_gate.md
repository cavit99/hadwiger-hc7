# A cross-trace rooted-(K_5)-or-gate lemma

## 1. Double-Moser frame

Let (G) be a proper-minor-minimal non-six-colourable graph and use the
adjacent degree-seven double-Moser notation

\[
 X=\{x_1,x_2,x_3,x_4\},\qquad A=\{a,b\},\qquad P=\{p,q\},
\]

where

\[
 N(u)=\{v\}\dot\cup X\dot\cup P,
 \qquad N(v)=\{u\}\dot\cup X\dot\cup A.
\]

The fixed edges include

\[
 x_1x_2,x_3x_4,ab,pq,
 \quad ax_1,ax_2,bx_3,bx_4,
 \quad qx_1,qx_2,px_3,px_4.
\tag{1.1}
\]

Fix the common cross nonedge (S=\{x_1,x_3\}).  Contract the connected
star (G[\{u,x_1,x_3\}]), colour the resulting proper minor with six
colours, and expand the star after deleting its centre.  This gives a
six-colouring (c) of (G-u) in which (x_1,x_3) have one colour
(alpha), while

\[
 T=\{v,x_2,x_4,p,q\}
\tag{1.2}
\]

has five pairwise distinct colours.  The trace is exact: these are all six
colours.

The graph induced by (T) is the cycle

\[
 v x_2 q p x_4 v,
\tag{1.3}
\]

and its missing-pair graph is the complementary cycle

\[
 F=vp,\;px_2,\;x_2x_4,\;x_4q,\;qv.
\tag{1.4}
\]

## 2. All five unique colours form a Kempe colouring

### Lemma 2.1

For any two vertices (s,t\in T), the vertices (s,t) lie in one
({c(s),c(t)})-component of (G-u).

#### Proof

If they lay in different components, switch the component containing
(s).  The vertex (s) is the unique member of (N(u)) with its old
colour, and (t) is the unique member with the new colour.  Thus the old
colour of (s) disappears from (N(u)).  Giving that colour to (u)
would six-colour (G), a contradiction.  (square)

Delete the entire colour class (alpha), and call the resulting
five-coloured graph (J_0).  Lemma 2.1 says that its five colour classes
form a Kempe colouring with transversal (T).

## 3. Reserving the literal opposite connector

The path

\[
                         R_A=x_1abx_3
\tag{3.1}
\]

is connected.  Its two internal vertices do not have colour (alpha),
because (a x_1,bx_3\in E(G)).  Put

\[
                         J=J_0-\{a,b\}.
\tag{3.2}
\]

### Theorem 3.1 (rooted (K_5) or a two-vertex Kempe gate)

At least one of the following holds.

1. (G) contains a (K_7)-minor.
2. For some edge (st\in E(F)), every
   ({c(s),c(t)})-coloured (s)-(t) path in (J_0) meets
   ({a,b}).  Equivalently, the set
   ({a,b}\cap c^{-1}(\{c(s),c(t)\})), of order one or two,
   separates (s) from (t) in that bichromatic graph.

#### Proof

Suppose outcome 2 fails.  Then every edge of the cycle (F) is realised
in (J) by a Kempe chain between its ends.  A cycle has property
((*)) in the sense of Kriesell--Mohr (more generally, every connected
graph with at most one cycle has that property).  Hence (J) contains
five disjoint connected branch sets ((B_t:t\in T)), rooted at (T),
such that (B_s,B_t) are adjacent whenever (st\in E(F)).

For the other five pairs, the literal edges of the cycle (1.3) join the
corresponding roots.  Thus the same five bags form a (T)-rooted
(K_5)-model in (J).

Now use the seven bags

\[
                  \{u\},\qquad V(R_A),\qquad (B_t:t\in T).
\tag{3.3}
\]

They are disjoint: the rooted model avoids the (alpha)-class and also
avoids (a,b).  The singleton (u) sees every other bag through its
seven neighbours.  The connector (R_A) sees the five rooted bags
through, respectively,

\[
 x_1v,\quad x_1x_2,\quad x_3x_4,\quad x_3p,\quad x_1q.
\]

The rooted bags are pairwise adjacent.  Hence (3.3) is a (K_7)-model,
proving outcome 1.  (square)

### Corollary 3.2 (paired gate at the other centre)

Apply the same argument at (v), using the exact trace obtained by
contracting (\{v,x_1,x_3\}).  Unless (G) has a (K_7)-minor, one
edge of the complementary cycle on

\[
                         \{u,x_2,x_4,a,b\}
\]

has all of its bichromatic paths blocked by (\{p,q\}).

Thus a (K_7)-minor-free double-Moser frame has two simultaneous,
colour-specific gates: an (A)-gate in a (u)-trace and a (P)-gate
in a (v)-trace.  The traces are different colourings, so their colour
names must not be identified.  What is invariant is the pair of blocked
edges in the two complementary five-cycles.

## 4. Scope

The theorem closes an infinite family: any cross trace for which the five
complementary-cycle Kempe chains survive deletion of the opposite literal
connector gives (K_7) immediately.  It does **not** yet eliminate the
simultaneous two-gate residue.  Closing that residue requires either

* converting the two bichromatic gates into a common colour-gluable
  adhesion, or
* showing that their portal orders cross and yield the existing
  three-carrier (K_7)-certificate.

No contraction-colouring interchange is used: all Kempe switches and
paths live in the fixed star-trace colouring of (G-u) (or, separately,
of (G-v)).

## 5. Label-free form

The proof uses the Moser labels only to verify a small frame condition.
The operative statement is the following.

### Proposition 5.1 (self-complementary trace gate)

Let (G) be non-(k)-colourable while every proper minor is
(k)-colourable.  Suppose (u) has (k+1) neighbours and an independent
pair (S\subseteq N(u)) has the following properties.

1. Contracting the star on (\{u\}\cup S) gives an exact trace in which
   (S) is one colour block and the set (T=N(u)-S) consists of (k-1)
   singleton colour blocks.
2. The missing-edge graph (F=\overline{G[T]}) has property ((*)).
3. There is a connected set (R), disjoint from (\{u\}\cup T), which
   contains (S) and is adjacent to every vertex of (T).

Then either (G) has a (K_{k+1})-minor, or, in the exact trace
colouring, deletion of (V(R)-S) destroys a bichromatic connection
corresponding to some edge of (F).

#### Proof

Delete the repeated colour class and (V(R)-S).  If every edge of (F)
is still represented by a Kempe chain, property ((*)) gives a
(T)-rooted (F)-model.  Literal edges of (G[T]) supply every
complementary bag adjacency, so the same bags form a rooted
(K_{k-1})-model.  Together with (R) and the singleton (u), these are
(k+1) pairwise adjacent bags.  The contrapositive is the asserted gate
outcome. (square)

For the double-Moser frame, (k=6), both (G[T]) and (F) are
five-cycles, and (R=x_1abx_3).  Proposition 5.1 isolates the reusable
principle: a selectable equality pair plus a self-complementary rooted
frame either completes the clique minor or forces a small, colour-specific
gate through the reserved connector.
