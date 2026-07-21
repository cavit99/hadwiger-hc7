# Normal form for the last pole move at a bounded interface

**Status:** written proof; [separately audited **GREEN**](hc7_bounded_interface_pole_move_normal_form_audit.md).
This is a nonterminal refinement of the exact-block Kempe reduction.  It
shows that a last pole move can be made pole-free unless it has one precise
five-block/six-block form.  It does not synchronize the two shore
colourings, force disjoint endpoint pairs, or prove `HC_7`.

## 1. Setup

Use the bounded-interface notation from the exact-block Kempe reduction.
Thus `G` is a hypothetical minor-minimal counterexample to `HC_7`, `u` is
a vertex of degree seven to nine, `C` is a component of `G-N[u]`,

\[
 S=N_G(C)\subseteq N(u),\qquad
 A=G[C\cup S],\qquad B=G-C,
\]

and `I` is a nonempty independent subset of `S`.

Let

\[
                         \phi_0,\phi_1,\ldots,\phi_k    \tag{1.1}
\]

be a shortest exact-`I` boundary Kempe transition, minimized over its
endpoint choices, from a colouring extending through `A` to one extending
through `B`.  The colour on `I` is fixed throughout and every interchange
avoids that colour.  Then `k>=1`, `phi_{k-1}` does not extend through `B`,
and `phi_k` does.  Fix a proper six-colouring `c` of `B` inducing `phi_k`
and write

\[
                              \delta=c(u).              \tag{1.2}
\]

The colour `delta` is absent from `S`.

## 2. Pole-move normal form

### Theorem 2.1

Suppose the last interchange in (1.1) is a pole move.  In the forward
direction it changes one boundary vertex `x` from colour `delta` to a
colour `beta`; equivalently, the reverse interchange starting at `phi_k`
assigns `x` the colour of `u`.

Then at least one of the following holds.

1. **Pole-free realization of the same last transition.**  For some proper
   six-colouring `hat c` of `B` inducing the same final boundary colouring
   `phi_k`, there is a `hat c`-bichromatic `delta`--`beta` path from `x` to
   another boundary two-colour component whose internal vertices lie in
   `B-(S union {u})`.
2. **Tight pole residue.**  The final boundary colouring `phi_k` uses
   exactly five colours, its `beta`-class contains `x` and at least one
   other boundary vertex, is disjoint from `I`, and `phi_{k-1}` uses all
   six colours.  Moreover, for every extension `c_*` of `phi_k` through
   `B`, the component of `x` in

   \[
             B[c_*^{-1}(\{\delta,\beta\})]-u           \tag{2.1}
   \]

   meets `S` only in `x`.

Thus a genuine last-pole obstruction is exactly a six-block-to-five-block
boundary move in which `x` merges into a non-singleton independent
`beta`-block and the universal pole is the only two-colour connection from
`x` to the rest of that boundary block.

### Proof

Because `delta` is absent from `S`, every component of the boundary
`delta`--`beta` graph under `phi_k` is a singleton `beta`-coloured vertex.
In particular, the operated component is `{x}`.

Suppose first that `phi_k` uses at most four colours on `S`.  Besides
`delta`, choose another colour `epsilon` absent from `S`.  In the full
colouring `c`, interchange `delta,epsilon` on the full two-colour component
containing `u`.  Neither colour occurs on `S`, so this interchange leaves
the complete labelled boundary colouring unchanged.  It gives another
extension `c'` of `phi_k` through `B`, now with `c'(u)=epsilon`.

Apply the one-interchange lifting lemma in reverse to the last
`delta`--`beta` move.  If the full `delta`--`beta` component of `c'`
containing `x` met no other boundary component, switching that full
component would extend `phi_{k-1}` through `B`.  This contradicts the
endpoint minimality of (1.1).  Hence a shortest path from `x` to the first
other boundary component exists.  Its internal vertices avoid `S`; they
also avoid `u`, whose colour in `c'` is `epsilon`.  This is outcome 1.

We may therefore assume that `phi_k` uses exactly five boundary colours.
The `beta`-class cannot be the singleton `{x}`.  If it were, replacing
`beta` by the previously absent colour `delta` would not change the
boundary equality partition: `phi_{k-1}` and `phi_k` would differ only by
a global permutation of the colour names `beta,delta`.  Since boundary
extension is invariant under colour permutations, `phi_{k-1}` would then
extend through `B`, again contradicting minimality.  Thus another boundary
vertex has colour `beta` in `phi_k`.

The fixed exact block `I` uses a colour excluded from every interchange,
so the `beta`-block is disjoint from `I`.

It follows that `phi_{k-1}` uses all six colours: the forward last move
removes the singleton `delta`-block `{x}` and inserts `x` into an already
nonempty `beta`-block, while leaving the other five colours present.

Finally consider any extension `c_*` of `phi_k` through `B`.  The unique
boundary-absent colour is `delta`, so `c_*(u)=delta`.  If the component of
`x` in (2.1) met another boundary vertex, choose a shortest path from `x`
to its first such vertex.  Its internal vertices would lie in
`B-(S union {u})`.  Since distinct `beta`-coloured boundary vertices are
distinct components of the boundary two-colour graph, this would be
outcome 1.  If outcome 1 never occurs, (2.1) meets `S` only in `x` for
every extension, and every assertion of outcome 2 holds.  \(\square\)

## 3. Consequence for transition surgery

The theorem removes every last pole move whose final boundary trace uses
at most four colours.  It also removes the five-colour case whenever the
two-colour component of the moved vertex has a route to the rest of its
new colour block which avoids `u`.

In the remaining configuration, deleting `ux` removes the direct edge
which forbids `u` and `x` from sharing a colour, but it need not make this
particular boundary interchange lift: another `delta`--`beta` route may
still join `x` to `u` or to the rest of the `beta`-block.  Proper-minor
minimality supplies only an uncontrolled colouring of `G-ux`.  The existing
anchored-response theorem does not place that colouring in the same
shortest transition or preserve the displayed `beta`-block.  Splicing it
into (1.1) therefore requires a new operation-coupling assertion;
transition length and endpoint overlap alone do not provide one.

Even outcome 1 is nonterminal.  Its path may share a boundary endpoint
with the first `C`-shore obstruction, and the two paths still require an
explicit `K_7`-minor construction, a common complete boundary partition,
or the exact aligned component descent.

## 4. Dependency

The only input is the one-interchange lifting argument in
[`hc7_bounded_interface_exact_block_kempe_reduction.md`](hc7_bounded_interface_exact_block_kempe_reduction.md),
especially Lemma 3.1 and Theorem 4.1.
