# A critical boundary edge gives a local fan or a smaller exact seven-separation

**Status:** written proof; separate internal audit GREEN in
[`hc7_exact7_critical_edge_fan_descent_audit.md`](hc7_exact7_critical_edge_fan_descent_audit.md).

This note gives a well-founded host-level reduction at an actual
seven-vertex separator.  A critical edge from an open component to the
separator produces five colour-indexed first edges.  Seven-connectivity
always extends those edges to a six-ended fan inside the component.  If the
original bichromatic paths use at most five boundary vertices together with
the deleted-edge endpoint, a target-preserving version either gives a clean
five-spoke packing or returns a strictly smaller component behind another
actual separator of order seven.  The smaller separator retains a proper
one-sided deletion colouring and an exact boundary colour class of order at
least two.

Nothing here identifies colours with clique-minor branch sets, constructs a
`K_7`-minor model, or proves `HC_7`.

## 1. Setting and the five critical paths

Let `G` be a seven-connected graph which is not six-colourable and whose
every proper minor is six-colourable.  Let `Y` be a seven-set and let `C` be
a component of `G-Y` such that

\[
                         G-(C\cup Y)\ne\varnothing .       \tag{1.1}
\]

Choose an edge

\[
                         xv\in E(G),\qquad x\in Y,
                         \quad v\in C.                    \tag{1.2}
\]

The proper minor \(G-xv\) has a proper six-colouring \(d\).  Necessarily

\[
                         d(x)=d(v)=\alpha,                 \tag{1.3}
\]

because otherwise \(d\) would already be a proper six-colouring of \(G\).
Every one of the other five colours occurs: if a colour \(\beta\) were
absent, recolouring \(v\) with \(\beta\) would make \(xv\) proper and
six-colour \(G\).

For every colour \(\beta\ne\alpha\), the vertices \(v,x\) lie in one component
of the \(\alpha\)--\(\beta\) subgraph of \(G-xv\).  Indeed, otherwise interchanging
the two colours on the component containing \(v\) would make the edge \(xv\)
proper and six-colour \(G\).  Choose a simple \(\alpha\)--\(\beta\) path from \(v\)
to \(x\), stop it at its first vertex of \(Y\), and denote the resulting path
by

\[
                         P_\beta=v s_\beta\cdots t_\beta,
                         \qquad t_\beta\in Y.             \tag{1.4}
\]

Every internal vertex of \(P_\beta\) lies in \(C\).  Moreover

\[
                         d(s_\beta)=\beta,                 \tag{1.5}
\]

so the five vertices \(s_\beta\) are distinct.  If paths belonging to
distinct colours \(\beta,\gamma\) meet, every common vertex has colour
\(\alpha\), because

\[
             \{\alpha,\beta\}\cap\{\alpha,\gamma\}
                         =\{\alpha\}.                     \tag{1.6}
\]

Only the first edges \(vs_\beta\) will be prescribed in the first conclusion;
the rerouted paths need not remain bichromatic.

## 2. A six-ended fan inside the component

### Theorem 2.1 (local prescribed-first-edge fan)

There are six paths from \(v\) to \(Y\) which

1. share no vertex other than \(v\);
2. have six distinct ends in \(Y\);
3. include the edge \(vx\); and
4. begin, on the other five paths, with the five prescribed edges
   \(vs_\beta\).

Apart from their boundary ends, all six paths lie in \(C\).

#### Proof

First dispose of prescribed paths which are already boundary edges.  Put

\[
 I=\{\beta:s_\beta=t_\beta\in Y\},\qquad r=|I|.          \tag{2.1}
\]

The \(r\) edges \(vs_\beta\), \(\beta\in I\), have distinct ends in
\(Y-\{x\}\).  If \(r=5\), these edges together with \(vx\) prove the
theorem.  Otherwise put

\[
 S=\{s_\beta:\beta\notin I\},\qquad
 T=Y-(\{x\}\cup\{s_\beta:\beta\in I\}),                \tag{2.2}
\]

and consider \(K=G[(C-\{v\})\cup T]\).  Here
\(|S|=5-r\) and \(|T|=6-r\).  Suppose that \(K\) has no \(5-r\)
pairwise vertex-disjoint \(S\)--\(T\) paths using every vertex of \(S\)
and having distinct ends in \(T\).  The set form of Menger's theorem gives
an \(S\)--\(T\) separator \(Z\) of order at most \(4-r\); it may contain
terminals.

Some \(s\in S-Z\) and some \(t\in T-Z\) survive.  Let \(A\) be the
component of \(K-Z\) containing \(s\).  Since \(Z\) separates \(S\) from
\(T\), the component \(A\) contains no vertex of \(T-Z\).  Hence
\(A\subseteq C-(\{v\}\cup Z)\) and

\[
 N_G(A)\subseteq Z\cup\{v,x\}
       \cup\{s_\beta:\beta\in I\}.                     \tag{2.3}
\]

The surviving target \(t\) lies outside \(A\cup N_G(A)\).  Thus (2.3) is
a nontrivial separator of order at most

\[
                           (4-r)+2+r=6,
\]

contrary to seven-connectivity.  The required linkage exists.  Prepend
\(vs_\beta\) to every newly linked path, restore the \(r\) direct paths,
and retain \(vx\).  The five non-\(x\) target vertices are distinct, and
every internal vertex lies in \(C\).  The resulting six paths have all the
asserted properties. \(\square\)

The theorem prescribes the five first edges but not which five vertices of
\(Y-x\) they reach.

## 3. Retaining the original bichromatic target set

Put

\[
                  T_0=\{x\}\cup\{t_\beta:\beta\ne\alpha\}.
                                                               \tag{3.1}
\]

### Theorem 3.1 (target-retaining packing or strict descent)

Assume that \(|T_0|\le5\), and choose any five-set \(T\subseteq Y\) containing
\(T_0\).  Then one of the following holds.

1. There are five \(v\)--\(T\) paths which preserve the five first edges
   \(vs_\beta\) and are pairwise vertex-disjoint outside \(\{v\}\cup T\).
   Their ends in \(T\) are allowed to coincide.
2. There are a four-set \(Z\subseteq C-\{v\}\) and a nonempty connected set
   \(A\subseteq C-(\{v\}\cup Z)\) such that

   \[
             N_G(A)=(Y-T)\mathbin{\dot\cup}\{v\}
                            \mathbin{\dot\cup}Z.          \tag{3.2}
   \]

   In particular, `N_G(A)` is the boundary of an actual order-seven
   separation and

   \[
                              |A|<|C|.                    \tag{3.3}
   \]

   The restriction of \(d\) to \(G[A\cup N_G(A)]\) is a proper colouring in
   the original graph \(G\).  Its exact \(\alpha\)-coloured boundary class has
   order at least two.

#### Proof

Work in

\[
                         K_T=G[(C-\{v\})\cup T].          \tag{3.4}
\]

Let \(I\) and \(r\) be as in (2.1).  The \(r\) direct paths
\(vs_\beta\), \(\beta\in I\), already satisfy the conclusion.  Apply
vertex-capacitated Menger from the remaining \(5-r\) sources to \(T\),
giving unit capacity to vertices of \(C-v\) and unlimited capacity to the
targets in \(T\).  If the maximum packing has order \(5-r\), it uses every
remaining source and its paths are pairwise disjoint outside `T`.
Prepending their prescribed first edges and adding the \(r\) direct paths
gives outcome 1.

Otherwise there is a set

\[
                         Z\subseteq C-\{v\},
                         \qquad |Z|\le4-r,                \tag{3.5}
\]

which meets every \(S\)--\(T\) path in \(K_T\).  Some source lies outside \(Z\).
Let \(A\) be its component in \(G[C-(\{v\}\cup Z)]\).  If \(A\) had a neighbour
in \(T\), the chosen source could be joined to that neighbour inside
\(A\cup T\), avoiding \(Z\).  Therefore

\[
             N_G(A)\subseteq (Y-T)\cup\{v\}\cup Z.       \tag{3.6}
\]

The right side of (3.6) has order at most

\[
                    (7-5)+1+(4-r)=7-r.                   \tag{3.7}
\]

The set \(T\) and the nonempty graph in (1.1) lie outside \(A\), so (3.6)
defines a genuine separation.  Seven-connectivity forces \(r=0\) and
equality throughout (3.5)--(3.7).  Hence \(|Z|=4\), every vertex displayed
on the right of
(3.6) belongs to \(N_G(A)\), and (3.2) follows.  Since \(v\in C-A\), (3.3)
is immediate.  Equality (3.2) also says that \(A\) is a component of
\(G-N_G(A)\) and is adjacent to every vertex of its new boundary.

For each \(\beta\ne\alpha\), the tail \(P_\beta-v\) is an \(S\)--\(T\) path in
\(K_T\), because \(t_\beta\in T_0\subseteq T\).  It therefore meets \(Z\).
Choose one vertex

\[
                         z_\beta\in V(P_\beta-v)\cap Z.   \tag{3.8}
\]

There are five choices in the four-set \(Z\), so
\(z_\beta=z_\gamma\) for two distinct colours \(\beta,\gamma\).  By (1.6), their
common value \(z\) has colour \(\alpha\).

The only edge on which \(d\) is improper in \(G\) is \(xv\).  But \(x\in T\),
whereas (3.2) is disjoint from \(T\); hence \(x\) does not belong to
\(A\cup N_G(A)\).  The restriction of \(d\) to that closed shore is
therefore proper in \(G\).  Its exact boundary colour class

\[
        J_A=\{y\in N_G(A):d(y)=\alpha\}                  \tag{3.9}
\]

contains the distinct vertices \(v,z\), and so has order at least two.  This
proves every assertion in outcome 2. \(\square\)

### Corollary 3.2 (the opposite shore attains the same exact block)

In outcome 2 of Theorem 3.1, some proper six-colouring of the opposite
closed shore has `J_A` as one exact boundary colour class.

#### Proof

The set \(A\cup J_A\) is connected: \(A\) is connected and (3.2) gives a
neighbour in \(A\) for every vertex of \(J_A\).  Contract a spanning tree of
\(G[A\cup J_A]\) and six-colour the resulting proper minor.  Keep the
colouring on the untouched opposite shore and assign every literal vertex
of `J_A` the colour of the contraction image.

The pullback is proper because \(J_A\) is independent and every edge from it
to an untouched vertex was represented at the contraction image.  It is
exact because the \(N_G(A)\)-full set \(A\) makes that image adjacent to every
vertex of \(N_G(A)-J_A\). \(\square\)

Thus the descent retains precisely the common-exact-block input needed by
the exact-seven boundary Kempe reduction; it does not retain a common full
equality partition.

## 4. Application to the fresh-colour exact-seven interface

Consider the setting in which

\[
                V(G)=L\mathbin{\dot\cup}Y
                         \mathbin{\dot\cup}R,
                \qquad |Y|=7,                            \tag{4.1}
\]

\(L\) and \(R\) are nonempty and anticomplete, \(p\in R\), \(v\in Y\), and
\(pv\in E(G)\).  Suppose a proper six-colouring of \(G-pv\) gives \(p,v\) one
common colour.  This is the interface used by the fresh-colour linkage
theorem.

Let \(C_p\) be the component of \(G-Y\) containing \(p\).  Apply Theorems 2.1
and 3.1 with

\[
                         C=C_p,\qquad x=v,
                         \qquad v_{\rm base}=p.           \tag{4.2}
\]

Theorem 2.1 gives a component-internal fan from `p` to six distinct
vertices of `Y`, preserving the five colour-indexed first edges and the
direct edge `pv`.

If the five original bichromatic first-hit vertices, together with `v`,
occupy at most five vertices of \(Y\), Theorem 3.1 gives either the clean
target-retaining packing or another actual order-seven separation.  In the
latter case its selected open component has order strictly less than
\(|C_p|\); the inherited deletion colouring is proper on that component's
closed shore and has an exact boundary class of order at least two.  The
old vertex \(v\) lies on the opposite side of the new separator, while \(p\)
is a new boundary vertex, so the sole deleted edge is again absent from the
coloured closed shore.

Consequently component order is a genuine well-founded rank for this
descent.  Indeed, (3.2) makes the new component adjacent to every vertex of
its new boundary, so any one of those incident edges supplies another
critical-edge instance, now with open-component order \(|A|\).  If one
chooses an exact-seven interface with its selected critical-edge component
of minimum order, the separator outcome of Theorem 3.1 is impossible: the
residue must exhibit either six distinct first-hit support or the clean
target-retaining five-spoke packing.

## 5. Exact limitations

1. The paths in Theorem 2.1 preserve their first edges but need not remain
   bichromatic and their five non-direct boundary ends are not prescribed.
2. In outcome 1 of Theorem 3.1, different paths may have the same boundary
   end.  The theorem does not allocate those paths among five named
   clique-minor branch sets.
3. The strict descent is available only when the original first-hit support
   \(T_0\) has order at most five and the target-retaining packing fails.
   Order-six support is a separate normalized obstruction.
4. Corollary 3.2 synchronizes one exact boundary block, not the entire
   boundary equality partition.
5. No conclusion here turns either clean fan into a `K_7`-minor model.
   That requires a label-preserving branch-set absorption theorem or a
   compatible-colouring theorem on the returned separator.

## 6. Dependencies

- Menger's theorem, in its set and vertex-capacitated forms.
- Las Vergnas--Meyniel style critical-edge Kempe switching is not needed as
  an external theorem; the short switching argument is included in
  Section 1.
