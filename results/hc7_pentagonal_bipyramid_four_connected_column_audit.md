# Independent audit of the four-connected PB-column theorem

**Verdict:** **GREEN** for the exact source revision identified below.

**Audited source:**
[`hc7_pentagonal_bipyramid_four_connected_column.md`](hc7_pentagonal_bipyramid_four_connected_column.md)

**Audited SHA-256:**
`c6f2c1fa6c7bad5ed46efcf51a53982dda66ea464b72622695489842a1ed48f3`

This is an internal mathematical audit, not external peer review.  The
source proves a rooted-minor/cofacial-portal dichotomy for one
four-connected column of arbitrary finite order.  It does not prove that a
live column is four-connected, that its portal matching has rank four, or
that the facial orders obtained in different columns are globally
compatible.

## 1. Completing a rooted `K_4`

Four distinct matched portal vertices `q_i in Z_{y_i}` give four distinct
neighbour labels.  If `B_i` is a `K_4` model rooted at these vertices, then
`B_i union L_{y_i}` is connected, and the four resulting sets remain
disjoint and pairwise adjacent through the old rooted model.

The two unused labels in `V(P)-{x,y_1,y_2,y_3,y_4}` have exactly the
properties claimed in both possible orbits of `x`.

* If `x` is a pole, they are the other pole and the unchosen rim vertex.
  They are adjacent, and the unused pole is adjacent to all four selected
  rim labels.
* If `x` is a rim vertex, the four selected labels are its complete
  neighbourhood: the two poles and its two rim neighbours.  The unused
  labels are the two remaining consecutive rim vertices.  Their union is
  adjacent to both poles and to both selected rim neighbours.

Consequently `L_a union L_b` is a fifth connected branch set adjacent to
the first four.  Every one of the five sets contains a whole old column,
so both fixed roots contact all five; the roots are disjoint, connected and
adjacent to one another.  The seven displayed sets are therefore an
explicit `K_7`-minor model.  This checks the PB completion for every choice
of four matched neighbour labels.

## 2. The portal transversal matroid

On the literal portal vertices, the family of subsets admitting an
injective assignment to distinct neighbour labels is the transversal
matroid of the portal-set family.  Portal matching rank at least four makes
its rank-four truncation a rank-four matroid.  Each basis consists of four
distinct literal vertices and has a representation by four distinct
labels, exactly as required by the completion lemma.

Every portal vertex is a nonloop: it belongs to at least one `Z_y`, so its
singleton is independent.  In a rank-four matroid each nonloop extends to
a basis.  Overlap between portal sets causes no problem, because the
matroid ground elements are literal vertices and a basis representation is
chosen injectively only after the four distinct vertices have been fixed.

## 3. Rooted-`K_4` scope and facial propagation

Fabila-Monroy--Wood Theorem 6 gives the required four-connected
specialization: for four distinct nominated vertices, either there is a
rooted `K_4` minor or the graph is planar with the four vertices on one
face.  Thus if the host column were nonplanar, every portal basis would
root a `K_4` and the first outcome would already hold.  In the surviving
case the column is planar and every basis is cofacial.  Equivalently, the
same cofacial conclusion follows from their three-connected planar
characterization (Theorem 9), since four-connectivity implies
three-connectivity.

The plane embedding is unique up to reflection.  In a three-connected
simple plane graph, two distinct faces share at most two vertices.  The
basis-exchange graph of a matroid is connected, and consecutive rank-four
bases share three literal vertices.  Therefore the faces containing two
consecutive bases coincide, and propagation along the basis graph puts all
bases on one fixed face.  Since every portal vertex extends to a basis,
every literal portal lies on that face.

No palette colour is identified with a quotient label in this argument,
and no virtual facial edge is treated as a host edge.

## 4. Trust boundary

The conclusion is local to one four-connected, rank-four column.  It does
not imply that four-connectivity of the spanning core is inherited by its
columns.  A matching-rank defect can concentrate several quotient labels
at fewer than four literal vertices.  Finally, even when every qualifying
column has one common portal face, the source proves no compatibility of
the cyclic orders across repeated inter-column bundles.

All PB branch-set completions, matroid steps and rooted-minor uses are
valid at the audited source hash.  **GREEN.**
