# Independent audit: common-label paired paths at an order-eight boundary

**Verdict:** GREEN for the exact source revision recorded below.

This audit checks the exact revision of
[`hc7_order8_common_label_paired_fan.md`](hc7_order8_common_label_paired_fan.md)
with SHA-256

```text
560dced4ba8ee95833e316978a7d8352f92670261194d68d3b203551cf1e09b3
```

The change from the initially checked source is limited to the opening
status line recording this GREEN audit; the mathematics is unchanged.

The source is a promoted theorem in `results/`.  This audit verifies its two-edge
matching theorem, its paired-source fan alternative, and its minimum-shore
corollary.  It does not establish the subsequent label-preserving branch-set
exchange or prove `HC_7`.

## 1. Hypotheses and invariant objects

The hypotheses used by the proof are explicit and sufficient:

1. `G` is seven-connected;
2. `S` has eight literal vertices and `G-S` has at least two components;
3. the selected component `C` is adjacent to every literal vertex of `S`;
4. the four vertices `s_D,s_{F_1},s_{F_2},s_{F_3}` have four distinct
   inherited common-model labels; and
5. for the colouring-response corollaries, `G` is seven-chromatic and every
   proper minor is six-colourable.

The branch-set adjacencies behind the phrase “common model labels” are not
used to prove the matching or fan alternatives.  They are used only to
interpret the five fan ends as five prescribed inherited labels.  No
palette colour is identified with a branch-set label.

Three invariants persist throughout the proof:

- the sets `C` and `S` are disjoint and `N_G(C)=S` because `C` is a
  boundary-full component of `G-S`;
- the selected edges have distinct ends in both bipartition classes;
- only the path `P` is contracted, so every separator vertex other than
  its image remains one literal host vertex.

## 2. Audit of the matching theorem

Consider the bipartite graph of the `C-R` edges, where

\[
                    R=\{s_D,s_{F_1},s_{F_2},s_{F_3}\}.
\]

Boundary fullness gives positive degree at every vertex of `R`.  If this
bipartite graph has matching number one, choose one incident edge at every
vertex of `R`.  If two chosen edges had distinct ends in `C`, their ends in
`R` would already be distinct, so they would form a matching of order two.
Hence all four chosen edges have one common end `a` in `C`.

Every other `C-R` edge also has its `C`-end at `a`: an edge `xr` with
`x\ne a` can be paired with `as'`, where `s'` is any of the other three
vertices of `R`.  This justifies the exact conclusion

\[
                         E_G(C-a,R)=\varnothing.
\]

If `C-a` is nonempty, a component `W` of `G[C-a]` can have neighbours only
at

\[
                    \{a,k_1,k_2,s_X,s_Y\}.
\]

Indeed, componenthood excludes other vertices of `C-a`, the preceding
matching argument excludes `R`, and distinct components of `G-S` are
anticomplete.  A second component of `G-S` lies outside
`W\cup N_G(W)`, so this is a genuine separation of order at most five.
Seven-connectivity excludes it.  Thus the claimed order-two matching
exists whenever `|C|>1`.

The singleton exception is genuine: all four common-label boundary edges
may have their `C`-end at the sole vertex.

## 3. Audit of the edge responses

For a selected edge `e=a_1s_i`, every proper six-colouring of `G-e` makes
its ends equal.  Otherwise restoring `e` would six-colour `G`.  The same
argument applies to `f`.

The edges are vertex-disjoint, so contracting both gives a proper minor
`G/e/f` with two distinct contraction vertices.  Expanding a proper
six-colouring of that minor gives a proper colouring of `G-\{e,f\}` in
which both endpoint pairs are monochromatic.  No stronger compatibility
between the separate one-edge colourings is asserted.

## 4. Audit of the five-fan outcome

The path `P` contains `a_1,a_2`, so its contraction image `r` has the two
designated direct edges to `s_i,s_j`.  A five-fan from `r` to the
five-element set

\[
                  T=\{k_1,s_D,s_{F_1},s_{F_2},s_{F_3}\}
\]

has all five elements of `T` as distinct ends.  Replacing the two relevant
fan limbs by the images of the original edges `e,f` preserves disjointness
away from `r`.

On lifting the contraction, each remaining limb starts at the literal
vertex of `P` incident with its first edge.  Consequently the lifted paths
may meet one another on `P`, but are pairwise vertex-disjoint outside `P`,
exactly as claimed.  The graph used for the fan contains no boundary
vertices outside `T`; truncation at the first boundary hit therefore gives
five paths whose only vertices of `S` are their distinct terminal
vertices.  In particular, the paths to `s_i,s_j` are the original literal
edges `e,f`, not unspecified parallel edges created by contraction.

## 5. Audit of the failed-fan separator

If no five-fan exists, fan Menger gives a set

\[
                    Z\subseteq V(H)-\{r\},\qquad |Z|\le4,
\]

separating `r` from `T-Z`.  The direct edges from `r` force
`s_i,s_j\in Z`.  Let `A` be the literal lift in `C` of the `r`-component.
Because `Z` excludes `r`, all of `P` lies in `A`.  Because only `P` was
contracted, every element of `Z` lifts to one literal vertex.

Every neighbour of `A` is either one of the three omitted boundary
vertices in `S-T` or a vertex of `Z`.  Hence

\[
                    N_G(A)\subseteq(S-T)\mathbin{\dot\cup}Z,
                    \qquad |N_G(A)|\le7.
\]

There is a vertex `t\in T-Z`.  Separation in `H` puts `t` outside both
`A` and `N_G(A)`, so the host separation is nontrivial.  Boundary fullness
gives a neighbour of `t` in `C`; that neighbour cannot lie in `A`, proving
`A\subsetneq C`.  Seven-connectivity now forces every inequality to be
equality:

\[
 |Z|=4,\qquad N_G(A)=(S-T)\mathbin{\dot\cup}Z,
 \qquad |N_G(A)|=7.
\]

Since `S-T=\{k_2,s_X,s_Y\}` and `s_i,s_j\in Z`, all five specified
boundary vertices occur literally in `N_G(A)`.  Since
`a_1,a_2\in P\subseteq A`, both selected edges cross the new boundary.
This validates the claimed strict full-neighbourhood separation.

## 6. Audit of trace preservation and minimum-shore strictness

For either crossing edge, a six-colouring of its edge-deleted graph is
proper on the operated closed `A`-shore and on the unchanged opposite
closed shore.  The two restrictions are restrictions of one global
colouring, so they induce the same literal equality partition on
`N_G(A)`.  The double-contraction response similarly expands to a colouring
of the graph with both crossing edges deleted.  The source correctly does
not claim that any such partition colours the intact closed `A`-shore.

In Corollary 3.3 the extra hypothesis `C\subsetneq C_0` is essential and is
stated.  The failed-fan set satisfies

\[
                         \varnothing\ne A\subsetneq C\subsetneq C_0.
\]

Choose either crossing edge and a proper six-colouring after deleting it.
The connected set `A`, its literal full neighbourhood of order seven, the
crossing edge, and the nonempty opposite side satisfy the definition of a
generic exact-seven response interface.  Therefore `|A|<|C_0|` contradicts
the global minimum choice of `C_0`.  The five-fan outcome follows.  This is
a host-level strict decrease; it does not rely on preserving the old
order-eight boundary or the old equality partition.

## 7. Trust boundary

The audited draft proves exactly the following unbounded local principle:
a non-singleton full component behind an eight-vertex boundary supplies two
differently labelled, vertex-disjoint common-model contact edges; these
edges either extend to a five-label paired fan or remain together on an
actual order-seven response boundary.  Inside a strictly larger
minimum-order generic response shore, the separation alternative is
excluded by shore order.

It does not prove that the five paths can be absorbed into the inherited
minor model, that they leave a connected reserved subgraph, or that they
produce a `K_7` minor.  It does not treat a singleton component.  It does
not prove that every order-eight configuration occurs strictly inside the
chosen minimum generic shore.  Finally, the paired trace on the returned
order-seven separation is not a colouring of its intact rejecting shore;
the common-partition or strict-response recursion remains necessary.
