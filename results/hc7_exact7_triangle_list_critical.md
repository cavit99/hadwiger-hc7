# Exact-seven triangle-free list-core classification

## 1. Purpose

The audited spanning-triangle state theorem reduces the live exact-seven
`(1,3)` adhesion to the following finite boundary question.  A triangle-free
graph `F=G[S]` has order seven, and every literal boundary vertex `s` has a
nonempty carrier-contact list

\[
                 \Lambda(s)\subseteq\{1,2,3\}.
\]

If `F` is properly colourable from these lists, the two proper-minor states
glue and the hypothetical `HC_7` counterexample is six-colourable.  This note
classifies the possible uncolourable boundary states after forced colours are
removed.  Its main reusable consequence is that every nonconflicting survivor
has a propagated core with at least five literal boundary vertices confined
to two colours.  This is a statement about the propagated lists, not
necessarily about the raw carrier-contact lists before singleton colours are
assigned.

The classification is exhaustively verified by
`../active/hc7_exact7_triangle_list_critical_verify.py`.

## 2. Unit propagation

Given a list instance `(F,\Lambda)`, perform the following operation whenever
`\Lambda(x)={c}`:

1. assign colour `c` to `x` and delete `x`; and
2. remove `c` from every remaining neighbour's list.

If a list becomes empty, call the result a **unit conflict**.  Every individual
step preserves colourability in both directions, so the original instance is
uncolourable precisely when propagation produces a unit conflict or leaves an
uncolourable residual instance.  In a nonconflicting residual instance every
list has size at least two and therefore belongs to

\[
              \{12,13,23,123\}.                         \tag{2.1}
\]

## 3. Critical cores

A residual instance `(H,L)` is called **critical** here if it is uncolourable
but becomes colourable after any one of the following operations:

* delete a vertex;
* delete an edge; or
* add one missing palette colour to one list.

Every uncolourable residual instance on at most seven vertices contains such
a core.  Indeed, first delete vertices and edges while uncolourability
persists, and then enlarge lists while uncolourability persists.  Deletion
minimality is not destroyed by later list enlargement, since enlarging lists
cannot destroy a colouring of a deleted subinstance.  The resulting graph is
connected.  Up to graph isomorphism and permutation of the palette, the
critical cores are exactly the following ten instances.

| ID | graph6 | edges | lists `vertex:list` |
|---|---|---|---|
| T1 | `Dhc` | `01 04 12 23 34` | `0:12 1:12 2:12 3:12 4:12` |
| T2 | `ElEG` | `01 03 05 12 23 34 45` | `0:12 1:13 2:23 3:12 4:13 5:23` |
| T3 | `FhCKG` | `01 06 12 23 34 45 56` | all seven lists `12` |
| T4 | ``F`EBW`` | `01 05 16 23 26 34 46 56` | `0:12 1:13 2:12 3:13 4:23 5:23 6:23` |
| T5 | `Fh_gg` | `01 04 12 23 25 36 45 56` | `0:12 1:12 2:13 3:23 4:13 5:13 6:12` |
| T6 | `FhEK_` | `01 05 06 12 23 34 36 45` | `0:12 1:13 2:13 3:12 4:23 5:23 6:12` |
| T7 | `FXJGg` | `02 05 12 15 23 24 36 45 56` | `0:12 1:13 2:12 3:12 4:23 5:123 6:12` |
| T8 | `FpUK_` | `01 02 05 06 14 23 34 36 45` | `0:123 1:12 2:12 3:12 4:12 5:13 6:13` |
| T9 | `FlO[O` | `01 03 06 12 14 23 35 45 46` | `0:123 1:123 2:12 3:12 4:12 5:12 6:12` |
| T10 | `FhELO` | `01 05 06 12 23 26 34 45 46` | `0:12 1:13 2:23 3:12 4:13 5:23 6:123` |

Here “contains” means that one may select a vertex set, retain a subgraph on
it, and enlarge the selected original lists to the displayed core lists.  In
particular, if a displayed core list is a pair, then the corresponding list
in the propagated instance is that exact pair.

The table has a compact topological interpretation.  `T1,T3` are odd cycles;
`T2,T5,T6` are theta graphs; `T4` is two four-cycles sharing one vertex; `T7`
is a four-path theta; `T8` is a subdivision of a three-vertex multigraph; and
`T9,T10` are subdivisions of `K_4`.  Hence every critical core has minimum
degree two, at most nine edges, cyclomatic number at most three, treewidth at
most three, and at least five vertices with two-element lists.  These bounds
are consequences of the exact catalogue, not assumptions in the search.

### Theorem 3.1 (finite critical-core classification)

Let `F` be triangle-free of order at most seven and let every list be a
nonempty subset of a fixed three-colour palette.  If `(F,\Lambda)` is
uncolourable, then unit propagation either reaches an empty list or its
residual instance contains one of `T1`--`T10` in the preceding sense.

Conversely, each displayed template is uncolourable and critical.

### Verification

NetworkX's graph atlas contains one representative of every unlabelled simple
graph on at most seven vertices.  The verifier retains every connected
triangle-free graph, enumerates all `4^n` assignments from (2.1), tests exact
list colourability by backtracking, applies the three criticality tests, and
then quotients by the automorphism group of the graph and all six palette
permutations.  It finds one template of order five, one of order six, and
eight of order seven, exactly as displayed.

As an independent census check, among all 107 (possibly disconnected)
triangle-free unlabelled graphs of order seven it finds:

* 34 graphs supporting a residual uncolourable assignment;
* 3,294 raw assignments on the atlas representatives;
* 239 orbits under graph automorphisms and palette permutations; and
* no uncolourable residual assignment with three full lists.

The executable output is pinned by assertions in the verifier.

## 4. Uniform consequence for the `HC_7` state

### Corollary 4.1 (five pair-limited vertices)

Let `F` be triangle-free of order seven and suppose every list has size at
least two.  If at least three vertices have the full list `123`, then `F` is
list-colourable.  Equivalently, every uncolourable residual state has at
least five vertices whose lists are two-element sets.

**Proof.**  The direct exhaustive census proves the first assertion.  It also
follows from the critical-core table.  Vertices deleted when extracting the
core may themselves have full lists.  However, `T1` has order five and no full
list (so it permits at most two deleted full-list vertices), `T2` has order six
and no full list (so it permits at most one), and every order-seven template
has at most two full lists.  Thus an order-seven instance containing any
critical core has at most two full-list vertices. `square`

### Corollary 4.2 (raw-state dichotomy)

For an arbitrary nonempty-list assignment on a triangle-free graph of order
seven, uncolourability implies one of the following:

1. singleton propagation reaches an empty list; or
2. the propagated residual contains at least five literal vertices whose
   residual lists are exact two-element sets.

**Proof.**  In the second case Theorem 3.1 supplies one of `T1`--`T10` after
only vertex/edge deletion and list enlargement.  Every template has at least
five pair-list vertices.  Since the propagated lists already have size at
least two and are contained in the template lists, a vertex displayed with a
pair list had that same exact pair before enlargement. `square`

More generally, Theorem 3.1 says that every nonconflicting uncolourable raw
state leaves, after singleton propagation, a core with at least five exact
two-element lists.  In carrier language, a legal spanning three-carrier
exchange therefore has only two ways to survive: singleton contacts propagate
to an explicit colour conflict, or at least five surviving literal boundary
vertices acquire exact two-colour restrictions in the propagated state.  The
third colour of such a propagated list may have been removed by a forced
neighbour even when the raw contact list was `123`; consequently this does
**not** justify the stronger claim that three full raw contact lists alone
close the state.

## 5. Uniform implication-bicycle certificate

The pair-list part of the catalogue has a formulation that is not specific to
seven vertices.  Suppose every list is a pair.  Regard the two choices at a
vertex `x` as complementary Boolean literals.  For every edge `xy` and every
colour `c` common to the two endpoint lists, properness gives the clause

\[
                 \neg(x=c)\ \vee\ \neg(y=c).             \tag{5.1}
\]

Equivalently, add the two implication arcs

\[
 (x=c)\longrightarrow(y\ne c),\qquad
 (y=c)\longrightarrow(x\ne c).                           \tag{5.2}
\]

Because each endpoint has exactly two choices, the right-hand sides are again
literal choices.  This is an exact two-SAT encoding: satisfying assignments
are precisely proper list-colourings.

### Lemma 5.1 (implication bicycle)

A pair-list instance is uncolourable if and only if its implication digraph
contains a literal `a` and directed paths

\[
                       a\leadsto\bar a,
             \qquad \bar a\leadsto a.                    \tag{5.3}
\]

**Proof.**  This is the standard strongly-connected-component criterion for
two-SAT.  Formula (5.1) gives the exact CNF encoding, so it applies without
loss. `square`

Thus the pair-only templates `T1`--`T6` are not six unrelated cases: they are
the order-at-most-seven triangle-free realizations of a minimal contradictory
pair of implication paths.  The two paths project to a small boundary
“bicycle”, exactly the sort of crossed-order object expected from the live
block-terminal web.

The full-list templates also reduce to this mechanism.  By the catalogue
there are at most two full-list vertices in a residual obstruction.  Branch
on their at most nine colour assignments and propagate forced colours.  Every
branch must end in an immediate conflict or an implication bicycle; otherwise
that branch supplies a list-colouring.  Templates `T7`--`T10` are precisely
the critical ways, on at most seven vertices, in which these branch
certificates coexist.

This supplies a general constructive target for the shore exchange: it is
enough to break one direction of every surviving implication bicycle (or open
one branch at a full-list vertex), rather than to reason about all 239 raw
states independently.

## 6. Falsified shortcuts

The catalogue rules out several tempting but false simplifications.

1. **Unit propagation is not complete.**  All ten residual cores have no
   singleton list.
2. **Odd uniform two-list cycles are not the only obstruction.**  `T2` is the
   bipartite theta graph with three `0`--`3` paths of lengths `1,3,3`.  If
   `(0,3)` receives `(1,2)`, the path `0-1-2-3` forces a conflict; if it
   receives `(2,1)`, the path `0-5-4-3` forces a conflict.  Thus it is
   uncolourable although it has no odd cycle.
3. **Every critical list need not have size two.**  `T7`--`T10` contain one
   or two essential full lists.
4. **A single concentrated portal is not the whole residue.**  There are 239
   residual symmetry types, but all collapse to ten critical cores.  Any next
   exchange theorem should target the five simultaneous pair restrictions,
   not individual raw assignments.

## 7. Exact scope

This classification does not by itself close the thin-shore cell.  It changes
the constructive target from “make the boundary state colourable” to the much
sharper alternative:

> find one legal arm/block exchange whose singleton propagation avoids a
> conflict and leaves three full lists, or show that the shore has a coherent
> block-terminal order capable of preserving a forced-colour conflict or five
> propagated pair restrictions under every exchange.

The second outcome is the appropriate candidate for the promised web or
fixed-two-apex certificate.
