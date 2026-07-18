# Independent audit: degree-seven aligned near-`K_7` model

## Verdict

**GREEN** at the exact source revision

```text
51bd2cf191f848a398a1a4aee711ef0c4d36c747468ce9613b9514cbc56cd060  results/hc7_degree7_aligned_near_k7_model.md
```

The theorem is correct as written.  Under its hypotheses, every
degree-seven vertex `u` yields seven disjoint connected branch sets
containing `{u}` and a second boundary singleton, with either one missing
adjacency or two adjacent missing adjacencies incident with that singleton.

The theorem does not prove `HC_7`: it is conditional on the existence of a
degree-seven vertex and does not repair the remaining deficient
adjacency or adjacencies.

## 1. Full exterior and four-colour boundary

The audited anti-neighbourhood theorem gives `C=G-N[u]` nonempty and
connected.  If `C` missed one member of `S=N(u)`, its neighbourhood would
have order at most six, contrary to seven-connectivity.  Contracting `C`
therefore gives one universal vertex over `H=G[S]`; `u` is a second,
nonadjacent universal vertex.  Hence

\[
                      \overline K_2\vee H\preccurlyeq G.
\]

The revised four-colour argument is correctly universal in the chosen
degree-seven vertex.  If `chi(H)=5`, the exact-seven classification gives
`H\cong K_2\vee C_5` and two connected full shores.  Deleting the two
universal boundary vertices leaves a graph of chromatic number at least
five, hence a `K_5` minor by `HC_5`; the cycle-boundary completion theorem
then gives a forbidden `K_7` minor.  Thus `chi(H)<=4`.

Together with `alpha(H)<=2`, this makes `F=\overline H` triangle-free and
gives a matching of size three.

## 2. The nonisolated complement core

For every `ab in E(F)`, the matching/rooted-model theorem supplies a
rooted `K_5` on `S-{a,b}`.  If a nonisolated vertex `a` had unique
`F`-neighbour `b`, then `{u}`, `{a}`, and those five rooted bags would form
a `K_7` model.  Hence every nonisolated vertex of `F` has degree at least
two.

The three-edge matching uses at least six vertices.  Every edge-component
has a cycle of length at least four, so there is one nontrivial component
`K` on six or seven vertices and at most one isolated vertex.

If `K` had a cutvertex, two triangle-free leaf blocks of its block tree
would each have at least four vertices.  Equality is forced: two
four-cycles share one cutvertex, say

\[
                   v a b c v,\qquad v d e f v.
\]

If `p,q` are the independent universal vertices of
`\overline K_2\vee H`, then

\[
 \{p,v\},\ \{b,e\},\ \{a\},\ \{c\},\ \{d\},\ \{f\},\ \{q\}
\]

are seven valid `K_7` branch sets.  In particular `be in E(H)`, the four
singleton vertices form a clique in `H`, `{b,e}` meets each singleton,
and `p,q` supply the remaining contacts.  Thus `K` is two-connected.

## 3. The branch-set constructions

If `N_F(a)={b,x}`, triangle-freeness gives `bx in E(H)`.  Therefore
`D={b}\cup B_x` is connected.  The seven sets

\[
 \{u\},\ \{a\},\ D,\quad(B_t:t\in S-\{a,b,x\})
\]

are disjoint and all pairs other than `{a},D` are adjacent.  If `a` met
`B_x`, they would form a `K_7` model.  Hence the unique absent adjacency is
`{a}--D`, giving the aligned `K_7^-` model.

If the two-connected core has minimum degree at least three, its order is
six or seven.  Mantel equality gives `K\cong K_{3,3}` in order six.  In
order seven, a vertex of degree at least five would force a neighbour of
degree at most two, while odd order excludes three-regularity.  A
degree-four vertex has an independent four-vertex neighbourhood; every
member must meet both remaining vertices, which are nonadjacent.  Thus
`K\cong K_{3,4}`.

For `K_{3,4}` and for `K_{3,3}\dot\cup K_1`, the displayed enlarged rooted
bag is connected and all contacts check.  The only possibly absent pairs
are the two stated pairs incident with `{b}`.  At least one is absent under
`K_7`-minor-freeness.

## Dependencies and trust boundary

The audit checked the following exact GREEN source revisions:

```text
a73429c60377546d55f9578a7795eb45634a98fdc87d84604ee62865880a90f3
results/hc7_degree7_anti_neighbourhood_connectivity.md

7fda58a909aabf5a49c32be513ebc598695c448855a4a8bede3ae1efdc63314a
results/hc7_degree7_matching_bridge_bundle.md

cd4b7fcf03242e41434522ac2eedd83425c418b83917d2ba1e94dd6740b3a568
results/hc7_exact7_no_rigid_trace.md

f87ddcf7e4bd33b0fc107033033d9a8ebb2f6e32533b1b9c4538c0bf4bd137db
results/hc7_cycle_boundary_completion.md
```

The proof also uses Dirac's contraction-critical neighbourhood inequality,
Mantel's theorem and its equality case, and the established case `HC_5`.
It does not prove that a hypothetical counterexample has a degree-seven
vertex, create the missing centre adjacency, or synchronize shore
colourings.
