# Independent cold audit: `K_4` plus two vertices and one edge

**Verdict:** **GREEN.**

The prescribed-edge cycle lemma is valid, all three possible positions of
the normalized split edge are covered, and both stated applications have
the exact hypotheses needed.  No claim beyond the displayed mutual
core-defect obstruction is certified.

## 1. Deletion connectivity

Deleting the four vertices of `Q` from a seven-connected graph leaves a
three-connected graph: deleting any further set of at most two vertices
amounts to deleting at most six vertices from `G`.  The four distinct
vertices `x,y,u,v` remain, so the usual order requirement for
three-connectivity is also satisfied.

## 2. Cycle through a prescribed edge and two vertices

The auxiliary cycle claim is correct.

First, a two-connected graph has a cycle containing any prescribed edge
`uv` and any further vertex `x`.  Start with a cycle containing `uv`; if
`x` is outside it, a two-fan from `x` to the cycle and the one fan-end arc
containing `uv` give the required cycle.

Now let `y` be outside that cycle and take a three-fan from `y` to three
distinct cycle vertices.  Those ends divide the cycle into three
edge-disjoint intervals.  The vertex `x` lies in the open interior of at
most one interval, while the edge `uv` belongs to exactly one interval.
At least one interval has neither obstruction.  Replacing that interval
by the corresponding two fan paths retains `x` and the literal edge `uv`
and adds `y`.  If `x` is a fan end, it lies on the complementary closed
arc automatically.  Thus endpoint coincidences do not create an omitted
case.

Computational counterexample search is unnecessary for this step: the fan
argument explicitly constructs the cycle from the defining
three-connectivity property.

## 3. Branch bags on the cycle

The cycle contains four distinct vertices `u,v,x,y`, so contracting its
edge `uv` leaves a cycle with three distinct marked objects.  Cutting one
edge in each of the three marked-object arcs leaves three nonempty,
connected, vertex-disjoint path bags.  In a cycle split into three
segments, every pair of segments is consecutive, so the three bags are
pairwise adjacent through the three cut edges.

Undoing the temporary contraction places both `u,v` in one connected bag.
That bag contacts every vertex of `Q` collectively; the other two bags
contact `Q` through their roots `x,y`.  The four `Q` singleton bags are a
clique and are disjoint from the cycle bags.  Hence all seven branch-set
conditions are literal.

## 4. Normalized six-support lemma

A spanning `K_5` model on six vertices has one two-vertex edge bag and four
singleton bags.  Up to interchanging `r,s`, there are exactly three split
edge positions.

1. If the split edge is `rs`, model adjacency directly says it is
   `Q`-full.
2. If it is `qr` with `q in Q`, the singleton clique is
   `(Q-{q}) union {s}`.  Thus `s` is complete to `Q-{q}`.  The edge bag
   must contact `s`; the contact cannot be `qs`, since that would make
   `Q union {s}` a literal `K_5`.  Hence it is `rs`, and `{r,s}` contacts
   `q` through `rq` and the rest of `Q` through `s`.
3. If it is `q_1q_2` inside `Q`, the singleton clique contains `r,s` and
   the other two vertices of `Q`, so `rs` is an edge.  Each of `r,s` must
   see one split endpoint.  No split endpoint can see both, or it plus the
   singleton clique is a literal `K_5`.  The contacts therefore form a
   matching and collectively cover `q_1,q_2`; the other two contacts are
   already in the singleton clique.

This exhausts the cases and proves Lemma 2.1.

## 5. Applications and trust boundary

In Corollary 3.1 the literal arms make `X` a `K_4` and make `p,q`
`X`-complete.  The equality `|A cap X|=4=|X|` gives
`A=X union {r,s}`.  Irredundancy is explicitly assumed as “contains no
literal `K_5`,” so Lemma 2.1 supplies the required `X`-full edge `rs`.
Theorem 1.1 applies exactly.

For each forced common-five-set support, its normalized split edge is full
to its singleton `K_4`.  If both other roots were complete to that core,
Theorem 1.1 would apply because those roots lie outside the six-vertex
support and hence are disjoint from its split edge.  Therefore condition
(4.1) is a correct necessary condition for survival.

Condition (4.1) is not claimed sufficient, impossible, or recursively
ranked.  The audit certifies only the theorem, maximum-overlap corollary,
and this necessary labelled obstruction.
