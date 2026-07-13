# Adversarial audit: complementary-lobe ownership

## Verdict

Theorems 3.1, 4.1, and 5.1 of
`hadwiger_degree9_complementary_lobe_ownership.md` are **GREEN** under
the balanced spanning-model hypotheses stated in Section 1.

The proposed outer-bag discussion in Section 7 is valid only after one
qualification to the optimization and remains a conditional lock, not an
elimination.  Corollary 6.1 is valid, but the block-cut-tree sentence that
follows it is not literally equivalent to the corollary.

## 1. Lexicographic exchange audit

Let

\[
  P_6=N_{R_0}(L_6),\quad P_0=N_{R_0}(L_0),\quad
  P_5=N_{R_0}(R_5).
\]

All three sets are nonempty because the four old bags form a rooted
\(K_4\)-model.  For a connected adjacent split
\(R_0=X\mathbin{\dot\cup}Y\) with the unique root of \(R_0\) in
\(Y\), the set \(X\) contains no model root and neither outer vertex
\(5,6\).  Hence every exchange used in Theorem 3.1 preserves:

* the four prescribed roots and their left/right types;
* \(6\in L_6\) and \(5\in R_5\);
* spanning and pairwise disjointness;
* all old clique adjacencies, by Lemma 2.1.

If \(X\) is moved into \(L_6\) or \(R_5\), the primary potential
\(|L_0|+|R_0|\) decreases by \(|X|\).  If it is moved into \(L_0\),
the primary potential is unchanged and the secondary potential
\(|R_0|\) decreases by \(|X|\).  Thus Theorem 3.1's ownership
conclusion follows from the stated global minimum; it does not silently
optimize inside the complementary cell.

## 2. Theorem 4.1: complete branch-set audit

Write

\[
 A=K,\quad B=D\cup R_5,\quad C=L_0\cup X,
 \quad E=\{v,3\}\cup Y.
\]

The seven bags are \(\{h\},\{1\},\{2\},A,B,C,E\).  They are
pairwise disjoint because \(K,D,L_0,R_5,R_0\) are disjoint old model
parts, \(X,Y\) partition \(R_0\), and none of the old bags contains
\(v,h,1,2,3,4\).

Connectivity is witnessed by:

* \(B\): the Moser edge \(56\), with \(6\in D\) and \(5\in R_5\);
* \(C\): the assumed \(X\)-\(L_0\) contact;
* \(E\): the path \(v-3-r_0\), where the right root \(r_0\in Y\).

The six adjacencies among \(A,B,C,E\) are, respectively,

\[
 AB:KD,\quad AC:KX,\quad AE:KY,\quad
 BC:R_5L_0,\quad BE:v6,\quad CE:XY.
\]

Their contacts with the three singleton bags are:

\[
\begin{array}{c|ccc}
 &h&1&2\\ \hline
A&he_6&1e_6&2e_6\\
B&hr_5&16&26\\
C&hr_0'&1r_0'&2r_0'\\
E&hr_0&v1&v2
\end{array}
\]

where \(e_6\) is the left root of \(K\), \(r_5\) is the right root
of \(R_5\), \(r_0'\) is the left root of \(L_0\), and \(r_0\) is
the right root of \(R_0\).  Finally \(h1,h2,12\) are Moser edges.
This accounts for all 21 required adjacencies.  No unproved cross-bag
contact is used.

## 3. Theorem 5.1: bipartition and ownership audit

The connected bipartition invoked in Theorem 5.1 exists.  A precise
argument is: choose two distinct vertices of
\(A=N_{R_0}(K)\), take a spanning tree of \(R_0\), and choose an edge
on the tree path between them so that one resulting component contains
the prescribed root together with at least one member of \(A\), while
the other contains another member of \(A\).  If the prescribed root is
itself in \(A\), choose any other member of \(A\) and an edge on their
path.  The two tree components give connected adjacent vertex sets
\(X,Y\), with the root in \(Y\) and both sides meeting \(A\).

Applying Theorem 3.1 with class \(P_6\) makes \(X\) own \(P_0\) or
\(P_5\).  In the latter case, applying it with class \(P_5\) makes
\(X\) own \(P_6\) or \(P_0\).  Since \(Y\cap A\ne\varnothing\) and
\(A\subseteq P_6\), ownership of all of \(P_6\) is impossible.
Therefore \(P_0\subseteq X\), and Theorem 4.1 applies.  The conclusion
\(|N_{R_0}(K)|\leq1\) is sound and does not assume any bound on
\(|R_0|\) or any block structure.

## 4. Corollary 6.1: valid conclusion, inaccurate equivalence

Corollary 6.1 itself is GREEN.  If two root-free components of
\(R_0-q\) met \(A\), their disjointness and the nonemptiness of
\(P_0,P_5\) force one to own \(P_0\); using it as \(X\), the
complement is connected, contains the root, and meets \(A\) through
the other component, so Theorem 4.1 applies.

However, this is not literally equivalent to saying that the minimal
subtree of the block-cut tree joining the root to all portals is a
path.  Such a subtree may branch at a **block node** rather than at a
cutvertex node; Corollary 6.1 only rules out two portal-bearing
root-free components after deletion of one cutvertex.  This sentence
should be weakened or deleted.  It does not affect Theorem 5.1, which
already gives the stronger vertex-cardinality conclusion.

## 5. Section 7: what is valid and what is not yet proved

For a split

\[
 R_5=X\mathbin{\dot\cup}Y,qquad \{5,r_5\}\subseteq Y,
 \qquad X\sim K,\;Y\sim K,
\]

the exchange \(X:R_5\to L_6\) preserves the primary and secondary
potentials and decreases \(|R_5|\).  Therefore its failure forces
\(X\) to own all \(R_5L_0\)-contacts or all \(R_5R_0\)-contacts,
**provided that \(|R_5|\) was chosen as a third, global
lexicographic potential over all balanced spanning models**.

It is not legitimate to minimize \(|R_5|\) only among models satisfying
the current condition \(K\not\sim R_0\): after moving \(X\) into
\(L_6\), the new root component can acquire an \(R_0\)-contact and
leave that restricted family.  Section 7 should therefore replace
"in the subcase ... choose additionally" by a global three-level
optimization from the outset, followed by the conditional analysis of
whichever attachment cell the selected model occupies.

Under that correction, the displayed model (7.2) is GREEN.  The set
\(D\cup R_0\) is connected because the old \(L_6R_0\) edge has its
\(L_6\)-endpoint in \(D\) when \(K\not\sim R_0\).  With

\[
 A=K,\quad B=D\cup R_0,\quad C=L_0\cup X,
 \quad E=\{v,3\}\cup Y,
\]

the six mutual contacts are

\[
 KD,\quad KX,\quad KY,\quad R_0L_0,\quad v6,\quad XY,
\]

and the same root/outer-vertex witnesses as in Section 2 give all
contacts to \(\{h\},\{1\},\{2\}\).  Thus ownership of the
\(R_5L_0\)-class indeed yields \(K_7\).

What remains is only a conditional ownership statement.  The note does
not prove that a root-and-5-preserving connected bipartition with
\(K\)-portals on both sides exists.  Multiple portals can all lie on a
mandatory path between \(r_5\) and \(5\), in which case keeping both
terminals in one connected side may leave no detachable portal side.
Nor does Section 7 eliminate the case with the unique possible
\(R_0\)-portal.  Consequently its final bullet list accurately
describes a residual ordered lock only if it is read conditionally; it
is not yet an outer-ownership theorem or a generic separator argument.

## 6. Re-audit of revised Sections 7--9

### 6.1 Global tertiary potential and Theorem 7.1

The revised protected-ownership theorem is GREEN, with the same ordering
qualification already recorded above: the model must be chosen globally
lexicographically by

\[
 (|L_0|+|R_0|,\ |R_0|,\ |R_5|)
\]

over the entire family of balanced spanning rooted models, and only then
may one condition on the selected model lying in the complementary cell.
For a split satisfying (7.2), moving \(X:R_5\to L_6\) preserves the
first two coordinates and strictly decreases the third.  The move is
label-preserving because \(r_5,5\in Y\), \(6\in L_6\), and
\(X\sim K\subseteq L_6\).  If \(Y\) retains both the \(L_0\)- and
\(R_0\)-contacts, Lemma 2.1 applies.  Hence failure forces exactly the
ownership alternative in (7.3).

The opening of the note should ideally state the full three-coordinate
global choice before (1.1), or say explicitly: choose the global
lexicographic minimizer and assume that this selected minimizer lies in
the complementary cell.  This is a quantifier/ordering clarification,
not a branch-set defect.

### 6.2 Both models in Theorem 7.2

The case \(K\not\sim R_0\) was audited above.  In the new case
\(K\sim R_0\), put

\[
 A=K,\quad B=L_0\cup X,\quad C=D\cup Y,
 \quad E=\{v,3\}\cup R_0.
\]

The four sets are connected: \(B\) uses the assumed \(X L_0\)
contact, \(C\) uses \(65\), and \(E\) uses the right-root--\(3\)--\(v\)
path.  Their six mutual contacts are

\[
 AB:KX,\quad AC:KD,\quad AE:KR_0,\quad
 BC:XY,\quad BE:L_0R_0,\quad CE:v6.
\]

They see \(h,1,2\), respectively, through: the left root in \(K\);
the left root in \(L_0\); the right root in \(Y\) together with the
vertex \(6\); and the right root in \(R_0\) together with \(v\).
The old bags and displayed literal vertices are disjoint.  Thus all 21
adjacencies in (7.6) are present.  In particular, the unique possible
\(R_0\)-portal creates the contact \(KR_0\) needed by the alternate
certificate rather than an exception.

Corollary 7.3 consequently follows: in a minor-free graph, a protected
split with \(K\)-portals on both sides must own all of \(Q_R\) on
the detachable side and cannot own all of \(Q_0\) there.

### 6.3 Theorem 8.1 and connectedness of the complement

The complement-connected claim is GREEN.  If \(U\) is a component of
\(R_5-V(Q)\), then every other component of \(R_5-V(Q)\) has an edge
to \(Q\): otherwise it would be a component of the connected graph
\(R_5\).  Therefore

\[
 R_5-U=Q\ \cup\!\bigcup_{U'\ne U}U'
\]

is connected.  It contains \(r_5,5,Q_R\), and \(U\) is connected and
adjacent to it.  If both sides met \(K\), Corollary 7.3 would put
\(Q_R\subseteq U\), whereas (8.1) puts the nonempty set
\(Q_R\subseteq Q\subseteq R_5-U\), a contradiction.  This proves both
the at-most-one-component assertion and the stronger assertion when the
core itself meets \(K\).

Here \(R_5-Q\) should be read as deletion of \(V(Q)\); spelling this out
would remove a minor notational ambiguity.  No ambient separator follows,
and Section 8 correctly declines to claim one.

### 6.4 Theorem 9.1 and the tie-break issue

The bifurcation and its counts are GREEN.

* If \(K_5\sim R_0\), the symmetric cross-half classification forces
  \(K_5\not\sim L_6,L_0\).  Its only portal bag is then \(R_0\), and
  strict surplus gives at least four distinct portals there.  The
  symmetric root-trap/ordered-spine theorem requires only global
  minimality of the primary potential \(|L_0|+|R_0|\), which the
  three-level minimizer has.
* If \(K_5\not\sim R_0\), the symmetric complementary cell has its
  portal set in \(L_6\cup L_0\).  The symmetric form of Theorem 5.1
  gives \(|N_{L_0}(K_5)|\le1\), and strict surplus then gives at least
  three portals in \(L_6\).

The note's tie-break explanation is correct.  Although the full
three-class Theorem 3.1 uses the secondary coordinate when a piece is
moved from \(R_0\) to \(L_0\), Theorem 5.1 itself invokes ownership
only with target classes \(L_6\) and \(R_5\).  Both moves strictly
decrease \(|L_0|+|R_0|\).  After left--right interchange, the two
targets are \(R_5\) and \(L_6\), and again both moves strictly decrease
the same primary sum.  Thus the symmetric application does **not** need
to minimize \(|L_0|\), and there is no conflict with the chosen
\(|R_0|\) secondary tie-break.

The last four-item description remains a description of the exact
residual lock, not its elimination.  Item 4 should be read as quantifying
only over connected/co-connected detachable splits for which the
root--5 side remains connected; arbitrary set partitions of the attached
component are not covered by Corollary 7.3.

## 7. Re-audit of complete protected-core capture

The strengthened Lemma 8.1 and Theorem 8.2 are **GREEN**, with one
minor citation/count correction.

### 7.1 Contracted-core spanning-tree split

Contracting the connected vertex set \(V(Q)\) to a root \(z\) is
legitimate.  In a spanning tree rooted at \(z\), two distinct marks,
not both represented by \(z\), can always be separated by deleting one
tree edge while leaving \(z\) on the retained side:

* if one mark is an ancestor of the other, delete the first edge after
  the ancestor on their tree path;
* otherwise delete the first edge toward either mark after the two root
  paths diverge.

The detached descendant subtree contains exactly the selected mark, and
the root component contains the other.  On undoing the contraction,
replace \(z\) by the connected subgraph \(Q\).  Every tree edge incident
with \(z\) restores to an edge incident with a vertex of \(Q\), so the
root side remains connected.  The deleted tree edge witnesses adjacency
of the two sides.  Extra non-tree edges do not hurt.  This proves the
claimed connected adjacent bipartition, including the case in which one
mark lies in \(Q\).

### 7.2 Portal capture

Given \(a\in A-Q\) and a second portal \(b\in A-\{a\}\), Lemma 8.1
produces a protected split whose two sides both meet \(K\).  Corollary
7.3 then puts \(Q_R\) in the detached side \(X\), while by construction
the nonempty old contact class \(Q_R\) lies in
\(Q\subseteq Y\).  This contradiction proves
\(N_{R_5}(K)\subseteq Q\) for every connected \(Z\)-hull.

The line "Corollary 5.2 gives \(|A|\ge3\)" is not valid if Theorem 8.2
is meant to include the exact-seven-cut case, because Corollary 5.2
explicitly excludes that case.  No restriction is needed: the universal
portal bound gives

\[
 |N_{R_5\cup R_0}(K)|\ge3,
\]

and Theorem 5.1 gives \(|N_{R_0}(K)|\le1\), hence \(|A|\ge2\).
That is exactly enough to choose \(b\).  Replace the cited sentence by
this two-line argument.  Alternatively, adding the strict-surplus
hypothesis would validate \(|A|\ge3\), but would unnecessarily weaken
Theorem 8.2.

### 7.3 Universal hull and cutvertex consequences

The universal-hull conclusion is sound.  If a nonterminal portal
\(a\notin Z\) failed to separate members of \(Z\), then all of \(Z\)
would lie in one component of \(R_5-a\).  That component itself is a
connected \(Z\)-hull avoiding \(a\), contradicting Theorem 8.2.
Therefore at least two components of \(R_5-a\) contain terminals from
\(Z\); in particular, \(a\) is a cutvertex and its cutvertex node lies
on the block-cut Steiner subtree joining \(Z\).

This does not say that the Steiner subtree is a path when \(|Z|>2\),
and the revised text correctly calls it a Steiner-tree state rather than
an ordered path in general.
