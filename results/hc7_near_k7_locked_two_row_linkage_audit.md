# Independent audit: locked two-row linkage

## Verdict

**GREEN after the incorporated helper-composition clarification.**  The
fixed linkage is label-faithful, the rooted-`K_4` implication is valid,
Theorem 2.3 is invoked with its exact rank-four SDR hypothesis, and the
ordered path is a genuine obstruction to an unconditional peel.

## 1. Literal fixed linkage

The two paths in Lemma 1 are vertex-disjoint subsets of the one carrier
`K`.  Their initial endpoints have literal edges to `L,R`, so adjoining
them gives disjoint connected shores.  The old path-cut edge survives,
and their terminal portal edges give the named contacts to `H,Q`.
No foreign-row vertex is absorbed.

Preservation of helper edges alone is not enough for composition.  The
corrected statement assumes two mutually disjoint helper families
outside `K`, with every helper piece already attached to its assigned
old path side.  Adjoining them to the enlarged shores preserves
connectedness, disjointness and all remaining literal contacts, so the
literal shore-completion theorem then applies.

## 2. Rooted `K_4` really gives the prescribed pairing

Fix an SDR `(l,r,h,q)`.  In a rooted `K_4` model let the four disjoint
connected branch sets be `B_l,B_r,B_h,B_q`.  Inside

\[
                 B_l\cup B_h\cup e_{lh}
\]

there is an `l-h` path, where `e_{lh}` is a literal model edge between
the two branch sets.  Similarly `B_r union B_q union e_{rq}` contains an
`r-q` path.  The two paths are vertex-disjoint because they use disjoint
pairs of branch sets.  Thus any rooted `K_4` at an SDR produces exactly
the fixed linkage required by Lemma 1; no arbitrary pairing is assumed.

If no fixed linkage exists, no SDR quadruple has a rooted `K_4`.  The
cited Theorem 2.3 applies because `K` is four-connected and the four
portal families have a full SDR.  It returns a single plane embedding
and one face containing every portal vertex occurring in any full SDR.
This is precisely the stated “usable portal” set; vertices which occur
in no SDR are not claimed cofacial.

For four distinct vertices on one facial cycle, the prescribed pairs
have disjoint boundary arcs exactly in the nonalternating order.  Hence
failure of the linkage forces every SDR to have alternating cyclic order.
Four-connectivity makes the planar face boundary a cycle, so no repeated
facial-walk ambiguity is needed.

## 3. Ordered path obstruction

For `K=k_L-k_Q-k_R-k_H`, the unique `k_L-k_H` path and unique
`k_R-k_Q` path share the edge `k_Qk_R`; therefore the prescribed fixed
linkage is impossible.  In the rooted triangle promotion of `L,R,Q`,
the natural median allocation puts `k_Q` in the promoted `Q` row and
`k_R` in the right shore.  The sole `H` portal lies behind `k_R`, so it
cannot be joined to the left shore without meeting the right shore.

Because the four external contact classes are disjoint, assigning six
external neighbours at each end and five at each internal vertex gives
local degrees at least seven and at least `6+5+5+6=22` distinct boundary
vertices.  This does not make the whole host seven-connected, and the
source correctly disclaims that conclusion.  It proves only the intended
negative statement: large numerical adhesion, protected ownership and
local degree do not force the fixed linkage or a strict internal peel.

## Scope

The one-face outcome is local to `K`.  It neither supplies a literal
global apex pair nor proves compatible rotations across different
carriers.  Any recursion still needs a strictly decreasing measure, and
any rural terminal must cover all remaining host edges with one fixed
pair.
