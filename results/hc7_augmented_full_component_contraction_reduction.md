# Contracting an augmented full-component interface

**Status:** written proof; separate internal audit GREEN in
[`hc7_augmented_full_component_contraction_reduction_audit.md`](hc7_augmented_full_component_contraction_reduction_audit.md).

This note treats the boundary-full outcome of the fresh-colour
augmented-boundary theorem.  Contracting the distinguished boundary edge
does not solve the branch-set allocation problem, but it converts the
order-eight asymmetric interface into an exact order-seven interface with
one boundary-full connected component on each side.  It also gives two
explicit minor decoders.  Nothing here proves `HC_7`.

## 1. Setting

Let `G` be seven-connected and `K_7`-minor-free.  Let

\[
                      X=Y\mathbin{\dot\cup}\{p\},
                      \qquad |Y|=7,                    \tag{1.1}
\]

and suppose that `A,D` are distinct components of `G-X` satisfying

\[
                         N_G(A)=Y,
                 \qquad N_G(D)=X.                     \tag{1.2}
\]

Let `v in Y` and `pv in E(G)`.  Put `H=G/pv`, let `x` be the contraction
image, and set

\[
                         S=(Y-\{v\})\cup\{x\}.          \tag{1.3}
\]

The hypotheses are exactly the non-colouring outcome 3 of the audited
fresh-colour augmented-boundary theorem.

## 2. Exact order-seven reduction

### Theorem 2.1 (split-vertex exact-seven interface)

In the setting above:

1. `|S|=7`, and `A,D` are distinct, anticomplete connected components of
   `H-S` with

   \[
                              N_H(A)=N_H(D)=S;          \tag{2.1}
   \]

2. if, for either `C in {A,D}`, the graph `H-C` contains a `K_6`-minor
   model every one of whose six branch sets meets `S`, then `G` contains a
   `K_7` minor;
3. if some `y in Y` satisfies

   \[
                         K_5\preccurlyeq G[Y-\{y\}],    \tag{2.2}
   \]

   then `G` contains a `K_7` minor.

Consequently, in the surviving `K_7`-minor-free case,

\[
       K_5\not\preccurlyeq G[Y-\{y\}]
       \quad\text{for every }y\in Y.                  \tag{2.3}
\]

By the established case `HC_5`, every graph `G[Y-{y}]` in (2.3) is
four-colourable.

#### Proof

The set in (1.3) has order seven.  The component `A` has no neighbour in
`p` and is adjacent to every vertex of `Y`.  After the contraction, the
neighbours represented by `v` make `A` adjacent to `x`, while all other
members of `S` remain literal members of `Y`.  Since `A` had no neighbour
outside `Y`, this proves `N_H(A)=S`.

The component `D` is adjacent to every vertex of `X`, so after identifying
`p,v` it is adjacent to every member of `S`.  It had no neighbour outside
`X`; hence `N_H(D)=S`.  The two sets remain connected and anticomplete,
because they were distinct components of `G-X`.  This proves item 1.

For item 2, let `M_1,...,M_6` be the asserted model in `H-C`.  Every
`M_i` contains a vertex of `S`, and the `S`-full component `C` has a
neighbour at that literal vertex.  Therefore

\[
                            C,M_1,\ldots,M_6            \tag{2.4}
\]

are seven disjoint connected pairwise adjacent branch sets in `H`.  They
form a `K_7`-minor model in the minor `H` of `G`, and hence in `G`.

For item 3, let `M_1,...,M_5` be a `K_5` model in `G[Y-{y}]`.  The seven
sets

\[
                         A,\quad D\cup\{y\},\quad
                         M_1,\ldots,M_5                 \tag{2.5}
\]

are pairwise disjoint.  They are connected: `D` has a neighbour at `y`.
The five `M_i` form a clique model.  Both of the first two sets are adjacent
to every `M_i`, because `A,D` have neighbours at every literal vertex of
`Y`.  Finally `A` is adjacent to `D union {y}` through a neighbour of `y`
in `A`.  Thus (2.5) is an explicit `K_7`-minor model.  Statements (2.3)
and the four-colour conclusion follow. \(\square\)

## 3. Consequence for regenerated models

Assume additionally that `G` is a hypothetical minor-minimal counterexample
to `HC_7`.  Then the contracted graph `H` is exactly six-chromatic and
six-connected.  For either `C in {A,D}`, precisely one of the following
holds:

1. `chi(H-C)<=5`; or
2. `chi(H-C)=6`, and every `K_6`-minor model in `H-C` has at least one
   branch set disjoint from `S`.

Indeed, `H-C` is a proper minor and so is at most six-colourable.  In the
six-chromatic case, `HC_6` supplies a `K_6` model; Theorem 2.1(2) excludes
one whose every branch set meets `S`.

Thus a surviving model necessarily spends one of its six labels entirely
away from the order-seven boundary.  Absorbing the other full component can
repair a missing adjacency only if a connected replacement for that spent
label is also produced.

## 4. Exact scope

The theorem is unbounded and uses literal branch sets.  It strictly lowers
the displayed interface from eight boundary vertices in `G` to seven in
the contracted graph `H`, but it is not a recursive counterexample: `H` is
six-colourable.  It does not produce an `S`-meeting `K_6` model, a common
shore colouring, or a fixed two-vertex `K_5`-minor transversal.

The rural two-apex constructions show that the hypotheses in Sections 1--2
alone cannot force the missing rooted model.  They realize the exact
defect-one/full-component geometry and an extremal contracted-edge model,
but are six-colourable and possess a coherent two-vertex planarizing pair.
Any closure must therefore use the rejection of a common six-colouring,
not only static fullness or fan paths.

## 5. Dependencies

- [fresh-colour linkages and augmented-boundary transition](hc7_exact7_fresh_colour_linkage.md)
- Hadwiger's Conjecture for `t=5` and `t=6`.
