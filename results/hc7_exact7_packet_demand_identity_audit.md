# Independent audit: packet demand as clique-deletion chromatic number

**Verdict:** **GREEN, with the empty-object conventions below made explicit.**

## 1. Required conventions

The statement and proof are correct provided that

* the empty set is admitted as a clique;
* \(\omega(\varnothing)=0\); and
* the empty graph has its unique empty partition into independent blocks and
  \(\chi(\varnothing)=0\).

The draft already states the last chromatic convention, but the first two
should also be stated.  They are used when a partition has no singleton
blocks, and they are needed to include \(H=\varnothing\) literally.  This is
a convention clarification, not a mathematical gap.

Write

\[
 q(H)=\min\{\chi(H-U):U\subseteq V(H),\ H[U]\text{ is a clique}\}.
\]

## 2. Audit of \(q(H)\leq\delta_{\rm pkt}(H)\)

Fix an independent-block partition \(\Pi\), put
\(X=\operatorname{sing}(\Pi)\), and choose a maximum clique
\(U\subseteq X\).  If \(X=\varnothing\), this means \(U=\varnothing\)
under the conventions above.

Deleting the singleton blocks indexed by \(U\) leaves exactly

\[
 |\Pi|-|U|=|\Pi|-\omega(H[X])=d_H(\Pi)
\]

independent blocks partitioning \(V(H)-U\).  Hence

\[
 q(H)\leq \chi(H-U)\leq d_H(\Pi).
\]

This holds for every \(\Pi\), so
\(q(H)\leq\delta_{\rm pkt}(H)\).  No assumption that the remaining blocks
are colour classes of an optimal colouring is needed.

## 3. Audit of \(\delta_{\rm pkt}(H)\leq q(H)\)

Fix any clique \(U\) and let \(k=\chi(H-U)\).  Take the \(k\) nonempty
colour classes of an optimal colouring of \(H-U\) (none when
\(H-U=\varnothing\)) and add one singleton block for each vertex of \(U\).
This is an independent-block partition \(\Pi_U\) having \(k+|U|\) blocks.

Every vertex of \(U\) is a singleton of \(\Pi_U\), so the singleton-induced
graph contains the clique \(H[U]\).  Additional singleton colour classes can
only increase its clique number.  Therefore

\[
 d_H(\Pi_U)
 =k+|U|-\omega(H[\operatorname{sing}(\Pi_U)])
 \leq k.
\]

Thus \(\delta_{\rm pkt}(H)\leq\chi(H-U)\) for every clique \(U\), and
minimizing gives \(\delta_{\rm pkt}(H)\leq q(H)\).  Together with Section 2
this proves the identity.

The proof permits strict inequality for this particular \(\Pi_U\), because
extra singleton colour classes may enlarge the retained clique.  That does
not affect the two opposite global inequalities.

## 4. Clique odd-cycle transversal consequence

Under the same empty-clique convention,

\[
 \delta_{\rm pkt}(H)\leq2
 \quad\Longleftrightarrow\quad
 \text{some clique }U\text{ has }\chi(H-U)\leq2
 \quad\Longleftrightarrow\quad
 H-U\text{ is bipartite}.
\]

So the clique odd-cycle transversal formulation is exact, including the
possibility \(U=\varnothing\).

## 5. Scope of the `119/10` interpretation

The numbers `119` and `10` do **not** follow from the identity alone.  They
follow only after importing the independently audited finite census of the
129 residual seven-vertex boundary graphs.  That census establishes that
119 residuals have minimum packet demand at most two and ten have minimum
packet demand three.  The identity then translates those two census classes
exactly into

* 119 residuals possessing a clique odd-cycle transversal; and
* ten residuals possessing no clique odd-cycle transversal.

There is one harmless trust-boundary detail.  The census enumerated equality
partitions with at most six blocks, whereas the identity minimizes over all
partitions.  On seven vertices the only omitted block count is seven, namely
the all-singleton partition.  Every graph in the 129 residual has
\(\omega(H)\leq3\), so that omitted partition has demand
\(7-\omega(H)\geq4\).  It therefore cannot improve the census minima two or
three.  The two notions of minimum agree on this residual family.

Finally, this remains a classification of *available abstract boundary
states*.  It supplies neither a proper-minor operation realizing a chosen
state nor the state-transfer step needed to close an actual `(1,2)`
adhesion.  The draft states this limitation correctly.
