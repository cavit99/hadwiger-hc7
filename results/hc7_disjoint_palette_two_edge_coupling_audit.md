# Independent audit: disjoint-palette coupling for two critical edges

**Audited file:** `results/hc7_disjoint_palette_two_edge_coupling.md`
**SHA-256:** `eaf69ebcb9d1441b1eafffc1f3712de40becbe1af24c235d77fe4a56a5ac6f4e`
**Verdict:** **GREEN.** Theorem 1.1, Corollary 1.2, and the two-five-clique
specialization are correct as stated. No mathematical correction is
required.

This is an independent internal mathematical audit, not external peer
review. It uses the already audited generalized two-deleted-edge Kempe fork
at source hash
`880b9d30946357b1df0540543b5ffe1d38def7f68224577ebe476e4bed9a6370`.

## Promotion recheck

The promoted source differs from the audited draft only in its status and
adjacent-audit link. Reversing those metadata edits reproduces the original
audited SHA-256
`38f7310c1e68e6505ca5d2028ef30bb88f18fa036bf6cc040a6b9b6ead7c7100`.
No mathematical statement or proof step changed, so the GREEN verdict
transfers to the promoted hash above.

## 1. Individual reachable-set rotations

Every vertex reachable in the `e`-orientation has a colour in `Omega_e`,
and every vertex reachable in the `f`-orientation has a colour in
`Omega_f`. The supports are disjoint, so the reachable vertex sets are
disjoint. Each individual rotation is proper on `H` by the generalized
fork.

If `b` is not reachable, the `e`-rotation separates the ends of `e`.
Non-`q`-colourability of `G` forces the ends of `f` to remain equal; hence
the rotation gives the asserted colouring of `G-f`. The symmetric statement
for `f` is identical.

## 2. Simultaneous-rotation check

The only point not obtained by applying the two forks separately is that
the two rotations may be performed simultaneously. This is valid.

Edges with neither or both ends in one rotated set are handled by the
individual reachable-set proof. An edge with one end in `F_e` and the other
in `F_f` still has one end coloured in `Omega_e` and the other in
`Omega_f` after both rotations. Those supports are disjoint, so such an
edge cannot become monochromatic. Likewise, rotating one support never
changes an endpoint of the other deleted edge.

Thus, if both opposite endpoints were unreachable, the commuting rotations
would give a proper colouring of `H` in which both deleted edges are proper.
Restoring both edges would `q`-colour `G`, a contradiction. This proves
Theorem 1.1(1).

If both endpoints are reachable, a simple directed path can be chosen in
each support. Their vertex sets are disjoint because their vertex colours
belong to disjoint supports. This proves assertion 2. If just one endpoint
is unreachable, its rotation is confined to its support and leaves the
other directed path and its orientation unchanged, proving assertion 3.

## 3. Both cyclic orders

A three-element colour set has exactly two cyclic orientations. If neither
edge were reachable in both orientations, one could choose an orientation
leaving the far end of `e` unreachable and independently choose one leaving
the far end of `f` unreachable. Theorem 1.1(1) excludes that pair. Hence one
edge is reachable in both cyclic orders, as Corollary 1.2 states.

The corollary does not assert that the two paths for that one edge are
internally disjoint from each other. It only couples their existence; the
source file preserves this distinction.

## 4. Two-five-clique specialization

In `L_e-e`, the common endpoint colour and the three pairwise distinct
colours on `r_1,r_2,r_3` use four colours. The remaining two colours, with
the endpoint colour, form `Omega_e`; the analogous statement holds for
`L_f-f`.

If the natural supports are disjoint, they partition the six colours. The
`r_i` therefore have exactly the colours of `Omega_f`, and the `t_i` have
exactly those of `Omega_e`. An `e`-replacement path uses only
`Omega_e` and consequently avoids the `r_i`; an `f`-replacement path avoids
the `t_i`. More strongly, every selected `e`-path is vertex-disjoint from
every selected `f`-path because their colour supports are disjoint.

The warning about cross-intersections is correct. An `e`-path may pass
through vertices of `L_f` coloured in `Omega_e`, namely the `t_i`, and an
`f`-path may pass through the `r_i`. Thus the paths do not automatically
produce two disjoint labelled five-clique minor models.

## 5. Trust boundary

This audit verifies the colouring coupling only. It does not derive a
label-preserving composition of both near-cliques, an order-seven
separation, a `K_7`-minor model, `HC_7`, or Hadwiger's Conjecture. The
additional host-level inputs named in the source remain genuinely
necessary.
