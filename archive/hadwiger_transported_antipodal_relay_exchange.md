# The transported antipodal row has a crossed-relay exchange

## 1. Setting

Use the transported degree-eight setting of
`hadwiger_transported_degree8_leaf_closure.md`.  Assume the only remaining
row: `P` contains an antipodal matching edge of the old triangular prism
and is not contained in an old-boundary four-clique.

Write the prism triangles as

\[
 \{a,a_1,a_2\},\qquad \{b,b_1,b_2\},
\]

with matching edges `ab,a_1b_1,a_2b_2`, and let `z` be the universal
old-boundary vertex.  Then

\[
                 \{a,b\}\subseteq P\subseteq\{a,b,z\}. \tag{1.1}
\]

For each `s in S-P`, `y_s` is the private relay with `sy_s` an edge.
The residual component `R` is nonempty, connected, and misses at most
one vertex `m` of `U=N(u)`.

For `i=1,2`, choose

\[
 t_i\in\{y_{a_i},y_{b_i}\},\qquad
 X_i=\{a_i,b_i,t_i\}.                              \tag{1.2}
\]

Each `X_i` is connected and meets `U`.  The four bags
`\{a\},\{b\},X_1,X_2` are pairwise adjacent, using the two prism
triangles and their matching edges.

## 2. Closure

### Theorem 2.1 (antipodal-row closure)

Every transported antipodal two-shore cell contains a `U`-meeting
`K_6`-model in `G-u`, and hence a `K_7`-minor in `G`.

### Proof

First suppose `z in P`, so `P=\{a,b,z\}`.  Add the singleton `\{z\}`
to the four bags above; these five bags form a `K_5`.  Choose each `t_i`
to avoid the possible defect `m`.

If `m in P`, fullness of `D-u` and the fact that `R` misses `m` give
an edge `mr` for some

\[
                   r\in\{w\}\cup\{y_s:s\in S-P\}. \tag{2.1}
\]

Choose the `t_i` also to avoid `r` (each pair in (1.2) has two choices),
and add `r` to `R`.  If `m notin P` (or there is no defect), add to `R`
any unused vertex of `U-P` different from `m`.  There are five vertices
in `U-P`, only two are used as `t_1,t_2`, and at most one is forbidden.
The resulting sixth bag is connected, meets `U`, sees both `X_i` through
`R-t_i`, and sees every singleton; the possible missing singleton is
repaired by `mr`.

Now suppose `P=\{a,b\}`.  Start with the five bags

\[
 \{a\},\quad\{b\},\quad\{z,y_z\},\quad X_1,\quad X_2. \tag{2.2}
\]

They form a `K_5` and all meet `U`.  If `m` is absent or is outside
`\{a,b,y_z\}`, choose `t_1,t_2` to avoid it and add any unused vertex
seen by `R`; then `R` is the sixth bag.

If `m=y_z`, the only neighbours of `y_z` outside `U` are `u,z`:
`R` misses `y_z`, `H` is anticomplete to `D`, and every other
old-boundary vertex of `S-P` has its own unique `D`-portal.  Hence
minimum degree gives `d_{G[U]}(y_z)>=5`.  Of the seven possible neighbours
in `U`, only `a,b,t_1,t_2` are committed to other bags, so an uncommitted
neighbour `r` exists.  Add `r` to `R`; `ry_z` repairs its adjacency to
the third bag in (2.2).

Suppose next that `m=a` or `m=b`; by symmetry take `m=a`.  Fullness of
`D-u` gives a neighbour of `a` in
`\{w\} union \{y_s:s in S-P\}`.  If one such neighbour `r` is not
`y_z`, choose `t_1,t_2` to avoid `r` and add `r` to `R`.  Again (2.2)
plus this sixth bag is the desired model.

The sole subcase left is the exact lock

\[
 N_{D-u}(a)=\{y_z\},\qquad U-N_U(R)=\{a\}.          \tag{2.3}
\]

Use instead the six bags

\[
\begin{array}{lll}
 B_1=\{a\},&B_2=\{b\},&B_3=\{z,a_1,y_{a_1}\},\\
 B_4=\{a_2,b_2,y_{a_2}\},&
 B_5=H\cup\{b_1,y_{b_1}\},&
 B_6=R\cup\{y_z\}.
\end{array}                                         \tag{2.4}
\]

They are disjoint and connected, and each meets `U`.  The prism and `z`
make `B_1,B_2,B_3,B_4` pairwise adjacent.  Fullness of `H` makes `B_5`
adjacent to each of those four.  The edge `ay_z` and the fact that `R`
sees `b,y_{a_1},y_{a_2},y_{b_1}` make `B_6` adjacent respectively to
`B_1,B_2,B_3,B_4,B_5`; for `B_3` one may also use `zy_z`.  Thus (2.4)
is a `U`-meeting `K_6`-model.  The case `m=b` is symmetric.

All defect positions have been covered.  Add `\{u\}` to obtain `K_7`.
QED.

## 3. Consequence

Together with `hadwiger_transported_locked_relay_exchange.md`, this
eliminates every two-exterior transported tight-hub-leaf row.  The
sole-exterior rows were already eliminated by Theorem 3.1 of
`hadwiger_transported_degree8_leaf_closure.md`.  Hence a tight leaf of
the full-deletion hub graph cannot occur in a hypothetical minimal
counterexample.
