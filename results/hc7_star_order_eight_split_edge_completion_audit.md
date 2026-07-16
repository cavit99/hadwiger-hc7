# Internal audit of split-edge completion at the order-eight boundary

**Verdict:** GREEN for the exact revision audited.

## Audited revision

- theorem file: `results/hc7_star_order_eight_split_edge_completion.md`
- SHA-256: `eda2cad385089bd40184c7b5560dd9804d37b438683263460f8a82750a5c8e95`
- audit date: 16 July 2026

This is a separate internal mathematical audit, not external peer review.
It checks the statement and proof of Theorem 1, all twenty-one branch-set
adjacencies, the exact inherited hypotheses used by Corollary 2, and the
comparison with the earlier asymmetric shore split.

## 1. Branch sets, disjointness, and connectedness

Write

\[
 E=V(e),\qquad X=V(P)\cup\{x\},\qquad
 Y=V(Q)\cup\{f_2\},\qquad Z=V(B)\cup\{f_1\}.
\]

The seven proposed branch sets are

\[
                  E,\ X,\ Y,\ Z,\ \{r\}\quad(r\in R).
\]

They are pairwise disjoint.  The subgraphs `P,Q` are vertex-disjoint and
lie in `A`; the set `B` and the boundary `S` are disjoint from `A`; and
the displayed parts `R,V(e),V(f),{x}` partition `S`.  In particular,
`f_1` and `f_2` are distinct and neither belongs to `E`.

Every branch set is connected:

- `E` is the edge `e`;
- `X` is connected by the assumed edge from `P` to `x`;
- `Y` is connected by `ell_e f_2`, since `ell_e` belongs to `Q`;
- `Z` is connected because `G[B]` is connected and boundary-fullness gives
  an edge from `f_1` to `B`; and
- the three remaining branch sets are singletons.

No edge between the two open sets `A,B`, and no edge between `P,Q`, is
used.

## 2. All twenty-one adjacencies

The three singleton branch sets from `R` are pairwise adjacent because
`R` is a clique.  Their twelve adjacencies to `E,X,Y,Z` are as follows.

| Pair class | Number | Witness |
|---|---:|---|
| `E-{r}` | 3 | collective adjacency of `e` to each `r in R` |
| `X-{r}` | 3 | `ell_f in P` is adjacent to every vertex of `R` |
| `Y-{r}` | 3 | `ell_e in Q` is adjacent to every vertex of `R` |
| `Z-{r}` | 3 | boundary-fullness of `B` |

The six adjacencies among `E,X,Y,Z` have literal witnesses:

| Pair | Witness |
|---|---|
| `E-X` | an edge from `ell_f` to `V(e)` |
| `E-Y` | the assumed edge from `Q` to `V(e)` |
| `E-Z` | an edge from `B` to an endpoint of `e` |
| `X-Y` | the edge `ell_e ell_f` |
| `X-Z` | an edge from `x` to `B` |
| `Y-Z` | the edge `f_1f_2` |

The counts are `3+12+6=21`.  Thus every pair of the seven disjoint
connected sets is adjacent, and the conclusion is an explicit `K_7`-minor
model.

The proof uses less than the full star-boundary setup.  It does not use
anticompleteness of the two open sets, anticompleteness of `e` and `f`, or
collective adjacency of `f` to `R`.  Full boundary contact of `B` is used
only at `x`, `f_1`, at least one endpoint of `e`, and every vertex of `R`.

## 3. Corollary 2

The exact order-eight star configuration supplies every hypothesis not
repeated in item 5 of Theorem 1.

1. The lifted separator has the displayed partition
   `S=R dotcup V(e) dotcup V(f) dotcup {x}`; `R` is a three-clique and
   `e,f` are disjoint edges.
2. The two open components are disjoint from `S`; the component denoted
   by `B` is connected and has a neighbour at every literal boundary
   vertex.
3. The rooted-web localization places the adjacent omitted clique vertices
   `ell_e,ell_f` in the other open component `A`.  Since they belong to the
   original five-clique `L=R union {ell_e,ell_f}`, they are adjacent to one
   another and each is complete to `R`.
4. The defect edge `e` is collectively adjacent to
   `L-{ell_e}`, so `ell_f` has a neighbour in `V(e)`.  Similarly, `f` is
   collectively adjacent to `L-{ell_f}`, so `ell_e` is adjacent to an
   endpoint `f_2` of `f`.
5. Collective adjacency of `e` to every vertex of `R` is part of the
   defect-edge normalization.

Consequently, if `A` contained `P,Q` satisfying item 5, Theorem 1 would
give a `K_7` minor, contrary to the ambient `K_7`-minor-free hypothesis.
The original star data are symmetric under simultaneously interchanging
`e` with `f` and `ell_e` with `ell_f`, so the relabelled conclusion is
valid as stated.

The corollary depends on the promoted rooted-web localization for the fact
that both omitted clique vertices lie in the same named open component.
It is not a statement about an arbitrary order-eight separator with two
full components.

## 4. Comparison with the asymmetric shore split

The comparison in the theorem file is accurate.  The earlier asymmetric
shore-split theorem requires both of its interior connected subgraphs to
have a neighbour at `x`.  This remains true after interchanging the two
interior subgraphs, interchanging `e,f`, or performing both relabellings.
The present theorem assumes a `P-x` contact but does not assume any
`Q-x` contact.

After interchanging `e` and `f`, the new contacts do make `P` eligible for
the first role of the old theorem: `P` meets `x`, `V(e)`, and every vertex
of `R`.  The second role still requires the missing `Q-x` contact.  Swapping
`P,Q` merely moves that same missing requirement.  Interchanging the two
open components is not licensed, because the hypotheses supply the two
disjoint connected subgraphs only in `A`.

The displayed branch-set constructions are also different.  The old
theorem keeps one boundary edge as a single branch set.  The new theorem
splits the endpoints `f_1,f_2` between `Z` and `Y`, uses `f_1f_2` for the
`Y-Z` adjacency, and uses `ell_e ell_f` for the `X-Y` adjacency.  Thus the
new hypotheses are not an unmentioned relabelling of the old hypotheses.
This comparison concerns what follows from the supplied witnesses `P,Q`;
it does not claim that a particular host graph cannot contain some other
pair satisfying the earlier theorem.

## 5. Trust boundary

The audited result is an unbounded explicit branch-set construction and
its exact exclusion inside the promoted order-eight star configuration.
The equivalent formulation by two vertex-disjoint paths follows by taking
paths inside the connected subgraphs `P,Q`, and conversely by using the
two paths as those subgraphs.

The final description of this linkage as crossing in the canonical web is
context inherited from the separately audited rooted-web theorem and is
not needed for Theorem 1 or Corollary 2.  This audit does not credit any
claim that the required linkage exists.  The result does not produce
`P,Q`, synchronize the two shore colourings, give a smaller separator,
eliminate the full balanced order-eight branch, prove the compact-model
transversal theorem, or prove `HC_7`.
