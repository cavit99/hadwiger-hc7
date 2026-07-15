# Independent audit: tight-gate packet analysis and receiver localization

**Verdict:** GREEN for the revised certificate-level claims.

The earlier accepted-`S3` and ranked-`S4` claims were RED.  The revised
source removes them and retains only packet-one-side regeneration,
packet-vector arithmetic, high-demand/state-labelled certificates, and
receiver-lock localization.

**Audited source:** `active/hc7_tight_gate_receiver_normalization.md`

**Source SHA-256:** `801a68a1c050e13d83101bd3585463f124f572af1ea33a36be1d32514cf2110a`

## 1. Audited entry and packet orientation

The tight-lobe input is used correctly.  It gives an actual separation

\[
        V(G)=D\mathbin{\dot\cup}\Omega\mathbin{\dot\cup}B,
        \qquad |\Omega|=7,
\]

with every component of either open shore `Omega`-full.  The exact-seven
packet theorem therefore gives packet vectors `(1,1)`, `(1,2)`, or
`(1,3)`, up to orientation.  It does not orient the packet-one shore at
the strict lobe `D`.  The source correctly recognizes this at the start of
Section 2.

The `(1,3)` branch is closed by the audited adaptive packet-reflection
theorem, symmetrically in the two shores.  The clique bounds in (3.6) are
also the correct specializations of
`omega(H)<=6-(nu_D+nu_B)`.

## 2. Lemma 2.1 is GREEN

If an open shore `L` has packet number one, it is connected: two open-shore
components would themselves be disjoint full packets.  It is full, so a
literal `L-Omega` edge exists.  Contracting such an edge toward its
boundary endpoint preserves all seven boundary labels and leaves the
opposite closed shore intact.

If the returned state had demand at most the opposite packet number `q`,
exact packet reflection with those `q` packets would construct an intact
colouring of the contracted shore with the same exact boundary partition.
It would align with the intact opposite-side restriction and glue.  Thus
the strict inequality `d_H(Pi_g)>q` is valid.  No old `S`-full packet is
mistaken for an `Omega`-full packet.

This lemma regenerates a named state on the actual packet-one side.  It
does not say that this side is the strict lobe or that the state has any
prescribed block structure.

## 3. Revised `(1,2)` certificate is GREEN

For packet vector `(1,2)`, Lemma 2.1 validly gives a named state of demand
at least three on the actual packet-one side.  Two further claims do not
follow.

First, in the orientation

\[
                         (\nu_D,\nu_B)=(2,1),
\]

regeneration occurs on `L=B`.  The marked strict lobe `D subsetneq A` is
then the packet-two shore.  Marking that smaller set does not make the
actual active packet-one shore smaller, and supplies no decreasing
packet-one-shore rank.

Second, in either orientation, `d_H(Pi_g)>=3` only says that the returned
state cannot be reflected by the two opposite packets.  It does not make
`Pi_g` the accepted paired-triangle or attained-duty state required by the
active `S3` receiver.  No audited theorem identifies an arbitrary
high-demand partition with that state language.

Therefore outcome 2 of Theorem 3.1 is proved exactly as a **regenerated
high-demand `(1,2)` certificate**.  The revised source now distinguishes
the two orientations, makes no active-shore claim when `L=B`, and does not
call the arbitrary high-demand state an accepted `S3` state.  Its scoped
claim is valid.

## 4. Revised `(1,1)` certificate is GREEN

For `(1,1)`, the following facts are valid:

* the named state has demand at least two;
* it is intact on the `B` side and attained through the named contraction
  on the `D` side;
* the local packet sum is two, compared with three in the old atomic cell;
* the common old labels `T_D` are retained and the equally sized gate set
  `Z_D` replaces `S-T_D` as a literal set substitution.

These facts do not define a ranked `S4` handoff.  Packet-sum `3 -> 2` is a
one-step stratum change, not a well-founded rank under later receiver
normalizations.  A later transition may reorient the shores.  The strict
set inclusion `D subsetneq A` does not prevent that reversal.  Moreover,
the simultaneous set substitution in (3.5) has no canonical pairing of
lost labels with new gates and has not been factored into legal
single-root transitions.  The existing twin-cell audit explicitly warns
that even a single-root exchange can be involutive without a separate
receiver rank.

Outcome 3 is therefore exactly a **state-labelled `(1,1)` certificate**,
not a normalized ranked `S4` receiver.  The revised theorem and scope say
this explicitly, so the claimed certificate is valid.

## 5. Theorem 4.1 is GREEN

In the colouring of `G-f`, strong criticality gives a global
`gamma-eta` lock between the equal-coloured ends `d,q`.  If `q` is absent
from the component containing `d` in the `D` closed shore, swapping that
component restores `f` and toggles exactly
`U_eta=K_eta^D intersect Omega` on the boundary.

On the intact `B` closed shore, if no bichromatic component meets both
`U_eta` and its complement, swapping every component which meets `U_eta`
toggles exactly the same boundary set.  The two intact colourings then
glue.  Otherwise a shortest path in a crossing component has distinct
boundary ends in the two displayed sets and no internal boundary vertex,
so all internal vertices lie in `B`.  This proves the internal-lock or
opposite-crossing alternative for each of the five other colours.  The
argument remains valid when `f` is a boundary-incidence edge.

The five alternatives are useful receiver data, but they do not by
themselves supply a decreasing rank or resolve all future transitions.

## 6. Scope and remaining theorem

The revised source has made all four required scope repairs: it distinguishes
the two `(1,2)` orientations, removes arbitrary-state `S3` acceptance,
renames the `(1,1)` outcome as a certificate, and states that no
well-founded `S4` rank has been proved.

The remaining research obligation is not part of this theorem: convert the
regenerated `(1,2)` state to the accepted `S3` language while preserving a
decreasing active orientation, or factor/resolve the `(1,1)` boundary
substitution with a declared rank that cannot reverse through later
lock/crossing transitions.  The revised source does not claim otherwise.
