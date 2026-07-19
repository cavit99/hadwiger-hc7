# Three disjoint boundary supports are not forced without minor exclusion

**Status:** computer-assisted finite counterexample to an intermediate
claim; separate internal audit GREEN in
[`hc7_order8_three_support_packing_barrier_audit.md`](hc7_order8_three_support_packing_barrier_audit.md).
The deterministic verifier is
[`hc7_order8_three_support_packing_barrier_verify.py`](hc7_order8_three_support_packing_barrier_verify.py).
This graph is not a counterexample to `HC_7`: it contains a `K_7` minor
and is not contraction-critical.

## 1. Refuted statement

The following implication is false, even with connectivity one higher than
the `HC_7` kernel.

> Let `S={d,e} dotcup X dotcup Y`, where `|X|=|Y|=3`, and let
> `(L,S,R)` be an order-eight separation in an eight-connected,
> seven-chromatic graph.  Assume that both open shores are connected and
> adjacent to every vertex of `S`.  Suppose the closed `L`-shore realizes
> the boundary partition
> `X | Y | {d,e}` but not `X | Y | {d} | {e}`, while the closed `R`-shore
> realizes the latter partition but not the former.  Suppose also that `R`
> contains two disjoint connected subgraphs, each adjacent to every vertex
> of `S`.  Then `R` contains three pairwise disjoint connected subgraphs:
> one adjacent to both `d,e`, one supporting every vertex of `X`, and one
> supporting every vertex of `Y`.

The example also has no separation of order seven.  Thus adding the usual
alternative “or an order-seven separation” does not repair the claim.

## 2. Construction

Put

\[
 S=\{d,e,x_1,x_2,x_3,y_1,y_2,y_3\},
 \qquad X=\{x_1,x_2,x_3\},\quad Y=\{y_1,y_2,y_3\},
\]

and let `G[S]` be the complete tripartite graph with parts
`{d,e},X,Y`.

The left open shore is a triangle `L={l_0,l_1,l_2}`, complete to `S`.
The right open shore has vertices `R={0,1,2,3,4,5}` and edges

\[
 02,03,05,12,14,15,23,25,34,35,45.                 \tag{2.1}
\]

The boundary-neighbour sets in `R` are

\[
\begin{array}{c|c}
s&N_R(s)\\ \hline
d&\{0,4,5\}\\
e&\{1,2,3\}\\
x_1&\{1,3,5\}\\
x_2&\{0,2,3,4\}\\
x_3&\{0,1,2,3,4,5\}\\
y_1&\{1,4\}\\
y_2&\{0,1,2,3,4,5\}\\
y_3&\{0,3\}.
\end{array}                                           \tag{2.2}
\]

There are no `L`--`R` edges.  The sets

\[
                       Q_0=\{0,1,2\},\qquad Q_1=\{3,4,5\}
\]

are disjoint and connected, and (2.2) shows that each is adjacent to every
literal vertex of `S`.

## 3. Exact opposite colouring responses

On the left shore, `X | Y | {d,e}` uses three colours.  The full triangle
`L` uses the other three.  Hence this partition extends with six colours.
The split partition uses four boundary colours, leaving only two colours
for `L`, so it does not extend.

On the right shore, every vertex of `R` sees at least one vertex in each of
`{d,e},X,Y`.  Under the merged partition, all vertices of `R` are therefore
restricted to the same three remaining colours.  But

\[
                          G[\{0,2,3,5\}]\cong K_4,
\]

so the merged partition does not extend.  The split partition does extend:
give `X,Y,d,e` colours `0,1,2,3`, respectively, and colour

\[
 (0,1,2,3,4,5)=(5,4,2,4,5,3).                       \tag{3.1}
\]

The verifier checks all boundary-constrained six-colourings independently.

Since `L` is a full triangle, any six-colouring of the whole graph would
leave exactly three colours for `S`.  The complete tripartite graph `G[S]`
then forces its three partite sets to be the three colour classes.  This is
the merged partition, which cannot extend through `R`.  Thus `G` is not
six-colourable.  A seven-colouring is supplied by (3.1), with the three
vertices of `L` using the three colours outside the four boundary colours.
Hence `chi(G)=7`.

## 4. No three-support packing

For a nonempty connected set `A subseteq R`, call it a root support when it
has neighbours at both `d,e`, an `X`-support when every `x_i` has a
neighbour in `A`, and a `Y`-support analogously.

The inclusion-minimal supports are as follows (a string such as `02`
denotes the set `{0,2}`).

\[
\begin{array}{c|l}
\text{role}&\text{inclusion-minimal connected supports}\\ \hline
\{d,e\}&02,03,14,15,25,34,35\\
X&3,05,12,14,25,45\\
Y&34,012,015,045,123,135.
\end{array}                                             \tag{4.1}
\]

Among the minimal `X`- and `Y`-supports, the only disjoint pairs are

\[
\begin{array}{c|c|c}
X\text{-support}&Y\text{-support}&\text{unused vertices}\\ \hline
3&012&45\\
3&015&24\\
3&045&12\\
05&34&12\\
05&123&4\\
12&34&05\\
12&045&3\\
25&34&01\\
45&012&3\\
45&123&0.
\end{array}                                             \tag{4.2}
\]

No unused set in the last column contains a root support from (4.1).
Therefore the required three pairwise disjoint connected subgraphs do not
exist.  The verifier reconstructs all connected subsets rather than relying
on the displayed minimal lists.

## 5. Connectivity and the target minor

For every nonempty connected `A subseteq R`, exhaustive finite checking
gives

\[
              |N_R(A)|+|N_S(A)|\ge 8.                 \tag{5.1}
\]

Together with the full triangle on the other shore and the complete
tripartite boundary, (5.1) yields `kappa(G)=8`; the verifier also checks
every deletion set of order at most seven directly.  Deleting `S`
disconnects the two shores, so the connectivity is exactly eight.

The graph contains a `K_7` minor already in `G[S union R]`.  Its branch
sets are

\[
\begin{aligned}
 &\{d,x_1\},\quad \{e,2\},\quad \{x_2,y_2\},
 \quad \{x_3\},\\
 &\{0,3,4,y_1,y_3\},\quad \{1\},\quad \{5\}.         \tag{5.2}
\end{aligned}
\]

They are disjoint and connected, and the verifier checks all twenty-one
pairwise adjacencies.  In particular, the opposite full triangle is not
responsible for the minor.

The model (5.2) has a reusable description.  The edge `15` forms two
singleton branch sets, and each endpoint is adjacent to every branch set
of the five-set model formed by the first five sets in (5.2).  Thus the
failure of the three-support packing can coexist with a **saturated edge**:
an edge whose ends both meet every branch set of a `K_5` model.  Such an
edge always completes that model to a `K_7` model.

## 6. Exact scope

This example proves that none of the following, even together, forces the
three-support packing or an order-seven separation:

* eight-connectivity and seven-chromaticity;
* an actual order-eight separation with connected full shores;
* exact opposite merged/split boundary responses; and
* two disjoint boundary-full connected subgraphs in the split-response
  shore.

It does not refute the live disjunctive theorem, because conclusion
“`G` contains a `K_7` minor” holds explicitly.  It also cannot satisfy the
proper-minor six-colourability of a nontrivial contraction-critical graph:
contracting the model (5.2) gives a proper `K_7` minor.

The useful restriction is therefore sharp.  Any positive packing theorem
must spend global `K_7`-minor exclusion (and, for the colouring conclusion,
the proper-minor responses); connectivity and the exact local colouring
responses cannot replace it.  A promising candidate disjunction is not
“packing or small separator” but

\[
 \text{three-support packing}
 \quad\text{or}\quad
 \text{saturated-edge `K_7` completion}
 \quad\text{or}\quad
 \text{compatible separator/descent}.
\]
