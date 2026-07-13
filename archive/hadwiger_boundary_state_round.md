# Boundary-colouring states in the two-component degree-seven cell

This note studies only the two-exterior-component residual at a vertex of
degree seven.  It proves a new two-sided boundary-state lemma and a genuine
Kempe compatibility lemma.  It also gives explicit finite state systems for
both Moser neighbourhoods which satisfy all of the resulting constraints.
Consequently, the hoped-for Moser support-switch conclusion does **not**
follow from boundary-state coverage, pairwise support consistency, and
commuting disjoint Kempe swaps alone.  A further graph-theoretic closure or
rerouting property is needed.

**Subsequent strengthening.**  The two-anchor contraction in
`hadwiger_moser_two_anchor_elimination.md` supplies additional
minor-critical information not represented by these abstract state axioms.
It excludes the classified one-cross-edge extension.  Thus the state
countermodel below remains a valid negative result about the axioms, but the
actual two-component residual has since been reduced to the pure Moser
spindle.

## 1. Setup and state notation

Assume the standing hypothetical counterexample setup.  Thus (G) is a
proper-minor-minimal counterexample to \(\mathrm{HC}_7\), (d_G(v)=7),

\[
 H=G-v,\qquad N=N_G(v),\qquad
 G-N[v]=C_1\mathbin{\dot\cup}C_2,
\]

and each (C_i) is connected and has neighbourhood exactly (N).  Put

\[
 Q=\overline{G[N]}.
\]

We have \(\alpha(G[N])=2\), so (Q) is triangle-free.  For
(i\in\{1,2\}), let

\[
 L_i=H[N\cup C_i].
\]

The equality classes on (N) in any proper six-colouring form a matching
(R\) of (Q): an edge (xy\in R) means that (x,y) have the same colour,
and every vertex not covered by (R) has its own colour.  Since seven
vertices are coloured with at most six colours, (R\ne\varnothing), and
(|R|\le3\).  We call (R) the **boundary state**.

Let \(\mathcal E_i\) be the family of matchings (R\) of (Q) which occur
as the boundary state of a proper six-colouring of (L_i).  Colour names do
not matter: two colourings with the same equality classes differ on (N)
by a permutation of the six colours.

Full accessibility of neighbourhood nonedges gives

\[
 \{e\}\in\mathcal E_1\cap\mathcal E_2
 \quad\hbox{for every }e\in E(Q).                 \tag{1.1}
\]

On the other hand,

\[
 \mathcal E_1\cap\mathcal E_2
 \text{ contains no state of size two or three}. \tag{1.2}
\]

Indeed, side colourings with the same state can be made identical on (N)
by a colour permutation and then glued.  A state of size at least two uses
at most five colours on (N), so the glued colouring of (H) extends to
(v), contrary to \(\chi(G)=7\).

## 2. Contracting the other component: both side families cover (Q)

The following strengthens (1.1)--(1.2) and is independent of Kempe-chain
choices.

### Lemma 2.1 (two-sided higher-state cover)

For each (i\in\{1,2\}) and every edge (e\in E(Q)), there is a state
(R\in\mathcal E_i) such that

\[
 e\in R,\qquad 2\le |R|\le3.                       \tag{2.1}
\]

Thus the two disjoint families

\[
 \mathcal F_i=\{R\in\mathcal E_i:|R|\ge2\}
\]

are each covers of the ground set (E(Q)) by two- and three-edge matchings
of (Q).

#### Proof

Write (e=xy), and let (j\ne i).  In (G), contract the connected star
(G[\{v,x,y\}]) to a vertex (q), and contract the connected component
(C_j) to a vertex (h).  Call the resulting proper minor (J).  It is
six-colourable.

The vertices (q,h) are adjacent: both (x) and (y) have neighbours in
(C_j).  Moreover, both (q) and (h) are adjacent to every vertex of

\[
 U=N-\{x,y\}.
\]

For (q), use the old edges from (v); for (h), use
(N_G(C_j)=N).  Hence (q,h) have distinct colours and (U) avoids both
of those colours.  It follows that (U) uses at most four colours.

Delete (h), uncontract the star (\{v,x,y\}), give (x,y) the colour of
(q), and then delete (v).  This is proper because
(xy\notin E(G)), and it colours exactly (L_i).  On its
boundary, (xy) is one equality pair and the five vertices of (U) use at
most four colours.  Thus at least one further equality pair occurs.  Since
\(\alpha(G[N])=2\), all equality classes have size at most two and hence
form a matching.  Its size is two or three and it contains (e), as
claimed. \(\square\)

The important point is that Lemma 2.1 does not say which larger state is
obtained for a given (e), and it gives no Kempe reconfiguration between
that colouring and a singleton-state colouring.

## 3. What exclusive support really implies about states

Fix a global six-colouring of (H) with singleton state \(\{r\}\), where
(r=xy\in E(Q)).  If (e=ab\in E(Q)) is disjoint from (r), the four
vertices (a,b,x,y) lie in distinct equality pairs except for (x,y).
Say that side (C_i) supports (e) when (a,b) lie in the same
bichromatic component of (L_i) in their two colours.

### Lemma 3.1 (an unsupported pair produces a double state)

If (C_i) does not support (e), then

\[
 \{r,e\}\in\mathcal E_i.                            \tag{3.1}
\]

#### Proof

The two roots lie in different components of the subgraph of (L_i)
induced by their two colours.  Swap those colours on the component
containing one root.  On (N), this merges exactly the two endpoints of
(e); the repeated pair (r) is untouched. \(\square\)

There is no valid converse to Lemma 3.1 using extension sets alone: a
double state may be realised by a completely different interior colouring.

### Corollary 3.2 (no reversal of exclusive support)

Suppose that, in some global colouring with singleton state \(\{r\}\), the
edge (e) is supported only by (C_1).  Then

\[
 \{r,e\}\in\mathcal E_2\setminus\mathcal E_1.       \tag{3.2}
\]

Consequently, in every global colouring with singleton state \(\{e\}\),
the edge (r) is supported by (C_1).  The analogous assertion holds with
the two sides interchanged.

#### Proof

The first membership follows from Lemma 3.1, and nonmembership follows from
(1.2).  If a colouring with singleton state \(\{e\}\) failed to support
(r) in (C_1), Lemma 3.1 would put the same unordered double state
(\{r,e\}) in \(\mathcal E_1\), a contradiction. \(\square\)

Thus opposite exclusive orientations cannot occur at the two ends of the
same unordered pair of disjoint (Q)-edges.  They may consistently have
the same orientation.

There is one useful three-state closure.

### Lemma 3.3 (commuting disjoint swaps)

Let (r,e,f) be a three-edge matching of (Q).  In a global colouring
with singleton state \(\{r\}\), if neither (e) nor (f) is supported by
(C_i), then

\[
 \{r,e,f\}\in\mathcal E_i.                          \tag{3.3}
\]

#### Proof

The two Kempe swaps from Lemma 3.1 use four distinct colours, since (e)
and (f) are vertex-disjoint.  Their bichromatic vertex sets are disjoint,
so the swaps commute.  Performing both produces the displayed triple
state. \(\square\)

## 4. The disjointness graph of neighbourhood nonedges

Let (D(Q)) be the graph whose vertices are the edges of (Q), with two
vertices adjacent exactly when the corresponding (Q)-edges are
vertex-disjoint.  Thus:

* vertices of (D(Q)) are singleton states;
* edges of (D(Q)) are double states; and
* triangles of (D(Q)) are triple states.

For the pure Moser spindle,

\[
 E(Q)=\{ap,aq,bd,be,bq,cd,ce,cq,dp,ep\}.             \tag{4.1}
\]

The degrees in the displayed order are

\[
 6,6,5,5,5,5,5,5,5,5.                               \tag{4.2}
\]

For (M+bd), remove (bd) from (4.1), and the degrees in the resulting
order

\[
 ap,aq,be,bq,cd,ce,cq,dp,ep
\]

are

\[
 5,5,5,5,5,4,4,5,4.                                 \tag{4.3}
\]

These tables follow directly by listing the (Q)-edges disjoint from each
given edge.

## 5. Explicit state countermodel for (G[N]=M)

In (D(Q)), colour the following five edges red:

\[
 \mathcal R=
 \{ap\!-!cq,\ aq\!-!ep,\ bd\!-!ce,\
   be\!-!dp,\ bq\!-!cd\}.                          \tag{5.1}
\]

They form a perfect matching of the ten vertices of (D(Q)).  Colour every
other edge of (D(Q)) blue.  By (4.2), every vertex is incident with one
red edge and at least four blue edges.

Interpret a red edge (r-e) as saying that (e) is supported only by
(C_1) in the singleton state (r), and also that (r) is supported only
by (C_1) in the singleton state (e).  Interpret blue symmetrically with
(C_2).  Therefore every singleton state has oppositely exclusive missing
edges, while Corollary 3.2 is respected because the label is attached to
the unordered edge (r-e).

Now define abstract extension families

\[
\begin{aligned}
 \mathcal A_1={}&
   \{\{r\}:r\in E(Q)\}
   \cup\{\{r,e\}:r-e\text{ is blue}\}
   \cup\{T:T\text{ is a three-edge matching of }Q\},\\
 \mathcal A_2={}&
   \{\{r\}:r\in E(Q)\}
   \cup\{\{r,e\}:r-e\text{ is red}\}.
                                                               \tag{5.2}
\end{aligned}
\]

Then:

1. their common states are exactly all singleton states;
2. their higher-state parts are disjoint;
3. each higher-state part covers every edge of (Q): the red edges form
   an edge cover of (D(Q)), and the blue edges do also;
4. red support means that the unsupported side is side 2, which contains
   the corresponding red double state; blue support similarly points to
   side 1, exactly as Lemma 3.1 requires; and
5. Lemma 3.3 is respected.  Indeed, a triangle of (D(Q)) contains at
   most one red edge because the red graph is a matching.  It therefore
   has two blue edges sharing a vertex.  The two corresponding side-1
   swaps force its triple state, and every triple state was put in
   \(\mathcal A_1\).  No triangle has two red edges, so no side-2 triple
   state is forced.

Thus all pairwise and commuting-swap constraints are simultaneously
consistent with an opposite-exclusive support pattern in every row.

## 6. Explicit state countermodel for (G[N]=M+bd)

Here use the red edge cover

\[
 \mathcal R^+=
 \{ap\!-!cd,\ ap\!-!cq,\ aq\!-!ep,\
   be\!-!dp,\ bq\!-!ce\}.                          \tag{6.1}
\]

It covers all nine vertices of (D(Q)).  The only vertex of red degree two
is (ap); all others have red degree one.  Equations (4.3) show that every
vertex also has a blue incident edge.

Moreover, the two red neighbours (cd,cq) of (ap) are not adjacent in
(D(Q)), because the (Q)-edges (cd,cq) meet at (c).  Hence no
triangle of (D(Q)) contains two red edges.  Defining
\(\mathcal A_1,\mathcal A_2\) by (5.2), with \(\mathcal R^+\) in place of
\(\mathcal R\), gives all five properties listed after (5.2).  In
particular, the red and blue double-state families are disjoint edge covers
of (E(Q)), and all forced commuting-swap triple states lie only on side
1.

This is an explicit negative answer to the finite matching-hypergraph
test: Lemma 2.1 and disjointness of the two larger-state families do not
contradict either Moser residual.

## 7. Proper-colouring audit and the realization boundary

Every state used above is a genuine proper boundary colouring.  A matching
(R) of (Q) is coloured by assigning one colour to the two ends of each
edge of (R) and distinct colours to all other vertices.  It uses
(7-|R|\in\{4,5,6\}) colours.  Equal vertices are nonadjacent in (G[N]),
so the colouring is proper.  Thus the countermodels are not using a
formally impossible boundary partition.

There is also a standard gadget-realization observation, though it must not
be confused with realization of the whole counterexample structure.

### Proposition 7.1 (extension relations are graph-realizable)

Each colour-permutation-invariant relation \(\mathcal A_i\) in (5.2) can
be realised as the exact six-colour boundary-extension relation of a finite
simple graph gadget.  Its interior can be made connected and adjacent
collectively to every vertex of (N).

#### Justification

Use the finite primitive-positive Galois theorem for the relational
structure \(([6];\ne)\).  Every polymorphism of \(\ne\) on a set of size
at least three is a projection followed by a permutation.  One way to see
this is to view a polymorphism as a proper six-colouring of a categorical
power of (K_6): the direct-product Erdős--Ko--Rado theorem says its maximum
independent sets are coordinate fibres, and the six colour fibres must
partition by one common coordinate.  Hence every relation invariant under
simultaneous colour permutations is primitive-positive definable from
\(\ne\).  Such a definition is exactly a graph-colouring gadget with the
free variables as boundary vertices.  If equality atoms occur, replace
(x=y) by five new vertices inducing (K_5), each adjacent to both (x)
and (y); this gadget extends precisely when (x,y) have the same colour.

Finally, connect distinct interior components by fresh length-two paths.
For any already chosen endpoint colours, the middle vertex avoids at most
two colours, so this changes no extension.  Choose an interior anchor and,
for each (n\in N), add a fresh vertex adjacent to (n) and the anchor;
again it avoids at most two colours.  The interior is then connected and
has neighbourhood all of (N), without changing the boundary relation.
\(\square\)

Gluing gadgets for \(\mathcal A_1,\mathcal A_2\) along (N), and adding a
vertex (v) complete to (N), gives an actual seven-chromatic graph in
which:

* there are exactly two connected exterior pieces, each attached to every
  vertex of (N);
* every singleton boundary state is globally accessible; and
* no larger boundary state is globally accessible.

This realization is only an audit of the colouring-state data.  It is not
claimed to be seven-connected, contraction-critical, or (K_7)-minor-free,
and Proposition 7.1 does not prescribe the internal Kempe transition graph.
Accordingly, it is not a counterexample to Hadwiger and not a graph-level
disproof of a possible deeper Moser support-switch theorem.

## 8. The tempting reconfiguration converse is false even on a Moser side

The nonconverse warning after Lemma 3.1 is essential, not merely logical
caution.  Here is a small explicit side gadget.

Start with three terminals (X,A,B), with (AB) absent and (XA,XB)
present, and three internal vertices (s,t,w).  Add the edges

\[
 Xt,\ As,\ At,\ Bs,\ Bw,\ sw,\ tw                 \tag{8.1}
\]

in addition to (XA,XB).  Call this six-vertex graph (P).  With only
three available colours it has the following two forced colourings.

* If (X,A,B) have three distinct colours (0,1,2), respectively, then
  
  \[
  s=0,\qquad t=2,\qquad w=1.                       \tag{8.2}
  \]
  
  In particular,
  
  \[
  A-t-w-B                                           \tag{8.3}
  \]
  
  is a bichromatic (A)-(B) path.
* If (X) has colour (0) and (A,B) both have colour (1), then
  
  \[
  s=t=2,\qquad w=0,                                \tag{8.4}
  \]
  
  is a proper colouring.

Both assertions follow immediately from the two-colour exclusions at
(t), then (s,w); the displayed colourings are unique once the terminal
colours are fixed.

To make this a six-colour side gadget, add a triangle
(Z=\{z_3,z_4,z_5\}) complete to all six vertices of (P).  In a
six-colouring, (Z) consumes three colours and forces (P) to use the
other three.  Hence (8.2)--(8.4) remain forced.

This gadget embeds with the **exact** residual boundary graphs.

* For (G[N]=M), take
  
  \[
  X=a,\qquad A=b,\qquad B=d,\qquad Y=p.
  \]
  
  The required edges (ab,ad) are in (M), while (ap,bd) are not.
* For (G[N]=M+bd), take
  
  \[
  X=a,\qquad A=b,\qquad B=e,\qquad Y=p.
  \]
  
  Here (ab,ae) are edges and (ap,be) are nonedges.

Add all prescribed edges of the relevant boundary graph.  For each boundary
vertex not already adjacent to the interior, add a fresh vertex adjacent to
that boundary vertex and to (z_3).  These fresh vertices impose no
restriction, since each avoids at most two colours.  The full interior is
connected and has neighbourhood exactly (N).

In the first embedding, the singleton state \(\{ap\}\) extends with
(a,p) coloured (0), (b) coloured (1), (d) coloured (2), and
(c,e,q) receiving colours (3,4,5).  In **every** extension, the triangle
(Z) uses colours (3,4,5), (8.2) is forced, and (b,d) are connected by
the bichromatic path (8.3).  Nevertheless the double state
\(\{ap,bd\}\) also extends, by (8.4).  The second embedding gives the same
conclusion for the states \(\{ap\}\) and \(\{ap,be\}\).

Consequently, even with (G[N]) exactly one of the two Moser residuals,
with a connected side interior and (N(C)=N), the implication

\[
 \{r\},\{r,e\}\in\mathcal E_i
 \quad\Longrightarrow\quad
 \text{some singleton-state extension leaves (e) unsupported}
                                                               \tag{8.5}
\]

is false.  Any valid reconfiguration statement must use additional global
hypotheses such as contraction-criticality, seven-connectivity, or minor
exclusion; side extension data and full boundary attachment do not suffice.

## 9. Exact consequence for the next attack

The valid new positive information is Lemma 2.1: for each side separately,
larger extendible states cover every neighbourhood nonedge.  The finite
models (5.1)--(6.1) show that the following information still does not
force a contradiction:

1. all singleton states occur on both sides;
2. no double or triple state occurs on both sides;
3. the larger states on each side cover all of (E(Q));
4. every singleton colouring has exclusive supports of both types;
5. exclusive support cannot reverse across a double state; and
6. swaps on disjoint colour pairs commute.

Therefore the missing mechanism must use information not present in the
two side extension relations.  The first natural reconfiguration converse
is ruled out explicitly by Section 8.  A sufficient next lemma must instead
be a genuinely global assertion, for example:

* a contraction-critical exchange that couples the special colouring from
  Lemma 2.1 to the star-contraction colouring giving full accessibility; or
* a graph/minor rerouting lemma using seven-connectivity or
  \(\eta(G)=6\), neither of which is recorded by the finite state families.

Without such an additional assertion, the Moser support-switch route is
blocked by the explicit red/blue systems above.
