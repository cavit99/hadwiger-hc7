# Independent audit of the same-bag exact-seven two-edge barrier

**Verdict:** **GREEN** at the exact source and verifier revisions recorded
below.  The construction has all hypotheses of the intermediate statement
it refutes, neither proposed local conclusion, and the two global defects
stated in its trust boundary: it contains an explicit `K_7` and is not
minor-minimal.

This is a separate internal mathematical audit, not external peer review.

## Exact revisions audited

```text
75993b8655219126151c0b985388d766a9b4efb95b966a82ea745d22a1611753  barriers/hc7_same_bag_two_critical_edges_exact7_barrier.md
0f68a6c58f0c426c407a9dc510bc9c63369c399686bc35d42501fe3cc39a7ebd  barriers/hc7_same_bag_two_critical_edges_exact7_barrier_verify.py
```

The source change after the mathematical audit is status-only: it replaces
"audit pending" with a link to this GREEN audit.

The verifier imports the adjacent base construction from
`hc7_joint_pair_first_hit_hall_barrier_verify.py`.  I inspected that
constructor directly and also ran its complete verifier before auditing the
new vertex extension.

## 1. Construction, connectivity and separation

The old graph has fifteen vertices.  Its deterministic verifier exhausts
all vertex deletions of order at most seven, proving that it is
eight-connected.  The new vertex `ell` has precisely the seven neighbours

```text
pA pB p1 p2 p3 c2 c3.
```

After deleting at most six vertices, the surviving old vertices remain
connected.  If `ell` remains, at least one of its seven neighbours remains
and joins it to that component.  Conversely, deleting the displayed
seven-set isolates `ell`.  Thus the enlarged graph has connectivity exactly
seven.

The verifier separately checks that the old vertices outside the boundary
induce a connected graph and that every boundary vertex has a neighbour in
it.  Hence

```text
{ell} | S | (V(G)-S-{ell})
```

is an actual order-seven separation with two nonempty connected open shores,
each adjacent to every literal boundary vertex.

## 2. Chromatic number and the labelled near-complete model

The seven vertices

```text
v a b c1 c2 c3 c4
```

induce `K_7`.  Recolouring `v` with a seventh colour in the displayed
six-colouring of the common deletion gives a proper seven-colouring of the
whole graph.  Therefore `chi(G)=7`.

The verifier checks that the seven displayed branch sets are nonempty,
pairwise disjoint, connected and spanning.  Their only missing pair is
`Y1,Y2`.  Both edges `va,vb` join the same two branch sets `R,U`.
The other edges `vpA,vpB` preserve the `R-U` adjacency after deleting either
or both selected edges, so this is genuinely a jointly persistent labelled
`K_7`-minus-one-edge model.

## 3. The two root-edge responses and their exact trace

The assignments `phi,psi` are checked on the complete deletion graphs, not
only on the displayed clique.  The first properly colours `G-va` with
`phi(v)=phi(a)`; the second properly colours `G-vb` with
`psi(v)=psi(b)`.  They consequently descend to the respective edge
contractions, which the verifier constructs explicitly and recolours.

For each edge deletion, six vertices of the literal `K_7` remain a clique.
For each contraction, the contracted image together with the other five
clique vertices is a `K_6`.  The supplied six-colourings therefore establish
all four exact equalities

```text
chi(G-va)=chi(G/va)=chi(G-vb)=chi(G/vb)=6.
```

Both responses assign colour one to `pA,pB,p1,p2,p3`, colour three to
`c2`, and colour four to `c3`.  Thus they agree literally, not merely up to
palette permutation, on the seven-boundary.  Giving `ell` colour five
extends this trace through the singleton closed shore.  The opposite closed
shore is the old graph and contains the displayed `K_7`, so no six-colouring
of it—and therefore no extension of this trace—exists.

## 4. Hall failure and the two further selected-trace probes

Under `phi`, the root `v` is a singleton branch set and has colour zero.
Its neighbours of colours three, four and five lie respectively in

```text
C1, C2, C2.
```

There are no other root neighbours of those colours.  The three-colour
subfamily therefore has only two possible first-hit labels, which violates
Hall's condition.  Since the root branch set is a singleton, these support
vertices are literal first hits; no hidden traversal inside the root bag is
being suppressed.

Deleting the internal edge `c3c4` admits the displayed six-colouring (4.2),
whose two ends are equal and which agrees literally with `phi` on the
boundary.  The verifier checks both the deletion colouring and the induced
contraction colouring.  The deletion retains a `K_6` obtained from the old
clique by omitting either `c3` or `c4`; the contraction has the contracted
image and the other five clique vertices as a `K_6`.  Hence both proper
minors are exactly six-chromatic.

The further colouring (4.3) properly colours `G-v`, agrees literally with
the same boundary trace, and uses six colours.  The six surviving vertices
of the old clique give the matching lower bound.  Thus both an internal
repeated-label edge probe and deletion of the repeated-exposure source can
preserve the selected trace.  The source correctly claims only that the
bare existence of these responses is insufficient; it does not claim that
the internal edge deletion preserves the old branch-set connectivity.

## 5. Trust boundary and verifier

The graph exits through the literal `K_7` already identified.  Moreover,
deleting `ell` leaves the original graph, which still contains that `K_7`
and is still seven-colourable by restriction of the displayed colouring.
Thus the host is not minor-minimal among seven-chromatic graphs.

Accordingly, the construction refutes only the local implication stated in
Section 1.  It is not a counterexample to a terminal-aware theorem using
`K_7`-minor exclusion and all proper-minor responses, and it is not a
counterexample to `HC_7`.

Running

```text
python3 barriers/hc7_same_bag_two_critical_edges_exact7_barrier_verify.py
```

at the audited revisions prints exactly

```text
GREEN same-bag exact-seven two-edge barrier: kappa=7, chi=7, shared trace, internal/root responses, Hall failure, explicit K7
```

No unresolved gap remains within the stated barrier scope.
