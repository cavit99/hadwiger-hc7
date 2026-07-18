# Independent audit: low-degree adjacent-pair alignment

**Verdict:** GREEN.

This verdict is conditional on the separately audited computer-assisted
degree-nine local completion lemma, the promoted
computer-assisted order-eight/nine boundary-absorption theorem, and the stated
external inputs.  The theorem does not prove `HC_7`.

## Exact revision audited

```text
61e5826d13d554ca6cc3b436e883b8e29b55729835e988ecd6005d649187641e  audited theorem content
```

Promotion changed only the status paragraph.  The promoted source hash is

```text
263611a40dc7829788967250e031a3f3170e1c7a6c8c9a3fbfbb358231b1f9ca  results/hc7_low_degree_adjacent_pair_alignment.md
```

The degree-nine dependency was checked at the revisions already pinned by its
independent audit:

```text
c25413c92817f52167196848276b70626d7541073d1319c1b66e281ba095480e  audited degree-nine Markdown content
b4bab9be44feb5dc749dc8ba3f41a85094896d4b3de8a7d8246342b2729c9c59  results/hc7_degree9_pole_verifier.py
```

The promoted hash of the degree-nine Markdown source, after its status and
documented invocation path were updated, is
`dd8817ceec58b083e12adae943f49cf2bb5a401f17ca87950477906f811c5a08`.

The conditional palette theorem invoked in Section 4 is the promoted source

```text
2b0c30b9d8566f6da4959df145bf0f527249bf887dfa844d19a98e524080a9f2  results/hc7_adjacent_pair_palette_linkage.md
```

and has its own GREEN audit.  Any mathematical change to the source theorem or
either finite-verifier source invalidates this audit until the affected checks
are renewed.

The four-colour boundary conclusion also uses the separately GREEN-audited
exact-seven classification, pentagonal cycle completion, and two-full-shore
boundary absorption theorems.  Their current promoted source revisions are:

```text
cd4b7fcf03242e41434522ac2eedd83425c418b83917d2ba1e94dd6740b3a568  results/hc7_exact7_no_rigid_trace.md
c627b4bc8222a674a13c7e4dc6e7d33f876becb163b24617764afedc7ee8c0da  results/hc7_pentagonal_separation_completion.md
f87ddcf7e4bd33b0fc107033033d9a8ebb2f6e32533b1b9c4538c0bf4bd137db  results/hc7_cycle_boundary_completion.md
f66559a43b49cdf77963f3dd64066f71da9defd69a111107e030e5a626602d8d  results/hc7_two_full_shore_boundary_absorption.md
```

## Statement checked

Under the stated hypothetical-counterexample hypotheses and `HC_6`, the
source proves that one can choose an edge `uz` with

```text
7 <= d_G(u) <= 9,
chi(G-{u,z}) = 6.
```

For every component `C` of `G-N[u]`, its full neighbourhood `S=N_G(C)` has
order seven, eight, or nine and defines an actual full separation.  Every
nonempty independent set of `G[S]` occurs as an exact colour block in a
six-colouring of either closed shore.  The graph

```text
overline(K_2) vee G[S]
```

is a minor of `G`, and `G[S]` is always four-colourable.  The boundary also
satisfies

```text
alpha(G[S]) <= alpha(G[N(u)]) <= d_G(u)-5 <= 4.
```

Finally, the conditional adjacent-pair colouring and five-path conclusions
apply at this same low-degree pole `u`.

All of these conclusions are established.  In particular, the strengthened
independent-set trace statement is not merely a singleton-boundary statement.

## 1. Low degree and nonuniversality

Mader's exact extremal theorem says that a simple `K_7`-minor-free graph on
`n>=7` vertices has at most `5n-15` edges.  Hence the average degree of `G` is

```text
2|E(G)|/|V(G)| <= 10-30/|V(G)| < 10.
```

Seven-connectivity gives minimum degree at least seven, so an integer-degree
vertex `u` satisfies `7<=d_G(u)<=9`.

The nonuniversality argument is correct.  Proper-minor minimality gives a
six-colouring of `G-u`.  If `G-u` were five-colourable, assigning a fresh
sixth colour to `u` would contradict `chi(G)=7`.  Therefore `chi(G-u)=6`, and
`HC_6` supplies a `K_6` minor in `G-u`.  A universal singleton `{u}` would be
adjacent to all six branch sets, producing a `K_7` minor.  Thus `u` is not
universal and `G-N[u]` has a component.

The proof uses only the stated hypotheses here.  In particular, it does not
assume in advance that the low-degree vertex lies on a non-double-critical
edge.

### The neighbourhood independence bound

Let `I` be a maximum independent set in `G[N(u)]`.  Contracting the connected
star `{u} union I` gives a proper minor.  In a six-colouring of that minor,
the contracted vertex is adjacent to every vertex of `N(u)-I`, so its colour
is absent from `N(u)-I`.  Expanding `I` with that colour therefore gives a
proper six-colouring of `G-u` in which `N(u)` uses at most

```text
1 + |N(u)-I|
```

colours.  If `|N(u)-I|<=4`, at least one of the six colours is absent from
`N(u)` and can be assigned to `u`, contradicting `chi(G)=7`.  Hence

```text
d_G(u)-alpha(G[N(u)]) = |N(u)-I| >= 5.
```

The inclusion `S subseteq N(u)` gives the first independence-number
inequality, and `d_G(u)<=9` gives `d_G(u)-5<=4`.  Thus the full chain in
(1.6) is correct.

## 2. The bounded full separation

Let `C` be a component of `G-N[u]` and `S=N_G(C)`.

Every neighbour of `C` outside `C` lies in `N(u)`.  Otherwise that neighbour
would itself lie in `G-N[u]` and would join `C` to a second vertex or component
of that induced graph.  Thus `S` is a subset of `N(u)`.  Also `u` belongs to
neither `C` nor `S`.

It follows directly that

```text
(G[C union S], G-C)
```

is a separation: the two induced subgraphs cover `G`, intersect exactly in
`S`, and no edge joins `C` to the opposite open side.  Both open sides are
nonempty, because one contains `C` and the other contains `u`.  Consequently
`S` is a vertex cut, so seven-connectivity gives `|S|>=7`; the inclusion in
`N(u)` gives `|S|<=d_G(u)<=9`.

Fullness is literal.  Every member of `S=N_G(C)` has a neighbour in `C`, and
`u` in the other open side is adjacent to every member of `S`.

### Exact independent-block trace on the `C` shore

Fix a nonempty independent set `I` of `G[S]`.  The set `{u} union I` induces
a connected star because `S` is contained in `N(u)`.  Contracting it produces
a proper minor, hence a six-colourable graph.  Its contracted vertex `w` is
adjacent to every member of `S-I`, through `u`.

Expand `w` on the closed shore `G[C union S]` by giving every vertex of `I`
the colour of `w`.  This is proper for two independent reasons:

1. there is no edge inside `I`; and
2. every original edge from a vertex of `I` to a vertex retained on the shore
   induces an edge from `w` after contraction.

Since `w` is adjacent to every vertex of `S-I`, no such vertex receives its
colour.  Thus `I` is exactly one boundary colour block.

### Exact independent-block trace on the opposite shore

The set `C union I` is connected: `C` is connected and every member of `I`,
being in `S`, has a neighbour in `C`.  Contract it to `w`.  Every vertex of
`S-I` also has a neighbour in `C`, so it is adjacent to `w` in the minor.

Expanding `w` to the independent set `I` in `G-C` is proper by the same edge
check, and again the colour is absent from `S-I`.  This proves the asserted
exact trace on the second closed shore.

The source correctly warns that these two colourings need not induce the same
partition on `S-I`.  Exact attainability of each chosen independent block is
not a common shore colouring and does not by itself permit gluing.

### The joined boundary minor

Contracting `C` to a vertex `c` makes `c` adjacent to every vertex of `S`.
The vertex `u` is also adjacent to every vertex of `S`, while `uc` is absent
because `C` is contained in `G-N[u]`.  Deleting all other vertices therefore
leaves exactly

```text
overline(K_2) vee G[S].
```

As a minor of the `K_7`-minor-free graph `G`, this graph is also
`K_7`-minor-free.

## 3. Four-colourability of every returned boundary

The three possible boundary orders are handled correctly.

### Order seven

The exact-seven theorem applies to the separation with open shores `C` and
`V(G)-(C union S)`.  Seven-connectivity makes every component on either shore
full to `S`.  Its classification gives `chi(G[S])<=5`, with equality only for

```text
G[S] = K_2 vee C_5.
```

Under the present contraction-critical hypotheses the same theorem says that
this equality case has exactly two connected full open shores.  Its universal
edge and induced 5-cycle therefore satisfy the pentagonal cycle-completion
theorem.  The needed `K_5` minor after deleting the universal edge is automatic
from `chi(G)=7` and `HC_5`.  A five-chromatic boundary would consequently give
a `K_7` minor, so the order-seven boundary is four-colourable.

### Orders eight and nine

The set `C` is a component of `G-S`.  The component `B` of `G-S` containing
`u` is distinct from `C`, connected, and full to `S`, because `u` is adjacent
to every boundary vertex.  The promoted two-full-shore boundary-absorption
theorem thus applies without requiring that `C,B` be the only components.

It makes every order-eight boundary four-colourable.  At order nine it leaves
only the possible exception

```text
G[S] = K_2 vee C_7.
```

Write the universal edge as `pq` and label the cycle `0,1,...,6` cyclically.
If `C` and `B` are the only components of `G-S`, the general cycle-boundary
completion theorem applies.  Its `K_5`-minor hypothesis follows because
deleting `p,q` lowers chromatic number by at most two, so `G-{p,q}` is not
four-colourable and `HC_5` gives a `K_5` minor.

If there is a third component `D`, seven-connectivity gives
`|N_G(D)|>=7`, so `D` misses at most two of the nine boundary vertices.  Up
to swapping `p,q` and a dihedral symmetry of the cycle, the source's list

```text
empty, {p}, {0}, {p,q}, {p,0}, {0,1}, {0,2}, {0,3}
```

is the complete list of possible missed sets.  In all eight cases `D` has
neighbours at cycle vertices `4` and `6`.

The seven displayed branch sets

```text
{p,0,1}, {q}, C union {2}, B union {3}, D union {4}, {5}, {6}
```

were checked pair by pair.  They are disjoint and connected.  The two first
sets meet every other set through the universal boundary vertices.  Among the
last five sets, fullness of `C` supplies its adjacencies to the bags containing
`3,4,5,6`; fullness of `B` supplies its adjacencies to those containing
`4,5,6`; the `D-4` contact connects `D union {4}`, the `D-6` contact supplies
its adjacency to `{6}`, and the cycle edges `2-3`, `4-5`, and `5-6` supply the
remaining adjacencies.  Hence these are an explicit `K_7`-minor model.

This eliminates the unique order-nine exception and proves
`chi(G[S])<=4` for every boundary order seven, eight, or nine.

## 4. The common-neighbour consequence

For the chosen low-degree `u`, the only possible values of
`chi(G-{u,x})`, for `x in N(u)`, are five and six.  The lower bound five
follows from

```text
chi(G) <= chi(G-{u,x})+2,
```

and the upper bound six follows by restricting a six-colouring of the proper
minor `G-u`.

Assume all these chromatic numbers are five.  In a fixed five-colouring of
`G-{u,x}`, every colour occurs on a common neighbour of `u` and `x`.  If one
colour did not, recolour all vertices of that colour in `N(u)` with a fresh
sixth colour, colour `u` with the vacated colour, and colour `x` with the new
colour.  The recoloured vertices are independent, and none is adjacent to
`x` by the assumed absence of a common neighbour.  This would be a proper
six-colouring of `G`, a contradiction.

The five colour classes give five distinct common neighbours.  Since the
argument applies to every `x in N(u)`, the graph `H=G[N(u)]` has minimum
degree at least five.

This is the only double-critical common-neighbour fact used later, and the
source proves it rather than relying solely on the cited literature.

## 5. The contracted exterior quotient and density count

Contract a component `C` of `G-N[u]` to `c`, delete all other exterior
vertices, and suppress loops and parallel edges.  The resulting simple minor
`M` has vertex set `{u} union V(H) union {c}`.  The vertex `u` is complete to
`H` and nonadjacent to `c`.  Moreover

```text
d_H(c) = |N_G(C)| >= 7,
```

where the lower bound is the separation bound already proved.  Thus, writing
`d=d_G(u)`, the three disjoint edge classes give

```text
|E(M)| = d + |E(H)| + d_H(c)
       >= d + ceil(5d/2) + 7.
```

No edge is double-counted.  This quotient is a minor of `G`, so it remains
`K_7`-minor-free.

### Degree seven

Here `M` has nine vertices and at least

```text
7 + 18 + 7 = 32 > 5*9-15 = 30
```

edges, contradicting Mader's theorem.

### Degree eight

Here `M` has ten vertices and at least `35=5*10-15` edges.  Any strictness in
the three lower bounds contradicts Mader.  Equality forces `d_H(c)=7` and
`|E(H)|=20`; because `H` has eight vertices and minimum degree five, it is
5-regular.  Its complement is therefore 2-regular and is exactly one of

```text
C_8, C_4 dotunion C_4, C_3 dotunion C_5.
```

The displayed branch sets in the source were checked directly.

For `C_8`, label the complementary cycle `0,1,...,7` cyclically.  For the
two-`C_4` case, label the complementary cycles `0,1,2,3` and `4,5,6,7`.
Then

```text
{0,4}, {2,6}, {1}, {3}, {5}, {7}
```

are connected and pairwise adjacent in `H`.

For `C_3 dotunion C_5`, automorphisms have two vertex orbits, so the unique
non-neighbour of `c` may be labelled `0` on the triangle or `3` on the
5-cycle.  In both cases

```text
{0,3}, {1,4}, {2}, {5}, {7}, {6,c}
```

are connected and pairwise adjacent in `H+c`.  This was also independently
checked from the two complement edge sets.  Every branch set in either model
meets `H`.

### Degree nine

Now `M` has eleven vertices.  Since `|E(H)|>=23` and `d_H(c)>=7`, every case
with more than 40 edges contradicts Mader.  The only remaining integer pairs
are

```text
(|E(H)|,d_H(c)) = (23,7), (23,8), (24,7).
```

These are exactly the regimes covered by the adjacent finite lemma.  If
`F=overline(H)`, then `Delta(F)<=3`; the regimes have respectively 13, 13,
and 12 complement edges and two, one, and two non-neighbours of `c`.

The independent audit of that lemma verifies the nauty catalogue, the graph6
decoder, all possible non-neighbour sets, the restricted model construction,
and a separate reimplementation.  I also reran the pinned repository verifier
for this audit.  It returned the documented result:

```text
case F_edges=13 c_nonneighbours=2 complements=20 instances=720 bad=0
case F_edges=13 c_nonneighbours=1 complements=20 instances=180 bad=0
case F_edges=12 c_nonneighbours=2 complements=103 instances=3708 bad=0
total_instances=4608 bad=0
catalogue_sha256=489ef6397133a86bddaabb3c0a27b78b36e172d041ec5aab05e9c89ed9e175eb
witness_sha256=168b7a1b4c863029ee4ee14b1b53d8843b9b79d4b0c2205d093636a13a1abdb1
PASS degree-nine local completion
```

The finite theorem always supplies a `K_6` model in `H+c` whose six branch
sets meet `H`.

## 6. Lifting the local models

Whenever a model uses `c`, replace `c` by the original connected component
`C`.  If the model branch set containing `c` also contains vertices of `H`,
its connectedness in `H+c` guarantees at least one corresponding edge from
those vertices into `C`, so the lifted branch set remains connected.  Every
inter-branch-set edge through `c` similarly lifts to an edge incident with
`C`.

Every one of the six branch sets meets `H=N(u)`.  Therefore the singleton
`{u}` is adjacent to every lifted branch set, and the model completes to a
`K_7` minor in `G`.  This contradicts the hypotheses in all degree-seven,
degree-eight, and degree-nine cases under the assumption that every incident
pair deletion is five-chromatic.

It follows that some neighbour `z` satisfies

```text
chi(G-{u,z}) = 6.
```

## 7. Alignment with the conditional adjacent-pair theorem

Put `J=G-{u,z}`.  Deleting two vertices from a seven-connected graph leaves
a five-connected graph, so `J` is connected.  The equality `chi(J)=6` and
`HC_6` give a `K_6` minor in `J`.

Any clique-minor model in a connected graph can be made spanning.  Its branch
set union is connected; while a vertex remains outside it, take an edge from
the union to an outside vertex and add the outside endpoint to the incident
branch set.  This preserves connectivity, disjointness, and all old branch-set
adjacencies.

The hypotheses of the separately audited conditional adjacent-pair palette
theorem are now satisfied at this particular edge `uz`.  It gives the stated
six-colouring of `G-uz`, saturation of the five other colours at each pole,
and the five pairwise vertex-disjoint palette paths in `J`.

Finally, every component of `G-N[u]` is contained in `J`: it contains neither
`u` nor any neighbour of `u`, and `z` is a neighbour of `u`.  Thus the
low-degree separation and the palette framework genuinely use the same pole
and the same two-vertex-deleted graph.

## 8. Trust boundary and exact remaining gap

The theorem is unbounded in `|V(G)|`.  Finite computation enters only in two
literal bounded interfaces: the nine-vertex pole neighbourhood in the
degree-nine equality regimes, and the already promoted classification of
five-critical boundaries of orders eight and nine under the two-full-shore
join exclusion.  The surviving order-nine boundary is eliminated here by the
hand branch-set model above.  Neither finite search is being used as an
unstated order bound on `G`.

The result does **not** prove any of the following:

1. that an order-eight or order-nine separation can be reduced to order
   seven;
2. that the independently attained shore colourings agree on all of `S`;
3. that a separation from a failed labelled branch-set exchange is the same
   anti-neighbourhood separation; or
4. that enlarging a deficient labelled branch set to its containing
   anti-neighbourhood component preserves the old branch-set labels and path
   data.

The primary external extremal input is W. Mader, *Homomorphiesatze fur
Graphen*, Math. Ann. **178** (1968), 154--168: for `n>=7`, at least
`5n-14` edges force a `K_7` minor.  The established `HC_5` and `HC_6` cases,
the four separately audited boundary results listed above, and the separately
audited adjacent-pair palette theorem are the other nonlocal mathematical
inputs.

Subject to these explicit dependencies and limitations, the low-degree
adjacent-pair alignment theorem is **GREEN**.
