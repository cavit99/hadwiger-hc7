# Independent audit: three-duty low-attachment descent

**Audit status:** separate internal mathematical audit; **GREEN**.

**Archive note:** The audited theorem remains valid, but maximal-union
normalization makes its outside-component hypothesis empty in the live
two-subgraph branch.  It is retained here for provenance rather than used
as a current proof dependency.

**Audited source:**
[`hc7_order8_three_duty_low_attachment_descent.md`](hc7_order8_three_duty_low_attachment_descent.md)

**Audited source SHA-256:**
`e09018f05abe67ceab8d00501b03a47306587ca1dc92494297af1d0fb6b69b93`

After this audit, the source status was changed only to record the GREEN
verdict and link to this file.  No hypothesis, conclusion, proof, scope, or
dependency changed.  The resulting source SHA-256 is
`486cb02de49594310e994e5bb7eb281a1c86eac9af337132a99d56b3c375d56e`.

This is an internal audit, not external peer review.  The theorem is an
unbounded conditional reduction and does not prove `HC_7`.

## Verdict

The three support assignments, the five-contact bound, the full-neighbourhood
identity, the edge-deletion response, and the invocation of the audited
small-boundary lobe theorem are all correct.  The three alternatives in item
3 exactly cover the dependency's outcomes, including an order-seven
separation whose connected component need not be `C`.  No unresolved
assumption or gap remains in the audited revision.

## 1. Components and ambient separation

Deleting `S` leaves the induced subgraphs on `L` and `R`, with no edge
between them.  Since `R` is nonempty and connected, it is a component of
`G-S`.  Since `L` is nonempty, `G-S` also has at least one component other
than `R`.  These are precisely the two component hypotheses needed when the
proof later invokes the small-boundary lobe descent.

For a component `C` of

```text
R-(V(Q0) union V(Q1)),
```

the vertex set `C` is nonempty and connected.  It is a proper subset of
`R`, because the two nonempty subgraphs `Q0,Q1` are disjoint from it.  Thus
every strict comparison with `R` is host-measured and literal.

## 2. Three-duty assignments and boundary count

Each of `Q0,Q1` is connected and adjacent to every vertex of `S`, so either
one supports each of `D,X,Y`.  The proof uses the following exact ordered
assignments:

```text
C supports D:  (C,Q0,Q1) supports (D,X,Y)
C supports X:  (Q0,C,Q1) supports (D,X,Y)
C supports Y:  (Q0,Q1,C) supports (D,X,Y).
```

The three selected subgraphs are nonempty, connected, and pairwise
vertex-disjoint in every line.  Therefore absence of a three-duty packing
forces `C` to support none of `D,X,Y`.

Failure of each duty supplies a boundary vertex missed by `C`.  The sets
`D,X,Y` are pairwise disjoint, so the three missed vertices are distinct.
As `|S|=8`, this gives exactly the claimed upper bound

```text
|N_G(C) intersect S| <= 8-3 = 5.
```

No assumption about the sizes of `X,Y` beyond their stated nonemptiness is
used.

## 3. Full neighbourhood and seven-connectivity

Componenthood after deleting `V(Q0) union V(Q1)` implies that every
neighbour of `C` in `R-C` lies in that deleted vertex set.  Consequently
`A=N_{G[R]}(C)` is exactly the set of attachments of `C` in `Q0 union Q1`.
There are no `L`--`R` edges, and the sets `A` and `S` are disjoint, so

```text
N_G(C) = A dot-union (N_G(C) intersect S),
|N_G(C)| <= |A|+5.
```

This full neighbourhood is a genuine separator.  Its selected open side
contains the nonempty connected set `C`, while the opposite open side
contains the nonempty set `L`.  Seven-connectivity therefore gives
`|N_G(C)|>=7`; the argument is not merely a quotient-neighbourhood count.

## 4. Exact-seven response from edge deletion

If `|A|<=2`, the upper and lower bounds force `|N_G(C)|=7`.  For every edge
`cv` from `C` to this boundary, edge deletion produces a proper minor
`G-cv`, hence a proper six-colouring `phi`.  The endpoints have the same
colour in every such colouring: otherwise restoring `cv` would give a
proper six-colouring of `G`, contrary to `chi(G)=7`.

The restriction of `phi` to the opposite closed shore is proper in the
intact graph, because the deleted edge has its `C`-endpoint outside that
shore.  Let `Pi` be its exact equality partition on `N_G(C)`.  If `Pi`
extended through the intact closed `C`-shore, a permutation of the six
colour names would align the boundary blocks and the two shore colourings
would glue to a six-colouring of `G`.  Thus the data satisfy the audited
definition of a generic exact-seven selected-response interface.

The response is strict relative to `R`: `C` is disjoint from the nonempty
subgraphs `Q0,Q1`, so `|C|<|R|`.  The same argument applies when `|A|=3`
and `|N_G(C)|=7`.

## 5. Small-boundary lobe descent

Assume `|A|=3` and `|N_G(C)|=8`.  The disjoint full-neighbourhood identity
then gives

```text
|N_{G[R]}(C)| + |N_G(C) intersect S| = 3+5 = 8.
```

All hypotheses of the audited small-boundary lobe theorem are present:

- the old boundary `S` has order eight;
- `R` is a component of `G-S`, and another component lies in `L`;
- `C` is a nonempty connected proper subset of `R`; and
- its internal and boundary neighbourhood orders sum to at most eight.

The dependency has two outcomes.  Its order-eight outcome makes `C` a
component behind the new boundary, makes every complementary component
full to that boundary, leaves exactly two or three components, and has
`|C|<|R|`.  This is the third alternative in item 3.

Its order-seven outcome can arise from another component of the complement
of `N_G(C)` which misses a new boundary vertex.  Because
`N_G(C)` already has order eight, that component is not `C`.  The audited
source therefore lists this actual order-seven separation separately and
does not claim an unjustified `C`-specific or strict response for it.  This
is exactly the trust boundary of the invoked theorem.

## 6. Consequence and scope

In an interface excluding every actual order-seven separation and every
strict boundary-full order-eight descent, neither `|A|<=2` nor any of the
three alternatives for `|A|=3` can survive.  Hence every residual component
has at least four distinct attachments in `Q0 union Q1`, as claimed.

The theorem does not produce a three-duty packing from that lower bound,
does not address the vacuous case `R=Q0 union Q1`, and does not preserve the
old boundary partition or the labels `d,e,X,Y` through a fresh generic
restart.  The source states all of these limitations explicitly.

The two invoked promoted dependencies were checked at their current audited
source revisions:

- generic exact-seven response restart:
  `e689c96686a936c27e58c2cba22d699c62ad649092eebfcdfc9c5db95a8e7b5`;
- small-boundary lobe descent:
  `de980671b3053459e4e11845e510e5d96bb0a4f18d1a8bd50fe4b9dfae996d52`.
