# Simultaneous singletonization at the exact order-eight boundary

**Status:** written proof; separately internally audited in
[`hc7_order_eight_simultaneous_singletonization_audit.md`](hc7_order_eight_simultaneous_singletonization_audit.md).
This note proves an exact normalization of the two nonadjacent two-vertex
branch sets in the exceptional order-eight configuration.  It then applies
the singleton-centre exchange inside an original complementary component;
the apparent exact degree-seven residue is itself an actual order-seven
separation.  The note does not eliminate the remaining larger-boundary
separator or prove `HC_7`.

## 1. Setup

Let `G` be a seven-connected, `K_7`-minor-free graph.  Suppose

\[
 S=R\mathbin{\dot\cup}V(e)\mathbin{\dot\cup}V(f)
       \mathbin{\dot\cup}\{x\},\qquad |R|=3,                 \tag{1.1}
\]

is an eight-vertex separator with the following properties.

1. `R` is a clique.
2. `e` and `f` are vertex-disjoint edges and are anticomplete to one
   another.
3. Each of `e,f` is collectively adjacent to every vertex of `R`.
4. `G-S` has exactly two components `C,D`, and each component is adjacent
   to every literal vertex of `S`.

These are the hypotheses of the exceptional outcome in Lemma 6.1 of
[`../results/hc7_star_kernel_rooted_four_contraction.md`](../results/hc7_star_kernel_rooted_four_contraction.md).
In particular, `C,D,S` partition `V(G)`.

For an endpoint `u` of one of the two edges, put

\[
        M(u)=\{r\in R:ur\notin E(G)\}.                     \tag{1.2}
\]

Call `u` **`R`-admissible** when `|M(u)|<=1`.

## 2. Both deficient branch sets can be made singletons

### Lemma 2.1 (`R`-admissible endpoints)

Each of `e` and `f` has an `R`-admissible endpoint.

#### Proof

Write one of the edges as `uv`.  Collective adjacency to every `r in R`
means that `r` cannot belong to both `M(u)` and `M(v)`.  Hence

\[
                    |M(u)|+|M(v)|\leq3.
\]

One of the two summands is at most one.  The other edge is identical.
\(\square\)

### Theorem 2.2 (simultaneous singletonization)

Choose an `R`-admissible endpoint `a` of `e` and an `R`-admissible endpoint
`b` of `f`, and denote their mates by `a'` and `b'`.  For either prescribed
choice `U in {C,D}`, there are five pairwise disjoint connected branch sets

\[
                 U,\quad V^+,\quad W_r\ (r\in R),          \tag{2.1}
\]

where `V={C,D}-\{U\}`, with all of the following properties.

1. Together with the singleton branch sets `{a},{b}`, the five sets in
   (2.1) partition `V(G)`.
2. The five sets in (2.1) are pairwise adjacent.
3. Each of `{a}` and `{b}` is adjacent to every set in (2.1).
4. `{a}` and `{b}` are anticomplete.
5. For every `r in R`, each of `a,b` has at most one neighbour in `W_r`.

Consequently these seven branch sets form a spanning `K_7`-minus-one-edge
model whose two nonadjacent branch sets are the literal singleton vertices
`a,b`.  The five-part branch-set frame is unchanged: two branch sets are
derived from `C,D` and the remaining three are rooted at the vertices of
`R`.

#### Proof

For `q in {a,b}`, let `q'` denote its mate.  If
`M(q)={r}`, assign `q'` to the branch set rooted at `r`; if `M(q)` is empty, call
`q'` free.  Define

\[
 W_r=\{r\}\cup
      \{q':q\in\{a,b\},\ M(q)=\{r\}\}.                  \tag{2.2}
\]

Every set `W_r` is connected: if `q'` was assigned to it, then `q` misses
`r`, so collective adjacency of the edge `qq'` to `r` forces `q'r`.

Put

\[
 V^+=V\cup\{x\}\cup
       \{q':q\in\{a,b\},\ M(q)=\varnothing\}.            \tag{2.3}
\]

The set `V^+` is connected.  Indeed, `V` is connected and is adjacent to
each literal boundary vertex, hence every added vertex has a neighbour in
`V`.  The sets in (2.1), together with `{a},{b}`, plainly partition
`V(G)`.

The five nonsingleton branch sets are pairwise adjacent.  The vertex `x` in
`V^+` has a neighbour in `U`; each `r in R` has a neighbour in each of
`U,V`; and the three root vertices in `R` form a clique.  Enlarging these
sets by `a'` or `b'` loses none of those adjacencies.

Consider the singleton `q in {a,b}`.  It has a neighbour in each of
`U,V`, by boundary-fullness.  If its mate `q'` is free, then the edge
`qq'` also joins `q` to `V^+`; otherwise its neighbour in `V` already
does so.  For `r in R`, either `qr` is an edge or
`M(q)={r}` and the edge `qq'` joins `q` to `W_r`.  Thus both singletons
meet all five branch sets.  They are anticomplete because the original edges
`e,f` are anticomplete.

Finally fix `r in R`.  If `a` misses `r`, then `W_r` contains `a'` but
`a` is adjacent to neither `r` nor the possible vertex `b'`; hence its
only neighbour in that branch set is `a'`.  If `a` meets `r`, its mate was not
assigned to `W_r`, and anticompleteness of `e,f` excludes an edge from
`a` to a possible `b'`; hence its only possible neighbour there is `r`.
The argument for `b` is symmetric.  This proves all five assertions.
\(\square\)

The construction is exact rather than existential: it permits either
component to be retained literally as the unmodified branch set `U`.  All
boundary vertices which do not enter one of the three branch sets rooted in
`R` are absorbed into the opposite component-derived branch set `V^+`.

## 3. When the singleton exchange descends inside an original component

We use the following immediate prescribed-branch-set form of Theorem 1 in
[`../results/hc7_near_k7_singleton_one_hole_trichotomy.md`](../results/hc7_near_k7_singleton_one_hole_trichotomy.md).

### Lemma 3.1 (prescribed repeated-neighbour branch set)

In the hypotheses of that theorem, suppose a specified neutral branch set
`U_i` contains two distinct neighbours of the singleton centre `a`.  Then
the proof of the theorem can be run with `U_i` as its selected branch set.  Its
two non-`K_7` outcomes therefore use a proper nonempty connected subset of
that specified `U_i`.

#### Proof

The seven-neighbour count in the cited proof is used only to find two
neighbours in one neutral branch set.  If the two neighbours are prescribed
in advance, start the proof with those two roots.  Every connected-core,
opposite-root, separator, transfer, and deficiency-rotation construction in
the remainder of the proof takes place inside that one branch set.  No later
step uses how the two roots were found.  Thus the two non-target sets `Y`
and `W` in that proof are proper nonempty connected subsets of the specified
`U_i`.  \(\square\)

### Lemma 3.2 (the only obstruction to a pure component branch set)

Let `q` be an `R`-admissible endpoint of `e` or `f`, and let `q'` be its
mate.  If neither `C` nor `D` contains two neighbours of `q`, then

\[
 d_G(q)=7,qquad
 N_G(q)=R\cup\{q',x,c_q,d_q\},                            \tag{3.1}
\]

where `c_q` and `d_q` are respectively the unique neighbours of `q` in
`C` and `D`.  In particular `q` is adjacent to every vertex of `R` and to
`x`.

#### Proof

Boundary-fullness gives at least one neighbour of `q` in each of `C,D`, so
the hypothesis says that it has exactly one in each.  It is anticomplete to
the opposite defect edge.  Apart from its mate, its possible remaining
neighbours outside `C,D` are `x` and the `3-|M(q)|` vertices of `R` which
it meets.  Hence

\[
 d_G(q)\leq 1+1+1+1+(3-|M(q)|)=7-|M(q)|.                 \tag{3.2}
\]

Seven-connectivity gives `d_G(q)>=7`.  Equality must hold throughout
(3.2), proving (3.1), `M(q)=emptyset`, and `qx in E(G)`. \(\square\)

### Theorem 3.3 (strict component reduction or an order-seven separation)

At least one of the following occurs.

1. `G` contains a `K_7` minor.
2. `G` has an actual order-seven separation.
3. There is a component `U in {C,D}` and a proper nonempty connected set
   `Y subsetneq U` such that `N_G(Y)` is an actual separator of order at
   least eight.
4. There is a labelled `K_7^-` or `K_7^vee` model whose deficient centre
   is a proper nonempty connected subset of one original component
   `U in {C,D}`.

#### Proof

By Lemma 2.1, each edge has an `R`-admissible endpoint.  If some
`R`-admissible endpoint `q` satisfies (3.1), then `d_G(q)=7`.  The vertex
`q` is nonadjacent
to both endpoints of the other defect edge.  Therefore deleting `N_G(q)`
isolates `q` while leaving one of those nonneighbours present, so `N_G(q)`
is an actual separator of order seven.  This is outcome 2.

Otherwise choose an `R`-admissible endpoint `a` of one edge and any
`R`-admissible endpoint `b` of the other edge.  Neither satisfies (3.1).
Lemma 3.2 gives a component `U in {C,D}` containing two neighbours of
`a`.

Apply Theorem 2.2 with this choice of `U`.  The resulting model is spanning,
so every neighbour of `a` lies in its six foreign branch sets.  Regard
`{b}` as the one branch set missed by `{a}`.  The other five branch sets
are the neutral branch sets of the singleton one-hole theorem.  They form a
clique model by Theorem 2.2, and the pure component branch set `U` contains the
two prescribed neighbours of `a`.

Apply Lemma 3.1 and the singleton one-hole trichotomy with this specified
branch set.  Its target outcome is item 1 here.  Its separator outcome is item 2,
unless that separator has order at least eight, in which case it is item 3.
Its exact-order-seven subcase is item 2 and has the standard full-boundary
property.  Its deficiency-rotation outcome is item 4.  In items 3 and 4
the new connected set is a proper subset of the original component `U`,
not merely a subset of a branch set enlarged by boundary vertices.
\(\square\)

## 4. Exact limit of the normalization

Theorem 2.2 answers the first normalization question affirmatively: the
two nonadjacent edge branch sets can always be made simultaneous singleton
branch sets on the same five-part frame.

The stronger proposed terminal conclusion does **not** yet follow from the
audited singleton one-hole theorem:

* its separator outcome has order **at least** seven, not necessarily
  exactly seven;
* it contains no theorem that a nominated pair meets every `K_5` minor;
  and a separator of order greater than seven does not itself supply the
  exact-seven colouring composition used elsewhere in the project.

Thus no honest argument presently turns every non-`K_7` output into the
three-way list “order-seven separation, strict near-`K_7` rotation inside
`C` or `D`, or a fixed pair”.  What is proved is one step weaker: the only
additional output is an actual separator whose one side is a strict proper
connected subset of `C` or `D`, but whose boundary may have order greater
than seven.  This is a strict reduction in component order, but the theorem
does not claim that the larger boundary preserves the same recursive state.
The apparent exact degree-seven endpoint obstruction is not live: its open
neighbourhood is itself the required order-seven separator.
