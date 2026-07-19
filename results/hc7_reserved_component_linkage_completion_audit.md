# Independent internal audit of reserved-component linkage completion

**Verdict:** GREEN for the exact source revision

```text
results/hc7_reserved_component_linkage_completion.md
SHA-256 9710607f41d2c5120f5a24daa0f909a0e5e5fbf119f9e0d7198ebcea98c0b2ff
```

This is a separate internal mathematical audit, not external peer review.
The first audit pass found a missing explicit proof that the separated
component is anticomplete to the retained donor.  The source was repaired
before the revision recorded above was approved.

## 1. Imported setting

The source correctly imports the spanning labelled `K_7`-minus-one-edge
model, the connected split `U=W dotcup U'`, the fixed `D-U'` response edge,
the complete owner set and the Rado--Menger certificate.  In particular:

- every owner portal set is nonempty;
- `B=N_G(U') cap W` is nonempty;
- a minimal deficient family of order three has a two-vertex transversal
  `K`; and
- every proper owner subfamily has the required labelled linkage from
  distinct vertices of `B`.

No palette colour is identified with a model label.

## 2. Eight-vertex boundary

The proof that `C cap B` is empty is essential and correct.  A vertex of
`C cap B`, joined inside connected `C subseteq W-K` to the selected owner
portal, would give a `B-A_I` path avoiding `K`.  Hence `C` is anticomplete
to `U'`.

All remaining neighbours of `C` lie either in `K` or in the six branch sets
different from `U`.  The no-repeated-contact hypothesis gives at most one
literal neighbour in each of those six sets.  Therefore the assumed
neighbourhood order eight forces equality: both vertices of `K` occur and
every outside branch set contributes exactly one literal vertex.

The component and connectivity deductions were also checked.

- `C` and the component containing `U'` are distinct components of `G-S`.
- If a component misses a boundary vertex, seven-connectivity forces its
  full neighbourhood to be exactly the other seven vertices, giving an
  actual order-seven separation.
- Otherwise every component is boundary-full.  The audited four-component
  closure leaves exactly two or three components, and two-full-shore
  absorption gives a four-colourable boundary.
- With three components, the cited finite classification applies only after
  the proof excludes a clique odd-cycle transversal and every compact
  boundary `K_4` model.  The source performs both reductions.

## 3. Rank-two linkage geometry

For every two-owner subfamily, each of its two disjoint paths must meet the
two-vertex transversal.  Neither path can use both transversal vertices,
because the other path must also meet the transversal.  Thus the paths use
the two vertices once each.

The switching-owner conclusion is the pigeonhole argument stated in the
source: if each of three owner labels always used one fixed transversal
vertex, two labels would use the same vertex in their mutual two-path
linkage.

The connected bipartition of `W` is valid.  A shortest path from the third
portal set to the first two linkage paths has no internal vertex on either
path; adjoining it to the first path met keeps the two connected subgraphs
disjoint.  Every remaining component of `W` has an edge to their union and
may be assigned to one adjacent subgraph.  A zero-edge shortest path, when
the third portal already lies on a linkage path, is harmless.

## 4. Parameter-uniform minor construction

Theorem 4.1 was checked for every `2<=m<=5`.  The `m-1` disjoint paths for
`I-{R_0}` all meet the transversal `K` of order `m-1`; hence each uses one
different vertex and their union contains all of `K`.  Their distinct
`B`-ends connect their union to `U'`, so the set `A` in (4.1) is connected.
Connectedness of `G[W]` gives an edge from `C` to `K subseteq A`.

The branch-set contacts are exact:

- terminal portal edges join `A` to every owner other than `R_0`;
- `U'` joins `A` to every nonowner among `X,Y,F_1,F_2,F_3`;
- the fixed response edge supplies `A-D`; and
- the reserved connected set `C` meets all six outside branch sets.

If `R_0` is `X` or `Y`, deleting it leaves five pairwise adjacent outside
branch sets.  Otherwise `R_0` is an `F_i`; the connected union `X union
R_0` reaches `Y` through the old `R_0-Y` edge and, together with the four
other outside branch sets, is a `K_5` model.  The seven sets

```text
A, C, Q_1, Q_2, Q_3, Q_4, Q_5
```

are disjoint, connected and pairwise adjacent.  This is an explicit
`K_7`-minor model.

Corollary 4.2 is also valid: an explicitly assumed connected remainder
`C_0`, disjoint from the linkage paths and adjacent to `A` and all six
outside branch sets, substitutes directly for `C`.

## 5. Adversarial and literature checks

The standard rank-two obstruction with two source vertices, a two-vertex
transversal and three portal leaves adjacent to both transversal vertices
shows that the three pairwise linkages alone do not yield a three-path
linkage or a parity contradiction.  The source does not make either claim.

Stephens--Ye kite-linkedness and Perfect fan augmentation preserve nominated
vertices or fan feet in the whole host, but not confinement to `W-C`,
distinct `B` sources, terminal-first-hit ownership or avoidance of the six
outside model branch sets.  They therefore do not remove the residual
identified by Corollary 4.4.  This is consistent with the source's trust
boundary.

## 6. Exact limitations

The result does not prove any of the following:

1. that the complete owner set has order three in every order-eight branch;
2. that one proper-subfamily linkage avoids the distinguished component;
3. that a linkage meeting the component leaves the connected residual
   required by Corollary 4.2;
4. that an order-seven boundary carries one equality partition on both
   closed shores; or
5. `HC_7`.

The exact remaining positive step is dynamic: a proper-minor colouring must
reroute one linkage off the reserved component, split it while keeping the
six outside contacts, or return a legal partition with its required
connected supports.
