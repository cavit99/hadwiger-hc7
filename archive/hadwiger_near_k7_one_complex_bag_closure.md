# Near-\(K_7\) models with one complex unaffected bag: the cut-bag closure

## Status

This note proves a label-preserving split for an infinite, fully specified
subfamily of the near-\(K_7\) obstruction.  It does **not** prove that every
one-complex-bag model upgrades: the complex bag here is one of the
unaffected bags.  The two-apex example \(K_2\vee I\), with
\(I\) the icosahedron, has such models and shows that a connectivity-only
claim would be false.  The surviving one-bag core is forced to be
2-connected, exactly where a rooted-minor/web theorem is needed.

## 1. Full contact behind a cutvertex

### Lemma 1.1 (six singleton portals force full contact on every cut side)

Let \(G\) be a seven-connected graph with a partition

\[
 V(G)=D\mathbin{\dot\cup}S,
 \qquad |S|=6,
\]

such that \(G[D]\) is connected.  If \(x\) is a cutvertex of \(G[D]\),
then every component \(P\) of \(G[D-x]\) has a neighbour at every vertex
of \(S\).

#### Proof

There are no edges from \(P\) to another component of \(G[D-x]\), and
hence

\[
 N_G(P)\subseteq S\cup\{x\}.
\]

Another component of \(G[D-x]\) remains outside \(P\cup N_G(P)\).
Seven-connectivity gives \(|N_G(P)|\ge7\).  The right-hand side of the
displayed containment has order seven, so equality holds.  In particular,
\(P\) has a neighbour at every vertex of \(S\). \(\square\)

If \(P\) is one component and \(R=D-P\), then \(P,R\) are nonempty and
connected, they are adjacent, and both meet all six singleton portals: a
second component of \(G[D-x]\), contained in \(R\), supplies the contacts
for \(R\).

## 2. The \(K_7^-\) cut-bag closure

### Theorem 2.1

Let \(G\) be a seven-connected graph with a spanning \(K_7^-\)-model

\[
 (A,C,D,Q_1,Q_2,Q_3,Q_4),
\]

where \(AC\) is the only non-required adjacency.  Suppose the six bags
other than \(D\) are singleton vertices.  If \(G[D]\) has a cutvertex,
then \(G\) contains a \(K_7\)-minor.

#### Proof

Write

\[
 S=\{a,c,q_1,q_2,q_3,q_4\}.
\]

If \(ac\in E(G)\), the displayed model is already a \(K_7\)-model, so
assume \(ac\notin E(G)\).  Lemma 1.1 gives a partition
\(D=P\mathbin{\dot\cup}R\) into adjacent connected sets, each meeting all
six vertices of \(S\).

Use the seven branch sets

\[
 P\cup\{a\},\quad \{c\},\quad
 \{q_1\},\ldots,\{q_4\},\quad R.
\]

The first bag is connected and becomes adjacent to \(c\) through \(P\).
It is adjacent to \(R\) through the edge \(PR\).  The set \(R\) meets
\(c,q_1,\ldots,q_4\), and all remaining adjacencies are edges of the old
near-clique.  Thus these bags form a \(K_7\)-model. \(\square\)

### Corollary 2.2 (tree bag)

Under the hypotheses of Theorem 2.1, if \(G[D]\) is a tree, then \(G\)
contains a \(K_7\)-minor.

#### Proof

Seven-connectivity gives minimum degree at least seven.  In the singleton
boundary, \(a,c\) each have four neighbours and each \(q_i\) has five.
Thus \(|D|\ge3\).  A tree of order at least three has a cutvertex, so
Theorem 2.1 applies. \(\square\)

## 3. The \(K_7^{\vee}\) cut-bag closure

### Theorem 3.1

Let \(G\) be a seven-connected graph with a spanning
\(K_7^{\vee}\)-model

\[
 (A,B,C,D,Q_1,Q_2,Q_3),
\]

where \(AB\) and \(AC\) are the only non-required adjacencies.  Suppose
the six bags other than \(D\) are singletons.  If \(G[D]\) has a
cutvertex, then \(G\) contains a \(K_7\)-minor (unless one missing edge was
already present, in which case the same argument starts from the resulting
\(K_7^-\)-model).

#### Proof

In the genuinely deficient case, let

\[
 S=\{a,b,c,q_1,q_2,q_3\}.
\]

Lemma 1.1 gives adjacent connected sets \(P,R\), each meeting all six
vertices of \(S\).  Replace \(A\) by \(P\cup\{a\}\), retain the five
singletons \(b,c,q_1,q_2,q_3\), and use \(R\) as the seventh bag.  The
contacts from \(P\) to \(b,c\) repair both deficient pairs, while the edge
\(PR\) and the full contacts of \(R\) preserve every other adjacency.
Hence the seven bags form a \(K_7\)-model. \(\square\)

### Corollary 3.2 (tree bag)

Under the hypotheses of Theorem 3.1, if \(G[D]\) is a tree, then \(G\)
contains a \(K_7\)-minor.

Indeed, the singleton \(a\) has only three boundary neighbours, so minimum
degree seven forces at least four neighbours in \(D\); in particular
\(|D|\ge4\), and a tree of that order has a cutvertex.

## 4. Exact limit and the first two-complex-bag target

Thus a seven-connected \(K_7\)-minor-free graph having a spanning
near-\(K_7\) model whose only complex bag is unaffected forces that bag to
be 2-connected.  This conclusion is sharp at the level of connectivity:
\(K_2\vee I\) is seven-connected, \(K_7\)-minor-free, two-apex, and has
such a spanning \(K_7^-\)-model.  In the notation of Proposition 2.1 of
`hadwiger_near_k7_split_round.md`, take the six singleton bags

\[
 \{t\},\{u_0\},\{u_1\},\{u_2\},\{p\},\{q\}
\]

and take the remaining eight icosahedral vertices as \(D\).  The singleton
bags induce \(K_6^-\), with missing edge \(u_0u_2\); the remaining bag is
connected and meets all six of them.  It is necessarily 2-connected by
Theorem 2.1 (and this is also immediate from the icosahedral labelling).

With two complex bags \(D,E\), the cutvertex proof fails for one precise
reason.  A component \(P\) of \(D-x\) has

\[
 N_G(P)\subseteq \{x\}\cup S_5\cup E,
\]

where \(S_5\) denotes the five singleton bags.  Seven distinct neighbours
may now be concentrated in \(E\), so connectivity no longer forces contact
with every branch-set label.  The next valid theorem must control that
concentration.  A natural exact local alternative is:

* either two cut sides of \(D\) have the labelled contacts needed for the
  one-bag split; or
* every deficient contact is routed through a bounded portal set in \(E\),
  producing the two-shore rooted \(K_{2,4}\)/web obstruction.

This is the first point at which contraction-critical state exchange, not
mere connectivity, is essential.
