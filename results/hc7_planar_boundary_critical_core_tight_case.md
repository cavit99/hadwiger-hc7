# Tight vertices in the planar fixed-boundary critical core

**Status:** written proof, independently audited in
[`hc7_planar_boundary_critical_core_tight_case_audit.md`](hc7_planar_boundary_critical_core_tight_case_audit.md).
The general Gallai-forest lemma and the exact slack identity apply to arbitrary planar
fixed-boundary critical cores.  In the balanced order-eight configuration,
the zero-slack `K_4` core is eliminated by an explicit `K_7`-minor
construction.  The note does not eliminate the two-vertex core, the
zero-slack triangle, or the positive-slack case, and does not prove `HC_7`.

## 1. General fixed-boundary setup

Let `X` be a graph, let `S subseteq V(X)`, and let `uv` be an edge with
both ends outside `S`.  Suppose that `kappa` is a proper six-colouring of
`X-uv`, with

\[
                         \kappa(u)=\kappa(v).
\]

For `w in V(X)-S`, put

\[
 L(w)=[6]-\{\kappa(s):s\in N_X(w)\cap S\}.
                                                        \tag{1.1}
\]

Suppose `K` is a connected induced subgraph of `X-S` which contains `uv`,
is not `L`-colourable, and every proper induced subgraph of `K` is
`L`-colourable.  As in the promoted
[fixed-boundary criticality theorem](../results/hc7_double_equality_boundary_criticality.md),

\[
                         d_K(w)\ge |L(w)|               \tag{1.2}
\]

for every `w in V(K)`.

Define

\[
 \varepsilon(w)=d_K(w)-|L(w)|,
 \qquad
 c(w)=6-|L(w)|.
                                                        \tag{1.3}
\]

Thus `c(w)` is the number of distinct colours seen by `w` on the literal
boundary, while `epsilon(w)` is the list-degree excess.  Let

\[
 T=\{w\in V(K):\varepsilon(w)=0\},
 \qquad E=V(K)-T.                                      \tag{1.4}
\]

## 2. The tight vertices form a Gallai forest

### Theorem 2.1

Every block of `K[T]` is a complete graph or an odd cycle.  Equivalently,
`K[T]` is a Gallai forest.

### Proof

Suppose a block `B` of `K[T]` is neither a complete graph nor an odd
cycle.  By the vertex-minimality of `K`, the proper induced subgraph
`K-V(B)` has an `L`-colouring `phi`; if `V(B)=V(K)`, take the empty
colouring.

For `w in V(B)`, delete from `L(w)` the colours used by its neighbours in
`K-V(B)`, and call the resulting list `L_B(w)`.  At most
`d_K(w)-d_B(w)` colours are deleted.  Since `w` is tight,

\[
 |L_B(w)|\ge |L(w)|-(d_K(w)-d_B(w))=d_B(w).            \tag{2.1}
\]

The degree-choosability theorem says that a connected graph is colourable
from every list assignment of orders at least its vertex degrees unless
each of its blocks is a complete graph or an odd cycle.  Applied to the
block `B` and the lists `L_B`, it gives an `L_B`-colouring of `B`.
Together with `phi`, this is an `L`-colouring of `K`, a contradiction.
Therefore no such block exists.  \(\square\)

This theorem is the safe Gallai conclusion.  It applies only to the tight
vertices; the whole core need not be a Gallai tree.

### Corollary 2.2 (exact planar slack)

If `K` is planar and has at least three vertices, then

\[
 \sum_{w\in V(K)}c(w)
   =6|K|-2|E(K)|+\sum_{w\in V(K)}\varepsilon(w)
   \ge 12+\sum_w\varepsilon(w)
   \ge 12+|E|.                                         \tag{2.2}
\]

If equality `sum c(w)=12` holds, then `K` is `K_3` or `K_4`.  In the
first case all three lists are one common two-set; in the second all four
lists are one common three-set.

### Proof

Summing (1.3) and using the degree sum gives

\[
\begin{aligned}
 \sum_w c(w)
   &=6|K|-\sum_w|L(w)|\\
   &=6|K|-2|E(K)|+\sum_w\varepsilon(w).
\end{aligned}                                          \tag{2.3}
\]

The planar bound `|E(K)|<=3|K|-6` proves (2.2).

If equality twelve holds, every vertex is tight and
`|E(K)|=3|K|-6`.  Hence `K` is a maximal planar graph (with the usual
`K_3` exception at order three), and in particular it consists of one
block.  Theorem 2.1 makes that block a planar complete graph or an odd
cycle.  Comparing its number of edges with `3|K|-6` leaves only `K_3`
and `K_4`.

For `K_t`, non-`L`-colourability is the failure of a system of distinct
representatives for its lists.  In the two remaining cases every list has
order `t-1`; Hall's theorem therefore forces the union of the lists to
have order at most `t-1`, so all lists are identical.  \(\square\)

## 3. Two elementary host consequences

Return to the balanced order-eight configuration and notation of
[`hc7_balanced_order8_frontier.md`](../active/hc7_balanced_order8_frontier.md).
Thus

\[
 S=R\mathbin{\dot\cup}V(e)\mathbin{\dot\cup}V(f)
       \mathbin{\dot\cup}\{x\},
 \qquad R\cong K_3,
\]

the leaf-side component is `C`, and
`L=R union {ell_e,ell_f}` is the original five-clique.  We use the already
promoted facts that

* `A=C-{ell_e,ell_f}` is connected;
* both leaves have a neighbour in `A`;
* `A` has a neighbour at `x` and contacts both `V(e)` and `V(f)`; and
* the
  [split-edge completion](../results/hc7_star_order_eight_split_edge_completion.md)
  and its symmetric form give a `K_7` minor
  from their two displayed disjoint connected subgraphs.

The first three bullets are the exact surviving conclusion of the
[disconnected leaf-side theorem](../results/hc7_star_order_eight_disconnected_leaf_side_completion.md)
after excluding its `K_7`-minor and order-seven-separation outputs.

### Lemma 3.1 (a seven-connected `K_7`-minor-free graph has no `K_6`)

If `G` is seven-connected and contains a `K_6` subgraph, then `G` contains
a `K_7` minor.

### Proof

Let `J` be the six-clique.  The graph `G-J` is nonempty, since a
seven-connected graph has at least eight vertices.  It is connected:
otherwise the neighbourhood of one of its components is a vertex cut
contained in the six-set `J`.  Every vertex of `J` has a neighbour in
`G-J`, since its degree is at least seven but it has only five neighbours
inside `J`.  Consequently the connected set `G-J`, together with the six
singleton vertices of `J`, is a `K_7`-minor model.  \(\square\)

### Lemma 3.2 (the distinguished boundary vertex misses both leaves)

If the balanced order-eight configuration has neither a `K_7` minor nor
an actual order-seven separation, then

\[
                    x\ell_e,x\ell_f\notin E(G).        \tag{3.1}
\]

### Proof

Suppose first that `x ell_f` is an edge.  Since `A` is connected, contains
a neighbour of `ell_e`, and contacts `V(e)`, it contains a connected
subgraph which, after adjoining `ell_e`, contains `ell_e` and has a
neighbour in `V(e)`.  This subgraph is disjoint from the singleton
`{ell_f}`, which has a neighbour at `x`.  The promoted split-edge
completion gives a `K_7` minor.  The case `x ell_e in E(G)` is symmetric,
using `V(f)`.  \(\square\)

## 4. The zero-slack four-clique is impossible

Assume the full balanced order-eight hypotheses, including
seven-connectivity, `chi(G)=7`, six-colourability of every proper minor,
absence of a `K_7` minor, and exclusion of the earlier actual
order-seven-separation output.  Let `kappa` be a simultaneous-equality colouring from the
promoted fixed-boundary theorem, and suppose that `g=ell_e ell_f` is
nonrepairable on the closed `C` side.  Let `K` be its planar critical core
and retain the definitions (1.1)--(1.4).

### Theorem 4.1

If

\[
              |K|\ge3,
 \qquad       \sum_{w\in V(K)}c(w)=12,                \tag{4.1}
\]

then either `K=K_3` or `G` contains a `K_7` minor.  In particular, the
zero-slack `K_4` core cannot occur in a hypothetical counterexample.

### Proof

By Corollary 2.2, `K` is `K_3` or `K_4`.  Suppose

\[
                 K=G[\{\ell_e,\ell_f,p,q\}]\cong K_4. \tag{4.2}
\]

All four lists are one common three-set.  The three vertices of `R` have
three distinct colours and are adjacent to both leaves.  The common list
is therefore exactly the complement in `[6]` of the three colours used on
`R`.  It follows that the set of boundary colours seen by each of `p,q`
is exactly the set of colours used on `R`.

Neither `p` nor `q` is adjacent to all of `R`.  Otherwise that vertex,
the two leaves, and `R` would induce a `K_6`, contrary to Lemma 3.1.
For `v in {p,q}`, choose a vertex of `R` missed by `v`.  Since `v` sees
the colour of that missed vertex on the boundary, it has a neighbour in

\[
                         S-R=V(e)\cup V(f)\cup\{x\}.   \tag{4.3}
\]

Partition (4.3) into the three displayed groups.  We claim that every
neighbour in `S-R` of `p` or `q` belongs to one common group.  Indeed,
both `p` and `q` have at least one such neighbour.  If `p` had a neighbour
in one group and `q` had a neighbour in a different group, use the two
length-two paths through `p,q`, assigning their leaf ends as follows:

* groups `V(e),V(f)`: join `ell_e` to `V(e)` and `ell_f` to `V(f)`;
* groups `V(e),{x}`: join `ell_e` to `V(e)` and `ell_f` to `x`;
* groups `V(f),{x}`: join `ell_f` to `V(f)` and `ell_e` to `x`.

The paths are vertex-disjoint.  The first placement supplies the missing
same-index rooted linkage in the
[canonical four-root graph](../results/hc7_star_order_eight_rooted_web.md);
its four rooted branch sets, lifted through the two boundary-edge
contractions, together with the three singleton vertices of `R`, are
the seven branch sets.  The other two placements invoke the promoted
split-edge completion or its symmetric form, whose displayed seven
branch sets use `R`, the opposite full shore, and the split endpoints of
one boundary edge.  Each gives an explicit `K_7`-minor model.  Therefore, in the
`K_7`-minor-free branch, the group sets of `p,q` are the same singleton;
call the group `U`.

The union of the sets of vertices of `R` missed by `p,q` has order at
least two.  If it had order at most one, two vertices of `R` would be
adjacent to both `p,q`, and those two vertices together with the four-clique
in (4.2) would induce a `K_6`, again contradicting Lemma 3.1.  The group
`U` cannot therefore be `{x}`: one literal vertex has only one colour and
cannot supply the colours of two distinct vertices of `R`.  Consequently

\[
                         U=V(e)\quad\hbox{or}\quad U=V(f).  \tag{4.4}
\]

Suppose `U=V(e)`; the other case is symmetric.  In particular each of
`p,q` has a neighbour in `V(e)`, and neither has a neighbour at `x`.
Choose a shortest path in the connected graph `A` from the set `{p,q}`
to a vertex having a neighbour at `x`.  Let its first vertex be `v` and
let `w` be the other member of `{p,q}`.  Its final vertex is not `p` or
`q`, and shortestness makes the path avoid `w`.

Adjoin `ell_f` to this path.  The resulting connected subgraph contains
`ell_f` and has a neighbour at `x`.  The edge `ell_e w`, together with
the chosen `w`--`V(e)` contact, gives a disjoint connected subgraph
containing `ell_e` and having a neighbour in `V(e)`.  These are precisely
the two connected subgraphs required by the split-edge completion, so
`G` has a `K_7` minor.

If `U=V(f)`, interchange the two leaf/defect-edge labels and apply the
symmetric completion.  This proves the theorem.  \(\square\)

The proof is label-preserving: the three groups in (4.3), rather than
abstract palette colours, determine which explicit branch-set construction
is used.

## 5. Exact residue of the tight case

### Corollary 5.1

In a hypothetical balanced order-eight counterexample, a nonrepairable
leaf-side core has one of the following forms.

1. `K` is the edge `ell_e ell_f`.  Both lists are the same singleton.
   Neither leaf is adjacent to `x`; the two colours absent from the
   five-clique `L` occur on the two endpoints of `f`, both adjacent to
   `ell_e`, and on the two endpoints of `e`, both adjacent to `ell_f`.
2. `|K|>=3` and `sum c(w)>=13`.
3. `K` is a triangle `ell_e ell_f w`, all three lists are the same
   two-set, and every one of its vertices sees the same four boundary
   colours.  If the two colours absent from `L` are `gamma,delta`, then
   one of them, say `eta`, is `kappa(w)` and

   \[
                L(w)=L(\ell_e)=L(\ell_f)
                   =\{\kappa(\ell_e),\eta\}.          \tag{5.1}
   \]

   The other absent colour occurs at a neighbour of `ell_e` in `V(f)`
   and at a neighbour of `ell_f` in `V(e)`.

In outcome 3, the image of `w` in the canonical web skeleton is the unique
vertex on the bounded facial triangle incident with the outer edge
`ell_e ell_f`.

### Proof

If `|K|=2`, the promoted fixed-boundary theorem gives identical singleton
lists at the two leaves.  They therefore see every other colour on `S`.
Lemma 3.2 excludes `x`, while `ell_e` is anticomplete to `e` and
`ell_f` is anticomplete to `f`.  The two colours absent from `L` must
therefore occur on, and exhaust, the two endpoints of the opposite defect
edge, proving outcome 1.

Assume `|K|>=3`.  Corollary 2.2 gives a sum of at least twelve.  If the
sum is greater than twelve, it is at least thirteen.  If it is twelve,
Theorem 4.1 leaves only `K_3`.

For that triangle the common-list assertion follows from Corollary 2.2.
The leaves see the three colours used on `R`, so the fourth excluded
colour is one of the two colours absent from `L`; call it the other colour
than `eta`.  The restricted colouring of `K-g` gives `w` the colour
`eta`, proving (5.1).  Both leaves see the fourth excluded colour on the
boundary.  Their anticompleteness to their same-index defect edge and
Lemma 3.2 force the two stated cross-index contacts.

Finally, the triangle `ell_e ell_f w` lies in the planar skeleton of the
canonical web.  Suppose that this triangle were separating in the web
completion.  It contains neither contracted defect vertex `z_e,z_f`, so
after lifting back to `G` the six-vertex set

\[
                 R\mathbin{\dot\cup}\{\ell_e,\ell_f,w\}
\]

would separate the vertices on its two sides.  Expanding the two defect
edges cannot reconnect those sides, because neither contracted image was
deleted.  This contradicts seven-connectivity.  Thus the triangle is
nonseparating.  Since it contains the outer edge `ell_e ell_f`, it bounds
the unique bounded face incident with that edge.  Hence `w` is the unique
third vertex of that facial triangle.  \(\square\)

## 6. Remaining implication

The tight four-clique is now closed for hosts of arbitrary order.  The
remaining fixed-boundary obstruction is not an unspecified planar graph:

* the two-vertex core gives the complete cross-index colour contacts on
  the two defect edges;
* the zero-slack core of order at least three is the facial triangle at
  the opposite outer edge of the canonical web; and
* every other core has positive Euler/list slack, while its tight-vertex
  subgraph is a Gallai forest and its excess set `E` satisfies
  `sum c(w)>=12+|E|`.

No conclusion here turns the excess set into a global two-vertex
transversal.  The next theorem must use the canonical web and
minor-critical responses to do one of two things: decode the crossed-frame
edge/triangle residue, or show that positive list-degree excess creates a
labelled route to `V(e)`, `V(f)`, or `x` rather than merely another
boundary-colour incidence.

## Reference

The degree-choosability characterization used in Theorem 2.1 is the
Borodin--Erdos--Rubin--Taylor theorem.  A modern statement is Theorem A of
Daniel W. Cranston and Landon Rabern,
[*Beyond Degree Choosability*](https://doi.org/10.37236/5357),
Electronic Journal of Combinatorics **24** (2017), #P3.29.
