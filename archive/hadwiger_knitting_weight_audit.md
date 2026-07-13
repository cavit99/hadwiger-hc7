# Audit and strengthening of the eight-knitting adhesion theorem

## 1. Audit verdict

The statements and proofs in
hadwiger_small_nonclique_knitted_adhesion.md are valid. The only wording
issue originally present in Corollary 3.3 has already been corrected:
the conclusion is that a relative separator exists; only the
*absence* of such a separator would knit both sides.

Here are the points which are easy to overlook.

1. **Existential cross-edges suffice.** If an edge witnessing adjacency
   of two blocks has ends in \(P_i\) and \(P_j\), then its ends lie in
   the disjoint connected sets \(C_i^Z,C_j^Z\). Contracting those sets
   therefore turns that particular edge into \(z_i z_j\). Complete
   bipartite adjacency between blocks is neither assumed nor needed.
   The same observation applies to a nonsingleton block and a singleton
   block.

2. **The contractions give proper minors.** If some vertex of the open
   side is not in a contracted set, it is deleted. Otherwise an open-side
   vertex lies in one of the contracted sets. Since that set contains a
   nonsingleton independent boundary block and is connected, it contains
   an edge and its contraction strictly decreases the number of vertices.
   When there are no nonsingleton blocks, the nonempty open side is simply
   deleted.

3. **The boundary state is exact.** The contracted block vertices and
   the retained singleton vertices form a clique. Hence they receive
   pairwise different colours. Expansion makes precisely the vertices
   within each prescribed independent block equal, so a palette
   permutation aligns the two side-colourings block by block.

4. **The greedy partition is valid.** If \(P_i\) is maximal independent
   in the remainder in which a later block \(P_j\) still lies, every
   vertex of \(P_j\) has a neighbour in \(P_i\). Thus every pair of
   blocks has a witnessing edge. If all greedy blocks are singletons,
   this same observation shows that the boundary graph is a clique.

5. **The \(+1\) is genuine.** After deleting the singleton set \(R\),
   an open-side vertex has degree at least \(t-|R|\). The knittedness
   theorem may consequently be applied with
   \(k_*=t-|R|+1\), giving the strict condition
   \(8|T|+|R|<t+1\). This uses the audited stronger fact
   \(\delta(G)\ge t\), not merely ordinary \(t\)-criticality.

6. **The lifted relative separator is a genuine smaller cut.** Write a
   proper relative separation as \((C,D)\), with the terminal set in
   \(C\), far side \(D-C\ne\varnothing\), and separator \(U=C\cap D\).
   In Theorem 3.4, \(D-C\) and the opposite original open side are
   nonempty and disjoint from \(U\cup R\). The original separation
   forbids an edge from the former side to the opposite open side, while
   the relative separation forbids an edge to \(C-D\); all vertices
   deleted in forming the relative graph lie in \(R\). Thus every escape
   meets \(U\cup R\), whose order is strictly less than \(|S|\).

The convention that a relative separation has a nonempty far side is
essential. It is also the only interpretation under which the hypothesis
of the Kawarabayashi--Yu theorem is useful. All applications in the
audited note have a nonempty open side \(H-X\). This also avoids the
degenerate \(H=X\) boundary case, in which the outside-degree hypothesis
would be vacuous and must not be used to infer knittedness.

## 2. A sharper exposure cost

The term \(|R|\) in the eight-knitting weight is a worst-case estimate.
For a component \(D\) of \(G-S\) and \(K\subseteq S\), define its
**exposure** to \(K\) by

\[
 e_D(K)=\max_{x\in D}|N_G(x)\cap K|.
\]

Deleting \(K\) costs only \(e_D(K)\) in the minimum-degree hypothesis,
not \(|K|\). The following theorem also assigns different costs to
different nonsingleton blocks: a block connected through its own full
shore costs no knitting terminals, while a block left for the knitted
shore costs eight units per vertex.

### Theorem 2.1 (hybrid full-shore/knitting theorem)

Let \(S\) be a minimum vertex cut of the proper-minor-minimal
counterexample \(G\), and let

\[
 \Pi=\{P_1,\ldots,P_q\}\mathbin{\dot\cup}
       \{\{x\}:x\in R\}
\]

be an independent-set partition of \(S\) whose block-adjacency quotient
is complete. Let \({\cal D}\) be the set of components of \(G-S\).

Choose \(I\subseteq[q]\), put

\[
 F=\bigcup_{i\in I}P_i,\qquad
 U=\bigcup_{i\notin I}P_i,\qquad K=S-U=R\cup F,
\]

and suppose \(U\ne\varnothing\). If there are \(2(|I|+1)\) distinct
components

\[
 A_0,A_i\ (i\in I),\qquad B_0,B_i\ (i\in I)
\]

of \(G-S\) such that

\[
 8|U|+\max\{e_{A_0}(K),e_{B_0}(K)\}<t+1,             \tag{2.1}
\]

then \(G\) is \((t-1)\)-colourable, a contradiction.

If \(U=\varnothing\), the same conclusion holds whenever \(G-S\) has at
least \(2q\) components.

#### Proof

Because \(S\) is a minimum cut, every vertex of \(S\) has a neighbour in
every component of \(G-S\). Indeed, if \(s\in S\) had no neighbour in a
component \(D\), then \(S-\{s\}\) would still separate \(D\) from any
other component of \(G-S\).

Consider

\[
 H_A=G[A_0\cup U].
\]

Every vertex \(x\in A_0\) has all its neighbours in \(A_0\cup S\), and
therefore

\[
 d_{H_A}(x)
 =d_G(x)-|N_G(x)\cap K|
 \ge t-e_{A_0}(K).                                  \tag{2.2}
\]

There is no proper separation of \((H_A,U)\) of order below \(|U|\).
For if \((C,D)\) were such a separation, oriented with \(U\subseteq C\),
far side \(D-C\ne\varnothing\), and separator \(W=C\cap D\), then
\(W\cup K\) would separate \(D-C\) from any other component of \(G-S\).
Its order would satisfy

\[
 |W\cup K|<|U|+|K|=|S|,
\]

contrary to the minimality of \(S\).

Set \(k_A=t-e_{A_0}(K)+1\). Inequality (2.1) gives
\(|U|<k_A/8\), and (2.2) is exactly the required degree bound
\(k_A-1\). Kawarabayashi--Yu knittedness now realizes, by pairwise
disjoint connected subgraphs in \(A_0\cup U\), all blocks \(P_j\) with
\(j\notin I\).

For every \(i\in I\), the set \(A_i\cup P_i\) is connected, by the full
attachment observation in the first paragraph. These \(|I|\) connected
sets are mutually disjoint and are disjoint from the knitted family in
\(A_0\cup U\). Consequently the \(A\)-collection realizes every
nonsingleton block of \(\Pi\). The same argument, using \(B_0,B_i\),
gives a disjoint \(B\)-collection.

Group the components containing the \(A\)-collection on one side of a
separation of \(G\), and put the components containing the \(B\)-collection
on the other side (assign all unused components arbitrarily). Lemma 2.1
of the audited note applies and glues the two exact boundary states, a
contradiction.

If \(U=\varnothing\), assign a distinct full component to every \(P_i\)
on each side. The connected sets \(D_i\cup P_i\) directly supply both
families, so the same gluing lemma applies. \(\square\)

### Corollary 2.2 (component-count obstruction)

Under the hypotheses of Theorem 2.1, if \(G-S\) has \(m\) components,
then every complete-quotient independent partition of \(G[S]\) with
\(q\) nonsingleton blocks satisfies

\[
 m\le 2q-1.                                         \tag{2.3}
\]

For \(q=0\), the boundary is a clique and exact-state gluing already
gives a contradiction.

#### Proof

If \(m\ge2q\), use the \(U=\varnothing\) conclusion of Theorem 2.1.
\(\square\)

### Corollary 2.3 (component-weighted obstruction)

Suppose \(U\ne\varnothing\) and \(m\ge2(|I|+1)\). Among the components
not assigned to the blocks indexed by \(I\), let \(a,b\) be two with
smallest exposure to \(K=S-U\). Then necessarily

\[
 8|U|+\max\{e_a(K),e_b(K)\}\ge t+1.                \tag{2.4}
\]

In particular, since exposure is at most \(|K|\), a purely boundary-size
version is

\[
 |S|+7|U|\ge t+1.                                  \tag{2.5}
\]

Thus up to \(\lfloor m/2\rfloor-1\) nonsingleton blocks may be paid for
at unit cost per vertex by assigning them full components; only the
vertices in the remaining blocks pay the eight-unit knitting cost.

### Theorem 2.4 (preconnected-block weighted knitting)

There is also a version which does not require separate components.
Return to an arbitrary proper separation \((A,B)\) with boundary \(S\)
and a complete-quotient partition \(\Pi\). Choose \(I\subseteq[q]\), set

\[
 U=\bigcup_{i\notin I}P_i,
\]

and suppose that, for each \(Z\in\{A,B\}\), there are pairwise disjoint
connected subgraphs \(F_i^Z\subseteq G[Z-R]\), \(i\in I\), such that
\(P_i\subseteq V(F_i^Z)\) and no \(F_i^Z\) meets \(U\). Put

\[
 W_Z=R\cup\bigcup_{i\in I}V(F_i^Z),\qquad
 H_Z=G[Z]-W_Z,
\]

and define the deletion loss

\[
 \Delta_Z=
 \max_{x\in V(H_Z)-U}\bigl(d_G(x)-d_{H_Z}(x)\bigr).
\]

If \(U\ne\varnothing\), neither \((H_A,U)\) nor \((H_B,U)\) has a
proper relative separation of order below \(|U|\), and
\(V(H_Z)-U\ne\varnothing\) for \(Z=A,B\), and

\[
 8|U|+\max\{\Delta_A,\Delta_B\}<t+1,                \tag{2.6}
\]

then \(G\) is \((t-1)\)-colourable. If \(U=\varnothing\), the fixed
witnesses alone give the same conclusion.

#### Proof

Every vertex of \(H_Z-U\) lies in \(Z-S\), so it has degree at least
\(t-\Delta_Z\) in \(H_Z\). With
\(k_Z=t-\Delta_Z+1\), (2.6) and the absence of a small relative
separation let Kawarabayashi--Yu knit the blocks indexed outside \(I\)
inside \(H_Z\). Those connected subgraphs avoid every fixed witness by
construction. Adjoin the fixed witnesses \(F_i^Z\). On each side this
is a pairwise disjoint realization of every nonsingleton block, and the
exact multipartite gluing lemma finishes. If \(U=\varnothing\), omit the
knitting step. \(\square\)

For a contact-maximal \(K_{t-1}\)-model, the inclusion-minimal
contact separator has two distinguished full shores. Theorem 2.4 makes
the remaining task precise: it is enough to peel fixed block witnesses
from each shore so that their deletion loss is small and the residual
terminal pair has no relative separator. A forced small relative
separator feeds the descent below. What is *not* currently proved is a
portal-splitting theorem guaranteeing such low-loss witnesses inside a
single shore.

## 3. Recursive strict-order separator descent

The same lifting argument does not require the starting cut to be
minimum. It gives the following useful laminar form of the obstruction.

### Proposition 3.1 (strict cut-order descent)

Let \(S\) be any vertex cut of \(G\), choose a component \(Q\) of \(G-S\),
and use the proper separation with open sides \(Q\) and
\(V(G)-(Q\cup S)\). If

\[
 \nu_8(G[S])<t+1,
\]

then \(G[S]\) is not a clique and Theorem 3.1 of the audited note yields
a vertex cut \(S'\) with \(|S'|<|S|\). Moreover, \(S'\) can be chosen as
\(W\cup R\), where \(W\) is a relative separator on one original side;
it separates a nonempty subset of that side from the opposite original
open side.

Iterating this operation terminates after at most \(|S|\) steps at a cut
\(S^*\) with

\[
 |S^*|\le |S|,\qquad \nu_8(G[S^*])\ge t+1,
\]

and the inequality in the first coordinate is strict whenever the
starting cut has weight below \(t+1\).

The new cut need not be a subset of the old cut, and successive cut
vertex sets need not be laminar.  Only their orders strictly decrease.
Accordingly, this proposition does not by itself supply a nested
tree-decomposition; that would require a separate uncrossing argument.

#### Proof

The first assertion is precisely the separator-lifting calculation in
Theorem 3.4, without invoking minimum-cut minimality. If the new cut
again has weight below \(t+1\), repeat. Its order strictly decreases at
every repetition, so the process terminates. A clique boundary cannot
be a stopping obstruction, since the singleton exact-state gluing lemma
forbids a proper clique separation. Hence the terminal cut has weight at
least \(t+1\). \(\square\)

## 4. Exact remaining limitation

Theorems 2.1 and 3.1 are stronger than the unweighted invariant, but they
do not by themselves solve the uniform model-meeting problem. A minimum
cut may have only two components, every nontrivial block may have to be
knitted, and every component may expose all singleton/protected boundary
vertices at a common internal vertex. In that worst cell the cost returns
to \(8|T|+|R|\), and the factor-eight barrier remains. Further progress
requires either a knittedness theorem sensitive to the number of blocks
rather than the number of terminals, or a rooted-model absorption step
which supplies fixed block realizations without consuming separate full
components.
