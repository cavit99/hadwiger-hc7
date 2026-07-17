# Pentagonal order-seven separation completion

**Status:** written corollary; separate internal audit GREEN.

## Corollary

Let `G` be a 7-connected graph. Suppose that

\[
S=\{p,q,c_1,c_2,c_3,c_4,c_5\}
\]

induces the join of the edge `pq` and the chordless cycle

\[
C=c_1c_2c_3c_4c_5c_1.
\]

Suppose also that `G-S` has exactly two nonempty connected components `A`
and `B`. If `G-\{p,q\}` contains a `K_5` minor, then `G` contains a
`K_7` minor.

### Proof

Each of `A,B` is adjacent to every vertex of `S`. Otherwise, if (say) `A`
missed `s\in S`, then

\[
                         N_G(A)\subseteq S-\{s\},
\]

while the nonempty component `B` lies on the other side of a separation of
order at most six. This contradicts 7-connectivity.

The hypotheses of the
[cycle-boundary completion theorem](hc7_cycle_boundary_completion.md)
now hold with the induced cycle `C` and the two full shores `A,B`. That
theorem gives a `K_7` minor in `G`. \(\square\)

## Automatic hypothesis in a minimal `HC_7` counterexample

The `K_5`-minor hypothesis is automatic when `G` is a minor-minimal
7-chromatic graph with no `K_7` minor. If `G-\{p,q\}` were
4-colourable, giving `p,q` two fresh colours would six-colour `G`.
Therefore

\[
                         \chi(G-\{p,q\})\ge5.
\]

The established `t=5` case of Hadwiger's Conjecture then gives a `K_5`
minor in `G-\{p,q\}`, so the corollary gives the forbidden `K_7` minor.

## Scope

The distinct content of this corollary is that, for the exact seven-vertex
boundary, 7-connectivity forces the full-shore hypothesis required by the
cycle-boundary theorem. It also records why the `K_5`-minor hypothesis is
automatic in the minimal `HC_7` setting. The rooted-minor planarity proof
belongs to the canonical cycle-boundary theorem and is not duplicated here.
