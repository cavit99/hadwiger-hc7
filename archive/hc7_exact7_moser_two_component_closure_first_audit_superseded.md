# Superseded first audit: complete pure-Moser two-component closure

The superseded audited source is not retained.  Its former working filename
was `hc7_exact7_moser_multiframe_exchange.md`.
Verdict: **GREEN**, subject only to the editorial clarifications in Section 6
below.

The new proof closes the full degree-seven pure-Moser cell in which
`G-N[v]` has exactly two components.  Its decisive step is one application
of the already audited seven-boundary four-port theorem to the literal
corners `1,2,3,4`; it does not assume a favourable five-root crossing or
compose paths selected in different trace frames.

## 1. Exact-state exchange

The Section 3 exchange was checked independently in an earlier audit which
was not retained.  For either cross
perfect matching

\[
13\mid24\qquad\text{or}\qquad14\mid23,
\]

the two blocks are independent, each dominates every boundary vertex outside
it, and each contains one left corner adjacent to `6` and one right corner
adjacent to `5`.  The first proper minor returns exactly one of

\[
R_0=\{r,e,0,5,6\},\quad
R_5=\{r,e,05,6\},\quad
R_6=\{r,e,06,5\}.
\]

Adjacent disjoint shore carriers for `r,e`, together with the star on
`v+I_q`, reproduce the selected state as a literal representative clique.
The shore-restricted pullbacks are proper because each contracted set meets
the retained closed shore in an independent block.  Palette alignment and
gluing are valid.

## 2. Generalized literal-disk lemma

Lemma 2.1 is valid with `D` merely two-connected and `|D|>=3`.

For either same-side pair `T={a,x}` or `T={b,y}`, if
`|N_D(T)|<=1`, then

\[
N_D(T)\cup(S-T)
\]

has order at most six.  The set `D-N_D(T)` is nonempty because `|D|>=3`,
and after deletion it has no edge to either surviving member of `T`, to the
opposite exterior component, or to `v`.  This contradicts
seven-connectivity.  Hence each portal union has order at least two.

Each individual portal set is nonempty by `S`-fullness.  For two nonempty
sets with union of order at least two, distinct representatives exist.  The
literal edges `ax=12` and `by=34` therefore give two ears with distinct ends
on the two-connected graph `D`.  Adding the ears, and then all unused edges,
preserves two-connectivity of the literal four-root closure `Q`.

In the returned disk embedding the outer boundary is consequently a cycle.
For cyclic order `a,x,b,y`, the missing pairs `a-y` and `x-b` are consecutive.
Their two open outer-cycle arcs are disjoint, nonempty, and have all internal
vertices in `D`.  A shortest path in connected `D` between their interiors,
assigned to one side except for its final endpoint, makes the two carriers
adjacent without losing disjointness or endpoint contacts.

No three-connectivity or order-four assumption is used.

## 3. One-call four-port closure

With `S=N(v)`, an exterior component `D` is a component of `G-S`; the
opposite side is nonempty because it contains `v` and the other exterior
component.  Fullness gives a neighbour in `D` for each of the four literal
roots.  The audited four-port theorem therefore applies to ordered tuple
`(1,2,3,4)`.

* In its linkage outcome, the paths join `1-3` and `2-4`.  Their interiors
  are nonempty because `13,24` are literal nonedges.  Shortest-path
  enlargement in connected `D` gives adjacent carriers for `13|24`.
* In its rural outcome, the theorem returns the **literal** graph
  `G[D\cup{1,2,3,4}]` in a disk with boundary order `1,2,3,4`.  Lemma 2.1
  gives adjacent carriers for `14|23`.

Both outcomes feed the GREEN exact-state exchange.  Thus every
two-connected exterior component of order at least three is impossible.
This implication has no dependency on a favourable crossing or on
multi-frame compatibility.

## 4. Low-cut dependency

`results/hc7_exact7_moser_rich_twocut_exchange.md`, Theorem 1.1, has exactly
the same hypotheses: a seven-connected, `K_7`-minor-free graph proper-minor
minimal subject to non-six-colourability, a degree-seven vertex with the
literal pure-Moser neighbourhood, and exactly two exterior components.  Its
audited conclusion is that neither component has a cutvertex or a
two-vertex cut.  Consequently a component of order at least four is
three-connected, while a connected component of order three is either a
triangle or has a cutvertex.

The invocation in Theorem 6.1 is therefore within scope and introduces no
new computation beyond the already certified low-cut quotient atlas.

## 5. Tiny components

### Order one

If `D={q}`, fullness and the component decomposition give

\[
N(q)=S=N(v),\qquad qv\notin E(G).
\]

A six-colouring of the proper minor `G-q` extends by assigning `q` the
colour of its open twin `v`.  This is a valid contradiction.

### Order two

Write `D=uv`.  For `A in {L,R}`, define explicitly

\[
P_D(A)=\{w\in\{u,v\}:N(w)\cap A\ne\varnothing\}.
\]

If `|P_D(A)|<=1`, the set `P_D(A)\cup(S-A)` has order at most six and
separates the nonempty graph `D-P_D(A)` from `v` and the other exterior
component.  Hence `P_D(L)=P_D(R)={u,v}`: each carrier sees at least one
label on each side.  Fullness also says every one of the two labels on each
side is seen by some carrier.

In each of the two `2`-by-`2` carrier--label incidence graphs, every vertex
on both sides has positive degree.  Hall's condition follows: singleton
carrier sets have a neighbour, and the two-carrier set sees both labels.
Thus there is a perfect matching on `L` and independently one on `R`.
Pair the label assigned to `u` in the two matchings, and do the same for
`v`.  The resulting complementary blocks are exactly one of
`13|24,14|23`; `u` and `v` contact their respective blocks and are adjacent.
Section 3 applies.

### Order three

A connected simple graph of order three which is not `K_3` is a path and
has a cutvertex, contrary to the low-cut theorem.  The triangle is
two-connected and is eliminated by Theorem 4.1.

Together with the order-at-least-four case from the low-cut theorem and
Theorem 4.1, these cases exhaust every exterior component.  Since either of
the two components may be chosen as `D`, Theorem 6.1 closes the branch.

## 6. Editorial clarifications

These do not affect correctness but should be repaired before promotion.

1. Section 2 should explicitly include `G` is seven-connected among its
   hypotheses, or cite immediately the audited Mader theorem deriving this
   from the noncomplete seven-contraction-critical setting.  The proof uses
   seven-connectivity repeatedly.
2. Define `P_D(A)` locally in the order-two paragraph, as above, instead of
   referring to an active note for the notation.
3. Rename the Section 4 heading from “3-connected full shore” to
   “two-connected full shore”; the theorem itself already has the correct
   strengthened statement.

With these precision edits, the proof is self-contained relative to its two
audited dependencies and the complete pure-Moser two-component closure is
GREEN.
