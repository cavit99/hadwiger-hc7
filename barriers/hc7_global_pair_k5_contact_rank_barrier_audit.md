# Audit of the global pair--`K_5` contact-rank barrier

## Verdict

**GREEN, with “every pair” read as every eligible adjacent pair.**  The
construction and exact rank assertion in
[`hc7_global_pair_k5_contact_rank_barrier.md`](hc7_global_pair_k5_contact_rank_barrier.md)
are correct.  The companion verifier was run independently and returned its
advertised GREEN result.

## 1. Host and eligible-pair census

The verifier exhaustively checks connectedness after deleting every set of
at most six vertices, so the concrete host `G=K_2 vee I` is certified
seven-connected.  The two universal apices together with the thirty
icosahedron edges and 24 apex--base edges give 55 edges in total.  Deleting
the apex--apex edge's endpoints leaves the planar icosahedron and no `K_5`
minor, so this pair is ineligible.  The other 54 edges are exactly the
eligible pairs searched by the program.

The note's opening phrase “among every pair for which a `K_5` model exists”
should be interpreted within its stated setup `pq in E(G)`: nonadjacent
pairs are outside this edge-pole potential.  The subsequent statement that
all 54 other edges are eligible is exact.

## 2. Exactness of `(4,5,-8)`

For any eligible edge `pq`, five bags contacted by both poles would join
the singleton bags `{p},{q}` to form a `K_7` model.  Since this host is
`K_7`-minor-free, `c<=4`; trivially `u<=5`.  Thus `(4,5)` is the largest
possible first-two-coordinate profile.

For total support at most `b`, each of five nonempty bags has order at most
`b-4`.  The verifier enumerates every connected candidate bag of that size,
then every unordered disjoint pairwise-adjacent five-tuple within the support
bound.  Its pruning retains every possible tuple.  It proves, separately for
all 54 eligible edges, that no support-at-most-seven model has profile
`(4,5)` and that a support-eight model does.  Since no model can improve the
first two coordinates, the global lexicographic optimum is exactly
`(4,5,-8)`.

The two displayed witnesses were also checked independently by the script:
their bags are connected and disjoint, pairwise touch, have total support
eight, have four common-contact bags, and cover all five bags.

## 3. Trust boundary

The argument that `G` has no `K_7` minor is sound: after deleting the at most
two branch bags containing the apices, five pairwise adjacent branch bags
would remain in the planar icosahedron, yielding an impossible `K_5` minor.

The barrier establishes a static terminal sink for the numerical rank.  It
does not refute an exchange theorem using seven-contraction-critical
proper-minor responses, because this two-apex host is six-colourable.  The
rank also applies only after the sharp `(4,5)` profile has been reached; it
does not prove that every hypothetical counterexample admits that profile.
