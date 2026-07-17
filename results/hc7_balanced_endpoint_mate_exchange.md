# Endpoint-mate exchange at the balanced order-eight boundary

**Status:** written proof with a separate GREEN internal audit in
[`hc7_balanced_endpoint_mate_exchange_audit.md`](hc7_balanced_endpoint_mate_exchange_audit.md).
This note isolates the exact endpoint obstruction left by the elementary branch-set
allocation in the balanced order-eight configuration.  It does not produce
the crossed two-path linkage and does not prove `HC_7`.

## 1. Setup

Let `G` have an eight-vertex separator

\[
 S=R\mathbin{\dot\cup}V(e)\mathbin{\dot\cup}V(f)
       \mathbin{\dot\cup}\{x\},\qquad |R|=3,
\]

such that the following hold.

1. `R` is a clique.
2. `e,f` are disjoint anticomplete edges, each collectively adjacent to
   every vertex of `R`.
3. `G-S` has exactly two connected components `C,D`, and each is adjacent
   to every literal vertex of `S`.
4. The component `C` contains adjacent vertices
   `ell_e,ell_f`, both complete to `R`.
5. The edge `e` is anticomplete to `ell_e` and has a neighbour at
   `ell_f`; symmetrically, `f` is anticomplete to `ell_f` and has a
   neighbour at `ell_e`.
6. The graph

   \[
                         H=C-\{\ell_e,\ell_f\}
   \]

   is connected, is met by each of `ell_e,ell_f,x`, and has a neighbour
   in each of `V(e),V(f)`.
7. Every endpoint of `e` and `f` has a nonempty set of nonneighbours in
   `R`, and the two endpoint nonneighbour sets belonging to either one
   of the edges are disjoint.

Put

\[
                         \lambda_e=\ell_f,
                 \qquad \lambda_f=\ell_e.
\]

Thus `lambda_q` is the clique vertex which has a neighbour in the defect
edge `q`.  For `q in {e,f}` define

\[
\begin{aligned}
 I_q&=\{z\in V(q):N_H(z)\ne\varnothing\},\\
 L_q&=\{z\in V(q):z\lambda_q\in E(G)\},\\
 O_q&=\{z\in I_q:\overline z\in L_q\},
\end{aligned}                                           \tag{1.1}
\]

where `overline z` denotes the other endpoint of `q`.  A vertex in `O_q`
is an endpoint which can be put into the branch set containing `H`, while
its mate can be put with `lambda_q`.

Finally define the set of clique vertices missed by the prospective
`H`-branch set before endpoint repair:

\[
       M=\{r\in R:N_G(r)\cap(V(H)\cup\{x\})=\varnothing\}.
                                                               \tag{1.2}
\]

In the current balanced branch, the promoted shared-missing-contact result
gives `M nonempty`, while the fact that `H` misses at most two boundary
vertices gives `|M|<=2`.

## 2. The endpoint allocation

### Lemma 2.1 (an interior-facing mate exists on each edge)

For each `q in {e,f}`,

\[
                       I_q\cup L_q=V(q)
             \quad\text{and}\quad O_q\ne\varnothing.       \tag{2.1}
\]

#### Proof

Consider `q=e`; the other edge is symmetric.  Every endpoint of `e` has
a neighbour in `C`, because `C` is adjacent to every literal vertex of
`S`.  Its possible neighbours in `C` lie in

\[
                   V(H)\cup\{\ell_e,\ell_f\}.
\]

The edge `e` is anticomplete to `ell_e`, so such a neighbour lies in `H`
or is `ell_f=lambda_e`.  This proves `I_e union L_e=V(e)`.  Both sets are
nonempty by hypotheses 5 and 6.

Write `V(e)={u,v}` and suppose `O_e` were empty.  Choose `u in I_e`.
Then `v notin L_e`, so (2.1) puts `v in I_e`.  Applying the definition of
`O_e` to `v` now gives `u notin L_e`.  Thus `L_e` is empty, a
contradiction.  Hence `O_e` is nonempty. \(\square\)

### Theorem 2.2 (endpoint-mate completion)

If there are `z_e in O_e` and `z_f in O_f` such that

\[
        M\subseteq N_R(z_e)\cup N_R(z_f),                  \tag{2.2}
\]

then `G` contains a `K_7` minor.

#### Proof

Put `u_e=overline z_e` and `u_f=overline z_f`.  Consider the following
seven vertex sets:

\[
 \{r\}\ (r\in R),\qquad
 \{\lambda_e,u_e\},\qquad
 \{\lambda_f,u_f\},\qquad
 V(H)\cup\{x,z_e,z_f\},\qquad
 V(D).                                                     \tag{2.3}
\]

They are pairwise disjoint.  They are connected: `u_q lambda_q` is an
edge because `z_q in O_q`; each of `x,z_e,z_f` has a neighbour in the
connected graph `H`; and `D` is connected.

Here is a check of all twenty-one branch-set adjacencies.  The three
`R`-singletons give three adjacencies.  Each such singleton is adjacent

- to `{lambda_e,u_e}` through `lambda_e`,
- to `{lambda_f,u_f}` through `lambda_f`,
- to `H union {x,z_e,z_f}` either through `H union {x}` or, for a vertex
  of `M`, through (2.2), and
- to `D` by boundary fullness.

These are twelve further adjacencies.  Among the remaining four branch
sets, the six adjacencies are witnessed as follows:

- the two leaf-and-endpoint sets meet through the edge
  `lambda_e lambda_f`;
- each leaf-and-endpoint set meets the `H`-set through a
  `lambda_q`--`H` edge;
- each leaf-and-endpoint set meets `D` through the boundary vertex `u_q`;
- the `H`-set meets `D` through the boundary vertex `x`.

Thus the seven sets in (2.3) are pairwise adjacent connected branch sets
and form a `K_7`-minor model. \(\square\)

## 3. Exact failure patterns

Assume for this section that `G` is `K_7`-minor-free.  For
`z in O_q`, write

\[
                         T(z)=N_R(z)\cap M.             \tag{3.1}
\]

Theorem 2.2 says

\[
       T(z_e)\cup T(z_f)\ne M
       \quad\text{for every }z_e\in O_e, z_f\in O_f.  \tag{3.2}
\]

### Theorem 3.1 (classification of the endpoint lock)

Suppose `1<=|M|<=2`.

1. If `M={r}`, then `O_e` and `O_f` are singletons.  Their two members
   both miss `r`, and their two mates both see `r`.
2. If `M={r,s}`, exactly one of the following holds.
   - Both `O_e` and `O_f` are singletons, and their members have a common
     nonneighbour in `{r,s}`.
   - After possibly interchanging `e` and `f`, `O_e=V(e)`.  Its two
     members have traces `{r}` and `{s}` in some order, while
     `O_f={z_f}` and `T(z_f)=emptyset`.  If `t` is the third vertex of
     `R`, then `z_f` is adjacent in `R` precisely to `t`, and its mate is
     adjacent in `R` precisely to `r,s`.

#### Proof

For either defect edge `q`, collective adjacency to every vertex of `R`
implies

\[
             \bigcup_{z\in V(q)}T(z)=M.                \tag{3.3}
\]

First let `M={r}`.  If `O_q=V(q)` for either `q`, then (3.3) gives a
member of `O_q` adjacent to `r`.  Together with an arbitrary member of
the other nonempty `O`-set, this contradicts (3.2).  Hence both `O`-sets
are singletons.  Equation (3.2) says that their members miss `r`.
Collective adjacency of each defect edge to `r` says that their mates see
`r`.

Now let `M={r,s}`.  If both `O`-sets are singletons, (3.2) says exactly
that the two selected endpoints fail together to cover `{r,s}`.  Hence
one of `r,s` is a common nonneighbour, giving the first alternative.

It remains to consider an `O`-set of order two; after interchanging the
edges, let `O_e=V(e)`.  The two traces belonging to `e` cover `M` by
(3.3).  Neither trace can equal `M`, since that endpoint alone would
contradict (3.2).  The only possibility is therefore that the two traces
are the complementary singletons `{r}` and `{s}`.

The set `O_f` cannot also have order two.  Indeed, an endpoint of `f`
which sees `r` could be paired with the endpoint of `e` which sees `s`,
and similarly with the roles reversed; (3.3) guarantees one of these
choices.  Thus `O_f={z_f}`.  If `z_f` saw either `r` or `s`, pairing it
with the endpoint of `e` which sees the other vertex would again violate
(3.2).  Hence `T(z_f)=emptyset`.

The endpoint `z_f` misses `r,s`, so collective adjacency makes its mate
see both.  By hypothesis 7 the mate has a nonempty nonneighbour set in
`R`, disjoint from that of `z_f`.  It must consequently miss the third
vertex `t` and no member of `{r,s}`.  Disjointness then makes `z_f` see
`t`.  This gives the displayed exact neighbourhoods and completes the
classification. \(\square\)

The second outcome is a genuine switching obstruction: either endpoint
of one defect edge can repair one of the two missing clique contacts, but
choosing it prevents use of the other endpoint; the unique usable endpoint
of the other defect edge repairs neither contact.

### Corollary 3.2 (the forced-theta two-row residue)

Write `R={p,r,s}`.  Suppose that `p` is adjacent to every endpoint of
`e,f`, and that on each defect edge one endpoint is adjacent to `r` and
nonadjacent to `s`, while its mate is adjacent to `s` and nonadjacent to
`r`.  These are exactly the endpoint incidences in the forced-theta
outcome of the aligned cross-matching dichotomy.

If `|M|=2` and `G` is `K_7`-minor-free, then

\[
             |O_e|=|O_f|=|L_e|=|L_f|=1,              \tag{3.4}
\]

and every endpoint of `e,f` has a neighbour in `H`.

#### Proof

Because `H` misses at most two boundary vertices, `|M|=2` forces `H` to
have a neighbour at every endpoint of `e,f`.  Thus

\[
                         I_e=V(e),\qquad I_f=V(f).     \tag{3.5}
\]

The switching outcome in Theorem 3.1 would give an endpoint of one edge
which is nonadjacent to both members of `M`.  If `p in M`, this contradicts
the completeness of `p` to all four endpoints.  If `M={r,s}`, it
contradicts the theta incidence, under which every endpoint is adjacent to
exactly one of `r,s`.  Hence only the singleton outcome of Theorem 3.1 is
possible, and `|O_e|=|O_f|=1`.

When `I_q=V(q)`, the definition in (1.1) says that `O_q` is the image of
`L_q` under the fixed-point-free mate involution on `V(q)`.  Therefore
`|O_q|=|L_q|`.  Equation (3.4) follows. \(\square\)

## 4. What minimum degree adds

Suppose `G` is seven-connected.  Then every vertex has degree at least
seven.  If, in addition, `G` has no actual order-seven separation, every
vertex used below has degree at least eight: each leaf has nonneighbours
in one defect edge, and each defect endpoint has the two endpoints of the
other defect edge as nonneighbours.  If such a vertex had degree seven,
its open neighbourhood would be an order-seven separator isolating it
from one of those nonneighbours.

For `q in {e,f}`, the neighbours of `lambda_q` are partitioned exactly as

\[
 d_G(\lambda_q)
   =4+|L_q|+\mathbf 1_{x\lambda_q\in E(G)}
      +|N_H(\lambda_q)|.                                \tag{4.1}
\]

Here the initial four vertices are `R` and the other clique leaf; the
leaf is anticomplete to the other defect edge and has no neighbour in
`D`.  Thus seven-connectivity alone gives

\[
 |N_H(\lambda_q)|+|L_q|+
 \mathbf 1_{x\lambda_q\in E(G)}\ge3,                    \tag{4.2}
\]

while exclusion of an order-seven separation improves the right-hand
side to four.

For an endpoint `z in V(q)`, let

\[
                         k(z)=|R-N_R(z)|.
\]

Its neighbours split exactly into its mate, its `3-k(z)` neighbours in
`R`, possible neighbours `lambda_q,x`, and its neighbours in `H,D`.
Consequently

\[
 |N_H(z)|+|N_D(z)|+
 \mathbf 1_{z\lambda_q\in E(G)}+
 \mathbf 1_{zx\in E(G)}
 \ge 3+k(z),                                             \tag{4.3}
\]

and the right-hand side is `4+k(z)` when no actual order-seven
separation exists.

These inequalities are useful but do not force the crossed two-path
linkage.  In particular, for a locked endpoint `z in O_q`, (4.3) controls
only the sum of its contacts with `H` and the opposite component `D`.
All degree excess beyond the one required `H`-contact may lie in `D`.
For a leaf, (4.1) forces additional `H`-contacts whenever its boundary
contacts are not maximal, but those contacts may still lie on one side of
the canonical web obstruction.

In the actual balanced branch, the separately proved tight-core argument
gives `x lambda_q notin E(G)` for both leaves.  Under Corollary 3.2 and
the exclusion of an order-seven separation, (4.1) therefore gives

\[
                         |N_H(\lambda_q)|\ge3
              \qquad(q\in\{e,f\}).                    \tag{4.4}
\]

Thus the forced-theta lock has three distinct leaf entrances into `H` on
each side.  Their multiplicity still does not determine their order in the
canonical web.

## 5. Relation to the remaining linkage

Fix `z_e in O_e`.  If `C` contained vertex-disjoint connected subgraphs
joining

\[
     \lambda_e\text{ to a neighbour of }x,
     \qquad
     \lambda_f\text{ to a neighbour of }z_e,             \tag{5.1}
\]

then the promoted split-edge completion, with the second subgraph ending
at the endpoint `z_e of e`, would give a `K_7` minor.  The symmetric
statement holds for every `z_f in O_f`.  Hence a surviving lock forbids
these endpoint-labelled two-path systems as well as the coarser
same-index linkage.

The contribution of Theorems 2.2 and 3.1 is therefore exact: elementary
endpoint allocation closes every case except the singleton common lock
and the one switching lock in Theorem 3.1.  Equations (4.1)--(4.3) do not
by themselves eliminate either pattern.  Moreover, the separately written
canonical-web crossing theorem shows that, while the same rooted-web model
is retained, both two-path systems in (5.1) and its symmetric version join
alternating pairs on a disk and are topologically impossible.  A further
proof must therefore change the labelled model through a proper-minor
colouring transition, contradict the locked contact placement by a planar
degree or list-critical argument, or expose an actual order-seven
separation.  The displayed minimum-degree inequalities alone do not move
contacts from `D` into the required labelled paths in `H`.
