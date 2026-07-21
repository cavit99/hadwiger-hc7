# Root contraction does not preserve the normalized-separator rank

**Status:** explicit counterexample to a local compression step, with a
deterministic verifier. It is not a counterexample to `HC_7` or to the
singleton-root completion-or-separation theorem.

## Refuted claim

**False claim.** For every singleton-root near-`K_7` instance with a
normalized dominating `K_5` separator outcome and `R_E` nonempty,
contracting an edge from a root in `R_E` into `E` and lifting a
six-colouring automatically produces a comparable normalized outcome for
the same nonadjacent singleton roots and prescribed path with smaller

`(omega(S,E), |E|, |C_X|)`.

## Construction

Let `C=c_0...c_5c_0` be a six-cycle and let

`H=K_5-{ab,tx}`

on vertices `a,b,t,x,s`. Put `G=C join H`. The graph is seven-connected.
It has the spanning `K_7`-minus-one-edge model

`{a}, {b}, {t}, {s,x}, {c_0,c_1,c_2,c_3}, {c_4}, {c_5}`,

whose only missing branch-set adjacency is `{a}`--`{b}`.

The path `a-x-b` is a shortest root-to-root path through the branch set
`{s,x}`; put `J=G-{a,b}` and `X={x}`. In `J`, the ordered tuple

`({t}, {s}, {c_0,c_1,c_2,c_3}, {c_4}, {c_5})`

is a normalized dominating `K_5` model: its final three branch sets induce
the cycle `C`. The set

`S={s,c_0,c_1,c_2,c_3,c_4,c_5}`

separates `X` from `T_1={t}`. Thus `E={t}`, `C_X={x}`, and
`R_E={a,b}`, giving signature `(9,1,1)`.

Now contract `at`. The first dominating branch set disappears into the
contracted root, and the contracted vertex is adjacent to `b` through the
old edge `tb`. Hence the result no longer has the prescribed nonadjacent
singleton roots. Undoing the contraction restores the original graph and
displayed outcome; without a separate regeneration argument, the colouring
supplies no comparable normalized tuple.

## Exact scope

The graph is five-colourable and contains an explicit `K_7` minor. It
therefore does not refute a theorem that genuinely uses strong
seven-contraction-criticality and `K_7`-minor exclusion. It refutes only the
automatic transition. Any positive proof must supply a separate
**response-to-regeneration lemma** in the original graph: from the
root-edge contraction colouring it must construct an explicit `K_7` model,
an order-seven separation, or a normalized outcome for the same roots and
prescribed path with strictly smaller rank.
