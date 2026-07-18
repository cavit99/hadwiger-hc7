# Audit of the degree-eight contact-allocation theorem

**Verdict: GREEN.**  This is a separate internal audit, not external peer
review.

**Audited source:**
[`hc7_degree8_contact_allocation.md`](hc7_degree8_contact_allocation.md)

**Audited SHA-256:**
`84c47863546f9800db24bf042e60952221dcf3649b4076170259efa9fde78049`

## Local branch-set constructions

The complete-contact and one-missing-contact constructions are correct.
An order-seven contact set among eight neighbours supplies the required
contacted vertices.  Every displayed bag is connected, all fifteen pairs
of the six local bags are adjacent, and every bag contains a vertex of the
outside component's neighbourhood.  Appending that connected component
therefore gives an explicit `K_7`-minor model.

Deleting one vertex from the literal spanning five-cycle leaves a
four-vertex path.  Deleting at most one further uncontacted vertex leaves
an edge, so the stated five-cycle corollary is valid.

## The two-defect table

Every row of Table (4.5) was checked independently against a graph having
only the literal five-cycle, the hub edges, and the permitted `B`--`C`
edges.  Each row partitions `\{v\} union B union C` into six connected
sets, supplies all fifteen pairwise adjacencies, and uses no edge inside
`B`.  The stabilizer orbits listed for the adjacent- and distance-two
defect patterns cover every possible omitted label.  In each omission
case, the omitted label lies in a two-vertex bag with a contacted label, so
all six bags meet the outside component.

The reduction from zero or one missing cross-edge to two is valid: delete
additional cross-edges with distinct endpoints and use the model found in
that spanning subgraph.

## Connected-set lift and plane corollary

Replacing each cyclic vertex by its whole connected set preserves
disjointness, connectivity, every cyclic adjacency and every permitted
cross adjacency.  The specified neighbour in each set supplies its edge to
the hub.  The proxy contact set is sufficient because an absent label is
always paired with a present label in the table.  Appending `D` remains a
valid lift.

For a degree-five vertex in a three-connected plane graph, deleting the
vertex leaves a two-connected graph.  The merged face consequently has a
cycle boundary through the five neighbours in rotation order, and its
arcs partition into five cyclic connected sets.  The source correctly
requires that cycle to be disjoint from the proposed seventh branch set;
it does not infer this disjointness from planarity.

## Trust boundary

No unresolved assumption remains within the theorem.  It does **not**
prove that a hypothetical counterexample supplies the needed contact-
defect matching or a facial cycle disjoint from the seventh branch set.
Those are host-level completion obligations, not consequences of the local
allocation theorem.
