# Independent audit: named-model packet orientation

Audited file:
`results/hc7_exact7_named_model_packet_orientation.md`.

Audited SHA-256:
`cbf0cc803ef2d7a098e40b4eb79a365682282168fa61c8664d4404d7db6837a6`.

Current SHA-256:
`1bd12fb3ebad33f26458799b0f4cb8b92997c2806d0df828b80b25ffee6fe93d`.
The only post-audit change was the status line recording this audit.

**Verdict:** **GREEN.**

The five-root fan preserves every original branch bag, has one distinct
literal boundary root in each enlarged bag, and uses at most six boundary
vertices in total.  Two disjoint full packets on the opposite open side
therefore produce seven disjoint connected branch sets with every required
adjacency witnessed literally.  It follows that the named model has only
one opposite component, that component has packet number one, and named
models on both components force packet vector `(1,1)`.

No mathematical repair is needed.  The conclusions do not use pairwise
disjointness of different named models and do not imply a strict recursive
descent, exactly as the source says.

## 1. Setup and fullness (lines 12--29)

Let `C` be any component of `G-S`.  Its neighbourhood is contained in `S`.
Because `G-S` has another component, deleting `N_G(C)` separates two
nonempty vertex sets.  Seven-connectivity gives

\[
                       |N_G(C)|\ge 7.
\]

Since `|S|=7`, necessarily `N_G(C)=S`.  Thus every component is connected
and has a neighbour at every literal boundary vertex, so it is itself an
`S`-full packet.  This verifies lines 13--15 and the later positivity
argument for packet numbers.

Ownership at lines 17--26 is the precise hypothesis used later: every
off-boundary vertex of the named support lies in one component `C`.  The
audited split-edge separator handoff supplies this property.  Once boundary
exclusion is proved, each preserved named model has an off-boundary vertex,
so its owner component is unique.

## 2. Boundary exclusion (lines 33--55)

Let `W` be the support of a boundary-contained `K_5` model.  The bound
`|W|<=6` and `|S|=7` leave a literal vertex `x in S-W`.  Choose distinct
components `C,D` of `G-S`.  The proposed branch sets are

\[
                B_1,\ldots,B_5,\qquad C\cup\{x\},\qquad D.       \tag{A.1}
\]

They are pairwise disjoint: the five original bags are disjoint subsets of
`W`, the components lie outside `S`, `C` and `D` are distinct, and `x` was
chosen outside `W`.  Each original bag and `D` is connected, while an
`x-C` edge supplied by fullness makes `C union {x}` connected.

Every clique adjacency has an explicit witness.

| Pair | Witness |
|---|---|
| `B_i,B_j` | the given `K_5` model |
| `B_i,C union {x}` | choose any boundary vertex in `B_i`; it has a neighbour in `C` |
| `B_i,D` | the same boundary vertex has a neighbour in `D` |
| `C union {x},D` | fullness of `D` at `x` gives an `x-D` edge |

Thus (A.1) is a literal `K_7` model.  Lemma 2.1 is correct, and the strict
support bound is used exactly to leave `x`.

## 3. Five-root fan (lines 59--116)

### 3.1 Representative deletion and linkage budget

There are five nonempty disjoint branch bags.  Hence a support of order at
most six has exactly one of the following forms:

* five singleton bags; or
* four singleton bags and one two-vertex bag.

After one representative `a_i` is selected from each bag, the remainder
`D=V(M)-A` therefore has order zero or one.  If `D={d}`, then `d` and the
representative from its bag are adjacent because that two-vertex bag is
connected.

Put `s=|A_S|`, so `r=|A_0|=5-s`, and let

\[
                       H=G-(D\cup A_S).
\]

The deleted sets are disjoint, and deletion of `|D|+s` vertices from a
seven-connected graph leaves connectivity at least

\[
             7-|D|-s = r+2-|D| \ge r.                          \tag{A.2}
\]

The target set is exactly the surviving part of the boundary not occupied
by representatives:

\[
                 S_0=S-(D\cup A).
\]

As `A_0` is outside `S`, its order satisfies

\[
          |S_0|=7-s-|D\cap S|
                 \ge 7-s-|D|=r+2-|D|\ge r.                    \tag{A.3}
\]

The sets `A_0` and `S_0` are disjoint subsets of `H`, of orders `r` and at
least `r`.  The set form of Menger therefore gives `r` pairwise
vertex-disjoint `A_0`--`S_0` paths.  Because there are exactly `r` paths
and exactly `r` vertices in `A_0`, every representative in `A_0` is the
end of one path; vertex-disjointness also prevents any other representative
from occurring internally on a path.  The boundary ends are distinct.
The case `r=0` is the valid empty linkage.

### 3.2 First-hit truncation

Every `a_i in A_0` belongs to the owner component `C`.  Before its path
first meets `S`, it cannot leave `C`, because different components of
`G-S` have no edge between them.  Truncating at that first boundary vertex
therefore leaves a path in `C union S` whose only boundary vertex is its
end.  All first-hit ends lie in `S_0`, because `D union A_S` was deleted.

For each `a_i in A_S`, the zero-length path `{a_i}` is disjoint from all
Menger paths: every member of `A_S` was deleted before those paths were
found.  Its end is also distinct from every end in `S_0`.  Consequently
there are exactly five pairwise distinct roots, one in each provisional
bag.

### 3.3 Whole-bag preservation, disjointness, and boundary count

If `D` is empty, every original bag is the singleton representative already
on its corresponding path.  If `D={d}`, adjoining `d` and its edge to the
path beginning at the representative of the unique two-vertex bag restores
that entire bag.  The vertex `d` cannot collide with another path because
it was deleted before the linkage was chosen.

Thus every `R_i` contains the whole original `B_i`.  In particular, every
original interbag witnessing edge is still present, so the five `R_i` are
pairwise adjacent.  The construction adds vertices but never transfers a
branch-bag vertex to a different enlarged bag.

The five truncated or zero-length paths contribute exactly their five
distinct boundary ends and no other boundary vertices.  The only possible
extra boundary vertex is `d`, and there is at most one such vertex.  Hence

\[
                 \left|S\cap\bigcup_{i=1}^5V(R_i)\right|\le6. \tag{A.4}
\]

This covers the two extreme cases that are easiest to mishandle:

* if all five representatives lie in `S` and the sixth support vertex lies
  in `C`, all five paths are trivial and that sixth vertex is restored to
  its own bag; and
* if `d in S` while its representative lies in `C`, the corresponding
  enlarged bag contains its first-hit root and `d`, giving six boundary
  vertices in total but still leaving one unused literal vertex.

All four conclusions of Lemma 3.1 follow.

## 4. Opposite two-packet construction (lines 120--154)

By (A.4), choose

\[
                 x\in S-\bigcup_iV(R_i).
\]

Let `P,Q` be disjoint `S`-full packets in the union of components other
than `C`.  The seven proposed branch sets are

\[
                    R_1,\ldots,R_5,\qquad P\cup\{x\},\qquad Q. \tag{A.5}
\]

They are disjoint.  Each `R_i` lies in `S union C`; both packets lie in
`G-S-C`; the packets are disjoint from one another; and `x` lies in none of
the first five bags or either packet.

They are connected.  The `R_i` and `Q` are connected by construction and
definition.  Fullness of `P` at `x` supplies an edge attaching `x` to `P`.

Finally every required adjacency is literal.

| Pair | Witness |
|---|---|
| `R_i,R_j` | preserved adjacency of `B_i,B_j` |
| `R_i,P union {x}` | the `P`-edge to the chosen root in `R_i cap S` |
| `R_i,Q` | the `Q`-edge to that same root |
| `P union {x},Q` | the `Q`-edge at the unused boundary vertex `x` |

The five roots are distinct, although distinctness is stronger than the
adjacency check needs; it is needed for the disjoint rooted fan.  The
argument works whether `P,Q` lie in different components or in the same
opposite component.  No unproved `P-Q` edge is used.  Thus (A.5) is a
genuine `K_7` model, proving the opposite-two-packet exclusion.

## 5. Component and packet conclusions (lines 156--178)

Every component of `G-S` is an `S`-full packet by Section 1.  If two
components other than the owner `C` existed, taking those two components as
`P,Q` would contradict Theorem 4.1.  At least one opposite component exists
by hypothesis, so there is exactly one; call it `D`.

The packet number of `D` is at least one because `D` itself is a full
packet, and at most one because two disjoint full packets in `D` would be
two packets on the opposite open side.  Hence it is exactly one.

If a second named small model is owned by `D`, applying the same theorem
with `C,D` interchanged makes the packet number of `C` exactly one.  Thus
named models on both sides force packet vector `(1,1)`.  In a `2+1`
ownership distribution, both sides contain a named model, and the model
with the unique label supplies an unambiguous label-preserving orientation.
No comparison of shore orders occurs in the proof.

The argument is model-by-model, so different named supports may overlap.
If the three named supports happen instead to be pairwise disjoint, any
two-vertex set meets at most two of them.  Such a set therefore cannot be a
global transversal of all support-at-most-six models, as lines 175--178
claim.

## 6. Counterexample search and sharpness

The following failure modes were tested directly against the construction.

1. A path cannot consume another branch representative: all boundary
   representatives and the possible sixth support vertex were deleted, and
   the `r` disjoint linkage paths exhaust `A_0` as their distinct ends.
2. A first-hit path cannot wander into another open component before
   reaching the boundary: components of `G-S` are anticomplete.
3. Restoring the possible sixth support vertex cannot break disjointness:
   that vertex was absent during the linkage and is restored only to its
   own two-vertex bag.
4. The two packet bags do not need a pre-existing edge: the unused literal
   boundary vertex joins them.
5. Three or more components do not evade the packet statement: any two
   opposite components themselves supply the forbidden packet pair.

The support bound is sharp for the boundary-exclusion mechanism.  In the
standard seven-connected, `K_7`-minor-free example `I vee K_2`, where `I`
is the icosahedral graph, the exact boundary is `K_2 vee C_5`.  It has a
seven-vertex `K_5` model with bags

\[

 \{u\},\quad\{v\},\quad
 \{c_0,c_1\},\quad\{c_2,c_3\},\quad\{c_4\},
\]

where `u,v` are the two universal vertices and
`c_0c_1c_2c_3c_4c_0` is the boundary cycle.  All seven boundary vertices
are used, so there is no unused `x`; Lemma 2.1 correctly stops at support
six.

The same example also shows that the trust boundary is real rather than a
proof artefact.  For the separator consisting of `u,v` and the neighbours
of an icosahedral vertex `w`, one component is `{w}` and the other contains
the six remaining icosahedral vertices.  A triangular face through `w`,
together with `u,v`, is a five-vertex named `K_5` owned by the first
component.  A triangular face not incident with `w`, necessarily using a
vertex of the other component because the boundary cycle is triangle-free,
gives another named `K_5` owned by the opposite component.  The audited
theorem therefore orients this genuine survivor to packet vector `(1,1)`;
it cannot be strengthened to eliminate that vector or to supply strict
descent without additional hypotheses.

No counterexample survives the representative-deletion, branch-bag,
boundary-budget, packet-adjacency, component-count, or packet-vector tests.

## 7. Editorial bookkeeping

After this audit is adopted, line 3 of the source may be changed from
`independent audit still required` to `independently audited`.  This is a
status-only edit, not a mathematical repair.  For complete local
self-containment, the source could also spell out the repository convention
that packet number means the maximum size of a family of pairwise
vertex-disjoint `S`-full packets, but every use in the proof already matches
that convention.
