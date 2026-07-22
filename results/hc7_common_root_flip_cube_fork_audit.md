# Audit: common-root rejection symmetry forces a synchronized fork

**Audit type:** separate internal cold audit

**Verdict:** GREEN
**Audited theorem revision (SHA-256):**
`e433cb80afc350252674a15f98ab85dd6e879c8f25f842bbeeca79bafcacc48e`

The audited file is
`results/hc7_common_root_flip_cube_fork.md`.  The audit checked it
from scratch against these exact input revisions:

```text
11f7c6433687847edc3635f3284a074fa2f6157c304035ea9fc42e6a224fbc2f  results/hc7_full_exterior_component_common_root_exchange.md
e659b2765053c34415cad0c6e9dcec78a250e751dd80d79f8e077d064d24835f  results/hc7_component_deletion_kempe_exchange.md
```

## Verdict scope

All three conclusions of Theorem 1 follow from the stated hypotheses.
The crossing-cycle argument, antipodal cube argument, fixed-extension
fork, simultaneous path contractions, and `K_6`-minor exclusion are valid.
The corrected two-or-three-edge alternative handles repeated endpoint
pairs exactly.  No unresolved assumption or proof gap was found.

This is a nonterminal refinement.  It neither proves `HC_7` nor proves
that the two paths separately obtained through the opposite exterior
component are compatible.  The theorem states that trust boundary
correctly.

## 1. Setup and exclusive-contact colouring

The recolouring of `x` is legal only if neither `alpha` nor `beta` occurs
on `N_H(x)`, so `W_0={x}` is indeed a component of
`H[alpha,beta]`.  Since `R(phi)={C}` and `R(psi)={D}`, `psi` extends
through `C` and `phi` extends through `D`.  Their restrictions agree on
`X-{x}`.  Deleting `x`, using those two extensions, and colouring `u`
with colour six therefore gives a proper six-colouring of `G-x`.

In the `psi`-extension, `x` has colour `beta`, so it has no
`beta`-neighbour in `C`.  Reverse lifting of the rejected recolouring
supplies an `alpha`-neighbour there.  The symmetric forward lift in the
`phi`-extension through `D` supplies a `beta`-neighbour and excludes an
`alpha`-neighbour.  Together with the absence of both colours on
`N_H(x)` and colour six on `u`, this proves the complete contact table
(1.3).

## 2. The induced crossing cycle

The Kempe interchange on all bichromatic components meeting `A` is
sound.  Under the contrary assumption, it changes every
`alpha`-neighbour of `x` to `beta` and changes no `beta`-neighbour of
`x` to `alpha`, because the latter neighbours are exactly the members of
`B` and none lies in a switched component.  It would leave colour
`alpha` absent from `N_G(x)`, allowing `x` to be coloured and
contradicting `chi(G)=7`.

For a shortest `A`--`B` path `P` in a crossing bichromatic component,
the internal avoidance claim is exact.  By (1.3), every vertex of
`N_G(x)` carrying colour `alpha` or `beta` lies in `A union B`; vertices
of the other colours cannot occur on `P`.  An internal member of `A` or
`B` would shorten the set-to-set path.  Hence

\[
                 V(P-\partial P)\cap N_G(x)=\varnothing.
\]

A chord of `P` would also be an edge of the induced bichromatic graph and
would shorten `P`.  Its ends have different colours, so its length is
odd.  The only edges from `x` to `P` meet its two ends.  Thus `P+x` is
the claimed induced odd cycle, with no hidden neighbour of `x` in its
interior.

## 3. Antipodal flip-cube argument

Interchanging the colour names `alpha,beta` after switching the boundary
components indexed by `S` switches exactly the complementary set.  Extend
this palette permutation by fixing colour six.  Extension through a fixed
exterior component is invariant under the permutation, proving
`r(S)=r(I-S)`.

The cube-cut proof is complete.  The edge `emptyset--{0}` changes the
rejector.  Dimension one would make its endpoints antipodal, contradicting
the preceding identity.  If every cube vertex had cut degree at most one,
the even cut parity in each square containing a chosen coordinate-`i`
cut edge would force the opposite coordinate-`i` edge to be cut.
Propagation makes every coordinate-`i` edge a cut edge.  The degree-one
assumption then forbids cuts in every other coordinate, so the rejector
depends only on bit `i`; complementation changes that bit and contradicts
antipodal invariance.  Therefore one vertex has rejector-changing edges in
two distinct coordinates, exactly as asserted in (1.5).

## 4. One fixed accepted extension

At the central cube vertex, `E` rejects `theta` and `F` accepts it.  At
either selected neighbouring cube vertex, the two labels reverse.  In any
fixed `theta`-extension through `F`, the full two-colour component meeting
`W_k` must meet another boundary two-colour component; otherwise switching
that full component would extend the boundary colouring that `F` rejects.
This necessity holds simultaneously for `k=i,j` in the same extension.

If the two full components coincide, outcome 3(a) follows.  Otherwise they
are disjoint and anticomplete: every edge between vertices coloured
`alpha,beta` either violates properness or joins the two components.
Shortest paths to another boundary component consequently have open
interiors in `F`, disjoint pairs of boundary-component endpoints, and
distinct nonedge endpoint pairs `f_i,f_j`.

For either one selected coordinate, the switched colouring is accepted by
`E` while `theta` is rejected there.  Reverse lifting supplies `Q` with
open interior in `E`.  Since `E,F` are different components of
`G-N[u]`, that interior is disjoint from and anticomplete to both
`F`-path interiors.  Thus all three open interiors are pairwise disjoint
and pairwise anticomplete, as the theorem states.

## 5. Compatible contraction and the repeated-pair alternative

The three contractions are compatible even when boundary endpoints are
shared.  Each open interior is disjoint from the others; contract its path
edges toward one retained endpoint while leaving the final edge.  A shared
boundary endpoint remains one intended vertex of the boundary minor, and
two paths with the same pair merely produce the same simple added edge.
After deleting any surplus edges, this realizes `H+\mathcal E` as a minor
of `G-u`.

Every branch set in a `K_6` model of this augmented boundary contains at
least one vertex of `X`.  Its lifted branch set therefore remains adjacent
to `u`; adding `{u}` would create a `K_7` model in `G`.  This proves the
`K_6`-minor exclusion in (1.6).

The cardinality classification is also exact.  The two `F`-paths use
disjoint pairs of boundary components, so `f_i` and `f_j` are distinct.
The `E`-path starts in the operated component `W_k`; it can duplicate the
corresponding `f_k`, but it cannot duplicate the other disjoint pair.
Hence either:

1. `e` differs from both, yielding three distinct added nonedges; or
2. `e=f_k`, yielding bilateral paths with the same endpoints through
   different exterior components, plus the other supported nonedge.

Thus `2<=|mathcal E|<=3`, with repeated edges included only once.  No
claim of three distinct edges survives in the duplicate case, and no such
claim is made in the audited revision.

## Promotion note

The theorem at the recorded hash is suitable for promotion beside its
audit as a written, separately internally audited, nonterminal result.
Any mathematical alteration requires a new hash check and audit.  The
minor wording convention that the palette transposition fixes colour six
is explicit in this audit and implicit in the theorem's standard palette
renaming sentence; it does not affect the verdict.
