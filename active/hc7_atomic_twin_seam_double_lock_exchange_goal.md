# Active goal: atomic twin-seam double-lock exchange

**Status:** immediate theorem target, not proved.

## 1. Strategic decision

The literal gate geometry is no longer the bottleneck.  The audited
two-gate and three-gate normal forms reduce every nonterminal gate to one
symmetric seam: two connected lobes have five old-boundary contacts each,
their contact sets overlap in three labels, and they meet through two or
three literal gates.

The next goal is to **close that seam**, not to enumerate its portal orders.
The proof must couple the two named proper-minor operations already present
in the counterexample:

\[
                         e=zu,
 \qquad                   f=dt\quad(d\in D, t\in Z).   \tag{1.1}
\]

The [crossed-state theorem](../results/hc7_atomic_twin_seam_crossed_states.md)
shows that the two operations disagree simultaneously on both actual
seven-boundaries.  The change need not be confined to their common
five-set.  The missing mathematics is therefore a double-lock exchange,
not another equality-partition census.

The unrestricted linkage obstruction is now eliminated uniformly.  The
[two-named-edge theorem](../results/hc7_atomic_two_named_edge_disjoint_cycles.md)
shows that deleting `e,f` leaves a five-connected nonplanar graph and hence
a literal `K_4` model rooted at `z,u,d,t`.  The remaining problem is to
allocate that rooted core relative to the twin boundaries and exact response
states; another Two-Paths/web analysis in the whole host is unnecessary.

The audited
[packet-transfer theorem](../results/hc7_atomic_twin_seam_packet_transfer.md)
now removes a separate arithmetic ambiguity.  Unless a twin is terminal
`(1,3)` or yields a literal, strictly smaller, named high-demand `(1,2)`
lobe certificate, both twin vectors are `(1,1)`.  The strict certificate
does not automatically preserve the old paired state, so it is an accepted
global handoff only after the receiving spine supplies a noncycling rank.
The local double-lock decoder should therefore be proved first in the
simultaneous `(1,1)/(1,1)` residue without forgetting that receiver
qualification.

There is one exact rank boundary.  If the source `A` is chosen globally
minimum among **all** packet-one shores of actual oriented `(1,2)`
seven-separations, the strict lobe-oriented `(1,2)` handoff is impossible,
regardless of its new equality state.  This cannot be assumed after
minimizing only inside the paired/twin subclass, and it does not rank a
`(1,1)` receiver or a near-model rotation.

Bare alignment has already been falsified by a `K_7`-minor-free shell in
which the contraction is clean on the common five-set.  That shell contains
the permitted rooted `K_5`.  Consequently the terminal-model alternative
is logically indispensable; the proof should select the one
response-matched lock determined by a contraction colouring before asking
for broader lock structure.

## 2. Frozen input

Use the atomic connected-bipartite kernel and the notation of the
[literal two-gate normal form](../results/hc7_atomic_literal_two_gate_transition.md):

\[
 |T_D|=|T_E|=5,qquad T_D\cup T_E=S,qquad |T_D\cap T_E|=3,
\]

\[
 \Omega_D=Z\mathbin{\dot\cup}T_D=N_G(D),qquad
 \Omega_E=Z\mathbin{\dot\cup}T_E=N_G(E),               \tag{2.1}
\]

where `Z={p,q}`, `z in E`, and `u in T_E-T_D`.  Put

\[
 K=Z\cup(T_D\cap T_E),qquad |K|=5.                    \tag{2.2}
\]

The full counterexample hypotheses remain active: seven-connectivity,
strong seven-contraction-criticality, `K_7`-minor-freeness, the unique edge
`zu`, the two old `S`-full rich packets, and the connected bipartite old
boundary.

Choose a six-colouring `phi` of `G/e`, expanded to `G-e`.  For each literal
gate edge `f=dt`, choose a six-colouring `c_f` of `G/f`, expanded to `G-f`.
The proved crossed-state theorem supplies:

1. mismatch on both `Omega_D` and `Omega_E` for every `f,c_f`;
2. four correctly oriented strict packet-demand inequalities; and
3. a named local handoff after the actual packet-one shore is identified.

The handoff is not yet recursive: no noncycling global rank is known.

## 3. Target theorem

### Twin-seam double-lock exchange theorem

Under the frozen input, the twin seam has one of the following literal
outcomes.

1. **Common state.**  Kempe exchanges attached to `e` and one gate edge
   `f` produce the same exact partition on `Omega_D` or `Omega_E`; the
   opposite colour-intact sides palette-align and six-colour `G`.
2. **Terminal model.**  The two lock systems and the two lobes produce a
   literal `K_7` model, or a fixed pair `{a,b}` for which
   `G-{a,b}` is `K_5`-minor-free.
3. **Strict state handoff.**  A named contraction produces an actual
   exact-seven receiver with its literal boundary map, actual packet vector,
   exact state and intact opposite shore, together with a declared
   nonreversible rank which is strictly smaller than the present twin seam.

No naked state mismatch, unranked `(1,1)` receiver, completion edge, or
unlabelled linkage is an outcome.  Proving this theorem closes the entire
symmetric two-/three-gate family.  It does not by itself prove `HC_7`.

## 4. Constructive split

### 4.1 Separating gate edge

Let `alpha` be the common colour of `z,u` in `phi`, and let `beta` be an
alternate colour.  Suppose a gate edge `f=dt` is a bridge of the
`alpha-beta` lock containing `z,u` in `G-e`.

Swapping the `z`-side of that bridge gives one named colouring of both
`G-f` and `G/f`.  The audited
[separating-gate theorem](../results/hc7_atomic_twin_seam_separating_gate_bridge.md)
then forces simultaneous literal `t`-rooted bichromatic mismatch paths in
the two twin views: one lies in the `D`-closed side and one in the
`B_E`-closed side.  Both contain `f`; they need not otherwise be disjoint.

Those two paths are no longer the operative certificate: they may coincide
completely.  The audited
[separating response bundle](../results/hc7_atomic_twin_seam_separating_response_bundle.md)
extracts the stronger exact object from the same response.  It gives a
literal cycle through `e,f`, four other colour-distinct `d-t` bypasses, and
either two internally disjoint paths in their full four-layer graph or one
common `gamma` palette gate with four internally disjoint mixed-colour
escape channels.  A colouring of `G/e/f` also forces five-colour saturation
at `z` or `d` without changing either twin boundary state.

The first subtheorem to prove is:

> **Separating-edge decoder.**  The full response bundle, together with the
> twin boundary maps and the double-contraction saturation fork, can be
> promoted label-faithfully into an adaptive two-carrier return, a fifth
> old-boundary-rooted bag/literal terminal model, or a strictly ranked
> receiver.

The proof must track literal vertices through the promotion.  The common
palette gate is not a graph separator, the bypasses may traverse either
twin shore or the old packets, and a palette colour is not a model label.

There is now a second exact substrate.  The audited
[compulsory-edge regeneration theorem](../results/hc7_atomic_compulsory_edge_not_double_critical.md)
proves `chi(G-{z,u})=6` and supplies a spanning `K_6` model avoiding both
ends.  The complementary `e,f` cycle meets that model from its two sides at
distinct vertices, possibly in one row.  The separating decoder may close
by proving the explicit two-pole row split in that theorem: either the two
poles already have the audited contact pattern giving `K_7`, or one
multiply hit row splits into two connected pieces which both retain all
five foreign-row duties.  Merely placing the first hits in distinct
vertices or distinct palette layers is insufficient.

The last sentence is sharp even after natural extremal normalization.  The
audited [minimal portal-core theorem](../results/hc7_same_row_minimal_portal_core.md)
reduces an extremal common row to two protected endpoint bundles and at
most two root-free lobes.  But the adjacent-two-apex icosahedron
[barrier](../barriers/hc7_same_row_split_two_apex_icosahedron.md) has a
balanced contact-maximal model with the named cycle and no such row split.
It has the permitted coherent fixed-pair terminal and is not
contraction-critical.  Consequently a proof must detect exactly one of
those two missing features; portal-tree minimality is not a decoder.

Likewise, the audited
[four-response trace barrier](../barriers/hc7_twin_seam_four_response_trace_barrier.md)
shows that the bridge response and all four further Kempe responses may
remain crossed on both twins while every new trace stays inside `K`.  The
certificate obeys all packet-one demand inequalities and is compatible
with a saturated double response.  Thus the separating decoder cannot be
completed by another exact-partition comparison.  It must use literal
path localization, a boundary-preserving transition between the two named
minor responses, or the labelled row/fixed-pair geometry above.

The reverse bridge response is now completely understood and is not that
transition.  The audited
[bridge-square involution](../results/hc7_atomic_twin_seam_bridge_square_involution.md)
shows that the forward `f`-swap and reverse `e`-swap form an exact
four-state involution, fully crossed on both twin boundaries.  No scalar
rank can decrease around this square.

The first canonical response outside the square is supplied by the audited
[third-response grid](../results/hc7_atomic_twin_seam_third_response_grid.md).
An internal edge of `D` and an internal edge of `E` give complementary
intact-side orientations; equality on either twin boundary would glue.
Each response also supplies five literal endpoint locks, and its paired
double contraction forces endpointwise five-colour saturation.  The
separating decoder must now allocate one of these literal lock/saturation
systems to an exclusive boundary duty or model row.  Another reverse
bridge swap or demand comparison cannot close it.

For the gate edge itself, the audited
[chromatic fork](../results/hc7_atomic_twin_seam_gate_chromatic_fork.md)
gives a sharper split.  A double-critical gate has a canonical singleton
`{t}` response and five internally disjoint length-two routes, including a
literal triangle internal to `D`; the other branch regenerates a second
spanning `K_6` frame with distinct first hits.  These are allocation inputs,
not terminal outputs or ranked receivers.

The audited
[two-pole contact trichotomy](../results/hc7_atomic_two_pole_contact_trichotomy.md)
exhausts the numerical part of that geometry.  Joint contact six is
`K_7`.  Joint contact five forces `mu=1`, and contact four supplies a
two-hole centre of order two, but neither is a ranked handoff.  At lower
contact, a same-row rooted partition gives `K_7` or an actual separator,
while a literal row transfer strictly increases contact.  The only
remaining model-relative object is therefore a row-duty lock: every
pole-rooted peel disconnects its donor, monopolizes a foreign duty, or
consumes an old pole contact.  The separating decoder must spend the
proper-minor response precisely on that lock or on the resulting actual
separator; another contact inequality cannot close it.

### 4.2 Response-matched gate-edge bypass

For a fixed response `c_f`, palette-align `c_f(z)` with the common
`phi`-colour of `z,u`; the colour of `c_f(u)` selects one response-matched
`e`-lock.  If its eligible gate edge is not separating, use its literal
bypass jointly with the corresponding `f`-lock.  Independently of the
palette layers, the common deletion `G-{e,f}` already contains four
pairwise adjacent connected bags rooted at `z,u,d,t`.  Separator allocation
forces at least three of those bags to meet one twin boundary.  The target
is:

> **Nonseparable double-lock decoder.**  A response-matched
> gate-edge-nonseparable `e`-lock and its crossed `f`-response force a common
> exact state on one twin boundary, a literal terminal model, or a strictly
> ranked receiver.

This branch must promote the guaranteed three-bag boundary incidence to a
fourth duty contact, or couple it to the exact response states.  The rooted
core itself is not a `K_7`: its bags may consume both old packets and both
lobes.  Edge-nonseparability alone still does not turn palette colours into
branch-set labels.

Together the two decoders prove the target theorem.

## 5. Literature decision from online research, 15 July 2026

No located primary source supplies this exchange as a black box.

* [Humeau--Pous](https://arxiv.org/abs/2505.16431) proves a constructive
  crossing-or-web theorem for arbitrary terminal tuples and generates webs
  by recursive parallel composition.  It organizes a failed two-path
  exchange, but a web completion can add nonliteral edges and transports no
  exact colouring state.
* [Dvorak--Swart](https://arxiv.org/abs/2504.07764), Theorem 3, realizes
  arbitrary permutation-closed boundary colouring languages while excluding
  the corresponding larger rooted and unrooted clique minors.  Therefore an
  abstract extension-language or overlap-partition argument cannot be the
  engine; the named operations and lock geometry are essential.
* [Kriesell--Mohr](https://arxiv.org/abs/1911.09998) gives useful positive
  rooted-minor packaging for sparse five-root Kempe skeletons, but also
  proves that generic pairwise bichromatic connectivity is insufficient in
  larger order.  It may package a literal skeleton after the decoder creates
  one; it cannot create the required disjoint skeleton.
* The recent
  [spanning-routing limitation](https://arxiv.org/abs/2607.09342) shows that
  irrelevant-vertex reductions can fail even in planar classes when the
  annotated routing requirement is distributed.  A bounded-folio route is
  therefore backup only, after the state is shown to be a finite boundary
  annotation invariant.
* [Norin--Totschnig](https://arxiv.org/abs/2507.03244) guarantees the
  near-`K_7` model used by the global proof spine, but does not preserve the
  two deficient labels through the present seam.

The research implication is asymmetric: spend the constructive effort on
the two named lock systems, and use web/folio machinery only after an
actual failure certificate has been extracted.

## 6. Falsification protocol

Before promoting either decoder, test it against:

1. the exact symmetric `(5,5)` list obstruction;
2. the known three-cut packet-collapse shell;
3. long planar tubes with a persistent hidden apex pair; and
4. bounded literal twin seams with arbitrary proper-minor colour responses.

Reject a proposed proof immediately if it assumes that the two states agree
on `K`, that old `S`-full packets meet the literal gates, or that two paths
sharing `f` are otherwise disjoint.

Existing exact search is only a guardrail: no survivor occurs in the tested
root-complete planar shores through order seven, but no unbounded conclusion
is inferred.  The explicit
[bare-alignment barrier](../barriers/hc7_twin_seam_bare_k_alignment_barrier.md)
must also be replayed: it proves that `K`-clean contraction and arbitrary
Kempe normalization cannot replace the rooted-terminal branch.

## 7. Success condition

Success is an audited proof of both decoders and hence of the target theorem,
including literal branch sets or a complete palette-alignment/gluing proof.
If one decoder fails, the acceptable output is a concrete infinite
counterfamily or a smallest exact shell identifying the missing hypothesis;
the response is then to change the exchange invariant, not to enumerate
more Moser or portal cases.
