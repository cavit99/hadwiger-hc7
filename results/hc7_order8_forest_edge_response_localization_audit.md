# Independent audit: contraction-critical responses at a boundary-forest edge

**Verdict:** **GREEN** for Theorem 2.1 at the exact revision below.  This is
a separate internal mathematical audit, not external peer review.  The result
is an unbounded conditional response lemma and does not prove `HC_7`.

## Audited revision

This audit checks the complete source file
[`hc7_order8_forest_edge_response_localization.md`](hc7_order8_forest_edge_response_localization.md)
at SHA-256

```text
91b441137daa74c5d57b5e7e621aa373b7430af8568896eb9a2e723d0aaf696e
```

The only source change after the mathematical audit replaced the pending
status with a link to this audit.

The exact hypotheses checked are the vertex partition (1.1), the two rooted
triangles (1.2), the forest and root-neighbourhood normalization (1.3), and
the minor-critical chromatic assumptions (1.4).  No contact or adjacency
property of `E,D,R_0,R_1` beyond their being the four literal parts of
`V(G)-S` enters this lemma.

## 1. Edge deletion and the endpoint colour

Let

```text
xy in E(G[F]) - {x_d y_d, x_e y_e}.
```

Deleting `xy` gives a proper minor, so (1.4) supplies a proper colouring with
at most six colours.  In any proper six-colouring `c` of `G-xy`, if
`c(x) != c(y)`, restoring the sole deleted edge leaves the colouring proper,
contrary to `chi(G)=7`.  Hence every such colouring satisfies
`c(x)=c(y)=alpha`, exactly as asserted in (2.2).

The proof that `chi(G-xy)=6` is also correct.  If `G-xy` had a colouring with
at most five colours, recolour `x` with one new sixth colour.  The new colour
occurs nowhere else, so all edges incident with `x` are proper; after
restoring `xy`, its other endpoint `y` still has one of the original colours.
This would be a proper six-colouring of `G`.  Therefore a proper
six-colouring of `G-xy` necessarily uses all six colours, so there are exactly
five alternate colours besides `alpha`.

## 2. The five Kempe paths

Fix one alternate colour `beta`.  If `x` and `y` were in different connected
components of the subgraph induced by colours `{alpha,beta}`, swapping those
two colours on the component containing `x` would preserve properness and
would change the colour of `x` to `beta` while leaving `y` coloured `alpha`.
Restoring `xy` would then produce a proper six-colouring of `G`.  Thus `x`
and `y` lie in the same bichromatic component, which contains an
`x`--`y` path `P_beta`.  Repeating this independently for every alternate
colour yields the five claimed paths.  The theorem does not claim that these
five paths are mutually disjoint, so no simultaneous-choice assumption is
hidden here.

## 3. Why no response path stays in the boundary

Since `G[F]` is a forest and `xy` is one of its edges, `x` and `y` lie in
different components of `G[F]-xy`.

The excluded-edge condition in (2.1) is essential.  It ensures that both
edges `x_d y_d` and `x_e y_e` remain in `G[F]-xy`.  Consequently the two
boundary neighbours of `d` lie in one component of `G[F]-xy`, and the same
is true for the two boundary neighbours of `e`.  By (1.3), these are all the
neighbours of the respective roots inside `S`.  Adding `d` or `e` therefore
attaches a new vertex only within one pre-existing component and cannot join
the components containing `x` and `y`.  The assumptions `de notin E(G)` and
`S={d,e} disjoint-union F` leave no further boundary edge through which the
components could reconnect.  Hence `x` and `y` are disconnected in
`G[S]-xy`.

Every `P_beta` is an `x`--`y` path in `G-xy`; if all its vertices lay in
`S`, it would contradict the preceding disconnection.  Its endpoints lie in
`F subseteq S`, so every such path has at least one **internal** vertex in
`V(G)-S`.

## 4. First-hit collision and path intersections

The four sets `E,D,R_0,R_1` partition `V(G)-S`.  After orienting a path from
`x` to `y`, its first outside vertex therefore belongs to exactly one named
part.  This makes `lambda(beta)` well-defined; it does not identify a colour
with a branch-set label, because the label is assigned by the literal first
outside vertex.

There are five alternate colours and four named parts.  The pigeonhole
principle gives distinct colours `beta,gamma` whose chosen paths first enter
the same named part.  This conclusion is independent of how one path is
chosen inside each bichromatic component.

If a vertex lies on both `P_beta` and `P_gamma`, its colour belongs to both
sets `{alpha,beta}` and `{alpha,gamma}`.  Since `beta` and `gamma` are
distinct alternate colours, the intersection of those colour sets is
`{alpha}`.  Every common path vertex is therefore coloured `alpha`, including
a common first outside vertex if the two first hits coincide.

## 5. Dependency and adversarial scope checks

The stated dependency is valid at its promoted audited revision:

- [`hc7_adjacent_full_pair_cycle_completion.md`](../results/hc7_adjacent_full_pair_cycle_completion.md)
  has SHA-256
  `832fff95b699aa73b1f1b10cc52e1f562d6e108dad059962b3563a799bc3f875`;
- its adjacent GREEN audit pins that exact promoted hash and checks
  Corollaries 3.2 and 3.5, which supply precisely the forest and boundary-root
  normalization assumed here.

The proof was tested against the following possible overextensions.

- If `xy` is one of the two rooted-triangle edges, deleting it can let the
  corresponding root reconnect its ends inside `G[S]-xy`; the theorem
  correctly excludes those edges.
- If `G[F]` is not a forest, deleting `xy` need not separate its ends; the
  boundary-exit conclusion is then unsupported.
- If either root has another neighbour in `S`, that root may join distinct
  components after deletion; equality in (1.3), not merely inclusion of the
  triangle neighbours, is needed.
- Without the proper-minor chromatic hypothesis, neither existence of a
  six-colouring of `G-xy` nor the Kempe contradiction follows.
- The first-hit collision alone gives neither disjoint response paths nor a
  split of the repeated named part.  The source states this trust boundary
  accurately and does not infer a `K_7` minor or a compatible separation.

Within these stated hypotheses, no counterexample or unresolved implication
was found.  Theorem 2.1 is therefore GREEN at the pinned revision.
