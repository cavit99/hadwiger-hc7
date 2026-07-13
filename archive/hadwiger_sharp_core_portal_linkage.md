# Portal-linkage targets for the two sharp order-seven contact cores

## 1. The rooted torso is genuinely seven-connected

Let \(G\) be seven-connected, let \(S\subseteq V(G)\) have order seven,
and let \(D\) be a component of \(G-S\).  Suppose there is another
component of \(G-S\).  Define the boundary torso

\[
 T_D:=G[D\cup S]+K_S,
\]

where all missing edges inside \(S\) are added.

### Lemma 1.1 (clique-boundary torso)

\(T_D\) is seven-connected.

#### Proof

Let \(W\subseteq V(T_D)\) have order at most six.  Some vertex of \(S\)
survives, and all surviving vertices of \(S\) lie in one component of
\(T_D-W\), since \(S\) is a clique in the torso.  If another component
\(X\) existed, then \(X\subseteq D\) and \(N_{T_D}(X)\subseteq W\).
Adding edges only inside \(S\) does not change the neighbourhood of a
set contained in \(D\), so \(N_G(X)\subseteq W\).  The other component of
\(G-S\) lies outside \(X\cup W\), and consequently \(W\) separates \(G\),
contrary to seven-connectivity.  Thus \(T_D-W\) is connected. \(\square\)

This is stronger packaging of the local inequalities

\[
 |N_D(X)|+|N_S(X)|\ge7
\]

for every nonempty proper \(X\subset D\).  It also identifies the exact
place where a rooted contraction/splitter theorem would apply.  A generic
\(k\)-connected splitter theorem is unavailable for \(k\ge4\), so any
compression must preserve the specified boundary or return a direct
minor/separator alternative.

## 2. The five-cycle core: an oriented two-path certificate

Assume

\[
 \overline{G[S]}=C_5\dot\cup2K_1.
\]

Label the complementary cycle \(0\,1\,2\,3\,4\,0\), so these five pairs
are precisely the nonedges among the cycle terminals, and call the two
isolated complement vertices \(r_1,r_2\).  Let \(D,D'\) be the two full
shores.

For \(i\in\{0,1,2,3,4\}\), put

\[
 A_i=N_D(i).
\]

### Lemma 2.1 (oriented bridge certificate)

Suppose \(D\) contains vertex-disjoint paths

\[
 P=x_0P x_1,\qquad Q=y_2Q y_3,
\]

where \(x_i\in A_i\) and \(y_i\in A_i\).  Suppose further that there is
a \(P\)-\(Q\) path \(R\) internally disjoint from \(P\cup Q\), with ends
\(x\in V(P)\), \(y\in V(Q)\), such that

\[
 x\ne x_0,\qquad y\ne y_3.                            \tag{2.1}
\]

Then \(G\) contains a \(K_7\)-minor.

#### Proof

Orient \(P\) from \(x_0\) to \(x_1\).  Cut \(P\) at the edge immediately
preceding \(x\); put the prefix in a bag rooted at \(0\), and the suffix,
together with the \(x\)-side of \(R\), in a bag rooted at \(1\).  If
\(x=x_1\), the same prescription cuts the last edge of \(P\).  Condition
\(x\ne x_0\) makes the cut available.

Orient \(Q\) from \(y_2\) to \(y_3\).  Cut it at the edge immediately
following \(y\); put the prefix, together with the \(y\)-side of \(R\),
in a bag rooted at \(2\), and the suffix in a bag rooted at \(3\).  If
\(y=y_2\), cut the first edge.  Condition \(y\ne y_3\) makes this cut
available.  Finally split \(R\) at any edge, assigning its two sides to
the rooted \(1\)- and \(2\)-bags.

The four resulting rooted bags are disjoint and connected.  The three
cut edges repair exactly the nonedges \(01,12,23\).  All other pairs
among \(0,1,2,3\) are edges of \(G[S]\).  Add the connected bag

\[
 D'\cup\{4\}.
\]

It is adjacent to all four rooted bags through the full shore \(D'\),
and hence repairs the remaining nonedges \(34,40\).  The five bags are a
rooted \(K_5\)-model at the cycle terminals.  The singleton bags
\(\{r_1\},\{r_2\}\) are adjacent to every rooted bag through its boundary
root and to one another.  These seven bags form a \(K_7\)-model.
\(\square\)

Thus the exact Two Paths input is obtained by adjoining four artificial
terminals \(a_0,a_1,a_2,a_3\) to the portal sets

\[
 A_0,A_1,A_2,A_3
\]

and asking for disjoint \(a_0a_1\)- and \(a_2a_3\)-paths.  A positive
answer closes the core whenever a bridge between the two paths has the
orientation (2.1).  If every positive linkage lacks such a bridge, its
path-bridge decomposition has a one-sided attachment order; if the Two
Paths instance is negative, Seymour's theorem gives its planar-web
alternative.  These are precise residuals, not an appeal to arbitrary
rooted \(K_5\).

## 3. The \(K_3\dot\cup2K_2\) core: a three-linkage certificate

Assume the missing edges on \(S\) are

\[
 01,02,12,34,56.                                      \tag{3.1}
\]

Again let \(D,D'\) be the two full shores and put \(A_i=N_D(i)\).

### Lemma 3.1 (three-pair linkage certificate)

If \(D\) contains three pairwise vertex-disjoint paths joining,
respectively,

\[
 A_1\text{ to }A_2,\qquad
 A_3\text{ to }A_4,\qquad
 A_5\text{ to }A_6,                                  \tag{3.2}
\]

then \(G\) contains a \(K_7\)-minor.

#### Proof

Split each path at an edge, assigning its two connected sides to bags
rooted at its two boundary terminals.  This creates six disjoint
connected rooted bags and repairs the nonedges \(12,34,56\).  Every
other pair among \(1,2,3,4,5,6\) is an edge of \(G[S]\).  Replace the
rooted \(0\)-bag by

\[
 D'\cup\{0\}.
\]

The full shore makes this bag adjacent to all other six bags, repairing
the remaining nonedges \(01,02\).  The seven bags form a \(K_7\)-model.
\(\square\)

Consequently the second sharp core is reduced to a fixed three-pair
linkage obstruction inside each seven-connected clique-boundary torso,
not to a general model-meeting assertion.

## 4. The exact next structural lemma

The two finite small-shore exhaustions and Lemmas 1.1--3.1 isolate the
following core-specific target.

> **Portal linkage-or-web lemma.**  Let \(T=D\cup S+K_S\) be a
> seven-connected clique-boundary torso, with \(D\ne\varnothing\).
> For the \(C_5\dot\cup2K_1\) portal order, either the oriented bridge
> certificate of Lemma 2.1 exists, or the Two Paths web has a cross
> forced by the other three full portal sets, or it exposes a separator
> of the original graph of order at most six.  For the
> \(K_3\dot\cup2K_2\) portal order, either the three-pair linkage (3.2)
> exists, or its linkage obstruction exposes such a separator.

The statement deliberately retains the boundary graph, portal sets,
seven-connectivity, and separator alternative.  Removing these features
would turn it into a false generic linkedness assertion.
