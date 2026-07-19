# Independent internal audit: singleton component at an order-eight boundary

**Verdict:** **GREEN** for Lemmas 2.1, 2.2, 3.1, 4.1, 4.2,
Corollary 4.3, Lemmas 5.1, 5.2, and Theorem 6.1, within the exact trust
boundary stated below.  This is an independent internal mathematical audit,
not external peer review.  The theorem does not prove `HC_7`.

## Audited revision

This audit checks the complete source file
[`hc7_order8_singleton_low_connectivity_reduction.md`](hc7_order8_singleton_low_connectivity_reduction.md)
at SHA-256

```text
a84f5b9d1eeeae70473dfdad565edf26fbd2ed78eebf3a403a89cbac02e0f680
```

The current source was compared byte-for-byte with the originally audited
revision at SHA-256

```text
90f2ef2526cfa00f2844cd18403baf5770f35f3fcd7f343a6e47a075635e7ca5
```

The only change inserts the missing TeX backslash in `\qquad` in display
(3.2) and removes one balancing space on that same line.  The theorem
statements, proofs, dependencies, and trust boundary are unchanged.

After the GREEN verdict was recorded, the source status line was changed
from “audit recorded” to “audit GREEN.”  The promoted source SHA-256 is

```text
dfc13ca824f17efa4dec7240828a2d375b3e65910dcf96c088ae694c97ee914f
```

No mathematical text changed in that promotion step.

The source was read independently line by line.  The audit did not assume
the proposed proof summary.  In particular, it reconstructed every displayed
minor model and both orientations of the cutvertex argument.

The two imported mathematical results used in Lemma 5.1 are separately
GREEN-audited at the following source revisions:

```text
1aa7c959a181b8d86075eb5c2822c5328c2438c5f2e4f47c0ee8c2a3bb18c059
  results/hc7_order8_strict_reversal_completion.md
69a63c7899081defb83a15d838e636d6eb5dc96cdc1b0bf5a66ee029c0beafd7
  results/hc7_order8_two_defect_clique_oct_reflection.md
```

No unresolved mathematical assumption or gap remains in the displayed
statements.

## 1. Scope of the hypotheses

The proof is conditional on the literal order-eight configuration stated in
Section 1 of the source.  In particular:

- `G-S` has exactly the three components `{v},Q_0,Q_1`;
- all three components are adjacent to every vertex of `S`;
- `G[S]` is three-colourable, has independence number at most three, and
  contains two vertex-disjoint odd cycles; and
- every proper minor of `G` is six-colourable.

The theorem does not derive these hypotheses from the 82-type census inside
its proof.  The census is mentioned only as the intended source of the three
boundary hypotheses.  Thus the unbounded statements audited here stand
under their displayed assumptions and do not infer an unbounded conclusion
from a finite computation.

## 2. Lemma 2.1: representative allocation

At stage `i`, the previous representatives form a set of order `i`.

- If no earlier representative lies in `D_i`, adding `D_i` forbids at most
  one further vertex, for at most `i+1` forbidden vertices.
- If `x_j` lies in `D_i` for some `j<i`, that `j` is unique because `D_i`
  has order at most one and the representatives are distinct.  The vertex of
  `D_i` is already in the previous set.  Adding `D_j` therefore enlarges the
  forbidden set by at most one, again giving at most `i+1` vertices.

Since `i<=4`, at most five of the six vertices are forbidden.  The new
representative avoids `D_i`, all previous representatives, and, whenever
`x_j` lies in `D_i`, also avoids `D_j`.  For every unordered pair this is
exactly the negation of mutual defect incidence.  The greedy proof therefore
establishes both distinctness and the full pairwise condition; it is not
merely an existence count for one final step.

As an independent sanity check, all `7^5=16,807` ordered lists of empty or
singleton defects on a six-element set were exhaustively checked and each
admits the required five representatives.  The written greedy proof, not
this finite check, proves the lemma.

## 3. Lemma 2.2: all seven branch sets

Because only four of the five connected subgraphs can have a nonempty
singleton defect, the union of the defects has order at most four.  Hence at
least four boundary vertices avoid every defect.  The independence-number
bound supplies an edge `ab` among them.  Both endpoints lie outside every
defect, and every defect is therefore contained in the six-set
`N=S-{a,b}`.

Lemma 2.1 supplies distinct `x_0,...,x_4` in `N`.  The five sets

```text
B_i=P_i union {x_i}
```

are pairwise disjoint and connected: `x_i` has a neighbour in `P_i` because
it is not in `D(P_i)`.  They avoid the singleton sets `{a},{b}`.

All twenty-one adjacencies of the proposed seven branch sets were checked:

1. `{a}` and `{b}` are adjacent through `ab`.
2. Each of the five `B_i` is adjacent to each singleton because `a,b` avoid
   every defect.
3. For `i!=j`, an existing edge between `P_i,P_j` is sufficient.  If there
   is no such edge, no-mutual-defect says that either `x_j` is seen by
   `P_i`, or `x_i` is seen by `P_j`.  That edge joins `B_i` to `B_j`.

Thus the displayed seven sets are disjoint connected pairwise adjacent
branch sets.  The proof correctly requires no anticompleteness among the
five original subgraphs.

## 4. Lemma 3.1: exclusion of a second singleton

The independence-number hypothesis ensures that every colour class in a
proper three-colouring of the eight-vertex boundary has order at most
three.  Consequently all three colours are used and the class sizes are
`3,3,2`, after relabelling.

The two sets `{v} union A` and `{q} union B` are disjoint connected stars.
Contracting spanning trees in both gives a proper minor.  Their images are
adjacent (for example through an edge from `v` to `B`), and each image is
adjacent to each vertex of `C`.  A proper six-colouring therefore gives the
two images distinct colours and gives neither colour to `C`.  After
restriction to `Q_1 union S` and expansion, the boundary uses at most four
colours.  Expansion is proper because `A,B` are independent colour classes,
all cross-block edges were represented at the contraction images, and all
edges from `A` or `B` into the retained component were also represented.

A colour absent from `S` can be assigned simultaneously to `v,q`.  They are
distinct components of `G-S`, so they are nonadjacent and have no neighbours
in `Q_1`; all their neighbours in `S` avoid the chosen colour.  This gives a
proper six-colouring of all of `G`, as claimed.

## 5. Lemmas 4.1 and 4.2: literal separators

For a component `L` of `G[Q]-x`, the only possible neighbour in `Q-L` is
`x`, and connectedness of `Q` guarantees that `x` is in fact a neighbour.
There are no edges from `Q` to either other component of `G-S`.  Hence

```text
N_G(L)={x} disjoint-union N_S(L).
```

Deleting this set leaves the nonempty set `L` on one side and another lobe,
as well as the other components of `G-S`, on the other.  It is therefore a
genuine separation boundary.  Seven-connectivity gives
`1+|N_S(L)|>=7`.  Equality is an actual order-seven separation; strict
inequality means that the lobe misses at most one of the eight boundary
vertices.

If there are exactly three lobes, those three lobes, `{v}`, and the other
exterior component are five pairwise disjoint connected subgraphs, with at
least one full and all four remaining subgraphs near-full.  If there are at
least four lobes, four lobes and `{v}` have the same property.  Lemma 2.2
therefore applies exactly as stated.

For a bridge `xy`, its deletion has two connected sides `A,B`, and `xy` is
the only edge between them.  Thus the source correctly identifies the full
neighbourhoods as

```text
N_G(A)={y} disjoint-union N_S(A),
N_G(B)={x} disjoint-union N_S(B).
```

Both are genuine separation boundaries.  The same connectivity count gives
an order-seven separation or two near-full sides.

Corollary 4.3 then follows without an overlap problem.  Two lobes from a
cutvertex are disjoint even though they omit the cutvertex, and two bridge
sides are disjoint.  Choosing two pieces in each exterior component and
adding `{v}` gives exactly the five disjoint subgraphs required by Lemma
2.2.  Hence, outside the two terminal outcomes, at most one exterior
component can possess a cutvertex or a bridge.

## 6. Lemma 5.1: complete audit of the two-piece cases

The four subgraphs `{v},R,A,B` are pairwise disjoint.  The first two are
boundary-full; the last two are near-full and adjacent.

### 6.1 At least one of `A,B` is full

Two vertex-disjoint odd cycles on an eight-vertex boundary have orders
`(3,3)` or `(3,5)`.  If the non-full subgraph has defect `d`, at least one
cycle avoids `d`.  There is then a boundary vertex `e` outside that cycle
and distinct from `d`.  A full subgraph satisfies the weaker requirement
of being adjacent to every vertex except the artificial defect `e`.

If both subgraphs are full, any one of the odd cycles leaves at least three
boundary vertices outside it, so two distinct artificial defects can be
chosen.  In both cases all hypotheses of Lemma 1.1 in the GREEN-audited
strict-reversal completion theorem hold.  Its seven branch sets remain
valid with the extra boundary contacts of a full subgraph.

### 6.2 The two defects are equal

Choose an odd cycle `O` avoiding the common defect `d`.

If `O` is a triangle, the four vertices of `S-(V(O) union {d})` anchor
`A,B,{v},R` distinctly.  Each anchored set is connected.  Every pair is
adjacent because `A,B` see every anchor except `d`, the two full subgraphs
see every anchor, and `A,B` also have their assumed direct edge.  All four
sets see every vertex of the triangle.  Together with its three singleton
vertices these are seven valid branch sets.

If `O` is a five-cycle, it can be partitioned into three nonempty cyclic
intervals which are connected and pairwise adjacent.  Write the remaining
boundary vertices as `{d,r,s}`.  The four other branch sets are

```text
A union {r},  B union {s},  {v,d},  R.
```

They are disjoint and connected.  Their six mutual adjacencies are:

- `A-B` by hypothesis;
- `A-{v,d}` through the edge `rv` and `B-{v,d}` through `sv`;
- `A-R` through an edge from `r` to `R`, and `B-R` through one from `s`;
- `{v,d}-R` through an edge from `d` to `R`.

Each of these four sets sees every cycle interval because the cycle avoids
the only defect `d`.  The three cycle intervals are pairwise adjacent.
This checks all twenty-one adjacencies of the seven-set model.

### 6.3 The defects are distinct

If `G[S-{d,e}]` is nonbipartite, a shortest odd cycle in that six-vertex
graph has order three or five.  The two full subgraphs, the two adjacent
one-defect subgraphs, and this cycle satisfy Lemma 1.1 of the strict-reversal
completion theorem exactly.

If the residual graph is bipartite and `de` is an edge, apply the
GREEN-audited adjacent-defect reflection theorem with

```text
L=Q=A disjoint-union B,
R'={v} disjoint-union R.
```

There are no edges between these open shores because they are unions of
distinct components of `G-S`.  The two one-defect subgraphs lie in `L`,
the two disjoint full subgraphs lie in `R'`, every proper minor is
six-colourable, and the boundary has two disjoint odd cycles.  These are all
of that theorem's hypotheses.  It returns a six-colouring.  Therefore the
only nonterminal possibility has distinct nonadjacent defects whose deletion
leaves a bipartite boundary.

## 7. Lemma 5.2: both orientations of a two-lobe cutvertex

The proof's compressed label-consistency step is valid.  Here is the full
inclusion argument.

In the first orientation, Lemma 5.1 returns

```text
D(L_1 union {x})={d},  D(L_2)={e}.
```

Because `D(L_1 union {x})` is contained in `D(L_1)` and `L_1` is near-full,
the first equality forces `D(L_1)={d}`.  It also forces `x` to miss `d`.

For the opposite orientation, `L_1` is therefore still the exact
`d`-defect side.  Moreover

```text
D(L_2 union {x}) subseteq D(L_2)={e}.
```

If this defect were empty, Lemma 5.1 would take its already-terminal full
side branch.  Under the lemma's nonterminal hypothesis it is nonempty, so it
equals `{e}`.  Hence `x` also misses `e`.  The distinct labels in the two
orientations are therefore the same `d,e`; they cannot silently be
permuted or replaced.

Both displayed partitions are legitimate: adding `x` to one lobe makes a
connected side, the other lobe is connected, and an edge from `x` to the
other lobe joins the two sides.  Adding `x` can only reduce a singleton
defect, so both sides remain near-full.  This verifies all hypotheses of
Lemma 5.1 in both orientations.

The source states this inclusion argument tersely in lines 335--344, but all
of its premises were established and the conclusion follows without an
additional assumption.

## 8. Theorem 6.1 and trust boundary

Lemma 3.1 gives non-singleton exterior components.  Lemmas 4.1 and 4.2
return a `K_7` minor or an actual order-seven separation unless every
cutvertex has two lobes and every selected lobe or bridge side is near-full.
Corollary 4.3 confines such low connectivity to at most one exterior
component.  Lemmas 5.1 and 5.2 then give exactly the structural residue
listed in outcome 4.  No additional case is lost in this assembly.

If the other exterior component is non-singleton and has neither a
cutvertex nor a bridge, it has at least three vertices: a connected simple
graph on two vertices has a bridge.  Thus the final assertion that it is
two-connected is valid under the standard convention.

The conclusion remains deliberately partial:

- the surviving distinct nonadjacent defect pair is not eliminated;
- a returned order-seven separation is not shown to carry compatible
  equality partitions from its two shores;
- no statement is proved for a two-connected, bridge-free selected
  component; and
- the result assumes, rather than proves, the exact three-component
  order-eight setting and its three boundary properties.

Within that boundary, the theorem is correct at the audited revision.
