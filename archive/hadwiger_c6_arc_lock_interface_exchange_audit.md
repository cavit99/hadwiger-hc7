# Audit of the cyclic arc interface exchange

## Verdict

The following parts of
`hadwiger_c6_arc_lock_interface_exchange.md` are sound.

1. Strict surplus gives an interface two-matching or a singleton hub.
2. In a minimum \(k\)-fragment, exposure defect \(q\) amplifies to an
   interface matching of order \(q+1\).
3. Deleting one of two independent interface edges preserves the
   covering split and creates a strict boundary state.
4. Every edge colour has either a retained-interface Kempe route or an
   outside exposure connector, and different colour-connectors overlap
   only in alpha-coloured vertices.
5. The forty-state boundary census and the sixteen displayed quotient
   models replay exactly.

The connector models require a clean lift: their new branch set must be
disjoint from the two reserved helper branch sets. The source note now
states this explicitly. No conclusion about an arbitrary dirty Kempe
path is valid without a detachable-helper argument.

## 1. Interface matching proof

If a bipartite interface has matching number one, Kőnig gives one common
endpoint. The opposite endpoint set is a singleton, so strict surplus
forces external exposure at least \(k\). Deleting the common endpoint
from the low-exposure side leaves any remaining component behind a cut
of order at most \(k-1\). This proves the singleton-hub alternative.

For the atomic amplification, a matching of order \(m\le q\) has a
vertex cover \(C\) of order \(m\). A component left after deleting
\(C\) from one side has all neighbours in \(L_i\cup C\), of order at
most \(k-q+m\le k\). Order below \(k\) violates connectivity; order
\(k\) is a fragment smaller than the chosen minimum fragment. Hence the
whole split lies in \(C\), impossible because a graph on \(m\) vertices
cannot have a matching of order \(m\).

The matching-three application is only for a type O split which itself
is the chosen minimum fragment and has two five-vertex exposures. In
type A, the old-arm neighbour enlarges an exposure and the split arm is
not automatically the whole minimum fragment.

## 2. Colour-state proof

For an interface edge \(xy\), every six-colouring of \(G-xy\) has
\(c(x)=c(y)=\alpha\). For every other colour \(\gamma\), the two ends
lie in one alpha/gamma component; otherwise a Kempe switch at one end
restores the edge. A simple path in this component either uses another
interface edge or has a last-exit/first-entry subpath outside the split.

If a component stays on one side, it must be anchored at that side's
external exposure. Otherwise switching the component fixes \(xy\).
This proves the palette-or-excursion and coloured portal-fan statements.

The dependency-free script `c6_arc_lock_palette_census.py` enumerates
the forty proper equality states of \(K_1\vee C_6\) using at most six
colours. Exactly two states allow alpha to be absent from both antipodal
five-vertex rows:

\[
0123124,\qquad0123214,
\]

with the sixth colour absent.

## 3. Certificate lift boundary

`c6_arc_cross_connector_verify.py` checks sixteen quotient models:
eight cross-exclusive pairs and eight long common-root pairs, in helper
geometries O and A. Every bag is checked for disjointness, connectivity,
and pairwise adjacency.

For a graph-theoretic lift, however, the connector support \(R\), the
two split pieces, and the two helper preimages must be five pairwise
disjoint connected sets. If \(R\) runs through a helper preimage, the
quotient certificate would use that helper twice. The corrected source
therefore proves:

* a clean connector is positive;
* a dirty connector is positive only when its helper passage is
  detachable while a connected residue retains all required helper
  contacts.

This is the same trust boundary as the clean-gate/locked-core theorem.

## 4. Exact residual

Inside a type O minimum-fragment antipodal lock, the interface has a
three-matching. For any deleted interface edge, the remaining obstruction
is one of:

1. two differently coloured retained interface routes;
2. a clean two-connector \(z\)-fan with both exclusive ends in the same
   arc; or
3. a dirty helper-core path for which no detachable helper arm has yet
   been proved.

The note does not claim that these three configurations are impossible.
In particular, the static same-arc connector quotient is negative, so
the final proof must retain actual portal placement inside the
three-rung interface or open the dirty helper core.

## 5. Block-capacity audit

The exceptional nested dirty passage is not an arbitrary one-defect
quotient.  After normalization its retained helper misses the common
root (c_0), while the peeled passage meets (c_0,c_1,c_5) and that
helper.  In both helper geometries, any additional passage contact at
(c_2,c_3), or (c_4) gives one of six explicit (K_7)-models.
`c6_arc_block_capacity_verify.py` independently checks those models;
it does not invoke a minor solver.  Thus the allowed boundary contacts
of the passage lie in the four-label block
({c_5,c_0,c_1,z}), or its half-turn.

The ensuing block-capacity theorem is a direct connectivity argument,
not a computational extrapolation.  If a connected passage (A) has
a nonempty far side and every forbidden boundary contact creates the
target minor, then in a target-minor-free (k)-connected graph its
nonboundary gate set has order at least (k-|Z|).  Equality with full
block contact is an exact (k)-adhesion.  If (A) is properly inside
a chosen minimum (k)-fragment, equality would make (A) a smaller
(k)-fragment and is impossible.

For (k=7) and (|Z|=4), this rigorously eliminates every normalized
one-defect nested dirty passage with at most two nonboundary gates.  A
three-gate passage is necessarily an exact-cut outcome; inside the
selected minimum fragment even that outcome is excluded, leaving only
a helper core with at least four nonboundary gates.  A retained helper
with further portal defects is outside the six certificates.  Thus the
result eliminates an infinite gate-width family but does not yet
eliminate either the four-gate core or the multi-defect portal lock, and
must not be quoted as closure of the complete arc lock.

There is also a sharp obstruction to the tempting next inference
“nondetachable portal passage implies a separator whose order is bounded
by the number of portal classes.”  In an \(m\times3\) grid, take the
middle column as the passage and the two outside columns as two portal
classes.  The passage cannot be removed while retaining a connected
representative of both classes, yet the \(m\) disjoint horizontal rows
force every class-separating vertex set to have order at least \(m\).
Any bounded-adhesion conclusion must therefore use contraction-critical
state transitions or further ambient branch-set structure.
