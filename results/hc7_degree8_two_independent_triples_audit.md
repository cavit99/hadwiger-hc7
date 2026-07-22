# Audit: two independent boundary triples

**Audit type:** separate internal cold audit

**Verdict:** **GREEN**

Audited theorem:
[`hc7_degree8_two_independent_triples.md`](hc7_degree8_two_independent_triples.md)

Audited source SHA-256:

```text
0029fd42a57d520a6c8a319c330ef0ad0633d2fd36f7024fe977b44966d92632
```

## Simultaneous contractions and expansion

For either retained shore `P`, the sets

```text
A = {u} union I,
B = P' union T
```

are disjoint and connected.  The first is a star, and the second is
connected because the opposite exterior component `P'` is connected and
has a neighbour at every member of `T`.  Contracting spanning trees of
these two sets strictly reduces the graph, so proper-minor
six-colourability applies.

Expanding the first contraction vertex only over `I` and the second only
over `T`, while discarding `u` and `P'`, gives a proper colouring of the
intact retained closed shore.  Independence of `I` and `T` handles edges
within the expanded sets; every retained edge from either set to its
exterior was represented at the corresponding contraction vertex.  Edges
between `I` and `T` were represented between the two contraction vertices.

Those contraction vertices are adjacent through the edges from `u` to
`T`.  Each of `p,q` is adjacent to the first contraction vertex through
`u` and to the second through a neighbour in the full component `P'`.
Consequently `I` and `T` receive distinct colours, each is an exact
boundary colour class, and neither colour occurs at `p` or `q`.  This
proves that both response sets are nonempty with exactly the boundary
forms stated in (2.5).

## Opposite response types and the nonedge

If the two shores admitted the same equality type at `p,q`, their boundary
equality partitions would be identical.  A bijection between the colours
of the common blocks extends to a permutation of the six-colour palette,
even when some colours are absent from the boundary.  The aligned shore
colourings then glue across `X` to colour `G-u`, because `E,F` are distinct
components of `G-N[u]` and hence anticomplete.

The common boundary uses three colours in the merged case and four in the
split case.  A colour absent from `X` may therefore be assigned to `u`,
whose entire neighbourhood is `X`.  This would six-colour `G`, so the two
response sets are disjoint.  If `pq` were an edge, properness would force
both nonempty sets to equal `{not equal}`, contradicting disjointness.
Thus `pq` is a nonedge, and two nonempty disjoint subsets of the two
available types must be the two opposite singletons.

## The shore-confined two-colour path

In a split-type colouring, suppose `p,q` belonged to different components
on their two colours.  A Kempe interchange on the component containing
`p` would merge their colours.  It does not change the exact blocks `I,T`,
because neither of their boundary colours is one of the two exchanged
colours.  This would create the forbidden second response type on the same
shore.  Hence `p,q` lie in one two-colour component.

Only `p,q` use those two colours on `X`.  A shortest joining path therefore
has no internal boundary vertex.  Since `pq` is a nonedge, its open
interior is nonempty and lies wholly in the named retained component.

## Five-vertex classification

A five-vertex graph with three edges is either a triangle plus two isolated
vertices or a forest with two components.  In the forest case its component
orders are `4+1` or `3+2`.  The trees on four vertices are `P_4` and
`K_{1,3}`; the latter plus an isolated vertex has independence number four
and is excluded.  The `3+2` case is `P_3` disjoint-union `K_2`.  This gives
exactly the three graphs in (3.3).

For `K_3` disjoint-union `2K_1`, the two isolated vertices and one triangle
vertex form an independent triple whose complementary pair is an edge.
For `P_4` disjoint-union `K_1`, the isolated vertex and the two path ends
form such a triple, with the middle path edge as complement.  Theorem 2.1
excludes both choices, leaving precisely `P_3` disjoint-union `K_2`.

## Dependencies and unresolved limit

No external theorem is used.  The proof depends exactly on:

- `chi(G)=7` and six-colourability of every proper minor;
- a degree-eight vertex with the displayed eight-vertex neighbourhood;
- exactly two nonempty exterior components, both full to that boundary;
  and
- two disjoint independent boundary triples.

No gap remains in Theorem 2.1 or Corollary 3.1 at the audited hash.  The
result does not construct a rooted `K_5` or a `K_7`-minor model and does not
settle the surviving `P_3` disjoint-union `K_2` case.  It therefore does not
prove `HC_7` or an unrestricted seven-demand rooted-minor theorem.

The status-only promotion linking this audit has SHA-256
`a4261f328857366972c320ebfd3f2e1b22478fdcc17cb5df6d734a0e79b52f6c` and
makes no mathematical change to the audited revision.
