# Independent audit: exact-block Kempe transitions across two full shores

**Verdict:** **GREEN** for the exact source revision identified below.

This is a separate internal mathematical audit, not external peer review.  It
checks the contraction anchors, the fixed-block Kempe space, the shortest-path
argument, both one-move obstruction paths, the simultaneous list-critical
conclusion, and the stated trust boundary.

## Audited revision

The audited source is
[`hc7_two_full_shore_exact_block_kempe_transition.md`](hc7_two_full_shore_exact_block_kempe_transition.md)
at SHA-256

```text
b9b1c08af789a08c3259f899cd821058d78bfd023e161ee5597a6eabaf127feb
```

## 1. Hypotheses and contraction anchors

The hypotheses used in Theorem 2.1 are all necessary at the points claimed.
Connectedness and fullness make `D union I` connected: `D` is connected and
every vertex of `I` has a neighbour in `D`.  Since `D` and the nonempty set
`I` are disjoint, this union has at least two vertices.  Contracting a
spanning tree of it therefore contracts at least one edge and gives a proper
minor even when `D` is a singleton.  The same observation applies to
`A union I` when `A` is a singleton.

Let `z` be the image of `D union I`.  In a six-colouring of the contracted
minor:

- every vertex of `B-I` avoids the colour of `z`, because fullness of `D`
  makes it adjacent to `z`;
- every vertex of `A` with a neighbour in `I` avoids that colour, because
  contraction turns the corresponding edge into an edge to `z`; and
- all edges internal to `A union (B-I)` remain properly coloured.

Reinserting every vertex of `I` in the colour of `z` is therefore proper:
`I` is independent, its actual neighbours in `A` avoid the colour by the
second point, and its neighbours in `B-I` avoid it by the first point.  The
colour occurs on the boundary exactly at `I`.  Renaming it colour six gives
the asserted `A`-shore anchor.  Contracting `A union I` proves the symmetric
`D`-shore anchor.  No unmentioned lower bound on either shore is needed.

## 2. Fixed-block Kempe connectivity

Deleting the fixed colour-six class `I` is a bijection between exact-`I`
boundary colourings and labelled proper five-colourings of `G[B-I]`; adding
`I` back in colour six is its inverse.  Under this bijection, the edges of
`Gamma_I(B)` are exactly the ordinary five-colour Kempe interchanges on
`G[B-I]`.  Thus every move preserves `I` pointwise as the exact sixth colour
class.

The induced subgraph `G[B-I]` is a subgraph, hence a minor, of `G[B]`.
Consequently the hypothesis that `G[B]` has no `K_5` minor passes to
`G[B-I]`.  The cited Las Vergnas--Meyniel theorem then connects all of its
labelled five-colourings.  Unused palette colours cause no exception.  If
`G[B-I]` is disconnected, the componentwise sequences concatenate because a
two-colour component inside one graph component is also a two-colour
component of the whole graph.  If `B-I` is empty, there is a unique boundary
colouring, so connectivity itself remains valid.

Finally, extensions of one exact labelled trace through both closed shores
glue: they agree on `B`, and `A` and `D` are anticomplete.  Since `G` is not
six-colourable, the two nonempty extension sets are disjoint.

## 3. Shortest extension-set path

Connectivity and the two anchors give a path between the extension sets.
Minimizing its length over both endpoints yields exactly (3.4): if a later
vertex extended through `A`, its suffix would be shorter, and if an earlier
vertex extended through `D`, its prefix would be shorter.  Disjointness gives
`k>=1`.  For `k>=2`, every internal colouring is therefore rejected by both
closed shores, not merely by one of them.

Every path vertex belongs to `Gamma_I(B)` by construction, so the exact
labelled class `I` remains fixed throughout; this conclusion is not inferred
from endpoint data alone.

## 4. The distance-one obstruction paths

For `k=1`, let `W` be the operated `alpha`--`beta` component in `B-I`.
In an extension of `phi_0` through `A`, if the full two-colour component
containing `W` met no other boundary component, switching that full component
would change the boundary trace exactly to `phi_1`.  This contradicts (3.4),
so the full component meets another boundary component.

A shortest connection from `W`, stopped at its first boundary vertex outside
`W`, has all internal vertices in `A`.  Its interior is nonempty: an edge
between the two boundary ends would join the allegedly different components
of `G[B-I][alpha,beta]`.  Reversing the sole interchange in a `D`-shore
extension gives the second path.  Swapping the two colour names on `W` does
not alter the underlying two-colour induced graph, so the reverse move uses
the same colour pair and the same operated component.  The path interiors
are disjoint because they lie in the disjoint sets `A` and `D`; no equality
of their other boundary components is inferred.

## 5. The simultaneous list-critical kernels

Fix one internal `phi_i` when `k>=2`.  Extending it through `A` is equivalent
to colouring `G[A]` from

```text
L_A(v) = {1,...,6} - phi_i(N_G(v) intersect B).
```

Indeed these are exactly the colours not forbidden by the already fixed
boundary neighbours, and properness on edges inside `A` is the remaining
condition.  Because `phi_i` is rejected through `A`, a vertex-minimal induced
non-`L_A`-colourable subgraph exists.  It is connected, since otherwise one
component would already be a smaller obstruction.  Deleting any vertex `v`
leaves a colourable graph; if `d(v)<|L_A(v)|`, one listed colour is absent
from all coloured neighbours and extends the colouring to `v`, a
contradiction.  Hence

```text
d_K(v) >= |L_A(v)| = 6 - |phi_i(N_G(v) intersect B)|.
```

The argument includes empty lists and one-vertex obstructions.  Applying it
to `D` with the same fixed `phi_i` gives the second kernel.  Thus the two
kernels are genuinely simultaneous under one boundary trace, and they are
vertex-disjoint because one lies in `A` and the other in `D`.

## 6. Falsification checks and trust boundary

The proof was checked against the principal edge cases: singleton shores,
disconnected or empty `B-I`, unused colours, a one-vertex list obstruction,
and reversal of the one-step interchange.  None creates a gap.  The
nonemptiness of `I`, its independence, shore fullness, and shore
anticompleteness are each used explicitly and are not silently dispensable.

The source correctly stops short of a common boundary colouring, prescribed
other path ends, boundary-full kernels, a neighbourhood bound, an
order-seven separation, or a `K_7`-minor model.  The cited common-colouring
barrier is used only to delimit those stronger inferences and not as an input
to either theorem.

No mathematical defect or unstated computational assumption was found.
