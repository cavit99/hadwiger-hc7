# The degree-nine Moser hub: cross-half contacts and the four-portal residue

## 1. Setting

Use the notation and hypotheses of
`hadwiger_degree9_hub_portal_lock.md`.  Thus \(G\) is seven-connected
and \(K_7\)-minor-free, the four spanning rooted bags are

\[
                    L_6,L_0,R_5,R_0,
\]

they are pairwise adjacent, \(6\in L_6\), \(5\in R_5\), the roots of
\(L_6,L_0\) see \(h,1,2\), and the roots of \(R_5,R_0\) see
\(h,3,4\).  Let \(e_6\) be the root of \(L_6\), let \(K\) be the
component of \(L_6-6\) containing \(e_6\), and put

\[
                         D=L_6-K.                 \tag{1.1}
\]

As in Corollary 4.4 of the cited note, \(D\) is connected, contains
\(6\), and has an edge to \(K\).

## 2. One cross-half contact closes the lock

### Theorem 2.1 (cross-half gate closure)

If \(K\) is adjacent to either \(3\) or \(4\), then \(G\) contains a
\(K_7\)-minor.

#### Proof

Suppose first that \(K\) is adjacent to \(3\).  Use the seven branch
sets

\[
\begin{array}{lll}
 A_0=\{v\},&A_1=\{h\},&A_2=\{1\},\\
 A_3=\{2\},&A_4=K\cup\{3\},&A_5=D\cup R_5,\\
 &&A_6=\{4\}\cup L_0\cup R_0 .
\end{array}                                      \tag{2.1}
\]

They are disjoint.  The only nontrivial connectivity checks are as
follows.

* \(A_4\) is connected by the assumed \(K\)-\(3\) edge.
* \(A_5\) is connected by \(56\), because \(6\in D\) and
  \(5\in R_5\).
* \(A_6\) is connected because the root of \(R_0\) sees \(4\), and
  the old rooted model has an \(R_0\)-\(L_0\) edge.

For completeness, the following table gives a witness for every one
of the twenty-one required adjacencies.  An entry in row \(A_i\),
column \(A_j\) is an edge or an old bag adjacency joining the two
sets.

\[
\begin{array}{c|cccccc}
 &A_1&A_2&A_3&A_4&A_5&A_6\\ \hline
A_0&vh&v1&v2&v3&v6&v4\\
A_1&  &h1&h2&he_6&h(E\cap R_5)&h4\\
A_2&  &  &12&1e_6&16&1(E\cap L_0)\\
A_3&  &  &  &2e_6&26&2(E\cap L_0)\\
A_4&  &  &  &  &E(K,D)&34\\
A_5&  &  &  &  &  &E(R_5,L_0)
\end{array}                                      \tag{2.2}
\]

Here expressions such as \(h(E\cap R_5)\) mean the edge from \(h\)
to the unique exterior root in that bag.  Thus (2.1) is a \(K_7\)-model.
If \(K\) is adjacent to \(4\), interchange \(3\) and \(4\) in (2.1)
and (2.2).  \(\square\)

This construction does not use any allocation of the three old
adjacencies from \(L_6\) to \(L_0,R_5,R_0\).  In particular, it applies
in both attachment alternatives of Corollary 4.4.

### Symmetric form

Let \(e_5\) be the root of \(R_5\), let \(K_5\) be the component of
\(R_5-5\) containing \(e_5\), and put \(D_5=R_5-K_5\).  If \(K_5\)
is adjacent to \(1\) or \(2\), then \(G\) contains a \(K_7\)-minor.
For example, from a \(K_5\)-\(1\) edge use

\[
 \{v\},\ \{h\},\ \{3\},\ \{4\},\
 K_5\cup\{1\},\ D_5\cup L_6,\
 \{2\}\cup R_0\cup L_0 .                       \tag{2.3}
\]

The adjacency audit is the image of (2.2) under

\[
 (1,2,6,L_6,L_0)\longleftrightarrow(3,4,5,R_5,R_0).
\]

## 3. Exact fixed-boundary neighbourhood and the sharper adhesion

### Theorem 3.1 (four fixed neighbours plus one portal class)

In the \(K_7\)-minor-free residue, one of the following two exact
descriptions holds:

\[
\begin{array}{ll}
 K\not\sim L_0,&
 N_G(K)=\{h,1,2,6\}\mathbin{\dot\cup}
       \bigl(N(K)\cap(R_5\cup R_0)\bigr),\\[1mm]
 K\not\sim R_5,R_0,&
 N_G(K)=\{h,1,2,6\}\mathbin{\dot\cup}
       \bigl(N(K)\cap L_0\bigr).
\end{array}                                      \tag{3.1}
\]

Consequently, if \(P\) denotes the portal set on the right hand side,
then

\[
                            |P|\ge 3.             \tag{3.2}
\]

If \(|P|=3\), then \(N_G(K)\) is an exact seven-vertex cut.  If the
exact-seven-adhesion outcome is excluded, the true strict-surplus
residue satisfies

\[
                            |P|\ge4.              \tag{3.3}
\]

#### Proof

Corollary 4.4 of the cited note supplies the two alternatives in
(3.1).  The spanning property puts every vertex outside
\(\{v,h,1,2,3,4\}\) in one of the four rooted bags.  Within \(L_6\),
the component \(K\) of \(L_6-6\) can leave only through \(6\).
Moreover, \(v\) has no neighbour in \(K\), since \(K\) contains no
member of \(N(v)\), and Theorem 2.1 says that \(K\) has no neighbour
in \(\{3,4\}\).  These observations give the inclusion from left to
right in (3.1).

Conversely, \(e_6\in K\) is adjacent to \(h,1,2\), and connectedness
of \(L_6\) forces the component \(K\) of \(L_6-6\) to have an edge to
\(6\).  The portal set is defined to contain all neighbours in its
allowed bags.  Hence equality holds in (3.1).

The set \(N_G(K)\) is a genuine separator: both \(K\) and the
non-neighbour \(v\) survive its deletion.  Seven-connectivity and
(3.1) give \(4+|P|=|N_G(K)|\ge7\), proving (3.2).  Equality is exactly
the seven-cut outcome, and its negation gives (3.3). \(\square\)

The symmetric statement is

\[
 N_G(K_5)=\{h,3,4,5\}\mathbin{\dot\cup}P_5,
                                                        \tag{3.4}
\]

where either \(K_5\not\sim R_0\) and
\(P_5=N(K_5)\cap(L_6\cup L_0)\), or
\(K_5\not\sim L_6,L_0\) and \(P_5=N(K_5)\cap R_0\).
Again \(|P_5|=3\) is an exact seven-cut, and the strict residue has
\(|P_5|\ge4\).

Thus the literal boundary contacts of \(K\) are now characterized:

\[
\begin{array}{c|c}
\text{status}&\text{literal boundary vertices}\\ \hline
\text{forced neighbours}&h,1,2,6\\
\text{forced non-neighbours}&v,3,4\\
\text{unrestricted by this argument}&5.
\end{array}                                      \tag{3.5}
\]

The vertex \(5\) belongs to \(R_5\), so a \(K\)-\(5\) edge is a
portal in the first line of (3.1), not a cross-half literal contact.
Unlike a \(K\)-\(3\) or \(K\)-\(4\) edge, it does not by itself give
the model (2.1).  A conservative double-split quotient with a direct
\(K\)-\(5\) edge remains \(K_7\)-minor-free under exact minor search;
therefore any use of that edge must also exploit the internal gate in
\(R_5\), rather than treating \(R_5\) as one contracted bag.

## 4. What the edge-critical Kempe fan does and does not add

Choose \(x\in K\) with \(x6\in E(G)\).  Such an \(x\) exists by the
proof of Theorem 3.1.  In every six-colouring of \(G-x6\), the two
endpoints have the same colour, say \(\lambda\).  For every other
colour \(\gamma\), they lie in one component of the
\(\{\lambda,\gamma\}\)-subgraph; otherwise switching that component
at \(x\) would colour the restored edge.  Hence there are five
colour-prescribed Kempe \(x\)-\(6\) paths.

This fact alone does **not** make those paths internally disjoint.
Paths for different second colours may share arbitrarily many
\(\lambda\)-coloured vertices.  In particular, a single
\(\lambda\)-coloured portal can carry all five Kempe paths.  Thus no
label-preserving bag split follows merely by counting the five paths.

Ambient seven-connectivity does supply six internally vertex-disjoint
alternate \(x\)-\(6\) paths besides the edge \(x6\), but this does not
count portals either: several such paths may stay in \(K\) until their
last edge to the common endpoint \(6\).  The bound \(|P|\ge3\) comes
instead from the genuine separator \(N_G(K)\) in Theorem 3.1.

The remaining problem is therefore accurately a
**four-portal, label-preserving splitter problem**, not a consequence
of the ordinary five Kempe paths.  Any successful edge-critical
argument must use recolouring transitions to control the placement of
the portals inside the target bag(s), or combine the two symmetric
four-portal gates; pairwise Kempe connectivity by itself is
insufficient.
