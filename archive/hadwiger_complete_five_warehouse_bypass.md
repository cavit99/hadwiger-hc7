# Complete five-warehouse bypass and the collective-contact boundary

## 1. The complete-contact cell closes

### Theorem 1.1 (connected-exterior warehouse bypass)

Let `C,X` be disjoint vertex sets in a graph `G`, with

\[
                         |C|=m,\qquad |X|=m+2,
\]

and assume every vertex of `C` is adjacent to every vertex of `X`.
If one component of `G-C` contains two vertices of `X`, then `G`
contains a `K_{m+2}` minor.

#### Proof

Choose a shortest path `P` in that component whose distinct ends
`u,v` belong to `X`.  Its interior avoids `X`; otherwise the subpath
between consecutive `X`-vertices is shorter.  Enumerate

\[
             C=\{c_1,\ldots,c_m\},\qquad
             X-\{u,v\}=\{x_1,\ldots,x_m\}.
\]

For `1<=i<=m`, put `D_i={c_i,x_i}`.  These bags are connected, and
`D_i` sees `D_j` through `c_ix_j`.  Split `P` at one edge into adjacent
connected sets `R,S`, with `u in R` and `v in S`.  The endpoint `u`
is adjacent to every `c_i`, so `R` sees every `D_i`; the endpoint `v`
does the same for `S`.  Thus

\[
                         D_1,\ldots,D_m,R,S
\]

are `m+2` disjoint connected pairwise adjacent branch sets.  QED.

### Corollary 1.2 (uniform connectivity form)

Every `(m+1)`-connected graph containing `K_{m,m+2}` as a subgraph
contains a `K_{m+2}` minor.

#### Proof

Deleting the `m`-vertex side leaves a connected graph, so Theorem 1.1
applies.  QED.

At `m=5`, every seven-connected graph containing the complete-contact
five-warehouse cell has a `K_7` minor.  This is stronger than the
requested operation-sensitive conclusion: neither criticality nor a
proper-minor state is needed.  The false-twin warehouse
`P_5 vee overline{K_7}` survives only at connectivity five, because
deleting its protected path leaves all seven targets isolated.

## 2. Why collective fullness is a different theorem

Theorem 1.1 uses literal complete bipartite contact.  It is false if
“`C` is full to `X`” means only that every `x in X` has at least one
neighbour somewhere in `C`.

The coherent two-apex survivor from
`hadwiger_exact_seven_two_gate_boundary_threshold.md` gives an exact
warning.  Let `I` be the icosahedron, let `u,v` be an adjacent universal
pair, and put `G_0=I vee K_2`.  In the standard NetworkX labelling take

\[
 C=N_I(0)=\{1,5,7,8,11\}
\]

and

\[
 X=\{0,2,4,6,9,10,u\}.
\]

Every vertex of `X` has a neighbour in `C`; the contact profiles in `I`
are

\[
\begin{array}{c|c}
0&1,5,7,8,11\\
2&1,8\\
4&5,11\\
6&1,5\\
9&7,8\\
10&7,11
\end{array}
\]

and `u` is complete to `C`.  The graph is seven-connected and has no
`K_7` minor, while deleting `u,v` leaves the planar icosahedron.

Thus the collective-contact version must retain the coherent two-apex
outcome.  The distinction is structural: in the complete cell, the five
paired bags `\{c_i,x_i\}` are automatically pairwise adjacent; under
collective contact, a matching between `C` and five targets does not
supply the cross-adjacencies between different paired bags.

## 3. Feed into `HC_7`

In the normalized near-`K_7` programme, a five-vertex protected carrier
with seven **complete** target rows is now eliminated immediately by
Theorem 1.1.  Hence a hypothetical counterexample can retain such a
carrier only if at least one target row is spatially deficient inside
the carrier.

The exact remaining operation-sensitive statement is consequently the
collective-contact version:

* proper-minor private contacts either repair the deficient rows enough
  to obtain the complete/paired branch-set construction; or
* their failures force the cyclic contact profiles to share one rural
  rotation, yielding the coherent two-apex outcome.

The icosahedral profiles above show that the second alternative is real;
it cannot be deleted from the theorem.  What has been closed is the
entire complete-contact warehouse family at arbitrary internal order,
not merely a finite path case.

