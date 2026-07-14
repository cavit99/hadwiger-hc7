# Adaptive clique-reservoir carrier return

**Status:** proved and independently audited.

## 1. Uniform exact return theorem

Let `k>=2`, and let `G` be strongly `k`-contraction-critical:

\[
 \chi(G)=k,
 \qquad\text{and every proper minor of }G\text{ is }(k-1)\text{-colourable}.
\]

Let

\[
             V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
\]

where `S,L,R` are nonempty and there is no `LR` edge.  Fix
`1<=q<=k-1`, and
assume that `R` contains `q` pairwise vertex-disjoint connected `S`-full
packets.

### Theorem 1.1 (adaptive clique-reservoir return)

Suppose there are pairwise disjoint, connected, pairwise adjacent sets

\[
                         C_1,\ldots,C_q\subseteq L
\]

and a partition

\[
                         S=I_1\mathbin{\dot\cup}\cdots
                              \mathbin{\dot\cup}I_q
                              \mathbin{\dot\cup}U             \tag{1.1}
\]

such that

1. every `I_i` is a nonempty independent set;
2. `U` is a clique (possibly empty); and
3. every literal vertex of `I_i` has a neighbour in `C_i`.

Then `G` is `(k-1)`-colourable.

No carrier is required to contact `U`.  The proper-minor colouring chooses
which, if any, member of the clique reservoir joins each seed block.  The
exact state which is actually returned has packet demand at most `q`,
irrespective of those choices.

#### Proof

Contract spanning trees of the pairwise disjoint connected sets

\[
                         A_i=C_i\cup I_i
                         \qquad(1\le i\le q)               \tag{1.2}
\]

to vertices `a_i`.  The sets in (1.2) are connected by item 3, and their
representatives form a clique because the `C_i` are pairwise adjacent.
The minor is proper because every `I_i` is nonempty and a literal
carrier--boundary edge is contracted.

Take a `(k-1)`-colouring of this proper minor and restrict it to the
untouched closed `R`-shore, expanding the colour of `a_i` over `I_i`.  This
gives a proper colouring of `G[R union S]`.  Let `Pi` be its exact equality
partition on `S`, and let `B_i` be the block containing `I_i`.  Since the
representatives form a clique, the `B_i` are pairwise distinct.

Every other boundary vertex belongs to the clique `U`.  Consequently at
most one member of `U` can join each `B_i`, and all members of
`U-\bigcup_iB_i` are singleton blocks of `Pi`.  Put

\[
                    r=\left|U-\bigcup_{i=1}^qB_i\right|.
\]

Those `r` singleton blocks induce a clique, and there are no other blocks
apart from `B_1,\ldots,B_q` and these singleton blocks.  Therefore

\[
                 |\Pi|=q+r,
   \qquad
                 \omega\bigl(G[S][\operatorname{sing}(\Pi)]\bigr)\ge r,
\]

where the second inequality is also valid for `r=0`.  Hence

\[
                              d_{G[S]}(\Pi)\le q.         \tag{1.3}
\]

Choose a maximum clique `K` in the singleton-block graph of `Pi`.  The
number of blocks outside `K` is exactly `d_{G[S]}(Pi)<=q`.  Assign a
different full packet to every such block `B` and contract the connected
set `P_B union B`.  The resulting representatives, together with the
retained literal singleton vertices in `K`, form a clique: packet fullness
supplies every packet--packet and packet--singleton adjacency, while `K`
is a literal clique.  A `(k-1)`-colouring of this proper minor, restricted
to `L union S` and expanded over the contracted blocks, therefore induces
exactly `Pi` on `S`.

If there is no block outside `K`, then `S` itself is a clique of singleton
blocks.  Delete the nonempty open shore `R` instead; a `(k-1)`-colouring of
that proper minor still induces exactly `Pi` on `S`.

The first minor returned the same exact partition on `G[R union S]`.
Align its block colours with those of the second colouring by a permutation
of the `(k-1)`-colour palette and glue across literal `S`.  There is no
`LR` edge, so this is a proper `(k-1)`-colouring of `G`.  \(\square\)

### Corollary 1.2 (exact-seven two-carrier form)

At `(k,q)=(7,2)`, it is enough to find disjoint adjacent connected
carriers `X,Y` and a partition

\[
                         S=I\dot\cup J\dot\cup U
\]

in which `I,J` are nonempty independent seeds contacted respectively by
`X,Y`, and `U` is a clique.  The graph is then six-colourable.  Neither
carrier needs to contact the clique reservoir.

## 2. Application to the two-lobe capacity residue

Retain the two-lobe setup of the support-four capacity transition.  Thus
`L-T` has lobes `D,E`, every lobe meets every member of the three-gate `T`,
and the old opposite shore contains two disjoint full packets.

Partition the three gate vertices arbitrarily between the two lobes and put

\[
 X=D\cup T_D,\qquad Y=E\cup(T-T_D).                       \tag{2.1}
\]

The sets in (2.1) are disjoint, connected and adjacent.  Theorem 1.1 gives
the following expansion-sensitive allocation criterion.

### Corollary 2.1

The lobe-centred-star or capacity-triangle residue closes whenever, for
some gate allocation (2.1), there is a clique `U subseteq S` such that the
graph `G[S]-U` has a bipartition `I dotunion J` with

\[
             \varnothing\ne I\subseteq N_S(X),
             \qquad
             \varnothing\ne J\subseteq N_S(Y),          \tag{2.2}
\]

after possibly interchanging `I,J`.

This conclusion uses a legal proper-minor response: it does not assert that
the prescribed state `I|J|U` is returned.  Instead the actual returned
blocks may absorb vertices of `U`; the unabsorbed vertices remain a clique
of singleton blocks, which is exactly why (1.3) survives.

In particular, the old requirement that both carrier representatives be
adjacent to every retained singleton is unnecessary in this cell.

## 3. First implication that does not follow

The support normal forms alone do not force (2.2).  Here is a concrete
support-only obstruction, stated without a boundary census.

Let

\[
 A=\{z,a_1,a_2,a_3\},\qquad
 C=\{z,b_1,b_2,b_3\},\qquad A\cap C=\{z\},              \tag{3.1}
\]

and let the boundary graph be the tree with edges

\[
 za_2, a_2a_3, a_3a_1,
 \qquad
 zb_1, b_1b_2, zb_3.                                  \tag{3.2}
\]

Take the three paired blocks to be

\[
               \{a_1,b_1\},\quad\{a_2,b_2\},
               \quad\{a_3,b_3\},                       \tag{3.3}
\]

with distinguished singleton `z`.  The pairs in (3.3) are independent;
`z` has a neighbour in every pair; and every two pairs have a literal edge
between them.  Thus (3.2) is a valid paired width-two boundary.  The two
four-sets in (3.1) have union `S`, exactly as in a lobe-centred star; gate
supports may be contained in `C` without adding any new contact.

There is nevertheless no clique `U` and no partition

\[
                    S-U=I\mathbin{\dot\cup}J,
       \qquad I\subseteq A,\quad J\subseteq C,           \tag{3.4}
\]

with nonempty independent `I,J`.  Indeed, unless `a_3 in U`, the two
edges `a_3a_1,a_3a_2` force the nonadjacent vertices `a_1,a_2` into `U`.
Hence `a_3 in U`.  The edge `b_1b_2` then forces one of `b_1,b_2` into
`U`, but neither is adjacent to `a_3`; this contradicts that `U` is a
clique.

This graph is only a boundary/support certificate, not an `HC_7`
counterexample.  It identifies the first unsupported implication exactly:

> the lobe-centred star/triangle support description does not by itself
> produce a clique-reservoir carrier allocation.

To close the remaining residue one must use internal lobe expansion,
`K_7`-minor-freeness, or another legal proper-minor transition to create
(2.2), or else turn its failure into a strict actual adhesion or fixed-pair
handoff.  Theorem 1.1 completes the state-selection step once that geometric
allocation is present.
