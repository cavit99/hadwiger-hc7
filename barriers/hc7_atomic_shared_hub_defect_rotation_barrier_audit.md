# Independent audit of the atomic shared-hub defect-rotation barrier

**Status:** separate internal audit GREEN, 21 July 2026.

This is an internal mathematical and computational audit, not external peer
review.

## Revisions audited

- barrier:
  [`hc7_atomic_shared_hub_defect_rotation_barrier.md`](hc7_atomic_shared_hub_defect_rotation_barrier.md)
- barrier SHA-256:
  `2f42d9f133f9ba37e674c8c53688a60a9e86b180d5d51d3a8b59b58dd705b180`
- retained checker:
  [`hc7_atomic_shared_hub_defect_rotation_verify.py`](hc7_atomic_shared_hub_defect_rotation_verify.py)
- checker SHA-256:
  `b7b637dae7d8ce61d94f2ac6b8ef11735a40ad7f449306582b7c1672d5521627`

## Verdict

GREEN.  The written barrier, its exact finite classification, and the
retained checker agree.  The checker was independently rerun with

```text
.venv/bin/python -B barriers/hc7_atomic_shared_hub_defect_rotation_verify.py
```

and returned the documented GREEN output, including all `1,716` choices of
seven branch vertices, no atomic strong immersion of length at most `27`,
and exactly the displayed route family at length `28`.

As a separate check of the most consequential negative calculation, I
reconstructed the thirteen-vertex graph independently and used a Z3
decreasing-depth encoding of seven nonempty, pairwise disjoint, connected,
pairwise adjacent branch sets.  The solver returned UNSAT.  This agrees with
the checker's independent spanning-partition oracle that the graph has no
`K_7` minor.

## Checks performed

1. The construction has thirteen vertices and thirty-four edges.  The four
   named subdivisions, their `f`- or `g`-anchor edges, the subdivided `fg`
   route, and the edges `eh,hx` agree with the note.  The displayed three
   colour classes are proper, `aef` is a triangle, and NetworkX returns
   vertex-connectivity three.
2. The eight displayed bags are nonempty, disjoint, connected, and spanning.
   Direct adjacency inspection gives exactly the three absent bag pairs
   `ab,cd,fg`; in particular, moving `h` into the `X`-bag consumes the only
   displayed `f`--`g` provenance route.
3. The original twenty-one routes use twenty-eight distinct edges, avoid all
   branch vertices internally, and have exactly one binary collision: `x`
   lies on the disjoint demands `ab,cd`.  The four subdivision vertices and
   `h` each have one internal transit role.
4. The clique-minor oracle canonically enumerates every spanning partition
   into seven nonempty blocks and checks connectedness and all twenty-one
   block adjacencies.  This is complete because the host is connected and
   every nonspanning clique-minor model can absorb each component outside
   its branch sets into an adjacent branch set.
5. The immersion search examines every branch set and every simple path
   whose interior avoids the other branches.  Edge masks enforce global
   edge-disjointness, and the usage vector enforces exactly one unit of
   collision excess.  For seven branches in a thirteen-vertex graph there
   are six nonbranch vertices, so an atomic strong immersion has at most
   seven internal transit roles and hence length at most `21+7=28`.  Thus
   the limits `L<=27` and `L=28` are exhaustive, not assumed search bounds.
6. Memoization in `find_atomic_routes` is sound: future feasibility depends
   only on the remaining demands, used-edge mask, per-vertex usage, and
   accumulated excess, all of which occur in the cache key.  The final
   enumeration deliberately uses no such memoization.  The hardened checker
   also compares its unique minimum solution directly with
   `original_routes()` after canonicalizing demand keys.
7. The lexicographic-potential conclusion is valid.  A weak immersion with
   `M=0` is a subdivision of `K_7`, excluded by the exact minor calculation.
   Matching `M=1,T=0` is precisely the enumerated atomic strong case, where
   `H=0`; the exhaustive length calculation therefore proves the stated
   global minimum and uniqueness.
8. The labelled strong lift of the rotated quotient fails for both choices
   of new collision label.  With literal root `x`, the `xe` and `xg` demand
   paths must both begin with `xh`; with literal root `h`, degree four is
   below the six distinct first edges required at an immersion branch
   vertex.  The exhaustive classification also excludes every alternative
   atomic strong lift at the minimum score.
9. Lemma 7.1 is correct.  Seven-connectivity makes `G-Z` connected.  If
   deleting `h` separates `f` from `g`, the seven distinct vertices
   `Z union {h}` form an actual order-seven separator.  Otherwise an
   `f`--`g` path exists in `G-Z-h`.  When that path meets the subdivision
   only at `f,g`, it repairs the `fg` adjacency after `h` is assigned to the
   `X`-bag; `eh` supplies `eX`, the two sides of the old `fg` route supply
   `fX,gX`, and all other subdivision routes retain their adjacencies.  The
   resulting eight bags have only `ab,cd` absent, and merging the `a`- and
   `c`-bags gives the displayed explicit `K_7` model.
10. The final contraction observation is also valid at host level: a cut of
    order at most six in `G/uv` must contain the contracted vertex, since
    otherwise it would already cut the seven-connected graph `G`.  Expanding
    that vertex to `u,v` gives a separator of order at most seven, hence
    exactly seven.

## Trust boundary

The finite graph is three-connected and three-colourable.  It does not
satisfy the seven-connected or contraction-critical hypotheses of a
hypothetical counterexample to `HC_7`, and it does not refute a theorem that
uses proper-minor colouring responses or additional host neighbours.  The
barrier proves that the bare quotient isomorphism
`K_8-{ab,cd,xe}` to `K_8-{ab,cd,fg}` is not by itself a well-founded
collision reduction.  Lemma 7.1 closes only the clean replacement path;
paths meeting other subdivision-route interiors remain the stated live
case.
