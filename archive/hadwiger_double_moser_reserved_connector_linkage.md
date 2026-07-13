# The five-connected double-Moser remainder: reserved connector or rural lock

## 1. Setting and the false static shortcut

Use the double-Moser endpoint with adjacent degree-seven vertices (u,v),
common roots

\[
 X=\{x_1,x_2,x_3,x_4\},\qquad
 H_1=\{x_1,x_2\},\quad H_2=\{x_3,x_4\},
\]

and outer edges (A=\{a,b\}), (P=\{p,q\}), labelled so that

\[
 aH_1, bH_2, qH_1, pH_2
\]

are complete.  Put

\[
                         H=G-\{u,v\}.                         \tag{1.1}
\]

Since (G) is seven-connected, (H) is five-connected.  It is
nonplanar: otherwise the Four Colour Theorem colours (H) with four
colours and the two adjacent vertices (u,v) receive two new colours.
Thus Jung's theorem makes (H) two-linked.

Two-linkedness alone is not the missing theorem.  The exact conservative
probe `double_moser_clean_2linkage_probe.cpp` checks every clean
two-linkage on four distinct interface terminals and finds

```text
positive=0 total=210
```

Even three pairwise internally disjoint clean paths with six distinct
interface ends do not suffice: `double_moser_three_detour_probe.cpp`
checks all 420 matchings and again finds no (K_7)-model.  These are
falsification checks only.  The positive statement below retains the
graph after deleting a connector, rather than contracting every path to
an edge.

## 2. A connector which reserves a rooted (K_4)

A **clean cross connector** is a path (T) of one of the types

\[
                         a\mathord{-}p,qquad b\mathord{-}q       \tag{2.1}
\]

whose internal vertices lie in the common body (R).  Such a connector
always exists because (R) is connected and is adjacent to all eight
interface labels.  We may and do choose (T) shortest in the induced
graph on (R) and its two ends; it is then induced.

### Lemma 2.1 (reserved-connector certificate)

Let (T) be a clean (a)-(p) connector and put

\[
                         L=H-V(T).                              \tag{2.2}
\]

If (L) contains an (X)-rooted (K_4)-model, then (G) contains a
(K_7)-minor.  The symmetric statement holds for a clean (b)-(q)
connector.

#### Proof

Let (B_i) be the rooted branch bag containing (x_i).  The seven bags

\[
                 \{u\},\quad\{v\},\quad V(T),\quad
                 B_1,B_2,B_3,B_4                              \tag{2.3}
\]

are disjoint and connected.  The first two are adjacent and each sees
all four rooted bags.  The connector bag sees (u) through (p), sees
(v) through (a), sees (B_1,B_2) through the edges from (a), and
sees (B_3,B_4) through the edges from (p).  The rooted bags are
pairwise adjacent.  Hence (2.3) is a (K_7)-model.  \(\square\)

This certificate is label-preserving and uses the whole connector as
the seventh branch bag.  It is exactly the information destroyed by the
clean-linkage quotient.

### Theorem 2.2 (reserved connector or rural/adhesion obstruction)

For every clean cross connector (T), at least one of the following
holds.

1. (G) contains a (K_7)-minor.
2. (L=H-V(T)) has a vertex separator of order at most three.
3. (L) is planar and (x_1,x_2,x_3,x_4) are incident with one face.

#### Proof

If (L) has no separator of order at most three, it is four-connected.
The rooted-(K_4) theorem of Fabila-Monroy and Wood says that four
specified vertices in a four-connected graph root a (K_4)-minor
unless the graph is planar and the four roots are cofacial.  In the
rooted-minor outcome apply Lemma 2.1; the other outcome is item 3.
\(\square\)

This is the corrected infinite consequence of five-connectivity and
two-linkedness.  Failure of the reserved minor is not another arbitrary
path pattern: it is a three-adhesion or a four-terminal disk web.

## 3. What a small adhesion must look like

The low-connectivity outcome still retains strong ambient connectivity.

### Lemma 3.1 (portal load on every blocker component)

Let (S\subseteq V(L)), (|S|\le3), and let (C) be a component of
(L-S), where (L-S) has at least two components.  Then

\[
                         |N_{V(T)}(C)|\ge 5-|S|.                 \tag{3.1}
\]

In particular, behind a three-separator every component has at least two
distinct attachments to the deleted connector.

#### Proof

Every neighbour of (C) outside (C) lies in

\[
                         S\cup V(T)\cup\{u,v\}.                 \tag{3.2}
\]

Indeed (H=L\dot\cup V(T)), and the only two vertices of (G-H) are
(u,v).  Therefore

\[
 |N_G(C)|\le |S|+|N_{V(T)}(C)|+2.
\]

The other component of (L-S) lies beyond this neighbourhood, so
seven-connectivity gives (|N_G(C)|\ge7), which is (3.1).  \(\square\)

If equality holds throughout, the displayed neighbourhood is a proper
exact seven-cut.  Otherwise the component has surplus ordered portals on
the induced path (T).  Thus item 2 of Theorem 2.2 is precisely a
two-shore path-bridge exchange problem, not a pendant-piece exception.

## 4. Parity and the planar palette lock

The planar outcome contains additional colouring information which is
lost in a purely topological web statement.

For a clean (a)-(p) connector (T), the graph induced by

\[
                         V(T)\cup\{u,v\}                        \tag{4.1}
\]

is the chordless cycle

\[
                         u v a T p u.                            \tag{4.2}
\]

The absence of chords uses the exact degree-seven neighbourhoods at
(u,v) and the choice of (T) as a shortest path in
(G[R\cup\{a,p\}]).

### Theorem 4.1 (planar parity lock)

Suppose outcome 3 of Theorem 2.2 holds for a clean (a)-(p)
connector (T).

1. The path (T) has even length.
2. Every proper four-colouring of (L) uses all four colours on each of

   \[
                         X\cup\{q\},\qquad X\cup\{b\}.          \tag{4.3}
   \]

3. There is a proper four-colouring of (L) in which (X) uses
   exactly three colours and (q,b) both receive the fourth colour.
   Consequently (qb\notin E(G)).

The symmetric clean (b)-(q) connector forces
(ap\notin E(G)) and the analogous equality state.

#### Proof

The cycle (4.2) has (|E(T)|+3) edges.  If (T) had odd length, this
cycle would be even.  Four-colour the planar graph (L) and two-colour
the cycle with two fresh colours, producing a six-colouring of (G), a
contradiction.  Hence (T) has even length.

Let (c) be any proper four-colouring of (L).  If a colour
\(\alpha\) is absent from (X\cup\{q\}), give (u) colour
\(\alpha\).  Removing (u) from the odd cycle (4.2) leaves a path;
colour that path with two fresh colours.  This again six-colours (G).
Therefore (X\cup\{q\}) uses all four colours.  Removing (v) instead
shows in the same way that (X\cup\{b\}) uses all four.

Finally add inside the common root face a new vertex adjacent to all four
vertices of (X).  The augmented graph is planar, so the Four Colour
Theorem gives a colouring in which (X) avoids the new vertex's colour,
say \(\alpha\).  By (4.3), (X) must use the other three colours and
both (q,b) must receive \(\alpha\).  Properness then gives
(qb\notin E(G)).  \(\square\)

This is a finite-boundary state forced by an unbounded planar web: the
two opposite outer vertices are equal in a canonical face-centre
colouring, while the four common roots use exactly the other three
colours.

The quantifier over **every** four-colouring gives a further Kempe
constraint which is absent from a generic rural expansion.

### Lemma 4.2 (two mandatory planar Kempe detours)

Let (c) be any colouring supplied by the face-centre construction in
Theorem 4.1.  Write

\[
 c(q)=c(b)=\alpha,
\]

and let \(\sigma,\tau\) be the two colours which occur exactly once on
(X) (the third non-\(\alpha\) colour occurs twice).  Then, for each

\[
                         \beta\in\{\sigma,\tau\},                \tag{4.4}
\]

the vertices (q,b) lie in the same \(\{\alpha,\beta\}\)-component
of (L).  Hence (L) contains two actual (q)-(b) Kempe paths,
one for each singleton root colour; paths chosen for the two colours can
intersect only in vertices of colour \(\alpha\).

#### Proof

Suppose (q,b) lie in different \(\{\alpha,\beta\}\)-components and
switch the component containing (q).  The resulting colouring is
another proper four-colouring of (L), so both saturation conclusions
in (4.3) still hold.

After the switch, (q) has colour \(\beta\) and (b) still has colour
\(\alpha\).  For (X\cup\{q\}) to use all four colours, the switched
component must contain a \(\beta\)-coloured root, which changes to
\(\alpha\).  For (X\cup\{b\}) to use all four, some
\(\beta\)-coloured root must remain outside the switched component.
This is impossible when \(\beta\) occurs exactly once on (X).
Thus (q,b) lie in the same component.  The final intersection claim
follows because the two bichromatic subgraphs have only colour
\(\alpha\) in common.  \(\square\)

So even the planar outcome supplies two typed detours across the deleted
connector.  Contracting those detours to parallel (q b)-edges is again
insufficient; their placement in the disk web is the information needed
for the next exchange.

There is also a uniform saturation statement along the entire deleted
cycle, not only at (u,v).

### Lemma 4.3 (every cycle vertex is four-saturated into the web)

Let

\[
                         C_T=uv a T p u
\]

be the odd cycle from Theorem 4.1.  For every (z\in V(C_T)) and every
proper four-colouring (c) of (L), all four colours occur on

\[
                         N_L(z).                                \tag{4.5}
\]

Consequently (L) has, for every (z\in V(C_T)), a (K_4)-model
whose four bags all meet (N_L(z)); in particular (L+z) contains a
(K_5)-minor with singleton bag (z).

#### Proof

If a colour \(\alpha\) were absent from (N_L(z)), give (z) colour
\(\alpha\).  Deleting (z) from the odd chordless cycle (C_T) leaves
a path, which can be coloured with two fresh colours.  Together with
(c), this is a six-colouring of (G), a contradiction.  This proves
(4.5).

The set (N_L(z)) is therefore four-saturating in the four-colourable
graph (L).  The proved four-colour case of the Strong Hadwiger theorem
gives a (K_4)-model every bag of which meets (N_L(z)).  Adding the
singleton (z) gives the last assertion.  \(\square\)

For the face-centre colouring, (4.5) says more concretely that every
vertex of the deleted Kempe carrier has a neighbour in the colour class
which is absent from (X).  Thus a planar blocker is a path all of whose
vertices are colour-saturated into the surrounding disk, rather than an
irrelevant chord across one face.

The planar alternative can now be hit with an independent linkage.  This
time the second deletion cannot leave another disk alternative.

### Theorem 4.4 (second detour forces a three-adhesion)

Assume the planar outcome of Theorem 4.1 for a clean (a)-(p)
connector (T).  There is a (q)-(b) path (Q\subseteq L) whose
internal vertices avoid

\[
                         Y=\{x_1,x_2,x_3\},                    \tag{4.6}
\]

such that, unless (G) contains a (K_7)-minor, the graph

\[
                         M=L-(V(Q)-\{q\})                      \tag{4.7}
\]

has a vertex separator of order at most three.

#### Proof

The planar blocker (L) is four-connected.  Menger's theorem gives
four internally vertex-disjoint (q)-(b) paths.  At most three of
them meet the three-element set (Y) internally, so choose (Q)
avoiding (Y).

Suppose (M) contains a (K_4)-model rooted at

\[
                         \{q,x_1,x_2,x_3\}.                    \tag{4.8}
\]

Extend the bag rooted at (q) along (Q), thereby making it contain
(b).  Together with the three other rooted bags, the connector bag
(V(T)), and the singletons (u,v), this gives seven pairwise adjacent
bags.  Indeed (u) sees the special bag through (q), (v) sees it
through (b), and (T) sees it through both (pq) and (ab); all
three of (u,v,T) see the three (X)-rooted bags.  Thus this is a
(K_7)-model.

It remains to show that a four-connected (M) would have the rooted
model (4.8).  The graph (M) is planar, being a subgraph of (L).
If its four specified roots did not root a (K_4), the
Fabila-Monroy--Wood theorem would put all four on one face.  But

\[
                         qx_1x_2q                              \tag{4.9}
\]

is a triangle.  In a four-connected planar graph it is facial, and in a
three-connected plane graph no different face can share all three of
its vertices.  Hence no face can contain the triangle together with
(x_3).  This contradiction proves that (M) is not four-connected,
so it has a separator of order at most three.  \(\square\)

### Corollary 4.5 (the exact two-path adhesion)

Let (S\) be a separator of (M) of order at most three and (C) a
component of (M-S), with another component on the far side.  Then

\[
 |N_{V(T)\cup(V(Q)-\{q\})}(C)|\ge 5-|S|.                       \tag{4.10}
\]

#### Proof

Every neighbour of (C) is in (S), one of the two deleted path
shores, or \(\{u,v\}\).  Apply seven-connectivity exactly as in Lemma
3.1.  \(\square\)

Thus the rural outcome does not recur indefinitely.  One independent
detour converts it into a genuine two-shore adhesion: a separator of
order at most three whose every side has at least two attachments to the
two disjoint deleted paths.  This is the precise capacity-state object
to which the portal exchange must now be applied.

## 5. Alignment with the edge-deletion trace

Use an edge-deletion six-colouring of (G-uv), normalized as in
`hadwiger_double_moser_edge_exchange.md`.  If a nonzero colour
\(\gamma\) is absent from (X), Lemma 3.1 there gives a shortest
(\{0,\gamma\})-coloured path (T_\gamma) from its unique vertex in
(A) to its unique vertex in (P), with every internal vertex in
(R).  Its two ends both have colour \(\gamma\), so alternation gives

\[
                         |E(T_\gamma)|\equiv0\pmod2.             \tag{5.1}
\]

### Corollary 5.1 (cross-trace trichotomy)

If the absent-colour matching contains (a\mathord{-}p) or
(b\mathord{-}q), its actual bichromatic Kempe carrier has one of the
following consequences:

1. a (K_7)-minor;
2. a separator of order at most three in its deletion, every side of
   which has the portal load (3.1); or
3. the planar cofacial equality lock in Theorem 4.1, together with the
   second detour and loaded two-path three-adhesion of Theorem 4.4 and
   Corollary 4.5.

In the three-colour-core trace, if the two absent colours give the cross
matching

\[
                         a\mathord{-}p,qquad b\mathord{-}q,      \tag{5.2}
\]

there are two genuine even Kempe blockers carrying complementary planar
equality states.  They may meet only at colour-zero vertices.  The next
exchange must show that the two three-adhesions or disk webs cannot be
simultaneously compatible; contracting them to four clean edges is
invalid and is exactly the shortcut refuted in Section 1.

## 6. Exact remaining exchange

The independent five-connected route has therefore reached the same
structural object as the palette-gate route, from a different starting
point:

\[
 \boxed{\text{rooted }K_4+\text{reserved connector}}
 \quad\text{or}\quad
 \boxed{\text{loaded three-adhesion on one or two path shores}}.
\]

The rural expansion is not terminal: Theorem 4.4 uses one independent
linkage as a detour and forces a second three-adhesion.  The remaining
work is now the capacity exchange on that adhesion.  Equality in the
portal counts already gives an exact seven-cut; the surplus case must
either reroute the reserved rooted model or make two attachment intervals
cross.  No claim of that final exchange is made here.
