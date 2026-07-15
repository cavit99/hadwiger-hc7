# Structural handoff for the overlap-four cross-arm cell

## Status

Proved, conditional only on the two adjacent computer-assisted decoders
and one published terminal-cycle lemma.  An independent cold audit is
**GREEN**; see
[`hc7_cross_arm_overlap_four_structural_handoff_audit.md`](hc7_cross_arm_overlap_four_structural_handoff_audit.md).

This closes the unbounded exterior-model question in the overlap-four
cell.  The output is a literal `K_7` or a labelled one-hole `K_7^-`
model; no further finite portal classification is used.

## 1. A rooted chord on five cyclic terminals

### Lemma 1.1

Let `H` be three-connected, let `T={t_0,...,t_4}`, and let `C` be a
cycle containing the five vertices in this cyclic order.  Then `H`
contains a `T`-rooted minor consisting of the five-cycle

```text
t_0 t_1 t_2 t_3 t_4 t_0
```

together with at least one chord.

### Proof

For indices modulo five, let `C_i` be the closed `t_i-t_{i+1}` arc of
`C` containing no other member of `T`.  Recall that a `C`-bridge is a
chord of `C`, or a component of `H-V(C)` together with its incident
edges to `C`.  Call a bridge **local** if all its attachments lie in one
arc `C_i`.

Not every bridge is local.  Otherwise assign each bridge to an arc
containing all its attachments.  A nontrivial bridge has at least three
attachments, by three-connectivity, so its arc is unique; a chord with
distinct ends is harmlessly assigned to either eligible arc.  For each
`i`, the internal vertices of `C_i` together with all bridges assigned
to it have no neighbour outside this piece except `t_i,t_{i+1}`.  If the
piece has an internal vertex, the pair `{t_i,t_{i+1}}` separates it from
the other three terminals, contrary to three-connectivity.  If no piece
has an internal vertex, then every `C_i` is one edge and there is no
bridge, so `H=C_5`, again contrary to three-connectivity.

Choose a nonlocal bridge.  It has two attachments `x,y` which do not lie
together in any one `C_i`; join them by a path `P` whose internal
vertices avoid `C`.  (For a chord, `P` is that edge.)  A vertex internal
to `C_i` may be assigned to either of the two terminal bags rooted at
`t_i,t_{i+1}`, while a terminal is assigned to its own bag.  Since
`x,y` do not lie in one terminal arc, these assignments can be chosen so
that `x` and `y` belong to nonconsecutive terminal bags.  To see this
directly, associate to an internal vertex of `C_i` the two-set
`{i,i+1}` and to `t_i` the singleton `{i}`.  If every choice from the two
associated sets were equal or consecutive on the five-cycle, their
vertices would lie in a common `C_i`.

Delete one edge in each open terminal arc so that the five remaining
path segments are disjoint connected bags, rooted respectively at the
five terminals, and put `x,y` in the selected nonconsecutive bags.
Adjoin `P-y` to the bag containing `x`.  Its last edge to `y` supplies a
chord between those two bags.  The five cut edges retain the five cycle
adjacencies.  This is the required rooted minor.  \(\square\)

## 2. Published terminal-cycle input

We use the following special case of Lemma 4 in Groenland--Nederlof--Koana,
*A Polynomial Time Algorithm for Steiner Tree when Terminals Avoid a
Rooted `K_4`-Minor* ([arXiv:2410.06793](https://arxiv.org/abs/2410.06793)):

> If `H` is three-connected and has no `T`-rooted `K_4` model--that is,
> no four `K_4` bags each meeting `T`--then `H` has a cycle containing
> every vertex of `T`.

For a five-set `T`, a `T`-rooted `K_4` model is exactly a `K_4` model
rooted at some four members of `T`: choose one terminal from each of its
four disjoint bags.  The fifth terminal may lie in one of those bags.

## 3. The crossed residue has a universal three-bag core

Use the normalized overlap-four labels

```text
A={0,1,2,3,4,5},        I={0,1,2,3},
X=I union {6},           p=7, q=8,
T={4,5,6,7,8},           H=G-I,
```

and the eleven irredundant support-six hypotheses of the audited rooted
and cycle decoders.

In the sole crossed residue of the cycle decoder, the complement on `I`
is a perfect matching

```text
M={u u', v v'},
```

and every terminal is complete to `I`, except that `6` may miss one
vertex `w in I`.  Choose `u=w` when that optional defect occurs, and
otherwise choose either endpoint of one matching edge; choose `v` from
the other matching edge.  Then

```text
{u,v},   {u'},   {v'}
```

are three connected, pairwise adjacent bags in `G[I]`.  The pair bag is
an edge because its ends lie in different complement-matching edges.
Every terminal contacts all three bags.  In particular, when `6u` is the
optional missing edge, vertex `6` contacts the pair bag through `v` and
is adjacent to both singleton bags.

### Lemma 3.1

Every crossed residue contains a `K_3` model supported on `I` such that
each of the five terminal vertices contacts every one of its bags.

The preceding construction proves the lemma.

## 4. Main handoff theorem

### Theorem 4.1

Let `G` be seven-connected and satisfy the normalized overlap-four
cross-arm hypotheses above.  Then `G` contains either a `K_7` minor or a
labelled `K_7^-` minor.

### Proof

The graph `H=G-I` is three-connected.  If it has a `T`-rooted `K_4`
model, select one terminal from each of its four bags.  The independently
audited rooted-`K_4` decoder gives either a literal `K_7`, or a common
support-at-most-five `K_4` contacted by three named roots.  The latter
gives `K_7` by the independently audited three-rooted composition
theorem.

Assume that no `T`-rooted `K_4` exists.  The published terminal-cycle
lemma gives a cycle through all five vertices of `T`.  Apply the audited
five-terminal cycle decoder in its cyclic order.  Its first two outcomes
again give `K_7`.  In its sole remaining crossed outcome, Lemma 3.1 gives
three pairwise adjacent bags on `I`, each contacted by every terminal.

Apply Lemma 1.1 to the terminal cycle in `H`.  It gives five rooted cycle
bags and a chord.  Relabel cyclically so the chord joins the first and
third bags.  Merge the fourth and fifth bags across their cycle edge.
The resulting four bags have all adjacencies of `K_4` except possibly
the edge from the second bag to the merged fourth bag: the chord supplies
the first--third edge, and the four retained cycle adjacencies supply
the other four edges.

Every one of these four exterior bags contains a terminal and is
therefore adjacent to every bag of the `K_3` model on `I`.  The three
`I`-bags and the four exterior bags are seven disjoint connected branch
sets with only one possible missing pair.  They form a labelled
`K_7^-` model.  \(\square\)

## 5. Exact contribution and boundary

The theorem is a uniform composition result for an exterior of arbitrary
order.  It reduces the complete overlap-four rigid cell to the existing
one-hole near-`K_7` spine.  It does **not** turn an arbitrary `K_7^-`
model into `K_7`, and therefore does not prove the support-six transversal
theorem or `HC_7` by itself.

There is a stronger connectivity split.  If `H` is four-connected, the
cofacial planar branch can use the connected complement of a peripheral
terminal face to repair a fixed crossed gate, giving `K_7`.  If `H` is
not four-connected, a three-cut `Z` of `H` makes `I union Z` an actual
seven-separator of `G`; seven-connectivity makes every component behind
it full to all seven boundary vertices.  This sharper exact-seven
handoff is recorded separately because it requires its own audit.
