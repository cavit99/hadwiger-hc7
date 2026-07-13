# Atomic forced-fan obstruction plus a covering crossing gives (K_7)

## 1. Reserved Moser setup

Use the pure Moser labels

\[
 a=1,qquad b=3,qquad U=\{0,2,4,5,6\},
\]

and let (w) be the sixth adhesion portal.  Suppose the (a)-shore
contains two adjacent outer-fan vertices (z_1,z_2) with a common
connected remainder (B), where:

1. (B) is adjacent to both (z_1,z_2);
2. for one ordinary Moser root profile (P), each (z_i) sees exactly
   (P\cup\{a,w\}) on the labelled boundary; and
3. (B\cup\{z_1,z_2\}) is full to (U\cup\{a,w\}).

Condition 3 implies that (B) sees every root of (U-P).  Contracting
(B) therefore gives a body vertex with those three conservative root
contacts.  Extra contacts may be deleted.

On the (b)-shore, suppose one Moser frame is crossed.  The connected
full-split extension from `hadwiger_full_split_cyclic_hull.md` enlarges its
two carriers to a connected bipartition

\[
 D_b=X\mathbin{\dot\cup}Y,
\]

where (X,Y) are adjacent, and their contact sets cover
(U\cup\{b,w\}).  Assign contacts in the overlap to obtain a disjoint
partition

\[
 P_X\mathbin{\dot\cup}P_Y=U\cup\{b,w\}
\tag{1.1}
\]

with the first crossing pair contained in (P_X) and the second in
(P_Y).

## 2. Atomic conversion theorem

### Theorem 2.1

Every configuration in Section 1 contains a (K_7)-minor.

### Finite core of the proof

There are five ordinary profiles, five Moser frames, and three unassigned
labels in (1.1).  Thus there are

\[
 5\cdot5\cdot2^3=200
\]

conservative quotients.  In each quotient retain:

* the pure Moser boundary and the apex (v);
* the contracted body (B);
* the two adjacent fan vertices (z_1,z_2); and
* the two adjacent contracted crossing pieces (X,Y).

For the body use only its three contacts in (U-P).  For (z_1,z_2)
use only (P\cup\{a,w\}).  For (X,Y) use the partition (1.1).  Every
one of these 200 graphs has seven explicit pairwise disjoint, connected,
pairwise adjacent branch sets.

The discovery program `fan_crossing_fullsplit_probe.py` writes one model
per cell to `fan_crossing_fullsplit_certificate.json`.  The independent
program `fan_crossing_fullsplit_verify.py` does not call a minor solver.  It
reconstructs all 200 conservative graphs, checks that the crossing contacts
form the required covering partition, and verifies for every archived
model:

1. seven nonempty pairwise disjoint bags;
2. connectivity of every bag; and
3. all twenty-one pairwise bag adjacencies.

It prints

```text
verified 200 atomic fan/full-split K7 certificates
```

Every quotient operation used above is a contraction of a connected set or
an edge/vertex deletion, so each certified model lifts to the original
graph.  This proves the theorem. \(\square\)

## 3. Consequence for the thirty residual transition states

Fix one of the thirty high-root/nonstar boundary states and a colour of the
common fan neighbour.  The forced-colour recurrence in
`hadwiger_fan_forced_colour_exchange.md` shows that the shortest possible
ordinary-profile obstruction is always

\[
 P,P,
\]

where both copies have the same singleton available colour.  Theorem 2.1
eliminates this atomic obstruction whenever the opposite shore is crossed.
The bilateral all-crossless theorem guarantees such an opposite crossing
when the current shore is all-crossless.

Thus no residual state can fail across an adjacent repeated ordinary
profile.  A surviving removable fan must use a genuinely mixed forced
chain, a triple lock, or expose a tight seven-adhesion.  This is a strict
structural reduction: repetition of the most basic list obstruction is
closed uniformly, at arbitrary fan length and for all thirty states.

## 4. Why a third portal-carrying piece is the next invariant

Distinct singleton-profile pairs are not all closed by the two-piece
quotient.  The first exact negative cell is

\[
 P_{02},P_{14},qquad
 \pi=06\mid14\mid25,qquad
 \text{crossing }06\mid25.

Its bad covering split assigns

\[
 P_X=\{0,3,6\},qquad P_Y=\{2,4,5,w\}.

However, splitting (Y) into two adjacent pieces, both adjacent to (X),
and moving either label (4) or (w) to the third piece immediately gives
a (K_7)-model.  This is replayed by
`fan_split_repair_single_probe.py`.

Hence the surviving geometry is not merely “three connected pieces.”  It
requires every surplus piece to be portal-free, or all free portal labels
to remain locked in one crossing carrier.  Seven-connectivity then points
to the alternative already isolated by the full-split theorem: a nested
tight adhesion.  Proving this portal-carrying-piece dichotomy for every
mixed forced chain is the remaining conversion step.
