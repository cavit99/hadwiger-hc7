# Dirty connectors collapse to a rooted-triangle exchange or a two-shore adhesion

## 1. Setting

Use the notation of Theorem 4.5 of
`hadwiger_four_connected_rooted_diamond.md`.  Thus

\[
                 T_0=\{h,1,2\},\qquad F=G-T_0,
\]

where (G) is seven-connected, (h12) is a triangle, and
(Q=F/56) is four-connected.  In the dirty-routing outcome, fix a
rooted (K_4)-model in (Q) at

\[
                        p,e_6,e_0,v,
\]

and lift it to four pairwise adjacent, disjoint, connected sets

\[
                        P,A_1,A_2,A_3                    \tag{1.1}
\]

in (F).  Here (5,6\in P), and (A_1,A_2,A_3) contain
(e_6,e_0,v), respectively.  In particular each (A_i) contains a
vertex adjacent to all three members of (T_0), while (P) contains
(6), which sees (1,2).

Let (r_5) be the prescribed root in the old bag (R_5), so
(hr_5\in E(G)), and let

\[
                    R\subseteq R_5
\]

be any (5)-(r_5) path.  The old model makes

\[
              \{e_6,e_0,v\}\cap V(R)=\varnothing.       \tag{1.2}
\]

The path is allowed to meet all three sets (A_i), repeatedly.  Put

\[
 C=P\cup R,qquad H=F-V(C),                               \tag{1.3}
\]

and, for (i=1,2,3), let (K_i) be the component of
(A_i-V(C)) containing the prescribed root of (A_i).

The point of (1.3) is that it absorbs the *whole* dirty connector at
once.  It does not assume that a first dirty vertex is peelable.

## 2. The three surviving root cores all contact the absorbed carrier

### Lemma 2.1 (simultaneous connector absorption)

The sets (C,K_1,K_2,K_3) are pairwise disjoint and connected, and

\[
                             C\sim K_i
                 \qquad (i=1,2,3).                         \tag{2.1}
\]

Moreover, (C) is adjacent to every member of (T_0), and each
(K_i) contains a vertex adjacent to every member of (T_0).

#### Proof

The set (C) is connected because (P) is connected, (5\in P\cap R),
and (R) is a path.  It contains (6) and (r_5), so it sees (1,2)
through (6) and (h) through (r_5).

The roots (e_6,e_0,v) avoid (C): they lie outside (P) because
the four bags in (1.1) are disjoint, and they avoid (R) by (1.2).
Thus every (K_i) is defined and contains its root.  The claimed
contacts to (T_0) follow from those roots.

If (A_i\cap R=\varnothing), then (K_i=A_i), and the old model edge
(PA_i) gives (2.1).  If (A_i\cap R\ne\varnothing), every component
of (A_i-V(R)) has a neighbour on (R): otherwise that component
would be disconnected from (A_i\cap R) inside the connected graph
(A_i).  In particular (K_i\sim R\subseteq C).  Disjointness is
immediate from the old model and the deletion in the definition of the
(K_i). \(\square\)

Thus absorbing a dirty connector never loses the three carrier contacts.
It can lose only adjacencies *among* the three surviving root cores.

## 3. A rooted-triangle lemma for three connected root sets

We use the following elementary form of the rooted (K_3) theorem.

### Lemma 3.1 (rooted triangle or a root-set separator)

Let (J) be two-connected and let (K_1,K_2,K_3\subseteq V(J)) be
pairwise disjoint connected sets.  Then one of the following holds.

1. There are pairwise disjoint connected sets (L_1,L_2,L_3) with
   (K_i\subseteq L_i) such that the (L_i) are pairwise adjacent.
2. For some permutation (i,j,k) of (1,2,3), the sets (K_j,K_k)
   lie in distinct components of (J-K_i).

#### Proof

Contract each (K_i) to a vertex (q_i), and call the resulting graph
(J').  A vertex (x\notin\{q_1,q_2,q_3\}) cannot be a cutvertex of
(J'): the graph (J-x) is connected, and contracting three connected
sets cannot disconnect it.  Hence every cutvertex of (J') belongs to
(\{q_1,q_2,q_3\}).

If one (q_i) separates (q_j) from (q_k), lifting the components of
(J'-q_i) gives outcome 2.  Suppose no (q_i) does so.  In the
block-cut tree of (J'), the three vertices (q_1,q_2,q_3) then belong
to one common nontrivial block.  Indeed, otherwise the minimal subtree
joining their block occurrences has a separating cutvertex; every such
cutvertex is one of the (q_i), and it separates the other two roots,
contrary to the assumption.

A two-connected graph contains a (K_3)-model rooted at any three
vertices.  If the third root lies on a cycle through the first two,
split that cycle into three bags.  Otherwise, take a cycle through the first two roots
and a two-fan from the third root to distinct vertices (x,y) of that
cycle.  If the first two roots lie on the same (x)-(y) arc, put the
other, root-free arc and the two-fan in the third bag, and split the
remaining arc between the first two bags.  If the roots lie on different
arcs, use the resulting theta: put (x), the first root, and the segment
of its arc between them in the first bag; put the interior of the other
arc in the second bag; and put (y), the third root and the remaining
segments in the third bag.  The three division edges give the three
pairwise adjacencies.  Apply this inside the common block and lift the
contractions of the (K_i).  This gives outcome 1. \(\square\)

The second outcome is sharp.  Contracting a connected root set can turn
it into a cutvertex even though the uncontracted graph is two-connected.
The lemma records exactly that failure rather than assuming that
two-connectivity survives the contraction.

## 4. The dirty-connector dichotomy

### Theorem 4.1 (clean rooted triangle or a loaded adhesion)

Retain the setting of Section 1.  At least one of the following holds.

1. **Rooted-triangle absorption.**  The graph (G) contains a
   (K_7)-minor.
2. **Carrier one-cut.**  The graph (H) is disconnected.  After
   contracting (C) to a vertex (c), the vertex (c) is a cutvertex
   of (F/C).  Every component (D) of (H) has at least four
   distinct neighbours in (C).  More precisely, with
   \[
                    \lambda(D)=|N_G(D)\cap T_0|,
   \]
   one has
   \[
                    |N_G(D)\cap C|\ge 7-\lambda(D)\ge4.   \tag{4.1}
   \]
3. **Carrier two-cut.**  The graph (H) is connected but has a
   cutvertex (z).  In (F/C), the set \(\{c,z\}\) is an exact
   two-vertex cut, and every component (D) of (H-z) is adjacent to
   both (c) and (z).  In the uncontracted graph it has
   \[
                    |N_G(D)\cap C|\ge 6-\lambda(D)\ge3.   \tag{4.2}
   \]
4. **Root-gate two-root-shore state.**  The graph (H) is two-connected,
   and for some permutation (i,j,k), the sets (K_j,K_k) lie in
   distinct components (D_j,D_k) of (H-K_i).  Let
   (\widehat K_i) be (K_i) together with every root-free component
   of (H-K_i) having no neighbour in (C).  Contracting (C)
   and (\widehat K_i) to (c,k_i), respectively, makes
   \(\{c,k_i\}\) an exact two-vertex cut separating (D_j,D_k).  Both of
   these selected root shores are adjacent to both cut vertices; there
   may also be additional root-free shores.  In the original
   graph, for \(\ell\in\{j,k\}\),
   \[
      |N_H(D_\ell)\cap K_i|\ge2,\qquad
      |N_F(D_\ell)\cap C|\ge1,                            \tag{4.3}
   \]
   and
   \[
      |N_G(D_\ell)\cap(C\cup \widehat K_i)|
                          \ge7-\lambda(D_\ell)\ge4.       \tag{4.4}
   \]

#### Proof

If (H) is disconnected, then for every component (D) of (H),

\[
                             N_F(D)\subseteq C.
\]

Another component remains, so (N_F(D)) separates the four-connected
graph (F).  It has order at least four.  In (G), all further
neighbours lie in (T_0), and seven-connectivity gives (4.1).  This is
outcome 2.

Suppose (H) is connected and has a cutvertex (z).  Every component
(D) of (H-z) is adjacent to (z), and

\[
                             N_F(D)\subseteq C\cup\{z\}.
\]

The neighbourhood again separates (F), so four-connectivity gives at
least three distinct (C)-neighbours.  Seven-connectivity of (G)
gives (4.2).  Contracting (C) proves all assertions in outcome 3.

It remains that (H) is two-connected.  Apply Lemma 3.1 to
(K_1,K_2,K_3).  In its first outcome, let (L_1,L_2,L_3) be the
rooted triangle.  Lemma 2.1 says that each (L_i), because it contains
(K_i), is adjacent to (C).  Therefore the seven sets

\[
                    \{h\},\quad\{1\},\quad\{2\},\quad
                    C,\quad L_1,\quad L_2,\quad L_3       \tag{4.5}
\]

form a (K_7)-model.  The first three form a triangle; (C) sees
(h,1,2) through (r_5,6,6); each (L_i) sees them through its
prescribed root; and the last four sets form a clique by Lemmas 2.1
and 3.1.  This is outcome 1, with every one of the twenty-one
adjacencies explicitly accounted for.

In the second outcome of Lemma 3.1, take the two components (D_j,D_k)
containing (K_j,K_k).  They are distinct.  Because (H) is
two-connected, each has at least two distinct neighbours in (K_i):
one neighbour would be a cutvertex separating it from the other root
shore.  Each shore also meets (C), because it contains (K_j) or
(K_k), respectively, and Lemma 2.1 gives \(K_j,K_k\sim C\).

Put \(\widehat K_i\) as in the statement.  Every absorbed component
has a neighbour in \(K_i\), so \(\widehat K_i\) is connected.  Every
component left outside it has a neighbour in \(C\) by construction;
in particular \(D_j,D_k\) do, as just observed.  Thus, after the two
contractions, every remaining shore is full to the cut
\(\{c,k_i\}\).  Deleting \(c\) leaves the connected contraction
\(H/\widehat K_i\), while deleting \(k_i\) leaves all remaining shores
joined through \(c\).  Hence the cut is exact.  Finally

\[
             N_G(D_\ell)\subseteq C\cup \widehat K_i\cup T_0,
\]

and the other root shore remains outside.  Seven-connectivity gives
(4.4).  This proves outcome 4. \(\square\)

The theorem is stronger than a first-dirty-vertex reduction.  It absorbs
every intersection of (R) with every rooted bag simultaneously.  Its
only non-(K_7) outcomes are a one- or two-vertex adhesion after
contracting the connected carrier, or a two-root-shore adhesion after also
contracting one connected root gate.  Outcome 4 does not assert that the
quotient has exactly two components; it singles out the two components
carrying the other prescribed roots, and proves that every additional
component is full to the same two-vertex quotient cut.

## 5. What lexicographic minimality adds

The preceding theorem requires no optimization.  The usual minimal
model/path choice nevertheless gives a useful local normal form.

### Lemma 5.1 (the first dirty hit is a locked root lobe)

Choose the rooted model and (R) to minimize, in order,

\[
  \sum_{i=1}^3 |V(R)\cap A_i|,qquad
  |P|+|A_1|+|A_2|+|A_3|,qquad |R|.                       \tag{5.1}
\]

Normalize a clean initial segment of (R) into (P), and let (x)
be the first remaining vertex of (R) in, say, (A_i).  Let (K) be
the component of (A_i-x) containing its prescribed root.  Then (K)
is anticomplete to at least one of the other two rooted bags.

#### Proof

The root of (A_i) is one of (e_6,e_0,v), so (1.2) implies that it
is not (x).  Suppose (K) retained an edge to each of the other two
rooted bags.  Move the clean prefix together with (x) into (P),
replace (A_i) by (K), and discard the other components of
(A_i-x).  The new (P)-bag is connected.  The edge from (x) to
(K) preserves the (P K) adjacency, while (K) retains the other
two required model adjacencies by assumption.  All roots and all other
model edges are untouched.  This is another rooted (K_4)-model with
strictly fewer dirty vertices on the same connector, contradicting
(5.1). \(\square\)

Thus a minimal first hit is not merely “dirty”: it is a literal
one-vertex gate inside a rooted bag, and the root side loses a specified
clique label.  The global Theorem 4.1 says that all such gates, considered
simultaneously along the connector, either reroute to a rooted triangle or
coalesce into one of the displayed two-shore adhesions.

## 6. Synchronization with the critical edge (56)

The edge (56) remains inside (C), so the operation-level information
of `hadwiger_critical_edge_split_cycles.md` is not lost.  In every
six-colouring of (G/56), for each of the five colours other than the
colour of the contracted vertex, there is either a common-coloured
neighbour of (5,6) or a bichromatic (5)-(6) path whose first and
last incidences have opposite side labels.

In outcomes 2--4 of Theorem 4.1, intersect such a path with a displayed
shore and take a maximal shore subpath.  Its ends lie in the exact
uncontracted boundary displayed in that outcome:

\[
 C\cup T_0,qquad C\cup\{z\}\cup T_0,qquad
 C\cup K_i\cup T_0,                                      \tag{6.1}
\]

respectively.  Hence every fan member which uses a shore supplies a
colour-labelled boundary-to-boundary excursion in that shore, while the
two incidences at the central contracted vertex retain their (5)- and
(6)-side labels.  This is precisely the extra transition data required
by a two-shore capacity-state exchange.

No claim is made that a fan member must use a particular shore.  That
would require a colour-to-bag alignment which the split-cycle theorem
does not provide.  The rigorous gain here is instead that the dirty
connector branch has been reduced to exact one-/two-adhesion quotients
with explicit portal lower bounds, and the critical fan now decorates
those quotients without any further contraction of the critical edge.

## 7. Exact residue

In a (K_7)-minor-free nested state, every choice of rooted model and
(5)-(r_5) connector therefore yields one of outcomes 2--4 of
Theorem 4.1.  In particular, if even one choice has a two-connected
remainder in which no surviving root core separates the other two, the
dirty branch closes completely.

The remaining theorem is no longer an unrestricted reserved-connector
statement.  It is the following bounded-interface exchange:

> two full shores behind the quotient cut \(\{c,z\}\) or
> \(\{c,k_i\}\), carrying the portal loads (4.2)--(4.4) and the
> side-labelled (56)-fan, cannot realize a contraction-critical
> state.

That is the same two-shore capacity-state object arising in the central
full-adhesion branch, so the two outcomes of Theorem 4.5 now feed a common
structural target.

## 8. The portal load already closes the distributed root-gate case

Outcome 4 has more information than the existence of a quotient two-cut.
Both selected root shores have at least two distinct portals in the
connected gate \(\widehat K_i\).  The following exact split consumes that
capacity.

### Lemma 8.1 (allocated root-gate split)

Use outcome 4 and write \(K=\widehat K_i\).  Suppose

\[
                            K=X\mathbin{\dot\cup}Y
                                                               \tag{8.1}
\]

is a partition into nonempty connected sets such that

\[
\begin{aligned}
 &\text{the prescribed root of }K\text{ lies in }Y,\\
 &X\sim D_j,D_k,\\
 &Y\sim C,D_k.
\end{aligned}                                                \tag{8.2}
\]

Then \(G\) contains a \(K_7\)-minor.

#### Proof

Use the seven bags

\[
 \{h\},\quad\{1\},\quad\{2\},\quad
 D_j\cup X,\quad D_k,\quad C,\quad Y.                        \tag{8.3}
\]

The fourth bag is connected through the \(X\)-\(D_j\) contact.  The
last four bags form a clique.  Their six contacts are, respectively,

\[
 XD_k,\quad D_jC,\quad XY,\quad D_kC,\quad D_kY,\quad CY.    \tag{8.4}
\]

Here \(XY\) is an edge because the two nonempty connected sides partition
the connected graph \(K\).  Each of the last four bags sees all of
\(T_0\): the first two use the prescribed roots in \(K_j,K_k\), the
third uses \(6,r_5\), and the last uses the prescribed root in \(K\).
Together with the triangle \(h12\), these are all twenty-one required
adjacencies. \(\square\)

The required split follows from a two-target linkage unless a single gate
vertex or the protected root--carrier core blocks it.

### Theorem 8.2 (distributed capacity or a protected-core gate)

Fix one of the two orientations \((j,k)\).  Let

\[
 A=N_K(D_k),\qquad B=N_K(D_j),                               \tag{8.5}
\]

so \(|A|,|B|\ge2\).  Let \(W\subseteq K\) be any connected set containing
the prescribed root of \(K\) and a \(C\)-portal.  Put \(B'=B-V(W)\).
Then at least one of the following holds.

1. \(G\) contains a \(K_7\)-minor.
2. \(B'=\varnothing\); equivalently, the protected root--carrier core
   \(W\) owns every \(D_j\)-portal in \(K\).
3. There is one vertex \(s\in V(K)-V(W)\) meeting every path in \(K\)
   from \(A\) to \(B'\cup V(W)\), or the connected core \(W\) meets
   every \(A\)-\(B'\) path.

The assertion holds independently after interchanging \(j,k\).

#### Proof

Assume \(B'\ne\varnothing\), contract \(W\) to one vertex \(w\), and
write \(K'=K/W\).  Let \(A'\) be the image of \(A\).  Apply the
two-target form of vertex Menger in \(K'\), with sink set \(A'\) and
the two disjoint target classes \(B'\) and \(\{w\}\).

For clarity, this form follows from the strict gammoid with sink set
\(A'\).  If there is no independent pair with one element in each
target class, every nonloop element of \(B'\) is parallel to the
nonloop element \(w\).  Hence the union has rank one.  Menger's theorem
then gives a one-vertex transversal for all \(A'\)-to-\(B'\cup\{w\}\)
paths.  If the transversal is not \(w\), it lifts to the single vertex
in outcome 3.  If it is \(w\), every \(A\)-\(B'\) path in \(K\) meets
\(W\), which is the other part of outcome 3.

Otherwise there are two vertex-disjoint paths in \(K'\), starting at
distinct vertices of \(A'\), one ending in \(B'\) and the other ending
at \(w\).  The first avoids \(w\).  Lift the two paths to \(K\).

Truncate the first lifted path at its first vertex of \(B'\), and the
second at its first vertex of \(W\).  Let \(X_0\) be the former path,
and let \(Y_0\) be the union of \(W\) with the latter path.  They are
disjoint connected sets (the first path avoids \(W\), and the two paths
are disjoint).
Contract \(X_0,Y_0\), extend them to a spanning tree of the connected
graph \(K\), and delete an edge on the tree path between the two
contracted vertices.  Undoing the contractions gives a connected
bipartition \(K=X\dot\cup Y\) with

\[
 X_0\subseteq X,\qquad Y_0\subseteq Y.                      \tag{8.6}
\]

The \(A\)-end of each path gives \(X,Y\sim D_k\); the \(B'\)-end gives
\(X\sim D_j\); and \(W\subseteq Y\) supplies both the prescribed root
and the \(C\)-contact.  Lemma 8.1 gives outcome 1. \(\square\)

The separator alternative is an actual new descent, not an unspecified
failure of splitting.  In its singleton form, deleting \(s\) separates
every component meeting \(A-\{s\}\) inside \(K\) from either the
opposite-shore portal class or the protected root--carrier core.  In its
other form, the specified connected protected core itself separates the
two portal roles.  Thus, in a
\(K_7\)-minor-free state, both orientations of the root-gate must exhibit
one of two rigid ownership patterns:

* the protected core owns an entire opposite-shore portal class; or
* a specified single vertex is a common transversal for all paths from
  one double portal class to the other portal class and the protected
  core, or that protected core separates the two portal classes.

This closes every root-gate state with distributed two-target capacity.
The singleton-transversal residue is the same bottleneck-lobe geometry
handled by the alternating carrier exchange.  The protected-core separator
is genuinely broader and is not declared closed here; it is the remaining
nested case for a portal-core peel.

### Corollary 8.3 (a two-connected gate cannot have a root carrier edge)

In a \(K_7\)-minor-free root-gate state, if \(K=\widehat K_i\) is
two-connected, then its prescribed root is not adjacent to \(C\).

#### Proof

Let \(r\) be the prescribed root and suppose \(r\sim C\).

If \(r\) is adjacent to at least one selected root shore, call that shore
\(D_k\).  Put

\[
                             Y=\{r\},\qquad X=K-r.           \tag{8.7}
\]

Two-connectivity makes \(X\) connected.  Both selected shores have at
least two distinct portals in \(K\), so \(X\) meets both \(D_j,D_k\).
The singleton \(Y\) meets \(C,D_k\) and contains the root.  Lemma 8.1
gives a \(K_7\)-minor.

It remains that \(r\) misses both selected shores.  Apply Theorem 8.2
with \(W=\{r\}\).  Here \(B'=B\) and both \(A,B\) have order at least
two.  No vertex \(s\) meets every \(A\)-to-\(B\cup\{r\}\) path: choose
vertices of \(A-s\) and \(B-s\), and join them in the connected graph
\(K-s\).  Nor does \(W\) meet every \(A\)-\(B\) path, since \(K-r\)
is connected.  Thus Theorem 8.2 again gives \(K_7\), a contradiction.
\(\square\)

Consequently the protected-core residue has a genuine geometric
restriction: either the root gate has a cutvertex, or every
root-to-carrier connector inside it has positive length.  The latter is
the first setting in which portal order along a minimal protected path,
rather than mere portal incidence, can matter.

### Corollary 8.4 (the two-connected residue is a path-bridge web)

Assume \(G\) has no \(K_7\)-minor and \(K\) is two-connected.  Let \(W\)
be a shortest path in \(K\) from the prescribed root to a \(C\)-portal.
For either orientation \((j,k)\), put

\[
                        A=N_K(D_k),\qquad B=N_K(D_j).
\]

Then at least one of the following holds:

1. \(A\subseteq V(W)\);
2. \(B\subseteq V(W)\);
3. no component of \(K-V(W)\) contains both a vertex of \(A\) and a
   vertex of \(B\).

Moreover every component of \(K-V(W)\) has at least two distinct
neighbours on \(W\).

#### Proof

Apply Theorem 8.2.  Its singleton-transversal outcome is impossible in
a two-connected \(K\): if \(s\notin W\), choose
\(a\in A-\{s\}\) (possible because \(|A|\ge2\)) and any \(w\in W\);
the connected graph \(K-s\) has an \(a\)-\(w\) path avoiding \(s\).

Thus either \(B\subseteq W\), or \(W\) meets every
\(A\)-\((B-W)\) path.  If \(A\subseteq W\) this is outcome 1.
Otherwise, a component of \(K-W\) meeting both \(A\) and \(B\) would
contain such a path avoiding \(W\), a contradiction.  This gives outcome
3.  Finally, a component of \(K-W\) with only one neighbour on \(W\)
would make that neighbour a cutvertex of \(K\); two-connectivity excludes
it. \(\square\)

Hence the surviving two-connected gate is literally a path society:
each off-path bridge has at least two attachments, but no bridge carries
both selected shore labels unless one whole portal class has collapsed
onto the protected path.  This is the precise rotation/web state on which
a bridge-crossing exchange can act.

In fact, model minimality consumes every nontrivial off-path bridge.  The
following statement is phrased for the near-clique core, so it remains
valid after each absorption even though the two shores need no longer be
literal components of the original \(H-K_i\).

### Theorem 8.5 (off-path bridge absorption descent)

Suppose

\[
                 \{h\},\{1\},\{2\},C,K,D_1,D_2              \tag{8.8}
\]

is a \(K_7^-\)-model whose only nonrequired pair is \(D_1D_2\).
Assume:

* \(C,K,D_1,D_2\) are connected and each is adjacent to every member of
  \(T_0=\{h,1,2\}\); the bags \(K,D_1,D_2\) retain their specified
  \(T_0\)-complete roots;
* \(r\in K\) is the specified \(T_0\)-complete root;
* \(K\sim C\); and
* each \(D_\ell\) has at least two distinct portal vertices in \(K\).

If \(G\) has no \(K_7\)-minor and \(K\) is two-connected, then one can
replace (8.8) by another \(K_7^-\)-model with the same singleton
triangle and the same missing pair, but with a strictly smaller
connected root bag \(K'\).  The new root bag still contains \(r\), meets
\(C\), and has at least two portals to each \(D_\ell\).  It may already
be not two-connected, in which case the descent stops.

Consequently, repeated exchanges terminate with a connected root bag
which is not two-connected.  Equivalently, it has a cutvertex or has at
most two vertices.  No two-connected path-bridge web survives.

#### Proof

Choose a \(C\)-portal \(q\in K\), and let \(W\) be a shortest
\(r\)-\(q\) path in \(K\).  Corollary 8.3 gives \(q\ne r\), so
\(W\) has at least two vertices.  Use the two shore portal classes as the
sets \(A,B\) of Corollary 8.4.  In a \(K_7\)-minor-free graph, every
component \(U\) of \(K-V(W)\) is **pure**:

* if \(A\subseteq W\), it contains no \(A\)-portal;
* if \(B\subseteq W\), it contains no \(B\)-portal; and
* otherwise Corollary 8.4 forbids it from containing both types.

Also $D_1,D_2$ are actually anticomplete.  Although their adjacency
is formally only "not required" in (8.8), any edge between them would
complete the seven displayed bags to a $K_7$-model.

If \(U\) contains no shore portal, discard \(U\) from \(K\).  If it
contains only \(D_\ell\)-portals, move all of \(U\) from \(K\) into
\(D_\ell\).  In either case put

\[
                         K'=K-V(U).                         \tag{8.9}
\]

The set \(K'\) is connected: it contains \(W\), and every other component
of \(K-W\) attaches to \(W\).  It retains \(r,q\), hence the specified
root and the \(C\)-contact.  In the absorption case
\(D'_\ell=D_\ell\cup U\) is connected through a shore portal.  It stays
anticomplete to the opposite shore because \(U\) is pure.  The old
contacts not involving \(K,D_\ell\) are untouched.

It remains to check \(K'D'_\ell\).  Since \(K\) is two-connected, \(U\)
has at least two distinct neighbours on \(W\); one attachment would be a
cutvertex.  After the absorption those attachment edges are two distinct
\(K'\)-\(D'_\ell\) portals.  The other shore's two portal vertices were
not in \(U\), by purity, and so also remain in \(K'\).  Thus (8.8) is
replaced by the asserted smaller model.  If \(K'\) is two-connected,
repeat.

For completeness, all six pairs among the four nonsingleton bags have
now been audited.  The pairs $CD'_\ell,CD_{3-\ell}$ keep their old
edges; $CK'$ keeps the edge at $q$; $K'D'_\ell$ uses the two
$U$-to-$W$ attachments; and $K'D_{3-\ell}$ keeps the old portal
vertices outside $U$.  The sixth pair $D'_\ell D_{3-\ell}$ remains
precisely the deficient pair.  The specified roots in $K,D_1,D_2$,
and hence all their contacts to $T_0$, remain in their old branch-set
roles.

At a repeated step the portal classes are recomputed for the current
shore bags.  The same fixed path $W$ is still valid.  Since $U$ was a
whole component of $K-W$, it has no edge to another off-$W$ component.
Absorbing it can therefore add new portals only at its attachment
vertices on $W$; the portal labels of every remaining component of
$K'-W$ are unchanged.  Vertex deletion cannot create a shorter
$r$-$q$ path, so $W$ remains shortest.  Thus Corollary 8.4 applies
afresh whenever $K'$ is two-connected.

The process is finite.  Suppose it removed every off-\(W\) component
while all successive root bags remained two-connected.  The surviving
root bag has vertex set \(V(W)\).  It has no edge joining nonconsecutive
vertices of \(W\), because such an edge would shortcut the chosen
shortest \(r\)-\(q\) path.  Hence it is exactly the path \(W\), which is
not two-connected.  This contradiction proves that the descent reaches a
non-two-connected root bag first. \(\square\)

This theorem subsumes the proposed crossing-versus-laminar bridge
analysis at the level needed here.  A mixed labelled bridge is the
positive distributed-capacity case and gives \(K_7\); a pure bridge,
whether crossing or laminar in the path order, is absorbed into its
unique shore.  Thus laminar bridge nesting cannot persist indefinitely:
it ends at a literal cutvertex (or a gate of order at most two), rather
than at another unbounded web.

### Corollary 8.6 (singleton-or-cutvertex normal form)

The descent in Theorem 8.5 can be continued until the tracked root bag is
either a singleton or has a cutvertex.

#### Proof

Only a two-vertex terminal gate needs comment.  Write it as
\(K=\{r,q\}\), where \(r\) is the protected root and \(q\) is the
chosen \(C\)-portal.  The two-portal conclusion retained by Theorem 8.5
forces both \(r,q\) to be adjacent to each of \(D_1,D_2\).  Move \(q\)
from \(K\) into \(C\).  The new carrier \(C'=C\cup\{q\}\) is connected;
the edge \(rq\) preserves \(rC'\); and \(r\) retains both shore
contacts.  Thus

\[
                 \{h\},\{1\},\{2\},C',\{r\},D_1,D_2
\]

is the same \(K_7^-\)-model with singleton tracked root bag. \(\square\)

Here $q$ is still the original endpoint of the fixed path $W$: every
root bag in the descent contains all of $W$.  Hence a terminal root bag
of order two forces $W=rq$, so $rq\in E(G)$, and $q$ has never lost
its edge to $C$.  These are exactly the two edges used in the displayed
move.

The remaining dirty-web obstruction is therefore not an unbounded
two-connected society.  It is a near-\(K_7\) model with either a literal
one-vertex root bag or a cutvertex lobe.  Closing those two normal forms
requires the contraction-critical transition; static bridge order has
been exhausted.

### Corollary 8.7 (the singleton gate is not \(v\))

In the nested Moser application, the singleton root produced by
Corollary 8.6 cannot be \(\{v\}\).

#### Proof

The carrier \(C\) still contains both \(5\) and \(6\).  If the singleton
tracked bag were \(\{v\}\), its three neighbours in the singleton
triangle are \(h,1,2\), and two more neighbours, \(5,6\), already lie in
\(C\).  Since

\[
                         N_G(v)=\{h,1,2,3,4,5,6\},
\]

the required adjacencies from \(\{v\}\) to the two deficient shores
\(D_1,D_2\) must use \(3\) and \(4\), one in each shore.  But
\(34\in E(G)\), so \(D_1\sim D_2\).  The supposedly missing model edge
is present, and the seven displayed bags form a \(K_7\)-model. \(\square\)

Thus a surviving singleton gate must carry one of the two exterior left
roots \(e_6,e_0\).  The degree-seven Moser root itself is completely
eliminated from the dirty-web residue.

## 9. The operation-level terminal state

The singleton and cutvertex endpoints admit two further exact
normalizations.  The first one removes a spurious cutvertex residue; the
second synchronizes the colour of a surviving exterior singleton with the
critical edge \(56\).

### Lemma 9.1 (pure owner lobes are not terminal)

Use the label-free setting of Theorem 4.1 of
hadwiger_general_protected_web_absorption.md.  Let \(q\) be a cutvertex
of \(K\), let \(U\) be a component of \(K-q\) disjoint from the protected
core, and suppose \(U\) is portal-pure of label \(i\).  Even when \(U\)
owns the whole \(i\)-portal class,

\[
                         A_i\subseteq U\cup\{q\},          \tag{9.1}
\]

one may replace

\[
               K\longmapsto K-U,\qquad
               D_i\longmapsto D_i\cup U.                  \tag{9.2}
\]

This is again a \(K_t^-\)-model with the same protected core and the same
deficient pair.  The only possible loss is that the new \(K\)-\(D_i\)
portal class may have order one.

#### Proof

The set \(K-U\) is connected and contains the protected core.  The set
\(D_i\cup U\) is connected through an old \(U\)-\(D_i\) portal.  Since
\(U\) is pure, it has no edge to \(D_{1-i}\), so enlarging \(D_i\) does
not repair or otherwise alter the deficient pair.  An edge from \(q\) to
\(U\) becomes a \(K-U\) to \(D_i\cup U\) edge, preserving the required
gate--shore adjacency.  The opposite gate--shore adjacency is unchanged,
and the fixed protected core retains all contacts to \(C\) and the
\(Q_j\)'s.  These are all model adjacencies.  If (9.1) holds, \(q\) can
indeed be the sole new \(i\)-portal, which explains why this move was not
available inside an induction which insisted on two portals. \(\square\)

Consequently a branch-set-minimal cutvertex gate has no pure owner lobe.
The remaining cutvertex alternatives are: a **double-owner lobe**, in
which one mixed nonprotected lobe contains every portal to both deficient
shores while the protected side (including \(q\)) contains none; or a
cutvertex lying wholly inside the protected-core side, with no
nonprotected owner lobe left to absorb.  The move (9.2) does not touch
\(C\) or the edge \(56\), so all five side-labelled critical-edge
witnesses survive unchanged.  This distinction is important: pure owners
are artifacts of maintaining capacity two, whereas a double owner and an
internal protected-core cut are actual label-preserving obstructions.

### Lemma 9.2 (spanning singleton normalization and carrier load)

Assume the tracked gate is a singleton \(r\in\{e_6,e_0\}\), and write the
displayed model as

\[
             \{h\},\{1\},\{2\},\{r\},C,D_0,D_1,           \tag{9.3}
\]

with \(D_0D_1\) the deficient pair.  The model can be made spanning while
keeping the four singleton bags fixed.  In such a spanning normalization,

\[
                 |N_C(D_0)|\ge3,\qquad |N_C(D_1)|\ge3.     \tag{9.4}
\]

#### Proof

Let \(U\) be a component outside the seven displayed bags.  If \(U\)
meets both \(D_0,D_1\), absorbing \(U\) into either shore repairs the sole
missing adjacency and gives a \(K_7\)-model.  Thus this cannot occur.  If
\(U\) meets none of \(C,D_0,D_1\), its neighbourhood is contained in the
four singleton vertices, contradicting seven-connectivity.  Hence \(U\)
can be absorbed into \(C\), if it meets \(C\), and otherwise into its
unique shore.  Different outside components are anticomplete, so the
operation can be repeated.

Afterwards \(D_0,D_1\) are genuinely anticomplete and every neighbour of
\(D_i\) outside \(D_i\) lies in

\[
                         \{h,1,2,r\}\cup C.                \tag{9.5}
\]

The opposite shore is nonempty and lies outside \(N[D_i]\), so
\(N(D_i)\) is a separator.  Seven-connectivity and (9.5) give at least
three distinct neighbours in \(C\), proving (9.4). \(\square\)

Thus the singleton state is not a capacity-one quotient: the central
carrier has three portals to each deficient shore.  What remains difficult
is placement of those six portals relative to the three protected carrier
roles (the \(h\)-root, the vertex \(6\) supplying \(1,2\), and the
\(r\)-portal).

### Theorem 9.3 (anchored \(56\)-trace at an exterior singleton)

Let \(r\in\{e_6,e_0\}\).  There is a proper six-colouring \(c\) of
\(G-56\) such that, with

\[
                         \alpha=c(5)=c(6),\qquad
                         \beta=c(r),                        \tag{9.6}
\]

the \(\alpha/\beta\)-component contains all four vertices

\[
                              h,r,5,6.                      \tag{9.7}
\]

Equivalently, one member of the side-labelled split-cycle fan is aligned
with the actual colour of the singleton branch set \(r\).  The statement
uses contraction-criticality and is not a consequence of the static
near-\(K_7\) model.

#### Proof

Delete \(56\), and contract the connected star on
\(\{v,h,5,6\}\), with centre \(v\), to one vertex.  Its three leaves are
independent after the deletion: \(h5,h6\notin E(G)\), and \(56\) was
deleted.  Six-colour this proper minor and expand the leaves after deleting
the centre \(v\).  This gives a colouring of \(G-v-56\) in which

\[
                              c(h)=c(5)=c(6)=\alpha.         \tag{9.8}
\]

The neighbourhood \(N(v)=\{h,1,2,3,4,5,6\}\) now uses at most five
colours, so at least one colour is absent from it and can be assigned to
\(v\).  If \(\beta=c(r)\) is absent from \(N(v)\), choose \(c(v)=\beta\).
This is proper because \(r\notin N(v)\).  The edges

\[
                              rh,\quad hv,\quad v5,\quad v6 \tag{9.9}
\]

then put \(h,r,5,6\) in one \(\alpha/\beta\)-component.

Suppose instead that \(\beta\) occurs on \(N(v)\).  The root \(r\) is
adjacent to \(h,1,2\), so

\[
                   \beta\notin\{\alpha,c(1),c(2)\}.        \tag{9.10}
\]

Consequently \(\beta=c(x)\) for some \(x\in\{3,4\}\).  Assign any colour
absent from \(N(v)\) to \(v\).  The path

\[
                              r-h-x-5                       \tag{9.11}
\]

is an \(\alpha/\beta\)-path.  Finally, criticality of the deleted edge
\(56\) says that \(5,6\) lie in the same \(\alpha/\beta\)-component in
every six-colouring of \(G-56\).  Adjoining that bichromatic connector to
(9.11) proves (9.7). \(\square\)

Theorem 9.3 is the first genuine colour-to-model synchronization in the
dirty residue.  It does **not** by itself allocate a clean segment to one
of the deficient shores: the \(5\)-\(6\) connector may return through the
carrier and the literal vertices \(h,3,4,v\).  The remaining terminal
exchange is therefore exact:

* in the singleton state, convert the anchored component (9.7), together
  with the three-plus-three carrier portal load (9.4), into a mixed
  removable carrier piece; or
* in the cutvertex state, show that an anchored \(56\)-connector cannot
  coexist with one double-owner lobe.

Unlike an unlabelled Kempe-path assertion, either conclusion would now
produce the allocated split of Lemma 8.1 and hence an explicit
\(K_7\)-model.
