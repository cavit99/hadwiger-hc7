# Independent audit: rich-edge quotient of the compulsory locks

**Verdict:** GREEN.

**Audited source:** `results/hc7_compulsory_lock_rich_quotient_two_routes.md`

**Source SHA-256:** `28eb7d9535defa4e668635ee0aa430ae354853df6550b06ae82715ff6e6a4f74`

**Post-audit editorial change:** the duplicated second equation tag `(3.1)`
and its later reference were changed to `(3.3)`; no mathematical content
changed.

## 1. Quotient construction

For one alternate colour `delta`, the compulsory Kempe lock `K_delta` is
connected and contains `z,u`.  Contracting each component of
`K_delta-R` therefore gives a connected multigraph.  Retaining parallel
edges is essential and is done in the source.  Any nonloop quotient edge
has at least one endpoint in `R`: an edge with both endpoints outside
`R` would join two vertices of the same component of `K_delta-R` and
become a loop.  Since the frozen separation has no `A-R` edge, every
retained edge is consequently either rich-internal or boundary--rich,
and each retained parallel edge has its own literal preimage.

The contracted source and target coincide exactly when `K_delta-R`
contains a literal `z-u` path.  This verifies the first alternative of
Theorem 2.1 without introducing a quotient-only adjacency.

## 2. Edge cut and lifting

Assume the quotient source and target are distinct.  A one-edge
source--target cut in the quotient is a bridge.  Its particular parallel
edge has one literal preimage `f`.  If `K_delta-f` still contained a
literal `z-u` path, contraction of that path would give a quotient walk,
and hence a quotient path, avoiding that parallel edge.  Thus `f` is a
literal rich-internal or boundary--rich separating lock bridge.  This is
exactly the branch excluded by Corollary 5.1 of the audited twin-state
handoff, under the residual-branch hypothesis explicitly made in the
source.

The quotient therefore has source--target edge-connectivity at least two.
Edge-Menger for finite multigraphs gives two edge-disjoint quotient paths.
Each occurrence of a contracted component along one path can be expanded
inside that connected component, so both quotient paths lift to literal
routes.  The lifts need not be vertex-disjoint, nor need their internal
thin edges be disjoint.  What is preserved is exactly what the theorem
claims: their sets of retained rich-internal/boundary--rich literal edges
are disjoint.

## 3. Separation between colour systems

In the fixed proper colouring, every literal edge of the `delta` Kempe
subgraph has endpoint-colour set `{alpha,delta}`.  A retained edge in an
`epsilon` system has endpoint-colour set `{alpha,epsilon}`.  Hence one
literal retained edge cannot occur in systems for two distinct alternate
colours.  This proves the cross-colour edge-set disjointness.  It does not
prove vertex disjointness: systems may share vertices of colour `alpha`,
as the source correctly records.

If no lock has a `z-u` path in `A union S`, the first alternative is
excluded for all five alternate colours, so Corollary 2.2 supplies two
routes per colour.  The conclusion is only a ten-route rich-edge capacity
certificate, not ten fully edge-disjoint literal paths.

## 4. Thin-lock consequence

For a thin `delta` lock, take a literal `z-u` path in `K_delta-R`.
Because the lock is formed in `G-zu`, its last edge is not `zu`.  The
predecessor of `u` cannot lie in `A`, since `zu` is the unique `A-u`
edge, and cannot lie in `R`, by the choice of path.  It is therefore a
literal neighbour in `W`, and bichromatic properness gives it colour
`delta`.  Distinct alternate colours give distinct predecessors.

The exceptional `K_{1,3} dotunion K_3` frontier has maximum degree three,
so at most three locks can be thin.  In the connected bipartite frontier,
five thin colours give five distinct neighbours of `u` in its opposite
bipartition class.  The class containing `u` has at least two vertices
(in particular the paired mate of the compulsory literal is not adjacent
to it), and the boundary has seven vertices.  Hence the classes have
sizes two and five, `u` is complete to the five-vertex class, and those
five vertices have the five alternate colours.  The seventh vertex must
repeat one of the six colours, yielding exactly one double equality block.
Thus Lemma 3.1 is valid.

## 5. Obstruction and scope

The displayed common-`alpha` hub architecture respects the proper-colour
constraints and has two edge-disjoint routes per alternate colour while
forcing every displayed route through the same vertex.  It is therefore
a valid sharp warning against upgrading the theorem by ordinary
vertex-Menger.  The note also correctly keeps separately attained
final-duty states logically independent of the fixed colouring used here.

Accordingly, Theorem 2.1 and Corollary 2.2 are proved as stated.  They do
not decode a lock path wholly in the thin closed shore, nor do they decode
the all-rich-routes capacity certificate into labelled branch sets.  The
source's corrected decoder order (thin-lock first, repeated-colour
articulation second, cross-state synchronization third) is logically
necessary.  The result does not close the residual atomic branch or
`HC_7`.
