# Boundary-relative audit of the 2026 D-reducibility route

## 1. Verdict

The following proposed inference is **not valid** for ordinary
D-reducibility:

> a D-reducible configuration sufficiently far from a society cycle
> can be deleted without changing the full set of colourings which
> extend from that cycle.

The obstruction is built into the definition.  D-reducibility permits
Kempe changes in the entire coloured exterior of the configuration.
Those Kempe components can meet a remote society boundary, and the
resulting repair is allowed to change its colouring.  Distance from the
configuration to the society boundary gives no bound on the diameter
of a Kempe component.

There is nevertheless a precise useful replacement.  A
**society-relative D-reduction**, whose improving Kempe changes fix the
society boundary, preserves the full extension set.  Finding even one
such occurrence would contradict the boundary minor-switching property
of a critical web.  The 2026 theorem does not supply this relative
property.

## 2. What the primary theorem actually says

The definitions and theorem used here are from Inoue, Kawarabayashi,
Miyashita, Mohar, Thomassen and Thorup,
[The Four Color Theorem with Linearly Many Reducible Configurations and
Near-Linear Time Coloring](https://arxiv.org/pdf/2603.24880), Sections
2.1 and 3.1.

For a configuration (Z), let (R) be the ring of its free
completion.  A 4-colouring of (R) is *0-extendible* if it extends
directly across (Z).  Recursively, it is (i)-extendible if, in every
plane exterior containing (R) as a facial cycle and from every
exterior colouring inducing the ring state, one Kempe change produces
an ((i-1))-extendible ring state.  A configuration is D-reducible when
all ring colourings have some finite level.  The configurations in the
paper have level at most 25.

Three distinctions are decisive.

1. The improving Kempe change is made in the whole exterior.  It is
   not required to avoid, or even preserve, a second designated cycle.
2. Theorem 3.3 is a dichotomy: it returns either linearly many
   non-touching induced D-reducible configurations **or** linearly many
   noncrossing obstructing cycles.  The configuration outcome is not
   unconditional.
3. In the algorithm, the configurations are deleted and the empty
   rings are triangulated using new auxiliary edges.  Thus the graph
   recursively coloured by the algorithm is generally not a minor of
   the original graph.  Deleting a single configuration is a minor
   operation, but the colouring of that deletion need not extend back
   with the same society state.

The paper emphasizes the global point explicitly: each improving Kempe
change may affect most of the graph.  This globality is essential to
ordinary D-reducibility, not an artefact of its proof.

The paper also defines C-reducibility using contractions in the free
completion.  Those contractions are minor operations when loopless,
but restoration still uses Kempe changes in the original exterior.
Consequently C-reducibility does not provide society-state preservation
either.

## 3. Exact extension-set statement

For a plane society ((Q,C)), write

\[
 \operatorname{Ext}(Q,C)
 =\{\psi:V(C)\to[4]:\psi\text{ extends to a proper
 4-colouring of }Q\}.
\]

Suppose that (Z\subseteq Q-V(C)) is an induced occurrence of a
D-reducible configuration.  Deletion always gives

\[
 \operatorname{Ext}(Q,C)
 \subseteq \operatorname{Ext}(Q-V(Z),C).             \tag{3.1}
\]

Ordinary D-reducibility supplies only the following orbit statement.
For every full colouring of (Q-V(Z)), some sequence of improving
Kempe changes changes its ring state to one which extends across (Z).
The restriction of the resulting full colouring to (C) may differ
from the original restriction.  Thus every exterior colouring can be
moved to an extendible exterior colouring in its Kempe-reachability
class, but (3.1) need not be equality.

There is one immediate positive case.

### Lemma 3.1 (level-zero configurations preserve every boundary state)

If every colouring of the ring of (Z) is 0-extendible, then

\[
 \operatorname{Ext}(Q,C)
 =\operatorname{Ext}(Q-V(Z),C).
\]

#### Proof

Let a colouring of (Q-V(Z)) extend a state \(\psi\) on (C).  Its
restriction to the ring extends directly through the free completion
of (Z).  Combining the two colourings restores (Z) without changing
any exterior vertex, in particular without changing (C).  The reverse
inclusion is (3.1). \(\square\)

This is *level-zero* reducibility.  It should not be confused with the
notation \(\mathcal D_0\) in the 2026 paper, which denotes Steinberger's
subcollection of D-reducible configurations and does not mean that its
members have reducibility level zero.

## 4. A strict five-boundary counterexample

Ordinary D-reducibility does not imply equality in (3.1), even for the
simplest D-reducible configuration and a boundary of order five.

Let

\[
 C=c_0c_1c_2c_3c_4c_0.
\]

Inside (C), add a vertex (z) adjacent to
(c_0,c_1,c_2,c_3), and a vertex (w) adjacent to
(z,c_0,c_3,c_4).  This is a triangulated disk: its seven inner faces
are

\[
 zc_0c_1, zc_1c_2, zc_2c_3,
 wc_0z, wz c_3, wc_3c_4, wc_4c_0.
\]

In particular (C) is an **induced** outer 5-cycle.  The singleton
(w), of degree four and with ring (c_0zc_3c_4c_0), is the
D1-reducible configuration of Lemma 2.1 of the 2026 paper.

If a sphere triangulation is desired, put one further vertex (x) on
the other side of (C) and join it to all five vertices of (C).
The resulting graph is simple, every face is a triangle, and (C)
remains induced.

Consider the boundary colouring

\[
 (\psi(c_0),\psi(c_1),\psi(c_2),\psi(c_3),\psi(c_4))
 =(1,2,1,3,2).                                      \tag{4.1}
\]

It extends after deleting (w): the neighbours of (z) on (C)
use precisely colours (1,2,3), so (z) receives colour (4).  In
the spherical version, (x) may also receive colour (4).  Hence

\[
 \psi\in\operatorname{Ext}(Q-w,C).
\]

But (z) is forced to colour (4) by the fixed boundary state, while
the other three neighbours (c_0,c_3,c_4) of (w) receive colours
(1,3,2).  Thus the four neighbours of (w) receive all four colours,
so no colour is available for (w).  Therefore

\[
 \psi\notin\operatorname{Ext}(Q,C).
\]

This remains a counterexample if boundary states are taken modulo a
global permutation of the colour names: restoring (z) requires a
change in the equality partition on (C), not merely a renaming.

Thus deletion of an induced D1-reducible configuration can strictly
enlarge the full extension set on an induced five-cycle society
boundary, even inside a sphere triangulation.

## 5. Why geometric remoteness does not repair the implication

The preceding strict example is deliberately minimal and has the
configuration adjacent to (C).  The mechanism responsible for the
failure is not local, however.

Let the degree-four configuration have ring

\[
 R=r_0r_1r_2r_3r_0
\]

coloured (1,2,3,4) in cyclic order.  In an annular exterior, attach a
path of arbitrary length from (r_0) to a vertex of (C), coloured
alternately (1,3), and keep it in the same ({1,3})-Kempe
component as (r_0) but not (r_2).  The standard improving move for
the degree-four configuration swaps that component, makes (r_0) and
(r_2) equal, and hence frees a colour for the centre.  The very same
move changes the endpoint on (C), no matter how long the annulus is.
Four disjoint radial tethers may analogously be attached to the four
ring vertices for the two complementary opposite-colour pairs.

This example is not claimed to rule out the existence of some
different boundary-fixing Kempe sequence in every such annulus.  It
establishes the point needed for the audit: the D-reducibility
certificate itself has no locality conclusion, and a configuration at
arbitrarily large graph distance can have an improving Kempe component
which reaches and changes (C).  A proof that some alternative
boundary-fixing repair always exists would be a new theorem, not a
consequence of D-reducibility or of distance.

Nor does the presence of linearly many pairwise non-touching
configurations immediately fix this.  One bicoloured Kempe component
can meet the rings of linearly many non-touching configurations.  The
paper's simultaneous algorithm is designed precisely to allow such
global components.  Moreover, unless boundary degree is separately
bounded, pairwise non-touching configurations need not yield a
configuration at large distance from a fixed boundary: many disjoint
local pieces may attach through different sectors at one high-degree
boundary vertex.

## 6. The exact replacement lemma

The useful notion is relative to the selected occurrence and society,
not merely to the abstract configuration.

### Definition 6.1 (C-relative D-reducibility)

An occurrence (Z\subseteq Q-V(C)) is **C-relative D-reducible** if,
for every 4-colouring of (Q-V(Z)), there is a sequence of Kempe
changes which fixes every vertex of (C) and leaves a ring state that
extends across (Z).

It is enough, but not necessary, that every swapped Kempe component be
disjoint from (C).

### Lemma 6.2 (relative reduction preserves the complete extension set)

If (Z) is C-relative D-reducible, then

\[
 \operatorname{Ext}(Q,C)
 =\operatorname{Ext}(Q-V(Z),C).
\]

#### Proof

Start from any extension of \(\psi\in\operatorname{Ext}(Q-V(Z),C)\).
Apply the boundary-fixing sequence in Definition 6.1, then extend the
resulting ring state through (Z).  The final colouring still restricts
to \(\psi\) on (C).  This proves the reverse inclusion in (3.1).
\(\square\)

### Corollary 6.3 (critical-web consequence)

Suppose a critical planar side has the one-step boundary
minor-switching property: every proper internal vertex deletion or
edge deletion/contraction strictly creates a boundary state compatible
with the opposite side.  Then it contains no C-relative D-reducible
configuration disjoint from (C).

Indeed, Lemma 6.2 gives

\[
 \operatorname{Ext}(Q,C)
 =\operatorname{Ext}(Q-V(Z),C).
\]

For any (z\in V(Z)), monotonicity under deletion sandwiches

\[
 \operatorname{Ext}(Q,C)
 \subseteq\operatorname{Ext}(Q-z,C)
 \subseteq\operatorname{Ext}(Q-V(Z),C).
\]

All three sets are therefore equal, so even the one-step deletion of
(z) creates no boundary state.  This contradicts one-step
minor-switching directly.

This corollary is the valid version of the hoped-for contradiction.
Its missing hypothesis is exactly the boundary-relative repair.

## 7. Consequences for the critical-web programme

The 2026 theorem remains relevant, but not through the proposed direct
inference.  A viable use must prove at least one of the following new
statements.

1. **Relative occurrence theorem.**  In the configuration outcome of
   Theorem 3.3, one occurrence is C-relative D-reducible.  Ordinary
   non-touching and distance do not establish this.
2. **Boundary-preserving simultaneous theorem.**  For every fixed
   extendible state on the society (C_5), a nonempty subfamily of the
   configurations can be restored by simultaneous Kempe changes which
   preserve the equality partition on (C_5).
3. **Obstructing-cycle lift.**  In the second outcome of Theorem 3.3,
   one short obstructing cycle lifts, after accounting exactly for
   protected-boundary exposure, to a separator forbidden by
   contraction-critical connectivity or to an already solved portal
   split.
4. **Direct level-zero subfamily.**  Prove that the relevant planar
   web contains a level-zero configuration.  The 2026 theorem only
   guarantees D-reducibility of level at most 25 and gives no such
   subfamily conclusion.

The first two are genuinely boundary-aware Four Color reducibility
theorems.  They cannot be replaced by the assertion that a reducible
configuration is geometrically remote.

## 8. Final strategic conclusion

The attempted shortcut is refuted at the exact point where ordinary
D-reducibility is substituted for extension-set preservation.  The
minor-critical switching programme can still use reducibility, but its
next target must explicitly control Kempe components relative to the
Moser (C_5) boundary.  The strongest clean target is:

> **Relative reducibility target.**  In every residual four-palette,
> high-exposure, boundary-minimal critical (C_5) web, either there is
> a C-relative D-reducible occurrence, or there is a short web
> separator whose lift has order below the ambient connectivity.

This packages the two outcomes required by the 2026 theorem in a form
that would interact with the already proved minor-switching and
separator machinery.  It is a new missing lemma; it is not contained in
the Four Color reducibility theorem itself.
