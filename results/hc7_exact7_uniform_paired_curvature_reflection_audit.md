# Independent audit: uniform paired-state curvature reflection

**Verdict:** **GREEN.**

Audited proof:

```text
results/hc7_exact7_uniform_paired_curvature_reflection.md
Final SHA-256: 34cfa369da7cb99176ab69c134eefe6b0819642947e9b51451007310a7996228
```

The mathematical proof was audited at SHA-256
`34b0bbdafbaaa89166a2cb315877ccf378440c0108902b5efffa25072c25e3ef`.
The final file changes only its status line from `frozen proof draft awaiting
independent audit` to `proved and independently audited`; every mathematical
line is unchanged.  The audit uses no finite census or portal-distribution
hypothesis.

## 1. Exact reflection reduction

Lines 11--35 state all inputs used later: seven-connectivity, six-colourability
of every proper minor, an actual order-seven separation with both shores
nonempty, the legally attained exact partition, a three-connected `S`-full
component `C`, and a disjoint connected `S`-full packet `Q`.

Lines 45--63 correctly show that nonreflection forbids two vertex-disjoint
duty carriers in `C`.  If `T_i,T_j` fund distinct duties and `k` is the third
index, then

\[
 T_i\cup B_i,\qquad T_j\cup B_j,\qquad Q\cup B_k,\qquad \{c\}
\]

are four pairwise disjoint connected branch sets.  The first three are
pairwise adjacent through the stipulated literal edges between old blocks,
and each is adjacent to `c` through its assigned block.  Thus their
contractions give a literal `K_4` indexed exactly by the four blocks of
`Pi`; mutual adjacency of the interior carriers is unnecessary.

The contraction is proper, every proper minor is six-colourable, and the
`K_4` forces four distinct block colours.  Pulling back each independent
pair `B_i` gives exactly `Pi`, not a coarsening.  The setup explicitly says
that the operation in the other shore returned the same exact partition, so
a permutation of the six colour names aligns the four used block colours.
The open shores are anticomplete, and the two closed-shore colourings glue.

## 2. Uniform Hall separator

The portal-matching observation in lines 65--90 is valid for every

\[
 D\subseteq S-\{c\},\qquad |D|\le |C|,
\]

including the empty set, whose matching assertion is vacuous.  If a nonempty
`U subseteq D` violates Hall, then

\[
 |N_C(U)|\le |U|-1\le |C|-1,
\]

so `C-N_C(U)` is nonempty.  The proposed deletion set

\[
 X=(S-U)\cup N_C(U)
\]

has exact order

\[
 |X|=7-|U|+|N_C(U)|\le6,
\]

because `S` and `C` are disjoint.

Every component of `C-N_C(U)` has no edge to a surviving label in `U`, by
the definition of `N_C(U)`, and every label in `S-U` was deleted.  Since `C`
is a component of `G[R]` and an actual separation has no `L-R` edge, `C` has
no exit to any vertex of `G-S` outside `C`.  Hence such a component is
separated from the nonempty old `L`-shore (and also from the surviving packet
`Q`).  This is a separator of order below seven, the required contradiction.
Arbitrary overlaps among portal sets do not affect this incidence-graph
argument.

## 3. Witnessed versus unwitnessed duties

Lines 92--103 use the exact logical negation of the witness definition.  If
duty `i` is unwitnessed, then every cross-pair

\[
 p\in N_C(a_i),\qquad q\in N_C(t_i),\qquad p\ne q
\]

is adjacent in `C`.  Equality `p=q` is deliberately allowed and causes no
problem.

A three-connected graph has at least four vertices.  For two unwitnessed
duties, apply the uniform Hall observation to their four distinct literal
labels.  The matching supplies four pairwise distinct portal vertices.
Within each duty its two matched portals are therefore distinct and, by
unwitnessedness, joined by a literal edge.  The two edges have disjoint
vertex sets, so they are two disjoint connected duty carriers.  Section 1
then reflects `Pi` with `Q`, contradicting nonreflection.  This remains valid
when the four complete portal sets overlap arbitrarily.  Consequently at
most one duty is unwitnessed and at least two are witnessed.

## 4. Two-witness common-face lemma

Lines 105--113 meet every hypothesis of the audited two-witness common-face
lemma in `results/hc7_exact7_single_missing_curvature_exchange.md`:

- `G` is seven-connected and `S` has order seven;
- `C` is three-connected and is a component of `G-S`;
- `G-(S union V(C))` is nonempty, since the old `L`-shore survives (as does
  `Q`);
- each literal pair `a_i,t_i` is nonadjacent because `B_i` is independent;
- nonreflection forbids two disjoint connected duty carriers in `C`; and
- the dichotomy supplies nonadjacent portal witnesses for two duties.

The lemma therefore makes `C` planar and places every vertex in all six
complete non-`c` portal sets on one facial cycle `F`.  It is essential, and
correct, that the conclusion concerns complete stars rather than only the
four chosen witnesses.  Three-connectivity makes the facial boundary a
simple cycle.  Since it contains a pair of nonadjacent vertices, its length
is at least four.

## 5. Components of order four and five

Lines 115--129 exhaust all small orders permitted by three-connectivity.

If `|C|=4`, then the facial cycle of length at least four contains all four
vertices.  Taking it as the outer face makes `C` outerplanar, whence
`|E(C)|<=5`; but `delta(C)>=3` gives `|E(C)|>=6`.

If `|C|=5`, the common face has length four or five.  Length five again makes
`C` outerplanar and gives `|E(C)|<=7`, whereas `delta(C)>=3` gives
`|E(C)|>=8`.  At length four, let `w` be the fifth vertex.  Complete-portal
cofaciality excludes every neighbour of `w` in `S-\{c\}`.  Componenthood
excludes neighbours outside `C union S`, so

\[
 d_G(w)\le d_C(w)+1\le4+1=5,
\]

contradicting the minimum degree at least seven supplied by
seven-connectivity.  Thus nonreflection forces `|C|>=6`.

## 6. Six-label matching, alternation, and curvature

For `|C|>=6`, lines 132--147 apply the Hall observation to all six non-`c`
labels and obtain six pairwise distinct representatives.  Complete-star
cofaciality puts all six on `F`, even if the underlying portal sets overlap.

For any two duties, failure of alternation of their four distinct selected
endpoints leaves two vertex-disjoint complementary facial subpaths joining
the prescribed pairs.  Those paths are connected duty carriers in `C`,
which Section 1 forbids.  Hence all three selected pairs alternate pairwise.
The unique cyclic word with three letters occurring twice and every pair
alternating is, up to the stated symmetries,

\[
                         A\ B\ D\ A\ B\ D.
\]

After relabelling the six complete portal sets in this order, opposite
indices are exactly the three original duties.  Lines 150--164 then satisfy
all hypotheses of the audited facial portal-incidence theorem: nonempty
portal sets, distinct cyclic representatives, arbitrary set overlaps, and
failure of two disjoint facial duty paths.  It gives

\[
                         \sum_{v\in V(F)}\lambda(v)\le |F|+6.
\]

The audited curvature theorem applies to the same three-connected plane
component of `G-S`.  Every non-`c` boundary portal is on `F`, while an
off-face vertex can have at most `c` as a boundary neighbour; together with
`delta(G)>=7` and Euler curvature this gives

\[
                         \sum_{v\in V(F)}\lambda(v)\ge2|F|+6.
\]

The two bounds are incompatible because `F` is nonempty.

## 7. Conclusion and scope

Every branch is covered: two unwitnessed duties give the exact literal
reflection immediately; otherwise two witnessed duties give the common
face, small orders are excluded, and order at least six ends in the audited
circle/curvature contradiction.  Shared portals are handled first by Hall
matchings and later by the complete-star versions of the common-face and
circle theorems.

The final gluing uses only the explicitly assumed proper-minor
six-colourability and the exact partition attained on the other shore.  The
scope statement is accurate: the proof needs `C` and `Q` in different rich
components, the exact paired state with its named literal adjacencies, and a
second full packet; it does not claim a generic demand-three or `(1,1)`
result.
