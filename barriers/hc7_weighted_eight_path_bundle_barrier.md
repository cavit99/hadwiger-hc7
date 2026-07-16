# Barrier: eight model-good paths do not compose three split bags

**Status:** explicit counterexample to the abstract path-composition lemma;
not a counterexample to `HC_7`.

The weighted matching-deletion theorem suggests trying to strengthen the
published three-clique path argument by obtaining eight disjoint good
paths between three support-six `K_5` models.  That local statement is
false even when all path endpoints are distinct literal vertices at each
support.

## Construction

Take three disjoint supports

```text
A = (a0,a1,a2,a3,xA,yA)
B = (b0,b1,b2,b3,xB,yB)
C = (c0,c1,c2,c3,xC,yC).
```

In each support the first four vertices form a clique and `xY-yY` is the
split edge.  Add these singleton contacts:

```text
A: xA-a0, xA-a1, xA-a2, yA-a3
B: xB-b0, xB-b2, yB-b1, yB-b3
C: xC-c2, xC-c3, yC-c0, yC-c1.
```

Thus each split edge is collectively adjacent to its singleton `K_4`,
and both complementary defect sets are nonempty.  Add eight disjoint
model-good paths, represented here by their direct connector edges:

```text
a0-c2, a1-yB, a2-c3, a3-xB,
xA-c1, yA-c0, b1-yC, b2-xC.
```

The path-type multiplicities are `AB=2, AC=4, BC=2`; the numbers of
distinct support vertices used are `(6,4,6)`.  Every endpoint is used at
most once.

## Why there is no `K_7` minor

The graph has a fill-elimination order of width five.  The later-neighbour
sets after each fill step are:

```text
b0: b1 b2 b3 xB
b3: b1 b2 xB yB
yA: a3 xA c0
b1: b2 xB yB yC
b2: xB yB xC yC
xB: a3 yB xC yC
yB: a1 a3 xC yC
a0: a1 a2 a3 xA c2
a2: a1 a3 xA c2 c3
xC: a1 a3 c2 c3 yC
a1: a3 xA c2 c3 yC
a3: xA c0 c2 c3 yC
xA: c0 c1 c2 c3 yC
c0: c1 c2 c3 yC
c1: c2 c3 yC
c2: c3 yC
c3: yC
yC:
```

Hence the graph has treewidth at most five.  Since treewidth is
minor-monotone and `tw(K_7)=6`, it has no `K_7` minor.  If each connector
edge is subdivided to retain a literal internal path vertex, append a
three-vertex bag consisting of its two ends and its subdivider; the width
bound is unchanged.

The adjacent verifier reconstructs the graph, checks every support and
connector condition, and replays the fill certificate.

## Minimality and consequence

Eight paths use sixteen endpoints among the eighteen support vertices.
Their support-degree profile is therefore, up to order, `(6,6,4)` or
`(6,5,5)`.  Every irredundant split support has at least eleven edges:
six in its singleton clique, the split edge, and at least four collective
contacts.  Thus a direct-connector instance has at least

\[
                         3\cdot11+8=41
\]

edges.  The displayed graph has exactly 41, so it is edge-minimum among
instances with these declared ingredients.

Therefore no proof may replace the weighted-order-eight residue by the
claim that eight ordinary model-good paths automatically compose.  A
positive theorem must additionally use the exact punctured-cube coloring
signatures, ambient attachments forced by seven-connectivity, or a
state/model-preserving weighted cut.
