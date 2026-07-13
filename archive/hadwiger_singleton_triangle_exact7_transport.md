# Exact seven-cuts transport the two-pair web to a singleton

## 1. Setting

Let \(G\) be seven-connected and \(K_7\)-minor-free.  Suppose that
\(B\) is a seven-cut with exactly two full components \(O,D\) behind it.
Assume that

\[
 B=P\mathbin{\dot\cup}Q\mathbin{\dot\cup}R,
 \qquad |P|=|Q|=2,\quad |R|=3,                 \tag{1.1}
\]

and that

\[
                  P\mid Q\mid\{r_1\}\mid\{r_2\}\mid\{r_3\} \tag{1.2}
\]

has complete block quotient, with \(R=\{r_1,r_2,r_3\}\) a triangle.
Suppose \(O\) contains a packet for \((P,Q)\), while \(D\) contains no
such packet.  This is exactly the oriented residue of
`hadwiger_singleton_triangle_q2_web_exchange.md`, but the result below
uses neither the Moser labels nor the particular edges realizing (1.2).

A **nested exact fragment** is a nonempty connected set \(F\subsetneq D\)
such that

\[
                         |N_G(F)|=7                     \tag{1.3}
\]

and \(F\) is a component of \(G-N_G(F)\).  Choose such an \(F\) of
minimum order and put \(S=N_G(F)\).

## 2. Linkage transports the five outer bags

### Lemma 2.1 (clean transport)

There are seven pairwise vertex-disjoint \(B\)-\(S\) paths
\((L_x:x\in B)\), inducing a bijection \(x\mapsto s_x\) from \(B\) to
\(S\).  Every vertex of \(B\cap S\) may be fixed by a trivial path, and
every nontrivial path has interior in

\[
                  D-(F\cup B\cup S).                    \tag{2.1}
\]

If \(X_P,X_Q\subseteq O\) are the two owner carriers, define

\[
\begin{aligned}
 A_P&=X_P\cup P\cup\bigcup_{x\in P}V(L_x),\\
 A_Q&=X_Q\cup Q\cup\bigcup_{x\in Q}V(L_x),\\
 A_i&=V(L_{r_i})\qquad(i=1,2,3).
\end{aligned}                                          \tag{2.2}
\]

Then, after repeated vertices at the path ends are retained only in their
unique displayed bag, the five sets in (2.2) are pairwise disjoint,
connected branch bags forming a \(K_5\)-model.  Moreover, \(A_P\) meets
\(S\) exactly in \(s_p\) for \(p\in P\), \(A_Q\) meets it in the two
\(Q\)-ends, and \(A_i\) meets it in \(s_{r_i}\).

#### Proof

Use the outer separation

\[
             (O\cup B,\;B\cup D)
\]

and the inner separation

\[
             (V(G)-F,\;S\cup F).
\]

They are nested because \(S=N_G(F)\subseteq B\cup D\).  Apply the nested
minimum-cut linkage lemma to these two separations.  This gives the paths
and (2.1).  They avoid \(O\) and \(F\), and distinct paths meet
neither one another nor the two disjoint owner carriers.  The unions in
(2.2) are connected because an owner carrier joins the two roots of its
pair block.  Their pairwise adjacencies are precisely those of the
complete block quotient (1.2). \(\square\)

Call

\[
 P'=\{s_p:p\in P\},\qquad Q'=\{s_q:q\in Q\},\qquad
 R'=\{s_{r_1},s_{r_2},s_{r_3}\}.                      \tag{2.3}
\]

### Lemma 2.2 (packet transport is faithful)

The fragment \(F\) contains no packet for \((P',Q')\).

#### Proof

Suppose \(Y_P,Y_Q\subseteq F\) were disjoint connected carriers for
\(P',Q'\).  For \(x\in P\cup Q\), put

\[
 T_x=\begin{cases}
 V(L_x)-\{x\},&L_x\text{ is nontrivial},\\
 \varnothing,&L_x\text{ is trivial}.
 \end{cases}
\]

The lifted carriers are

\[
 \widehat Y_P=Y_P\cup\bigcup_{p\in P}T_p,
 \qquad
 \widehat Y_Q=Y_Q\cup\bigcup_{q\in Q}T_q.          \tag{2.4}
\]

For a trivial path the corresponding \(Y\)-set is already adjacent to the
original boundary root.  The two sets in (2.4) lie in \(D\), are
connected and disjoint, and meet respectively both roots of \(P\) and
both roots of \(Q\).  They are a packet in \(D\), contrary to the
hypothesis. \(\square\)

## 3. A minimum nonsingleton fragment is atomic

### Lemma 3.1 (relative atomicity)

If \(|F|\ge2\), then for every nonempty proper \(Y\subsetneq F\),

\[
 |(N_F(Y)-Y)\mathbin{\dot\cup}N_S(Y)|\ge8.             \tag{3.1}
\]

#### Proof

The displayed set is exactly \(N_G(Y)\), because \(F\) is a component
behind \(S\).  Seven-connectivity gives the lower bound seven.  If
equality held, take a component \(K\) of \(G-N_G(Y)\) contained in
\(Y\).  Its neighbourhood is contained in \(N_G(Y)\), and
seven-connectivity forces equality.  The nonempty outer component \(O\)
is anticomplete to \(D\) and hence survives on the far side.  Thus \(K\)
would be a nested exact fragment contained in \(D\), of order smaller
than \(F\), contradicting the choice of \(F\). \(\square\)

The two-pair packet/web theorem can consequently be applied to \(F\)
with the transported boundary \(P'\dot\cup Q'\dot\cup R'\).  It makes
\(F\) a bare disk web unless a packet occurs, which Lemma 2.2 excludes.

### Lemma 3.2 (one- and two-cuts close after transport)

If \(|F|\ge2\), then \(F\) is three-connected.

#### Proof

First note that \(|F|\ge4\).  Lemma 3.1 of the two-pair web theorem gives
at least two portals for each of the four labels in \(P'\cup Q'\), while
its no-double-pair conclusion lets a vertex contribute at most one
\(P'\)-incidence and one \(Q'\)-incidence.  Thus at least eight incidences,
at most two per vertex, are required.

The label-free atomic-web lemma excludes a cutvertex.  If \(Z\) is a
two-cut, its crossed-lobe theorem gives exactly two components
\(K_1,K_2\) of \(F-Z\).  After possibly interchanging the pair blocks,
each \(K_i\) is full to \(Q'\cup R'\), the two components have
complementary one-root defects in \(P'\), and
\(N_F(K_1)=N_F(K_2)=Z\).

Put \(W_0=K_1\cup Z\) and \(W_1=K_2\).  Both sets are connected, an
edge joins them, and each sees every one of the five transported bags in
(2.2): it sees \(A_P\) through its retained \(P'\)-root and is full to
the other four root blocks.  Hence

\[
                 A_P\mid A_Q\mid A_1\mid A_2\mid A_3
                    \mid W_0\mid W_1                 \tag{3.2}
\]

is a \(K_7\)-model, a contradiction. \(\square\)

## 4. Curvature closes every nonsingleton minimum fragment

### Theorem 4.1 (transported atomic-web closure)

Every minimum nested exact fragment \(F\) has order one.

#### Proof

Suppose \(|F|\ge2\).  By Lemmas 2.2, 3.1 and 3.2, \(F\) is a
three-connected plane disk web in which all four portal sets belonging to
\(P'\cup Q'\) lie on the outer face.  For the first curvature count,
triangulate every bounded face arbitrarily and call the resulting disk
\(T\).

Every outer vertex has \(F\)-degree at least three.  An interior vertex
sees no root of \(P'\cup Q'\), so (3.1) gives it \(F\)-degree at least
five.  In the disk-curvature identity

\[
 \sum_{u\in\operatorname{int}T}(6-d_T(u))+
 \sum_{u\in\partial T}(4-d_T(u))=6,                 \tag{4.1}
\]

every positive summand equals one.  Its vertex sees all three roots of
\(R'\).  Let \(U\) be the set of vertices seeing all of \(R'\).  Thus
at least six positive vertices belong to \(U\).

If four vertices of \(U\) are not cofacial, the rooted-\(K_4\) theorem
for a three-connected plane graph gives a \(K_4\)-model in \(F\) rooted
at them.  Its four bags, together with \(A_1,A_2,A_3\), form a
\(K_7\)-model: the latter three bags form a triangle and every rooted bag
sees all three of them.  Therefore every four vertices of \(U\) are
cofacial.  Since two faces of a three-connected plane graph meet in at
most one edge, all of \(U\) lies on one face.

That face must be the outer face.  Otherwise it meets the outer face in
at most two vertices.  Redo the triangulation, this time triangulating the
common \(U\)-face as a fan and all other bounded faces arbitrarily.  Of
the vertices on the common face all but at most two receive a new incident
diagonal, while at most two vertices of \(U\) lie on the outer face.
The same degree count says that every positive-curvature vertex for this
new triangulation belongs to \(U\).  Its positive part would therefore be
at most four, contrary to (4.1).

Consequently all positive vertices are outer.  If \(z\) is one of them,
then \(d_F(z)=3\), and (3.1), together with the fact that no vertex sees
both roots of \(P'\) or both roots of \(Q'\), forces

\[
 N_S(z)=R'\cup\{p(z),q(z)\},
 \qquad p(z)\in P',\quad q(z)\in Q'.                \tag{4.2}
\]

Choose two distinct positive vertices \(z_0,z_1\).  A spanning tree of
\(F\), cut at an edge on its \(z_0z_1\)-path, gives a connected
bipartition \(F=W_0\dot\cup W_1\), with \(z_i\in W_i\) and an edge
between the two parts.  Equation (4.2) makes each \(W_i\) adjacent to all
five transported bags.  The seven bags in (3.2) again form a
\(K_7\)-model, the final contradiction. \(\square\)

### Corollary 4.2 (exact-cut descent reaches a degree-seven singleton)

In the oriented singleton-triangle residue, if the nonowner \(D\) is
nonsingleton, then it contains a vertex \(z\) with

\[
                              d_G(z)=7.              \tag{4.3}
\]

More precisely, \(\{z\}\) is a component behind the exact seven-cut
\(N_G(z)\), nested inside the original \(B\)-side.

#### Proof

Corollary 6.3 of the two-pair web note gives a proper nested exact
fragment.  Choose one of minimum order.  Theorem 4.1 says it is a
singleton, and (1.3) then says its unique vertex has degree seven.
\(\square\)

This is a strict closure of the unbounded exact-cut branch: no
nonsingleton atomic torso, web, or repeated exact-cut ladder survives.
The only endpoint is the same finite-capacity obstruction at a genuine
degree-seven vertex.

## 5. Exact form of the singleton endpoint

Let \(F=\{z\}\).  Lemma 2.1 and the owner packet give five transported
bags forming a \(K_5\), with contact multiplicities

\[
                           2,2,1,1,1                 \tag{5.1}
\]

on the seven distinct vertices of \(N_G(z)\).  The singleton \(\{z\}\)
is adjacent to all five bags, so these six bags form a \(K_6\)-model.

Before using those transported bags, the original five outer bags already
give a useful global restriction.

### Lemma 5.1 (a packet-free nonowner is two-connected)

If \(|D|\ge2\), then \(D\) in fact has order at least three and has no
cutvertex; hence it is two-connected.

#### Proof

Suppose \(w\) is a cutvertex and let \(K_1,\ldots,K_m\), \(m\ge2\),
be the components of \(D-w\).  Each \(K_i\) has no neighbour outside

\[
                            \{w\}\cup B.
\]

Seven-connectivity therefore gives \(|N_B(K_i)|\ge6\).  Record its
possible unique defect \(\delta_i\in B\), using \(\delta_i=\varnothing\)
when it is full.

If \(\delta_i\) is empty or belongs to \(R\), then \(K_i\) is a carrier
for both \(P\) and \(Q\).  Every other component is a carrier for at
least one of those two pairs, so two components give a packet, a
contradiction.  If one defect lies in \(P\) and another in \(Q\), the
corresponding components are respectively \(Q\)- and \(P\)-carriers,
again a packet.  Hence all defects lie in the same pair block, say
\(P\).

It follows that every \(K_i\) is adjacent to each of the five original
outer bags

\[
 (P\cup X_P)\mid(Q\cup X_Q)\mid
 \{r_1\}\mid\{r_2\}\mid\{r_3\}.                 \tag{5.2}
\]

Indeed, missing one root of \(P\) does not miss the aggregate \(P\)-bag,
and the component is full to \(Q\cup R\).  The two connected sets
\(K_1\cup\{w\}\) and \(K_2\) are adjacent and each sees all five bags
in (5.2).  They complete (5.2) to a \(K_7\)-model, a contradiction.
Thus \(D\) has no cutvertex.

It remains to exclude \(|D|=2\), the only convention-sensitive case.
Write \(D=uv\).  Applied to either singleton, seven-connectivity says
that each of \(u,v\) contacts at least six vertices of \(B\).  If one,
say \(u\), has its possible defect in \(R\) (or has no defect), then it
is a singleton carrier for both \(P\) and \(Q\).  The other vertex is a
carrier for at least one of those pairs, giving a packet.  Thus both
defects lie in \(P\cup Q\).  Defects in different pair blocks again give
a packet.  Defects in the same pair block make both \(u\) and \(v\)
adjacent to all five outer bags in (5.2); since \(uv\in E(G)\), those two
singletons complete (5.2) to a \(K_7\)-model.  Therefore \(|D|\ne2\).
The singleton \(|D|=1\) is outside the nested-fragment branch presently
under discussion.  Hence a nonsingleton \(D\) is two-connected. \(\square\)

In particular, at the singleton fragment \(z\),

\[
                         C=D-z                       \tag{5.3}
\]

is connected.  Since its external neighbourhood is contained in
\(\{z\}\cup B\), seven-connectivity gives

\[
                         |N_B(C)|\ge6.               \tag{5.4}
\]

Thus \(C\) has one possible boundary defect \(\delta\).  If
\(\delta\notin P\) then \(C\) is a \(P\)-carrier, and if
\(\delta\notin Q\) it is a \(Q\)-carrier.  Packet-freeness consequently
implies:

* if \(\delta\notin P\), the singleton \(z\) does not see both roots of
  \(Q\);
* if \(\delta\notin Q\), the singleton \(z\) does not see both roots of
  \(P\).

In particular, when \(\delta\in R\cup\{\varnothing\}\), \(z\) sees at
most one root of each pair.  Since \(D\) is two-connected,

\[
                         |N_C(z)|\ge2.               \tag{5.5}
\]

Equations (5.3)--(5.5) are the exact one-defect splitter normal form:
one connected annulus, at most one lost outer label, and at least two
internal portals at the degree-seven hub.

There is one useful immediate closure.  If there is a connected set
\(K\) disjoint from the six displayed bags, adjacent to \(z\) and to
every one of the five transported root bags, then

\[
             A_P\mid A_Q\mid A_1\mid A_2\mid A_3\mid\{z\}\mid K
                                                               \tag{5.6}
\]

is a \(K_7\)-model.

The count (5.4) alone does **not** justify the displayed \(K_7\)-model:
the connected annulus may contain some of the linkage strands used by the
five transported bags, and removing those strands can disconnect it.  The
required next invariant is therefore the placement of the strands, not
the coarse contact row.

What remains is therefore not another web torso: it is a degree-seven
**one-defect splitter**.  The connected annulus has defect at most one,
while the two double-hit \(K_5\) bags cannot yet be split
label-preservingly.  Closing that splitter requires a branch-set peel or a
one-step colouring transition; contact counts alone give only the six
bags above.

## 6. The original full-singleton endpoint has portal surplus

For completeness, suppose the original nonowner itself is the singleton
\(D=\{d\}\).  Then \(N(d)=B\).  In the exact zero-optional triangle
boundary, the edge \(db\) has the four common neighbours

\[
                              \{a,c,1,2\}.          \tag{6.1}
\]

They are the disjoint union of the independent sets \(\{a,1\}\) and
\(\{c,2\}\).  The audited simultaneous-star inequality, applied with
six colours and \(d(d)=7\), gives

\[
                              d_G(b)\ge9.            \tag{6.2}
\]

Indeed equal degree seven would bound (6.1) by three, and unequal degrees
with \(d_G(b)\le8\) would do the same.  Since \(b\) has exactly the five
neighbours \(d,a,c,1,2\) outside the owner shore,

\[
                              |N_O(b)|\ge4.           \tag{6.3}
\]

Thus the full-singleton cell is not the conservative two-portal quotient:
its central triangle root has at least four actual owner portals.  This
does not by itself split a packet carrier--the four portals may all lie
on the same locked side--but any proposed singleton closure may assume
the strict surplus (6.3).

The same simultaneous-star operation gives more than the count.  Put

\[
                              E_b=N_O(b).             \tag{6.4}
\]

The degree-free rooted-core theorem from
`hadwiger_degree9_hub_rainbow_rooted_k4.md`, applied to the edge \(db\)
and the partition in (6.1), gives an \(E_b\)-rooted \(K_4\)-model in

\[
                         G-\{d,b,a,c,1,2\}.          \tag{6.5}
\]

Together with the singleton bag \(\{b\}\), this is a controlled
\(K_5\)-model.  If \(d_G(b)=9\), then \(|E_b|=4\); in every simultaneous
star trace these four portals are rainbow in the four residual colours
and are pairwise joined by the corresponding bichromatic Kempe
components.  Thus the unresolved full-singleton cell also comes with a
rooted four-bag core, not merely four unordered portal vertices.
