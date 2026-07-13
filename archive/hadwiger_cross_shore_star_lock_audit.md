# Independent audit: cross-shore star lock

## Verdict

**GREEN**, with one harmless scope clarification: Theorem 3.1 should
state `m>=1`.  The simultaneous switching proof is valid even when
several selected colours coincide.  The theorem gives a genuine
full-palette lock on one component of a full adhesion.

It does **not** by itself close the descended repeated-pole covering
split.  The exact missing ambient axiom is a specified-side warehouse
breaker: either the palette-locked leaf must be selectable in one of the
two members of the covering split, or a lock forced into the opposite
full shore must have a boundary state compatible with the split-side
operation.  Neither conclusion follows from Theorems 1.1 or 3.1 because
the two split pieces are adjacent, not distinct components of the
adhesion.

## 1. The two-shore theorem

Contracting `x-d-h` is a legitimate proper minor: the star is connected,
and `d,h` are nonadjacent because they lie in distinct components of
`G-S`.  Expanding a colouring gives exactly a colouring of

\[
                         G-\{xd,xh\}
\]

with the three displayed vertices in one colour `alpha`.

A `D`-repair is a colouring of `G-xh` agreeing with the reference
colouring on `S`; it has restored `xd`.  An `H`-repair is symmetric.  If
both existed, use the `D`-repair on the closed `D` side and the `H`-repair
on the closed `H` side.  The restrictions agree literally on `S`, both
deleted edges are restored on the side whose colouring is retained, and
different open components are anticomplete.  This splices to an
`r`-colouring of `G`, so at most one repair exists.

If no `D`-repair exists and the `alpha/beta` component of `d` avoids
`S`, that component is contained in `D`.  Switching it fixes `S`, moves
`d` away from `alpha`, and permits restoration of `xd`; this is a
`D`-repair.  Thus all `r-1` bichromatic components meet `S`.  The
symmetric case is identical.  Theorem 1.1 is correct.

Corollary 1.2 is also correct.  If a selected leaf had no neighbour of
some other colour, recolouring that leaf alone would make the forbidden
repair.  Truncating a bichromatic component at its first boundary vertex
gives the claimed connected carrier.  No disjointness between carriers
is implied.

## 2. Multi-shore switching

Assume `m>=1`.  If no leaf is full-palette locked, choose for each `i` a
colour `beta_i` whose component `K_i` at `d_i` avoids `S`.  Then

\[
                         K_i\subseteq C_i.
\]

The sets `K_i` are pairwise anticomplete because the `C_i` are distinct
components of `G-S`.  Therefore all switches can be performed
simultaneously.  This remains true when `beta_i=beta_j`: the switched
sets are still disjoint unions of whole bichromatic components and have
no edge between them.  Every `d_i` changes away from `alpha`, `x` and
all of `S` stay fixed, and all deleted star edges can be restored.  The
result would colour `G`, a contradiction.  Theorem 3.1 is sound.

The proof would be false with arbitrary connected sets in place of the
components `C_i`.  Anticompleteness, not merely disjointness, is what
allows all Kempe switches to commute.

## 3. Composition with the SPQR descent

The descended state in `hadwiger_c6_spqr_exact7_descent.md` has exactly
two full shores `R,H` and a promoted boundary pole `x`.  The new transfer
theorem gives two distinct `x`-neighbours in (say) `R`; fullness gives an
`x`-neighbour in `H`.  Applying Theorem 1.1 therefore selects one of:

1. an `R`-leaf whose five bichromatic components all reach the literal
   adhesion; or
2. an `H`-leaf with the symmetric property.

This is genuine progress over five independently chosen Kempe witnesses:
one leaf owns all five palettes in one colouring.  But it does not say
that the selected leaf in `R` lies in a prescribed member `X` or `Y` of
the repeated-pole covering split.  More importantly, it is allowed to
select `H` every time.

The multi-shore theorem does not repair that issue by taking leaves in
`X,Y,H`: the sets `X,Y` are adjacent pieces of the same component `R`,
not components of `G-S`.  Their bichromatic components can meet or have
edges across the split, so the simultaneous-switch proof of Theorem 3.1
does not apply.

## 4. Why the alpha-hub/ear architectures survive this theorem

A full-palette lock only says that every `alpha/beta` carrier reaches
`S`.  All five carriers may share alpha-coloured vertices, and all may
reach `S` through one small portal region.  Thus the alpha-hub example
in `hadwiger_order8_tight_hall_palette_exchange.md` satisfies the local
conclusion after its leaves are given boundary continuations.  The
theorem selects the hubbed shore; it does not split the hub into two
protected columns.

Likewise, the one-label ear system in
`hadwiger_unique_interface_anchor_tight_cut.md` is compatible with one
full-palette locked endpoint.  Its five ears can all be present while
the contracted boundary quotient remains `K_7`-negative.  The new lock
adds a simultaneous palette label to those ears, but no theorem yet
forces two of them to be disjoint after their common alpha vertices are
removed.

Seven-connectivity rules out a hub only when the hub together with all
boundary exits has order at most six.  The star-lock theorem neither
bounds the number of exits nor says that all paths from the selected leaf
to the rest of its shore use the displayed alpha warehouse.  Therefore
one cannot infer a small separator from the lock alone.

## 5. Exact missing ambient axiom

The needed statement can be isolated without `C_6` labels.

> **Specified-side warehouse exchange.**  Let a seven-connected,
> six-minor-critical, `K_7`-minor-free graph have a full exact
> seven-adhesion with shores `R,H`.  Suppose
> `R=X\dot\cup Y` is a connected covering negative split with strict
> interface surplus, and a boundary root `x` occurs in both contact
> rows.  For `x`-neighbours `a\in X,b\in Y`, the crossed operation
> states and a full-palette lock in `R` or `H` must yield one of:
>
> 1. two disjoint labelled palette columns completing the positive
>    quotient;
> 2. a nested exact seven-cut; or
> 3. the same equality partition from opposite boundary-faithful
>    operations.

What is missing beyond Theorem 3.1 is exactly one of the following
equivalent mechanisms:

* **side selection:** force the locked leaf to be `a` or `b` in the
  split shore, with at least one carrier crossing the split away from a
  common alpha warehouse; or
* **state transport:** if the opposite shore `H` is selected, transport
  its one-colouring five-palette lock through the strict split interface
  to the deletion/star state on `R`, forcing a common adhesion partition.

This is the ambient axiom that excludes the hub/ear counterarchitectures.
Ordinary fullness, seven-connectivity, and Theorem 3.1 do not supply it
separately.

## 6. Conclusion

The cross-shore star theorem is a correct and useful new uniform
rooted-carrier principle.  Composed with the SPQR descent it upgrades the
residue to one full-palette locked shore in a single proper-minor
colouring.  The remaining obstruction is no longer independent palette
selection, but the placement of one common alpha warehouse relative to
the repeated-pole covering split.  No `HC_7` closure follows until the
specified-side warehouse exchange above is proved.
