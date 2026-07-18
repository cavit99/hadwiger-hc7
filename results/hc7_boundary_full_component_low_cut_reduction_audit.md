# Independent audit: low-order separators inside a boundary-full component

## Verdict

**GREEN** at the exact source revision

```text
b6205cae0d5ee6fe25a7258b3b8e3aa1894ce97d0fa348cef2c06935f5c24d87  results/hc7_boundary_full_component_low_cut_reduction.md
```

The full-neighbourhood equalities, every use of seven-connectivity, the
two-connected lobe attachments, the exact two-cut criterion, and both
exceptional-pattern classifications are correct.  No unresolved
mathematical assumption remains in this conditional structural reduction.

## 1. Boundary fullness and the cutvertex case

Because `D` is a component of `G-T`, all its external neighbours lie in
the seven-set `T`.  The assumed vertex outside `D union T` makes its full
neighbourhood a genuine separator.  Seven-connectivity therefore gives

```text
N_G(D)=T.
```

If `x` is a cutvertex and `A` is a component of `D-x`, connectedness of
`D` gives an actual `A-x` edge.  No vertex of `A` can have a neighbour in
another component of `D-x`, and no external neighbour lies outside `T`.
Hence

```text
N_G(A)={x} union N_T(A)
```

is an equality, not merely an inclusion.  Another component of `D-x` and
the vertex outside `D union T` both survive beyond this neighbourhood, so
seven-connectivity gives `|N_T(A)|>=6`.  Equality yields the asserted
order-seven separation.  Otherwise every component of `D-x` is
boundary-full; one connected component supplies a path adjacent to `b`
and `I`, and a second supplies the disjoint residual connected subgraph.

## 2. Attachments of a two-cut lobe

Let `D` be two-connected and let `Z={x,y}` separate it.  Every component
`A_h` of `D-Z` has a neighbour at both `x` and `y`.  If, for example, it
missed `x`, then `y` alone would separate `A_h` from another `Z`-lobe,
contradicting two-connectivity.  Consequently

```text
N_G(A_h)=Z union N_T(A_h).
```

This is again a literal equality.  The other lobes and the external
vertex make it a genuine separator, so seven-connectivity yields
`|N_T(A_h)|>=5`, equivalently `|delta(A_h)|<=2`.  Defect two gives an
actual order-seven boundary; the later analysis correctly restricts to
defect at most one.

## 3. Exact repair-versus-residual criterion

Under defect at most one, every lobe sees at least one member of the
two-set `I`.  The three admissible choices have the stated meanings:

1. with neither separator vertex consumed, a `b`-neighbour and an
   `I`-neighbour can be joined inside the connected repair lobe;
2. if `x` is consumed, an `x`-to-`I` path inside `A_c union {x}` together
   with `bx` gives the repair support; and
3. the case consuming `y` is symmetric.

Every unconsumed lobe is adjacent to every retained separator vertex.
Thus

```text
Z_w union union_{h != c} A_h
```

is connected and disjoint from the repair support.  A boundary vertex is
missed by it exactly when all retained lobes miss that vertex and every
retained separator vertex misses it.  This is precisely

```text
(intersection_{h != c} delta(A_h)) - N_T(Z_w).
```

Its emptiness is equivalent to criterion (3.7), proving both necessity
and sufficiency.

## 4. Exhaustion for two lobes

Classify by the number of lobes adjacent to `b`.

- If exactly one lobe sees `b`, the other has defect `{b}`.  Using the
  first lobe without consuming a separator vertex succeeds exactly when
  `x` or `y` sees `b`.  Its failure is pattern 1.
- If neither lobe sees `b`, both defects are `{b}`.  Boundary fullness
  forces at least one of `x,y` to see `b`.  A repair must consume one such
  vertex, and the residual sees `b` exactly when the other separator
  vertex also sees it.  Failure is pattern 2.
- If both lobes see `b`, either can be used without consuming `x,y`.
  Failure in both orientations requires two nonempty singleton defects,
  each missed by both separator vertices.  Boundary fullness excludes
  equal defects, giving exactly pattern 3.

In pattern 2, the unique separator vertex `z` seeing `b` is the unique
neighbour of `b` in `D`.  Two-connectivity makes `D-z` connected, and

```text
N_G(D-z) subseteq {z} union (T-{b}).
```

The right side has order seven and separates a nonempty connected set
from the external vertex.  Seven-connectivity forces equality, proving
(4.1).

## 5. Exhaustion for at least three lobes

The same count of `b`-adjacent lobes is exhaustive.

- With exactly one such lobe, all other defects are `{b}`.  Retaining both
  separator vertices repairs that common defect unless both miss `b`,
  which is pattern 1.
- With no such lobe, all defects are `{b}`.  Boundary fullness forces a
  separator contact, and consuming it leaves a full residual exactly when
  the other separator vertex also sees `b`.  The exceptional case is
  pattern 2 and gives (4.1).
- With at least two `b`-adjacent lobes, suppose an unconsumed-separator
  choice at `A_c` fails.  Then every other lobe has one common singleton
  defect `{t}`, missed by both separator vertices.  Boundary fullness
  forces `A_c` to see `t`.  Choosing a different `b`-adjacent lobe for the
  repair leaves `A_c` in the residual, so the intersection of the
  remaining defects is empty.  Criterion (3.7) then succeeds.

This proves that no additional exceptional pattern is omitted.

## 6. Unique portal and scope

If `t` has unique neighbour `z` in the two-connected graph `D`, then
`D-z` is connected and nonempty, misses `t`, and has no possible external
neighbour outside

```text
{z} union (T-{t}).
```

The candidate set has order seven.  The external vertex supplies the
opposite side, so seven-connectivity again upgrades the inclusion to the
equality in Lemma 5.1.

The source correctly limits its conclusion.  The repair support need not
preserve a previously selected labelled branch set, and the returned
order-seven separation carries no automatically compatible pair of shore
colourings.
