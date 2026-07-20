# Independent audit: demand-two Hall responses on a two-piece shore

**Verdict:** **GREEN** for the exact source revision identified below.

This is a separate internal mathematical audit, not external peer review.
It checks every response orientation, the demand lower bound, the two exact
Hall-deficient incidence forms, the literal-neighbourhood count, and the
matching-or-smaller-side theorem.  The result is conditional and does not
prove `HC_7`.

## Audited revision

The audited source is
`results/hc7_order8_two_piece_hall_response_exchange.md` at SHA-256

```text
f16e7f08ea17cfd4e77c80dbf318fad24aa4621d796f39d9513be913f2c6ccc4
```

The mathematical revision audited directly had SHA-256
`917ce9baf93e9cebf8b5b2eefefe05276306ba25613bfb19562b385f0cdd0939`.
The final source differs from it only by replacing the pending-audit status
with the adjacent GREEN-audit link.  No hypothesis, conclusion, definition,
or proof step changed.  The mathematical revision itself differed from the
initially supplied revision only in the accurate final description of
outcome 3 as a singleton nonowner adjacent to every vertex of the old
eight-set `S`; it does not call that vertex full to the larger response
boundary `B`.

## 1. Inputs and invariant geometry

The audit checked the inherited GREEN source
`results/hc7_order8_positive_excess_frozen_outer_shore.md` at SHA-256

```text
b9e913fbece2258d4a9d8448c2ea414a5f2b76df7ab895ffe3a13a115becc9f3
```

and the transported-partition theorem at SHA-256

```text
e22e88a66d4a9eed07e1f86888adcb80c7ab826c03de99e4a5a830999f3ccbd4
```

The inherited geometry gives exactly

\[
 V(G)=E\mathbin{\dot\cup}B\mathbin{\dot\cup}C,
 \qquad E_G(E,C)=\varnothing,
 \qquad C=Q_0\mathbin{\dot\cup}Q_1.
\]

The sets `E,C,Q_0,Q_1` are connected, `Q_0,Q_1` are adjacent, every
`Q_i` is adjacent to all eight old vertices of `S`, and `C` is adjacent to
every vertex of `B=(S-{e}) dotcup W`.  Hence `E` and `C` are the two
components of `G-B`, while each `Q_i` has a nonempty opposite side.  These
facts justify every later full-neighbourhood separation and every gluing
argument.

## 2. Orientation and demand at least two

For an `E`--`B` edge, a six-colouring after deletion restricts properly to
the intact `C`-side.  Its boundary partition cannot extend through the
intact `E`-side, because such an extension would align with the `C`-side
restriction by a palette permutation and six-colour `G`.  Thus the
partition is legal on `C` and rejected on `E`.

In this orientation the whole connected set `C` is a universal support:
it is adjacent to every literal vertex of `B`.  If the full-subgraph demand
were one, the transported-partition theorem would reflect the partition
through the rejected shore, contradicting rejection.  The demand is not
zero: `|B|>=9`, while the colouring has at most six blocks, so at least one
block is nonsingleton and is not represented in any clique of singleton
blocks.  Therefore the demand is at least two.

For a `C`--`B` edge the argument reverses correctly.  The colouring is
legal on `E`, rejected on `C`, and the connected set `E` is adjacent to
every vertex of `B` because `B=N_G(E)`.  The same reflection argument gives
demand at least two.  This also verifies the two orientations used for the
one-edge colourings in the inherited incident-edge bypass proposition.

## 3. Exact two-by-two Hall forms

At demand exactly two, the two required blocks `C_1,C_2` form the right
side of a two-by-two incidence graph with supports `Q_0,Q_1`.  The inherited
theorem proves that this graph has no matching saturating both blocks.

If a right vertex has degree zero, source form 1 holds.  Otherwise both
right vertices have positive degree.  Hall failure then forces their union
of neighbours to have order one; after relabelling, `Q_0` is incident with
both blocks and `Q_1` with neither.  This is source form 2.  The forms are
disjoint and exhaustive.

Every absent incidence has a witness in `W`, because both supports meet all
seven members of `S-{e}`.  In form 1, witnesses missed by the two supports
are distinct: their equality would make the boundary-full union
`C=Q_0 dotcup Q_1` miss that same literal vertex.  Consequently the
opposite support meets each witness.  In form 2, the incident support meets
every vertex of both required sets, including each witness missed by the
nonowner.

If the two form-2 witnesses coincide, the common vertex lies in
`R_U(C_1) intersect R_U(C_2)`.  Since the partition blocks are disjoint,
this intersection consists precisely of singleton-clique vertices having
no boundary edge to either block.  The source's final assertion in Lemma
3.1 is therefore exact.

## 4. Literal neighbourhood identity and response rank

There are no `E`--`C` edges.  For each `Q_i`, all neighbours outside
`Q_i` lie either in `B` or in the disjoint opposite part `Q_{1-i}`.  The
support meets all seven vertices of `S-{e}` and misses exactly `m_i`
vertices of `W`; it has exactly `h_i` distinct neighbouring vertices in
the other part.  The two neighbour classes are disjoint, so

\[
 |N_G(Q_i)|=7+(|W|-m_i)+h_i=|B|+h_i-m_i.
\]

Deleting any edge from `Q_i` to its full neighbourhood gives a proper
minor colouring.  Its restriction is legal on the opposite closed side,
and the induced partition is rejected by the intact `Q_i`-side, since an
extension there would glue to a six-colouring of `G`.  Thus `Q_i` is a
response side, not merely a connected subset.

If `h_i<m_i`, its boundary order is smaller than `|B|`.  If `h_i=m_i`,
the boundary order is equal but `Q_i` is a proper subset of
`C=Q_0 dotcup Q_1`.  Both are strict decreases in the declared
lexicographic rank.  Outside that outcome, integrality gives
`h_i>=m_i+1` exactly as claimed.

## 5. Matching or smaller side

In Hall form 1, each support misses a boundary witness, so `m_0,m_1>=1`.
Failure of descent gives `h_0,h_1>=2`.  Hence at least two vertices in each
bipartition class of the cross-edge graph `J` are incident with an edge.
A bipartite graph of matching number at most one has all its edges incident
with one common vertex and therefore has only one incident vertex on one
side.  This is impossible, so `J` has a matching of order two.

In Hall form 2, orient `Q_1` as the unique nonincident support.  It misses a
witness, so `m_1>=1`, and failure of descent gives `h_1>=2`.  If `J` has no
matching of order two, all cross edges form a star.  Because at least two
vertices of `Q_0` are incident, its centre is one vertex `v` of `Q_1`.

For any component `A` of `Q_1-{v}`, there is no edge from `A` to `Q_0`, and
every neighbour of `A` inside `Q_1` is `v`.  Its boundary neighbours form a
subset of the `|B|-m_1` vertices met by `Q_1`; hence

\[
 |N_G(A)|\le |B|-m_1+1\le |B|.
\]

The same proper-minor restriction-and-rejection argument makes `A` a
response side.  A strict inequality lowers boundary order; equality keeps
the boundary order but has `A` properly contained in `C`.  Both contradict
failure of the first outcome.  Therefore `Q_1-{v}` is empty.  The remaining
outcome is exactly a singleton nonowner `Q_1={v}` which still has all old
`S`-contacts inherited from the normalization; it need not meet every
vertex of `W`.

## 6. Application and trust boundary

The colouring of `G-wu` in Section 6 is correctly oriented: it is legal on
the `C`-side and rejected by the intact `E`-side, so its exact-demand-two
case is governed by Theorem 5.1.  The symmetric one-edge partition is legal
on `E` and rejected by `C`, and independently has demand at least two.

The proof does not identify a Hall witness with either named bichromatic
component, convert the two-edge matching into the additional connected
subgraph required for reflection, or turn a singleton nonowner into a
`K_7`-minor model.  A smaller response side need not already have boundary
order seven or carry a partition extending through both intact shores.
Those limitations are stated explicitly.  Within the conditional theorem's
scope, no mathematical error or unresolved assumption was found.
