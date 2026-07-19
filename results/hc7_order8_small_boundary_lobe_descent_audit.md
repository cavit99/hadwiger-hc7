# Audit of small-boundary lobe descent at an order-eight interface

**Verdict:** GREEN.

**Audited source:**
[`hc7_order8_small_boundary_lobe_descent.md`](hc7_order8_small_boundary_lobe_descent.md)

**Audited SHA-256:**
`79df6eb5a3942abe1baf19c440ccc1d1c7d9818181b13f3ddad5cb525101a0eb`

After this audit, the source was moved into `results/` and its status line
was changed only to record the GREEN verdict and link to this audit.  No
theorem statement, proof, scope, or trust boundary changed.  The resulting
source SHA-256 is
`de980671b3053459e4e11845e510e5d96bb0a4f18d1a8bd50fe4b9dfae996d52`.

**Audit type:** independent internal mathematical audit.  This is not
external peer review and does not prove `HC_7`.

## Theorem 1

Because `C` is a component of `G-S`, the open neighbourhood of `L` is
exactly the disjoint union of its neighbours in `G[C]` and its neighbours
in `S`.  The assumed inequality therefore bounds `T=N_G(L)` by eight.

The claimed separation has two nonempty shores: `L` is nonempty, and the
assumed second component of `G-S` is outside `L\cup T`.  Seven-connectivity
therefore forces `|T|` to be seven or eight.

At order eight, `L` is a component of `G-T`.  If another component `D`
misses a boundary vertex, then `|N_G(D)|<=7`; this is a genuine separator
because `L` is on the other side.  The exceptional possibility `D=L` is
excluded by `N_G(L)=T`.  Thus absence of an order-seven separation makes
every component of `G-T` full to `T`.  The promoted four-full-component
closure applies literally at this new boundary and leaves exactly two or
three components.

The proper-minor colouring response is also correct: deletion of any
actual `L`--`T` edge produces a six-colourable proper minor, and the two
ends must share a colour in every such colouring or the edge can be
restored.

## Corollary 2

For a genuine two-cut `X={x,y}` in the two-connected graph `G[C]`, every
component of `G[C]-X` has a neighbour of both `x` and `y`; otherwise one of
the two vertices alone is a cutvertex.  It has no other neighbour in `C`,
so its internal neighbourhood is exactly `X`.  Consequently a lobe with at
most six boundary neighbours satisfies Theorem 1.

If two such lobes were full to `S`, then they and the two original full
components would be four disjoint connected subgraphs full to `S`.  The
boundary triangle gives the explicit seven-branch-set construction.
Therefore at most one lobe is full; absent a descent, every other lobe has
exactly seven neighbours in `S`.

## Exact trust boundary

The theorem is a sufficient descent criterion.  It does not prove that a
suitable lobe always exists.  Corollary 2 leaves the nearly-full two-cut
residue in which every lobe sees seven or eight boundary vertices.  Neither
result preserves old colouring partitions, branch labels, demand pairs, or
interval data.  A two-component order-eight return and colour compatibility
at an order-seven separation remain open.

Within the stated scope, no mathematical gap was found.  Safe to promote
with the source hash above.
