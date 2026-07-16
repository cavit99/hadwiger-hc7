# Attachment concentration for a repaired component

**Status:** written proof; independently audited GREEN in the adjacent audit.
The result treats an infinite family in the canonical `3+1` six-linkage.  It
does not prove that two residual components compose to a $K_7$ minor.

## 1. Canonical linkage

Let `G` contain the endpoint configuration

\[
 A=\{a_0,a_1,a_2,a_3,x,y\},\qquad
 B=\{b_0,b_1,b_2,r,p,q\}.                              \tag{1.1}
\]

Assume that `a0,a1,a2,a3` induce a clique, that

\[
                   xy,\ a_3y,\ xa_0,\ xa_1,\ xa_2      \tag{1.2}
\]

are edges, and that `B` induces $K_6-pq$.  Let

\[
\begin{array}{lll}
 P_0:a_0-b_0,&P_1:a_1-b_1,&P_2:a_2-b_2,\\
 P_3:a_3-p,&P_4:x-q,&P_5:y-r
\end{array}                                               \tag{1.3}
\]

be six pairwise vertex-disjoint paths, internally disjoint from $A\cup B$,
and put $\Sigma=\bigcup_{i=0}^5P_i$.

Let `C` be a component of $G-V(\Sigma)$ which is adjacent to both `a3`
and `x`.  These are precisely the two fixed contacts of a residual
`a3`--`x` path after the six-terminal crossing decoder.

## 2. Two forbidden linkage paths

### Lemma 2.1

If `C` has a neighbour in $V(P_3)-\{a_3\}$ or in
$V(P_4)-\{x\}$, then `G` contains a $K_7$ minor.

#### Proof

Suppose first that `C` has a neighbour `v` in
$V(P_3)-\{a_3\}$; the possibility `v=p` is included.  Inside `C`, choose
a finite connected subgraph meeting attachment edges to `a3`, `x`, and
`v`, and contract it to a vertex `c`.  Contract the `v`--`p` segment of
`P3` toward `p`, and then contract the edge `cx` into `x`.  Shorten the
six named paths while keeping their twelve ends distinct.  The resulting
minor contains the normalized endpoint graph and the extra edge `px`.

Seven branch sets are

\[
 \{b_0\},\ \{b_1\},\ \{b_2\},\ \{r\},\ \{p\},\
 \{x,q\},\ \{a_0,a_1,a_2,a_3,y\}.                       \tag{2.1}
\]

The two-vertex set in (2.1) contains the shortened `x`--`q` path, and the
last set is connected through the clique on `a0,a1,a2,a3` and the edge
`a3y`.  The only adjacency in (2.1) not already supplied by the two
endpoint graphs or the six named paths is that between `{p}` and `{x,q}`;
it is the newly created edge `px`.  Thus (2.1) is a $K_7$-minor model.

If `C` instead has a neighbour in $V(P_4)-\{x\}$, perform the symmetric
terminal contraction toward `q` and contract the image of `C` into `a3`.
This creates the edge `a3q`.  Seven branch sets are

\[
 \{b_0\},\ \{b_1\},\ \{b_2\},\ \{r\},\ \{q\},\
 \{a_3,p\},\ \{a_0,a_1,a_2,x,y\}.                       \tag{2.2}
\]

Here the shortened `a3`--`p` path lies in the sixth set, and `a3q`
supplies its only formerly missing adjacency.  Hence (2.2) is a
$K_7$-minor model.  Every contraction used above is label-preserving on
the branch sets displayed in (2.1) or (2.2), so the models lift to `G`.
\(\square\)

## 3. Two attachment sectors

### Theorem 3.1

Assume that `G` has no $K_7$ minor.  Then one of the following two sets
contains every neighbour of `C` on the linkage:

\[
\begin{aligned}
 \mathcal S_5&=V(P_5)\cup\{a_3,x,b_0,b_1,b_2\},          \tag{3.1}\\
 \mathcal S_{012}&=V(P_0\cup P_1\cup P_2)
                         \cup\{a_3,x,y\}.                \tag{3.2}
\end{aligned}
\]

More precisely:

1. if `C` has a neighbour in $V(P_5)-\{y\}$, then
   $N_\Sigma(C)\subseteq\mathcal S_5$;
2. otherwise $N_\Sigma(C)\subseteq\mathcal S_{012}$.

#### Proof

Lemma 2.1 excludes `p`, `q`, and all internal vertices of `P3,P4` from
$N_\Sigma(C)$.

Suppose `C` has a neighbour $u\in V(P_5)-\{y\}$.  If it also had a
neighbour $v\in V(P_i)-\{b_i\}$ for some $i\in\{0,1,2\}$, take a shortest
`u`--`v` path through the connected graph `C`, including its two attachment
edges.  Its internal vertices lie in `C`, so it is a clean augmenting path
from `P5-y` to `Pi-bi`.  The explicit clean-augmentation theorem gives a
$K_7$ minor, a contradiction.  Therefore the only possible neighbour of
`C` on `Pi` is `bi`, for each $i\le2$.  Together with Lemma 2.1, this is
exactly (3.1).

If `C` has no neighbour in $V(P_5)-\{y\}$, its only possible neighbour on
`P5` is `y`.  Lemma 2.1 again removes `P3-a3` and `P4-x`.  All remaining
linkage vertices are precisely those in (3.2).  \(\square\)

The clean-augmentation input is Theorem 2.1 of
[`hc7_disjoint_k6minus_support6_bridge_augmentation.md`](../results/hc7_disjoint_k6minus_support6_bridge_augmentation.md).

### Corollary 3.2 (canonical first--last interval)

If $|N_\Sigma(C)|\ge8$, then:

- in outcome 1 of Theorem 3.1, `C` has at least three distinct neighbours
  on `P5`, at least two of which are internal vertices of `P5`; and
- in outcome 2, `C` has at least five distinct neighbours in
  $P_0\cup P_1\cup P_2$, at least two of which are internal vertices of
  those three paths; moreover at least one of the paths has two neighbours
  of `C`.

Consequently each attachment sector contains a nontrivial first--last
interval on at least one named path: on `P5` in outcome 1, and on a member
of `P0,P1,P2` having at least two neighbours of `C` in outcome 2.

#### Proof

The seven-endpoint attachment decoder says that a connected off-linkage
subgraph adjacent to `a3,x` and five further normalized endpoints gives a
$K_7$ minor.  Thus, in the present $K_7$-minor-free graph, `C` has at most
six normalized endpoint neighbours in total.  At order at least eight it
therefore has at least two neighbours in path interiors.

The set $\mathcal S_5-V(P_5)$ has order five, while
$\mathcal S_{012}-V(P_0\cup P_1\cup P_2)$ has order three.  Subtract from
the eight distinct linkage neighbours.  Theorem 3.1 places every internal
neighbour on `P5` in the first case and on `P0,P1,P2` in the second.  The
pigeonhole principle gives the last assertion.  \(\square\)

The endpoint input is Theorem 2.1 of
[`hc7_disjoint_k6minus_seven_attachment_decoder.md`](../results/hc7_disjoint_k6minus_seven_attachment_decoder.md).

## 4. Consequence for the proposed two-component composition

Combine this theorem with the independently audited leaf-block separation
lemma.  If any leaf-block interior of either exterior component has exactly
six linkage neighbours, it already gives an actual order-seven separation
whose closed opposite shore contains the six named paths.  Otherwise every
leaf-block interior has at least seven linkage neighbours.

For the component containing the residual `a3`--`x` path, Lemma 2.1 and
Theorem 3.1 remove arbitrary six-path attachment geometry: all remaining
contacts lie in one of the two sets (3.1)--(3.2), and at order at least
eight they determine a first--last interval on one path.  What remains
unproved is the composition step: a distinct component containing a
`y`--`z` path, $z\in\{p,q,r\}$, must either cross that interval in a
closing order or force an order-seven boundary around it.  The present
theorem establishes the needed concentration but does not assume that
crossing conclusion.
