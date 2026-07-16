# Audit of the seven-terminal cycle-or-biclique theorem

## Verdict

**GREEN.**  The theorem in
[`hc7_seven_terminal_rooted_cycle_or_biclique.md`](hc7_seven_terminal_rooted_cycle_or_biclique.md)
is correct.  Every seven prescribed vertices in a simple three-connected
graph root either a `C_7` or a `K_{3,4}`.  The proof uses Dirac's standard
circumference theorem and Wu's contractible-edge theorem at their stated
strengths, the eight-vertex suppression argument is complete, and the lift
through terminal-legal contractions is label-faithful.

## 1. Seven-vertex base

Dirac's circumference theorem gives a cycle of length at least six in a
three-connected seven-vertex graph.  If there is no spanning cycle, fix a
six-cycle

```text
C=c_0c_1...c_5c_0
```

and let `x` be the remaining vertex.  Minimum degree gives at least three
neighbours of `x` on `C`.  No two can be consecutive, because the two
incident rim edges could then be replaced by a two-edge path through `x`.
The maximum independent sets of `C_6` have size three and are its two
alternating triples.  Thus, after relabelling,

```text
N_C(x)={c_0,c_2,c_4}.
```

If two odd-indexed vertices are adjacent, symmetry permits the edge
`c_1c_3`, and

```text
c_0 c_1 c_3 c_2 x c_4 c_5 c_0
```

is a spanning cycle.  Otherwise the odd-indexed vertices are pairwise
nonadjacent.  For each such vertex its two rim neighbours are its only
available neighbours except for the opposite even-indexed vertex, because
it is also nonadjacent to `x`.  Minimum degree therefore forces

```text
c_1c_4, c_3c_0, c_5c_2.
```

The six rim edges, these three edges, and the three edges from `x` are the
twelve required cross-edges between

```text
{c_0,c_2,c_4} and {x,c_1,c_3,c_5}.
```

They form a spanning `K_{3,4}`.  Possible additional edges inside either
part do not affect containment.  Lemma 1.1 is exhaustive.

## 2. Contraction criterion

Lemma 2.1 is valid.  Let `z` be the contracted image of `vx`.  A deletion
of at most two quotient vertices avoiding `z` lifts to the same deletion in
the three-connected graph `M`, after which contraction preserves
connectedness.  Deleting `z`, with possibly one other vertex `y`, leaves
`H-x` or `(H-x)-y`, both connected when `H-x` is two-connected.  The
simplified quotient is therefore three-connected.  No converse is claimed
or needed in this file, although the exact converse is established in the
adjacent irreducible-kernel classification.

## 3. Hamilton remainder on eight vertices

Put `H=M-v`.  It is two-connected.  Wu supplies at least four degree-three
neighbours of `v`, all of which have degree two in `H`.  Hence, for

```text
D={u:d_H(u)=2},  B=V(H)-D,
```

we have `|D|>=4`, `|B|<=3`, and every member of `B` has degree at least
three in `H`.

The cases `|B|=0,1` are correctly dismissed.  If `B` is empty, `H` is a
connected two-regular graph.  If `B={b}`, then `H-b` is a connected graph
of maximum degree two.  It cannot be a cycle with an attachment to `b`,
since an attached vertex would then lie in `B`; hence it is a path whose
ends attach to `b`, making `H` a cycle and contradicting `b in B`.

For `|B|` equal to two or three, every component of `H[D]` is a path.  A
cycle component could not attach to `B`, and the two ends of a path cannot
attach to the same member of `B` because that vertex would cut the
two-connected graph `H`.  Suppression therefore gives a loopless
multigraph on `B`, with every long-edge weight positive and total weight
`|D|`.

### Two high-degree vertices

There are at least three parallel routes because both high-degree vertices
have degree at least three, while simplicity permits at most one direct
route.  If at most two routes were long, those two long routes, or the one
long route and the direct edge, would contain every member of `D` and form a
Hamilton cycle.  Thus at least three routes are long.  Their positive
weights sum to five, so one has weight one.

Deleting its sole internal vertex leaves at least two internally disjoint
routes between the high-degree vertices, hence a two-connected graph.
Deleting those two high-degree vertices from `M` must leave a connected
graph; since the selected internal vertex has only those two neighbours in
`H`, it must be adjacent to `v`.  Lemma 2.1 then contracts that edge, a
contradiction.

### Three high-degree vertices

The underlying simple suppressed graph is a triangle: any missing side
would leave a cutvertex in `H`.  If each pair supports at most one long
route, selecting that route where present and otherwise the direct edge
gives a triangle containing all long routes, which lifts to a Hamilton
cycle.  Therefore two long routes have the same ends.

Their weights cannot both exceed one.  If they did, their total would use
all four vertices of `D`; the two remaining sides of the underlying
triangle would then have to be direct, leaving the third high-degree vertex
with degree two.  Thus one repeated route has one internal vertex.  Deleting
that vertex leaves the other repeated route and the underlying triangle,
so the remainder is two-connected.  The same two-vertex-deletion argument
forces adjacency to `v`, and Lemma 2.1 again contradicts the hypothesis.

All possibilities are covered, proving that `M-v` is Hamiltonian.

## 4. Terminal-irreducible base and rooted lift

In an order-eight `T`-irreducible kernel, the unique nonterminal `v` has
only terminal neighbours.  Every incident edge is therefore `T`-legal and
none is contractible.  Lemma 2.2 supplies a Hamilton cycle in `M-v=M[T]`,
with the nonterminal unused.  Corollary 2.3 follows exactly.

The audited terminal-kernel theorem gives, for seven terminals, a
three-connected terminal-irreducible rooted minor with

```text
7 <= |V(M)| <= 7+floor(7/4)=8.
```

If the kernel has order seven, Lemma 1.1 applies to its seven distinct
terminal images.  If it has order eight, Corollary 2.3 applies.  Reversing
each terminal-legal contraction expands only the unique bag containing the
contracted image.  It cannot identify terminal labels, and it preserves bag
connectivity, pairwise disjointness, and every carrier adjacency.  The
result is therefore a literal `T`-rooted model in the original graph.

The proof does not prescribe which terminal occupies which position on the
cycle or on either side of the biclique.  The stated non-prescribed
bijection is the exact conclusion justified by the two finite bases.

## 5. Label-faithful overlap-three application

Deleting the three vertices of `I` from a seven-connected graph leaves a
four-connected graph, so the universal theorem applies to the seven literal
members of `T`.  The file correctly distinguishes:

* original edges among the labelled vertices, which may be used in the
  irredundant support constraints; and
* carrier adjacencies between expanded rooted bags, which may be used only
  in the final branch-set composition.

Because each carrier bag contains its named terminal, every original edge
incident with a terminal remains available after expansion.  Conversely,
the argument never upgrades a carrier adjacency to a literal
terminal-terminal edge or assumes a prescribed carrier placement.  The
application section is sound and does not overstate Theorem 3.1.

## 6. Independent finite replay

The supplied falsifier was replayed successfully.  It enumerated all
simple three-connected graphs of orders seven and eight and every choice of
seven terminals.  The exact results were

```text
order 7: 136 graphs, 136 rooted sets, 132 C7 outcomes, 4 K3,4 outcomes
order 8: 2388 graphs, 19104 rooted sets, 18927 C7 outcomes, 177 K3,4 outcomes
```

Thus it found no counterexample even to the stronger order-eight statement
that permits assigning the sole nonterminal directly to one rooted bag
without first requiring terminal irreducibility.  Among the terminal-
irreducible order-eight instances there were exactly ten rooted cases, and
all ten had a Hamilton cycle on the literal terminals, as Lemma 2.2
requires.  This computation is corroboration, not a dependency of the hand
proof.

## 7. Scope

The theorem supplies a bounded carrier with an arbitrary labelled cyclic
order or arbitrary labelled `3+4` bipartition.  It does not assert that
either carrier alone closes a particular `HC_7` quotient.  Any such
composition remains a separate universal finite check over all labelled
carrier placements.
