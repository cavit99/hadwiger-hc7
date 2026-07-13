# The neutral separator forced by a nontrivial both-missing path

## Status

The endpoint-shadow exchange turns the nontrivial path branch into an
exact two-missing branch.  This note records the resulting ambient
separator, rather than continuing with path-portal enumeration.  The
whole path-side envelope is separated from the two twin bags by vertices
lying in only the four neutral branch bags.  Seven-connectivity therefore
forces at least seven literal neutral vertices and a multiply hit neutral
bag.  At equality the adhesion is full on both principal shores.

This is the exact input needed by a neutral-row split theorem.  It does
not itself split the multiply hit bag.

## Theorem 1 (four-row separator)

Let `G` be seven-connected and `K_7`-minor-free.  Let

\[
                  A,B,C,U_1,U_2,U_3,U_4
\]

be a deficient-first minimal, not necessarily spanning, labelled
`K_7^vee` model whose nontrivial deficient bag `A` is the normalized
path.  Let `X` be the union of `A` and every component outside the model
union which has a neighbour in `A`.  Then

\[
          X\text{ is connected},\qquad
          E(X,B\cup C)=\varnothing,                       \tag{1.1}
\]

and

\[
             S=N_G(X)\subseteq U_1\cup U_2\cup U_3\cup U_4,
             \qquad |S|\ge7.                              \tag{1.2}
\]

The graph `G-S` has one component containing `X` and another containing
`B union C`.  In particular, some neutral bag contains at least two
distinct vertices of `S`, and every member of `S` has an actual neighbour
in `X`.

### Proof

The set `X` is connected because every added exterior component is
connected and has an edge to `A`; different such components need not be
adjacent.  The target-free exterior conclusion of the endpoint-shadow
theorem says that `A` and every one of these components are anticomplete
to both twins.  This proves (1.1).

An exterior component not included in `X` has no edge to `A` and no edge
to an included exterior component, because distinct components outside
the old model union are anticomplete.  Hence every neighbour of `X`
outside `X` lies in an old model bag.  It lies in neither twin by (1.1),
so it lies in one of the four neutral bags, proving the containment in
(1.2).

By definition, deleting `S` leaves `X` as a connected component.  The
nonempty connected bags `B,C` are disjoint from `S` and adjacent to each
other, so they lie together in a different component of `G-S`.
Thus `S` is an actual vertex separator; seven-connectivity gives
`|S|>=7`.  Four neutral bags cover `S`, so one contains at least
`ceil(7/4)=2` distinct members.  Finally `S=N_G(X)` makes every member a
literal `X`-portal. \(\square\)

## Theorem 2 (exact-seven fullness)

If `|S|=7` in Theorem 1, every vertex of `S` has a neighbour in every
component of `G-S`.  In particular the two principal shores `X` and the
component containing `B union C` are both full to the adhesion.

### Proof

Every `s in S` has a neighbour in `X` by the definition of `S`.  Let `D`
be any other component of `G-S`.  If `s` had no neighbour in `D`, then
`S-{s}` would separate `D` from `X`: after deleting the other six cut
vertices, the surviving vertex `s` has no edge to `D`, and distinct
components of `G-S` have no edges between them.  This would be a
separator of order six, contrary to seven-connectivity. \(\square\)

## Uniform form

The counting mechanism is parameter-free.  If a connected carrier in a
`k`-connected host is anticomplete to `d` bags of a foreign clique model
and every exterior component incident with the carrier shares those
absences, then its full envelope is separated from those `d` bags by
vertices in the remaining contacted bags.  If `r` contacted bags cover
the separator, one of them contains at least `ceil(k/r)` literal carrier
portals.  At separator order exactly `k`, every cut vertex is full to
every component.

For the `HC_7` equality cell, `(k,r)=(7,4)`, so a two-portal neutral row
is unavoidable.  Closing the branch now requires a label-preserving
split of that row (or a proper-minor state splice), not another
enumeration of exterior path pieces.
