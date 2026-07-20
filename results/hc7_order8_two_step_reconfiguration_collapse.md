# Opposite shore languages are at distance at most two

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_two_step_reconfiguration_collapse_audit.md`](hc7_order8_two_step_reconfiguration_collapse_audit.md).
This theorem concerns the four-or-five-colour boundary reconfiguration
graph.  It does not prove `HC_7`.

## 1. Setting

Let `H` be a graph and let `R_5^{>=4}(H)` be the graph of proper labelled
five-colourings of `H` which use at least four colours, with two colourings
adjacent when they differ at one literal vertex.  Let `E_A,E_D` be disjoint
nonempty subsets of this graph.  Assume:

1. each of `E_A,E_D` is invariant under every permutation of the five
   colour names; and
2. every proper colouring of `H` using all five colours belongs to exactly
   one of `E_A,E_D`.

Choose a shortest path

\[
                         c_0,c_1,\ldots,c_k                 \tag{1.1}
\]

with `c_0 in E_A` and `c_k in E_D`, minimizing over both endpoint sets.

In the two-shore application, `E_A,E_D` are the equality traces extending
through the two closed shores after one exact boundary colour class has
been fixed.  Their invariance follows by permuting the other five colour
names in a shore colouring.

## 2. Two-step collapse

### Theorem 2.1

Under the hypotheses above,

\[
                              1\le k\le2.              \tag{2.1}
\]

If `k=2`, the sole internal colouring `c_1` uses exactly four colours and
belongs to neither extension set.  No endpoint edge of (1.1) merely
renames the five colours globally.

#### Proof

Disjointness of the endpoint sets gives `k>=1`.  Minimality gives

\[
                  c_i\notin E_A\cup E_D
                  \qquad(1\le i\le k-1).              \tag{2.2}
\]

Suppose `k>=3`.  Apply the audited missing-colour transport theorem to the
internal edge `c_1c_2`.  There are distinct colours `a,b` and one operated
vertex `v` such that

* `a` is absent under `c_1` and occurs only at `v` under `c_2`;
* `b` occurs only at `v` under `c_1` and is absent under `c_2`; and
* all other vertex colours are unchanged.

Consequently, if `tau` is the global transposition of the colour names
`a,b`, then

\[
                              \tau(c_2)=c_1.           \tag{2.3}
\]

Apply `tau` to every colouring in the suffix

\[
                              c_2,c_3,\ldots,c_k.
\]

A global colour permutation preserves properness, the number of used
colours and one-vertex adjacency.  It also preserves `E_D` by hypothesis.
Equation (2.3) therefore turns

\[
                    c_0,c_1,\tau(c_3),\ldots,\tau(c_k) \tag{2.4}
\]

into a path from `E_A` to `E_D` of length `k-1`, contradicting the choice
of (1.1).  Hence `k<=2`.

If `k=2`, (2.2) says that `c_1` belongs to neither endpoint set.  A
surjective colouring belongs to exactly one endpoint set, so `c_1` is not
surjective; because it lies in `R_5^{>=4}(H)`, it uses exactly four
colours.

Finally, suppose the first edge merely applies a global colour permutation.
Since `c_0 in E_A` and `E_A` is invariant, this would put `c_1 in E_A`.
For `k=1` this contradicts `c_1 in E_D`; for `k=2` it contradicts
(2.2).  The last edge is symmetric.  \(\square\)

## 3. Host-level consequence

In the order-nine two-full-shore endpoint, assume each shore-extension
language contains a boundary trace whose eight-vertex restriction uses at
least four colours.  The audited four-or-five-colour reconfiguration
theorem supplies (1.1), and the maximum-palette alternative supplies the
surjective ownership hypothesis.  Theorem 2.1 leaves exactly two cases:

1. one oppositely owned one-vertex boundary move, with the audited pair of
   shore-internal bichromatic obstruction paths; or
2. one four-colour boundary trace rejected by both shores, giving a
   selected connected vertex-minimal list-colouring obstruction in each
   open shore.

Thus there is no transition chain on which a missing colour can cycle.  In
particular, when the residual boundary graph is four-chromatic, the
endpoint hypothesis is automatic and the entire reconfiguration branch has
this two-step form.

The theorem does not close either remaining host case.  The one-step paths
may hit different boundary colour components, and the two list-critical
subgraphs need not align with the five named branch sets.  The next theorem
must still use seven-connectivity, global `K_7`-minor exclusion or a
proper-minor response to obtain an explicit `K_7`-minor model, a common
order-seven boundary colouring or a strict host-level descent.

## 4. Dependency

- [missing-colour transport along a shortest shore transition](../results/hc7_order8_shortest_path_hole_transport.md).
