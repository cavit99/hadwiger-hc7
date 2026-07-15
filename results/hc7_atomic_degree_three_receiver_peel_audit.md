# Audit: atomic degree-three receiver peel

**Verdict:** GREEN with the one-sided-receiver limitation stated in the
theorem.

The relative-cut calculations are correct: the singleton side has defect
at most its internal degree, and `A-v` has at most the single internal
neighbour `v` outside it.  Fullness makes the two defect sets disjoint.

The bipartition analysis is also correct as a sufficient-case elimination.
With three `Y`-forced literals and at most one `X`-forced literal, every
pattern is resolved after deleting at most one forced literal except the
possible `2:1` split in which the `X`-forced literal lies in the majority
class.  The result correctly does not claim that this remaining pattern is
itself an obstruction, because deletion may disconnect the frontier and
allow componentwise orientations.

In the residue, `q in D_Y-D_X` proves that `qv` exists and is the only
`A-q` edge.  The equality

\[
                     N_G(A-v)=\{v\}\cup(S-\{q\})
\]

uses connectedness of `A`, the definition of `D_Y`, and the absence of
`A-R` edges; all are available.  The far side is nonempty, so this is a
literal actual seven-boundary.

Contracting `qv` is a named proper-minor operation.  Its colouring restricts
intact to the closed `A-v` shore and gives an exact state there.  It does
not give an intact opposite-shore colouring or a reflected state.  The main
statement and scope section preserve this distinction, so no state-transfer
or packet-vector claim is hidden.
