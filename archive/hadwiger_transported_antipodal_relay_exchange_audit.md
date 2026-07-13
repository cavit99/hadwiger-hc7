# Independent audit: transported antipodal relay exchange

## Verdict

**GREEN**, conditional on the already audited transported degree-eight
setup, the old-boundary prism description, and the minimum-degree/fullness
facts for a hypothetical minimal `HC_7` counterexample.

The six-bag construction in
`hadwiger_transported_antipodal_relay_exchange.md` is literal and covers
every possible position of the sole `R` defect.  It does not use stronger
connectivity than the transported setup and it does not identify a palette
label with a model bag.

## 1. The five base bags

Write the prism triangles as
`{a,a_1,a_2}` and `{b,b_1,b_2}`, with matching edges `ab,a_1b_1,a_2b_2`.
For

\[
 X_i=\{a_i,b_i,t_i\},\qquad
 t_i\in\{y_{a_i},y_{b_i}\},
\]

connectivity follows from `a_i b_i` and the appropriate private-relay
edge.  The bags `X_1,X_2` are adjacent through (for example) `a_1a_2`.
Each sees `{a}` through `a_i a` and `{b}` through `b_i b`.  Thus
`{a},{b},X_1,X_2` is a literal `K_4` row.  The fifth bag is `{z}` when
`z in P`, and `{z,y_z}` otherwise; it is adjacent to the row because `z`
is universal in the old boundary.  Every one of the five bags meets `U`.

This verifies both connectivity and all ten base-bag adjacencies.

## 2. The three generic defect classes

If `z in P`, a defect outside `P` can be avoided when choosing `t_1,t_2`,
and at least one of the five vertices of `U-P` remains unused and seen by
`R`.  Adding it to `R` makes the sixth bag connected and `U`-meeting.
If the defect is `p in P`, fullness of `D-u` supplies a neighbour
`r in {w} union {y_s:s in S-P}`.  Since `R` misses only `p`, it sees
`r`; choosing the one relay in each matching pair to avoid `r` leaves
`R union {r}` disjoint and adjacent to both `X_i`, while `pr` repairs the
sole missed singleton.  There is no `y_z` in this case because `z in P`.

If `z notin P` and the defect lies outside `{a,b,y_z}`, the same avoidance
argument applies.  The base uses five of the eight `U` vertices and at
most one of the three remaining vertices is missed, so a connected
sixth bag exists.  If the defect is `a` or `b` and a fullness neighbour
other than `y_z` exists, that neighbour supplies the same repair.  These
counts are exact; no hidden edge is assumed.

## 3. The missed `y_z` state

When `R` misses `y_z`, that relay has no edge to `R` or `H`.  Among old
boundary vertices outside `U`, it sees only `z`, because each
`s in S-P` has the unique `D`-portal `y_s`.  Together with its edge to
`u`, this gives exactly two possible neighbours outside `U`, so
minimum degree yields `d_{G[U]}(y_z)>=5`.

Only `a,b,t_1,t_2` among the seven other `U` vertices are committed to
other base bags.  Therefore an uncommitted neighbour `r` of `y_z`
exists.  Since the missed vertex is `y_z`, `R` sees `r`; hence
`R union {r}` is connected, is adjacent to the first, second, fourth and
fifth base bags through `R`, and is adjacent to `{z,y_z}` through
`r y_z`.  This case is sound.

## 4. The exact `a-y_z` lock

The only final state, up to symmetry, is

\[
 U-N_U(R)=\{a\},\qquad N_{D-u}(a)=\{y_z\}.
\]

The six displayed bags in equation (2.4) of the source note are disjoint
and connected:

* `{z,a_1,y_{a_1}}` uses the path `z-a_1-y_{a_1}`;
* `{a_2,b_2,y_{a_2}}` uses `b_2-a_2-y_{a_2}`;
* `H union {b_1,y_{b_1}}` is connected because `H` contacts `b_1`;
* `R union {y_z}` is connected because `R` sees every `U` vertex except
  `a`.

The first four bags are pairwise adjacent by the prism edges and the
universal vertex `z`.  Fullness of `H` joins the fifth bag to all four.
The sixth bag joins `{a}` by the forced edge `a y_z`, `{b}` through an
`R-b` edge, the third and fourth bags through the seen traces
`y_{a_1},y_{a_2}`, and the fifth through the seen trace `y_{b_1}`.
Thus all fifteen interbag adjacencies hold.  Each bag contains a distinct
vertex of `U`.

## 5. Scope

The theorem eliminates the entire antipodal transported two-shore row,
for arbitrary shore orders.  Together with the sole-shore theorem and
the locked-relay detour exchange, it eliminates every transported tight
hub-leaf configuration.  This is an infinite-family closure, but it is
not by itself a proof of `HC_7`: the hub-cycle alternative remains.
