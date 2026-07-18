# Audit: exact-seven paired-block trace parity barrier

## Verdict

**GREEN** at the exact revisions

```text
aaef229a36ab6eae0fb15a55a0f9faf7de1862a0ac376327460921bb8963a89b  barriers/hc7_exact7_paired_block_trace_parity_barrier.md
c3f144632ff9ced17c51e4a842b6dd232f0ca1d993098f53d8225b70ae94d6ba  barriers/hc7_exact7_paired_block_trace_parity_barrier_verify.py
```

The verifier passes under both ordinary Python and `python3 -O`; its
always-active `require` checks are not removed by optimization.

The boundary graph is exactly two disjoint triangles and an isolated
vertex.  The returned partition

```text
{j_0,j_1,q} | {b,z_1} | {r} | {z_2}
```

is proper and has four blocks.  For one or two disjoint prescribed
independent blocks, deleting their union leaves at least one vertex in each
triangle.  The residual graph is therefore noncomplete and at most
three-colourable.  Splitting a nonsingleton class of an optimal colouring
gives two extensions of opposite block-count parity, and both have at most
six blocks.  This proves the one- and two-block trace assertions.

Independent enumeration confirms 174 proper states, split into 93 even and
81 odd states; 31 nonempty independent sets; and 222 unordered pairs of
disjoint nonempty independent sets.  Every corresponding cylinder meets
both parity families, while the displayed target belongs to the even one.

The two-packet quotient has nine vertices and clique number four.  In any
putative seven-branch-set minor model, at most two branch sets could be
nonsingletons, leaving at least five singleton branch sets.  Those five
vertices would form a `K_5` subgraph, a contradiction.  Hence the quotient
has no `K_7` minor.

The source states the trust boundary exactly.  It refutes only an inference
from these abstract static language and quotient summaries; it does not
claim realization by two shores of one seven-connected, seven-chromatic,
`K_7`-minor-free graph whose every proper minor is six-colourable.  The
positive split-boundary residual follows from the separately audited
split-boundary synchronization theorem.  No unresolved mathematical or
computational issue remains within this stated scope.
