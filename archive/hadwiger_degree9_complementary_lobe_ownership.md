# Complementary attachment: residual-adjacency exchange and portal ownership

## 1. Setup and optimization

Use the balanced spanning rooted model

\[
                 L_6,L_0,R_5,R_0
\]

from `hadwiger_degree9_hub_portal_lock.md`.  Thus \(6\in L_6\),
\(5\in R_5\), the roots of \(L_6,L_0\) see \(h,1,2\), and the roots
of \(R_5,R_0\) see \(h,3,4\).  Let \(K\) be the root component of
\(L_6-6\), and let \(D=L_6-K\).  The complementary attachment cell is

\[
 K\not\sim L_0,qquad
 N(K)-\{h,1,2,6\}\subseteq R_5\cup R_0.            \tag{1.1}
\]

Choose the balanced spanning model first to minimize

\[
                         |L_0|+|R_0|,               \tag{1.2}
\]

among minimizers of (1.2), minimize \(|R_0|\), and among those minimize
\(|R_5|\).  Thus the full potential is the globally chosen lexicographic
triple

\[
                 (|L_0|+|R_0|, |R_0|, |R_5|).       \tag{1.3}
\]

This optimization is over all balanced spanning models with the four
prescribed exterior roots and with \(5,6\) in their indicated bags; only
after choosing the global minimizer do we assume it lies in the
complementary cell (1.1).  Every exchange below stays in this admissible
family of balanced spanning models.

## 2. The correct lobe exchange

The anticompleteness hypothesis in the basic root-free lobe exchange is
sufficient but stronger than necessary.

### Lemma 2.1 (residual-adjacency exchange)

Let \((B_1,\ldots,B_m)\) be a rooted clique model.  Suppose

\[
 B_i=X\mathbin{\dot\cup}Y
\]

is a partition into nonempty connected adjacent sets, with the root of
\(B_i\) in \(Y\).  Fix \(j\ne i\).  If

1. \(X\sim B_j\); and
2. \(Y\sim B_\ell\) for every \(\ell\notin\{i,j\}\),

then replacing

\[
 B_i\longmapsto Y,qquad B_j\longmapsto B_j\cup X       \tag{2.1}
\]

gives another rooted clique model with the same roots and the same union.

#### Proof

Both new bags are connected, and they are adjacent through the
\(X\)-\(Y\) edge.  The residue \(Y\) retains every old adjacency from
\(B_i\) except possibly the one to \(B_j\), which has just been supplied
by \(X\)-\(Y\).  Enlarging \(B_j\) cannot destroy any adjacency.  The
root of \(B_i\) remains in \(Y\), and no other root lies in \(X\).
All other bags are unchanged. \(\square\)

Notice that \(X\) may have arbitrarily many contacts to the other bags.
Only the contacts retained by \(Y\) matter.

## 3. Three-class ownership inside the ordinary right bag

Put \(T=R_0\), and let \(r\) be its prescribed root.  Define the three
nonempty contact classes

\[
 P_6=N_T(L_6),\qquad P_0=N_T(L_0),\qquad P_5=N_T(R_5). \tag{3.1}
\]

### Theorem 3.1 (three-class ownership)

Let \(T=X\dot\cup Y\) be a connected adjacent bipartition with
\(r\in Y\).  If \(X\cap P_i\ne\varnothing\) for
\(i\in\{6,0,5\}\), then

\[
                 P_j\subseteq X
        \quad\text{for some }j\in\{6,0,5\}-\{i\}.  \tag{3.2}
\]

#### Proof

Suppose instead that \(Y\) meets both of the other contact classes.
Apply Lemma 2.1, moving \(X\) from \(R_0\) into the bag indexed by
\(i\).

If \(i=6\) or \(i=5\), the move decreases (1.2) by \(|X|\).  If
\(i=0\), it preserves (1.2) but decreases the secondary potential
\(|R_0|\) by \(|X|\).  Roots, outer vertices, types and spanning are
unchanged.  Each case contradicts the chosen global minimum. \(\square\)

For the actual \(K\)-portals put

\[
                         A=N_T(K)\subseteq P_6.       \tag{3.3}
\]

Theorem 3.1 gives the sharper statement

\[
 X\cap A\ne\varnothing
       \quad\Longrightarrow\quad
 P_0\subseteq X\text{ or }P_5\subseteq X.            \tag{3.4}
\]

Thus every detachable root-free \(K\)-piece owns an entire old bag
adjacency.  Merely touching two bags is not the obstruction; ownership of
all contacts to one bag is.

## 4. A new explicit two-sided portal model

The ownership law becomes decisive because two \(K\)-carrying sides
cannot coexist when one owns the \(L_0\)-contact.

### Theorem 4.1 (ordinary-right two-sided closure)

Suppose

\[
                         R_0=X\mathbin{\dot\cup}Y       \tag{4.1}
\]

is a partition into connected adjacent sets, the root of \(R_0\) lies
in \(Y\), and

\[
             X\sim K,\qquad X\sim L_0,\qquad Y\sim K. \tag{4.2}
\]

Then \(G\) contains a \(K_7\)-minor.

#### Proof

Use the seven branch sets

\[
 \{h\},\quad \{1\},\quad \{2\},\quad K,\quad
 D\cup R_5,\quad L_0\cup X,\quad \{v,3\}\cup Y.    \tag{4.3}
\]

They are disjoint.  Their connectivity follows from, respectively,
the edge \(56\) between \(D\) and \(R_5\), the \(X\)-\(L_0\)
contact, and the path from the right root in \(Y\) through \(3\) to
\(v\).

The last four sets form a clique.  The six required contacts are

\[
 KD,quad KX,quad KY,quad R_5L_0,quad v6,quad XY. \tag{4.4}
\]

They also all see each of \(h,1,2\): use the root of \(K\), the root
of \(R_5\) together with the vertex \(6\), the root of \(L_0\), and
the vertex \(v\), respectively.  Finally \(h12\) is a triangle.
Thus (4.3) is a \(K_7\)-model. \(\square\)

Every overlap has been accounted for: \(K,D,L_0,R_5,X,Y\) lie in
distinct parts of the spanning rooted model, and none contains
\(v,h,1,2,3\).

## 5. Complete elimination of ordinary-bag portal multiplicity

### Theorem 5.1 (at most one \(R_0\)-portal from \(K\))

In the globally optimized model, if \(G\) has no \(K_7\)-minor, then

\[
                              |N_{R_0}(K)|\le1.       \tag{5.1}
\]

#### Proof

Suppose \(A=N_{R_0}(K)\) contains two distinct vertices.  In any
connected graph with a distinguished root and two marked vertices there
is a connected adjacent bipartition

\[
                         T=X\dot\cup Y               \tag{5.2}
\]

with the root in \(Y\) and with both \(X\cap A\) and \(Y\cap A\)
nonempty.  For completeness, take a spanning tree of \(T\), root it at
\(r\), take the minimal subtree containing \(r\cup A\), and delete an
edge of that subtree which has marked vertices on both sides.  The two
tree components, with all remaining tree branches retained on their
respective sides, give (5.2).

Apply Theorem 3.1 to \(X\), first with contact class \(P_6\).  Either

\[
                         P_0\subseteq X              \tag{5.3}
\]

or \(P_5\subseteq X\).  In the second case apply Theorem 3.1 again,
now with contact class \(P_5\).  It gives

\[
                         P_6\subseteq X
       \quad\text{or}\quad P_0\subseteq X.           \tag{5.4}
\]

But \(Y\cap A\ne\varnothing\) and \(A\subseteq P_6\), so the first
alternative in (5.4) is impossible.  Hence (5.3) holds in every case.
Therefore \(X\sim L_0\), while both sides meet \(K\).  Theorem 4.1
gives a \(K_7\)-minor, a contradiction. \(\square\)

This is an infinite-family elimination: no assumption on \(|R_0|\),
its block structure, or the placement of its old model contacts is used.
Although Theorem 3.1 used the \(|R_0|\) tie-break for its \(i=0\)
direction, the proof of Theorem 5.1 uses only \(i=6\) and \(i=5\).
Both corresponding exchanges move vertices from an ordinary bag into an
outer bag and strictly decrease the symmetric primary potential
\(|L_0|+|R_0|\).  Consequently Theorem 5.1 and its left--right image do
not depend on choosing opposite secondary tie-breaks.

### Corollary 5.2 (the complementary surplus is outer)

Outside the exact seven-cut outcome, Theorem 3.1 of
`hadwiger_degree9_cross_half_gate.md` gives at least four distinct
portals in \(R_5\cup R_0\).  Theorem 5.1 therefore forces

\[
                         |N_{R_5}(K)|\ge3.            \tag{5.5}
\]

Thus the complementary cell is no longer a two-bag portal-distribution
problem.  All but at most one protected portal lie in the outer bag
\(R_5\).

## 6. Block-spine formulation

The proof also yields a useful local form before taking the cardinality
conclusion.

### Corollary 6.1 (no branching \(K\)-portal block tree in \(R_0\))

For every \(q\in R_0\), at most one component of \(R_0-q\) not
containing the prescribed root can meet \(A=N_{R_0}(K)\).

#### Proof

If two such components \(U,V\) existed, apply (3.4) to each, using the
partition \(U\mid(R_0-U)\) and similarly for \(V\).  Since \(U,V\)
are disjoint and \(P_0,P_5\) are nonempty, one of them, say \(U\),
contains all of \(P_0\), while the complement contains the other
\(K\)-portal component \(V\).  Theorem 4.1 applies with
\(X=U\), \(Y=R_0-U\). \(\square\)

This forbids branching at a cutvertex.  It does not assert that the
Steiner subtree in the block-cut tree is a path: several portal-bearing
directions can still meet in one block node.  The stronger cardinality
theorem bypasses that distinction and leaves at most one portal vertex
in \(R_0\) altogether.

## 7. Root--5 protected ownership in the outer bag

The argument does not immediately eliminate the at least three portals
now forced inside \(R_5\): both the vertex \(5\) and the prescribed
right root must stay in that bag during a balanced exchange.  Nevertheless
the residual-adjacency principle gives an exact protected ownership
theorem.

Use the third global coordinate in (1.3).  Put \(T=R_5\), let \(r_5\)
be its prescribed root, and set

\[
 Q_6=N_T(L_6),\qquad Q_0=N_T(L_0),\qquad Q_R=N_T(R_0). \tag{7.1}
\]

All three sets are nonempty, because the four original bags form a
clique model.

### Theorem 7.1 (root--5 protected ownership)

Suppose

\[
 T=X\mathbin{\dot\cup}Y,\qquad G[X],G[Y]\text{ connected},\qquad
 \{r_5,5\}\subseteq Y,\qquad X\sim K.               \tag{7.2}
\]

Then

\[
                         Q_0\subseteq X
             \quad\text{or}\quad Q_R\subseteq X.    \tag{7.3}
\]

#### Proof

If \(Y\) retained a contact to both \(L_0\) and \(R_0\), Lemma 2.1
would move \(X\) from \(R_5\) into \(L_6\).  The primary potential
and \(|R_0|\) would be unchanged, while \(|R_5|\) would decrease.
The root and \(5\) remain in \(Y\), and \(6\) remains in \(L_6\), so
the new model belongs to the optimized family.  This is impossible.
\(\square\)

The possible unique portal in \(R_0\) from Theorem 5.1 does not create
an exception to the positive branch-set certificate.

### Theorem 7.2 (outer two-sided closure, including \(K\sim R_0\))

In addition to (7.2), suppose \(Y\sim K\) and \(X\sim L_0\).  Then
\(G\) contains a \(K_7\)-minor.

#### Proof

If \(K\not\sim R_0\), use

\[
 \{h\},\{1\},\{2\},K,
 D\cup R_0, L_0\cup X, \{v,3\}\cup Y.             \tag{7.4}
\]

The set \(D\cup R_0\) is connected because the old \(L_6R_0\)
edge has its \(L_6\)-endpoint in \(D\).  The last four bags form a
clique through

\[
 KD,\quad KX,\quad KY,\quad R_0L_0,\quad v6,\quad XY. \tag{7.5}
\]

If \(K\sim R_0\), use instead

\[
 \{h\},\{1\},\{2\},K,
 L_0\cup X, D\cup Y, \{v,3\}\cup R_0.             \tag{7.6}
\]

Here \(D\cup Y\) is connected through \(65\), and the last bag is
connected through the right root--\(3\)--\(v\) path.  The six
contacts among the last four bags are

\[
 KX,\quad KD,\quad K R_0,\quad XY,\quad L_0R_0,
 \quad v6.                                           \tag{7.7}
\]

In both models the four large bags see \(h,1,2\), respectively through
the left root, the left root, the vertex \(6\) plus a right root, and
the vertex \(v\).  The three singleton bags induce the triangle
\(h12\).  Disjointness follows from the spanning four-bag partition.
Thus (7.4) or (7.6) is a \(K_7\)-model. \(\square\)

### Corollary 7.3 (exact crossed ownership)

Assume there is no \(K_7\)-minor and, in (7.2), \(Y\sim K\).  Then

\[
                  Q_R\subseteq X,\qquad Q_0\nsubseteq X.    \tag{7.8}
\]

Thus every protected split with \(K\)-portals on both sides has one
fixed orientation: the detachable side owns every \(R_0\)-contact,
while the root--5 side retains an \(L_0\)-contact.

#### Proof

Theorem 7.1 gives one of the two ownership alternatives.  Ownership of
\(Q_0\) invokes Theorem 7.2, including when the unique possible
\(K\)-portal in \(R_0\) is present.  Hence only \(Q_R\subseteq X\)
survives.  If also \(Q_0\subseteq X\), Theorem 7.2 again applies.
\(\square\)

## 8. Concentration in a protected core

The crossed orientation converts immediately into an unbounded-order
structural theorem.

### Lemma 8.1 (a connected core separates any two outside marks)

Let \(T\) be connected, let \(Q\subseteq T\) be connected, and let
\(a,b\in V(T)\) be distinct with at least one of them outside \(Q\).
There is a connected adjacent bipartition \(T=X\dot\cup Y\) such that

\[
             Q\subseteq Y,qquad
             |\{a,b\}\cap X|=|\{a,b\}\cap Y|=1.     \tag{8.1}
\]

#### Proof

Contract \(Q\) to a root \(z\), take a spanning tree, and root it at
\(z\).  If one of \(a,b\) is an ancestor of the other, delete an edge
of their tree path immediately below the ancestor.  Otherwise delete
the first edge on the root-to-one-mark branch after the two root paths
diverge.  The two tree components contain the two marks separately and
put \(z\) on the \(Y\)-side.  Undoing the contraction gives the desired
partition. \(\square\)

### Theorem 8.2 (complete protected-core capture)

Let \(Q\subseteq R_5\) be **any** connected subgraph containing

\[
                  Z=\{r_5,5\}\cup Q_R.                      \tag{8.2}
\]

If \(G\) has no \(K_7\)-minor, then

\[
                         N_{R_5}(K)\subseteq Q.              \tag{8.3}
\]

#### Proof

Put \(A=N_{R_5}(K)\).  The universal portal bound gives at least three
portals in \(R_5\cup R_0\), while Theorem 5.1 leaves at most one in
\(R_0\); hence \(|A|\ge2\).  If
\(a\in A-Q\), choose any \(b\in A-\{a\}\) and apply Lemma 8.1.
Both sides of the resulting partition meet \(A\), while the root and
\(5\) lie in \(Y\).  Corollary 7.3 therefore gives
\(Q_R\subseteq X\).  But \(Q_R\subseteq Q\subseteq Y\), a
contradiction.  Hence no such \(a\) exists. \(\square\)

Theorem 8.2 holds for every connected \(Z\)-hull, not merely a selected
minimal one.  Consequently every \(K\)-portal in \(R_5\) is an
unavoidable vertex of the connected Steiner hull of
\(Z=\{r_5,5\}\cup Q_R\).  In particular, a portal outside \(Z\) is
a cutvertex of \(R_5\): deleting it disconnects two members of \(Z\),
for otherwise \(R_5-a\) would contain a connected \(Z\)-hull avoiding
it.  In the block-cut tree, all nonterminal \(K\)-portals therefore lie
on the Steiner subtree joining the protected terminal set \(Z\).

This is a literal ordered-spine theorem when the protected terminal set
has two elements, and a Steiner-tree version for the actual set \(Z\).
There is no branching family of dirty helper lobes outside that tree.

This is the strongest conclusion available from model exchange alone.
The protected terminal set and its hull may still be large because the
contact class \(Q_R\) need not be small.  Consequently neither an
internal one-vertex bottleneck nor a separator of order at most six in
the ambient graph follows from Theorem 8.1.  Claiming such a separator
would silently replace a set of portal vertices by one contracted bag
label.

## 9. Symmetric-gate interaction and exact remaining lock

Let \(K_5\) be the component of \(R_5-5\) containing the prescribed
right root.  The symmetric cross-half classification gives

\[
 K_5\not\sim R_0
 \quad\text{or}\quad
 K_5\not\sim L_6,L_0.                                  \tag{9.1}
\]

Hence:

* if \(K_5\sim R_0\), then every \(K\)-portal in \(R_5\) lies outside
  \(K_5\), because the second alternative of (9.1) makes \(K_5\)
  anticomplete to \(L_6\);
* if \(K_5\not\sim R_0\), then every \(R_5R_0\)-portal lies on the
  \(5\)-side of the symmetric gate.

Outside the symmetric exact-seven-cut outcome, the preceding results give
the following sharper bifurcation.

### Theorem 9.1 (opposite-gate bifurcation)

At least one of the following holds.

1. \(K_5\sim R_0\).  Then \(K_5\not\sim L_6,L_0\), it has at least
   four distinct portals in \(R_0\), and the symmetric form of the
   minimal-model root-trap theorem in
   `hadwiger_rooted_clique_lobe_exchange.md` confines those portals to
   its exceptional root-bearing ordered-spine state in \(R_0\).
2. \(K_5\not\sim R_0\).  Then, in the strict-surplus state,

   \[
          |N_{L_0}(K_5)|\le1,\qquad
          |N_{L_6}(K_5)|\ge3.                       \tag{9.2}
   \]

#### Proof

If \(K_5\sim R_0\), (9.1) forces
\(K_5\not\sim L_6,L_0\).  The symmetric cross-half theorem puts every
portal in \(R_0\), and strict surplus gives at least four.  This is the
symmetric same-bag cell, so the globally minimized rooted-model lobe
exchange gives the stated root trap and spine.

If \(K_5\not\sim R_0\), this is the symmetric complementary cell.  Apply
Theorem 5.1 after interchanging left and right: the ordinary target bag is
now \(L_0\), so it contains at most one \(K_5\)-portal.  The symmetric
strict-surplus bound supplies at least four portals altogether in
\(L_6\cup L_0\), proving (9.2).  This symmetric application uses only
the primary potential, as recorded after Theorem 5.1; it does not require
a contradictory \(|L_0|\) tie-break. \(\square\)

Thus the protected outer core is coupled to one of two independently
rigid objects: a four-portal ordered spine in \(R_0\), or at least three
opposite-gate portals back into \(L_6\).  The second outcome is exactly
the label-preserving opposite-bypass cell; the first is the remaining
double-spine cell.

These facts align the protected core in Theorem 8.1 with the symmetric
outer gate, but do not yet split it.  The exact surviving cell is now:

1. at most one \(K\)-portal in \(R_0\);
2. at least three \(K\)-portals in \(R_5\);
3. every one of those portals belongs to every connected hull of the
   root, \(5\), and the \(R_5R_0\)-portal set; and
4. every nonterminal portal is a cutvertex on the corresponding
   block-cut Steiner tree.

Thus the general connected/co-connected exchange eliminates the ordinary
bag and all branching outer lobes.  What remains is one protected
two-terminal core with a fixed crossed state.  Closing it requires an
exchange using the symmetric \(K_5\)-gate or a minor-critical colouring
transition; no generic small-separator conclusion is justified by the
current hypotheses.
