# Audit: independent two-defect four-bag barrier

## Verdict

**GREEN** at the exact revisions

```text
2135ac4c04ee8a592c997237be0dd103207761de95638b47c632b8f9577e5696  barriers/hc7_degree8_independent_two_defect_four_bag_barrier.md
051a718541ea0d7e2106cafe0f7e8dae807b3711fefaa3c260278616d80a1252  barriers/hc7_degree8_independent_two_defect_four_bag_barrier_verify.py
```

This is a separate internal audit, not external peer review.  The example
refutes exactly the independent-defect four-bag claim stated in the source.
It does not refute `HC_7`, the common-defect four-bag theorem, or a theorem
that uses the omitted host-level colouring and provenance hypotheses.

## Construction and hypotheses

The graph6 string `GCOcaO` decodes to the asserted disjoint union

```text
K3[0,3,6] + K3[1,4,7] + K2[2,5].
```

Choosing one vertex from each component shows that its independence number
is three.  After deleting any two boundary vertices, every remaining
component has at most three vertices, so the remaining graph cannot contain
a `K_4` minor.  This proves both boundary hypotheses of the refuted claim.

The constructed host has thirteen distinct vertices and forty-one edges:
seven boundary edges, eight edges from `u` to the boundary, twenty-four
bag--boundary edges, and the two same-shore edges.  Each of the four
singleton bags is connected, the bags are pairwise disjoint and outside
`S union {u}`, and its exact boundary nonneighbour set is the displayed
two-set.  Thus every premise of the false strengthening is met literally.

For completeness, the scope disclaimers are also correct.  Boundary
vertices `1,5,7` have degree five, so the host is not seven-connected.  The
five independent colour classes

```text
{0,1,2}, {3,4,5}, {6,7}, {u,e0,f0}, {e1,f1}
```

give a proper five-colouring, so the host is not seven-chromatic and cannot
be a minor-minimal `HC_7` counterexample.

## Four-anchor predicate

The verifier ranges over every boundary edge `rs` and every ordered choice
of four distinct anchors outside `{r,s}`.  For each bag it requires its own
anchor to avoid that bag's missed set.  For each cross-shore bag pair it
then requires one bag to see the other anchor or the two anchors to be
adjacent in the boundary.  For each bag and each of `r,s`, it requires a
direct bag contact or an anchor--singleton boundary edge.

Together with the two assumed same-shore edges and the six automatic
adjacencies from `u` to the selected boundary vertices, these are exactly
the twenty-one adjacencies among the seven proposed branch sets.  The
enumeration is complete for this certificate form and finds zero such
certificates.  This supplementary check is not used to infer global
`K_7`-minor exclusion; that is established by the exact solver below.

## Contraction-only `K_7` solver

The solver's contraction-only recurrence is complete for a connected host.
Given any `K_7`-minor model, every component outside its branch sets can be
assigned to an adjacent branch set, so the seven connected branch sets may
be assumed to cover every host vertex.  If the host has more than seven
vertices, one branch set contains an edge; contracting that edge preserves
the model.  Conversely, a `K_7` minor after an edge contraction lifts to
one before the contraction.  At order seven, a `K_7` minor exists exactly
when the graph itself is complete.  Induction therefore justifies trying
every edge contraction until seven vertices remain, with no deletion
branch.

The implementation preserves precisely the union of the two contracted
neighbourhoods, removes loops, and relabels all retained vertices.  Edge
contraction preserves connectedness, so the checked precondition remains
valid recursively.  Memoisation removes repeated labelled states without
identifying any inequivalent state.  The `K_7`, subdivided-`K_7`, and `K_6`
controls exercise both the terminal test and a nontrivial positive
contraction.  The displayed host reaches 99,925 cached states and no
complete seven-vertex contraction.

As an independent cold cross-check, a separate exact encoding assigned all
thirteen vertices to seven nonempty connected branch sets and required an
edge between every pair of sets.  That formulation was unsatisfiable,
agreeing with the contraction search.

## Verifier replay

All substantive checks use the always-active `require` function.  Ordinary
and optimized runs produced identical output:

```text
python3 barriers/hc7_degree8_independent_two_defect_four_bag_barrier_verify.py
python3 -O barriers/hc7_degree8_independent_two_defect_four_bag_barrier_verify.py

boundary GCOcaO: K3 + K3 + K2; alpha=3; compact
missed_sets E0=37 E1=05 F0=17 F1=16
anchor_certificates 0
solver_controls K7=True subdivided_K7=True K6=False
host vertices=13 edges=41 contraction_states=99925 K7_minor=False
PASS independent_two_defect_four_bag_barrier
```

No unresolved issue remains within the barrier's stated scope.
