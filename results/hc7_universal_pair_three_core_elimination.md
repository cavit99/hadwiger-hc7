# A universal boundary pair and three small models force `K_7`

**Status:** proved and independently audited GREEN.

This is the model-preserving terminal for the sole five-chromatic
order-nine boundary left by `hc7_two_full_shore_boundary_absorption.md`.
It is stated without cycle labels and uses only the universal pair.

## Theorem 1 (universal-pair core fan)

Let `G` be seven-connected.  Let

\[
                        V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}B
\]

where `A,B` are nonempty connected sets with no edge between them, and
every vertex of `S` has a neighbour in each of `A,B`.  Suppose that

1. `|S|>=6`;
2. `p,q in S` are adjacent and each is adjacent to every vertex of
   `S-{p,q}`; and
3. `G` contains three pairwise vertex-disjoint `K_5` models, each having
   four singleton branch bags (and an arbitrary fifth branch bag).

Then `G` contains a `K_7` minor.

### Proof

The pair `{p,q}` meets at most two of the three disjoint model supports.
Choose a model whose support avoids both vertices, and let `Q` be the
literal four-clique formed by its singleton branch bags.  Put

\[
                R=Q\cap S,\qquad K=Q-S,\qquad r=|K|=4-|R|.
\]

Because `Q` is a clique and there are no `A-B` edges, all vertices of `K`
lie in one of `A,B` when `K` is nonempty; call that component-side `C` and
call the other one `D`.  If `K` is empty, choose either open side as `D`.

Assume first that `r>0`.  Apply the forbidden-set form of Menger's theorem
in `G` with

\[
 \mathcal A=K,\qquad
 \mathcal B=S-(R\cup\{p,q\}),\qquad
 D_0=R\cup\{p,q\}.
\]

The three sets are pairwise disjoint.  Moreover

\[
              r+|D_0|=(4-|R|)+(|R|+2)=6\le7,
\]

and

\[
              |\mathcal B|=|S|-|R|-2\ge4-|R|=r.
\]

Hence there are `r` disjoint paths from the vertices of `K` to distinct
vertices of `mathcal B`, avoiding `D_0`.  Truncate every path at its first
vertex of `S`.  Before that first hit it lies in `C`, because `C` is a
component of `G-S`.  Denote the truncated path starting at `x in K` by
`P_x`.

Use the following four bags:

\[
                  V(P_x)\quad(x\in K),
                  \qquad \{x\}\quad(x\in R).          \tag{1.1}
\]

They are disjoint and pairwise adjacent, since each contains a different
named vertex of the clique `Q`.  Each contains a distinct vertex of `S`,
and none contains `p` or `q`.  When `r=0`, take the four singleton bags
`{x}` for `x in Q`; they have exactly the same properties.

Complete (1.1) by the three bags

\[
                              \{p\},\qquad\{q\},\qquad D. \tag{1.2}
\]

The first two are adjacent.  Since `p,q` are complete to the rest of `S`,
each is adjacent to every bag in (1.1) through that bag's boundary vertex.
Fullness of `D` makes it adjacent to every bag in (1.1) and to each of
`{p},{q}`.  It is connected and disjoint from (1.1).  Thus the seven sets
in (1.1)--(1.2) are pairwise disjoint, connected and pairwise adjacent;
they are a literal `K_7` model.  \(\square\)

## Corollary 2 (the excess-nine cyclic exception is impossible)

In the `m=3` two-component residue of
`hc7_three_split_minimal_bad_contraction.md`, the three named support-six
models are pairwise disjoint and each has a literal singleton `K_4` core.
If the expanded nine-vertex boundary were `K_2 vee C_7`, the `K_2` is an
adjacent pair complete to the rest of the boundary.  Theorem 1 would give
`K_7`, a contradiction.

Combining this with the audited boundary-absorption theorem proves:

> In every `K_7`-free exact two-component residue produced by a minimal
> bad contraction of two or three disjoint normalized support-six models,
> the expanded boundary is four-colourable.

The remaining obstruction is therefore purely a state/model transfer
across a four-colourable boundary.  No five-chromatic boundary geometry
survives.

## Trust boundary

The theorem needs three **vertex-disjoint** model supports so that one
literal four-clique avoids both universal vertices.  It does not claim
that the universal pair is a global transversal.  The fifth branch bag of
the selected model is unused.
