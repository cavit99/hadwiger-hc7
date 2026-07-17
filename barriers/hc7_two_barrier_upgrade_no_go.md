# Why the two sharp barrier families cannot be upgraded directly

**Status:** written barrier synthesis; separate internal audit GREEN in the
adjacent audit note.  This note proves limitations of two construction
methods.  It is not a counterexample to `HC_7`.

The capped-antiprism complete-join family and the amplified boundary-state
family satisfy complementary large subsets of the active hypotheses.  The
lemmas below identify the first condition which each family cannot acquire
without abandoning its defining architecture.

## 1. A two-vertex `K_5`-minor transversal forbids seven colours

### Proposition 1.1

Let `G` be a graph and let `P` be a set of at most two vertices.  If `G-P`
has no `K_5` minor, then `chi(G)<=6`.

### Proof

This is Theorem 1.1 of the adjacent note
[`hc7_two_vertex_k5_transversal_chromatic_obstruction.md`](../results/hc7_two_vertex_k5_transversal_chromatic_obstruction.md).
The `t=5` case of Hadwiger gives a four-colouring of `G-P`, and the two
vertices of `P` use two fresh colours.  \(\square\)

### Application to the capped-antiprism family

For the capped-antiprism graph `G_n=K_2 vee H_n`, deleting the two vertices
of the complete factor leaves the planar graph `H_n`.  Thus the complete
factor is a two-vertex transversal of all `K_5`-minor models, and
Proposition 1.1 forces `chi(G_n)<=6`.

More generally, the audited identity

\[
                       eta(K_2\vee H)=2+eta(H)
\]

and the `t=5` case show that no `K_7`-minor-free complete join `K_2 vee H`
can be seven-chromatic.  Hence **seven-chromaticity is the first impossible
counterexample hypothesis for this architecture**.  Any attempted upgrade
which retains the two-vertex transversal is impossible even before
all-operation contraction-criticality is considered.

The explicit capped-antiprism graph is therefore a sharp test of
geometry-only separator bounds, but not a candidate obstruction to a
theorem which is allowed to use seven-chromaticity.

## 2. False-twin amplification forces a large clique minor

### Lemma 2.1

For every integer `m>=1`, the complete bipartite graph `K_{m,m}` contains a
`K_{m+1}` minor.

### Proof

Write its bipartition as

\[
              \{a_1,\ldots,a_m\}\mathbin{\dot\cup}
              \{b_1,\ldots,b_m\}.
\]

For `1<=i<m`, use the connected branch set `\{a_i,b_i\}`.  Use also the
two singleton branch sets `\{a_m\}` and `\{b_m\}`.  The paired branch sets
are mutually adjacent by cross-edges; `a_m` is adjacent to every `b_i`,
`b_m` is adjacent to every `a_i`, and `a_mb_m` is an edge.  These `m+1`
sets form a `K_{m+1}`-minor model.  \(\square\)

### Lemma 2.2

A vertex-critical graph has no two distinct nonadjacent vertices with the
same open neighbourhood.

### Proof

Suppose `u,v` are nonadjacent and `N(u)=N(v)`.  If `G` is `k`-vertex-
critical, then `G-u` has a proper `(k-1)`-colouring.  Give `u` the colour
of `v`.  Every neighbour of `u` is a neighbour of `v`, and `uv` is not an
edge, so this extends to a `(k-1)`-colouring of `G`, a contradiction.
\(\square\)

### Application to the boundary-state amplification

The connected-full boundary-state realizer contains an open-side edge.
The order-seven connectivity amplification replaces each endpoint of that
edge by an independent false-twin class of order seven and replaces the
edge by all edges between the two classes.  Consequently the amplified
host contains `K_{7,7}`.  Lemma 2.1 gives an explicit `K_8` minor, and in
particular a `K_7` minor.

The same amplification contains nonadjacent false twins.  If its chromatic
number is seven, deleting one member of a twin class leaves a graph which
is still seven-chromatic: otherwise the deleted vertex could be restored
with its surviving twin's colour.  Thus a named vertex deletion already
violates seven-contraction-criticality.

Therefore the parity-language barrier's particular high-connectivity
amplification cannot be made `K_7`-minor-free or all-operation
seven-contraction-critical while its false-twin construction is retained.
This is a limitation of the construction, not of arbitrary boundary-state
realizers.

## 3. In the actual critical host the two missing properties coincide

### Lemma 3.1

Let `G` be a seven-connected graph with `chi(G)=7` such that every proper
minor of `G` is six-colourable.  Then `G` has no `K_7` minor.

### Proof

Seven-connectivity implies that `G` has at least eight vertices, so it is
not isomorphic to `K_7`.  If `G` had a `K_7` minor, that minor would be a
proper minor of `G` with chromatic number seven, contrary to the
hypothesis.  \(\square\)

Thus, for a seven-connected host, upgrading the parity-language barrier to
full contraction-criticality would automatically supply global `K_7`-minor
exclusion.  The two omissions are not independent technical checkboxes.
The false-twin amplification blocks the criticality upgrade at a single
vertex deletion and blocks minor exclusion at a single amplified edge.

## 4. Exact strategic conclusion

The two families lie on opposite sides of the missing theorem.

* The capped-antiprism family has seven-connectivity, global `K_7`-minor
  exclusion, and the labelled near-complete model, but its two-vertex
  transversal forces six-colourability.
* The amplified parity-language family has seven-connectivity,
  seven-chromaticity, rich proper-minor trace data, and no two-vertex
  transversal, but one amplified edge already supplies a `K_7` minor and
  one false-twin deletion already refutes full contraction-criticality.

Accordingly neither architecture falsifies the active conditional
exchange-or-gluing theorem.  A stronger counterarchitecture would have to
combine seven-chromaticity with the literal labelled model geometry while
avoiding both a global two-vertex `K_5`-minor transversal and all false-twin
amplification.  Constructing such a `K_7`-minor-free host would already
cross the central `HC_7` frontier; it is not a routine strengthening of
either barrier.

## Dependencies

- [two-vertex chromatic obstruction](../results/hc7_two_vertex_k5_transversal_chromatic_obstruction.md)
- [complete-factor join dichotomy](../results/hc7_join_near_clique_dichotomy.md)
- [capped-antiprism separator-excess barrier](hc7_five_bag_separator_excess_barrier.md)
- [`K_{3,5}` state barrier with no two-vertex transversal](hc7_k35_no_common_state_or_two_vertex_transversal.md)
