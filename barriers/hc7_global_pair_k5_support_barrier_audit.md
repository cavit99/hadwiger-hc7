# Audit of the global pair--`K_5` support barrier

## Verdict

**GREEN.**  The construction, exact support census, and rotation-triangle
plateau in
[`hc7_global_pair_k5_support_barrier.md`](hc7_global_pair_k5_support_barrier.md)
are correct in their stated scope.  The companion verifier was run
independently and returned its advertised GREEN result.

## 1. Exhaustiveness and pair counts

The graph is `G=K_2 vee I`, where the twelve-vertex icosahedron `I` has
thirty edges.  Its 91 unordered pairs split exactly as follows:

* 66 pairs contained in `I`, namely thirty edges and 36 nonedges;
* 24 apex--icosahedron pairs; and
* the one pair formed by the two apices.

For a proposed support bound `b`, every bag in a five-bag model has order at
most `b-4`, since the other four bags are nonempty.  The verifier enumerates
every connected subset of this maximum order in `G-P`, then every unordered
five-tuple of such bags, testing disjointness, pairwise adjacency, and total
support at most `b`.  Its recursive pruning uses only the necessary lower
bound of one vertex per unchosen bag.  It therefore loses no candidate
model.

The search finds support five for all 66 base pairs.  This is automatically
minimum because five nonempty bags require at least five vertices.  For each
of the 24 apex--base pairs it exhausts bounds five and six, finds no model,
and finds one at support seven.  For the apex pair, the remaining graph is
the planar icosahedron and hence has no `K_5` minor.  Thus the asserted
values `5`, `7`, and `infinity` are exact.

## 2. Rotation-state mapping

The verifier's labels agree literally with
[`hc7_global_invariant_rotation_triangle.md`](hc7_global_invariant_rotation_triangle.md):

* `C={3,4,8,9}` is `{u_3,u_4,w_3,w_4}`;
* the three non-apex fixed rows are `{1,6}=F_1`, `{2}=F_2`, and
  `{5,7,11}=F_3`; and
* the three centre/donor/missed-row triples are exactly `M_T`, `M_C`, and
  `M_0` from the rotation note.

For every state, it checks disjoint connected bags and exactly one missing
bag adjacency.  It then checks every literal pair across that missing
adjacency, not merely one representative, and obtains support value five.
The centre and donor also have the same union in all three states.  Hence
the claimed neutral plateau is established exactly.

## 3. Trust boundary

The example is six-colourable and is not seven-contraction-critical.  It
therefore refutes only a state-local monotonicity claim for `mu`; it does not
refute a criticality-enriched global exchange theorem.  Conversely, the
terminal pair is certified by planarity rather than by the exponential
search, which is a valid mathematical shortcut and is stated explicitly.
