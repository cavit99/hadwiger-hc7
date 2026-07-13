# Independent audit: 3-connected Moser rural exchange

**Verdict:** GREEN, conditional only on the already-audited favourable
crossing and four-port linkage-or-disk inputs cited by the theorem.  The
carrier construction, contractions, exact boundary states, gluing, and
final colour for `v` are all valid.

I first tried to falsify the two interface lemmas by concentrating all
portals at one vertex, by allowing the two ears to reuse their ends in
`K`, and by putting additional vertices on each outer facial arc.  The
first construction violates exactly the displayed union condition; the
other two are allowed and do not invalidate the proofs.  I also checked
the three quotient states directly from their literal adjacency graphs.
No counterexample satisfying the stated hypotheses was found.

## 1. Interface lemmas

### Lemma 2.1

For two nonempty portal sets `N_K(a),N_K(b)`, the condition
`|N_K({a,b})|>=2` is exactly enough to choose distinct representatives:
failure would force both sets to be the same singleton.  Thus
`x-a-b-y` is an ear with distinct ends in the 2-connected graph `K`.
The same applies to `c-d`; its internal vertices are new and its distinct
ends remain in the original `K`, so overlap with endpoints of the first
ear is harmless.  Adding unused portal edges cannot create a cutvertex.

### Lemma 2.2

Because `Q` is two-connected, the outer-face boundary in the supplied disk
embedding is a simple cycle.  In the cyclic order `a,b,c,d`, the open
`a-b` arc avoiding `c,d` and open `c-d` arc avoiding `a,b` are disjoint.
The nonedges `ab,cd` make both interiors nonempty, and every internal
vertex belongs to `K`.  A shortest path inside connected `K` between the
two interiors can be truncated to meet them only at its ends.  Assigning
its internal vertices to the first carrier preserves disjointness,
connectedness, all four endpoint contacts, and supplies the required
carrier edge.  No planarity claim is used after that enlargement.

## 2. The rural complementary carriers

The cited favourable crossing gives the ordered four-port instance
`(1,3,4,2)`.  Its linkage pairs are therefore `1-4` and `3-2`, exactly the
two literal row duties in the cited crossed-page construction.  The
linkage outcome closes by the audited two-row completion.

In the disk outcome, `D` is full to every literal of `S`.  If
`|N_D({1,2})|<=1`, deleting

`N_D({1,2}) union (S-{1,2})`

removes at most six vertices.  The set `D-N_D({1,2})` is nonempty because
`|D|>=4`; it has no edge to the surviving literals `1,2`, and `D` has no
edge to `v` or `C`.  Hence this is genuinely a cut separating it from
`v,C`.  Seven-connectivity gives `|N_D({1,2})|>=2`; the argument for
`{3,4}` is identical.

The literal edges `12,34`, together with these two representative-pair
conditions, satisfy Lemma 2.1 and make
`Q=G[D union {1,2,3,4}]` two-connected.  Lemma 2.2 then applies in the
disk order `(1,3,4,2)` because `13,24` are Moser nonedges.  Its two
carriers are disjoint, connected, adjacent and literally contact the
independent blocks

`r={1,3}` and `e={2,4}`.

There are two different pairings here, and both are legitimate.  To prove
two-connectivity, Lemma 2.1 is instantiated as

`(a,b,c,d)=(1,2,3,4)`,

using the present edges `12,34`.  Only afterwards is Lemma 2.2 instantiated
as `(a,b,c,d)=(1,3,4,2)`, using the absent consecutive pairs `13,42` in the
supplied disk order.  No virtual edge is carried from one instantiation to
the other.

## 3. State returned from the crossed shore

The sets `{v} union r` and `C union e` are disjoint and connected; the
first is a star and the second uses fullness and connectedness of `C`.
They are adjacent by a `v-e` edge, so their simultaneous contraction is a
proper minor.

Both representatives see each of `0,5,6` (through `v` and `C`,
respectively), and they see one another.  Thus neither `r` nor `e` can
share a colour with any of `0,5,6`, or with each other.  Since the only
edge in `G[{0,5,6}]` is `56`, the complete and exact list of possible
equality partitions is precisely `R_0,R_5,R_6` in (4.2).  Pulling the
representative colours back to `r,e` is proper because both are
independent and every relevant shore edge survives at the representative.

More explicitly, `0` either has a third colour, the colour of `5`, or the
colour of `6`; it cannot have both latter colours because `56` is an edge.
It cannot use either representative colour because both representatives
are adjacent to `0`.  These are respectively

```text
R0 = 13 | 24 | 0  | 5 | 6,
R5 = 13 | 24 | 05 | 6,
R6 = 13 | 24 | 06 | 5.
```

The first contracted set is connected through the star at `v`.  The second
is connected because the full connected component `C` has a portal from
each of `2,4`.  Both contractions strictly reduce the graph, so the invoked
minor really is proper.

## 4. Reflection through the rural shore

For each `q`, the three contracted sets in (5.2) are pairwise disjoint and
connected.  The `X-Y` edge joins the first two representatives, and `v`
joins the star representative to both boundary blocks.

The displayed cliques are literal:

* for `q=0`, the five blocks
  `X+r`, `Y+e`, `v+0`, `5`, `6` form a `K_5`; the four carrier-to-singleton
  edges are `35,16,45,26`, the star sees `5,6` through `v`, and `56` is
  literal;
* for `q=5`, the four blocks with literal `6` form a `K_4`, using `16,26`
  and `v6` (or `56`); and
* for `q=6`, the symmetric `K_4` with literal `5` uses `35,45` and `v5`
  (or `65`).

Consequently every minor colouring forces distinct colours on exactly the
blocks of the requested `R_q`; expanding the independent blocks remains
proper on the unchanged closed `C`-shore.  Vertices of `D` not used by
`X,Y` may remain in the minor but are simply discarded when restricting
to that shore, which causes no problem.

For expansion, note that `13`, `24`, `05`, and `06` are all literal Moser
nonedges.  Every edge from one of these blocks to the unchanged component
`C`, and every edge between two displayed boundary blocks, becomes an edge
at the corresponding contracted representative.  Hence assigning the
representative colour back to every literal in its independent block is a
proper colouring, not merely an equality pattern on an abstract quotient.

## 5. Gluing and last colour

Equality of exact partitions gives a bijection between the boundary-block
colours in the two six-colourings.  Since there are at most five blocks,
that bijection extends to a permutation of all six colours.  After the
permutation the colourings agree on every literal vertex of `S` and glue,
because `C,D` are anticomplete.

Every `R_q` has at most five blocks, so one palette colour is absent from
`S`.  As `N_G(v)=S`, assigning that colour to `v` is proper.  This yields
the claimed contradiction.

## 6. Trust boundary

The theorem closes the unbounded 3-connected rural component only when the
opposite component supplies the specific favourable disjoint paths
`0-5` and `2-4`.  It does not establish that an arbitrary crossed
five-root frame can be normalized to that pair.  The theorem states this
remaining multi-frame gap accurately.
