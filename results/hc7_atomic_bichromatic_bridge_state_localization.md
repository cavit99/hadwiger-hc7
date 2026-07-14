# Atomic bichromatic-bridge state localization

**Status:** proved and independently audited, including the
boundary-incidence extension.

This note localizes one exact trace transition to one literal rich-shore
edge.  It does not compose that transition with the compulsory edge
`zu`, and therefore does not close the atomic cell.

## 1. Setup

Let

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad |S|=7,
\]

with no `A-R` edge.  Assume every proper minor of `G` is six-colourable
and `R` contains two disjoint connected `S`-full packets.  Assume also
that `G` has no `K_7` minor.

Let `c` be a proper six-colouring of `G[R union S]`, and let `Pi` be its
exact equality partition on `S`.  Let `B,C in Pi` be two distinct blocks
with no literal edge between them.  Write their colours as `b,c`, and let

\[
                    K=G[R\cup S][c^{-1}(\{b,c\})].       \tag{1.1}
\]

Suppose `f=xy` is an edge of `K` with at least one end in `R` such that
`K-f` has no component
meeting both `B` and `C`, while the two components of `K-f` containing
`x,y` meet `B,C`, respectively.  Thus `f` is a literal separating edge
of the blocking bichromatic connection, not merely an edge of one chosen
shortest path.  Since `B,C` are anticomplete, `f` cannot have both ends in
`S`; it is either rich-internal or a literal boundary--rich incidence edge.

Let `Pi/BC` denote the partition obtained by replacing `B,C` with
`B union C`.  This is a proper boundary partition because `B union C` is
independent.

## 2. The localization theorem

### Theorem 2.1 (separating-edge state localization)

If

\[
                      d_{G[S]}(\Pi/BC)\le2,              \tag{2.1}
\]

then there is a proper six-colouring of both `G-f` and `G/f` whose exact
boundary partition on the literal set `S` is `Pi/BC`.

Equivalently, `Pi/BC` belongs to both the deletion and contraction state
families of the single literal edge `f`.  If `f` has a boundary end, the
contracted image retains that literal boundary label.

#### Proof

Delete `f` from the bichromatic graph `K`.  Interchange the colours
`b,c` on every component of `K-f` which meets `B`.

No such component meets `C` by hypothesis.  Every member of `B` changes
to colour `c`, every member of `C` retains colour `c`, and no other
boundary block uses either colour.  Hence the resulting colouring `c'`
of `G[R union S]-f` has exact boundary partition `Pi/BC`.

Orient `f=xy` so that the component of `K-f` containing `x` meets `B`
and the component containing `y` meets `C`.  The edge `xy` was
bichromatic under `c`.  Exactly the `x`-component is interchanged, so

\[
                              c'(x)=c'(y).                \tag{2.2}
\]

Apply exact packet reflection to `Pi/BC` using the two disjoint full
packets in `R`.  Condition (2.1) gives a proper six-colouring `a` of the
opposite closed shore `G[A union S]` with exact boundary partition
`Pi/BC`, unless the reflection itself displays a literal `K_7` model.
The latter is excluded by the setup, so the colouring case holds.

Permute the colours of `a` so that it agrees with `c'` on every literal
vertex of `S`.  There is no `A-R` edge, so the two colourings glue to a
proper six-colouring of `G-f`.  Equality (2.2) then identifies the ends
of `f`, and the same colouring descends to a proper six-colouring of
`G/f`.  When one end of `f` lies in `S`, its contracted image is simply
the labelled copy of that boundary vertex.  Both colourings therefore
retain the exact literal boundary partition `Pi/BC`.  \(\square\)

### Corollary 2.2 (same-state five-lock edge)

Assume additionally that `G` is not six-colourable.  In the colouring
of Theorem 2.1, put

\[
                         \gamma=c'(x)=c'(y).
\]

For each of the other five colours `delta`, the vertices `x,y` lie in
one `gamma-delta` Kempe component of `G-f`.  Thus the exact state
`Pi/BC` and all five literal `x-y` Kempe locks coexist in one full
proper-minor colouring.

#### Proof

If the `gamma-delta` component containing `x` did not contain `y`, swap
the two colours on that component.  The result would still colour `G-f`
but would give `x,y` different colours, so restoring `f` would
six-colour `G`.  \(\square\)

### Theorem 2.3 (the old-colour lock pulls back through the opposite shore)

Use the orientation in the proof of Theorem 2.1.  Thus `x` lies in a
component of `K-f` meeting `B`, `y` lies in one meeting `C`, and the swap
changes the `B`-colour `b` to the common colour `c` of `B union C`.

Every `c-b` Kempe `x-y` path in the full colouring of `G-f` supplied by
Theorem 2.1 has a subpath whose ends lie one in `B` and one in `C` and
whose internal vertices lie in `A`.  In particular, the localized
rich-shore edge forces a literal opposite-shore `B-C` connector in the
same exact compressed state.

#### Proof

Corollary 2.2 supplies a `c-b` path `Q` from `x` to `y` in `G-f`.  On
the rich closed shore, the passage from `c` to `c'` only interchanged the
names `b,c` on components.  It did not change the vertex set of the
two-colour graph.  Consequently, if `Q` lay in `R union S`, it would be
an `x-y` path in `K-f`, contrary to the fact that `f` separates the
chosen `B`- and `C`-components.  Hence `Q` meets `A`.

The colour `b` is absent from the literal boundary after the merge:
before the swap its only boundary block was `B`, and afterwards every
member of `B union C` has colour `c`.  Therefore every boundary vertex
of `Q` has colour `c` and lies in `B union C`.

Delete the vertices of `A` from `Q`.  Each remaining nonempty path
segment lies in one component of `K-f`.  The first segment lies in the
component containing `x` and has type `B`; the last lies in the
component containing `y` and has type `C`.

Components of `K-f` meeting neither `B` nor `C` may exist, but none can
occur in this segment sequence between two visits of `Q` to `A`.
Indeed, there is no `A-R` edge, so every entrance into or exit from `A`
along `Q` uses a literal vertex of `S`.  Every segment adjacent to an
`A`-subpath therefore contains a vertex of `S`; and every boundary
vertex on `Q` lies in `B union C`, as proved above.  Thus each such
segment lies in a component meeting `B` or `C`.  No component meets
both, so every segment has a unique type `B` or `C`.

Consecutive segments are joined along `Q` by a maximal subpath whose
internal vertices lie in `A` and whose two ends lie in `S`.  Excursions
whose ends lie in the same block are harmless: they preserve the type
of consecutive segments.  Since the type sequence starts with `B` and
ends with `C`, it has a first change of type.  The intervening maximal
`A`-subpath then has one end in `B`, the other in `C`, and all internal
vertices in `A`, as required.  \(\square\)

## 3. Final-two-duty form

Use the atomic trace notation

\[
                         S=I\mathbin{\dot\cup}J
                         \mathbin{\dot\cup}K_0,
\]

where `I,J` are independent and `K_0` is empty or a singleton clique.
Suppose an exact `I`-trace colouring has exactly two equality blocks
`B,C` meeting `J`, and the possible member of `K_0` is a singleton
block.  Then

\[
                       \Pi/BC= I\mid J
                       \quad\hbox{or}\quad
                       I\mid J\mid K_0.                  \tag{3.1}
\]

The first partition has demand at most two.  In the second, the retained
singleton is a clique of order one, so its demand is also at most two.
Consequently every separating edge with at least one rich end in the final
`B-C`
bichromatic connection satisfies Theorems 2.1, 2.3 and Corollary 2.2.

This is uniform in the length of the blocking path.  It replaces a
proper-minor state attached to a whole trace contraction by a canonical
compressed state attached to one literal edge of that path.

## 4. Exact remaining alternative

Let `K_{BC}` be the union of the components of the bichromatic graph
(1.1) which meet `B union C`.  If no edge separates `B` from `C`, the
edge form of Menger's theorem gives two edge-disjoint `B-C` paths in
`K_{BC}`.  Every separating edge has at least one end in `R`, because
`B,C` are anticomplete and hence no `S-S` edge joins the two colour
classes.  Therefore the final-two-duty branch has the exact dichotomy

\[
\boxed{
\begin{array}{c}
\text{one rich-internal or boundary-incidence separating edge carrying
the compressed state, five locks,
and an opposite-shore duty connector},
\\[1mm]
\text{or two edge-disjoint literal bichromatic routes.}
\end{array}}
\tag{4.1}
\]

The second outcome is an actual branching certificate, not a claim that
the two routes are internally vertex-disjoint or avoid the selected full
packets.

Theorem 2.1 does not force an intersection with the compulsory-edge state
family.  Indeed every live state returned by deleting the compulsory
edge `zu` has packet demand at least three, whereas the state in (3.1)
has demand at most two.  The next composition lemma must enlarge the
opposite-shore `B-C` connector, or decode the two-route alternative, into
legal adjacent carriers with the required literal `I,J` contact lists.
A failure of that enlargement must instead expose a canonical gate
giving a labelled near model, fixed pair, or strict state-carrying
descent.  Equality with the unrelated compulsory-edge family still
cannot be asserted.
