# Independent audit: both-missing neutral separator

## Verdict

**GREEN.**  The envelope includes every whole exterior component incident
with the nontrivial deficient path.  Its open neighbourhood is therefore
an actual vertex set contained in the four neutral bags, not a collection
of contracted carriers.  Seven-connectivity gives the claimed order and
two-portal pigeonhole conclusion.  At order exactly seven, every adhesion
vertex is full to every component of the deleted graph.

## 1. The envelope is connected and twin-free

Let `M` be the union of the seven old model bags.  Each member used in
the envelope is a whole connected component of `G-M` having an actual
edge to `A`.  Unioning all of them with connected `A` therefore gives a
connected set `X`; the exterior components need not be mutually adjacent.

The independently audited endpoint-shadow Corollary 3 applies because
`A` is nontrivial and deficient-first minimal.  It says both that `A` is
anticomplete to `B,C` and that every component of `G-M` meeting `A` is
anticomplete to `B,C`.  Hence all of `X` avoids both twins.  No stronger
target-free inference is being inserted here.

## 2. The full open neighbourhood lies in four actual bags

An exterior component omitted from `X` has no edge to `A`; otherwise it
would have been included.  It has no edge to an included exterior
component, because distinct components of the induced graph `G-M` are
anticomplete.  Thus a neighbour of `X` outside `X` must lie in one of the
six old foreign bags.  Twin-freeness excludes `B,C`, leaving

\[
                         N_G(X)\subseteq U_1\cup\cdots\cup U_4.
\]

This is a containment of actual vertices.  It neither contracts a neutral
bag nor counts one bag as one separator vertex.

## 3. Separation, order, and pigeonhole

Put `S=N_G(X)`.  Removing `S` leaves `X` as a component, since every edge
out of `X` ends in `S`.  The nonempty bags `B,C` are disjoint from `S`,
connected, and adjacent to one another, so `B union C` lies in a different
component of `G-S`.  Hence `S` is an actual separator with two nonempty
sides.  Seven-connectivity gives `|S|>=7`.

The four neutral bags are pairwise disjoint and cover `S`.  One therefore
contains at least `ceil(7/4)=2` distinct vertices of `S`.  Every member of
`S` has an actual neighbour in `X` by the definition of open
neighbourhood.

## 4. Equality gives full components

Assume `|S|=7`, fix `s in S`, and let `D` be any component of `G-S`
other than `X`.  If `s` had no neighbour in `D`, then deleting the six
vertices `S-{s}` would still separate `D` from `X`: different components
of `G-S` have no mutual edges, and `D` has no edge to the sole restored
cut vertex `s`.  The vertex `s` is on the `X` side because every member
of `S=N_G(X)` has a neighbour in `X`.  This produces an order-six
separator, contradicting seven-connectivity.

Thus every `s` meets every component of `G-S`.  In particular the
principal `X` shore and the component containing `B union C` are both
full to the actual adhesion.

## Scope

The lemma forces two literal `X`-portals in one neutral bag but does not
say that the bag can be split while retaining its other five model
adjacencies.  When `|S|>7` it also gives no fullness conclusion.  The next
step must use the internal normalization of the multiply-hit neutral bag,
a proper-minor equality state, or a port-labelled rural expansion.
