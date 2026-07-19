# Density closure for the join-type surplus obstruction

**Status:** written proof; audit pending.  This is a host-level closure of
the infinite family exhibited in
[`hc7_two_edge_list_surplus_control_barrier.md`](hc7_two_edge_list_surplus_control_barrier.md).
It shows that `K_7`-minor exclusion converts that unbounded list-critical
family into either an exact order-seven separation or a bounded residue.
It does not classify arbitrary positive-surplus list-critical shores and
does not prove `HC_7`.

## Theorem 1 (large `K_2`-odd-cycle joins force a terminal outcome)

Let `G` be a seven-connected graph and suppose

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,\qquad E_G(L,R)=\varnothing,             \tag{1.1}
\]

where `L,R` are nonempty.  Suppose

\[
                         G[R]\cong K_2\vee C_N,         \tag{1.2}
\]

where `N>=5` is odd.  Then one of the following holds.

1. `G` contains a `K_7` minor;
2. some cycle vertex `v` has `d_G(v)=7`, so `N_G(v)` is the boundary of an
   actual order-seven separation with singleton open side `{v}`; or
3. `N<=13`.

More precisely, if `s=|E(G[S])|` and neither outcome 1 nor outcome 2
holds, then

\[
                         2N+s\le27.                    \tag{1.3}
\]

Consequently every such shore with `N>=15` gives outcome 1 or outcome 2.
If `G[S]` is four-chromatic, or merely has at least six edges, then the
bounded residue improves to `N<=9`.

### Proof

Let `a,b` be the two vertices of the `K_2` in (1.2).  Every cycle vertex
has four neighbours in `R`: its two cycle neighbours and `a,b`.  Seven-
connectivity therefore gives it at least three neighbours in `S`.  If some
cycle vertex has exactly three boundary neighbours, its total degree is
seven.  Since the nonempty set `L` is anticomplete to it, its full
neighbourhood separates the singleton from `L`, giving outcome 2.

Assume that outcome 2 does not occur.  Every cycle vertex then has at least
four neighbours in `S`.

Choose a component `D` of `G[L]`.  Its neighbourhood is contained in `S`.
If it missed one boundary vertex, its neighbourhood would have order at
most six and would separate `D` from the nonempty set `R`, contrary to
seven-connectivity.  Hence `N_G(D)=S`.

Contract `D` to one vertex `ell`, delete the other vertices of `L`, and
retain `S union R`.  The resulting simple minor `H` has

\[
                         |V(H)|=N+10.                  \tag{1.4}
\]

The graph `K_2\vee C_N` has `3N+1` edges.  There are at least `4N` edges
from its cycle vertices to `S`, the contracted vertex has seven edges to
`S`, and the boundary contributes `s` edges.  Thus

\[
                         |E(H)|\ge7N+8+s.              \tag{1.5}
\]

If outcome 1 does not hold, `H` is `K_7`-minor-free.  Mader's sharp bound
for `K_7` minors gives

\[
 |E(H)|\le5|V(H)|-15=5N+35.                          \tag{1.6}
\]

Combining (1.5) and (1.6) yields (1.3).  In particular `N<=13`; since `N`
is odd, no value `N>=15` survives.

For the final assertion, a four-chromatic graph contains a four-critical
subgraph.  Such a subgraph has minimum degree at least three and therefore
at least six edges.  Substituting `s>=6` in (1.3) gives `2N<=21`, so the
odd integer `N` is at most nine.  \(\square\)

## Corollary 2 (bounded surplus in the uniform four-list realization)

In the uniform-list realization from the barrier note, the only
positive-surplus vertices are the two vertices `a,b` of the `K_2`, and

\[
 \varepsilon(a)=\varepsilon(b)=N-3.
\]

Under the additional hypotheses that the host is seven-connected,
`K_7`-minor-free, and has no singleton-side order-seven separation at a
cycle vertex, Theorem 1 gives

\[
                 \varepsilon(a)+\varepsilon(b)=2N-6\le20. \tag{2.1}
\]

Thus the unbounded list-theoretic obstruction cannot persist inside the
hypothetical host.  The surviving join residues have cycle orders
`5,7,9,11,13` (and only `5,7,9` when the boundary is four-chromatic or has
at least six edges).

## Trust boundary

The proof uses exactly the two global hypotheses absent from the abstract
list-critical example: seven-connectivity makes an opposite component
adjacent to the whole seven-boundary and supplies the singleton separator,
while `K_7`-minor exclusion activates the sharp density bound.  It does not
use a selected near-complete minor model or any palette-to-label
identification.

The conclusion is an unbounded-family closure, not a general surplus
theorem.  An arbitrary positive-surplus list-critical shore need not
contain a spanning `K_2\vee C_N`, and the bounded residues above still
require either a label-preserving first-hit argument or compatible
colourings at the returned exact boundary.

The external extremal input is Mader's theorem for `p<=7`: a simple
`K_p`-minor-free graph on `m>=p` vertices has at most
`(p-2)m-binom(p-1,2)` edges.  Here `p=7` and `m=N+10`.
