# Order-eight near-full bipartition census

**Status:** reproducible diagnostic computation; separate internal audit GREEN
in
[`hc7_p2_nearfull_bipartition_census_audit.md`](hc7_p2_nearfull_bipartition_census_audit.md).
This is not a theorem and not evidence that `HC_7` is proved.

## Question tested

This census accompanies the
[two-vertex-shore contraction lemma](hc7_two_vertex_shore_bipartite_contraction.md).
For an eight-vertex boundary graph `H`, an ordered pair `(r,s)` records the
unique boundary vertex missed by each endpoint of the open-shore edge; the
symbol `FULL` records a boundary-full endpoint.  The program asks whether
there are

\[
 |Z|\le2,\qquad V(H)-Z=P\mathbin{\dot\cup}Q,
\]

such that `P,Q` are nonempty independent sets, `r` is not in `P` when the
first endpoint is not full, and `s` is not in `Q` when the second endpoint
is not full.  Such an oriented bipartition is exactly the finite condition
needed to apply the written contraction lemma.

## Exact finite universe

Run

```text
python3 active/hc7_p2_nearfull_bipartition_census.py
```

with nauty's `geng` on `PATH`.  The program enumerates one representative of
each of the 12,346 isomorphism classes of simple graphs on eight vertices.
It retains `H` when

\[
 \alpha(H)\le4,\qquad \chi(H)\le4.
\]

An ordered pair `(r,s)` is retained when one proper surjective
five-colouring of `H` exposes each non-full miss in a non-singleton colour
class, the two non-full misses are distinct, and

\[
 \alpha(H-r)\le3\quad\hbox{and}\quad\alpha(H-s)\le3
\]

for whichever misses are present.  Thus the enumeration is exhaustive for
this explicitly defined static universe, not for all possible operated
shore responses in a host graph.

The checked output is:

```text
graphs=12346
eligible_graphs=10460
eligible_instances=469852 by_miss_count={0: 10460, 1: 117796, 2: 341596}
incompatible_instances=209246 by_miss_count={0: 2514, 1: 39742, 2: 166990}
k4_minor_free_eligible_graphs=1116
k4_minor_free_eligible_instances=18844 by_miss_count={0: 1116, 1: 6446, 2: 11282}
k4_minor_free_incompatible_instances=520 by_miss_count={0: 0, 1: 0, 2: 520}
```

The count `520` is therefore reproducible, but it has a narrow meaning:
it counts ordered marked pairs on the chosen unlabelled graph
representatives.  It is neither an orbit count nor a count of labelled
graphs.

## Mathematical reading

Inside the `K_4`-minor-free subuniverse, every full/full instance and every
one-miss instance has a compatible oriented bipartition.  All 520 failures
have two distinct misses.  Combined with the separately checked fact that
every eight-vertex `K_4`-minor-free graph has an odd-cycle transversal of
order at most two, these are precisely the surviving bipartition-orientation
or parity conflicts for this finite model.

This does **not** show that any of the 520 marked configurations is realised
by the operated shore of a hypothetical counterexample.  Conversely, the
finite predicates omit eight-connectivity, `K_7`-minor exclusion, literal
opposite-shore geometry, and the named edge-deletion operation.  Those
host-level hypotheses must eliminate the residue or return the required
strict exact-seven response.
