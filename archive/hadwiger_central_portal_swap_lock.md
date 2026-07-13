# The central defect cut is a single-portal swap lock

## 1. A label-free two-shore configuration

Let \(G\) be a \(k\)-contraction-critical graph. Suppose that its vertex
set has the disjoint form

\[
 V(G)=U\mathbin{\dot\cup}\{x,y\}
 \mathbin{\dot\cup}A\mathbin{\dot\cup}B,
\tag{1.1}
\]

where \(A,B\) are nonempty and connected, \(xy\in E(G)\), and

\[
\begin{aligned}
 &N_G(A)=U\cup\{x\},\qquad N_G(B)=U\cup\{y\},\\
 &E(A,B)=\varnothing,\qquad E(x,B)=E(y,A)=\varnothing.
\end{aligned}
\tag{1.2}
\]

Thus each of \(A,B\) is full to the common root set \(U\), while \(x\)
and \(y\) are the unique cross-portals of the other side. Put

\[
 S_x=U\cup\{x\},\qquad S_y=U\cup\{y\}.
\tag{1.3}
\]

### Lemma 1.1 (portal-swap cuts)

Both \(S_x\) and \(S_y\) are vertex cuts. More precisely,

\[
\begin{array}{c|c}
\text{cut}&\text{the two components}\\ \hline
S_y&A\cup\{x\},\ B,\\
S_x&A,\ B\cup\{y\}.
\end{array}
\tag{1.4}
\]

If \(G\) is \((|U|+1)\)-connected, then the two components in each row
are full to the displayed cut. In particular, both cuts are exact
minimum cuts.

#### Proof

The assertions about the components follow immediately from (1.2) and
the edge \(xy\). Every component behind a minimum cut in a graph whose
connectivity equals the order of the cut is full: if a component missed
one cut vertex, its neighbourhood would be a smaller cut. Apply this to
the two cuts of order \(|U|+1\). \(\square\)

Contract \(xy\) to a vertex \(p\), and write \(L=G/xy\). Equations
(1.1)--(1.2) give a third exact presentation:

\[
 P=U\cup\{p\},\qquad L-P=A\mathbin{\dot\cup}B,
\tag{1.5}
\]

and both \(A,B\) are full to \(P\). Thus the contraction does not erase
the two-shore geometry; it turns the two exchanged boundary vertices into
one labelled split vertex.

## 2. Exact chromaticity after the portal contraction

### Lemma 2.1

The contracted graph \(L=G/xy\) has chromatic number exactly \(k-1\).

#### Proof

Minor-criticality gives \(\chi(L)\le k-1\). If \(L\) had a
\((k-2)\)-colouring, expand \(p\) to the two nonadjacent vertices \(x,y\)
with their common old colour, and then recolour \(x\) with one new colour.
That new colour occurs nowhere else, so all edges incident with \(x\),
including \(xy\), are proper. This is a \((k-1)\)-colouring of \(G\), a
contradiction. \(\square\)

Fix a proper \((k-1)\)-colouring \(c\) of \(L\), and put

\[
 \alpha=c(p).
\tag{2.1}
\]

The split-cycle theorem for the critical edge \(xy\) applies. Its
localization is particularly sharp in (1.1).

### Theorem 2.2 (every split cycle crosses the common core)

For every colour \(\beta\ne\alpha\), one of the following holds.

1. \(x,y\) have a common \(\beta\)-coloured neighbour in \(U\).
2. There is an \(\alpha/\beta\)-coloured \(x\)-\(y\) path in \(G-xy\)
   whose first edge is an \(x\)-edge and whose last edge is a \(y\)-edge.
   Every such path meets \(U\).

Consequently:

\[
 \boxed{\alpha\notin c(U)}
 \quad\Longrightarrow\quad
 \boxed{\text{every colour }\beta\ne\alpha\text{ occurs on }U}.
\tag{2.2}
\]

If instead a colour \(\beta\ne\alpha\) is absent from \(U\), every
\(\alpha/\beta\) split path meets the nonempty gate

\[
 U_\alpha=U\cap c^{-1}(\alpha).
\tag{2.3}
\]

#### Proof

The split-cycle theorem gives the common-neighbour/path alternative.
A common neighbour cannot lie in \(A\), since \(y\) has no neighbour in
\(A\), and cannot lie in \(B\), since \(x\) has no neighbour in \(B\).
It therefore lies in \(U\).

Likewise, in \(G-xy-U\), the vertex \(x\) and all of \(A\) lie in one
component, while \(y\) and all of \(B\) lie in another; (1.2) gives no
edge between the two. Hence every \(x\)-\(y\) path in \(G-xy\) meets
\(U\).

If \(\alpha\) is absent from \(U\), the boundary vertex at which an
\(\alpha/\beta\) path first meets \(U\) has colour \(\beta\). The same is
true in the common-neighbour outcome. This proves (2.2). If both
\(\alpha,\beta\) were absent from \(U\), neither outcome could meet \(U\),
a contradiction. Thus, when \(\beta\) is absent, every split path hits
the set (2.3). \(\square\)

### Corollary 2.3 (the tight \(HC_7\) trace)

Suppose \(k=7\) and \(|U|=6\). In every six-colouring of \(G/xy\),
exactly one of the following occurs.

1. The colour of \(p\) occurs on \(U\).
2. The vertex \(p\) is the unique boundary vertex of its colour, all
   other five colours occur on \(U\), and precisely one of them occurs
   twice. Hence the equality partition on
   \(P=U\cup\{p\}\) has exactly one nonsingleton block, an independent
   pair contained in \(U\).

#### Proof

If \(\alpha\notin c(U)\), Theorem 2.2 makes all five other colours occur
on the six vertices of \(U\). Exactly one is therefore repeated and the
others occur once. A repeated colour class is independent. The other
case is the stated alternative. \(\square\)

The second row is an exact one-pair trace, not merely a count of colours.
The first row is also geometric: every colour missing from \(U\) has all
of its split paths forced through the actual \(\alpha\)-gate \(U_\alpha\).

## 3. Application to the central defect cut

Use the notation of *hadwiger_degree9_exact7_two_shore_funnel.md*. Thus

\[
 S=\{h,1,2,5,6,y,z\}
\tag{3.1}
\]

is an exact cut with two full shores \(C_v,D\), the first contains the
old vertex \(v\), and \(R\) is the component of \(C_v-v\) containing an
old literal. Suppose \(R\) has its unique boundary defect

\[
 d\in\{1,2,6\}.
\tag{3.2}
\]

Put

\[
 U=S-\{d\}.
\tag{3.3}
\]

### Lemma 3.0 (the degree-seven frame has only one \(v\)-lobe)

The graph \(C_v-v\) is connected. Consequently \(C_v-v=R\).

#### Proof

Every component of \(C_v-v\) contains a neighbour of \(v\); otherwise
it would also be a component of the connected graph \(C_v\).  The five
old neighbours \(h,1,2,5,6\) belong to \(S\).  Hence every
\(v\)-neighbour in \(C_v-v\) belongs to
\[
                         \{3,4\}-S.
\]
This set is nonempty in the present, nonexceptional placement. If it
has two members, the old edge \(34\) puts them in the same component of
\(C_v-v\); if it has one member, it plainly lies in one component.
Every component must contain a member of this same one- or two-element
set, so no second component exists. \(\square\)

### Theorem 3.1 (the defect outcome is a portal-swap lock)

The graph has the decomposition (1.1)--(1.2) with

\[
 x=v,\qquad y=d,\qquad A=R,\qquad B=D.
\tag{3.4}
\]

Consequently:

1. the cut \(T_d=U\cup\{v\}\) and the original cut
   \(S=U\cup\{d\}\) are the two portal-swap cuts;
2. \(v\) is the unique \(S\)-shore portal of \(d\), and
   \(d\) is the unique \(T_d\)-opposite-shore portal of \(v\);
3. after contracting the actual edge \(vd\), the boundary
   \(U\cup\{vd\}\) is again an exact seven-cut with exactly the two full
   shores \(R,D\); and
4. every six-colouring of \(G/vd\) has one of the two trace geometries in
   Corollary 2.3, with five side-labelled split chains crossing \(U\).

#### Proof

The funnel already proves

\[
 N_G(R)=U\cup\{v\}.
\tag{3.5}
\]

The old vertex \(v\) is adjacent to \(d\). The shore \(D\) is a
component of \(G-S\), so it has no edge to \(v\notin S\), while fullness
gives \(N_G(D)=S=U\cup\{d\}\). Distinct components \(R,D\) of
\(G-(U\cup\{v,d\})\) are anticomplete. These are exactly
(1.1)--(1.2). Lemma 1.1, Lemma 2.1, Theorem 2.2 and Corollary 2.3 give
the four conclusions. \(\square\)

The old degree-seven star makes the second trace row much smaller than
the label-free statement suggests.

### Corollary 3.2 (exact one-pair trace or a two-gate fan)

Let \(p\) be the image of \(vd\), and let \(c\) be any six-colouring of
\(G/vd\), and put \(\alpha=c(p)\). Then exactly one of the following
holds.

1. The seven boundary vertices \(U\cup\{p\}\) use all six colours.
   Their equality partition is therefore an exact one-pair state.
2. Some colour is absent from \(U\cup\{p\}\), and every split path for
   every such absent colour meets the fixed nonempty gate
   \[
                 U_\alpha\subseteq\{y,z\},\qquad |U_\alpha|\le2.
   \tag{3.6}
   \]

If \(p\) is adjacent to at least one of \(y,z\), the gate in outcome 2
has order one.

#### Proof

The four vertices

\[
                 \{h,1,2,5,6\}-\{d\}
\tag{3.7}
\]

belong to \(U\) and are all adjacent to \(v\), hence to \(p\) after the
contraction. None can have colour \(\alpha\). Thus

\[
                         U_\alpha\subseteq\{y,z\}. \tag{3.8}
\]

If \(\alpha\notin c(U)\), Corollary 2.3 gives outcome 1. Suppose
\(\alpha\in c(U)\). If all other five colours also occur on \(U\), then
the six vertices of \(U\) use the six colours once each, and \(p\)
repeats \(\alpha\); this is again outcome 1. Otherwise some
\(\beta\ne\alpha\) is absent from \(U\). Since \(\beta\ne c(p)\), it is
also absent from the whole boundary \(U\cup\{p\}\), and Theorem 2.2
forces every corresponding split path through \(U_\alpha\). The same
argument applies to every absent colour. Equation (3.8) gives (3.6).
Finally, an \(\alpha\)-coloured boundary vertex cannot be adjacent to
\(p\), proving the last assertion. \(\square\)

### Corollary 3.3 (the lock lies in the sole-exterior Moser cell)

Assume the installed pure-Moser two-exterior closure. Then
\[
                         G-N[v]\text{ is connected}. \tag{3.9}
\]
Consequently the portal-swap row is not a new degree-seven component
geometry: it is a transition inside the already isolated sole-exterior
reserved-connector cell.

More explicitly:

* if \(\{y,z\}=\{3,4\}\), then \(S=N(v)\), the shore containing \(v\)
  is the singleton \(\{v\}\), and the other shore is literally the sole
  exterior;
* otherwise at least one of \(y,z\), say \(w\), lies outside \(N(v)\).
  In the defect row \(R\) contacts \(w\), and the full opposite shore
  \(D\) also contacts \(w\). Thus the parts of \(R\) and \(D\) incident
  with \(w\) already lie in one component of \(G-N[v]\). Any failure of
  (3.9) would be an additional exterior component, which the global
  component closure excludes.

#### Proof

Every component of \(G-N[v]\) is full to \(N(v)\), by
seven-connectivity. If there were at least three, choose a triangle in
the pure Moser neighbourhood, anchor three components at three distinct
vertices outside that triangle, and use the triangle vertices as
singleton bags. These six \(N(v)\)-meeting bags, together with
\(\{v\}\), form a \(K_7\)-model. Exactly two components are excluded by
the supported-pair exact-state transfer theorem. At least one exterior
component exists, so (3.9) follows. The two placement descriptions use
only that \(y,z\) are distinct from \(h,1,2,5,6\), and hence a member
of \(\{y,z\}\cap N(v)\) must be \(3\) or \(4\). \(\square\)

This cross-pollination is useful but does not reverse the portal-transfer
direction. The singleton apex shore accepts the normalized four-block
states but has no two-packet of its own. Hence the reserved-connector
packet theorem cannot simply be pointed backwards to colour \(R\) or
\(D\); the side-labelled \(vd\)-fan must still be used as an actual
portal exchange.

## 4. Exact gain and remaining exchange

The defect row of the central funnel is therefore not an arbitrary new
seven-cut. It is a **single-portal swap lock** around one actual critical
edge. Its entire unbounded geometry has only two palette continuations:

* an exact one-pair trace on the contracted seven-boundary; or
* an actual same-colour gate of order at most two, contained in the two
  exceptional labels \(\{y,z\}\), hit by every split chain whose other
  colour is absent from the common core.

This removes a false stopping point: citing \(T_d\) as a nested cut without
retaining the unique \(v\leftrightarrow d\) portal loses the strongest
available transition. Conversely, the theorem does **not** claim that an
exact one-pair trace or an \(\alpha\)-gate already gives \(K_7\). The live
operation is now the same bounded-interface exchange as in the central
\(56\)-lock: either two side-labelled chains cross and lift to the allocated
diamond, or their common gate must be converted into a label-preserving
shore split.
