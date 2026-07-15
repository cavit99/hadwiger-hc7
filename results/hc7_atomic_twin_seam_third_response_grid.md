# Atomic twin-seam third-response grid

**Status:** proved and independently audited.

The separating bridge swaps form a reversible four-state square.  This
note supplies the first response family which is literally outside that
square: contract an edge internal to either lobe while retaining both
named seam edges.  The resulting states have the two complementary
closed-side orientations, and opposite orientations can never agree on
either twin boundary.  A paired double contraction then turns each such
third response into an exact palette-saturation fork.

This is a state-labelled input to the missing allocation theorem.  It does
not claim that palette saturation already supplies a labelled carrier.

## 1. Setup

Use the frozen twin seam and notation of the
[crossed-state theorem](hc7_atomic_twin_seam_crossed_states.md):

\[
 e=zu,\qquad f=dt,
\]

where `z in E`, `u in B_0`, `d in D`, and `t in Z`.  The two actual
seven-boundaries are

\[
 \Omega_D=N_G(D),\qquad \Omega_E=N_G(E),
\]

with complementary open shores `B_D` and `B_E`.  Thus there is no
`D-B_D` edge across `Omega_D`, and no `E-B_E` edge across `Omega_E`.

Let

\[
 g=xy\in E(G[D]),\qquad h=ab\in E(G[E]).             \tag{1.1}
\]

The edges in each of the pairs `(e,g)` and `(f,h)` are vertex-disjoint.
For a six-colouring `c_g` of `G/g`, lifted to `G-g`, write
`Pi_D^g,Pi_E^g` for its exact partitions on the two twin boundaries.
Define `Pi_D^h,Pi_E^h` symmetrically from a six-colouring of `G/h`.

## 2. The missing-edge host

### Lemma 2.1

\[
                         \chi(G-e-f)=6.              \tag{2.1}
\]

Here `G-e-f` means deletion of the two edges, not deletion of their four
ends.

### Proof

The graph `G-e-f` is a proper minor of `G`, so it is six-colourable.  If it
had a five-colouring, give `z` and `d` one fresh sixth colour.  This restores
both missing edges: `u` and `t` retain old colours.  The vertices `z,d` are
nonadjacent because they lie in the distinct components `E,D` of `A-Z`.
Every other edge remains proper.  This would six-colour `G`, a
contradiction.  \(\square\)

The bridge-square responses occupy the chambers in which exactly one of
`e,f` is monochromatic (and the double-contraction response occupies the
chamber in which both are monochromatic).  By contrast, every colouring of
`G/g` or `G/h` keeps both literal edges `e,f` present and proper.  Its
restriction to `G-e-f-g` or `G-e-f-h` therefore lies in the fourth chamber,
which is unavailable without deleting the third edge.  This is the precise
sense in which (1.1) gives a response outside the involutive square.

## 3. Exact orientation of the third responses

### Theorem 3.1 (third-response grid)

For every choice of the internal edges in (1.1) and every six-colouring of
their contractions, the following statements hold.

1. The `g`-response is colour-intact on the `B_D`-closed side of
   `Omega_D` and on the `E`-closed side of `Omega_E`.  Its states cannot be
   extended to the complementary original closed sides.  In particular,

   \[
      d_{H_D}(\Pi_D^g)>\nu_{B_D},\qquad
      d_{H_E}(\Pi_E^g)>\nu_E.                         \tag{3.1}
   \]

2. The `h`-response is colour-intact on the `D`-closed side of `Omega_D`
   and on the `B_E`-closed side of `Omega_E`.  Its states cannot be
   extended to the complementary original closed sides.  In particular,

   \[
      d_{H_D}(\Pi_D^h)>\nu_D,\qquad
      d_{H_E}(\Pi_E^h)>\nu_{B_E}.                     \tag{3.2}
   \]

3. Opposite orientations are fully crossed:

   \[
      \Pi_D^g\ne\Pi_D^h,\qquad
      \Pi_E^g\ne\Pi_E^h.                             \tag{3.3}
   \]

   The same conclusion holds if `Pi^h` is replaced by the fixed
   `G/e`-response `Pi^phi`, or if `Pi^g` is replaced by any `G/f` response.

### Proof

The only edge missing from the lifted `g`-response is internal to `D`.
Consequently its restrictions to `G[B_D union Omega_D]` and
`G[E union Omega_E]` are proper colourings of the original closed-side
graphs.  If `Pi_D^g` extended to a proper colouring of
`G[D union Omega_D]`, palette alignment and gluing across `Omega_D` would
six-colour `G`.  The same argument across `Omega_E` forbids an extension
of `Pi_E^g` to `G[B_E union Omega_E]`.

Exact packet reflection on the already colour-intact side would construct
precisely either such a forbidden complementary extension or a literal
`K_7`.  The latter is excluded by the kernel.  This proves (3.1).

For `h`, the missing edge is internal to `E`.  Its intact restrictions are
therefore `G[D union Omega_D]` and `G[B_E union Omega_E]`.  The identical
gluing and reflection argument proves the two nonextension statements and
(3.2).

If `Pi_D^g=Pi_D^h`, glue the intact `D`-side of the `h`-response to the
intact `B_D`-side of the `g`-response.  If
`Pi_E^g=Pi_E^h`, glue the intact `E`-side of the `g`-response to the intact
`B_E`-side of the `h`-response.  Either equality therefore six-colours
`G`, proving (3.3).

The fixed `G/e` response has the same intact-side orientation as the
`h`-responses, while every `G/f` response has the same orientation as the
`g`-responses.  Repeating the same gluing argument proves the last
assertion.  \(\square\)

In the simultaneous `(1,1)/(1,1)` residue, all four inequalities
(3.1)--(3.2) say that the corresponding exact state has packet demand at
least two.  Unlike the bridge square, however, the response families are
indexed by literal lobe edges and hence carry geometric locations which a
later allocation theorem can use.

## 4. Five locks and a common-state saturation fork

### Lemma 4.1 (edge-response locks)

Let `r=vw` be any edge of `G`, and let `c_r` be a six-colouring of `G/r`,
lifted to `G-r`, with common end colour `alpha`.  Then:

1. each of `v,w` has a neighbour of every colour other than `alpha`; and
2. for every `beta ne alpha`, the vertices `v,w` lie in one
   `alpha,beta` component of `G-r`.

Hence every internal lobe-edge response supplies five literal
bichromatic end-to-end locks.

### Proof

If an alternate colour were absent from `N(v)-{w}`, recolouring `v` with
that colour would restore `r` and six-colour `G`; the same holds for `w`.
If `v,w` lay in distinct `alpha,beta` components, swapping the component
containing exactly one endpoint would make their colours different while
preserving a proper colouring of `G-r`.  Restoring `r` again six-colours
`G`.  Both outcomes contradict the kernel.  \(\square\)

### Theorem 4.2 (twin double-contraction forks)

For every `g=xy in E(G[D])` and every six-colouring of `G/e/g`, lifted to
`G-e-g`, at least one of the following holds:

\[
 \begin{array}{ll}
  \text{(D1)} & z\text{ sees all five alternate colours in }N(z)-\{u\};\\
  \text{(D2)} & x\text{ and }y\text{ each see all five alternate colours}
                 \text{ outside their mate.}
 \end{array}                                           \tag{4.1}
\]

For every `h=ab in E(G[E])` and every six-colouring of `G/f/h`, lifted to
`G-f-h`, at least one of:

\[
 \begin{array}{ll}
  \text{(E1)} & d\text{ sees all five alternate colours in }N(d)-\{t\};\\
  \text{(E2)} & a\text{ and }b\text{ each see all five alternate colours}
                 \text{ outside their mate.}
 \end{array}                                           \tag{4.2}
\]

The forks are state-preserving: if the first named endpoint and one end of
the internal edge were simultaneously free, recolouring those two literal
vertices would produce complementary intact-side colourings with one
common exact boundary state, and these would glue to a six-colouring of
`G`.

Moreover,

\[
                         \chi(G/e/g)=\chi(G/f/h)=6.    \tag{4.3}
\]

### Proof

Lift a six-colouring of `G/e/g` to `G-e-g`.  If `z` is free relative to
`u`, recolour only `z`; this restores `e` and gives a colouring of `G-g`
whose `B_D`-closed restriction is intact.  If, say, `x` is free relative
to `y`, recolour only `x`; this restores `g` and gives a colouring of
`G-e` whose `D`-closed restriction is intact.  Both recolourings are
outside `Omega_D`, so the two restrictions have exactly the boundary
state of the common double-contraction colouring.  They palette-align and
glue, contradicting the kernel.  Thus `z` cannot be free simultaneously
with either end of `g`, which is exactly (4.1).

For (4.2), use boundary `Omega_E`, complementary shores `B_E,E`, the
boundary edge `f=dt` on the `B_E` side, and the internal edge `h` in `E`.
The repair recolours `d`, not the retained boundary label `t`, together
with one end of `h`.  Both vertices lie outside `Omega_E`, so the same
two-recolouring and gluing proof gives (4.2) without changing the exact
boundary state.

Finally, each double contraction is a proper minor and hence has chromatic
number at most six.  If either admitted a colouring using at most five
colours, one globally unused sixth colour would make all three relevant
literal endpoints free in its lift.  The corresponding common-state
repair just proved would six-colour `G`.  This proves (4.3).  \(\square\)

## 5. What this discharges

The third operation required by the bridge-square audit is now canonical:
every internal edge of `D` gives an opposite-orientation state with five
literal locks, and every internal edge of `E` gives the complementary
orientation.  Equality of any opposite pair is already the common-state
outcome of the double-lock theorem.  Pairing the response with `e` or `f`
also gives a literal, state-preserving saturation fork rather than an
abstract boundary-language comparison.

The remaining implication is allocation, not response existence.  One
must show that in a static-return-irreducible seam the saturation witnesses
or five locks either:

1. attach an exclusive old-boundary duty to a disjoint carrier;
2. split a regenerated model row while retaining its five foreign duties;
3. force equality with an opposite-orientation state; or
4. expose an actual globally smaller oriented `(1,2)` receiver or a valid
   fixed-pair terminal.

Neither a demand inequality nor a palette-colour neighbour is silently a
branch-set label, so no terminal conclusion is claimed here.
