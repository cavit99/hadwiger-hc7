# Three-guard and rooted-page normalization for the `K_3\vee C_4` residue

## Status and proof-spine role

The principal result of this note is a three-guard normalization.  Once
one actual vertex is selected from each of the three common rows, local
crossless web pieces do **not** have to be embedded with one globally
compatible rotation.  It is enough that they form a clique-adhesion tree
of four-colourable torsos.  Their four-colourings align by palette
permutations, and the audited uniform Strong-`HC_4` lifting theorem turns
the resulting three-vertex deletion into a literal `K_7` model.

This removes two formerly live difficulties at once: overfull facial
triangles and incompatible planar rotations.  Both matter for proving
that a union is planar; neither matters for four-colour gluing across an
actual clique.

The note also proves the constructive normalization available once two
adjacent vertices have been extracted from two common rows as literal
model-universal roots.  It removes an unbounded family of row lobes at
once.  In a `K_7`-minor-free host, all the lobes left after deleting the
two roots have one common diagonal type, except possibly for one unique
four-terminal web page.

The theorems are label-free apart from the cyclic order of four rim bags.
They do **not** yet prove that three arbitrary nonsingleton triangle rows
have a transversal whose deletion yields the required clique-adhesion
tree.  That is now the exact lobe-median/state step needed for the full
`HC_7` normalization.  No quotient separator is treated as an actual
clique adhesion.

## 0. The three-guard four-colour terminal

We first record the structural gain which changes the endgame.

### Lemma 0.1 (four-colour gluing on a clique tree)

Let `H` have a tree decomposition `(T,{V_t:t in V(T)})` such that

1. every edge of `H` has both ends in some `V_t`;
2. the bags containing any fixed vertex form a connected subtree of `T`;
3. every adhesion `V_t cap V_u`, for `tu in E(T)`, induces a clique in
   `H`; and
4. every graph `H[V_t]` is four-colourable.

Then `H` is four-colourable.

The same conclusion holds if each `H[V_t]` is replaced by a
four-colourable torso containing all adhesion-clique edges.

#### Proof

Root `T` and four-colour the root torso.  Suppose the parent side has
already been coloured and let `t` be a child with adhesion `S`.  Choose
an arbitrary four-colouring of the child torso.  Both the old and new
colourings are injective on `S`, because `S` is a clique.  Therefore a
permutation of the four colour names sends the child's colour on every
vertex of `S` to its already fixed colour.  Apply that permutation to
the whole child torso.

Continue away from the root.  The running-intersection property makes
all previously coloured overlap vertices lie in the parent adhesion, so
the procedure is consistent.  Every edge is checked in a torso by item
1.  The resulting colouring of the union is proper. \(\square\)

There is deliberately no bound on the number of pages using one triangle.
For example, arbitrarily many planar pieces may be glued on one triangle:
the union need not be planar, but all pieces can use the same three
distinct boundary colours and a common fourth colour elsewhere.

### Theorem 0.2 (three-guard crossless normalization)

Let `G` satisfy `chi(G)>=7`, and let `A` be a set of at most three actual
vertices.  Suppose `G-A` has a clique-tree presentation satisfying
Lemma 0.1 in which every torso is one of the following:

1. a planar graph;
2. an actual subgraph of a crossless web in which every original vertex
   belongs to the planar rib (the edge-only completion may still contain
   empty facial cells); or
3. any other graph with an exhibited proper four-colouring.

Then `G` contains a literal `K_7` minor.

#### Proof

A torso in item 1 is four-colourable by the Four Colour Theorem.  The
rib remaining in item 2 is planar, and edge deletion preserves
four-colourability.  Item 3 is four-colourable by hypothesis.  Lemma 0.1
therefore gives

\[
                              \chi(G-A)\le4.                \tag{0.1}
\]

Apply the audited uniform clique-apex lifting theorem
`../results/hc7_three_apex_planar_endgame.md`, Lemma 0, with
`(r,s)=(4,3)`.  Strong Hadwiger is proved for four colours, so (0.1) and
`|A|<=3` yield a literal `K_7` minor. \(\square\)

### Corollary 0.3 (one guard per common row suffices)

In the `K_3\vee C_4` residue, let

\[
                         a_i\in R_i\quad(i=1,2,3).         \tag{0.2}
\]

If every target-free lobe of the four cycle bags and the three row
remainders belongs, after deleting `A={a_1,a_2,a_3}`, to a
four-colourable crossless torso and all interfaces between those torsos
are **actual clique adhesions** in a tree decomposition, then `G` has a
`K_7` minor.

Thus a successful normalization no longer has to find two universal
vertices, make `G-A` planar, synchronize rural rotations, or bound the
number of pages on a facial triangle.  It has to find the three actual
vertices (0.2) and convert every noncrossing lobe interface to an actual
clique adhesion.  A non-clique interface must instead return the matched
proper-minor partition carriers.

#### Proof

Apply Theorem 0.2. \(\square\)

## 0.4 A literal model-universal root from a tree-convex row

The next theorem discharges the root-extraction step for an unbounded
class of common rows.  It uses actual portal vertices, not colours.

Let `R` be one of the three common row bags and let

\[
             B_1,B_2,B_3,B_4,S_1,S_2                    \tag{0.3}
\]

be its six neighbouring bags: the four cycle bags and the other two
common rows.  Fix a spanning tree `T` of `G[R]` and put

\[
                         P_Q=N_R(Q)                       \tag{0.4}
\]

for every bag `Q` in (0.3).  Call the row **tree-convex** when every
nonempty actual portal set `P_Q` induces a connected subtree of `T`.

### Lemma 0.4 (a full row split gives `K_7`)

Suppose an edge `e` of `T` has the property that both components
`R^-`,`R^+` of `T-e` meet every one of the six portal sets (0.4).  Then
`G` contains a literal `K_7` minor.

#### Proof

The four bags

\[
                         R^-,R^+,S_1,S_2                 \tag{0.5}
\]

are connected and pairwise adjacent.  The first two are adjacent across
`e`; each meets `S_1,S_2` by hypothesis; and `S_1S_2` is an old edge of
the common-row triangle.

Write the four cycle bags in order as `B_1,B_2,B_3,B_4`.  They contain
the following literal `K_3` model:

\[
                         B_1\cup B_2,\qquad B_3,\qquad B_4. \tag{0.6}
\]

The first set is connected through the cycle edge `B_1B_2`; its edges
to the last two sets are supplied by `B_2B_3` and `B_1B_4`, and the last
two are adjacent through `B_3B_4`.  Every bag in (0.5) meets every bag
in (0.6), because both tree shores meet all four cycle portal sets and
the two unchanged common rows are complete to the cycle at model level.
Thus (0.5)--(0.6) are seven disjoint connected pairwise adjacent branch
sets. \(\square\)

### Theorem 0.5 (tree-convex Helly root extraction)

Let `R` be a tree-convex common row in a `K_7`-minor-free
`K_3\vee C_4` model.  If its six portal subtrees (0.4) are pairwise
intersecting, then there is a **single actual vertex**

\[
                           a_R\in R                         \tag{0.7}
\]

which has a neighbour in every one of the six other model bags.

More generally, exactly one of the following holds for a tree-convex
row:

1. `G` has a `K_7` minor;
2. the model-universal actual root (0.7) exists; or
3. two named actual portal subtrees `P_Q,P_{Q'}` are disjoint, and every
   `P_Q`--`P_{Q'}` path in the fixed spanning tree crosses the unique tree
   corridor between them.

#### Proof

Subtrees of a tree have the Helly property.  If the six portal subtrees
are pairwise intersecting, their total intersection

\[
                              K=\bigcap_QP_Q               \tag{0.8}
\]

is a nonempty connected subtree of `T`.  If `K` contained an edge `e`,
then every `P_Q`, being connected and containing both ends of `e`, would
meet both components of `T-e`.  Lemma 0.4 would give a `K_7` minor.
Target-minor exclusion therefore makes `K` a single vertex `a_R`.
Membership in every `P_Q=N_R(Q)` says literally that `a_R` has a
neighbour in every other bag.  This proves (0.7).

If the portal subtrees are not pairwise intersecting, choose a disjoint
   pair.  In a tree their unique connecting corridor contains an edge whose
   deletion separates the two entire subtrees.  The unique tree path between
   them crosses that corridor, giving item 3.  Non-tree edges are not claimed
   to be blocked.  These alternatives
are exhaustive. \(\square\)

### Corollary 0.6 (three actual guards in the convex-row cell)

If all three common rows are tree-convex and have pairwise-intersecting
six-portal families, then a `K_7`-minor-free host has an actual transversal

\[
                           A=\{a_{R_1},a_{R_2},a_{R_3}\},
                           \qquad |A|\le3.                 \tag{0.9}
\]

No adjacency between the selected vertices is required.  If `G-A` has
the crossless clique-tree presentation of Corollary 0.3, Theorem 0.2
gives a literal `K_7` minor.

#### Proof

Apply Theorem 0.5 independently in the three disjoint rows, then apply
Corollary 0.3. \(\square\)

The surviving failure of this extraction theorem is not an arbitrary
portal mask: it is a named pair of disjoint convex portal classes in one
row, separated by one tree corridor.  An internal edge operation on that
corridor is therefore the exact place where the opposite six-block
partition-carrier splice must next be applied.

## 0.7 Lex-minimal rows have at most three tree arms

The tree-convex hypothesis is not automatic.  Lex-minimality nevertheless
gives a degree-free normalization for every common row.

Choose the labelled `K_3\vee C_4` model lexicographically by first
minimizing the number of absent pairs among the seven bags and then the
order of the common row `R` under consideration.  The comparison class
allows an old bag to be enlarged by vertices removed from `R`; no required
model edge may be lost.  Fix any spanning tree `T` of `G[R]`.

For a vertex set `L subseteq R` and a neighbouring bag `Q` from (0.3),
say that `L` **owns** `Q` if every actual `R-Q` edge has its `R`-end in
`L`.

### Lemma 0.7 (leaf ownership)

Every leaf `x` of `T` owns at least two of the six neighbouring-bag
duties.  Owner sets of distinct leaves are disjoint.  Consequently `T`
has at most three leaves.

#### Proof

The graph `R-x` is connected, since `T-x` is a spanning tree of it.
If `x` owns no duty, delete `x` from the model bag; every required row
edge survives, contradicting minimality.

Suppose `x` owns exactly one duty, say `Q`.  Move `x` from `R` into `Q`.
The enlarged bag is connected through an actual `x-Q` edge.  The residual
row is connected, and the old tree edge from `x` to `T-x` restores the
adjacency between the enlarged `Q` bag and the residual row.  Every other
row duty survives because it was not owned by `x`; every adjacency not
incident with `R` survives automatically.  If the move creates one of the
formerly absent diagonal edges, it decreases the primary defect count;
otherwise it preserves that count and decreases `|R|`.  Either conclusion
contradicts the lexicographic choice.  Hence every leaf owns at least two
duties.

One duty cannot be owned by two distinct leaves: the nonempty set of
actual `R-Q` edges cannot have all its `R`-ends equal to two different
vertices.  Thus the leaf owner sets are disjoint subsets of a six-element
set.  There are at most three of them. \(\square\)

### Corollary 0.8 (one actual three-arm guard per row)

For every lex-minimal common row there is an actual vertex `p_R` such
that `G[R]-p_R` has at most three components.  Hence the three common
rows have a transversal

\[
                        A=\{p_{R_1},p_{R_2},p_{R_3}\}      \tag{0.10}
\]

for which the row remainder has at most nine connected page components
before components joined by cross-row edges are merged.

#### Proof

A tree with two leaves is a path.  A tree with three leaves has one
degree-three vertex and all other vertices of degree at most two (use
`|L(T)|=2+sum_(d_T(v)>=3)(d_T(v)-2)`).  In the path case choose an
internal vertex when one exists, and otherwise an arbitrary vertex.  In
the three-leaf case choose the unique degree-three vertex.  Deleting the
chosen vertex from `T` leaves at most three tree components.  Every
component of the induced graph `G[R]-p_R` is a union of those tree
components, so there are at most three of them.  Apply this independently
to the three rows. \(\square\)

This is the promised nonenumerative page reduction.  Row order is
unbounded, but after deleting the three actual guards there are at most
nine row pages.  The Strong-`HC_4` terminal means that no global apex-pair
or compatible planar rotation has to be extracted from them.

## 0.9 Opposite diagonal tripods close literally

The following is the constructive discharge when two of those pages are
internally rich.  It is stated so that the two pages may lie in the same
common row or in different common rows.

Let the three common rows, after choosing the guards, have disjoint
connected retained cores `Z_1,Z_2,Z_3`, pairwise adjacent.  They need not
be singletons.  Suppose there are two disjoint page regions `L_0,L_1`,
disjoint from the `Z_i` and the four cycle bags, and, for `k=0,1`, three
disjoint connected sets

\[
                         A_k,B_k,C_k\subseteq L_k           \tag{0.11}
\]

which are pairwise adjacent within that triple.  Assume

\[
\begin{array}{c|cc}
 &B_k&C_k\\ \hline
k=0&U_0&U_2\\
k=1&U_1&U_3
\end{array}                                               \tag{0.12}
\]

means that `B_k,C_k` have actual edges to the displayed cycle bags, and
assume the union of the appropriate retained row core with `A_k` remains
connected.  After adding the `A_k` to their corresponding retained cores,
assume the resulting three row cores are still pairwise adjacent and each
is adjacent to every enlarged cycle bag; the contacts supplied by
`A_kB_k,A_kC_k` may be used for the two duties of its own tripod.

### Lemma 0.9 (opposite-tripod promotion)

Under (0.11)--(0.12), `G` contains a literal `K_7` minor.

#### Proof

Absorb `B_0,C_0,B_1,C_1` into `U_0,U_2,U_1,U_3`, respectively, and
absorb each `A_k` into its retained common-row core.  The four enlarged
cycle bags are connected.  Their rim adjacencies survive, while the
edges `B_0C_0` and `B_1C_1` repair the two diagonals.  They therefore
form a `K_4` model.  The three enlarged retained row cores are connected
and pairwise adjacent by hypothesis.  For each `k`, the edges from `A_k`
to `B_k,C_k` give that row core its two required new cycle contacts; all
other row-to-cycle contacts are retained by hypothesis.  Thus the three
row cores and four cycle bags are seven disjoint connected pairwise
adjacent sets. \(\square\)

If a page together with its guard attachment is two-connected and has
three distinct portal roots (guard side and the two opposite rim sides),
the standard rooted-`K_3` theorem supplies the triple (0.11).  Therefore
the only opposite-type page collision not covered by Lemma 0.9 is a
block-separable corridor or a loss of one retained row duty.  The former
is already a clique-tree input for Lemma 0.1; the latter is exactly an
owner lobe and hence the literal place for the lobe-median transfer or an
opposite proper-minor partition state.

## 1. The rooted wheel shell

Let

\[
             p,q,C,U_0,U_1,U_2,U_3                         \tag{1.1}
\]

be pairwise disjoint, with `p,q` vertices and the other five objects
nonempty connected vertex sets.  Indices on the `U_i` are modulo four.
Assume

1. `pq` is an edge;
2. `C` is adjacent to every `U_i`;
3. `U_i` is adjacent to `U_{i+1}` for every `i`;
4. the only possibly absent pairs among the five core bags are

   \[
                         U_0U_2,\qquad U_1U_3;             \tag{1.2}
   \]

5. each of `p,q` has a neighbour in every one of the five core bags.

Thus the five core bags contract to the wheel `W=C\vee C_4`, while
`{p}` and `{q}` are two adjacent singleton bags complete to that wheel
at model level.

Let `mathcal L` be a family of pairwise disjoint, pairwise anticomplete,
connected sets, disjoint from (1.1).  In the intended application these
are the components left in two common rows after deleting `p,q`.  We do
not require a member of `mathcal L` to be anticomplete to the core.

For `L in mathcal L`, call it

* a **zero page** if `L` is adjacent to both `U_0,U_2`;
* a **one page** if `L` is adjacent to both `U_1,U_3`; and
* a **mixed page** if it is both a zero page and a one page.

A page which is neither zero nor one has its four-rim shadow contained
in one edge of the rim cycle and will be called **facial**.  Notice that
this last assertion concerns only the rim shadow: contacts with the hub
`C` are allowed.

The terminology is invariant under replacing a bag by an arbitrary
connected expansion society.  It records only which of the two missing
rim diagonals a connected page can repair.

## 2. Opposite pages give the literal `K_7`

### Lemma 2.1 (opposite-page promotion)

If there are distinct pages `L_0,L_1` such that `L_0` is a zero page and
`L_1` is a one page, then `G` contains a literal `K_7` model.

#### Proof

Use the seven branch sets

\[
 \{p\},\quad \{q\},\quad C,\quad
 U_0\cup L_0,\quad U_1\cup L_1,\quad U_2,\quad U_3.       \tag{2.1}
\]

The two enlarged bags are connected because `L_0` meets `U_0` and
`L_1` meets `U_1`.  They are disjoint because the pages and core bags
are disjoint.  The page contacts repair the two absent diagonals:

\[
       (U_0\cup L_0)U_2\ne\varnothing,qquad
       (U_1\cup L_1)U_3\ne\varnothing.                    \tag{2.2}
\]

All four rim-cycle adjacencies survive, the hub `C` meets all four rim
bags, and the two singleton roots meet every core bag.  Finally `pq` is
an edge.  Hence the seven sets in (2.1) are connected, disjoint and
pairwise adjacent.  \(\square\)

The proof uses no edge between `L_0` and `L_1`, and therefore works for
arbitrarily large pages and arbitrary internal topology.

### Corollary 2.2 (global monochromaticity outside a mixed page)

If `G` has no `K_7` minor, then:

1. no zero page and one page are distinct;
2. if a mixed page `M` exists, every other page is facial; and
3. if no mixed page exists, all nonfacial pages have the same diagonal
   type.

#### Proof

Item 1 is Lemma 2.1.  A mixed page has both types, so any distinct
nonfacial page has one of the two types and forms an opposite pair with
`M`; this proves item 2.  Item 3 is item 1 with no mixed page. \(\square\)

Thus arbitrary many lobes do not create arbitrary many states.  Before
using any planarity theorem, target-minor exclusion alone reduces their
defect support to one bit, with a single possible shared-page exception.

## 3. A mixed page is crossed or one web

For a mixed page `M`, form its four-terminal augmentation `Q(M)` as
follows.  Add distinct artificial terminals `t_0,t_1,t_2,t_3`; join
`t_i` precisely to the vertices of `N_M(U_i)`; and add the four frame
edges `t_it_{i+1}`.  Give the terminals the cyclic order

\[
                         t_0,t_1,t_2,t_3.                  \tag{3.1}
\]

The frame edges copy actual consecutive core-bag adjacencies.  They are
included only to make the terminal frame literal; a terminal-clean
crossing cannot use another terminal internally.

### Lemma 3.1 (mixed-page cross promotion)

If `Q(M)` has disjoint terminal-clean paths joining `t_0` to `t_2` and
`t_1` to `t_3`, then `G` contains a literal `K_7` minor.

#### Proof

Neither path can be a frame edge, since the two demanded pairs are the
diagonals of (3.1).  Delete the artificial terminal ends and replace the
first and last terminal edges by their corresponding actual portal
edges.  The remaining vertices of the first path form a connected set
`K_0 subseteq M` adjacent to `U_0,U_2`; the second similarly gives a
connected set `K_1 subseteq M` adjacent to `U_1,U_3`.  Terminal
cleanliness and disjointness of the two paths make `K_0,K_1` disjoint.

Now use (2.1) with `K_0,K_1` in place of `L_0,L_1`.  The same literal
adjacency check proves a `K_7` model. \(\square\)

### Theorem 3.2 (the unique mixed-page web)

Suppose `G` has no `K_7` minor.  If a mixed page `M` exists, then

1. `M` is the unique nonfacial page; and
2. the ordered tuple (3.1) is crossless.  Consequently the same-vertex
   generalized Two Paths Theorem gives an edge-only completion of
   `Q(M)` to a four-web with (3.1) as its frame.

#### Proof

The first assertion is Corollary 2.2(2).  Lemma 3.1 excludes a crossing.
The audited generalized Two Paths Theorem used in
`../results/hc7_guarded_cycle_web_exchange.md`, Theorem 2, then gives the
stated same-vertex web completion. \(\square\)

This is the promised replacement for a list of mixed portal patterns.
There is one connected society with one specified cyclic frame.  Inserted
facial cliques and the distribution of actual portal occurrences are
retained; they are not contracted away.

## 4. The rural terminal is a four-colour clique tree

We now state the expansion hypothesis exactly.  Put

\[
                         H=G-\{p,q\}.                     \tag{4.1}
\]

A **four-colour rooted-page presentation** means a tree decomposition
with distinguished core roles `c,u_0,u_1,u_2,u_3` such that:

1. the root torso contains the wheel
   `c\vee(u_0u_1u_2u_3u_0)` at model level;
2. every actual core bag and page society is contained in a torso;
3. every adhesion is an actual clique and the running-intersection
   property holds; and
4. every torso is four-colourable.  A sufficient certificate for item 4
   is a planar rib or an individually rural disk expansion.  Different
   torsos need not use compatible rotations.

This is weaker than one compatible plane expansion.  Repeated pages on
one triangle and opposite local rotations are allowed.  The actual-clique
condition is essential: colourings do not align across an arbitrary
nonclique boundary merely by permuting four colour names.

### Theorem 4.1 (rooted-page normalization)

Assume that the vertices and bags in (1.1), together with the members of
`mathcal L`, cover `V(G)`.  Then at least one of the following holds.

1. `G` contains a literal `K_7` minor.
2. There is no mixed page, all nonfacial pages have one common diagonal
   type.
3. There is one unique mixed page, its four-terminal society is the
   crossless web in Theorem 3.2, and every other page is facial.

Moreover, in either outcome 2 or outcome 3, if `H` has a four-colour
rooted-page presentation (using the one diagonal in outcome 2 or the
unique web as a torso in outcome 3), then

\[
                         \chi(G-\{p,q\})\le4.              \tag{4.2}
\]

Thus `G` is six-colourable.  A simultaneous rural disk system would also
make `G-{p,q}` planar, but planarity is no longer required.

#### Proof

If there are distinct pages of opposite type, Lemma 2.1 gives outcome 1.
If a mixed page is crossed, Lemma 3.1 gives outcome 1.  Otherwise
Corollary 2.2 and Theorem 3.2 give exactly the support descriptions in
outcomes 2 and 3.

When the corresponding four-colour rooted-page presentation exists,
Lemma 0.1 gives (4.2).  Use two fresh colours on `p,q`; hence
`chi(G)<=6`.  Equivalently, if `chi(G)>=7`, the uniform clique-apex lift
gives a literal `K_7` minor.
This proves every assertion. \(\square\)

### Corollary 4.2 (minor-minimal `HC_7` use)

In a hypothetical 7-contraction-critical, `K_7`-minor-free graph, the
rooted shell of Theorem 4.1 cannot have a four-colour clique-tree
presentation.  Consequently, after an adjacent model-universal pair has
been extracted, the only live event is a non-four-colourable torso, an
actual nonclique adhesion, or a proper-minor-state failure.  Rotation
mismatch and overfull clique adhesions are no longer live events, and
neither is another family of page support masks.

#### Proof

Outcome 1 contradicts `K_7`-minor-freeness.  Outcomes 2 and 3 give a
six-colouring, contradicting seven-criticality. \(\square\)

## 5. Application to the lobe-median residue

In the exceptional state of
`hc7_three_anchor_lobe_median.md`, write

\[
       C=R_3,quad (U_0,U_1,U_2,U_3)=(X,Y,D,R_4).          \tag{5.1}
\]

The quotient on these five bags is the wheel `C\vee C_4`; the two absent
rim diagonals are exactly `XD` and `YR_4`.  If two of the three common
rows can be rooted at adjacent actual vertices `p,q` satisfying item 5
of Section 1, the components left in those rows are precisely the pages
of this note.  Theorems 2.1 and 3.2 then show:

\[
\boxed{
 \begin{array}{c}
 \text{opposite row lobes or a mixed-page cross}
       \Longrightarrow K_7,\\[2mm]
 \text{otherwise one diagonal orientation or one unique web page.}
 \end{array}}
                                                               \tag{5.2}
\]

The two-root formulation shows that the lobe-median state has no residual
multi-lobe support combinatorics once literal universal roots happen to
exist.  The stronger three-guard route no longer asks for them.  Apply
Lemma 0.7 and Corollary 0.8 to the three common rows of a defect-minimal
nonspanning model and choose

\[
                         A=\{p_{R_1},p_{R_2},p_{R_3}\}.    \tag{5.3}
\]

The exact unfinished statement is now:

> **Three-arm clique/state lemma.**  For the at most nine row arms left
> by (5.3), every first interaction with a cycle-bag lobe either supplies
> the opposite tripods of Lemma 0.9, belongs to a four-colourable torso
> joined through actual clique adhesions, or lies on a full actual
> adhesion whose two proper-minor operations realize one common
> six-block partition.

The first alternative is a literal `K_7`.  The second is terminal by
Theorem 0.2, with no rotation or overfull-triangle compatibility still
required.  The third is terminal by the audited opposite
partition-carrier splice in
`../results/hc7_guarded_cycle_web_exchange.md`, Theorem 5.

This note proves the three-arm bound, the convex-row root subfamily, the
opposite-tripod branch, and the whole four-colour clique-tree terminal.
It does not prove the displayed three-arm clique/state lemma.  Its exact
live mechanism is a block-separable owner arm meeting a cycle bag across
a nonclique adhesion, with no matching opposite operation state.

## 6. Trust boundary

The following uses are safe.

* The branch sets in Lemmas 2.1 and 3.1 are literal and do not consume
  the singleton roots or the hub.
* Arbitrarily many components of the same diagonal type are covered by
  one statement; they are not enumerated.
* A mixed component is either crossed or one specified four-web.
* In the auxiliary two-root theorem the same two actual vertices are used
  globally; in the main theorem only the three-vertex deletion set (5.3)
  is needed.

The following inferences are **not** made.

* Collective adjacency of a nonsingleton row is not treated as one
  universal vertex.
* A planar quotient is not called a planar expansion.  For the main
  conclusion only an actual clique tree of four-colourable torsos is used.
* Several facial pages may meet one clique adhesion: their colours glue
  even when their plane embeddings do not.  No such gluing is claimed for
  a nonclique adhesion.
* A palette colour is not identified with a row label.  That precise
  noncommutation remains in the three-arm clique/state lemma above.
