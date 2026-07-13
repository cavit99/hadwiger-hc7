# Independent audit: exact three-packet quotient characterization

**Verdict:** GREEN.

## Verdict

**GREEN.**  Both equivalences are correct, all four packet-bag counts
`r=0,1,2,3` leave the asserted literal boundary anchors, and every quotient
model lifts to the stated packet configuration.  The supplied verifier
passes.  A separate run over all 1,044 unlabelled seven-vertex graphs, rather
than only the 685 `K_4`-free graphs used by the active application, found no
failure of either equivalence.

## 1. Easy directions

If `H-{x,y}` has a `K_4` model with bags `B_1,...,B_4`, then in `J_0(H)`

```text
{u_0,x}, {u_1,y}, {u_2}, B_1, B_2, B_3, B_4
```

are seven disjoint connected bags.  The first three are pairwise adjacent:
the first two use a universal-vertex edge to the other bag's anchor, and the
unanchored third bag uses `x` and `y`.  Universality joins each to every
`B_i`; the four boundary bags form the given model.

If `H-x` has a `K_4` model, the analogous bags in `J_1(H)` are

```text
{u_0,x}, {u_1}, {u_2}, B_1, B_2, B_3, B_4.
```

The edge `u_1u_2` supplies their mutual adjacency, while `x` joins the
`u_0` bag to each of them.  All remaining adjacencies again follow from
universality or the boundary model.

## 2. Necessity for `J_0(H)`

Let `r` be the number of model bags containing packet vertices.  The other
`7-r` bags lie wholly in `S`, so they are connected and pairwise adjacent in
`H`, not merely in the quotient.

* `r=0`: select four of seven boundary bags.  Three nonempty unused boundary
  bags leave at least three literal vertices outside the selected model.
* `r=1`: select four of six boundary bags.  Two nonempty unused bags give two
  distinct outside vertices.
* `r=2`: select four of five boundary bags, leaving one outside vertex in the
  fifth.  The two packet bags cannot be adjacent if both contain only packet
  vertices, since the packet vertices of `J_0` are independent.  Hence a
  packet bag contains a boundary vertex.  It is distinct from the fifth-bag
  vertex by branch-set disjointness and is also outside all four selected
  bags.
* `r=3`: the four boundary bags are selected.  Each packet bag contains one
  packet vertex.  If at most one packet bag contained a boundary vertex, the
  other two unanchored packet bags would be nonadjacent.  Thus at least two
  packet bags contain boundary vertices; branch-set disjointness makes those
  literal vertices distinct and outside the four selected bags.

In every case the selected bags are a `K_4` model avoiding two distinct
literal vertices `x,y`, proving `H-{x,y} \succeq K_4`.  The argument also
covers nonspanning models that omit one or more packet vertices.

## 3. Necessity for `J_1(H)`

For `r<=2`, there are at least five boundary bags.  Four form a `K_4` model,
and any literal vertex in a fifth nonempty bag is an avoided anchor `x`.

For `r=3`, there are exactly four boundary bags.  If all packet bags were
unanchored, the `u_0` bag would be nonadjacent to both other packet bags; the
single edge `u_1u_2` cannot repair either missing adjacency.  Therefore at
least one packet bag contains a literal boundary vertex `x`.  Disjointness
places `x` outside the four boundary bags, which consequently form a `K_4`
model in `H-x`.

Only existence of an anchor is used here.  A single anchor in an arbitrary
packet bag need not itself make the three packet bags pairwise adjacent, but
that stronger assertion is neither stated nor needed.

## 4. Literal lifting

Replacing a quotient vertex by its connected `S`-full packet preserves:

* connectivity of a singleton packet bag;
* connectivity of a packet--boundary bag, because every included literal
  boundary vertex has a neighbour in the packet;
* every packet--boundary adjacency, by fullness; and
* all boundary--boundary edges and branch-set disjointness.

In `J_0` no packet--packet edge has to be lifted.  In `J_1`, when the two
rich packets lie in the same connected open shore, a shortest path between
them has no internal vertex in either packet.  Assigning all path vertices
except the endpoint in the second packet to the first makes the two enlarged
packets adjacent while preserving connectedness, disjointness, and fullness.
Thus the artificial edge `u_1u_2` lifts whether its quotient endpoints lie
in one model bag or in two.

## 5. Verifier audit

The 5,880 masks are exactly the Stirling number `S(10,7)`, so they enumerate
all unordered partitions of the ten quotient vertices into seven nonempty
bags.  Restricting the search to spanning models is valid: each `J_i(H)` is
connected, and every component outside an arbitrary minor model has an edge
to a model bag; assigning that entire component to such a bag extends the
model without destroying any adjacency.

The connectedness and pairwise-adjacency tests on every partition are exact.
The active verifier reports:

```text
branch_partitions=5880
k4_free_boundaries=685
anchor_equivalence_checks=1370
closed_by_robust_or_exact_quotient=556
residual=129
```

It also reproduces the 33 additional one-anchor closures when the rich
packet edge is present.  As an extra falsification check, the same exact
quotient search and anchor tests were run over all 1,044 atlas graphs of
order seven; both equivalences held in every case.

## 6. Scope

The theorem is an exact characterization of these two **static** quotient
graphs.  It does not rule out a `K_7` model using additional internal shore
structure that disappears when each full packet is contracted to one
vertex, and it does not by itself close the remaining exact `(1,2)` cells.
