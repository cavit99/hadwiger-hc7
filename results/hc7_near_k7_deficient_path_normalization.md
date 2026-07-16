# Deficient-bag normalization in an arbitrary spanning `K_7^vee` model

## Status

This is a direct attempt on P1 of the archived
[`hc7_near_k7_proof_spine_20260715.md`](../archive/hc7_near_k7_proof_spine_20260715.md).

It proves a stronger lexicographic normalization for the deficient bag
`A`: because `A` has only four required model neighbours, applying
minimality to both sides of every connected split forces `G[A]` itself to
be a path.  Its four neutral portal classes are singleton sets, two at
each end.  Thus every nonsingleton deficient bag is a canonical induced
bipartite carrier to which the audited total-contraction theorem applies.

The attempted next step—identifying its five palette rows with the six
foreign model labels—is invalid when the foreign bags are nonsingleton.
The failure is exact: contracting those bags produces a colour state of a
proper minor, but a colouring of the carrier expands only to the partially
contracted graph, not to the original graph.  Consequently the singleton
shell alignment theorem cannot be invoked at this point.

This note therefore advances normalization but does not close P1.

## 1. Model and deficient-first order

Let `G` contain a labelled `K_7^vee` model

\[
                       A,B,C,U_1,U_2,U_3,U_4,             \tag{1.1}
\]

where only `AB,AC` are not prescribed.  The four required neighbours of
`A` are the neutral bags

\[
                         \mathcal U=\{U_1,U_2,U_3,U_4\}. \tag{1.2}
\]

Among all labelled models choose one minimizing

\[
 (|A|,|U_1|,|U_2|,|U_3|,|U_4|,|B|,|C|)                 \tag{1.3}
\]

lexicographically.  The model need not be spanning during this
minimization; deleting an inessential part of a bag must be an admissible
comparison.

For a nonempty proper `X subset A`, call `X` **detachable** if both
`G[X]` and `G[A-X]` are connected.  Put

\[
 \Omega_A(X)=\{U_i:\text{ every }A-U_i\text{ model edge has its}
                         A\text{-end in }X\}.             \tag{1.4}
\]

### Theorem 1.1 (two-owner rule in the deficient bag)

Every detachable `X subset A` satisfies

\[
                         |\Omega_A(X)|\ge2.                \tag{1.5}
\]

#### Proof

If `Omega_A(X)` is empty, replace `A` by `A-X`; every required model
adjacency survives and the first coordinate in (1.3) decreases.

If `Omega_A(X)={U_i}`, replace

\[
                    A\longmapsto A-X,qquad
                    U_i\longmapsto U_i\cup X.             \tag{1.6}
\]

The enlarged `U_i` is connected because an old `A-U_i` edge has its
`A`-end in `X`.  The residual `A-X` retains every required adjacency
except possibly `AU_i`, and the cut edge between `X` and `A-X` restores
that pair after (1.6).  Every other old adjacency of `U_i` survives.
Thus (1.6) is a labelled `K_7^vee` model with smaller first coordinate,
again a contradiction.  \(\square\)

The proof uses that all four targets in (1.2) occur later than `A` in the
lexicographic order.  This is why the deficient-first order is sharper for
`A` than the neutral-first order in the audited literal-rooting bridge.

### Corollary 1.2 (at most two disjoint deficient lobes)

Every family of pairwise disjoint detachable subsets of `A` has order at
most two.

#### Proof

Their monopoly sets are pairwise disjoint: the nonempty set of all
`A`-ends of the edges to one `U_i` cannot be contained in two disjoint
sets.  Each monopoly set has order at least two by Theorem 1.1, and only
four labels are available.  \(\square\)

For `U_i in mathcal U`, let

\[
 P_i=\{a\in A:a\text{ is the }A\text{-end of an }A-U_i
                         \text{ edge}\}.                    \tag{1.7}
\]

Every `P_i` is nonempty.

### Theorem 1.3 (the deficient bag is a `2+2` portal path)

Either `A` is a singleton, or `G[A]` is an induced path.  In the latter
case there are distinct endpoints `a_0,a_1` and a partition

\[
                    \mathcal U=\mathcal U_0\mathbin{\dot\cup}
                               \mathcal U_1,
                    \qquad |\mathcal U_0|=|\mathcal U_1|=2, \tag{1.8}
\]

such that

\[
       P_i=\{a_0\}\quad(U_i\in\mathcal U_0),\qquad
       P_i=\{a_1\}\quad(U_i\in\mathcal U_1).               \tag{1.9}
\]

#### Proof

Let `X dotcup Y=A` be any partition into nonempty connected sets.  Both
sets are detachable.  Theorem 1.1 gives at least two monopoly labels to
each.  Their monopoly sets are disjoint and there are only four labels,
so each side owns exactly two labels and together they own all four.
Consequently no portal set `P_i` meets both `X` and `Y`.

Fix a spanning tree `T` of `G[A]`.  The two vertex sets on the sides of
every edge of `T` are connected and hence satisfy the preceding
conclusion.  If some `P_i` contained distinct vertices `p,p'`, an edge on
the `p-p'` path in `T` would put them on opposite sides, a contradiction.
Thus every `P_i` is one singleton vertex.

Every leaf `ell` of `T` is detachable: `A-ell` contains the connected
tree `T-ell`.  Hence `ell` is the unique portal of exactly two neutral
labels.  Distinct leaves own disjoint label pairs, so `T` has exactly two
leaves and is a path.  This holds for every spanning tree of `G[A]`.

If `G[A]` had a vertex of degree at least three, the three incident edges
form a forest and could be extended to a spanning tree in which that
vertex has degree at least three, contradicting that every spanning tree
is a path.  Therefore `G[A]` has maximum degree at most two and is itself
a path or a cycle.  A cycle of order at least three is impossible: every
singleton vertex of a cycle is detachable and would own at least two
labels, giving at least six pairwise disjoint monopoly labels.  Hence
`G[A]` is a path.

Its two endpoints are the leaves of its unique spanning tree, each owns
two labels, and all four portal sets are singleton.  This is exactly
(1.8)--(1.9).  Since `G[A]` denotes the induced subgraph on the bag, the
path is induced in `G`.  \(\square\)

## 2. The block tree is a path

### Theorem 2.1 (deficient block-path theorem)

The block-cutvertex tree of `G[A]` has at most two leaves.  Consequently
it is a path.  Every end block has at most two noncut vertices, and every
internal block has at most two vertices other than its two block-tree
cutvertices.  In particular every block has order at most four.

If `G[A]` is two-connected, then `|A|<=2`.

#### Proof

The interior of a leaf block—its vertices other than its unique
block-tree cutvertex—is detachable.  Interiors of distinct leaf blocks
are disjoint, so Corollary 1.2 permits at most two leaves.  A finite tree
with at most two leaves is a path.

Every noncut vertex `x` of a block is itself detachable: deleting it
leaves its nonseparable block connected and does not disturb the remaining
block tree.  Distinct such singleton parts have disjoint monopoly sets of
order at least two.  Hence a block contains at most two noncut vertices.
An end block has one block-tree cutvertex and an internal block has two,
giving the asserted orders.

If `G[A]` is two-connected and has at least three vertices, every
singleton is detachable.  The same disjoint-monopoly count gives
`2|A|<=4`, a contradiction.  \(\square\)

Thus an arbitrary SPQR-sized deficient bag is impossible in a
deficient-first model.  Its only unbounded feature is the length of its
block path.

## 3. Constant-owner intervals are induced bipartite carriers

Root the block path at one end.  For an open descendant lobe `L` at a
cutvertex, `Omega_A(L)` is the set of neutral portal endpoint sets wholly
contained in `L`.  Along nested descendant lobes these sets are monotone.
Every lobe has an owner set of order at least two, so along the whole path
there are at most three distinct owner sets, hence at most two strict
owner changes:

\[
                         2\longrightarrow3\longrightarrow4. \tag{3.1}
\]

### Theorem 3.1 (constant-owner bridge collapse)

Between consecutive owner changes, every intervening block is a single
bridge edge and no intermediate cutvertex has an off-interval component.
The vertices traversed by such a constant-owner interval induce a path in
`G[A]`.  Every strictly internal vertex is anticomplete to each neutral
bag in the common owner set.

#### Proof

Let `c,d` be consecutive block-path cutvertices in a constant-owner
interval, and let `K` be their common block.  If
`x in K-{c,d}` is not a cutvertex, then `{x}` is detachable and owns at
least two labels.  Those labels belong to the larger descendant lobe but
not the smaller one, contradicting constancy.  If such an `x` is a
cutvertex, the component hanging from it off the displayed block path is
detachable and yields the same contradiction.  Hence `K={c,d}`, a bridge
edge.

The identical argument excludes every off-path component at an
intermediate cutvertex.  A chord between nonconsecutive path vertices
would put the intervening edges in one nonseparable block, already
excluded.  Thus the interval is induced.

If an internal path vertex met an owner bag `U_i`, its occurrence in the
`A-U_i` portal endpoint set would prevent that entire endpoint set from
lying in the deeper of the two consecutive lobes.  This again contradicts
constant ownership.  \(\square\)

### Corollary 3.2 (a canonical P2 carrier)

Every unbounded deficient bag contains a nontrivial connected induced
bipartite carrier `X` which is a constant-owner path.  Contracting `X`
in a 7-contraction-critical host and applying
`../results/hc7_near_k7_bipartite_total_contraction.md` gives a split

\[
                              X=X^-\mathbin{\dot\cup}X^+    \tag{3.2}
\]

into adjacent connected shores which simultaneously see all five colours
different from the contraction colour in one proper-minor state.

This is a genuine P1 normalization output.  It is not yet a
label-preserving split of the old model.

## 4. The palette-to-label lift fails before singletonization

One tempting continuation is:

1. contract the six foreign bags to labelled quotient vertices;
2. contract `X` and six-colour the quotient;
3. use the five secondary colours as five old branch-label rows; and
4. invoke the singleton-shell alignment theorem.

Step 3 is invalid.

### Proposition 4.1 (partial-expansion obstruction)

Let `Q` be obtained by contracting one or more nonsingleton foreign model
bags in addition to `X`.  A six-colouring of `Q`, together with a
list-colouring of `G[X]` obtained from its exterior quotient colours,
need not expand to a six-colouring of `G`.

Consequently non-six-colourability of `G` does not imply that `X` is
uncolourable from those quotient lists, and neither the parity-saturation
lemma nor the singleton palette-to-label theorem applies.

#### Proof

Expanding the colouring on `X` leaves every contracted foreign bag as one
coloured quotient vertex.  A connected branch bag is not generally an
independent set and has no automatic expansion in the colour assigned to
its contraction image.  It may require several colours, and its boundary
constraints may depend on which internal vertex carries each portal.
Thus the combined colouring is only a colouring of the partially
contracted graph, not of `G`.

The contradiction used in the singleton-shell list lemma is valid exactly
because every foreign bag there is already one literal vertex.  No such
coexistence holds here.  \(\square\)

There is a second, independent defect.  A palette colour in a colouring of
the partially contracted minor need not occur in only one old branch bag;
vertices outside the model or in other nonsingleton bags may carry the
same colour.  Thus even full palette exposure on both shores does not
identify literal old label contacts.

## 5. Exact next step and stopping point

The deficient-first normalization proves:

\[
 \boxed{
 \begin{array}{c}
 \text{bounded event blocks of order at most four}\cr
 \text{joined by induced bipartite constant-owner paths.}
 \end{array}}                                             \tag{5.1}
\]

It does **not** prove P1.  The missing local theorem is no longer a
generic splitter, but it is still a genuine global-strength exchange:

> Given one constant-owner path in the deficient bag and the one bilateral
> five-colour state from its total contraction, either extract literal
> private extensions into four of the six foreign bags while preserving
> the other two reserve roles, or prove that all failed extensions have
> one rural embedding with a fixed two-vertex apex pair.

The active fixed-extension face theorem completes the argument after the
four private extensions exist.  Proposition 4.1 proves that those
extensions cannot be obtained merely by contracting and recolouring the
foreign bags.  Any continuation must retain their internal portal
geometry or use faithful operations on opposite actual shores.
