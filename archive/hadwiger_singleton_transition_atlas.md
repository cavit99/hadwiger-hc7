# The operation-critical atlas at a full-singleton lock

## 1. Boundary and terminology

Use the zero-optional singleton-triangle boundary

\[
 B=\{h,1,2,r,a,b,c\},\qquad
 E(\overline {G[B]})=
 \{hc,ra,hb,rb,1a,1c,2a,2c\}.                 \tag{1.1}
\]

Assume

\[
                    G-B=\{d\}\mathbin{\dot\cup}O,             \tag{1.2}
\]

where (d) is full to (B), (O) is connected and full to (B),
and (d) is anticomplete to (O).  The graph (G) is
minor-minimal non-six-colourable.  In the alternating orientation of
`hadwiger_singleton_packet_owner_lock.md`, all (1)-portals are on the
(Q)-side and all (2)-portals are on the (P)-side.

A matching state of order (m) is an equality partition of (B)
whose (m) nonsingleton blocks are pairwise vertex-disjoint edges of
the complement (1.1).  It has (7-m) boundary colour blocks.

The purpose of this note is deliberately local.  It gives the complete
state atlas at an operated alternating rung, converts the low-capacity
states into actual coloured paths, and isolates the exact-adhesion exit.
It does not assert that every alternating owner contains a low-capacity
rung.

## 2. The complete (17+8) atlas

Let

\[
 \sigma=(1\ 2),\qquad \tau=(h\ r)(a\ c).                       \tag{2.1}
\]

Both are automorphisms of the labelled boundary.  The following table is
an exhaustive orbit list under 
(\langle\sigma,\tau\rangle\).

\[
\begin{array}{c|c|c|c}
\text{order}&\text{representative}&\text{orbit size}&
 (1\text{ paired?},2\text{ paired?})\\ \hline
2&hc+ra&1&(0,0)\\
2&hc+rb&2&(0,0)\\
2&hc+1a&4&(1,0)\text{ or }(0,1)\\
2&hb+1a&4&(1,0)\text{ or }(0,1)\\
2&rb+1a&4&(1,0)\text{ or }(0,1)\\
2&1a+2c&2&(1,1)\\ \hline
3&hc+rb+1a&4&(1,0)\text{ or }(0,1)\\
3&hb+1a+2c&4&(1,1)
\end{array}                                                     \tag{2.2}
\]

For reference, without quotienting by symmetry the order-three states
are

\[
\begin{split}
 &hc+rb+1a,\ hc+rb+2a,\ ra+hb+1c,\ ra+hb+2c,\\
 &hb+1a+2c,\ hb+1c+2a,\ rb+1a+2c,\ rb+1c+2a.        \tag{2.3}
\end{split}
\]

### Lemma 2.1 (exhaustiveness)

There are exactly seventeen order-two states and eight order-three
states, and (2.2) is their complete orbit decomposition.

#### Proof

Two complement edges form a matching precisely when their four ends are
distinct.  Testing the eight edges in (1.1) gives the six rows of order
two in (2.2), of total size

\[
                         1+2+4+4+4+2=17.
\]

Three complement edges must cover six of the seven vertices.  If one of
(1,2) is uncovered, the other is paired and the remaining two edges
are (hc,rb), or its image under \(\tau\).  These are the first four
states in (2.3).  If neither is uncovered, (1,2) use one of the two
cross matchings (1a+2c,1c+2a), and the third edge is (hb) or
(rb).  These are the last four.  The displayed automorphisms give
exactly the stated orbits. \(\square\)

Every internal deletion or contraction in (O) unlocks one of these
twenty-five states by singleton transition polarity.  Thus (2.2), not
the forty-two-state pure-Moser atlas, is the exact state universe of the
full-singleton terminal.

## 3. Capacity at an endpoint-saturated rung

Let (xy\in E(O)).  Call (xy) an **endpoint-saturated alternating
rung** if

\[
 N_B(x)=B-\{1\},\qquad N_B(y)=B-\{2\}.             \tag{3.1}
\]

Contract (xy), six-colour the resulting proper minor, and write
(\alpha) for the colour of the contracted vertex.  Its boundary
state is a matching (M) in (2.2).  Put (s_i(M)=1) when (i) is a
singleton block of (M), and (s_i(M)=0) when (i) is paired.

### Theorem 3.1 (rung-capacity table)

If (M) has order (m\in\{2,3\}), then

\[
\begin{aligned}
 d_O(x)&\ge 6-\bigl((7-m)-s_1(M)\bigr),\\
 d_O(y)&\ge 6-\bigl((7-m)-s_2(M)\bigr).             \tag{3.2}
\end{aligned}

Equivalently,

\[
\begin{array}{c|c|c}
\text{state order}&i\text{ singleton}&i\text{ paired}\\ \hline
2&d_O(\text{endpoint missing }i)\ge2&d_O\ge1\\
3&d_O(\text{endpoint missing }i)\ge3&d_O\ge2.
\end{array}                                                     \tag{3.3}
\]

#### Proof

The contracted vertex is adjacent to all of (B), so its colour
(\alpha) is absent from (B).  The state (M) uses (7-m)
colours on (B).  Deleting (i) from the row loses one of those
colours exactly when (i) is a singleton block.  Hence

\[
 |c(N_B(x))|=(7-m)-s_1(M),
\]

and symmetrically for (y).  Apply contraction-state saturation

\[
 d_O(u)+|c(N_B(u))|\ge6
\]

at (u=x,y). \(\square\)

This table is invariant under replacing six by (r): at an
endpoint-saturated rung the lower bound is always (r) minus the number
of boundary colours actually visible at that endpoint.  Thus the
capacity calculation is not tied to the Moser labels.

## 4. Degree-two rungs export actual paths

The following is the useful operation-level part of the atlas.  It uses
the Kempe fan at the deleted edge, rather than merely recording the new
state.

### Theorem 4.1 (low-capacity transition path)

Suppose (3.1) holds and

\[
                         d_O(x)=d_O(y)=2.            \tag{4.1}
\]

Let (x'\ne y) and (y'\ne x) be their other neighbours in (O).

1. An unlocked order-three state must be one of

   \[
   hb+1a+2c,\ hb+1c+2a,\ rb+1a+2c,\ rb+1c+2a.       \tag{4.2}
   \]

2. For every state in (4.2), one may choose the colour of (d), say
   (delta), different from (alpha), and then

   \[
                         c(x')=c(y')=\delta.          \tag{4.3}
   \]

   Moreover (O-xy) contains an (alpha/\delta)-alternating
   (x)-(y) path whose first and last edges are (xx') and
   (y'y).  In particular, (xy) lies on an explicit cycle in (O).

3. If an unlocked order-two state leaves (1) singleton, then equality
   holds at (x) in (3.2) and

   \[
                         c(x')=c(1).                 \tag{4.4}
   \]

   The (alpha/c(1))-Kempe fan supplies an (x)-(y) path whose
   first edge is (xx').  The symmetric statement holds for a
   singleton (2) at (y).

#### Proof

For order three, (3.3) excludes every state in which (1) or (2)
is singleton.  The remaining four states are exactly (4.2).

They use four colours on (B).  Since both missing roots are paired,
each of the rows in (3.1) sees all four.  There are two colours absent
from (B).  Recolour (d), which has no neighbour outside (B), so
that its colour (delta) is the absent colour different from
(alpha).  Equality holds in contraction-state saturation at both
ends.  Its equality clause says that the sole internal neighbour other
than the opposite end has the unique non-(alpha) colour absent from
the boundary row.  This is (delta), proving (4.3).

Expand the contracted vertex to the equally coloured nonadjacent pair
(x,y) in (G-xy).  The edge-transition Kempe fan says that (x,y)
belong to one (alpha/\delta)-component.  Neither colour occurs on
(B).  The only vertex outside (B\cup O) is (d), and it has no
neighbour in (O); it is isolated from (x,y) in this bichromatic
subgraph.  Therefore a shortest connecting path lies wholly in
(O-xy).  Equation (4.3) forces its first and last edges.

For order two, (B) uses five colours and (alpha) is the unique
absent colour (also the colour which may be used on (d)).  If (1)
is singleton, (N_B(x)=B-\{1\}) sees the other four boundary colours.
Again equality holds in saturation, and its equality clause forces
(x') to have the fifth boundary colour (c(1)).  The deleted-edge
Kempe fan gives the claimed path.  The proof at (y) is identical.
\(\square\)

The conclusion in part 2 is stronger than non-bridgeness: it specifies
the two colours and the forced entry and exit of the replacement path.
It is the exact alternating rung which a subsequent carrier exchange
must use.

## 5. A genuine bottleneck is an exact seven-adhesion

The word “bottleneck” is sometimes used for a portal-order obstruction
which need not disconnect the shore.  For an actual bridge, however,
seven-connectivity gives a complete answer.

### Theorem 5.1 (bridge or state path)

Assume (G) is seven-connected.  Let (xy) be a bridge of (O), with
components (A\ni x) and (C\ni y) in (O-xy).  If

\[
 N_B(A)\subseteq B-\{1\},\qquad
 N_B(C)\subseteq B-\{2\},                         \tag{5.1}
\]

then

\[
 N_G(A)=\{y\}\cup(B-\{1\}),\qquad
 N_G(C)=\{x\}\cup(B-\{2\}).                     \tag{5.2}
\]

Thus both sides of the rung expose exact seven-cuts.  Consequently a
surviving alternating lock with no nested exact-adhesion exit has no
bridge separating its (1)- and (2)-portal sides.  If such a rung is
endpoint-saturated and has degree two at both ends, every order-three
transition instead gives the explicit internal detour of Theorem 4.1.

#### Proof

There is no edge from (d) to (O), and (xy) is the only
(A)-(C) edge.  Hence

\[
                         N_G(A)=\{y\}\cup N_B(A).
\]

Seven-connectivity gives (|N_G(A)|\ge7), while (5.1) gives the
reverse bound (|N_G(A)|\le1+6=7).  Equality proves the first
identity.  The other is symmetric. \(\square\)

The theorem is label-free in the following form: if a bridge side of a
full (k)-boundaried shore has defect at least one, ambient
(k)-connectivity makes a one-defect side with its bridge endpoint an
exact (k)-adhesion.

## 6. The independent rooted-(K_4) core and its exact completion test

Operation-criticality at the boundary edge (db) supplies a second,
independent object.  The four common neighbours

\[
                         \{a,c,1,2\}
   =\{a,1\}\mathbin{\dot\cup}\{c,2\}              \tag{6.1}
\]

are partitioned into two independent pairs.  The degree-free rooted-core
theorem in `hadwiger_degree9_hub_rainbow_rooted_k4.md`, applied to
(db), yields four pairwise adjacent disjoint connected bags

\[
                         K_1,K_2,K_3,K_4            \tag{6.2}
\]

in (G-\{d,b,a,c,1,2\}), each containing a distinct neighbour of
(b) in (O).  Thus ({b},K_1,ldots,K_4) is a controlled
(K_5)-model.

The following elementary criterion records exactly how this core can
finish the proof; it is useful when a transition path redistributes one
of the four boundary portal classes.

### Lemma 6.1 (rooted-core two-bag completion)

Let (Z=\{d,a,c,1,2\}).  If there is a partition
(Z=Z_0\mathbin{\dot\cup}Z_1) such that both induced sets are connected,
an edge joins them, and each (Z_j) is adjacent to every bag in (6.2),
then (G\succeq K_7).

It suffices to test the six choices

\[
 Z_1\in\bigl\{\{a\},\{c\},\{1\},\{2\},\{a,c\},\{1,2\}\bigr\},
 \qquad Z_0=Z-Z_1.                                  \tag{6.3}
\]

#### Proof

Use the seven bags

\[
                         K_1\mid K_2\mid K_3\mid K_4
                         \mid\{b\}\mid Z_0\mid Z_1. \tag{6.4}
\]

The first four form a clique model and each is adjacent to ({b})
through its prescribed (b)-portal.  The singleton (b) is adjacent
to every vertex of (Z), while the hypotheses give all remaining
adjacencies.  This proves (6.4).

The graph induced by (Z) consists of the vertex (d), complete to
the other four vertices, together with the two edges (ac,12).  In a
connected bipartition, the side not containing (d) may be reduced to
a connected nonempty set, hence to one of the six sets in (6.3);
enlarging either side only preserves its contacts. \(\square\)

Accordingly, a (K_7)-free singleton lock imposes a concrete
concentration condition on the rooted core: for every set in (6.3),
one of that set and its (d)-complement misses at least one of the four
rooted bags.  This is the finite contact obstruction on which the
transition paths of Theorem 4.1 must act.  It is strictly stronger than
the coarse inequality (|N_O(b)|\ge4), because the four (b)-portals
now lie in four mutually adjacent branch bags.

## 7. Exact residual

Theorems 2.1--5.1 close two genuine infinite subfamilies of the
full-singleton lock:

* every true alternating bridge descends through an exact seven-cut;
* every endpoint-saturated degree-two rung rejects half of the
  order-three atlas, while every surviving order-three operation creates
  a specified internal alternating detour.

The rooted-core criterion then turns any transition which distributes
the four boundary contacts across both sides of one of (6.3) into the
explicit (K_7)-model (6.4).

What is not proved here is that a minimal packet/crossed ladder must have
an endpoint-saturated degree-two rung, or that one of its transition
paths must satisfy Lemma 6.1.  A distributed lock may have all its
bottleneck vertices of larger shore degree and may route every
one-step Kempe detour through the same rooted-core bag.  That is now the
precise operation-level residue; the twenty-five states themselves have
been exhausted.
