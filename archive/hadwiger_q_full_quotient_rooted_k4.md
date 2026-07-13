# A uniform rooted-`K_4` theorem for `Q`-full connected quotients

## 0. The general clique-full lifting principle

### Theorem 0.1 (clique-full quotient lifting)

Let `Q` be a clique of order `q` in a graph `G`.  Partition `G-Q` into
nonempty connected sets, each of which is collectively adjacent to every
vertex of `Q`, and let `R` be the simple quotient obtained by contracting
those sets.  If `R` contains a `K_r` minor, then `G` contains a
`K_{q+r}` minor.

#### Proof

Lift the `r` quotient branch sets through the contractions.  They are
disjoint, connected and pairwise adjacent.  Every lifted bag contains a
partition part and is therefore adjacent to every vertex of `Q`.  Add
the `q` vertices of `Q` as singleton branch sets.  The resulting `q+r`
bags form a clique model.  QED.

This is the label-free rooted-model principle used below.  Its content is
that collective contact is sufficient once it is attached to the pieces
*before* taking the quotient; no common portal vertex inside a piece is
required.  The case `(q,r)=(3,4)` is the `HC_7` normalization theorem.

## 1. Statement

Let `G` be a graph, let `Q={q_1,q_2,q_3}` be a triangle, and put
`H=G-Q`.  Let `a,b,c` be three distinct vertices of `H`, each adjacent
to all of `Q`.  Suppose

\[
 \mathcal P=(\{a\},\{b\},\{c\},D_1,\ldots,D_m)
                                                               \tag{1.1}
\]

is a partition of `V(H)` into connected sets and every `D_i` is
collectively adjacent to all three vertices of `Q`.  Contract every
member of `mathcal P` and delete loops and parallel edges; call the
resulting simple quotient `R`.

### Theorem 1.1 (`Q`-full quotient lifting)

If `R` contains a `K_4` minor, then `G` contains a `K_7` minor.

#### Proof

Lift the four branch sets through the contractions.  Each lifted branch
set is connected, the four are disjoint and pairwise adjacent, and each
contains at least one member of `mathcal P`.  Every member of
`mathcal P` is adjacent to all three vertices of `Q`.  Adding the three
singleton bags of `Q` gives a `K_7` model.  QED.

### Theorem 1.2 (four-connected quotient closure)

If `R` is four-connected, then `G` contains a `K_7` minor.

This theorem is independent of the number, size, treewidth, portal order,
and support masks of the connected pieces.  It is exactly the
contraction-first strengthening of the nested-triangle argument that is
valid without a carrier-splitting hypothesis.

In particular, in a `K_7`-minor-free graph every `Q`-full connected
quotient is `K_4`-minor-free, hence is a partial 2-tree.  The
four-connected branch is therefore excluded even without the root labels.
The proof below gives the stronger rooted localization requested by the
near-clique application.

## 2. Rooted proof of Theorem 1.2

Every vertex of `R` represents a connected set in `H` collectively
adjacent to every member of `Q`.  Write `d_i` for the vertex representing
`D_i`.

Fix `i` and apply Fabila-Monroy and Wood's rooted-`K_4` theorem to the
four roots

\[
                            a,b,c,d_i              \tag{2.1}
\]

in the four-connected graph `R`.  If `R` has a rooted `K_4` at these
vertices, lift its four branch sets through the contractions.  A connected
branch set of `R` lifts to the connected union of the corresponding
members of `mathcal P`; quotient adjacencies lift to literal edges of
`H`.  Each lifted branch set contains at least one member of `mathcal P`
and is therefore adjacent to all three vertices of `Q`.  The four lifted
bags together with

\[
                         \{q_1\},\{q_2\},\{q_3\}
                                                               \tag{2.2}
\]

form a `K_7` model.

Assume no such rooted model exists for any `i`.  The rooted theorem says
that `R` is planar and, for every `i`, the four vertices
`a,b,c,d_i` lie on a common face.  Since `R` is four-connected it is
three-connected, so its plane embedding is unique up to reflection and
each face has a simple boundary.  Two distinct faces of a
three-connected plane graph share at most an edge.  Hence the faces
containing `a,b,c,d_i` for the different indices `i` are all the same:
they already share the three distinct vertices `a,b,c`.

Thus one face contains

\[
                         a,b,c,d_1,\ldots,d_m,
\]

which is every vertex of `R`.  Therefore `R` is outerplanar.  A simple
outerplanar graph has a vertex of degree at most two, whereas a
four-connected graph has minimum degree at least four.  This is a
contradiction.  (If `m=1`, then `R` has only four vertices and cannot be
four-connected in the first place.)  The rooted model, and hence the
`K_7` minor, is unavoidable.  QED.

## 3. Exact contraction-first residue

### Corollary 3.1 (a target-free quotient has a carrier cut)

Assume additionally that `H` is four-connected and `G` has no `K_7`
minor.  Then `R` is `K_4`-minor-free and has a separator of order at most
two.  Every such
separator contains at least one vertex `d_i` representing a nonsingleton
or otherwise contracted piece.

Indeed Theorem 1.1 makes `R` a connected partial 2-tree.  Since
`|V(R)|>=4`, it is not three-connected and has a separator of order at
most two.  A separator containing
only vertices among `a,b,c` would lift unchanged to a separator of `H`
of order at most three, contrary to four-connectivity.

The lift of a separator containing `d_i` contains the whole carrier
`D_i`; its order is not bounded by three.  Thus this is a genuine
**carrier adhesion**, not yet an ordinary separator of `G` of order at
most six.

### Corollary 3.2 (maximal full-piece normal form)

Choose `mathcal P` with the maximum possible number of connected
`Q`-full pieces.  In a `K_7`-minor-free graph, every separator of order at
most two in `R` contains a `Q`-indecomposable piece: a member of
`mathcal P` which cannot be partitioned into two nonempty connected sets
both adjacent to all three vertices of `Q`.

Indeed a decomposable member could be split to give a strictly finer
`Q`-full partition, contradicting the maximal choice.  Corollary 3.1 says
that at least one such member lies in every small quotient separator.

## 4. What this proves and what it does not

The theorem closes every contracted quotient containing a `K_4` minor;
equivalently, it confines the entire target-free quotient to treewidth at
most two.  In particular it closes the **four-connected contracted quotient**
branch without any support-mask enumeration and without requiring a
literal common portal vertex inside a complex piece.  The three literal
shell neighbours `a,b,c` are enough.

It also identifies the exact missing strengthening.  To obtain the
proposed trichotomy with an actual separator of order at most six, one
must prove:

> a `Q`-indecomposable piece appearing in a separator of the `Q`-full
> quotient either admits a label-preserving split, forces one globally
> coherent apex pair, or contains an actual separator which lifts with at
> most three vertices of `H`.

Four-connectivity alone cannot supply that statement.  Contracting a
connected carrier may turn a four-cut into a three-cut whose contracted
vertex represents arbitrarily many original vertices.  The octahedral
example in `hadwiger_triangle_carrier_contraction_dichotomy.md` is the
small sharp warning.  Seven-connectivity, faithful operation states, or
a minimum-fragment hypothesis must be used to turn the carrier adhesion
into an ordinary cut or a rooted split.
