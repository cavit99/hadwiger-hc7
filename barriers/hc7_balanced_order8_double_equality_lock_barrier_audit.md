# Independent audit of the balanced order-eight double-equality barrier

**Verdict:** **GREEN** for the exact revisions identified below.

**Audit date:** 2026-07-17

**Audited barrier note:**
`hc7_balanced_order8_double_equality_lock_barrier.md`, SHA-256
`ecf1e83a16d2df1e107be842b34baa4b0d37d760b2f1186e88a5397dc8a8ad22`.

This revision differs from the originally audited note only in its status
paragraph: the pending-audit wording was replaced by a link to this GREEN
audit.  Reversing that single metadata edit reproduces the previously
audited SHA-256
`bf3ec799db3434d0ee9523565df8c2a7556a053891f6b3e5696923b7b8384506`.
No theorem statement, construction, verifier claim, or trust boundary
changed.

**Audited verifier:**
`hc7_balanced_order8_double_equality_lock_barrier_verify.py`, SHA-256
`6e66773bd9ab4d0df27d0d0f2888e56c24d28ab31fb0e5c6390f026cde0fca05`.

This is a separate internal audit, not external peer review.

## Verdict

The 19-vertex graph has every property claimed in the barrier note.  In
particular, the displayed simultaneous-equality colouring cannot be
repaired by a single boundary-preserving Kempe interchange, its boundary
partition occurs in neither one-edge-restoration language, and the two
restoration languages have no common boundary partition or one-step Kempe
transition.  The fixed-boundary list-critical core is planar but is not a
Gallai tree.

The stated trust boundary is essential and correctly recorded: the graph
contains a `K_7` minor, is not minor-minimal, and has the same-index rooted
linkage which is absent in the canonical-web case.  The example therefore
refutes only a local double-equality-repair principle.  It is not a
counterexample to `HC_7` and does not refute an argument using all three of
`K_7`-minor-freeness, minor-minimality, and the canonical missing linkage.

## Hand audit

### Separation and boundary data

The construction partitions the vertex set as

```text
A_open = {a,b,pa,qa,pb,qb}
S      = {t0,t1,t2,ap,u,bp,v,x}
B_open = {c,d,y0,y1,y2}.
```

All `A_open`--`B_open` edges are explicitly forbidden.  The induced open
shores are connected, nonempty, and each has a neighbour at every literal
vertex of `S`.  Exhaustive deletion of every set of at most seven vertices
leaves the graph connected, while deleting `S` separates the two open
shores.  Thus the graph is exactly eight-connected and the displayed
separation is an actual order-eight separation with exactly two
`S`-full open components.

Direct edge checks verify the triangle `R`, the anticomplete boundary edges
`ap-u` and `bp-v`, their collective contacts with the original five-clique,
and the required disjoint nonempty endpoint-nonneighbour sets in `R`.  The
sets

```text
R union {a,b} and {c,d,y0,y1,y2}
```

are disjoint five-cliques in the asserted shores.  The connected residual
set `{pa,qa,pb,qb}` has boundary neighbourhood exactly `S-{t2}`.  Finally,
the four nonedges `t0-x,t1-u,t2-v,ap-bp` cover `S`, and hence form the
claimed perfect matching in the complement of the boundary graph.

### Chromatic number, response languages, and minors

Fixing the three colours of the triangle loses no six-colourings, since
the colours on a triangle can always be globally relabelled.  The exhaustive
search finds no six-colouring of the full graph, and the displayed proper
seven-colouring proves `chi(G)=7`.

The three displayed target colourings certify six-colourability of `G-g`,
`G-h`, and the simultaneous contraction `G/g/h`: for the last assertion,
the colouring of `G-{g,h}` assigns equal colours to both contracted endpoint
pairs and therefore descends to the contracted graph.  Enumeration after
normalising the triangle gives exactly 24, 342, and 792 six-colourings of
`G-g`, `G-h`, and `G-{g,h}`, respectively.  The last family splits as

```text
(g equal,  h proper):  24
(g proper, h equal):  342
(g equal,  h equal):  426
(g proper, h proper): 0.
```

The two one-edge-restoration families induce respectively two and twelve
boundary partitions, with empty intersection.  A separate five-colour
search and the explicit six-colouring show that the common deletion is
exactly six-chromatic.  The displayed six branch sets were checked for
connectedness, disjointness, and every pairwise adjacency, so they give the
claimed `K_6` minor in the common deletion.

### The locked simultaneous-equality colouring

The displayed colouring is proper on `G-{g,h}` and has the stated boundary
partition.  Exhaustive comparison with both response languages confirms
that this partition extends to neither one-edge restoration.

For `g=ab`, the endpoints lie in one bichromatic component in the closed
`A`-shore for alternate colours `0,1,2,4`.  For alternate colour `5`, their
components are disjoint but meet the boundary in exactly `{bp,v}` and
`{ap,u}`.  Switching either component would therefore alter the literal
boundary equality partition; switching both does not separate `a` and `b`.
For `h=cd`, the endpoints lie in one bichromatic component for every
alternate colour.  This proves the claimed elementary local lock.

The verifier constructs every one-component Kempe interchange in the common
deletion, globally renormalises the triangle colours, and compares the
result with the complete opposite response family.  No colouring of one
response family is one Kempe interchange from a colouring of the other.
This assertion concerns a standard single-component Kempe interchange; it
does not claim that the two response families lie in different connected
components of the full Kempe-reconfiguration graph.

### Fixed-boundary list-critical core

The open `A`-shore is exactly `\overline{K_2}\vee P_4`, and hence is planar.
For the locked boundary colouring, the induced fan on
`{a,b,pa,pb,qa}` has the lists stated in the note.  An independent direct
case split agrees with the exhaustive check: whichever of the two colours
is assigned to the hub `qa`, both `a` and `b` are forced to colour `3`, so
the edge `ab` cannot be coloured properly.

Deleting any one vertex, or deleting `ab`, makes this list instance
colourable.  Thus it is a minimal fixed-boundary list-critical core.  It is
two-connected, has degree sequence `4,3,3,2,2`, and is neither a clique nor
an odd cycle, so it is not a Gallai tree.  Three of its vertices have degree
strictly larger than their list size.  The example therefore correctly
blocks applying the degree-choosability theorem without first proving
degree--list-size equality throughout the critical core.

## Trust-boundary audit

The seven displayed branch sets form a `K_7` minor; their connectedness,
disjointness, and all pairwise adjacencies are checked directly.  Deleting
`u` leaves no six-colouring, while the displayed seven-colouring restricts
to that deletion, so the graph is not minor-minimal.

After contracting `ap-u` and `bp-v` and deleting `R`, the two disjoint paths

```text
a-x-z_e and b-qa-z_f
```

join the same-index root pairs.  Every edge of their literal preimages is
checked.  Consequently the canonical rooted-web missing-linkage hypothesis
fails exactly as claimed.

## Verifier audit

The verifier was read in full and its construction agrees with the written
definition.  Its colouring search is exhaustive: at every step it branches
over every colour not used on an already coloured neighbour, using only a
choice of variable order as a search heuristic.  The connectivity loop
tests every deleted vertex set of order zero through seven.  The Kempe loop
enumerates every colour pair and every connected component of the induced
two-colour graph.  The branch-set checker separately verifies connectivity,
disjointness, and all required adjacencies.

Running

```text
python3 barriers/hc7_balanced_order8_double_equality_lock_barrier_verify.py
```

completed with:

```text
balanced order-eight double-equality lock barrier: verified
vertices=19 edges=105 connectivity=8 chromatic_number=7
fixed-triangle six-colourings: G-g=24 G-h=342 H=792
response partitions: 2 versus 12, with empty intersection
planar leaf side: minimal fixed-boundary core is not a Gallai tree
trust boundary: contains K7; non-minimal; canonical missing linkage fails
```

## Exact retained scope

The audited example shows that exact balanced boundary geometry, two named
five-cliques, opposite critical edges, all three local response types,
eight-connectivity, and planar fixed-boundary criticality do not by
themselves force local double-equality repair.  A valid continuation must
use at least one genuinely global ingredient excluded here, such as the
canonical missing linkage together with `K_7`-minor-freeness or
minor-minimality.  No conclusion about a genuine minimal `HC_7`
counterexample is drawn from this finite barrier.
