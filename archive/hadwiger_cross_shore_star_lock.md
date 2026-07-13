# A boundary-centred star forces a locked full-palette shore

## 1. Uniform theorem

### Theorem 1.1 (cross-shore star lock)

Let `G` be a graph which is not `r`-colourable although every proper
minor of `G` is `r`-colourable.  Let `S` be a separator and let `D,H` be
distinct components of `G-S`.  Choose

\[
 x\in S,\qquad d\in N_D(x),\qquad h\in N_H(x).
\]

Contract the connected star `G[{x,d,h}]`, colour the resulting proper
minor, and expand its image.  This gives an `r`-colouring `f` of

\[
                         G-\{xd,xh\}
\]

with `f(x)=f(d)=f(h)=alpha`.  Then at least one of the following holds.

1. For every `beta != alpha`, the `alpha/beta` component containing `d`
   meets `S`.
2. For every `beta != alpha`, the `alpha/beta` component containing `h`
   meets `S`.

The chosen side is therefore locked to the literal adhesion in every
other palette in one simultaneous colouring.

### Proof

Call a **`D`-repair** an `r`-colouring of `G-xh` which agrees with `f`
on `S`, and define an **`H`-repair** symmetrically as a colouring of
`G-xd` agreeing with `f` on `S`.

Both repairs cannot exist.  If they did, use the `D`-repair on
`G[D\cup S]` and the `H`-repair on `G[H\cup S]` (and, for any further
components, either restriction on that component together with `S`).
The two colourings agree on `S`.  The first has restored `xd`, because
its only missing edge is `xh`; the second has restored `xh`, because its
only missing edge is `xd`.  Distinct components of `G-S` are
anticomplete.  Hence the
two restrictions splice to an `r`-colouring of `G`, a contradiction.

Suppose no `D`-repair exists.  Fix `beta != alpha` and let `K` be the
`alpha/beta` component of `f` containing `d`.  If `K` avoided `S`, then
it would lie wholly in `D`: every path from `D` to another component of
`G-S` meets `S`.  Switch `alpha,beta` on `K`.  This preserves the colours
on `S`, changes `d` away from `alpha`, and leaves `x,h` unchanged.
Restoring `xd` now gives a `D`-repair, a contradiction.  Thus every such
`K` meets `S`, which is outcome 1.  If a `D`-repair exists, the
no-two-repairs conclusion says that no `H`-repair exists, and the
symmetric argument gives outcome 2.  QED.

### Corollary 1.2 (palette neighbours and adhesion carriers)

On the locked side, the operated leaf has a neighbour of every colour
different from `alpha`, and for each such colour there is a connected
`alpha/beta` carrier from the leaf to `S`.

### Proof

If the leaf had no `beta`-neighbour, recolouring just that leaf with
`beta` and restoring its edge to `x` would be a repair.  The carrier is
the component supplied by Theorem 1.1, truncated at its first vertex of
`S`.  QED.

## 2. Repeated-root application

Let an exact seven-cut have two full shores and let `x` be a boundary
label with two neighbours in one shore.  Applying Theorem 1.1 with either
of those neighbours and any `x`-neighbour in the opposite full shore
does more than provide separate edge-critical colourings: one of the two
literal shores is simultaneously adhesion-locked in all five remaining
palettes.

This is a parameter-uniform operation-state-to-rooted-carrier principle.
It does **not** yet produce five disjoint carriers.  Different
`alpha/beta` components may share alpha-coloured vertices, and several
palettes may meet the adhesion at the same alpha-coloured vertex.  The
remaining exchange theorem must use seven-connectivity and the covering
bad split to turn that common alpha warehouse into either

* disjoint labelled columns and a `K_7` model;
* a smaller exact seven-adhesion; or
* a common boundary state which colour-glues.

The qualification is essential: a hub shared by all bichromatic
carriers realizes the conclusions of Theorem 1.1 at low connectivity.

## 3. Multi-shore form

### Theorem 3.1 (one full-palette leaf among any number of shores)

Let `m>=1`, let `C_1,...,C_m` be distinct components of `G-S`, let
`x in S`, and
choose `d_i in N_{C_i}(x)` for every `i`.  Contract the connected star
on `x,d_1,...,d_m`, colour the proper minor, and expand it to a colouring
`f` of the graph with all `xd_i` deleted.  Write `alpha` for their common
colour.  Then some index `i` has the following property:

\[
 \text{for every }\beta\ne\alpha,\quad
 K_{\alpha,\beta}(d_i)\cap S\ne\varnothing.       \tag{3.1}
\]

### Proof

If not, choose for each `i` a colour `beta_i != alpha` such that the
`alpha/beta_i` component `K_i` containing `d_i` avoids `S`.  Then
`K_i subseteq C_i`.  The sets `K_i` are pairwise anticomplete, even when
some of the colours `beta_i` coincide.  Switch `alpha,beta_i` on every
`K_i` simultaneously.  This leaves `x` and all of `S` unchanged and
changes every `d_i` away from `alpha`.  Restoring all star edges gives an
`r`-colouring of `G`, a contradiction.  QED.

This gives a genuine uniform rooted-model principle at a full adhesion:
one simultaneous proper-minor witness selects an entire palette-locked
shore, rather than assigning palettes independently to different shores.
Its sharp residue is again a common alpha warehouse inside the selected
shore.

## 4. Unique portals descend at a minimum adhesion

### Lemma 4.1 (unique-portal descent)

Let `G` be `k`-connected, let `S` be a `k`-cut, and let `C` be a
component of `G-S`.  Suppose `C` is full to `S` and some `s in S` has a
unique neighbour `u in C`.  Then either `C={u}`, or every component `Q`
of `C-u` has

\[
                      N_G(Q)=(S-\{s\})\cup\{u\}.       \tag{4.1}
\]

In the latter case the right side is another exact `k`-cut and `Q` is a
proper fragment contained in `C`.

### Proof

Assume `C-u` is nonempty and let `Q` be one of its components.  Since
`u` is the only `s`-neighbour in `C` and `C` is a component of `G-S`,

\[
                     N_G(Q)\subseteq(S-\{s\})\cup\{u\}.
\]

The set on the right has order `k`.  Another component of `G-S` lies
beyond `N_G(Q)`, so `N_G(Q)` separates two nonempty vertex sets.
`k`-connectivity gives `|N_G(Q)|>=k`, forcing equality throughout.  Thus
(4.1) is an exact `k`-cut, and `Q` is a proper subset of `C`.  QED.

### Corollary 4.2 (two portals per label at a minimum fragment)

Choose, among all components behind exact `k`-cuts of `G`, one of minimum
order.  It is either a singleton or every one of its `k` boundary labels
has at least two distinct neighbours in it.

In the singleton case its sole vertex has neighbourhood exactly the
boundary and degree `k`.  For `HC_7` this is a degree-seven re-rooting;
in the nonsingleton case every boundary-centred cross-shore star can be
chosen with two distinct portal choices on the minimum side.
