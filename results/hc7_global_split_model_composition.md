# Composition of support-six `K_5` models

## Status

The two composition lemmas below are proved.  They are stated in standard
rooted-minor language and do not use colouring states or a selected
exact-seven separation.

The first lemma eliminates an infinite family: three support-six models
with one common singleton `K_4` core and pairwise disjoint split edges
already force a literal `K_7` minor in a seven-connected graph.  The second
lemma records the exact hypotheses under which models with different cores
can be composed by the published three-clique theorems.

Neither result proves that a family with transversal number greater than two
contains models satisfying those hypotheses.  That extraction/composition
step remains open.

## 1. A rooted-triangle composition lemma

### Lemma 1.1

Let `H` be a graph and let `A_1,A_2,A_3` be pairwise vertex-disjoint,
nonempty connected subgraphs.  Suppose that

1. `H-v` is connected for every
   `v in V(H)-(V(A_1) union V(A_2) union V(A_3))`; and
2. `H-V(A_i)` is connected for `i=1,2,3`.

Then `H` has three pairwise disjoint, pairwise adjacent connected subgraphs
`B_1,B_2,B_3` with `A_i subseteq B_i` for every `i`.

#### Proof

Contract each `A_i` to a vertex `a_i`, and call the resulting graph `J`.
The graph `J` has no cutvertex.  Indeed, deleting an uncontracted vertex is
the image of the connected graph `H-v`, while deleting `a_i` is the image of
the connected graph `H-V(A_i)`.  Thus `J` is two-connected.

For completeness, three prescribed vertices in a two-connected graph root a
`K_3` minor.  Choose an `a_1-a_2` path `P` in `J-a_3`.  The Fan Lemma gives
two internally disjoint paths from `a_3` to distinct vertices `p,q` of `P`,
with no other vertices on `P`.  Order `P` from `a_1` to `a_2`, with `p`
before `q`, and choose an edge `rs` of the subpath `pPq`.  One branch set
contains `a_1Pr`, a second contains `sPa_2`, and the third contains `a_3`
and the two fan paths with their ends `p,q` removed.  The edge `rs` joins
the first two sets, and the last edges of the fan paths join the third set
to each of them.  These are a rooted `K_3` model at `a_1,a_2,a_3`.

Expanding the three contractions gives the required `B_1,B_2,B_3` in
`H`.  \(\square\)

## 2. Three disjoint split bags over one clique core

Call a connected subgraph `A` **complete to a set `Q` as a branch set** if
for every `q in Q` at least one vertex of `A` is adjacent to `q`.  Individual
vertices of `A` need not be complete to `Q`.

### Theorem 2.1 (nonseparating common-core composition)

Let `Q` be a literal `r`-clique in a graph `G`, and put `H=G-Q`.  Suppose
that `H` is two-connected and that `A_1,A_2,A_3` are pairwise
vertex-disjoint connected subgraphs of `H` such that

1. every `A_i` is complete to `Q` as a branch set; and
2. `H-V(A_i)` is connected for each `i`.

Then `G` contains a `K_{r+3}` minor.

#### Proof

The hypotheses of Lemma 1.1 hold: two-connectivity gives `H-v` connected
for every vertex outside the three roots, and item 2 handles deletion of a
whole root.  The lemma gives three pairwise adjacent connected bags
containing the `A_i`.  Together with the singleton bags in `Q`, they form a
`K_{r+3}` model.  \(\square\)

### Corollary 2.2 (small roots in a highly connected graph)

Let `r>=1`, let `G` be `(r+3)`-connected, and let `Q` be a literal
`r`-clique.  Suppose `A_1,A_2,A_3` are pairwise vertex-disjoint connected
subgraphs of `G-Q`, each on at most two vertices, and each is complete to
`Q` as a branch set.  Then `G` contains a `K_{r+3}` minor.

#### Proof

Put `H=G-Q`.  The graph `H` is three-connected.  In particular `H-v` is
connected for every vertex `v`, and `H-V(A_i)` is connected because
`|V(A_i)|<=2`.  Apply Theorem 2.1.  \(\square\)

### Corollary 2.3 (support six)

Let `G` be seven-connected.  Suppose three six-vertex `K_5` models have
the same four singleton bags `Q` and have pairwise vertex-disjoint
two-vertex bags.  Then `G` contains a `K_7` minor.

#### Proof

Each two-vertex bag is an edge, is disjoint from `Q`, and is complete to
`Q` as a branch set.  Apply Corollary 2.2 with `r=4`.  \(\square\)

The complementary-defect type of each split edge is irrelevant to this
proof.  It is needed in the global support-six normalization only to rule
out a literal `K_5` obtained from one endpoint.

## 3. Models with different cores: the safe-contraction theorem

Let `M_i` (`i=1,2,3`) be a support-six `K_5` model with singleton core
`Q_i` and split edge `e_i=x_i y_i`.  Say the three models are **contraction
clean** when the `e_i` are pairwise vertex-disjoint and

\[
             V(e_i)\cap (Q_j\cup V(e_j))=\varnothing
             \qquad(i\ne j).
\]

Contract all three edges and denote their images by `z_i`.  Then

\[
                         L_i=Q_i\cup\{z_i\}
\]

is a literal `K_5` in the contracted graph.

### Lemma 3.1 (anchored separators after parallel contractions)

Let `G` be `k`-connected and let `F` be a matching.  Put `H=G/F`, and
for a vertex separator `T` of `H` let `rho(T)` be the number of contracted
images belonging to `T`.  Then

\[
                            |T|+\rho(T)\ge k.             \tag{3.1}
\]

#### Proof

Replace every contracted image in `T` by the two ends of its edge.  The
resulting set `T^+` has order `|T|+rho(T)`.  Every path in `G-T^+` maps to a
walk in `H-T`, so two components separated by `T` remain separated by
`T^+`.  Thus `T^+` is a vertex separator of `G`, and `k`-connectivity gives
(3.1).  \(\square\)

For three contractions in a seven-connected graph, the quotient is
automatically four-connected.  More precisely, every separator of order
four contains all three contraction images; a separator of order five
contains at least two; and a separator of order six contains at least one.
In the `(4,3)`, `(5,2)`, and `(6,1)` cases its lift is an actual
seven-separation.  This is the full connectivity information supplied by
parallel contraction alone.

### Theorem 3.2 (published-clique lift)

Let `G` contain three contraction-clean support-six models and put
`H=G/e_1/e_2/e_3`.

1. If `H` is seven-connected and
   `|L_1 union L_2 union L_3|>=12`, then `G` contains a `K_7` minor.
2. If `H` is seven-connected and non-two-apex, and
   `|L_i cap L_j|<=3` for all distinct `i,j`, then `G` contains a `K_7`
   minor.

#### Proof

For item 1, apply Theorem 1.11 of Kawarabayashi--Luo--Niu--Zhang,
*On the structure of k-connected graphs without K_k-minor*, European
Journal of Combinatorics 26 (2005), 293--308, with `k=5`.  It states that a
seven-connected graph containing three `5`-cliques whose union has order at
least twelve has a `K_7` minor.

For item 2, apply Theorem 1.10 of Niu--Zhang, *Cliques, minors and apex
graphs*, Discrete Mathematics 309 (2009), 4095--4107, with `k=5`.  The
hypotheses are exactly seven-connectivity, non-two-apexness, and pairwise
intersection at most three.

In either case the resulting `K_7` model in `H` expands through the three
edge contractions to a `K_7` model in `G`.  \(\square\)

### Corollary 3.3

Under the hypotheses of Theorem 3.2, contraction cleanliness gives

\[
 |L_i\cap L_j|=|Q_i\cap Q_j|=|V(M_i)\cap V(M_j)|
\]

and

\[
 |L_1\cup L_2\cup L_3|
       =|V(M_1)\cup V(M_2)\cup V(M_3)|-3.
\]

Consequently, if `H` is seven-connected and the union of the three model
supports has order at least fifteen, then `G` has a `K_7` minor.  In
particular this holds if the three supports intersect pairwise in at most
one vertex.

## 4. Sharp limits and the remaining theorem gap

The common-core theorem needs both the connectivity and disjoint-root
mechanisms.  Without connectivity, take a `K_4` named `Q` and three mutually
anticomplete edges, making each edge collectively adjacent to all of `Q`.
This has the three displayed support-six models but no `K_7` minor.  Without
disjoint split bags, three qualified edges may share endpoints, so they
cannot be three branch sets.

No purely six-uniform set-family argument extracts the hypotheses of
Theorem 3.2 from transversal number greater than two, even when the ground
set is unbounded.  Let `B={1,...,8}`, include every six-subset of `B`, and
also include

\[
                  \{1,2,3,4,5,x_i\}\qquad(i=1,2,\ldots)
\]

for distinct new elements `x_i`.  The resulting family has transversal
number three: its subfamily of all six-subsets of `B` already needs three
points, while `{1,2,3}` meets every displayed set.  Nevertheless the union
of any three members has order at most ten.  In particular it supplies no
three supports with union fifteen and no three nearly disjoint supports.
The special graph structure of the models must therefore be used.

The exact unresolved composition problem is therefore not another
intersection calculation.  Given a family of support-six models with no
two-vertex transversal, one must prove one of the following:

1. three models have a common singleton core and disjoint split bags, so
   Theorem 2.1 applies;
2. three contraction-clean models can be chosen so that their simultaneous
   contraction remains seven-connected and satisfies Theorem 3.2; or
3. failure of those choices gives one coherent pair meeting **all** `K_5`
   models, not merely the selected three, or a state-preserving exact-seven
   handoff.

Contraction cleanliness alone does not preserve seven-connectivity.  The
existing support-six contraction dichotomy handles one split edge at a
time; simultaneous contractions may expose interacting separators.  Also,
a two-apex pair in the contracted graph need not pull back to two literal
vertices of `G`.  These are the two precise obstructions to promoting
Theorem 3.2 into the desired global support-six transversal theorem.
