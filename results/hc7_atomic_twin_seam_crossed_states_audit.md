# Audit: atomic twin-seam crossed states

**Verdict:** GREEN.

## Colour-intact sides

With `e=zu` and

\[
 K=Z\cup(T_D\cap T_E),\qquad
 \Omega_D=K\cup(T_D-T_E),\qquad
 \Omega_E=K\cup(T_E-T_D),
\]

the colouring of `G/e`, expanded to `G-e`, is proper on the `D`-closed side
of `Omega_D`, since both `z,u` lie outside it.  It is proper on the opposite `B_E`-closed side
of `Omega_E`, since that side excludes `z`.

For `f=dt`, with `d in D` and `t in Z`, a colouring of `G/f` restricts
properly to the `B_D`-closed side of `Omega_D` and the `E`-closed side of
`Omega_E`, because both exclude `d`.  The literal label `t` is retained.
Contraction may add edges at `t`, so the safe statement is colour-intactness
of the original subgraphs, not graph-isomorphism to their minor images.

## Gluing audit

Equality of the two exact partitions on `Omega_D` permits a partial colour
bijection on the used boundary colours, extendable to a permutation of all
six colours.  After that palette alignment, the `G-zu` colouring on the
`D`-side glues to the `G/f` colouring on the `B_D`-side.  Equality on
`Omega_E` similarly glues the `G-zu` colouring on the `B_E`-side to the
`G/f` colouring on the `E`-side.  In both cases the original edge `zu` is
contained in the `G/f`-coloured side, so no deleted edge is overlooked.
This proves the two inequalities of partitions.

## Demand orientation

Exact reflection must use packets in the same open shore as the already
colour-intact restriction: contracting those packets constructs the
opposite closed-side colouring.  The four strict inequalities are therefore

\[
 d_{H_D}(\Pi_D^\phi)>\nu_D,
 \qquad d_{H_D}(\Pi_D^f)>\nu_{B_D},
\]

\[
 d_{H_E}(\Pi_E^\phi)>\nu_{B_E},
 \qquad d_{H_E}(\Pi_E^f)>\nu_E.
\]

These directions are correct and boundary-relative.

## Packet-aligned handoff

At `Omega_D`, if `D` is packet-one, the boundary contraction `f` returns
`Pi_D^f` intact on `B_D` and its demand exceeds `nu_B_D`; if `B_D` is
packet-one, the internal contraction `e` returns `Pi_D^phi` intact on `D`
and its demand exceeds `nu_D`.  At `Omega_E`, packet-one `E` selects the
boundary contraction `e` and packet-one `B_E` selects the boundary
contraction `f`, with the two inequalities in (2.3).  These operations
retain all seven boundary labels.  Hence the named local handoff and its
`(1,2)`/`(1,1)` demand bounds are valid.

It is only local.  Neither the side order nor packet-sum is proved to
decrease in every orientation, so no global `S4` rank follows.

## Scope

The theorem does not prove that the partition change is confined to the
two exclusive labels on either boundary.  The two colourings may already
differ on the common five-set `K`.  Calling the result a crossed pair of
state inequalities is accurate; calling it state localization would be an
overclaim until a `K`-alignment or Kempe-normalization theorem is proved.
