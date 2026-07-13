# Audit of the three-cut active-torso reduction

## Verdict

The three-cut argument in Theorem 8.3 of
`hadwiger_k7vee_constant_owner_corridor.md` is correct.  One order-four
edge case must be stated explicitly: under the convention used elsewhere
in the project, `K_4` is not called four-connected.  That case closes
directly and does not survive as a residue.

## 1. The three-cut count

Let

\[
                         V(G)=L\mathbin{\dot\cup}B^*,
                         \qquad |L|=6,
\]

be the spanning sole-complex shell, and let `Z` be a three-cut of the
three-connected graph `B^*`.  For a component `D` of `B^*-Z`, every
neighbour of `D` is in `Z union L`.  Since another component remains,
this neighbourhood is an actual separator.  Hence

\[
          7\le |N_G(D)|
             =|N_{B^*}(D)|+|N_L(D)|
          \le3+6=9.                                           \tag{1.1}
\]

A component whose boundary is not of order seven or eight has equality
throughout (1.1), and is full to both `Z` and `L`.

At most one component of `B^*-Z` can have this order-nine boundary.  If
`D_1,D_2` were two, write the shell as

\[
                       L=\{v,b_1,b_2,b_3,b_4,b_5\},
\]

with the `b_i` forming a clique.  Then

\[
             D_1\cup\{v\},\quad D_2,\quad
             \{b_1\},\ldots,\{b_5\}
\]

are seven literal pairwise adjacent connected bags.  The adjacency of the
first two is supplied by the edge from `D_2` to `v`; no edge between
`D_1,D_2` is assumed.  Thus they form a `K_7` model.

Every three-cut has at least two components, so one component has boundary
seven or eight.  No virtual torso edge or contracted carrier enters this
count.

## 2. The `K_4` convention

If `B^*` has order at least five, absence of a three-cut in a
three-connected graph is exactly four-connectivity.  If `B^*\cong K_4`,
argue separately.

For `d in B^*`, seven-connectivity gives

\[
                         7\le |N_G(d)|=3+|N_L(d)|,
\]

so every `d` sees at least four singleton labels.  If some `d` sees four
or five labels, the singleton shore `{d}` has an actual boundary of order
seven or eight: a missed label lies outside the shore and its
neighbourhood, so the boundary is a genuine separator.

Otherwise every vertex of `B^*` is full to `L`.  Label its vertices
`d_1,d_2,d_3,d_4`.  The seven bags

\[
            \{b_1\},\ldots,\{b_5\},\quad
            \{d_1\},\quad \{v,d_2,d_3,d_4\}
\]

form a `K_7` model.  The last bag is connected, it sees `d_1` through the
`K_4`, and both nonsingleton-side bags see every `b_i` by fullness.

Thus the patched conclusion is:

> a literal order-seven/eight shore, a labelled `K_7`, or a genuinely
> four-connected active torso.

The four-connected branch is then exactly in the valid range of the
Fabila--Monroy--Wood active-root theorem.

