# Independent audit: endpoint-rigid Gallai--Edmonds collapse

**Verdict:** GREEN for the exact theorem revision audited.

## Audited revision

- theorem file:
  [`hc7_endpoint_rigid_gallai_exchange.md`](hc7_endpoint_rigid_gallai_exchange.md)
- SHA-256:
  `270f4cde346a861ce2cf92ca71157bf609ea3a40f46f0f078cfb13e490b99fc9`

The preceding active revision had SHA-256
`b0bf03a54187e0c588d6e3ae33c7c7f6d333e97bf3633c00cda21b9062794c6c`.
The promoted theorem changes only its opening status paragraph and final
audit-status paragraph.  Replacing those two metadata blocks by their exact
pre-promotion text reproduces the preceding hash.  The theorem statement,
hypotheses, proof, displayed branch sets, and mathematical limitations are
unchanged.

This is an independent internal mathematical audit, not external peer
review.  It reconstructs the Gallai--Edmonds case analysis, checks every
displayed minor model and its support order, independently verifies the
small-support exclusion for the theta graph joined to two independent
universal vertices, and checks the contraction from the two open sides of
the separation back to the quotient.

The theorem proves a boundary-structure and branch-set-interaction result.
It does not perform the remaining exchange between the two branch sets that
meet one open side, and it does not prove `HC_7`.

## 1. Inputs and complement notation

For a specified edge `uv`, collective adjacency to the three-clique `K`
means that the two sets

\[
        N_F(u)\cap K,\qquad N_F(v)\cap K
\]

are disjoint.  Endpoint-contact rigidity makes both sets nonempty.  Thus
display (1.2) follows exactly from Conditions 4 and 5.

The use of Condition 5 has a precise trust boundary.  It is supplied in the
full five-support star configuration by the separately audited endpoint-
contact theorem.  It is not claimed to follow from an arbitrary
eight-vertex graph satisfying Conditions 1--4 alone.

Contracting two connected, anticomplete open sides which are each adjacent
to every boundary vertex produces two nonadjacent vertices complete to the
boundary.  Hence the quotient is exactly `I_2 \vee J`; if the host has no
`K_7` minor, neither does this quotient.

The four Gallai--Edmonds types in (3.2) are the exact output of the linked,
separately audited canonical boundary theorem.  The proof uses only the
standard Gallai--Edmonds facts listed in lines 103--106 after that reduction.

## 2. Lifting a small boundary model

If a `K_5`-minor model in `J` uses at most seven of the eight boundary
vertices, an unused vertex `w` exists.  If `p,q` are the two vertices of
`I_2`, then

\[
       B_1,\ldots,B_5,\{p,w\},\{q\}
\]

are disjoint and connected.  The first five branch sets retain their old
adjacencies; `p` and `q` are each complete to every old branch set; and the
edge `wq` supplies the adjacency between the last two branch sets.  Lemma
2.1 and its support bound are therefore correct.

## 3. Gallai--Edmonds alternatives

### Type `(0,4)`

The four specified endpoints induce a connected cycle in `F`.  With
`A=emptyset`, it lies in one component of `F[D]` or one component of
`F[C]`.  The two distinct `K`-neighbours of one specified edge lie in the
same component.  A `D`-component would therefore have order at least six
and hence odd order at least seven, leaving three further nonempty
`D`-components.  A `C`-component would have order at least six, leaving
four nonempty `D`-components.  Both counts exceed eight.  Case 1 is valid.

### Type `(1,3)`

If the unique `A`-vertex is not specified, at least one of the two distinct
`K`-neighbours of `a,b` lies outside `A` and joins their `F`-component.  A
component in `C` consequently has even order at least six, which is too
large after counting `A` and the three `D`-components.

If the component lies in `D` and the `A`-vertex is not in `K`, both
distinct neighbours lie in it.  Its odd order is at least seven, again too
large.  The only remaining placement is therefore

\[
 A=\{r_0\}\subseteq K,
 \qquad C=\varnothing,
 \qquad |H|=5,
\]

with two singleton `D`-components.  The five-vertex component is
`{a,b,c,d,r}`.  Any `F`-neighbour in the third vertex of `K` would join
that vertex to `H`, so each specified edge has missing-contact sets
`{r_0}` and `{r}`.  Orient one edge `uv` so that
`ur_0,vr in E(F)`.  Then

\[
                    r_0-v-u-r-r_0
\]

is a cycle in `J`: `r_0v` and `ur` follow from disjointness of the two
missing-contact sets, `uv` is specified, and `rr_0` lies in the clique
`K`.  The displayed model (3.7) is valid:

\[
       \{r_0,r\},\quad\{u\},\quad\{v\},
       \quad\{z_1\},\quad\{z_2\}.
\]

The first set is connected through `r_0r`; it is adjacent to `u` through
`ru` and to `v` through `r_0v`; and `uv` is an edge.  Each singleton
`D`-component is complete in `J` to the five-vertex `D`-component, so it
is adjacent to the first set through `r` and to `u,v`; the two singleton
components are also adjacent in `J`.  The support order is six.

If the `A`-vertex is a specified endpoint, the other three endpoints and
the two distinct `K`-neighbours of the intact specified edge force one
five-vertex `D`-component and two singleton components.  In (3.9), if
`c rho_c,d rho_d in E(F)`, then collective adjacency gives
`d rho_c,c rho_d in E(J)`, while `cd` and `rho_c rho_d` are also edges of
`J`.  Hence (3.9) is a four-cycle.  The connected set `{c,d}` and the two
`K`-singletons form a triangle minor, and the two singleton `D`-components
extend it to the support-six model (3.10).  Case 2 is complete.

### Type `(2,4)`

A vertex of `C` together with one representative of each `D`-component
would induce a `K_5` in `J`, so `C` is empty.  The four odd component
orders of the six-vertex set `D` are therefore `3,1,1,1`.

With no specified endpoint in `A`, the connected four-cycle cannot fit in
a three-vertex component.  With exactly one specified endpoint in `A`,
the remaining three endpoints form an `F`-path.  At most one of the two
distinct `K`-neighbours of the intact edge is the other `A`-vertex, so the
path's `D`-component has at least four vertices.  This is the correct
count and already contradicts the component orders.

If `A` is one whole specified edge, the other edge and its two distinct
`K`-neighbours either occupy at least four vertices in one component or
force two odd components of order at least three; both alternatives are
impossible.  In the remaining placement, the two mates `u,v` lie with a
vertex `r in K` in the unique three-vertex component, and the other
components are the singletons `r'`, `r''`, and `x`.  Since `ur in E(F)`,
the mate `u' in A` satisfies `u'r in E(J)`.  In model (3.14), the first
four singleton vertices lie in four distinct `D`-components and induce a
`K_4`; `{u',r}` is connected, meets `{u}` through `u'u`, and meets the
other three sets through `r`.  Its support order is six.  Case 3 is valid.

### Type `(0,2)`

If the specified four-cycle lies in `C`, its two distinct `K`-neighbours
force `|C|=6` and two singleton `D`-components.  The edges in (3.15) form
a four-cycle by the same disjoint-missing-contact argument.  The connected
set `{a,b}`, the two `K`-singletons, and the two singleton `D`-components
are exactly the support-six `K_5` model in (3.16).

Therefore the specified cycle lies in a `D`-component.  It and two
distinct `K`-neighbours occupy at least six vertices, so factor-criticality
makes its order at least seven.  Counting the second component gives
`A=C=emptyset` and component orders seven and one.  The singleton cannot
be a specified endpoint.  If it were `x`, it would be universal in `J`.
Every pair of branch sets in (3.17) is adjacent:

- the three `r_i` are pairwise adjacent;
- `{a,b}` meets each `r_i` by collective adjacency;
- `{p,y}` meets `{q}` through `yq`;
- `p` or `q` supplies all their adjacencies to the old boundary sets; and
- the universal vertex `x` meets every other branch set.

Thus (3.17) is a `K_7`-minor model, so the isolated vertex belongs to `K`
and `x` belongs to the seven-vertex component.  Theorem 3.1 is proved.

## 4. The theta graph and support at most six

Because the isolated vertex `s` has no `F`-neighbour, no missing-contact
set contains it.  On the remaining two vertices `r_1,r_2`, each pair of
nonempty disjoint missing-contact sets must consist of the two complementary
singletons.  Together with the specified edges, the absence of all edges
between their endpoint pairs, and the edge `r_1r_2`, these are all possible
edges of `J[B]`.  Thus Lemma 4.1 gives exactly the claimed theta graph, not
merely a spanning theta subgraph.  It is triangle-free.

A `K_5`-minor model has support order at least five.  At support order five
all branch sets are singletons.  At support order six exactly one branch
set has two vertices and is an edge, while the other four are singleton
branch sets inducing a `K_4`.

For support five, using zero or one of `p,q` would require respectively a
`K_5` or `K_4` in the triangle-free graph `J[B]`; using both would require
the absent edge `pq`.  For support six:

- using neither `p,q` requires a `K_4` in `J[B]`;
- using exactly one as a singleton leaves a triangle among the other
  singleton vertices;
- using exactly one in the two-vertex branch set leaves a `K_4` among the
  singleton vertices; and
- using both forces one to be a singleton and the other into an edge branch
  set `{p,w}` or `{q,w}`, leaving a triangle among the remaining three
  singleton vertices.

The two vertices cannot themselves be the two-vertex branch set because
`pq` is absent.  These cases are exhaustive, so Theorem 4.2 is correct.

As a computational falsification check independent of the proof, an
exhaustive labelled enumeration considered all 18,432 boundary graphs
satisfying Conditions 1--5, including all 128 possible adjacency patterns
at `x`.  Of the 1,176 complements without a perfect matching, every graph
of type `(1,3)`, every graph of type `(2,4)`, and every type `(0,2)` graph
with two singleton `D`-components had a `K_5`-minor model in `J` supported
on at most seven vertices.  Only type `(0,2)` with component orders `7,1`
survived that test.  A separate exhaustive branch-set check on the theta
join found no support-five or support-six `K_5` model (support seven is
possible).  These computations are corroboration only; no finite search is
used in the written proof.

## 5. Quotient-to-host implication

Let a `K_5` model in `G-{s,x}` of support order at most six meet each open
side in at most one branch set.  If a branch set meets an open side, its
union with the entire connected side remains connected and is disjoint
from every other branch set; if no branch set meets the side, it remains
unused.  Enlarging in this way preserves every old adjacency.

Afterward, contracting each open side either occurs wholly inside one
branch set or outside every branch set.  It therefore preserves all five
branch-set labels and cannot increase the support order.  The result is a
support-at-most-six `K_5` model in `Q-{s,x}`, contradicting Theorem 4.2.
The argument also permits the same branch set to meet both open sides.

The equality

\[
                   \max_{|P|=2}\mu_G(P)=6
\]

implies `mu_G({s,x})<=6`, so such a response model exists.  Corollary 5.1
therefore follows, and its stronger wording "every support-at-most-six
model" is justified.

## 6. Exact scope

The audited result leaves a concrete labelled problem: at least one open
side meets two distinct branch sets of every small response model.  The
proof does not show how to split or reroute that side while retaining the
five branch-set labels.  It consequently proves none of the three outcomes
listed in lines 477--480 and does not close the maximal-pair support-height
exchange or `HC_7`.
