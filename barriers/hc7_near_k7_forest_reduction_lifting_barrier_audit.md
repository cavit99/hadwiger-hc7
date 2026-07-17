# Independent audit of the forest-reduction lifting barrier

**Verdict:** GREEN for the exact revision audited.

## Audited revision

- statement: `hc7_near_k7_forest_reduction_lifting_barrier.md`
- SHA-256: `5a969d6338ad4419309b4fb4c81aa25772a45fee5727772e7e9e578d79b5c540`

This audit checks the attachment-tree reduction, the cited one-vertex
forest exchange, every path and order calculation in the infinite family,
its labelled near-`K_7` embedding, and the separate prescribed-pair/model-
alignment limitation.

## 1. Attachment-tree reduction

For each model edge, one original edge is retained and its endpoint in each
incident branch set is placed in `S_i`.  An inclusion-minimal subtree of the
connected branch set spanning `S_i` retains every selected model edge, and
every one of its leaves is a required attachment vertex.  The reduced trees
remain disjoint because each lies inside its original branch set.  Thus they
form the same labelled minor model.

For `K_7^vee`, the attachment counts are bounded by the corresponding label
degrees: at most six generally and at most four at the common endpoint of
the two omitted edges.  The atomic lemma is invoked only when
`|S_i|>=2`, so no empty-boundary convention is needed there.

## 2. One-vertex insertion

Theorem 4 of Kawarabayashi--Yu, *Connectivities for k-knitted graphs and for
minimal counterexamples to Hadwiger's Conjecture*, arXiv:2606.01586v2,
has threshold `d(u,F)>=|S'|+2` when the forest has one component.  Its
construction joins the active component through `u`; in the one-component
specialisation the returned forest is therefore a tree.  It contains `u`
and all of `S_i`, has every leaf in `S_i`, and has strictly fewer vertices
than the original tree.  This is exactly Lemma 2.1.

All labelled adjacencies survive because every selected edge incident with
label `i` ends in `S_i`.  Adding the single outside vertex `u` preserves
branch-set disjointness.  Avoidance of a prescribed set is also preserved
under the stated hypotheses.  The resulting local inequality for a
minimum-total-order attachment-tree model follows by contradiction.

The equality discussion is scoped correctly: the cited extremal theorem
classifies only the induced one-tree-plus-vertex instance and supplies no
ambient separator or attachment control.

## 3. Exact quotient path calculation

Before contraction, `T=s v_1 v_2 v_3 v_4 t` and `C_m` are disjoint paths,
and the four displayed edges are the only edges between them.  Contracting
`C_m` gives a vertex `u` adjacent exactly to `v_1,v_2,v_3,v_4` within this
construction.

A finite tree containing `s,t` and having every leaf in `{s,t}` is an
`s`--`t` path.  A simple such path through `u` enters from `v_i` and leaves
through `v_j` with `i<j`.  Its vertex count is

\[
 (i+1)+1+(6-j)=8+i-j.
\]

The maximum possible gap is `j-i=3`, attained only by `(i,j)=(1,4)`.
Consequently the unique path with fewer than the six vertices of `T` is
`s v_1 u v_4 t`, of order five.

The quotient edges `v_1u` and `uv_4` have unique attachment locations in
the uncontracted exterior path: `v_1` meets `C_m` only at `c_1`, while
`v_4` meets it only at `c_m`.  Any connected lift of the contracted vertex
must therefore contain both ends of `C_m`, and hence every one of its `m`
vertices.  The shortest lift is `s v_1 C_m v_4 t`, with exactly `m+4`
vertices.  This exceeds six for every `m>=3` and grows without bound.  The
claimed connector-cost obstruction is exact.

## 4. Labelled near-clique embedding

The six added singleton branch sets form a clique.  The tree branch set
meets `U_1,U_2` through `s` and `U_3,U_4` through `t`, while its missing
adjacencies may be the two singleton labels `B,C`.  Thus these seven branch
sets are a labelled `K_7^vee` model whose deficient-label branch set is
`T`, with selected attachment set exactly `{s,t}`.  The exterior path is
disjoint from the model.

Contracting that exterior path reproduces the strict quotient replacement.
Any label-preserving lift that uses the contracted component pays the
proved `m`-vertex connector cost, so it cannot lower total attachment-tree
order.  Extra singleton branch sets cannot be used to shorten the lift
without violating branch-set disjointness.  The family is explicitly not
claimed to be seven-connected or contraction-critical.

## 5. Prescribed-pair and designated-deletion limitations

The prescribed-pair discussion is a logically separate limitation, not a
second counterexample.  Lemma 2.1 preserves avoidance of `P` only from a
starting labelled model already contained in `G-P`, with the inserted
vertex also outside `P`.  Existence of a near-`K_7` model somewhere in `G`
and existence of only a `K_5` model in `G-P` do not provide such an aligned
starting model.  The note claims only that no repository theorem currently
performs this alignment; it does not claim that alignment is impossible.

After deleting a designated vertex `p` from a branch tree, preserving the
selected model endpoints alone need not let the returned forest reconnect
when `p` is restored.  Including the relevant neighbours of `p` in the
boundary is a valid sufficient requirement.  For a forest with at least two
components, the cited theorem's threshold is one more than the boundary
order and its conclusion can reduce, rather than eliminate, the component
count.  Hence it does not by itself return one connected branch set avoiding
`p`.  The final observations about seven-connectivity and dominating-model
contacts correctly distinguish total boundary neighbourhood from many
contacts at one literal outside vertex.

## Scope

The note proves a sound atomic exchange and an unbounded obstruction to
lifting its unweighted strict order through an arbitrarily contracted
connected exterior component.  It neither refutes a weighted connector
theorem nor rules out a new label-preserving model-alignment theorem, and it
does not present an `HC_7` counterexample.  These limitations are stated
accurately.
