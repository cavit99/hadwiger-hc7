# Full state shores or one rooted torso

## Status

This note proves the label-preserving carrier extraction needed before the
two-layer transport theorem.  Unlike a split using only the three deficient
boundary rows, both extracted shores retain **every neutral/model portal
row**.  Consequently the contact graph between any two extracted carrier
pairs has no isolated vertex and therefore contains a perfect matching.

The theorem is independent of the number of neutral rows and of the target
clique order.  Its obstruction is not an unstructured large carrier: it is
one named bag of any chosen tree decomposition.  In a Tutte decomposition
this is exactly a gate of order at most two, a cycle torso, or a
3-connected rooted torso.

## 1. Two families of full rooted carriers

Let `D` be a connected graph.  Let

\[
             Q_1,\ldots,Q_s,A,B,C\subseteq V(D)                 \tag{1.1}
\]

be nonempty portal sets; they need not be disjoint.  Fix one of the two
state types `epsilon in {0,1}`.  A connected subgraph is called a
**left state carrier** when it meets every `Q_i` and

\[
 \begin{cases}
 A,B,&\epsilon=0,\\
 A,C,&\epsilon=1.
 \end{cases}                                                     \tag{1.2}
\]

A connected subgraph is called a **right state carrier** when it meets
every `Q_i` and meets `B,C`.  A **full typed shore pair** is a bipartition
`V(D)=X dotunion Y` into nonempty adjacent connected vertex sets such that
`X` is a left state carrier and `Y` is a right state carrier.

Thus its displayed boundary rows are

\[
             AB\mid BC\quad(\epsilon=0),\qquad
             AC\mid BC\quad(\epsilon=1),                         \tag{1.3}
\]

and, crucially, both shores retain every neutral row `Q_i`.

### Lemma 1.1 (disjoint carriers extend to shores)

If `D` contains a left state carrier and a right state carrier which are
vertex-disjoint, then it has a full typed shore pair.

#### Proof

Let the two disjoint connected carriers be `L,R`.  If they are not
adjacent, choose a shortest `L`--`R` path in `D`.  Its internal vertices
avoid `L union R`; add them to `L`.  We may therefore assume `L,R` are
adjacent.

Contract `L` and `R`, take a spanning tree of the resulting connected
graph which contains one edge between their images, and delete that tree
edge.  The two tree components lift to a bipartition of `V(D)` into
connected adjacent sets containing the original `L` and `R`, respectively.
All required portal contacts are retained.  \(\square\)

## 2. The cross-Helly theorem

Let `(T,(V_t)_{t in V(T)})` be an arbitrary tree decomposition of `D`.

### Theorem 2.1 (full state-shore or bi-Helly core)

At least one of the following holds.

1. `D` has a full typed shore pair.
2. Some node `z in V(T)` has the property that **every** left state
   carrier meets `V_z`.
3. Some node `z in V(T)` has the property that **every** right state
   carrier meets `V_z`.

If the decomposition has adhesion at most `k`, then in outcomes 2 and 3
every component `K` of `D-V_z`

* misses at least one portal row required by the corresponding state
  carrier; and
* has at most `k` neighbours in `V_z`.

#### Proof

Let `mathcal L` and `mathcal R` be the finite families of
inclusion-minimal left and right state carriers.  Both are nonempty:
because `D` is connected, a spanning tree contains a connected subgraph
meeting any prescribed finite family of nonempty portal sets.

For a connected subgraph `K`, put

\[
       T(K)=\{t in V(T):V_t\cap V(K)\ne\varnothing\}.             \tag{2.1}
\]

As usual, `T(K)` is a subtree of `T`: the bag subtrees belonging to
successive vertices and edges of the connected graph `K` meet.

Assume outcome 1 fails.  Lemma 1.1 then says that every member of
`mathcal L` intersects every member of `mathcal R`.  Hence

\[
        T(L)\cap T(R)\ne\varnothing
        \quad(L in mathcal L,\ R in mathcal R).                  \tag{2.2}
\]

If the subtrees `T(L)`, `L in mathcal L`, are pairwise intersecting, the
Helly property for subtrees gives a node `z` common to all of them.
Every left state carrier contains an inclusion-minimal one, so outcome 2
holds.

Otherwise choose `L_1,L_2 in mathcal L` whose trace subtrees are disjoint.
Let `P` be the unique nonempty path in `T` joining these two subtrees and
choose a node `z` on `P`.  Every `T(R)`, `R in mathcal R`, meets both
`T(L_1)` and `T(L_2)` by (2.2).  Since `T(R)` is connected, it contains
the whole joining path `P`, and in particular contains `z`.  Again every
right state carrier contains an inclusion-minimal one, so outcome 3
holds.  This proves the trichotomy.

In outcome 2, a component of `D-V_z` cannot meet all the portal rows in
(1.1)--(1.2), since that connected component would itself be a left
state carrier avoiding `V_z`.  The symmetric statement holds in outcome
3.  Finally the standard running-intersection argument for a tree
decomposition puts all neighbours in `V_z` of one component of `D-V_z`
inside one adhesion `V_z cap V_u`, where `u` is the first node toward
that component.  There are at most `k` such neighbours.  \(\square\)

The proof uses a genuinely bipartite form of subtree Helly.  Cross
intersection of the two carrier families is enough: if one trace family
is not pairwise intersecting, two disjoint traces force every trace of the
other family through the same joining path.

### Corollary 2.2 (gate, cycle, or 3-connected state core)

Use the Tutte decomposition of `D`.  If `D` has no full typed shore pair,
there is one bag `Z` meeting every carrier of one of the two state halves,
and the torso on `Z` is one of

1. a gate of order at most two;
2. a cycle torso; or
3. a 3-connected torso.

Every component outside `Z` misses a named row of that state half and
attaches through at most two vertices of `Z`.

Virtual torso edges record their named two-vertex bridges and are not
asserted to be literal edges of `D`.

#### Proof

Apply Theorem 2.1 to the standard block/2-separation (Tutte) tree
decomposition, whose adhesion is at most two.  The listed torso types are
the standard types in that decomposition.  \(\square\)

## 3. Exact interface with rigid retained views

Consider retained carriers `D_1,...,D_n` in a normalized near-clique
model.  For carrier `D_i`, let

\[
             Q_{ij}=N_{D_i}(D_j)\quad(j\ne i)                   \tag{3.1}
\]

be its portal rows to the other carriers, and let

\[
 A_i=N_{D_i}(a),\quad B_i=N_{D_i}(b),\quad C_i=N_{D_i}(c).      \tag{3.2}
\]

All these rows are nonempty because the original branch bags are
pairwise adjacent and every neutral bag is adjacent to `a,b,c`.
Prescribe type zero to a retained state `AB` and type one to a retained
state `AC`.

### Corollary 3.1 (arbitrary-order state-shore extraction)

For every rigid carrier `D_i`, either

1. it has two disjoint adjacent connected shores with its prescribed row
   from (1.3), **both** shores meeting every `Q_{ij}`; or
2. one gate/cycle/3-connected torso meets every connected subgraph of one
   state half, and every off-torso lobe has a named missing state or
   intercarrier portal row and an adhesion of order at most two.

#### Proof

Apply Corollary 2.2 with the neutral family
`(Q_{ij}:j ne i)` and with `A_i,B_i,C_i`.  \(\square\)

### Corollary 3.2 (the extracted shores enter the cocycle theorem)

Suppose outcome 1 of Corollary 3.1 holds for every `i`; write the two
shores as `P_i,Q_i`.  For every pair `i,j`, the bipartite contact graph
between `{P_i,Q_i}` and `{P_j,Q_j}` has no isolated vertex and hence has
a perfect matching.  Selecting one such matching for every pair gives
exactly the data of Theorem 5.3 in
`hadwiger_seven_view_state_cocycle_exchange.md`.

Consequently, for `n>=4`, a mixed type word with any state-relative
matching discrepancy gives a labelled `K_{n+3}` model.  In the flat
branch the shores switch into two labelled `K_n` layers.  Thus an
arbitrarily large carrier introduces no additional internal case once
outcome 1 holds.

#### Proof

Each of `P_i,Q_i` meets `Q_{ij}`, so each has a neighbour in
`D_j=P_j union Q_j`; the symmetric assertion for `j` shows that all four
vertices of the two-by-two contact graph have positive degree.  A
bipartite graph with two vertices in each part and no isolated vertex has
a perfect matching.  The selected matchings and the row contacts are
precisely hypotheses (5.6)--(5.8) of the connected-shore cocycle theorem.
Its conclusions now apply verbatim.  \(\square\)

## 4. Faithful cut and web consequences

The torso outcome is an exact bounded-adhesion obstruction, not yet an
automatic cut in the ambient graph.  Two standard faithful lifts are now
available.

* If the left and right incidence systems of a one-carrier quotient cut
  lie in components separated by the order-at-most-two torso gate, then
  Lemma 3.1 of `hadwiger_qfull_carrier_adhesion_lift.md` turns the three
  neutral vertices, the possible singleton quotient-cut vertex, and the
  gate into an actual cut of order at most six.
* In a cycle or 3-connected torso, fix four named marks with the following
  **state-forcing** property: expansion of a crossing (respectively a
  rooted `K_4`) through the named adhesion lobes gives one left and one
  right state carrier disjointly.  Since such a crossing/model would give
  outcome 1 by Lemma 1.1, its absence is exactly a crossless/rooted-web
  state.  The generalized Two Paths theorem (cycle case) or the rooted
  `K_4` theorem (3-connected case) then gives the corresponding rural
  disk order.

The qualifier `state-forcing` is essential.  The theorem confines the
selection problem to one torso and names every missing portal row, but it
does not turn a virtual edge into a literal edge or assert that arbitrary
four marks preserve all neutral rows.

## 5. Sharp boundary of the result

If the neutral rows `Q_{ij}` are omitted, the simpler two-source Menger
lemma extracts the boundary rows or gives a one-vertex boundary gate.
That is insufficient here: an `AB|BC` split may put all contact with some
other carrier on only one shore, so the two-by-two intercarrier contact
graph may have an isolated vertex.

The full-row hypotheses in Theorem 2.1 are exactly what repairs this
defect.  The remaining obstruction is one rooted torso (or a faithful
small cut/web after lifting), not another enumeration of the vertices of
`D`.
