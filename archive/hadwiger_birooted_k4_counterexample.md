# A 5-connected counterexample to the birooted \(K_4\) principle

## 1. The proposed principle is false

Let \(F\) be the disjoint union of the two paths

\[
                 0-5-6-2,\qquad 1-7-4-3,
\]

and put

\[
                         J=\overline F=K_8-E(F).
\]

Thus the six nonedges of \(J\) are

\[
             05,56,62,\qquad 17,74,43.                 \tag{1.1}
\]

Define

\[
                  X=\{1,4,5,6\},\qquad
                  Y=\{3,5,6,7\}.                       \tag{1.2}
\]

### Theorem 1.1

The graph \(J\) is 5-connected and 4-colourable, and both \(X\) and
\(Y\) use all four colours in every proper four-colouring of \(J\).
Nevertheless, \(J\) has no \(K_4\)-model whose four branch sets each
meet both \(X\) and \(Y\).

This disproves the proposed birooted principle even at connectivity
five.

## 2. Connectivity and colour saturation

Every vertex of \(F\) has degree at most two.  Hence every vertex of
\(J\) has degree at least five, and the four internal path vertices
\(5,6,7,4\) have degree exactly five.

Suppose deletion of at most four vertices disconnected \(J\), and let
\(A,B\) be two unions of components of the remaining graph.  At least
four vertices remain.  Since no edge of \(J\) joins \(A\) to \(B\), the
forest \(F\) contains every edge of the complete bipartite graph
\(K_{|A|,|B|}\).  A forest contains no \(K_{2,2}\), so one side has
order one.  Its vertex then has degree at least three in \(F\), because
\(|A|+|B|\ge4\), contradicting \(\Delta(F)=2\).  Thus \(J\) is
5-connected.  Since \(\delta(J)=5\), its connectivity is exactly five.

The independence number of \(J\) is two, because \(F\) is triangle
free.  Consequently every four-colouring of the eight-vertex graph
\(J\) consists of four independent pairs, and those pairs form a perfect
matching of \(F\).  Each four-vertex path has the unique perfect matching
given by its two end edges.  Hence, up to permuting the colours, the
unique colour classes are

\[
                  \{0,5\},\quad \{6,2\},\quad
                  \{1,7\},\quad \{4,3\}.               \tag{2.1}
\]

Both sets in (1.2) meet every pair in (2.1).  They are therefore
four-colour-saturating.

## 3. No birooted model exists

Suppose that \(B_1,B_2,B_3,B_4\) were four disjoint connected branch
sets, pairwise adjacent, with every \(B_i\) meeting both \(X\) and
\(Y\).

Because \(|X|=|Y|=4\), disjointness forces each branch set to contain
exactly one vertex of \(X\) and exactly one vertex of \(Y\), and all
vertices of both sets are used.  In particular, the common vertices
\(5,6\in X\cap Y\) lie in distinct branch sets, say \(B_5,B_6\), and

\[
 B_5\subseteq\{5,0,2\},\qquad
 B_6\subseteq\{6,0,2\}.                                \tag{3.1}
\]

The only vertices outside \(X\cup Y\) are \(0,2\); call them the two
helpers.

We first observe that adjacency of the connected bags \(B_5,B_6\)
uses both helpers.  Indeed, \(56\) is a nonedge.  If their adjacency is
witnessed by \(5-2\), then \(2\in B_6\); since \(26\) is a nonedge,
connectivity of \(B_6\) forces \(0\in B_6\).  Symmetrically, if it is
witnessed by \(0-6\), connectivity of \(B_5\) forces \(2\in B_5\).
The only other possible helper-to-helper witness is \(02\), which also
uses both helpers.  Thus

\[
                         \{0,2\}\subseteq B_5\cup B_6.  \tag{3.2}
\]

The two remaining bags must pair the two vertices
\(X-Y=\{1,4\}\) with the two vertices \(Y-X=\{3,7\}\).  Either the
pairs are

\[
                         (1,3),(4,7)
\]

or they are

\[
                         (1,7),(4,3).
\]

In the first pairing \(47\) is a nonedge.  In the second pairing both
\(17\) and \(43\) are nonedges.  By (3.2) no helper remains, and a bag
containing one of these pairs has no third available vertex through
which it can become connected.  This contradiction proves Theorem 1.1.

## 4. Consequence for parity-rooted compression

The counterexample directly blocks the proposed simultaneous upgrade of
`hadwiger_bipartite_compression_rooted_core.md`.  That note proves only
that the two parity portal sets \(X_U,X_W\) are separately
four-colour-saturating in the four-colour graph \(J\).  Separate
saturation does not imply a single \(K_4\)-model meeting both sets in
every bag, even when \(J\) is 5-connected.

There is an additional applicability gap: connectivity of the ambient
\(HC_7\) host does not pass to the subgraph induced by four colour
classes.  Thus even a true theorem requiring 5-connectivity of \(J\)
would need a new relative-connectivity lemma before it could be used in
the compression argument.

The parity-rooted cores can still be transported only with extra data,
for example a four-way linkage between the two existing rooted models,
a common saturating subset, or reserved carriers which absorb the
capacity defect.  None of those resources follows from the two
saturation statements alone.
