# Audit of the colour-matched path component-exchange criterion

**Verdict:** GREEN (separate internal audit)

**Audited theorem revision:** SHA-256
`eb024c94213b993bccc3b7c116117831ee898cb8eaf94535e7dd1b7fe622257c`
of `hc7_colour_matched_path_component_exchange.md`.

## Checks performed

The seven branch sets in Theorem 2.1 were checked for connectivity,
pairwise disjointness, and every required adjacency.  In particular, a
chosen residual component is adjacent to the repaired path-side branch
set either through a deleted path vertex in its original connected branch
set or, when no such vertex was deleted, through the original pole
contact.

The neighbourhood decomposition in Proposition 3.1 is exact.  Missing an
entire anchor or protected branch set leaves that set on the far open side,
so the separation is nontrivial and seven-connectivity applies.  The note
correctly keeps failure between particular selected residual components as
a separate four-partite compatibility obstruction.

The minimizing family in Proposition 4.1 is explicit and nonempty.  Any
alternative path after deletion of one protected hit would trim to an
admissible path meeting fewer protected vertices.  The conclusion is
correctly stated in terms of unavoidable blockers, without claiming that
a terminal blocker is necessarily a cut vertex.

For Proposition 5.1, restricting a six-colouring of the contraction to
the graph outside the contracted set and colouring the set from colours
absent on its boundary gives the stated contradiction.  The exact
five-colour conclusion for every nontrivial bipartite residual component
and the singleton variant are valid.

## Scope

The result is a sufficient, label-preserving exchange theorem and an exact
description of two kinds of failure.  It does not prove the existence of
the required component transversal, bound every returned separator by
seven, or synchronize the proper-minor boundary colourings.  It therefore
does not prove `HC_7`.

No unresolved assumption or proof gap remains within this stated scope.
