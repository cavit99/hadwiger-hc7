# Rooted clique-model lobe exchange

## 1. A label-preserving exchange lemma

Let \(\mathcal B=(B_1,\ldots,B_m)\) be a clique-minor model in a
graph \(G\): the bags are pairwise disjoint and connected, and every
two bags are adjacent.  Suppose that each bag \(B_i\) has a prescribed
root \(r_i\in B_i\).

### Lemma 1.1 (root-free lobe exchange)

Fix distinct indices \(i,j\).  Let \(q\in B_i\), and let \(U\) be a
component of \(G[B_i]-q\).  Assume

1. \(r_i\notin U\);
2. \(U\) is adjacent to \(B_j\); and
3. \(U\) is anticomplete to every \(B_\ell\) with
   \(\ell\notin\{i,j\}\).

Then

\[
 B_i'=B_i-U,\qquad B_j'=B_j\cup U,\qquad
 B_\ell'=B_\ell\quad(\ell\notin\{i,j\})                 \tag{1.1}
\]

is another rooted \(K_m\)-model with the same prescribed root in every
bag.  If the original model was spanning, so is the new one.

#### Proof

The graph \(G[B_i-U]\) is connected: it consists of \(q\) together
with all components of \(G[B_i]-q\) other than \(U\), and every such
component has an edge to \(q\).  The graph \(G[B_j\cup U]\) is
connected by hypothesis 2.  The two new bags are adjacent because
connectedness of \(B_i\) gives an edge from \(U\) to \(q\).

For \(\ell\notin\{i,j\}\), the old \(B_i\)-\(B_\ell\) adjacency
cannot have its \(B_i\)-endpoint in \(U\), by hypothesis 3, and hence
survives from \(B_i'\).  All adjacencies incident with \(B_j\) survive
after enlarging that bag, and all other bag adjacencies are unchanged.
Hypothesis 1 leaves \(r_i\) in \(B_i'\); no root of another bag lies
in \(U\), because the old bags were disjoint.  Thus all labels and
roots are preserved.  Equation (1.1) repartitions the same union, so
spanning is preserved. \(\square\)

### Corollary 1.2 (minimal rooted models have no transferable lobes)

Let \(I\subseteq\{1,\ldots,m\}\), and let \(\mathfrak M\) be a
nonempty finite family of rooted spanning \(K_m\)-models which is
closed under the exchange in Lemma 1.1 whenever its hypotheses hold.
Choose a member of \(\mathfrak M\) minimizing

\[
                         \sum_{i\in I}|B_i|.                \tag{1.2}
\]

If \(i\in I\), \(j\notin I\), and \(U\subseteq B_i\) satisfies
Lemma 1.1, then no such \(U\) exists.

#### Proof

The exchange decreases (1.2) by \(|U|\) and remains in
\(\mathfrak M\) by exchange-closure. \(\square\)

The exchange has an immediate connected/co-connected extension.  The
set \(U\) may be replaced by any nonempty \(X\subset B_i\) such that
\(G[X]\) and \(G[B_i-X]\) are connected, \(r_i\notin X\), \(X\) is
adjacent to \(B_j\), and \(X\) is anticomplete to all other bags.  The
same proof applies, using an \(X\)-\((B_i-X)\) edge in place of the
edge to \(q\).  A model potential may only be used after checking that
the optimized family is closed under the relevant exchange.

## 2. Application to the degree-nine pure-Moser lock

Use the notation and hypotheses of
`hadwiger_degree9_protected_portal_peel.md`.  Thus

\[
                         L_6,L_0,R_5,R_0                    \tag{2.1}
\]

is a spanning exterior-rooted \(K_4\)-model in the balanced lock,
\(6\in L_6\), \(5\in R_5\), \(K\) is the root component of
\(L_6-6\), and in the same-bag alternative

\[
 K\not\sim R_5,R_0,\qquad A=N_{L_0}(K).                    \tag{2.2}
\]

First choose (2.1), among **all** spanning balanced models with these
four exterior roots and with \(6,5\) in their indicated bags, to minimize

\[
                         |L_0|+|R_0|.                       \tag{2.3}
\]

This unrestricted balanced family is exchange-closed: a root-free
lobe move preserves the roots, types, spanning property, and ownership
of \(5,6\).  Assume now that this globally minimal model satisfies the
same-bag alternative (2.2).  Let \(q\in L_0\) be the bottleneck from
Corollary 4.5 of the cited note, and let \(\mathcal A\) be the
components of \(L_0-q\) meeting \(A-\{q\}\).

### Theorem 2.1 (minimal-model root trap)

In a \(K_7\)-minor-free graph, \(q\) is not the exterior root of
\(L_0\), and \(\mathcal A\) consists of one
component, and that component contains the exterior root of \(L_0\).
Equivalently, all portals in \(A-\{q\}\) are trapped in the unique
root-bearing \(q\)-lobe.

#### Proof

Every \(U\in\mathcal A\) is adjacent to \(K\).  By item 1 of Theorem
4.7 in the cited note, \(U\) contains no vertex adjacent to either
\(R_5\) or \(R_0\).  Hence, if \(U\) does not contain the exterior
root of \(L_0\), Lemma 1.1 applies with

\[
            B_i=L_0,\qquad B_j=L_6,qquad U=U.              \tag{2.4}
\]

Indeed, the only two other bags are \(R_5,R_0\), and \(U\) is
anticomplete to both.  The exchange moves \(U\) into \(L_6\), keeps
both outer vertices \(6,5\) in their old bags, keeps all four exterior
roots in their labelled bags, and preserves spanning and the balanced
left/right types.  It therefore gives another model in the optimized
family, but decreases (2.3), a contradiction.

Thus every member of \(\mathcal A\) contains the unique root of
\(L_0\).  Distinct components of \(L_0-q\) are disjoint, so there is
at most one such member.  In the strict-surplus same-bag state
\(|A|\ge4\); hence \(A-\{q\}\ne\varnothing\) and \(\mathcal A\) is
nonempty.  It consequently consists of exactly one root-bearing
component, which also shows that \(q\) itself is not the root.
\(\square\)

Write \(r_0\) for the \(L_0\)-root and \(U\) for this unique
root-bearing component.

### Theorem 2.2 (ordered portal spine)

Assume the strict-surplus state \(|A|\ge4\).

Every vertex

\[
                         a\in (A\cap U)-\{r_0\}             \tag{2.5}
\]

separates \(r_0\) from \(q\) in \(G[L_0]\).  Consequently all
vertices in (2.5) lie, in one fixed linear order, on every
\(r_0\)-to-\(q\) path.  Since \(|A|\ge4\), at least two distinct
non-root portals occur on this ordered cutvertex spine.

#### Proof

Suppose that some \(a\) in (2.5) does not separate \(r_0\) from
\(q\).  In \(L_0-a\), let \(C\) be the component containing both
\(r_0\) and \(q\), and put

\[
             X=\{a\}\cup\bigl(V(L_0)-V(C)-\{a\}\bigr).     \tag{2.6}
\]

Every component of \(L_0-a\) other than \(C\) has a neighbour at
\(a\), so \(G[X]\) is connected; its complement \(C\) is connected.
The set \(X\) contains \(a\), hence is adjacent to \(K\), and excludes
the root \(r_0\).  Moreover, because \(q\in C\), every vertex of
\(X\) lies in the component \(U\) of \(L_0-q\).  Item 1 of Theorem
4.7 makes \(U\), and hence \(X\), anticomplete to \(R_5\cup R_0\).
The connected/co-connected exchange therefore moves \(X\) from
\(L_0\) to \(L_6\), contradicting the global minimality of (2.3).

Thus every vertex in (2.5) separates \(r_0,q\).  The cutvertices that
separate two fixed vertices occur on the unique path between their
blocks in the block-cut tree, and are therefore linearly ordered; every
\(r_0q\)-path meets them in that order.  Finally all members of
\(A-\{q\}\) lie in \(U\).  Excluding the two possible vertices
\(q,r_0\) from a set of order at least four leaves at least two members
of (2.5). \(\square\)

The symmetric conclusion holds at the \(R_5-5\) gate after minimizing
the same potential: every symmetric same-bag portal set is trapped in
the unique root-bearing lobe of \(R_0\).

## 3. Consequence and exact limitation

Conditional on the global potential-minimizer lying in the same-bag
cell, Theorem 2.1 eliminates, for bags of arbitrary order, every ordinary
portal-transfer configuration in Theorem 4.7 of the cited note.  The
only same-bag bottleneck residue in a potential-minimal model is the
exceptional root-ownership lock of Corollary 4.8.  Theorem 2.2 then
turns that residue into an ordered portal spine with at least two
literal portal cutvertices; it is no longer an arbitrary root-bearing
lobe.

This does not itself produce a \(K_7\)-minor, nor does it prove that a
global minimizer must lie in the same-bag cell.  Moving the remaining
root-bearing spine wholesale would move the prescribed \(L_0\) root
into \(L_6\).  The exact next obstruction is therefore label ownership,
rather than contact count: one must either reroot the two left bags
simultaneously, combine the symmetric root-bearing lock, or use a
contraction-critical boundary transition.
