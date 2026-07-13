# Linkage transport removes every nonsingleton exact-cut descendant

## 1. Statement

Let \(G\) be seven-connected and let

\[
 B=\{h,1,2,r,a,b,c\},\qquad
 P=\{h,c\},\quad Q=\{r,a\},\quad R=\{1,2,b\}.
\]

Assume that \(G[B]\) contains the two cliques
\(\{h,1,2,r\}\cong K_4\), \(\{a,b,c\}\cong K_3\), and the four
edges \(ha,1b,2b,rc\).  Suppose

\[
                 G-B=O\mathbin{\dot\cup}D,                 \tag{1.1}
\]

where \(O,D\) are connected, anticomplete, and full to \(B\).  Suppose
that \(O\) contains disjoint connected carriers for \(P\) and \(Q\),
whereas \(D\) contains no such pair of carriers.

### Theorem 1.1 (transported atomic descent)

If \(G\) has no \(K_7\)-minor, there is a seven-cut \(S\) and a vertex
\(x\in D\) such that \(\{x\}\) is a component of \(G-S\).  Moreover,
there are seven pairwise vertex-disjoint paths from \(B\) to \(S\), one
starting at each labelled vertex of \(B\), whose nontrivial interiors
lie in \(D-\{x\}\).

Thus every singleton-triangle nonowner, including an arbitrarily deep
tower of nested exact seven-cuts, terminates at a transported full
singleton.  No nonsingleton atom survives.

## 2. The minimum nested fragment and its linkage

Consider all pairs \((S,F)\) such that \(|S|=7\) and \(F\) is a
component of \(G-S\) contained in \(D\).  The pair \((B,D)\) belongs to
this family.  Choose a pair with \(|F|\) minimum.

Every vertex of \(S\) has a neighbour in \(F\).  Otherwise
\(S-\{s\}\) would separate \(F\) from the nonempty set \(O\), contrary
to seven-connectivity.  Thus \(F\) is full to \(S\).

The separations with inner sides \(B\cup D\) and \(S\cup F\) are
nested.  The nested minimum-cut linkage lemma therefore gives seven
pairwise vertex-disjoint \(B\)-to-\(S\) paths

\[
                         L_t\quad(t\in B),                  \tag{2.1}
\]

whose nontrivial interiors lie in \(D-F\).  Common vertices of \(B\)
and \(S\) are represented by trivial paths.  Relabel the end of
\(L_t\) in \(S\) by \(t\).  The seven paths retain all edges of the
old boundary: the branch sets \(L_t\) and \(L_u\) are adjacent whenever
\(tu\in E(G[B])\).

### Lemma 2.1 (the minimum fragment is atomic)

If \(|F|>1\), then for every nonempty proper \(X\subsetneq F\),

\[
 |N_F(X)-X|+|N_S(X)|\ge8.                              \tag{2.2}
\]

#### Proof

The displayed union is exactly \(N_G(X)\), because \(F\) is a component
behind \(S\).  It separates every component of \(G[X]\) from \(O\), so
seven-connectivity gives a lower bound of seven.  If equality held,
choose a component \(K\) of \(G[X]\).  Its neighbourhood is contained
in the same seven-set and has order at least seven; hence it is exactly
that set.  Then \(K\) is a component behind a seven-cut, is contained
properly in \(F\), and contradicts the minimum choice of \(F\).
\(\square\)

### Lemma 2.2 (the transported fragment is packet-free)

With the labels transported by (2.1), \(F\) has no disjoint
\((P,Q)\)-packet.

#### Proof

Suppose \(A_P,A_Q\subseteq F\) were disjoint connected carriers.  For
each \(t\in P\cup Q\), remove the old endpoint \(t\) from a nontrivial
path \(L_t\), retaining its tail through the labelled vertex of \(S\);
for a trivial path no tail is needed.  Join the two \(P\)-tails through
\(A_P\), and the two \(Q\)-tails through \(A_Q\).  These two unions lie
in \(D\), are connected and disjoint, and meet the old portal sets of
the two roots in their respective pair.  They are a \((P,Q)\)-packet
in \(D\), contrary to (1.1). \(\square\)

## 3. The transported two-cut lift

Assume for contradiction that \(|F|>1\).  Lemmas 2.1--2.2 and the
label-free two-pair web theorem give a bare plane web for \(F\).  The
atomic one- and two-cut lemmas apply verbatim with the labels now on
\(S\).  Notice also that \(|F|\ge4\): the four pair-root labels have at
least two portals each, while no vertex can see both roots of either
pair, so at least eight incidences are distributed at no more than two
per vertex.  In particular, a two-cut would have two lobes with complementary
defects in one of the pairs.  Up to the automorphism

\[
 (h\ r)(a\ c)(1\ 2),                                  \tag{3.1}
\]

write those lobes as \(F_h,F_c\), where \(F_h\) misses only the
\(c\)-label and \(F_c\) misses only the \(h\)-label.

Let the old full shore \(O\) be used whole.  The seven bags

\[
 L_h\mid L_1\mid L_2\mid L_r\mid
 (L_a\cup F_c)\mid(L_b\cup O)\mid F_h               \tag{3.2}
\]

form a \(K_7\)-model.  The first four retain the old \(K_4\).
The fifth bag sees \(L_h\) through \(ah\), and sees \(L_1,L_2,L_r\)
through the full contacts of \(F_c\).  The sixth sees the first four
through the fullness of \(O\), while \(F_h\) sees them through its
transported boundary contacts.  Among the last three bags use,
respectively, the old edge \(ab\), the \(a\)-label contact of \(F_h\),
and the \(b\)-label contact of \(F_h\).  Hence a two-cut is impossible,
and \(F\) is three-connected.

## 4. Curvature after transport

The curvature proof for an atomic two-pair web depends only on (2.2)
and the seven labelled portal sets, not on edges induced by \(S\).
Consequently, after triangulating bounded faces, it gives at least six
positive-curvature vertices \(z\in F\) with

\[
 d_F(z)=3,\qquad
 N_S(z)=R\cup\{p(z),q(z)\},quad p(z)\in P, q(z)\in Q. \tag{4.1}
\]

For completeness, the cofacial step also transports.  If four common
\(R\)-neighbours were not cofacial, the rooted-\(K_4\) theorem inside
\(F\), together with the three mutually adjacent outer branch sets
\(L_1,L_2,L_b\), would give a \(K_7\)-model.  Hence all common
\(R\)-neighbours lie on one face; the disk-curvature fan argument makes
it the outer face and yields (4.1).

Choose distinct \(z_0,z_1\) satisfying (4.1).  Delete an edge on their
path in a spanning tree of \(F\), obtaining adjacent connected parts
\(W_0,W_1\), with \(z_i\in W_i\).

Let \(X_P,X_Q\subseteq O\) be the original owner carriers.  Use

\[
 (X_P\cup L_h\cup L_c)\mid
 (X_Q\cup L_r\cup L_a)\mid
 L_1\mid L_2\mid L_b\mid W_0\mid W_1.             \tag{4.2}
\]

The first two bags are connected and disjoint.  They are adjacent
through the retained edge \(hr\) (also through \(ca\)); they see the
three \(R\)-bags through \(h1,h2,cb\) and \(r1,r2,ab\), respectively.
The \(R\)-bags form a triangle.  By (4.1), each \(W_i\) sees both owner
bags and all three \(R\)-bags, and the two \(W_i\) are adjacent.  Thus
(4.2) is a \(K_7\)-model, the final contradiction.

We conclude that the minimum fragment \(F\) has order one.  Writing
\(F=\{x\}\) proves Theorem 1.1; fullness gives \(N_G(x)=S\), and the
paths (2.1) give the stated transported terminal. \(\square\)

## 5. Exact remaining cell

The theorem removes both the unbounded atomic web and every nonsingleton
nested exact-cut descendant.  Its terminal singleton is genuine: the
static packet data alone do not split the owner into the six
\(B\)-meeting bags needed beside that singleton.  Closing the branch now
requires the contraction-critical trace at the degree-seven terminal
\(x\), or an owner-carrier split theorem; it cannot be obtained by
another descent of the same kind.
