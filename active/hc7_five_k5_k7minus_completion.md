# Five `K_5` subgraphs force a `K_7^-` minor

**Status:** written proof on an experimental branch; not yet separately audited or
promoted.  The theorem is independent of the bounded-interface programme.

Here `K_7^-` denotes the graph obtained from `K_7` by deleting one edge.

## Theorem

Let `G` be a seven-connected graph.  If `G` contains five distinct subgraphs
isomorphic to `K_5`, then `G` contains a `K_7^-` minor.

Equivalently, a seven-connected `K_7^-`-minor-free graph has at most four
`K_5` subgraphs.

## External inputs

We use the following established results.

1. **Three-clique completion.**  If a seven-connected graph contains three
   `K_5` subgraphs whose union has order at least twelve, then it contains a
   `K_7` minor.  This is the `k=5` case of Kawarabayashi--Luo--Niu--Zhang,
   *On the structure of k-connected graphs without K_k-minor*, European J.
   Combin. 26 (2005), 293--308; it is also stated as Theorem 18 in
   Norin--Totschnig, arXiv:2507.03244.

2. **Common-pair completion.**  If three `K_5` subgraphs of a
   seven-contraction-critical graph have the same two-vertex pairwise
   intersection, then the graph has a `K_7` minor.  The proof of the cited
   Kawarabayashi--Toft lemma uses only seven-connectivity in this application;
   we use it in that seven-connected form.  See Kawarabayashi--Toft,
   *Any 7-chromatic graph has K_7 or K_{4,4} as a minor*, Combinatorica 25
   (2005), Lemma 3(i), and Norin--Totschnig, Lemma 17.

3. **Specified independent edges on a cycle.**  Every set of `k` independent
   edges in a `(k+1)`-connected graph lies on one cycle.  We need only `k=3`.
   This is Häggkvist--Thomassen, *Circuits through specified edges*, Discrete
   Math. 41 (1982), 29--34, DOI `10.1016/0012-365X(82)90078-4`.

We also use the fan and set-to-set forms of Menger's theorem.

## 1. Two preliminary intersection bounds

Let `L_1,L_2` be distinct `K_5` subgraphs of a seven-connected graph with no
`K_7^-` minor.

### Lemma 1.1

\[
                         |L_1\cap L_2|\le2.                  \tag{1.1}
\]

### Proof

If the intersection has order four, `G[L_1 union L_2]` contains `K_6^-`.
Choose a vertex outside this six-set.  The fan lemma gives six internally
disjoint paths from it to the six vertices, with distinct ends.  Their union
outside the six-set is a seventh connected branch set adjacent to all six,
so the `K_6^-` extends to a `K_7^-` minor.

Suppose the intersection has order three.  Put

\[
 Z=L_1\cap L_2,\qquad L_1-Z=\{x_1,x_2\},\qquad
 L_2-Z=\{y_1,y_2\}.
\]

The graph `G-Z` is four-connected.  Take two vertex-disjoint paths `P_1,P_2`
between the two displayed pairs, with ends relabelled as `x_i,y_i`.
After deleting `x_1,y_2`, the graph remains two-connected, and hence there is
a path `Q` joining `P_1` to `P_2`, internally disjoint from both.  Contract
`P_1-x_1` and `P_2-y_2`, and contract all but one edge of `Q`.  Together with
the three singleton vertices of `Z`, the resulting seven branch sets have
all pairwise adjacencies except possibly one.  This is the explicit
`K_7^-` construction used in Norin--Totschnig, Claim 4.6.  Both cases are
impossible.  \(\square\)

### Lemma 1.2

If a family of at least three `K_5` subgraphs occurs in a seven-connected
`K_7^-`-minor-free graph, then every two members of the family intersect.

### Proof

Suppose `L_1 cap L_2=empty` and choose a third member `L_3`.  By the
three-clique completion theorem,

\[
                      |L_1\cup L_2\cup L_3|\le11.             \tag{1.2}
\]

Hence `L_3` has at least four vertices in `L_1 union L_2`.  Lemma 1.1 forces
exactly two in each and one outside.  Put

\[
 S=L_3\cap(L_1\cup L_2),
 \qquad A=L_1-L_3,
 \qquad B=L_2-L_3.
\]

Thus `S` is a four-clique and `A,B` are disjoint three-sets.  The graph `G-S`
is three-connected.  Menger's theorem gives three pairwise vertex-disjoint
`A`--`B` paths with distinct ends, and therefore with all three members of
`A` and all three members of `B` as ends.  Contract each path to one branch
set.  These three sets are pairwise adjacent through their ends in the clique
`L_1`; each is adjacent to all four singleton vertices of `S`, seeing two
through its `L_1` end and the other two through its `L_2` end.  They and the
four vertices of `S` form a `K_7` minor, a contradiction.  \(\square\)

## 2. The remaining three-clique patterns

Let `L_1,L_2,L_3` be three distinct `K_5` subgraphs.  By Lemmas 1.1--1.2,
all three pairwise intersection sizes belong to `{1,2}`.  The three-clique
completion theorem gives

\[
                     |L_1\cup L_2\cup L_3|\le11.              \tag{2.1}
\]

Write

\[
 s_{ij}=|L_i\cap L_j|,
 \qquad t=|L_1\cap L_2\cap L_3|.
\]

Inclusion--exclusion gives

\[
                15-(s_{12}+s_{13}+s_{23})+t\le11.             \tag{2.2}
\]

The possible multisets of pairwise intersection sizes are therefore

\[
                 (2,1,1),\qquad(2,2,1),\qquad(2,2,2).          \tag{2.3}
\]

The `(2,1,1)` case has empty triple intersection.  It is the configuration
of Rolek--Song--Thomas, Lemma 2.4, Figure 3(a).  Deleting the four vertices
in the three pairwise intersections leaves a three-connected graph; three
disjoint paths between the private three-set of one clique and the private
four-set of the other two contract, together with those four singleton
vertices, to a `K_7` minor.

The `(2,2,1)` case with empty triple intersection is Figure 3(b) of the same
lemma.  Deleting the five vertices in the pairwise intersections leaves a
two-connected graph; two disjoint paths between the two private pairs,
together with those five singletons, contract to a `K_7` minor.  If its
triple intersection is nonempty, no exclusion is needed: this remains the
allowed two-edge pattern in the auxiliary graph below.

It remains to eliminate `(2,2,2)`.

### Lemma 2.1

Three `K_5` subgraphs with all three pairwise intersections of order two
force a `K_7^-` minor in a seven-connected graph.

### Proof

Let `Z=L_1 cap L_2 cap L_3`.

If `|Z|=2`, all three pairwise intersections equal `Z`, and the established
common-pair completion lemma gives a `K_7` minor.

If `Z` is empty, the three pairwise intersections are disjoint two-sets.
Their union induces a `K_6`: every two of the three two-sets lie together in
one of the `K_5` subgraphs.  A six-fan from a vertex outside this `K_6`
provides a seventh branch set adjacent to all six, yielding a `K_7` minor.

Suppose finally that `Z={z}`.  There are distinct vertices `a,b,c` and
pairwise disjoint edges

\[
 P=\{p_1,p_2\},\qquad Q=\{q_1,q_2\},\qquad R=\{r_1,r_2\}
\]

such that

\[
 \begin{aligned}
 L_1&=\{z,a,b,p_1,p_2\},\\
 L_2&=\{z,a,c,q_1,q_2\},\\
 L_3&=\{z,b,c,r_1,r_2\}.
 \end{aligned}                                                \tag{2.4}
\]

The graph

\[
                              G-\{z,a,b\}                      \tag{2.5}
\]

is four-connected.  By the Häggkvist--Thomassen theorem, it has a cycle `C`
containing the three independent edges `p_1p_2,q_1q_2,r_1r_2`.

If `c notin V(C)`, delete those three distinguished cycle edges.  The three
remaining cycle segments are disjoint connected branch sets.  Each contains
endpoints belonging to two different private pairs in (2.4), and is
therefore adjacent to each of `z,a,b,c`.  The three segments are pairwise
adjacent through the three deleted cycle edges.  Together with the four
singletons `{z},{a},{b},{c}`, they give a `K_7` model.

Assume `c in V(C)`.  Orient and relabel the private pairs so the cyclic order
is

```text
p1--p2 ... c ... q1--q2 ... r1--r2 ... p1.
```

Partition the cycle into four connected segments:

* `X`: from `p2` up to, but not including, `c`;
* `Y`: from `c` through `q1`;
* `Z_1`: from `q2` through `r1`;
* `Z_2`: from `r2` through `p1`.

Consecutive segments are adjacent along the cycle.  In addition, `Y` is
adjacent to `Z_2`, because `Y` contains `c`, `Z_2` contains `r_2`, and
`cr_2` is an edge of `L_3`.  Thus the four segments have every pairwise
adjacency except possibly `X Z_1`.

Every segment is adjacent to each of `z,a,b`: `X` contains a `P`-vertex,
`Y` contains `c`, `Z_1` contains a `Q`- and an `R`-vertex, and `Z_2` contains
an `R`- and a `P`-vertex.  Consequently

\[
                 \{z\},\{a\},\{b\},X,Y,Z_1,Z_2               \tag{2.6}
\]

are seven pairwise disjoint connected branch sets with at most the one
missing adjacency `XZ_1`.  They form a `K_7^-` model.  \(\square\)

It follows from (2.3) and Lemma 2.1 that, in a seven-connected
`K_7^-`-minor-free graph, every triple of distinct `K_5` subgraphs has
exactly two pairwise intersections of order two and one of order one.

## 3. Auxiliary-graph contradiction

Let `mathcal C` be the family of all `K_5` subgraphs of `G`, and define a
graph `J` on `mathcal C` by

\[
 L_iL_j\in E(J)\quad\Longleftrightarrow\quad |L_i\cap L_j|=2. \tag{3.1}
\]

The preceding section says that every three vertices of `J` induce exactly
two edges.

The graph `J` is bipartite.  Indeed, an induced odd cycle has either length
three, which gives three edges on one triple, or length at least five, in
which case three suitably chosen cycle vertices induce one edge.  Both
contradict the exact-two-edge property.

Moreover `J` has no independent set of order three.  Hence each side of its
bipartition has order at most two, and

\[
                              |mathcal C|\le4.                 \tag{3.2}
\]

Therefore five distinct `K_5` subgraphs force a `K_7^-` minor.  \(\square\)

## Trust boundary

The proof uses only seven-connectivity and the three cited clique/cycle
results.  It does not use contraction-critical colouring responses, the
bounded-interface programme, or any finite computation.  Before promotion,
the following points require a separate cold audit:

1. the seven-connected formulation of the common-pair Kawarabayashi--Toft
   lemma;
2. the exact branch-set contractions in Lemma 1.1 for intersection three;
3. the four-segment allocation in the `|Z|=1` case of Lemma 2.1; and
4. the set-system identification of the two Rolek--Song--Thomas Figure 3
   configurations.
