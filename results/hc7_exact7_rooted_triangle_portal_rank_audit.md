# Independent audit: exact-seven rooted-triangle portal-rank funnel

## Verdict

**GREEN for every claimed result in Sections 2 and 3.**  The
block--cutvertex obstruction is exact, every non-singleton lobe behind
an actual three-gate has a literal gate-rooted `K_3` model, and portal
rank three lifts literally to `K_7` through the other lobe and the three
opposite full packets.

The final **maximal portal-rank triangle exchange** is correctly labelled
as the next missing link.  This audit does not promote or assume it.

## 1. Rooted-triangle obstruction

Suppose a vertex `x` has the stated property.  At most one rooted branch
bag can contain `x`.  The other two rooted bags must lie in two distinct
components of `H-x`, and hence cannot be adjacent.  Thus the obstruction
and a rooted triangle model cannot coexist.

Conversely, consider the block--cutvertex tree and the minimal subtree
joining the three root locations.  If its median is a cutvertex node
`x`, deleting `x` puts the remaining roots in distinct components, which
is exactly the stated obstruction.  If its median is a nondegenerate
block, the three arms enter that block at distinct vertices.  A
two-connected graph has a `K_3` model rooted at any three distinct
vertices: take a cycle through two entries and a two-fan from the third
entry to the cycle, then partition the resulting cycle-plus-ear into
three connected pairwise adjacent pieces.  The three disjoint arms of
the block tree can be absorbed into the corresponding pieces.  A bridge
block has degree at most two toward distinct arms and cannot be this
median.  This proves the dichotomy, including cases in which a root is
itself a cutvertex.

As a bounded independent check,
`active/hc7_exact7_rooted_triangle_portal_rank_verify.py` tested all
32,331 connected atlas-graph/root-triple instances of order at most
seven.  In every instance, exactly one of the rooted model and the
cutvertex obstruction occurred.

## 2. The lobe argument

Let `K` be a non-singleton component of `L-T` and put `H=L[K union T]`.
Three-connectivity of `L` first forces `K` to meet every literal member
of `T`; otherwise the other two gate vertices separate it from the other
lobe.

If `H` had no rooted triangle, the obstruction vertex `x` supplied by
the preceding lemma could not lie in `T`: after deleting a gate vertex,
connected `K` and its contacts with the other two gates put those two
gates in one component.  Hence `x in K`.  Because `K` is non-singleton,
some component `A` of `H-x` contains a vertex of `K`.  It contains at
most one gate vertex `t`.  Every exit in `L` from `A cap K` is through
`x` or `t`; an edge to another gate would put that gate in `A`, and
there are no edges to the other lobe.  Deleting `{x,t}` (or just `x`
when no gate lies in `A`) is therefore a cut of order at most two in
`L`, a contradiction.

The singleton exception is real: one lobe vertex adjacent to all three
gate vertices gives a three-leaf star and no rooted triangle.  The atlas
verifier separately checked every nontrivial lobe behind an exact
two-lobe three-cut in every three-connected atlas graph; all passed.

## 3. Portal-rank lift

For a rank-three rooted model `B_1,B_2,B_3`, choose distinct literal
representatives `s_1,s_2,s_3`.  The other lobe `J` is adjacent to each
`B_i` through its contact with the literal root `t_i`.  Moreover
`|N_S(J)|>=4`, since `T union N_S(J)` separates `J` from the first lobe
and the nonempty opposite shore.  Thus `J` has a fourth representative
outside `{s_1,s_2,s_3}`.

These are four disjoint connected clique carriers with four distinct
literal boundary anchors.  The three disjoint `S`-full packets, anchored
at the remaining boundary vertices, supply all other branch-set
adjacencies.  This is a literal seven-bag clique model; no virtual gate
edge, colour-class identification, or hidden planarity assumption is
used.

Therefore a target-free survivor really does force **every** rooted
triangle in every nontrivial lobe to have portal rank at most two.  The
unproved issue is precisely whether maximality of such a model can turn
the independently available three labelled portals into rank three, a
state splice, or the allowed fixed two-vertex endgame.
