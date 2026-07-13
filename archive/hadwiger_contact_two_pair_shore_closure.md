# Complete closure of the two-pair contact adhesion for \(\mathrm{HC}_7\)

## General full-shore augmentation

### Lemma 1

Let \(S\subseteq V(G)\), and let \(D\subseteq V(G)-S\) be connected and
adjacent to every vertex of \(S\). Then

\[
\eta(G[S\cup D])\ge \eta(G[S])+1.                    \tag{1}
\]

#### Proof

Take a maximum clique-minor model
\((B_1,\ldots,B_m)\) in \(G[S]\). The set \(D\) is disjoint from all its
bags, connected, and adjacent to every \(B_i\), because every nonempty
bag contains a vertex of \(S\) and \(D\) touches every such vertex.
Therefore

\[
B_1,\ldots,B_m,D
\]

is a \(K_{m+1}\)-model. \(\square\)

In particular, if \(G\) has no \(K_t\)-minor, every full-shore boundary
satisfies

\[
\eta(G[S])\le t-2.                                   \tag{2}
\]

## The shore-repair lemma

Let

\[
S=\{p_1,p_2,q_1,q_2\}\mathbin{\dot\cup}R
\]

and suppose that the only nonedges of \(G[S]\) are

\[
p_1p_2,\qquad q_1q_2.
\]

The boundary graph already has a \(K_{|S|-1}\)-model:

\[
\{p_1\},\quad\{q_1\},\quad
\{r\}\ (r\in R),\quad\{p_2,q_2\}.                   \tag{3}
\]

Indeed, the last bag is connected, sees \(p_1\) through \(q_2p_1\), and
sees \(q_1\) through \(p_2q_1\); all other required boundary edges are
present.

If a connected set \(D\subseteq V(G)-S\) is adjacent to every vertex of
\(S\), Lemma 1 appends \(D\) and gives a \(K_{|S|}\)-minor. Explicitly,
the bags are

\[
\{p_1\},\quad\{q_1\},\quad
\{r\}\ (r\in R),\quad
\{p_2,q_2\},\quad D.
\]

There are \(|R|+4=|S|\) of them. If \(|S|>t\), any \(t\) bags give the
required \(K_t\)-submodel; equivalently use any \(K_{t-1}\) submodel of
(3) and append \(D\).

## Application to deficient contact

Let \(G\) be a proper-minor-minimal counterexample at parameter \(t\), let
\(v\in V(G)\), and fix a contact-maximal \(K_{t-1}\)-model in \(G-v\).
Let \(A\) be the union of its contact bags and \(C\) the connected union
of its noncontact bags.

Maximality implies that \(A\) separates \(v\) from \(C\). Choose an
inclusion-minimal separator \(S\subseteq A\). If \(D_C\) is the component
of \(G-S\) containing \(C\), every \(s\in S\) has a neighbour in \(D_C\):
otherwise \(s\) could be deleted from the separator. Thus \(D_C\) is a
connected full shore for \(S\).

Consequently, if

\[
\overline{G[S]}=2K_2\mathbin{\dot\cup}(|S|-4)K_1,
\]

then \(G\) has a \(K_{|S|}\)-minor. Therefore every such separator in a
\(K_t\)-minor-free counterexample satisfies

\[
\kappa(G)\le |S|\le t-1.                             \tag{4}
\]

For \(t=7\), Mader's theorem gives \(\kappa(G)\ge7=t\), contradicting
(4). More generally, Lemma 1 gives the uniform contact-adhesion
restriction

\[
\boxed{\eta(G[S])\le t-2}                            \tag{5}
\]

for every inclusion-minimal separator \(S\) inside the contact region.
Hence:

> No deficient-contact separator with complement \(2K_2\) plus isolated
> vertices occurs in a hypothetical \(\mathrm{HC}_7\) counterexample.

This completely eliminates the pair-pair adhesion cell. It supersedes the
earlier reduction of that cell to bilateral alternating disk webs.
