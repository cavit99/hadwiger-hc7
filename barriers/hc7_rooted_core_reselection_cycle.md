# Rooted-core reselection is a neutral two-cycle

**Status:** explicit global-invariant barrier with a dependency-free
checker.  It is not an `HC_7` counterexample.

## Construction

Let `I` be the icosahedron with vertices

\[
 T,B,U_0,\ldots,U_4,L_0,\ldots,L_4
\]

and the usual edges

\[
 TU_i,\quad BL_i,\quad U_iU_{i+1},\quad L_iL_{i+1},
 \quad U_iL_i,\quad U_iL_{i-1}.
\]

Put `G=K_2 vee I`, with adjacent universal vertices `a,b`, and use the
actual seven-separation

\[
 X=\{T\},\qquad
 \Omega=\{a,b,U_0,\ldots,U_4\},\qquad
 Y=\{B,L_0,\ldots,L_4\}.
\]

The graph is seven-connected and `K_7`-minor-free.  For the latter, after
discarding the at most two model bags containing `a,b`, a hypothetical
`K_7` model would leave a `K_5` model in the planar graph `I`.

Delete the two disjoint named edges

\[
 e=TU_0,\qquad f=L_2U_2
\]

and root the four bags at `(T,U_0,L_2,U_2)`.  In `G-{e,f}` both

\[
 \begin{array}{llll}
 M_a:\;&\{T,a\},&\{U_0,U_1\},&\{L_2,b\},&\{U_2\},\\
 M_b:\;&\{T,b\},&\{U_0,U_1\},&\{L_2,a\},&\{U_2\}
 \end{array}
\]

are literal rooted `K_4` models.  Every bag meets `Omega`.  The involution
interchanging `a,b` fixes the separation, roots and deleted edges and
interchanges the two models.

The dependency-free checker is
[`../active/hc7_rooted_core_allocation_falsifier.py`](../active/hc7_rooted_core_allocation_falsifier.py).
It verifies the two displayed models.  It also exhausts all 3,168 crossing
named-edge/root choices over all twelve actual order-seven cuts of this
host; each admits an all-boundary rooted `K_4`.

## Invariant consequence

The two states have exactly the same

* four-bag boundary-contact vector;
* sorted bag-size vector `(1,2,2,2)`;
* union of model vertices; and
* literal separation and rooted labels.

Therefore rooted-core reselection cannot itself be a strict global move.
Any isomorphism-invariant rank built from boundary incidence, bag balance,
or the coarse model carrier is constant on this two-cycle.  Such
reselections must be quotiented as neutral moves.  A claimed proof which
allows either direction and nevertheless declares one direction a strict
improvement has no well-founded invariant.

The same warning applies to swapping two unnamed rich packets: a
packet-reserving normalization can be terminal data, but packet exchange
alone cannot orient a descent.  Promoting three boundary-contacting bags
to four can be a bounded local improvement, but regeneration at the
opposite twin may lose the fourth contact.  To become global progress, the
maximal-contact sink still needs an independent classification.

## Why the standard two-apex family does not refute the allocation lemmas

In fact the natural two-apex guardrail is unusually friendly to the first
allocation claim.  If `G=K_2 vee P` is seven-connected, `P` is planar,
and an actual order-seven separation has nonempty open shores, both universal vertices
belong to its boundary.  The remaining five boundary vertices separate
the two base shores.  Universal-apex assignment and one base path in
`P-{z,d}` give an all-boundary four-root model; that path exists because
seven-connectivity makes `P` five-connected.  The checker confirms this
throughout the icosahedron and the next pentagonal tube.

Nor can this family contain an actual packet vector `(1,2)`.  Three
disjoint full packets across the two shores, contracted in the planar base,
together with the five nonapex boundary vertices would give a `K_{3,5}`
minor.  Thus the family has total packet capacity at most two.

These observations make the trust boundary precise: the example is a
barrier to a **rank**, not to the all-boundary normalization itself.

## Trust boundary

The pair `{a,b}` is coherent and

\[
                         G-\{a,b\}=I
\]

is planar.  The graph is six-colourable and is not seven-contraction-
critical.  Hence the example does not refute a terminal dichotomy which
allows a coherent fixed pair, nor a transition theorem which genuinely
uses the response to every proper minor.  It shows exactly why one of
those two ingredients is necessary after quotienting the neutral
reselection component.
