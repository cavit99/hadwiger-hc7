# A portal-preserving splitter for the all-crossless pentagram web

## 1. Setting

Let (D) be a simple three-connected relative shore with fixed labelled
boundary

\[
 L=U\mathbin{\dot\cup}\{w,a\},\qquad |U|=5,
\]

such that (D) is full to (L) and

\[
 \phi_D(X):=|N_D(X)-X|+|N_L(X)|\ge7
 \tag{1.1}
\]

for every nonempty proper (X\subsetneq D).  The missing-edge graph on
(U) is a (C_5).  Assume that each of its five disjoint-edge frames is
crossless in (D).

When an internal edge (xy) is contracted, parallel edges are suppressed,
the new vertex receives the union of the (L)-neighbourhoods of (x,y),
and the labels in (L) are not changed.

## 2. What contraction preserves

### Lemma 2.1 (crosslessness lifts through contraction)

If (D) is crossless for a fixed frame, then (D/xy) is crossless for the
same frame.

### Proof

Suppose (D/xy) contains disjoint connected supports (A',B') for the two
root pairs, and let (z) be the contracted vertex.  At most one of
(A',B') contains (z).  A support avoiding (z) lifts unchanged and
avoids both (x,y).  In a support containing (z), replace (z) by the
connected pair ({x,y}).  Every incident support edge lifts to an edge
incident with at least one of (x,y), and every portal label incident with
(z) was incident with at least one of them.  Thus the lifted set is
connected and has the required root contacts.  The two lifted supports are
still disjoint, contradicting crosslessness in (D). \(\square\)

Consequently contracting an internal edge preserves all five crossless
frames.  Fullness is also preserved, since portal rows are replaced by
their union.

### Lemma 2.2 (only a tight seven-cut can destroy (1.1))

Let (xy\in E(D)).  If (D/xy) violates (1.1), then there is a nonempty
proper set

\[
 Y\subseteq D-\{x,y\}
\]

such that

\[
 \phi_D(Y)=7,\qquad x,y\in N_D(Y).
 \tag{2.1}
\]

After contraction the corresponding boundary has order six.

### Proof

This is the exact preimage calculation.  A violating set containing the
contracted vertex lifts to a set containing both (x,y), with identical
boundary, contradicting (1.1).  A violating set avoiding the contracted
vertex is a set (Y\subseteq D-\{x,y\}).  Its boundary changes only when it
sees both ends of the edge; then two distinct boundary vertices become one,
so the order drops by exactly one.  Hence (2.1) is necessary and sufficient.
\(\square\)

## 3. The splitter

### Theorem 3.1 (safe contraction or exact seven-cut)

Assume (|D|\ge7).  Then at least one of the following holds.

1. There is an internal edge (xy) such that (D/xy) is
   three-connected, full to (L), satisfies (1.1), and remains
   all-crossless.
2. There is a three-connectivity-preserving contractible edge (xy) and a
   tight witness (Y) satisfying (2.1).

In outcome 2, if (1.1) is inherited from a seven-connected ambient graph,
every component (K) of (D[Y]) is a full shore for the exact order-seven
boundary

\[
 T=(N_D(K)-K)\mathbin{\dot\cup}N_L(K).
 \tag{3.1}
\]

### Proof

Tutte's contractible-edge theorem gives an edge (xy) for which the
simplification of (D/xy) is three-connected; the order assumption keeps
at least six vertices after contraction.  Lemma 2.1 and row union preserve
all-crosslessness and fullness.  If (1.1) is preserved, outcome 1 holds.
Otherwise Lemma 2.2 gives outcome 2.

For the last assertion, the external neighbourhood of a component (K) of
(D[Y]) is contained in the seven-set in (3.1).  Seven-connectivity forces
equality; otherwise a set of at most six vertices separates (K). \(\square\)

This is a genuine portal splitter: absent an exact new seven-adhesion, it
reduces the all-crossless three-connected society by one vertex without
losing any of its five frame obstructions.

## 4. Exact critical-state exchange on a safe edge

Now suppose (D) is the (a)-side shore in a proper-minor-minimal
counterexample (G) to (mathrm{HC}_7).  Keep the full local boundary

\[
 L=S\cup\{a\},qquad S=U\cup\{w\},
\]

and write \(\mathcal E(D)\) for the exact six-colour extension family on
(L).

### Lemma 4.1 (terminal-aware contraction transition)

For every internal edge (xy\in E(D)), there is a boundary state

\[
 \pi_{xy}\in\mathcal E(D/xy)-\mathcal E(D).
 \tag{4.1}
\]

In particular, no internal contraction is extension-family-preserving.

### Proof

The proper minor (G/xy) has a six-colouring (c).  Its restriction to
(L) is a state (pi_{xy}\in\mathcal E(D/xy)).  If this state extended to
the original (D\cup L), keep (c) on (G-D) and use that extension on
(D\cup L).  The colourings agree on (L), and every edge leaving (D)
ends in (L); hence they would six-colour (G).  This is impossible, so
(pi_{xy}\notin\mathcal E(D)). \(\square\)

The proof retains (v,b) and the opposite shore, so it does not lose the
apex-star information by pretending that (S) alone is the boundary.

### Corollary 4.2 (exact decorated-state alternative)

For the safe edge in outcome 1 of Theorem 3.1, either its new state
(pi_{xy}) is a decorated (T)-state, or it has one of the following two
explicit defects:

1. (U) uses at least four colour classes; or
2. the colour class of (a) meets (U).

### Proof

If (U\) uses exactly three colours, every proper three-colouring of the
present (C_5=G[U]) has class sizes (2,2,1).  The two two-vertex classes
are disjoint missing-cycle edges.  If the (a)-class is disjoint from
(U), it is the star block.  The portal (w) either joins one of these four
independent blocks or is a singleton.  This is exactly one of the decorated
(T)-states.  The negation gives the two displayed defects. \(\square\)

Thus the general all-crossless critical web has the following rigorous
trichotomy:

\[
 \boxed{\text{tight seven-adhesion}}
 \quad\text{or}\quad
 \boxed{\text{new decorated }T\text{-state}}
 \quad\text{or}\quad
 \boxed{\text{new high-root/nonstar state}}.
\]

The last box is the exact residue; it may not be silently identified with a
decorated (T)-state.

For the labelled pure Moser spindle this residue has a complete finite
description. The colour of \(v\) is absent from its seven-vertex
neighbourhood, and \(\alpha(N(v))\le2\). Hence the nonsingleton colour
classes on \(N(v)\) form a matching of order two or three in the ten-edge
complement of the Moser spindle. There are exactly 42 such matchings. With
\(a=1,b=3\) and \(U=\{0,2,4,5,6\}\), they split as follows:

\[
\begin{array}{c|r}
\text{local trace type on }a\cup U&\text{number}\\ \hline
\text{decorated-\(T\) trace}&12\\
a\text{ shares a \(U\)-colour, }|c(U)|=3&2\\
a\text{ shares a \(U\)-colour, }|c(U)|=4&13\\
a\text{ shares a \(U\)-colour, }|c(U)|=5&4\\
a\text{ is separate, }|c(U)|=4&11.
\end{array}
\]

The dependency-free enumeration
moser_safe_transition_state_probe.py prints all 42 matchings and asserts
these counts. Thus 12 of the 42 possible contraction witnesses immediately
give the desired local \(T\)-trace; the other 30 are the exact
high-root/nonstar target for a Kempe or opposite-shore exchange.

## 5. Why arbitrary contraction-chain pumping is invalid

Lemma 4.1 concerns a one-step operation on the original critical graph.
After the first contraction the resulting graph is already a colourable
proper minor.  If a chain

\[
 D=D_0\to D_1\to D_2\to\cdots
\]

has \(\mathcal E(D_i)=\mathcal E(D_j)\) for (0<i<j), that equality does
not extend a colouring back across (D_0) unless it also equals
\(\mathcal E(D_0)\).  Therefore finite-state pigeonholing along an arbitrary
contraction chain is not justified.

The separate linked-annulus pumping theorem remains valid because the two
equal-state boundaries occur simultaneously as nested replaceable regions
inside the original graph, with clean label-preserving paths through the
annulus.  That retained-shell hypothesis is precisely what an arbitrary
successive contraction chain lacks.

## 6. Why linkage density is not the replacement invariant

The complementary branch to the all-crossless web is not solved merely by
counting linked frames.  The exhaustive falsification probe
`moser_three_frames_rooted_k5_probe.py` already finds an order-six
three-connected shore satisfying every relative inequality (1.1) (with
the two omitted labels complete to the shore) in which all five frames are
linked but there is no rooted (K_5)-model on the five Moser roots.  One
small witness has shore

\[
 D=K_6-\{14,25\}
\]

and the five roots use the distinct portals (0,1,4,2,5).  The verifier
checks both the five two-linkages and every allocation of shore vertices to
five rooted branch sets.

This witness is not asserted to be a counterexample-derived shore; in
particular it does not impose the ambient target-minor exclusion or the
one-step transition axiom of Lemma 4.1.  Its role is exact: the next
structural lemma must use one of those two hypotheses.  Replacing the
critical exchange by the bare assertion "at least three frames are linked"
is false even at the minimum permitted shore order.
