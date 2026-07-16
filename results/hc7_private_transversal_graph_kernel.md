# The private-transversal graph of a minimal support obstruction

**Status:** written proof; independently audited in
[`hc7_private_transversal_graph_kernel_audit.md`](hc7_private_transversal_graph_kernel_audit.md).
This is a finite set-system reduction inside the support-six programme.  It
does not prove the two-vertex transversal theorem or $HC_7$.

## 1. Setup

Let $G$ be a seven-connected graph with no $K_7$ minor.  For
$r\in\{5,6\}$, let $\mathcal F_r(G)$ be the family of supports of
$K_5$-minor models in $G$ using at most $r$ vertices.  Let

\[
             \mathcal C=\{A_1,\ldots,A_m\}
                \subseteq \mathcal F_6(G)-\mathcal F_5(G)       \tag{1.1}
\]

be nonempty and inclusion-minimal subject to

\[
       \tau\bigl(\mathcal F_5(G)\cup\mathcal C\bigr)>2.          \tag{1.2}
\]

For every $i$, choose a two-vertex transversal $P_i$ of

\[
       \mathcal H_i=\mathcal F_5(G)\cup
                    (\mathcal C-\{A_i\})                         \tag{1.3}
\]

which is disjoint from $A_i$.  Such a pair exists by minimality; it may be
chosen as in Theorem 2.1 of
[`../results/hc7_maximal_support_pair_private_pair_bridge.md`](../results/hc7_maximal_support_pair_private_pair_bridge.md),
so every $P_i$ is also globally maximal for the support-height potential.

Call the simple graph with edge set $\{P_1,\ldots,P_m\}$ the
**chosen private-transversal graph**.

## 2. Matching-or-small-kernel theorem

### Theorem 2.1

The pairs $P_1,\ldots,P_m$ are distinct.  Moreover, exactly one of the
following alternatives holds.

1. Two of the pairs $P_i$ are vertex-disjoint.
2. There are a vertex $p$ and distinct vertices
   $\ell_1,\ldots,\ell_m$ such that

   \[
       P_i=\{p,\ell_i\},\qquad
       \{p,\ell_i\}\cap A_i=\varnothing,
       \qquad
       \{\ell_j:j\ne i\}\subseteq A_i                 \tag{2.1}
   \]

   for every $i$, and $m\le6$.
3. We have $m=3$, and for three vertices $a,b,c$ the three private pairs
   are $ab,bc,ca$.  If $A_{ab}$ denotes the support whose private pair is
   $ab$, and similarly for the other two edges, then

   \[
                      c\in A_{ab},\qquad
                      a\in A_{bc},\qquad
                      b\in A_{ca}.                    \tag{2.2}
   \]

Consequently, either the critical family supplies two disjoint globally
support-maximal private pairs, or it has at most six members and its chosen
private pairs have one of the explicit structures in alternatives 2--3.

#### Proof

For distinct $i,j$, the pairs $P_i$ and $P_j$ cannot be equal.  Indeed,
$P_i$ is disjoint from $A_i$ but, because $A_i\in\mathcal H_j$, the pair
$P_j$ meets $A_i$.  Equality would contradict these two assertions.

Suppose that alternative 1 fails.  Then the edge set of the chosen
private-transversal graph is pairwise intersecting.  A nonempty
pairwise-intersecting family of distinct edges in a simple graph is either
contained in a star or is exactly a triangle.  To see this, fix two
distinct intersecting edges $pa,pb$.  Every further edge contains $p$
unless it is $ab$; if $ab$ occurs, every edge is one of $pa,pb,ab$.

First suppose that all the pairs have the common endpoint $p$.  Write
$P_i=\{p,\ell_i\}$.  Their distinctness makes the leaves $\ell_i$
distinct.  Since $P_i\cap A_i=\varnothing$, neither $p$ nor $\ell_i$
belongs to $A_i$.  If $j\ne i$, then $A_i\in\mathcal H_j$, so $P_j$
meets $A_i$.  The vertex $p$ is absent from $A_i$, and therefore
$\ell_j\in A_i$.  This proves (2.1).

Every $A_i$ has order six.  Thus (2.1) first gives $m-1\le6$, or
$m\le7$.  If $m=7$, put $L=\{\ell_1,\ldots,\ell_7\}$.  Equation (2.1)
and $|A_i|=6$ force

\[
                            A_i=L-\{\ell_i\}           \tag{2.3}
\]

for every $i$.  Hence every six-subset of the seven-set $L$ supports a
$K_5$-minor model.  Lemmas 4.2--4.3 of the
[separated-support theorem](../results/hc7_support_at_most_six_separated_triple_extraction.md)
give a $K_6$ minor supported on $L$ and then, by seven-connectivity, a
seventh branch set.  This produces a $K_7$ minor, contrary to the
hypothesis on $G$.  Therefore $m\le6$, proving alternative 2.

Finally suppose that the chosen private-transversal graph has no common
edge endpoint.  The elementary classification above makes its edge set
exactly the triangle $ab,bc,ca$, so $m=3$.  The support $A_{ab}$ avoids
$a,b$ but must meet each of the other two private pairs $bc$ and $ca$.
The only possible common witness is $c$, so $c\in A_{ab}$.  The other two
containments in (2.2) follow cyclically.  This proves alternative 3 and
completes the proof. \(\square\)

### Corollary 2.2 (literal-clique witnesses in the star alternative)

Suppose alternative 2 holds and $m\ge2$.  For every two distinct indices
$i,j$, the graph $G$ contains a literal $K_5$ subgraph $K_{ij}$ such that

\[
                 p\in V(K_{ij}),\qquad
                 \{\ell_i,\ell_j\}\cap V(K_{ij})=\varnothing.  \tag{2.4}
\]

#### Proof

The pair $\{\ell_i,\ell_j\}$ meets every member of $\mathcal C$.  It
meets $A_i$ at $\ell_j$, meets $A_j$ at $\ell_i$, and meets every other
$A_k$ at both vertices, by (2.1).  It cannot be a transversal of
$\mathcal F_5(G)\cup\mathcal C$, by (1.2).  Hence some member of
$\mathcal F_5(G)$ avoids both leaves.  That member is the vertex set of a
literal $K_5$ subgraph $K_{ij}$.  Since the private pair
$P_i=\{p,\ell_i\}$ transverses $\mathcal F_5(G)$ and $K_{ij}$ avoids
$\ell_i$, it follows that $p\in V(K_{ij})$. \(\square\)

## 3. Exact contribution and limitation

The previous sharp general bound on $m$ is twenty-seven.  Theorem 2.1
shows that every branch without two disjoint private pairs has at most six
supports and has a canonical star or triangle incidence pattern.  It also
retains the actual vertices of every private pair, rather than only the
support intersections.

The theorem does not compose the $K_5$ models carried by those supports.
In alternative 1, a label-preserving construction from the two disjoint
pairs is still required.  In alternatives 2--3, the bounded number of
supports does not by itself bound their ambient branch-set linkages or
produce a two-vertex transversal of all of $\mathcal F_6(G)$.
