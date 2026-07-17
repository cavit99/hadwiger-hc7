# A two-vertex `K_5`-model transversal yields an order-seven separation

**Status:** written proof; separate internal audit GREEN.  This removes the
fixed-pair conclusion as a separate terminal outcome in the minimal
`HC_7` setup.  It does not prove that such a pair or separation exists.

## Theorem 1.1

Let `G` be a seven-connected, seven-chromatic graph with no `K_7` minor,
and suppose every proper minor of `G` is six-colourable.  If two vertices
`p,q` meet every `K_5`-minor model in `G`, then `G` has an actual
separation of order seven.

### Proof

Put

\[
                         H=G-\{p,q\}.
\]

The graph `H` has no `K_5` minor, since any such model would avoid both
`p,q`.  The sharp edge bound for `K_5` minors gives

\[
                         |E(H)|\le 3|V(H)|-6.
\]

Hence `H` has a vertex `v` with `d_H(v)<=5`.  Since only `p,q` were
deleted,

\[
                         d_G(v)\le7.
\]

Seven-connectivity gives the reverse inequality, so `d_G(v)=7`.

The vertex `v` is not universal.  If it were, then `G-v` would be
six-chromatic: it is six-colourable as a proper minor, while a colouring
with at most five colours would extend to a six-colouring of `G` by giving
`v` a new colour.  The proved case `HC_6` would then give a `K_6` minor in
`G-v`, and the universal singleton `{v}` would extend it to a `K_7` minor
in `G`, a contradiction.

Choose a non-neighbour `w` of `v`.  The pair

\[
       (\{v\}\cup N_G(v),\ V(G)-\{v\})
\]

is an actual separation: its boundary is `N_G(v)`, its first open side is
`{v}`, and its second open side contains `w`.  Its order is
`d_G(v)=7`.  \(\square\)

## Consequence

Within a hypothetical minor-minimal counterexample, a proposed terminal
alternative of the form

\[
          \text{“two vertices meet every `K_5` model”}
\]

need not be carried separately.  It already implies the order-seven
separation outcome.  The unresolved task is still to align proper-minor
six-colourings across that separation.

## External input

The proof uses the classical sharp edge bound for `K_5` minors: every
`n`-vertex graph with no `K_5` minor has at most `3n-6` edges.  This is a
standard consequence of Wagner's structure theorem.
