# The singleton carrier descends to a cut or a three-terminal triangle

## 1. Setting

Let \(G\) be seven-connected and \(K_7\)-minor-free, and retain a
spanning singleton model

\[
             \{h\},\{1\},\{2\},\{r\},C,D_0,D_1,           \tag{1.1}
\]

whose only deficient pair is \(D_0D_1\).  The four singleton vertices
form a clique.  The carrier \(C\) and both shores see all four
singletons.  In the Moser application \(C\) contains:

* a vertex \(a_h\) adjacent to \(h\) (the right exterior root);
* the vertex \(6\), adjacent to \(1,2\); and
* a vertex \(a_r\) adjacent to the singleton \(r\).

The first two are distinct because \(h6\notin E(G)\).  Put

\[
                         Z=\{a_h,6,a_r\}.                  \tag{1.2}
\]

Repeated vertices in this display are retained only once.  Choose a
vertex-minimal set \(W\subseteq C\) containing \(Z\) for which \(G[W]\)
is connected.

## 2. The descent

### Theorem 2.1 (three-terminal carrier descent)

At least one of the following holds.

1. The carrier can be replaced, by label-preserving absorptions, with a
   connected carrier having a cutvertex or at most two vertices.
2. It can be replaced with the three-vertex triangle \(G[W]\), where
   \(W=Z\); the new carrier retains at least two distinct portals to
   each of \(D_0,D_1\).

All four singleton contacts, both shore roots, and the deficient pair are
preserved.  The replacement model need not remain spanning: an off-core
component with no shore portal may be left unused.  It does retain the
weaker invariant needed below that every unused vertex is anticomplete to
both shores.

#### Proof

By the spanning carrier-load lemma,

\[
                         |N_C(D_i)|\ge3
                         \qquad(i=0,1).                    \tag{2.1}
\]

The set \(W\) is connected, meets the singleton bag \(\{r\}\) through
\(a_r\), and sees \(h,1,2\) through \(a_h,6\).  It is therefore a
protected core for the all-\(t\) protected-web absorption theorem, with
gate \(K=C\), carrier bag \(\{r\}\), shore bags \(D_0,D_1\), and old
clique bags \(\{h\},\{1\},\{2\}\).

If \(C\) is not two-connected, outcome 1 already holds.  Otherwise
apply protected-web absorption with the fixed core \(W\).  Every
off-\(W\) bridge is either discarded or absorbed into its unique shore;
a mixed bridge gives a \(K_7\)-model and is impossible here.  At every
two-connected stage, two distinct portals to each shore are retained.
The finite descent stops either when the carrier ceases to be
two-connected, giving outcome 1, or when its vertex set is exactly
\(W\).

Suppose the latter carrier is still two-connected.  If
\(x\in W-Z\), then \(G[W]-x\) is connected and still contains \(Z\),
contrary to the vertex-minimal choice of \(W\).  Hence \(W=Z\), so
\(|W|\le3\).  The two distinguished vertices \(a_h,6\) show
\(|W|\ge2\); a two-connected terminal carrier has at least three
vertices.  Thus \(|W|=3\), and its connected two-connected induced
graph is a triangle.  The absorption theorem retains the asserted
  portal multiplicities and all protected contacts.  A discarded bridge
  has no portal to either current shore.  Different off-core components
  are anticomplete, so later absorptions cannot create a shore edge into
  an earlier discarded bridge.  Thus every unused vertex remains
  anticomplete to both shores throughout the descent. \(\square\)

### Corollary 2.2 (the triangle endpoint is an exact bounded interface)

In outcome 2, both shores are adjacent to every vertex of

\[
                         \{h,1,2,r\}\cup W.                \tag{2.2}
\]

#### Proof

Initially the model is spanning, and the proof of Theorem 2.1 shows that
every vertex subsequently left unused is anticomplete to both shores.
Moreover \(D_0,D_1\) remain anticomplete.  Hence every neighbour of
\(D_i\) outside \(D_i\) lies in the seven-set (2.2).
The other shore is nonempty and lies beyond this neighbourhood, so
\(N(D_i)\) is a separator.  Seven-connectivity gives
\(|N(D_i)|\ge7\), forcing equality with (2.2). \(\square\)

### Corollary 2.3 (there are exactly two full shores)

At the triangle endpoint,

\[
                         G-B=D_0\mathbin{\dot\cup}D_1,      \tag{2.3}
\]

where \(B=\{h,1,2,r\}\cup W\).  In particular no vertex discarded
during the descent remains outside the two shore bags.

#### Proof

Every discarded vertex is anticomplete to \(D_0,D_1\), so each nonempty
discarded component of \(G-B\) would be a third component.  Since
\(|B|=7\), seven-connectivity makes every component of \(G-B\) full to
\(B\).

If three full components \(R_0,R_1,R_2\) existed, use the seven bags

\[
 \{h\},\{1\},\{2\},\{r\},\quad
 R_0,\quad R_1\cup\{a\},\quad R_2\cup\{b\},               \tag{2.4}
\]

where \(a,b\) are two vertices of the carrier triangle.  Fullness makes
every new bag adjacent to the singleton \(K_4\) and to the anchors in
the other new bags; the edge \(ab\) supplies the remaining adjacency.
These bags form a \(K_7\)-model, a contradiction. \(\square\)

## 3. Exact scope

This eliminates every unbounded two-connected carrier web in the
singleton state.  The surviving geometry is either a genuine
cutvertex/protected-core obstruction, or a fixed three-vertex triangle
to which both deficient shores are fully attached.  The latter is not
declared impossible: the conservative quotient need not contain
\(K_7\), so contraction-critical colouring information is still needed
at this bounded interface.

## 4. The triangle boundary has one canonical four-block state

Write the triangle endpoint as

\[
                         W=\{a,b,c\},                       \tag{4.1}
\]

where \(ah,b1,b2,cr\in E(G)\).  Besides the two cliques
\(G[\{h,1,2,r\}]\cong K_4\) and \(G[W]\cong K_3\), these are the four
protected cross edges.  Corollary 2.2 says that both shores are full to
the seven-vertex boundary

\[
                         B=\{h,1,2,r,a,b,c\}.               \tag{4.2}
\]

### Lemma 4.1 (all extra cross edges are one-centred)

If \(G\) has no \(K_7\)-minor, then

\[
 hb,hc,ra,rb\notin E(G),                                  \tag{4.3}
\]

and the optional edges from \(\{1,2\}\) to \(\{a,c\}\) are all
incident with the same member \(x\in\{1,2\}\).  Thus they form an
arbitrary subset of \(\{xa,xc\}\).

#### Proof

Let the two full shores be denoted \(E,F\).  Each forbidden minimal
pattern in the first column of the following table gives the seven bags
in the second column:

\[
\begin{array}{c|l}
 hb&
 h\mid1\mid2\mid rc\mid aE\mid b\mid F\\
 hc&
 h\mid1\mid2\mid r\mid aE\mid bc\mid F\\
 ra&
 h\mid1\mid2\mid r\mid ab\mid cE\mid F\\
 rb&
 ha\mid1\mid2\mid r\mid b\mid cE\mid F\\
 1a,\ 2a&
 hE\mid1\mid2\mid rc\mid a\mid b\mid F\\
 1a,\ 2c&
 h\mid1\mid2\mid r\mid ac\mid bE\mid F\\
 1c,\ 2a&
 h\mid1\mid2\mid r\mid ac\mid bE\mid F\\
 1c,\ 2c&
 ha\mid1\mid2\mid rE\mid b\mid c\mid F .
\end{array}                                               \tag{4.4}
\]

Juxtaposition denotes union.  Every union involving \(E\) is connected
by fullness, and every other nonsingleton union is an edge of one of the
two boundary cliques or one of the protected spokes.  A direct check of
the displayed base edges shows that each row consists of seven pairwise
adjacent connected sets.  Hence every row is a \(K_7\)-model.

The first four rows prove (4.3).  The last four say that optional edges
cannot be present at both \(1\) and \(2\).  This is exactly the asserted
one-centred form. \(\square\)

Choose \(x\in\{1,2\}\) as the common centre (arbitrarily if there is no
optional edge), and let \(y\) be the other vertex.  Lemma 4.1 gives the
proper boundary partition

\[
             \Pi=\{h,c\}\mid\{r,b\}\mid\{y,a\}\mid\{x\}.   \tag{4.5}
\]

The first three blocks are independent by (4.3) and the one-centred
condition.  The last block is a singleton.  The four blocks are pairwise
adjacent because their members \(h,r,y,x\) form the singleton \(K_4\).
Thus (4.5) is an optimal four-colouring of the triangle boundary.

The dependency-free verifier
singleton_triangle_terminal_quotient_verify.py checks all \(2^8\)
possible cross-edge augmentations and independently confirms that exactly
the seven one-centred patterns survive the quotient \(K_7\) test.

There is a second boundary state which is weaker geometrically and is
therefore the one to use first.  Independently of the optional edges, put

\[
 \Pi_2=\{h,c\}\mid\{r,a\}\mid\{1\}\mid\{2\}\mid\{b\}.
                                                               \tag{4.6}
\]

The two pairs are independent by (4.3).  The five blocks are pairwise
adjacent: the singleton vertices \(1,2,b\) form a triangle; both pair
blocks see \(1,2\) through \(h,r\), respectively, and see \(b\) through
\(c,a\); and the two pair blocks see each other through \(hr\) (also
through \(ca\)).  Thus their quotient is \(K_5\).

### Lemma 4.2 (two crossed carriers realize the universal state)

For each \(i\in\{0,1\}\), suppose \(D_i\) contains two vertex-disjoint
connected sets \(X_i,Y_i\) such that

\[
 X_i\sim h,c,\qquad Y_i\sim r,a.                         \tag{4.7}
\]

Then \(G\) is six-colourable.

#### Proof

To colour the closed \(D_0\)-side, use \(X_1,Y_1\) in the opposite
shore and contract

\[
 X_1\cup\{h,c\},\qquad Y_1\cup\{r,a\}.                 \tag{4.8}
\]

These sets are connected and disjoint.  Together with the uncontracted
vertices \(1,2,b\), their images form the \(K_5\) verified immediately
after (4.6).  Colour the resulting proper minor with six colours and
expand the boundary parts of (4.8).  This gives a six-colouring of
\(G[B\cup D_0]\) inducing exactly \(\Pi_2\) on \(B\).  The symmetric
contraction using (X_0,Y_0) gives the same exact state on the closed
(D_1)-side.  Align the five block colours and glue across the two
anticomplete shores.  This six-colours (G), a contradiction. \(\square\)

This replaces a three-packet problem by one ordinary Two Paths demand:
in a surviving triangle endpoint, at least one shore has no two disjoint
carriers for the terminal pairs \((h,c)\) and \((r,a)\).

### Lemma 4.3 (three carriers realize the canonical state)

For \(i\in\{0,1\}\), suppose \(D_i\) contains three pairwise disjoint
connected sets \(R_{i,1},R_{i,2},R_{i,3}\) such that \(R_{i,j}\) is
adjacent to both vertices of the \(j\)-th pair block in (4.5).  If this
holds for both shores, then \(G\) is six-colourable.

#### Proof

To colour the closed \(D_0\)-side, use the three carriers in \(D_1\)
and contract

\[
\begin{aligned}
 Q_1&=R_{1,1}\cup\{h,c\},\\
 Q_2&=R_{1,2}\cup\{r,b\},\\
 Q_3&=R_{1,3}\cup\{y,a\}.
\end{aligned}                                             \tag{4.9}
\]

The sets are connected and disjoint.  They are pairwise adjacent through
the edges \(hr,hy,ry\), and the uncontracted singleton \(x\) is adjacent
to all three through \(xh,xr,xy\).  Their images together with \(x\)
therefore form a \(K_4\) in a proper minor of \(G\).  Six-colour that
minor and expand only the boundary vertices in (4.9).  This gives a
six-colouring of \(G[B\cup D_0]\) inducing exactly the partition
\(\Pi\).

Use the three carriers in \(D_0\) symmetrically to colour
\(G[B\cup D_1]\) with the same exact partition.  Permute the four block
colours so the two restrictions agree on \(B\), and glue across the
two anticomplete shores.  This six-colours \(G\), a contradiction.
\(\square\)

The bounded triangle residue is therefore already an exact two-carrier
transition problem.  The three-carrier state (4.5) remains available as a
second mode, but closure only needs to show that the failed crossed demand
from Lemma 4.2 either reroutes, exposes a nested exact seven-cut, or
produces a boundary state accepted by both unoperated shores.

## 5. Exact one-step polarity at the triangle cut

For \(i\in\{0,1\}\), let \(\mathcal E_i\) be the exact equality
partitions of \(B\) which extend to a six-colouring of
\(G[B\cup D_i]\).

### Proposition 5.1 (triangle-cut transition polarity)

Let \(\mu\) delete a vertex of \(D_i\), delete or contract an edge
internal to \(D_i\), or delete or contract a \(D_i\)-\(B\) edge while
retaining its boundary endpoint as a label.  Then there is a matching
\(M_\mu\) of order one, two, or three in
\(\overline{G[B]}\) whose equality partition \(\Pi_\mu\) satisfies

\[
       \Pi_\mu\in
       \mathcal E_{1-i}\cap\mathcal E_i^\mu
       \setminus\mathcal E_i.                             \tag{5.1}
\]

#### Proof

Apply \(\mu\) to the full graph \(G\) and six-colour the resulting
proper minor.  Restriction to the unchanged shore and to the operated
shore gives the first two memberships in (5.1).  If the same exact
boundary state extended the original \(D_i\)-side, align the block
colours and glue the two shore colourings across \(B\), producing a
six-colouring of \(G\).  Hence the state is rejected by the original
side.

The boundary \(B\) contains the clique \(S\cong K_4\), so it uses at
least four colours.  It has seven vertices and the whole minor uses at
most six colours, so at least one boundary colour repeats.  Since
\(B\) is the union of the two cliques \(S\cong K_4\) and
\(W\cong K_3\), every independent set has order at most two.
Consequently the nonsingleton colour classes are a matching of order
one, two, or three in the complement of \(B\). \(\square\)

Thus the finite transition problem has an exact polarity: every internal
operation on one shore creates a previously rejected cross-clique
matching state which the opposite unoperated shore already accepts.
Static fullness or the canonical partition alone does not encode (5.1).

## 6. The one-extra-edge triangle family is impossible

The web theorem closes one entire infinite subfamily without using the
one-step transition.

### Theorem 6.1 (single-cross-edge closure)

At the triangle endpoint of Corollary 2.3, the set of optional
\(\{1,2\}\)-to-\(\{a,c\}\) edges cannot have order one.

#### Proof

The automorphisms interchanging \(1,2\), and simultaneously interchanging
\((h,a)\) with \((r,c)\), reduce the four possibilities to
\[
                              1a\in E(G).                  \tag{6.1}
\]
Assume that this is the only optional edge.  Put
\[
             C=(h,2,b,a),\qquad Z=\{1,r,c\}.               \tag{6.2}
\]
The graph \(G[C]\) is exactly the displayed four-cycle: its frame edges
are \(h2,2b,ba,ah\), while the diagonals \(hb,2a\) are absent by
Lemma 4.1 and the hypothesis.  Moreover \(G[Z]\) is the path
\(1-r-c\).

Apply the two-shore web-gluing theorem to the two full components
\(D_0,D_1\) and the frame \(C\).  Its connectivity hypothesis is sharp:
\[
                         \kappa(G)=7=|Z|+4.
\]
If the frame tuple is crossless in both shores, the theorem makes
\(G-Z\) planar.  Four-colour \(G-Z\) and use two fresh colours on the
path \(G[Z]\).  This six-colours \(G\), a contradiction.

Hence one shore contains two disjoint crossing carriers.  Let \(X\)
join the portal sets of \(2,a\), and let \(Y\) join those of \(h,b\).
Extend them inside that connected shore, along a shortest connector
split at one edge, so that \(X,Y\) remain disjoint and connected and
become adjacent.  Let \(E\) denote the opposite full shore.  Then
\[
 \{h\}\mid\{1\}\mid\{2\}\mid E\mid\{r,c\}
       \mid(X\cup\{a\})\mid(Y\cup\{b\})                    \tag{6.3}
\]
is a \(K_7\)-model.

For completeness, the first, second, third and fifth bags form a
\(K_4\), using the singleton \(K_4\) on \(h,1,2,r\) and the edge
\(rc\).  The \(X\)-bag sees them through \(ha,1a\), its \(2\)-portal,
and \(ac\); the \(Y\)-bag sees them through its \(h\)-portal,
\(1b,2b\), and \(bc\).  The two crossing bags are adjacent by
construction, and the full shore \(E\) sees every other bag through its
boundary vertex.  Thus all twenty-one adjacencies are present, contrary
to \(K_7\)-minor-freeness. \(\square\)

Consequently the two-connected triangle endpoint has only three boundary
orbits left: no optional edge, or one of the two two-edge stars
\(\{1a,1c\}\), \(\{2a,2c\}\).  This is a closure of an unbounded shore
family: no bound on \(|D_0|\) or \(|D_1|\) was used.

### Theorem 6.2 (two-edge-star closure)

Neither of the two two-edge-star boundary orbits occurs.  Consequently,
at a surviving triangle endpoint there are no optional cross edges.

#### Proof

By symmetry suppose
\[
                         1a,1c\in E(G).                    \tag{6.4}
\]
First suppose one shore has the two crossed carriers from Lemma 4.2.
Contract the two carriers, take a spanning tree of the contracted shore,
and delete an edge on the tree path between their images.  Expanding the
two tree components extends the carriers to a connected covering split
\(D=X\dot\cup Y\), labelled so that
\[
                 X\sim h,c,\qquad Y\sim r,a.               \tag{6.5}
\]
Let \(E\) be the opposite full shore.  If \(X\sim2\), use the seven
bags
\[
 \{h\}\mid\{1\}\mid\{2\}\mid\{r\}\mid E
       \mid(X\cup\{c\})\mid(Y\cup\{a,b\}).                 \tag{6.6}
\]
If \(X\not\sim2\), fullness of the split gives \(Y\sim2\), and instead
use
\[
 \{h\}\mid\{1\}\mid\{2\}\mid\{r\}\mid E
       \mid(X\cup\{b,c\})\mid(Y\cup\{a\}).                 \tag{6.7}
\]
All displayed unions are connected, using \(ab,bc\) where necessary.
The first four bags form the singleton \(K_4\), and \(E\) is adjacent
to every other bag.  In (6.6), the \(Xc\)-bag sees \(h,1,2,r\) through
its \(h\)-portal, \(c1\), its \(2\)-portal, and \(cr\); the \(Yab\)-bag
sees them through \(ah,a1,b2\), and its \(r\)-portal.  In (6.7), the
\(Xbc\)-bag uses its \(h\)-portal, \(b1,b2,cr\), while the \(Ya\)-bag
uses \(ah,a1\), its \(2\)-portal, and its \(r\)-portal.  The last two
bags are adjacent through the split edge (and also through boundary
edges).  Hence either display is a \(K_7\)-model.

It follows that both shores are crossless for the ordered terminal
cycle
\[
                              (h,r,c,a),                    \tag{6.8}
\]
whose opposite pairs are \((h,c)\) and \((r,a)\).  Apply the structural
part of the two-shore web-gluing theorem with
\[
                              Z=\{1,2,b\}.
\]
The two disk webs glue to show that \(G-Z\) is planar and therefore
four-colourable.  But \(Z\) is a triangle.  The audited
triangle/core dichotomy (the \(k=4\) case of Strong Hadwiger) says that
a graph consisting of a triangle over a four-colourable remainder is
either six-colourable or contains a \(K_7\)-minor.  Both conclusions
contradict the standing counterexample.  Thus (6.4), and by symmetry
the other two-edge star, is impossible. \(\square\)

The triangle branch has therefore been reduced, for shores of arbitrary
order, to one exact boundary graph: the disjoint union of the protected
cross edges \(ha,b1,b2,cr\) between the singleton \(K_4\) and carrier
\(K_3\), with no other cross edge.
