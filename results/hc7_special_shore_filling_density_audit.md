# Independent audit of the special shore-filling density theorem

**Verdict:** GREEN for Theorems 2.1 and 3.1 in
[`hc7_special_shore_filling_density.md`](hc7_special_shore_filling_density.md)
at source SHA-256

```text
4f4dae9db11ed51ce33fe1054550cab8588360c1398e0954d76c9c3b0c3c65d9
```

This is a separate internal mathematical audit, not external peer review.

## 1. Boundary multiplicity and the density inequality

The double-contraction partition has demand greater than `nu_B\ge1`.
A boundary colour class of order seven gives demand one; a class of order
six leaves one singleton and again gives demand `2-1=1`.  Hence every
boundary colour class has order at most five.

For every shore vertex, a seen boundary colour consequently contributes at
most four neighbours beyond the first.  Thus the total repeated-colour
incidence satisfies

\[
                              P\le4C.
\]

The audited shore identities give

\[
                         P=3r+\Delta-E
\]

and the exact Mader count gives

\[
              2r+C-E+2s+2\Delta+4a\le40.
\]

The boundary is nonsplit, so it has at least two edges and `s\ge2`; the
opposite shore is nonempty, so `a\ge1`.  Therefore

\[
 2r+C-E+2\Delta\le32,
 \qquad
 C\ge\frac{3r+\Delta-E}{4}.
\]

Substitution and multiplication by four give exactly

\[
                         11r+9\Delta\le128+5E.
\]

The signs and the constant `128` are correct.  In the all-tight case
`E=0`, the absence of degree-seven/eight vertices makes `\Delta\ge0`, so
`r\le\lfloor128/11\rfloor=11`.

## 2. Gallai-tree endblocks

Since every `\varepsilon(v)` is nonnegative, `E=0` makes every vertex
tight.  The audited degree-choosability theorem then makes `G[A]` a Gallai
tree.

For an endblock with unique cutvertex `w`, its lobe `Q` has full
neighbourhood contained in `{w}\cup Y`.  Seven-connectivity forces at
least six boundary contacts.  Exactly six gives a literal order-seven
separation; absent that outcome, the lobe is `Y`-full.  Distinct endblock
lobes are disjoint, and the special exact-seven packing theorem gives
`nu_A\le2`.  A multi-block block-cutvertex tree therefore has exactly two
leaves and is a path.

## 3. Single-block case

A single Gallai block is a clique or an odd cycle.  For `K_n`, tightness
gives lists of order `n-1`.  An uncolourable such assignment has all lists
equal: every proper subfamily automatically satisfies Hall, so only the
full vertex family can fail, and that requires union size `n-1`.

The two marked vertices are adjacent and use distinct `psi`-colours.  Each
colour lies outside the common list because it equals the colour of the
corresponding boundary neighbour.  Thus `(n-1)+2\le6` and `n\le5`.
Degree excludes `K_2`; `K_1` cannot contain both marked vertices.  For
`K_3`, degree at least nine forces all seven boundary neighbours at all
three vertices, contradicting `nu_A\le2`.  Hence only `K_4,K_5` remain.

In an odd-cycle block every vertex has internal degree two.  Degree at
least nine again forces every vertex to meet all seven boundary vertices;
three singleton vertices then contradict `nu_A\le2`.  The odd-cycle case
is impossible.

## 4. Trust boundary

The theorem reduces the all-tight infinite branch to an order-seven
endblock separation or a block path of order at most eleven, with the
one-block case `K_4` or `K_5`.  It does not bound positive total excess,
align the new separation colourings, eliminate the bounded block paths, or
construct a `K_7`-minor model.  The separate odd-wheel barrier correctly
shows that the excess bound needs global minor-critical dynamics beyond
the local two-root list data.
