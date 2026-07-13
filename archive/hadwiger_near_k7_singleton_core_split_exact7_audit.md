# Audit: singleton-`K_4` core split and exact-seven localization

## Verdict

**GREEN for the stated literal-shell theorem.**  The result applies to a
spanning `K_7^-` normalization with four actual singleton core vertices;
it does not root an arbitrary `K_7^vee` model.

## Checks

1. Every three prescribed vertices of a two-connected graph have a
   rooted `K_3` minor.  The cycle/fan proof covers both the common-cycle
   and three-theta-path placements.  Therefore three vertices complete
   to the singleton `K_4` core give seven literal branch bags.
2. The typed split uses an `xy`-carrier and a disjoint `y`-carrier.  After
   adjoining `x` to the first shore, the seven displayed bags are
   connected and pairwise adjacent; only the unabsorbed shore needs all
   four neutral core rows.
3. In the full-state bi-Helly theorem take the four core portal sets as
   neutral rows, `A=P_x`, and `B=C=P_y`.  Its two carrier families are
   exactly those used in the split lemma.
4. If `D` were not two-connected, its nontrivial block tree has an
   off-common-bag component missing one of the six boundary rows and
   attached through at most one cutvertex.  Its neighbourhood has order
   at most six, contradicting seven-connectivity.  The degree of `x`
   excludes the order-at-most-two exception.
5. In the Tutte decomposition, an off-torso component misses one of the
   six boundary vertices and has at most two actual gate neighbours.
   Its neighbourhood therefore has order at most seven; connectivity
   forces all five other literal rows and both distinct gate vertices,
   giving the asserted exact seven-cut.  No virtual edge is used as a
   literal edge.
6. Four such off-torso lobes have two-element portal sets and five of the
   six literal contacts.  The bouquet theorem applies to the subgraph
   `K_6-{ab,ac}` of the denser `K_6-xy` shell and forces portal rank four.
7. Two core rows complete across `D` are universal vertices of the whole
   spanning shell.  A `K_5` minor after deleting them would extend to
   `K_7`; `HC_5` therefore four-colours the remainder and two fresh
   colours finish the graph.
8. The `K_2`-icosahedron witness has connectivity seven, no `K_7` minor,
   the displayed literal shell, and a three-connected complex bag.  The
   independent verifier reproduces these facts.

## Exact remaining boundary

The unresolved step is operation-sensitive: in the one common torso,
with at most one globally complete core row, obtain the typed split or
force the second complete row.  Separately, an arbitrary `K_7^vee` model
still has four connected unaffected bags rather than a literal singleton
`K_4`; label-preserving rooting of those bags is not proved here.
