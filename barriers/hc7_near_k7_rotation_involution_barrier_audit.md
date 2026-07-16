# Audit: deficiency-pivot involution and the icosahedral balanced cycle

## Verdict

**GREEN in its stated scope.**  The general pivot is literally reversible,
the bag-size identity is correct, and the displayed two-cycle occurs in a
seven-connected `K_7`-minor-free coherent-two-apex graph.  Proposition 5
correctly enlarges the first model to a spanning `K_7^-` model with two
nonadjacent singleton branch sets, proves that their common host has
chromatic number six, and exhibits a six-colouring in which neither omitted
root is colour-dominating.  The sharpened guardrail therefore isolates a
genuine missing criticality input.  The note makes no claim that this graph
is contraction-critical and no claim that the cycle closes `HC_7`.

Audited source:
`hc7_near_k7_rotation_involution_barrier.md`.

Source SHA-256:
`5e8c75b67c7887ba68ecb4a853ce4d40897f46fa7a76d414642a9a06bcfa61e2`.

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

## 5. Spanning singleton model

The bags in Proposition 5 have orders

\[
                       1,1,2,1,3,5,1,
\]

and their union is the full fourteen-vertex set of `G`.  More explicitly,
the six bags other than `P^+` cover

\[
             \{u_3,u_1,t,u_0,u_2,b,w_0,w_2,q\},
\]

whose complement is exactly

\[
                    P^+=\{p,u_4,w_1,w_3,w_4\}.
\]

Thus the bags are disjoint and spanning.  The bag `P^+` is connected since
`p` is adjacent to each of its other four vertices.  The connectivity of
`D,E` and all adjacencies among the other six bags were checked in Sections
3--4.  Enlarging `P={p}` to `P^+` preserves every one of those contacts,
because `p` remains in the enlarged bag.  The only anticomplete bag pair is
still

\[
                       A=\{u_3\},\qquad B=\{u_1\};
\]

the two upper-cycle vertices are nonconsecutive.  Hence the model is a
spanning `K_7^-` model whose missing pair consists of two singleton branch
sets.  The same inert enlargement may be retained through the pivot, so it
does not remove the involution established in Proposition 4.

## 6. Exact chromatic and root-neighbourhood checks

The vertices `w_0,...,w_4` induce a chordless five-cycle and `b` is adjacent
to all five.  Hence the displayed induced wheel has chromatic number four:
its rim needs three colours and its hub needs a fourth.  It survives in
`I-{u_1,u_3}`.  Since `p,q` are adjacent to each other and to every surviving
icosahedral vertex, they require two further colours.  Therefore

\[
                         \chi(J)\ge 4+2=6.
\]

Each class in (2.12) is independent.  In detail, `t` has no `w`-neighbour
and `w_1,w_3` are nonconsecutive; `b` has no `u`-neighbour and `u_0,u_2`
are nonconsecutive; `u_1,u_3` are nonconsecutive and neither meets `w_4`;
and `w_0,w_2` are nonconsecutive while neither meets `u_4`.  Giving `p,q`
the fresh colours `4,5` is proper because they are adjacent and universal
to `I`.  Restriction to `J` gives the matching upper bound, so
`chi(J)=6` exactly.

The two external-root neighbourhoods inside `J` are

\[
\begin{aligned}
 N_G(u_3)\cap V(J)&=\{t,u_2,u_4,w_2,w_3,p,q\},\\
 N_G(u_1)\cap V(J)&=\{t,u_0,u_2,w_0,w_1,p,q\}.
\end{aligned}
\]

Under (2.12) and the fresh apex colours, their colour multisets are,
respectively,

\[
 \{0,1,3,3,0,4,5\},\qquad
 \{0,1,1,3,0,4,5\}.
\]

Both neighbourhood-colour sets are therefore exactly
`{0,1,3,4,5}`.  The sole colour-`2` vertex left in `J` is `w_4`, adjacent
to neither omitted root.  Thus the displayed colouring really makes both
roots fail colour domination.

An independent exhaustive colouring check on the explicitly defined
fourteen-vertex graph found no proper colouring of `J` with at most five
colours and found the displayed proper six-colouring.  The same check
verified that the seven bags partition `V(G)`, that every bag is connected,
that `AB` is the unique missing bag pair, and that both root-neighbourhood
colour sets equal the set above.

## 7. Sharpened scope guard

The graph is six-colourable: four colours suffice on the planar
icosahedron and two new colours suffice for the adjacent universal
vertices.  Therefore it is not a hypothetical minimal `HC_7`
counterexample.  What it refutes is precisely a geometry-only assertion
that every legal **single-gate** deficiency pivot strictly decreases a
raw model potential.  The different two-piece/two-target rotation is
outside this involution lemma.  A state-sensitive gluing theorem or a
theorem recognizing one coherent apex pair remains necessary.

Proposition 5 adds four facts to the same example: the model is spanning,
its missing pair is represented by singleton branch sets, the common host
is exactly six-chromatic, and the ambient graph is still seven-connected
and `K_7`-minor-free.  Nevertheless the colouring in Section 6 makes both
roots miss colour `2`, while the pivot remains reversible.  Consequently
that conjunction alone neither forces the missing branch-set adjacency nor
supplies an orientation of the exchange.

For comparison, in a strongly seven-contraction-critical graph every
six-colouring of `J=G-{a,b}` must make at least one of two nonadjacent roots
colour-dominating: if both missed a colour, assigning each a missing colour
would six-colour `G`.  Six-colourings of the two proper deletion minors
`G-a` and `G-b` then attain the two opposite possibilities separately,
because the retained root necessarily misses its own colour.  These are
exactly the universal root-domination condition and opposite witnesses used
by the current common-host/root-contact Kempe arguments.  They are absent
from the example, which is itself six-colourable.  No unresolved assumption
is being imported from the spanning-model or colouring calculation.
