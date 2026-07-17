# Independent audit: simultaneous singletonization at the exact order-eight boundary

**Theorem revision audited:** SHA-256
`ac7b9116d1e1a6fff1916b462d0b10d581cb0c6ab7808cf8bfcfeab48df7360e`.

**Dependency checked:**
[`../results/hc7_near_k7_singleton_one_hole_trichotomy.md`](../results/hc7_near_k7_singleton_one_hole_trichotomy.md),
SHA-256
`14248092b994e303d977eb6c2a9bc922c3538ea6a3de752277fe0dac30883b72`,
together with its adjacent GREEN audit.

## Verdict

**GREEN.** Under the stated exact order-eight hypotheses, Theorem 2.2 gives
a spanning `K_7`-minus-one-edge model in which the two nonadjacent
two-vertex branch sets are simultaneously reduced to selected singleton
endpoints.  Theorem 3.3 validly returns a `K_7` minor, an actual order-seven
separation, an actual separator of order at least eight whose near side is a
strict subset of `C` or `D`, or a labelled one-/two-spoke-deficient
near-`K_7` model centred in such a strict subset.  No mathematical
correction is required.

## Checks

1. For an edge `uv`, collective adjacency to every `r in R` gives
   `M(u) cap M(v)=emptyset`.  Hence `|M(u)|+|M(v)|<=3`, and at least one
   endpoint is `R`-admissible.  This applies independently to `e` and `f`.
2. In Theorem 2.2 each mate belongs to exactly one branch set: to `W_r`
   when its selected endpoint misses the unique `r`, and otherwise to
   `V^+`.  Therefore `U,V^+,{W_r:r in R},{a},{b}` are disjoint and
   partition `V(G)`.
3. Each `W_r` is connected because collective adjacency forces `rq'`
   whenever `M(q)={r}`.  The set `V^+` is connected because the component
   `V` has a neighbour at every added boundary vertex.
4. All adjacencies among the five nonsingleton branch sets are literal:
   `U-V^+` through an edge from `U` to `x`; `U-W_r` and `V^+-W_r` through
   component-to-`r` edges; and `W_r-W_s` through `rs in E(R)`.  Enlarging
   a branch set loses no adjacency.
5. Each selected singleton `q` meets `U` and `V^+` by boundary-fullness and
   meets every `W_r` either through `qr` or through the mate edge `qq'`.
   The two singletons are anticomplete because `e` and `f` are
   anticomplete.  For fixed `W_r`, anticompleteness between the defect
   edges leaves at most `r` or the selected mate as a neighbour of either
   singleton, including when both mates enter the same `W_r`.
6. In Lemma 3.2, `C,D,S` partition `V(G)`.  If `q` has only one neighbour
   in each component, all possible neighbours are its mate, `x`, the
   `3-|M(q)|` met vertices of `R`, and those two component neighbours.
   Thus `d(q)<=7-|M(q)|`.  Seven-connectivity forces equality,
   `M(q)=emptyset`, the edge `qx`, and precisely the neighbourhood in
   (3.1).
7. If an `R`-admissible endpoint `q` satisfies (3.1), then `|N(q)|=7`.
   Both endpoints of the opposite defect edge are nonneighbours of `q`, so
   they remain in `G-N(q)`, while `q` becomes an isolated vertex.  Hence
   `G-N(q)` has at least two components and `N(q)` is a literal vertex cut
   of order seven.  Equivalently it induces an actual order-seven
   separation.  No quotient adjacency or unstated connectivity is used.
8. If no `R`-admissible endpoint satisfies (3.1), Lemma 2.1 permits choices
   `a,b`, and the contrapositive of Lemma 3.2 puts two neighbours of `a` in
   one prescribed component `U`.  Theorem 2.2 leaves that component
   literally unmodified.  Its spanning model satisfies all hypotheses of
   the singleton one-hole theorem with centre `{a}`, missed branch set
   `{b}`, and `U` as the prescribed repeated-neighbour neutral branch set.
9. The prescribed-branch-set specialization is valid: in the dependency
   proof the degree count only locates a two-root branch set.  Once two
   roots in `U` are supplied, every connected-core, reverse-root,
   separator, transfer, and rotation construction stays inside `U`.  Thus
   its non-target set is a proper nonempty connected subset of the original
   component, not of the enlarged opposite component branch set.
10. The dependency's separator has integer order at least seven.  Exact
    order seven is outcome 2; every other possibility has order at least
    eight and is outcome 3.  This is only a partition of the audited
    conclusion--no separator order has been strengthened.  The
    dependency's rotation gives outcome 4, and its target gives outcome 1.
    The four cases are exhaustive.

## Scope

The theorem does not show that a separator of order greater than seven
preserves the exact-seven colouring data needed for recursive composition,
does not prove that a nominated pair meets every `K_5` minor, and does not
terminate labelled deficiency rotations.  Its progress is exact: the former
degree-seven endpoint residue is discharged as an actual order-seven
separation, while the larger-boundary strict-component separator remains.
