# Internal audit of the clean three-arm closure

**Status:** separate internal audit GREEN, 21 July 2026.

This is an internal mathematical audit, not external peer review.

## Revision audited

- result:
  [`hc7_atomic_h0_clean_three_arm_closure.md`](hc7_atomic_h0_clean_three_arm_closure.md)
- exact SHA-256:
  `6071c020cb7aa9fa2c963c13718a02db2b29a218fa742d924b460d540a5fc869`

The hash was computed after the result status was changed to GREEN.

## Verdict

GREEN.  Three distinct attachments admitting pairwise disjoint arms from
`e,f,g` give the stated explicit `K_7`-minor model.  The matching,
component-bridge, and ordered-contact corollaries use exactly those
hypotheses, including the possible two-contact conflict on a single
clean--clean segment.

## Checks performed

1. The seven initial bags are `X`, `V(T_ac)`, `{b}`, `{d}`, and the three
   clean-root arms.  They are disjoint: no clean root is adjacent to `x` in
   `H_0`; an arm ending internally on a segment stops before its other branch
   end; and the hypothesis separates the three arms.  Each bag is connected.
2. Assigning every unused segment interval to an endpoint bag preserves
   connectedness and leaves a joining edge whenever the endpoint bags are
   different.  On a selected arm segment, the far suffix can be assigned to
   the opposite endpoint bag.  When two arms enter one clean--clean segment,
   their disjointness leaves either a nonempty middle interval or a direct
   edge across which to split, so no zero-length case is omitted.
3. The bag `X` meets the three clean bags at the selected attachments and
   meets the `ac`, `b`, and `d` bags through the four segments incident with
   `x`.  The merged `ac` bag meets `b` through `cb` and `d` through `ad`,
   repairing the missing pairs `ab` and `cd`; `bd` is present.  Each clean
   label meets every one of `a,b,c,d`, and `e,f,g` are pairwise adjacent.
   These account for all 21 quotient adjacencies.
4. In a saturating clean-incidence matching, arms on different segments are
   disjoint because distinct subdivision segments meet only at branch
   vertices and every arm stops before a foreign branch end.  The only
   conflict is two internal attachments on the same segment between two
   clean roots.  Both contacts support both roots; assigning the contact
   nearer each endpoint to that endpoint uncrosses the arms.  This also
   covers adjacent contacts and the endpoint-contact cases.
5. For a component of `G-V(T)` adjacent to `x`, adjoining `x` gives a
   connected `X` meeting `T` only at `x`.  Seven-connectivity supplies at
   least seven component attachments and hence at least six besides `x`.
   The matching-number bound passes to the subgraph induced by the bridge's
   own attachments even if `M_X` has additional contacts coming directly
   from `x`.
6. Two distinct contacts ordered along `T_ef`, together with adjacency to
   `g`, give the disjoint arms from `e`, from `f`, and `{g}`, including when
   either or both contacts are endpoints.  The symmetric `T_eg` statement is
   identical.
7. In the linked multipartite guardrail, `T_ef=e-p-f`, `X={x}`, and the
   added contacts are `xp,xg`.  Their clean-incidence edges are precisely
   `ep,fp,gg`, so the matching number is two.  A second distinct contact on
   `T_ef` invokes the ordered-contact corollary exactly as claimed.

## Trust boundary

The result closes only the saturating three-clean-arm pattern.  A large
component bridge may have Hall-deficient clean supports, and the proof does
not derive a separator, planar deletion, strict reduction, or labelled
proper-minor response from that deficiency.  It also does not align an
arbitrary normalized dominating `K_5` model with the three clean roots or
close the full atomic collision theorem.
