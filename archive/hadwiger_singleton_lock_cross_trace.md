# The singleton owner lock has a forced crossed Kempe linkage

## 1. Setting

Retain the exact zero-optional singleton-triangle boundary

\[
B=\{h,1,2,r,a,b,c\},\qquad
P=\{h,c\},\quad Q=\{r,a\},\quad R=\{1,2,b\}.
\tag{1.1}
\]

Thus \(h,1,2,r\) induce a \(K_4\), \(a,b,c\) induce a
triangle, the additional boundary edges are

\[
ha,\quad 1b,\quad 2b,\quad rc,
\tag{1.2}
\]

and there are no other edges.  In particular

\[
E(\overline {G[B]})=
\{hc,ra,hb,rb,1a,1c,2a,2c\}.
\tag{1.3}
\]

Assume

\[
G-B=\{d\}\mathbin{\dot\cup}O,
\tag{1.4}
\]

where \(d\) is full to \(B\), \(O\) is connected and full to
\(B\), and \(d\) is anticomplete to \(O\).  The graph \(G\) is
minor-minimal non-six-colourable.  Put \(H=G-d\).

The owner theorem supplies disjoint connected carriers \(X_P,X_Q\)
for \(P,Q\).  If neither carrier can be enriched to meet both the
\(1\)- and \(2\)-portal classes while remaining disjoint from a
carrier for the other pair, Theorem 5.1 of
`hadwiger_singleton_packet_owner_lock.md` gives, after interchanging
\(1,2\),

\[
N_{C_P}(1)=\varnothing,\qquad N_{C_Q}(2)=\varnothing,
\tag{1.5}
\]

where \(C_P\) is the component of \(O-X_Q\) containing \(X_P\)
and \(C_Q\) is the component of \(O-X_P\) containing \(X_Q\).
Moreover

\[
N_O(1)\subseteq C_Q,
\qquad N_O(2)\subseteq C_P.
\tag{1.6}
\]

The purpose of this note is to add the exact crossed linkage which is
forced by minor-criticality but absent from a static packet.

## 2. Every boundary nonedge is an exact trace

### Lemma 2.1 (full trace family)

For every \(uv\in E(\overline {G[B]})\), the graph \(H\) has a
proper six-colouring in which \(u,v\) have one colour and the five
vertices of \(B-\{u,v\}\) have the other five colours bijectively.

#### Proof

Contract the connected star on \(\{d,u,v\}\), with centre \(d\),
to a vertex \(z\).  Colour the resulting proper minor with six
colours.  Delete \(z\), restore the two independent vertices \(u,v\),
and give both the colour of \(z\).  This is a proper colouring of
\(H\): every old neighbour of \(u\) or \(v\) was adjacent to \(z\)
in the contracted graph.

Every six-colouring of \(H\) uses all six colours on \(B=N(d)\),
since otherwise the missing colour could be assigned to \(d\).  Also
\(\alpha(G[B])\le2\), by Dirac's neighbourhood inequality at the
degree-seven vertex \(d\).  Therefore the displayed equality \(u=v\)
is the unique repeated boundary class and the other five boundary
vertices have distinct colours. \(\square\)

### Lemma 2.2 (external Kempe paths)

Fix the exact trace associated with \(uv\), and let
\(W=B-\{u,v\}\).  If \(xy\) is a nonedge of \(G[W]\), then the
two uniquely coloured roots \(x,y\) lie in one bichromatic component
of \(H\).  Consequently there is an \(x\)-\(y\) path whose internal
vertices lie in \(O\).

For two vertex-disjoint nonedges \(xy,x'y'\) of \(G[W]\), the two
paths can be chosen vertex-disjoint.

#### Proof

Let the colours of \(x,y\) be \(\xi,\eta\).  If their
\(\xi/\eta\)-components were different, switch the component
containing \(x\).  On \(B\), the old colour \(\xi\) would disappear
and \(x,y\) would form a second repeated pair in addition to \(u,v\).
Thus at most five colours would occur on \(B\), and the missing colour
could be assigned to \(d\), six-colouring \(G\), a contradiction.

A shortest bichromatic \(x\)-\(y\) path has no other boundary vertex
internally, since all five roots in \(W\) have distinct colours and
the repeated roots have a sixth colour.  Its interior therefore lies
in \(O\).

If \(xy\) and \(x'y'\) are vertex-disjoint, their four boundary roots
have four distinct colours.  The two bichromatic subgraphs use disjoint
sets of colours and hence have disjoint vertex sets.  Choose one path
in each. \(\square\)

### Corollary 2.3 (complete owner state family)

Up to permutation of the six colour names, the boundary extension
family of the unoperated closed owner \(H=G[B\cup O]\) is exactly

\[
 \mathcal E_O=E(\overline {G[B]}),                 \tag{2.1}
\]

where an edge denotes the unique two-vertex equality block and all
other boundary vertices are singleton blocks.  In contrast, every
proper \(B\)-label-preserving rooted minor of \(O\) admits a boundary
state whose nonsingleton blocks form a matching of order two or three
in \(\overline {G[B]}\).

There are exactly seventeen order-two and eight order-three such
matchings.

#### Proof

Boundary saturation and \(\alpha(G[B])\le2\) say that every colouring
of the unoperated owner has one nonedge pair and five singleton blocks.
Lemma 2.1 realizes each of the eight possible pairs, proving (2.1).

After any proper rooted minor operation in \(O\), colour the resulting
proper minor of \(G\).  The retained vertex \(d\) has a colour absent
from all of \(B\), so \(B\) uses at most five colours.  Independence
number two makes every nonsingleton class a pair.  Seven vertices use at
least four colours, hence there are exactly two or three disjoint pairs.
If that state extended the original owner, it would glue to the retained
\(B\cup\{d\}\)-side and colour \(G\), so it is genuinely new.

For the count, the degrees in the eight-edge graph (1.3) are
\(2,2,2,2,3,2,3\), in the displayed vertex order.  Hence the number
of two-matchings is

\[
 \binom82-5\binom22-2\binom32=17.
\]

A three-matching leaves one vertex unmatched.  Deleting any one of
\(h,r,1,2\) leaves exactly two perfect matchings, while deleting any
one of \(a,b,c\) leaves none (this is immediate from (1.3), whose two
degree-three vertices are \(a,c\)).  Thus there are \(4\cdot2=8\)
three-matchings. \(\square\)

## 3. The alternating lock is crossed twice

### Theorem 3.1 (forced crossed linkage)

In the alternating orientation (1.5)--(1.6), the shore \(O\) contains
vertex-disjoint external paths

\[
L_{c1}:c\longrightarrow1,
\qquad
L_{a2}:a\longrightarrow2,
\tag{3.1}
\]

whose internal vertices lie in \(O\).

The same conclusion with \(1,2\) interchanged holds in the opposite
orientation.

#### Proof

Use Lemma 2.1 with the repeated nonedge \(hb\).  The five unique roots
are

\[
W=\{1,2,r,a,c\}.
\]

Both \(1c\) and \(2a\) are missing edges of \(G[W]\), and their
four endpoints are distinct.  Lemma 2.2 supplies the two paths and
makes them vertex-disjoint. \(\square\)

This theorem removes the two-vertex static lock recorded in the earlier
note.  More generally it says that an actual counterexample lock is not
merely a polarity of portal sets: two disjoint bichromatic corridors
cross the polarity in opposite directions.

## 4. Why the crossed linkage is not yet an enriched packet

The following finite graph is a sharp warning.  Let \(O_0\) have
vertices

\[
x_0,x_1,x_2,y_0,y_1,y_2,s,t
\]

and edges

\[
x_0x_1,x_1x_2,quad y_0y_1,y_1y_2,quad
x_2t,ty_1,quad y_2s,sx_1.
\tag{4.1}
\]

Give it the singleton portal sets

\[
\begin{array}{c|ccccccc}
\text{label}&h&c&r&a&1&2&b\\ \hline
\text{portal}&x_0&x_2&y_0&y_2&y_1&x_1&\{s,t\}.
\end{array}
\tag{4.2}
\]

Then \(x_0x_1x_2\) and \(y_0y_1y_2\) are a \((P,Q)\)-packet.
The paths

\[
c-x_2-t-y_1-1,
\qquad
a-y_2-s-x_1-2
\tag{4.3}
\]

are vertex-disjoint and have exactly the crossed form (3.1).  Yet no
\((P,Q)\)-packet is enriched at \(\{1,2\}\).

Indeed, every connected \(P\)-carrier contains \(x_1\), and every
connected \(Q\)-carrier contains \(y_1\).  A connected set carrying
\(P,1,2\) must contain \(y_1\), so it meets every \(Q\)-carrier.
Symmetrically, a connected set carrying \(Q,1,2\) contains \(x_1\)
and meets every \(P\)-carrier.

Thus Theorem 3.1 is the strongest conclusion available from the full
trace family plus ordinary Kempe connectivity alone.  The example is
not seven-connected and does not satisfy the operation transition
polarity.  It identifies exactly what the final argument must use:
after deleting or contracting one of the four bottleneck edges incident
with \(x_1,y_1\), the resulting order-two/order-three boundary state and
the five edge-detours must break the alternating lock, or expose an
exact seven-adhesion.

## 5. Exact residual

Combining this note with `hadwiger_singleton_packet_owner_lock.md`, a
surviving full-singleton cell has all of the following simultaneously.

1. All eight nonedges in (1.3) occur as unique repeated-pair traces.
2. Every internal one-step operation produces one of the seventeen
   order-two or eight order-three matchings in
   \(\overline {G[B]}\), accepted by the operated owner and rejected
   by the original owner.
3. Every deleted edge has five bichromatic detours.
4. Every packet has the alternating portal polarity (1.5)--(1.6).
5. In that polarity there are two vertex-disjoint crossed Kempe paths
   (3.1).

Hence the remaining statement is no longer a static protected-split
lemma.  It is the following finite-interface exchange theorem:

> An operation-critical seven-boundaried graph with the full trace
> family and the crossed linkage (3.1) cannot retain the alternating
> carrier lock after every one-step operation.

The crossed ladder (4.1)--(4.3) shows why the words
``operation-critical'' cannot be removed.
