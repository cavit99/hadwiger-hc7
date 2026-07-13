# Double colour saturation does not force a doubly rooted `K_5`

## Status

At a critical edge `sw`, deleting the common colour class leaves a
5-chromatic graph `H`, and both `N_H(s)` and `N_H(w)` are saturated in
every five-colouring.  The tempting next assertion is that `H` therefore
has a `K_5` model every bag of which meets both neighbourhoods.  This
eight-vertex example disproves that assertion without the ambient
seven-connectivity/contraction-critical geometry.

The example is six-colourable and `K_7`-minor-free, so it is not an
`HC_7` counterexample.  It fixes the exact extra hypothesis a usable
rooted-model principle must exploit.

## Construction

Let

\[
 H=K_6-03
\]

on vertices `0,1,2,3,4,5`, and put

\[
 S=V(H)-\{3\},\qquad T=V(H)-\{0\}.
\]

Add adjacent vertices `s,w` with

\[
 N_H(s)=S,\qquad N_H(w)=T,
\]

and call the resulting graph `Q`.  Equivalently,

\[
 Q=K_8-\{s3,30,0w\};
\]

the three missing edges form the path `s-3-0-w`.

## Proposition 1 (both root sets are five-colour-saturating)

The graph `H` is five-chromatic, and in every proper five-colouring of
`H` both `S` and `T` use all five colours.

### Proof

The four vertices `1,2,4,5` form a clique and are complete to `0,3`.
Thus a five-colouring gives those four vertices four distinct colours and
must give the nonadjacent pair `0,3` the fifth common colour.  Both `S`
and `T` induce a `K_5`, so each uses all five colours.  \(\square\)

## Proposition 2 (there is no doubly rooted `K_5` model)

There are no five pairwise disjoint connected pairwise adjacent branch
sets in `H` each meeting both `S` and `T`.

### Proof

The intersection

\[
                         S\cap T=\{1,2,4,5\}
\]

has only four vertices.  A branch set meeting both `S` and `T` either
contains one of these four common vertices, or contains both exclusive
vertices `0,3`.  Five disjoint branch sets would force one bag of the
latter kind.  But `0,3` are nonadjacent, so every connected subgraph of
`H` containing both also contains a common vertex.  All five bags would
therefore require distinct vertices of the four-element intersection, an
impossibility.  \(\square\)

## Proposition 3 (`Q` is six-chromatic and `K_7`-minor-free)

### Proof

The vertices `s,w,1,2,4,5` induce a `K_6`, so `chi(Q)>=6`.  Colour
`1,2,4,5` distinctly, colour the nonadjacent pair `0,w` with a fifth
colour, and colour the nonadjacent pair `3,s` with a sixth.  Hence
`chi(Q)=6`.

Any `K_7` model in an eight-vertex graph either is a seven-vertex clique
or partitions all eight vertices into one two-vertex bag and six
singletons.  Deleting one vertex cannot cover all three edges of the
complementary path, so `Q` has no `K_7` subgraph.

In the second case, the two-vertex bag must be a vertex cover of the
complementary path.  Its possible size-two covers are

\[
                         \{3,0\},\quad\{s,0\},\quad\{3,w\}.
\]

The first pair is disconnected in `Q`.  The bag `{s,0}` is anticomplete
to the remaining singleton `3`, and `{3,w}` is anticomplete to the
remaining singleton `0`.  None is a valid clique-model bag.  Thus `Q`
has no `K_7` minor.  \(\square\)

## Consequence

The safe critical-edge reduction may record two five-colour-saturating
root sets, but saturation alone cannot turn them into labelled branch
sets.  A successful theorem must additionally use at least one of:

* seven-connectivity of the full host;
* the actual near-`K_7` carrier/row geometry;
* proper-minor state incompatibility across an adhesion; or
* a conclusion allowing the coherent two-apex alternative.
