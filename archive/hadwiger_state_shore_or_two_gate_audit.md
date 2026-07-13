# Adversarial audit: state shore or two-gate theorem

## Verdict

**GREEN.**  The protected-source Menger assertion is valid even when the
portal sets overlap, target portals coincide with source portals, or the
only relevant paths have order one.  The shortest-connector construction
and the universal two-gate consequence are also correct.

## 1. Protected-source linkage

Use a supersource with capacity-one arcs to the protected vertices
`alpha,gamma`, give those two vertices infinite internal capacity, split
every vertex of `D` with capacity one, and connect the `B` outputs to a
sink.  Direct the source-to-portal arcs away from the protected sources,
so neither protected source can occur internally on the other path.

An integral flow of value two is exactly two vertex-disjoint paths with
distinct protected-source ends and distinct `B` ends.  If it does not
exist, connectedness and nonempty portals give a flow of value at least
one.  Hence a minimum cut has capacity one.

Such a cut cannot be just `s-alpha` or `s-gamma`: the other protected
source still has a path through the connected graph to a `B` portal, and
no other finite-capacity arc would have been cut.  Therefore the cut is
the split arc of one vertex `z_B` in `D`.  It separates both protected
sources from `B`, so it meets every `A`--`B` and every `C`--`B` path.
This is exactly every `(A union C)`--`B` path.

If a portal lies in both a source class and `B`, the corresponding
order-one path is represented by entering that portal and leaving through
its split arc.  Consequently a gate must equal that portal, unless another
order-one path avoids it.  Thus overlaps create no exception to the cut
argument.

## 2. Shore construction

After deleting `alpha,gamma` from a value-two linkage, the remainders
`P_A,P_C` are nonempty disjoint connected subgraphs meeting `A,B` and
`C,B`, respectively.  Their `B` ends are distinct.

If the subgraphs touch, they are already the two shores.  Otherwise a
shortest connector between them has all internal vertices outside both.
Putting all internal connector vertices into `P_A` preserves connectivity
and disjointness, while its final edge makes the enlarged `P_A` adjacent
to `P_C`.  All required portal incidences survive.  This verifies every
condition in the shore definition.

## 3. Two gates

Applying the first lemma to common class `B` and then after swapping
`B,C` gives gates `z_B,z_C` whenever neither shore state exists.  A
connected subgraph meeting `A,B,C` contains an `A`--`B` path and an
`A`--`C` path, so it contains both respective gates.  This remains true
when a path has order one or the two gates coincide.

If a component of `D-{z_B,z_C}` met all three portal classes, that
component itself would be a connected subgraph meeting all three while
avoiding the gates.  Hence every component is dark to at least one class.

## 4. Exhaustive overlap audit

`state_shore_two_gate_verify.py` checks every connected labelled graph
through order four and every ordered triple of nonempty, possibly
overlapping portal sets.  A gate is tested by deleting its vertex and
examining components, with intersections of the surviving source and
target sets treated as order-one paths.  It reports:

```text
connected graph / overlapping portal triples checked: 129650
```

Every instance satisfies each one-state shore-or-gate lemma and the
two-state theorem.

## Scope

The theorem extracts a typed split inside one connected carrier or an
internal gate of order at most two.  It does not create the parallel or
crossed two-contact matching between independently split carriers.  That
intercarrier compatibility, or a lift of the internal gates to a genuine
small adhesion of the full host, remains separate.

