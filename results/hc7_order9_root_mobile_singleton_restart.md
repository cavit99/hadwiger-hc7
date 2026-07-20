# Root-mobile singleton restarts across two boundary-full shores

**Status:** written proof; separate internal audit GREEN in
[`hc7_order9_root_mobile_singleton_restart_audit.md`](hc7_order9_root_mobile_singleton_restart_audit.md).

This note records a consequence of having two anticomplete connected open
shores which are each adjacent to every literal boundary vertex.  Every
boundary vertex can be made the unique boundary vertex of one colour on
either closed shore.  At a nine-vertex boundary this gives a copy of the
audited five-colouring reconfiguration problem rooted at every boundary
vertex, rather than only at the originally selected exact colour class.

The conclusion is a family of restarts, not a common boundary colouring or
a proof of `HC_7`.

## 1. Setting

Let

\[
 V(G)=A\mathbin{\dot\cup}B\mathbin{\dot\cup}D,
 \qquad A,D\ne\varnothing,
 \qquad E_G(A,D)=\varnothing,                         \tag{1.1}
\]

where `G[A]` and `G[D]` are connected.  Assume that every literal vertex of
`B` has a neighbour in `A` and a neighbour in `D`.  Assume also that

\[
 K_7\not\preccurlyeq G,
 \qquad \chi(G)>6,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G. \tag{1.2}
\]

## 2. Every deleted boundary vertex leaves a `K_5`-minor-free graph

### Lemma 2.1

For every `s in B`, the boundary graph `G[B-{s}]` has no `K_5` minor.

#### Proof

Suppose that `M_1,...,M_5` is a `K_5`-minor model in `G[B-{s}]`.
The seven sets

\[
             A\cup\{s\},\qquad D,\qquad M_1,\ldots,M_5             \tag{2.1}
\]

are pairwise disjoint and connected.  The first two are adjacent because
`s` has a neighbour in `D`.  Each of them is adjacent to every `M_i`, since
both open shores have a neighbour at every boundary vertex.  The last five
sets are pairwise adjacent by their definition.  Thus (2.1) is an explicit
`K_7`-minor model, contrary to (1.2).  \(\square\)

## 3. Exact singleton traces rooted at every boundary vertex

### Lemma 3.1

For every `s in B`, each closed shore has a proper six-colouring in which
`{s}` is exactly one boundary colour class.

#### Proof

Contract a spanning tree of the connected graph `G[D union {s}]` to one
vertex `z`.  This is a proper minor: `D` is nonempty and `s` has a neighbour
in `D`.  By (1.2), the minor has a proper six-colouring.

The vertex `z` is adjacent to every vertex of `B-{s}`, through the
boundary-full subgraph `D`.  Its colour is consequently absent from
`B-{s}`.  Discard the contracted image of `D`, retain the colouring on
`G[A union (B-{s})]`, and give the literal vertex `s` the colour of `z`.
Every edge incident with `s` on this retained closed shore was represented
by an edge incident with `z` in the minor.  The expansion is therefore a
proper colouring of `G[A union B]`, and `{s}` is exactly the boundary colour
class of the colour of `z`.

Contracting `A union {s}` instead gives the symmetric colouring of
`G[D union B]`.  \(\square\)

The two boundary traces in Lemma 3.1 need not be the same partition.  In
fact, no complete boundary trace can extend through both closed shores:
after a permutation of colour names, the two extensions would agree on
`B` and would glue across (1.1) to a six-colouring of `G`.

## 4. A reconfiguration restart at every root

### Theorem 4.1

Assume in addition that `|B|=9`.  Fix any `s in B` and put

\[
                              H_s=G[B-\{s\}].          \tag{4.1}
\]

Boundary colourings in which `{s}` is exactly one colour class correspond,
after naming that colour six, to proper five-colourings of `H_s`, with
unused colours allowed.  The sets of such colourings extending through the
two closed shores are nonempty and disjoint.

Moreover, a shortest path between the two extension sets has exactly one of
the following forms.

1. Two oppositely extendable boundary traces differ at one literal vertex.
   The host-level one-vertex transition then gives a bichromatic obstruction
   path through each open shore, with disjoint interiors.
2. One boundary trace extends through neither closed shore.  It gives a
   connected vertex-minimal list-colouring obstruction in each open shore.

#### Proof

Lemma 2.1 says that `H_s` is `K_5`-minor-free and has eight vertices.
The audited order-eight full reconfiguration theorem therefore says that
the graph `R_5(H_s)` of all proper five-colourings under one-vertex
recolourings is connected.  Lemma 3.1 makes the two shore-extension sets
nonempty, and the gluing observation after that lemma makes them disjoint.

Choose a shortest path in `R_5(H_s)` between the two extension sets.  If it
has one edge, its endpoints are the traces in outcome 1.  The host-level
consequence of the reconfiguration theorem supplies the two stated paths.

If the shortest path has at least two edges, any internal vertex of the
path extends through neither shore.  Otherwise it would give a shorter
path from one extension set to the other.  Restricting the fixed boundary
trace to either open shore gives an uncolourable list assignment; an
induced vertex-minimal uncolourable subgraph is connected.  This is outcome
2.  \(\square\)

Thus every literal boundary vertex supplies a fresh one-step-or-paired-core
fork.  The theorem does not assert that the forks for different roots use
the same proper-minor colouring, the same obstruction paths, or the same
minor-model branch sets.

## 5. Pairwise overlap of the root systems

### Proposition 5.1

For every two distinct vertices `s,t in B`, there is a proper boundary
colouring using all six colours in which `{s}` and `{t}` are two distinct
singleton colour classes.

#### Proof

By Lemma 2.1, `G[B-{s}]` is `K_5`-minor-free.  The known case `HC_5` makes
it four-colourable, and hence so is its induced subgraph `G[B-{s,t}]`.
This graph has seven vertices.  Starting with any proper colouring using at
most four colours, repeatedly split a colour class of order at least two by
giving one of its vertices a previously unused colour.  This produces a
proper colouring using exactly four colours.

Give `s` and `t` two new distinct colours.  The resulting boundary
colouring uses all six colours and has the claimed singleton classes.
\(\square\)

Consequently, if every full exact-`s` trace happened to extend through one
fixed shore and every full exact-`t` trace happened to extend through one
fixed shore, those two shores would have to be the same: the trace from
Proposition 5.1 belongs to both exact-root families.  Rootwise constant
orientations cannot disagree.

## 6. A static barrier to extracting more from overlap alone

Pairwise overlap is not a gluing principle, even if one assumes more static
extension data than Lemma 3.1 supplies.

Let `B` be an independent set of order nine.  Consider its full labelled
six-colour traces and declare a trace to have type `A` when its multiset of
colour-class orders is

\[
                         (4,1,1,1,1,1),               \tag{6.1}
\]

and type `D` for every other full trace.  This rule is invariant under every
permutation of the six colour names, and every full trace has exactly one
type.

For every root `s`, there are traces of both types in which `{s}` is a
singleton class.  More strongly, for every pair `s,t`, there are traces of
both types in which `{s}` and `{t}` are distinct singleton classes:

- for type `A`, put four of the other seven vertices in one class and make
  the remaining vertices singleton classes;
- for type `D`, use three two-vertex classes and three singleton classes,
  choosing `s,t` among the singleton vertices.

Hence even complete pairwise overlap, both orientations at every root, and
colour-permutation invariance do not force a trace with both orientations.
This is an abstract boundary-language barrier, not a pair of actual shores:
it does not encode seven-connectivity, `K_7`-minor exclusion, or the
operation-specific colourings of Lemma 3.1.

The next valid use of root mobility must therefore couple two roots through
one literal host operation, a shared first-hit configuration, or a common
full-neighbourhood separator.  Static overlap of the exact-root languages
is insufficient.

## 7. Dependencies and exact limitation

- the known case `HC_5`, only in Proposition 5.1;
- the audited
  [order-eight full five-colouring reconfiguration theorem](../results/hc7_order8_full_five_colour_reconfiguration.md),
  including its host-level shortest-path consequence.

The note does not construct a `K_7` minor beyond the deletion argument in
Lemma 2.1, produce a boundary trace extending both shores, align palette
colours with inherited branch-set labels, or reduce a returned order-eight
interface to order seven.
