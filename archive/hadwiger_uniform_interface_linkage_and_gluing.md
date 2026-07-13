# Uniform interface linkage and exact boundary-state gluing

## 1. Connectivity-budget linkage

### Theorem 1.1 (contact or linkage)

Let \(G\) be \(k\)-connected, let \(S\subseteq V(G)\), and let \(C\) be
a component of \(G-S\). Put

\[
 F=N_G(C)\cap S,\qquad |F|=m.
\]

Assume \(m\ge k\). (This is automatic when \(F\) separates \(C\) from
a vertex outside \(C\cup F\).) Let \(P\) be any nonempty proper subset
of \(C\), put \(Q=C-P\), and define

\[
 R=N_G(P)\cap S,\qquad D=F-R,\qquad I=N_G(P)\cap Q.
\]

If \(r=|R|<k\), then \(G[Q\cup D]\) contains \(k-r\) pairwise
vertex-disjoint \(D\)-to-\(I\) paths. Their initial vertices in \(D\)
are distinct, their terminal vertices in \(I\) are distinct, and all
internal vertices lie in \(Q\).

Equivalently, every shore piece either contacts at least \(k\) boundary
vertices or its unused connectivity budget produces the same number of
disjoint, label-preserving interface paths.

#### Proof

By the assumed boundary order,

\[
 |D|=m-r\ge k-r.                                             \tag{1.1}
\]

Use the endpoint-allowed set form of Menger's theorem in
\(H=G[Q\cup D]\). If fewer than \(p=k-r\) disjoint paths exist, there is
\(Z\subseteq Q\cup D\), allowed to meet both terminal sets, such that

\[
 |Z|<p,qquad H-Z\text{ has no path from }D-Z\text{ to }I-Z. \tag{1.2}
\]

After deleting \(R\cup Z\), take \(P\) together with every component of
\(H-Z\) meeting \(I-Z\); if \(I\subseteq Z\), take just \(P\). No edge
leaves this side. Edges from \(P\) to \(S\) end in \(R\), edges from
\(P\) to \(Q\) end in \(I\), and vertices of \(Q\subseteq C\) have no
neighbor outside \(C\cup F\). An edge from a selected component to
\(D-Z\) would contradict (1.2).

The selected side is nonempty. By (1.1), some vertex of \(D-Z\) remains
on the other side. Hence \(R\cup Z\) separates \(G\), but

\[
 |R\cup Z|<r+(k-r)=k,
\]

contradicting \(k\)-connectivity. The endpoint statements follow from
vertex-disjointness. Finally, replace each oriented \(D\)-to-\(I\) path by
the subpath beginning at its last vertex in \(D\). The new initial vertices
remain distinct and every internal vertex now lies in \(Q\). \(\square\)

Connectedness of \(P\) and \(Q\) is not needed.

### Corollary 1.2 (equality boundary)

If \(|F|=k\), then \(|D|=k-r\), so every vertex of \(D\) starts one of
the paths. Thus every missing boundary label is linked to a distinct
opposite-side interface vertex.

### Proposition 1.3 (sharpness)

The bound \(k-r\) is best possible for every \(k\ge2\),
\(0\le r<k\), and \(m\ge k\).

#### Proof

Take disjoint sets \(F,I\) with \(|F|=m\), \(|I|=k-r\), choose
\(R\subseteq F\) of order \(r\), and add a vertex \(x\). Make
\(F\cup I\) a clique and make \(x\) adjacent exactly to \(R\cup I\).
The graph is \(k\)-connected: fewer than \(k\) deletions leave a neighbor
of \(x\), and the remaining vertices outside \(x\) form a clique. The
set \(R\cup I\) is a cut of order \(k\).

Take \(S=F\), \(C=\{x\}\cup I\), \(P=\{x\}\), and \(Q=I\). The
terminal set \(I\) has order \(k-r\), so a larger linkage is impossible.
\(\square\)

## 2. The exact coloring invariant

For a graph \(H\) with distinguished set \(X\), let
\(\Pi_q(H,X)\) be the set of equality partitions of \(X\) induced by all
proper \(q\)-colorings of \(H\).

### Lemma 2.1 (partition criterion)

Let \((A,B)\) be a separation of \(G\), with adhesion \(X=A\cap B\).
Colorings of \(G[A]\) and \(G[B]\) can be aligned by a palette permutation
and glued if and only if their two sets \(\Pi_q\) have a common partition.

#### Proof

If the equality partitions agree, map each used color on one restriction
to the color of its corresponding block on the other. This injective
partial map extends to a permutation of the \(q\)-color palette. The
restrictions then agree, and no edge joins \(A-B\) to \(B-A\).
The converse follows by restricting a glued coloring to \(X\). \(\square\)

### Theorem 2.2 (minimal incompatible states)

Let \(G\) be non-\(q\)-colorable while every proper minor of \(G\) is
\(q\)-colorable. For every nontrivial separation \((A,B)\) with adhesion
\(X\):

1. both side graphs are \(q\)-colorable;
2. \(\Pi_q(G[A],X)\) and \(\Pi_q(G[B],X)\) are disjoint; and
3. after every deletion or contraction supported entirely in \(A-X\),
   the modified \(A\)-side partition set intersects the original
   \(B\)-side set, and symmetrically for operations in \(B-X\).

#### Proof

The side graphs and every graph after an indicated operation are proper
minors. If the original side partition sets intersected, Lemma 2.1 would
color \(G\). A coloring of a graph after an internal minor operation
restricts to one common partition on the unchanged adhesion, proving the
transition assertion. \(\square\)

Thus proper-minor criticality supplies a minimal incompatible pair, not
automatic exact-adhesion gluing.

### Lemma 2.3 (connected-shore exact trace)

Let \(G\) be non-\(q\)-colourable while every proper minor is
\(q\)-colourable.  Let \(C\) be a connected vertex set with boundary
\(X=N_G(C)\), and let \(S\subseteq X\) be a nonempty independent set.
There is a proper \(q\)-colouring of \(G-C\) in which one colour has
trace exactly \(S\) on \(X\).

#### Proof

The set \(C\cup S\) is connected.  Contract it to a vertex \(z\) and
colour the resulting proper minor.  Delete the vertices of \(C\) and
expand only the independent set \(S\) with colour \(c(z)\).  Every
vertex of \(X-S\) was adjacent to \(z\) through its neighbour in
\(C\), so none receives \(c(z)\).  All other edges were represented by
the contraction, and there is no edge inside \(S\). \(\square\)

This is the shore version of the independent-star trace witness; it
uses full boundary contact rather than a universal centre.

### Corollary 2.4 (unique-colourability gluing)

Let \((A,B)\) be a nontrivial separation with adhesion \(X\).  Suppose
each open side contains a connected set which is adjacent to every
vertex of \(X\).  If an independent set \(S\subseteq X\) has the
property that \(G[X-S]\) is uniquely \((q-1)\)-colourable (as an
equality partition, up to permuting colours), then \(G\) is
\(q\)-colourable.

#### Proof

Contract the full connected set on the \(B\)-side together with \(S\),
delete the rest of \(B-A\), and colour the proper minor.  Expanding only
\(S\) gives a colouring of \(G[A]\) in which \(S\) is one colour block
and every vertex of \(X-S\) avoids that colour.  Unique
\((q-1)\)-colourability fixes the remaining equality blocks.  The
symmetric contraction on the \(A\)-side gives the same partition on
\(G[B]\).  Lemma 2.1 aligns and glues the two colourings. \(\square\)

In particular, if \(|X|=q+1\), \(S\) is an independent pair, and
\(X-S\) is a \((q-1)\)-clique, such an adhesion is impossible in a
proper-minor-minimal non-\(q\)-colourable graph.

## 3. What proper-minor criticality can glue

### Theorem 3.1 (two-sided rooted-clique gluing)

In the setting of Theorem 2.2, suppose

\[
 X=X_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}X_s,
 \qquad s\le q,                                             \tag{3.1}
\]

where every \(X_i\) is independent. Suppose that on each side
\(Y\in\{A,B\}\) there are pairwise disjoint connected subgraphs
\(T_1^Y,\ldots,T_s^Y\) such that

\[
 V(T_i^Y)\cap X=X_i,qquad
 T_i^Y\text{ is adjacent to }T_j^Y\quad(i\ne j).             \tag{3.2}
\]

Then \(G\) is \(q\)-colorable, a contradiction.

#### Proof

Contract the \(B\)-side rooted clique branch sets and delete every
remaining vertex of \(B-A\). This is a proper minor. Its contracted images
form a clique, so a \(q\)-coloring gives them distinct colors. Restrict to
the \(A\)-side and expand every independent \(X_i\) monochromatically.
Every external edge was represented after contraction, so this is a proper
coloring of \(G[A]\) whose equality partition is exactly (3.1).

Using the \(A\)-side model symmetrically colors \(G[B]\) with the same
partition. Lemma 2.1 aligns and glues the two colorings. \(\square\)

Hence an exact \(k\)-adhesion is color-gluable when the linkage geometry
can be packaged into the same rooted clique partition on both sides.
Theorem 1.1 alone supplies disjoint paths, not the pairwise branch-set
adjacencies required by (3.2).

## 4. Minimal obstruction to bare adhesion gluing

### Proposition 4.1 (odd-cycle parity obstruction)

Let \(G=C_5\), choose vertices \(x,y\) at distance two, and split the
cycle into its two \(x\)-to-\(y\) arcs. The adhesion \(X=\{x,y\}\) has
order \(\kappa(C_5)=2\). One side is a path of length two and forces
\(x,y\) to have the same color in every two-coloring. The other has length
three and forces different colors. Thus the two boundary partition sets
are disjoint.

The graph is minimally non-bipartite under vertex deletion, edge deletion,
and every **single** edge contraction: one contraction gives \(C_4\).
After any one-step operation, the parity obstruction disappears. Therefore
exact connectivity plus all immediate deletion/contraction witnesses does
not force the original adhesion to be color-gluable.

The example is not proper-minor-minimal, since two successive contractions
can produce \(K_3\). This distinction matters because chromatic number is
not monotone under contraction. Under the full proper-minor hypothesis,
Theorem 2.2 is the unconditional conclusion: the original states are
incompatible, while every internal transition makes them compatible.

## 5. Consequence

The general mechanism is now exact:

\[
\begin{array}{c}
k\text{-connectivity}\Longrightarrow k-|R|\text{ disjoint paths},\\
|F|=k\Longrightarrow\text{every missing label is linked},\\
\text{minor criticality}\Longrightarrow
\text{minimal incompatible boundary partitions},\\
\text{two-sided rooted clique partition}\Longrightarrow\text{gluing}.
\end{array}
\]

The remaining substantive step is linkage-to-rooted-clique packaging, or a
structural description of the exact-adhesion states preventing it. No
stronger path count follows from connectivity alone by Proposition 1.3.
