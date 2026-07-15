# Independent audit: reduced rotation triangle and quotient scaffold

**Verdict:** GREEN after the heading clarification and the two explicit
gate-containment assertions added to the verifier.

**Audited files:**

* `barriers/hc7_global_invariant_rotation_triangle.md`;
* `barriers/hc7_global_invariant_rotation_triangle_verify.py`.

This audit checks the graph construction, the `K_7`-minor-free claim, all
three literal rotations, the length-eight exact-seven packet capacities,
and Lemma 6.1.  It does not promote the closed-component coherence target;
that target remains open.

## 1. Tube, connectivity and the fixed pair

For `m=1` the displayed graph has the two pole vertices, two pentagonal
rings and the usual triangulated belt, so it is the icosahedral graph.
For `m=8` the same construction is a pentagonal triangulated tube.  The
checker independently returns a plane embedding and vertex connectivity
five for each of the two cores.  Joining the adjacent universal vertices
`p,q` raises the certified host connectivity to seven.  There is also a
direct lower-bound proof: after deleting at most six vertices, either an
apex survives and connects the remainder, or both apices were deleted and
at most four vertices were removed from the five-connected core.

The `K_7`-minor-free proof is correct.  At most two branch sets of a
putative seven-bag clique model contain `p` or `q`.  Removing those branch
sets leaves at least five pairwise adjacent connected branch sets wholly
inside the planar core, hence a `K_5` minor there, impossible.  Deleting
the same literal pair `{p,q}` leaves exactly the planar core.  Thus the
barrier has the claimed coherent fixed-pair terminal and is not being
presented as an `HC_7` counterexample.

## 2. Five-row frame and the three near states

The five frame bags are pairwise disjoint and connected.  The nonuniversal
checks can be witnessed as follows:

* `F_1F_2` by `u_1u_2`;
* `F_1F_3` by `w_1w_2` (also `u_1w_0`);
* `F_2F_3` by `u_2w_2`.

The deeper rings in `F_3` form a connected continuation to `B`; adding
them does not alter any state contact at the top of the tube.  The two
singleton apex rows meet every other row.

For `M_T`, the centre `{T}` misses exactly `F_3`.  For `M_C`, the four-
vertex centre `C` misses exactly `F_1`.  For `M_0`, the centre `{u_0}`
misses exactly `F_2`.  In all three cases the active row together with the
five fixed rows is a literal `K_6` model.  The checker verifies connectivity,
global disjointness, all fifteen row adjacencies and the exact missing-row
tuple for each state.

## 3. The reduced rotation word

Each arrow satisfies the exact single-gate datum.

1. `M_T -> M_C`: split `{u_0} union C` with gate `{u_0}`.  It meets the
   old centre through `Tu_0`, the residual through `u_0u_4`, and repairs
   `F_3` through `u_0w_0`.
2. `M_C -> M_0`: split `{T,u_0}` with gate `{T}`.  It meets `C`, meets the
   residual `u_0`, and repairs `F_1` through `Tu_1`.
3. `M_0 -> M_T`: split `{T} union C` with gate `C`.  The connected gate
   meets `u_0`, meets residual `{T}`, and repairs `F_2` through `u_3u_2`.

The inverse of an exact rotation uses the same gate.  The next gates in
the displayed word are respectively `{T}`, `C`, and `{u_0}`, so no two
consecutive arrows cancel.  The five literal rows and the union

\[
                         C\cup\{T,u_0\}
\]

are constant, while the centre orders are `1,4,1`.  The claimed reduced
cycle and all stated failures of representative-local monotonicity follow.

The revised Section 4.3 heading is important: the coarse carrier union is
a genuine invariant of the neutral class.  What the example refutes is
its use as an internal progress measure or as a complete description of
the missing duty.

## 4. Exact-seven tube frontiers

For `1<=r<=7`, deleting

\[
                         S_r=\{p,q\}\cup R_r
\]

leaves the two nonempty anticomplete connected shores stated in the
source.  Each boundary vertex has a neighbour in either shore, so both
shores are `S_r`-full.

Any full packet on the left must collectively meet all five vertices of
`R_r`.  The only possible left endpoints of those five contacts lie in
`R_{r-1}`, and every such endpoint sees exactly two boundary-ring
vertices.  It therefore uses at least three vertices of the five-element
ring `R_{r-1}`.  Two disjoint full packets would require at least six
vertices there.  The right-hand argument using `R_{r+1}` is symmetric.
The whole connected shore itself is one full packet, so both maxima are
exactly one.  Hence the seven displayed frontiers are genuine `(1,1)`,
not `(1,2)`, adhesions.  This supports precisely the orientation-reset
warning and does not challenge the separately proved global `(1,2)`
minimum principle.

## 5. Neutral-reset certificate and Lemma 6.1

The four-state abstract certificate is valid: both arrows decrease the
orders of their selected representatives, but neutral movement within the
target class resets `3` to `5` and closes the directed cycle.  Therefore
local numerical decrease is insufficient unless the number is constant on
neutral classes.

Lemma 6.1 repairs this exactly.  The map `C([M])` is defined on whole
neutral classes, and every strict quotient edge gives proper set inclusion.
Thus `|C([M])|` decreases at least once per strict edge, so a strict walk
has at most `|V(G)|` edges.  Applying Newman's lemma to the terminating
quotient is legitimate under the separately stated local-confluence-modulo-
neutral-equivalence hypothesis.  The source correctly leaves sink
classification as an additional obligation.

## 6. Reproduction

The two supplied checks were rerun after strengthening the pivot guard:

```text
GREEN length=1: core connectivity 5, host connectivity 7; literal reduced rotation triangle verified
GREEN length=8: core connectivity 5, host connectivity 7; literal reduced rotation triangle verified
fixed frame and active carrier union are constant around the cycle
common fixed pair: {p,q}; deleting it leaves the planar tube
```

No inference in the note depends on an unverified `K_7`-minor search or on
palette colours being treated as row labels.
