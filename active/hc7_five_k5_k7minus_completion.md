# Three `K_5` subgraphs force a `K_7` minor under `K_7^-` exclusion

**Status:** written proof on an experimental branch; not yet separately audited
or promoted.

Here `K_7^-` denotes the graph obtained from `K_7` by deleting one edge.

## Theorem

Let `G` be a seven-connected graph with no `K_7^-` minor.  If `G` is not
two-apex, then `G` contains at most two distinct literal `K_5` subgraphs.

Consequently, every seven-connected seven-chromatic graph containing three
distinct `K_5` subgraphs contains a `K_7^-` minor; in fact it contains a
`K_7` minor.

## Proof

Suppose that `G` contains three distinct `K_5` subgraphs

\[
                             L_1,L_2,L_3.                     \tag{1}
\]

We first show that

\[
                         |L_i\cap L_j|\le3                    \tag{2}
\]

for every distinct `i,j`.  Two distinct five-vertex sets cannot intersect in
five vertices.  If, say, `|L_1 cap L_2|=4`, then their union induces a graph
containing `K_6^-`: all pairs are edges except possibly the pair of vertices
unique to the two cliques.

Let

\[
                            X=L_1\cup L_2,\qquad |X|=6.
\]

Because `G` is seven-connected, `G-X` is nonempty and connected.  Moreover
every vertex of `X` has a neighbour in `G-X`: its degree is at least seven,
while it has at most five neighbours inside the six-set `X`.  Contract the
connected graph `G-X` to one branch set and retain the six singleton vertices
of `X`.  These seven branch sets form a `K_7^-` model, contrary to the
hypothesis.  This proves (2).

Now apply Niu and Zhang's clique-minor theorem with `k=5`: if a
`(k+2)`-connected non-`(k-3)`-apex graph contains three `k`-cliques whose
pairwise intersections have order at most `k-2`, then it contains a
`K_{k+2}` minor.  Here `G` is seven-connected, non-two-apex, and (2) supplies
three `K_5` subgraphs with pairwise intersections at most three.  Therefore

\[
                              K_7\preccurlyeq G,               \tag{3}
\]

contradicting the stronger assumption that `G` has no `K_7^-` minor.

This proves the first assertion.

For the consequence, a seven-chromatic graph is not two-apex: if
`G-{x,y}` were planar, four colours on that planar graph and two fresh colours
for `x,y` would give a proper six-colouring of `G`.  Hence the first assertion
applies, and three distinct `K_5` subgraphs force (3).  \(\square\)

## Published input

The external theorem used above is Theorem 1.10 of Jianbing Niu and Cun-Quan
Zhang, *Cliques, minors and apex graphs*, Discrete Mathematics 309 (2009),
4095--4107, DOI `10.1016/j.disc.2008.12.009`:

> If `k>=2` and a `(k+2)`-connected non-`(k-3)`-apex graph contains three
> `k`-cliques with pairwise intersections of order at most `k-2`, then it
> contains a `K_{k+2}` minor.

The same input and its exact `k=5` specialization are already recorded in
`results/hc7_global_literal_k5_transversal.md`.

## Exact contribution

The former five-clique intersection programme was unnecessary.  In a
hypothetical minor-minimal counterexample to the `K_7^-` intermediate
conjecture, **three** distinct literal `K_5` subgraphs are terminal.  Thus it
is enough to prove that at least eleven low-degree vertices lie in literal
`K_5` subgraphs, because two distinct `K_5` subgraphs cover at most ten
vertices.
