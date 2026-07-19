# An order bound for a tight exact-seven shore

**Status:** written proof; separate internal audit GREEN in
[`hc7_tight_shore_order_bound_audit.md`](hc7_tight_shore_order_bound_audit.md).
This strengthens the shore-filling
equality branch of
[`hc7_direct_entry_two_edge_list_core.md`](../results/hc7_direct_entry_two_edge_list_core.md).
It is an unbounded host-level reduction: an all-tight open shore either has
an order-seven or order-eight singleton-side boundary, or has at most
eighteen vertices.  It does not decide the bounded residue, synchronize the
two closed-side colourings, or prove `HC_7`.

## Theorem 1 (tight-shore order bound)

Let `G` be a seven-connected graph with no `K_7` minor and suppose

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,\qquad E_G(L,R)=\varnothing,             \tag{1.1}
\]

where `L,R` are nonempty.  Let `psi` be a six-colour assignment on `S` and
put

\[
 A(v)=[6]\setminus
 \{\psi(s):s\in N_G(v)\cap S\}
 \qquad(v\in R).                                      \tag{1.2}
\]

Assume the **tightness equality**

\[
                          d_{G[R]}(v)=|A(v)|           \tag{1.3}
\]

for every `v in R`.  Then at least one of the following holds.

1. Some vertex `v in R` has degree seven or eight.  Its full neighbourhood
   is the boundary of an actual singleton-side separation of the same
   order.
2. `|R|<=18`.

Equivalently, every tight open shore of order at least nineteen exposes a
singleton-side separation of order seven or eight.

### Proof

Write `r=|R|`, `e_R=|E(G[R])|`, and
`e_{RS}=|E_G(R,S)|`.  Equation (1.2) gives `|A(v)|<=6`, so tightness gives

\[
 d_{G[R]}(v)\le6\quad(v\in R),
 \qquad e_R\le3r.                                     \tag{1.4}
\]

If some `v in R` has degree at most eight in `G`, seven-connectivity gives
`7<=d_G(v)<=8`.  Because `v` has no neighbour in the nonempty set `L`, its
full neighbourhood separates `{v}` from `L`.  This is outcome 1.

Assume therefore that every vertex of `R` has degree at least nine.  There
are no `L-R` edges, and hence

\[
 2e_R+e_{RS}=\sum_{v\in R}d_G(v)\ge9r.                \tag{1.5}
\]

Choose a component `D` of `G[L]`.  Its neighbourhood is contained in `S`.
Seven-connectivity and `|S|=7` imply `N_G(D)=S`: omitting even one boundary
vertex would give a separator of order at most six.  Contract `D` to one
vertex `ell`, delete the other vertices of `L`, and retain all vertices in
`S union R`.  The resulting simple minor `H` has `r+8` vertices and contains
all `R`-edges, all `R-S` edges, and the seven distinct edges from `ell` to
`S`.  Thus, by (1.4)--(1.5),

\[
\begin{aligned}
 |E(H)|
   &\ge e_R+e_{RS}+7\\
   &\ge 9r-e_R+7\\
   &\ge 6r+7.                                         \tag{1.6}
\end{aligned}
\]

Mader's exact extremal bound for `K_7` minors applies to the minor `H`:

\[
 |E(H)|\le5|V(H)|-15=5r+25.                           \tag{1.7}
\]

Combining (1.6) and (1.7) gives `r<=18`, which is outcome 2. \(\square\)

## Corollary 2 (the all-tight direct-entry endpoint is finite)

In the shore-filling branch of the direct-entry two-edge list-core theorem,
if equality holds in the list-degree inequality at every shore vertex, then
the branch yields an order-seven or order-eight singleton-side separation,
or the connected list-critical shore has at most eighteen vertices.

No assumption on the number of colours used on `S`, no Gallai-tree
classification, and no finite enumeration are needed for this conclusion.

## Trust boundary and external input

The proof uses W. Mader, *Homomorphiesätze für Graphen*, Math. Ann. **178**
(1968), 154--168: for `p<=7`, a simple `K_p`-minor-free graph on `N`
vertices has at most `(p-2)N-binom(p-1,2)` edges.  For `p=7` this is
`5N-15`.

The theorem does not distinguish the order-seven and order-eight exits and
does not provide compatible boundary colourings.  The bounded alternative
`|R|<=18` is a theorem-level reduction, not a claim that an unaudited finite
search settles the residue.
