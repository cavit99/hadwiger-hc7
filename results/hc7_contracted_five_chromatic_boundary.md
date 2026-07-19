# A five-chromatic boundary after contracting the distinguished edge

**Status:** written proof; separate internal audit GREEN in
[`hc7_contracted_five_chromatic_boundary_audit.md`](hc7_contracted_five_chromatic_boundary_audit.md).
This theorem
identifies the only five-chromatic boundary in the contracted
boundary-full interface and reduces it to a planar graph with one vertex
split.  It does not prove `HC_7`.

## 1. Setting

Let `H` be a six-connected graph with no `K_7` minor.  Let `S` be a set of
seven vertices, and suppose that `A,D` are distinct components of `H-S`
such that

\[
                         N_H(A)=N_H(D)=S.                \tag{1.1}
\]

Put `F=H[S]`.  The intended application is obtained from a hypothetical
minor-minimal counterexample `G` to `HC_7` by contracting an edge `pv` to a
vertex `x`.  The exact order-seven interface (1.1) is supplied by the
[augmented full-component contraction
reduction](hc7_augmented_full_component_contraction_reduction.md).

## 2. The boundary is four-degenerate

### Lemma 2.1 (deleting a boundary vertex excludes a `K_5` minor)

For every `s in S`,

\[
                         K_5\not\preccurlyeq F-s.        \tag{2.1}
\]

#### Proof

Suppose that `Q_1,...,Q_5` are the branch sets of a `K_5`-minor model in
`F-s`.  Then

\[
                  A\cup\{s\},\qquad D,\qquad
                  Q_1,\ldots,Q_5                         \tag{2.2}
\]

are seven pairwise disjoint connected sets.  The first set is connected
because `A` has a neighbour at `s`.  It is adjacent to `D` through an edge
from `s` to `D`.  Each of `A` and `D` is adjacent to every `Q_i`, because
each `Q_i` contains a literal vertex of `S` and (1.1) gives a neighbour at
that vertex.  The five sets `Q_i` are pairwise adjacent by hypothesis.
Thus (2.2) is a `K_7`-minor model in `H`, a contradiction. \(\square\)

### Lemma 2.2 (four-degeneracy)

The graph `F` is four-degenerate.  Consequently, assuming the established
case `HC_5`,

\[
                              \chi(F)\le5.               \tag{2.3}
\]

#### Proof

We first record the elementary six-vertex density fact used below.  A graph
`J` on six vertices with at least thirteen edges has a `K_5` minor.  Indeed,
its complement has at most two edges.  With at most one missing edge,
deleting a suitable endpoint leaves a `K_5`.  If two missing edges share
an endpoint, deleting that common endpoint leaves a `K_5`.  If the missing
edges are disjoint, say `ab` and `cd`, then

\[
                         \{a,c\},\{b\},\{d\},\{e\},\{f\} \tag{2.4}
\]

are the branch sets of a `K_5` minor: `ac` is an edge, and the only two
missing adjacencies are supplied from the other member of the first branch
set.

By Lemma 2.1, every six-vertex graph `F-s` therefore has at most twelve
edges.

Suppose that `F` is not four-degenerate, and let `T` be an induced subgraph
of minimum degree at least five.  Then `|T|` is six or seven.  If `|T|=6`,
then `T=K_6`; choosing the seventh vertex `s` makes `F-s` contain a `K_5`,
contrary to Lemma 2.1.  Hence `T=F`.  Minimum degree at least five gives
`e(F)>=18`, whereas

\[
             5e(F)=\sum_{s\in S} e(F-s)\le 7\cdot12=84, \tag{2.5}
\]

because each edge of `F` occurs in exactly five of the seven vertex-deleted
graphs.  Thus `e(F)<=16`, a contradiction.  This proves four-degeneracy.

For any `s in S`, Lemma 2.1 and `HC_5` give `chi(F-s)<=4`.  Colour `F-s`
with four colours and give `s` a fifth colour to obtain (2.3). \(\square\)

## 3. Classification of the five-chromatic boundary

### Lemma 3.1

If `chi(F)=5`, then

\[
                              F\cong K_2\vee C_5.        \tag{3.1}
\]

#### Proof

Lemma 2.2 and the assumption `chi(F)=5` show that `F-s` is
four-colourable for every `s`.  Thus `F` is vertex-critical and
five-chromatic.  In particular `delta(F)>=4`.  Set `R=overline F`.  Then
`Delta(R)<=2`, so every component of `R` is a path, a cycle, or an isolated
vertex.

A proper colouring of `F` is the same thing as a partition of `V(R)` into
cliques.  Let `theta(J)` be the minimum number of cliques partitioning
`V(J)`, and define

\[
                         \sigma(J)=|V(J)|-\theta(J).     \tag{3.2}
\]

The criticality statements above say

\[
                         \sigma(R)=7-5=2,
               \qquad \sigma(R-s)\ge6-4=2              \tag{3.3}
\]

for every `s`.  The parameter `sigma` is additive over components.

For paths,

\[
                       \sigma(P_n)=\lfloor n/2\rfloor, \tag{3.4}
\]

because a clique in a path has at most two vertices and a maximum matching
gives an optimal clique partition.  For cycles of order at least four,

\[
                       \sigma(C_n)=\lfloor n/2\rfloor. \tag{3.5}
\]

Also `sigma(C_3)=2`, and an isolated vertex has saving zero.  Hence the
connected components with saving one are `P_2,P_3`, while those with
saving two are

\[
                         P_4,P_5,C_3,C_4,C_5.           \tag{3.6}
\]

Every longer path or cycle has saving at least three.

Since the total saving is two, either `R` has two components of saving one,
or it has one component from (3.6), with every other component isolated.
The first possibility contradicts the deletion condition in (3.3): in one
of the two saving-one components, delete an endpoint of `P_2` or the middle
vertex of `P_3`; that component then has saving zero and the total saving
drops to at most one.

The same deletion test excludes every graph in (3.6) except `C_5`:

- deleting an endpoint of `P_4` leaves `P_3`, of saving one;
- deleting a vertex next to an endpoint of `P_5` leaves `P_3` and an
  isolated vertex, of total saving one;
- deleting any vertex of `C_3` leaves `P_2`, of saving one;
- deleting any vertex of `C_4` leaves `P_3`, of saving one; while
- deleting any vertex of `C_5` leaves `P_4`, whose saving is still two.

It follows that

\[
                             R\cong C_5\mathbin{\dot\cup}2K_1.       \tag{3.7}
\]

The complement of `C_5` is again `C_5`, and the two isolated vertices of
`R` become adjacent universal vertices of `F`.  Taking complements in
(3.7) proves (3.1). \(\square\)

## 4. The five-chromatic boundary has exactly two complementary components

Assume `chi(F)=5`.  Write

\[
                 S=\{a,b\}\mathbin{\dot\cup}V(C),
                 \qquad C=c_0c_1c_2c_3c_4c_0,          \tag{4.1}
\]

where `a,b` are adjacent and complete to the induced cycle `C`.

### Lemma 4.1

The graph `H-S` has exactly the two components `A,D`.

#### Proof

Suppose that `E` is a third component.  Since `H` is six-connected and
`N_H(E) subseteq S`, the component `E` has neighbours at at least six of
the seven boundary vertices.  Thus it misses at most one member of `S`.

First suppose that the possible missed vertex is `c_i`.  Indices below are
modulo five.  The seven sets

\[
 \begin{aligned}
   &E\cup\{c_{i-1}\},qquad
    A\cup\{c_{i+2}\},qquad
    D\cup\{c_{i+3}\},\\
   &\{c_i\},\qquad \{c_{i+1}\},qquad \{a\},\qquad \{b\}
 \end{aligned}                                         \tag{4.2}
\]

form a `K_7`-minor model.  The three nonsingleton sets are connected.
The two full components `A,D` supply all their required adjacencies.  The
component `E` is adjacent to every displayed boundary vertex except
possibly `c_i`; its branch set is adjacent to `c_i` through the cycle edge
`c_{i-1}c_i`.  Finally the four singleton vertices
`c_i,c_{i+1},a,b` form a clique.

If the possible missed vertex is `a`, `b`, or no vertex, choose any cycle
edge, say `c_0c_1`.  The seven sets

\[
       E\cup\{c_2\},\quad A\cup\{c_3\},\quad D\cup\{c_4\},
       \quad\{c_0\},\quad\{c_1\},\quad\{a\},\quad\{b\}             \tag{4.3}
\]

again form a `K_7`-minor model.  If `E` misses one of `a,b`, its branch set
is still adjacent to that singleton through `c_2`, since both universal
vertices are adjacent to every cycle vertex.  Every other adjacency is
supplied by boundary fullness, by a cycle edge, or by the join in (4.1).

Both (4.2) and (4.3) contradict the exclusion of a `K_7` minor.  Hence no
third component exists. \(\square\)

## 5. A planarizing pair in the contracted graph

We use Lemma 3.1 of Anders Martinsson and Raphael Steiner,
*Strengthening Hadwiger's conjecture for 4- and 5-chromatic graphs*,
Journal of Combinatorial Theory, Series B 164 (2024), 1--16,
<https://doi.org/10.1016/j.jctb.2023.08.009>:

> If `J` is three-connected, `R subseteq V(J)` has order at least four and
> is spread out across every order-three separation of `J`, and `J` has no
> `R`-rooted `K_4` minor, then adding one new vertex adjacent to every
> member of `R` produces a planar graph.

Here a set is spread out if neither side of an order-three separation
contains the whole set.

### Theorem 5.1 (contracted two-apex conclusion)

Under (4.1),

\[
                              H-\{a,b\}\text{ is planar}.            \tag{5.1}
\]

#### Proof

Put `P=H-{a,b}`.  Since `H` is six-connected, `P` is four-connected.
Define

\[
                         J_A=H[A\cup V(C)],
                  \qquad J_D=H[D\cup V(C)].             \tag{5.2}
\]

We verify the Martinsson--Steiner hypotheses for `J_A`; the proof for
`J_D` is identical.

First, `J_A` is three-connected.  Let `Z subseteq V(J_A)` have order at
most two.  Every component of `J_A-Z` meets `C-Z`: otherwise such a
component lies in `A` and has all its neighbours in `P` contained in `Z`,
contrary to four-connectivity of `P`.  If `Z` contains a vertex of `A`, at
most one cycle vertex is deleted and `C-Z` is connected.  If `Z subseteq
V(C)`, the connected graph `A` is untouched and has a neighbour at every
remaining cycle vertex, so it joins all components of `C-Z`.  Thus
`J_A-Z` is connected.

Second, `V(C)` is spread out across every order-three separation of `J_A`.
If one side contained all of `C`, the nonempty part of the other open side
would lie in `A` and would have all its neighbours in `P` contained in the
three-vertex separator: there are no edges from `A` to `D` by Lemma 4.1.
This contradicts four-connectivity of `P`.

If `J_A` has a `V(C)`-rooted `K_4` model with branch sets
`M_1,...,M_4`, then

\[
                         M_1,\ldots,M_4,D,\{a\},\{b\}                 \tag{5.3}
\]

are the branch sets of a `K_7` minor in `H`.  The component `D` is
adjacent to each `M_i` at a cycle vertex in that branch set and is adjacent
to `a,b`; the universal vertices `a,b` are adjacent to each other and to
every `M_i`.  Thus no such rooted model exists.  The same argument excludes
a rooted `K_4` in `J_D`.

Martinsson--Steiner Lemma 3.1 now says that adding a new vertex complete to
`C` makes each of `J_A,J_D` planar.  In either embedding the new vertex
together with `C` is a wheel.  The connected open component lies in one
face of this wheel.  It cannot lie in a triangular face incident with the
new vertex: it has no edge to that artificial vertex and is adjacent to
all five cycle vertices, whereas such a face has only two cycle vertices
on its boundary.  Hence it lies in the face on the opposite side of `C`.
Deleting the artificial vertex gives a planar disc embedding with `C` as
the boundary.

Reflect one of the two disc embeddings and identify their copies of `C`.
By Lemma 4.1 there are no further components, and there is no edge between
`A` and `D`.  The result is a planar embedding of `P`, proving (5.1).
\(\square\)

## 6. What lifts to the original graph

Assume now that `G` is not six-colourable, `pv in E(G)`, and `H=G/pv`.
Let `x` denote the contraction image.  Every proper six-colouring of `H`
expands to a proper six-colouring of `G-pv` in which `p,v` have the same
colour.  We shall use the following elementary critical-edge observation.

### Lemma 6.1 (split-edge colour saturation)

In every such colouring, each of `p,v` has a neighbour in every other
colour class.

#### Proof

If, for example, `p` had no neighbour of a colour different from its own,
recolouring `p` with that colour would make `p,v` different and would
permit the edge `pv` to be restored.  This would six-colour `G`, a
contradiction.  The argument for `v` is identical. \(\square\)

### Corollary 6.2 (the lifted split-planar normal form)

Let `U={a,b}` be the universal pair from (4.1).

1. If `x notin U`, then

   \[
                         pa,pb,va,vb\in E(G).            \tag{6.1}
   \]

   The graph `G-U` is obtained by splitting `x` into the adjacent vertices
   `p,v` in the planar graph `H-U`.  Every `K_5`-minor model in `G-U` uses
   `p` and `v` in two distinct branch sets.

2. If `x=a` (the case `x=b` is symmetric), then

   \[
                      G-\{p,v,b\}=H-\{x,b\}\text{ is planar},
             \qquad pb,vb\in E(G).                       \tag{6.2}
   \]

   Every `K_5`-minor model in `G-{p,b}` contains `v`, and every
   `K_5`-minor model in `G-{v,b}` contains `p`.

If in addition `chi(G)=7`, all three assertions about `K_5` models are
nonvacuous: deleting two vertices leaves chromatic number at least five,
and `HC_5` supplies a `K_5` minor.

#### Proof

Four-colour the planar graph `H-U`.  If `x notin U`, give `a,b` two new,
distinct colours.  This is a six-colouring of `H` in which the two new
colours occur only at `a,b`.  Expand it to `G-pv`.  Lemma 6.1 forces both
`p` and `v` to see both unique colours, proving (6.1).

The first sentence of item 1 is now immediate from the definition of edge
contraction.  Let `M` be a `K_5`-minor model in `G-U`.  If at most one of
`p,v` belongs to its branch sets, contracting `pv` preserves the five
disjoint connected branch sets.  The same is true if both vertices belong
to one branch set.  Either event would give a `K_5` minor in the planar
graph `H-U`.  Hence `p,v` occur in distinct branch sets of every such
model.

Suppose next that `x=a`.  Four-colour `H-{x,b}`, give `x,b` two unique new
colours, and expand to `G-pv`.  Lemma 6.1 applied to the unique colour at
`b` gives `pb,vb in E(G)`.  Deleting the contracted vertex `x` corresponds
to deleting both `p,v`, so the planar identity in (6.2) holds.  A `K_5`
model in `G-{p,b}` which avoided `v` would lie in the planar graph
`G-{p,v,b}`; hence every such model contains `v`.  The symmetric argument
gives the assertion for `G-{v,b}`.

Finally, `chi(G-Q)>=chi(G)-|Q|>=5` for every two-set `Q`.  The established
case `HC_5` therefore makes each relevant two-vertex deletion contain a
`K_5` minor. \(\square\)

## 7. Exact scope and remaining gap

Theorem 5.1 is a planarizing-pair theorem in the **contracted graph** `H`.
It does not say that `G-U` is planar.  Undoing an edge contraction is a
vertex split, and a vertex split need not preserve planarity; the elementary
example `K_5/e\cong K_4` already prevents that inference.

Thus the five-chromatic boundary is not yet eliminated.  In the intended
hypothetical-counterexample application, where `G` is seven-connected, the
case `x notin U` leaves a five-connected graph `G-U` obtained by one
adjacent vertex split from the four-connected planar graph `H-U`, and every
`K_5` model uses the two split vertices in distinct branch sets.  To obtain
a `K_7` minor by adjoining `a,b`, one still needs a label-preserving theorem
which makes the other three branch sets meet the cycle `C` (or otherwise
makes both `a,b` adjacent to them).  When `x in U`, the remaining structure
is the pair of oppositely rooted `K_5`-model obligations in Corollary 6.2(2).

No common boundary colouring, `S`-meeting `K_6` model, or actual
two-vertex planarizing set in `G` is asserted here.
