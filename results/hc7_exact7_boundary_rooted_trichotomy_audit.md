# Independent audit: exact-seven boundary rooted-model trichotomy

## Verdict

**GREEN.**  The finite theorem, Z3 encoding, complete 107-graph census,
`60/84/6` obstruction counts, adjacent two-vertex-cover conclusion,
anchored-model lift, and one-block proper-minor splice are all correct.
The result is a genuine seven-boundary trichotomy and closes every exact
`(1,3)` spanning three-carrier state whose three literal supports have order
at least four.

I reran the full catalogue from scratch with

```text
PYTHONPATH=active/runtime/deps python3 \
  active/hc7_exact7_raw_list_no_k4_search.py --start 0 --end 107
```

The run completed successfully and printed

```text
triangle_free_graphs=107
graphs_with_obstructions=3
raw_assignments=150
catalogue=.../active/hc7_exact7_raw_list_no_k4_catalogue_0_107.json
```

Its nonzero per-graph outputs were exactly

```text
atlas index 1: 60
atlas index 2: 84
atlas index 5:  6
```

The regenerated catalogue is byte-for-byte identical to the authoritative
merged catalogue:

```text
SHA-256 70da064919e2664909ac1f5f52a1ffdfa34326532a4ad17b27cbd624511c0f3b
```

As a separate guardrail, I used an independent brute-force list-colouring
and anchored-model checker on all 150 stored assignments.  It reproduced

```text
INDEPENDENT_VERIFIED 107 150
F???G:60, FH???:84, F??KG:6
```

and verified nonemptiness, all three support bounds, uncolourability, absence
of an anchored `K_4`, and existence of an adjacent two-vertex cover for every
record.

The computational proof trusts the standard completeness of NetworkX's
graph atlas through order seven and the soundness of Z3's finite Boolean and
pseudo-Boolean solver.  The encoding itself is exact, as audited below.

## 1. Atlas coverage

`atlas_graphs()` selects every graph in `nx.graph_atlas_g()` with exactly
seven vertices and no triangle.  `nx.graph_atlas_g()` contains one
representative of every unlabelled simple graph on at most seven vertices.
The filter returns 107 graphs, matching the independently audited census in
the triangle-free critical-core theorem.  It includes disconnected graphs;
no connectedness restriction is silently imposed.

Every labelled pair `(F,Lambda)` is represented.  Transport `Lambda` through
an isomorphism from `F` to its atlas representative.  The solver enumerates
all 21 incidence Booleans on that representative, so it necessarily visits
the transported assignment.  The theorem's conclusions are invariant under
transport back through the isomorphism.

## 2. Nonempty lists and support constraints

For each boundary vertex `s`, the constraint

```python
solver.add(z3.Or(*contacts[s]))
```

is exactly `Lambda(s) ne emptyset`.  No upper bound on list order is imposed;
singletons, pairs, and full lists are all included.

For each palette colour `q`,

```python
z3.PbGe([(contacts[s][q], 1) for s in range(7)], 4)
```

is exactly the support lower bound

\[
                     |\{s:q\in\Lambda(s)\}|\ge4.
\]

Thus the solver's raw domain matches Theorem 1.1 exactly.

## 3. Exact negation of list-colourability

The loop visits all `3^7` ordinary colour assignments `phi`.  It retains
precisely those satisfying

\[
                         \phi(u)\ne\phi(v)
             \qquad(uv\in E(F)),
\]

so it visits every proper ordinary three-colouring of `F` and no improper
one.  For each retained `phi`, the clause

\[
                     \bigvee_{s\in S}\neg x_{s,\phi(s)}
\]

says exactly that at least one assigned colour is absent from its vertex's
list.  Conjoining these clauses over all proper `phi` says that no proper
ordinary colouring selects only allowed list colours.  This is precisely
that `(F,Lambda)` is not list-colourable.

Disconnected and edgeless graphs cause no special case: their proper
colourings are included by the same loop.

## 4. Exact negation of an anchored `K_4`

An anchored model, by definition, uses exactly four boundary vertices, one
in each bag.  Since the auxiliary graph has only three other vertices—the
carrier triangle—each bag is exactly its root together with a subset of the
carrier vertices.  A carrier vertex belongs to one bag or is unused.

The encoding enumerates

* all `binom(7,4)` choices of four roots; and
* all `5^3` assignments of the three carrier vertices to one of the four
  bags or to the unused value.

This is exhaustive; an anchored bag cannot contain an additional boundary
vertex under the theorem's definition.

For a carrier-bearing bag, its assigned carriers induce a clique.  The bag
is connected exactly when its root sees at least one assigned carrier, which
is the encoded disjunction

```python
Or(contacts[root][q] for q in carriers)
```

A singleton-root bag is connected automatically.

For two bags:

* if both contain a carrier, they are adjacent automatically through the
  carrier triangle; the carrier sets are disjoint and nonempty, so the two
  witnessing carrier vertices are distinct;
* otherwise, adjacency exists exactly when the two roots have a boundary
  edge, the root of the carrier-free bag sees a carrier in the other bag, or
  symmetrically the other root sees a carrier in its opposite bag.

These are exactly the alternatives accumulated by the code.  If there is no
possible alternative, that carrier assignment can never be a model and
needs no constraint.  Otherwise the conjunction of connectivity and all six
pair-adjacency requirements is true exactly when that assignment is an
anchored `K_4`.  Its negation therefore forbids that exact model.

Conjoining over all roots and carrier assignments is precisely the negation
of outcome 2.  No more general branch set is omitted, because the definition
forbids extra boundary vertices and the only nonboundary auxiliary vertices
are the three individually enumerated carriers.

## 5. Complete model enumeration

After adding the three groups of constraints, every satisfying assignment is
one raw list state with

1. nonempty lists and support at least four per colour;
2. no list-colouring; and
3. no anchored `K_4`.

All 21 contact variables occur in the constraints.  `model.eval()` therefore
returns a Boolean value for each.  The blocking clause is the disjunction of
inequalities against all 21 values, so it excludes exactly the current
assignment and no other.  Repeating until `unsat` enumerates every satisfying
assignment.

The parent process invokes one fresh child Python/Z3 process for each atlas
graph, parses its complete JSON output, and aggregates every nonempty record.
No solver state leaks between graphs.  The independently regenerated
catalogue contains three records and 150 assignments, exactly as claimed.

The diagnostic fields also reproduce:

* every assignment has exactly two raw singleton lists;
* no assignment has a full list; and
* every assignment reaches a unit-propagation conflict.

These facts are consistent with the promoted forced-path theorem but are not
used to prove the trichotomy.

## 6. Identification of the three boundary graphs

The three catalogue records are:

| atlas index | graph6 | literal edges | count | graph type |
|---:|---|---|---:|---|
| 1 | `F???G` | `56` | 60 | `K_2 dotunion 5K_1` |
| 2 | `FH???` | `12,23` | 84 | `P_3 dotunion 4K_1` |
| 5 | `F??KG` | `06,45,56` | 6 | `P_4 dotunion 3K_1` |

For the last row the path order is `4-5-6-0`.  These identifications use
the literal edge lists emitted by the catalogue, not graph6 names alone.

The counts sum to

\[
                            60+84+6=150.
\]

All other 104 triangle-free atlas graphs returned `unsat` and hence have no
assignment simultaneously negating outcomes 1 and 2.

## 7. Adjacent two-vertex covers

Each of the three surviving graph types has an edge whose endpoints meet
every edge.

* For `K_2 dotunion 5K_1`, take its unique edge.
* For `P_3 dotunion 4K_1`, take either edge incident with the middle vertex.
* For `P_4 dotunion 3K_1`, take the middle path edge, which is `56` in the
  catalogue labelling.

If the chosen edge is `pq`, every edge of `F` meets `{p,q}`.  Therefore the
five-set

\[
                             I=S-\{p,q\}
\]

contains no edge and is independent.  Since `pq` itself is literal,
`Q_0={p,q}` is a two-vertex clique.  This proves outcome 3 for every one of
the 150 remaining assignments, independently of its contact lists.

The conclusion is invariant under relabelling, so it applies to every graph
represented by the three atlas records.

## 8. Literal lift of outcomes 1 and 2

In the exact `(1,3)` cell, outcome 1 invokes the already audited uniform
carrier-list synchronization theorem with the three spanning thin-shore
carriers and three opposite full packets.  A proper list-colouring partitions
`S` into at most three independent blocks, and literal contractions on both
sides produce the same exact equality partition; the six-colourings align by
a palette permutation.

For outcome 2, replace each auxiliary carrier vertex `c_q` by the actual
connected carrier `C_q`.  Auxiliary connectivity and adjacency lift edge by
edge through literal carrier--carrier edges and literal root contacts.  The
four lifted bags have four distinct boundary anchors.  Anchoring the three
opposite full packets at the remaining boundary vertices gives

| Bag pairs | Count | Witness |
|---|---:|---|
| among the four anchored bags | 6 | lifted auxiliary model |
| packets to anchored bags | 12 | packet fullness at their four anchors |
| among packet bags | 3 | packet fullness at the other packets' anchors |

All seven bags are disjoint and connected, and all `6+12+3=21` adjacencies
are literal.  Thus outcome 2 gives a `K_7` minor.

## 9. One-block packet-state splice

Let outcome 3 give the independent five-set `I=S-\{p,q\}` and literal edge
`pq`.  Choose a connected `S`-full packet `P_R` in the right open shore.
The set

\[
                              P_R\cup I
\]

is connected because every literal vertex of `I` has a neighbour in
`P_R`.  Contract it to a vertex `x_R`.  This is a proper minor.  Packet
fullness makes `x_R` adjacent to both untouched vertices `p,q`, and the
literal edge `pq` makes

\[
                              \{x_R,p,q\}
\]

a triangle.  A six-colouring of the proper minor therefore assigns three
distinct colours to `x_R,p,q`.

Restrict this minor colouring to the left closed shore and expand every
vertex of `I` with the colour of `x_R`.  The result properly colours the
left closed shore:

* `I` is independent;
* every original edge from `I` to the left shore became an edge from `x_R`
  in the minor; and
* edges incident with `p,q` remain proper.

Its exact boundary equality partition is

\[
                            I\mid\{p\}\mid\{q\}.
\]

Choose symmetrically a connected `S`-full packet `P_L` in the left open
shore, contract `P_L\cup I`, six-colour that proper minor, restrict to the
right closed shore, and expand `I`.  This gives the same exact three-block
partition on `S`.

The three block colours are distinct on each side because the contracted
image and `p,q` induce a triangle.  The bijection between the three colours
used on corresponding blocks extends to a permutation of the six-colour
palette.  After applying it to one side, the two colourings agree at every
literal boundary vertex.  There are no edges between the two open shores,
so they glue to a proper six-colouring of all of `G`.

Only one full packet per open shore is used.  Such packets exist in the
exact-seven cell: seven-connectivity makes every component behind the
literal seven-boundary `S` full to `S`, and both open shores are nonempty.
No planarity, model-label alignment, or unstated boundary edge is used.

## 10. Rank-two block-chain consequence and exact scope

At a cutvertex in the opposite lobe of a rank-two rooted-triangle state, the
promoted block-chain exchange either constructs a literal `K_7` from a
noncrossed gate-duty split or produces a crossed spanning partition into
three connected pairwise adjacent thin-shore carriers.  Each of those
carriers has at least four literal boundary contacts.  The boundary
trichotomy and Sections 8--9 therefore give a `K_7` or a six-colouring.
Corollary 4.1 is valid and closes the entire cutvertex branch, independently
of block-chain length.

The exact graph-theoretic conclusion is that, in a target-free rank-two
cell, the opposite lobe has **no cutvertex**.  Calling it two-connected is
standard only when its order is at least three; singleton and two-vertex
lobes require whatever separate small-lobe results the proof spine invokes.
The corollary itself states only the valid conditional implication and does
not close portal rank one or a pair of cutvertex-free lobes.
