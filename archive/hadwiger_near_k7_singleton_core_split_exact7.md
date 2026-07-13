# A singleton `K_4` core: rooted split, exact-seven torso, or a colourable apex pair

## 1. Scope

This note treats the strongest literal normalization of a near-`K_7`
model.  Let `G` be seven-connected and let

\[
                         Q=\{q_1,q_2,q_3,q_4\}
\]

induce `K_4`.  Put

\[
                         S=Q\mathbin{\dot\cup}\{x,y\}.
\]

Assume that `x,y` are nonadjacent, each is adjacent to every vertex of
`Q`, and

\[
                         D=G-S                                      \tag{1.1}
\]

is connected, adjacent to each of `x,y`, and collectively adjacent to
every vertex of `Q`.  Thus

\[
                  \{x\}\mid D\mid\{y\}\mid
                  \{q_1\}\mid\cdots\mid\{q_4\}                    \tag{1.2}
\]

is a spanning `K_7^-` model whose only deficient pair is `xy`.

The conclusion below is not that seven-connectivity alone repairs `xy`.
That is false, even when `D` is three-connected.  The conclusion is an
exact carrier split or a literal exact-seven torso obstruction.  It also
identifies and eliminates the sharp coherent two-apex realization in a
minor-minimal non-six-colourable graph.

## 2. Two elementary rooted completions

### Lemma 2.1 (three roots in a two-connected graph)

If `H` is two-connected and `u,v,w` are three distinct vertices of `H`,
then `H` contains a `K_3` minor rooted at `u,v,w`.

#### Proof

Take a cycle `C` through `u,v`.  If `w` lies on `C`, split the cycle at
the three roots.  Otherwise the Fan Lemma gives two internally disjoint
paths from `w` to two distinct vertices `a,b` of `C`, with no other
vertices on `C`.  Their union with the two `a-b` arcs of `C` is a theta.
If `u,v` lie on one theta path, that path together with the path through
`w` is a cycle through all three roots.  If the roots lie on the three
different theta paths, split the three paths at `a,b`: give `a` to the
bag on the `u`-path, give `b` to the bag on the `v`-path, and give the
interior of the third path to the `w`-bag.  The three resulting connected
bags are pairwise adjacent and contain the named roots.  QED.

### Lemma 2.2 (common-portal multiplicity lock)

Let `G` be seven-connected and `Q` a four-clique.  Put `H=G-Q` and

\[
                         U=\bigcap_{q\in Q}N_H(q).                 \tag{2.1}
\]

If `G` has no `K_7` minor, then

\[
                         |U|\le2.                                  \tag{2.2}
\]

#### Proof

Deleting four vertices from a seven-connected graph leaves a
three-connected, hence two-connected, graph `H`.  If `U` contained three
vertices, Lemma 2.1 would give a rooted `K_3` model in `H`.  Each of its
three bags contains a vertex complete to `Q`; adding the four singleton
vertices of `Q` gives a `K_7` model.

This proves (2.2).  QED.

There is a separate edge form, with the exact extra hypothesis it needs.
If `uv in E(G[U])` and `H-\{u,v\}` contains a connected subgraph `R`
which is collectively adjacent to every vertex of `Q`, the uniform
singleton-core fan completion applied to `Q,R,u,v` gives `K_7`.  Thus in
a target-free near-model an adjacent pair of common portals is possible
only when deleting that pair destroys every connected `Q`-full carrier.
In the shell (1.2), `D` supplies the carrier for the named pair `x,y`;
accordingly the only unresolved shell has `xy` nonadjacent, as assumed.

### Proposition 2.3 (exact rooting hypothesis for a singleton neutral core)

Let a seven-connected graph have a spanning `K_7^vee` model

\[
                 A,B,C,\{q_1\},\ldots,\{q_4\},                 \tag{2.3}
\]

where the only non-required pairs are `AB,AC`.  If the graph has no
`K_7` minor, then, after interchanging `B,C` if necessary, the actual
three-bag quotient is the path

\[
                              A-B-C,                            \tag{2.4}
\]

and `A,C` are anticomplete.

Suppose there are vertices `x in A`, `y in C` which are each complete to
`Q`, and suppose

\[
                         D=G-(Q\cup\{x,y\})                    \tag{2.5}
\]

is connected and has a neighbour at each of the six vertices of
`Q\cup\{x,y\}`.  Then the model is exactly in the setting of Section 1.

#### Proof

The graph `G-Q` is three-connected and in particular connected.  Since
`B,C` are adjacent, `A` must be adjacent to at least one of them.  If it
were adjacent to both, the seven displayed old branch bags would already
form a `K_7` model.  Hence exactly one edge occurs and (2.4) follows.
In particular `xy` is a nonedge.  The hypotheses on (2.5) are precisely
connectedness and the six nonempty portal rows required in Section 1.
QED.

Thus the boundary-faithful lift from a contracted near-clique needs exactly
three things: a common `Q`-portal vertex in each end bag, connectedness
after retaining those two roots, and survival of the six literal portal
rows.  Failure of any of these is a distributed portal-tree obstruction;
when they hold, Theorem 4.1 below localizes the remaining failure to one
exact-seven torso.

## 3. The exact carrier split

For `s in S`, write

\[
                         P_s=N_D(s).                            \tag{3.1}
\]

All six portal rows are nonempty.  A connected subgraph of `D` is an
`xy`-carrier when it meets every `P_{q_i}` and also meets `P_x,P_y`.
A connected subgraph is a `y`-carrier when it meets every `P_{q_i}` and
meets `P_y`.

### Lemma 3.1 (typed carrier split completes the clique)

If `D` contains a vertex-disjoint `xy`-carrier `L` and `y`-carrier `R`,
then `G` contains a `K_7` minor.

#### Proof

Choose a shortest `L-R` path in `D` and absorb its internal vertices into
`L`.  Thus `L,R` may be assumed adjacent.  Extend them along a spanning
tree of `D` to a bipartition

\[
                         D=X\mathbin{\dot\cup}Y                 \tag{3.2}
\]

into adjacent connected sets, with `L subseteq X` and `R subseteq Y`.
Use the seven bags

\[
       \{x\}\cup X,\quad Y,\quad\{y\},\quad
       \{q_1\},\ldots,\{q_4\}.                                \tag{3.3}
\]

The first bag is connected because `X` meets `P_x`.  It sees `y` because
`X` meets `P_y`; `Y` sees `y` by its carrier row; and `X,Y` are adjacent.
The first and third bags see every `q_i` through `x,y`, while `Y` sees
every `q_i` through the four retained rows.  The four singleton bags form
a clique.  Hence (3.3) is a `K_7` model.  QED.

This is weaker than asking both shores to retain all six rows: only the
unabsorbed shore `Y` must be `Q`-full.

## 4. Failure is a literal exact-seven torso obstruction

### Theorem 4.1 (singleton-core split or exact-seven torso)

Under the hypotheses of Section 1, at least one of the following holds.

1. `G` contains a `K_7` minor.
2. One bag `Z` of a Tutte decomposition of the two-connected graph `D`
   meets every `xy`-carrier, or meets every `y`-carrier.  Every component
   `K` of `D-Z` has a named missed boundary vertex `s_K in S` and two
   actual gate vertices `z_K^1,z_K^2 in Z` such that
   \[
        N_G(K)=(S-\{s_K\})\mathbin{\dot\cup}
                 \{z_K^1,z_K^2\}.                              \tag{4.1}
   \]
   In particular every off-torso lobe lies behind a literal exact
   seven-cut.  The common torso is a gate, a cycle, or a three-connected
   torso.

#### Proof

Apply the full state-shore/bi-Helly theorem to `D`, taking the four rows
`P_{q_i}` as neutral rows, taking `A=P_x`, and taking `B=C=P_y`.  Its left
carriers are exactly the `xy`-carriers and its right carriers are exactly
the `y`-carriers.  Disjoint carriers give outcome 1 by Lemma 3.1.

Suppose there are no disjoint carriers.  First apply the same cross-Helly
argument to the block decomposition of `D`, whose adhesions have order at
most one.  A component off the common block misses one named row and has
at most one attachment in that block.  Since all vertices outside `D`
are the six literal vertices of `S`, its neighbourhood has order at most

\[
                         (6-1)+1=6,
\]

and separates it from the missed boundary vertex.  This contradicts
seven-connectivity.  If `D` were not two-connected, its block tree would
have more than one bag, so whichever block bag is supplied by cross-Helly
would have a nonempty component outside it and would give exactly this
contradiction.  Hence `D` is two-connected.  The cases of order at most
two are separately excluded by `d(x)>=7`: the vertex `x` has only its
four neighbours in `Q` and its neighbours in `D`, since `xy` is absent.

Now use a Tutte decomposition of `D`, of adhesion at most two.  The
cross-Helly theorem gives one common bag `Z`.  Every component `K` of
`D-Z` misses a named required row, say `P_{s_K}`, and has at most two
actual neighbours in `Z`.  Therefore

\[
       N_G(K)\subseteq(S-\{s_K\})\cup Z_K,
       \qquad |Z_K|\le2.                                      \tag{4.2}
\]

The right side has order at most seven and separates `K` from `s_K`.
Seven-connectivity forces equality throughout: `|Z_K|=2`, all five other
boundary contacts occur, and (4.1) follows.  The standard Tutte torso
types give the last assertion.  QED.

Thus the unbounded branch-bag problem does not survive as arbitrary
portal placement.  It is confined to one two-connected torso with
operation-sensitive exact-seven lobes.

### Corollary 4.2 (four exact-seven lobes have portal rank four)

Assume `G` has no `K_7` minor and let `K_1,...,K_4` be four distinct
off-torso components in outcome 2 of Theorem 4.1.  Their two-element gate
sets have a system of distinct representatives.  In particular:

* three of the lobes cannot have the same gate pair; and
* the union of the four gate pairs has order at least four.

If the common torso is itself a two-vertex gate, it therefore has at most
two off-torso components.

#### Proof

The literal boundary `S` induces `K_6-xy`, and hence contains the shell
`K_6-\{ab,ac\}` used in the audited exact-seven bouquet theorem.  By
(4.1), each `K_i` is connected, has two actual torso poles, and sees every
literal shell row except its one named missed row.  The two-pole triple
bouquet and three-pole four-bouquet closure theorems therefore say that a
rank-at-most-three family of four such lobes gives a `K_7` model.  This is
excluded, so the transversal rank is four.  The final assertion follows
from the two-pole triple closure already with three lobes.  QED.

## 5. The coherent two-apex row is colourable

### Lemma 5.1 (two universal core rows cannot occur in a counterexample)

Assume in addition that `G` is `K_7`-minor-free.  If two vertices
`q_i,q_j in Q` are complete to `D`, then `G` is six-colourable.

#### Proof

The two vertices are adjacent and are complete to every other vertex of
`G`: they see `Q` because it is a clique, see `x,y` by the shell
hypothesis, and see `D` by assumption.  Put

\[
                         F=G-\{q_i,q_j\}.
\]

The graph `F` has no `K_5` minor, since such a model together with the two
universal singleton vertices would be a `K_7` model in `G`.  The known
case `HC_5` therefore four-colours `F`.  Give `q_i,q_j` two new colours.
This is a six-colouring of `G`.  QED.

This is the exact form of the coherent two-apex outcome needed here.  It
does not require proving that the remainder is planar: `K_5`-minor-free
and `HC_5` already provide the four-colouring.

Consequently, in a hypothetical minor-minimal `HC_7` counterexample, the
residue in Theorem 4.1 has at most one core row which is complete across
the common torso and all exact-seven lobes.

## 6. Sharp coherent counterarchitecture

Let `I` be the icosahedron with vertices

\[
                  t,b,u_0,\ldots,u_4,w_0,\ldots,w_4
\]

and edges

\[
 tu_i,\quad bw_i,\quad u_iu_{i+1},\quad w_iw_{i+1},
 \quad u_iw_i,\quad u_iw_{i-1}
\]

with subscripts modulo five.  Let `p,q` be adjacent universal vertices
and put `G=K_2\vee I`.  Set

\[
\begin{aligned}
 Q&=\{p,q,t,u_0\},\\
 x&=u_1,\qquad y=u_4,\\
 D&=\{b,u_2,u_3,w_0,w_1,w_2,w_3,w_4\}.
\end{aligned}                                                   \tag{6.1}
\]

Then `Q` is a `K_4`, `x,y` are nonadjacent and complete to `Q`, and `D`
is connected, collectively `Q`-full, and adjacent to both `x,y`.  In
fact `G[D]` is three-connected.  The graph `G` is seven-connected and
has no `K_7` minor: the icosahedron is five-connected and planar, and a
`K_7` model in its join with `K_2` would leave a `K_5` model in `I` after
removing the at most two bags containing `p,q`.

Here the two rows `p,q` are complete across `D`; deleting them leaves the
planar icosahedron.  Thus the example realizes the coherent alternative
of Lemma 5.1 and shows simultaneously that none of the following alone
forces the split:

* seven-connectivity;
* a spanning shell with six singleton bags;
* a literal singleton `K_4` core;
* a three-connected complex bag; or
* three or more portals from each of `x,y` into that bag.

The accompanying verifier checks every displayed incidence, the
connectivities, and the explicit model.

## 7. Exact remaining principle

For the literal singleton-core branch, the unresolved statement is now
strictly narrower than a general near-clique splitter:

> In the exact-seven torso outcome of Theorem 4.1, with at most one
> globally complete core row, proper-minor state exchange either produces
> disjoint typed carriers or makes two core rows globally complete.

The first conclusion is `K_7` by Lemma 3.1.  The second is six-colourable
by Lemma 5.1.  Static connectivity cannot prove this final exchange,
because the icosahedral construction satisfies every preceding static
hypothesis.
