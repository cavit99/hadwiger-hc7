# Label obstruction at the degree-eight singleton outcome

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_singleton_label_obstruction_audit.md`](hc7_order8_singleton_label_obstruction_audit.md).
This note treats the singleton outcome of the six-label branch-set transfer
theorem.  It does not eliminate that outcome or prove `HC_7`.

## 1. Setting

Let `G` be a seven-connected graph with no `K_7` minor.  Suppose that its
vertex set is partitioned into seven nonempty connected branch sets

\[
                     X,Y,D,U,F_1,F_2,F_3,              \tag{1.1}
\]

which form a spanning labelled `K_7`-minus-one-edge model whose only
possible missing adjacency is `X-Y`.  Fix the roots, response subgraph,
boundary partition and relaxed first-hit rank from the six-label
branch-set transfer theorem.  In particular, the ranked labels form a
subset of `\{X,Y,U,F_1,F_2,F_3\}` containing `U`, paths may overlap inside
the fixed response subgraph `Z_0 subseteq D`, and there is a fixed edge

\[
                       z_0u_0,
              \qquad z_0\in Z_0,\quad u_0\in U.       \tag{1.2}
\]

Among the compatible spanning labelled models, first maximize that rank
and then minimize `|U|`.

Assume that an eight-boundary component has reduced to a singleton
`{v}` contained in `U`.  Thus

\[
 U=U_0\mathbin{\dot\cup}\{v\},\qquad
 U_0\ne\varnothing\text{ is connected},               \tag{1.3}
\]

the prescribed root of `U` and `u_0` lie in `U_0`, and

\[
 N_G(v)=S=
 \{k_1,k_2,s_X,s_Y,s_D,s_{F_1},s_{F_2},s_{F_3}\},     \tag{1.4}
\]

where `k_1,k_2 in U_0`, `s_R in R` for every foreign label `R`, and every
displayed vertex is adjacent to `v`.  In particular, `d_G(v)=8`.

For a foreign branch-set label put

\[
 \Omega=\{R\in\{X,Y,D,F_1,F_2,F_3\}:
                    E_G(U_0,R)=\varnothing\}.          \tag{1.5}
\]

The fixed edge (1.2) gives

\[
                              D\notin\Omega.            \tag{1.6}
\]

## 2. At least two lost labels

### Theorem 2.1

In the setting above,

\[
                              |\Omega|\ge2.             \tag{2.1}
\]

#### Proof

Suppose first that `Omega` is empty.  Move `v` from `U` to `D`, replacing

\[
                       U\longmapsto U_0,
             \qquad    D\longmapsto D\cup\{v\}.       \tag{2.2}
\]

The first replacement is connected.  The second is connected through
the edge `vs_D`.  It is adjacent to `U_0` through `vk_1`, and `U_0`
retains an edge to every other foreign branch set because `Omega` is
empty.  All other required model adjacencies are unchanged.  Hence (2.2)
is another spanning labelled `K_7`-minus-one-edge model with a smaller
`U`.

Now suppose that `Omega={R}`.  Move `v` from `U` to `R`.  The set
`R union {v}` is connected through `vs_R`, is adjacent to `U_0` through
`vk_1`, and `U_0` retains every required foreign adjacency except the one
to `R`, which has just been restored through `v`.  If `R` is `X` or `Y`,
the edge from `v` to the opposite polar branch set repairs `X-Y`; in
that event the seven replacement sets are an explicit `K_7`-minor model.
Otherwise the replacements again form a spanning labelled
`K_7`-minus-one-edge model with a smaller `U`.

It remains to check the extremal data.  All prescribed roots remain in
their old branch sets, because the prescribed `U`-root lies in `U_0`.
The boundary partition and `Z_0` are unchanged; in the first case `Z_0`
is merely contained in the enlarged branch set `D union {v}`.  A ranked
first-hit path ending at a label different from `U` avoided the old
branch set `U`, and hence avoided `v`; it therefore survives.  If the
ranked `U`-path ended at `v`, retain its designated source port, join that
port to `z_0` inside connected `Z_0`, and append the fixed edge `z_0u_0`.
Overlaps inside `Z_0` are permitted, while outside `Z_0` the replacement
has only the new endpoint `u_0`.  Every other ranked path avoided the old
`U`, so it avoids `u_0`.  Thus the relaxed first-hit rank does not
decrease.

The `K_7` outcome contradicts the hypothesis on `G`; every other outcome
contradicts the maximum-rank, minimum-`|U|` choice.  Therefore neither
`|Omega|=0` nor `|Omega|=1` is possible. \(\square\)

## 3. A polar label is necessarily lost

### Theorem 3.1

In the same setting,

\[
                         \Omega\cap\{X,Y\}\ne\varnothing.       \tag{3.1}
\]

#### Proof

Suppose that neither `X` nor `Y` belongs to `Omega`.  Then `U_0` is
adjacent to both `X` and `Y`.  The following seven sets are pairwise
disjoint and connected:

\[
       U_0\cup X,\quad \{v\},\quad Y,\quad D,
                    \quad F_1,\quad F_2,\quad F_3.     \tag{3.2}
\]

The first set is connected through an edge from `U_0` to `X`.  It is
adjacent to `Y` through an edge from `U_0` to `Y`, and it is adjacent to
`D,F_1,F_2,F_3` through the old edges from `X`.  The singleton `{v}` is
adjacent to each of the other six sets by (1.4).  Finally,
`Y,D,F_1,F_2,F_3` are pairwise adjacent in the old model.  Hence (3.2) is
an explicit `K_7`-minor model, a contradiction. \(\square\)

### Corollary 3.2 (three-owner normal form)

If the provenance of the singleton additionally gives `|Omega|=3`, then,
up to interchanging `X,Y` and permuting `F_1,F_2,F_3`, exactly one of the
following two label patterns remains:

\[
             \Omega=\{X,Y,F_1\},
       \qquad\text{or}\qquad
             \Omega=\{X,F_1,F_2\}.                  \tag{3.3}
\]

#### Proof

Equation (1.6) excludes `D`, Theorem 3.1 requires at least one of `X,Y`,
and the stated symmetries give precisely the two possibilities according
to whether both or only one of `X,Y` occurs. \(\square\)

## 4. The boundary cannot contain a vertex-deleted `K_5` model

### Theorem 4.1

Let `Q` be any component of `G-S` different from `{v}`, and suppose that

\[
                              N_G(Q)=S.                \tag{4.1}
\]

Then

\[
                    K_5\not\preccurlyeq G[S-w]
                         \qquad(w\in S).               \tag{4.2}
\]

#### Proof

Suppose that `M_1,...,M_5` is a `K_5`-minor model in `G[S-w]`.  Then

\[
                    \{v,w\},\quad Q,\quad
                    M_1,M_2,M_3,M_4,M_5               \tag{4.3}
\]

are seven pairwise disjoint connected sets.  The first set is connected
because `vw` is an edge.  It is adjacent to every `M_i` through `v`, and
it is adjacent to `Q` through an edge from `w` to `Q`.  The component `Q`
is adjacent to every `M_i`, because every `M_i` contains a vertex of `S`
and `Q` is adjacent to every literal vertex of `S`.  The five sets `M_i`
are pairwise adjacent by assumption.  Thus (4.3) is an explicit
`K_7`-minor model, contrary to the hypothesis on `G`. \(\square\)

## 5. Exact gain and remaining obstruction

The singleton is therefore not an arbitrary degree-eight residue.  At
least two required foreign adjacencies of `U_0` are realized only through
`v`, and at least one of those labels is an endpoint of the unique missing
model adjacency `X-Y`.  In the three-owner branch this leaves only the two
patterns (3.3).  Independently, every vertex-deleted boundary graph is
`K_5`-minor-free whenever an opposite boundary-full component is present.

These conclusions do not eliminate the singleton.  The opposite component
in Theorem 4.1 need not be disjoint from the inherited branch sets: the
model is spanning, so treating that component as one additional branch set
would double-count vertices.  A completion still has to repartition that
component while preserving the six foreign branch-set labels, or return an
order-seven separation carrying one equality partition through both closed
shores.

The deficient-singleton persistence theorem is not directly applicable:
`v` has the common label `U`, rather than an endpoint of the missing
`X-Y` adjacency, and the old branch set `U=U_0 union {v}` is not a
singleton.  Likewise, the degree-eight cyclic contact-allocation theorem
requires five cyclic connected sets and three correctly incident connected
sets; those objects do not follow merely from (1.1)--(1.4).  Reselecting a
model rooted at `(U,v)` may provide deletion-persistent incident edges, but
without an additional argument it need not preserve the selected boundary
partition, the two vertices labelled `U`, or the six literal boundary
representatives in (1.4).

## 6. Dependencies

- the extremal setting and rank-preserving replacement path from
  [the six-label branch-set-contained component reduction](../results/hc7_order8_six_label_donor_fan_reduction.md);
- the spanning labelled order-eight normal form from
  [reserved-component completion](../results/hc7_reserved_component_linkage_completion.md).
