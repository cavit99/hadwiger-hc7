# Bipartite thin-shore cutvertex exchange

## Status and scope

**Status:** proved and independently audited.

This is a proved structural lemma for an actual order-seven adhesion with
thin-shore packet number one and at least two rich-shore packets.  In the
current `HC_7` residue it applies in particular to the exact vector `(1,2)`.
It closes every cutvertex configuration in the nonempty bipartite-boundary
branch except one precisely described crossed-defect cell.  The result is
label-free and uses the audited exact two-carrier state criterion.  It does
not close the remaining two-lobe cell or all bipartite boundaries.

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

with no `LR` edge.  Assume `G` is strongly seven-contraction-critical:
`chi(G)=7` and every proper minor is six-colourable.  Assume also that `G`
is seven-connected, `L` has packet number one, and `R` contains two
disjoint `S`-full packets.  Put `H=G[S]`.  Suppose `H` is bipartite and
nonempty, and fix a bipartition

\[
                         S=I\mathbin{\dot\cup}J            \tag{0.1}
\]

with both classes nontrivial.

## Theorem 1 (cutvertex dichotomy)

If `z` is a cutvertex of `G[L]`, then one of the following holds.

1. `L` contains disjoint connected `I`- and `J`-carriers.  Consequently the
   exact state `I|J` is funded on the thin shore and the two rich packets
   reflect it, so `G` is six-colourable.
2. `L-z` has exactly two components `C_a,C_b`, for distinct vertices
   `a,b` in the same class of (0.1), such that

   \[
   N_S(C_a)=S-\{a\},\qquad N_S(C_b)=S-\{b\},
   \qquad za,zb\notin E(G).                               \tag{1.1}
   \]

Moreover outcome 2 can persist over the freedom to choose a bipartition of
`H` only if `a,b` lie in one connected component of `H` and have even
distance there.

### Proof

First, `L` is connected.  Indeed, for every component `C` of `G[L]`,
`N_G(C)\subseteq S`; since the opposite shore is nonempty,
seven-connectivity gives `N_G(C)=S`.  Thus every component of `G[L]` is an
`S`-full packet, and packet number one permits only one component.

Let `C_1,...,C_k` be the components of `L-z`.  Each is adjacent to `z`
because `L` is connected.  Since

\[
                         N_G(C_i)\subseteq S\cup\{z\},
\]

and deleting `N_G(C_i)` separates the nonempty set `C_i` from the nonempty
opposite shore, seven-connectivity gives

\[
                   |N_S(C_i)|\ge6.                         \tag{1.2}
\]

Write `D_i=S-N_S(C_i)`, so `|D_i|<=1`.

For any index `j`, the set

\[
 X_j=\{z\}\cup\bigcup_{i\ne j}C_i
\]

is connected and adjacent to the connected set `C_j`.  Its defect is

\[
 S-N_S(X_j)
   =\bigl(S-N_S(z)\bigr)\cap\bigcap_{i\ne j}D_i.           \tag{1.3}
\]

If `k>=3`, some `X_j` is `S`-full.  Otherwise, for every `j`, all defects
with index different from `j` would be the same nonempty singleton missed
also by `z`.  Comparing two choices of `j` (possible because `k>=3`) shows
that every `D_i` is that same singleton and `z` misses it.  Then all of `L`
misses one boundary vertex, contradicting that its packet number is one.

Choose `j` with `X_j` full.  The component `C_j`, having defect at most one,
contacts at least one whole class of (0.1).  Assign it to such a class and
assign the full carrier `X_j` to the other.  The carriers are adjacent, so
the audited two-carrier criterion funds `I|J`.

It remains that `k=2`.  Put `D_i=\varnothing` when `C_i` is full.  A
component whose defect is empty is a carrier for either class.  If the two
singleton defects lie in opposite bipartition classes, `C_1,C_2` themselves
contact the opposite prescribed classes; adding `z` to either one makes the
two carriers adjacent.  If `z` contacts the defect of `C_i`, then
`C_i\cup\{z\}` is full and the other component contacts one whole class, so
the same assignment works.

Thus failure requires nonempty defects `D_1={a}`, `D_2={b}` in one
bipartition class and `z` adjacent to neither `a` nor `b`.  Fullness of `L`
forces `a!=b`; this is (1.1).  Conversely the displayed contact data are
exactly the case not decided by this carrier argument.

Finally, bipartitions of distinct connected components of `H` may be flipped
independently.  Within one connected bipartite component, two vertices lie
in opposite classes exactly when their distance is odd.  Hence defects in
different components, or at odd distance in one component, can be put in
opposite classes and outcome 1 applies.  This proves the last assertion.
\(\square\)

## Corollary 2 (Dirac refinement of the crossed cell)

In outcome 2, name the class containing `a,b` as `I`, put `p=|I|`, and put

\[
 r=d_L(z),\qquad Z=N_S(z).
\]

Then `2<=p<=6`,

\[
       r+|Z\cap J|\ge5,\qquad r+|Z\cap I|\ge5,             \tag{2.1}
\]

and

\[
                     r\ge \max\{7-p,p-2\}\ge3.             \tag{2.2}
\]

Thus one of the two lobes contains at least two distinct neighbours of
`z`.

### Proof

Each class of (0.1) is independent.  Therefore

\[
 \alpha(G[N(z)])\ge |Z\cap I|,
 \qquad
 \alpha(G[N(z)])\ge |Z\cap J|.
\]

Dirac's inequality at parameter seven says

\[
                    \alpha(G[N(z)])\le d_G(z)-5=r+|Z|-5.
\]

Using first `I` and then `J` gives (2.1).  Both bipartition classes are
nonempty and `I` contains the two distinct defects, so `2<=p<=6`.  Since
`z` misses `a,b`,

\[
        |Z\cap I|\le p-2,\qquad |Z\cap J|\le 7-p.
\]

The two inequalities in (2.1) now give `r>=p-2` and `r>=7-p`,
respectively.  Their maximum is at least three for every integer
`2<=p<=6`, proving (2.2).  The pigeonhole conclusion follows because
`L-z` has two components. \(\square\)

## Exact remaining sub-gap

Only the following cutvertex geometry is not closed by the theorem:

* two lobes;
* distinct defects `a,b` in the same connected boundary component at even
  parity;
* `z` misses both defects and has at least three lobe neighbours.

This is a genuine crossed-frame state problem.  The separate verified
barrier
`../barriers/hc7_exact7_bipartite_carrier_connectivity_dirac_barrier.md`
shows that seven-connectivity and the static Dirac inequalities cannot by
themselves eliminate all such carrier failures.  A completion must use
proper-minor state transitions or `K_7`-minor-freeness.
