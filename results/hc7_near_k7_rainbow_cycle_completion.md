# Rainbow-cycle completion

## Status

This note closes the unique-shadow outcome of the spanning singleton
bipartite shell.  Its mechanism is uniform: a clique of ordinary labels,
two poles complete to that clique, and one internal vertex complete to the
clique need only lie on one common cycle.  Three pole-to-pole paths are not
needed.

## Theorem 1 (three-root cycle completion)

Let `C` be a clique in a graph `G`.  Let `v,b,x` be three distinct vertices
outside `C`, each adjacent to every vertex of `C`.  If `G-C` contains a
cycle through `v,b,x`, then `G` contains a `K_{|C|+3}` minor.

### Proof

Let `Z` be such a cycle.  Its two `v-b` arcs are denoted by `P` and `Q`,
with `x` internal to `P`.  Put

\[
                         R=V(P)-\{v,b\}.
\]

Then `R` is nonempty and connected.  Choose any edge `yz` of the other arc
`Q`, oriented from `v` toward `b`, and split `Q` at that edge:

\[
 X=V(vQy),\qquad Y=V(zQb).
\]

The sets `X,Y,R` are nonempty, pairwise disjoint and connected.  They are
pairwise adjacent: `yz` joins `X` to `Y`, the first edge of `P` joins `X`
to `R`, and the last edge of `P` joins `R` to `Y`.  Moreover `X` contains
`v`, `Y` contains `b`, and `R` contains `x`.  Hence each of `X,Y,R` is
adjacent to every singleton bag `{c}`, `c in C`.  Together with those
`|C|` singleton bags they form a `K_{|C|+3}` model.  QED.

The edge `yz` exists even when `vb` is an edge; in that case one may take
`X={v}`, `Y={b}`.  In the application below `vb` is in fact absent.

## Theorem 2 (connected remainder corollary)

If `G-C` is 3-connected, then every three distinct vertices `v,b,x` of
`G-C` lie on a common cycle.  Consequently, under the adjacency hypotheses
of Theorem 1, `G` contains a `K_{|C|+3}` minor.

### Proof

The first assertion is the three-vertex case of the elementary fan lemma.
For completeness, delete `x`.  The remaining graph is 2-connected, so it
has a cycle `Z` through `v,b`.  The 3-fan lemma supplies three internally
disjoint paths from `x` to three distinct attachment vertices of `Z`,
with their other vertices outside `Z`.  The three attachment vertices cut
`Z` into three cyclic intervals.  At most two interval interiors contain
one of `v,b`, so one interval has neither pole in its interior.  Use the
two fan paths ending at the ends of this interval, together with the
complementary arc of `Z`.  The resulting cycle contains `x` and both
poles (a pole equal to an interval end is retained as an end).  Apply
Theorem 1.  QED.

## Corollary 3 (unique apex shadow is impossible)

Use the spanning singleton setup of
`../archive/hc7_near_k7_bipartite_shadow_exchange.md` with `G`
`(r+1)`-connected.
In the unique-shadow outcome let

\[
                 C=\{b_i:i\ne j\}.
\]

Then `G` contains a `K_{r+1}` minor.

### Proof

The unique-shadow conclusion gives that both poles `v,b_j` are adjacent
to every vertex of `C`.  Lemma 5.3 of the cited note supplies a vertex
`x` of the bipartite bag adjacent to every vertex of `C` (and to at least
one pole, although that last fact is unnecessary here).  Connectivity
drops by at most the number of deleted vertices, so

\[
              \kappa(G-C)\ge (r+1)-(r-2)=3.
\]

Theorem 2 applied to `v,b_j,x` gives a `K_{(r-2)+3}=K_{r+1}` minor.  QED.

## Scope and consequence

The proof uses literal singleton labels only to turn saturation of `x`
into adjacency to every member of the clique `C`.  It does not use the
Moser spindle, a portal order, or a prescribed theta.  For `HC_7`, `C` is
a literal `K_4`; hence the former non-rainbow crossed-theta outcome is
empty.

This closes the `d=1` part of proof-spine link P4.  The two-cut and
two-vertex portal-concentration parts of P4 remain open, as does the
general-model normalization P1.
