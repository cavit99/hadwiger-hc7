# Independent audit of the partial-loss chromatic-lift barriers

**Status:** separate internal audit GREEN, 21 July 2026.

This is an internal mathematical audit, not external peer review.

## Revision audited

- barrier:
  [`hc7_partial_loss_chromatic_lift_barriers.md`](hc7_partial_loss_chromatic_lift_barriers.md)
- exact SHA-256:
  `5cc7262a04a2e5782b39e76fc9829d612e21fad09e217901f4e6df7203f051b7`

The mathematical content was audited at SHA-256
`eb2b27d83570dda9e8b309decc1114a4f84aae8298146467a97e1d4309138456`.
The only subsequent source edit changed its status line to record this
GREEN audit.  That status-only revision was rechecked, and the final hash
above was independently reproduced with `shasum -a 256`.

## Verdict

GREEN.  The triangle correctly refutes naive all-equal expansion through a
multi-edge contraction fibre, while preserving the distinction between
that false expansion and the valid two-colour lift through an induced
bipartite fibre.  The family `G_n` has exactly the claimed clean-support
incidence obstruction and is `K_7`-minor-free for the stated two-apex
planarity reason.

Both examples are explicitly and correctly limited to intermediate
inferences; neither is presented as a full-hypothesis counterexample.

## Checks performed

1. The selected edges `r_0r_1,r_1r_2` form a tree, but the host edge
   `r_0r_2` is a chord within its contracted fibre.  Full contraction
   suppresses that chord as a loop.  Pulling the quotient colour back
   equally to all three vertices leaves `r_0r_2` monochromatic in
   `G-F_0`, so the proposed all-equal expansion is false.
2. The note distinguishes the two relevant obstructions accurately.  Any
   host chord inside a fibre defeats the all-equal expansion, even if the
   chord crosses the forest tree's bipartition.  A crossing chord remains
   compatible with the two-colour fibre lift.  The latter fails only when
   the full induced fibre is non-bipartite; the displayed triangle supplies
   that smallest failure.
3. In `G_n`, the vertices `x,y,l_1,...,l_n` induce the tree obtained from a
   star at `y` by attaching `x` as one additional leaf.  It meets the fixed
   subdivision only at `x`, and deleting any edge needed to reach one of the
   selected leaves disconnects that leaf or `x`.  Thus it is minimal as a
   connected subgraph containing the root and all contact-owning leaves.
4. Every selected attachment `p_i` lies internally on the one subdivided
   `ef` route, so its endpoint support is exactly `{e,f}`.  Hence the
   clean-incidence graph has identical neighbourhoods
   `N(e)=N(f)={p_1,...,p_n}` and empty `N(g)`.  Its matching number is two
   for every `n>=5`, independent of the number of leaves or attachments.
   The contacts through `x` reach only the four non-clean roots
   `a,b,c,d` and do not alter this incidence calculation.
5. After deleting `e,f`, the six vertices `x,g,a,b,c,d` induce
   `K_{2,2,2}` with parts `{x,g}`, `{a,b}`, and `{c,d}`.  The remaining
   `p_i,l_i,y` vertices induce a subdivided fan: the `p_i` form its rim
   path and each `y-p_i` spoke is subdivided by `l_i`.  The only edge from
   that planar fan to the planar octahedron is the bridge `xy`.  Their union
   is therefore planar.
6. If `G_n` had a seven-branch-set clique-minor model, deleting the at most
   two branch sets containing `e` or `f` would leave at least five disjoint
   connected pairwise adjacent branch sets entirely in
   `G_n-{e,f}`.  They would form a `K_5` minor in a planar graph, a
   contradiction.  This argument remains valid when `e,f` occupy the same
   branch set.
7. As a supplementary construction check, I generated `G_n` for
   `n=5,8,13` with NetworkX.  In every case the induced six-vertex graph was
   isomorphic to the octahedron, `xy` was a bridge, and
   `G_n-{e,f}` returned a valid planar embedding.  The analytic argument in
   items 5--6 applies to every `n>=5`; these finite checks are not used as an
   unbounded proof.

## Trust boundary

The triangle is only a counterexample to expanding one quotient colour
equally over a chorded multi-edge fibre.  It does not obstruct a two-colour
lift when the whole induced fibre is bipartite.

The graphs `G_n` are low-connectivity constructions and do not satisfy the
first-loss, seven-connectivity, or contraction-critical hypotheses.  They
show that arbitrarily many common leaves or selected attachments can remain
concentrated in two clean incidence classes.  They do not refute an argument
that separately proves support diversity from host connectivity, bridge
attachments, or proper-minor colouring responses.
