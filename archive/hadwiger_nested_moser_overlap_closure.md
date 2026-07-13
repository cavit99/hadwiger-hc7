# Nested-frame overlap closes the three-shore Moser descent

## 1. The reusable overlap lifts

The following two elementary lemmas are the reason a nested exact cut
does not create another three-shore recursion.  A connected set is **full**
to a vertex set if every vertex of that set has a neighbour in it.

### Lemma 1.1 (five-root overlap lift)

Let \(S,T\subseteq V(G)\) have order seven and

\[
 |S\cap T|=5.
\]

Put \(R=S\cap T\), \(S-R=\{u,v\}\).  Suppose there are four pairwise
disjoint connected sets \(A_1,A_2,C_1,C_2\), disjoint from \(S\cup T\),
such that

* \(A_1,A_2\) are full to \(S\); and
* \(C_1,C_2\) are full to \(T\).

If \(G[T]\) is a pure Moser spindle, then \(G\) has a \(K_7\)-minor.

#### Proof

We first record a five-root property of the Moser spindle.  For every
five-element set \(R\) of its vertices, it has a \(K_3\)-model

\[
 L_1,L_2,L_3
\tag{1.1}
\]

such that \(|L_i\cap R|=1\) for \(i=1,2,3\), and whose union avoids
the other two vertices of \(R\).  If the
subgraph induced by \(R\) contains a triangle, use its singleton
vertices.  Otherwise, in the standard labelling

\[
 E(M)=\{01,02,03,04,12,16,26,34,35,45,56\},
\tag{1.2}
\]

the only possibilities, together with suitable bags, are

\[
\begin{array}{c|c|c}
R&V(M)-R&(L_1,L_2,L_3)\\ \hline
\{0,1,3,5,6\}&\{2,4\}&(\{0,2,4\},\{5\},\{6\})\\
\{0,1,4,5,6\}&\{2,3\}&(\{0,2,3\},\{5\},\{6\})\\
\{0,2,3,5,6\}&\{1,4\}&(\{0,1,4\},\{5\},\{6\})\\
\{0,2,4,5,6\}&\{1,3\}&(\{0,1,3\},\{5\},\{6\}).
\end{array}
\tag{1.3}
\]

These are exactly the five-subsets hitting each of the four triangles
\(012,034,126,345\).  Each first bag in (1.3) is connected, sees both
singleton bags, and \(56\) is an edge.  This proves (1.1).

Let \(r_1,r_2,r_3\in R\) be the unique roots of \(R\) contained
respectively in the bags
in (1.1), and let \(R-\{r_1,r_2,r_3\}=\{r_4,r_5\}\).  The following
seven sets are branch sets:

\[
 A_1\cup\{u\},\quad A_2\cup\{v\},\quad
 C_1\cup\{r_4\},\quad C_2\cup\{r_5\},\quad
 L_1,L_2,L_3.                                    \tag{1.4}
\]

They are pairwise disjoint and connected.  Either of the first two sets
is adjacent to every other set through the old root of that set, because
\(A_1,A_2\) are full to \(S\).  Either of the next two is adjacent to
every \(L_i\) and to the other one through its root in \(T\), because
\(C_1,C_2\) are full to \(T\).  Its adjacency to the first two sets is
already supplied from the old-shore side.  Finally the three \(L_i\)
are pairwise adjacent by (1.1).  Thus (1.4) is a \(K_7\)-model. \(\square\)

### Lemma 1.2 (matched one-root overlap lift)

Let \(|S|=|T|=7\), \(S\cap T=\{s\}\), and write

\[
 S-\{s\}=\{x_1,\ldots,x_6\},\qquad
 T-\{s\}=\{y_1,\ldots,y_6\}.
\]

Assume \(x_i y_i\in E(G)\) for every \(i\).  Suppose there are four
pairwise disjoint connected sets \(A_1,A_2,C_1,C_2\), disjoint from
\(S\cup T\), with \(A_1,A_2\) full to \(S\) and \(C_1,C_2\) full to
\(T\).  If \(G[S]\) contains a triangle, then \(G\) has a
\(K_7\)-minor.

#### Proof

Form seven disjoint connected **rung bags**

\[
 R_s=\{s\},\qquad R_i=\{x_i,y_i\}\quad(1\le i\le6).
\tag{1.5}
\]

Choose three of these bags whose old roots form a triangle in \(G[S]\).
Leave those three bags unchanged, and assign
\(A_1,A_2,C_1,C_2\), one apiece, to the other four rung bags.

Every enlarged bag is connected: an old full set sees the old root of
its rung, and a new full set sees the new root.  Moreover, an enlarged
bag is adjacent to every other rung bag.  This is witnessed through the
old root when the assigned set is \(A_1\) or \(A_2\), and through the
new root when it is \(C_1\) or \(C_2\).  The three unenlarged bags are
pairwise adjacent through their old triangle.  The seven bags therefore
form a \(K_7\)-model. \(\square\)

The proofs expose the label-free principle.  Two frames joined by rooted
rungs, with \(q\) full connected helper sets distributed between the
frames, lift a rooted \(K_{n-q}\)-model in the residue to a \(K_n\)-model.
Here \((n,q)=(7,4)\), so the only residue needed is a rooted triangle.

## 2. Application to the low-owner descent

Let \(G\) be a hypothetical proper-minor-minimal counterexample to
\(HC_7\).  Let \(S\) be a seven-cut with three components

\[
 G-S=D\mathbin{\dot\cup}A_1\mathbin{\dot\cup}A_2,
\qquad N(D)=N(A_1)=N(A_2)=S,
\tag{2.1}
\]

and suppose \(G[S]\) is the pure Moser spindle.  By the audited
owner-count theorem, a low-owner shore either has the eliminated finite
base or yields a proper connected \(C\subsetneq D\) with

\[
 |N_G(C)|=7.                                      \tag{2.2}
\]

Put \(T=N_G(C)\).  Every component of \(G-T\) is full to \(T\), by
seven-connectivity.  The audited component bound says that \(G-T\) has
at most three components.  We prove that it cannot have three.

If (2.2) comes from an internal two-cut \(\{p,q\}\) of \(D\), the
descent theorem gives

\[
 T=\{p,q\}\cup N_S(C),\qquad |N_S(C)|=5.
\tag{2.3}
\]

Thus \(|S\cap T|=5\).  If \(G-T\) had three components, besides \(C\)
there would be another component \(C'\) not containing the old shores
\(A_1,A_2\).  Indeed, each of the two vertices of \(S-T\) has a
neighbour in both old full shores, so \(A_1,A_2\) and \(S-T\) lie in
one component of \(G-T\).  Consequently \(C'\) contains no old boundary
vertex.  The four sets \(A_1,A_2,C,C'\) are therefore pairwise
disjoint, avoid \(S\cup T\), and the sets \(C,C'\) are full to \(T\).
The three-component boundary classification makes \(G[T]\) a pure
Moser spindle.  Lemma 1.1, with old helpers \(A_1,A_2\) and new helpers
\(C,C'\), gives a \(K_7\)-minor, a contradiction.

If (2.2) comes from the three-face synchronization obstruction, then

\[
 T=\{s\}\cup\{y_x:x\in S-\{s\}\},               \tag{2.4}
\]

where the six vertices \(y_x\in D\) are distinct portal
representatives and \(xy_x\in E(G)\).  Hence \(S\cap T=\{s\}\) and
the six matching edges required by Lemma 1.2 are present.  Again, if
\(G-T\) had three components, every vertex of \(S-T\) joins both old
full shores, so \(A_1,A_2\) and all of \(S-T\) lie in one component.
The other two components are \(C,C'\); they avoid \(S\cup T\) and are
full to \(T\).  The old Moser spindle contains a triangle, so Lemma 1.2
gives a \(K_7\)-minor.

We have proved the following closure.

### Theorem 2.1 (three shores export only to two shores)

In a hypothetical proper-minor-minimal counterexample to \(HC_7\), every
three-component seven-cut with pure-Moser boundary exposes a nested exact
seven-cut having exactly two components.

The finite low-owner endpoint is excluded separately by the audited
degree-seven pure-Moser two-exterior theorem.  Therefore a three-shore
Moser cut cannot terminate locally, recur as another three-shore Moser
cut, or create an unbounded enumeration tree.  Its only possible output
is the uniform two-shore exact-adhesion obstruction.

## 3. Scope

Theorem 2.1 does not eliminate the final two-shore adhesion and hence is
not a proof of \(HC_7\).  Its contribution is structural: the
multi-component recursion is closed by a four-helper/rooted-residue lift.
The same lemma applies to arbitrary frames whenever the overlap residue
has the required rooted clique model.
