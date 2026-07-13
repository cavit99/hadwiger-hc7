# Audit: deficiency-pivot involution and the icosahedral balanced cycle

## Verdict

**GREEN in its stated scope.**  The general pivot is literally reversible,
the bag-size identity is correct, and the displayed two-cycle occurs in a
seven-connected `K_7`-minor-free coherent-two-apex graph.  The note makes
no claim that this graph is contraction-critical and no claim that the
cycle closes `HC_7`.

Audited source:
`hc7_near_k7_rotation_involution_barrier.md`.

## 1. General pivot

The forward branch bags are

\[
                         W,\ A\cup Z,\ F_1,\ldots,F_5.
\]

The checks are complete:

* `A union Z` is connected by the assumed `A-Z` edge;
* it meets old contacted rows through `A` and old missed rows through
  `Z`;
* `W` meets `A union Z` through the split edge;
* the only lost `W-F_j` spokes are exactly `Omega`.

For the reverse direction, if `j in Omega`, all old `U-F_j` edges have
their `U`-end in `Z`, because `U=W dotcup Z` and `W` is anticomplete to
`F_j`.  Thus the same `Z` repairs every current missing spoke.  Removing
`Z` from `A union Z` leaves the old connected bag `A`, whose exact
missing set is `M`.  The inverse therefore uses literal edges and does not
assume that contraction preserves a colouring.

The quadratic calculation is

\[
 (a+z)^2+w^2-a^2-(w+z)^2=2z(a-w).
\]

No lexicographic-minimality inference is drawn from this identity.  This
is important: centre order and quadratic dispersion move in opposite
directions, so minimizing one first gives no control of the other after a
rotation which worsens the first coordinate.

## 2. Ambient graph

The labelled graph in (2.1) is the standard icosahedral graph, hence
planar and five-connected.  In `G=K_2 vee I`:

* deletion of at most six vertices leaves a universal vertex unless both
  join vertices were deleted;
* if both were deleted, at most four icosahedral vertices were deleted,
  so five-connectivity leaves the remainder connected.

Thus `kappa(G)>=7`; since every icosahedral vertex has degree seven in
the join, in fact `kappa(G)=7`, although equality is not needed.

For minor exclusion, a `K_7` model has at most two bags containing the
two join vertices.  Removing those bags leaves at least five pairwise
adjacent connected bags contained in `I`, a `K_5` model.  This contradicts
planarity of `I`.  This proof is independent of any unproved Hadwiger
case.

Deleting the two join vertices leaves `I`, so the asserted coherent
two-apex pair is literal.

## 3. First `K_7^-` model

The nonsingleton bags are connected:

* `D={t,u_0}` by `tu_0`;
* `E={b,w_0,w_2}` by `bw_0,bw_2`.

Among `D,B,R,E`, the six edges listed in (2.7) witness every pair.
The singleton bags `P,Q` are adjacent to each other and universal to the
other five bags.  The centre `A={u_3}` has the five listed required
contacts and no edge to `B={u_1}`.  Thus the missing pair is exactly
`AB`, not merely an allowed pair.

## 4. Forward and reverse pivots

For the forward split `D={u_0} dotcup {t}`:

* the gate `t` meets the old centre `u_3` and old missed row `u_1`;
* residual `u_0` meets `u_1,E,p,q` and misses exactly `u_2`;
* enlarged `A'={u_3,t}` meets every new foreign row;
* `u_0t` is the new centre-donor edge.

For the reverse split `A'={u_3} dotcup {t}`:

* the gate `t` meets the current centre `u_0` and current missed row
  `u_2`;
* residual `u_3` misses exactly `u_1` among the other rows;
* moving `t` back produces the original donor `{t,u_0}`.

Both centres have order one, the moved gate has order one, and the donor
before either move has order two.  Hence this is an exact balanced
two-cycle and not merely two unrelated near models.

## 5. Scope guard

The graph is six-colourable: four colours suffice on the planar
icosahedron and two new colours suffice for the adjacent universal
vertices.  Therefore it is not a hypothetical minimal `HC_7`
counterexample.  What it refutes is precisely a geometry-only assertion
that every legal **single-gate** deficiency pivot strictly decreases a
raw model potential.  The different two-piece/two-target rotation is
outside this involution lemma.  A state-sensitive gluing theorem or a
theorem recognizing one coherent apex pair remains necessary.
