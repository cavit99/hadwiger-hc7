# Cross-part Hall completion for pair-mode boundaries

## Status

This note extracts the parameter-uniform rooted-model theorem behind the
order-four strict packet closure.  It is a direct branch-set theorem; no
colour criticality, planarity, or finite boundary enumeration is used.

## 1. The completion theorem

Let

\[
 k=2q+1,\qquad
 S=B_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}B_q
       \mathbin{\dot\cup}\{s\},\qquad |B_i|=2,
 \tag{1.1}
\]

where `G[S]` is the complete multipartite graph with parts
`B_1,...,B_q,{s}`.  Thus the only missing edges of `G[S]` are the `q`
pair edges inside the `B_i`.

### Theorem 1.1 (cross-part Hall completion)

Suppose `G-S` contains a connected set `R` adjacent to every vertex of
`S`, and suppose, disjointly from `R union S`, it contains

\[
                         U_1,\ldots,U_{k-3}                 \tag{1.2}
\]

which are nonempty connected and pairwise adjacent.  For each `i`, put

\[
                         P_i=N_S(U_i)\cap(S-\{s\}).          \tag{1.3}
\]

Assume:

1. the family `(P_i)` satisfies Hall's condition; and
2. for every pair part `B_j`, at least one member of `B_j` belongs to
   `union_i P_i`.

Then `G` contains a `K_k` minor.

#### Proof

Hall's theorem gives distinct representatives

\[
                         t_i\in P_i\qquad(1\le i\le k-3).   \tag{1.4}
\]

Exactly two vertices `u,v` of `S-{s}` are not used.  If they belong to
different pair parts, retain this matching.  Otherwise
`{u,v}=B_j`.  By hypothesis 2, one of them, say `u`, belongs to some
`P_h`.  Replace `t_h` by `u`, and put `w` equal to the old representative
`t_h`.  The newly unmatched vertices are `v` and `w`; the latter is not
in `B_j`, because neither member of `B_j` was used by the old matching.
Rename this new unmatched pair as `u,v`.  After this one exchange the two
unmatched vertices therefore belong to different parts and hence

\[
                               uv\in E(G[S]).                  \tag{1.5}
\]

Use the following `k` branch sets:

\[
 U_i\cup\{t_i\}\quad(1\le i\le k-3),\qquad
 R,\qquad \{s\},\qquad \{u,v\}.                              \tag{1.6}
\]

They are pairwise disjoint and connected.  The first `k-3` bags are
pairwise adjacent through the `U_i`.  Each sees `R` through its distinct
boundary root, sees `{s}` through the boundary edge `t_i s`, and sees
`{u,v}` because at least one of `u,v` lies in a different pair part from
`t_i`.  Fullness makes `R` adjacent to the last two boundary bags, and
`s` is adjacent to both `u,v`.  Hence all bags in (1.6) are pairwise
adjacent and form a `K_k` model.  \(\square\)

### Theorem 1.2 (dominating-edge complement completion)

The same construction has the following boundary-independent form.  Let
`|S|=k`, let `s in S`, and suppose `s` is adjacent to every vertex of
`T=S-{s}`.  Let `R` and `U_1,...,U_{k-3}` satisfy the disjointness,
connectivity, pairwise-adjacency, and fullness hypotheses of Theorem 1.1.
If the portal rows `P_i=N_S(U_i) cap T` have distinct representatives
`t_i` whose two omitted roots `u,v` satisfy

\[
 uv\in E(G[S])
 \quad\hbox{and}\quad
 N_{G[S]}(\{u,v\})\supseteq\{t_1,\ldots,t_{k-3}\},              \tag{1.7}
\]

then `G` contains a `K_k` minor.

Indeed, the bags in (1.6) work verbatim.  Condition (1.7) is exactly the
adjacency needed between every matched carrier bag and the final two-root
bag; no multipartite structure is otherwise used.  Thus the selection
problem is a transversal-matroid problem with a dominating-edge
complement.

For the `C_6 dotcup K_1` boundary at `k=7`, every antipodal pair of the
missing six-cycle is a dominating edge in this sense.  Consequently four
pairwise-adjacent pieces with a portal transversal onto the other four
cycle roots, together with the opposite full shore and the universal
root, force `K_7`.

The distinction from the earlier rooted Hall completion is useful.  No
common `s`-portal is required on the pieces: their matched roots see `s`
inside the complete multipartite boundary.  The price is the exact
pair-mode boundary and collective contact with every pair part.

## 2. Strict clique-shore consequence

For `X subseteq D`, write

\[
 \partial_S(X)=(N_D(X)-X)\mathbin{\dot\cup}N_S(X).             \tag{2.1}
\]

### Corollary 2.1 (strict clique shore)

In the setting of (1.1), suppose `D` is a clique of order

\[
                              |D|=k-3=2q-2,                    \tag{2.2}
\]

disjoint from `R union S`, satisfies `N_{S-{s}}(D)=S-{s}`, and satisfies

\[
              |\partial_S(X)|\ge k-2
       \quad(\varnothing\ne X\subsetneq D).                  \tag{2.3}
\]

Then `G` contains a `K_k` minor.

#### Proof

Use the singleton pieces `U_x={x}` for `x in D`.  They are connected
and pairwise adjacent.  Put `T=S-{s}`.  For a nonempty proper
`X subsetneq D`, cliquehood and (2.3) give

\[
\begin{aligned}
 |N_T(X)|
 &\ge |N_S(X)|-1\\
 &\ge (k-2)-|D-X|-1\\
 &=|X|.
\end{aligned}                                                 \tag{2.4}
\]

For `X=D`, the collective hypothesis gives `N_T(D)=T`, of order
`k-1>|D|`.  Thus the portal rows into `T` satisfy Hall's condition.  It
also gives the pair-part contact required in Theorem 1.1, which supplies the
`K_k` minor.  \(\square\)

For `q=3`, this is the order-four `HC_7` packet closure.  The proof works
unchanged for every `q>=2`; its substantive hypothesis is the strict
relative boundary, which is exactly what a globally minimum fragment
has after all nested minimum-cut descents have been excluded.
