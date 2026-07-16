# Cross-star traces and the only safe rank for three split models

**Status:** Sections 2--4, 7, and 8 are proved and independently
cold-audited.  Section 5 is the exact remaining exchange lemma; it is not
proved here.  Section 6 is a verified falsification guardrail.  This note
does not prove the support-six transversal theorem or `HC_7`.

The purpose of the note is to put the three-model separator residue in
standard graph-minor language.  It identifies a representation-invariant
object carried by every support-six model which crosses an exact
separator, and proves the separator rank which is actually well founded.
An unrooted shore size, crossing count, or row type is not such a rank.

## 1. Conventions

A separation is an ordered pair `(A,B)` with `A union B=V(G)` and no edge
from `A-B` to `B-A`.  Its boundary is `S=A cap B`; its open shores are
`L=A-B` and `R=B-A`.

An **irredundant support-six model** is a spanning `K_5` model on a
six-set `W` which contains no literal `K_5`.  Write one of its model
representations as

\[
                 Q\mathbin{\dot\cup}\{x,y\},          \tag{1.1}
\]

where `Q` is a literal four-clique and `xy` is the two-vertex branch bag.
Put

\[
 D_x=\{q\in Q:xq\notin E(G)\},\qquad
 D_y=\{q\in Q:yq\notin E(G)\}.                        \tag{1.2}
\]

Then `D_x,D_y` are nonempty and disjoint.

## 2. The representation-invariant complement stars

### Lemma 2.1 (all possible split rows)

For an irredundant support-six model `W`, the complement of `G[W]` is the
disjoint union of two nontrivial stars and isolated vertices:

\[
       \overline {G[W]}=
       K_{1,|D_x|}\mathbin{\dot\cup}K_{1,|D_y|}
       \mathbin{\dot\cup} I.                           \tag{2.1}
\]

The displayed nontrivial components do not depend on the selected model
representation.  Every two-vertex branch bag of a spanning `K_5` model
on `W` is obtained by choosing one vertex cover of order one in each of
the two star components.  In a star with at least two leaves the centre
is forced; in a star which is one edge either endpoint may be chosen.

#### Proof

The set `Q` is a clique and `xy` is an edge.  For every `q in Q`, at
least one of `xq,yq` is an edge because the branch bag `{x,y}` is adjacent
to the singleton bag `{q}`.  Hence the only complement edges are

\[
                    xq\ (q\in D_x),\qquad
                    yq\ (q\in D_y),                   \tag{2.2}
\]

and `D_x cap D_y` is empty.  Irredundancy makes both stars nontrivial.
This proves (2.1), including its invariance as the component decomposition
of the fixed graph `overline{G[W]}`.

Now let `{u,v}` be the two-vertex bag of any spanning `K_5` model on `W`.
The other four vertices are singleton bags and hence form a clique in
`G[W]`.  Thus `{u,v}` is a vertex cover of `overline{G[W]}`.  Both
nontrivial components in (2.1) must be met, so one member is a one-vertex
cover of each star.  A nontrivial star has the unique one-vertex cover
given by its centre unless it is `K_2`, when either endpoint works.

Conversely, choose one such cover vertex from each star.  They lie in
different complement components, so they are adjacent in `G`.  Every
remaining vertex is adjacent in `G` to at least one chosen vertex, and
the remaining four vertices form a clique.  They therefore give the
two-vertex bag and four singleton bags of a spanning `K_5` model.  \(\square\)

The two nontrivial components in (2.1) will be called the **defect
stars** of the support.  This language does not name an arbitrarily chosen
split edge.

## 3. Exact form of a model crossing a separation

### Theorem 3.1 (cross-star trace)

Let `(A,B)` be a separation of a graph `G`, and let `W` support a `K_5`
model using at most six vertices.  If `W` meets both open shores, then
either `W` contains a literal `K_5`, which is contained in one closed
shore, or all of the following hold.

1. `|W|=6` and the support is irredundant.
2. Of the two defect stars of `W`, one lies wholly in the boundary `S`,
   while the other meets both open shores.
3. Every vertex of `W` outside the crossing defect star lies in `S`.

More explicitly, after orienting the shores and choosing a representation
as in (1.1),

\[
 x\in R,\qquad y\in S,\qquad
 \varnothing\ne Q\cap L\subseteq D_x,qquad
 D_y\subseteq Q\cap S,                                \tag{3.1}
\]

and every common-contact vertex
`Q-(D_x union D_y)` lies in `S`.  Hence

\[
        \{y\}\cup D_y\subseteq S,qquad
        \{x\}\cup D_x\text{ meets both }L\text{ and }R. \tag{3.2}
\]

If the crossing defect star is `K_2`, its two ends may exchange their
roles as centre and leaf in the two possible model representations.  If
it has at least three vertices, its centre, and therefore its orientation
across the separation, is forced.

#### Proof

A five-vertex `K_5` model is a literal clique.  A clique cannot meet both
open shores, since any two such vertices would give an edge between the
open shores.  If the six-set `W` contains a literal `K_5`, that clique is
likewise contained in one closed shore and is the asserted replacement.
We may therefore assume that `W` is irredundant.  It has order six and a
representation (1.1).

The singleton clique `Q` has vertices outside `S` in at most one open
shore.  It cannot be contained in `S`: if all four singleton bags lay in
`S`, the adjacent edge `xy` could meet at most one open shore.  Orient so
that `Q cap L` is nonempty.  Then `Q cap R` is empty.

The edge `xy` cannot have one end in each open shore.  Since the support
does meet `R`, one endpoint, say `x`, lies in `R`.  The other endpoint
cannot also lie in `R`, because a vertex `q in Q cap L` must be adjacent
to the branch bag `{x,y}`, and neither endpoint would be allowed an edge
to `q`.  Nor can the other endpoint lie in `L`, because `xy` is an edge.
Consequently `y in S`.

For `q in Q cap L`, the cross-shore edge `xq` is absent, while branch-bag
adjacency forces `yq` to be present.  Thus

\[
                         Q\cap L\subseteq D_x.         \tag{3.3}
\]

If `q in D_y`, disjointness of the two defect sets gives `xq in E(G)`.
Such a `q` cannot lie in `L`, because `x in R`, and it cannot lie in `R`
because `Q cap R` is empty.  Hence `D_y subseteq Q cap S`.  Finally, a
common-contact vertex is adjacent to `x`, so it cannot lie in `L`; it too
lies in `S`.  These observations prove (3.1)--(3.2), and therefore items
2 and 3.  The last assertion is Lemma 2.1 applied to the crossing star.
\(\square\)

#### Independent finite audit

The local assertion was also checked exhaustively (this check is not used
in the proof).  Label the support by `x,y,q0,q1,q2,q3`.  Each `qj` was
assigned to `D_x`, `D_y`, or the common-contact set, with both defect sets
required nonempty.  This gives 50 labelled defect patterns.  For each
pattern all `3^6` assignments of the six vertices to `L,S,R` were tested,
retaining only assignments which meet both shores and have no host edge
from `L` to `R`.  There are 440 retained assignments.  In every one,
exactly one complement-star component crosses the shores, the other lies
wholly in `S`, and every vertex outside the crossing component lies in
`S`.  There were zero failures.  The SHA-256 digest of the sorted retained
records in the format `defect-labels:shore-labels` is

```text
f12d66d2f0653664e766a9d1b27acdd184d7cf9c42866035cf76fdac20cab52b
```

Thus a model does not cross an adhesion through an arbitrary collection
of portals.  It crosses through one canonical complement-star component.
Any exchange theorem which refers only to a selected endpoint of a split
edge is not representation invariant when that component is `K_2`.

### Corollary 3.2 (the exact residue after a one-edge bad contraction)

Let three irredundant support-six models be named.  Suppose contraction of
one named split edge yields, on expansion, an actual exact-seven
separation which carries the hit model in a closed shore.  Then each of
the other two named models is either also contained in one closed shore,
or has precisely the cross-star trace of Theorem 3.1.  There is no third
kind of failure of model preservation.

#### Proof

Apply Theorem 3.1 separately to every named support which is not contained
in a closed shore.  \(\square\)

## 4. The anchored rank supplied by separator submodularity

The next theorem records the rank which is safe under repeated exact-seven
handoffs.  It must retain literal roots and the side assignment of every
named model.

Fix disjoint nonempty vertex sets `X,Y` and named supports
`W_1,...,W_m`, together with a side map

\[
                       epsilon:[m]\longrightarrow\{L,R\}. \tag{4.1}
\]

For a positive integer `k`, call an exact-`k` separation `(A,B)`
**admissible** when

\[
 X\subseteq A-B,\qquad Y\subseteq B-A,                 \tag{4.2}
\]

and `W_i subseteq A` for `epsilon(i)=L`, while `W_i subseteq B` for
`epsilon(i)=R`.

### Theorem 4.1 (anchored model-preserving uncrossing)

Let `G` be `k`-connected.  If `(A,B)` and `(C,D)` are admissible
exact-`k` separations for the same data `(X,Y,epsilon)`, then

\[
             (A\cap C,\ B\cup D),\qquad
             (A\cup C,\ B\cap D)                      \tag{4.3}
\]

are also admissible exact-`k` separations.

In particular, if the left open shores of the two separations are not
nested, the first separation in (4.3) has a left open shore properly
contained in both.  Therefore

\[
                         r(A,B)=|A-B|                  \tag{4.4}
\]

is a strict well-founded rank on an anchored, model-side-preserving
handoff class.  A minimum-rank member cannot be crossed by another member
of the same class.

#### Proof

The two pairs in (4.3) are the meet and join in the separation lattice.
The order function is submodular, so their orders have sum at most

\[
                         |A\cap B|+|C\cap D|=2k.       \tag{4.5}
\]

The roots in (4.2) lie in opposite open shores of both pairs in (4.3).
Thus both are actual separations.  `k`-connectivity makes each order at
least `k`; (4.5) makes both orders exactly `k`.

If `epsilon(i)=L`, then `W_i subseteq A cap C`; if `epsilon(i)=R`, then
`W_i subseteq B cap D`, which is contained in both right sides displayed
in (4.3).  Hence the meet is model preserving.  The join is model
preserving by the symmetric containments `W_i subseteq A union C` and
`W_i subseteq B cap D`.  The root conditions are already preserved, so
both separations are admissible.

The left open shore of the meet is

\[
        (A\cap C)-(B\cup D)=(A-B)\cap(C-D).            \tag{4.6}

\]

It is nonempty because it contains `X`.  If the original left shores are
not nested, (4.6) is a proper subset of each.  This proves the strict
rank assertion.  \(\square\)

The theorem also states the exact limitation of the rank.  If literal
roots or model-side assignments are allowed to change, a shore-swapping
involution can produce a two-cycle with all unanchored numerical data
unchanged.  Consequently an arbitrary exact-seven separation is not a
ranked output.

## 5. Exact remaining exchange lemma

Combine Corollary 3.2 with Theorem 4.1.  A one-edge minimal bad
contraction already gives an exact-seven separation carrying its hit
model.  To turn it into an accepted three-model receiver it is necessary
and sufficient to eliminate at most two canonical cross-star traces.

The next theorem must have the following form.

> **Anchored cross-star exchange target.**  Let `(A,B)` be an exact-seven
> separation obtained from a named split-edge contraction, with fixed
> literal roots `X subseteq A-B`, `Y subseteq B-A`.  Let a second named
> irredundant support have a cross-star trace.  Then either:
>
> 1. `G` contains a literal `K_7` model;
> 2. one literal pair meets every support-at-most-six `K_5` model;
> 3. the crossed support can be replaced by a named model contained in one
>    closed shore; or
> 4. there is another exact-seven separation with the same roots and the
>    same assignments for every already carried model, whose appropriate
>    corner with `(A,B)` has a strictly smaller rooted open shore.

Outcome 4 is genuinely ranked by Theorem 4.1.  A separator with changed
roots, reversed shores, a changed named support, or no declared model-side
map is not a valid substitute.

Theorems 3.1 and 4.1 do not prove this target.  They show precisely what
is left to move and precisely which output would be well founded.  Minimal
bad contraction alone supplies neither: contracting the crossing row moves
one open-shore vertex into the quotient boundary, but lifting that
separator back has order eight, not seven.  Proper-minor colouring supplies
an equality at the contracted row, but does not by itself preserve the two
literal roots or the named side assignments.

This is the first exact gap in a simultaneous three-row contraction proof.
It is narrower than a general rooted-model theorem: there are at most two
crossing supports, and each crossing is one canonical defect star of a
six-vertex model.

## 6. Falsification guardrail

The need for anchoring is not formalism.  Let `P` be obtained from two
copies of the icosahedron with one vertex deleted by identifying their
five-cycle boundaries, and put `J=K_2 join P`.  Then `J` is
seven-connected and `K_7`-minor-free; the two join vertices meet every
`K_5` model.  The common `K_2` together with the identified five-cycle is
an exact seven-boundary, and the two cap shores are exchanged by an
automorphism.  Three separated literal `K_5` supports are obtained from
the join pair and facial triangles.

Thus every isomorphism-invariant quantity depending only on unlabelled
shore orders, crossing-support counts, or crossing types takes the same
value after the shore swap.  It cannot strictly decrease in both
directions.  This example is terminal by its coherent join pair, so it
does not refute the target above; it proves that pair detection must occur
before descent and that the descent must retain the anchors in Theorem
4.1.

## 7. A synchronized ranked bundle for a three-edge contraction circuit

There is one place where the proved one-split/two-clique theorem applies
automatically and its transversal alternative disappears entirely.  This
gives a genuine ranked object, although in three predecessor minors rather
than an actual exact-seven separation of the original graph.

### Theorem 7.1 (three-predecessor synchronization)

Let `G` be seven-connected and `K_7`-minor-free.  Let
`M_1,M_2,M_3` be pairwise vertex-disjoint irredundant support-six models,
with split edges

\[
                         e_i=x_i y_i\quad(i=1,2,3).     \tag{7.1}
\]

Suppose that `F={e_1,e_2,e_3}` is inclusion-minimal subject to `G/F` not
being seven-connected.  Put

\[
 H=G/F,\qquad J_i=G/(F-\{e_i\}),                       \tag{7.2}
\]

and write `z_i` for the image of `e_i` in `H`.  Then:

1. `H` is six-connected.  Every six-separator `T` of `H` contains
   `z_1,z_2,z_3`; deleting `T` has exactly two components.
2. For every such `T` and every `i`,

   \[
                S_i=(T-\{z_i\})\cup\{x_i,y_i\}       \tag{7.3}
   \]

   is an exact-seven boundary in the seven-connected predecessor `J_i`.
   It carries all three named models in closed shores: `M_i` is the one
   split model, and the other two models are literal `K_5` cliques in
   `J_i`.
3. The global-pair outcome of the one-split/two-clique trichotomy is
   impossible in every `J_i`.  Thus, in a `K_7`-minor-free host, (7.3) is
   the compulsory outcome of that trichotomy.
4. The three exact-seven separations in (7.3) have one common side map:
   it is the side map of the three quotient cliques in the two components
   of `H-T`.  Fix one literal root in each component.  Among six-cuts of
   `H` preserving those roots and that side map, open-shore order is the
   strict well-founded rank of Theorem 4.1.  Every crossing replacement
   cut gives, simultaneously in all three predecessors, a strictly
   smaller ranked bundle.

#### Proof

The minimal-bad-contraction theorem gives item 1 except for the number of
components: `H` is six-connected, every six-cut contains all three
contracted images, and three or more components give a literal `K_7`
model in `G`.  Hence exactly two components remain.

Minimality of `F` makes every `J_i` seven-connected.  Replacing `z_i` in
`T` by the two ends of `e_i` gives (7.3), of order seven, and leaves the
same two open components.  In `J_i`, the model `M_i` is still split while
the other two named models have become literal `K_5` cliques.  Their
supports remain pairwise disjoint.  Every quotient clique has all its
vertices outside `T` in at most one component, so expansion places each
named carrier in one closed shore.  This proves item 2.

The hypotheses of the one-split/two-clique theorem hold in `J_i`: the two
literal cliques are disjoint from `e_i`, and all three quotient
intersections are zero.  Its first outcome would be a `K_7` minor in
`J_i` and hence in `G`.  Its second outcome would be a two-set meeting
every support-at-most-six `K_5` model in `J_i`.  But the two literal
cliques and the disjoint support of `M_i` are three pairwise disjoint
members of that support family.  No two-set meets all three.  Thus only
the exact-seven outcome remains, proving item 3 without any pullback of a
quotient transversal.

For every named quotient clique, its vertices outside `T` lie in one of
the same two components of `H-T`; the choice is independent of `i`.
This is the common side map.  Choose roots `a,b` in the two components.
Apply Theorem 4.1 with `k=6` in `H`, retaining the three literal quotient
cliques and their side map.  A crossing admissible six-cut uncrosses to a
six-cut with a strictly smaller `a`-side.  Lifting that cut by (7.3) in
each `J_i` preserves all three models and the same strict rank.  This
proves item 4.  \(\square\)

### Exact limit

Theorem 7.1 resolves two logical questions cleanly.

* In a minimal bad set of three rows, the one-split theorem's global pair
  does not need to be pulled through the two earlier contractions: it is
  impossible before pullback.
* The three predecessor handoffs are not unrelated separators.  They are
  synchronized lifts of one six-cut and admit a branch-bag-anchored rank.

It does **not** yet close the size-three circuit.  Expanding both earlier
contractions in (7.3) produces the pointwise-full order-nine boundary in
the original graph, not an exact-seven boundary.  The rank is therefore a
ranked predecessor bundle, not by itself an accepted receiver in `G`.
The missing composition mechanism must either use the three synchronized
proper-minor states on this one bundle, or turn a new admissible six-cut
into a strict corner in the sense of item 4.  A minimal bad set of order
two also lies outside Theorem 7.1 because its predecessor still contains
two split models rather than one.

## 8. The punctured-cube invariant on the common deletion

Strong contraction-criticality adds one simultaneous invariant which is
not visible from separator geometry alone.

### Theorem 8.1 (three-row punctured cube and chromatic fork)

Let `G` be strongly seven-contraction-critical and let

\[
                         F=\{e_1,e_2,e_3\}             \tag{8.1}
\]

be a matching.  Put `K=G-F`, where the three edges are deleted rather
than contracted.

1. For every nonempty set `C subseteq F`, the graph `K` has a
   six-colouring in which the ends of `e` have the same colour exactly
   for `e in C`, and have different colours for `e in F-C`.
   No six-colouring of `K` makes all three pairs different.  Thus every
   vertex of the Boolean three-cube except the all-proper vertex is
   realized exactly.
2. `chi(K)>=4`.  If `chi(K)=4`, the six endpoints of `F` induce a literal
   `K_6` in `G`.
3. Consequently, if `G` is also seven-connected and `K_7`-minor-free,
   then

   \[
                              \chi(K)\in\{5,6\}.       \tag{8.2}
   \]

4. In the five-chromatic branch, the graph induced by the six endpoints
   has no independent transversal of the three pairs.

#### Proof

For nonempty `C`, the contraction `G/C` is a proper minor and hence has a
six-colouring.  Expand every contracted vertex after deleting the edges
of `F`.  The ends of every edge in `C` receive the same colour.  Every
edge in `F-C` is still present in `G/C`, so its ends receive different
colours.  This gives the exact signature in item 1.  Conversely, an
all-proper six-colouring of `K` would already be a six-colouring of `G`,
which is impossible.

If `K` were three-colourable, choose one endpoint of each deleted edge
and give those three selected vertices three distinct fresh colours.
Leave all other colours unchanged.  This restores every edge of `F` and
gives a six-colouring of `G`, a contradiction.  Hence `chi(K)>=4`.

Now fix a four-colouring of `K`, and choose arbitrarily one endpoint from
each of the three deleted edges.  If the selected three vertices did not
induce a triangle, their induced graph would be two-colourable.  Recolour
them with two fresh colours according to such a two-colouring.  All their
neighbours retaining old colours are safe, the three deleted matching
edges are restored with differently coloured ends, and edges among the
selected vertices are proper.  This would again six-colour `G`.

Therefore every transversal of the three endpoint pairs is a triangle.
Given endpoints `u` and `v` from two different pairs, extend them by
either endpoint of the third pair.  The resulting transversal triangle
contains `uv`.  Hence all cross-edges between distinct pairs are present;
together with the three matching edges, the six endpoints induce `K_6`.
This proves item 2.

If `G` is seven-connected, deleting the six clique vertices leaves a
nonempty connected graph, and every clique vertex has a neighbour in that
remainder.  The six singleton clique bags together with the connected
remainder form a `K_7` model.  Thus the four-colour branch is impossible
in a `K_7`-minor-free host.  Since `K` is a proper subgraph of `G`, strong
contraction-criticality gives `chi(K)<=6`, proving (8.2).

Finally, in a five-colouring of `K`, an independent transversal of the
three endpoint pairs could be recoloured with one fresh common colour,
again restoring all three deleted edges and six-colouring `G`.  No such
transversal exists.  \(\square\)

### Consequence for the size-three contraction circuit

In Theorem 7.1 the common deletion of the three split rows is therefore an
exact five- or six-chromatic host carrying all seven nonterminal row
signatures.  The remaining composition question is no longer to obtain
three compatible proper-minor responses: all of them already exist on one
literal graph.  It is to convert this punctured cube, together with the
three synchronized predecessor separations, into the missing all-proper
state, a `K_7` model, a coherent two-vertex transversal, or a strict
anchored cut.  Abstract signature existence alone does not perform that
conversion.
