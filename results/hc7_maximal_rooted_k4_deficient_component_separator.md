# A deficient branch set in a contact-maximal rooted `K_4` model determines a separating component

**Status:** written proof; separate internal audit GREEN.  This is a
conditional structural lemma in the lifted star-Kempe setup.  It does not
prove `HC_7`, and it does not provide an upper bound on the separator order.

## 1. Setup

Let `G` be a seven-connected graph with a vertex partition

\[
                         V(G)=X\mathbin{\dot\cup}V(Q),
\]

where `X` is connected and dominates `Q`.  Let `z,u` be adjacent vertices
of `Q`, put

\[
                         R=Q-\{z,u\},
\]

and write

\[
                  S=N_R(z),\qquad T=N_R(u).
\]

For a vertex set `Y`, write \(N_X(Y)=N_G(Y)\cap X\).

In the star-Kempe application, `X` is the connected induced bipartite
subgraph supplied by the compression theorem, `R` is four-chromatic, and
both `S,T` are colourful in `R`.

Let

\[
                         (D_1,D_2,D_3,D_4)             \tag{1.1}
\]

be an `S`-rooted `K_4`-minor model in `R`: the `D_i` are pairwise disjoint
connected subgraphs, are pairwise adjacent, and each meets `S`.  Choose
(1.1) to maximize

\[
             \tau(D_1,D_2,D_3,D_4)
                =|\{i:D_i\cap T\ne\varnothing\}|.     \tag{1.2}
\]

## 2. Deficient-component separator lemma

### Theorem 2.1

Suppose \(D_j\cap T=\varnothing\).  Put

\[
              U_j=\bigcup_{i\ne j}D_i,
\]

and let `C_j` be the component of `R-U_j` containing `D_j`.  Then:

1. \(C_j\cap T=\varnothing\);
2. \(N_R(C_j)\subseteq U_j\); and
3. the full neighbourhood of `C_j` in `G` is the disjoint union

   \[
       N_G(C_j)=N_R(C_j)\mathbin{\dot\cup}N_X(C_j)
                    \mathbin{\dot\cup}\{z\}.          \tag{2.1}
   \]

Consequently, `N_G(C_j)` is a separator with nonempty open sides, one
containing `C_j` and the other containing `u`.  In particular,

\[
          |N_R(C_j)|+|N_X(C_j)|+1\ge 7.               \tag{2.2}
\]

Equality in (2.2) gives an actual separation of order seven.  The theorem
does not assert equality or any other upper bound.

### Proof

Suppose first that `C_j` contains a vertex \(t\in T\).  Since `C_j` is
connected and contains the connected subgraph `D_j`, there is a path in
`C_j` from `D_j` to `t`.  Add the vertices of such a path to `D_j`.  The
enlarged branch set remains connected and is disjoint from every `D_i`
with \(i\ne j\), because `C_j` is a component of `R-U_j`.  It retains all
previous adjacencies to the other three branch sets and still meets `S`.
It now also meets `T`, while the other branch sets are unchanged.  This
strictly increases (1.2), contrary to its maximality.  Hence

\[
                              C_j\cap T=\varnothing.   \tag{2.3}
\]

The definition of `C_j` immediately gives

\[
                              N_R(C_j)\subseteq U_j.  \tag{2.4}
\]

The vertex partition of `G` shows that every neighbour of `C_j` outside
`R` belongs to `X` or to `\{z,u\}`.  Equation (2.3) and the identity
`T=N_R(u)` show that `u` has no neighbour in `C_j`.  On the other hand,
`D_j` meets `S=N_R(z)`, so `z` has a neighbour in
\(D_j\subseteq C_j\).
This proves (2.1).

Let

\[
       A=C_j\cup N_G(C_j),\qquad B=V(G)-C_j.
\]

Then `(A,B)` is a separation with separator `N_G(C_j)`.  Its first open
side contains `C_j`.  Its second open side contains `u`, which belongs to
neither `C_j` nor `N_G(C_j)` by (2.3).  Seven-connectivity now gives
\(|N_G(C_j)|\ge 7\); substituting (2.1) proves (2.2).  If equality holds, the
displayed separation has order seven and both open sides are nonempty.
\(\square\)

## 3. What the proper-minor colouring response records

Assume now the full star-Kempe host hypotheses: every proper minor of `G`
is six-colourable.  Contract `X` to `x` and every `D_i` to `d_i`, delete
the vertices of `R` outside the four branch sets, and retain `z,u`.  The
two colour classes forming `X` are nonempty, so the contraction of `X` is
nontrivial and the resulting minor is proper.  The
six vertices

\[
                         x,z,d_1,d_2,d_3,d_4           \tag{3.1}
\]

form a `K_6`.  The vertex `u` is adjacent to `x,z`, and it is adjacent to
`d_i` exactly when `D_i` meets `T`.  Therefore, in every proper
six-colouring of this minor, the vertices in (3.1) receive six distinct
colours and `u` repeats the colour of a `T`-deficient branch set.

This colour repetition is an exact description of the missing adjacency,
but it does not bound the separator in (2.1).  The contractions identify
all vertices of \(N_R(C_j)\cap D_i\) with the single label `d_i` and all
vertices of `N_X(C_j)` with `x`.  Thus the quotient records at most the
three other branch-set labels, the label `x`, and `z`; it does not record
the number of actual boundary vertices represented by those labels.
Seven-connectivity supplies the lower bound (2.2), not the upper bound
needed to force equality.
