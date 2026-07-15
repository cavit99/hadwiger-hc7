# A `K_4` plus two vertices and one edge composes to `K_7`

**Status:** proved and independently cold-audited.

This is a reusable split-row extension of the common-`K_4` cycle
construction.  It also closes the maximum-overlap literal-arm cell in the
order-six rigid cross-arm outcome.

## 1. Edge-preserving cycle composition

### Theorem 1.1

Let `G` be seven-connected and let `Q` be a four-vertex clique.  Let
`x,y,u,v` be distinct vertices outside `Q` such that:

1. `x` and `y` are each complete to `Q`;
2. `uv` is an edge; and
3. for every `q in Q`, at least one of `u,v` is adjacent to `q`.

Then `G` contains a `K_7` minor.

### Proof

The graph `H=G-Q` is three-connected.  We first record that a
three-connected graph has a cycle containing any prescribed edge and any
two further prescribed vertices disjoint from that edge.

Indeed, start with a cycle containing the prescribed edge and the first
vertex.  Such a cycle follows by taking a two-fan from the vertex to a
cycle containing the edge and retaining the arc containing that edge.
If the second vertex is not on the resulting cycle, take a three-fan from
it to three distinct cycle vertices.  The three fan ends divide the old
cycle into three edge-disjoint intervals.  At most one interval has the
first prescribed vertex in its open interior, and exactly one contains the
prescribed edge.  Delete an interval having neither obstruction and use
the complementary arc with the two corresponding fan paths.  This gives a
cycle containing the edge and both vertices.

Apply this fact in `H` to the edge `uv` and the vertices `x,y`, obtaining a
cycle `D`.  Contract `uv` only for the purpose of viewing `D` as a cycle
through three marked objects: `uv`, `x`, and `y`.  Cut one edge in each of
the three open arcs between consecutive marked objects.  The three
resulting path bags are nonempty, connected, pairwise disjoint, and
pairwise adjacent through the three cut edges.  On undoing the temporary
contraction, one bag contains the whole edge `uv`; the other two contain
`x` and `y`, respectively.

The `x`-bag and `y`-bag are adjacent to every singleton vertex of `Q`
through their roots.  The `uv`-bag is adjacent to every such singleton by
hypothesis 3.  Together with the four singleton bags of the clique `Q`,
these are seven pairwise disjoint, connected and pairwise adjacent branch
sets.  They form a `K_7` model.  \(\square\)

## 2. A six-support over a prescribed `K_4`

### Lemma 2.1

Let `Q` be a four-clique and let `r,s` be two further vertices.  Suppose
`Q union {r,s}` supports a spanning `K_5` model and contains no literal
`K_5`.  Then `rs` is an edge and the edge bag `{r,s}` is collectively
adjacent to every vertex of `Q`.

### Proof

Choose a normalized spanning model.  It has one two-vertex edge bag `e`
and four singleton bags forming a clique.

If `e={r,s}`, the conclusion is exactly the model adjacency condition.
After interchanging `r,s` if necessary, suppose next that `e={q,r}` with
`q in Q`.  Then the singleton clique is
`(Q-{q}) union {s}`, so `s` is complete to `Q-{q}`.  The edge bag must
contact the singleton `s`.  If `qs` were an edge, `Q union {s}` would be a
literal `K_5`; hence `rs` is an edge.  The pair `{r,s}` contacts `q`
through `rq` and every other vertex of `Q` through `s`.

It remains that `e={q_1,q_2}` lies in `Q`.  The singleton clique contains
`r,s` and `Q-{q_1,q_2}`, so `rs` is an edge and both `r,s` are complete to
the other two vertices of `Q`.  Each of `r,s` must have a neighbour in
`{q_1,q_2}`.  Neither `q_i` can be adjacent to both `r,s`, since then that
`q_i` together with the four singleton bags would be a literal `K_5`.
Thus the two required contacts form a matching, and `{r,s}` collectively
contacts both `q_1,q_2`.  The conclusion follows.  \(\square\)

## 3. Maximum-overlap rigid-arm closure

### Corollary 3.1

In the rigid outcome of the corrected private-pair cross-arm theorem,
suppose:

* the avoided support `A` has order six and contains no literal `K_5`;
* the two near-identical arms have order five, so their common core `X`
  is a literal `K_4`; and
* `|A cap X|=4`.

Then `G` contains a `K_7` minor.  Consequently this cell cannot occur in
the `K_7`-minor-free support kernel.

### Proof

The two literal arms `X union {p}` and `X union {q}` make `p,q` complete
to `X`.  Write `A=X union {r,s}`.  Lemma 2.1 makes `rs` an `X`-full edge.
Theorem 1.1, with `Q=X`, now gives a `K_7` minor.  \(\square\)

## 4. Exact residual split-row obstruction

For a normalized irredundant six-vertex `K_5` support, the complement on
its support is a union of two nonempty, vertex-disjoint stars centred at
the endpoints of the split edge.  Equivalently, the split edge is
collectively adjacent to its singleton `K_4`, but neither endpoint can be
deleted to expose a literal `K_5`.

Apply this normalization to the three forced supports

\[
             U\cup\{a\},\qquad U\cup\{p\},\qquad
             U\cup\{q\},
\]

where `U=A-{a}`.  Write their split edges and singleton cores as
`(e_r,Q_r)` for `r in {a,p,q}`.  Theorem 1.1 gives the following exact
necessary condition for a surviving `K_7`-minor-free configuration:

\[
 \boxed{\text{For every }r,\text{ at least one of the other two roots is
 not complete to }Q_r.}                               \tag{4.1}
\]

Indeed, `e_r` is a `Q_r`-full edge, so two other `Q_r`-complete roots would
trigger Theorem 1.1.  Condition (4.1) is the irreducible labelled
**mutual core-defect obstruction**.  It is the precise point at which the
literal-root common-cycle proof stops: every available singleton `K_4`
has a named missing contact on at least one of the two other roots.

The remaining problem is to reroute one of those missing root-to-core
contacts without consuming the corresponding split edge.  No claim that
(4.1) is itself impossible is made here.
