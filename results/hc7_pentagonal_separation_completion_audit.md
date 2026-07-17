# Audit of the pentagonal order-seven separation completion

**Verdict:** GREEN.

**Source audited:** `results/hc7_pentagonal_separation_completion.md` at
SHA-256
`f0398670a072af6c325a34ae959168af00edf1b5363d1298129327f16d094a59`.

The mathematical source was audited at SHA-256
`07549d36bccdb4be2d6e11309537f073a6616eb3b65a50480a2c401fc6f7c846`.
The promoted revision changes only the status line from “awaiting separate
internal audit” to “separate internal audit GREEN”; restoring the former
line reproduces the audited hash exactly.  No theorem statement,
hypothesis, proof, citation, or scope qualification changed.

**Audit class:** separate internal line-by-line audit.  This is not external
peer review.

## 1. External input

The quoted Martinsson--Steiner statement is exact.  Lemma 3.1 of
Anders Martinsson and Raphael Steiner, *Strengthening Hadwiger's conjecture
for 4- and 5-chromatic graphs*, Journal of Combinatorial Theory, Series B
164 (2024), 1--16, states that if `F` is 3-connected, `X` has order at
least four and is spread out across every order-three separation, and `F`
has no `X`-rooted `K_4` minor, then adding one vertex adjacent to every
member of `X` produces a planar graph.  The source definition of an
`X`-rooted model agrees with the definition used in the theorem.

## 2. Full attachment and shore connectivity

Because `A` and `B` are components of `G-S`, their external neighbours lie
in `S`.  If either component missed one boundary vertex, its neighbourhood
would have order at most six and would separate it from the other nonempty
component.  Seven-connectivity therefore gives full attachment to every
literal boundary vertex.

Deleting `p,q` from a 7-connected graph leaves the graph `H` 5-connected.

Fix `Z subseteq V(F_A)` with `|Z|<=2`.  A component `D` of `F_A-Z` which
missed `C-Z` would lie in `A`; since there are no `A`--`B` edges, its full
neighbourhood in `H` would lie in `Z`, contradicting 5-connectivity.  If
`Z` meets `A`, at most one cycle vertex is deleted, so `C-Z` is connected
and all components meeting it coincide.  If `Z subseteq C`, the undeleted
connected shore `A` meets every vertex of `C-Z`, so the whole graph remains
connected.  Thus `F_A` is 3-connected.  The argument is symmetric for
`F_B`.  Both graphs have at least six vertices, so the order convention for
3-connectivity is satisfied.

For an order-three separation `(U,W)` of `F_A`, if `C subseteq U`, the
nonempty open side `W-U` lies in `A` and has all neighbours in `U intersect
W` inside `H`: it has no edge to `B`, and the separation excludes edges to
`U-W`.  This is a cut of order three in the 5-connected graph `H`.
Therefore neither closed side of such a separation contains all of `C`,
which is exactly the spread-out condition.  The symmetric cases are
valid.

## 3. The seven branch sets

If `M_1,...,M_4` form a `C`-rooted `K_4` model in `F_A`, then

\[
 M_1,M_2,M_3,M_4,\quad B,\quad\{p\},\quad\{q\}
\]

are disjoint connected sets.  Every `M_i` meets a cycle root.  Full
attachment makes `B` adjacent to that root and hence to `M_i`; the join
edges make both `p` and `q` adjacent to `M_i`; full attachment at `p,q`
makes `B` adjacent to both singleton sets; and `pq` supplies their mutual
edge.  All 21 required adjacencies are present.  The same applies with the
shores interchanged.

Thus `K_7`-minor exclusion legitimately supplies the no-rooted-`K_4`
hypothesis of Martinsson--Steiner on both shores.

## 4. From apex planarity to two disc embeddings

In a planar embedding of `F_X^+`, the added apex and the chordless cycle
`C` contain a wheel.  As a plane subgraph, that wheel divides the sphere
into the five triangular regions incident with the apex and the remaining
region bounded by `C`.

The connected graph `F_X-C` lies in one region of this wheel: an edge
joining vertices in different regions would cross the wheel.  It cannot
lie in an apex-side triangular region.  Such a region has only two cycle
vertices on its boundary, and the added apex has no neighbours outside
`C`; those two cycle vertices would therefore separate the nonempty shore
from the rest of `F_X`, contradicting 3-connectivity.  Hence the entire
shore lies in the region on the side of `C` opposite the apex.  Deleting
the apex gives a planar disc embedding of `F_X` with `C` as its boundary.

Reflecting one of the two disc embeddings and identifying their boundary
copies of `C` gives a plane embedding of `H`.  There are no `A`--`B` edges,
so no edge is omitted or forced to cross.  This contradicts the assumed
`K_5` minor in `H`, since planarity is minor-closed.

The minimal-counterexample corollary is also valid.  If
`G-{p,q}` were four-colourable, two fresh distinct colours on the adjacent
vertices `p,q` would six-colour `G`, independently of their additional
shore neighbours.  Hence `chi(G-{p,q})>=5`; the established `t=5` case of
Hadwiger gives a `K_5` minor there, exactly the theorem's remaining
hypothesis.

## 5. Scope

The proof is host-level and unbounded.  It establishes exactly the theorem
stated in the source.  It does not prove that every 5-connected graph with
an induced five-cycle and two full shores has a five-cycle-rooted `K_5`
minor; the two additional boundary vertices and their full attachment are
used in the explicit `K_7` construction.

No unresolved mathematical gap was found.
