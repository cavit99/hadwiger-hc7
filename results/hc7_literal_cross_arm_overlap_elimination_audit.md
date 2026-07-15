# Independent cold audit: literal cross-arm overlap elimination

**Verdict:** **GREEN after clarifying one endpoint case in the fan-lemma
derivation.**

The strengthened theorem is correct.  It closes every rigid cross-arm
outcome whose avoided support has order five and intersects the common
core, independently of whether the two arms have order five or six.

## 1. Forced clique contacts

Take `a in A cap X` and put `U=A-{a}`.  The corrected cross-arm theorem
supplies the two supports

\[
                 U\cup\{p\},\qquad U\cup\{q\}.
\]

Since `|A|=5`, all three sets `A`, `U union {p}`, and `U union {q}` have
order five.  A `K_5` model supported on five vertices has five singleton
bags and hence is a literal `K_5`.  Therefore:

* `U` is a literal `K_4`;
* `a` is complete to `U`, through the clique `A`;
* `p` is complete to `U`, through the first replacement clique; and
* `q` is complete to `U`, through the second replacement clique.

No adjacency inside the order-six arm supports `B,C` is used.  Thus the
proof is unaffected by their split-row labels or missing contacts.

## 2. Connectivity after deleting the four-clique

A standard deletion inequality gives

\[
                    \kappa(G-U)\ge \kappa(G)-|U|\ge3.
\]

Explicitly, deleting fewer than three additional vertices from `G-U`
amounts to deleting fewer than seven vertices from `G`, so the remainder
is connected.  The graph `G-U` has at least four vertices: a
seven-connected graph has at least eight vertices, while `|U|=4`.
Consequently `G-U` is genuinely three-connected under the standard order
convention, and the distinct vertices `a,p,q` all lie in it.

The distinctness is literal: the corrected cross-arm theorem has
`P={p,q}` disjoint from `A` and its common core `X`, while `a in A cap X`.

## 3. Common-cycle step

Every three specified vertices of a three-connected graph lie on one
cycle.  The fan-lemma proof is valid with the following endpoint care.
Start with a cycle through two specified vertices.  If the third is not
on it, take a three-fan from the third vertex to three distinct cycle
vertices.  The three **open interiors** of the cyclic intervals cannot all
contain one of the first two specified vertices, so choose an interval
whose open interior contains neither.  Its complementary closed arc still
contains both first vertices, including either that coincides with a fan
end.  The complementary arc and the two fan paths at its ends form a cycle
through all three specified vertices.

The pre-audit wording “an interval contains neither” was ambiguous and is
false if closed intervals are intended and the first two vertices are fan
ends.  The theorem file now uses the precise open-interior/closed-complement
form.  The underlying common-cycle conclusion was always correct.

## 4. Literal branch-set construction

Let `D` be a cycle in `G-U` through `a,p,q`.  The three vertices occur in
some cyclic order and divide `D` into three nonempty arcs.  Choose one edge
from the interior connection between each consecutive pair of roots and
delete those three cycle edges.  The resulting three path components:

1. are nonempty, pairwise vertex-disjoint, and connected;
2. contain respectively exactly one of the roots `a,p,q`; and
3. are pairwise adjacent through the three deleted cycle edges.

Equivalently, these are the three cycle bags asserted in the theorem.
They lie in `G-U`, so they are disjoint from the four singleton bags
indexed by `U`.  Each cycle bag is adjacent to every singleton `u in U`
through its root, since all of `a,p,q` are complete to `U`.  The four
singletons are pairwise adjacent because `U` is a clique.

Thus all seven bags are nonempty, connected, pairwise disjoint, and
pairwise adjacent: four singleton bags plus three cycle bags give a
literal `K_7` minor model.

This remains valid in the shortest cases.  If two roots are consecutive
on `D`, their corresponding cut edge directly supplies adjacency between
two singleton or shorter path bags; if `D` is the triangle `apqa`, the
three cycle bags may simply be the three singleton roots.

## 5. Falsification checks and scope

The construction would fail if the host were only six-connected, because
deleting `U` would guarantee only two-connectivity and three prescribed
vertices need not lie on one cycle.  It would also fail without both forced
replacement supports, because then `p` or `q` need not contact all four
vertices of `U`.  The theorem has exactly the stronger hypotheses needed
to exclude both counterarchitectures.

The proof establishes only that an order-five avoided support is disjoint
from the common core.  It does not constrain split-row adjacencies inside
order-six supports or close the disjoint-core and all-order-six cases.
Within that boundary, the strengthened theorem is GREEN.
