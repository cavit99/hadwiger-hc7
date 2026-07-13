# A small-nonclique contact-or-separator theorem

## 1. Setting

Let \(t\ge 7\) be the least parameter at which Hadwiger's Conjecture
fails, and let \(G\) be a proper-minor-minimal counterexample. Put
\(r=t-1\). We use the audited consequences

\[
 \chi(G)=t,\qquad \delta(G)\ge t,
\]

and the fact that every proper minor of \(G\) is \(r\)-colourable.

The purpose of this note is to extend the one-block gluing theorem in
hadwiger_uniform_contact_oneblock_adhesion.md. Several independent
blocks can be handled at once, provided that the total nontrivial part
of the adhesion is small enough for the knittedness theorem.

We use the following theorem of Kawarabayashi and Yu. If
\(X\subseteq V(H)\), \(|X|=\ell<k/8\), every vertex of \(H-X\) has
degree at least \(k-1\), and there is no separation of \((H,X)\) of
order less than \(\ell\), then \((H,X)\) is knitted. Thus every
partition of \(X\) is realized by pairwise disjoint connected subgraphs
of \(H\).

Throughout this note, a separation \((C,D)\) of \((H,X)\) is oriented
with \(X\subseteq C\) and has a nonempty far side \(D-C\). This is the
proper relative-separation convention in the knittedness theorem; without
it the empty far side would make the hypothesis vacuous.

## 2. Exact multipartite gluing

### Lemma 2.1

Let \((A,B)\) be a separation of \(G\), with

\[
 S=A\cap B,\qquad A-B\ne\varnothing,\qquad B-A\ne\varnothing.
\]

Suppose

\[
 \Pi=\{P_1,\ldots,P_q\}\mathbin{\dot\cup}
      \bigl\{\{x\}:x\in R\bigr\}                    \tag{2.1}
\]

is a partition of \(S\) such that every part is independent and the
**block-adjacency quotient is complete**: for every two distinct parts
of \(\Pi\), at least one edge of \(G[S]\) joins the two parts. Put

\[
 T=P_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}P_q,
\]

where the \(P_i\) are the nonsingleton parts; \(R=S-T\).

Assume that, on each side \(Z\in\{A,B\}\), there are pairwise disjoint
connected subgraphs

\[
 C^Z_1,\ldots,C^Z_q\subseteq G[Z-R]
 \quad\text{with}\quad P_i\subseteq V(C^Z_i).       \tag{2.2}
\]

Then \(G\) is \(r\)-colourable.

#### Proof

For the \(A\)-side realization, contract every \(C^A_i\) to a vertex
\(z_i\), delete all remaining vertices of \(A-S\), and retain \(G[B]\).
This is a proper minor \(M_B\) of \(G\), hence it has an
\(r\)-colouring.

The vertices

\[
 \{z_1,\ldots,z_q\}\cup R                           \tag{2.3}
\]

form a clique in \(M_B\): at least one cross-edge between every pair of
parts was present in \(G[S]\), and contraction turns it into the
corresponding edge of (2.3). Expand the boundary by giving every vertex of \(P_i\) the
colour of \(z_i\), while retaining the colours on \(R\). This is a
proper colouring of \(G[B]\). Indeed, \(P_i\) is independent, and
every edge from \(P_i\) to \(B-S\) became an edge from \(z_i\) after
the contraction. The clique (2.3) also shows that the equality
partition induced on \(S\) is *exactly* \(\Pi\).

The symmetric construction using the \(B\)-side realization gives an
\(r\)-colouring of \(G[A]\) with the same exact boundary partition.
Permute the palette on one side so that corresponding blocks agree.
There are no edges from \(A-S\) to \(B-S\), so the two colourings glue
to an \(r\)-colouring of \(G\), a contradiction. (The clique (2.3) in
the \(r\)-coloured proper minor also shows \(q+|R|\le r\), so no hidden
palette-size assumption is needed.)
\(\square\)

## 3. Knittedness forces a small relative separator

### Theorem 3.1 (small-nonclique contact-or-separator)

In the setting of Lemma 2.1, suppose that (2.1) is an independent-set
partition with complete block-adjacency quotient and \(T\ne\varnothing\).
If

\[
 |T|<\frac{t-|R|+1}{8},                             \tag{3.1}
\]

then at least one of the two pairs

\[
 \bigl(G[A]-R,T\bigr),\qquad
 \bigl(G[B]-R,T\bigr)                               \tag{3.2}
\]

has a separation of order less than \(|T|\).

Equivalently, if neither side has such a relative separator, then \(G\)
is \(r\)-colourable.

#### Proof

Set

\[
 k_*=t-|R|+1,\qquad \ell=|T|.
\]

Consider \(H_A=G[A]-R\). Every vertex \(u\in A-S\) has all its
neighbours in \(A\), because \((A,B)\) is a separation. Deleting \(R\)
therefore gives

\[
 d_{H_A}(u)\ge d_G(u)-|R|\ge t-|R|=k_*-1.          \tag{3.3}
\]

If \((H_A,T)\) has no separation of order below \(\ell\), then (3.1),
(3.3), and the Kawarabayashi--Yu theorem show that \((H_A,T)\) is
knitted. Apply knittedness to the partition
\(T=P_1\dot\cup\cdots\dot\cup P_q\); it supplies the \(A\)-side
subgraphs in (2.2). Exactly the same argument applies to
\(H_B=G[B]-R\).

If neither pair in (3.2) has a separation of order below \(\ell\), both
families (2.2) exist, and Lemma 2.1 colours \(G\), a contradiction.
Thus at least one of the stated relative separators exists.
\(\square\)

### Corollary 3.2

If \(R=\varnothing\), every adhesion admitting a complete-quotient
independent partition on fewer than \((t+1)/8\) vertices is either
colour-gluable or has a relative separator smaller than the adhesion on
at least one side.

More generally, writing the numerical hypothesis without fractions,

\[
 8|T|+|R|<t+1,                                      \tag{3.4}
\]

shows that an arbitrary clique \(R\) may be retained as singleton
blocks at a cost of only one unit of the degree budget per vertex.

### Corollary 3.3 (arbitrary adhesion and knitting weight)

Every graph \(J\) has an independent-set partition with complete
block-adjacency quotient. Indeed, choose \(P_1\) maximal independent in
\(J\), then \(P_2\) maximal independent in
\(J-P_1\), and continue. If \(i<j\), maximality of \(P_i\) in the graph
which still contained \(P_j\) implies that every vertex of \(P_j\) has
a neighbour in \(P_i\). In particular the two blocks are adjacent.

Define the **eight-knitting weight**

\[
 \nu_8(J)=\min_{\Pi}
 \left(
  8\left|\bigcup_{\substack{P\in\Pi\\|P|\ge2}}P\right|
  +\left|\{P\in\Pi:|P|=1\}\right|
 \right),                                           \tag{3.5}
\]

where the minimum is over all independent-set partitions with complete
block-adjacency quotient.

For an arbitrary adhesion \(S\) in a minor-minimal counterexample,

\[
 \nu_8(G[S])<t+1                                   \tag{3.6}
\]

has the following consequence. If a partition attaining (3.5) has a
nonempty union \(T\) of nonsingleton blocks, it forces a relative
separator, on at least one open side, whose order is smaller than
\(|T|\). If \(T=\varnothing\), then \(G[S]\) is a clique and the
vacuous realizations in Lemma 2.1 already glue the two proper-minor
colourings, so such an adhesion cannot occur at all. Equivalently, when
\(T\ne\varnothing\), if neither side has the stated relative separator,
Theorem 3.1 knits the attaining partition on both sides and colours
\(G\).

In particular, taking the greedy partition proves the assertion without
any multipartite hypothesis. The invariant \(\nu_8\) records how much of
the boundary is genuinely nonclique: singleton blocks cost one unit,
while vertices which must be knitted together cost eight.

### Theorem 3.4 (weighted minimum-cut obstruction)

If \(S\) is a minimum vertex cut of \(G\), then

\[
 \nu_8(G[S])\ge t+1.                                \tag{3.7}
\]

Consequently

\[
 \kappa(G)\ge\left\lceil\frac{t+1}{8}\right\rceil.  \tag{3.8}
\]

#### Proof

Let \((A,B)\) be the separation obtained by taking one component of
\(G-S\) on one side and all remaining components on the other. Both
open sides are nonempty. Choose a partition \(\Pi\) attaining (3.5),
and retain the notation \(T,R\).

Suppose first that \(T=\varnothing\). Then all blocks of \(\Pi\) are
singletons and completeness of the block quotient says that \(G[S]\)
is a clique. The vacuous connected realizations in Lemma 2.1 give
matching singleton equality states on both sides and colour \(G\), a
contradiction.

Now suppose \(T\ne\varnothing\) and, contrary to (3.7), that
\(\nu_8(G[S])<t+1\). This is exactly

\[
 8|T|+|R|<t+1,
\]

so Theorem 3.1 gives, after possibly interchanging \(A,B\), a separation
\((C,D)\) of

\[
 H=G[A]-R
\]

of order \(|U|<|T|\), where \(U=C\cap D\), \(T\subseteq C\), and
\(D-C\ne\varnothing\). In the original graph, every neighbour of
\(D-C\) outside \(H\) lies in \(R\): the original separation forbids
edges to \(B-A\), and the relative separation forbids edges to
\(C-D\). Hence

\[
 U\cup R
\]

separates the nonempty set \(D-C\) from the nonempty set \(B-A\).
But

\[
 |U\cup R|<|T|+|R|=|S|,
\]

contradicting the minimality of the vertex cut \(S\). This proves
(3.7).

Finally, the greedy complete-quotient partition from Corollary 3.3 has
weight at most \(8|S|\). Thus

\[
 t+1\le\nu_8(G[S])\le8|S|,
\]

and minimizing over all vertex cuts gives (3.8).
\(\square\)

The numerical improvement over the unweighted knittedness argument is
strict when \(t\) is divisible by eight. More importantly, (3.7)
retains the boundary structure: a minimum cut with many singleton blocks
must be larger than the crude connectivity estimate, because those
blocks consume only one unit rather than eight in the knitting budget.

### Corollary 3.5 (universal vertices in a minimum cut)

If a minimum cut \(S\) has \(u\) vertices which are universal in
\(G[S]\), then

\[
 8|S|-7u\ge t+1.                                    \tag{3.9}
\]

#### Proof

Put each of the \(u\) universal vertices in a singleton block, and
greedily partition the remaining vertices into maximal independent sets.
The quotient is complete: the universal singleton blocks see every other
block, and the greedy argument handles pairs of nonsingleton blocks.
Its weight is at most

\[
 u+8(|S|-u)=8|S|-7u.
\]

Apply (3.7).
\(\square\)

## 4. Structural significance

Theorem 3.1 and Corollary 3.3 are genuine contact-or-separator
statements. They do not enumerate a boundary graph, assume it is
multipartite, or fix the value of \(t\). They say that a
counterexample-derived adhesion with small knitting weight cannot remain
highly linked on both sides: knittedness would force matching exact
boundary states and hence a colouring.

The theorem also isolates the quantitative obstruction to a uniform
proof. When the nontrivial core has order at least about \(t/8\), the
currently known connectivity/knittedness bound no longer applies.
Thus the remaining general mechanism must either shrink the core by
rooted-model absorption, or uncross the forced relative separators and
propagate exact states along the resulting decorated decomposition.
This is precisely the label-free version of the portal/web phenomenon
found in the \(C_6\dot\cup K_1\) laboratory.
