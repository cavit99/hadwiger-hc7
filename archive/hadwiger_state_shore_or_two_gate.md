# State shores or a two-vertex portal gate

## Status and purpose

This note proves a label-free extraction lemma for the connected carriers
which occur in the normalized near-clique programme.  It does **not** by
itself finish the carrier lift: after extracting shores in several
carriers, one must still obtain compatible contacts between the shores of
different carriers.  What it removes is the separate concern that an
arbitrarily large carrier may have no two connected pieces carrying one
of the required boundary states.

## 1. One common portal class

Let `D` be a connected graph and let `A,B,C` be three nonempty subsets of
`V(D)`.  The sets need not be disjoint.  A pair `(X,Y)` of vertex sets is
an `AB|BC` shore pair if

* `D[X]` and `D[Y]` are connected;
* `X` and `Y` are nonempty, disjoint, and adjacent;
* `X` meets both `A` and `B`; and
* `Y` meets both `B` and `C`.

The symmetric definition of an `AC|BC` shore pair is obtained by taking
`C` as the common portal class: one shore meets `A,C`, and the other meets
`B,C`.

### Lemma 1.1 (two sources to one portal class)

Exactly one of the following alternatives may fail, and at least one of
them holds:

1. `D` has an `AB|BC` shore pair;
2. there is a vertex `z_B in V(D)` such that every path in `D` from
   `A union C` to `B` contains `z_B`.

Here a path is allowed to have order one.  Consequently the second
outcome includes the case in which one vertex is the only available
`B`-portal.

#### Proof

Adjoin two protected source vertices `alpha,gamma`, join `alpha` to every
vertex of `A`, and join `gamma` to every vertex of `C`.  Ask for two
vertex-disjoint paths from the two-element source set
`{alpha,gamma}` to `B`, with distinct source and target ends and with
neither protected source allowed internally on the other path.

The protected-source form of the vertex version of Menger's theorem says
that either these two paths exist, or a set of fewer than two vertices of
`D` separates both protected sources from `B`.  For completeness, this
is the ordinary integral max-flow theorem after splitting every vertex
of `D` into an in-vertex and an out-vertex joined by a capacity-one arc,
giving `alpha,gamma` infinite vertex capacity, and joining a supersource
to each of them by a capacity-one arc.  Since `D` is connected and all
three portal sets are nonempty, each protected source individually has a
path to `B`.  A cut of capacity one therefore cannot consist of just one
supersource arc; it is one split vertex `z_B` of `D`.  It meets every
`A`--`B` path and every `C`--`B` path, which is outcome 2.

Suppose instead that the two paths exist.  Delete `alpha,gamma` from
them.  Their remainders are disjoint connected subgraphs `P_A,P_C` of
`D`, where `P_A` meets `A,B` and `P_C` meets `C,B`.  If they are adjacent,
they are the required shores.  Otherwise, take a shortest path in `D`
from `P_A` to `P_C`.  Its internal vertices avoid both subgraphs.  Add
all of its internal vertices to `P_A`; the enlarged first subgraph is
connected, remains disjoint from `P_C`, and is adjacent to `P_C` through
the last edge of the path.  This gives outcome 1.  \(\square\)

The two outcomes are not asserted to be mutually exclusive.  The useful
content is that failure of the shore pair produces the displayed
one-vertex gate.

### Corollary 1.2 (the other state)

Either `D` has an `AC|BC` shore pair, or there is a vertex `z_C` met by
every path from `A union B` to `C`.

#### Proof

Apply Lemma 1.1 after interchanging `B` and `C`.  \(\square\)

## 2. The two-state dichotomy

### Theorem 2.1 (state-shore or two-gate theorem)

For every connected `D` with nonempty portal sets `A,B,C`, at least one
of the following holds:

1. `D` has an `AB|BC` shore pair;
2. `D` has an `AC|BC` shore pair;
3. there are vertices `z_B,z_C` (possibly equal) such that

   \[
   \begin{aligned}
   &z_B\text{ meets every }(A\mathbin\cup C)\text{--}B\text{ path},\\
   &z_C\text{ meets every }(A\mathbin\cup B)\text{--}C\text{ path}.
   \end{aligned}                                                   \tag{2.1}
   \]

In outcome 3 every connected subgraph meeting all three portal classes
contains both gates, except that a gate already belonging to two portal
classes accounts for both incidences at that same vertex.  In particular,
every component of

\[
                      D-\{z_B,z_C\}                              \tag{2.2}
\]

is dark to at least one of `A,B,C`.

#### Proof

If outcome 1 fails, Lemma 1.1 supplies `z_B`.  If outcome 2 fails,
Corollary 1.2 supplies `z_C`.  This proves (2.1).

Let `R` be a connected subgraph meeting `A,B,C`.  It contains an
`A`--`B` path and hence meets `z_B`; it also contains an `A`--`C` path
and hence meets `z_C`.  If a component of (2.2) met all three portal
sets, a connected subgraph inside that component would do so while
avoiding both gates, a contradiction.  \(\square\)

### Corollary 2.2 (typed carrier extraction)

Let `a,b,c` be three external boundary vertices and put

\[
 A=N_D(a),\qquad B=N_D(b),\qquad C=N_D(c).
\]

If outcome 1 of Theorem 2.1 holds, its shores have the type-zero rows

\[
                         AB\mid BC.
\]

If outcome 2 holds, its shores have the type-one rows

\[
                         AC\mid BC.
\]

These are exactly the two connected-shore rows used in Theorem 3.1 of
`hadwiger_flat_full_host_matching_dichotomy.md`.  If neither row can be
extracted, all three portal classes are confined by the explicit gate of
order at most two in (2.2).

### Corollary 2.3 (gate lobes are portal-monochromatic)

In outcome 3 of Theorem 2.1, every component of
`D-{z_B,z_C}` meets **at most one** of `A,B,C`.

#### Proof

A component meeting `A` and `B` contains an `A`--`B` path avoiding
`z_B`, contrary to the first line of (2.1).  A component meeting `A` and
`C` contains an `A`--`C` path avoiding `z_C`, contrary to the second
line.  A component meeting `B` and `C` contradicts either gate condition.
Thus no component meets two portal classes. \(\square\)

This strengthens mere darkness and is the faithful datum for combining
two gated carriers: each individual lobe has one portal label, although
cross-edges between lobes of different carriers may join different
labels into one combined-network component.

## 3. What remains for the near-clique lift

The theorem is internal to one carrier.  It does not assert that, after
choosing shores independently in several pairwise adjacent carriers,
each pair of shore systems has a parallel or crossed two-edge matching.
An original branch-set adjacency can be concentrated between just one
pair of shores.  Therefore the exact remaining transport theorem is:

> either choose the shore pairs so that their inter-carrier contact
> graphs admit the compatible matchings required by the full-host
> dichotomy, or the concentrated contacts of a failed pair combine with
> the one/two-vertex gates to give an actual adhesion of order at most
> six or one coherent rural two-apex state.

Thus the arbitrary internal order of a carrier has been reduced to an
order-two portal gate.  The unresolved information is the placement of
contacts **between** different carriers (and, for a two-carrier quotient
cut, in their combined network), not the existence of a typed connected
split inside a single carrier.
