# Independent audit: degree-nine pole local completion

**Verdict:** **GREEN** for the finite local completion claim stated in
`results/hc7_degree9_pole_verifier.md`.

**Claim status:** computer-assisted finite result.  This audit does not, by
itself, promote the surrounding degree-nine reduction to a theorem.

## Exact revision audited

```text
c25413c92817f52167196848276b70626d7541073d1319c1b66e281ba095480e  audited Markdown content
9a59ff768994b7aef86b9c54b5c1b4c613629d45a307dc1ba6300d1c4c7ec342  results/hc7_degree9_pole_verifier.py
```

Promotion changed only the status line and the documented invocation path
after moving the verifier from `active/` to `results/`.  Its promoted
content hash is

```text
dd8817ceec58b083e12adae943f49cf2bb5a401f17ca87950477906f811c5a08  results/hc7_degree9_pole_verifier.md
```

Any mathematical or computational change to either source invalidates this
audit until the hashes and the checks below are renewed.

## Statement checked

Let `H` be a nine-vertex graph with minimum degree at least five, and add a
vertex `c`.  In each of

```text
e(H)=23, d_H(c)=7;
e(H)=23, d_H(c)=8;
e(H)=24, d_H(c)=7,
```

the graph `H+c` has a `K_6`-minor model all of whose six branch sets meet
`H`.  More precisely, the branch sets may be chosen from a partition of
`V(H)` into three edges and three singletons, with `c` adjoined to one of
those six sets.

## Mathematical reduction audit

The three finite regimes are exactly the exceptional regimes in the stated
degree-nine setup.

Let `u` have degree nine and put `H=G[N(u)]`.  If every incident edge `uv`
is double-critical in a seven-chromatic graph, a five-colouring of
`G-{u,v}` shows that `u` and `v` have a common neighbour in each of the five
colour classes.  Hence every vertex of `H` has at least five neighbours in
`H`, and therefore

```text
e(H) >= ceil(9*5/2) = 23.
```

For completeness, the common-neighbour step is elementary.  If one colour
class `A` contained no common neighbour, recolour the vertices
`A intersect N(u)` with one new colour, give `u` the old colour of `A`, and
give `v` the new colour.  The recoloured vertices are independent and none
is adjacent to `v`, so this would be a six-colouring of `G`, a
contradiction.  Distinct colour classes supply distinct common neighbours.

For a component `C` of `G-N[u]`, seven-connectivity gives
`|N_G(C)|>=7`.  Contracting `C` to `c` and deleting the other exterior
vertices gives an eleven-vertex minor with exactly

```text
9 + e(H) + d_H(c)
```

edges: the first term is contributed by `u`, and `uc` is not an edge.
Mader's exact `K_7` extremal bound is `5*11-15=40`.  Thus a
`K_7`-minor-free graph can remain only when

```text
(e(H),d_H(c)) in {(23,7),(23,8),(24,7)}.
```

For these pairs, the complement `F` of `H` has respectively 13, 13, or 12
edges and maximum degree at most three, while `c` has respectively two,
one, or two non-neighbours in `H`.  This is exactly the finite input used by
the verifier.

Finally, a verified `K_6` model in `H+c` lifts through the contraction of
`C`.  Every branch set meets `H`, so the singleton `{u}` is adjacent to all
six lifted branch sets and completes an explicit `K_7`-minor model.

The standard common-neighbour lemma, seven-connectivity, Mader's extremal
bound, and the existence of a component of `G-N[u]` are mathematical inputs,
not consequences of the finite search.  In the hypothetical-counterexample
application, nonexistence of such a component would make `u` universal; the
known `HC_6` result then gives a `K_6` minor in `G-u`, again completed by
`u`.

## Line-by-line verifier audit

### Catalogue generation and decoding

The call to `geng` requests all unlabelled simple graphs of order nine with
the specified edge count and maximum degree three.  The returned catalogue
sizes are checked to be

```text
20  for 13 edges;
103 for 12 edges.
```

The short graph6 decoder uses the correct order

```text
(0,1),(0,2),(1,2),(0,3),(1,3),(2,3),...
```

and was cross-checked on a generated representative against nauty's
`showg -e` edge listing.  The script independently checks every decoded
edge count and maximum degree before using the graph.

Passing to the complement is correct: a maximum degree-three graph on nine
vertices becomes a minimum degree-five graph.

### Candidate construction

There are

```text
C(9,6) * 5!! = 84 * 15 = 1260
```

partitions of the nine vertices into three unordered pairs and three
singletons.  The generator produces exactly 1,260 distinct partitions.  It
keeps only those for which all three pairs are edges of `H`, and it tries
adjoining `c` to every block containing a neighbour of `c`.

### Certificate checking

The final checker does not trust the construction.  For each proposed
model it checks from the augmented adjacency relation that:

* there are exactly six branch sets;
* every branch set contains a vertex of `H`;
* the branch sets are nonempty, disjoint, and together contain all ten
  vertices;
* each branch set is connected; and
* every pair of branch sets is adjacent.

These conditions are sufficient for the claimed `K_6` minor and for the
subsequent addition of `{u}`.

### Coverage of attachments

For every unlabelled complement representative the script tries every
subset of one or two non-neighbours of `c`.  Although this retains
automorphic duplicates, it omits no rooted isomorphism type: any labelled
pair `(F,N_H(c))` maps to one catalogue representative and to one of the
enumerated subsets.

The rooted counts are therefore

```text
20 * C(9,2) = 720;
20 * C(9,1) = 180;
103 * C(9,2) = 3708;
total = 4608.
```

## Independent reimplementation

The audit used a separate standard-library implementation written without
consulting the repository verifier.  It decoded graph6 independently,
enumerated triples of pairwise vertex-disjoint edges of `H` directly rather
than generating set partitions, and then checked connectivity and all
fifteen branch-set adjacencies using ordinary vertex sets.  It returned:

```text
F_edges=13, c_nonneighbours=2: representatives=20, instances=720, bad=0
F_edges=13, c_nonneighbours=1: representatives=20, instances=180, bad=0
F_edges=12, c_nonneighbours=2: representatives=103, instances=3708, bad=0
```

A second pass required `c` to occur in one of the six branch sets rather
than allowing it to be omitted.  It again returned zero failures in all
three regimes.  Thus the independently checked certificates establish the
stronger formulation in the source note.

Running the repository verifier itself with nauty produced exactly the
documented output, including

```text
total_instances=4608 bad=0
catalogue_sha256=489ef6397133a86bddaabb3c0a27b78b36e172d041ec5aab05e9c89ed9e175eb
witness_sha256=168b7a1b4c863029ee4ee14b1b53d8843b9b79d4b0c2205d093636a13a1abdb1
PASS degree-nine local completion
```

## Trust boundary and caveats

1. Exhaustiveness of the unlabelled catalogue relies on the standard nauty
   program `geng`.  The script checks the returned objects and the expected
   catalogue sizes, but it is not an independent proof of nauty itself.
2. The finite claim does not prove that the hypotheses arise in every
   hypothetical counterexample.  The reduction through a low-degree pole,
   the double-critical common-neighbour lemma, and the use of Mader's bound
   require a separate written proof and audit.
3. The 4,608 count is a deliberately redundant rooted census over
   unlabelled complements; it is not asserted to be the number of
   isomorphism classes of augmented graphs.
4. No finite order bound is being substituted for an unbounded statement:
   the order-nine input is exactly the neighbourhood of the assumed
   degree-nine vertex, and the contracted exterior component is one
   additional vertex.

Subject to these explicit inputs, the finite local completion claim is
**GREEN**.
