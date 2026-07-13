# Connected triangle carriers: the exact contraction boundary

## 1. Purpose

Let \(T\) be a triangle and put \(J=G-T\).  In the distributed-portal
near-\(K_7\) residue, two connected bags meet all three vertices of
\(T\) collectively, but need not contain a vertex complete to \(T\).
A tempting operation is to contract a minimal \(T\)-carrier in each bag
and apply the rooted-\(K_4\) theorem to the quotient.

This note proves the exact separator lift for one contraction and records
the smallest obstruction to the proposed iteration.  The separator half is
valid and useful.  The assertion that a four-colouring of the contracted
core automatically lifts is false, even when four-connectivity survives.

## 2. A failed edge contraction gives an exact adhesion

Before contracting, a minimum three-portal carrier already has a useful
label-free structure.

### Lemma 2.0 (three-portal carriers are triangular block trees)

Let \(P_1,P_2,P_3\) be vertex sets in a graph, and let \(C\) be an
inclusion-minimal vertex set such that \(G[C]\) is connected and meets
each \(P_i\).  Then

1. \(G[C]\) has at most three non-cutvertices;
2. every block of \(G[C]\) has order at most three; and consequently
3. every block is an edge or a triangle, so \(G[C]\) is
   three-colourable and has treewidth at most two.

#### Proof

If \(v\) is not a cutvertex of \(G[C]\), then \(C-\{v\}\) is
connected.  Minimality says that deleting \(v\) must lose one of the
three portal classes.  Thus \(v\) is the unique vertex of \(C\) in
some \(P_i\).  Two different non-cutvertices cannot be unique for the
same class, proving item 1.

Let \(B\) be a block.  A vertex of \(B\) which is not a cutvertex of
\(G[C]\) is already one of the at most three vertices counted above.
For every cutvertex \(b\in V(B)\), the block-cut tree has a component
attached at \(b\) away from \(B\).  That component contains a
non-cutvertex \(\ell_b\) of \(G[C]\).  For distinct cutvertices of
\(B\), these away-components are disjoint, so the vertices \(\ell_b\)
are distinct.  Associating a non-cutvertex of \(B\) with itself and a
cutvertex \(b\) with \(\ell_b\) injects \(V(B)\) into the set of
non-cutvertices of \(G[C]\).  Hence \(|B|\le3\).  A nontrivial
two-connected block of order three is a triangle; bridge blocks are
edges.  The last assertions follow by colouring successively along the
block-cut tree. \(\square\)

Thus an unbounded carrier is not an arbitrary graph: it is a tree of edge
and triangle blocks, with at most three terminal leaves.  The remaining
difficulty is boundary-list propagation along this block tree, not internal
high treewidth.

### Corollary 2.0.1 (two bounded pendant peels)

If \(|C|\ge2\), the carrier in Lemma 2.0 has at least two disjoint sets
\(L_1,L_2\), each of order at most two, such that for each \(L_i\):

* \(G[L_i]\) and \(G[C-L_i]\) are connected;
* \(L_i\) is adjacent to \(C-L_i\); and
* \(L_i\) contains the unique \(C\)-portal for at least one of the three
  portal classes \(P_1,P_2,P_3\) from Lemma 2.0.

#### Proof

If \(G[C]\) has only one block, Lemma 2.0 makes it an edge or a
triangle.  Choose two different singleton vertices.  Each is a
non-cutvertex, deleting it leaves a connected graph, and each is uniquely
charged to a portal class.

Otherwise take two leaf blocks of the block-cut tree of \(G[C]\).  A leaf block is
either an edge with one non-cut end or a triangle with two non-cut
vertices, by Lemma 2.0.  Let \(L_i\) be its non-cut part.  It has order
one or two, is connected, and deleting it leaves the rest of the block-cut
tree connected.  At least one of its non-cut vertices is uniquely charged
to a portal class by the first paragraph of Lemma 2.0.  Distinct leaf
blocks have disjoint non-cut parts. \(\square\)

Thus every nontrivial distributed triangle carrier supplies two literal
one- or two-vertex candidates for the compensating piece \(Z\) in the
two-bag peel certificate.  A surviving obstruction must lock both peels:
moving either one must destroy a different required portal or the opposite
bag contact.  This reduces the carrier-expansion problem to a bounded leaf
state plus possible parity propagation along the intervening edge/triangle
block chain.

### Lemma 2.1 (four-cut lift)

Let \(J\) be four-connected and let \(uv\in E(J)\).  If \(J/uv\) is not
four-connected, then there are distinct vertices
\(x,y\notin\{u,v\}\) such that

\[
                       \{u,v,x,y\}                 \tag{2.1}
\]

is a vertex cut of \(J\).  In particular it is an exact four-cut.

#### Proof

Let \(w\) be the image of \(uv\) in \(J/uv\), and choose a cut
\(S\) of the quotient with \(|S|\le3\).  The vertex \(w\) belongs to
\(S\); otherwise the same set would separate \(J\).  Now

\[
             (S-\{w\})\cup\{u,v\}                 \tag{2.2}
\]

separates in \(J\) the two sides separated by \(S\) in the quotient.
Four-connectivity gives

\[
 4\le |(S-\{w\})\cup\{u,v\}|=|S|+1\le4.
\]

Thus \(|S|=3\), and writing \(S-\{w\}=\{x,y\}\) gives (2.1).
\(\square\)

### Corollary 2.2 (seven-cut lift under a triangle)

If \(G\) is seven-connected, \(T\) is a triangle, \(J=G-T\), and the
hypotheses of Lemma 2.1 hold, then

\[
                    T\cup\{u,v,x,y\}              \tag{2.3}
\]

is an exact seven-cut of \(G\).

#### Proof

The set in (2.3) separates the same two nonempty sides as (2.1), and it
has order seven.  Seven-connectivity says that no smaller cut is possible.
\(\square\)

Thus the **first** contraction of an original carrier edge either preserves
four-connectivity or exports precisely the exact adhesion required by the
cut-descent programme.  No Moser labels are involved.

## 3. What an iterated failure really lifts to

Suppose that some connected pieces have already been contracted and that a
subsequent edge \(uv\) of the quotient is the first non-four-contractible
edge.  Lemma 2.1 still gives a quotient cut
\(\{u,v,x,y\}\).  If \(u,v\) represent connected original sets
\(U,V\), its lift has adhesion

\[
                       U\cup V\cup\{x,y\}.         \tag{3.1}
\]

This is a connected portal adhesion, but its cardinality need not be four.
Consequently it cannot be called an exact four-cut, and adjoining \(T\)
does not by itself give an exact seven-cut.  A valid iteration therefore
needs an additional peel theorem that replaces the two connected pieces in
(3.1) by at most two actual portal vertices, or directly performs the
two-bag surgery.

## 4. Safe contraction does not preserve four-colourability

The exact obstruction to lifting a **single edge split** can nevertheless
be expressed by two strong-Hadwiger states.

### Lemma 4.0 (edge-split colouring or bilateral rooted states)

Let \(uv\in E(J)\), let \(Q=J/uv\), and denote the contracted vertex by
\(d\).  Put

\[
 A=N_J(u)-\{v\},\qquad B=N_J(v)-\{u\},
\]

viewing \(A,B\) as subsets of \(V(Q)-\{d\}\).  If \(Q\) is
four-colourable, then either

1. \(J\) is four-colourable; or
2. each of \(A\cup\{d\}\) and \(B\cup\{d\}\) takes all four
   colours in every proper four-colouring of \(Q\).

In outcome 2, the strong four-colour Hadwiger theorem gives both an
\((A\cup\{d\})\)-rooted and a
\((B\cup\{d\})\)-rooted \(K_4\)-model in \(Q\).

#### Proof

Fix a four-colouring \(c\) of \(Q\) and put \(\alpha=c(d)\).  Every
vertex of \(A\cup B\) avoids \(\alpha\).  If \(B\) omits some other
colour \(\beta\), expand the colouring by giving \(u\) colour
\(\alpha\) and \(v\) colour \(\beta\).  This is proper: all neighbours
of \(u\) represented at \(d\) avoid \(\alpha\), all neighbours of
\(v\) avoid \(\beta\), and \(uv\) has differently coloured ends.
The symmetric argument works when \(A\) omits a colour other than
\(\alpha\).

Consequently, if no four-colouring of \(J\) exists, then in every
four-colouring of \(Q\), both \(A\) and \(B\) use all three colours
different from \(c(d)\).  Adjoining \(d\) shows that each of the two
displayed sets uses all four colours.  Strong \(HC_4\) gives the final
rooted models. \(\square\)

Thus the safe edge-contraction obstruction is not an unstructured failure
to lift: it produces two simultaneous rooted \(K_4\) states, one for each
side of the carrier edge.  A near-\(K_7\) proof may close the edge-carrier
base case by composing either state with the opposite complex bag; without
that composition, the following example shows that the colouring failure
is real.

### Proposition 4.1 (minimal chromatic counterarchitecture)

Let

\[
                         J=K_2\vee C_5.
\]

Then \(J\) is four-connected and five-chromatic.  If \(e\) is any rim
edge of the \(C_5\), then

\[
                 J/e\cong K_2\vee C_4
\]

is still four-connected but is four-colourable.

#### Proof

For noncomplete graphs \(A,B\), vertex connectivity of a join satisfies

\[
 \kappa(A\vee B)=min\{|B|+\kappa(A),
                         |A|+\kappa(B),\delta(A\vee B)\}.
\]

Here \(\kappa(C_5)=\kappa(C_4)=2\).  Hence both displayed joins are
four-connected.  Join additivity of chromatic number gives

\[
 \chi(K_2\vee C_5)=2+3=5,
 \qquad
 \chi(K_2\vee C_4)=2+2=4.
\]

Contracting a rim edge of \(C_5\) produces \(C_4\), proving the
isomorphism and the claim. \(\square\)

The edge \(e\) can be viewed as a minimal connected carrier: distribute
three portal labels between its two ends so that neither end carries all
three.  Proposition 4.1 therefore refutes the implication

\[
 \begin{gathered}
 \text{minimal carrier contraction preserves four-connectivity}\
 \Longrightarrow
 \text{a four-colouring of the quotient lifts to the original core}.
 \end{gathered}                                    \tag{4.1}
\]

The obstruction is not an artificial low-connectivity graph:
\(K_2\vee C_5\) is the dense degree-seven neighbourhood type already
encountered in the planar/two-apex extremal architecture.

## 5. Correct connected-carrier endpoint

Let \(D_0,E_0\) be disjoint minimal connected \(T\)-carriers in
\(J\).  Contracting them can support a proof only through the following
three-way conclusion.

1. A contraction fails at an original edge, and Corollary 2.2 gives an
   exact seven-adhesion.
2. A later contraction fails, and the lifted connected adhesion (3.1) must
   be converted by a genuine portal-peel theorem into the two-bag
   certificate of Lemma 3.3 in
   `hadwiger_near_k7_two_complex_bag_round.md`.
3. Both carriers contract through a four-connected quotient.  Rooted
   \(K_4\) and the strong-\(HC_4\) triangle dichotomy apply to that
   quotient, but Proposition 4.1 shows that one still needs a
   portal-sensitive colouring expansion of \(D_0,E_0\).  Quotient
   four-colourability alone is not enough.

The exact missing lemma is therefore not another unqualified contraction
statement.  It is a **carrier expansion-or-peel lemma**: either a
six-colouring of the contracted triangle/core instance expands across both
minimal carriers, or one carrier has a label-preserving peel, or an exact
seven-adhesion is exposed.  Any proposed proof must defeat Proposition 4.1
by explicitly using the three portal labels and the simultaneous second
carrier.
