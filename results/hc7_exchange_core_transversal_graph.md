# The minimum-transversal graph of the canonical support-exchange core

**Status:** written proof; independently audited in
[`hc7_exchange_core_transversal_graph_audit.md`](hc7_exchange_core_transversal_graph_audit.md).
This is a finite set-system theorem inside the support-six programme.  It
does not prove the two-vertex transversal theorem or `HC_7`.

## 1. Setup

Let `G` and the set families `C,H` be as in Theorem 2.1 of
[`../results/hc7_one_vertex_support_exchange.md`](../results/hc7_one_vertex_support_exchange.md).
Thus

\[
 H=\mathcal F_5(G)\cup(C-\{A\}),\qquad \tau(H)=2,
\]

every member of `H` has order five or six, and

\[
 Z_H=V(G)-\bigcup\{R:R\text{ is a two-vertex transversal of }H\}.
\]

Define the **minimum-transversal graph** `B_H` on `V(G)-Z_H` by declaring
`uv` to be an edge exactly when `{u,v}` is a transversal of `H`.
There are no isolated vertices by the definition of `Z_H`.

## 2. Canonical dichotomy

### Theorem 2.1

Exactly one of the following structural alternatives holds.

1. `B_H` has two vertex-disjoint edges.  These edges are two disjoint
   globally support-maximal private pairs for every exact six-vertex
   `K_5`-model support contained in `Z_H`.
2. All edges of `B_H` have a common endpoint `p`.  If `L` is the set of
   their other endpoints, then

   \[
                         |L|\le6,
        \qquad V(G)-Z_H=\{p\}\cup L.                 \tag{2.1}
   \]

   Moreover, every member of `H` which avoids `p` contains all of `L`.
3. `B_H` is a triangle on vertices `{a,b,c}`.  In this case

   \[
                       V(G)-Z_H=\{a,b,c\},            \tag{2.2}
   \]

   and every member of `H` contains at least two of `a,b,c`.

In particular,

\[
 \boxed{\text{either there are two disjoint globally maximal private pairs,
 or }|V(G)-Z_H|\le7.}                                  \tag{2.3}
\]

#### Proof

If `B_H` has two disjoint edges, let `R` be either one.  It is a
two-vertex transversal of `H` and is disjoint from `Z_H`.  Hence it avoids
every exact six-vertex support `A' subseteq Z_H`.  It meets every literal
`K_5` support, because `F_5(G) subseteq H`, and `A'` is a six-vertex
support in `G-R`.  Therefore

\[
                         \mu_G(R)=6.
\]

Under the standing contradictory assumption
`tau(F_6(G))>2`, no pair has support height above six.  Thus both disjoint
edges are globally support-maximal private pairs for every such `A'`.
This proves alternative 1 and its extra assertion.

Assume now that `B_H` has no two disjoint edges.  Its edge set is therefore
pairwise intersecting.  A simple graph with a nonempty pairwise-intersecting
edge set is either a subgraph of a star or a triangle: fix two incident
edges `pa,pb`; every further edge contains `p`, unless it is `ab`, and if
`ab` occurs then every edge is one of `pa,pb,ab`.

Suppose first that all edges have the common endpoint `p`, and let `L` be
the set of their other endpoints.  Since `tau(H)=2`, the singleton `{p}`
is not a transversal of `H`; choose `E in H` with `p notin E`.  For every
`x in L`, the pair `{p,x}` transverses `H`, so it meets `E`.  As `p` is
absent from `E`, this forces `x in E`.  Hence `L subseteq E`.  Every member
of `H` has order at most six, so `|L|<=6`.  The same argument, with an
arbitrary member of `H` avoiding `p`, proves the final assertion of
alternative 2.  Since `B_H` has no isolated vertices, its vertex set is
exactly `{p} union L`, proving (2.1).

Finally suppose the edges have no common endpoint.  The elementary
classification above makes `B_H` exactly the triangle `ab,bc,ca`; again
there are no other vertices because there are no isolated vertices.  Every
`E in H` meets each of these three transversal edges.  A subset of
`{a,b,c}` meeting all three edges has order at least two, so
`|E cap {a,b,c}|>=2`.  This proves alternative 3.

The three displayed alternatives exhaust the possibilities, and (2.3)
follows. \(\square\)

### Corollary 2.2 (connectivity or an exact order-seven boundary)

Assume that alternative 2 or 3 of Theorem 2.1 holds, and put

\[
                           U=V(G)-Z_{\mathcal H}.
\]

If $|U|\le6$, then $G-U$ has no separation of order below
$7-|U|$ with both open sides nonempty.  In particular, it is connected.

If $|U|=7$ and $G-U$ is disconnected, then $U$ is an actual order-seven
boundary.  Every component $C$ of $G-U$ satisfies

\[
                              N_G(C)=U.                \tag{2.4}
\]

#### Proof

Let $(J_1,J_2)$ be a separation of $G-U$ with both open sides nonempty
and boundary $S$.  Then deleting $U\cup S$ disconnects $G$.  Seven-
connectivity therefore gives

\[
                              |U|+|S|\ge7,
\]

which proves the first assertion.

Now let $|U|=7$ and let $C$ be a component of $G-U$.  Its neighbourhood
is contained in $U$.  If it omitted a vertex of $U$, its neighbourhood
would have order at most six and would separate $C$ from that omitted
vertex, contrary to seven-connectivity.  Hence $N_G(C)=U$. \(\square\)

## 3. Consequence for repaired-contact exchanges

Every one-vertex support replacement inside `Z_H` preserves the same graph
`B_H`.  Thus an `a_3`--`x` bypass that leaves the canonical exchange core
does not enter an unstructured collection of new private pairs:

- either two disjoint globally maximal private pairs are already available;
  or
- every possible first exit lies in one fixed set of at most seven
  vertices.  If that set disconnects the host, Corollary 2.2 makes it an
  exact order-seven boundary with full attachment on every component;
  otherwise the remaining core has the corresponding residual
  connectivity.

This is a genuine global normalization, but it is not yet a descending
argument.  The disjoint-pair branch still needs a label-preserving model
composition theorem, while the bounded-locus branch needs either a rooted
linkage avoiding that locus or an actual order-seven separation using it as
boundary.
