# Independent audit: wholesale exterior-piece transfer

## Verdict

**GREEN after the incorporated scope corrections.**  Theorem 1 is a
valid label-preserving repartition of a spanning near-`K_7` model, and
Corollary 2 follows from deficient-bag minimality.  The conclusion removes
foreign-contacting pieces only from the deficient bag `A`: each such
piece is absorbed wholesale into one actual foreign bag.  It does not
split the piece between two labels and does not by itself solve a two-row
collision inside the enlarged foreign bag.

## 1. The comparison class is preserved

Let `K=K_i`, and choose `T=E` whenever `K` meets `E`; otherwise choose a
retained foreign bag met by `K`.  Set

\[
                         A'=A-K,\qquad T'=T\cup K.
\]

The fixed path `P`, its four endpoint-row edges, and the fixed missed twin
`D` are untouched.  Removing one complete member of the displayed
decomposition of `A-P` leaves the same kind of decomposition: `A'`
contains `P`, and every remaining connected piece is still attached to
`P` and anticomplete to the other pieces.  The minimization class must,
as the source states, permit enlargement of a retained foreign bag by a
whole old exterior piece.  Under that explicit class, the comparison is
admissible.

## 2. Connectedness, disjointness, and spanning

The literal `KT` edge makes `T'` connected.  The path `P` and the
remaining `K_j` make `A'` connected.  Since the old bags were disjoint
and `K` moves in its entirety from `A` to `T`, the new bags remain
pairwise disjoint and have the same union as before.  Thus the model is
still spanning.

The old `PK` attachment is now an `A'T'` edge.  This point is essential
when `T=E`: it replaces any required `AE` edge which might have used the
moved piece.

## 3. Every labelled model edge survives

* All foreign--foreign adjacencies survive because `T'` contains all of
  old `T`; no old foreign bag loses a vertex.
* The four `A'U_i` adjacencies survive on the fixed literal endpoint
  edges of `P`.
* If `T=E`, an old `PK` edge supplies `A'E`.  If `T!=E`, the choice rule
  implies that `K` had no edge to `E`, so deleting `K` from `A` cannot
  delete the old `AE` adjacency.
* The fixed absent pair remains absent: `A' subseteq A` and `A` was
  anticomplete to `D`.  Although `T'` contains `K`, every required
  `T'D` adjacency already survives inside old `T-D`.

No palette colour is identified with a model label, no virtual edge is
used, and no contraction is performed.

## 4. Minimality and the seven-neighbour conclusion

If a remaining piece `K_i` met any foreign bag other than `D`, Theorem 1
would produce a comparison model with smaller `|A|`.  It cannot meet `D`
because `AD` is the fixed missing pair, and it cannot meet another
`K_j` by the coherent-transport decomposition.  Hence its entire external
neighbourhood lies on `P`.

That neighbourhood is an actual vertex separator.  Both sides are
nonempty: one contains `K_i`, while the other contains the nonempty
foreign bag `D`, which is anticomplete to `K_i`.  Seven-connectivity
therefore gives at least seven distinct neighbours on `P`.  This does not
count a whole piece as one separator vertex.

## 5. Exact scope of Corollary 3

The transfer proves that a locked helper carrier cannot remain as a
separate `A-P` component.  It does **not** prove that its geometry has
vanished.  Once the carrier is placed in one target row `T`:

* its `P-K` edges are portals from `P` to `T` only;
* its old edges to other foreign bags are merely foreign--foreign model
  edges; and
* all of its vertices have the one branch-set label `T`.

Thus the operation cannot be read as assigning the carrier simultaneously
to `H` and `Q`, or as making both path sides meet every retained row.  The
remaining problem is an ordered path interface with generally
nonsingleton foreign bags, possible internal owner collisions, and
path-private lobes.  The corrected source states exactly this residual.
