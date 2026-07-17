# Internal audit of the selected Kempe-fan barrier

**Audit status:** GREEN — the written counterexample and deterministic
verifier were independently checked.

**Audit date:** 2026-07-16

**Audited barrier note:**
`hc7_order_eight_selected_kempe_fan_barrier.md`, SHA-256
`78f9871ff145c9ac6cc3228723c7e26d1acd5a78364e9d65bd2595ddf740d74d`.

**Audited verifier:**
`hc7_order_eight_selected_kempe_fan_barrier_verify.py`, SHA-256
`4f5def0208adda5ed5d73dc5d07373107bbf07f89b1ca1e309c6f75a59f6ba3f`.

This is a separate internal audit, not external peer review.

## Verdict

The example has every property claimed in the note and refutes precisely
the selected-colouring strengthening stated there.  In particular, the two
opposite deletion colourings and their five internally disjoint root-paths
do not force a `K_7` minor, an order-seven boundary from the displayed
two-colour component, or a `K_5`-minor transversal consisting of the two
nominated roots.

The example deliberately fails universal colour saturation on the common
host.  It therefore does not refute the universal-saturation theorem, any
argument which uses the full space of six-colourings, the stated global
terminal alternatives, or `HC_7`.

## Hand audit

### Ambient graph

The edges in (2.1) give the standard planar icosahedral graph `I`: the two
five-cycles, their ten cross edges, and the two poles have 12 vertices and
30 edges.  Its standard five-connectivity is also verified exhaustively by
the script.  In `G=K_2 join I`, deletion of fewer than seven vertices leaves
a universal apex unless both apices were deleted; in the latter case at
most four vertices were deleted from `I`, whose remainder is connected.
Thus `G` is seven-connected.

In any `K_7`-minor model in `G`, at most two branch sets can contain one of
the two added apices.  At least five remaining branch sets would lie wholly
in `I` and would form a `K_5` minor there, contrary to planarity.  The same
argument shows that every `K_5`-minor model in `G` meets `{p,q}`.  These
arguments remain valid if both apices occur in one branch set, since then
even more than five branch sets remain in `I`.

### Exact order-eight structure and near-clique model

For the displayed set `S`, direct inspection gives `|S|=8`, the triangle
`R`, the two edges `e,f`, their mutual anticompleteness, and the required
collective contacts with `R`.  Deleting `S` leaves exactly the connected
sets

```text
{u3,u4,w3,w4} and {u1,w1}.
```

Each has a neighbour at every literal vertex of `S`.  Thus this is an
actual order-eight separation, not only a quotient configuration.

The seven sets in (3.4), together with `{u0}` and `{u2}`, are disjoint,
connected, and span `G`.  Every pair is adjacent except the two singleton
roots.  Hence they form the claimed spanning `K_7`-minus-one-edge model.

After deleting the roots, the lower five-cycle together with `d` is a
four-chromatic odd wheel.  The adjacent vertices `p,q` are complete to it
and require two additional colours.  The displayed colouring gives the
matching upper bound, so the common host is exactly six-chromatic.

### Colourings, paths, and separators

Both tables (4.1) and (4.3) are proper six-colourings of the asserted
vertex-deleted graphs.  In the first, `b` misses its own colour while `a`
sees all six colours; in the second the roles reverse.  Every displayed
path uses existing edges.  After the uncoloured deleted root is omitted,
the remainder of each path uses the retained root colour and the indicated
second colour.  Within each of the two five-path systems, path interiors
are pairwise disjoint.  The note does not claim that all ten path interiors
from the two different colourings are simultaneously disjoint.

For colouring (4.1), the `{2,3}` component containing `b` is exactly
`{u2,w0,w1}`.  Its open neighbourhood in the original graph is the listed
nine-vertex set.  Removing that neighbourhood leaves this component and
the edge `{u4,w3}`, so it is an actual order-nine separator and does not
instantiate the desired order-seven return.

Colouring (5.1) is proper on the common host.  Root `a` misses colour one
and root `b` misses colour two; because the roots are nonadjacent, assigning
those colours to them extends the colouring to all of `G`.  This directly
certifies the failure of universal saturation.

Finally, `{p,q,t,u3,u4}` is a literal `K_5` disjoint from the nominated
roots.  Conversely `{p,q}` is a valid `K_5`-minor transversal by planarity
of `I`, and deleting the seven vertices in (5.3) separates `t` from the
connected lower wheel.  The example therefore retains, rather than
refutes, the allowed global outcomes.

## Verifier audit

The verifier was read in full.  Its graph construction agrees with (2.1)
and (2.2).  The face list gives 20 triangular faces, every one of the 30
icosahedral edges occurs twice, all vertex links are cycles, and Euler's
formula is satisfied.  The exhaustive deletion loops test five-connectivity
of `I` and seven-connectivity of `G`.  Subsequent assertions check the
separator components, all literal boundary contacts, all branch-set
adjacencies, properness and palettes of all three colourings, every path
edge and within-system disjointness, both claimed separator component
sets, and the literal `K_5`.

From the repository root,

```text
python3 barriers/hc7_order_eight_selected_kempe_fan_barrier_verify.py
```

completed with:

```text
icosahedron certificate: 12 vertices, 30 edges, 20 triangular faces
connectivity checks: I is 5-connected; G is 7-connected
exact boundary components: [['u1', 'w1'], ['u3', 'u4', 'w3', 'w4']]
spanning near-K7 bag orders: [1, 1, 4, 5, 1, 1, 1]
exclusive fan paths: 5 + 5, internally disjoint in each witness
selected {2,3}-component boundary order: 9
universal saturation: explicitly false
ALL CHECKS PASSED
```

## Scope retained

The audited barrier concerns a finite selected-data principle.  Its
deletion-root paths have an uncoloured endpoint, as the note explicitly
explains; they are not Kempe chains in a proper colouring of all of `G`.
Most importantly, the graph is six-colourable and fails the universal
root-saturation condition forced by a genuine seven-chromatic critical
graph.  Any valid continuation may still exploit that universal condition,
relations among all common-host colourings, or a different global pair or
order-seven separation.
