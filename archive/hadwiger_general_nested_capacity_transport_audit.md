# Adversarial audit: general nested capacity transport

## Verdict

**GREEN after one hypothesis is made explicit.**  The phrase “the outer
side contains the bags” must mean

\[
                         A_i\subseteq V(G)-D            \tag{A.1}
\]

(with the roots in \(S_0\subseteq V(G)-D\)).  Under (A.1), the nested
linkage, exact inner traces, capacity lift, and minimum-fragment argument
are all correct for arbitrary \(k,m\), including overlapping cuts and
trivial linkage paths.

If “outer side” is not interpreted as (A.1), Theorem 1.1 is false.  A
literal counterexample is given in Section 6 below.  The source note should
therefore define the two ordered separations and state (A.1) in symbols.

## 1. Why \(N(F)=S_1\)

Since \(F\) is a component of \(G-S_1\), initially only
\(N(F)\subseteq S_1\) is automatic.  Equality follows from minimum cut
order, but the source proof omits this step.

If some \(x\in S_1-N(F)\), then \(S_1-\{x\}\) still separates \(F\)
from any other component of \(G-S_1\).  This is a separator of order
\(k-1\), contrary to \(k\)-connectivity.  Hence

\[
                              N(F)=S_1.             \tag{1.1}
\]

In particular every inner adhesion vertex has a portal into \(F\).

Moreover, because \(F\subseteq D\) and \(D\) is a component of
\(G-S_0\), every neighbour of \(F\) lies in \(D\cup S_0\).  Thus

\[
                              S_1\subseteq D\cup S_0. \tag{1.2}
\]

## 2. The two separations really are nested

Write the ordered outer and inner separations explicitly as

\[
\begin{aligned}
 (O_0,I_0)&=(V(G)-D,\ S_0\cup D),\\
 (O_1,I_1)&=(V(G)-F,\ S_1\cup F).
\end{aligned}                                       \tag{2.1}
\]

Their adhesions are \(S_0,S_1\), respectively.  Since \(F\subseteq D\),
we have \(O_0\subseteq O_1\); (1.2) gives
\(I_1\subseteq I_0\).  Thus they are nested in the required direction.

Let \(R=S_0\cap S_1\).  Delete \(R\).  The graph \(G-R\) is
\((k-|R|)\)-connected, so Menger gives \(k-|R|\) disjoint paths from
\(S_0-R\) to \(S_1-R\), with distinct ends.  Add the \(|R|\) prescribed
trivial paths at the common vertices.  Minimal truncation at the first
and last adhesion vertices makes every nontrivial path avoid both
adhesions internally.

Nesting confines a retained path to

\[
 (I_0\cap O_1)-(S_0\cup S_1)
   =D-(F\cup S_0\cup S_1).                         \tag{2.2}
\]

Indeed, leaving \(I_0\) would force another meeting with \(S_0\), and
entering \(I_1-S_1\) before the final end would force an earlier meeting
with \(S_1\).  This proves the exact path assertion even when the two cuts
overlap.

## 3. Old bags and exact inner roots

Under (A.1), every old bag is disjoint from the open annulus in (2.2).
Its intersection with \(S_0\) is exactly its assigned root block:
although the statement initially says only \(R_i\subseteq A_i\), the
sets \(R_i\) partition \(S_0\), and disjointness of the bags forbids
\(A_i\) from containing a root assigned to another bag.

Every nontrivial linkage path meets an old bag only at its distinct old
root.  A common root in \(S_0\cap S_1\) is represented by its trivial
path.  A nontrivial inner end lies in

\[
                         S_1-S_0\subseteq D,         \tag{3.1}
\]

and hence in no old bag by (A.1).  Therefore the enlarged bags are
pairwise disjoint and connected, preserve every old clique-model edge,
and satisfy the exact equality

\[
                         A_i'\cap S_1=\lambda(R_i).  \tag{3.2}
\]

No unlabelled permutation is hidden: the linkage itself defines the
bijection \(\lambda\), while every common root is fixed.

## 4. Capacity tails lift correctly

Let \(Y_j\subseteq F\) be an inner carrier.  For a nontrivial path from
\(s\) to \(\lambda(s)\), put

\[
                         T_s=V(L_s)-\{s\}.          \tag{4.1}
\]

By (2.2)--(3.1), \(T_s\subseteq D\).  Since \(Y_j\) meets the portal
set of \(\lambda(s)\), some vertex of \(Y_j\) is adjacent to the inner
end of \(T_s\); hence

\[
                         Y_j\cup\bigcup_{s\in T_j}T_s \tag{4.2}
\]

is connected.  Its first vertex after the deleted old end \(s\) is an
old \(s\)-portal in \(D\), so (4.2) meets the required old portal set.

If the path is trivial, \(s=\lambda(s)\) and \(Y_j\) itself contains a
neighbour of the old root; no tail is needed.  Different lifted carriers
are disjoint because the label blocks, paths, and inner carriers are all
disjoint, and path interiors avoid \(F\).  Thus Theorem 2.1 is valid,
including all overlap/trivial-path cases.

## 5. Minimum fragments

Let \((S,F)\) minimize \(|F|\) among order-\(k\) cuts with a component
contained in \(D\), allowing \((S_0,D)\).  Fix nonempty proper
\(X\subsetneq F\).  Another component of \(G-S\) is anticomplete to
\(F\), so it is disjoint from \(N(X)\) and remains as a far side.
Consequently \(N(X)\) is a separator and \(|N(X)|\ge k\).

If equality holds, take a component \(K\) of \(G[X]\).  Then
\(N(K)\subseteq N(X)\).  The same far side survives, so
\(k\)-connectivity gives \(|N(K)|\ge k\), forcing

\[
                              N(K)=N(X).             \tag{5.1}
\]

Thus \(K\) is a component behind the order-\(k\) cut \(N(K)\), lies
properly in \(F\), and contradicts minimality.  Hence every nonempty
proper subset has neighbourhood at least \(k+1\).  The argument remains
valid for disconnected \(X\).

The concluding use of this fact needs the explicitly stated extra
hypothesis that the original shore \(D\) forbids the capacity returned by
the local augmentation theorem.  With that understood, the new capacity
lifts by Section 4 and contradicts the obstruction, while a proper nested
cut contradicts minimum choice.

## 6. Counterexample if the bags may enter the annulus

Let \(G=C_8\) with cyclic order

\[
                         0,1,2,3,4,5,6,7,0.
\]

This graph is two-connected.  Put

\[
 S_0=\{0,4\},\qquad D=\{1,2,3\},
\]

and

\[
 S_1=\{2,4\},\qquad F=\{3\}.
\]

Both are two-cuts and \(F\subseteq D\).  Take \(m=2\), root blocks
\(R_1=\{0\}\), \(R_2=\{4\}\), and the disjoint connected adjacent bags

\[
 A_1=\{0,7,6,5\},qquad A_2=\{4,3,2\}.           \tag{6.1}
\]

They form a \(K_2\)-model and contain the assigned roots, but \(A_2\)
enters \(D\).  The common root \(4\) must be fixed trivially, so the other
linkage path is \(0-1-2\) and \(\lambda(0)=2\).  Enlarging \(A_1\) along
that path makes it meet \(A_2\) at vertex \(2\); moreover
\(A_2\cap S_1=\{2,4\}\ne\lambda(R_2)=\{4\}\).

Thus disjointness and the exact trace both fail if “outer-side bag” is
allowed to contain annular vertices.  Condition (A.1) is essential, not
merely cosmetic.

