# Gallai--Edmonds collapse at the endpoint-rigid order-eight boundary

**Status:** written proof with a separate GREEN internal audit in
[`hc7_endpoint_rigid_gallai_exchange_audit.md`](hc7_endpoint_rigid_gallai_exchange_audit.md).
The main result is a quotient-support theorem.  Its last corollary identifies
the precise branch-set interaction still needed in the original graph.  It
does not close that interaction or prove \(HC_7\).

## 1. Boundary setup

Let

\[
 S=K\mathbin{\dot\cup}\{a,b,c,d\}\mathbin{\dot\cup}\{x\},
 \qquad K=\{r_1,r_2,r_3\},
\]

and let \(J\) be a graph on \(S\) satisfying:

1. \(K\) is a clique;
2. \(ab,cd\in E(J)\);
3. there is no edge between \(\{a,b\}\) and \(\{c,d\}\);
4. each of the edges \(ab\) and \(cd\) is collectively adjacent to every
   vertex of \(K\); and
5. every one of \(a,b,c,d\) is nonadjacent to at least one vertex of \(K\).

Put \(F=\overline J\).  Conditions 2 and 3 say

\[
                     F[\{a,b,c,d\}]\cong K_{2,2},       \tag{1.1}
\]

with bipartition \(\{a,b\}\mid\{c,d\}\).  Conditions 4 and 5 say

\[
\begin{aligned}
 &N_F(a)\cap K,\ N_F(b)\cap K
       &&\text{are nonempty and disjoint},\\
 &N_F(c)\cap K,\ N_F(d)\cap K
       &&\text{are nonempty and disjoint}.              \tag{1.2}
\end{aligned}
\]

Let \(p,q\) be two new nonadjacent vertices, each adjacent to every
vertex of \(J\), and write

\[
                            Q=I_2\vee J.                 \tag{1.3}
\]

This setup is the unresolved order-eight output of the five-support star
reduction.  The two specified two-vertex branch sets have vertex sets
\(\{a,b\}\) and \(\{c,d\}\), and \(K\) is the common three-clique.
Condition 5 is not an additional heuristic assumption.  It is the
surviving conclusion of the audited
[endpoint-contact theorem](../results/hc7_star_order_eight_endpoint_contacts.md),
Theorem 2.1: if condition 5 fails in the host, then the host already has a
\(K_7\) minor or an actual order-seven separation.

For a minor model \(\mathcal M\), its **support order** is

\[
                  \left|\bigcup_{B\in\mathcal M}V(B)\right|.
\]

## 2. Lifting a small boundary model

### Lemma 2.1

If \(J\) has a \(K_5\)-minor model of support order at most seven, then
\(Q\) has a \(K_7\) minor.

### Proof

Let \(B_1,\ldots,B_5\) be the branch sets.  Choose

\[
                 w\in S-\bigcup_{i=1}^5V(B_i),
\]

which is possible because \(|S|=8\).  Then

\[
                     B_1,\ldots,B_5,\quad \{p,w\},\quad\{q\}
                                                               \tag{2.1}
\]

are seven pairwise disjoint connected branch sets.  Both new vertices are
complete to \(S\), and \(wq\) supplies the adjacency between the last two
sets.  Thus (2.1) is a \(K_7\)-minor model in \(Q\). \(\square\)

## 3. Collapse of the Gallai--Edmonds alternatives

Let

\[
                         V(F)=D\mathbin{\dot\cup}A
                                \mathbin{\dot\cup}C       \tag{3.1}
\]

be the Gallai--Edmonds decomposition of \(F\), and let \(q_D\) be the
number of components of \(F[D]\).  We use the standard facts that:

- every component of \(F[D]\) is factor-critical and has odd order;
- \(F[C]\) has a perfect matching;
- there is no edge of \(F\) from \(D\) to \(C\); and
- there is no edge of \(F\) between distinct components of \(F[D]\).

The audited
[canonical boundary theorem](../results/hc7_eight_boundary_gallai_edmonds.md)
gives, when \(F\) has no perfect matching and \(Q\) has no \(K_7\) minor,

\[
        (|A|,q_D)\in\{(0,2),(0,4),(1,3),(2,4)\}.        \tag{3.2}
\]

### Theorem 3.1 (endpoint-rigid Gallai--Edmonds collapse)

Assume that \(F\) has no perfect matching and \(Q\) has no \(K_7\) minor.
Then

\[
                         A=C=\varnothing,                \tag{3.3}
\]

and \(F\) has exactly two components: an isolated vertex \(s\) and a
factor-critical component on the other seven vertices.  Moreover,

\[
                         s\in K,\qquad x\ne s.           \tag{3.4}
\]

### Proof

We eliminate all possibilities in (3.2) except \((0,2)\), and then
determine the latter exactly.

#### Case 1: \((|A|,q_D)=(0,4)\)

The vertices \(a,b,c,d\) induce a connected four-cycle in \(F\).  Since
\(A=\varnothing\), this cycle lies in one component of \(F[D]\) or in one
component of \(F[C]\).

If it lies in \(C\), the two distinct \(K\)-neighbours in \(F\) required
for \(a,b\) by (1.2) also lie in that component.  Hence \(|C|\ge6\).
The four components of \(F[D]\) contribute at least four more vertices,
contrary to \(|S|=8\).

If the cycle lies in a component of \(F[D]\), the same two distinct
neighbours lie in that component.  Its order is at least six and, being
odd, at least seven.  The other three \(D\)-components contribute at least
three more vertices, again a contradiction.

#### Case 2: \((|A|,q_D)=(1,3)\)

First suppose that the unique vertex of \(A\) is not among
\(\{a,b,c,d\}\).  The four-cycle (1.1) lies in one component \(H\) of
\(F[D]\) or \(F[C]\).  At least one of the two distinct \(K\)-neighbours
of \(a,b\) is outside \(A\), and therefore belongs to \(H\).  If
\(H\subseteq C\), then \(|H|\ge5\); because every component of \(F[C]\)
has a perfect matching, \(|H|\ge6\).  Together with \(A\) and the three
\(D\)-components this exceeds eight vertices.

Thus \(H\) is a component of \(F[D]\).  If \(A\not\subseteq K\), both
distinct \(K\)-neighbours of \(a,b\) lie in \(H\), so \(|H|\ge6\) and
oddness gives \(|H|\ge7\), again too many vertices after adding \(A\) and
the other two \(D\)-components.  Consequently

\[
 A=\{r_0\}\subseteq K,\qquad
 C=\varnothing,\qquad
 |H|=5,                                      \tag{3.5}
\]

and the other two \(D\)-components are singletons.  The component \(H\)
contains \(a,b,c,d\) and exactly one vertex \(r\in K-\{r_0\}\).  For either
specified edge, its two nonempty disjoint missing-contact sets in \(K\)
can therefore use only \(r_0\) and \(r\); a vertex in another
\(D\)-component has no \(F\)-edge to an endpoint in \(H\).  Choose one
specified edge \(uv\) and orient it so that

\[
                   ur_0,vr\in E(F).
\]

Then (1.2) and the clique \(K\) give the four-cycle

\[
                         r_0-v-u-r-r_0                  \tag{3.6}
\]

in \(J\).  If \(z_1,z_2\) are the singleton \(D\)-components, the five
explicit branch sets

\[
                    \{r_0,r\},\quad\{u\},\quad\{v\},
                    \quad\{z_1\},\quad\{z_2\}           \tag{3.7}
\]

form a \(K_5\)-minor model in \(J\).  The first three form a triangle
model by (3.6).  Each \(z_i\) is complete in \(J\) to \(H\), so it is
adjacent to the first three sets through \(r,u,v\); and \(z_1z_2\in E(J)\).
The support order is six, contradicting Lemma 2.1.

It remains in this case to suppose that the unique vertex of \(A\) is a
specified endpoint; by symmetry let it be \(a\).  The vertices \(b,c,d\)
induce a connected path in \(F\), so they lie in one component \(H\) of
\(F[D]\) or \(F[C]\).  The intact edge \(cd\) has distinct
\(K\)-neighbours \(\rho_c,\rho_d\) in \(F\), and \(A=\{a\}\) contains
neither.  Hence both neighbours lie in \(H\).

The component cannot lie in \(C\): it contains at least five vertices,
and the perfect matching of \(F[C]\) would make its order at least six;
together with \(A\) and the three \(D\)-components this is impossible.
Thus \(H\) is a \(D\)-component.  Counting gives

\[
 F[D]\text{ component orders }5,1,1,\qquad C=\varnothing.       \tag{3.8}
\]

Let \(z_1,z_2\) be the singleton \(D\)-components.  Collective adjacency
and (1.2) give the four-cycle

\[
                    c-d-\rho_c-\rho_d-c               \tag{3.9}
\]

in \(J\).  Therefore

\[
             \{c,d\},\quad\{\rho_c\},\quad\{\rho_d\},
             \quad\{z_1\},\quad\{z_2\}                 \tag{3.10}
\]

is a \(K_5\)-minor model: the first three sets form a triangle model by
(3.9), and the last two vertices, lying in different \(D\)-components,
are adjacent to one another and complete in \(J\) to \(H\).  Its support
order is six, contradicting Lemma 2.1.

#### Case 3: \((|A|,q_D)=(2,4)\)

Here \(C=\varnothing\).  Indeed, if \(z\in C\), choose one vertex from
each of the four \(D\)-components.  Those four vertices and \(z\) are five
singleton branch sets inducing a \(K_5\) in \(J\).  Lemma 2.1 then gives
the explicit \(K_7\)-minor model (2.1), a contradiction.

It follows that \(|D|=6\), and the four odd component orders are

\[
                              3,1,1,1.                 \tag{3.11}
\]

Put \(k=|A\cap\{a,b,c,d\}|\).  If \(k=0\), the four-cycle (1.1) lies in
one \(D\)-component, contrary to (3.11).  If \(k=1\), the remaining three
specified endpoints induce a connected path in \(F\).  The intact
specified edge among them has two distinct \(K\)-neighbours.  At most one
of those neighbours is the other vertex of \(A\), so at least one joins
the three-vertex path in its \(D\)-component.  That component has order at
least four, again contrary to (3.11).

Suppose \(k=2\) and \(A\) contains both endpoints of the same specified
edge.  The endpoints of the other specified edge lie in \(D\) and have
two distinct \(K\)-neighbours.  If the endpoints lie in one
\(D\)-component, it has order at least four.  If they lie in different
\(D\)-components, each such odd component has order at least three, so
the four \(D\)-components have total order at least eight.  Both
alternatives contradict (3.11).

The only remaining placement has one endpoint of each specified edge in
\(A\).  Let \(u,v\) be their respective mates.  Since \(u,v\) come from
different specified edges, \(uv\in E(F)\) by (1.1), and they lie in the
unique three-vertex \(D\)-component.  Condition 5 forces that component to
be

\[
                              \{u,v,r\}                 \tag{3.12}
\]

for some \(r\in K\); otherwise one of \(u,v\) would have no
\(K\)-neighbour.  The other three \(D\)-components are

\[
                          \{r'\},\quad\{r''\},\quad\{x\},
                          \qquad K=\{r,r',r''\}.        \tag{3.13}
\]

Let \(u'\in A\) be the mate of \(u\) in its specified edge.  Since
\(ur\in E(F)\), (1.2) gives \(u'r\in E(J)\).  The five branch sets

\[
                 \{u\},\quad\{r'\},\quad\{r''\},\quad\{x\},
                 \quad\{u',r\}                         \tag{3.14}
\]

form a \(K_5\)-minor model.  The first four vertices lie in four distinct
\(D\)-components and hence induce a \(K_4\) in \(J\).  The last set is
connected, is adjacent to \(\{u\}\) through \(u'u\), and is adjacent to
the other three singleton sets through \(r\).  Again the support order is
six, and Lemma 2.1 gives a contradiction.

#### Case 4: \((|A|,q_D)=(0,2)\)

The four-cycle (1.1) lies in one component of \(F[D]\) or one component
of \(F[C]\).  Suppose first that it lies in \(C\).  The distinct
\(K\)-neighbours \(\rho_a,\rho_b\) of \(a,b\) also lie in that component.
Counting forces \(|C|=6\), while both \(D\)-components are singletons,
say \(z_1,z_2\).  Collective adjacency and (1.2) give the four-cycle

\[
                         a-b-\rho_a-\rho_b-a           \tag{3.15}
\]

in \(J\).  Thus

\[
             \{a,b\},\quad\{\rho_a\},\quad\{\rho_b\},
             \quad\{z_1\},\quad\{z_2\}                 \tag{3.16}
\]

is a \(K_5\)-minor model: the first three sets form a triangle model by
(3.15), while \(z_1,z_2\) are adjacent to one another and complete in
\(J\) to \(C\).  Lemma 2.1 gives a contradiction.

Therefore the four-cycle lies in one component of \(F[D]\).  The two
distinct \(K\)-neighbours of \(a,b\) lie in the same component, which has
order at least six and hence, being odd, at least seven.  The other
\(D\)-component is nonempty.  Since \(|S|=8\), equality holds throughout:
\(C=\varnothing\), the component orders are seven and one, and the
one-vertex component is an isolated vertex \(s\) of \(F\).  This proves
(3.3).

All four specified endpoints lie in the seven-vertex component.  Hence
\(s\in K\cup\{x\}\).  Suppose \(s=x\).  Choose \(y\in\{c,d\}\).  The seven
sets

\[
 \{r_1\},\quad\{r_2\},\quad\{r_3\},\quad\{a,b\},
 \quad\{p,y\},\quad\{q\},\quad\{x\}                    \tag{3.17}
\]

form a \(K_7\)-minor model in \(Q\).  Indeed, \(K\) is a clique, the
connected edge \(\{a,b\}\) is collectively adjacent to all of \(K\), and
\(p,q\) are complete to the boundary.  The edge \(yq\) joins
\(\{p,y\}\) to \(\{q\}\).  Finally, \(x\), being isolated in \(F\), is
universal in \(J\) and is adjacent to \(p,q\).  This contradiction proves
\(s\ne x\), and therefore \(s\in K\). \(\square\)

## 4. The canonical quotient pair

Relabel \(K=\{s,r_1,r_2\}\).  Since \(s\) is isolated in \(F\), none of
the four nonempty sets in (1.2) contains \(s\).  For each specified edge,
its two missing-contact sets are therefore the two singleton sets
\(\{r_1\}\) and \(\{r_2\}\).  After swapping endpoints if necessary,

\[
\begin{aligned}
 &ar_1,br_2\in E(F),\qquad ar_2,br_1\in E(J),\\
 &\text{and either }cr_1,dr_2\in E(F)
      \text{ or }cr_2,dr_1\in E(F).                    \tag{4.1}
\end{aligned}
\]

Put

\[
                       B=S-\{s,x\}
                         =\{r_1,r_2,a,b,c,d\}.          \tag{4.2}
\]

### Lemma 4.1 (theta remainder)

The graph \(J[B]\) is the union of the edge \(r_1r_2\) and two internally
vertex-disjoint paths of length three from \(r_1\) to \(r_2\).  In
particular, it is triangle-free.

### Proof

For \(ab\), one path is

\[
                         r_1-b-a-r_2.                  \tag{4.3}
\]

For \(cd\), (4.1) gives either \(r_1-d-c-r_2\) or
\(r_1-c-d-r_2\).  Condition 3 excludes every edge between the internal
vertices of the two paths.  The exact singleton missing-contact sets
exclude any further edge between a specified endpoint and
\(\{r_1,r_2\}\).  These are all possible edges of \(J[B]\), proving the
claim. \(\square\)

### Theorem 4.2 (quotient support-height exchange)

The graph

\[
                           Q-\{s,x\}=I_2\vee J[B]       \tag{4.4}
\]

has no \(K_5\)-minor model of support order at most six.

### Proof

A model of support order five is a \(K_5\) subgraph.  If it uses neither
of \(p,q\), then \(J[B]\) contains a \(K_5\); if it uses exactly one, then
\(J[B]\) contains a \(K_4\); and it cannot use both because \(pq\notin
E(Q)\).  All alternatives contradict triangle-freeness.

A model of support order six has exactly one two-vertex branch set, which
induces an edge, and four singleton branch sets, which induce a \(K_4\).
If it uses neither \(p\) nor \(q\), the four singleton vertices give a
\(K_4\) in \(J[B]\).  If it uses exactly one apex, then either that apex
is a singleton and the other three singleton vertices give a triangle in
\(J[B]\), or it belongs to the two-vertex branch set and all four
singleton vertices give a \(K_4\) in \(J[B]\).

It remains that both \(p,q\) are used.  They cannot both be singleton
branch sets, and the set \(\{p,q\}\) is disconnected.  Hence one, say
\(q\), is a singleton and the other belongs to the edge branch set
\(\{p,w\}\) for some \(w\in B\).  The remaining three singleton branch
sets then induce a triangle in \(J[B]\), again impossible. \(\square\)

## 5. Exact implication in the original graph

Let \(G\) have a separation

\[
               V(G)=U\mathbin{\dot\cup}S
                         \mathbin{\dot\cup}W,           \tag{5.1}
\]

where \(U,W\) are nonempty and connected, there is no edge from \(U\) to
\(W\), and every vertex of \(S\) has a neighbour in each of \(U,W\).
Contracting \(U\) and \(W\) separately produces the quotient \(Q\) in
(1.3), with contraction vertices \(p,q\).

For a two-vertex set \(P\), let \(\mu_G(P)\) be the minimum support order
of a \(K_5\)-minor model in \(G-P\), with value \(+\infty\) if no such
model exists.

### Corollary 5.1 (a shore meets two branch sets)

Assume

\[
                          \max_{|P|=2}\mu_G(P)=6.       \tag{5.2}
\]

Then \(G-\{s,x\}\) has a \(K_5\)-minor model of support order at most six,
and every such model meets at least one of \(U,W\) in vertices belonging
to two distinct branch sets.

### Proof

Equation (5.2) gives \(\mu_G(\{s,x\})\le6\).  Choose such a model and
suppose that each of \(U,W\) meets at most one of its branch sets.  If an
open side meets one branch set, enlarge that branch set to contain the
entire connected open side; if it meets none, leave the open side unused.
The enlargements are disjoint and preserve every old branch-set adjacency.
Now contract \(U\) and \(W\).  Each contraction occurs inside at most one
branch set and cannot increase the support order.  The resulting model is
a \(K_5\)-minor model of support order at most six in \(Q-\{s,x\}\),
contrary to Theorem 4.2. \(\square\)

Theorem 4.2 concerns support in the contracted graph \(Q\), whereas (5.2)
concerns support in the original graph \(G\).  Corollary 5.1 is exactly
what follows from their difference: the contraction of an open side would
merge two named branch sets of every small response model.

The remaining implication is therefore the following standard
branch-set/separation problem.

> Let \(G\) be a \(7\)-chromatic graph for which every proper minor is
> \(6\)-colourable, and suppose \(G\) has no \(K_7\) minor.  In the
> order-eight configuration above, use a support-at-most-six
> \(K_5\)-minor model in \(G-\{s,x\}\), two of whose branch sets meet the
> same connected open side, to obtain at least one of:
>
> 1. a \(K_7\)-minor model in \(G\);
> 2. a two-vertex set \(P\) with \(\mu_G(P)\ge7\); or
> 3. an order-seven separation which preserves the specified branch sets
>    and strictly decreases a declared induction parameter.

Merely contracting the open side cannot prove this statement: that
contraction merges the two branch-set labels which Corollary 5.1 forces.
The missing step must use the two branch sets together with colourings of
proper minors obtained by deleting or contracting an internal edge of the
open side.  Those colourings yield colour-labelled Kempe connections, but
they do not by themselves identify colours with the vertices
\(r_1,r_2,a,b,c,d\).  No such label-preserving lift is claimed here.

## 6. Trust boundary

The only external input is the classical Gallai--Edmonds decomposition
theorem.  The four-type reduction (3.2) is proved and separately audited in
the linked canonical boundary theorem.  The origin of condition 5 is
proved and separately audited in the linked endpoint-contact theorem.
Every deduction after those two inputs is a hand argument in this file.  The
adjacent audit checks this exact promoted revision; it is an internal audit,
not external peer review.
