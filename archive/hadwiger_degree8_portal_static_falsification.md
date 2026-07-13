# Explicit falsification of a coarse degree-eight portal dichotomy

## Encoded graph

Let \(N=\{0,\ldots,7\}\), let \(z\) be a portal, and add shore vertices
\(r_1,r_2,d\).  Put

\[
E(G[N])={01,07,17,24,45,35,36,26\};
\]

thus \(G[N]\cong K_3\mathbin{\dot\cup}C_5\) and
\(\alpha(G[N])=3\).  Add

\[
N(z)\cap N=\{2\},
\]

make each \(r_i\) adjacent to \(z\) and every vertex of
\(N-\{0,1\}\), and make \(d\) adjacent to every vertex of
\(N-\{0\}\) but not to \(z\).  The three shore vertices are pairwise
nonadjacent.  Finally, for the complementary-state test, add an apex \(v\)
adjacent exactly to \(N\).

This satisfies precisely the coarse data obtained by splitting one of two
degree-eight exterior components at a cutvertex:

* two portal-meeting shores of boundary defect two;
* one portal-avoiding shore of boundary defect one; and
* \(\alpha(N)\le3\).

## Exhaustive conclusions

The direct verifier `degree8_portal_static_falsification_verify.py` proves:

1. the graph on \(N\cup\{z,r_1,r_2,d\}\) has no \(N\)-meeting
   \(K_6\)-model;
2. among every partition of \(X=N\cup\{z\}\) into at most six
   independent blocks, with at most five blocks meeting \(N\), none is
   clique-realized by the complement of each of the three pieces
   \(X+r_1,X+r_2,X+d\).

For item 1 the verifier exhausts all 462 partitions of an arbitrary used
subset of \(N\) into six nonempty bag traces and all \(7^4\) placements or
omissions of \(z,r_1,r_2,d\).  For item 2 it checks 19,052 eligible
partitions of \(X\), of which 2,355 are independent, and every assignment
of \(v\) and the two complementary shores to their branch sets.

Expected output:

```text
alpha(N)<=3 verified
no N-meeting K6 portal-quotient model
static exact states checked: 19052 candidate partitions; 2355 independent
no common complementary realization for R1,R2,D
```

## Exact scope

This is a counterexample to the static local implication

\[
\text{defect bounds + }\alpha(N)\le3
\Longrightarrow
\text{an }N\text{-meeting }K_6\text{ or common complementary state}.
\]

It is not asserted to be seven-connected, contraction-critical, or a
counterexample to Hadwiger.  In particular it is not required to satisfy
the one-step transition condition proved in
`hadwiger_portal_exact_boundary_transfer.md`.  Its purpose is to show
exactly why minor-transition information must be added before attempting
to close the full cutvertex family.
