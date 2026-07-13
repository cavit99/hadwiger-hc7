# Moser four-corner exact-state exchange

**Status:** proved and independently audited.

The theorem uses one four-port linkage-or-disk call on the literal Moser
corners `1,2,3,4`.  Its two outcomes give the two complementary matchings
`13|24` and `14|23`; either matching supports the same proper-minor equality
state and a six-colouring contradiction.  No favourable five-root crossing
or synchronization of several rural embeddings is required.

## 1. Fixed Moser boundary

Let
\[
 S=\{0,1,2,3,4,5,6\},\qquad
 E(G[S])=\{01,02,03,04,12,16,26,34,35,45,56\}.
\]
Put \(L=\{1,2\}\) and \(R=\{3,4\}\).  Every pair containing one
vertex of `L` and one of `R` is independent.  Moreover, each such pair
dominates the other five boundary vertices: `12` and `34` dominate the
complementary corners, `0` sees every corner, `5` sees both vertices of `R`,
and `6` sees both vertices of `L`.

## 2. Exact hypothesis: a four-corner rural carrier

Let \(G\) be a seven-connected, strongly 7-contraction-critical,
\(K_7\)-minor-free graph, meaning that every proper minor is six-colourable.
Let
\(v\in V(G)\) have \(N(v)=S\) with the Moser graph above, and suppose
\[
                         G-N[v]=C\mathbin{\dot\cup}D
\]
has exactly two nonempty connected components.
Seven-connectivity implies that both are \(S\)-full.

Assume that for some orders \((a,x)\) of \(L\) and \((b,y)\) of \(R\),
the shore \(D\) supplies two vertex-disjoint connected subgraphs \(X,Y\)
such that
\[
 \begin{aligned}
  &X\text{ has neighbours at both }a,y,\\
  &Y\text{ has neighbours at both }x,b,\\
  &E(X,Y)\ne\varnothing.
 \end{aligned}                                      \tag{2}
\]
This is the literal carrier conclusion of a **literal two-connected
four-root disk closure** with boundary order \(a,x,b,y\): its two
complementary facial arcs join the noncrossing pairs \(a-y\) and \(x-b\),
and connectedness of the shore permits an adjacent enlargement.  A bare
cyclic order of possibly overlapping portal classes is not enough.  Stating
(2) separately avoids that unsafe inference.

### Lemma 2.1 (the literal rural disk does supply (2))

Assume additionally that \(|D|\ge3\), \(D\) is two-connected, and
\[
 Q=G[D\cup\{a,x,b,y\}]
\]
has a disk embedding with the four literal roots on its boundary in cyclic
order \(a,x,b,y\).  Then (2) holds.

#### Proof

First,
\[
 |N_D(\{a,x\})|\ge2,\qquad |N_D(\{b,y\})|\ge2.       \tag{2.4}
\]
For if, say, the first union had order at most one, then
\[
 N_D(\{a,x\})\cup(S-\{a,x\})
\]
would have order at most six and would separate the nonempty set
\(D-N_D(\{a,x\})\) from \(v\) and the opposite component.  Nonemptiness
uses \(|D|\ge3\).  This contradicts seven-connectivity.  The other
inequality is identical.

The literal Moser edges \(ax=12\) and \(by=34\), together with (2.4),
make \(Q\) two-connected by the two-ear argument: start from the
two-connected graph \(D\), choose distinct representatives of the two
nonempty portal sets for \(a,x\), add the ear through the literal edge
\(ax\), and repeat for \(b,y\); (2.4) is exactly what guarantees distinct
ends for each ear.  The
outer facial boundary is therefore a cycle.  In the cyclic order
\(a,x,b,y\), the pairs \(a-y\) and \(x-b\) are consecutive.  Both are
Moser nonedges.  The two open facial arcs between these pairs have disjoint,
nonempty, connected interiors in \(D\), contacting respectively
\(\{a,y\}\) and \(\{x,b\}\).  The audited adjacent-enlargement argument
inside connected \(D\) makes the two interiors adjacent without destroying
their disjointness or contacts.  These are \(X,Y\) in (2). \(\square\)

## 3. Four-corner exact-state exchange theorem

**Theorem 3.1.**  The configuration in Section 2 is impossible.
Equivalently, a literal four-corner rural carrier on either shore of the
two-component Moser cell forces a six-colouring of \(G\).

### Proof

Set
\[
                   r=\{a,y\},\qquad e=\{x,b\}.
\]
Both \(r\) and \(e\) are independent: every edge between \(L\) and \(R\)
is absent in the Moser graph.

Contract the connected set \(\{v\}\cup r\) to a vertex \(z_r\), and
contract the disjoint connected set \(C\cup e\) to a vertex \(z_e\).
The latter set is connected because \(C\) is connected and \(S\)-full.
The two contracted sets are adjacent (already through the edges from \(v\)
to \(e\)).  This is a proper minor of \(G\), hence is six-colourable.
Restrict such a colouring to \(G[D\cup S]\).

On the literal boundary, the colour blocks containing \(r\) and \(e\) are
exactly \(r\) and \(e\): every vertex of \(S-r\) is adjacent to \(z_r\),
and every vertex of \(S-e\) is adjacent to \(z_e\).  The remaining boundary
vertices are \(0,5,6\).  Here \(56\in E(G)\), whereas \(05,06\notin E(G)\).
All three are adjacent to both contracted representatives (through \(v\)
on the \(r\)-side and through the \(S\)-full component \(C\) on the
\(e\)-side), so none can reuse either contracted colour.  Thus \(5,6\)
have distinct colours, while \(0\) is either new or reuses exactly one of
their colours.  The induced equality partition is therefore one of
\[
 \begin{aligned}
 R_0&=\{r,e,\{0\},\{5\},\{6\}\},\\
 R_5&=\{r,e,\{0,5\},\{6\}\},\\
 R_6&=\{r,e,\{0,6\},\{5\}\}.             \tag{3}
 \end{aligned}
\]
These are equality blocks rather than named colours; the labels \(R_5,R_6\)
record which of \(5,6\) shares the colour of \(0\).

We now realize the same partition on the opposite side by proper-minor
contractions.  Contract \(X\cup r\) and \(Y\cup e\).  These are disjoint
connected sets, and they are adjacent by (2).  For \(q\in\{0,5,6\}\), put
\[
                  I_0=\{0\},\quad I_5=\{0,5\},\quad I_6=\{0,6\},
\]
and also contract the connected star \(\{v\}\cup I_q\).  The resulting
three contracted vertices, together with the remaining singleton vertices
of \(\{0,5,6\}-I_q\), form a clique: the two carrier contractions are
adjacent; each sees \(5\) through its \(R\)-corner and \(6\) through its
\(L\)-corner; the star sees every other representative through \(v\); and
\(56\) is an edge.  More explicitly, for \(q=0\) the five representatives
are a \(K_5\), while for \(q=5,6\) the four representatives are a \(K_4\).

Colour this proper minor with six colours.  Its restriction to
\(G[C\cup S]\) has exactly the corresponding partition \(R_q\) on literal
\(S\): every boundary vertex outside a contracted block is adjacent to the
representative of that block, so no unintended equality is possible, while
the displayed representative clique forces all block colours to differ.

Choose \(q\) matching the partition obtained in (3), permute the six colours
on one shore so equal literal blocks have equal colours, and glue the two
shore colourings along \(S\).  At most five colours occur on \(S\), so give
\(v\) a sixth colour absent from \(S\).  This is a proper six-colouring of
\(G\), contradicting 7-contraction-criticality.  \(\square\)

## 4. Four-port closure of every two-connected full shore

**Theorem 4.1.**  In the setting of Section 2, if one of the two
open shores, say \(D\), has order at least three and is two-connected, then
the configuration is impossible.  In particular this conclusion does not
require a favourable crossing in any of the four five-root frames.

### Proof

Apply the audited seven-boundary four-port linkage-or-disk theorem
(`hc7_moser_crossing_carrier.md`, Theorem 4.1) to the ordered literal
roots
\[
                           1,2,3,4.                     \tag{4.1}
\]
Its hypotheses hold because \(D\) is a component of \(G-S\), all four roots
have neighbours in the \(S\)-full component \(D\), and the opposite side
contains at least \(C\cup\{v\}\).

In the linkage outcome there are vertex-disjoint paths \(P_{13},P_{24}\)
whose interiors lie in \(D\).  Since \(13,24\) are literal Moser nonedges,
both interiors are nonempty connected sets.  The audited adjacent-enlargement
lemma in connected \(D\) turns them into disjoint adjacent connected carriers
\(X,Y\), still contacting respectively
\[
                          \{1,3\},\qquad\{2,4\}.        \tag{4.2}
\]
Use Section 3 with
\[
                  (a,x)=(1,2),\qquad (b,y)=(4,3).
\]
Then \(r=\{a,y\}=\{1,3\}\) and
\(e=\{x,b\}=\{2,4\}\), so (4.2) is exactly carrier hypothesis (2), and
Section 3 gives a six-colouring contradiction.

In the rural outcome,
\[
                   Q=G[D\cup\{1,2,3,4\}]
\]
has a disk embedding with its literal roots on the boundary in cyclic order
\(1,2,3,4\).  Lemma 2.1, with
\[
                  (a,x,b,y)=(1,2,3,4),
\]
supplies disjoint adjacent carriers contacting respectively
\[
                          \{1,4\},\qquad\{2,3\}.        \tag{4.3}
\]
These again satisfy (2), now for
\(r=\{1,4\}\), \(e=\{2,3\}\).  Section 3 gives the same six-colouring
contradiction.  The two outcomes are exhaustive. \(\square\)

The theorem eliminates an infinite family and includes a triangular shore.
It also identifies why the
previous multi-frame sign analysis was unnecessarily fine: the two outcomes
of one four-corner call return the two perfect matchings
\[
                  (13\mid24)\quad\text{or}\quad(14\mid23),
\]
and every block in either matching is an independent left-right pair in the
Moser boundary.  Exact-state reflection is insensitive to which matching is
returned.

Theorem 4.1 bypasses the former multi-frame extraction problem entirely:
the four-port theorem itself returns either literal carriers or one literal
four-root disk embedding.  No compatibility theorem for several portal
orders is needed for a two-connected shore of order at least three.
