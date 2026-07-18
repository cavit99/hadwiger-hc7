# Audit of the root-protected double-loss closure

**Verdict:** GREEN.

**Audited source:**
`results/hc7_root_protected_double_loss_closure.md`

**Current SHA-256:**
`1cd5ae4eac0c518370b7800a174af948f4612bb434e202021d3c7e0704a7433d`

The mathematical revision was independently audited GREEN at SHA-256
`ee249ed1fb6fef07d782c9a16105e2cd47c4ccd1e41f5badebde4e06390f6d5c`.
The current hash differs only in the status line and path.

## Checks

1. In the exceptional lobe-median outcome, ownership by `L` means every
   old edge from `F` to `D,R_1,R_2,R_3` has its `F`-end in `L`.  Thus
   `F_0=F-L` is anticomplete to all four named sets.
2. The degree-two aligned-model provenance gives `F intersect S={f}`,
   `D intersect S={b,x}`, one root in every other non-pole bag, and no
   additional boundary vertex after spanning absorption.
3. Since `f notin L`, the connected set `L` lies in
   `C=G-N[u]`.  It is anticomplete to `u`; hence the one missed named row
   is exactly `{u}`.
4. Ownership makes `f` nonadjacent to the five distinct boundary vertices
   `b,x,r_1,r_2,r_3`.  Dirac's bound `alpha(G[S])<=2` forces those five
   vertices to form a clique.
5. The seven displayed sets are disjoint and connected.  The pole `u`,
   the connected `S`-full set `C union {f}`, and the five singleton clique
   vertices have every one of the 21 required adjacencies.

## Trust boundary

This is conditional on the degree-two aligned-model and protected-root
orientation.  It is not a closure of every one-missing-adjacency model or
of the two exceptional boundary-complement graphs.  It does not prove
`HC_7`.
