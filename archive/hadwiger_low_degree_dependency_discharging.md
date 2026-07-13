# Low-degree dependency: a two-centre lemma and the degree-nine hub cap

## 1. Scope

Let (G) be non-six-colourable while every proper minor of (G) is
six-colourable.  In the zero-optional full-singleton endpoint, a
degree-seven vertex (d) has a distinguished neighbour (b), four
common neighbours inducing (2K_2), and (d_G(b)\geq 9).  The purpose
of this note is to determine what can actually be extracted by orienting
(d\to b) globally.

There are two positive conclusions.  The first is a fully elementary
two-centre compression theorem, including nonadjacent centres.  The
second is an exact finite capacity bound at a degree-nine hub.  The
capacity bound is computer-certified; its transparent 36-variable
encoding is archived in `singleton_hub_indegree_capacity_z3.py`.

The resulting cap does not, by itself, make Mader's degree inequality a
contradiction.  Thus a global discharging proof still needs either a
degree-at-least-ten analogue or a mechanism which turns several distinct
hub traces into a labelled minor.

## 2. Simultaneous compression at two centres

### Theorem 2.1 (two-centre independent compression)

Let (G) be non-(k)-colourable while every proper minor is
(k)-colourable.  Let (x,y) be distinct vertices and let

\[
 S=I_x\mathbin{\dot\cup}I_y\subseteq N(x)\cap N(y),
\]

where (I_x,I_y) are nonempty independent sets.  Suppose

\[
 |S|\ge d(x)-k+3,qquad |S|\ge d(y)-k+3.          \tag{2.1}
\]

Then this configuration is impossible.

#### Proof

Contract the two disjoint stars

\[
 \{x\}\cup I_x,qquad \{y\}\cup I_y
\]

and (k)-colour the resulting proper minor.  Delete the two centres
and expand only the leaves.  This properly colours (G-\{x,y\}): each
leaf set is independent, and if an edge joins the two leaf sets then
the two contracted images were adjacent and therefore received
different colours.

The set (S) uses at most two colours.  If (xy\notin E(G)), then

\[
 |[k]-c(N(x))|\ge k-\bigl(2+d(x)-|S|\bigr)\ge1,
\]

and likewise at (y).  Since (x,y) are nonadjacent, choose an
available colour at each centre independently and extend the colouring
to (G), a contradiction.

If (xy\in E(G)), the other centre is absent from the already coloured
neighbourhood.  Hence

\[
 |[k]-c(N(x)-\{y\})|
 \ge k-\bigl(2+d(x)-1-|S|\bigr)\ge2,
\]

and symmetrically at (y).  Two sets of order at least two have
distinct representatives, so colour (x,y) distinctly and obtain the
same contradiction. \(\square\)

### Corollary 2.2 (degree-seven overlap prohibition)

In a six-minor-critical graph, no two degree-seven vertices, adjacent
or nonadjacent, have four common neighbours which can be partitioned
into two independent pairs.

For singleton arcs (d\to b), write

\[
 W_d=N(d)\cap N(b).
\]

Then two degree-seven vertices pointing to the same hub cannot have
the same four-set (W_d).  More generally, if two such endpoints share
an external neighbour (z\notin N[b]) and
(W_d\cap W_e) contains a nonedge (uv), then

\[
 \{b,z\}\mathbin{\dot\cup}\{u,v\}
\]

is a forbidden common four-set.

## 3. What criticality adds at a degree-nine hub

Fix a degree-nine vertex (b), and put

\[
                         F=G[N(b)].                \tag{3.1}
\]

Call (d\in N(b)) an **incoming singleton endpoint** when (d) is a
degree-seven zero-optional full-singleton endpoint whose distinguished
neighbour is (b).  For such a (d),

\[
 d_F(d)=4,qquad F[N_F(d)]\cong2K_2.              \tag{3.2}
\]

Let (A_d,C_d) be the two edges of this (2K_2), and put

\[
 E_d=N(b)-\bigl(\{d\}\cup N_F(d)\bigr).          \tag{3.3}
\]

Because (d_G(b)=9), the set (E_d) has exactly four vertices.  The
degree-free rooted-core theorem supplies an (E_d)-rooted (K_4)-model
outside the two simultaneous stars.  Its four disjoint bags use the
four vertices of (E_d) one apiece.

### Lemma 3.1 (dark-root necessity)

If (G) has no (K_7)-minor, then, for every incoming endpoint (d),
some (e\in E_d) is anticomplete to all of (A_d), or anticomplete to
all of (C_d).

#### Proof

Otherwise every one of the four roots in (E_d) has a neighbour in
both (A_d) and (C_d).  Hence every bag of the rooted (K_4)-model
sees both edges.  In the notation of the singleton completion theorem,
use the seven bags

\[
 K_1\mid K_2\mid K_3\mid K_4\mid\{b\}
 \mid A_d\mid(\{d\}\cup C_d).
\]

Both of the last two sets are connected, they are adjacent through
(d), and each sees every rooted bag.  This is a (K_7)-model, a
contradiction. \(\square\)

Inside the nine-vertex graph (F), (3.2) and Lemma 3.1 say precisely
that (d) is a degree-four vertex with local graph (2K_2), and some
triangle containing (d) has a common antivertex.

## 4. Exact degree-nine capacity

### Theorem 4.1 (six-incoming cap; computer-certified)

In the setting of Section 3, a degree-nine hub (b) has at most six
incoming singleton endpoints.

#### Finite verification

Use Boolean variables (e_{ij}), one for each of the 36 possible edges
of a graph (F) on nine labelled vertices.  For a prescribed vertex
(v), the local condition is encoded by

1. (d_F(v)=4); and
2. every (u\in N_F(v)) has exactly one neighbour in
   (N_F(v)-\{u\}).

These two clauses are equivalent to (F[N_F(v)]=2K_2).  The dark-root
condition is the disjunction over triples ((a,c,x)) of

\[
 va,vc,ac\in E(F),qquad vx,ax,cx\notin E(F).    \tag{4.1}
\]

The archived exact check proves the stronger finite statement:

> If seven prescribed vertices of a nine-vertex graph satisfy the local
> (2K_2) condition, then none of those seven vertices has a witness
> (4.1).

Thus seven incoming endpoints contradict Lemma 3.1.  The same encoding
finds a graph with six prescribed vertices satisfying both conditions,
so six is sharp for this interface statement.

The verifier prints

```text
seven local vertices, vertex 0 dark: unsat
six local and dark vertices: sat
```

No graph-minor search, colouring search, or unbounded-order assumption
is hidden in this check; it is a finite Boolean assertion about 36 edge
variables.  For publication it should still be independently rerun and
exported with a proof certificate.

## 5. Why this does not yet close the global discharging route

Mader's inequality gives

\[
 3n_7+2n_8+n_9
 \ge30+\sum_{j\ge11}(j-10)n_j.                  \tag{5.1}
\]

Theorem 4.1 bounds only arcs entering degree-nine hubs.  It gives no
corresponding capacity at degree ten or above, and (5.1) remains
compatible even with the sharp six-incoming cap.  For example, the
formal degree data

\[
 n_7=6,qquad n_8=6,qquad n_9=2
\]

already satisfy (5.1) and have enough degree-nine capacity for all six
arcs.  Thus no redistribution using only (5.1), (d\to b), and the
degree-nine cap can force a contradiction.

The exact next global target is consequently one of the following:

1. a degree-at-least-ten capacity theorem using the *set* of possible
   rooted (K_4) traces, where the portal set has order greater than
   four; or
2. a labelled-minor theorem saying that several distinct four-sets
   (W_d) at one hub force a (K_7)-model before degree counting is
   invoked.

Theorem 2.1 shows that repeated traces are already impossible.  Theorem
4.1 shows that a degree-nine hub cannot support seven distinct locked
traces.  These are the rigorous limits of the present dependency
orientation; a pure Mader discharging argument does not yet escape the
singleton lock.

## 6. The neighbourhood-only capacity route does not scale

The dark-root condition itself is not special to degree nine.  If
(d_G(b)=s\ge9), then

\[
 E_d=N(b)-\bigl(\{d\}\cup N_F(d)\bigr)
\]

has (s-5) vertices.  The rooted-core theorem still gives four
pairwise adjacent bags, each rooted somewhere in (E_d).  If every
vertex of (E_d) met both local (K_2) components, every one of those
four bags would meet both components and the proof of Lemma 3.1 would
again give a (K_7)-model.  Thus every incoming endpoint still gives
the same local dark row in (F=G[N(b)]).

There is, however, no sublinear packing bound for such rows even when
(F) is planar.

### Proposition 6.1 (planar dark-row family)

For every positive integer (m), there is a connected planar graph
(F_m) on (9m) vertices with (6m) distinguished vertices (v)
satisfying

\[
 d_{F_m}(v)=4,qquad F_m[N(v)]\cong2K_2,          \tag{6.1}
\]

and such that a triangle containing (v) has a common antivertex.
In particular (F_m) is (K_6)-minor-free.

#### Proof

Start with the graph (H) on ({0,1,\ldots,8}) having edge set

\[
\begin{split}
E(H)=\{&02,03,05,07,
13,14,15,18,
24,25,26,\\
&34,37,46,58,78\}.                              \tag{6.2}
\end{split}
\]

The six distinguished vertices are (0,1,2,3,4,5).  Their local
matching and one dark witness are displayed in the following table.

\[
\begin{array}{c|c|c}
v& E(H[N(v)])&\text{triangle and antivertex}\\ \hline
0&25+37&037;6\\
1&34+58&158;6\\
2&05+46&246;7\\
3&07+14&037;6\\
4&13+26&246;7\\
5&02+18&158;6
\end{array}                                                    \tag{6.3}
\]

Here, for example, `(037;6)' says that (037) is a triangle and
(6) is anticomplete to it.  Thus (6.1) and the dark-row condition are
checked directly.

For an explicit planarity certificate, the following are the facial
walks of a sphere embedding of (H):

\[
\begin{gathered}
0342,quad073,quad0587,quad025,quad246,\\
26415,quad314,quad3781,quad518.                \tag{6.4}
\end{gathered}
\]

Every edge of (6.2) occurs twice in opposite directions in (6.4), the
induced cyclic orders agree at every vertex, and

\[
 |V(H)|-|E(H)|+|\mathcal F|=9-16+9=2.
\]

Thus (6.4) is a planar cellular embedding.

Take (m) disjoint copies of (H), and, for consecutive copies, add a
bridge between their respective vertices labelled (6).  These bridges
make the graph connected and preserve planarity.  They alter neither
the neighbourhood nor any dark witness of a distinguished vertex.
The resulting graph is (F_m).  Planar graphs are closed under minors
and (K_6) is nonplanar, so (F_m) is (K_6)-minor-free. \(\square\)

The density (6m/(9m)=2/3) is enough to rule out the hoped-for
discharging estimate.  In particular, no theorem using only

* (F=G[N(b)]) is (K_6)-minor-free;
* the local (2K_2) row (3.2); and
* the dark-root consequence of the rooted core

can bound the number of incoming rows by (o(d(b))), let alone by the
roughly ((d(b)-10)/3) capacity needed to absorb three units from every
degree-seven endpoint.

Proposition 6.1 is an interface counterarchitecture, not a hypothetical
Hadwiger counterexample: it does not realize the two external neighbours
which make every distinguished row into a degree-seven singleton
endpoint, nor the one-step colouring transitions.  It proves exactly
that the neighbourhood graph and its rooted-core dark rows are
insufficient.  Any scalable dependency argument must couple different
rows through global contraction-critical transition data or build the
minor directly outside (N[b]).
