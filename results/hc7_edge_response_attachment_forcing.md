# Attachment forcing from proper-minor colourings

**Status:** written proof; separate internal audit GREEN.  The results
below concern the attachment of the endpoints of an operated edge to the two
classes of an induced bipartite subgraph.  They do not identify colour classes
with prescribed branch sets, do not produce compatible colourings across a
separation, and do not prove \(\mathrm{HC}_7\).

## 1. Setup and notation

Let \(q\ge 3\), put \(p=q-1\), and let \(G\) be a graph with

\[
                              \chi(G)>q.                           \tag{1.1}
\]

Let

\[
                         X=G[A\mathbin{\dot\cup}B]                 \tag{1.2}
\]

be an induced bipartite subgraph with nonempty bipartition classes \(A,B\),
and put \(Q=G-V(X)\).  Connectivity of \(X\) and domination of \(Q\) are not
assumed until Section 5.

Fix an edge \(e=xy\in E(Q)\).  Let \(m\) be either deletion or contraction
of \(e\), and put

\[
                G_m=G/m,\qquad Q_m=G_m-V(X).                       \tag{1.3}
\]

In the contraction case, write \(w\) for the image of \(x,y\).  Define

\[
 S_m=N_{G_m}(A)\cap V(Q_m),\qquad
 T_m=N_{G_m}(B)\cap V(Q_m).                                      \tag{1.4}
\]

A proper \(p\)-colouring has the fixed palette \([p]\); it need not use
every colour.

## 2. Endpoint attachment forcing

### Theorem 2.1 (edge-response attachment forcing)

Let \(\psi\) be a proper \(p\)-colouring of \(Q_m\).

1. If some \(c\in[p]\) is absent from \(\psi(T_m)\), then each original
   endpoint \(x,y\) has a neighbour in \(A\).
2. If some \(c\in[p]\) is absent from \(\psi(S_m)\), then each original
   endpoint \(x,y\) has a neighbour in \(B\).

Consequently, if one colour is absent from both attachment sets, then each
of \(x,y\) has a neighbour in each of \(A,B\).

#### Proof for edge deletion

Suppose \(m\) deletes \(e\) and \(c\) is absent from \(\psi(T_m)\).
Extend \(\psi\) to a \(q\)-colouring \(\varphi\) of \(G-e\) by assigning
colour \(c\) to \(B\) and the fresh colour \(q\) to \(A\).  This is proper:
\(c\) is absent from the neighbours of \(B\) in \(Q\), the fresh colour
does not occur in \(Q\), and every edge of \(X\) joins its two classes.

The vertices \(x,y\) have the same colour, say \(\alpha\).  Otherwise
restoring \(e\) would \(q\)-colour \(G\), contrary to (1.1).  Moreover,
each endpoint has a neighbour of every colour \(\beta\ne\alpha\).  If one
endpoint had no such neighbour of colour \(\beta\), recolour that endpoint
with \(\beta\) and restore \(e\), again contradicting (1.1).

In particular, both endpoints have a neighbour of the fresh colour \(q\),
and all vertices of that colour lie in \(A\).  This proves item 1.
Interchanging \(A,B\) proves item 2.

#### Proof for edge contraction

Suppose \(m\) contracts \(e\), let \(w\) be its image, and put
\(\alpha=\psi(w)\).  If \(c\) is absent from \(\psi(T_m)\), extend
\(\psi\) to a proper \(q\)-colouring of \(G/e\) by colouring \(B\) with
\(c\) and \(A\) with the fresh colour \(q\).

If, say, \(x\) had no neighbour in \(A\), expand \(w\) by colouring \(x\)
with \(q\) and \(y\) with \(\alpha\).  The fresh colour causes no conflict
at \(x\).  Every neighbour of \(y\), apart from \(x\), was a neighbour of
\(w\) and has colour different from \(\alpha\); and \(xy\) has differently
coloured ends.  This would \(q\)-colour \(G\), a contradiction.  Thus
both \(x,y\) have neighbours in \(A\).  This proves item 1, and item 2 is
symmetric.  Applying both items proves the final assertion. \(\square\)

### Proposition 2.2 (endpoint colour saturation)

In either proof of Theorem 2.1, let \(\alpha\) be the colour of \(x,y\) in
the deletion case, or the colour of \(w\) in the contraction case.  Relative
to the displayed \(q\)-colouring, each original endpoint has a neighbour of
every colour \(\beta\ne\alpha\).

#### Proof

The deletion case was proved above.  In the contraction case, if \(x\) had
no neighbour of colour \(\beta\ne\alpha\), expand \(w\) by assigning
\(\beta\) to \(x\) and \(\alpha\) to \(y\).  The verification in the
contraction proof of Theorem 2.1 gives a \(q\)-colouring of \(G\).
Apply the same argument to \(y\). \(\square\)

This saturation concerns colours in a particular extension.  It does not
place the witnessing neighbours in prescribed minor branch sets.

## 3. The safe Kempe-chain conclusion after edge deletion

The contraction case has one quotient vertex \(w\), so it does not itself
supply two distinguished endpoints of a Kempe chain.  The following result
is specifically for deletion.

### Theorem 3.1 (two alternating paths and a local lens)

Suppose \(m\) deletes \(e\), and one colour \(c\in[p]\) is absent from both
\(\psi(S_m)\) and \(\psi(T_m)\).  Then

\[
                         \psi(x)=\psi(y)=\alpha\ne c.              \tag{3.1}
\]

There are \(x\)-\(y\) paths

\[
 P_A\subseteq G[\psi^{-1}(\alpha)\cup A],\qquad
 P_B\subseteq G[\psi^{-1}(\alpha)\cup B].                         \tag{3.2}
\]

The paths can meet internally, but only in \(\psi^{-1}(\alpha)\).  Their
union contains a cycle formed by internally disjoint subpaths of \(P_A\)
and \(P_B\), with common ends in \(\psi^{-1}(\alpha)\).  Those common ends
need not be \(x,y\).

#### Proof

The deletion proof of Theorem 2.1 gives
\(\psi(x)=\psi(y)=\alpha\), and the common-hole conclusion makes both
endpoints adjacent to \(A\) and \(B\).  Since \(c\) is absent from both
attachment sets, neither endpoint can have colour \(c\), proving (3.1).

Form two \(q\)-colourings of \(G-e\):

\[
\begin{array}{c|cc}
 &A&B\\ \hline
\varphi_A&q&c\\
\varphi_B&c&q.
\end{array}                                                       \tag{3.3}
\]

In \(\varphi_A\), the vertices \(x,y\) belong to the same
\(\alpha\)-\(q\) Kempe component.  Otherwise interchange \(\alpha,q\)
in the component containing \(x\); then \(x,y\) have different colours
and \(e\) can be restored.  An \(\alpha\)-\(q\) path in that component is
\(P_A\).  Because \(\alpha\ne c\), all its \(\alpha\)-coloured vertices
belong to \(\psi^{-1}(\alpha)\), proving the first containment in (3.2).
The same argument with \(\varphi_B\) gives \(P_B\).

The two paths have no common edge: the non-\(\alpha\) end of every edge of
\(P_A\) lies in \(A\), while that of every edge of \(P_B\) lies in \(B\).
Their common vertices therefore lie in \(\psi^{-1}(\alpha)\).  Traverse
\(P_A\) from \(x\), and let \(v\ne x\) be the first vertex encountered
which also lies on \(P_B\).  Such a vertex exists because
\(y\in P_A\cap P_B\).  The interior of \(P_A[x,v]\) is disjoint from
\(P_B\), so \(P_A[x,v]\) and the \(x\)-\(v\) subpath of \(P_B\) are
internally disjoint.  They share no edge and hence form the asserted
cycle. \(\square\)

### Example 3.2 (the paths need not form an \(x\)-\(y\) lens)

Let \(G\) have vertices \(\{r,s,t,a,b,c,d\}\) and edges

\[
 E(K_4[\{r,s,a,b\}]-rs)
 \;\cup\;
 E(K_4[\{r,t,c,d\}]-rt)
 \;\cup\;\{st,ad\}.                                               \tag{3.4}
\]

Put

\[
 A=\{a,c\},\qquad B=\{b,d\},\qquad Q=\{r,s,t\},\qquad e=st.       \tag{3.5}
\]

The induced graph \(X=G[A\mathbin{\dot\cup}B]\) is the connected bipartite
path \(b-a-d-c\), and it dominates \(Q\).  The graph \(G\) is not
three-colourable: the first \(K_4\) minus an edge forces \(r,s\) to have
the same colour, the second forces \(r,t\) to have the same colour, and
the edge \(st\) gives a contradiction.

Take \(q=3,p=2\), and colour all vertices of \(Q-e\) with
\(\alpha=1\).  Colour \(2\) is a common hole because \(S_m=T_m=Q\).
In the two extensions (3.3), the relevant alternating paths are uniquely

\[
                         s-a-r-c-t,\qquad s-b-r-d-t.               \tag{3.6}
\]

They share the internal vertex \(r\).  Thus Theorem 3.1 cannot be
strengthened, under its stated hypotheses, to two internally disjoint
\(x\)-\(y\) paths.  The example is not asserted to be minor-minimal or
seven-connected.

## 4. Vertex-deletion analogue

Let \(v\in V(Q)\), put \(Q_v=Q-v\), and define

\[
 S_v=N_{G-v}(A)\cap V(Q_v),\qquad
 T_v=N_{G-v}(B)\cap V(Q_v).                                      \tag{4.1}
\]

### Theorem 4.1 (vertex-response attachment forcing)

Let \(\psi\) be a proper \(p\)-colouring of \(Q_v\).

1. If a colour is absent from \(\psi(T_v)\), then \(v\) has a neighbour
   in \(A\).
2. If a colour is absent from \(\psi(S_v)\), then \(v\) has a neighbour
   in \(B\).

Hence a common missing colour forces \(v\) to have neighbours in both
bipartition classes.

#### Proof

If \(c\) is absent from \(\psi(T_v)\), colour \(B\) with \(c\) and \(A\)
with the fresh colour \(q\).  This gives a \(q\)-colouring of \(G-v\).
If \(v\) had no neighbour in \(A\), assigning colour \(q\) to \(v\)
would \(q\)-colour \(G\), contradicting (1.1).  This proves item 1;
item 2 is symmetric. \(\square\)

Every colour in fact occurs in the neighbourhood of \(v\) in the displayed
colouring of \(G-v\), since any absent colour could be assigned to \(v\).
Again, this is palette saturation, not a labelled branch-set statement.

## 5. Consequences under minor-minimality and domination

Assume for this section that

1. every proper minor of \(G\) is \(q\)-colourable;
2. \(X\) is connected; and
3. \(X\) dominates \(Q\).

Call \(u\in V(Q)\) **two-sided** if it has neighbours in both \(A,B\),
**\(A\)-only** if it has a neighbour in \(A\) and none in \(B\), and
**\(B\)-only** symmetrically.  Domination ensures that every vertex has
exactly one of these three types.

### Proposition 5.1 (connected-subgraph type trichotomy)

For every connected subgraph \(L\subseteq Q\), at least one of the following
holds:

1. \(L\) contains a two-sided vertex;
2. \(L\) contains an edge with one \(A\)-only and one \(B\)-only endpoint;
3. every vertex of \(L\) is \(A\)-only, or every vertex is \(B\)-only.

#### Proof

If there is no two-sided vertex and both one-sided types occur, a path in
\(L\) between the two types contains consecutive vertices of different
types.  Otherwise all vertices have the same type. \(\square\)

### Theorem 5.2 (full attachment palettes after one operation)

Let \(e=xy\) be an edge of \(Q\), and let \(m\) delete or contract \(e\).

1. If \(x\) is \(A\)-only and \(y\) is \(B\)-only, every proper
   \(p\)-colouring of \(Q_m\) uses all \(p\) colours on both \(S_m,T_m\),
   and
   \[
                              \chi(Q_m)=p.                         \tag{5.1}
   \]
2. If both endpoints are \(A\)-only, every proper \(p\)-colouring of
   \(Q_m\) uses all \(p\) colours on \(S_m\), and (5.1) holds.
3. If both endpoints are \(B\)-only, every proper \(p\)-colouring of
   \(Q_m\) uses all \(p\) colours on \(T_m\), and (5.1) holds.

For a one-sided singleton \(v\), the corresponding statement holds after
deleting \(v\): if \(v\) is \(A\)-only, every proper \(p\)-colouring of
\(Q-v\) uses all \(p\) colours on \(S_v\), and symmetrically for a
\(B\)-only vertex.  In either case \(\chi(Q-v)=p\).

#### Proof

In item 1, a colour missing from \(T_m\) would force both original
endpoints to have neighbours in \(A\), contrary to \(y\) being \(B\)-only.
A colour missing from \(S_m\) would similarly contradict \(x\) being
\(A\)-only.  Thus both sets are full.  In item 2, a colour missing from
\(S_m\) would force both endpoints to have neighbours in \(B\), which is
impossible.  Item 3 is symmetric.

Contract \(X\) in the proper minor \(G_m\).  Because \(X\) is connected
and dominates \(Q_m\), the resulting graph is

\[
                              K_1\vee Q_m.                         \tag{5.2}
\]

It is a proper minor of \(G\), so \(\chi(Q_m)\le q-1=p\).  In every case
at least one attachment set uses all \(p\) colours in every proper
\(p\)-colouring.  If \(\chi(Q_m)\le p-1\), regard a colouring with at most
\(p-1\) colours as one with palette \([p]\); its unused colour contradicts
that fullness.  This proves (5.1).

For a singleton, Theorem 4.1 gives the relevant fullness, and contracting
\(X\) in \(G-v\) gives the same upper bound. \(\square\)

The minor-minimality, connectivity, and domination assumptions are needed
for the chromatic equalities.  They are not needed in Sections 2--4.

## 6. Application to the conditional defect-one branch of \(\mathrm{HC}_7\)

In the connected bipartite compression used in the current
\(\mathrm{HC}_7\) programme, \(q=6,p=5\), the graph \(G\) is
seven-chromatic, every proper minor is six-colourable, and
\(X=G[A\mathbin{\dot\cup}B]\) is connected and dominates the
five-chromatic remainder \(Q\).  Theorem 5.2 therefore applies to an
internal edge of a selected connected component in one of the protected
subgraphs \(D_i\subseteq Q\).

For such a component \(L\), Proposition 5.1 gives the following division:

1. a two-sided vertex occurs;
2. an internal cross edge forces both attachment sets to use all five
   colours after deletion or contraction; or
3. a one-sided component forces the corresponding attachment set to use
   all five colours after an internal edge operation, with Theorem 4.1
   handling a singleton.

This is operation-specific information, but none of the cases is currently
terminal.  In particular:

- a two-sided vertex is not two disjoint connected branch sets;
- a full palette does not identify colours with the five prescribed branch
  sets adjacent to a lifted simplicial component;
- the paths in Theorem 3.1 may meet at additional \(\alpha\)-vertices;
- contraction supplies endpoint saturation but not two endpoint-rooted
  Kempe paths;
- no conclusion bounds a full neighbourhood by seven vertices;
- no conclusion gives closed-shore six-colourings with the same equality
  partition on an order-seven separator; and
- no conclusion produces a new eligible defect-one configuration with a
  strictly smaller lifted component.

Thus the remaining \(\mathrm{HC}_7\) step requires a label-preserving
theorem converting these colour contacts into prescribed branch-set
contacts, a compatible order-seven separation, or a strict host-level
descent.

## 7. Exact trust boundary

The following stronger statements are not proved here.

1. The paths \(P_A,P_B\) are internally disjoint between \(x,y\).
2. Palette saturation implies contact with a fixed minor model.
3. Every lifted simplicial component lies in \(Q\); it may instead lie in
   \(X\).
4. An elementary operation preserves the selected colour-matched path,
   its cut, the protected labels, or the defect-one contact graph.
5. A failed exchange returns an order-seven separator with compatible
   boundary colourings.
6. Every adjacent-pair configuration reaches the conditional defect-one
   hypotheses.

Example 3.2 disproves item 1 under Theorem 3.1's hypotheses.  It does not
disprove a strengthening using all minor-minimality and seven-connectivity
hypotheses of the \(\mathrm{HC}_7\) setting.

## 8. Current dependencies

Sections 2--5 are self-contained.  Their present application uses:

- [one-step minor dynamics in the connected bipartite compression](../results/hc7_star_core_one_step_minor_dynamics.md);
- [component-contact defect and the conditional two-tree equality case](../results/hc7_component_contact_defect_theorem.md); and
- [normal form around a lifted simplicial component](../results/hc7_defect_one_simplicial_normalization.md).
