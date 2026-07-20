# Independent audit of the two-vertex path-column census

**Verdict: GREEN.**

This audit checks

- `hc7_pentagonal_bipyramid_two_vertex_path_census.md` at SHA-256
  `f1c2f19509180ce61a8d01697ec1221a4e36168e41cc14032ac3a1f92914fe16`;
- `hc7_pentagonal_bipyramid_two_vertex_path_census_verify.py` at SHA-256
  `d707309335bca4a47760de7cf53cdaae61942e7a38f5a6c6f9d4f07d3e867210`.

## Encoding

The verifier has fourteen fixed vertices and sixty Boolean variables, one
for every possible edge between two columns adjacent in the pentagonal
bipyramid.  The seven internal path edges are fixed.  There are no
variables for forbidden quotient contacts, so every solver model has
exactly the host class stated in the theorem.  A positive disjunction on
each of the fifteen quotient edges enforces the other direction of the
exact contact condition.

The degree constraints count only inter-column edges and require at least
four of them at every vertex; the fixed internal edge then gives degree at
least five.  They are necessary for five-connectivity and therefore cannot
discard a theorem counterexample.

For every column and every four-element subsequence of its cyclic neighbour
order, the solver forbids both alternating orientations.  Portal variables
allow a label to occur at both endpoints, so repeated contacts are handled
without an implicit exclusivity assumption.

For an adjacent rim pair, all nonempty simple paths on its four vertices
occur among the enumerated permutations.  After choosing the first path,
the second is enumerated on every nonempty subset of the unused vertices.
The endpoint portal conditions and internal edge conditions are exact.
Consequently the conjunctions forbidden by the solver are precisely all
pairs of vertex-disjoint connected subgraphs required by the adjacent-rim
completion theorem, including singleton connected subgraphs and overlapping
portal sets.

## Counterexample-guided cuts

For a solver model with a cut `S` of order below five, each component `D`
of the complement must acquire an allowed edge to the other components in
every five-connected graph.  The connectivity disjunction added for `D`
is therefore necessary.  Adding it for every component remains sound.  If
there is no allowed crossing edge, that side of the search contains no
five-connected graph.

For a five-connected model, the auxiliary solver returns a proper
four-colouring when one exists.  Every graph not coloured by that fixed
assignment must contain at least one allowed inter-column edge with
equal-coloured ends.  The corresponding disjunction remains necessary even
if a later model deletes edges of the current model; it does not assume a
monotone supergraph search.  Fixed internal edges already have differently
coloured ends.  Thus the colouring cuts exclude no non-four-colourable
candidate.

The finite Boolean search either finds a five-connected non-four-colourable
survivor, which the script treats as a failed assertion, or eventually
returns exact Z3 `unsat`.  No timeout or `unknown` result is accepted.

## Reproduction and scope

Running

```text
python3 results/hc7_pentagonal_bipyramid_two_vertex_path_census_verify.py
```

returned

```text
pentagonal-bipyramid two-vertex path census: PASS
```

The result is complete for seven induced two-vertex path columns.  It does
not bound, suppress, or otherwise reduce larger columns, and it proves
four-colourability rather than planarity.  No unbounded conclusion or
claim about `HC_7` follows without a separate reduction to this finite
class.
