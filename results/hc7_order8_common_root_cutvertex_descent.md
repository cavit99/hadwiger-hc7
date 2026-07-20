# A common root at a shore cutvertex gives a three-subgraph reflection or an exact-seven descent

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_common_root_cutvertex_descent_audit.md`](hc7_order8_common_root_cutvertex_descent_audit.md).
This is a conditional unbounded reduction inside the order-eight
opposite-response interface.  It does not prove `HC_7`.

## 1. Setting

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
 \qquad |S|=8,
 \qquad L,R\ne\varnothing,                            \tag{1.1}
\]

where `R` is connected.  Assume that `G` is seven-connected,
`K_7`-minor-free, is not six-colourable, and every proper minor of `G` is
six-colourable.  Let `d,e`
be distinct nonadjacent vertices of `G[S]`, and let

\[
                 S-\{d,e\}=X\mathbin{\dot\cup}Y       \tag{1.2}
\]

be a bipartition into two nonempty sets.  Assume the boundary conditions
of the root-connector reflection theorem: there is an `X`--`Y` edge and
each of `d,e` has a neighbour in both `X,Y`.

Suppose that `R` contains two disjoint connected subgraphs `Q_0,Q_1`, each
adjacent to every literal vertex of `S`.  Let `q in Q_i` be adjacent to
both `d,e`, and put `j=1-i`.

For a connected subgraph `C` disjoint from `S`, say that `C` **supports**
`Z subseteq S` when every vertex of `Z` has a neighbour in `C`.

## 2. Cutvertex dichotomy

### Theorem 2.1

At least one of the following holds.

1. The graph `R-q` is connected.
2. The open shore `R` contains three pairwise disjoint nonempty connected
   subgraphs `D,C_X,C_Y`, where `D` has neighbours at both `d,e`, `C_X`
   supports `X`, and `C_Y` supports `Y`.
3. There are unique vertices `x in X`, `y in Y` and a nonempty connected
   set `K subset R` such that

   \[
            N_G(K)=\{q\}\mathbin{\dot\cup}
                    (S-\{x,y\}).                     \tag{2.1}
   \]

   Thus `N_G(K)` is the boundary of an actual separation of order seven.
   Moreover `K` is a component of `R-q` not containing `Q_j`, and every
   edge `qv` with `v in K` gives a strict generic exact-seven response
   descent with selected shore `K`.

If the closed `R`-shore realizes the split-root partition

\[
                         X\mid Y\mid\{d\}\mid\{e\},  \tag{2.2}
\]

whereas the closed `L`-shore does not, outcome 2 is impossible by the
root-connector reflection theorem.  Hence every surviving common root
neighbour which is a cutvertex of the whole open shore yields outcome 3.

#### Proof

Assume that `R-q` is disconnected.  Because `Q_j` is connected and does
not contain `q`, it lies in one component `W_*` of `R-q`.  Choose any other
component `K`.

If `K` supports `X`, then

\[
                         \{q\},\qquad K,\qquad Q_j    \tag{2.3}
\]

are pairwise disjoint connected subgraphs with, respectively, both root
contacts, support for `X`, and support for `Y`.  This is outcome 2.  The
same argument with `X,Y` interchanged applies if `K` supports `Y`.

We may therefore assume that `K` supports neither class.  Choose

\[
          x\in X-N_G(K),\qquad y\in Y-N_G(K).         \tag{2.4}
\]

Since `K` is a component of `R-q` and there are no `L`--`R` edges,

\[
                         N_G(K)\subseteq \{q\}\cup S. \tag{2.5}
\]

The opposite shore `L` is nonempty, so `N_G(K)` is the boundary of a
genuine separation.  Seven-connectivity and (2.4)--(2.5) give

\[
  7\le |N_G(K)|\le 1+|S-\{x,y\}|=7.                 \tag{2.6}
\]

All inequalities are equalities.  In particular `q` is adjacent to `K`,
`K` is adjacent to every vertex of `S-\{x,y\}`, and it misses exactly the
two displayed vertices.  This proves (2.1), including uniqueness of `x,y`.

As `R` is connected, `K` has an edge `qv` to `q`.  Delete that edge and
choose a proper six-colouring of `G-qv`.  Its restriction to the closed
shore opposite `K` is proper.  Let `Pi_K` be its exact equality partition
on `N_G(K)`.  The partition `Pi_K` cannot also be induced by a proper
six-colouring of `G[K union N_G(K)]`: otherwise the two closed-shore
colourings could be aligned blockwise and glued to a proper six-colouring
of `G`.

Consequently

\[
  \bigl(K,N_G(K),V(G)-(K\cup N_G(K));\ qv,\Pi_K\bigr) \tag{2.7}
\]

is a generic exact-seven response interface.  It is strict because `K`
is a proper subset of `R`: the component `W_*` contains the nonempty
subgraph `Q_j` and is disjoint from `K`.  This proves outcome 3.  The last
paragraph follows directly from the root-connector reflection theorem.
\(\square\)

## 3. Block-cut-tree consequence

### Corollary 3.1

Under the opposite-response orientation in the last paragraph of Theorem
2.1, every cutvertex `q` of `R` which is adjacent to both roots and lies in
one of the named boundary-full subgraphs produces an actual order-seven
separation and a strict generic response descent.  Therefore, in a
survivor which admits neither such descent nor a common boundary partition,
no common-root vertex in either named boundary-full subgraph is a
cutvertex of `R`.

#### Proof

This is Theorem 2.1, applied once for each named boundary-full subgraph.
\(\square\)

## 4. Attachment count after deleting the common root and the other support

The next statement remains valid when `q` is not a cutvertex of `R`.

### Theorem 4.1

Assume outcome 2 of Theorem 2.1 does not occur.  Let `H` be a component of

\[
                         R-(\{q\}\cup V(Q_j)),        \tag{4.1}
\]

and put

\[
 A_H=N_G(H)\cap V(Q_j),
 \qquad
 \epsilon_H=
 \begin{cases}
 1,&q\in N_G(H),\\
 0,&q\notin N_G(H).
 \end{cases}                                          \tag{4.2}
\]

Then either

1. `G` has an actual separation of order seven;
2. `G` has an actual separation of order eight with connected selected
   shore `H`, and every edge from `H` to its boundary supplies a fresh
   operation-specific response on a shore strictly smaller than `R`.
   Unless outcome 1 occurs elsewhere, every component outside this new
   boundary is boundary-full and there are only two or three such
   components; or
3. one has

   \[
                          |A_H|+\epsilon_H\ge3.        \tag{4.3}
   \]

Thus, after excluding the two separator outcomes, every residual component
which is adjacent to `q` has at least two distinct attachment vertices in
`Q_j`, and every residual component not adjacent to `q` has at least three.

#### Proof

The component `H` cannot support `X`: otherwise `\{q\},H,Q_j`, in that
order, give the root connector, the `X`-support and the `Y`-support in
outcome 2.  The same argument shows that `H` cannot support `Y`.  Choose
vertices `x_H in X` and `y_H in Y` missed by `H`.

By componenthood in (4.1) and the absence of `L`--`R` edges,

\[
 N_G(H)\subseteq
 (S-\{x_H,y_H\})\cup A_H\cup
 \begin{cases}
 \{q\},&\epsilon_H=1,\\
 \varnothing,&\epsilon_H=0.
 \end{cases}                                          \tag{4.4}
\]

The full neighbourhood is the boundary of a genuine separation, because
`L` is nonempty.  If \(|A_H|+\epsilon_H\le2\), seven-connectivity and (4.4)
give

\[
                     7\le |N_G(H)|\le8.               \tag{4.5}
\]

The lower value is outcome 1 and the upper value is outcome 2.  For the
response assertion in outcome 2, choose any boundary edge `hv` with
`h in H`.  A six-colouring of `G-hv` is proper on the closed shore
opposite `H`; its exact equality partition on `N_G(H)` is rejected by the
intact `H`-shore, since otherwise the two colourings glue and six-colour
`G`.  Finally `H` is a proper subset of `R`, because the disjoint nonempty
subgraph `Q_j` lies outside it.

Put `T=N_G(H)` in the order-eight case.  Let `D` be any component of
`G-T`.  If `D` misses a vertex of `T`, its full neighbourhood has order at
most seven and is the boundary of an actual separation.  Seven-connectivity
then forces an order-seven separation, which is outcome 1.  Hence, in the
absence of outcome 1, every component of `G-T` is `T`-full.  There cannot
be four such components: the four-full-component order-eight closure would
give an explicit `K_7`-minor model or a proper six-colouring of `G`.
Therefore there are exactly two or three components.  This completes
outcome 2 and proves the theorem. \(\square\)

## 5. Exact gain and trust boundary

The theorem eliminates the entire **whole-shore cutvertex** part of the
support-entangled common-root obstruction.  It is not a finite
enumeration: the shore and all of its blocks may have arbitrary order.

The exact-seven descent preserves the fresh operation-specific response
at the edge `qv`; it does **not** preserve the old split-root partition
(2.2), the old eight boundary vertices, or inherited minor-model labels.
Nor does the theorem apply merely because `q` is a cutvertex of the chosen
subgraph `Q_i`: bypasses in `R-V(Q_i)` may join the components of `Q_i-q`.
The remaining case has `R-q` connected.  Theorem 4.1 additionally forces
every component outside `q union Q_j` to have at least two or three literal
attachments to `Q_j`, according as it is or is not adjacent to `q`.  A
completion still requires a label-preserving use of those attachments or
of contraction-critical colouring responses.

## 6. Dependencies

- seven-connectivity and proper-minor six-colourability;
- the root-connector reflection theorem for the final opposite-response
  application; and
- the four-full-component order-eight closure; and
- the elementary block-cutvertex tree.
