# Internal audit of the normalized root-contraction rank barrier

**Verdict:** GREEN.

Audited source:
`hc7_normalized_root_contraction_rank_barrier.md`.

Source SHA-256:
`bb0b55c7b834e39dca7e68c0f19f17ed4a113875416ea6ed996a517f4c62e366`.

Audited verifier:
`hc7_normalized_root_contraction_rank_barrier_verify.py`.

Verifier SHA-256:
`0baeb78a5a60d954de2d5e40f7d6852efc22c48f6f6147baaa20c6adf16bd99e`.

## Checks

1. For `G=C_6 join (K_5-{ab,tx})`, direct computation gives
   `kappa(G)=7`.
2. The seven displayed spanning branch sets form a
   `K_7`-minus-one-edge model whose only missing adjacency is
   `{a}`--`{b}`.
3. The path `a-x-b` is a shortest root-to-root path through the named old
   branch set. In `J=G-{a,b}`, the displayed ordered five-tuple is a
   dominating `K_5` model, and its final three branch sets induce the
   six-cycle.
4. Deleting `S={s,c_0,...,c_5}` from `J` leaves the components
   `E={t}` and `C_X={x}`. Both roots meet `E`, so the normalized
   signature is exactly `(9,1,1)`.
5. Contracting `at` makes the contracted root adjacent to `b` through
   `tb`; the two-nonadjacent-singleton-root comparison class is not
   preserved. The verifier also supplies a proper six-colouring of the
   contracted graph and checks its expansion on `G-at`.
6. The displayed five-colouring of `G` is proper, and the displayed seven
   bags form an explicit `K_7`-minor model.

## Reproduction

Run:

```text
.venv/bin/python barriers/hc7_normalized_root_contraction_rank_barrier_verify.py
```

Expected final line:

```text
GREEN: normalized root-contraction rank barrier verified
```

## Scope

The example is deliberately five-colourable and has a `K_7` minor. It
does not refute the singleton-root completion theorem or any implication
that genuinely uses all strong contraction-critical and minor-exclusion
hypotheses. It refutes only the automatic root-contraction rank transition.
The frozen frontier now states the missing response-to-regeneration lemma
explicitly and does not treat the tuple as transition-monotone.
