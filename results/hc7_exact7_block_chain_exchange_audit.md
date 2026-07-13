# Independent audit: exact-seven block-chain exchange

## Verdict

**GREEN.**  The graph-theoretic attachment claim, both Hall arguments,
the rooted-triangle construction, all carrier disjointness and
connectivity claims, the two seven-connectivity estimates, and all 21
literal `K_7` adjacencies are correct under the stated hypotheses.
Corollary 4.1 correctly concludes that each lobe's block--cutvertex tree
is a path.  It does not say that the lobe itself is a path or bound its
order.

## 1. Components outside a maximal block

Let `B` be a maximal nontrivial 2-connected block of the connected lobe
`J`.  A component `A` of `J-V(B)` has a neighbour in `B` by
connectedness.  It cannot have distinct neighbours `x,y in B`: a
shortest `x-y` path with interior in `A`, added as an ear to the
2-connected graph `B`, is again 2-connected and strictly enlarges `B`.
Thus `A` has the unique attachment `z_A` asserted in the note.

Inside `G[L]`, every exit from `A` lies in `\{z_A\} union U_A`.  If
`|U_A|<=1`, those at most two vertices separate `A` from the nonempty
opposite lobe `K`, contradicting 3-connectivity.  Hence `|U_A|>=2`.

In the whole graph every exit lies in

\[
                  \{z_A\}\cup U_A\cup N_S(A).
\]

Deleting this set leaves both `A` and vertices of `K` and `R`, so it is
a genuine separator.  Seven-connectivity gives

\[
 1+|U_A|+|N_S(A)|\ge7,
 \qquad |N_S(A)|\ge6-|U_A|\ge3.
\]

No edge through `S` is incorrectly used in the 3-connectivity argument,
and no possible exit is omitted in the 7-connectivity argument.

## 2. Gate SDR and its exceptional pattern

The allowed gate sets are the three 2-subsets of the 3-set `T` and `T`
itself.  Three such sets fail Hall exactly when all three equal one fixed
2-set.  A direct enumeration of all `4^3=64` ordered triples found
exactly the three failures

\[
 (\{1,2\},\{1,2\},\{1,2\}),\quad
 (\{1,3\},\{1,3\},\{1,3\}),\quad
 (\{2,3\},\{2,3\},\{2,3\}).
\]

The choice paragraph is also sound when several branches share an
attachment vertex.  If any branch has a gate set different from the
common failed 2-set, choose that branch at its attachment and branches
at two other distinct attachment vertices.  The resulting triple is
not three copies of one 2-set and therefore has an SDR.  Since `B` has
at least three distinct attachment cutvertices, the three roots remain
distinct.

Thus the only global failure has one fixed pair `\{u,v\}` on every
`B`-branch.  The lobe `J` meets the third gate `w`, by
3-connectivity of `G[L]`.  Every vertex of `J-V(B)` lies in a
`B`-branch and no such branch meets `w`; consequently a literal edge
`yw` exists for some `y in B`, as claimed.

## 3. Rooted `K_3` inside `B`

The standard assertion used in the proof is valid:

> Every 2-connected graph has a `K_3` minor rooted at any three
> distinct prescribed vertices.

One construction is as follows.  Take a cycle through two roots.  By
the fan lemma, the third root has two internally disjoint paths to two
distinct points of the cycle.  The two cycle arcs and the path through
the third root form a theta subgraph.  Cut the two cycle arcs so that
the first two roots lie on opposite connected sides; put the third
root and the interiors of its two fan paths in the third bag.  The three
bags are connected, disjoint, rooted correctly, and pairwise adjacent.

Any rooted model can be made spanning: each component outside the union
of its three bags has an edge to that connected union and may be assigned
wholly to one adjacent bag.  Repeating preserves connectivity,
disjointness, roots, and the three existing bag adjacencies.  Hence, in
the exceptional gate case, the rooted partition may be chosen spanning,
and all indices may be renamed so that `y in Q_3` without changing
which branch is rooted in which bag.

## 4. Literal carriers

In the SDR case the carriers are

\[
                       W_i=A_i\cup Q_i\cup\{u_i\}.
\]

They are disjoint because the branches have distinct attachment
vertices and hence are distinct components outside `B`, the rooted bags
partition disjoint parts of `B`, and the gates `u_i` are distinct.
Each is connected through the literal edges `A_i-z_i` and `A_i-u_i`.
They are pairwise adjacent through the rooted `Q_i` bags.  The opposite
lobe `K` meets every literal gate and is therefore adjacent to each
`W_i`.

In the exceptional case the same checks apply to

\[
 A_1\cup Q_1\cup\{u\},\quad
 A_2\cup Q_2\cup\{v\},\quad
 A_3\cup Q_3\cup\{w\}.
\]

The third carrier is connected by `A_3-z_3`, connectivity of `Q_3`,
and the literal edge `yw` with `y in Q_3`.  The three gates are distinct,
so the carriers remain disjoint.  The opposite lobe meets `u,v,w`, and
the rooted bags retain all three mutual carrier adjacencies.

Thus `W_1,W_2,W_3,K` are four disjoint connected pairwise adjacent
literal carriers in both cases.

## 5. Boundary SDR and the final `K_7`

Each of the three branch contact sets `N_S(A_i)` has order at least
three.  Hall's condition is automatic for three subsets of a
seven-element set with this lower bound: every nonempty subfamily has
union of order at least three, hence at least its number of members.
Choose distinct representatives `s_i in N_S(A_i)`.

Every exit from `K` lies in `T union N_S(K)`.  This set separates `K`
from `J` and the nonempty opposite open shore, so seven-connectivity
gives `|N_S(K)|>=4`.  A fourth representative

\[
                 s_0\in N_S(K)-\{s_1,s_2,s_3\}
\]

therefore exists.  Adding these four distinct boundary vertices to the
four carriers preserves their connectivity and disjointness.

Let `r_1,r_2,r_3` be the remaining boundary vertices and let
`E_i=P_i union \{r_i\}` for the three disjoint `S`-full packets in `R`.
The 21 adjacencies are:

| Bag pairs | Number | Literal witness |
|---|---:|---|
| among the four enlarged carriers | 6 | the rooted `K_3` edges and the three `K`-gate edges |
| packet bags to enlarged carriers | 12 | `P_i-s_j`, by fullness |
| among the three packet bags | 3 | `P_i-r_j`, by fullness |

All seven bags are connected and disjoint.  The count
`6+12+3=21` proves that they form a literal `K_7` model.

## 6. Block--cutvertex tree corollary

For a cutvertex `z` of a connected graph, its degree as a cutvertex node
in the block--cutvertex tree equals the number of components after
deleting `z`.  The independently audited nested-cutvertex exchange
bounds this by two in each lobe.

A nontrivial block node is adjacent precisely to the distinct
cutvertices contained in that block.  Theorem 3.1 bounds their number by
two.  A bridge block has only its two endpoints and hence also has block
tree degree at most two; an isolated trivial block has degree zero.
Therefore the block--cutvertex tree has maximum degree at most two.  It
is a finite connected tree, so it is a path.

No stronger conclusion is implicit: its block nodes may represent
arbitrarily large 2-connected graphs, and the theorem supplies neither
a global portal order nor an apex pair.
