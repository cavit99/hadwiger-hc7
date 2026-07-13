# Two-component boundary states at a degree-seven vertex

This note records a strengthening of the two-exterior-component reduction.
It is a finite boundary-state lemma, not a proof of the degree-seven case.

## 1. Setup

Let \(G\) be a proper-minor-minimal counterexample to
\(\mathrm{HC}_7\), let \(d_G(v)=7\), put
\[
 N=N_G(v),\qquad G-N[v]=C_1\mathbin{\dot\cup}C_2,
 \qquad Q=\overline{G[N]}.
\]
Seven-connectivity gives \(N_G(C_i)=N\) for \(i=1,2\), and Dirac's
neighbourhood inequality gives \(\alpha(G[N])=2\).  Thus \(Q\) is
triangle-free.

For \(i\in\{1,2\}\), let \(L_i=G[N\cup C_i]\).  A proper six-colouring
of \(L_i\) partitions \(N\) into independent colour classes.  Whenever
at most six colours occur on \(N\), these non-singleton classes are
pairwise disjoint edges of \(Q\), because \(\alpha(G[N])=2\).  Let
\(\mathcal E_i\) be the family of matchings \(M\) in \(Q\) for which
some proper six-colouring of \(L_i\) has precisely the edges of \(M\)
as its two-vertex colour classes on \(N\), all other vertices of \(N\)
being singleton colour classes.

Colour names do not matter in this definition.

## 2. The boundary-state trichotomy

### Lemma 2.1

The two families \(\mathcal E_1,\mathcal E_2\) satisfy all of the
following.

1. For every \(e\in E(Q)\), the singleton matching \(\{e\}\) belongs to
   \(\mathcal E_1\cap\mathcal E_2\).
2. No matching of order at least two belongs to
   \(\mathcal E_1\cap\mathcal E_2\).
3. For every \(e\in E(Q)\) and each \(i\in\{1,2\}\), there is a
   matching \(M\in\mathcal E_i\) such that \(e\in M\) and
   \(2\le |M|\le3\).

#### Proof

Write \(e=xy\).  Contract the connected triple \(\{v,x,y\}\) to a
vertex \(q\).  Every six-colouring of the resulting proper minor expands
to a six-colouring of \(G-v\) in which \(x,y\) form the repeated pair
on \(N\) and the other five boundary vertices are rainbow.  Restriction
to either \(L_i\) proves (1).

For (2), suppose \(M\in\mathcal E_1\cap\mathcal E_2\) and \(|M|\ge2\).
Permute the colours in the two witnessing colourings so that they agree
on every vertex of \(N\); the colours absent from \(N\) can be aligned
arbitrarily.  Since \(C_1,C_2\) are distinct components of
\(G-N[v]\), the two colourings then glue to a proper six-colouring of
\(G-v\).  A matching of order at least two uses at most five colours on
the seven vertices of \(N\).  Giving \(v\) a colour absent from \(N\)
six-colours \(G\), a contradiction.

For (3), fix \(i\) and let \(j\ne i\).  In addition to contracting
\(\{v,x,y\}\) to \(q\), contract the connected component \(C_j\) to a
vertex \(h\).  These are disjoint branch sets of a proper minor.  The
vertices \(q,h\) are adjacent, because \(C_j\) has a neighbour at
\(x\) (and at \(y\)); and each of the five vertices
\(U=N-\{x,y\}\) is adjacent to both \(q\) and \(h\).  In a proper
six-colouring, therefore, \(q,h\) have distinct colours and \(U\) uses
at most the other four colours.

Delete \(h\), restore \(x,y\) with the colour of \(q\), and retain the
colouring on \(C_i\).  This is a proper six-colouring of \(L_i\).
The pair \(xy\) is one two-vertex colour class.  Among the other five
boundary vertices at least one further colour repeats.  No colour occurs
three times on \(N\), since every colour class in \(G[N]\) has order at
most two.  Hence the boundary classes give a matching \(M\) containing
\(xy\), of order two or three.  This proves (3). \(\square\)

This formulation separates the gluing obstruction from the particular
Kempe paths used to witness it.  An exclusive bichromatic support for an
edge is one mechanism that puts the corresponding two-edge matching into
exactly one of the two families.

## 3. Why the three set-system conditions do not yet contradict each other

In the audited two-component cell, \(G[N]\) is either the Moser spindle
\(M\), with
\[
 E(M)=\{ab,ac,bc,bp,cp,ad,ae,de,dq,eq,pq\},
\]
or \(M+bd\).  The abstract requirements of Lemma 2.1 admit disjoint
covers by larger matchings in both cases.

For \(G[N]=M\), the following two disjoint collections of matchings each
cover every edge of \(Q\):
\[
\begin{aligned}
 \mathcal F_1={}&\{\{ap,bd\},\{aq,ce\},
                  \{be,cq,dp\},\{bq,cd,ep\}\},\\
 \mathcal F_2={}&\{\{ap,be\},\{aq,cd\},
                  \{bd,cq,ep\},\{bq,ce,dp\}\}.
\end{aligned}
\]
For \(G[N]=M+bd\), two such collections are
\[
\begin{aligned}
 \mathcal F_1={}&\{\{ap,be,cq\},\{aq,ce,dp\},
                  \{bq,cd,ep\}\},\\
 \mathcal F_2={}&\{\{ap,bq,ce\},\{aq,cd,ep\},
                  \{be,cq,dp\}\}.
\end{aligned}
\]
Every displayed set is a matching in the appropriate complement, the
two collections in each line are disjoint, and direct inspection shows
that each collection covers every complement edge.

Consequently, Lemma 2.1 alone cannot prove that
\(\mathcal E_1\cap\mathcal E_2\) contains a larger matching.  A closing
argument must use an additional closure property of boundary colourings,
such as a rigorously justified Kempe transition between the displayed
matching states, or use the internal graph structure of the two exterior
components.  Merely counting the larger states or observing that both
families cover every complement edge is insufficient.

## 4. Exact next question

The finite target is now:

> Prove that extension families arising from the two sides of a
> seven-contraction-critical graph cannot realize disjoint larger-matching
> covers of the forms above, while containing every singleton state.

The word "arising" is essential.  Arbitrary set families do realize all
three conclusions of Lemma 2.1.  What remains to be extracted is a graph-
colouring closure law linking a larger boundary matching to the singleton
states obtained by splitting one of its pairs.
