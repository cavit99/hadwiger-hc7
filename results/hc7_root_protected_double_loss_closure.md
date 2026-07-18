# Root-protected closure of one double-loss orientation

**Status:** written proof; separate internal audit GREEN.  This is a conditional
closure theorem inside the degree-seven branch.  It does not prove `HC_7`,
and it does not treat the opposite orientation in which the protected
boundary root lies in the connected subgraph missing the singleton pole.

## 1. Degree-seven setup and literal provenance

Let `G` be a seven-connected graph such that

\[
   \chi(G)=7,
   \qquad K_7\not\preccurlyeq G,
\]

and every proper minor of `G` is six-colourable.  Let `u` be a vertex of
degree seven, put

\[
   S=N_G(u),\qquad H=G[S],\qquad C=G-N_G[u],
\]

and assume the proved degree-seven conclusions:

1. `C` is nonempty and connected;
2. `C` is adjacent to every literal vertex of `S`; and
3. `alpha(H)<=2`.

Suppose that `G` has a **spanning boundary-labelled one-missing-adjacency
model**

\[
             \{a\},\quad D,\quad F,\quad R_1,R_2,R_3,R_4,       \tag{1.1}
\]

with the following literal provenance.

1. The seven sets in (1.1) partition `V(G)`, are nonempty and connected,
   and every pair is adjacent except `\{a\}D`.
2. The vertex `a` lies in `S`.
3. The deficient bag `D` contains two distinct vertices `b,x in S`.
4. The donor bag `F` contains exactly one vertex `f in S`.
5. Of the four bags `R_1,...,R_4`, one is the singleton `\{u\}` and each
   of the other three contains exactly one vertex of `S`.
6. No bag in (1.1) contains any further vertex of `S union {u}`.

Let `L` be a nonempty proper connected subset of `F` such that

\[
  f\notin L,\qquad F_0=F-L\text{ is connected},                \tag{1.2}
\]

and suppose that

\[
  L\sim\{a\},D,R_1,R_2,R_3,qquad L\not\sim R_4,              \tag{1.3}
\]

while

\[
  F_0\not\sim D,R_1,R_2,R_3.                                  \tag{1.4}
\]

Condition (1.4) is exactly the ownership conclusion in the exceptional
lobe-median configuration: every old edge from `F` to each of
`D,R_1,R_2,R_3` has its `F`-end in `L`.  The closure proof below uses only
this ownership consequence; it does not require the remaining quotient
adjacencies of the lobe-median configuration.

## 2. Closure theorem

### Theorem 2.1

The configuration (1.1)--(1.4) cannot occur.  In fact, those hypotheses
give an explicit `K_7`-minor model in `G`.

### Proof

Since `F` contains no vertex of `S` other than `f`, condition (1.2) gives

\[
                            L\subseteq C.                       \tag{2.1}
\]

The vertex `u` has no neighbour in `C`.  Hence (2.1) makes `L`
anticomplete to `\{u\}`.  By (1.3), none of `R_1,R_2,R_3` is `\{u\}`.
The provenance in item 5 therefore forces

\[
                              R_4=\{u\}.                         \tag{2.2}
\]

For `i=1,2,3`, let `r_i` be the unique vertex of `S` contained in
`R_i`.  Because `f in F_0`, (1.4) implies that `f` has no edge to any of

\[
                         b,x,r_1,r_2,r_3.                        \tag{2.3}
\]

All six vertices in (2.3) together with `f` lie in `S`.  If two distinct
vertices `v,w` from the five-set in (2.3) were nonadjacent, then

\[
                             \{f,v,w\}
\]

would be an independent set of `H`, contrary to `alpha(H)<=2`.
Consequently

\[
                     H[\{b,x,r_1,r_2,r_3\}]\cong K_5.           \tag{2.4}
\]

The set `C union {f}` is connected because `C` is connected and is
adjacent to every vertex of `S`, in particular to `f`.  Consider the
seven pairwise disjoint connected sets

\[
   \{u\},\quad C\cup\{f\},\quad
   \{b\},\quad\{x\},\quad\{r_1\},\quad\{r_2\},\quad\{r_3\}.
                                                                    \tag{2.5}
\]

The last five sets are pairwise adjacent by (2.4).  The singleton `u` is
adjacent to every vertex of `S`, so it meets the last five sets and also
meets `C union {f}` through the edge `uf`.  Finally, `C union {f}` is
adjacent to every one of the last five sets because the connected graph
`C` is adjacent to every vertex of `S`.  Thus (2.5) is a `K_7`-minor
model, contradicting `K_7\not\preccurlyeq G`.  \(\square\)

## 3. Exact scope

The theorem spends the protected-root orientation `f notin L`.  If the
protected root instead lies in `L`, then `L` may meet `u`, (2.2) no longer
follows, and `F-L` contains no boundary vertex with which to create the
five common anti-neighbours in (2.3).  That opposite orientation remains a
dynamic proper-minor colouring problem.

No planarity, Two Paths theorem, quotient separator, or unlabelled minor
regeneration is used.  The closure rests on the literal degree-seven
facts that the exterior `C` is connected and full to `S`, and that
`alpha(G[S])<=2`.

## 4. Dependencies

- [connected degree-seven anti-neighbourhood](../results/hc7_degree7_anti_neighbourhood_connectivity.md)
- [boundary-labelled near-`K_7` model](../results/hc7_degree7_aligned_near_k7_model.md)
- [three-anchor lobe-median exchange](../results/hc7_three_anchor_lobe_median.md)
