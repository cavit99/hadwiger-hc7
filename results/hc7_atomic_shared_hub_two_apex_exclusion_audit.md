# Independent audit of the atomic shared-hub two-apex exclusion

**Verdict:** GREEN.

## Audited revisions

- theorem note:
  [`hc7_atomic_shared_hub_two_apex_exclusion.md`](hc7_atomic_shared_hub_two_apex_exclusion.md),
  SHA-256
  `46da8f85aab2377516135937a5fbb35caa71ac10b53ed90125240f8acbfd191c`;
- retained verifier:
  [`hc7_atomic_shared_hub_two_apex_exclusion_verify.py`](hc7_atomic_shared_hub_two_apex_exclusion_verify.py),
  SHA-256
  `6b8b6483b8576eeb6fc552a93f866f182332ee6ab30d1b06d4d8c9b16df9bd08`.

I did not alter either audited file.  I compared the graph builder against
the independently retained builder for the prior
[`shared-hub barrier`](../barriers/hc7_atomic_shared_hub_defect_rotation_barrier.md),
reran the verifier, and used a separate temporary audit program with a
different certificate parser.

## 1. Graph identity

The construction starts with the nineteen edges of
`K_7-{ab,cd}` on `a,...,g` and the four edges from `x` to `a,b,c,d`.
Replacing `ac,bd,ad,bc,fg` by two-edge paths adds the five vertices
`p_ac,p_bd,p_ad,p_bc,h` and increases the edge count by five.  The four
edges from `f,g` to the indicated `p`-vertices and the two edges `eh,hx`
then give

\[
                         |V(G_*)|=13,\qquad |E(G_*)|=34.
\]

The two implementations have identical labelled vertex and edge sets.
The degree calculation also agrees with the note: `f` retains its six
core incidences, with `h` replacing `g`, and gains `fp_ac,fp_bd`; symmetrically
`g` gains `gp_ad,gp_bc`.  Thus both have degree eight.

## 2. Exhaustive two-object calculation

The object universe has `13+34=47` distinct members.  Its subsets of order
at most two split exactly as follows:

\[
  1+13+34+\binom{13}{2}+13\cdot34+\binom{34}{2}
   =1+13+34+78+442+561=1129.                              \tag{2.1}
\]

In particular, the 442 mixed cases include the redundant choices in which
the selected edge is incident with the selected vertex, exactly as required
by the deletion convention in the theorem.  The verifier's universe and
combination loops enumerate each of these sets once.  Its deletion routine
removes a selected vertex first and removes a selected edge only if that
edge survives, which implements the stated convention.

I reran

```text
.venv/bin/python -B results/hc7_atomic_shared_hub_two_apex_exclusion_verify.py
```

and obtained

```text
GREEN shared-hub two-apex exclusion
deletion_cases=1129 none=1 v=13 e=34 vv=78 ve=442 ee=561
kuratowski_certificates={'TK3,3': 974, 'TK5': 155}
icosahedral_sharpening=G_*-{f,g} contains the displayed TK5
consequence=no subdivision of G_* embeds in a two-apex graph
```

For every deletion set, the returned certificate is checked to use only
vertices and edges of the corresponding remainder.  The retained parser
then follows each maximal degree-two path between branch vertices.  It
rejects repeated core edges and accepts only a five-vertex 4-regular simple
core or a six-vertex 3-regular bipartite simple core.  These are respectively
`K_5` and `K_{3,3}`.

As a cold cross-check, my temporary parser removed every traversed
certificate edge from an unused-edge set, rejected closed branch paths and
parallel core paths, and tested the resulting core by graph isomorphism
against `K_5` and `K_{3,3}`.  It independently reproduced all six case
counts and the split of 155 `TK_5` and 974 `TK_{3,3}` certificates.  Thus
every one of the 1,129 remainders contains a literal Kuratowski subdivision,
which proves Theorem 2.1.

## 3. Audit of the subdivision reduction

Let `S` be a subdivision of `G_*` in a graph `J`, and suppose
`J-Z` is planar for a set `Z` of at most two vertices.  Each member of `Z`
has one of the following exact effects on `S`.

1. A vertex outside `S` affects no route and records no object.
2. The image of a vertex `v` of `G_*` records the vertex object `v`.
   Removing it breaks exactly the routes representing edges incident with
   `v`; discarding those route remnants leaves the subdivision with `v`
   deleted.
3. An internal vertex of a subdivided route belongs to a unique route,
   because distinct edge routes in a subdivision are internally disjoint.
   Recording that edge object and discarding the entire broken route has
   exactly the effect of deleting that edge of `G_*`.

If both deleted vertices are internal on the same route, they record one
repeated edge object and discarding that route once is sufficient.  If a
deleted branch vertex and the other deleted vertex lie on one of its
incident routes, the edge record is redundant after the vertex record,
which is precisely one of the mixed cases included in Theorem 2.1.  Two
different internal routes, or a branch vertex together with an unrelated
route, give two distinct objects.  Therefore all possibilities, including
apices outside the subdivision, branch vertices, internal edge vertices,
and repeated records, produce a set

\[
                 D\subseteq V(G_*)\mathbin{\dot\cup}E(G_*),
                 \qquad |D|\le2.
\]

All edge routes representing surviving objects avoid the deleted vertices
and remain mutually internally disjoint.  After the broken remnants are
discarded, `S-Z` therefore contains a subdivision of `G_*-D`, not merely a
minor with unidentified ownership.  This subdivision lies in the planar
graph `J-Z`, while Theorem 2.1 supplies a Kuratowski subdivision in
`G_*-D`.  Subdividing that Kuratowski graph again would put a subdivision
of `K_5` or `K_{3,3}` in `J-Z`, a contradiction.  This proves the full
two-apex corollary.  Deleting the complete two-vertex factor from
`K_2\vee P` leaves `P`, so its stated specialisation is immediate.

## 4. Icosahedral sharpening

In `K_2\vee I`, where `I` is the icosahedral graph, the twelve vertices of
`I` have degree `5+2=7`, while each vertex of the complete factor has
degree `12+1=13`.  A degree-eight branch vertex of a subdivision needs
eight distinct first edges on its incident subdivided routes.  Hence the
distinct vertices representing `f` and `g` must be exactly the two
complete-factor vertices.

After deleting them, every route between surviving branch vertices remains
inside the planar graph `I`.  The displayed paths in `G_*-{f,g}` give all
ten pairs among roots `b,c,d,e,x`:

```text
b-p_bc-c,
b-p_bd-d,
c-p_ac-a-p_ad-d,
e-h-x,
```

together with the six literal edges `be,bx,ce,cx,de,dx`.  Their internal
vertex sets are respectively `\{p_bc\}`, `\{p_bd\}`,
`\{p_ac,a,p_ad\}`, `\{h\}` and six empty sets, so they are pairwise
disjoint and avoid the roots.  They form a subdivision of `K_5`.  Its image
would survive in `I`, contradicting planarity.  The verifier checks these
routes, and the independent audit reconstructed all ten root pairs and
their disjoint interiors.

## 5. Unresolved issues and scope

There are no unresolved assumptions or proof gaps for the exact labelled
`G_*` subdivision statement or its two-apex and icosahedral consequences.
The finite theorem remains computer-assisted, with the retained Python and
NetworkX runtime inside its software trust boundary; the generated
Kuratowski subdivisions and the independent parser materially narrow that
boundary.

As the theorem note correctly states, this result does not exclude a minor,
weak immersion, or less literal dirty-path configuration that fails to
contain a subdivision of the exact graph `G_*`.  That is a scope boundary,
not a gap in the audited claims.
