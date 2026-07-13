# Unique carrier ownership forces a literal lobe boundary

## 1. Setting

Retain the left double-same-bag cell of the degree-nine Moser lock.
Thus

\[
 L_6=K\mathbin{\dot\cup}D,qquad 6\in D,qquad
 K\not\sim R_5,R_0,                                      \tag{1.1}
\]

where (K,D) are connected and adjacent, and the root (rin K)
is the unique exterior (h)-neighbour in (K).  The cross-half
closure gives

\[
                         K\not\sim\{3,4\}.                 \tag{1.2}
\]

Assume the carrier edge is uniquely owned at (r), in the precise
sense

\[
                         N_K(D)=\{r\}.                      \tag{1.3}
\]

This is the static obstruction exhibited by the width-five double-spine
family: the protected root is the only vertex of the outer root
component which can remain on the (6)-side of a root exchange.

Let (U) be any component of (K-r).  It is a root-free lobe.  Put

\[
 I(U)=N_G(U)\cap\{1,2\},qquad
A(U)=N_G(U)\cap L_0.                                     \tag{1.4}
\]

Before imposing unique ownership, an additional carrier contact has a
complete structural interpretation.  Use an ordered-prefix split

\[
                         L_0=P\mathbin{\dot\cup}S,          \tag{1.5}
\]

where (P) contains the ordinary-left root, (P,S) are connected and
adjacent, (P,S\sim K), and (S) retains the two right contacts.

### Lemma 1.1 (extra carrier contact is exchange or ownership)

Let (U) be a component of (K-r), put (E=K-U), and suppose

\[
                         U\sim P,D.                         \tag{1.6}
\]

Then exactly one of the following descriptions applies.

1. If (E\sim S,P), then (G) contains a (K_7)-minor.
2. If (E\sim S) but (E\not\sim P), the split
   (K=E\dot\cup U) gives the two-left-bag root exchange; moreover
   (U) owns every (K)-to-(P) contact.
3. If (E\not\sim S), then (U) owns every (K)-to-(S) contact.

#### Proof

The set (E) is connected: it consists of (r) together with every
component of (K-r) other than (U).  If (E\sim S), then

\[
 r\in E,qquad E\sim S,qquad U\sim P,D
\]

are precisely the hypotheses of the two-left-bag root exchange.  If
also (E\sim P), use the seven bags

\[
 \{h\},\ \{1\},\ \{2\},\ P,\ E,\
 \{v\}\cup S\cup R_5,\ U\cup D\cup R_0.
\]

The last four form a clique through (PE,PS,PU,ES,EU,v6), and the
usual roots and the vertices (v,6) give all contacts to (h,1,2).
This is outcome 1.  Otherwise every (K)-to-(P) edge has its
(K)-endpoint in (U), and the exchanged left bags are

\[
                    P\cup U\cup D,qquad S\cup E,
\]

which is outcome 2.  If (E\not\sim S), connectedness of the old
model still gives (K\sim S), so every such contact is owned by (U),
proving outcome 3. \(\square\)

In a globally minimized model, outcome 2 also has the familiar size
orientation (|E|\ge|P|).  Thus an extra (D)-boundary class is not a
new uncontrolled case: it produces (K_7), a label-preserving model
transition, or total ownership of one ordered-spine side.  Theorem 2.1
below treats the only remaining branch, where no lobe has such a
carrier contact and (1.3) holds.

## 2. Exact boundary classification

### Theorem 2.1 (unique-owner lobe boundary)

If (G) is (K_7)-minor-free in the double-same cell, then

\[
                   N_G(U)=\{r\}\mathbin{\dot\cup}I(U)
                                  \mathbin{\dot\cup}A(U).  \tag{2.1}
\]

Consequently, seven-connectivity gives

\[
                         |A(U)|\ge6-|I(U)|\ge4.             \tag{2.2}
\]

If equality holds in the first inequality, then (N_G(U)) is an
exact seven-cut.  In particular,

\[
\begin{array}{c|c}
|I(U)|&\text{minimum ordinary-spine capacity}\\ \hline
2&4\\
1&5\\
0&6.
\end{array}                                                \tag{2.3}
\]

#### Proof

Because (U) is a component of (K-r) and (K) is connected,

\[
                            N_K(U)=\{r\}.                   \tag{2.4}
\]

Equation (1.3) makes (U) anticomplete to (D).  Equation (1.1)
makes it anticomplete to (R_5\cup R_0), and (1.2) excludes (3,4).
The vertex (v) has no exterior neighbour, since (N(v)) is exactly
the seven-vertex Moser boundary.  Finally (h) has degree nine and its
four exterior neighbours are the four prescribed roots; hence its only
neighbour in (K) is (r\notin U).  The spanning four-bag model
exhausts all remaining exterior vertices.  Thus every neighbour of
(U) outside (K) lies in ({1,2}\cup L_0), proving the inclusion
from left to right in (2.1).  The reverse inclusion is the definition
of (I(U),A(U)), together with (2.4).

The set (N_G(U)) is a genuine separator: (U) and (v) survive in
different components after its deletion.  Seven-connectivity and
(2.1) give

\[
 7\le |N_G(U)|=1+|I(U)|+|A(U)|,
\]

which is (2.2).  Equality gives a separator of order seven. \(\square\)

This is stronger than a portal count on the whole outer bag.  Every
individual component behind the carrier-owning root must expose four to
six distinct vertices of the one ordinary bag.

### Corollary 2.2 (full exact adhesion)

If equality holds in (2.2), put (S=N_G(U)).  Then (U) is a full
(S)-shore, and every component of (G-S) is full to (S).

#### Proof

The first assertion is the definition of (S=N_G(U)).  If a component
(C) of (G-S) missed (s\in S), then

\[
                         N_G(C)\subseteq S-\{s\},
\]

which would be a separator of order at most six.  This contradicts
seven-connectivity. \(\square\)

Thus equality is not merely a count: it is an actual palette-tight
adhesion and therefore a concrete exact boundary-state/transition
instance.  The previously proved alternating capacity exchange has a
more specific two-carrier invariant, so it may be invoked here only
after a separate mapping of this boundary into that invariant.  No such
mapping is asserted in this note.

## 3. A literal lobe--spine exchange

The boundary theorem also identifies the only available static descent.
The following exchange is label-free.

### Lemma 3.1 (lobe--interval swap)

Let (U) be a component of (K-r), and let
\(\varnothing\ne X\subset L_0\) avoid the prescribed root of (L_0).
Assume

1. ((L_6-U)\cup X) is connected;
2. ((L_0-X)\cup U) is connected; and
3. (L_0-X) retains an edge to each of (R_5,R_0).

Then

\[
 \widehat L_6=(L_6-U)\cup X,qquad
 \widehat L_0=(L_0-X)\cup U,qquad
 \widehat R_5=R_5,qquad \widehat R_0=R_0               \tag{3.1}
\]

is another spanning balanced rooted (K_4)-model with the same four
roots and the same locations of (5,6).

#### Proof

Connectivity is assumed for the two changed bags.  Both roots stay in
their labelled bags because (r\notin U) and (X) avoids the
(L_0)-root.  The vertex (6) remains in (L_6-U), and (5) is
untouched.  The two new left bags are adjacent through an edge from
(U) to (r), which crosses in the new allocation.  The first new
left bag retains both right-bag contacts through (D): (D R_5) is
witnessed by (65), and the retained cross-carrier edge gives
(D R_0).  The second retains both by hypothesis 3.  All right-hand
data are unchanged. \(\square\)

For the globally minimized ordinary-bag potential, Lemma 3.1 gives the
sharp size inequality

\[
                              |X|\le |U|,                   \tag{3.2}
\]

because the change in (|L_0|+|R_0|) is exactly
(|U|-|X|).  Therefore any segment of the ordered spine which is
bridged by (U), retains a contact to (K-U), and can be removed
without losing the two far contacts is either no larger than (U) or
contradicts global minimality.  This converts portal order into a
metric capacity constraint rather than another finite contact case.

The symmetric lemma holds at the right gate.  If proposed swaps on both
sides are only jointly admissible, assume explicitly that the four
reallocated bags are connected and retain all six pairwise bag
adjacencies (in particular the new ordinary bags remain adjacent).
The same cardinality calculation then gives

\[
                       |X_L|+|X_R|\le |U_L|+|U_R|.          \tag{3.3}
\]

## 4. Why boundary cardinality alone still stops short

The family in
`hadwiger_degree9_double_same_bag_counterarchitecture.md` can be
strengthened as follows.  Take (c=3), and join (x_1) to every
vertex of the left spine and (y_1) to every vertex of the right
spine; leave (x_2,x_3,y_2,y_3) as the original edge-simplicial
capacity vertices.  This is implemented by

```text
build_double_same_spines(m, 3, distributed_capacity=1).
```

For (m=6), the lobe ({x_1}) has the exact boundary

\[
                         \{k,u_0,u_1,u_2,u_3,u_4,u_5\},    \tag{4.1}
\]

of order seven.  For (m>6), its boundary is strictly larger than
seven.  Every ordered-prefix row still has at least four distinct
outer-bag neighbours, the old carrier edges and global potential
minimum are retained, and both rooted exchanges remain blocked because
(k) is still the unique (6)-owner.

Nevertheless the graphs still have treewidth at most five.  Eliminate
the undistributed capacity vertices first.  On the left eliminate
(u_1,\ldots,u_{m-3}), then (x_1), then (u_{m-2},u_{m-1})
(omit nonexistent terms when (m=2)); do the symmetric operation on
the right.  At the first stage the later-neighbour set is
({k,x_1,u_0,u_{i+1}}); at the (x_1)-step it is contained in
({k,u_0,u_{m-2},u_{m-1}}); the final two spine vertices have at
most three later neighbours.  The remainder is the width-five order in
Proposition 6.1 of the cited note.  The independent script
`degree9_unique_owner_lobe_boundary_verify.py` checks the boundary and
width certificates for every (2\le m\le12), and rechecks the exact
potential minimum on the order-(m=4) core.

Hence the strict alternative in Theorem 2.1 may consist entirely of
additional vertices of the **same** ordinary-spine class.  There need
not be a new boundary class which gives a static crossed model.
Seven-connectivity supplies the capacity lower bound, but the operation
which consumes that capacity must use either the lobe--interval swap,
an exact boundary-state transition at equality, or a
contraction-critical state transition.

## 5. Exact remaining sub-gap

The unique-owner branch has now been reduced to a literal statement.
For every root-free lobe (U), either

1. (N(U)) is an exact full seven-adhesion and becomes a concrete
   boundary-state/transition instance; or
2. (U) has strict same-spine capacity, and every admissible
   lobe--interval swap satisfies the size lock (3.2).

What is still missing is a proof that the one-step deletion/contraction
transition breaks one of these size locks, or that two opposite locked
lobes admit a jointly smaller swap.  The distributed width-five family
shows that this conclusion cannot be obtained from boundary size,
portal order, and model potential alone.
