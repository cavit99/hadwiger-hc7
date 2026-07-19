# Independent audit of the first-hit exposure-collision alternative

**Verdict:** **GREEN** for Theorem 2.1, Corollary 2.2 and Proposition 3.1
at the exact corrected source revision below.

**Audited source:** `results/hc7_labelled_first_hit_exposure_collision.md`

**Audited source SHA-256:**

```text
78c8f35c75a652ed97b0263a16bad5f782089c46a652ec43d8989e30303b7911
```

The audited theorem and proof are unchanged; the refreshed hash records the
source status-line update made after the independent GREEN verdict.

This is a separate internal mathematical audit, not external peer review.
An earlier draft incorrectly asserted that contracting an arbitrary edge
between two model branch sets necessarily left a `K_6` model.  The audited
revision removes that assertion and proves the chromatic equality directly.

## 1. Rado deficiency and a surviving source

The clean first-hit setting incorporates `|P|>=5`.  Failure of a linkage
to all five labelled terminal classes therefore gives, by the audited
Rado--gammoid theorem, a nonempty index set `I`, a directed Menger set `Z`,
and

```text
|Z| <= |I|-1.
```

Since `|P|>=5>=|I|>|Z|`, some source survives.  Mapping nonterminal
members of `Z` to themselves and selected terminal-sink members to their
literal terminals is injective.  The component `C` containing a surviving
source is nonempty and lies wholly in `H-(T union F)` after deleting the
nonterminal members of `Z`.

Every nonterminal neighbour of `C` belongs to the literal image of `Z`.
A selected terminal adjacent to `C` must have its sink copy in `Z`, or a
path inside `C` followed by the last sink arc would avoid the Menger set.
The only remaining host neighbours lie in `F` or in unselected terminal
classes.  This proves the exact exposure containment (2.3).

At least one selected terminal sink is not in `Z`, because every selected
class is nonempty and `|T_I|>=|I|>|Z|`.  Its literal terminal is outside
`C` and outside the displayed exposure set.  Hence that set is a genuine
separator with nonempty sets on both sides.

## 2. The order-seven arithmetic and repeated exposure

If no unselected class contributes two exposed vertices, each of the
`5-|I|` unselected classes contributes at most one.  Together with
`|F|<=3` and the Rado bound,

```text
|N_H(C)| <= (|I|-1)+3+(5-|I|)=7.
```

Seven-connectivity gives the reverse lower bound for the full
neighbourhood of the nonempty component `C`.  Since that neighbourhood is
contained in the displayed separator of order at most seven, all
inequalities are equalities and the displayed set is exactly `N_H(C)`.
It is therefore the boundary of an actual order-seven separation.

If this case fails, the pigeonhole conclusion is exact: some unselected
terminal class contains two distinct vertices of `N_H(C)`.  Each such
vertex is a literal first hit.  A path from the surviving source inside
the connected set `C`, followed by the final edge to the terminal, has no
other vertex in `T union F`.  The theorem correctly makes no disjointness
claim for the two paths.

Corollary 2.2 draws only the resulting reduction.  It does not treat the
bare order-seven separation as terminal: compatible boundary colourings
remain necessary.  Nor does it assert the quoted collision exchange.  Its
extremal alternatives therefore have the correct logical status.

## 3. The model-preserving critical edge

Let the repeated exposed vertices `t_1,t_2` lie in one model branch set
`U_j`, while `C` lies in a different model branch set `D`.  Choosing
incident edges `e=c_1t_1` and `e'=c_2t_2` gives distinct edges because the
`U_j` endpoints are distinct.  Deleting `e` preserves the old
`D`--`U_j` branch-set adjacency through `e'`; internal connectivity and
all other model adjacencies are unchanged.  Thus the same spanning
labelled one-edge-deficient model survives.

Both `G-e` and `G/e` are proper minors, so they are six-colourable.  Neither
is five-colourable.  A five-colouring of `G-e` becomes a six-colouring of
`G` by recolouring one endpoint of `e` with a fresh sixth colour.  A
five-colouring of `G/e` expands to the two endpoints and the same fresh
recolouring again produces a six-colouring of `G`.  Both contradict the
hypothesis that `G` is not six-colourable.  Consequently

```text
chi(G-e)=chi(G/e)=6.
```

This proof no longer relies on an invalid claim that the contraction
automatically leaves a `K_6` model when the unique missing model adjacency
could be between two other branch sets.

## 4. Kempe connections and fixed-trace response

In every six-colouring of `G-e`, the endpoints of `e` have a common colour
`alpha`; distinct colours would permit `e` to be restored and would
six-colour `G`.  For any other palette colour `beta`, if the endpoints lay
in different `alpha`--`beta` components, swapping the two colours on the
component containing exactly one endpoint would make their colours
different.  Restoring `e` would again six-colour `G`.  Thus all five
bichromatic Kempe connections asserted in Proposition 3.1 are present in
each deletion colouring.

When `e` lies wholly in one open shore, the opposite closed-shore colouring
defines exactly the list assignment used by the audited fixed-trace
alignment theorem.  Membership or nonmembership of its labelled trace in
the response set of `G-e` gives the exhaustive attainment/rejection split.
In the attainment branch, the fixed-trace theorem indeed puts `e` in every
induced non-list-colourable obstruction for that trace.  The assertion is
about exact labelled colour values, not merely the equality partition.

## 5. Trust boundary

The result localizes a first-hit rank failure to either an actual
order-seven full-neighbourhood separation or two literal contacts in one
named branch set, and it converts the latter into one persistent critical
edge with five Kempe connections.  It does not make those connections
pairwise disjoint, identify their first model branch sets, force attainment
of the previously selected trace, or give compatible colourings on the
order-seven boundary.  The total-rejection branch may also lose the five
model labels under subsequent transfer.  These are explicit remaining
obligations, not conclusions of the audited theorem.
