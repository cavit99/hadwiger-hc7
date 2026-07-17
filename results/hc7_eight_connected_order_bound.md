# An order bound for eight-connected `K_7`-minor-free graphs

**Status:** written proof; separate internal audit GREEN.  The proof is
entirely mathematical and does not use the exploratory order-16 solver.

## 1. Statement

Write `t_G(xy)=|N_G(x)\cap N_G(y)|` for the number of triangles containing
an edge `xy`.

For the proposed counterexample search this is the right connectivity
level: a seven-connected noncomplete graph with no actual separation of
order seven is eight-connected.  A `K_7`-minor-free graph containing the
displayed models is noncomplete, so no exceptional convention is involved.

### Theorem 1.1 (order-16 exclusion)

Every eight-connected `K_7`-minor-free graph has at least seventeen
vertices.

Consequently there is no counterexample of order at most sixteen to the
connectivity-only adjacent-pair principle considered here.  In particular,
the proposed stronger buffer-colour obstruction cannot first occur at
order sixteen.

The new ingredient is the following elementary complement lemma.

### Lemma 1.2 (the `(16,7,4)` complement obstruction)

There is no seven-regular graph `H` on sixteen vertices in which every
nonadjacent pair has at least four common neighbours.

This lemma is independent of graph-minor theory.

## 2. Extremal input

We use two established results.

1. Mader's theorem gives
   `|E(H)|<=5|V(H)|-15` for every `K_7`-minor-free graph `H`.
2. Jorgensen's equality classification says that the graphs attaining
   equality are the five-clique sums of edge-maximal two-apex graphs,
   together with `K_{2,2,2,3}`.  See L. K. Jorgensen, *Extremal graphs
   for contractions to K7*, Ars Combin. 25C (1988), 133--148.
The equality classification has the following immediate connectivity
consequence.

### Lemma 2.1

Every eight-connected `K_7`-minor-free graph `H` satisfies

\[
                         |E(H)|\leq 5|V(H)|-16.          \tag{2.1}
\]

#### Proof

A nontrivial five-clique sum has a vertex cut of order five.  The
exceptional graph `K_{2,2,2,3}` has connectivity six.  Finally, an
edge-maximal two-apex graph has connectivity at most seven: after deleting
an apex set of order at most two, either at most six vertices remain, in
which case the whole graph has order at most eight, or the planar remainder
has a vertex of degree at most five, whose degree in the original graph is
at most seven.  Hence no graph in Jorgensen's equality class is
eight-connected.  Mader's bound is integral, giving (2.1).  \(\square\)

## 3. A complement lemma

We prove Lemma 1.2.  Suppose, to the contrary, that `H` is such a graph.
Fix `v\in V(H)`, put

\[
 A=N_H(v),\qquad B=V(H)-N_H[v],
\]

and let

\[
 L=H[A],\qquad F=H[B],\qquad a=|E(L)|.
\]

Thus `|A|=7` and `|B|=8`.  For every `b\in B`, the nonadjacent pair
`v,b` has at least four common neighbours.  All of them lie in `A`, so

\[
 |N_H(b)\cap A|\geq4,
 \qquad d_F(b)=7-|N_H(b)\cap A|\leq3.                  \tag{3.1}
\]

Counting the edges between `A` and `B` first from `A` gives

\[
 e_H(A,B)=\sum_{x\in A}(6-d_L(x))=42-2a.
\]

Counting the degrees of the vertices of `B` now gives

\[
 2|E(F)|=56-e_H(A,B)=14+2a,
 \qquad |E(F)|=7+a.                                   \tag{3.2}
\]

By (3.1), `|E(F)|\leq12`, and hence `a\leq5`.

The graph `L` has no isolated vertex.  Indeed, if `x\in A` were isolated
in `L`, then `x` would have six neighbours in `B` and hence two
nonneighbours there.  For either such nonneighbour `b`, a common neighbour
of `x` and `b` cannot be `v`, cannot lie in `A`, and has at most
`d_F(b)\leq3` choices in `B`.  This contradicts the four-common-neighbour
hypothesis.  Therefore `a\geq4`.

Suppose `a=4`.  Since all seven degrees in `L` are positive and sum to
eight, exactly one vertex of `L` has degree two and the other six have
degree one.  By (3.2), the degrees in `F` sum to twenty-two, while every
one of them is at most three.  Hence either one vertex of `F` has degree
one and the other seven have degree three, or two vertices have degree two
and the other six have degree three.

Let `b` be a vertex of `F` of degree one or two.  Since

\[
 |A-N_H(b)|=d_F(b),                                    \tag{3.3}
\]

there are exactly `d_F(b)` vertices `x\in A` nonadjacent to `b`.  For
each such `x`, the common neighbours of `x,b` lie either among the at most
`d_L(x)` neighbours of `x` in `A`, or among the at most `d_F(b)`
neighbours of `b` in `B`.  Thus

\[
 4\leq |N_H(x)\cap N_H(b)|\leq d_L(x)+d_F(b).          \tag{3.4}
\]

If `d_F(b)=1`, (3.4) asks for a vertex of degree at least three in `L`,
which does not exist.  Otherwise there are two degree-two vertices of
`F`; for either one, its two nonneighbours in `A` would both have to be
the unique degree-two vertex of `L`.  This is also impossible.  Therefore
`a\ne4`, and so `a=5`.

The choice of `v` was arbitrary.  Hence every vertex of `H` belongs to
exactly five triangles, because the triangles through `v` are counted by
the five edges of `H[N_H(v)]`.  Summing over all vertices would count the
triangles three times and give

\[
                3\,\#K_3(H)=16\cdot5=80,
\]

an impossibility.  This proves Lemma 1.2.  \(\square\)

## 4. Proof of Theorem 1.1

Suppose that `G` is eight-connected and `K_7`-minor-free.  Put
`n=|V(G)|` and `m=|E(G)|`.  Eight-connectivity gives minimum degree at
least eight, hence

\[
                              4n\leq m.
\]

Lemma 2.1 gives `m\leq5n-16`, so `n\geq16`.  Assume for a contradiction
that `n=16`.  Equality then holds in the degree lower bound: `m=64` and
every vertex has degree eight.

Fix an edge `xy` and write `t=t_G(xy)`.  Contracting `xy` deletes the edge
itself and merges the `t` pairs of parallel edges, so

\[
                         |E(G/xy)|=63-t.                \tag{4.1}
\]

Mader's order-fifteen bound is sixty.  Since `G/xy` is still
`K_7`-minor-free, equation (4.1) gives `t\geq3`.

Equality `t=3` is impossible.  In that case `G/xy` attains Jorgensen's
bound.  Contracting one edge of an eight-connected graph leaves a
seven-connected graph: a separator of order at most six in the contraction
lifts to a separator of order at most seven in `G`.  Hence `G/xy` cannot be
a nontrivial five-clique sum, and its order excludes `K_{2,2,2,3}`.  It is
therefore an edge-maximal two-apex graph.

At order fifteen and size sixty, such a graph is `K_2\vee T`, where `T`
is a maximal planar graph on thirteen vertices: the elementary two-apex
edge count

\[
 (3(15-2)-6)+2(15-2)+1=60
\]

has equality only when the two apex vertices are adjacent and universal
and the planar remainder is triangulated.  The contracted vertex has
degree

\[
                         8+8-2-3=11,
\]

so it is not one of the two universal vertices of degree fourteen.  Each
universal vertex lifts to a vertex of degree at least fourteen in `G`,
contrary to eight-regularity.  Thus every edge has `t\geq4`.

Let `H=\overline G`.  It is seven-regular.  If `x,y` are nonadjacent in
`H`, then they are adjacent in `G`; since `H` has degree seven on sixteen
vertices,

\[
\begin{aligned}
 |N_G(x)\cap N_G(y)|
 &=14-|N_H(x)\cup N_H(y)|\\
 &=|N_H(x)\cap N_H(y)|.
\end{aligned}
\]

The left side is at least four.  Thus `H` satisfies the hypotheses of
Lemma 1.2, a contradiction.  Therefore `n\geq17`.  \(\square\)

## 5. Consequences for the active search

At the previously suspected minimum order, two unlabelled minor
consequences would have been automatic.  Deleting an adjacent pair from an
eight-regular graph on sixteen vertices leaves 49 edges on fourteen
vertices, which exceeds the exact `K_6`-minor-free bound
`4n-10=46`.  Deleting any pair leaves at least 48 edges, which exceeds the
exact `K_5`-minor-free bound `3n-6=36`.  Hence the first deletion contains
a `K_6` minor and the second contains a `K_5` minor.  These are the
`p=6` and `p=5` cases of the same Mader theorem cited below.  No colouring,
rooting, or label-preserving conclusion follows from these edge counts.
Lemma 1.2 shows that the required host graph itself cannot exist.

Thus a connectivity-only counterexample to the adjacent-pair principle,
and a fortiori a counterexample satisfying the contraction-critical
colouring hypotheses, must have at least seventeen vertices.  This note
does not exclude such graphs of larger order and does not by itself prove
the adjacent-pair principle or `HC_7`.

## 6. Sources and trust boundary

The proof uses the following external results, and no computation.

* W. Mader, *Homomorphiesätze für Graphen*, Math. Ann. 178 (1968),
  154--168, DOI `10.1007/BF01350657`: for `p<=7`, the exact extremal
  bound used here is
  `(p-2)n-binom(p-1,2)` edges for a `K_p`-minor-free graph.  In
  particular the `p=5,6,7` bounds are `3n-6`, `4n-10`, and `5n-15`.
* L. K. Jorgensen, *Extremal graphs for contractions to K7*, Ars Combin.
  25C (1988), 133--148: the equality classification quoted in Section 2.

The complement lemma, the connectivity consequence of the equality
classification, and the order-sixteen exclusion are deductions made in
this note.  Their proof has received a separate internal audit; this is not
external peer review or a claim of literature priority.  The experimental
solver script is not part of the proof.  No assertion is made about the
existence or structure of order-seventeen examples.
