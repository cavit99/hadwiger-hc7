# Independent audit: both-missing neutral separator

## Verdict

**GREEN.**  The envelope construction gives an actual vertex separator
covered by the four neutral bags.  The order-seven fullness conclusion
uses only seven-connectivity and is exact.

## Checks

1. Every exterior component placed in `X` has an edge to the connected
   path `A`, so their union with `A` is connected.  Distinct exterior
   components need not meet one another.
2. Endpoint-shadow Corollary 4 applies component by component in the
   target-free nontrivial branch: each `A`-incident component is
   anticomplete to both twins.  Thus so is their union `X`.
3. An exterior component omitted from `X` has no edge to `A` by
   definition and no edge to an included exterior component because both
   are distinct components outside the old model union.  Therefore every
   external neighbour of `X` lies in an old model bag.  The twin
   absences leave only `U_1,...,U_4`.
4. With `S=N(X)`, the set `X` is a component of `G-S`.  The disjoint
   connected bags `B,C` survive outside `S` and an old model edge joins
   them, so they lie in another component.  Hence `S` is a genuine
   separator and has order at least seven.
5. The neutral bags are disjoint, so four of them covering at least seven
   cut vertices forces one to contain at least two distinct vertices.
   Every cut vertex has a literal neighbour in `X` by the definition of
   open neighbourhood; this is vertex multiplicity, not a count of bags.
6. If `|S|=7` and `s in S` misses a component `D` of `G-S`, then
   `S-{s}` separates `D` from `X`.  Any path leaving one component of
   `G-S` must use `S`; after the other six vertices are deleted, the only
   surviving candidate is `s`, which has no edge to `D`.  This forbidden
   order-six separator proves fullness to every component.

## Scope

For `|S|>7`, seven-connectivity does not imply that every cut vertex is
full to the opposite shore.  The theorem supplies a multiply hit neutral
bag but not a connected split of that bag preserving all six old labels.
That portal-peel/state-splice step remains open.
