# Repeated boundary roots at a two-shore equality gate

## 1. Setting

Let `G` be seven-connected, have minimum degree at least seven, and
contain no `K_7` minor.  Let `S` be a seven-vertex cut such that

\[
                       G-S=R\mathbin{\dot\cup}D                 \tag{1.1}
\]

has exactly two connected components, both full to `S`.  Put

\[
                 J=G[S],\qquad Q=\overline J .                  \tag{1.2}
\]

The application is the equality outcome of
`hadwiger_double_root_p4_capacity_state.md`.  There the installed
order-seven closure gives

\[
                         |E(Q)|\ge7.                             \tag{1.3}
\]

The point of this note is that (1.3) forces actual multiplicity inside
one of the two shores.  It therefore supplies a second, independently
constructed covering split at the equality gate.

## 2. The low-degree count

### Lemma 2.1 (three sparse boundary labels)

If `|E(Q)|>=7`, at least three vertices `s in S` satisfy

\[
                         d_J(s)\le4.                             \tag{2.1}
\]

#### Proof

Condition (2.1) is equivalent to `d_Q(s)>=2`.  Suppose at most two
vertices have missing degree at least two.  Every edge of `Q` except
possibly the edge between those two vertices has an endpoint among the
other five vertices.  The sum of the missing degrees of those five
vertices is at most five.  Hence

\[
                         |E(Q)|\le1+5=6,
\]

contrary to the hypothesis. \(\square\)

### Lemma 2.2 (two labels repeat in one shore)

There are distinct `a,b in S` and a choice `C in {R,D}` such that

\[
                  |N_C(a)|\ge2,\qquad |N_C(b)|\ge2.             \tag{2.2}
\]

#### Proof

Let `L` be three labels supplied by Lemma 2.1.  For `s in L`, minimum
degree gives

\[
 |N_R(s)|+|N_D(s)|
   =d_G(s)-d_J(s)\ge3.                              \tag{2.3}
\]

Both summands are positive because both shores are full.  Thus one of
them is at least two.  Assign `s` to such a shore.  Two of the three
labels receive the same assignment, proving (2.2). \(\square\)

This is the useful capacity consequence of the seven-missing-edge
threshold.  It uses the number of *distinct portal vertices*, not merely
the existence of contacts.

## 3. The repeated-root split theorem

### Theorem 3.1 (double-root covering split or nested cut)

Under (1.1)--(1.3), after interchanging `R,D` if necessary, one of the
following holds.

1. There is a connected adjacent bipartition

   \[
                       R=X\mathbin{\dot\cup}Y                     \tag{3.1}
   \]

   whose contact rows cover `S` and have two common labels:

   \[
      N_S(X)\cup N_S(Y)=S,
      \qquad |N_S(X)\cap N_S(Y)|\ge2.              \tag{3.2}
   \]

2. There is a nested exact seven-cut `T` with a nonempty side properly
   contained in `R`.
3. There is a split (3.1) in which **both** `X` and `Y` are full to
   `S`.

Moreover, in outcomes 1 and 3 put

\[
 P_X=N_S(X),\quad P_Y=N_S(Y),\quad
 T_X=N_Y(X),\quad T_Y=N_X(Y).                       \tag{3.3}
\]

Then

\[
 |T_X|\ge |S-P_X|,\qquad |T_Y|\ge |S-P_Y|.          \tag{3.4}
\]

Equality in either inequality exposes a nested exact seven-cut.  If no
such cut occurs, both inequalities improve by one:

\[
 |T_X|\ge |S-P_X|+1,
 \qquad
 |T_Y|\ge |S-P_Y|+1.                               \tag{3.5}
\]

#### Proof

Choose `a,b,R` as in Lemma 2.2 and apply Theorem 1.1 of
`hadwiger_root_multiplicity_split.md` to the two portal classes

\[
                        N_R(a),\qquad N_R(b).
\]

Its linkage outcome gives (3.1), with both `a,b` in both contact rows.
Fullness of `R` makes the two rows cover `S`, proving outcome 1.

In the other outcome there is a vertex `q in R` such that `R-q` has at
least two components and no component contains portals of both selected
classes.  Let `C` be any component of `R-q`.  Since `R` is a component
of `G-S`,

\[
                         N_G(C)=N_S(C)\mathbin{\dot\cup}\{q\}.    \tag{3.6}
\]

The opposite shore `D` lies beyond this neighbourhood.  Seven-connectivity
therefore gives `|N_S(C)|>=6`.  If equality holds, (3.6) is the nested
exact seven-cut in outcome 2.

Suppose equality never holds.  Every component of `R-q` is then full to
`S`.  Choose one such component `C`, put `X=C`, and put `Y=R-C`.
Every component of `R-q` has a neighbour at `q`, so `Y` is connected and
adjacent to `X`.  The set `X` is full, and `Y` contains another full
component.  Thus both rows are full, proving outcome 3.

For any split (3.1), no vertex outside `S union R` is adjacent to either
side.  Consequently

\[
 N_G(X)=P_X\mathbin{\dot\cup}T_X,
 \qquad
 N_G(Y)=P_Y\mathbin{\dot\cup}T_Y.                  \tag{3.7}
\]

Each displayed set separates its side from `D`.  Seven-connectivity
gives (3.4).  Equality makes the corresponding neighbourhood an exact
seven-cut; integrality gives (3.5) otherwise. \(\square\)

### Corollary 3.2 (the exact static residue)

Contract `D,X,Y` to vertices `h,x,y`, respectively, retaining `xy`, all
boundary edges, the full `h` row, and the two actual contact rows.  The
resulting ten-vertex quotient has no `K_7` minor.  Thus every survivor of
Theorem 3.1 is a **double-overlap covering bad split**, or a nested exact
seven-cut; away from equality its two interfaces satisfy the strict
surplus inequalities (3.5).

If `G` is also proper-minor-minimal non-six-colourable, deletion of any
interface edge carries the strict boundary transition and the
ear-or-two-anchor Kempe alternative of
`hadwiger_bad_split_interface_exchange.md`.  Independently,
`hadwiger_full_split_cyclic_hull.md` supplies a cyclic-hull bad split in
at least one of the two shores.  The two splits need not be the same.

#### Proof

A `K_7` model in the quotient lifts through the three contracted
connected sets, contradicting the hypothesis on `G`.  The state and
cyclic-hull assertions are exactly the cited theorems. \(\square\)

This corollary is the promised capacity--state funnel: missing-edge
capacity forces a two-root split, while failure to lift it is no longer
an arbitrary portal configuration but a strict bad split or a nested
minimum adhesion.

## 4. Sharp finite information at seven missing edges

There is a useful computer-assisted sharpening of the sparsest row.
Assume `|E(Q)|=7` and exactly three vertices of `Q` have degree at least
two.  The proof of Lemma 2.1 is then tight, so `Q` consists of a triangle
with four pendant leaves, every leaf having its neighbour in the
triangle.

For completeness, let `H` be the three vertices of missing degree at
least two and `L=S-H`.  Every vertex of `L` has missing degree at most
one, and hence

\[
\begin{aligned}
 7=|E(Q)|
 &=|E(Q[H])|+|E_Q(H,L)|+|E(Q[L])|\\
 &\le 3+\sum_{x\in L}d_Q(x)\le7.                 \tag{4.0}
\end{aligned}
\]

Equality throughout forces `Q[H]=K_3`, every vertex of `L` to have
degree one, and \(E(Q[L])=\varnothing\): a low--low edge is counted twice in
the degree sum but only once in the middle line, and would make the first
inequality strict.  Thus every low vertex is a pendant leaf attached to
the triangle, as claimed.

### Proposition 4.1 (pendant-triangle split atlas)

Choose the two common split labels from the triangle.  If the four leaf
multiplicities on the triangle are, up to order,

\[
                  (4,0,0),\quad(3,1,0),\quad(2,2,0),              \tag{4.1}
\]

then the quotient in Corollary 3.2 contains a `K_7` minor.  The only
negative distribution is

\[
                              (2,1,1).                            \tag{4.2}
\]

Normalize (4.2) by

\[
 E(Q)=\{01,02,12,03,04,15,26\}.                    \tag{4.3}
\]

For common labels `0,1`, every negative row is coordinatewise contained
in one of the following four maximal rows, written by defects:

\[
\begin{array}{c|c}
 S-P_X&S-P_Y\\ \hline
 \{2,4,5\}&\{6\}\\
 \{2,3,5\}&\{6\}\\
 \{6\}&\{2,4,5\}\\
 \{6\}&\{2,3,5\}.
\end{array}                                                     \tag{4.4}
\]

There are exactly ten ordered negative rows.  For each of the other
common pairs `0,2` and `1,2` there are again ten rows and four maxima.
The pair `1,2` is a different orbit from a pair containing the
double-leaf triangle vertex, so the verifier prints all three lists
rather than silently identifying them.

The exact verifier is `equality_gate_repeated_root_verify.py`.  It
enumerates all `3^5` covering rows for every common pair and performs a
complete branch-set search, over 11,880 candidate seven-bag partitions
of the ten-vertex quotient.  Its audited counts are `0,0,0,10` for the
four distributions in (4.1)--(4.2), for every triangle pair.

### Proposition 4.2 (one frame is forced into the repeated-root shore)

Assume additionally that `G` is not six-colourable.  In the normalized
residue (4.3), the five cyclic hulls are

\[
\begin{split}
 &(0,1,3,5),\ (0,1,4,5),\ (0,2,3,6),\ (0,2,4,6),\\
 &(1,2,5,6).                                      \tag{4.5}
\end{split}
\]

For every one of the thirty negative rows over the three possible common
pairs, the last hull in (4.5) is crossed in the **repeated-root shore**.
Equivalently, that shore contains vertex-disjoint paths for the two
portal demands

\[
                              1\!-!5,qquad2\!-!6.              \tag{4.6}
\]

#### Proof

For every cyclic hull, non-six-colourability and two-shore web gluing
force a crossing in at least one shore.  Suppose the last hull were
crossed in the opposite shore.  Extend its two paths to a connected
covering split, contract that split and the repeated-root split, and
delete overlap contacts to obtain a disjoint boundary partition.  The
eleven-vertex quotient is `K_7`-positive for every one of the thirty
negative repeated-root rows and all eight assignments of the other three
boundary labels.  This is checked by the same verifier, now over 159,027
candidate seven-bag partitions.  The model lifts, a contradiction.
\(\square\)

### Lemma 4.3 (the forced packet closes the balanced row)

The packet in (4.6), together with the opposite full shore, gives a
`K_7` minor.  Consequently the balanced distribution (4.2) is
impossible.

#### Proof

Let `C_15,C_26 subseteq R` be the two disjoint connected packet
carriers, touching `1,5` and `2,6`, respectively.  Since `R` is
connected, join them by a shortest path and absorb the internal vertices
of that path into its two ends.  We may therefore assume, without losing
either contact pair, that `C_15` and `C_26` are adjacent.

Use the seven branch sets

\[
 \{0,5\},\quad \{1\}\cup C_{15},\quad
 \{2\}\cup C_{26},\quad \{3\},\quad\{4\},\quad
 \{6\},\quad D.                                    \tag{4.7}
\]

They are disjoint and connected.  The only missing boundary edges are

\[
                 01,02,12,03,04,15,26.             \tag{4.8}
\]

The `1`- and `2`-contacts make the second and third bags connected; the
`5`- and `6`-contacts repair their adjacencies to the first and sixth
bags, respectively.  The adjacency between the two carriers repairs the
missing `12` edge.  The vertex `5` is
adjacent to `2,3,4,6`, repairing every missing incidence of `0` in the
first bag.  All remaining pairs in (4.7) are boundary edges, and the
full shore `D` sees every boundary-containing bag.  Thus (4.7) is a
`K_7` model. \(\square\)

If a path convention includes its boundary endpoints, remove `1,5` and
`2,6` from the two paths before defining the carriers.  Since the two
demand edges are missing, each path has a nonempty interior, and the same
seven bags result.

### Corollary 4.4 (complete closure of the three-high seven-edge row)

If `G` is additionally not six-colourable, `|E(Q)|=7`, and exactly three
vertices of `Q` have degree at least two, the equality gate is impossible.
Indeed, (4.0) gives a triangle with four leaves; Proposition 4.1 closes
the first three leaf distributions, and Proposition 4.2 plus Lemma 4.3
closes `(2,1,1)`.

The final branch-set replay is included in
`equality_gate_repeated_root_verify.py`.  It checks (4.7) directly, in
addition to the exhaustive quotient searches.

## 5. Exact remaining gap

The theorem does not prove `HC_7`.  In particular, seven missing edges
does not imply that exactly three boundary labels have missing degree at
least two.  For example, a missing `K_4` plus one pendant edge has four
such labels and is outside Corollary 4.4.  At the level of the hypotheses
used in Sections 1--4 this is a real quotient obstruction: take

\[
 E(Q)=\{01,12,13,14,23,24,34\},                   \tag{5.1}
\]

let one split row be all of `S`, let the other be exactly `{1,2}`, and
add the adjacent split vertices and one opposite full helper.  Complete
seven-bag search finds no `K_7` minor in this ten-vertex quotient.  The
check is `audit_four_high_static_obstruction` in the verifier.  This
particular `Q` is split and is therefore excluded once the independent
exact-block theorem is added.  It does not construct a seven-connected
critical host; it proves only that multiplicity and the static quotient,
without exact-block nonsplitness, cannot close the larger layer.

After imposing nonsplitness, the complete seven-edge funnel is now
`hadwiger_equality_seven_edge_packet_funnel.md`: 31 possible boundary
types reduce to ten state-decorated packet cores.

The work leaves two genuinely structural possibilities:

1. a nested exact seven-adhesion, to which the operation-state descent
   must be applied; or
2. a strict double-overlap bad split, decorated by an interface
   transition and by a cyclic crossing.  This includes the seven-edge
   boundaries with at least four low-boundary-degree labels, as well as
   denser missing graphs.

The missing uniform statement can now be phrased without Moser labels:

> **Repeated-root split exchange.**  In a seven-connected minor-critical
> two-shore gate, a covering split with two common labels and strict
> interface surplus either admits a label-preserving further split, or
> its edge-transition state glues across the opposite full shore.

Static multiplicity alone cannot establish this last exchange.  The new
content proved here is that every equality gate reaches precisely this
dynamic object; the portal split no longer has to be postulated.  The
balanced seven-edge packet, which initially appeared to require such a
synchronization, is now completely closed by (4.7).
