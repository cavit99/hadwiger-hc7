# Independent audit: exact-seven triangle-free list-core classification

## Verdict

**GREEN, for the corrected statement.**  Theorem 3.1, Corollaries 4.1
and 4.2, and Lemma 5.1 are mathematically valid.  The verifier exhausts
the claimed search space, its colourability and criticality tests are exact,
its quotient is by the full product of graph automorphisms and palette
permutations, and its asserted census and ten templates reproduce.

The qualification “for the corrected statement” is important.  Three full
lists close a **residual state in which every list has size at least two**;
three full lists in the raw carrier-contact assignment do not suffice.  A
forced singleton can delete a colour from a neighbouring raw full list or
can cause an immediate conflict.  The present draft states the valid
residual result and the correct raw dichotomy:

1. unit propagation reaches an empty list; or
2. the nonconflicting propagated residual contains at least five literal
   vertices with exact two-element lists.

The formerly overbroad raw “three full contacts close” claim has been
withdrawn explicitly.

## 1. Reproduction

From the repository root I ran

```text
PYTHONPATH=active/runtime/deps python3 \
    results/hc7_exact7_triangle_list_critical_verify.py
```

The process exited successfully and printed

```text
VERIFIED
critical_templates=10
orders=5:1,6:1,7:8
order7_uncolourable_graphs=34
order7_raw_residual_assignments=3294
order7_residual_orbits=239
maximum_full_lists_in_uncolourable_residual=2
```

It also reproduced the displayed graph6 strings, edge sets, and list tuples
for `T1`--`T10`.  The assertions pin both the ordered template catalogue and
the four census values, so a discrepancy fails rather than merely changing
diagnostic output.

As a separate atlas sanity check, NetworkX supplies exactly 107
triangle-free unlabelled graphs of order seven, 59 of them connected.  The
residual census deliberately uses all 107; the critical-template search
correctly uses only connected graphs.

## 2. Exactness of unit propagation

If `L(x)={c}`, every list-colouring must assign `c` to `x`.  Deleting `x`
and removing `c` from every neighbour therefore gives a bijection between
colourings before and after that step.  An empty neighbour list is an exact
certificate of failure.  Repeating until conflict or until no singleton
remains consequently preserves colourability in both directions.

In a nonconflicting residual, every list is a subset of the three-colour
palette of size at least two, hence is one of

\[
                         12,13,23,123.
\]

This is precisely the four-element domain enumerated by the verifier.  The
argument does not depend on which currently forced singleton is processed
first: every individual reduction is equivalent, and Theorem 3.1 applies to
whatever nonconflicting residual is obtained.

## 3. Existence and meaning of a critical core

Starting with an uncolourable residual, delete vertices and edges whenever
uncolourability persists, and then enlarge individual lists whenever
uncolourability persists.  Finiteness guarantees termination.  Later edge
deletions or list enlargements cannot destroy a colouring already present
after a vertex deletion; similarly, later list enlargements cannot destroy a
colouring already present after an edge deletion.  Thus the final object is
minimal under every vertex and edge deletion and maximal, while still
uncolourable, under every one-colour list enlargement.

Such an object is connected.  If it had more than one component, one
component would already be uncolourable, and deleting a vertex from another
component would preserve uncolourability, contradicting vertex criticality.
Vertex and edge deletion preserve triangle-freeness and never increase the
order, so it is covered by the connected atlas enumeration.

The note's containment direction is also correct.  Core extraction selects
vertices, retains a subgraph, and enlarges lists.  Therefore an original
residual list is contained in its displayed core list.  Since residual lists
already have size at least two, a displayed pair list forces the original
residual list at that literal vertex to be that exact pair.

## 4. Exhaustive coverage and colourability test

`nx.graph_atlas_g()` contains one representative of every unlabelled simple
graph on at most seven vertices.  `atlas_graphs()` retains exactly the
connected, triangle-free representatives of orders one through seven.
For a graph of order `n`,

```text
product(PAIR_OR_FULL, repeat=n)
```

enumerates all `4^n` residual list assignments without pruning.

`colourable()` is an exact finite backtracking search.  Its static ordering
by list size and degree changes only search order.  At each vertex it tries
every permitted palette colour not already used by a coloured neighbour,
and it accepts only after all vertices are assigned.  Thus it has neither a
relaxation nor a heuristic rejection.

The labels of an atlas graph are `0,...,n-1`.  After a vertex is deleted,
the surviving labels can have a gap, but the unchanged list tuple is still
indexed by those original labels; `colourable()` iterates the actual graph
vertices, so this causes no indexing error.

## 5. Criticality tests

`critical()` first rejects every colourable assignment.  It then checks:

* every single vertex deletion;
* every single edge deletion; and
* for every vertex, every palette colour absent from its list, enlargement
  by that one colour.

On the residual domain a pair has exactly one possible enlargement and a
full list has none, exactly matching the definition.  The graph-copy tests
retain the correct lists on surviving literal vertices.  Therefore the code
tests all and only the three stated forms of criticality.

The ten returned representatives individually pass these same exact tests,
so the computational result proves both uncolourability and criticality of
every displayed template.  Conversely, every possible connected
triangle-free critical core on at most seven vertices is visited by the
atlas/list loops.

## 6. Isomorphism and palette quotient

For each fixed atlas graph, `GraphMatcher(graph,graph).isomorphisms_iter()`
enumerates its full automorphism group.  For every automorphism the code also
enumerates all six permutations of the three colours.  It transports every
old vertex list to its image vertex and transports every colour bit through
the palette permutation, then selects the lexicographically least resulting
tuple.

Thus `canonical_lists()` is constant on, and ranges over, the full
`Aut(F) x Sym(3)` orbit.  Atlas representatives already quotient graph
isomorphism, so no additional cross-graph identification is missing.  The
239-orbit census repeats the same canonicalization separately on each of the
107 nonisomorphic order-seven boundary graphs.

## 7. The full-list bound and its exact scope

The direct order-seven census records maximum full-list count two among all
uncolourable assignments from `{12,13,23,123}`.  Hence an order-seven
no-singleton assignment with at least three `123` lists is colourable.

The same conclusion follows from the core catalogue with the stated
containment direction:

* `T1` has order five and no full list, allowing at most two deleted full-list
  vertices in an order-seven superinstance;
* `T2` has order six and no full list, allowing at most one;
* every order-seven template has at most two full lists.

A full list in the original selected residual cannot be contained in a
displayed pair, so these counts bound the original residual assignment, not
merely the enlarged core.  Every template also has at least five displayed
pair lists; those selected residual lists must be the same exact pairs.
This proves Corollary 4.2 after nonconflicting propagation.

It does **not** bound the number of full lists before singleton propagation.
The corrected carrier-language consequence is therefore exactly the one in
the note: a surviving raw state either produces an explicit unit conflict or
leaves at least five exact pair restrictions in its propagated residual.

## 8. Implication-bicycle lemma

When every residual list is a pair, choose one Boolean variable per vertex,
whose two literals represent its two allowed colours.  For every edge `xy`
and every colour `c` common to the endpoint lists, properness forbids the
single simultaneous assignment `x=c,y=c`, giving

\[
                  \neg(x=c)\vee\neg(y=c).
\]

These clauses are exact: they forbid precisely all monochromatic edge
assignments and impose nothing else.  The two standard implication arcs for
each clause therefore yield a two-SAT formula whose satisfying assignments
are exactly the proper list-colourings.  The standard SCC criterion says it
is unsatisfiable exactly when some literal and its complement are mutually
reachable.  This proves Lemma 5.1.

If a residual core has one or two full-list vertices, branching on their at
most `3^2=9` assignments and propagating leaves either an immediate conflict
or a pair-list instance.  An uncolourable original residual requires every
branch to fail, so every nonconflicting branch has an implication bicycle.
The interpretive connection to `T7`--`T10` is consequently sound.

## 9. Scope

The classification is a finite boundary theorem and a useful invariant for
the live exchange argument.  It does not prove that a legal carrier exchange
with a colourable state exists, nor does it close the thin-shore cell.  The
note states those limitations accurately.
