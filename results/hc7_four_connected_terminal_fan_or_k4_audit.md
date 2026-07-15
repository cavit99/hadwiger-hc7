# Cold audit of the four-connected rooted clique-or-fan theorem

## Verdict

**GREEN.**  The published rooted-`K_4` input has exactly the stated
four-connected alternative, the cofacial propagation through one fixed
anchor triple is valid, and the facial remainder gives literal (rather
than completed) adjacencies for the rooted fan.

This audit verifies only the theorem in
[`hc7_four_connected_terminal_fan_or_k4.md`](hc7_four_connected_terminal_fan_or_k4.md).
Whether either output closes a particular cross-arm decoder remains a
separate labelled-composition question.

## 1. Published input

Theorem 6 of R. Fabila-Monroy and D. R. Wood, *Rooted K4-Minors*,
Electronic Journal of Combinatorics **20** (2013), P64, states that for
four distinct vertices in a four-connected graph, either they root a
`K_4` minor, or the graph is planar and the four vertices lie on a common
face.  This is precisely the dichotomy used in the proof.  No stronger
linkedness assertion is being imported.

The paper also proves the corresponding planar three-connected
characterisation (its Theorem 9).  Thus the wording in the source file is
consistent with both of the cited special cases.

## 2. Propagation of one face

Assume that no anchored set `A union {x}` roots `K_4`, where
`A={a,b,c}`.  The published theorem makes the graph planar and puts every
such four-set on a face.  In the unique embedding of a three-connected
planar graph, two distinct facial boundary cycles share at most one edge
and therefore at most two vertices.  Faces containing the same three
distinct vertices `a,b,c` must consequently coincide.  Hence one face
contains every member of `T`.

The hypotheses `k>=5` and `|A|=3` leave at least two choices outside `A`,
but the same argument also works one terminal at a time after the first
face is fixed.

## 3. Peripheral facial cycle

The boundary `C` of a face in a simple three-connected plane graph is a
peripheral cycle: it is induced and `H-V(C)` is connected when nonempty.
Here the remainder is nonempty, since otherwise `H=C` would not be
four-connected for `|C|>=|T|>=5`.

Every vertex of `C` has exactly two neighbours on `C`, because `C` is
induced.  Four-connectivity gives minimum degree at least four, so every
vertex of `C` has a neighbour (indeed at least two) in the connected
remainder `R=H-V(C)`.

## 4. Literal fan model

Cut `C` immediately before successive terminals in cyclic order.  The
resulting terminal-rooted path bags are pairwise disjoint and connected,
and consecutive bags are adjacent by an edge of `C`.  For a prescribed
terminal `t`, add all of `R` to its path bag.  This bag is connected because
`R` meets every boundary vertex, and it is adjacent to every other path
bag for the same reason.  Deleting its position from the cyclic list
leaves the other `k-1` bags in a path.  These are exactly the edges of
`K_1 join P_{k-1}`.

All contacts used here are edges of the original graph.  No edge drawn
across the face or inserted by a planar completion is treated as literal.
The construction works for every prescribed universal terminal, as
claimed.

## 5. Trust boundary

The result does not say that a rooted `K_4` avoids the other terminals;
an unrooted terminal may lie inside one of its four bags.  Any finite
decoder using outcome 1 must therefore avoid those other terminals as
separate branch sets, or prove an additional cleaning lemma.  The rooted
fan outcome has one bag per member of `T` and has no such ambiguity.
