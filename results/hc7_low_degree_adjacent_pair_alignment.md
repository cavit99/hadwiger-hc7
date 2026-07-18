# A low-degree adjacent pair and a bounded separation in a hypothetical `HC_7` counterexample

**Status:** written proof; separately audited GREEN.  The degree-nine local
completion is computer-assisted and separately audited.  This theorem does
not prove `HC_7`.

## Theorem 1 (low-degree adjacent-pair alignment)

Let `G` be a finite simple graph such that:

1. `G` is seven-connected and `chi(G)=7`;
2. `G` has no `K_7` minor; and
3. every proper minor of `G` is six-colourable.

Assume the established case `HC_6`.  Then there are adjacent vertices
`u,z` such that

\[
                 7\le d_G(u)\le9,
        \qquad   \chi(G-\{u,z\})=6.                 \tag{1.1}
\]

For every component `C` of `G-N[u]`, put `S=N_G(C)`.  Then

\[
                    S\subseteq N(u),
        \qquad 7\le |S|\le d_G(u)\le9,             \tag{1.2}
\]

and

\[
                         \bigl(G[C\cup S],G-C\bigr)       \tag{1.3}
\]

is an actual separation with nonempty open sides.  Both sides are full to
`S`: every vertex of `S` has a neighbour in `C`, while the opposite open
side contains `u`, which is adjacent to every vertex of `S`.

There is also a trace-complete boundary-colouring response on both closed
shores.  For every nonempty independent set `I` of `G[S]`, each of
`G[C∪S]` and `G-C` has a proper six-colouring in which `I` is an
exact colour block on `S`: all vertices of `I` have one colour, and no
vertex of `S-I` has that colour.

Moreover, contracting `C` to one vertex shows that

\[
                         \overline{K_2}\vee G[S]          \tag{1.4}
\]

is a minor of `G`, where `vee` denotes graph join.  Consequently it has no
`K_7` minor.

In fact the boundary is always four-colourable:

\[
                              \chi(G[S])\le4.             \tag{1.5}
\]

It also satisfies the contraction-critical neighbourhood bound

\[
                 \alpha(G[S])\le \alpha(G[N(u)])
                    \le d_G(u)-5\le4.                    \tag{1.6}
\]

Consequently the same low-degree vertex `u` supports both the audited
adjacent-pair palette framework and a full actual separation of order
seven, eight, or nine.

## 1. A low-degree nonuniversal vertex

Mader's exact extremal bound for a `K_7`-minor-free graph gives

\[
                         |E(G)|\le5|V(G)|-15.       \tag{1.7}
\]

Thus the average degree is strictly below ten.  Seven-connectivity gives
minimum degree at least seven, so some vertex `u` satisfies

\[
                              7\le d_G(u)\le9.      \tag{1.8}
\]

The vertex `u` is not universal.  Otherwise `G-u` is six-colourable by
proper-minor minimality.  It is not five-colourable, since a fifth-colour
colouring together with one fresh colour on the universal vertex would
six-colour `G`.  Hence `chi(G-u)=6`; by `HC_6`, the graph `G-u` has a
`K_6` minor, and the singleton branch set `{u}` completes it to a `K_7`
minor.  This contradiction proves that `G-N[u]` is nonempty.

For completeness, the last inequality in (1.6) follows directly from
proper-minor criticality.  Let `I` be a maximum independent set in
`G[N(u)]` and contract the connected star on `\{u\}\cup I` to a vertex
`w`.  Lift a six-colouring of this proper minor to `G-u` by giving every
vertex of `I` the colour of `w`.  The set `N(u)-I` avoids that colour.  If
`|N(u)-I|<=4`, then at most five colours occur on `N(u)`, leaving a sixth
colour for `u`, contrary to `chi(G)=7`.  Hence
`|N(u)-I|>=5`, which is exactly
`alpha(G[N(u)])<=d_G(u)-5`.  The first inequality in (1.6) follows from
`S⊆N(u)`.

## 2. The bounded full separation

Let `C` be any component of `G-N[u]` and put `S=N_G(C)`.  Every neighbour
of `C` outside `C` lies in `N(u)`: any other such vertex would be a vertex
of `G-N[u]` joined to `C`, contrary to the definition of a component.
Thus `S` is a subset of `N(u)`.  The vertex `u` lies outside both `C` and
`S`, so

\[
                    \bigl(G[C\cup S],\,G-C\bigr)   \tag{2.1}
\]

is an actual separation with nonempty open sides.  Seven-connectivity and
the inclusion `S⊆N(u)` give (1.2).  By the definition of `S`,
every member of `S` has a neighbour in `C`; the vertex `u` on the other
open side is adjacent to all of `S`.

Fix a nonempty independent set `I` of `G[S]`.  Contract the connected star
on `\{u\}\cup I` to a vertex `w`.  The resulting proper minor is
six-colourable.  Every vertex of `S-I` is adjacent to `u`, so `w` is
adjacent to all of `S-I`.  Restrict the minor colouring to `G[C∪S]`,
assigning every member of `I` the colour of `w`.  This is proper because
`I` is independent, and every edge incident with a vertex of `I`
corresponds to an edge at `w` in the minor.  The set `I` is an exact colour
block on `S`.

For the other shore, contract the connected set `C∪I` to one vertex
`w`.  It is connected because every member of `I` has a neighbour in `C`.
Every member of `S-I` also has a neighbour in `C`, so `w` is adjacent to
all of `S-I`.  Restrict the minor colouring to `G-C`, assigning every
member of `I` the colour of `w`.  The same edge check proves that this is a
proper six-colouring and that `I` is again an exact colour block on `S`.

The two colourings need not induce the same partition of `S-I`.  The
theorem does not claim colour compatibility across the separation.

Finally, contract `C` to one vertex `c`.  The vertices `c,u` are
nonadjacent and each is adjacent to every vertex of `S`.  Retaining only
`\{c,u\}\cup S` gives the minor (1.4).

### 2.1. The boundary is four-colourable

We use two previously audited boundary theorems.  For an order-seven
separation, every boundary component is full by seven-connectivity; the
exact-seven classification says that a five-chromatic boundary would be
`K_2 join C_5`, with exactly two connected full open shores.  The
pentagonal instance of the cycle-boundary completion theorem then gives a
`K_7` minor.  Hence `chi(G[S])<=4` when `|S|=7`.

For `|S|=8` or `9`, apply the two-full-shore boundary-absorption theorem to
`C`, the component of `G-S` containing `u`, and `S`.  It gives
`chi(G[S])<=4` when `|S|=8`.  When `|S|=9`, its only alternative is

\[
                              G[S]\cong K_2\vee C_7.      \tag{2.2}
\]

Write the universal edge of (2.2) as `pq` and label the induced cycle in
cyclic order by `0,1,...,6`.  Let `A=C` and let `B` be the component of
`G-S` containing `u`.  Both are connected and full to `S`.

If `A,B` are the only components of `G-S`, the cycle-boundary completion
theorem applies.  Its `K_5`-minor hypothesis is automatic: deleting `p,q`
lowers the chromatic number by at most two, so `chi(G-{p,q})>=5`, and the
established case `HC_5` supplies the `K_5` minor.

Otherwise choose a third component `D` of `G-S`.  Seven-connectivity gives
`|N_G(D)|>=7`, so `D` misses at most two vertices of `S`.  Up to swapping
`p,q` and applying a dihedral symmetry of the cycle, its missed set is one
of

\[
 \varnothing,\ \{p\},\ \{0\},\ \{p,q\},\ \{p,0\},
 \ \{0,1\},\ \{0,2\},\ \{0,3\}.                   \tag{2.3}
\]

In every case in (2.3), `D` meets `4`, `6`, and at least one of
`p,0,1`.  The following seven sets are therefore an explicit `K_7`-minor
model:

\[
 \{p,0,1\},\quad \{q\},\quad A\cup\{2\},\quad
 B\cup\{3\},\quad D\cup\{4\},\quad \{5\},\quad \{6\}. \tag{2.4}
\]

They are disjoint and connected.  The universal vertices `p,q`, fullness
of `A,B`, the contacts of `D` just listed, and the cycle edges
`2-3`, `4-5`, and `5-6` supply all pairwise adjacencies.  For clarity, the
only less immediate pairs are joined as follows: `A∪{2}` meets
`D∪{4}` through an edge from `A` to `4`; `B∪{3}` meets
`D∪{4}` through an edge from `B` to `4`; and `D∪{4}` meets
`{6}` through a `D-6` edge.

Thus (2.2) is impossible, proving (1.5) for all three boundary orders.

## 3. An eligible adjacent edge at the same vertex

Suppose for a contradiction that

\[
             \chi(G-\{u,x\})=5\quad\hbox{for every }x\in N(u). \tag{3.1}
\]

These are the only possible smaller values: deleting two vertices from a
seven-chromatic graph lowers its chromatic number by at most two, while a
proper minor is six-colourable.

Put `H=G[N(u)]` and `d=d_G(u)`.  For any `x` in `N(u)`, fix a five-colouring
of `G-{u,x}`.  Every colour occurs on a common neighbour of `u` and `x`.
For completeness, if colour `i` did not, recolour every colour-`i`
neighbour of `u` with one new sixth colour, give `u` colour `i`, and give
`x` the new colour.  The recoloured vertices are independent and none is
adjacent to `x`; this would six-colour `G`.  Therefore

\[
                              \delta(H)\ge5.         \tag{3.2}
\]

Choose a component `C` of `G-N[u]`.  Contract `C` to a vertex `c`, delete
all other vertices outside `N[u]∪C`, and simplify parallel edges.
The resulting minor `M` has vertex set

\[
                         \{u\}\cup V(H)\cup\{c\},   \tag{3.3}
\]

where `u` is complete to `H`, `u` is nonadjacent to `c`, and

\[
                          d_H(c)=|N_G(C)|\ge7.       \tag{3.4}
\]

Here `d_H(c)` denotes the number of neighbours of `c` in `H`.  From
(3.2),

\[
        |E(M)|\ge d+\left\lceil\frac{5d}{2}\right\rceil+7. \tag{3.5}
\]

### Degree seven

The minor `M` has nine vertices and at least

\[
                        7+18+7=32>5\cdot9-15
\]

edges.  This contradicts Mader's bound.

### Degree eight

The minor `M` has ten vertices and at least `35=5*10-15` edges.  If any
inequality is strict, Mader's bound is contradicted.  Equality therefore
forces `H` to be 5-regular and `d_H(c)=7`.  The complement of `H` is a
2-regular graph on eight vertices, hence one of

\[
                   C_8,\qquad C_4\mathbin{\dot\cup}C_4,
                   \qquad C_3\mathbin{\dot\cup}C_5. \tag{3.6}
\]

For the first two graphs, use their natural cyclic labels.  The six sets

\[
       \{0,4\},\ \{2,6\},\ \{1\},\ \{3\},\ \{5\},\ \{7\} \tag{3.7}
\]

form a `K_6`-minor model in `H`.

For the third graph, label its triangle `0,1,2` and its 5-cycle
`3,4,5,6,7`.  By symmetry the unique non-neighbour of `c` in `H` may be
labelled `0` or `3`.  In either case

\[
 \{0,3\},\ \{1,4\},\ \{2\},\ \{5\},\ \{7\},\ \{6,c\} \tag{3.8}
\]

forms a `K_6`-minor model in `H+c`.

Every branch set in (3.7) or (3.8) meets `H=N(u)`.  Replacing `c`, when
present, by the original connected subgraph `C` lifts the model to `G-u`.
The singleton `{u}` is adjacent to every lifted branch set and completes a
`K_7` model, a contradiction.

### Degree nine

Now `M` has eleven vertices and at least 39 edges.  The only cases not
settled immediately by Mader's bound are

\[
              (|E(H)|,d_H(c))=(23,7),(23,8),(24,7). \tag{3.9}
\]

The adjacent computer-assisted finite lemma proves that in each case
`H+c` has a `K_6`-minor model whose six branch sets all meet `H`.  Its
deterministic verifier exhausts the complements $F=\overline H$ with
maximum degree at most three: twenty isomorphism types with 13 edges and
103 with 12
edges, together with every one- or two-vertex non-neighbour set of `c`.
It checks

\[
                  720+180+3708=4608                 \tag{3.10}
\]

rooted instances and, more strongly, always finds a model consisting of
three `H`-edges, three singleton vertices of `H`, and `c` adjoined to one
of those six branch sets.  See
[`hc7_degree9_pole_verifier.md`](hc7_degree9_pole_verifier.md).

Replacing `c` by `C` and adjoining `{u}` again gives a `K_7` model.

All three values of `d` contradict (3.1).  Thus some neighbour `z` of
`u` satisfies `chi(G-{u,z})=6`, proving (1.1).

## 4. Alignment with the existing adjacent-pair theorem

Put `J=G-{u,z}`.  Deleting two vertices from a seven-connected graph
leaves a five-connected graph, so `J` is connected.  Since `chi(J)=6`,
the established case `HC_6` gives a `K_6` minor in `J`; connectivity lets
us enlarge its branch sets to a spanning model.  Therefore every conclusion
of the audited conditional adjacent-pair palette theorem applies with this
particular low-degree pole `u`.

In particular, `G-uz` has a six-colouring in which `u,z` share one colour,
each sees all five other colours, and five pairwise vertex-disjoint paths
join selected complete five-colour palettes at the two poles.  Every
component of `G-N[u]` lies inside this same graph `J`, because `z` belongs
to `N(u)`.

## 5. Scope

The genuinely new conclusion is the alignment in (1.1).  The degree
window and the anti-neighbourhood separation were known separately; the
theorem places the full adjacent-pair framework at that same bounded-degree
vertex.

This still does not prove `HC_7`:

1. a returned separation can have order eight or nine rather than seven;
2. its two singleton-boundary colourings need not agree on the remaining
   boundary vertices;
3. the bounded anti-neighbourhood separation need not equal a separator
   returned by a failed rooted-model exchange; and
4. enlarging a labelled deficient branch set to its containing component
   of `G-N[u]` can lose the branch-set labels and path data used by that
   exchange.

## Inputs

- W. Mader, the exact extremal bound `|E(G)|<=5|V(G)|-15` for graphs with
  no `K_7` minor.
- K. Kawarabayashi, A. S. Pedersen and B. Toft,
  *Double-critical graphs and complete minors*, Electronic Journal of
  Combinatorics **17** (2010), R87, Proposition 3.3 and Corollary 3.1 for
  the standard common-neighbour consequence.  The elementary local proof
  needed here is included above.
- The established case `HC_6`.
- [adjacent-pair palette linkage and contact consequences](../results/hc7_adjacent_pair_palette_linkage.md).
- [exact seven-vertex boundary classification](../results/hc7_exact7_no_rigid_trace.md).
- [two-full-shore boundary absorption at orders eight and nine](../results/hc7_two_full_shore_boundary_absorption.md).
- [cycle-boundary completion theorem](../results/hc7_cycle_boundary_completion.md).
