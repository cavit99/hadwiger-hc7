# A singleton degree-seven shore forces a nonbipartite opposite shore

**Status:** written proof; separate internal audit GREEN in
[`hc7_singleton_shore_nonbipartite_audit.md`](hc7_singleton_shore_nonbipartite_audit.md).
This theorem
eliminates every bipartite, and hence every tree, exterior in the singleton
`(1,1)` branch of the special exact-seven interface.  It does not eliminate
the remaining odd-cycle exteriors or prove `HC_7`.

## Theorem 1.1

Let `G` be a seven-chromatic graph with

\[
 V(G)=\{a\}\mathbin{\dot\cup}Y\mathbin{\dot\cup}B,
 \qquad |Y|=7,
 \qquad N_G(a)=Y,
 \qquad E_G(\{a\},B)=\varnothing.
\tag{1.1}
\]

If

\[
                  \alpha(G[Y])\le2,
             \qquad \chi(G[Y])\le4,
\tag{1.2}
\]

then

\[
                              \chi(G[B])\ge3.
\tag{1.3}
\]

#### Proof

Seven vertices cannot be partitioned into three independent sets of order
at most two.  Thus (1.2) gives

\[
                              \chi(G[Y])=4.
\]

Suppose `G[B]` were bipartite.  Colour `G[Y]` with four colours and
`G[B]` with two new colours.  Give `a` either one of the latter two colours.
This is proper because `a` has no neighbour in `B`, while its entire
neighbourhood `Y` uses only the first four colours.  It is a six-colouring
of `G`, contradicting `chi(G)=7`.  Hence `chi(G[B])>=3`.  \(\square\)

### Corollary 1.2

In the singleton alternative of the audited
[special two-edge list-critical reduction](hc7_special_exact7_two_edge_list_core.md),
the connected exterior `B=G-N_G[a]` is nonbipartite.  In particular it is
not a tree.

#### Proof

That alternative gives `N_G(a)=Y`, `|Y|=7`, and `E(a,B)=empty`.  Dirac's
neighbourhood-independence inequality gives `alpha(G[Y])<=2`, while the
audited special exact-seven response theorem gives `chi(G[Y])<=4`.
Apply Theorem 1.1.  \(\square\)

## Exact scope

The argument uses no minor-model construction.  It says only that the
singleton exterior contains an odd cycle.  Binary cutvertices and
nonbipartite two-connected exteriors remain open.

## Dependencies for the corollary

- [special two-root list-critical reduction](hc7_special_exact7_two_edge_list_core.md)
- [special exact-seven response theorem](hc7_special_five_plus_two_exact7_response.md)
- Dirac's neighbourhood-independence inequality for contraction-critical
  graphs
