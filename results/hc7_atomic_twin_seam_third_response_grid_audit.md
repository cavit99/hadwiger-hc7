# Independent audit: atomic twin-seam third-response grid

**Verdict:** GREEN, with one formal citation correction in the first
double-contraction application.  Relative to `Omega_D`, the compulsory
edge `e=zu` is internal to the open shore `B_D`, rather than a
boundary--shore edge of the exact form stated in the earlier
double-contraction theorem.  The proof of that theorem applies verbatim to
two disjoint internal edges in opposite open shores, and is reproduced in
Section 6 below.  No conclusion changes.

**Audited source:**
`results/hc7_atomic_twin_seam_third_response_grid.md`.

**Source SHA-256:**
`77587176ea9953fc7deba6061df66c311686db6278908ef7022602ef8dc520c7`.

## 1. The two-edge deletion has chromatic number six

Edge deletion is a minor operation, so minor-criticality six-colours
`G-e-f`.  Suppose it had a five-colouring.  Recolour `z` and `d` with one
globally fresh sixth colour.  The restored edges

\[
                         e=zu,\qquad f=dt
\]

are proper because `u,t` retain old colours.  No other edge at `z,d`
becomes monochromatic.  Moreover `zd` is absent: `z` lies in `E` and `d`
lies in `D`, distinct components of `A-Z`.  Thus the common fresh colour
on `z,d` is safe and would six-colour `G`.  This proves

\[
                              \chi(G-e-f)=6.
\]

The notation is correctly edge deletion, not deletion of the four ends.

## 2. Intact-side orientations

Let `g=xy` be internal to `D`.  A colouring of `G/g`, lifted to `G-g`,
has only `g` missing.  Hence it is intact on

* `B_D union Omega_D`, which excludes `D`; and
* `E union Omega_E`, which also excludes `D`.

These are exactly the two sides claimed for a `g`-response.

Likewise an edge `h=ab` internal to `E` is absent from neither

* `D union Omega_D`; nor
* `B_E union Omega_E`.

These are exactly the two sides claimed for an `h`-response.  Contraction
may add edges incident with the contracted image, but this does not affect
the assertion: each displayed restriction is a proper colouring of the
corresponding original induced closed-side graph.

The choices of internal edges are conditional.  The theorem does not
assert that a singleton lobe contains such an edge.

## 3. Nonextension, reflection, and demand direction

If `Pi_D^g` extended to `D union Omega_D`, it would palette-align with the
already intact `g`-response on `B_D union Omega_D` and glue across the
actual separation.  This would six-colour `G`.  Therefore the state does
not extend to that complementary side.  The identical argument at
`Omega_E` excludes extension to `B_E union Omega_E`.

Exact packet reflection must use packets in the already intact open shore:
they construct the matching colouring on the opposite closed side.  Thus
the strict inequalities are correctly oriented as

\[
 d_{H_D}(\Pi_D^g)>\nu_{B_D},
 \qquad
 d_{H_E}(\Pi_E^g)>\nu_E.
\]

Reflection either gives the forbidden complementary extension or a
literal `K_7`; both are excluded in the kernel.

For `h`, the already intact shores are `D` and `B_E`, so the corresponding
inequalities are correctly

\[
 d_{H_D}(\Pi_D^h)>\nu_D,
 \qquad
 d_{H_E}(\Pi_E^h)>\nu_{B_E}.
\]

In a simultaneous `(1,1)/(1,1)` cell, strict integrality makes every one
of these demands at least two, exactly as stated.

## 4. Opposite-state gluing

At `Omega_D`, an `h`-response is intact on the `D` side and a
`g`-response is intact on the `B_D` side.  Equality of their exact
partitions permits a palette permutation making their boundary colours
agree literally, after which the two restrictions glue.

At `Omega_E`, the `g`-response is intact on `E` and the `h`-response is
intact on `B_E`.  The same argument applies.  Therefore

\[
                         \Pi_D^g\ne\Pi_D^h,
             \qquad     \Pi_E^g\ne\Pi_E^h.
\]

The fixed `G/e` response has the same orientation as `h`: it is intact on
`D` at `Omega_D` and on `B_E` at `Omega_E`.  Every `G/f` response has the
same orientation as `g`: it is intact on `B_D` and `E`.  The two extended
crossing assertions therefore follow from the identical complementary-side
gluing proof.  The note does not incorrectly compare two responses with
the same orientation.

## 5. Five endpoint locks

Lift a six-colouring of `G/r` to `G-r`, with the two ends of `r` in common
colour `alpha`.  If an alternate colour is absent from the neighbourhood
of one end outside its mate, recolouring that end restores `r` and
six-colours `G`.  Hence each end sees all five alternate colours.

For any alternate `beta`, if the two ends lie in distinct
`alpha,beta` components, swapping the component of exactly one endpoint
makes the restored edge proper.  Thus the five end-to-end Kempe locks are
literal.  This proof applies to every internal lobe edge response and does
not identify palette colours with boundary or model-row labels.

## 6. The two double-contraction forks

### The `Omega_D` fork

Relative to the actual separation

\[
             V(G)=D\mathbin{\dot\cup}\Omega_D
                         \mathbin{\dot\cup}B_D,
\]

the edges `g=xy` and `e=zu` are vertex-disjoint and lie internally in the
two opposite open shores `D` and `B_D`, respectively.  This is slightly
more symmetric than the formal setup of the earlier double-contraction
theorem, where one mate is a boundary vertex.

Let `c` colour `G/e/g`, lifted to `G-e-g`.  If `z` is free relative to
`u`, recolour `z` and restore `e`; this gives a colouring of `G-g` intact
on the `B_D` closed side.  If, say, `x` is free relative to `y`, recolour
`x` and restore `g`; this gives a colouring of `G-e` intact on the `D`
closed side.  Both recoloured vertices lie outside `Omega_D`, so the two
restrictions retain literally the exact boundary state of `c`.  There is
no `D-B_D` edge, and the restrictions therefore glue.

The same applies with `y`.  Thus `z` cannot be free simultaneously with
either endpoint of `g`.  Logical negation gives exactly

\[
 z\text{ saturated outside }u
 \quad\text{or}\quad
 x,y\text{ both saturated outside their mate}.
\]

This proves (4.1) directly and supplies the formal generalization needed
for the citation.

### The `Omega_E` fork

Relative to

\[
             V(G)=E\mathbin{\dot\cup}\Omega_E
                         \mathbin{\dot\cup}B_E,
\]

the edge `h=ab` is internal to `E`, while `f=dt` joins the open `B_E`
shore at `d` to the retained boundary label `t`.  This is literally the
orientation of the audited double-contraction theorem.  Recolour `d`, not
`t`, when repairing `f`, and recolour one of `a,b` when repairing `h`.
The recoloured vertices lie outside `Omega_E`; the common exact state is
preserved and the complementary restrictions glue.

Possible edges from `t` to `a` or `b` cause no problem.  A colour present
at such a boundary neighbour is, by definition, unavailable when that
endpoint is declared free.  The logical negation is precisely (4.2).

In both forks, “alternate colours” is endpoint-relative: the colour shared
by `z,u` need not equal the colour shared by the internal-edge endpoints.

## 7. Exact scope

The theorem genuinely produces response families outside the involutive
bridge square:

* their two orientation classes are exact and fully crossed;
* every internal-edge response has five literal endpoint locks; and
* pairing a lobe edge with the named opposite edge gives a common-state,
  boundary-preserving palette-saturation fork.

It does not localize the saturation witnesses to exclusive boundary
duties, preserve disjoint old packets, split a regenerated model row, or
give a ranked receiver.  The final allocation alternatives in the source
are therefore correctly stated as remaining obligations rather than
conclusions.
