# Internal audit: opposite-shore single Kempe transition

**Verdict:** GREEN.

**Audited source:**
`results/hc7_opposite_shore_single_kempe_transition.md`

**SHA-256:**

```text
54b07b1173d828535e878b24a504fd86ddd0052a2681f500e8a159db30f02181
```

This is a separate internal mathematical audit, not external peer review.

## 1. Response orientation

The two deletion colourings are oriented correctly.  The colouring of
`G-e_D` restricts to a proper colouring of the unchanged closed side
`G[A union X]`, while the colouring of `G-e_A` restricts properly to the
unchanged side `G[D union X]`.  If a boundary interchange makes these
restrictions agree, they genuinely glue to a proper `q`-colouring of `G`.

## 2. Boundary Kempe lifting

Let `K` be the boundary two-colour component on which `gamma_D` is
interchanged.  In the `A`-closed side, if the full two-colour component
containing `K` meets no other boundary component, switching it changes the
boundary trace exactly to `gamma_A`, giving the forbidden gluing.  Hence it
meets another boundary component.  A shortest set-to-set path, stopped at
its first boundary vertex outside `K`, has every internal vertex in `A`.

The reverse argument in the `D`-closed side is identical.  Interchanging
the two colour names on `K` does not change the underlying boundary
two-colour graph.  The two path interiors lie in opposite open sides and
are therefore disjoint.  Distinct boundary two-colour components have no
two-colour edge between them, so both interiors are nonempty.  The theorem
correctly makes no claim that the boundary ends are distinct.

## 3. Order-eight consequence

Each nonempty connected path interior lies in one component `Q_Z` of
`G-X`, and `N_G(Q_Z) subseteq X`.  The opposite open side supplies a vertex
outside that component and its neighbourhood.  Seven-connectivity and
`|X|=8` therefore give `7<=|N_G(Q_Z)|<=8`.  Equality seven is an actual
cut; equality eight forces `N_G(Q_Z)=X`.  The supporting components are
distinct because they lie in disjoint open sides.

## 4. Same-edge deletion/contraction identity

Every `q`-colouring of `G-f` gives the ends `r,s` of `f` the same colour;
otherwise `f` could be restored.  For every other colour `beta`, the two
ends lie in one full `alpha`--`beta` component, since otherwise switching
the component containing only one end would again permit restoration of
`f`.  Contracting two vertices already in one such component cannot merge
two distinct components; colour pairs not using `alpha` are unchanged.
Thus the colouring bijection preserves every full Kempe component and
every interchange, as claimed.

## 5. Trust boundary

The result does not prove that suitable opposite-shore responses one
boundary move apart always exist.  It does not allocate either path to
minor-model labels, force distinct boundary ends, produce a common
partition, or close the order-seven output.  These limitations are stated
accurately.

No mathematical defect was found.
