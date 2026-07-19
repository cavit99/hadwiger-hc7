# Unbounded list-degree surplus in a two-edge response core

**Status:** written proof; audit pending.  This note records the strongest
purely list-critical edge-minimal conclusion available without using
`K_7`-minor exclusion, and an infinite family showing that the total
list-degree surplus need not be bounded or concentrated on the two marked
vertices.  The host graphs in the family are seven-connected and
seven-chromatic, but they contain a `K_7` minor and are not asserted to be
minor-minimal.  Thus the construction is a barrier to a list-critical-only
argument, not a counterexample to `HC_7`.

## 1. What edge-minimality does give

Let `H` be vertex-minimal non-`L`-colourable, where every list is nonempty.
Choose a spanning subgraph `F` of `H` inclusion-minimal subject to being
non-`L`-colourable.

### Lemma 1.1 (edge-deletion equality witness)

The graph `F` is connected and vertex-minimal non-`L`-colourable, and

\[
                         d_F(v)\ge |L(v)|              \tag{1.1}
\]

for every vertex `v`.  Moreover, for every edge `uv` and every
`L`-colouring `c` of `F-uv`:

1. `c(u)=c(v)`;
2. every colour in `L(u)-{c(u)}` occurs on a neighbour of `u` other than
   `v`, and symmetrically at `v`;
3. if `c(u) notin L(u)`, then `d_F(u)>=|L(u)|+1`;
4. if `d_F(u)=|L(u)|`, then `c(u) in L(u)` and the neighbours of `u` use
   the colours of `L(u)` exactly once.

#### Proof

If `F` were disconnected, one component would already be non-
`L`-colourable, contradicting the minimal choice of its spanning edge set.
Every proper induced subgraph of `F` is a subgraph of a proper induced
subgraph of `H`, and hence is `L`-colourable.  Colouring `F-v` and then
extending greedily proves (1.1).

Minimality of the edge set makes `F-uv` `L`-colourable.  In any such
colouring the endpoints have the same colour, since otherwise the same
assignment colours `F`.  Put `gamma=c(u)=c(v)`.  If a colour
`alpha in L(u)-{gamma}` were absent from `N_F(u)-{v}`, recolouring `u` with
`alpha` would repair the edge `uv` and give an `L`-colouring of `F`.
This proves assertions 1 and 2.

If `gamma notin L(u)`, the vertex `v` uses the extra colour `gamma`, while
`|L(u)|` distinct neighbours other than `v` are needed to display all
colours in `L(u)`.  This gives assertion 3.  Finally, if equality holds in
(1.1), assertion 3 forces `gamma in L(u)`; assertion 2 and the neighbour
`v` then account for all `|L(u)|` neighbours, with one neighbour in each
list colour.  This is assertion 4.  \(\square\)

The lemma supplies operation-specific equality witnesses, but it does not
bound the surplus `d_F(v)-|L(v)|`.  The following family shows that this is
an essential limitation.

## 2. An edge-minimal infinite family

For `n>=2`, let

\[
                         R_n=K_2\vee C_{2n+1}.          \tag{2.1}
\]

Write `a,b` for the two vertices of the `K_2`, and write the cycle in order
as

\[
                         c_0c_1\cdots c_{2n}c_0.
\]

Put `p=c_0`, `q_0=c_2`, and give every vertex the same list

\[
                         A(v)=\{1,2,3,4\}.              \tag{2.2}
\]

### Theorem 2.1 (unbounded surplus away from the marked vertices)

The graph `R_n` has all of the following properties.

1. It is vertex-minimal and edge-minimal non-`A`-colourable.
2. It has a proper six-colouring `psi` in which precisely the two
   nonadjacent marked vertices `p,q_0` lie outside their lists.
3. With

   \[
                          \varepsilon(v)=d_{R_n}(v)-|A(v)|,
   \]

   one has

   \[
     \varepsilon(p)=\varepsilon(q_0)=0,
     \qquad
     \varepsilon(a)=\varepsilon(b)=2n-2.               \tag{2.3}
   \]

In particular, the total surplus is unbounded although both marked
vertices are tight, and all positive surplus lies on unmarked vertices.

#### Proof

The chromatic number of a join is the sum of the chromatic numbers, so

\[
                         \chi(R_n)=2+3=5.
\]

Deleting `a` or `b` leaves `K_1\vee C_{2n+1}`, which is four-colourable.
Deleting a cycle vertex leaves `K_2` joined to a path, which is also
four-colourable.  Hence every proper induced subgraph is `A`-colourable.

Every edge deletion is also four-colourable.  Deleting `ab` lets `a,b`
share one colour while the odd cycle uses three more.  Deleting a cycle
edge leaves a path, so the two join vertices and the path use two colours
each.  Finally, if the deleted edge is `ac_i` (the case at `b` is
symmetric), give `a,c_i` one colour, give `b` a second colour, and
two-colour the path `C_{2n+1}-c_i` with the remaining two colours.  Thus
`R_n` is edge-minimal as well as vertex-minimal non-`A`-colourable.

To construct `psi`, colour `a,b` with colours 1 and 2, respectively.
The graph `C_{2n+1}-{p,q_0}` is a disjoint union of paths, so colour it with
colours 3 and 4.  Give `p` colour 5 and `q_0` colour 6.  The two marked
vertices are nonadjacent, so this is proper, and they are the only vertices
coloured outside (2.2).

Every cycle vertex has degree four in `R_n`, while `a` and `b` have degree
`2n+2`.  Equation (2.3) follows.  \(\square\)

## 3. A seven-connected direct-entry realization

The same list assignment occurs literally as the boundary-complement lists
of a two-edge response in a seven-connected, seven-chromatic graph.

Let `S=X dotcup Y`, where `|X|=3`, `|Y|=4`, and `G[S]=K_{3,4}` with
bipartition `(X,Y)`.  Choose `x_0 in X`, `y_0 in Y`, and add one vertex
`ell` adjacent to every vertex of `S`.  Take `R_n` disjoint from these
vertices and add no edge from `ell` to `R_n`.  Add the following
`S-R_n` edges:

* every vertex of `R_n-{p,q_0}` is adjacent to every vertex of `S`;
* `p` is adjacent precisely to `Y union {x_0}` in `S`;
* `q_0` is adjacent precisely to `X union {y_0}` in `S`.

Denote the resulting graph by `G_n`, and put

\[
                         e=x_0p,\qquad f=y_0q_0.         \tag{3.1}
\]

### Proposition 3.1 (scope-strengthened barrier)

For every `n>=2`:

1. `G_n` is seven-connected and seven-chromatic;
2. the colouring in Theorem 2.1 extends to a proper six-colouring of
   `G_n-{e,f}` by colouring `X` with 5, `Y` with 6, and `ell` with 1;
3. the boundary-complement lists induced on `R_n` by that colouring are
   exactly (2.2);
4. `G_n` contains a `K_7` minor.

Thus seven-connectivity, seven-chromaticity, edge-minimality of the list
core, and the exact two-edge response do not control total list-degree
surplus.  Any theorem doing so in the `HC_7` programme must use further
host information, in particular `K_7`-minor exclusion and/or full
minor-critical response data.

#### Proof

First consider connectivity.  Let `W` contain at most six vertices.  Some
vertex of the seven-set `S` remains.  Every vertex of
`R_n-{p,q_0}` which remains is adjacent to every remaining vertex of `S`.
The vertex `p` has five boundary neighbours and four neighbours in
`R_n-{p,q_0}`; the corresponding numbers for `q_0` are four and four.
Consequently neither marked vertex can be separated from all remaining
boundary and ordinary core vertices by deleting at most six vertices.
The vertex `ell`, if present, is adjacent to all remaining boundary
vertices.

Unless `n=2` and all five ordinary core vertices have been deleted, at
least one ordinary core vertex remains and the preceding adjacencies make
`G_n-W` connected.  In the exceptional case only one further vertex can
have been deleted.  Then at least six boundary vertices remain,
`K_{3,4}-W` is connected, and each surviving marked vertex still has a
boundary neighbour.  Thus `G_n-W` is connected in every case.  Since the
seven-set `S` separates `ell` from `R_n`, the connectivity is exactly
seven.

A seven-colouring is obtained by using five colours on `R_n`, two new
colours on `S`, and reusing a core colour on `ell`.  Conversely, suppose
that `G_n` had a six-colouring.  Every vertex of

\[
                         R_n'=R_n-\{p,q_0\}
\]

is adjacent to every vertex of `S`.  The graph `R_n'` is `K_2` joined to a
forest containing an edge, so `chi(R_n')=4`, while `chi(G_n[S])=2`.
The two complete-to-each-other sets `R_n'` and `S` therefore use four and
two disjoint colour sets.  A two-colouring of the connected bipartite graph
`K_{3,4}` makes `X` and `Y` its two colour classes.  Each of `p,q_0` has a
neighbour in both `X` and `Y`, so all of `R_n` would have to use the four
colours assigned to `R_n'`.  This contradicts `chi(R_n)=5`.  Hence
`chi(G_n)=7`.

The displayed extension of `psi` is proper except on the two edges in
(3.1).  Every vertex of `R_n` has neighbours in both boundary colour
classes 5 and 6, and in no other boundary colour.  Its list is therefore
`[6]-{5,6}={1,2,3,4}`, as claimed.

Finally, partition the cycle into the three connected branch sets

\[
 \{c_0,c_1\},\qquad \{c_2,c_3\},\qquad
 \{c_4,c_5,\ldots,c_{2n}\}.
\]

Together with the singletons `{a},{b}` these form a `K_5`-minor model in
`R_n`.  Every cycle branch set contains an ordinary vertex different from
`p,q_0`, and is therefore adjacent to every vertex of `S`.  One vertex of
`X` and one vertex of `Y` give two adjacent singleton branch sets, both
adjacent to all five old branch sets.  These seven sets form a `K_7`-minor
model in `G_n`.  \(\square\)

## 4. Consequence for the active proof search

The family rules out any deduction of the following forms from the
shore-filling list-core hypotheses alone:

* a bound on `sum_v epsilon(v)` depending only on the two marked vertices;
* concentration of all positive surplus on the marked vertices;
* elimination of positive surplus by taking an edge-minimal
  non-list-colourable spanning subgraph; or
* a conclusion based only on seven-connectivity and seven-chromaticity.

Lemma 1.1 shows what survives: every edge of an edge-minimal refinement has
an operation-specific equality colouring with saturated endpoint lists.
To turn that witness into progress, the `HC_7` argument must couple it to
literal first hits in the five named branch sets, or use `K_7`-minor
exclusion to forbid the high-surplus join geometry exhibited above.
