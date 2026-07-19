# Independent internal audit of three-owner component concentration

**Verdict:** GREEN for the exact source revision

```text
results/hc7_three_owner_reserved_component_concentration.md
SHA-256 d30971fa491a1264101cc949b0712e9b41d87f8879499e529a124403149aea9d
```

This is a separate internal mathematical audit, not external peer review.
The proof was also tested against the explicit `K_2`-join-icosahedron static
residue.  That example admits exactly the model reduction used here and is
therefore a guardrail, not a counterexample to the extremal theorem.

## 1. Connected retained donor

Every proper two-owner subfamily has two vertex-disjoint linkage paths.
Both meet the two-vertex transversal, so each uses a different transversal
vertex and neither can use both.  Their prefixes before the first
transversal vertex avoid the distinguished component, whose whole internal
neighbourhood is the transversal.  The prefixes connect both transversal
vertices through `B` to connected `U'`.

Every other component of the donor after deleting the transversal has a
neighbour in the transversal.  Hence all of `W-C`, together with `U'`,
induces one connected retained donor.  Its adjacency to `C` follows from
the exact internal-neighbourhood equality.

## 2. The zero- and one-exclusive cases

If no owner portal set is contained in `C`, moving `C` from the donor to
`D` is valid.  The set `D union C` is connected through the literal `C-D`
contact.  The retained donor meets every owner outside `C`, every nonowner
through `U'`, and `D union C` through the fixed response edge.

If exactly one owner is exclusive, moving all of `C` to that owner is
valid.  The enlarged owner is connected through its portal and meets the
retained donor through a `C-K` edge; every other owner keeps a portal in the
retained donor.

In both cases all outside branch-set adjacencies and prescribed roots remain.
Repairing the missing `X-Y` edge is terminal; otherwise the result is the
same compatible labelled near-complete model with a proper smaller donor.

The first-hit-rank argument is exact.  A ranked path with label other than
`U` avoided the whole old donor, including `C`.  A ranked `U`-path ending in
`C` is replaced inside the fixed connected response subgraph and then uses
the fixed edge into `U'`.  Thus the rank does not decrease.

## 3. The two-exclusive case

Let `R_1,R_2` be the two exclusive owners.  Their linkage paths use distinct
transversal vertices and, after entering `C`, cannot leave without either
revisiting their own transversal vertex or meeting the transversal vertex
already used by the other path.  Their terminal tails in `C` are therefore
disjoint and connected.

Every component left after deleting the two tails has an edge to their
union and may be assigned to an adjacent tail.  This partitions `C` into
two connected sets, each with its named owner portal and its edge to the
retained donor.  Enlarging the two owners by these sets preserves all labels,
roots, outside adjacencies, the fixed response subgraph and the relaxed
first-hit rank.  The third owner retains its outside-`C` portal.  The donor
strictly decreases unless the split directly repairs `X-Y` and gives a
`K_7` model.  Thus extremality excludes this case, and all three owner
portal sets lie in `C`.

## 4. Two-edge response substrate

Any two-owner linkage terminates at two distinct vertices of `C`, giving
vertex-disjoint contact edges into distinct owner branch sets.
Seven-connectivity implies that deleting those two edges leaves a connected
graph.  Colourings of the double contraction and the two single
contractions give the three signatures

```text
(equal,equal), (equal,proper), (proper,equal).
```

The fourth signature would be a six-colouring of the intact graph.  The
audited common-deletion theorem therefore applies and gives either a
literal `K_4` on the four endpoints or a six-chromatic common host with a
spanning `K_6`-minor model.

## 5. Trust boundary

The proof uses both `K_7`-minor exclusion and the global lexicographic model
choice: maximize the relaxed first-hit rank and then minimize the donor.
`K_7`-freeness alone does not force complete concentration.

The theorem does not align palette colours with the three owner labels,
make the bichromatic lock paths disjoint, preserve one boundary partition
across the two single-contraction responses, or complete `HC_7`.
