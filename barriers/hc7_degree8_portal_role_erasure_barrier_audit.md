# Audit: terminal-free portal role-erasure barrier

## Verdict

**GREEN** at the exact revisions

```text
f384c2666d7d805184abf119a270bfeb8596403429551c074259dfec36d05c95  barriers/hc7_degree8_portal_role_erasure_barrier.md
047438792a76fe95d86e515080d34c38067e838079e4c6554af6dd5ba18f5d16  barriers/hc7_degree8_portal_role_erasure_barrier_verify.py
```

This is a separate internal audit, not external peer review.  The example
validly refutes only the stated local inference that two independently
completed terminal-free cuts must retain different `I`- and `T`-roles.  It
does not refute `HC_7` or the live host-level target using seven-connectivity,
minor-critical colouring responses, and `K_7`-minor exclusion.  During this
audit, Lemma 1.1 was repaired to state explicitly the necessary condition
`C cap K=emptyset`; the bound revision above includes that correction.

## Boundary and shores

The boundary graph is exactly the disjoint union of two triangles and one
edge.  It consequently has order eight, independence number three, and no
`K_4` minor after deleting any two vertices: every remaining component is a
subgraph of a triangle.  The roots `p,q` are nonadjacent and `I,T` are
independent.

The vertex `u` has neighbourhood exactly `S`.  After deleting `N[u]`, the
only components are the connected sets `Q` and `F`; both meet every boundary
vertex and there are no edges between them.  The seven-vertex order of `Q`
is indeed just beyond the portal reduction's `|Q|<=6` alternative.

## Colourings, paths, and incidence splits

Both displayed closed-shore colourings are proper.  Their boundary equality
partitions are respectively

```text
I | T | {p,q}
I | T | {p} | {q}.
```

The paths `p-a-c-b-q` and `p-x-y-q` are boundary-clean and alternate in the
two relevant colours.  In each colouring the path places `p,q` in one full
bichromatic component while the corresponding boundary bichromatic graph
has them in distinct singleton components.  They therefore certify the two
opposite failed lifts.  Their interiors lie in different open shores and
their union is a simple seven-cycle.

Deleting the first path interior leaves exactly the four singleton
components displayed in the source.  Their contacts split each of `I,T`
between several incidence components, and all four have boundary defect at
least six, so none is a two-defect component.  The second path fills `F`;
the two incidence graphs there have only the isolated block vertices and
hence are split.  Thus all four incidence-split assertions, including the
vacuous filled-shore cases, are correct.

## Universal entanglement

The verifier exhausts every nonempty connected subset of each shore.  It
finds 17 root connectors and 40 carriers for each block in `Q`, and one root
connector and three carriers for each block in `F`.  It checks every
connector--carrier pair, not merely selected witnesses, and none is
disjoint.

This also has a direct structural explanation.  Every root connector in
`Q` contains the unique root portals `a,b`.  A carrier for either block
which avoids one of these portals is forced through the other one.  In `F`,
the unique root connector contains both `x,y`, so it meets every nonempty
carrier.

## The two completions and common lobe

Both nominee maps use five distinct valid representatives.  For each map,
the seven virtual completion edges have both ends among the nominees.  With

```text
K={a,b,r2,r3,s3},  C={c},
```

deleting `K` from either completion leaves exactly the components `{c}` and
`{d}`.  The first is terminal-free for both nominee sets, so the two portal
applications genuinely return the same literal lobe rather than merely
isomorphic lobes.

The arithmetic is exact:

```text
N_Q(C)=K,  |N_Q(C)|=5,
N(C) cap S={i2,i3,t2,t3},  |N(C)|=9,
|S-N(C)|=4=|N_Q(C)|-1.
```

The surviving vertex `d` proves that this is an actual separation.  Hence
the positive-excess and boundary-defect assertions match the completed-cut
reduction exactly.

## Absence of the desired pair and exact scope

Proposition 4.1 is correct.  A common six-element boundary contact set for
two disjoint connected subsets cannot contain `p` or `q`, because their
unique `Q`-neighbours are `a` and `b`.  It would therefore have to be all of
`I union T`.  Meeting both `i1` and `t1` forces each set through
`{a,d}` and `{b,d}`.  If neither set contains `d`, both contain `a,b`; if
one contains `d`, disjointness excludes `a,b` from that set, leaving it as
the singleton `{d}`, which misses four required contacts.  Both cases are
impossible.  The verifier independently exhausts the adjacent subclass
needed by the proposed conclusion and finds maximum common contact order
two.

The scope exclusions are also genuine.  The vertex `r3` has degree two, so
the graph is not seven-connected.  The displayed proper five-colouring of
the whole graph is valid.  Restricted to any edge-deleted graph, it keeps
the ends of that original edge different, so the universal monochromatic-
endpoint response required by contraction-criticality fails.  The source
correctly makes no claim that this local graph is `K_7`-minor-free.

## Verifier replay

Every executable check uses the always-active `require` function.  Ordinary
and optimized runs produced identical output:

```text
python3 barriers/hc7_degree8_portal_role_erasure_barrier_verify.py
python3 -O barriers/hc7_degree8_portal_role_erasure_barrier_verify.py

GREEN degree8 portal role-erasure local barrier
boundary: order=8 alpha=3; shores=(7,2); bilateral_cycle=7; Q_residual_components=4 two_defect=0
entanglement: QI=(17,40) QT=(17,40) FI=(1,3) FT=(1,3)
common_lobe: internal_boundary=5 full_boundary=9 defect=4; connected_subsets=65 adjacent_disjoint_pairs=200 max_common_contacts=2
scope: not seven-connected; globally five-colourable; no critical entering-edge responses
```

The executable does not separately run a generic minor detector on the
boundary deletion condition; the explicit disjoint-union structure proves
that condition immediately.  It also exhausts only adjacent connected pairs,
while the written proof establishes the stronger assertion for all disjoint
connected pairs.  These are coverage distinctions, not mathematical gaps.
No unresolved issue remains in the concrete barrier or its stated scope.
