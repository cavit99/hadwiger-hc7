# Independent audit: three-support packing barrier

**Verdict:** GREEN.

**Audit type:** separate internal mathematical and computational audit.

**Audited source:**
[`hc7_order8_three_support_packing_barrier.md`](hc7_order8_three_support_packing_barrier.md)

**Audited source SHA-256:**
`2b98bd3281fc3c88d6c9069fcf27432c74e2cabbb3607d89fda9f486d757c687`

**Promoted source SHA-256:**
`11a0b37c657a9663b9809fc681b1014483a98e6098768b7b950db72ea3bf36e8`

The promoted revision changes only the status paragraph to link this audit;
the refuted statement, construction, verifier, scope, and trust boundary are
unchanged.

**Audited verifier:**
[`hc7_order8_three_support_packing_barrier_verify.py`](hc7_order8_three_support_packing_barrier_verify.py)

**Audited verifier SHA-256:**
`2a6da666118e856e121bee34f8da37ec70bc68145aaf3d7fc1801364d22690f3`

During the audit, the source changed only the scope phrase “promising
correct disjunction” to “promising candidate disjunction.”  The refuted
statement, construction, proofs, certificates, and verifier did not change.
The pre-correction source SHA-256 was
`b17e28ead427893991d9fdee518d9de6a72ef98fb6b79e52364379a73586b97d`.
This is an internal audit, not external peer review.  The example is a
counterexample to the displayed intermediate implication, not to `HC_7`.

## Verdict

The graph construction, exact opposite responses, chromatic number,
eight-connectivity, absence of the three-support packing, and explicit
`K_7`-minor model are all correct.  The deterministic verifier represents
the displayed graph exactly and exhausts the finite searches it claims.
No unresolved mathematical or computational gap remains within the stated
scope.

## 1. Construction

The verifier constructs 17 vertices and 88 edges.  The edge count separates
as follows:

```text
R:                         11
triangle L:                 3
complete tripartite S:     21
S--R portal edges:         29
complete S--L incidence:   24
                           --
                           88
```

There are no `L`--`R` edges.  The boundary is exactly the complete
tripartite graph with parts `{d,e}`, `X`, and `Y`; `L` is a triangle complete
to `S`; and the right-shore edges and eight portal sets agree entry by entry
with (2.1)--(2.2).

Both shores are connected and adjacent to every literal boundary vertex.
The sets `Q0={0,1,2}` and `Q1={3,4,5}` are disjoint and connected: the first
contains the edges `02,12`, and the second contains `34,35,45`.  Direct
intersection with every portal set confirms that both are `S`-full.

## 2. Exact responses and chromatic number

On the left closed shore, the merged-root partition uses three boundary
colours, leaving three colours for the universal triangle.  The split-root
partition uses four boundary colours and leaves only two for that triangle.
Thus the left response is exactly merged-only.

On the right, every vertex has a neighbour in each of the three merged
boundary blocks `{d,e}`, `X`, and `Y`.  All right-shore vertices would
therefore be restricted to the other three colours, but `{0,2,3,5}` induces
a `K_4`.  The merged response is impossible.  The displayed split colouring

```text
(0,1,2,3,4,5) = (5,4,2,4,5,3)
```

was checked edge by edge against both the right-shore edges and the portal
table and is proper with boundary colours `X=0`, `Y=1`, `d=2`, `e=3`.

The verifier fixes these canonical boundary colours and recursively
enumerates every assignment of the six colours to the selected shore.  This
loses no response colouring, because any colouring inducing the prescribed
equality partition is equivalent under a permutation of colour names.  It
finds exactly the two positive responses above and rejects the other two.

For the whole graph, the universal triangle `L` consumes three colours and
excludes them from `S`.  The nonempty complete tripartite graph `G[S]` then
requires the other three colours and forces its three partite sets to be the
three colour classes.  This is the merged-root boundary partition, which
does not extend through `R`; hence `G` is not six-colourable.  The split
colouring above, together with three colours on `L` outside the four
boundary colours, gives a seven-colouring.  Therefore `chi(G)=7`.

## 3. Absence of a three-support packing

Enumerating all nonempty connected subsets of the six-vertex right shore
reproduced the displayed inclusion-minimal support families exactly:

```text
roots: 02 03 14 15 25 34 35
X:     3 05 12 14 25 45
Y:     34 012 015 045 123 135
```

The independent reconstruction also reproduced all ten disjoint minimal
`X`/`Y` pairs and their unused vertex sets in (4.2).  None of those unused
sets contains a minimal root support.  This suffices mathematically because
every finite connected support contains an inclusion-minimal connected
support for the same role.

The verifier performs the stronger direct check: it forms every connected
root support, every connected `X`-support, and every connected `Y`-support,
then tests every triple for pairwise vertex-disjointness.  The resulting
packing list is empty.  Thus the finite encoding is exact and does not rely
on a bounded proxy for an unbounded host.

## 4. Eight-connectivity

For each nonempty connected `A subseteq R`, the verifier computes its open
neighbourhood inside `R` plus the set of boundary vertices having a neighbour
in `A`.  The minimum sum is exactly eight, reproducing (5.1).

More decisively, it tests every deletion set of orders zero through seven:

```text
sum(binomial(17,k), k=0,...,7) = 41226.
```

The remaining graph is connected in every case.  The breadth-first search
uses the literal constructed adjacency sets and permits no path through a
deleted vertex.  Deleting the eight-set `S` leaves the connected shores
`L` and `R` anticomplete, so it disconnects the graph.  Hence
`kappa(G)=8`, and in particular there is no separation of order seven.

## 5. Explicit `K_7`-minor model

The seven displayed branch sets are pairwise disjoint.  Their internal
connectivity is immediate except for the fifth set; there the edges
`03,34`, together with the portal edges from `y1` to `4` and from `y3` to
`0,3`, give a connected subgraph.  The verifier checks connectivity for all
seven sets and checks a literal edge between every one of the 21 pairs.

All branch vertices lie in `S union R`.  The singleton branch sets `{1}` and
`{5}` are joined by the edge `15`, and each is adjacent to every one of the
first five branch sets.  Thus those first five sets form a `K_5` model and
the saturated edge `15` completes it to the asserted `K_7` model without
using the opposite triangle.

## 6. Verifier execution

The audited command

```text
python3 barriers/hc7_order8_three_support_packing_barrier_verify.py
```

returned exactly

```text
GREEN exact-order-eight three-support packing barrier
host: vertices=17 edges=88 connectivity=8 cuts_tested=41226
chromatic_number=7; responses: left=merged-only right=split-only
right_shore: two disjoint S-full connected subgraphs; three-support packing=none
relative_connected_set_boundary_min=8
K7 minor: explicit seven branch sets verified inside S union R
scope: K7-minor exclusion and contraction-criticality deliberately absent
```

The same output was reproduced with Python hash seeds `0`, `1`, and `17`.

## 7. Exact scope

The example simultaneously has eight-connectivity, chromatic number seven,
an actual order-eight separation with connected full shores, exact opposite
merged/split responses, and two disjoint boundary-full connected subgraphs
on the split-response shore.  It nevertheless has neither the required
three-support packing nor an order-seven separation.  This refutes exactly
the statement displayed in Section 1.

The graph contains the explicit `K_7` minor above.  Contracting and deleting
to that model gives a proper seven-chromatic minor, so the graph also fails
proper-minor six-colourability and is not a nontrivial contraction-critical
host.  It therefore does not refute any theorem retaining global `K_7`-minor
exclusion and the appropriate proper-minor responses.

The final three-way display in the source is a candidate research direction
motivated by the saturated-edge certificate.  This barrier does not prove
that those three outcomes are exhaustive, and the display must not be cited
as a proved disjunction.
