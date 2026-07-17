# Endpoint allocation at the balanced order-eight boundary

**Status:** written proof with a separate GREEN internal audit in
[`hc7_balanced_endpoint_allocation_audit.md`](hc7_balanced_endpoint_allocation_audit.md).
This note gives an explicit `K_7`-minor construction and characterizes the exact endpoint
obstruction when that construction fails.  It does not prove the remaining
two-path linkage and does not prove `HC_7`.

## 1. Setup

Let `G` contain an eight-vertex separator

\[
 S=R\mathbin{\dot\cup}A\mathbin{\dot\cup}B
       \mathbin{\dot\cup}\{x\},
 \qquad |R|=3,\quad |A|=|B|=2,
\]

with two connected open components `C,D`, each adjacent to every vertex of
`S`.  Suppose that:

1. `R` is a clique;
2. `A` and `B` induce edges, are anticomplete to one another, and each is
   collectively adjacent to every vertex of `R`;
3. `C` contains adjacent vertices `ell_A,ell_B`, both complete to `R`;
4. `ell_A` is anticomplete to `A` and has a neighbour in `B`, while
   `ell_B` is anticomplete to `B` and has a neighbour in `A`; and
5. the graph

   \[
                         H=C-\{\ell_A,\ell_B\}
   \]

   is connected and has a neighbour at each of `ell_A,ell_B,x` and in
   each of `A,B`.

For each of `A,B`, assume also that the two endpoint nonneighbour sets in
`R` are nonempty and disjoint.  This is the endpoint rigidity present in
the balanced order-eight branch.

Define the two nonempty sets of boundary vertices which can be joined
directly to the clique vertices by

\[
 A_L=N_G(\ell_B)\cap A,
 \qquad
 B_L=N_G(\ell_A)\cap B.                              \tag{1.1}
\]

Define

\[
 Z=\{z\in A\cup B:N_G(z)\cap V(H)\ne\varnothing\},
 \qquad
 U_H=\{r\in R:N_G(r)\cap V(H)=\varnothing\}.         \tag{1.2}
\]

Put

\[
 M=\{r\in U_H:xr\notin E(G)\}.                       \tag{1.3}
\]

Thus `Z` records exactly the defect-edge endpoints which may be absorbed
individually into the connected subgraph `H`.  The set `M` records exactly
the clique vertices whose adjacency to `H union {x}` must be supplied by
such an absorbed endpoint.

## 2. The endpoint-allocation completion

### Theorem 2.1

If there are `a in A_L` and `b in B_L` such that

\[
 \text{for every }r\in M\text{ there is }
 z\in Z-\{a,b\}\text{ with }rz\in E(G),              \tag{2.1}
\]

then `G` contains a `K_7` minor.

### Proof

Put

\[
 K=G\bigl[V(H)\cup\{x\}\cup(Z-\{a,b\})\bigr].       \tag{2.2}
\]

The graph `K` is connected: `H` is connected, `x` has a neighbour in
`H`, and every member of `Z` has a neighbour in `H`.  Consider the seven
vertex sets

\[
 \{r\}\ (r\in R),\qquad
 \{\ell_B,a\},\qquad
 \{\ell_A,b\},\qquad
 V(K),\qquad
 V(D).                                                \tag{2.3}
\]

They are pairwise disjoint and connected.  We check their adjacencies.
The three singleton sets form a clique.  Each clique vertex is adjacent
to both leaf-and-endpoint sets through `ell_A,ell_B`, and to `D` by the
boundary-fullness of `D`.  If `r notin U_H`, it has a neighbour in `H`.
If `r in U_H-M`, it is adjacent to `x`.  Finally, if `r in M`, condition
(2.1) gives a neighbour in `K`.  Hence every clique singleton is also
adjacent to `K`.

The two leaf-and-endpoint sets are adjacent through the edge
`ell_A ell_B`.  Each is adjacent to `K` through a leaf--`H` edge and to
`D` through its boundary endpoint.  Finally `K` is adjacent to `D`
through the boundary vertex `x`.  Thus all twenty-one required
adjacencies in (2.3) are present, and (2.3) is an explicit `K_7`-minor
model. \(\square\)

## 3. The exact obstruction to endpoint allocation

Assume now that `G` has no `K_7` minor and no actual order-seven
separation.  In the balanced order-eight branch the already proved
leaf-side theorem gives

\[
                         |N_G(H)\cap S|\ge 6,          \tag{3.1}
\]

and `x` has a neighbour in `H`.  The cross-matching normalization gives
at least one vertex of `R` missed by both `H` and `x`, so `M` is nonempty.
Since `H` misses at most two boundary vertices,
`M subseteq U_H` and `|U_H|<=2`.

For `r in M`, put

\[
                         T_r=Z\cap N_G(r).             \tag{3.2}
\]

### Theorem 3.1 (row-cover form of the obstruction)

Under these assumptions:

1. `|Z|>=2+|U_H|>=2+|M|`, and every `T_r` is nonempty;
2. the Cartesian product of the two possible leaf-anchor sets satisfies

   \[
    A_L\times B_L
       =\bigcup_{r\in M}
          \{(a,b)\in A_L\times B_L:
                         T_r\subseteq\{a,b\}\};       \tag{3.3}
   \]
3. in particular, at least one of `A_L,B_L` is a singleton; and
4. some endpoint `q` which belongs to one of the sets `T_r` is the unique
   neighbour of the corresponding clique vertex in its opposite defect
   edge.  The endpoint `q` also has a neighbour in `H`.

### Proof

The boundary neighbours of `H` are exactly

\[
       (R-U_H)\mathbin{\dot\cup} Z\mathbin{\dot\cup}\{x\}.
\]

Therefore (3.1) gives

\[
             3-|U_H|+|Z|+1\ge6,
\]

which is assertion 1's lower bound.  For a fixed `r in R`, at most one
endpoint of `A` and at most one endpoint of `B` can be nonadjacent to
`r`, because the two nonneighbour sets belonging to either edge are
disjoint.  Since `M` is nonempty, `|U_H|>=1` and hence `|Z|>=3`; at least
one member of `Z` is adjacent to `r`.
Thus every `T_r` is nonempty.

Fix `(a,b) in A_L times B_L`.  If no `r in M` satisfied
`T_r subseteq {a,b}`, then for every `r in M` there would be a member of
`T_r-{a,b}`.  This is precisely condition (2.1), and Theorem 2.1 would
give a `K_7` minor.  Hence (3.3) holds.

Suppose for a contradiction that `A_L=A` and `B_L=B`.  If `|M|=1`, the
nonempty set `T_r` is contained in at most two of the four pairs in
`A times B`, so it cannot cover the product in (3.3).  If `|M|=2`, then
`U_H=M`, and the bound in assertion 1 gives `Z=A union B`.  Collective
adjacency of each
edge to each member of `R` then makes every `T_r` contain at least one
endpoint from `A` and one from `B`.  Consequently each set on the
right-hand side of (3.3) contains at most one pair, so two such sets
cannot cover the four pairs.  This proves assertion 3.

It remains to prove assertion 4.  If `|M|=1`, then the nonempty set `T_r`
is contained in every pair of `A_L times B_L` by (3.3).  Any member of
`T_r` must therefore be the unique member of its corresponding anchor
set.

Suppose `|M|=2`.  Then `U_H=M`, `Z=A union B`, and each set `T_r` contains an
endpoint from each of `A,B`.  If both anchor sets are singletons, choose
any member of the nonempty `T_r` which witnesses their sole pair.  If,
say, `A_L={q}` and `B_L=B`, the two anchor pairs must be covered separately
by the two rows in (3.3).  Each covering `T_r` is then exactly
`{q,b}` for the relevant `b in B`.  In particular, `q` is in `Z`, lies
in a set `T_r`, and is the unique member of `A_L`.  The case with `A,B`
interchanged is identical.  Membership in `Z` gives the last assertion.
\(\square\)

Theorem 3.1 is a structural statement, not a finite boundary census.  It
says that failure of the explicit model (2.3) consumes every available
endpoint which can repair at least one missed clique contact.  At least
one such endpoint is forced to be the unique boundary contact of one
clique vertex.

## 4. Consequence in the forced theta boundary

The matching-alignment obstruction has the following standard-language
form.  Write `R={p,r,q}` and suppose:

1. `p` is adjacent in `G[S]` to all four vertices of `A union B`; and
2. on each of the edges `A,B`, one endpoint is adjacent to `r` and
   nonadjacent to `q`, while the other is adjacent to `q` and nonadjacent
   to `r`.

Equivalently, after deleting `{p,x}`, the six boundary vertices induce the
edge `rq` together with two internally disjoint length-three `r`--`q`
paths whose internal edges are `A` and `B`.  This is the forced theta
outcome of the aligned cross-matching dichotomy.

### Corollary 4.1

Assume the forced theta boundary and `|M|=2`.  If `G` has no `K_7` minor,
then

\[
                          |A_L|=|B_L|=1.              \tag{4.1}
\]

Moreover every endpoint of `A union B` has a neighbour in `H`.

### Proof

The inequality in Theorem 3.1 gives `|Z|>=4`, so
`Z=A union B`.  If `p in M`, then `T_p=A union B`, and therefore the row
`p` covers no pair in (3.3).  The other missed row contains exactly one
endpoint from each of `A,B`, so it covers at most one anchor pair.  Hence
`A_L times B_L` has order one.

It remains that `M={r,q}`.  In that case `T_r,T_q` are complementary
pairs, each containing one endpoint from each of `A,B`.  They have no
coordinate in common.  Each covers only its own pair in (3.3).  A
Cartesian product of order two consists of two pairs with one coordinate
in common, and a product of order four contains all four pairs.  Neither
can be covered by the two complementary pairs.  Again the product has
order one, proving (4.1).  The assertion about `H` is `Z=A union B`.
\(\square\)

### Corollary 4.2 (minimum-degree strengthening)

In a hypothetical minor-minimal counterexample to `HC_7`, continue under
Corollary 4.1 and exclude the earlier `K_7`-minor and order-seven exits.
Then each of `ell_A,ell_B` has at least three distinct neighbours in `H`.

### Proof

The graph has at least ten vertices because `S,C,D` are disjoint and both
open components are nonempty.  In a seven-connected graph every vertex
has degree at least seven.  A vertex of degree exactly seven would have an
order-seven neighbourhood separating it from a vertex outside its closed
neighbourhood, contrary to the excluded order-seven outcome.  Hence
`delta(G)>=8`.

The promoted tight-core argument shows that neither clique vertex is
adjacent to `x`.  The neighbours of `ell_B` outside `H` are therefore the
other clique vertex, the three vertices of `R`, and its unique neighbour
in `A`; it is anticomplete to `B` and to the opposite open component.
Thus

\[
                         d_H(\ell_B)=d_G(\ell_B)-5\ge3.
\]

The argument for `ell_A` is symmetric. \(\square\)

## 5. Exact remaining linkage

Let `A_L={a}` and `B_L={b}` in Corollary 4.1.  Both `a,b` have neighbours
in `H`.  If `C` contained disjoint connected subgraphs, one joining
`ell_B` to a neighbour of `x` and the other joining `ell_A` to a neighbour
of `a`, the promoted split-edge completion would give a `K_7` minor.  The
symmetric assertion holds with `A,B` interchanged.

Thus the forced-theta, two-missed-row residue is reduced to two explicit
prescribed two-path obstructions in one connected graph.  Corollary 4.2
adds at least three distinct entrances from each clique vertex into that
graph.  This
is stronger than the previous statement that the shore merely contacts
the two defect edges, but it does not force the disjoint paths: a
three-connected rooted web can still block an alternating terminal
pairing.  The next positive theorem must use the canonical cut rigidity or
the proper-minor colouring transitions to exclude that web.  Neither the
perfect matching nor minimum degree alone supplies the missing linkage.
