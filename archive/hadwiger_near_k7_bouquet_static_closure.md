# Static closure of the exact-seven Hall bouquets

## 1. Outcome

The Hall-deficient residue in Sections 7--9 of
`hadwiger_near_k7_active_root_face_exchange.md` is empty.  The closure is
static: crossed minor states and the multi-shore star lock are not needed.

The operative boundary fact is shared by both one-complex
normalizations.  The six literal singleton labels contain the graph

\[
 J=K_6-\{ab,ac\},
 \qquad V(J)=\{a,b,c,r_1,r_2,r_3\}.                 \tag{1.1}
\]

In the `K_7^-` normalization there is only one missing singleton edge,
so (1.1) is a subgraph; in the `K_7^\vee` normalization it is exact.
Every dark lobe has two torso poles, is connected, and sees all six
literal labels except its one named missed row.

## 2. Three almost-complete bags need only a marked `K_4`

### Lemma 2.1 (three-mark `K_4` in the singleton core)

For any multiset of three marked vertices of `J`, there is a `K_4`
minor in `J` such that no branch bag is a singleton at a marked vertex.

#### Proof

It is enough to treat a three-element set `M` containing all distinct
marks.  Enlarge the distinct-mark set arbitrarily if it has order below
three.  Put `R={r_1,r_2,r_3}`.  The graph `J-a` is a `K_5`, and every
vertex of `R` is universal in `J`.

If `a notin M`, choose `r in M cap R`, which is nonempty because
`{b,c}` has order two.  Use `{a,r}` as one branch bag, the other two
members of `M` as a second branch bag, and the two remaining vertices as
singleton bags.  The second bag is connected inside `J-a`, the remaining
singletons lie in `J-a`, and the universal vertex `r` supplies every
adjacency from the first bag.

If `a in M` and `M={a,b,c}`, use

\[
             \{a,r_1\},\quad\{b,c\},\quad\{r_2\},\quad\{r_3\}.
                                                               \tag{2.1}
\]

Otherwise choose `r in (M-{a}) cap R` and write `M={a,r,m}`.  Use
`{a,r}`, pair `m` with any one unmarked vertex `u`, and take the last two
vertices as singletons.  The bag `{m,u}` is an edge because both of its
vertices lie in the `K_5=J-a`; the last two vertices lie there as well.

In every case the four bags are connected and pairwise adjacent, and
every member of `M` lies in a nonsingleton bag.  QED.

### Lemma 2.2 (three-lobe triangle completion)

Let `H_1,H_2,H_3` be disjoint connected pairwise adjacent sets.  Suppose
`H_i` sees every vertex of `J` except possibly one vertex `m_i`.  Then
`J union H_1 union H_2 union H_3` contains a `K_7` minor.

#### Proof

Apply Lemma 2.1 to the marks `m_1,m_2,m_3`.  Every one of its four
branch bags either has order at least two or is an unmarked singleton.
Thus every `H_i` is adjacent to every one of the four bags.  The three
sets `H_i` and those four bags are seven pairwise adjacent connected
branch sets.  QED.

## 3. The two-pole triple bouquet closes immediately

### Theorem 3.1 (two-pole bouquet closure)

Let `D_1,D_2,D_3` be three disjoint dark lobes with the same two torso
poles `p,q`.  Then `G` contains a `K_7` minor.

#### Proof

The three sets

\[
              \{p\}\cup D_1,\qquad
              \{q\}\cup D_2,\qquad D_3              \tag{3.1}
\]

are connected and disjoint.  They are pairwise adjacent: `q` sees
`D_1,D_3` and `p` sees `D_2,D_3`.  Each misses at most its lobe's one
literal row.  Lemma 2.2 gives the target.  QED.

No edge `pq`, no edge between lobes, and no pole--literal edge is used.

## 4. The three-pole four-bouquet

Let the pole set be `{p,q,s}` and let four lobe portal sets be two-subsets
of it.  If one portal pair occurs at least three times, Theorem 3.1
applies.  If all three pairs occur, select lobes `D_{pq},D_{ps},D_{qs}`.
Then

\[
 \{p\}\cup D_{pq},\qquad
 \{q\}\cup D_{qs},\qquad
 \{s\}\cup D_{ps}                                  \tag{4.1}
\]

form a triangle of connected bags: the cross adjacencies are respectively
supplied by `q`, `p`, and `s`.  Lemma 2.2 again applies.

The only remaining portal multiset is therefore

\[
             pq,pq,ps,ps.                            \tag{4.2}
\]

Write the corresponding lobes as `A_1,A_2,B_1,B_2`, and write `m(D)`
for the literal row missed by `D`.  Put

\[
                 M=\{m(A_1),m(A_2),m(B_1),m(B_2)\},
 \qquad U=V(J)-M.                                    \tag{4.3}
\]

### Lemma 4.1 (the four-helper frame)

If `J[U]` contains a triangle, the profile (4.2) gives a `K_7` minor.

#### Proof

Choose a triangle `T subseteq U`.  We may also choose a label
`x notin T` missed by at most one of the four lobes.

Indeed, if `|M|<=2`, then `|U|>=4`.  Every four-vertex induced subgraph
of `J` contains a triangle: if it contains `a`, its other three vertices
lie in the clique `J-a`, and otherwise it itself lies in that clique.
Choose `T` while leaving some `x in U-T`; this `x` is missed zero times.
If `|M|=3`, then `U=T`, and the four missed occurrences on three used
labels have multiplicities `(2,1,1)`.  Choose for `x` either label of
multiplicity one.

Interchange the two portal-pair groups and interchange lobes inside a
group so that the possible unique lobe missing `x` is `A_1`.  Use

\[
 \begin{aligned}
 P&=\{p\}\cup A_1,\\
 Q&=\{q,x\}\cup A_2,\\
 R&=\{s\}\cup B_1,\\
 Z&=B_2.
 \end{aligned}                                      \tag{4.4}
\]

These four bags are connected.  They form a `K_4`: `P-Q`, `P-R`, and
`P-Z` use respectively the `p,q,s` portal incidences, while `Q-R` and
`Q-Z` use the literal vertex `x`, and `R-Z` uses `s`.  Every lobe sees
all three vertices of `T`, so the four bags are each adjacent to the
three singleton bags in `T`.  The latter form a triangle.  Thus (4.4)
and the three vertices of `T` are a `K_7` model.  QED.

### Lemma 4.2 (the spent-pair frame)

If `J[U]` has no triangle, the profile (4.2) gives a `K_7` minor.

#### Proof

If `|M|<=2`, then `|U|>=4`, and every four vertices of `J` contain a
triangle.  Hence this case was already handled by Lemma 4.1.  There are
two cases left.

**Case 0: `|M|=4`.**  The four lobes have four distinct missed labels.
At least one of the four distinct misses lies in `R`.  Orient its
portal-pair group as the `A` group and take that lobe as `A_2`; in
particular `A_2` sees `a,b,c`.  Choose any `z in R`, and orient the
other group so that `B_2` does not miss `z`, which is possible because
at most one lobe misses `z`.

Put `x=a,y=z` and use

\[
 \begin{aligned}
 P&=\{p\}\cup A_1\cup B_1,\\
 Q&=\{q,x\}\cup A_2,\\
 R'&=\{s,y\}\cup B_2,
 \end{aligned}                                      \tag{4.5}
\]

together with the four singleton bags `J-{a,z}`.  The singleton bags
form a clique.  The two lobes in `P` have different missed labels and
therefore jointly see every singleton.  The bag `Q` sees every retained
label: if `A_2` misses a retained label, it lies in `R` and hence is
adjacent to `x=a`.  The universal literal vertex `y=z` repairs the one
possible missed contact of `B_2`.  The three large bags are connected
and pairwise adjacent through the two portal crosses and the edge `az`.
This is a `K_7` model.

We may therefore assume `|M|=3`.  Since `J[U]` is triangle-free, up to
interchanging `b,c` and permuting `R`, there are two possibilities.

**Case 1: `U={a,b,c}` and `M=R`.**  The four missed occurrences have
multiplicities `(2,1,1)`.  Let `z in R` be the repeated label.  Orient
the two portal-pair groups and their lobes so that `B_2` does not miss
`z` and so that either `m(A_1) ne m(B_1)` or both equal `z`.  This is
always possible: if both copies of `z` lie in one group, call the other
group the `B` group; if they are split between the groups, take those two
copies as `A_1,B_1` and take the non-`z` member of the `B` group as
`B_2`.

Put `x=a,y=z` and use

\[
 \begin{aligned}
 P&=\{p\}\cup A_1\cup B_1,\\
 Q&=\{q,x\}\cup A_2,\\
 R'&=\{s,y\}\cup B_2,
 \end{aligned}                                      \tag{4.6}
\]

together with the four singleton bags `V(J)-{x,y}`.  The three large
bags are connected.  Their pairwise adjacencies use the two portal
cross-edges and the literal edge `xy`.  The four singletons form a
`K_4` because `J-{a,z}` is complete.  The orientation condition says
that `P` misses no retained singleton.  If `A_2` misses a retained
neutral label, the literal `x=a` in `Q` repairs that contact; the
literal `y=z` likewise repairs the possible retained missed row of
`B_2`.  Hence all seven bags are pairwise adjacent.

**Case 2: `U={a,b,r_1}` and `M={c,r_2,r_3}`.**  The case with `b,c`
interchanged is symmetric.  Orient a portal-pair group as the `A` group
and choose `A_2` not to miss `c`; this is possible because `c` occurs at
most twice among the four misses.  Choose `B_1` so that
`m(B_1) ne m(A_1)` whenever `m(A_1) in {r_2,r_3}`.  This is possible:
if both `B` lobes had that same miss, it would already account for both
copies of the repeated value, so `A_1` could not have it.

Now put `x=c,y=b` and use the three bags (4.6), together with the four
singletons `J-{b,c}`.  The latter induce the clique on
`{a,r_1,r_2,r_3}`.  The lobe in `Q` sees `c=x`, every lobe sees `b=y`,
and `b,c` are adjacent.  If `A_2` or `B_2` misses a retained neutral
label, the spent vertex `c` or `b`, respectively, is adjacent to it.
Neither can miss `a`, since `a in U`.  The choice of `A_1,B_1` makes
`P` see every retained singleton.  Thus the displayed seven bags form a
`K_7` model.  QED.

### Theorem 4.3 (three-pole four-bouquet closure)

Four dark lobes whose two-element portal sets have union of order at
most three always give a `K_7` minor.

#### Proof

If a portal pair occurs three times, use Theorem 3.1.  If all three
pairs occur, use (4.1) and Lemma 2.2.  Otherwise the multiplicities are
`(2,2,0)`, and Lemmas 4.1--4.2 apply.  QED.

## 5. Consequence for the active-root exchange

### Corollary 5.1 (the rank-deficient bouquet residue is empty)

In either normalized one-complex near-`K_7` shell, four fixed dark lobes
cannot have portal rank below four in a `K_7`-minor-free graph.

#### Proof

Corollary 9.2 of `hadwiger_near_k7_active_root_face_exchange.md` reduces
rank deficiency to a two-pole triple bouquet or a at-most-three-pole
four-bouquet.  Theorems 3.1 and 4.3 give `K_7` in the two cases.  QED.

Accordingly, for four **distinct fixed off-torso lobes**, the active
portal family always has an SDR.  The remaining active-root obstruction
can only be a shared-lobe collision or an unusable attachment occurrence;
Hall rank deficiency is no longer a live state-exchange residue.

The verifier `near_k7_four_bouquet_verify.py` independently replays both
allocation templates on all `6^4=1296` missed-row profiles of (4.2), over
the weakest singleton core `K_6-{ab,ac}`.  It is a check of the proof,
not an additional hypothesis.
