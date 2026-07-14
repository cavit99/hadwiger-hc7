# Barrier: `K_7`-minor-freeness does not force the width-two thin split

## Status

**Exact static counterexample.**  The graph below has the literal paired
frontier boundary, an `S`-full cutvertex-free thin packet `L`, and two
adjacent `S`-full packet vertices `p,q`.  It is `K_7`-minor-free, but `L`
has no two disjoint carriers for the two bipartition duties.

It also satisfies the full local degree condition on the thin packet:

\[
                 d_{G[L]}(x)+|N_S(x)|=7\qquad(x\in L).             \tag{0.1}
\]

More strongly, every nonempty thin subset has the expansion forced by an
ambient seven-cut:

\[
                    |N_G(X)|\ge7\qquad(\varnothing\ne X\subseteq L). \tag{0.2}
\]

The neighbourhood orders are seven for singletons and for `L`, and eight
for two-vertex subsets.

The graph is five-connected, not seven-connected.  It therefore refutes
the proposed static implication using packet data, `K_7`-minor-freeness,
and even all thin-side cut expansion; it does not refute a theorem which
spends global seven-connectivity across the other shore or the proper-minor
transition witnesses of contraction-criticality.

It also does **not** satisfy the full Dirac neighbourhood inequality:
for every `l_i`, `d(l_i)=7` but
`alpha(G[N(l_i)])=3`.  Thus adding the genuine contraction-critical
inequality `alpha(N(x))<=d(x)-5`, rather than degree alone, remains a live
static strengthening.

## 1. Literal graph

Use the paired boundary

\[
 S=\{c,a_1,t_1,a_2,t_2,a_3,t_3\},\qquad
 A=\{c,t_1,t_2,t_3\},\quad B=\{a_1,a_2,a_3\}.
\]

Let `H=G[S]` have edges

\[
 ca_1,\ ca_2,\ ca_3,\ a_1t_2,\ t_1a_3,\ a_2t_3.       \tag{1.1}
\]

Thus `H` is the paired-state subdivided claw and `A,B` are its two
bipartition classes.

Let `L={l_0,l_1,l_2}` induce a triangle and add the contacts

\[
\begin{aligned}
 N_S(l_0)&=\{c,a_1,t_1,t_2,a_3\},\\
 N_S(l_1)&=\{c,a_1,a_2,t_2,t_3\},\\
 N_S(l_2)&=\{c,t_1,a_2,a_3,t_3\}.
\end{aligned}                                                   \tag{1.2}
\]

Finally add adjacent vertices `p,q`, each complete to `S`, and no edge
from `{p,q}` to `L`.  The open shores are therefore literally
anticomplete.

## 2. Packet and duty assertions

The triangle `L` is connected and has no cutvertex.  It is `S`-full, and
every two-vertex subset of `L` is already full.  Since any two such subsets
intersect, while no singleton is full, the thin packet number is exactly
one.

No singleton funds `A`: respectively `l_0,l_1,l_2` miss
`t_3,t_1,t_2`.  No singleton funds `B`: respectively they miss
`a_2,a_3,a_1`.  Every duty carrier therefore has order at least two.
Two subsets of a three-set having order at least two must intersect.
Hence no `A`-carrier is disjoint from a `B`-carrier.  In particular the
adjacent connected split required by Lemma 5.2 of
`../results/hc7_exact7_connected_rich_width2_frontier.md` does not exist.

The singleton packets `{p}` and `{q}` are disjoint, adjacent, and
`S`-full.

## 3. Exact `K_7`-minor exclusion

Put `F=G-{p,q}`.  It is planar.  One planar rotation system has facial
walks

```text
c l1 a1
c a2 l1
c l2 a2
c a3 l2
c l0 a3
c a1 l0
a1 t2 l0
a1 l1 t2
a2 t3 l1
a2 l2 t3
a3 t1 l2
a3 l0 t1
t2 l1 l0
t1 l0 l2
t3 l2 l1
l0 l1 l2
```

In fact `F` is a maximal planar graph: it has ten vertices and twenty-four
edges, and all sixteen displayed faces are triangles.  The graph `G` is a
subgraph of the join `K_2 vee F`: the only edges missing
from that join are the edges from `p,q` to `L`.  If `K_2 vee F` had a
`K_7` model, at most two branch sets could contain the two `K_2` vertices.
Deleting those branch sets would leave at least five pairwise adjacent
connected branch sets wholly in `F`, a `K_5` minor.  This contradicts
planarity of `F`.  Therefore `G` is `K_7`-minor-free.

The verifier also exhausts all connected spanning seven-block partitions
of `G` and finds no `K_7` model.

## 4. The exact missing contraction-critical transition

This example identifies the minimum extra datum that a positive argument
must spend.  For a closed shore `X` with literal boundary `S`, let
`Sigma(X)` be the set of exact boundary equality partitions induced by
proper six-colourings of `X`.

The barrier itself has the common low state: colour `A` with colour zero,
`B` with colour one, give `l_0,l_1,l_2` colours two, three, four, and give
`p,q` colours two, three.  This is a proper five-colouring of the whole
graph.  Thus static attainment of `A|B` is deliberately not the missing
counterexample property.

In an actual minimal `HC_7` counterexample separated into closed shores
`Lbar,Rbar`, one has

\[
                  \Sigma(\overline L)\cap\Sigma(\overline R)=\varnothing.
                                                                  \tag{4.1}
\]

For every internal thin-shore edge `e=xy`, proper-minor criticality gives

\[
\begin{aligned}
 \Sigma(\overline L-e)\cap\Sigma(\overline R)&\ne\varnothing,\\
 \Sigma(\overline L/e)\cap\Sigma(\overline R)&\ne\varnothing.    \tag{4.2}
\end{aligned}
\]

Every state in either intersection is genuinely absent from
`Sigma(Lbar)`, by (4.1).  In the deletion witness, every six-colouring has
`x` and `y` equal; otherwise it colours the undeleted graph.  Each of
`x,y` also sees all other five colours, since recolouring an endpoint to a
missing colour would again colour the undeleted graph.

Thus the remaining width-two theorem cannot be a statement about the
static portal hypergraph alone.  It must use either exact
seven-connectivity to rule out this planar lock, or the **new compatible
state after every internal deletion/contraction** in (4.2).  Merely knowing
that the low state `A|B|U` is attained on one shore does not encode this
minimal incompatibility.

## 5. Reproduction

Run

```text
active/runtime/venv/bin/python \
  barriers/hc7_width2_k7free_static_split_barrier_verify.py
```

The verifier checks all literal incidences, packet and carrier statements,
the exact local degree condition (0.1), the maximal-planar certificate,
the full thin expansion (0.2), connectivity, the exact failure of the
stronger Dirac inequality, and the exhaustive `K_7`-minor search.
