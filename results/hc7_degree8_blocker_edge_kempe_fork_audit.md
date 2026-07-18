# Audit: a boundary-edge obstruction yields three far-shore Kempe connections

## Verdict

**GREEN** at the exact source revision

```text
ab33c617b53e45d6f881e932074e9c96ced3457bed8c3e699168899bcdfbb144  results/hc7_degree8_blocker_edge_kempe_fork.md
```

The four connected subgraphs are explicitly contained in the closed shore
`G[L union I union J]`.  The two simultaneous contractions are valid in
the original graph, their minor
colouring pulls back to a proper colouring of exactly
`G[R union T]-F_b`, every edge of `F_b` is restored by the stated Kempe
interchange, and the five-row reflection theorem applies.  The three
colour-indexed paths and their intersection restrictions follow.  No
unresolved mathematical assumption remains in this conditional theorem.

## 1. Construction and contraction of the two supports

The induced subgraph on `V(C_0) union V(C_2) union {b}` is connected
because `b` has a neighbour in each of the two connected sets.  It is
`X_I`, and the exact traces of the two disjoint `C_s` give

```text
X_I intersect T = I union {b}.
```

The same argument gives `X_J` on `V(C_1) union V(C_3) union {q}`, with
trace `J union {q}`.  The four
`C_s` are pairwise disjoint, and the boundary traces and `b ne q` prevent
an intersection between `X_I` and `X_J`.  Each support contains at least
one selected contact edge.  Contracting spanning trees of the two disjoint
supports therefore strictly reduces the graph and gives a proper minor.

The contractions must, and do, take place in the original graph `G`.
An edge of `F_b` can be the selected edge joining `b` to one of the two
rooted connected subgraphs; deleting `F_b` first could disconnect `X_I`.
This causes no pullback problem because all internal vertices of the two
supports lie in `L`.  Every vertex of `R` remains literal in the minor.

## 2. Properness of the defective far-shore colouring

Expand only the literal boundary trace of each representative and discard
the internal vertices in `L`.  The resulting colouring of
`G[R union T]-F_b` is proper:

1. `I` is independent and deletion of all of `F_b` makes
   `I union {b}` independent;
2. `J union {q}` is independent by hypothesis;
3. an edge from an expanded boundary vertex to an unchanged vertex of
   `R union T` survived at the relevant contraction representative; and
4. an edge between the two expanded traces survived between the two
   representatives.

The final assumption that `X_I` and `X_J` are adjacent therefore forces
their representative colours to be distinct.  This verifies both the
properness and the distinct-support-colour claim in Lemma 2.1.

## 3. Restoring all blocker edges by a Kempe interchange

The boundary consists of the two monochromatic triples and `r`, so it uses
at most three colours.  Fix a colour `beta` absent from the boundary, and
let `K_beta` be the `alpha,beta` component containing `b` in the defective
far-shore colouring.

If `K_beta` misses `I`, swapping its two colours changes `b` from `alpha`
to `beta` while both vertices of `I` stay `alpha`.  Since

```text
F_b = E_G({b},I),
```

this single swap makes every deleted edge proper, not merely one selected
edge.  The trace `J union {q}` is unchanged: its colour differs from
`alpha`, and it cannot be `beta` because `beta` is absent from `T`.
Consequently the swapped colouring is genuinely proper on the unchanged
closed shore `G[R union T]`.

All five row traces are then monochromatic: `I` and `J` by construction,
and the other three because their traces have order at most one.  A row is
boundary-free.  These are exactly the two hypotheses of the independently
audited five-row reflection theorem at source revision

```text
31adbe5d6255d2424c3fd9aeb9f1cef52068ea4d9bfe1150dea12cdb6c93fb06  results/hc7_five_row_separator_reflection.md
```

Thus the two shore colourings align and glue.  In a non-six-colourable
host, every absent `beta` must instead have its `b`-component meet `I`.

## 4. Paths and intersections

A shortest path in that component from `b` to its first vertex of `I`
alternates between colours `alpha` and `beta`.  No boundary vertex has
colour `beta`.  Among boundary vertices of colour `alpha`, only
`I union {b}` and possibly `r` occur, because the colour on
`J union {q}` is distinct.  Stopping at the first vertex of `I` leaves at
most `r` as an internal boundary vertex.  If `r` is not `alpha`, every
internal vertex lies in `R`.

For different absent colours `beta,gamma`, a common vertex on the two
chosen paths must have colour in

```text
{alpha,beta} intersect {alpha,gamma} = {alpha}.
```

The qualification "away from their ends" is correct: `b` is a common end,
and two paths may end at the same member of `I`.  No claim of pairwise
disjointness follows.

## 5. Deleting the blocker set and the critical-edge response

The defective far-shore colouring can be matched on the opposite shore in
`G-F_b` by the carrier construction from the reflection proof.  Every
minor used there is a proper minor of `G`, since `F_b` is nonempty.
There is one small connectivity subcase to check.  If the distinguished
vertex `a` equals `b` and deletion of `F_b` removes all of its edges to
`Q_I`, assign the stipulated boundary-free row to the same equality block
as `I union {b}`.  That row is adjacent both to `b` and to `Q_I`, so the
corresponding carrier remains connected in `G-F_b`.  In all other cases
the deleted edges are not needed for an `a`-to-row contact.  Hence the
claimed global six-colouring of `G-F_b` is valid.

In the singleton case `F_b={e}`, any six-colouring of `G-e` gives its ends
the same colour, or the
colouring would already extend to `G`.  For each other colour, their two
colour components must coincide; otherwise a swap on the component of one
end makes `e` proper.  Recolouring one endpoint also proves that each end
has a neighbour of every other colour.  The critical-edge assertions in
Section 4 are therefore exact.

Finally, proper colourings of `G/e` are in bijection with proper colourings
of `G-e` in which the ends of `e` receive the same colour.  Lifting or
identifying those two ends gives the two directions.  Since every
six-colouring of `G-e` is of this form, the source correctly concludes that
deletion and contraction at this same edge do not yield two independent
boundary responses.

## 6. Trust boundary

This audit proves only the conditional proper-minor composition and its
three colour-indexed paths.  It does not prove that:

- the paths have distinct first hits in named connected sets;
- two of them are internally vertex-disjoint;
- an intersection in their union is a separator of `G`; or
- the degree-eight cyclic-sector configuration always satisfies the setup.

Those limitations are stated correctly in the source.
