# Independent audit of the two-step reconfiguration collapse

## Verdict and audited revision

**Verdict: GREEN.**

This audit checks the complete source
[`hc7_order8_two_step_reconfiguration_collapse.md`](hc7_order8_two_step_reconfiguration_collapse.md)
at SHA-256

```text
133a9b0fcb3df6dccf71239ba5b431283d75a63c2c133e6cc223c21c7e73ca70
```

Two agents independently checked the suffix-transposition proof and its
host-level specialization.  The distance-two theorem and stated scope are
correct.  The theorem does not prove `HC_7`.

## 1. The suffix-transposition argument

For a shortest path `c_0,...,c_k`, endpoint minimality excludes every
internal colouring from both extension sets.  When `k>=3`, the audited
missing-colour transport theorem applies to `c_1c_2`.  If `c_1` misses
`a` and `c_2` misses `b`, the operated vertex is the unique `b`-vertex in
`c_1` and the unique `a`-vertex in `c_2`; all other vertices have colours
outside `{a,b}`.  Hence the global transposition `(a b)` maps `c_2`
exactly to `c_1`.

Applying that transposition to the whole suffix preserves properness,
one-vertex adjacency, the four-colour threshold and membership of the
target extension language.  The transformed suffix starts at `c_1`, so
splicing it onto the prefix removes one edge and yields a path of length
`k-1`.  This contradicts minimality.  The indexing is exact: the
missing-colour theorem applies at `i=1` precisely when `k>=3`.

If `k=2`, the unique internal state is rejected by both languages.  It is
not surjective by the full-trace ownership hypothesis and therefore uses
exactly four colours.  A globally renamed endpoint edge is impossible by
colour-permutation invariance: for `k=1` it would put one endpoint in both
sets, and for `k=2` it would put the internal state in an endpoint set.

## 2. Host application and trust boundary

Shore extension relations are invariant under permutations of the five
non-root colours.  The maximum-palette theorem supplies exact ownership of
every surjective trace, while the four-or-five-colour connectivity theorem
supplies a path when both shore languages meet that state space.  Therefore
the abstract hypotheses hold in the stated order-nine application.  If the
eight-vertex residual is four-chromatic, every shore trace automatically
uses at least four colours, so the endpoint condition is automatic.

The result eliminates arbitrary chains of palette-deficient intermediate
states.  It leaves either one opposite one-vertex move or one common
rejected four-colour trace.  It does not align remote path endpoints with
named minor branch sets, make the selected list-critical subgraphs unique,
produce a common order-seven boundary colouring, or construct a
`K_7`-minor model.
