# Endpoint-contact rigidity at the exact order-eight boundary

**Status:** written proof with a separate GREEN internal audit in
[`hc7_star_order_eight_endpoint_contacts_audit.md`](hc7_star_order_eight_endpoint_contacts_audit.md).
This theorem eliminates an unbounded subfamily of the exceptional
order-eight output.  It does not eliminate the whole five-support star
branch or prove Hadwiger's conjecture for `t=7`.

## 1. Setup

Let `G` be a seven-connected graph with no `K_7` minor.  Let

\[
                         L=R\mathbin{\dot\cup}\{\ell_e,\ell_f\}
\]

be a five-clique, where `|R|=3`.  Let `e` and `f` be vertex-disjoint
edges outside `L` such that

1. `e` is anticomplete to `ell_e` and collectively adjacent to
   `L-{ell_e}`;
2. `f` is anticomplete to `ell_f` and collectively adjacent to
   `L-{ell_f}`; and
3. `e` and `f` are anticomplete to one another.

Assume that `G-L` contains a five-clique `Y` disjoint from `L`.  These are
the labelled objects supplied by the five-support star reduction and its
exact order-eight branch.

An **actual order-seven separation** means a separation with both open
sides nonempty and separator order seven.

## 2. Endpoint-contact theorem

### Theorem 2.1

If one endpoint of `e` or one endpoint of `f` is adjacent to all three
vertices of `R`, then `G` contains a `K_7` minor or has an actual
order-seven separation.

Consequently, in the branch with neither of those outcomes, every endpoint
of each of `e,f` is nonadjacent to at least one vertex of `R`.  For either
edge, the two endpoint nonneighbour sets in `R` are then nonempty and
disjoint.  Up to exchanging its endpoints, its incidence with `R` has one
of the two forms

\[
                         (1,1)\quad\hbox{or}\quad(1,2),       \tag{2.1}
\]

where the entries are the orders of the two endpoint nonneighbour sets.

### Proof

By symmetry suppose `e=aa'` and `a` is adjacent to every vertex of `R`.
Write `f=bb'`.  Since `f` is collectively adjacent to each of the three
vertices of `R`, the two sets

\[
 M(b)=\{r\in R:br\notin E(G)\},\qquad
 M(b')=\{r\in R:b'r\notin E(G)\}
\]

are disjoint.  Choose the names so that `|M(b)|<=1`.

Construct three pairwise disjoint connected row sets indexed by `R`.
If `M(b)` is empty, put `W_r={r}` for every `r in R`.  If
`M(b)={r_0}`, put

\[
               W_{r_0}=\{r_0,b'\},\qquad
               W_r=\{r\}\quad(r\ne r_0).                  \tag{2.2}
\]

The exceptional set in (2.2) is connected: collective adjacency of `f`
to `r_0`, together with `br_0` being absent, forces `b'r_0` to be an
edge.  Let

\[
                         W=\bigcup_{r\in R}W_r.              \tag{2.3}
\]

Thus `|W|` is three or four.  The three row sets are pairwise adjacent
because `R` is a clique.  Each is adjacent to each of

\[
                         \ell_e,\ \ell_f,\ a,\ b.            \tag{2.4}
\]

For the two leaf vertices this follows from the clique `L`.  The vertex
`a` is adjacent to every vertex of `R` by hypothesis.  The vertex `b` is
adjacent directly to every row except possibly `W_{r_0}`, and in that row
the edge `bb'` supplies the adjacency.

Put `K=G-W`.  If `K` has a `K_4` minor rooted at the four vertices in
(2.4), its four rooted branch sets together with the three row sets
`W_r` are seven pairwise disjoint, pairwise adjacent connected subgraphs.
They form an explicit `K_7`-minor model in `G`.  We may therefore assume
that this rooted `K_4` does not exist.

Suppose `K` has a vertex cut `X` of order at most `7-|W|`.  Deleting
`W union X` from `G` leaves the distinct nonempty components of `K-X`, so
it is an actual separator of order at most seven.  Seven-connectivity
excludes order at most six, while order seven is one of the theorem's
conclusions.  In the remaining branch `K` is therefore

\[
                         (8-|W|)\text{-connected},           \tag{2.5}
\]

and in particular is four-connected.

Apply Theorem 6 of Fabila-Monroy and Wood, *Rooted K4-Minors*.  Since the
rooted minor is absent, `K` is planar and the four nominated vertices lie
on a common face.

On the other hand, `K` contains a literal four-clique.  Indeed, `Y` is
disjoint from `R`, and the only possible additional vertex of `W` is
`b'`.  Thus at most one vertex of the five-clique `Y` was deleted.

A four-connected planar graph containing a literal `K_4` must equal that
`K_4`: in a plane embedding, every component outside the clique lies in
one of its four triangular regions and is separated from the opposite
clique vertex by the bounding triangle.  But `K` cannot equal `K_4`.
Its four distinct nominated vertices would then themselves form the
excluded rooted `K_4` (and, equivalently, a four-vertex graph is not
four-connected under the convention used by the cited theorem).  This
contradiction proves the first assertion.

For the consequence, collective adjacency says that the two endpoint
nonneighbour sets of either edge are disjoint.  In the surviving branch
Theorem 2.1 makes both nonempty.  Two nonempty disjoint subsets of a
three-set have orders `(1,1)` or `(1,2)` up to exchange.  This proves
(2.1). \(\square\)

## 3. Exact contribution

The theorem converts a qualitative portal-placement problem into a sharp
incidence restriction: every surviving endpoint has a genuine missing
contact in the three-clique, and the two endpoints of each distinguished
edge split those missing contacts without overlap.  It uses the second
literal five-clique to eliminate the planar rooted-minor obstruction; no
colour-state synchronization or finite boundary enumeration is used.

The remaining `(1,1)` and `(1,2)` incidence forms are not eliminated here.
In those forms, choosing one endpoint from each edge and absorbing its mate
into the unique missed row deletes five vertices before the rooted-
`K_4` test, so only three-connectivity remains.  The resulting web
obstruction is the next label-preserving exchange problem.
