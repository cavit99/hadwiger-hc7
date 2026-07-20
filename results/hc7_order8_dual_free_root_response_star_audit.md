# Independent audit of the dual-free-root response-star theorem

**Verdict:** **GREEN** for the exact source revision identified below.

**Audited source:**
[`hc7_order8_dual_free_root_response_star.md`](hc7_order8_dual_free_root_response_star.md)

**Audited SHA-256:**
`bb78ac1cc61c501a5f871ab9b69a402f765ee333dabe0c9deeff5805bc94a323`

The mathematical source was audited at the preceding revision; its only
subsequent change replaces the pending-audit status line with a link to this
GREEN audit.

This is an internal mathematical audit, not external peer review.  The
source closes one precise pentagonal-bipyramid placement in the
two-component order-eight interface.  It does not close the low-degree
contact case, the dirty-path exchange, the whole order-eight interface, or
`HC_7`.

## 1. Eight latent columns

### 1.1 The first fan and its labels

Deleting `e=vx` gives a six-colouring in which `v,x` have one colour
`alpha`.  For each of the five alternate colours, the corresponding
bichromatic component containing `v` contains `x`; otherwise one Kempe
interchange would make `e` proper.  The five paths therefore have five
distinct first neighbours at `v`, distinguished by their five colours, and
none uses `e` as its first edge.

Together with `e` these are six prescribed first edges.  Seven-
connectivity supplies a seventh incident edge.  The independently audited
prescribed-first-edge all-boundary fan theorem then gives exactly the
alternatives used in Lemma 2.1:

- an actual order-seven full-neighbourhood separation;
- a strict generic order-eight response side for one of the seven
  prescribed edges; or
- an eight-fan preserving the seven prescribed first edges and using one
  additional first edge.

In the third outcome, the target limb, the five response-source limbs and
the two remaining limbs have eight distinct literal ends in `S`.  Thus the
labelling

\[
                 S=\{t,c_0,c_1,c_2,c_3,c_4,a,b\}
\]

is valid even when a first neighbour already belongs to `S`.  As usual,
fan limbs may be truncated at their first boundary hit without changing a
first edge; the eight distinct limbs then end bijectively at `S`.

### 1.2 The opposite fan and latent columns

For any `w in D`, the ordinary fan form of Menger gives an eight-fan from
`w` to `S`, unless its failure returns an actual full-neighbourhood
separation of order seven.  Boundary-fullness of `D`, the opposite
component `C`, and seven-connectivity justify this alternative exactly as
in the audited all-boundary fan theorem.

After truncation at first boundary hits, the two fan tails with common end
`s` meet one another only at `s`.  Hence

\[
                 K_s=(P_s^C-v)\cup(P_s^D-w)
\]

is connected, and the eight sets `K_s` are pairwise disjoint.

## 2. Consuming an arbitrary label

Fix any `r in S`.  The proposed roots are

\[
                 R_C^r=P_r^C,
        \qquad   R_D^r=P_r^D-\{r\}.
\]

They have all the asserted properties.

- Both are connected.  If the second limb is the edge `wr`, then
  `R_D^r={w}`.
- They are disjoint: the first root contains the boundary end `r`, while
  the second root omits it and otherwise lies in `D`.
- The last edge of `P_r^D` joins the two roots.
- For every `s ne r`, the first edge of `P_s^C` joins `R_C^r` to `K_s`,
  and the first edge of `P_s^D` joins `R_D^r` to `K_s`.
- Fan disjointness makes the roots disjoint from the seven surviving
  columns and makes those columns pairwise disjoint.

Thus **any** one of the eight labels can be consumed after the fan systems
are fixed.  Contacts among the seven surviving columns are unchanged, so
their contact graph is exactly the induced graph `K-r`.  A `K_5` minor in
`K-r`, together with these two roots, consequently lifts to an explicit
`K_7` minor in `G`.

## 3. Combining the two exceptional placements

Assume both exceptional hypotheses in Theorem 3.1.

From `K-a` being a pentagonal bipyramid with pole `t` and opposite pole
`b`, the five response labels `c_0,...,c_4` induce a five-cycle and both
`t,b` are complete to those five vertices, while `tb` is absent.  From
the corresponding statement for `K-b`, the vertex `a` is complete to the
same five response labels and `ta` is absent.  The second pentagonal
bipyramid may give a different cyclic ordering of the five labels; this is
irrelevant because the first already supplies the required cycle and the
second is used only for the five adjacencies from `a`.

The edge `ab` is unrestricted.  If it exists, it may be omitted when
taking a subgraph.  Therefore `K` contains

\[
                         I_3\vee C_5
\]

as a not-necessarily-induced subgraph, with independent side
`{a,b,t}` and the cycle supplied by the first exceptional placement.

## 4. The explicit `K_5` model

Relabel that cycle as `c_0c_1c_2c_3c_4c_0`.  The five proposed branch sets
are

\[
 \{c_0\},\quad \{c_1\},\quad \{a\},\quad
 \{c_2,b\},\quad \{c_3,t\}.
\]

The last two sets are connected through `bc_2` and `tc_3`.  Their pairwise
adjacencies can be checked without any hidden edge:

- `c_0c_1`, `c_1c_2` and `c_2c_3` are cycle edges;
- every singleton or nonsingleton set containing one of `a,b,t` is
  adjacent to each required rim singleton through a pole-to-rim edge; and
- the two nonsingleton sets contact through the cycle edge `c_2c_3`.

The model uses precisely the seven labels

\[
                  a,b,t,c_0,c_1,c_2,c_3
\]

and avoids `c_4`.

Consume `K_{c_4}`.  Section 2 gives two adjacent roots, each adjacent to
every one of the seven columns used by the displayed `K_5` model.  Taking
unions of literal columns over its five quotient branch sets gives five
pairwise disjoint, connected and pairwise adjacent host branch sets.  They
are disjoint from the two roots.  The five lifted sets together with the
two roots are therefore an explicit `K_7`-minor model in `G`.

This contradicts the theorem's `K_7`-minor-free hypothesis, so the two
exceptional placements cannot coexist.

## 5. Trust boundary

The source states the exact residual correctly.

- It proves nothing terminal when only one of the two free-root choices
  has the pole-target exceptional placement.
- A non-pentagonal, `K_5`-minor-free induced contact graph yields only a
  low-degree column, which need not be the target.
- No dirty Kempe path is split, no compatible boundary partition is
  produced, and no selected response is preserved through an order-eight
  descent.
- Consuming the response label `c_4` is legitimate only because the
  quotient `K_5` model has already been explicitly chosen to avoid it; the
  proof does not claim to preserve the discarded response path.

## 6. Verdict

The eight latent columns, arbitrary consumed-label root construction,
deduction of the `I_3 join C_5` subgraph, explicit `K_5` branch sets avoiding
`c_4`, and final `K_7` lift are all correct at the audited source hash.
**GREEN.**
