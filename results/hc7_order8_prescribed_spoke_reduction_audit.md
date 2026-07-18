# Internal audit of the prescribed-spoke order-eight reduction

**Verdict:** GREEN for Theorems 1.1 and 3.1, corrected Corollaries 2.1 and
4.1, and Lemma 5.1, subject to the explicit non-conclusions in Section 6 of
the source.

**Audited source:** `hc7_order8_prescribed_spoke_reduction.md`, SHA-256

```text
3b55f263775f35164efe1d32c6ed86eab777ea2272b24293129e8e65517517d6
```

This is a separate internal mathematical audit, not external peer review.
The unrestricted prescribed-spoke theorem and the target-retaining
fan-or-separator theorem were checked independently by different agents.

## 1. Prescribed-spoke theorem

The Menger argument is correct.  Direct prescribed neighbours in the target
set are retained as one-edge paths and removed together with `v`.  Both
remaining terminal sets have the required order.  Any smaller separator,
including one containing terminals, combined with the removed vertices
would delete fewer than `k+1` vertices from the `(k+1)`-connected host.
Set-Menger therefore supplies all remaining source paths with distinct
target ends.  Truncating at the first target and prepending the prescribed
edges preserves disjointness.

For Corollary 2.1 the deleted edge `vp` is legitimately used in the original
graph as the sixth spoke, while the five other spokes are distinct first
edges of the edge-disjoint colour paths.  The target has order six, so every
selected boundary vertex is used.  The `vp` path is direct; all other paths
avoid `p`.  Before their first boundary hit they remain inside the named
component of `G-X`.

The rerouted paths need not be bichromatic, need not remain in the selected
component, and may contain unselected boundary vertices internally.  An
earlier draft incorrectly truncated them at their first boundary vertices;
the corrected source makes no such claim.

## 2. Target-retaining alternative

The direct/non-direct count and the construction of `I` are sound.  A direct
end has its private colour, so direct ends are distinct and are different
from every endpoint of a non-direct path belonging to another colour pair.
There are enough unused boundary vertices to enlarge the prescribed set to
order `ell+1` while avoiding all direct ends.

The vertex-capacitated Menger statement must, and does, permit `Z` to contain
source vertices and repeated target endpoints.  In the packing branch every
source is used; truncation before prepending the original first edges gives
five paths disjoint outside the base and boundary.

In the cut branch `|Z|<|S|`, so a source survives.  Its component `A` has no
neighbour in `I`, no uncut neighbour elsewhere in `C-{v}`, and no neighbour
outside `C union X`.  Hence its full neighbourhood is contained in the
displayed seven-set.  The separate component of `G-X` makes the separation
nontrivial.  Seven-connectivity forces equality and `|Z|=ell-1`.

Every original non-direct tail is an `S`--`I` path and meets `Z`, with a
source in `Z` counted as a meeting.  Pigeonhole gives one vertex on two
different-colour tails, which must have the common colour `alpha`.  Since
`p in I`, the missing edge `pv` is absent from the closed `A`-side, so the
restricted deletion colouring is proper in the original graph.

## 3. Exact-seven colouring data

For a minimum seven-boundary, every complementary component is boundary-
full: missing one literal boundary vertex would give a separator of order at
most six.  Under the explicitly added hypothesis that every proper minor is
six-colourable, contracting `A union J` forces the exact independent block
`J` on the opposite closed shore.  The source does not claim the full
boundary partition is reproduced.

Because `|J|>=2`, the remaining boundary has at most five vertices and is
four-degenerate.  Las Vergnas--Meyniel connects its labelled five-colourings.
If that remaining graph is a clique, the exact-block equality partition is
unique and the two shore colourings glue.  Otherwise only a connected
exact-block transition space is obtained.

## 4. Label decoder and trust boundary

Lemma 5.1 is an explicit seven-branch-set construction.  All new path pieces
are absorbed into one branch set, so neither mutual disjointness among those
pieces nor an injective colour-to-label assignment is needed.  They must,
however, avoid the other six model branch sets until their intended terminal
contacts.

The audit specifically rejects these stronger inferences:

- the local pair selected by a boundary three-colouring is an inherited
  minor-model pair;
- the five rerouted paths remain bichromatic;
- the arbitrary-target fan stays in the selected complementary component or
  avoids unselected boundary vertices;
- distinct boundary ends belong to five distinct named branch sets;
- the order-seven output already has a common full equality partition; or
- the present results close either order-eight component count or `HC_7`.

The exact remaining issue is a label-preserving model alignment, not path
packing.
