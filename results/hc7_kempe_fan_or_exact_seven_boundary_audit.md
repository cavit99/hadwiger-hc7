# Audit: three Kempe connections give a packing or an exact-seven boundary

## Verdict

**GREEN** at the exact source revision

```text
1c616beccaea3d798e6c1659ee0311247a5d78bf90c593acae2cb86d31cdd258  results/hc7_kempe_fan_or_exact_seven_boundary.md
```

The terminal-capacitated form of Menger's theorem is applied correctly:
give capacity one to nonterminals and capacity at least three to `b` and
the two vertices of `I`, and attach `I` to a supersink.  Integral paths may
share `b` and a final vertex of `I` but no other vertex.  If no packing of
three exists, a set `Z` of at most two nonterminals meets every
`b`--`I` path.

The first vertices after `b` on the three selected two-colour paths have
their three distinct absent colours.  They are therefore distinct vertices
of `R`, so one avoids `Z`.  Its component `A` inside the `b`-reachable part
of `R-Z` is nonempty, connected, and adjacent to `b`.  Every neighbour of
`A` is in \(Z\cup(T-I)\): an additional neighbour in `R-Z` would join the
same reachable component, a neighbour in `I` would give a `Z`-avoiding
`b`--`I` path, and `L` is anticomplete to `R`.  Restoring `F` does not change
this full-neighbourhood calculation because every edge of `F` has ends
`b` and `I`, neither in `A`.

The nonempty set `L` is outside \(A\cup N_G(A)\), so this is a genuine
separation.  Seven-connectivity forces equality throughout

\[
7\le |N_G(A)|\le |Z\cup(T-I)|\le 2+5=7.
\]

Hence `|Z|=2`, `Z` is disjoint from `T-I`, and the only possible boundary
vertex of `H` in `Z`, namely `r`, is excluded. Thus \(Z\subseteq R\) and

\[
N_G(A)=(T-I)\mathbin{\dot\cup}Z.
\]

All three selected paths meet this two-set.  One member lies on two paths,
and the intersection of their distinct two-colour palettes forces it to
have colour `alpha`.  Finally no edge of `F` lies in the closed graph on
\(A\cup N_G(A)\), since its `b`-end is on the boundary and its `I`-end is on
the opposite side.  The restricted six-colouring is therefore proper in
the original graph and has exactly the two asserted monochromatic boundary
subsets.  The theorem correctly leaves extension of this partition through
the opposite shore unresolved.
