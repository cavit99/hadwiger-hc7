# Audit of the adjacent defect-one carrier barrier

**Verdict:** GREEN.

**Audited source:**
`barriers/hc7_order8_adjacent_defect_one_carriers_barrier.md`

**Audited source SHA-256:**
`c293b2c1910a491a0774090baeaaa7b204f193a1131d539f2b030aa75f92c360`

**Verifier:**
`barriers/hc7_order8_adjacent_defect_one_carriers_barrier_verify.py`

**Verifier SHA-256:**
`24212f718a6c4c73e2e2a70c5ab05f17030d2742eb87b08352ebc1823803dde7`

**Audit type:** independent internal mathematical and verifier audit.  This
is not external peer review and is not a counterexample to `HC_7`.

## Construction check

The graph has the claimed twelve vertices.  Its boundary is exactly two
disjoint triangles plus two isolated vertices.  The vertices `Q_0,Q_1`
are adjacent to all eight boundary vertices.  Vertex `A` misses only
boundary vertex `0`, vertex `B` misses only boundary vertex `3`, and those
missed vertices lie in different triangles.  The edge `AB` is present and
there is no other edge among the four added vertices.  Thus the graph
exactly satisfies the refuted contact-only hypotheses.

The example models the adjacent-carrier abstraction obtained by assigning
the two cut vertices to opposite lobes.  The source now says this explicitly
and does not claim that the raw lobe interiors, which are anticomplete, are
the adjacent vertices of the quotient.

## Width certificate

An independent reconstruction reproduced every later-neighbour set in the
displayed elimination order.  The maximum later-neighbour order after fill
is five.  The filled graph is chordal with clique number at most six, so the
original graph has treewidth at most five.  Treewidth is minor-monotone and
`tw(K_7)=6`; therefore the graph has no `K_7` minor.

## Verifier check

The verifier constructs exactly the displayed graph, checks the four
boundary contact sets and `AB`, performs the fill process, compares all
later-neighbour sets with the certificate, and checks width five.  Its
exact output is

```text
vertices=12
defects=A:{0} B:{3} full=Q0,Q1 edge=AB
elimination_order=0,6,7,1,2,3,4,5,8,9,10,11
elimination_width=5
K7_minor=no (treewidth at most 5)
```

The ordered fill loop preserves symmetry: both orientations of every pair
of later neighbours are visited.

## Trust boundary

The graph is not seven-connected, seven-chromatic, or contraction-critical
and has no operation-specific response colouring.  In particular, its two
isolated boundary vertices have degree four in the full graph, and the
width-five certificate also makes it six-colourable.  The example refutes
only the static contact-and-adjacency implication.  No mathematical or
computational gap was found within that scope.
