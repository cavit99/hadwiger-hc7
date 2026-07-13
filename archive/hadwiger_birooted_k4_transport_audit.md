# Birooted \(K_4\) transport: a sharp five-connectivity obstruction

## 1. Verdict

Two colourful sets in the same four-colourable slice do not force one
\(K_4\)-model meeting both sets, even when the slice is five-connected.
The obstruction can arise as the two parity portal sets of one induced-edge
contraction and can be supplied with four internally disjoint,
colour-matched Kempe carriers.

Thus any connectivity-only positive theorem needs connectivity at least
six.  More importantly for bipartite compression, neither common
contraction origin nor the separate parity-rooted \(K_4\) models nor the
matched carrier family synchronizes the two models.  A genuinely
minor-critical, model-relative exchange remains necessary.

## 2. The five-connected slice

Let

\[
 A=a_0a_1a_2a_3,\qquad B=b_0b_1b_2b_3
\]

be two disjoint four-vertex paths, and put

\[
                         J=A\vee B.                         \tag{2.1}
\]

Thus every vertex of \(A\) is adjacent to every vertex of \(B\).  Define

\[
 X=\{a_0,a_1,b_0,b_3\},\qquad
 Y=\{a_2,a_3,b_0,b_3\}.                                  \tag{2.2}
\]

### Theorem 2.1

The graph \(J\) is five-connected and four-chromatic.  Both \(X\) and
\(Y\) are colourful in every proper four-colouring of \(J\), but \(J\)
has no \(K_4\)-model whose four bags each meet both \(X\) and \(Y\).

#### Proof

If at most four vertices are deleted, then either a vertex remains in each
of \(A,B\), in which case the join edges connect everything, or one whole
four-vertex factor was deleted and the other path remains connected.
Hence \(J\) is five-connected.  An endpoint has degree five, so the
connectivity is exactly five.

Chromatic number is additive under joins.  Since both paths are connected
bipartite graphs with an edge,

\[
                         \chi(J)=\chi(A)+\chi(B)=4.          \tag{2.3}
\]

In every four-colouring the two factors use disjoint two-colour palettes.
The bipartition of a connected bipartite graph is unique.  Each of
\(\{a_0,a_1\}\), \(\{a_2,a_3\}\), and \(\{b_0,b_3\}\) meets both sides
of the relevant path bipartition.  Consequently both sets in (2.2) use
all four colours.

Suppose \(C_1,C_2,C_3,C_4\) were a birooted \(K_4\)-model.  Since the
bags are disjoint and \(|X|=|Y|=4\), every bag contains exactly one
vertex of \(X\) and exactly one vertex of \(Y\).  The two common roots

\[
                         X\cap Y=\{b_0,b_3\}                 \tag{2.4}
\]

therefore lie in two distinct bags, and those bags contain no vertex of
\(A\): all four vertices of \(A\) are among the remaining roots.

The two bags containing \(b_0,b_3\) are disjoint connected subgraphs of
the path \(B\) and must be adjacent.  A connected subgraph containing
\(b_0\) is a prefix and one containing \(b_3\) is a suffix; disjointness
and adjacency force their union to contain all of \(B\).  Hence the other
two bags use only vertices of \(A\).

Each of those two bags must contain one of \(a_0,a_1\) and one of
\(a_2,a_3\).  Every connected subgraph of the path \(A\) meeting both
sets contains the central edge vertices \(a_1,a_2\).  Two such subgraphs
cannot be disjoint, a contradiction. \(\square\)

The graph is isomorphic to the complement of two disjoint copies of
\(P_4\).  It is not atlas graph 1228 (which has seven vertices); it is a
new eight-vertex obstruction at the next connectivity level.

## 3. Exact parity-compression realization with matched carriers

The obstruction is not merely an abstract colourful pair.  Add vertices
\(d_0,d_1,u,w\) as follows.

* \(d_0d_1\) and \(uw\) are edges.
* Both \(d_0,d_1\) are complete to \(J\).
* Both \(u,w\) see \(d_1\), while neither sees \(d_0\).
* The neighbours of \(u\) in \(J\) are exactly \(X\), and the neighbours
  of \(w\) in \(J\) are exactly \(Y\).

Finally add relay vertices \(h_0,h_1\), with edges

\[
                         a_0h_0a_2,qquad a_1h_1a_3,         \tag{3.1}
\]

and no other relay edges.  Call the resulting graph \(F\).

### Theorem 3.1

The graph \(F\) is not six-colourable.  Contracting the induced edge
\(uw\) gives a six-colouring whose four-colour slice is exactly \(J\) and
whose two parity portal sets are exactly \(X,Y\).  Moreover \(F-uw\) has
a six-colouring in which \(u,w\) lie in the same bichromatic component for
each of the four slice colours, with four internally disjoint matched
carriers.

#### Proof

In a hypothetical six-colouring of \(F\), the adjacent vertices
\(d_0,d_1\), both complete to the four-chromatic graph \(J\), use two
distinct colours absent from \(J\).  Thus \(J\) uses the other four
colours.  Colourfulness of \(X,Y\) makes both \(u,w\) see all four of
those colours, and both see the colour of \(d_1\).  Their only available
colour is the colour of \(d_0\), contradicting \(uw\in E(F)\).

Colour the bipartition classes of \(A\) with colours \(0,1\), those of
\(B\) with \(2,3\), give \(u,w,d_0,h_0,h_1\) colour \(4\), and give
\(d_1\) colour \(5\).  This properly colours \(F-uw\), and it descends
to a colouring of \(F/uw\).  The four-colour induced slice is literally
\(J\), and the two endpoint neighbourhoods inside it are (2.2).

The four bichromatic \(u\)-\(w\) paths are

\[
\begin{array}{ll}
u a_0 h_0 a_2 w,&u a_1 h_1 a_3 w,\\
u b_0 w,&u b_3 w.
\end{array}                                               \tag{3.2}
\]

Their interiors are pairwise disjoint, and each uses colour \(4\) and
one distinct slice colour. \(\square\)

The construction is verified independently by
`birooted_k4_five_connected_counterexample.py`.

## 4. Consequence for the parity-rooted core

Theorem 1.1 of `hadwiger_bipartite_compression_rooted_core.md` correctly
gives an \(X\)-rooted \(K_4\)-model and a separate \(Y\)-rooted
\(K_4\)-model.  Theorem 2.1 proves that they cannot in general be chosen
to be the same model, even under five-connectivity of the entire slice.
Theorem 3.1 additionally supplies the strongest fixed-colouring data from
the operated edge: one disjoint colour-matched carrier for every slice
colour.

The ambient graph \(F\) is deliberately not proper-minor-critical (the
relay vertices already expose this).  Therefore the exact surviving
positive target is operation-sensitive:

> Does six-connectivity of the fixed slice, together with its occurrence
> inside a proper-minor-minimal non-six-colourable host and the full
> one-step transition family, force a birooted \(K_4\)-model or an actual
> colour-gluable adhesion?

The present theorem shows that every clause matters.  Dropping
six-connectivity fails by Theorem 2.1; dropping full minor-criticality
fails even after adding the four matched carriers by Theorem 3.1.  No
claim that six-connectivity alone suffices is made here.
