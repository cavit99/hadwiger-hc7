# An aligned degree-eight pair forces a bilateral response cycle

**Status:** written proof; separate internal audit **GREEN** in
[`hc7_degree8_aligned_pair_bilateral_cycle_audit.md`](hc7_degree8_aligned_pair_bilateral_cycle_audit.md).
This result does not prove `HC_7`.

## 1. Setup

Let `G` be a finite simple graph such that

\[
 \chi(G)=7,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G. \tag{1.1}
\]

Let `u` have degree eight, put `S=N_G(u)`, and suppose that `G-N_G[u]`
has exactly two nonempty components `E,F`, each adjacent to every vertex
of `S`.  Suppose

\[
 S=I\mathbin{\dot\cup}T\mathbin{\dot\cup}\{p,q\},
 \qquad |I|=|T|=3,                                      \tag{1.2}
\]

where `I,T` are independent and `pq` is a nonedge.

These are exactly the aligned boundary data supplied outside the odd-wheel
exception by the audited
[degree-eight nonedge-bipartition classification](hc7_degree8_nonedge_bipartition_classification.md).

## 2. Bilateral paths with one operation provenance

### Theorem 2.1 (aligned bilateral response cycle)

There are proper six-colourings `c_E,c_F` of the two closed shores and
`p`--`q` paths `P_E,P_F` such that:

1. `c_E` and `c_F` induce, in some order, the two complete boundary
   partitions

   \[
                    I\mid T\mid\{p,q\},
       \qquad       I\mid T\mid\{p\}\mid\{q\};        \tag{2.1}
   \]

2. the open interior of `P_E` lies in `E`, and the open interior of `P_F`
   lies in `F`; each path meets `S` only at `p,q`;
3. both paths are failed lifts of the same boundary Kempe interchange,
   read in opposite directions; and
4. `P_E union P_F` is a literal simple odd cycle.

### Proof

Apply Lemma 1.1 of the audited
[concentrated-reserve response theorem](hc7_low_degree_concentrated_reserve_elimination.md).
For each closed shore, consider six-colourings in which `I,T` are distinct
exact boundary colour classes.  Both response sets are nonempty and their
possible equality types on `p,q` are opposite singletons.  Since the four
sets in (1.2) exhaust the boundary, the two equality types give exactly the
two complete partitions in (2.1).

Relabel the shores if necessary.  Independently permute their colour names
so that `I` has colour `a`, `T` has colour `b`, and `p` has colour `gamma`
in both colourings.  In `c_E`, let `q` also have colour `gamma`; in `c_F`,
let it have colour `delta`, where `delta` is absent from the merged
boundary colouring.  Thus changing only `q` from `gamma` to `delta` is a
boundary Kempe interchange on the singleton component `{q}` of the
`gamma`--`delta` boundary graph.  The vertex `p` is a different singleton
component because `pq` is a nonedge.

This interchange cannot lift through the `E`-shore: a lift would give the
split equality type there, contrary to the response dichotomy.  Hence the
full `gamma`--`delta` component of `c_E` containing `q` also contains `p`.
A shortest `p`--`q` path in that component is `P_E`.  No other boundary
vertex has colour `gamma` or `delta`, so its open interior lies in `E`.

Read the same interchange in reverse from `c_F`.  If it lifted through the
`F`-shore, that shore would realize the merged type.  Its full
`gamma`--`delta` component therefore also joins `p` to `q`, giving `P_F`
with open interior in `F`.  This proves items 1--3.

The paths have disjoint interiors and share only `p,q`, because `E,F` are
different components of `G-N[u]`.  Their union is consequently a simple
cycle.  Along `P_E` the endpoint colours agree, so its length is even;
along `P_F` they differ, so its length is odd.  The cycle is odd, proving
item 4. \(\square\)

## 3. A separating operation or doubled route

For `Q in {E,F}`, let `K_Q` be the full two-colour component in the fixed
colouring from Theorem 2.1 which contains `p,q`.  It meets the boundary
exactly in `{p,q}`.

### Theorem 3.1 (bridge or two edge-disjoint routes)

For each `Q in {E,F}`, exactly one of the following alternatives is
available.

1. A bridge `e` of `K_Q` separates `p` from `q`.  There is a proper
   six-colouring of `G-e` which induces on `S` the complete partition of
   the fixed opposite-shore colouring in Theorem 2.1.  The ends of `e`
   are monochromatic, so this is equivalently a colouring response of
   `G/e`.  It retains the named `p`--`q` boundary operation and the fixed
   opposite-shore path.
2. The graph `K_Q` contains two edge-disjoint `p`--`q` paths.

### Proof

Suppose first that a bridge `e` separates `p,q`.  Delete `e` and interchange
the two colours on the component of `K_Q-e` containing `q`.  This is proper:
the deleted bridge was the only two-colour edge between the two sides, and
edges to every other colour remain proper.  On the boundary, exactly `q`
changes colour.  The resulting complete partition is therefore the one
induced by the fixed opposite-shore colouring.  Align the colour names,
glue the two shore colourings, and give `u` a colour absent from the
four-colour boundary.  This gives the asserted colouring of `G-e`.

The ends of `e` are monochromatic after the one-sided interchange.  This
also follows from (1.1): if any six-colouring of `G-e` separated their
colours, restoring `e` would six-colour `G`.  Identifying the equal-coloured
ends gives the equivalent contraction response.  The opposite shore was
not recoloured, so its fixed path and the named operation provenance are
retained.

If no bridge separates `p,q`, the minimum size of an edge cut separating
them in the connected graph `K_Q` is at least two.  The edge form of
Menger's theorem gives two edge-disjoint `p`--`q` paths. \(\square\)

## 4. Exact residual in a hypothetical counterexample

Assume additionally that `G` is seven-connected and has no `K_7` minor.
For either path `P_Q` from Theorem 2.1, form the component-incidence graphs
`J_I(P_Q),J_T(P_Q)` on the same shore as in the audited
[parallel-cycle normalization](hc7_common_root_parallel_two_cycle_normalization.md#3-a-conditional-carrier-test).

### Corollary 4.1 (four incidence splits)

In a hypothetical counterexample, all four incidence graphs

\[
 J_I(P_E),\quad J_T(P_E),\quad J_I(P_F),\quad J_T(P_F)            \tag{4.1}
\]

split their named three-vertex block between at least two connected
components.  Equivalently, neither shore contains an `I`-carrier or a
`T`-carrier disjoint from the open interior of its aligned path.

### Proof

The independence bound `alpha(G[S])<=3` is part of the audited low-degree
entry.  It forces an `I`--`T` edge and makes each of `p,q` adjacent to at
least one vertex in each block.  Apply Corollary 3.2 of the parallel-cycle
normalization first to `P_E` and then with the shores interchanged to
`P_F`.  A connected incidence component containing all of either block
would supply the disjoint carrier and six-colour `G`. \(\square\)

## 5. Exact gain and limitation

Outside the odd-wheel boundary, the degree-eight classification and
Theorem 2.1 solve the operation-compatible endpoint-alignment problem:
the selected nonedge is realized by boundary-clean paths in both literal
shores, in two fixed colourings, and by one named Kempe operation.  This is
strictly stronger than the existence of an unrelated aligned pair or an
untagged path.

The result is not terminal.  In a surviving host, deleting either aligned
path interior splits both independent triples on that shore.  The bridge
alternative gives a named proper-minor response but not yet a common
colouring of the intact graph; the doubled-route alternative gives
edge-disjoint rather than vertex-disjoint routes.  Neither alternative
alone constructs a `K_7` model or an actual smaller component of
`G-N[u]`.  The unique boundary exception `K_1 vee C_7` is not treated.

The next degree-eight theorem should therefore close either the fourfold
incidence-split residue or the odd-wheel boundary, using seven-connectivity
and uncontracted `K_7`-minor exclusion.  Further static boundary response
enumeration cannot supply those missing host-geometric conclusions.

## Inputs

- [degree-eight nonedge-bipartition classification](hc7_degree8_nonedge_bipartition_classification.md)
- [opposite pair responses](hc7_low_degree_concentrated_reserve_elimination.md)
- [conditional incidence/carrier test](hc7_common_root_parallel_two_cycle_normalization.md)
