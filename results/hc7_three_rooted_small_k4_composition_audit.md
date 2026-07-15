# Audit of three-rooted small-`K_4` composition

## Verdict

**GREEN.**  The connectivity loss, rooted-triangle construction, all
branch-set adjacencies, and the eight-vertex obstruction are correct.  The
theorem may be used exactly under its stated common-rooted-`K_4` hypothesis.

## 1. Connectivity after deleting the small support

Let

```text
W=V(D_1) union ... union V(D_4),   H=G-W.
```

The roots `a,p,q` do not lie in `W`, so `H` has at least three vertices.
The graph `H` is connected because otherwise `W`, of order at most five,
would separate `G`.  For every `z in V(H)`,

```text
H-z = G-(W union {z})
```

is connected because `|W union {z}|<=6` and `G` is seven-connected.
Consequently `H` is two-connected.  This is the exact connectivity needed;
the proof does not silently assume that `H` is three-connected.

## 2. The rooted `K_3` in `H`

The dependency on Lemma 1.1 of
[`hc7_global_split_model_composition.md`](hc7_global_split_model_composition.md)
is valid.  It can also be checked directly.  In `H-q`, choose an `a-p`
path `P`.  A two-fan from `q` to two distinct vertices of `P` exists by
two-connectivity.  Cutting `P` at an edge between the two fan ends gives
two disjoint connected bags containing `a` and `p`; the union of `q` with
the fan interiors gives the third.  The cut edge joins the first two bags,
and the last fan edges join the third bag to each of them.  This remains
valid when a fan end is one of `a,p` or a fan path has one edge.

Thus there are disjoint, connected, pairwise adjacent bags
`R_a,R_p,R_q` rooted at `a,p,q`.

## 3. Literal `K_7` branch sets

The four `D_i` are disjoint connected bags and are pairwise adjacent by
the definition of the given `K_4` model.  They are disjoint from every
`R_r`, because the latter lie in `H=G-W`.  For every
`r in {a,p,q}` and every `i`, the vertex `r` belongs to `R_r` and has a
neighbour in `D_i`; hence `R_r` and `D_i` are adjacent.  Together with the
pairwise adjacencies among the three rooted bags, this verifies every edge
of the claimed seven-bag model.

The application to a five-set `U` is also exact: a `K_4` model contained
in `G[U]` has total support at most five, so the theorem applies whenever
all three roots contact all four of its bags.

## 4. Eight-vertex obstruction

Write

```text
Q={u_1,u_2,u_3},   T={x,y},   R={a,p,q},   U=Q union T.
```

The only edges are those inside the triangle `Q`, all `Q-T` edges, and all
`T-R` edges.

For each `r in R`, the bag `{x,r}` is connected and is adjacent to each of
the singleton bags `u_1,u_2,u_3,y`: the edges to the `u_i` come from `x`,
and the edge to `y` comes from `r`.  The four singleton bags are pairwise
adjacent where required (`Q` is a triangle and `y` is complete to `Q`).
Hence they form the asserted support-six `K_5` model.

Every root has neighbourhood exactly `{x,y}` in `U`.  Therefore every bag
of a common root-contacted model in `U` would have to contain `x` or `y`.
Four disjoint bags cannot all do so, proving that no such rooted `K_4`
exists.

Finally, the graph has clique number four: `Q` together with either `x` or
`y` is a `K_4`, and the missing `xy`, `Q-R`, and `R-R` edges prevent a
larger clique.  Any `K_7` model in an eight-vertex graph has at least six
singleton branch sets, since seven nonempty disjoint bags use at most eight
vertices.  Those singleton bags would induce a literal `K_6`, contradicting
the clique-number calculation.  Thus the example has no `K_7` minor.

An independent exhaustive enumeration of connected disjoint branch sets
on these eight labelled vertices also returned zero common root-contacted
`K_4` models in `U` and zero `K_7` models; the proof above does not depend
on that computation.

## 5. Exact trust boundary

The result is a **composition** theorem, not an extraction theorem.  It
requires one common `K_4` model of total support at most five whose four
bags are each contacted by all three named roots.  Three separate
support-six `K_5` models do not imply that hypothesis; the eight-vertex
example proves precisely this failure.  Nor does the theorem by itself
produce a coherent global pair or a decreasing invariant.
