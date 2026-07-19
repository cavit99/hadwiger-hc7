# Independent audit: two--three allocation in the ordered order-eight interface

**Verdict:** **GREEN** for Lemmas 2.1--5.1, Corollary 5.2,
Proposition 5.3, Theorem 6.1, and the stated trust boundary.  This is a
separate internal mathematical audit, not external peer review.  The result
is a conditional reduction and does not prove `HC_7`.

## Audited revision

This audit checks the complete source file
[`hc7_order8_ordered_two_three_allocation.md`](hc7_order8_ordered_two_three_allocation.md)
at SHA-256

```text
3f62092ab492815d5c21489e001e5732da76bc28454dac75206ba5aa61299dde
```

The promoted revision differs from the independently audited mathematical
source only in its status line and adjacent-audit link; the theorem statement
and proof are unchanged.

The following promoted inputs were also checked at the revisions pinned by
their adjacent GREEN audits:

- `hc7_order8_ordered_defect_crossing.md` at
  `434efeab93a4f693d212b4ee434532e81647df775a69494384ffcb3349735dde`;
- `hc7_merged_root_three_kempe_locks.md` at
  `2705b68b8452fd8642601ed48f93c84db98e313be46c12c3f4f7ba85cd94cd41`;
- `hc7_order8_three_portal_two_three_reduction.md` at
  `96595654a3e764710485c73c9dccd1f438f49d650e1d7f7c03dba9737514b202`;
  and
- `hc7_order8_small_boundary_lobe_descent.md` at
  `de980671b3053459e4e11845e510e5d96bb0a4f18d1a8bd50fe4b9dfae996d52`.

No unresolved mathematical gap was found in the audited source.  Two
proof-text issues found during the audit were repaired before the pinned
revision: the branch-set construction now explicitly permits its fifth set
to contain the literal vertex `x_e`, and the completed-cut proof explicitly
includes the case in which all five terminals lie in the separator.

## 1. Hypotheses and the induced two-part normalization

The displayed partition of `V(G)`, connectedness of `G[L]` and `G[R]`, and
absence of `L`--`R` edges make `L,R` precisely the two components of
`G-S`.  This fact is used correctly whenever `R` certifies that a returned
neighbourhood is an actual separation boundary.

The two spanning trees of the disjoint connected subgraphs `A_e,A_d`,
together with one stipulated edge between them, form a tree.  A tree in a
connected graph extends to a spanning tree, so deleting that selected edge
does give two connected vertex sets `E,D` covering `L`, with the two named
subgraphs wholly on their prescribed sides.  The induced graphs `G[E]` and
`G[D]` remain connected because they contain the corresponding tree
components, and the deleted tree edge makes them adjacent.

The contact equalities in (2.2) are justified rather than assumed.  The
inclusions in (1.3) give every required contact except possibly
`E`--`e` and `D`--`d`.  If `E` met `e`, then `G[E]` would be a connected
subgraph adjacent to both `d,e`, disjoint from `A_d`.  The GREEN-audited
ordered-defect crossing theorem applies with the same two full subgraphs
`P_0,P_1` and the same two deficient connected subgraphs, and gives an
explicit `K_7`-minor model.  This contradicts the standing hypothesis.  The
reverse orientation proves that `D` misses `d`.  Hence (2.2) is exact.

In particular, `P_d,P_{x_d},P_{y_d},P_{x_e}` are nonempty because
`A_e subseteq E` meets all of `S-{e}`, and `P_D` is nonempty because the
deleted tree edge joins `E,D`.

## 2. Literal portal multiplicities

For each of the three fixed Kempe paths, the first internal vertex after
`d` lies in `L`.  It cannot lie in `D`, since `D` has no neighbour at `d`,
so it lies in `E` and hence in `P_d`.  Proper alternation on an
`alpha`--`beta_i` path makes its colour `beta_i`.  The three `beta_i` are
distinct in one fixed colouring, so these three portal vertices are
distinct and `|P_d|>=3`.

If `P_D` were the singleton `{q}`, every path from `d` to `e` in
`G[L union {d,e}]` would start in `E`, eventually enter `D`, and use an
`E`--`D` edge whose `E`-end is `q`.  Thus every such path would contain the
same internal vertex `q`, contrary to the assumed two internally
vertex-disjoint `d`--`e` paths.  Therefore `|P_D|>=2`.

No conclusion here identifies a palette colour with a branch-set label.
The only colour use is to distinguish the three literal first vertices in
`P_d`.

## 3. The explicit seven branch sets

Under Lemma 3.1, the seven sets

```text
P_0, P_1, {x_d}, {y_d}, T, D union {e}, J union {d}
```

are pairwise disjoint.  The first two lie in `R`; the next five use distinct
boundary vertices and disjoint subsets of `E,D`; `J` is disjoint from `T`;
and `T` contains `x_e` but no other displayed boundary singleton.

They are connected: `P_0,P_1,J,T,D` are connected by hypothesis,
`D union {e}` is connected because `A_d subseteq D` sees `e`, and
`J union {d}` is connected because `J` meets `P_d`.

All twenty-one pairwise adjacencies are present:

- `P_0,P_1` are adjacent to each other, and their literal `S`-fullness
  makes each adjacent to the other five sets through
  `x_d,y_d,x_e,e,d`, respectively;
- the triangle `d x_d y_d d` gives the three adjacencies among
  `{x_d},{y_d},J union {d}`;
- the contacts of `T` with `P_{x_d},P_{y_d}` join it to the two singleton
  sets;
- `A_d subseteq D` joins `D union {e}` to both singleton sets;
- the boundary edge `x_e e` joins `T` to `D union {e}`;
- the stipulated `J`--`T` edge joins `T` to `J union {d}`; and
- the contact of `J` with `P_D` joins the last two sets.

Thus the construction uses only literal host edges and is a valid explicit
`K_7`-minor model.

## 4. Xie's completion and shortest-path absorption

Lemma 3.2 explicitly requires the five terminals
`a,b,x_e,p,q` to be distinct.  The invoked version of Xie's theorem has
exactly the seven virtual edges in (3.2): the pair edge and the six edges
between the terminal pair and terminal triple.  Six-connectivity of this
completion returns two disjoint connected subgraphs of the **original**
graph `F`, one containing the triple and one containing the pair; none of
the virtual edges is promoted to a host edge.

Since the triple subgraph `T` contains `x_e`, the disjoint pair subgraph
`J_0` avoids `x_e` and hence lies in `E`.  The triple subgraph meets `E` at
the distinct vertices `a,b`.  A shortest path in connected `G[E]` from
`J_0` to `T cap E` has no internal vertex in either endpoint set.  Absorbing
all but its `T`-endpoint into `J_0` therefore preserves connectedness and
disjointness and creates a literal edge from the enlarged `J` to `T`.
The pair portals and triple portals are retained, so the seven sets audited
in Section 3 apply directly, with `T` itself as the fifth branch set.

The common-portal completion likewise has five distinct terminals.  Indeed,
`|P_D|>=2` gives `q` distinct from `v`; `|P_d|>=3` gives `p` outside
`{v,q}`; and `|E|>=4` gives `w` outside `{p,q,v}`.  The vertex `x_e` is
outside `E`.  Its returned triple set contains `v,x_e`, and the equality
`P_{x_d}=P_{y_d}={v}` supplies both named boundary contacts.  The filler
`w` is used only to meet the five-terminal theorem's distinctness
requirement.

The source correctly retains small completions.  The completion has
`|E|+1` vertices, and a six-connected graph must have at least seven
vertices.  No separator conclusion is inferred when its order is at most
six.

## 5. Hall collapse

Let `I` be a Hall-deficient family and `Z` its union.  If `P_D in I`, write
`J` for the subset of the three boundary labels `d,x_d,y_d` represented in
`I`.  Then `|Z|<=|J|`.  For a component `C` of `G[E-Z]`:

- every neighbour in `E` lies in `Z`;
- it has no neighbour in `D`, because every `E`-vertex with a `D`-neighbour
  belongs to `P_D subseteq Z`;
- it misses each boundary vertex in `J`, since its entire portal set is in
  `Z`;
- it misses `e` by (2.2); and
- it has no neighbour in `R`.

Therefore its neighbourhood is contained in
`Z union (S-({e} union J))` and has order at most
`|J|+(7-|J|)=7`.  The nonempty set `R` remains outside
`C union N_G(C)`, so this is an actual separation, not merely a numerical
cut bound.  If instead `E=Z`, then `|E|<=3`; the lower bound
`|P_d|>=3` forces the retained `|E|=3` outcome.

If `P_D` is absent from `I`, then `I` contains at most the three sets
`P_d,P_{x_d},P_{y_d}`.  A deficient family containing `P_d` would have a
union of order at least three but be required to have order at most two,
which is impossible.  Nonempty portal sets rule out a deficient singleton.
The only remaining family is therefore `{P_{x_d},P_{y_d}}`; its two
nonempty sets have union of order at most one and hence are the same
singleton.  The three Hall alternatives are exhaustive.

## 6. The common portal

For a common portal `v`, properness and its adjacency to both `x_d,y_d`
exclude their two distinct colours.  The explicit six-colour palette in
Section 1 leaves exactly `alpha,beta_1,beta_2,beta_3`.

If `v` has colour `beta_j`, a path `K_i` with `i!=j` avoids `v`.  If it has
colour `alpha`, the two internally disjoint paths in `H` cannot both use
the internal vertex `v`, so one avoids it.  Thus a `d`--`e` path `Q`
avoiding `v` exists in either case.

The path starts in `E`, and before ending at `e` it must first enter `D`.
The consecutive segment from its first `E`-vertex to the `E`-vertex just
before that first entry is a connected subgraph of `E-v`; its first vertex
lies in `P_d` and its last in `P_D`.  A shortest path in `G[E]` from this
segment to `v`, with `v` excluded from the absorbed vertices, preserves a
connected subgraph disjoint from and adjacent to `G[{v,x_e}]`.  When
`v in P_{x_e}`, that two-vertex subgraph is connected, contains `x_e`, and
meets both `P_{x_d},P_{y_d}`.  Lemma 3.1 therefore yields the claimed
minor.

## 7. A non-six-connected completion

When `|E|>=6`, the completion has at least seven vertices.  Failure of
six-connectivity therefore supplies a vertex separation with separator
`K` of order at most five and two nonempty open sides.

The terminal-side classification is correct.  A pair terminal surviving
outside `K` is virtually adjacent to the other pair terminal and to every
surviving triple terminal.  Hence, if nominated terminals occur in both
open sides, neither pair terminal can survive: both are in `K`, and the
surviving triple terminals occur on both sides.  If nominated terminals
occur in at most one side, a terminal-free side exists.  This includes the
edge case in which all five terminals are contained in `K`.

In the terminal-free case, a component of a terminal-free side contains no
endpoint of a virtual edge, so its connectedness is witnessed by original
edges.  In the split-triple case, both pair terminals are in `K`, so every
virtual edge incident with a surviving triple terminal ends in `K`; a
component containing such a terminal is again connected by original edges.
Choosing a side not containing `x_e` (or either side when `x_e in K`)
ensures `C subset E`.

The chosen `C` is proper.  The opposite open side contains a vertex outside
`C`; if that vertex is in `E`, this is immediate.  If its only possible
vertex outside `E` is `x_e`, then the virtual neighbours of `x_e` in the
terminal pair must be in `K`, so `K cap E` is nonempty and again lies
outside `C`.  Thus `C` is a nonempty connected proper subset of `E`.

No original edge crosses between the two open sides, so
`N_E(C) subseteq K cap E`.  All other neighbours of `C` lie either in `D`
or in `S`; none lies in `R`, and `e` is absent by (2.2).  These are disjoint
vertex classes, proving (5.3).  A vertex in the other open side and the
entire nonempty opposite shore `R` remain outside `C union N_G(C)`, so its
full neighbourhood is an actual host separation boundary.  The virtual
edges are used only to discover the cut.

## 8. Small boundary and positive excess

Seven-connectivity forces every actual separator `B=N_G(C)` obtained above
to have order at least seven.  At order eight, `C` is a nonempty connected
proper subset of the original component `L` of `G-S`, and (5.3) gives

```text
|N_{G[L]}(C)| + |N_G(C) intersect S| = 8.
```

These are exactly the hypotheses of the GREEN-audited small-boundary lobe
theorem: `S` has order eight, `L,R` are distinct components of `G-S`, and
the global minor-critical assumptions are (1.1).  It returns only the
claimed order-seven separation or strict order-eight boundary-full lobe
descent.

When `|B|>=9`, the three disjoint terms in (5.3) give

```text
|N_D(C)| + |N_G(C) intersect S|
    >= 9 - |N_E(C)| >= 9 - |K| >= 4.
```

The occurrence of `x_e` in `K` causes no overcount: (5.2) uses
`K cap E`, so `|N_E(C)|<=|K cap E|<=|K|`.  The source calls this positive
excess an open residue and does not assert that it decreases under further
operations.

## 9. Operation-specific colouring obstruction

For every boundary edge `uv` with `u in C` and `v in B`, the deletion
`G-uv` is a proper minor and hence has a six-colouring.  Every such colouring
makes `u,v` equal; otherwise the deleted edge can be restored and gives a
six-colouring of `G`.

The fixed merged-root colouring is defined on all of `C union B`: by (5.3)
this set is contained in `L union S`.  If an outer colouring of `G-C`
induced the same equality partition on `B`, the bijection between its used
boundary colours and the fixed colouring's boundary colours would extend to
a permutation of the six colour names.  After that permutation the two
colourings agree vertexwise on `B`.  The fixed inner colouring covers every
edge with an endpoint in `C`, including the deleted edge, while the outer
colouring covers all remaining edges.  They therefore glue to a proper
six-colouring of `G`, a contradiction.  Thus the boundary partitions must
differ as claimed.

This proves incompatibility, not compatibility, of the operation-specific
response with the fixed response.

## 10. Exhaustiveness and trust boundary

If the four portal sets have distinct representatives, the selected
completion is either six-connected, of order at most six, or has order at
least seven and is not six-connected.  Lemma 3.2 closes the first case;
outcome 4 retains the second; and Lemma 5.1 plus Corollary 5.2 gives an
order-seven separation, a strict order-eight descent, or the positive-
excess residue in the third.

If distinct representatives fail, Hall's lemma gives an actual separator
of order at most seven, the three-vertex part, or the common portal.
Seven-connectivity makes the first separator have order exactly seven.  A
common portal adjacent to `x_e` is closed by Lemma 4.2.  Otherwise the
common-portal completion exists for `|E|>=4` and has the same exhaustive
three connectivity/order alternatives.  The remaining case has
`|E|<=3`, while Lemma 2.2 gives `|E|>=3`, so it is precisely the retained
small part.

The source accurately records all remaining obligations.  It does not
eliminate a completion of order at most six, the Hall three-vertex part, or
the positive-excess lobe.  It does not show that a structural order-seven
separation carries a common equality partition, that positive excess is a
well-founded rank, or that later minor operations preserve the labels
`E,D,P_0,P_1`.  It proves only the stated unbounded closure of every
six-connected five-terminal completion inside its conditional setting.

I attempted to falsify the argument at the collision points most likely to
hide a label error: overlapping portal sets, a common portal belonging to
`P_D` or `P_d`, placement of `x_e` in every completed-cut position, all five
terminals contained in `K`, and an opposite open side consisting only of
`x_e`.  Each is covered by the literal choices and cut analysis above.  No
counterexample to the stated conditional reduction was found.
