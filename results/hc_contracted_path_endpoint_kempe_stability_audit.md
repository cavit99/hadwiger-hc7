# Audit of the endpoint Kempe-stability criterion

**Verdict:** GREEN (internal proof replay; not external peer review)

**Audited theorem revision:** SHA-256
`ece6f1009bf29f238c7c77ea05290867d92591a38b1241e9984137ab19032269`
of `hc_contracted_path_endpoint_kempe_stability.md`.

## Checks performed

The components of the subgraph induced by two fixed colours do not change
as vertex sets when either colour is interchanged on one component.  If a
component contains neighbours of both colours at the external vertex,
those two neighbours exchange colours together, so that component alone
keeps both colours present after every sequence of interchanges.

If no component is mixed, the components meeting an `a`-coloured
neighbour and those meeting a `b`-coloured neighbour are disjoint
families.  Switching exactly the first family changes every `a`-neighbour
to colour `b`; no switched component contains a `b`-neighbour which could
change to `a`, and no unswitched component contains an `a`-neighbour.
Thus the necessity argument removes colour `a` exactly as claimed.

The two-vertex corollary is only the conjunction of the two individual
universal statements.  It correctly warns that the two witnessing
components need not coincide.  No clique-minor or separator conclusion is
asserted.

## Scope

This audit checks the local equivalence only.  It does not promote
pairwise component data to a quasi-clique model or identify colour classes
with prescribed branch sets.
