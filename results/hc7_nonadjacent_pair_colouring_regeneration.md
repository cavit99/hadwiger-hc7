# Colouring and minor regeneration after deleting a nonadjacent pair

**Status:** written proof; independently audited in
[`hc7_nonadjacent_pair_colouring_regeneration_audit.md`](hc7_nonadjacent_pair_colouring_regeneration_audit.md).
This is an input to the support-six extraction problem, not a proof of its
transversal theorem or of $HC_7$.

## 1. Statement

### Theorem 1.1

Let $G$ be a graph with

\[
 \chi(G)=7
 \quad\text{and}\quad
 \chi(H)\le 6\text{ for every proper minor }H\text{ of }G.
\]

Let $P=\{p,q\}$ be a nonadjacent pair, and put $H=G-P$.  Then:

1. $\chi(H)=6$;
2. in every proper six-colouring of $H$, at least one of $p,q$ has a
   neighbour in every colour class;
3. there is a proper six-colouring $c_p$ of $H$ in which $p$ has a
   neighbour in every colour class, and there is a possibly different
   proper six-colouring $c_q$ in which $q$ has a neighbour in every colour
   class;
4. $H-v$ contains a dominating $K_5$ model for every $v\in V(H)$; and
5. $H$ contains a $K_6$ minor.

If, in addition, a four-clique $X\subseteq V(H)$ is complete to both
$p$ and $q$, then in the colouring $c_p$ the vertex $p$ has neighbours
outside $X$ in each of the two colours absent from $X$.  The analogous
statement holds for $q$ and $c_q$.

### Proof

The graph $H$ is a proper subgraph of $G$, so it is six-colourable.  If it
were five-colourable, the nonadjacent vertices $p,q$ could both be assigned
one new sixth colour.  This would six-colour $G$, a contradiction.  Hence
$\chi(H)=6$.

Fix any proper six-colouring $c$ of $H$.  If $p$ misses one colour on its
neighbourhood and $q$ misses one colour on its neighbourhood, assign to
each vertex one such missing colour.  The two assigned colours need not be
different because $pq\notin E(G)$.  This again extends $c$ to a proper
six-colouring of $G$.  Therefore at least one of $p,q$ sees every colour
class, proving part 2.

The proper minor $G-p$ has a proper six-colouring.  Every one of its six
colours must occur in $N_G(p)$, since otherwise the missing colour could be
assigned to $p$.  Because $pq\notin E(G)$, all neighbours of $p$ lie in
$H$.  Restricting this colouring to $H$ therefore gives the required
colouring $c_p$.  Applying the same argument to $G-q$ gives $c_q$.

For $v\in V(H)$, suppose that $H-v$ were four-colourable.  Give $v$ a
fifth colour and give both $p,q$ a sixth colour.  This is a proper
six-colouring of $G$, again a contradiction.  Thus $\chi(H-v)\ge5$.
The Dominating 4-Colour Theorem now implies that $H-v$ contains a
dominating $K_5$ model (and hence an ordinary $K_5$ minor).  Similarly,
$\chi(H)=6$ and the proved $t=6$ case of Hadwiger's Conjecture imply that
$H$ contains a $K_6$ minor.

Finally, a proper colouring assigns four distinct colours to the clique
$X$.  In $c_p$, the vertex $p$ sees all six colours and its neighbours in
$X$ account for only those four colours.  It consequently has a neighbour
in $H-X$ in each of the remaining two colours.  The assertion for $q$ is
symmetric.  \(\square\)

## 2. Application to the live zero-intersection branch

In the order-five common-core outcome of the private-pair dichotomy, the
two additional supports are $X\cup\{p\}$ and $X\cup\{q\}$, where $X$ is a
four-clique complete to the nonadjacent pair $p,q$.  The globally maximal
private-pair theorem permits the avoided support to be chosen as a
six-vertex $K_5$ model disjoint from $P$; in the zero-intersection case it
is also disjoint from $X$.

Theorem 1.1 therefore adds three facts not present in the static quotient
counterexample:

- $G-P$ is exactly six-chromatic and contains a $K_6$ minor;
- every vertex can be avoided by some dominating $K_5$ model in $G-P$; and
- both choices of a colour-dominating endpoint of $P$ are legally attained
  by proper-minor colourings, with two differently coloured neighbours
  outside $X$ in each mode.

The theorem does not preserve the branch-set labels of the regenerated
minors, make the two dominating colourings compatible, or compose the
disjoint six-vertex model and $K_6^-$ into a $K_7$ minor.  Those are the
remaining label-preserving linkage obligations.

The external input in part 4 is Theorem 1.1 of A. Girão, F. Illingworth,
B. Mohar, S. Norin, R. Steiner, Y. Tamitegama, J. Tan, D. R. Wood and
J. H. Yip, *The Dominating 4-Colour Theorem*, arXiv:2605.10112 (2026).
Its statement and terminology have already been independently checked in
the audit of
[`../results/hc7_common_deletion_dominating_five_substrate.md`](../results/hc7_common_deletion_dominating_five_substrate.md).
