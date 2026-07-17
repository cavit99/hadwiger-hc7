# An all-cut interval criterion for the colour-matched path exchange

**Status:** written proof; separate internal audit GREEN.  This is an exact
branch-set exchange criterion in the unique-deficiency star--Kempe setup.  It
does not force an order-seven separation and does not prove `HC_7`.

## 1. Setup and cut branch sets

Use the setup of the audited colour-matched path exchange theorem.  Thus

\[
 C,\ \{u\},\ \{z\},\ X,\ D_1,D_2,D_3
\]

form a `K_7`-minus-one-edge model whose only missing adjacency is
`C`--`{u}`.  Let

\[
                       P=p_0p_1\cdots p_m,
                       \qquad m\geq 1,                \tag{1.1}
\]

be a colour-matched path, oriented so that `p_0` is its unique vertex in
`C` and `p_m` is its unique vertex in `T=N_R(u)`.  In particular,
`p_m u` and `zu` are edges, and no vertex of `P` is `z` or `u`.

For every cut edge `p_{q-1}p_q`, where `1<=q<=m`, put

\[
 \begin{aligned}
 C_q&=C\cup\{p_1,\ldots,p_{q-1}\},\\
 U_q&=\{u,p_q,\ldots,p_m\}.
 \end{aligned}                                      \tag{1.2}
\]

Empty displayed path intervals are omitted.  The sets `C_q,U_q` are
disjoint and connected, and the cut edge makes them adjacent.

Write

\[
                         \mathcal K=\{X,D_1,D_2,D_3\}.
\]

For `K in mathcal K`, let `L` be a component of `G[K-V(P)]`, and define
its set of attachment indices on the path by

\[
 A_P(L)=\{r\in\{0,\ldots,m\}:E_G(L,\{p_r\})\ne\varnothing\}. \tag{1.3}
\]

Use the following endpoint conventions:

\[
 \lambda(L)=
 \begin{cases}
  1,&E_G(L,C)\ne\varnothing,\\
  1+\min A_P(L),&E_G(L,C)=\varnothing\ne A_P(L),\\
  m+1,&E_G(L,C)=\varnothing=A_P(L),
 \end{cases}                                         \tag{1.4}
\]

and

\[
 \rho(L)=
 \begin{cases}
  m,&E_G(L,\{u\})\ne\varnothing,\\
  \max A_P(L),&E_G(L,\{u\})=\varnothing\ne A_P(L),\\
  0,&E_G(L,\{u\})=\varnothing=A_P(L).
 \end{cases}                                         \tag{1.5}
\]

The interval `[lambda(L),rho(L)]` is understood to contain only integer cut
indices in `{1,...,m}`; it is empty when `lambda(L)>rho(L)`.

## 2. Exact valid-cut lemma

### Lemma 2.1

For every residual component `L` and every `q in {1,...,m}`, the following
are equivalent:

1. `L` is adjacent to both `C_q` and `U_q`;
2. `lambda(L)<=q<=rho(L)`.

#### Proof

The set `L` is adjacent to `C_q` exactly when it is adjacent to `C`, or it
has a path neighbour among `p_0,...,p_{q-1}`.  If it is not adjacent to
`C`, this is equivalent to

\[
                         \min A_P(L)\le q-1,
\]

with no solution when `A_P(L)` is empty.  This is precisely
`lambda(L)<=q` under (1.4).

Similarly, `L` is adjacent to `U_q` exactly when it is adjacent to `u`, or
it has a path neighbour among `p_q,...,p_m`.  In the second case this is
equivalent to

\[
                         q\le\max A_P(L),
\]

again with no solution when `A_P(L)` is empty.  This is precisely
`q<=rho(L)` under (1.5).  Combining the two equivalences proves the
lemma. \(\square\)

## 3. Simultaneous interval exchange

### Theorem 3.1

For every `K in mathcal K`, choose a component `L_K` of `G[K-V(P)]`.
Suppose that:

1. every `L_K` is adjacent to `z`;
2. the four chosen components are pairwise adjacent; and
3. their valid-cut intervals have a common integer point, equivalently

   \[
       \max_{K\in\mathcal K}\lambda(L_K)
          \le
       \min_{K\in\mathcal K}\rho(L_K).              \tag{3.1}
   \]

Then `G` contains a `K_7` minor.  More precisely, for any integer `q`
between the two sides of (3.1), an explicit model is

\[
                 C_q,\quad U_q,\quad\{z\},\quad
                 (L_K:K\in\mathcal K).               \tag{3.2}
\]

#### Proof

All seven sets in (3.2) are nonempty, connected and pairwise disjoint.
The cut edge `p_{q-1}p_q` joins `C_q` to `U_q`.  The vertex `z` is
adjacent to `C_q` because `C` contains the deficient branch set meeting
`S=N_R(z)`, and it is adjacent to `U_q` through the edge `zu`.

By Lemma 2.1, each `L_K` is adjacent to both `C_q` and `U_q`.  It is
adjacent to `z` by hypothesis 1, and the four such components are mutually
adjacent by hypothesis 2.  These are every required pair of branch-set
adjacencies in (3.2), proving that (3.2) is a `K_7`-minor model.
\(\square\)

For a fixed four-tuple of residual components, Lemma 2.1 makes (3.1) the
exact condition under which one cut of `P` makes all four components
adjacent to both repaired branch sets.  The theorem does not assert that a
suitable four-tuple exists.

## 4. A quasi-`K_7` strengthening

A **quasi-`K_7` model** is a family of seven pairwise disjoint nonempty
vertex sets, not assumed connected individually, such that the union of
every two induces a connected graph.

### Lemma 4.1

Every graph containing a quasi-`K_7` model contains a `K_7` minor.

#### Proof

Let `B_1,...,B_7` be a quasi-`K_7` model, let `c_i` be the number of
components of `G[B_i]`, and put `n=sum_i c_i`.  Contract each of those
components to one vertex, delete all other vertices, and suppress parallel
edges.  The resulting simple graph `J` is a minor of `G` and has `n`
vertices.

For every `i<j`, the subgraph of `J` on the component vertices arising
from `B_i union B_j` is connected.  It consequently has at least
`c_i+c_j-1` edges.  Edges counted for distinct unordered pairs `{i,j}`
are disjoint, because distinct components belonging to the same `B_i`
have no edge between them.  Hence

\[
 |E(J)|\ge
 \sum_{i<j}(c_i+c_j-1)=6n-21.                         \tag{4.1}
\]

Every `c_i` is positive, so `n>=7`, and

\[
                         6n-21\ge5n-14.               \tag{4.2}
\]

Mader's exact extremal theorem for `K_7` minors says that a simple graph
on `n>=7` vertices with at least `5n-14` edges contains a `K_7` minor.
Thus `J`, and therefore `G`, contains a `K_7` minor. \(\square\)

### Corollary 4.2

For every `K in mathcal K`, let `B_K` be a nonempty union of components
of `G[K-V(P)]`.  Suppose there is a cut `q` such that:

1. every component `L` included in any `B_K` satisfies
   `lambda(L)<=q<=rho(L)` and is adjacent to `z`; and
2. for every two distinct `K,K' in mathcal K`, the graph
   `G[B_K union B_{K'}]` is connected.

Then `G` contains a `K_7` minor.

#### Proof

Lemma 2.1 says that every component included in `B_K` is adjacent to both
`C_q` and `U_q`.  Since those two sets are connected, both
`G[B_K union C_q]` and `G[B_K union U_q]` are connected.  Adjacency of
every component to `z` similarly makes `G[B_K union {z}]` connected.
The three sets `C_q,U_q,{z}` are connected and pairwise adjacent, and
hypothesis 2 handles every pair of the remaining four sets.  Therefore

\[
                     C_q,U_q,\{z\},(B_K:K\in\mathcal K)
\]

is a quasi-`K_7` model.  Lemma 4.1 finishes the proof. \(\square\)

Unlike Theorem 3.1, this corollary permits a protected representative to
be disconnected and does not require one selected component from each
protected branch set to form a transversal clique.  It instead requires
each two protected representatives to have connected union.

## 5. Limitation exposed by the joined-triangulation barrier

The audited 44-vertex graph `K_2 vee P` from the three-common-branch-set
barrier admits the connected-star colouring

\[
\begin{array}{c|l}
0&6,10,11,13,17,23,25,33,37,39\\
1&2,9,14,16,26,28,29,32,35,40\\
2&0,1,3,8,22,24,30,31,34,38\\
3&4,5,7,15,19,20,21,27,36,41\\
4&42\\
5&43.
\end{array}
\]

Taking the first two classes for `X`, the rooted model with singleton
branch sets `42,43,1,20` has unique deficient branch set `20`.  Its
expanded component is

\[
                         C=\{3,8,20,21,24,27\},
\]

and the shortest colour-matched path is

\[
                              20-17-19.                \tag{5.1}
\]

The residual components are

\[
                    X-\{17\},\quad\{42\},\quad\{43\},\quad\{1\}.
\]

All four have the full valid-cut interval `[1,2]`.  Nevertheless,
`X-{17}` is nonadjacent to `{1}`, so they do not form the required
four-partite transversal clique.  The two corresponding neighbourhoods
have orders 24 and 7, respectively.  The graph also has the order-seven
separator `N_G(z)`.

Thus changing the cut edge cannot resolve every branch-set compatibility
failure, and the interval criterion alone supplies no upper bound on a
separator.  This example does not refute a global theorem saying that the
full `HC_7` hypotheses force some order-seven separation: it is
six-colourable, and it already has such separations.  Any such theorem must
use the compulsory proper-minor colouring responses, not just the interval
geometry and seven-connectivity.

The same example also shows that the natural residual representatives do
not automatically form a quasi-`K_7`: the union
`(X-{17}) union {1}` is disconnected.  Thus Corollary 4.2 is a genuine
additional sufficient condition, not an automatic consequence of the
original near-`K_7` model.

## 6. Dependencies

- [colour-matched repair path](hc7_colour_matched_repair_path.md)
- [component exchange criterion](hc7_colour_matched_path_component_exchange.md)
- [fixed-path exchange or separation](hc7_colour_matched_path_exchange_or_separator.md)
- [three-common-branch-set barrier](../barriers/hc7_three_common_geodesic_two_apex_barrier.md)

The external extremal input in Lemma 4.1 is W. Mader,
*Homomorphiesatze fur Graphen*, Math. Ann. **178** (1968), 154--168,
DOI `10.1007/BF01350657`: a simple `K_7`-minor-free graph on `n>=7`
vertices has at most `5n-15` edges.
