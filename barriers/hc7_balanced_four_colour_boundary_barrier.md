# Balanced four-colour pullback is false; the correct obstruction is a co-Tutte barrier

**Status:** proved barrier and replacement reduction.  This note concerns
only the state-free boundary hypotheses.  It does not rule out a balanced
state after using additional contraction-critical information from either
shore.

## 1. The proposed bridge fails

Let `a,b` be nonadjacent vertices complete to a boundary graph `J`.  Thus
the two-shore quotient is `I_2 vee J`.

### Order eight

Take

\[
                              J=K_{3,5}.
\]

This graph is connected and bipartite, hence four-colourable.  Every
independent set of `J` lies wholly in one side of its bipartition.  A
partition into four independent pairs would therefore partition each of
the two odd partite sets into pairs, which is impossible.

On the other hand

\[
                         I_2\vee J=K_{2,3,5}.
\]

A complete multipartite graph on `n` vertices with largest part of order
`m` has treewidth `n-m`: the vertices outside a largest part together with
one vertex of that part give a tree decomposition of width `n-m`, while
vertex connectivity gives the reverse inequality.  Hence
`tw(K_{2,3,5})=5`.  Since a `K_7` minor requires treewidth at least six,
this quotient is `K_7`-minor-free.

Thus even connectedness, bipartiteness, and the exact join-minor exclusion
do not force a `(2,2,2,2)` proper colour partition.

### Order nine

Take

\[
                              J=K_3\vee I_6.
\]

In every proper four-colouring the three clique vertices use three distinct
colours and no one of those colours can occur on `I_6`.  The boundary
colour-class sizes are therefore `(6,1,1,1)`, not `(3,2,2,2)`.  Moreover,

\[
                      I_2\vee J=K_3\vee K_{2,6}
\]

is the complete multipartite graph with part sizes
`1,1,1,2,6`, so it again has treewidth five and no `K_7` minor.

Consequently neither order admits the proposed state-free balanced-colour
bridge.

## 2. Exact matching reformulation

The failure has a standard structural description.

### Lemma 2.1 (order eight)

An eight-vertex graph `J` has a proper colour partition of type
`(2,2,2,2)` if and only if its complement `F=overline J` has a perfect
matching.

**Proof.**  The four colour pairs are four disjoint nonedges of `J`, hence
the edges of a perfect matching in `F`, and conversely.  \(\square\)

### Lemma 2.2 (order nine)

A nine-vertex graph `J` has a proper colour partition of type
`(3,2,2,2)` if and only if `F=overline J` has a triangle `T` such that
`F-T` has a perfect matching.

**Proof.**  The three-vertex colour class is a triangle of `F`; the other
three colour pairs are a perfect matching of the remaining six vertices.
The converse is immediate.  \(\square\)

This reformulation shows that the obstruction is parity/matching structure,
not chromatic number.

## 3. The join exclusion bounds every Tutte obstruction

The two full shores do still give a useful uniform reduction.

### Lemma 3.1 (proper boundary `K_5` lift)

If `J` contains a `K_5` model supported on a proper subset of `V(J)`, then
`I_2 vee J` contains a `K_7` minor.

**Proof.**  Let `Q_1,...,Q_5` be the boundary bags and choose a boundary
vertex `s` outside their union.  If `a,b` are the two vertices of `I_2`,
then

\[
                      Q_1,\ldots,Q_5,\{a,s\},\{b\}
\]

are seven disjoint connected pairwise adjacent bags.  In particular,
`{a,s}` meets `{b}` through the edge `sb`; all other required adjacencies
use the join edges.  \(\square\)

### Proposition 3.2 (bounded co-Tutte barrier at order eight)

Suppose `|V(J)|=8`, `J` is four-colourable, `I_2 vee J` is
`K_7`-minor-free, and `J` has no `(2,2,2,2)` partition.  Then
`F=overline J` has a set `X` such that

\[
              |X|\le2,\qquad
              o(F-X)>|X|,\qquad o(F-X)\le4.             \tag{3.1}
\]

Here `o` denotes the number of odd components.

**Proof.**  By Lemma 2.1 and Tutte's theorem there is `X` with
`q=o(F-X)>|X|`.  Selecting one vertex from each of five distinct
components of `F-X` would give a `K_5` in `J`, because distinct complement
components are pairwise complete in `J`.  It would be supported on a
proper subset of the eight-vertex boundary, contradicting Lemma 3.1.
Thus `q<=4`, and `q>|X|` gives `|X|<=3`.  Parity gives

\[
                 q\equiv 8-|X|\pmod2,
\]

so `q-|X|` is positive and even.  If `|X|=3`, then `q>=5`, already
excluded.  Hence `|X|<=2`.  \(\square\)

Equivalently, after deleting at most two boundary vertices, the complement
has too many odd co-components.  Distinct co-components are joined
completely in `J`.  This is the reusable structural handoff left by an
unbalanced order-eight boundary.  The possible pairs
`(|X|,o(F-X))` are exactly among

\[
                         (0,2),(0,4),(1,3),(2,4).       \tag{3.3}
\]

There is a further colour-budget consequence.  The components of `F-X`
are pairwise completely joined in `J-X`, and hence

\[
       \chi(J-X)=\sum_{C\in\operatorname{comp}(F-X)}\chi(J[C])\le4.
                                                               \tag{3.4}
\]

In particular `F-X` has at most four components in total.  If it has four
odd components, these are all its components and every `J[C]` is
independent.  Thus `J-X` is a complete four-partite graph with four odd
parts.  The other outcomes are likewise complete joins of at most four
induced colour-budget blocks.  This is substantially more rigid than an
arbitrary failed four-colour state, although it still does not select a
state on both shores.

### Proposition 3.3 (bounded co-Tutte barriers at order nine)

Suppose `|V(J)|=9`, `J` is four-colourable, `I_2 vee J` is
`K_7`-minor-free, and `J` has no `(3,2,2,2)` partition.  Then `F` contains
a triangle.  For every triangle `T` of `F`, there is a set
`X_T \subseteq V(F)-T` such that

\[
 |X_T|\le2,\qquad
 o(F-T-X_T)>|X_T|,
 \qquad o(F-T-X_T)\le4.                                \tag{3.2}
\]

**Proof.**  Some colour class in any proper four-colouring of nine
vertices has order at least three, so `F` has a triangle.  By Lemma 2.2,
for every such triangle `T`, the six-vertex graph `F-T` has no perfect
matching.  Tutte's theorem supplies `X_T` with more odd components than
vertices.  Five such components would yield a boundary `K_5` supported on
five of the six vertices outside `T`, hence a proper boundary `K_5` and a
contradiction to Lemma 3.1.  Therefore the number of odd components is at
most four.  The same parity calculation on six vertices then forces
`|X_T|<=2`.  \(\square\)

For each fixed `T`, the same parity argument restricts
`(|X_T|,o(F-T-X_T))` to the four pairs in (3.3).
Moreover, the analogue of (3.4) shows that `F-T-X_T` has at most four
components.  Hence every failed order-nine state consists of an
independent triple `T`, at most two exceptional vertices, and a complete
join of at most four induced colour-budget blocks.  The decomposition can
still depend on `T`.

Unlike the order-eight case, the set `X_T` may depend on the chosen
triangle.  Proving that contraction-critical shore states select a common
triangle/barrier would be new information; it is not a consequence of the
boundary graph alone.

## 4. Consequence for the active spine

The four-colour conclusion of the two-full-shore boundary theorem cannot
by itself be pulled back to the paired-triangle exact-seven state.  The
valid state-free replacement is:

* a balanced matching state; or
* a co-Tutte obstruction controlled by at most two boundary vertices.

The second outcome is potentially compatible with the desired fixed-pair
or labelled-S1 handoff, because outside at most two vertices the boundary
is a complete join of complement components.  But the controlling pair is
only a boundary matching obstruction.  It is not automatically a global
transversal of `K_5` models, and it does not synchronize the two shore
colouring languages.

Any continuation must therefore use proper-minor state transitions or the
named model carriers to turn this bounded co-Tutte barrier into a common
state, a literal `K_7`, or a genuine global terminal pair.  Requiring a
balanced colour partition from four-colourability and the join-minor
exclusion alone is false.

## 5. Reproducible falsification probe

`../active/hc7_boundary_balanced_partition_probe.py` tests the balanced
partition and exact join-minor conditions on graph6 input.  It is
diagnostic only; the counterexamples and reductions above are entirely
hand proofs.
