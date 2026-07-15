# Audit: bounded critical support-six kernels

**Verdict:** GREEN.

## 1. Critical-pair construction

For each member `A_i`, criticality supplies a transversal `P_i` of the
other members with order at most two.  If `P_i` met `A_i`, it would meet
the whole family, contradicting `tau(F)=3`.  Hence `A_i cap P_i` is empty,
while `P_i cap A_j` is nonempty for every `j!=i`.  Both cross-intersection
directions required by the symmetric set-pairs theorem follow by swapping
`i,j`.  The witness has order exactly two: a witness of order zero or one,
together with any vertex of `A_i`, would be a two-transversal of the whole
family.

## 2. Numerical bound

The Two Families Theorem is stated for upper bounds
`|A_i|<=a, |P_i|<=b`; with `a=6,b=2` it gives
`|F|<=binom(8,6)=28` directly.  No uniformization by dummy vertices is
being used.

Its unique equality characterization is precisely all complementary
`(6,2)` partitions of one eight-set.  The cited modern statement explicitly
records both the upper-bound formulation and uniqueness.

## 3. Corollary check

An inclusion-minimal subfamily with transversal number greater than two
has transversal number exactly three: after deleting a member, take its
two-transversal and add one vertex of the deleted nonempty member.  It is
therefore 3-critical.  The equality family lies inside eight vertices.
The host has at least nine vertices: a seven-connected graph of order
eight is `K_8`.  Extend the eight-set by one host vertex and apply the
independently audited nine-vertex closure.  The reduction from 28 to 27
is therefore valid only with that graph-global input.

## 4. Non-claims

The proof does not bound the ambient graph, make the 27 selected models
contraction-clean, or ensure that any three of them satisfy a published
clique-composition theorem.  Its value is a bounded irredundant witness
and the private-pair system (1.2), not an HC7 closure.
