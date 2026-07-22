# Audit: a rejection-cut edge forces an alternating full-component cycle

**Audit type:** separate internal cold audit

**Verdict:** GREEN

**Audited theorem SHA-256:**
`ca18ef33d9bf3d0b98220df8bfbc965a29373300c0b93f56c35c660a8ac2ef3c`

The audited theorem is
`results/hc7_common_root_alternating_trace_cycle.md`.  I checked every statement and
proof from the hypotheses in Section 1, including affine palette alignment,
the multigraph argument with parallel edges, and every literal assertion in
Corollary 3.2.  No unresolved assumption or proof gap was found.

Promotion changed only the status sentence.  The promoted source hash is

```text
79d4b4ab1ea7c1b696f2978bb8616988667ceb0454dfc4af1297e53112c7d7ee  results/hc7_common_root_alternating_trace_cycle.md
```

The result is nonterminal.  It proves an alternating full-component
intersection cycle, not clean internal paths, disjoint branch sets, or an
`HC_7` conclusion.  Its exact trust-boundary section records this correctly.

## 1. Full-component switch spaces

Each `W_k` is connected in the boundary two-colour graph.  Consequently,
in either fixed shore extension, it lies wholly in one full
`alpha`--`beta` component.  Conversely, the intersection of a full
component with `X` is exactly the union of all `W_k` that it contains.
This makes `mathcal P_D` and `mathcal P_C` genuine partitions of `I`.

Swapping `alpha,beta` on a full two-colour component preserves
properness.  Different full components are disjoint, so arbitrary
collections can be swapped simultaneously.  On the `D` side this changes
the boundary by exactly a vector of `L(mathcal P_D)`.  On the `C` side it
changes the boundary relative to `theta^{\{i\}}` by exactly a vector of
`L(mathcal P_C)`, producing `theta^{e_i+q}`.  Lemma 2.1 is therefore
correct; it makes no unsupported assumption that a clean path exists
inside a full component.

The sets `W_k` remain the same in both extensions.  Swapping an entire
boundary component changes only the two colour names on its vertices and
does not change the vertex set or edge set of `H[alpha,beta]`.

## 2. Affine intersection and labelled gluing

The affine equivalence is exact:

\[
L(mathcal P_D)\cap(e_i+L(mathcal P_C))\ne\varnothing
\quad\Longleftrightarrow\quad
e_i\in L(mathcal P_D)+L(mathcal P_C).
\]

Indeed, in characteristic two, `p=e_i+q` is equivalent to `e_i=p+q`.
If the intersection contained `v`, Lemma 2.1 would supply extensions of
the same labelled boundary colouring `theta^v` through both shores.  The
labels, not merely the unlabelled colour classes, agree on `X`.  The two
exterior components are anticomplete and exhaust `G-N[u]`; their extensions
therefore glue.  Both use the common six-colour palette whose five boundary
names are fixed, and the remaining colour can be assigned to `u`.  This
contradicts hypothesis 3 and proves Lemma 2.2 without a hidden palette
permutation.

## 3. Incidence row space, bridges, and parallel two-cycles

In the bipartite multigraph `Gamma`, the row for a partition block is
precisely that block's incidence vector in `mathbf F_2^I`.  Hence the row
space of the unoriented incidence matrix is exactly
`L(mathcal P_D)+L(mathcal P_C)`.

For a finite loopless multigraph over `mathbf F_2`, this row space is its
cut space.  The singleton vector `e_i` belongs to the cut space exactly
when edge `i` is a bridge:

- if `i` is a bridge, one component of `Gamma-i` has cut `{i}`;
- if some vertex set has cut `{i}`, deleting `i` separates its ends.

This remains correct with parallel edges.  Every cut separating the common
ends of a parallel pair contains both parallel edges, so neither singleton
edge is a bridge.  Lemma 2.2 excludes `e_i` from the row space, hence `i`
is a nonbridge.  Every nonbridge edge lies on a cycle; two parallel edges
give the allowed cycle of length two.  Theorem 3.1 is valid.

The converse wording is also justified.  Were `i` a bridge, a row-space
representation `e_i=p+q` would give `p=e_i+q`, an actual common labelled
boundary colouring supplied by Lemma 2.1, and hence the displayed
six-colouring of `G`.

## 4. Literal realization of a shortest alternating cycle

Let a shortest cycle containing `i` have alternating block vertices
`B_1,Q_1,...,B_m,Q_m`.  Every selected block has two distinct incident
cycle-edge labels.  This remains true when `m=1`: the two edges are
parallel but have distinct coordinate labels.  Thus each selected full
component contains at least two distinct boundary components `W_k`.
Those cannot be connected inside `H[alpha,beta]`, so the full component
must contain at least one vertex in its literal shore.  This proves the
nonempty-outside-`X` assertion without assuming any specially chosen path.

Distinct selected full components from one fixed shore colouring are
disjoint.  They are anticomplete because an edge between two
`alpha`--`beta` vertices either violates properness (equal colours) or
joins the two induced two-colour components (different colours).

For opposite shores, the intersection formula is exact:

\[
K_B^D\cap K_Q^C
=\bigcup\{W_k:k\in B\cap Q\}.
\]

The interiors lie in the disjoint sets `D` and `C`; on `X`, each full
component contains exactly the union of the boundary components in its
block.  A cycle edge labelled `k` therefore gives the asserted literal
overlap on the whole connected subgraph `W_k`.

## 5. Chords and opposite-shore anticompleteness

The shortest-cycle chord claim is sound, including in a multigraph.  An
edge between nonconsecutive cycle vertices, together with the cycle arc
containing `i`, forms a strictly shorter cycle containing `i`; both arcs
between nonconsecutive vertices contain at least two cycle edges.  A
parallel edge between consecutive vertices is not a chord and causes no
problem.  For a two-edge parallel cycle there are no nonconsecutive
vertices.

Hence nonconsecutive opposite-shore block vertices have `B cap Q` empty,
so their full components are disjoint by the exact intersection formula.
They are also anticomplete, with every possible edge location accounted
for:

1. an edge from `D` to `C` is impossible because the exterior components
   are anticomplete;
2. an edge with both ends in `X` is an edge of `H[alpha,beta]`, so both
   ends lie in one `W_k`, forcing `k in B cap Q`;
3. if the `D`-side end is in `D` and the `C`-component end is a boundary
   vertex in `W_k`, then both ends have colours `alpha,beta` in `c_D`.
   The edge puts that boundary vertex in the full component `K_B^D`, so
   `k in B cap Q`;
4. the symmetric `C`-interior to `D`-boundary case is identical in `c_C`.

Each of cases 2--4 would supply an edge of `Gamma` between the selected
blocks, contradicting their nonconsecutiveness on the chordless shortest
cycle.  Combined with same-shore anticompleteness, this proves item 5 of
Corollary 3.2 literally.

## 6. Parallel-edge and application checks

When `m=1`, the two distinct coordinate edges have the same pair of block
ends.  One fixed full component in each shore consequently contains both
corresponding boundary components.  This is exactly the claimed bilateral
two-shore outcome; no assertion of two disjoint paths is made.

The synchronized-fork application uses one fixed accepted `F`-extension
and, separately for each chosen coordinate, one extension through `E` of
the switched boundary colouring.  Theorem 3.1 applies after interchanging
the shore names if necessary.  The text correctly refuses to combine the
two cycles because their `E`-extensions may differ.

## Promotion note

The mathematical theorem at SHA-256
`ca18ef33d9bf3d0b98220df8bfbc965a29373300c0b93f56c35c660a8ac2ef3c`
is promoted at the status-only hash recorded above with this audit as a
written, separately internally audited, nonterminal result.  Any mathematical
change requires a new hash and audit.  No narrow correction is required for
validity.
