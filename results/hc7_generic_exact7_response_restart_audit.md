# Internal audit: generic exact-seven response restart

**Verdict:** GREEN for the exact source revision

```text
e689c96686a936c27e58c2cba22d699c62ad649092eebfcdfc9c5db95a8e7b5a
```

of
[`hc7_generic_exact7_response_restart.md`](hc7_generic_exact7_response_restart.md).
This is a separate internal audit, not external peer review.  The revision
checked line by line had source hash
`c0bec96df24799f6cf6667763fdfc125dcf78a3c355977ebabbcbe6607937614`;
the pinned revision changes only the opening status line to link this audit.
Its mathematical content is identical.

## 1. Scope checked

The audit checked:

1. the automatic legal/rejected orientation of the selected edge-deletion
   response;
2. the use of seven-connectivity, exact-seven full-subgraph packing,
   adaptive reflection and boundary classification;
3. the retention of the selected entrance edge while finding a second
   vertex-disjoint entrance edge;
4. every hypothesis of the parameter-uniform two-edge list-critical
   descent;
5. the construction of a fresh generic exact-seven response interface from
   a proper core whose full neighbourhood has order seven; and
6. the strict decrease in the order of the connected shore.

## 2. Findings

### The generic response properties require no inherited labels

The partition in (1.2) is an actual separation with both open sides
nonempty.  Seven-connectivity therefore makes every component behind the
seven-vertex boundary adjacent to every boundary vertex.  The exact-seven
packing and adaptive-reflection theorems leave only packing vectors `(1,1)`
and `(1,2)`, up to orientation.

The no-rigid-trace theorem identifies the sole five-chromatic boundary as
`K_2` joined to `C_5`; its two shores are connected and full, and deleting
the two universal boundary vertices leaves the required `K_5` minor.  The
cycle-boundary completion theorem therefore excludes that case.  The
selected partition is legal on the unchanged shore and rejected on the
operated shore.  Exact full-subgraph reflection is oriented correctly from
the legal shore, so its demand exceeds the legal shore's packing number.

None of these deductions uses the special five-plus-two provenance.

### The retained-edge entrance argument is exact

If `A-{a}` is nonempty, a component `C` of that graph has no neighbours in
another such component or in the opposite open shore.  If every boundary
vertex other than `z` missed `C`, then

\[
                              N_G(C)\subseteq\{a,z\},
\]

contradicting seven-connectivity.  The resulting edge `z'a'` is
vertex-disjoint from the originally selected edge `za`.

### The two-edge core produces a valid strict restart

With the shore names `(L,S,R)=(B,S,A)`, every hypothesis of the
parameter-uniform two-edge list-critical theorem is present.  Its core
meets at least one marked operated-shore endpoint.  If the core is proper
and its full neighbourhood has order seven, the corresponding marked edge
crosses from the core to that literal boundary.  A six-colouring after
deleting the edge is proper on the opposite closed shore and its complete
boundary partition is rejected by the intact core side.

The old opposite shore is anticomplete to the whole old operated shore, so
it is disjoint from the core and its full neighbourhood and remains a
nonempty opposite side.  The new interface is therefore genuine, and the
proper inclusion of the core gives the declared strict decrease.

## 3. Trust boundary

The theorem proves a well-founded generic selected-response restart at an
exact order-seven proper-core boundary.  It does not preserve the old
complete partition, special five-plus-two vertices, full connected
subgraphs, or near-clique branch-set labels.

It does not tighten a boundary of order at least eight, eliminate the
singleton or shore-filling outcomes, synchronize two shore colourings, or
prove `HC_7`.  The final contextual dependency on the special pullback is
used only for Corollary 3.2, not for the generic proof.

No unresolved assumption remains in the stated theorem.
