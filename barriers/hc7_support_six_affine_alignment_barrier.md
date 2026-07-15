# Affine pair-cover barrier to private support-six alignment

**Status:** proved abstract barrier, with a proved graph-realization
terminal.  This note rules out a purely set-system extraction of three
contraction-clean split models.  It is not a counterexample to the global
support-six transversal theorem: if the whole affine pattern is realized by
actual `K_5` models in one graph, it already forces a `K_7` minor.

## 1. The false extraction principle

Let a **decorated six-support** be a six-set `A` with a distinguished
two-set `e_A` (the prospective split edge); the other four vertices are the
prospective singleton rows.  Three decorated supports are
**contraction-clean** only if

\[
 e_{A_i}\cap(A_j\cup A_k)=\varnothing
 \qquad(\{i,j,k\}=\{1,2,3\}).                    \tag{1.1}
\]

Condition (1.1) is exactly the privacy condition used by simultaneous
split-edge contraction.  In particular, it also implies that every shared
support vertex is a singleton row in every model containing it.

The following tempting strengthening of the audited separated-triple
theorem is false even when every failed pair has a unique witness:

> A decorated family of six-supports with transversal number greater than
> two contains a contraction-clean separated triple.

## 2. The affine-plane obstruction

Let `X=F_3^2`, and let `L` be the twelve affine lines of the affine plane
`AG(2,3)`.  For each line `l`, put

\[
                         A_l=X-l.                       \tag{2.1}
\]

Thus every `A_l` has order six.  Mark an arbitrary two-set
`e_l subset A_l` as its split pair.  One may additionally put any one of
the four locally admissible deficiency decorations on
`A_l-e_l`; none of the assertions below uses that choice.

### Theorem 2.1 (unique witnesses without private alignment)

The family

\[
                         F=\{A_l:l\in L\}              \tag{2.2}
\]

has all of the following properties.

1. `tau(F)=3`.
2. Every two distinct supports meet in three or four vertices.  Hence every
   triple is a separated triple in the sense of the small-support
   extraction theorem.
3. Every two-set `P subset X` has a unique avoiding support in `F`.
4. `F` contains no full seven-vertex top and no full six-vertex family from
   the near-identical-family classification.
5. No three distinct decorated members are contraction-clean, regardless
   of how their split pairs were marked.  Indeed, no selected six-support
   has even two vertices private from the other two supports.
6. No three supports have a common four-set, so the common-singleton-`K_4`
   composition theorem cannot apply either.

#### Proof

Every pair of points of `AG(2,3)` lies on a unique affine line.  Therefore,
for every two-set `P`, the support complementary to the line through `P`
is disjoint from `P`, and it is the unique such support.  This proves item
3 and the lower bound `tau(F)>2`.  A noncollinear triple of points meets
every `A_l`, since it is contained in no affine line.  Hence `tau(F)=3`.

Two affine lines are either disjoint or meet in one point.  Consequently

\[
 |A_l\cap A_m|=9-|l\cup m|\in\{3,4\}             \tag{2.3}
\]

for distinct `l,m`, proving item 2.

If a six-support `A_l` were contained in a fixed seven-set `U`, the
two-set `X-U` would be contained in `l`.  There is only one line through
that pair, so at most one member of `F` is contained in `U`.  Thus no full
seven-vertex top occurs.  All members of `F` have order six, so the full
six-vertex family made from five-sets does not occur.  This proves item 4.

For three distinct lines `l,m,n`, direct complementation gives

\[
 A_l-(A_m\cup A_n)=(m\cap n)-l.                    \tag{2.4}
\]

The right side has order at most one.  It therefore cannot contain the
two-set `e_l`.  This proves item 5 simultaneously for every possible split
decoration.

Finally, three distinct affine lines have union of order at least six.
Therefore

\[
 |A_l\cap A_m\cap A_n|=9-|l\cup m\cup n|\le3,     \tag{2.5}
\]

which proves item 6. \(\square\)

Theorem 2.1 is stronger than the elementary eight-point obstruction made
from all six-subsets of an eight-set.  The affine family contains no full
near-identical top, every pair has an exact unique failed-pair witness, and
all of its triples already satisfy the best available support-intersection
bounds.  Thus neither failed-pair witnesses nor the audited set-system
classification can force private split edges.

## 3. Genuine realization of the affine pattern is terminal

The abstract obstruction cannot be promoted verbatim to a graph-minor
counterexample.

### Lemma 3.1 (four points do not block the affine plane)

Every set of at most four points of `AG(2,3)` is disjoint from an affine
line.

#### Proof

It is enough to consider four points.  If no three are collinear, the four
points meet

\[
                         4\cdot4-\binom42=10
\]

of the twelve lines: every point lies on four lines and every pair accounts
for the unique line counted twice.  If three points lie on one line, those
three meet that line and nine other lines.  The fourth point adds only the
line through it parallel to the first line; its other three lines already
join it to the three collinear points.  Thus at most eleven lines are met.
In either case some line is disjoint. \(\square\)

### Lemma 3.2 (complement form of a spanning six-vertex model)

If a six-vertex graph `J` has a spanning `K_5` model, then
`overline J` is a star forest with at most two nontrivial components.  In
particular `overline J` contains neither a triangle nor a three-edge path.

#### Proof

The five branch bags have sizes `(2,1,1,1,1)`.  Write the two-vertex edge
bag as `{x,y}` and the four singleton rows as `Q`.  In the complement,
`Q` is independent, `xy` is absent, and no `q in Q` is adjacent to both
`x` and `y`, because the edge bag must be adjacent to the singleton bag
`{q}` in `J`.  Hence all complement edges form two vertex-disjoint stars
centred at `x,y`. \(\square\)

### Lemma 3.3 (nine-vertex star-forest complement)

If `D` is a star forest on nine vertices, then `overline D` has a `K_7`
minor.

#### Proof

Let the nontrivial star components have centres `c_1,...,c_r`, and let
`Y` be the set of all leaves and isolated vertices.  Then `Y` is a clique
in `overline D` and `|Y|=9-r`.  Since every nontrivial component has at
least two vertices, `r<=4`.

If `r<=2`, the clique `Y` has order at least seven.  If `r=3`, use the six
vertices of `Y` as singleton bags and `{c_1,c_2,c_3}` as a seventh bag.
The centres form a clique in `overline D`; the centre bag is adjacent to
each leaf because it contains two centres other than the leaf's own
centre.  If `r=4`, use the five vertices of `Y` as singleton bags and
partition the four centres into two two-vertex bags.  Both bags are
connected and adjacent, and each is adjacent to every leaf through the
centre different from that leaf's own centre.  These are seven pairwise
adjacent connected bags. \(\square\)

### Theorem 3.4 (four-cover support composition)

Let `G` be a graph and let `X` have order at least nine.  Suppose `A` is a
family of six-subsets of `X` such that

1. every set of at most four vertices of `X` is contained in some member of
   `A`; and
2. `G[A]` has a spanning `K_5` model for every `A in A`.

Then `G[X]` has a `K_7` minor.

#### Proof

Put `D=overline{G[X]}`.  If `D` contained a triangle or a three-edge path,
its vertex set `Y` would have order at most four.  Choose `A in A` with
`Y subseteq A`.  The same forbidden subgraph would occur in `D[A]`,
contrary to Lemma 3.2.  Hence `D` has neither a triangle nor a three-edge
path.

Every connected graph which is not a star contains a triangle or a
three-edge path: take a shortest cycle if it is not a tree, and a longest
path if it is a tree.  Thus `D` is a star forest.  Restrict `D` to any
nine vertices of `X` and apply Lemma 3.3.  This gives a `K_7` minor in
`G[X]`. \(\square\)

### Corollary 3.5 (affine support realization forces `K_7`)

Let `G` be any graph containing a nine-set `X` identified with
`AG(2,3)`.  If, for every affine line `l`, the graph `G[X-l]` has a
spanning `K_5` model, then `G[X]` has a `K_7` minor.

#### Proof

By Lemma 3.1, the twelve six-sets `X-l` cover every set of at most four
vertices of `X`.  Apply Theorem 3.4. \(\square\)

## 4. Consequence for the active interface

The correct next composition theorem cannot promise private or
contraction-clean split edges merely from

* `tau(S_{<=6})>2`,
* the full failed-pair witness family,
* the pairwise separated-support conclusion, and
* the four local split-edge deficiency types.

The affine family satisfies the strongest possible pair-witness condition
and still defeats that conclusion.  The graph-specific terminal in Theorem
3.4 (with Corollary 3.5 as the exact affine instance) shows the viable
replacement shape:

\[
 \boxed{\text{private/row-compatible composition}
        \quad\text{or}\quad
        \text{a low-codegree pair-cover design forcing }K_7.}
\]

At minimum, simultaneous-contraction work should weaken privacy to
**row compatibility**: contracting one marked edge is harmless to another
model whenever its two endpoints do not occupy two distinct rows of that
model.  Literal support privacy is sufficient but, by Theorem 2.1, is too
strong to be a general extraction target.
