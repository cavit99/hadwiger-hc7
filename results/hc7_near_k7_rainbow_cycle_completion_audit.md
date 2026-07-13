# Audit: rainbow-cycle completion

## Verdict

**GREEN**, with one harmless correction to the informal fan proof of
Theorem 2.  The standard theorem that any three vertices of a
3-connected graph lie on a common cycle applies, and all displayed branch
sets in Theorem 1 are literal and pairwise adjacent.  Consequently the
unique-shadow (`d=1`) residue of `P4` is closed in the singleton bipartite
shell.

## 1. Three-root cycle branch sets

Let the cycle through `v,b,x` have `v-b` arcs `P,Q`, with `x` internal
to `P`.  Put `R=V(P)-{v,b}` and split `Q` at an edge `yz`, oriented from
`v` to `b`, into

\[
 X=V(vQy),\qquad Y=V(zQb).
\]

Then:

* `X,Y,R` are nonempty, connected and pairwise disjoint;
* `yz` is an `X-Y` edge;
* the first edge of `P` is an `X-R` edge because `v in X`;
* the last edge of `P` is an `R-Y` edge because `b in Y`; and
* `X,Y,R` contain `v,b,x`, respectively.

Since those three vertices are each complete to the literal clique `C`,
every one of the three branch sets sees every singleton `{c}`, `c in C`.
The singleton bags for `C` are mutually adjacent.  Thus the displayed
sets are exactly `|C|+3` disjoint connected pairwise adjacent branch
sets.  No collective-contact or contraction-to-original confusion is
present.

The case `Q=vb` is also valid: take `X={v}`, `Y={b}` and use that edge as
`yz`.

## 2. Common cycle in the 3-connected remainder

The invoked result is the standard three-vertex cycle theorem (the
three-vertex case of Dirac's cycle theorem): any three distinct vertices
of a 3-connected graph lie on one cycle.

The note's short fan explanation contains a reversed phrase.  If the
three fan attachments avoid the poles `v,b`, two attachments are on the
**same**, not necessarily different, open `v-b` arc by the pigeonhole
principle.  The complementary arc between those two attachments contains
both poles and, together with the two fan paths, gives the required
cycle.  If an attachment is a pole, pair it with any other attachment and
use the pole-to-attachment arc containing the other pole.  This repairs
the explanation without changing the theorem or its application.

## 3. Application to the unique shadow

In the singleton-shell application:

* `C={b_i:i ne j}` is a literal clique of order `r-2`;
* the unique-shadow state makes both poles `v,b_j` complete to `C`;
* the list-saturated vertex `x in B` is distinct from the poles and lies
  in every ordinary portal set, so it is complete to `C`; and
* deleting `C` from an `(r+1)`-connected graph leaves a graph of
  connectivity at least `(r+1)-(r-2)=3`.

The common-cycle theorem and the literal branch-set construction therefore
give a `K_{r+1}` minor.  For `r=6`, this is a literal `K_7` model.

This uses neither the extra pole incidence of `x` nor the earlier theta,
and it does not assume connectivity stronger than seven in the `HC_7`
case.
