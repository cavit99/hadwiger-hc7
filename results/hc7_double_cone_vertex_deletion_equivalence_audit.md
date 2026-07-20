# Independent audit: double-cone vertex-deletion equivalence

**Verdict:** **GREEN** for the exact source revision identified below.

This is a separate internal mathematical audit, not external peer review.  It
checks both directions of the double-cone equivalence, the boundary-deletion
corollary, the rerouting of a clique-minor model away from a simplicial
boundary vertex, and the explicit seven-branch-set lift.  It does not audit or
use the exploratory classification discussed in Section 4 of the source.

## Audited revision

The audited source is
[`hc7_double_cone_vertex_deletion_equivalence.md`](hc7_double_cone_vertex_deletion_equivalence.md)
at SHA-256

```text
0a70d3a8bdbfc6655f7a405165eb138ef07d423f44a6f25b55c88f722bb427b3
```

No finite census or conjectural classification is used in the proved
statements.

## 1. The forward implication in Theorem 1

Let `M_1,...,M_5` be a `K_5`-minor model in `J-v`.  The seven displayed
sets

```text
{a}, {b,v}, M_1, ..., M_5
```

are pairwise disjoint and connected.  The set `{b,v}` is connected through
the cone edge `bv`.  The first two sets are adjacent through `av`, despite
the stipulated nonedge `ab`.  The vertex `a` and the vertex `b` respectively
make both cone-derived sets adjacent to every `M_i`, and the five old branch
sets retain all mutual adjacencies.  Thus this direction gives a literal
seven-branch-set model and uses no hidden edge between the cone vertices.

## 2. The reverse implication in Theorem 1

In a `K_7`-minor model, disjointness permits at most two branch sets to meet
the two-element set `{a,b}`.

- If none meets it, seven branch sets lie wholly in `J`.  Five may be kept,
  and a vertex `v` may be taken from a sixth; the kept five avoid `v`.
- If exactly one meets it, the other six lie wholly in `J`, so the same
  choice works.
- If two meet it, the other five lie wholly in `J`.  The two exceptional
  sets cannot both be `{a}` and `{b}`, because those singleton sets are
  nonadjacent.  Hence at least one exceptional set contains a vertex of
  `J`; choosing such a vertex as `v` leaves the five wholly-`J` branch sets
  in `J-v`.

The last point also covers an exceptional branch set meeting both cone
vertices: because `a` and `b` are nonadjacent, a connected branch set
containing both must contain a vertex of `J`.  In all three cases the five
retained sets remain connected and pairwise adjacent.  The assumption that
`J` is nonempty is harmless and is sufficient for every displayed
construction; no unmentioned spanning assumption is used.

## 3. Corollary 2

Contracting the two connected subgraphs `Q_0,Q_1` separately and deleting
all unwanted vertices and edges gives exactly `I_2 \vee G[B]` as a minor:

- fullness makes each contracted vertex adjacent to every literal vertex of
  `B`; and
- anticompleteness makes the two contracted vertices nonadjacent.

Minor transitivity and Theorem 1 therefore show that `G[B]-v` has no
`K_5` minor for every `v in B`.  Hadwiger's theorem for `t=5` is the
established implication

```text
no K_5 minor  =>  four-colourable,
```

so every vertex deletion is four-colourable.  If `G[B]` itself is
five-chromatic, this is exactly vertex-5-criticality.

## 4. Rerouting a branch set away from the simplicial vertex

Assume a `K_5`-minor model in `G[B]` uses `d` in `M_1`.  The singleton
`{d}` cannot be a branch set: its only two boundary neighbours can make it
adjacent to at most two other disjoint branch sets, rather than the required
four.  Thus `M_1-d` is nonempty.

Connectedness is preserved.  A connected set containing `d` contains at
least one of `x_d,y_d`.  If it contains exactly one, `d` is a leaf in the
induced connected subgraph on `M_1`.  If it contains both, the edge
`x_dy_d` replaces the only possible use of the two-edge path through `d`.

No branch-set adjacency is lost.  Every edge incident with `d` has other end
`x_d` or `y_d`.  If one of those vertices lies outside `M_1` in another
branch set while the other lies in `M_1`, the edge `x_dy_d` supplies the
same inter-branch adjacency after deleting `d`.  If both lie in `M_1`, no
external adjacency used an edge at `d`; the remaining possibilities are
immediate.  Therefore

```text
M_1-d, M_2, ..., M_5
```

is a `K_5`-minor model in `G[B]-d`, contradicting Corollary 2.

## 5. Explicit lift in Corollary 3

The seven displayed sets

```text
Q_0, Q_1 union {d}, M_1-d, M_2, ..., M_5
```

are disjoint.  The second is connected because `Q_1` is full to `B` and
therefore has an edge to `d`.  The edge from `Q_0` to `d` makes the two
shore-derived branch sets adjacent.  Fullness makes each shore-derived set
adjacent to every one of the five boundary-model sets, while those five sets
retain their `K_5` adjacencies.  This is an explicit `K_7`-minor model in
`G`; it does not silently require a `Q_0-Q_1` edge.

It follows that `G[B]` has no `K_5` minor and hence is four-colourable by
the established `t=5` case.

## 6. Trust boundary

The audit verifies only Theorem 1 and Corollaries 2 and 3.  It does not
promote the proposed classification of vertex-5-critical graphs in Section
4, does not infer an unbounded statement from the cited finite census, and
does not claim that the full live order-eight interface or `HC_7` is
closed.
