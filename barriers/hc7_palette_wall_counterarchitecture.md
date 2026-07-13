# A palette-wall long-ear counterarchitecture

## 1. Purpose

The blocker-incidence audit shows that a long minimum connector can have
strict-surplus portal components without exposing an exact seven-cut.  The
next natural hope is that the smallest genuinely chromatic input already
rules this out:

* the original sole shore admits no boundary state with at most five
  blocks;
* deleting or contracting every internal edge unlocks such a state.

That hope is false without universal trace accessibility or `K7`-minor
exclusion.  The dependency-free verifier
`moser_palette_wall_ear_probe.py` certifies the construction below.

## 2. Construction

Let `S={0,...,6}` induce the pure Moser spindle and add the apex `v`
complete to `S`.  Put

\[
 P=p_0p_1p_2,qquad
 A=\{a_0,a_1,a_2,a_3\},qquad
 B=\{b_0,b_1,b_2,b_3\}.
\]

Make `A` and `B` cliques.  Make `p0,p1` complete to `A`, and `p1,p2`
complete to `B`.  Add `p2a1` and `p0b0`.  Thus

\[
 A\cup\{p_0,p_1\},\qquad B\cup\{p_1,p_2\}
\]

are overlapping `K6` palettes.

The boundary contact sets are:

\[
\begin{array}{c|l}
0&a_0,a_1,a_2,p_0\\
1&a_0,a_2,a_3,p_0\\
2&a_0,a_1,a_2,b_1,b_2,p_2\\
3&b_1,b_2,b_3,p_2\\
4&a_0,a_3,b_2,p_0\\
5&b_0,b_1,b_2,b_3,p_2\\
6&a_0,a_2,a_3,b_0,b_1,b_3,p_0.
\end{array}                                      \tag{2.1}
\]

There are no other edges.

## 3. Certified properties

### Proposition 3.1

The graph in Section 2 has all of the following properties.

1. It is seven-connected, and `S` is its only cut of order seven.
2. `P` is a minimum-order `13`-connector; the minimum order is three.
3. The components of `C-P` are `A,B`, with rows

   \[
   R_A=\{0,1,2,4,6\},\qquad
   R_B=\{2,3,4,5,6\}.                            \tag{3.1}
   \]

   Each has external neighbourhood of order eight.  Hence `05` is the
   unique carrier-blocked edge of the missing `C5`, and neither component
   exposes an exact cut.
4. `H=G-v` is six-colourable, but every six-colouring of `H` uses all six
   colours on `S`.  Equivalently, no at-most-five-block boundary state
   extends the original shore, and `G` is not six-colourable.
5. For every edge `xy` internal to `C`, the graph `G-xy` has a
   six-colouring with `x,y` equal.  Equivalently, both deletion and
   contraction of every internal edge unlock an at-most-five-block state.
6. For the consecutive connector edge `p0p1`, one transition state is

   \[
                    06\mid13\mid25\mid\{4\}.     \tag{3.2}
   \]

7. Of the ten exact one-pair Moser traces, only the trace `15` extends
   `H`.  Thus the universal exact-trace axiom fails sharply.
8. The graph contains a `K7` minor.

### Verification

The script exhausts every vertex deletion set through order seven, all
candidate `13`-carriers, every canonical colouring of the two overlapping
palette cliques, every boundary list-colouring, and every internal edge
transition.  It also tests all ten exact traces.

For item 8, six singleton bags are

\[
 p_0,p_1,a_0,a_1,a_2,a_3.
\]

The seventh bag is `\{b0,6,2\}`.  It is connected through
`b0-6-2` and is adjacent to all six singletons: `b0` sees `p0,p1`,
label `6` sees `a0,a2,a3,p0`, and label `2` sees `a0,a1,a2`.

## 4. Consequence for the ear programme

This construction survives exactly the incremental conditions requested
for an edge between consecutive portals of a length-three connector.  In
fact it survives them for every internal edge, and its `p0p1` operation
already produces a normalized `2+2+2+1` state.  Nevertheless the blocked
edge and strict portal rows remain.

Therefore no lemma of the form

\[
\begin{array}{c}
\text{palette wall + every internal edge transition}\\
\text{+ seven-connectivity + minimum connector incidence}
\end{array}
\Longrightarrow
\text{exact adhesion or support rerouting}
\]

is valid.  The next proof must use at least one of the two genuine
counterexample axioms absent here:

1. **universal trace accessibility:** every Moser nonedge is realized as
   the exact repeated pair by its star contraction; or
2. **minor exclusion:** the transition/ear geometry must not assemble the
   explicit `K7` model above (or any alternative one).

The first is particularly concrete.  The palette wall by itself realizes
only `15`; a hypothetical contraction-critical counterexample realizes all
ten traces.  The correct next finite-state test is therefore to impose the
ten star-contraction traces in addition to the internal-edge transitions.
This is a materially stronger condition, not another incidence refinement.

