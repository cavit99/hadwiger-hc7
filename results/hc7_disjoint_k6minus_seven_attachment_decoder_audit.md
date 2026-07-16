# Independent audit of the seven-attachment decoder

**Verdict:** GREEN for the exact theorem and checker revisions audited.

## Audited revisions

- theorem file: `hc7_disjoint_k6minus_seven_attachment_decoder.md`
- theorem SHA-256: `b532339c299b1a28746a461bcf7d22d0171a5d59e3d88fac514c0824378d42dd`
- checker file: `hc7_disjoint_k6minus_seven_attachment_decoder.py`
- checker SHA-256: `bc5962664c39890717c0a411d0aa69be2500019f68cf388a5da20baebbb6a736`

After the mathematical audit, the theorem file was moved from `active/`
to `results/`; only its status metadata and documented invocation path were
updated.  The audited mathematical content and checker are unchanged; the
hashes above bind the final promoted revisions.

This audit covers the unbounded contraction lifts in Theorem 2.1 and
Corollary 3.1, both finite catalogues, the exact-search recurrence, and the
scope statements in Sections 4--5.

## Verifier replay

The documented command completed successfully under Python 3 and returned
the exact expected output:

```text
minimal_seven_attachment_sets 252
minimal_seven_attachment_orbits 72
certificate_digest 2b2b5f5b30bed58f598a3f491ec434682d3845951235cf0d710ddffd1ad368cb
six_attachment_positive_sets 203
six_attachment_negative_sets 7
six_attachment_negative_orbits 3
five_of_six_interior_rail_projections 6
mixed_site_sets 4368
mixed_projection_resistant_sets 41
mixed_actual_negative_sets 21
mixed_actual_negative_orbits 4
mixed_status_digest 24c1fc7e8b81591d71c7d0dc701f867d0682f8bad19a9a60161fbf1df96195d7
two_vertex_contact_distributions 551124
GREEN: endpoint saturation and projection checks verified
```

## Checks performed

### 1. Exact order-thirteen search

For a seven-branch model on at most thirteen vertices, if `s` bags are
singletons then `s>=14-n`.  The checker tries every possible singleton
clique for every admissible `s`, then every family of pairwise disjoint,
connected, mutually adjacent non-singleton vertex sets of order at least
two.  Its candidate-size upper bound is exactly the number of remaining
vertices after reserving two for every other non-singleton bag.  Unused
vertices are permitted.  Consequently `find_k7_model` is exhaustive, not
merely a search for spanning models.

The reconstructed branch sets in all 252 seven-contact cases are checked
again for nonemptiness, disjointness, connectivity, and pairwise adjacency.
The same exact search establishes all 203 positive and seven negative
six-contact cases.  The three displayed negative orbit types expand to
exactly those seven labelled cases.

### 2. Low-degree recurrence

In a `K_7` model, a vertex of degree below six cannot be a singleton bag.
Such a vertex is therefore either unused, giving the deletion branch, or
lies in a non-singleton connected bag containing an incident edge, giving
one of the contraction branches.  This proves the deletion/contraction
recurrence in both directions.  For every generated graph above order
thirteen, the run-time assertion verifies that a degree-below-six vertex is
available; structurally, an as-yet-unsuppressed subdivision vertex has
degree at most three.  Thus the recurrence reaches the exhaustive
order-thirteen search and proves negative as well as positive outcomes.

### 3. Contraction lifts

A connected off-linkage subgraph can be contracted to one vertex without
identifying any linkage endpoint.  The six internally disjoint linkage
paths can independently be shortened until their named ends are adjacent.
Choosing five distinct additional endpoint contacts therefore gives one of
the 252 verified quotient minors.  Extra contacts and edges can be deleted,
so Theorem 2.1 lifts correctly to the host graph.

For Corollary 3.1, the designated endpoints
`a0,a1,a2,p,q,y` are pairwise distinct and avoid the fixed vertices
`a3,x`.  Contracting the terminal subpath from each selected interior
attachment toward its designated endpoint creates five distinct additional
endpoint contacts while retaining the two fixed contacts.  Internal
disjointness of the paths makes these contractions compatible.  The six
once-subdivided projections replay this lift directly.

### 4. Mixed-site catalogue

There are `binom(16,5)=4368` endpoint/midpoint site sets.  Every midpoint
orientation is tested before exact search.  Of the 41 projection-resistant
sets, the actual subdivided graph is tested by the exact recurrence; the 21
negative sets are exactly the four displayed orbit forms, with labelled
counts `6+6+6+3`.  An uncontacted degree-two subdivision can be suppressed
without changing the conclusion: the same low-degree argument places it in
the deletion/contraction recurrence.  Thus representing only selected
midpoints does not omit another negative configuration.

### 5. Distribution and scope claims

The `252*3^7=551124` two-vertex distributions are all checked after
contracting the edge joining the two carrier vertices; every result is
exactly the corresponding verified star quotient.  This justifies the
arbitrary connected-subgraph extension because contraction depends only on
the union of endpoint neighbourhoods.

The final residue is stated only as a necessary concentration condition.
The note correctly refrains from extending the one-subdivision catalogue to
arbitrarily long paths and does not claim a bounded separator or a complete
solution of the exceptional linkage.

## Unresolved assumptions or gaps

None within the stated quotient and contraction results.  The stable-
rerouting premise mentioned conditionally in Section 5 is external to this
theorem and was not re-audited here.
