# Internal audit of the singleton-web-cell barrier

**Verdict:** **GREEN**.  The graph is a full-hypothesis counterexample to the
formally stated four-outcome bridge exhaustion, and its surviving
three-column chained absorption is valid.  The exhaustive root-placement
sweep proves that this fixed graph is paired-rooted-positive for every
admissible pair of root sets.  It is not a counterexample to Conjectural
Theorem 3.1.

**Audited barrier:**
[`hc7_pentagonal_bipyramid_singleton_web_cell_barrier.md`](hc7_pentagonal_bipyramid_singleton_web_cell_barrier.md),
SHA-256
`5ab012b23aa1706af86c8a7e04cf3d226b1ec30c0cd570b1c31ee99a4b46ac61`.

**Audited verifier:**
[`hc7_pentagonal_bipyramid_singleton_web_cell_barrier_verify.py`](hc7_pentagonal_bipyramid_singleton_web_cell_barrier_verify.py),
SHA-256
`333561d9b942ab8ac63b8ba0e1f45dbc3874ba369a3f73c27d478f178a0d43f7`.

**Audited root-placement sweep:**
[`hc7_pentagonal_bipyramid_singleton_root_sweep_verify.py`](hc7_pentagonal_bipyramid_singleton_root_sweep_verify.py),
SHA-256
`76d06ad6c3dceaa123e08c51acf95d86f301b63e402a988602e875120a13ef1f`.

**Imported chained theorem:**
[`hc7_pentagonal_bipyramid_three_column_chained_absorption.md`](../results/hc7_pentagonal_bipyramid_three_column_chained_absorption.md),
SHA-256
`8626c51e077675b90bdbb24330b58a28fd89f43d1d3f1dc7d0affeb1abb4ee31`.

**Audit type:** separate internal mathematical cold audit, adversarial logical
scope audit, and independent graph reconstruction.  This is not external peer
review.

## Logical scope

The four-outcome statement is genuinely sufficient for Conjectural Theorem
3.1.  If its universal residual fails, one shortest path in `F[C_i]` has a
two-sided off-path component, so the audited any-path transfer applies.  Each
of outcomes 1--3 is stated as the exact internal condition of its cited
construction and gives five bags containing five distinct whole columns;
because every column meets `A,B`, the model is paired-rooted.  Outcome 4 is
the other conclusion of Conjectural Theorem 3.1.

The counterexample negates this exact statement only.  It does not refute a
broader theorem allowing an arbitrary paired-rooted model, the chained
absorption proved here, or a strict same-form reduction.

## Host hypotheses and negative outcomes

Independent reconstruction from the prose, without importing the verifier,
confirmed the following.

- The graph has 16 vertices, 47 edges, the exact 15-edge
  pentagonal-bipyramid quotient, and seven connected columns.
- Every deletion of at most four vertices leaves it connected.  The five
  neighbours of vertex `15` separate that vertex, so its connectivity is
  exactly five.
- The two displayed root sets are disjoint and contain one vertex in every
  column.  The literal column paths are `0-1`, `3-2`, `4-5`, `7-6-15`,
  `8-9`, `10-11`, and `12-13`.
- The vertices `{2,3,6,14,15}` induce `K_5`, so the graph is not
  four-colourable.
- There are exactly six shortest internal pole-portal paths.  Every component
  off each path is empty or contacts at most one adjacent rim column.
- Exhaustion of all connected column bipartitions, all five adjacent-rim
  carriers, and all 20 elements of \(D_5\mathbin{\times}C_2\) finds no alternating split,
  adjacent-rim linkage, or two-column absorption.

The separate five-owner search checked all 137,376 allocations and found no
`K_5` model whose bags have five distinct whole-column owners.  This is an
independent cross-check on the three older mechanisms, each of which would
produce such a model.  The displayed model with four distinct owners is
valid, so the asserted maximum is exact.

## Exhaustive root-placement sweep

The seven column sizes are `2,3,2,3,2,2,2`, so there are exactly `288`
minimal root transversals and `288^2=82,944` ordered pairs, with overlap
allowed.  Independent reconstruction reproduced the overlap counts

```text
0:1152, 1:6912, 2:17568, 3:24480, 4:20160, 5:9792, 6:2592, 7:288.
```

The retained sweep enumerates all twenty oriented pentagonal-bipyramid
frames and all six theorem pieces.  It audits their locations and
disjointness, the connectedness of `D_1,D_2,D_3`, all seven literal contacts,
the five resulting branch sets, and their incidence with both root
transversals.  Exactly `98` distinct chained-absorption models survive.  Every
one of the `82,944` placements is covered by between four and ninety-eight
of them, including all `1,152` columnwise-disjoint placements.

An independent NetworkX implementation reconstructed the graph and the
theorem search without importing the retained code.  It reproduced the 98
models, every placement count, the certificate-catalogue digest
`2690d4c1f8b8f2add17849c5b76ce432694a3d57e7b64497ec77c51fc8ca6642`,
and the canonical-witness digest
`cb92d3289e6fe067ed56b911af5f4c17752ff3436fed6717c0714f0972cf890e`.
It also checked the three fixed models used as a compact cover.  Every
one-root transversal is covered by at least two of those models, so every
ordered pair shares one.

The extension from minimal transversals to arbitrary admissible root sets is
valid: choose one root in every column from each set, use the certified model
for those choices, and apply root-set inclusion.  This is a finite theorem
about the one retained graph, not an unbounded conclusion.

## Web and surviving mechanism

The pre-insertion rib has 8 vertices, 17 edges, and the 11 displayed faces.
Its directed face boundaries cover every edge twice, and its ten triangles
are exactly the ten inner faces.  Inserting vertex `15` subdivides the face
`5,6,t_1`.  The edges `15 5` and `15 6` are literal carrier edges, and the
terminal incidence at `t_1` records the three literal owner contacts
`15 2,15 3,15 14`.  Only the four outer-frame edges are completion-only.

The five chained bags are disjoint, connected, pairwise adjacent, and each
meets both displayed root sets.  All ten written edge witnesses and the seven
hypotheses of the chained theorem were checked directly.  Unused vertices
`6,14` cause no issue for a minor model.

## Reproduction

The retained checks were rerun with the repository environment:

```text
.venv/bin/python barriers/hc7_pentagonal_bipyramid_singleton_web_cell_barrier_verify.py
env PYTHONHASHSEED=1 .venv/bin/python barriers/hc7_pentagonal_bipyramid_singleton_web_cell_barrier_verify.py
.venv/bin/python -m py_compile barriers/hc7_pentagonal_bipyramid_singleton_web_cell_barrier_verify.py
.venv/bin/python barriers/hc7_pentagonal_bipyramid_singleton_root_sweep_verify.py
env PYTHONHASHSEED=987654 .venv/bin/python barriers/hc7_pentagonal_bipyramid_singleton_root_sweep_verify.py
.venv/bin/python -m py_compile barriers/hc7_pentagonal_bipyramid_singleton_root_sweep_verify.py
.venv/bin/python barriers/hc7_pentagonal_bipyramid_four_colour_combined_negative_verify.py
python3 tools/research_index.py check
```

Both new-verifier runs reported:

```text
singleton web-cell PB barrier: PASS order=16 size=47 connectivity=5 five_owner_models=0 maximum_distinct_owner_bags=4 shortest_residual_paths=6
```

Both root-sweep runs reported `placements=82944`, `chained=82944`,
`negative=0`, `disjoint=1152`, `certificates=98`, and
`compact_covered=82944`; their complete output was byte-identical under the
two hash seeds.

The imported base verifier and repository integrity check also passed.

## Unresolved boundary

No assumption remains unresolved in the stated finite counterexample or the
chained theorem.  The unbounded target remains open: a complete theorem must
also allow this root-sensitive multi-column allocation, or derive a compatible
whole-graph four-colouring, or return a proved strict same-form reduction.
