# Fixed-root rural pages have no signed holonomy

## Status and role

This is an **audited theorem**.  It closes the
ordered-page composition problem whenever the 4-connected connector and
its two literal attachment roots remain fixed.

The conclusion is uniform: all private-row comparisons come from one
linear order on one facial arc.  A directed triangle, a context-conflicting
basis square, or any longer signed cycle therefore forces an actual
private rooted linkage.  In the no-`K_7^-` branch, the common-row
augmentation lemma turns that linkage into a terminal `K_7^-` model.

The theorem deliberately does not identify root pairs belonging to
different connectors.  That root/frame transport is the remaining global
holonomy edge.

## 1. Ordered portal constraints

Let `H` be a 4-connected graph, let `alpha,beta` be distinct vertices,
let `I` contain at least two labels, and let

\[
                         P_i\subseteq V(H)-\{\alpha,\beta\}
                         \qquad(i\in I)                  \tag{1.1}
\]

be nonempty, pairwise disjoint portal sets.  Let `Q` be a loopless directed
graph on `I` with nonempty arc set; its underlying undirected graph is
assumed connected.
For an arc `i -> j`, impose the **rural constraint**

\[
 \text{there are no disjoint paths joining }\alpha\text{ to }P_i
       \text{ and }\beta\text{ to }P_j.                 \tag{1.2}
\]

Here a path to a set may end at any member of that set.

## Theorem 1 (fixed-root ordered-page coherence)

Under (1.1)--(1.2), `H` is planar and in its unique plane embedding there
is one face `F` with the following properties.

1. `alpha,beta` and every vertex in `union_i P_i` lie on the facial cycle
   of `F`.
2. All portal sets lie on one open `alpha-beta` boundary arc `R` of `F`.
3. Orient `R` from `beta` to `alpha`.  For every arc `i -> j` of `Q`,
   every occurrence of `P_i` precedes every occurrence of `P_j` on `R`.

Consequently `Q` is acyclic, and all of its signed page relations are
restrictions of one global linear order.

### Proof

Fix an arc `i -> j` and vertices `x in P_i,y in P_j`.  The 4-connected
form of the Two Paths Theorem applied to the pairs `(alpha,x)` and
`(beta,y)` says that `H` is planar and that these four vertices occur in
alternating order on one facial cycle.  Since `H` is 4-connected, its
plane embedding is unique up to reflection.

Fix one arc `i_0 -> j_0` and representatives
`x_0 in P_{i_0},y_0 in P_{j_0}`; let `F` be their face.  Varying the
representative in either endpoint set cannot change the face: two
distinct facial cycles in a 3-connected plane graph cannot contain the
three distinct vertices `alpha,beta,x_0` (or
`alpha,beta,y_0`).  Hence all vertices of
`P_{i_0} union P_{j_0}` lie on `F`.

Now traverse a spanning tree of the underlying connected graph of `Q`.
Whenever a new label `k` is reached across an edge incident with a label
already placed on `F`, apply the same three-common-vertices argument to
that edge.  It places every member of `P_k` on the same face.  This proves
item 1.

For each arc `i -> j`, alternation of the pairs
`(alpha,x),(beta,y)` puts `x` and `y` on the same open
`alpha-beta` boundary arc.  Connectedness of the underlying graph of `Q`
therefore puts every portal set on one common arc `R`, proving item 2.

Choose the orientation of `R` so that it runs from `beta` to `alpha`.
For an arc `i -> j`, the only order on this arc which makes
`alpha,x,beta,y` alternate is that every `P_i` occurrence comes before
every `P_j` occurrence (with all inequalities reversed if the opposite
orientation for `R` was chosen).  This proves item 3.  A directed cycle
would demand a strict cyclic chain of positions on a line, which is
impossible. \(\square\)

## Corollary 2 (a signed cycle forces a literal private linkage)

Retain a fixed 4-connected `H` and fixed roots `alpha,beta`.  If a
collection of proposed rural constraints contains a directed cycle, then
at least one arc `i -> j` has disjoint `alpha-P_i` and `beta-P_j` paths.

In an overlapping rotation

\[
                         \{a,i\}\longrightarrow\{a,j\},
\]

the private-linkage augmentation lemma in
`../results/hc7_near_k7_common_row_rural_book.md` enlarges one of those paths to meet
the common portal class `P_a`.  Thus it supplies two rooted carriers
covering three of the four demand occurrences.  If the host has no
`K_7^-` minor, this is terminal.

### Proof

If every arc lacked its private linkage, Theorem 1 would make the directed
constraint graph acyclic.  Hence some arc has the linkage.  The last
assertion is exactly Lemma 2 and Corollary 2.1 of the cited note.
\(\square\)

## 2. The basis-exchange certificate is only a triangle or square

The missing pairs are the vertices of the basis graph `J(5,2)` of the
uniform matroid `U_{2,5}`.  An overlap transition

\[
                 \{a,b\}\longrightarrow\{a,c\}
\]

records a comparison `b <_a c`.  Reversing the transition reverses the
comparison.

## Lemma 3 (local flatness of signed basis exchanges)

For every context `a` and every unordered pair `{b,c}` disjoint from `a`,
suppose exactly one of `b<_a c` and `c<_a b` is assigned.  Thus each
contextual comparison is a total antisymmetric tournament sign; traversing
the corresponding basis edge in reverse reads the same sign backwards and
does not add a second comparison.  These signs arise from one global linear
order on the five row labels if and only if both of the following local
conditions hold.

1. **Star triangles are transitive.**  For fixed `a`, there are no
   distinct `b,c,d` with

   \[
                         b<_a c<_a d<_a b.               \tag{2.1}
   \]
2. **Basis squares are context-independent.**  For four distinct labels
   `a,d,b,c`,

   \[
                         b<_a c\quad\Longleftrightarrow\quad b<_d c.
                                                               \tag{2.2}
   \]

Therefore every failure of global signed coherence has a certificate on
either the three bases

\[
                         \{a,b\},\{a,c\},\{a,d\},        \tag{2.3}
\]

or the four bases

\[
                 \{a,b\},\{a,c\},\{d,c\},\{d,b\}.      \tag{2.4}
\]

### Proof

Necessity is immediate.  For sufficiency, define `b<c` using `b<_a c`
for any `a` outside `{b,c}`.  Condition (2.2) makes this independent of
the chosen context.  It is a tournament relation.  If it contained a
directed triangle `b<c<d<b`, choose either of the two labels `a` outside
`{b,c,d}`.  Condition (2.2) would reproduce that directed triangle in
the context `a`, contrary to (2.1).  Thus the tournament is acyclic and
hence is a linear order.  By construction it induces every assigned
comparison. \(\square\)

## Corollary 4 (fixed-root basis holonomy is flat)

Suppose the comparisons in Lemma 3 are all realized as absent private
linkages in one fixed 4-connected connector with one fixed ordered root
pair.  Then both (2.1) and (2.2) hold, so all transition signs come from
one global row order.

Conversely, a directed star triangle or a context-conflicting square
forces a private linkage on at least one of its edges by Corollary 2.

### Proof

Theorem 1 places every comparison on a single oriented facial arc, whose
ordinary linear order satisfies (2.1)--(2.2).  The converse is the
contrapositive, noting that a context conflict gives the two opposite
comparisons `b<c` and `c<b`, a directed 2-cycle. \(\square\)

## Trust boundary

The theorem proves the desired holonomy statement for a **fixed literal
connector and fixed literal roots**, under the stated pairwise-disjoint
portal-set hypothesis.  Abstract page signs alone are not enough: different
planar gadgets with different root pairs can realize inconsistent signs
while their disjoint union remains planar, and overlapping portal classes
require a separate common-portal absorption argument.

Accordingly, every genuine nontrivial `HC_7` holonomy must now do at least
one of the following:

1. change the two attachment roots;
2. change the 4-connected connector torso;
3. pass through a cutvertex/2-adhesion state; or
4. use the separate concentrated two-piece rotation.

The remaining global theorem must transport roots across those changes,
or match the equality states on the intervening actual adhesions.  It may
not infer a `K_7` from signed basis data alone.
