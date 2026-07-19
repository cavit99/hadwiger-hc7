# Completion of a shared portal at an end of a nontrivial path component

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_endpoint_shared_portal_completion_audit.md`](hc7_order8_endpoint_shared_portal_completion_audit.md).
This note treats the endpoint case omitted by the internal
shared-portal minor construction.  It does not treat a singleton component
and does not prove `HC_7`.

## Theorem 1.1

Let `G` be seven-connected, not six-colourable, and `K_7`-minor-free, and
assume every proper minor of `G` is six-colourable.  Let `S` have order
eight and suppose that `G-S` has exactly three components, each adjacent to
every literal vertex of `S`.  Suppose one component is the induced path

\[
                         P=p_0p_1\cdots p_m,
                         \qquad m\ge1.                 \tag{1.1}
\]

In the shared-portal outcome of the audited overlapping-interval normal
form, if the shared portal is `p_0` or `p_m`, an actual order-seven
separation is returned.

## Proof

By reversing the path, it is enough to treat a shared portal at `p_0`.
Use the normal-form notation `d,e`; in particular `p_0` is adjacent to
both `d,e`.  Put

\[
                         A=\{p_0\},\qquad B=P[1,m].    \tag{1.2}
\]

The suffix conclusion in the shared-portal normal form either already
returns an actual order-seven separation or says that `B` is adjacent to
every vertex of `S-\{e\}`.  Assume the latter.

Because `P` is an induced component of `G-S`,

\[
                    N_G(p_0)=\bigl(N_G(p_0)\cap S\bigr)
                               \mathbin{\dot\cup}\{p_1\}.           \tag{1.3}
\]

This neighbourhood separates `p_0` from either of the other two
components.  Seven-connectivity gives

\[
                         |N_G(p_0)\cap S|\ge6.         \tag{1.4}
\]

Equality in (1.4) makes (1.3) an actual order-seven boundary.  Otherwise
`p_0` is adjacent to at least seven vertices of `S`.  Choose `f\ne e` so
that `p_0` is adjacent to every vertex of `S-\{f\}`: take the unique missed
vertex when there is one, and choose any vertex other than `e` when
`p_0` is `S`-full.  Such an `f` is distinct from `e` because `p_0e` is an
edge.

The other two components of `G-S`, denoted `Q_0,Q_1`, are `S`-full.  Thus
the four connected subgraphs

\[
                            Q_0,Q_1,A,B                \tag{1.5}
\]

are pairwise disjoint, `A,B` are adjacent, `A` is adjacent to every vertex
of `S-\{f\}`, and `B` to every vertex of `S-\{e\}`.

The audited three-component boundary classification says that `G[S]`
contains two vertex-disjoint odd cycles.  If `G[S-\{f,e\}]` is
nonbipartite, it contains an odd cycle of order three or five.  Lemma 1.1
of the [strict-reversal completion](hc7_order8_strict_reversal_completion.md),
applied with defects `f,e`, gives an explicit `K_7`-minor model, a
contradiction.

It remains to suppose that

\[
                         S-\{f,e\}=X\mathbin{\dot\cup}Y             \tag{1.6}
\]

is bipartite.  Both classes are nonempty, and each of `f,e` has a neighbour
in each class.  Indeed, every one of the two disjoint odd cycles must meet
`\{f,e\}`; neither can contain both, since then the other would be an odd
cycle in the bipartite graph (1.6).  Removing `f` or `e` from its respective
odd cycle leaves an odd-length path with ends in opposite classes.

Suppose first that `fe` is not an edge.  Give `X`, `Y`, and `\{f,e\}`
three distinct colours, and colour the path `P` with two fresh colours.
This properly colours `G[P\cup S]` and induces the partition

\[
                              X\mid Y\mid\{f,e\}.       \tag{1.7}
\]

For `i\in\{0,1\}`, write `j=1-i` and contract spanning trees of

\[
                     A\cup X,\qquad B\cup Y,
                     \qquad Q_j\cup\{f,e\}.            \tag{1.8}
\]

The three sets are disjoint and connected.  Their images form a triangle:
the first two are adjacent through `p_0p_1`, the first meets the third
through `e`, and the second meets it through `f`.  A six-colouring of this
proper minor restricts and expands to a colouring of `G[Q_i\cup S]` which
induces exactly (1.7).  The three closed-side colourings align and glue,
contrary to the choice of `G`.

Finally suppose that `fe` is an edge.  Colour `X,Y,\{f\},\{e\}` with four
distinct colours and again colour `P` with two fresh colours.  For each
`i`, contract spanning trees of

\[
                              A\cup X,qquad B\cup Y.   \tag{1.9}
\]

Their two images together with the unchanged vertices `f,e` form a
four-clique.  The images are adjacent through `p_0p_1`; the first image is
adjacent to `e` through `A` and to `f` through a boundary edge from `f`
to `X`; symmetrically the second is adjacent to `f` through `B` and to
`e` through `Y`; and `fe` is an edge.  A six-colouring of the resulting
proper minor restricts to `G[Q_i\cup S]` with the exact four-block boundary
partition.  These two colourings and the direct path-side colouring again
align and glue, a contradiction.

Every alternative to an actual order-seven separation has therefore led
to either a `K_7` minor or a six-colouring. \(\square\)

## Corollary 1.2

In the exact three-component boundary-full setting, if the selected
component is an induced path with at least two vertices, every overlap
outcome of the audited interval normal form returns an actual order-seven
separation or gives an explicit `K_7` minor or a six-colouring.

### Proof

Strict reversal is covered by the audited strict-reversal completion.  An
internal shared portal is covered by the audited path-component minor
construction.  Theorem 1.1 covers a shared portal at either endpoint.
These are all outcomes of the interval normal form. \(\square\)

## Trust boundary

The theorem returns an actual order-seven separation but does not prove
that its two closed shores induce a common equality partition.  The result
does not cover a singleton selected component, a non-path component, the
two-component order-eight interface, or any degree-eight/nine case outside
the stated setting.

## Dependencies

- the [overlapping-interval path normal form](hc7_order8_overlapping_interval_normal_form.md);
- the [three-component boundary classification](hc7_order8_three_component_boundary_classification.md);
- the [strict-reversal completion](hc7_order8_strict_reversal_completion.md); and
- the [internal shared-portal construction](hc7_order8_three_component_path_completion.md).
