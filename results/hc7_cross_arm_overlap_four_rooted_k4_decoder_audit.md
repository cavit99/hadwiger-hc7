# Audit of the overlap-four rooted-`K_4` decoder

## Verdict

**GREEN.**  The six-support complement equivalence, the eleven-relation
join, completion of the remaining original-edge variables, separation of
original and virtual edge layers, both direct residue constructions, and
the lift through an exterior rooted `K_4` are correct.  The checker was run
independently and returned the five rows and counts stated in the theorem.

The result may be used only under its stated hypothesis that `G-I` already
contains a `K_4` model rooted at four of the five terminals.  It is a
labelled composition theorem; it does not extract that rooted model from
three-connectivity.

## 1. Exact six-support relation

On a six-vertex support, a spanning `K_5` model has exactly one two-vertex
bag `{x,y}` and four singleton bags.  Hence `xy` is an original edge, the
four singleton vertices form a clique, and each singleton is adjacent to
at least one of `x,y`.  In the complement, the possible edges are therefore
two stars centred at `x` and `y`, their leaf sets are disjoint, and neither
centre is a leaf of the other star.

The support contains a literal `K_5` after deleting one vertex exactly when
all complement edges meet that vertex.  For the displayed two-star
relation this is equivalent to one of the stars being empty.  Thus the
irredundant supports are exactly the complements consisting of two
nonempty vertex-disjoint stars and isolates.  The checker does not assume
this characterization when constructing the local table: it directly
tests every one of the `2^15` labelled complements for a spanning `K_5`
model and for absence of a literal `K_5`, obtaining 375 relations.

## 2. Exhaustiveness of the eleven-support join

The support list in the checker is exactly

```text
A, X+p, X+q,
(A-i)+p, (A-i)+q for i in I.
```

For each support, `global_patterns` maps all fifteen local pair variables
to their literal global pairs and records both nonedges and edges.  The
recursive join rejects precisely assignments that put the same original
pair in both sets.  Selecting the currently smallest compatible relation
changes only traversal order; adding the selected constraint to `done`
and deduplicating identical resulting assignments cannot remove a future
solution.  The resulting 387 partial assignments are therefore exactly
the consistent join of the eleven finite relations.

For a fixed omitted terminal, `relevant_complements` includes every pair
queried by either conclusion:

* all pairs on `A union {p,q}` for the common rooted-`K_4` conclusion; and
* all pairs on the eight vertices other than the omitted terminal for the
  direct `K_7` conclusion.

It branches over every relevant pair not fixed by the join.  Projecting
away constrained pairs outside this set is harmless because neither
conclusion queries them.  A zero complement bit denotes an original edge,
so fixed edges and chosen unknown edges are both represented correctly.

The common-model search is complete.  Four nonempty branch sets of total
support at most five use either four or five vertices; the checker
enumerates every such support and every partition into four bags, then
tests connectedness, all six bag adjacencies, and contact by each of the
three named vertices.  This test is made in the original edge layer.

## 3. Original edges versus virtual edges

For each four-terminal exterior model, the six bits of its terminal clique
are cleared from the complement only after the original-edge join and the
common rooted-`K_4` test.  Consequently, a virtual adjacency cannot satisfy
one of the eleven irredundancy constraints or a named root contact in
outcome 1.

On the eight surviving labels, every `K_7` model either uses seven
vertices as singleton bags or all eight vertices with one edge bag and six
singleton bags.  `k7_avoiding` enumerates exactly these two possibilities,
so its final-model test is complete.  The stronger residue check then
shows that every non-common completion has one of the explicit forms

```text
{ab,cd}
{ab,cd,s6},
```

where `{ab,cd}` is a perfect matching of `I`; the second form can occur
only when terminal `6` survives.  The reproduced counts are:

| omitted terminal | completions | common | direct | direct projections |
|---:|---:|---:|---:|---:|
| `q` | 2520 | 1440 | 1080 | 15 |
| `p` | 2520 | 1440 | 1080 | 15 |
| `6` | 126 | 72 | 54 | 3 |
| `5` | 1548 | 1008 | 540 | 15 |
| `4` | 1548 | 1008 | 540 | 15 |

## 4. Explicit direct branch sets

There are two residue rows.

* If the complement is the matching `{ab,cd}`, choose one endpoint of
  each matching edge, say `a,c`, for the two-vertex bag.  The edge `ac` is
  original, every complement edge meets this bag, and the other six
  vertices are pairwise adjacent singleton bags.
* If the complement is `{ss',cd,s6}`, use `{s,c}` as the two-vertex bag,
  where `c` is either endpoint of the other matching edge `cd`.  Both
  vertices lie in `I`, so `sc` is an original edge rather than a virtual
  one.  All three complement edges meet the bag, leaving six pairwise
  adjacent singleton bags; the bag contacts terminal `6` through `c` and
  every other singleton through at least one of its two vertices.

Thus the parameterized residue table supplies a literal seven-bag model
after interpreting only terminal-terminal virtual edges through the
exterior rooted model.

## 5. Lift through the exterior rooted model

Let `B_c` be the four exterior bags rooted at `T-{t}`.  They lie in
`G-I`, are pairwise disjoint, connected, and pairwise adjacent.  In the
explicit local direct model the unique two-vertex bag lies wholly in `I`,
and each surviving terminal is a singleton.  Replacing that singleton by
`B_c` preserves:

* local-to-terminal adjacencies, because the literal root `c` belongs to
  `B_c`;
* terminal-to-terminal adjacencies, because the exterior bags are
  pairwise adjacent; and
* disjointness from every local bag, because the exterior model lies in
  `G-I`.

The local model omits `t`.  Therefore it remains disjoint even when `t`
is an internal vertex of one of the rooted bags `B_c`; no unproved
avoidance of the fifth terminal is being used.

In the common outcome, the cited three-rooted small-`K_4` composition
theorem applies exactly when `G` is seven-connected: its four bags have
support at most five and each is contacted by `i,p,q`.  That dependency
has its own GREEN audit.

## 6. Reproduction and trust boundary

Running

```text
python3 active/hc7_cross_arm_overlap_four_decoder_verify.py
```

completed without an assertion failure and reproduced all counts above.
The computation uses only the Python standard library.

This audit certifies the finite implication encoded by the eleven exact
support relations.  It does not certify that every overlap-four exterior
contains one of the five rooted `K_4` models, and it does not turn
three-connectivity alone into such a model.  The remaining rooted-model or
web/gate extraction step is outside this theorem's scope.
