# Independent audit of the same-bag exact-seven two-edge barrier

**Verdict:** **GREEN** at the exact source and verifier revisions recorded
below.  The construction has all hypotheses of the intermediate statement
it refutes, neither proposed local conclusion, and the two global defects
stated in its trust boundary: it contains an explicit `K_7` and is not
minor-minimal.

This is a separate internal mathematical audit, not external peer review.

## Exact revisions audited

```text
aa4e557365cc35621753d8df9f630ca2703d6a0b4da67dd803db834e7529cc28  barriers/hc7_same_bag_two_critical_edges_exact7_barrier.md
036f43ff06b787a611376e6926297fa9a177227a874413382a02f6a1bba8d85a  barriers/hc7_same_bag_two_critical_edges_exact7_barrier_verify.py
```

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

The verifier separately checks the second displayed model.  Its bags are
connected, disjoint and spanning, and its unique missing adjacency is again
`Y1,Y2`.  In this model `va` joins `R` to `A`, while `vb` joins `R` to the
distinct label `B`; `vpA` and `vpB` retain the respective model adjacencies
after the common deletion.  Thus the same graph verifies both the
same-outer-label and distinct-outer-label formulations claimed by the
source.

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

There are no additional endpoint signatures or boundary partitions hidden
by the two selected responses.  After fixing distinct colours on the
`K_6`

```text
a b c1 c2 c3 c4,
```

the verifier exhausts every assignment of the remaining vertices.  Fixing
this clique loses only the global permutation of the six colour names, so
the search covers every six-colouring of the common deletion.  It returns
exactly six normalized colourings: three of signature `EP` and three of
signature `PE`.  All six induce the same complete equality partition

```text
{pA,pB,p1,p2,p3} | {c2} | {c3}.
```

The absence of `EE` and `PP` also follows directly.  The displayed `K_6`
uses all six colours, while `v` is adjacent to its four `c` vertices and
nonadjacent to `a,b`, so `v` receives exactly one of the colours on `a,b`.
Under `phi`, the colour-zero/colour-two component containing `v` is the
singleton `{v}`; switching it produces `psi`.  This is the claimed
one-step Kempe transition.

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

For the second branch-set model, all three colours have the sole first-hit
label `C`.  Hence the Hall failure persists—and is stronger—even though
the two selected response edges enter the distinct labels `A,B`.

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
GREEN shared-portal exact-seven two-edge barrier: kappa=7, chi=7, same/distinct outer labels, shared trace, internal/root responses, Hall failure, explicit K7
```

No unresolved gap remains within the stated barrier scope.
