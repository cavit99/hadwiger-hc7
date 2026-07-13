# Harmonica structure in a two-heavy rural contraction state

## Status

This note sharpens the audited active-face list splice in
`../results/hc7_near_k7_dynamic_locked_gate.md`.  It eliminates every
two-heavy state in which both heavy vertices see only four boundary
colours.  If exactly one is forced by all five non-contraction colours,
the only surviving planar list obstruction is a coloring harmonica.

The input beyond the audited note is the planar list-extension theorem of
Postle and Thomas, *Five-list-coloring graphs on surfaces III. One list
of size one and one list of size two*, Theorems 1.2 and 1.3.

## Setting

Let `K` be a connected plane graph with outer facial cycle `F`, and let
all vertices of `K` having neighbours in the actual adhesion `S=N_G(K)`
lie on `F`.  Contract `K` to `z` and fix a six-colouring `c` of `G/K`.
Put

\[
 \alpha=c(z),\qquad
 L(x)=\{1,\ldots,6\}-c(N_G(x)\cap S).
\]

Every vertex of `S` is adjacent to `z`, so no boundary vertex has colour
`alpha`; consequently `alpha in L(x)` for every `x in K`.  An interior
vertex of `K` has the full six-element list.  Call a facial vertex heavy
when it sees at least four boundary colours, equivalently when its list
has order at most two.

## Theorem 1 (two-heavy harmonica dichotomy)

Assume exactly two facial vertices `x,y` are heavy.  Then one of the
following holds.

1. `G` is six-colourable.
2. Exactly one of `L(x),L(y)` is the singleton `{alpha}` and the other
   has order two.  After interchanging `x,y` if necessary,
   \[
                      L(x)=\{\alpha\},\qquad |L(y)|=2,
   \]
   and the pair `(K,L)` contains a coloring harmonica from `x` to
   `y` in the sense of Postle--Thomas.
3. `L(x)=L(y)={alpha}`; equivalently both vertices see all five colours
   occurring on `S`.

Thus a non-six-colourable two-heavy state is not an arbitrary web: it is
either the explicit one-to-two-list harmonica or a two-vertex common-
colour forcing state.

### Proof

Every vertex of `F-{x,y}` is nonheavy and hence has a list of order at
least three.  Every vertex inside `F` has a list of order six, in
particular at least five.

If both `L(x),L(y)` have order at least two, the Two Lists of Size Two
Theorem (Postle--Thomas, Theorem 1.2) gives an `L`-colouring of `K`, even
when `x,y` are nonadjacent.  As in the audited list-splice theorem, this
colouring avoids the colour of every boundary neighbour and therefore
glues to `c` on `G-K`.  This is outcome 1.

Otherwise one of the two nonempty lists is a singleton.  Since every
list contains `alpha`, that singleton is `{alpha}`; call its vertex `x`.
If `|L(y)|=2`, Postle--Thomas Theorem 1.3 says that `K` is
`L`-colourable if and only if the pair `(K,L)` contains no coloring
harmonica from `x` to `y`.  Colourability again gives outcome 1, while
noncolourability gives outcome 2.  The sole remaining possibility is
that both lists are the singleton `{alpha}`, which is outcome 3.
\(\square\)

## Exact next use

A coloring harmonica is generated recursively by facial triangles and
two-colour democratic/dictatorial transitions.  The next proof-spine
step is concrete: align one triangle transition with the literal cyclic
portal order of the locked `L-H`, `R-Q` gate.  A transition that crosses
that order must give the protected fixed linkage; a transition that never
crosses must be shown to form one compatible rural strip and to expose
the same boundary equality state at its two ends.

The theorem does not address states with at least three heavy vertices or
the double-singleton state.  It also does not turn a harmonica into a
global two-apex pair without this literal portal comparison.

## Theorem 2 (four-connectivity excludes the harmonica)

Assume in addition that `K` is four-connected and that `F` contains a
system of distinct representatives of the four literal portal classes.
Then outcome 2 of Theorem 1 cannot occur.  Consequently, if `G` is not
six-colourable and the contraction state has exactly two heavy vertices,
both have list `{alpha}` and both see all five non-contraction colours on
the actual adhesion.

### Proof

The boundary of every face of a three-connected plane graph is an
induced cycle.  Thus the outer facial boundary `F` of `K` is an induced
cycle.  The four distinct portal representatives show that `|F|>=4`.

Suppose outcome 2 occurs, with `L(x)={alpha}`.  By the first recursive
clause in the definition of a coloring harmonica from a one-list vertex,
the contained harmonica has a triangle `xuv` satisfying

\[
 L(u)-L(x)=L(v)-L(x),\qquad |L(u)-L(x)|=2.                \tag{2.1}
\]

There is a containment subtlety: `u,v` are incident with the outer face
of the *contained harmonica*, and that alone would not put them on the
original cycle `F`.  The special total-contraction lists do.  Every list
contains `alpha`, because no boundary vertex has the contraction colour.
It follows from (2.1) that

\[
                   L(u)=L(v)=\{\alpha,\beta,\gamma\}
\]

for two colours `beta,gamma`; in particular both lists have order three.
Every vertex strictly inside `F` has the full six-element list under the
fully rural hypothesis.  Hence `u,v` already lie on `F`.  The vertex `x`
also lies on `F`, since it is one of the original heavy facial vertices.

But three vertices of an induced cycle of length at least four cannot be
pairwise adjacent: one edge of the triangle `xuv` would be a chord of
`F`.  This contradiction excludes the harmonica.  Theorem 1 then leaves
only the double-singleton outcome in a non-six-colourable exactly-two-
heavy state. \(\square\)

The phrase *contains a coloring harmonica* is nevertheless important.
The proof does not infer original faciality merely from containment; it
uses the exact inherited lists and the fact that every original interior
vertex has a six-element list.
