# Audit: atomic asymmetric `(5,6)` carrier closure

**Verdict:** GREEN.

## Hypothesis audit

The proof uses only the stated atomic data and the already audited adaptive
clique-reservoir theorem.  In particular, it does not identify palette
colours with boundary labels and does not require preservation of an older
exact state.

Because `X,Y` partition the `S`-full shore `A`, no boundary vertex can miss
both carriers.  Thus `D_X cap D_Y` is empty.  The unique edge `zu` and
`z in Y` correctly force `u in D_X-D_Y`.  The support bounds then give
exactly `|D_X|<=2` and `|D_Y|<=1`.

## List-colouring audit

There are only two structural cases.

1. `D_X` lies in one bipartition class.  Orient that class to `Y`; the only
   possible conflicting prescription is the single vertex of `D_Y`, which
   may be deleted.
2. `D_X` consists of two vertices in opposite classes.  Delete one of them
   so that the remaining `Y` prescription is opposite the possible `X`
   prescription.

The deleted set is always empty or a singleton and hence a clique.  All
surviving prescriptions agree with one global bipartition orientation, so
the resulting list-colouring is proper even if deletion disconnects `H`.

If an edge survives, it uses both labels.  If no edge survives, connectedness
of `H` forces the reservoir to be nonempty; among the six surviving vertices
at most two retain singleton lists, so a flexible vertex supplies the second
label.  The two seed classes are therefore both nonempty, as required by the
adaptive return theorem.

## Cut audit

For `X={v}`, the separator of the singleton has order
`d_A(v)+|N_S(v)|`; the nonempty rich shore lies outside it, so
seven-connectivity gives the first support bound.  For `Y=A-v`, its only
possible neighbour in `A-Y` is `v`, and adjacency follows from connectedness
of `A`; the rich shore again lies outside.  Hence `1+|N_S(Y)|>=7`.

Two-connectivity makes `A-v` connected for every `v`.  Since the old root
bound handles `z`, the minimum-degree conclusion follows.  The standard
two-degree-vertices property of two-connected outerplanar graphs then
excludes the whole outerplanar family.

## Scope audit

The proof does not claim the symmetric `(5,5)` case.  The displayed tree
really is a list-level obstruction to deleting one clique vertex, so the
stated boundary is genuine.  Nor does planarity imply outerplanarity; the
remaining rural case must contain an interior torso.
