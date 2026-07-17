# Independent audit: paired colourful-set `K_4` barrier

**Audited source:** `hc7_two_colorful_sets_paired_k4_barrier.md`
**SHA-256:** `f9d41fdffb6ca5a7bbc54cd67a5491aae7e6fdf12d03c8725403b7a4abfb8e6f`
**Verdict:** **GREEN.**

The independent audit was performed on source hash
`e587c290440f63e191e2b6c450d4fb947dba3eab136588e2ac7ebfd47b7c798f`.
The only subsequent source change replaced the status phrase “separate
internal audit pending” by “separate internal audit GREEN”; the theorem,
construction, proof, and scope statements are unchanged.

The construction and every stated consequence are correct.  The join of
the two four-vertex paths is five-connected and four-chromatic; both named
sets are colourful; no `K_4`-minor model has all four branch sets meeting
both sets; the six displayed branch sets form a `K_6` model; and deleting
any fixed set of at most two vertices leaves a three-connected graph.

## 1. Chromatic number and vertex-connectivity

Let

\[
 A=a_0a_1a_2a_3,\qquad B=b_0b_1b_2b_3,
 \qquad J=A\vee B.
\]

Every colour used on `A` is forbidden on `B` by the join edges.  Each path
requires two colours, and independent two-colourings of the two paths give
a four-colouring of the join.  Hence

\[
                         \chi(J)=\chi(A)+\chi(B)=4.
\]

The connectivity calculation is also exact.  If a deleted set leaves at
least one vertex in each factor, every surviving vertex of one factor is
adjacent to every surviving vertex of the other, so the remainder is
connected.  A vertex cut must therefore delete one whole four-vertex
factor and then disconnect the other path.  This takes at least five
vertices.  Conversely, deleting all four vertices of `A` and either
internal vertex `b_1` or `b_2` disconnects the remaining part of `B`.
Thus

\[
                           \kappa(J)=5.
\]

This also checks the source's join-connectivity sentence without relying
on a formula for the connectivity of a join.

## 2. Colourfulness of `S` and `T`

In every proper four-colouring of `J`, the two factors have disjoint
palettes.  Each factor needs at least two colours, so each uses exactly two.
Because each path is connected and bipartite, its two-colouring is its
bipartition colouring up to exchanging the two colour names.

The edge `a_0a_1` displays both colours used on `A`, as does the edge
`a_2a_3`.  The vertices `b_0,b_3` are in opposite bipartition classes of
`B`, so together they display both colours used on `B`.  Consequently

\[
 S=\{a_0,a_1,b_0,b_3\},\qquad
 T=\{a_2,a_3,b_0,b_3\}
\]

each use all four colours in every proper four-colouring.  Both sets are
therefore colourful under the definition in the source.

## 3. Impossibility of a paired-rooted `K_4` model

Suppose four disjoint branch sets form a `K_4`-minor model and every branch
set meets both `S` and `T`.  Since each root set has order four, disjointness
forces every branch set to contain exactly one vertex of `S` and exactly
one vertex of `T`; all vertices of each root set are used.

The common roots are

\[
                         S\cap T=\{b_0,b_3\}.
\]

They lie in distinct branch sets.  Each of these two branch sets has
already used its unique `S`-vertex and its unique `T`-vertex.  Every vertex
of `A` lies in `S\cup T`, so neither branch set can contain a vertex of
`A`.  Each is consequently a connected interval of the path `B`, one
containing `b_0` and the other containing `b_3`.

Those two branch sets must be adjacent.  Two disjoint connected intervals
of a path, containing its opposite endpoints, are adjacent only if their
union is the whole path.  Hence these two branch sets use every vertex of
`B`.

The remaining two branch sets therefore lie wholly in `A`.  Each must
meet both

\[
 S\cap V(A)=\{a_0,a_1\}
 \quad\text{and}\quad
 T\cap V(A)=\{a_2,a_3\}.
\]

Any connected interval of `a_0a_1a_2a_3` meeting both displayed pairs
contains both middle vertices `a_1,a_2`.  Two such branch sets cannot be
disjoint.  This is the required contradiction, and it covers branch sets
of arbitrary size rather than only singleton or edge branch sets.

## 4. The explicit `K_6` model and its lift

The displayed family is

\[
 \{a_0\},\ \{a_1\},\ \{b_0\},\ \{b_1\},\
 \{a_2,b_2\},\ \{a_3,b_3\}.
\]

It consists of six pairwise disjoint connected sets.  The two `A`
singletons are adjacent along `a_0a_1`, and the two `B` singletons are
adjacent along `b_0b_1`.  Every `A` singleton is adjacent to every branch
set containing a `B` vertex, and every `B` singleton is adjacent to every
branch set containing an `A` vertex, by the join.  Finally, the last two
branch sets are adjacent along both `a_2a_3` and `b_2b_3`.  Thus every pair
of branch sets is adjacent and the family is a valid `K_6`-minor model.

If `J` lay disjointly beside a connected subgraph that dominated all its
vertices, that connected subgraph would be adjacent to every one of the
six branch sets.  Adding it would therefore give a `K_7`-minor model.  The
source correctly concludes that this barrier cannot be the
`K_6`-minor-free four-chromatic residue of the star-Kempe compression.

## 5. Three-connectivity after deleting at most two vertices

Fix `C subseteq V(J)` with `|C|<=2` and put

\[
                         A'=A-C,\qquad B'=B-C.
\]

Both factors have at least two vertices.  To test three-connectivity, let
`D subseteq V(J-C)` have `|D|<=2`.  If both `A'-D` and `B'-D` are nonempty,
the surviving join edges make `(J-C)-D` connected.

Suppose instead that `D` deletes all of `A'`.  Since `|A'|>=2` and
`|D|<=2`, equality holds throughout: `|A'|=2` and `D=A'`.  Therefore the
original set `C` consists of two vertices of `A`, so it contains no vertex
of `B`; hence `B'=B`.  No vertex of `B'` lies in `D`, and the surviving
graph is the connected path `B`.  The argument is symmetric if `D` deletes
all of `B'`.  Thus no set of at most two vertices disconnects `J-C`.

Since `J-C` has at least six vertices, this proves that it is
three-connected.  The source's proof uses the prospective cut `D`
implicitly; distinguishing it from the initially fixed set `C` makes the
quantifiers explicit and confirms the claimed conclusion.

Every three-connected graph on at least four vertices contains a `K_4`
minor.  For completeness, take a cycle avoiding a chosen vertex and use
the three-fan lemma to join that vertex to three distinct points of the
cycle; the resulting subdivision contains a subdivision of `K_4`.
Therefore `J-C` has a `K_4` minor for every `|C|<=2`.  Equivalently, no set
of at most two vertices meets the support of every `K_4`-minor model in
`J`.

## 6. Scope and assumptions

- Graphs are finite and simple; `P_4` denotes the path in the displayed
  vertex order, and `A\vee B` adds every edge between the two factors.
- A clique-minor model consists of pairwise disjoint nonempty connected
  branch sets that are pairwise adjacent.  A common root such as `b_0`
  counts simultaneously as the unique `S`-vertex and unique `T`-vertex of
  its branch set in the counting argument.
- Vertex-connectivity is used in its standard sense.  All graphs to which
  three-connectivity is applied have at least four vertices.
- The construction refutes only the proposed simultaneous two-set rooting
  theorem, even under five-connectivity.  It does not refute the ordinary
  one-set Strong Hadwiger theorem.
- Because `J` already contains a `K_6` minor, the construction does not
  satisfy the derived `K_6`-minor exclusion of the actual `HC_7` residue.
  It therefore does not refute a stronger paired-root theorem that retains
  that exclusion and the full contraction-critical host hypotheses.
- The final argument rules out a two-vertex transversal for all `K_4`
  minor supports in this abstract construction only.  It does not rule out
  a fixed-pair conclusion after lifting into the actual `HC_7` setting.

No correction to the audited source is required.
