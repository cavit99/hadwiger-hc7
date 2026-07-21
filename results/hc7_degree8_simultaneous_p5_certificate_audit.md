# Independent audit: fixed-colouring `P_5` certificate theorem

**Verdict:** **GREEN** for every assertion of Theorem 1.1, including the
actual-defect interval criterion and its final residue, and for Corollary
6.1.  This is a separate internal mathematical cold audit, not external peer
review.  The result is nonterminal and proves neither `HC_7` nor a strict
same-form reduction.

## Exact revisions audited

```text
b5eef7914da4270ed39ec8276aa97d4dcfa666a232b8bd789a5cb5c9abfb489e  mathematical content before promotion
da00186a910c7ef9ffcc230bfbc0e45362b91ead74bb34b909022e8938e99d55  results/hc7_degree8_simultaneous_p5_certificate.md
```

The source was audited while its status paragraph still said that a separate
audit was pending.  The only later source change was the status link to this
audit, followed by path-only promotion beside it; neither alters the
mathematical verdict.  Any change to the theorem, proof, corollary, or trust
boundary requires renewed audit.

## 1. Star contraction and one fixed colouring

The set `Q` is independent and every member is adjacent to `u`, so the graph
on `{u} union Q` is a connected star.  Contracting it is a proper-minor
operation.  In a six-colouring of the contraction, expanding its image with
one colour `gamma` gives exactly a proper colouring of `G-E_G(u,Q)`: the
deleted star edges are the only edges made monochromatic, and every external
neighbour of the star image has another colour.

On restricting to `G-u`, all five vertices of `U` avoid `gamma`.  If any of
the five remaining palette colours were absent from `U`, that colour could be
assigned to `u`, contradicting the hypothesis that `G` is not
six-colourable.  Hence `U` receives those five colours bijectively.

For distinct `x,y in U`, a separation of `x,y` into different components of
their two-colour subgraph permits a Kempe interchange on the component of
`x`.  It does not move `y` or any member of `Q`, and it removes the original
colour of `x` from `U`.  Recolouring `u` with that absent colour again gives
a six-colouring of `G`.  This verifies the complete five-root routing claim
in the same fixed colouring.

## 2. Localized paths and the five-colour core

A bichromatic path between two roots cannot contain another member of `U`
internally, because the five roots have distinct colours, and it cannot
contain a member of `Q`, whose colour is `gamma`.  Since the path lies in
`G-u`, all of its internal vertices are outside `N_G[u]`.  Its interior is
connected when nonempty and therefore lies in one component of
`G-N_G[u]`.

The pairs `ea` and `bc` are nonedges, so their shortest paths have nonempty
interiors.  Their four root colours are distinct, making the two paths
vertex-disjoint.  Together with the literal edges `ab,cd`, they form exactly
the subdivision with rooted order `e,a,b,c,d`.

The `gamma` class `Gamma` is independent.  Removing it leaves a graph `X`
with the displayed five-colouring.  A four-colouring of `X`, a fifth colour
on `Gamma`, and a sixth colour on `u` would colour `G`, so `chi(X)=5`.

For an arbitrary proper five-colouring of `X`, if one colour were absent
from `U`, assign a new sixth colour to `Gamma` and the absent colour to `u`.
This is proper because

```text
Gamma intersect N_G(u)=Q,
```

and `N_G(u)=Q union U`.  Thus every five-colouring of `X` makes `U` a
transversal.  No uniqueness of the five-colouring is assumed or needed.

## 3. Exact Kriesell--Mohr application

All bichromatic root paths avoid `Gamma`, so the routing graph of
`(X,phi|X,U)` is the complete graph on `U`.  The graph

```text
D=K_U-E(e-a-b-c-d)
```

has exactly the six edges `eb,ec,ed,ac,ad,bd`.  Kriesell--Mohr, Theorem 7,
was checked directly in arXiv:1911.09998v2: every graph on five vertices
with at most six edges has property `(*)`.  Applying it to this spanning
subgraph of the routing graph gives the five disjoint connected rooted bags
and precisely the six required contacts.  The literal root edges `ab,cd`
supply two further contacts.  Only `ea,bc` can remain absent; the proof does
not submit `K_5` itself to property `(*)`.

## 4. Simultaneous interval repair and exact residue

The revised statement correctly defines

```text
M={xy in {ea,bc}: B_x and B_y are nonadjacent},
```

so it asks for intervals only for contacts actually missing from the chosen
certificate.  Adding all but the terminal `B_y` vertex of an `xy` interval
to `B_x` preserves connectedness, disjointness, roots, and all old contacts;
the last path edge creates the missing contact.

If both pairs belong to `M`, their interval endpoints lie in four distinct
bags.  Two subpaths of one simple path with four distinct endpoints cannot
overlap without an endpoint of one lying internally on the other, which the
definition forbids.  Intervals chosen on the two vertex-disjoint localized
paths are also disjoint.  If `|M|<=1`, there is no simultaneous allocation
issue.  Thus all cases `|M|=0,1,2` are covered and the enlarged quotient is
`K_5`.

Maximal visits to the bags give a reduced label trace.  Two distinct labels
are consecutive exactly when the intervening subpath has no internal vertex
of the model union, equivalently when it is a consecutive-bag interval.  If
the criterion fails, an actually missing pair `xy in M` has no such
transition on either path.  The designated path starts in `B_x` and ends in
`B_y`; any subpath between those endpoint bags which visited no third bag
would contain a consecutive `x,y` transition after suppressing repetitions.
Hence every such passage contains a vertex of a foreign bag, exactly as the
source states.

## 5. Rooted completion or a full separator

Under Corollary 6.1, the independent triple `Q` and
`alpha(G[N(u)])<=3` imply that `Q` jointly dominates `U`.  Every original
bag lies in `X`, and every added interval lies on a path using two
non-`gamma` colours, so the completed bags also lie in `X` and are disjoint
from `Q`.

If one component `K` of `(G-u)-W'` contains all of `Q`, then `K` is adjacent
to each rooted bag through a `Q-U` edge.  The singleton `{u}` sees `K`
through `Q` and sees every rooted bag through its root.  Together with the
five pairwise adjacent rooted bags, these are seven disjoint connected,
pairwise adjacent branch sets, giving the claimed explicit `K_7` model.

Otherwise two members `q_i,q_j` of `Q` lie in different components of
`(G-u)-W'`.  The model union is therefore a `q_i-q_j` separator.  Choose an
inclusion-minimal separator `Z` inside it.  Since deleting `u` from a
seven-connected graph leaves a six-connected graph, `|Z|>=6`.

For every `z in Z`, minimality gives a `q_i-q_j` path in
`H-(Z-{z})`; its two portions show that `z` has a neighbour in each
distinguished component of `H-Z`.  Componenthood gives the reverse
containment, proving

```text
N_H(R_i)=N_H(R_j)=Z.
```

The only vertex outside `H=G-u` is `u`, and `u` has neighbours `q_i,q_j` in
the respective components.  Consequently

```text
N_G(R_i)=N_G(R_j)=Z union {u}.
```

Thus these are literal full components of the displayed actual separation.
Finally, at least six separator vertices distributed among five disjoint
bags force a repeated bag, as claimed.

## Trust boundary

No unresolved assumption remains in the stated theorem or corollary.  The
proof synchronizes two paths and the six-demand certificate in one
colouring, but it does not make that certificate avoid the paths.  Its
full-separator outcome has no bounded order, can contain non-neighbours of
`u`, and does not preserve a named aligned response or decrease the order of
a component of `G-N[u]`.  It is therefore correctly labelled nonterminal.
