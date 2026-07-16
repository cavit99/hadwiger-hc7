# Independent audit: attachment concentration for a repaired component

**Verdict:** GREEN for the exact theorem revision identified below.

**Audited source:**
`results/hc7_repaired_component_attachment_concentration.md`

**SHA-256:**
`054113fa7554a02f80d7deee7d392f925510ff089702c75d4ae8d226d028084a`

This audit covers both explicit minor models in Lemma 2.1, the exclusions of
the two exceptional linkage paths, the two-sector dichotomy, the use of the
seven-endpoint attachment theorem, and the first--last interval conclusion.

## 1. Normalized configuration

The six paths are pairwise vertex-disjoint and have twelve distinct named
ends.  Their internal vertices avoid both endpoint supports.  Consequently a
component of the complement of their union is disjoint from all endpoint
vertices as well as from every linkage path.  The only left-support edges
used later are among the displayed clique on `a0,a1,a2,a3`, the edge `xy`,
the three edges from `x` to `a0,a1,a2`, and `a3y`.  The only right-support
nonedge that any model must avoid is `pq`.

## 2. Attachments to `P3` or `P4`

Suppose first that the exterior component also attaches at
`v in P3-a3`.  Contracting a connected subgraph of the component that meets
the three attachment edges to `a3,x,v`, then contracting the `v`--`p`
segment toward `p` and the component image into `x`, preserves `a3,x,p` as
distinct vertices and creates the edge `px`.  The seven displayed branch
sets are disjoint and connected:

\[
 \{b_0\},\{b_1\},\{b_2\},\{r\},\{p\},
 \{x,q\},\{a_0,a_1,a_2,a_3,y\}.
\]

The first five singletons form a clique in the right support.  Their
adjacencies to the last branch set are supplied by `P0,P1,P2,P5,P3`, and
their adjacencies to `{x,q}` are supplied at `q`, except for `{p}`, where the
new edge `px` is used.  The last two branch sets meet through a displayed
left-support edge.  Thus all 21 pairwise adjacencies hold without using
`pq`.

For an attachment at `v in P4-x`, the symmetric contractions create
`a3q`.  The branch sets

\[
 \{b_0\},\{b_1\},\{b_2\},\{r\},\{q\},
 \{a_3,p\},\{a_0,a_1,a_2,x,y\}
\]

are again disjoint and connected.  The new edge `a3q` replaces the sole
missing right-support contact, while the six linkage paths and the displayed
support edges supply every other adjacency.  An independent endpoint-graph
check reconstructed and verified both seven-branch models.  The contractions
never identify two displayed branch sets, so both quotient models lift.

It follows exactly, not merely up to path interiors, that a `K7`-minor-free
host permits no neighbour of the component in `P3-a3` or `P4-x`.

## 3. Sector dichotomy

If the component meets `P5-y` and also meets `Pi-bi` for some
`i in {0,1,2}`, a shortest path through the component between the two
attachment vertices has all internal vertices in the exterior component.
It therefore satisfies every avoidance condition of the independently
audited clean-augmentation theorem.  That theorem gives a `K7` minor.
Hence, when `P5-y` is met, the only possible contacts on each of
`P0,P1,P2` are the endpoints `b0,b1,b2`; the preceding paragraph leaves
only `a3,x` on `P3,P4`.  This is precisely the first displayed sector.

If `P5-y` is not met, the only possible contact on `P5` is `y`; the same
`P3,P4` exclusions leave arbitrary contacts only on `P0,P1,P2`.  This is
precisely the second displayed sector.  The two alternatives cover every
linkage vertex because the six paths have disjoint vertex sets.

## 4. Endpoint bound and first--last interval

The independently audited seven-endpoint attachment theorem applies to the
whole connected exterior component.  Since it already meets `a3,x`, five
additional normalized endpoint contacts would give a `K7` minor.  Thus it
has at most six normalized endpoint neighbours in total.

When there are at least eight distinct linkage neighbours, at least two are
therefore path-interior vertices.  In the first sector every interior
contact lies on `P5`; moreover the five vertices outside `P5` in that sector
force at least three contacts on `P5`.  In the second sector only three
vertices lie outside `P0 union P1 union P2`, so at least five contacts lie on
those three paths; all path-interior contacts lie there, and pigeonhole gives
one path with at least two contacts.  In either case the first and last
contacts on a suitable oriented path delimit a nontrivial interval.

The source was narrowed during audit from saying that the choice of such a
path is “canonical” to asserting only the proved existence of a nontrivial
first--last interval.  Multiple members of `P0,P1,P2` can each have two
contacts, so no unique path choice follows from the hypotheses.

## 5. Scope

The theorem proves concentration for one connected component adjacent to
`a3,x`.  The leaf-block paragraph correctly uses the separately audited
seven-connectivity lemma only to obtain an order-seven separation at exactly
six linkage neighbours.  Neither result controls the relative order of a
second component's attachments.  The source therefore correctly leaves the
two-component composition step open and does not claim `HC7`.

## Unresolved assumptions or gaps

None within the stated attachment-concentration theorem.  The final
two-component crossing-or-separation assertion is explicitly identified as
unproved and was not assumed in this audit.
