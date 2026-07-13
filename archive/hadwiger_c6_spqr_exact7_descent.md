# The SPQR tree descends before it needs to be peeled

## 1. Scope

Let

\[
 S=W\mathbin{\dot\cup}\{z\},\qquad
 \overline{G[S]}=C_6\mathbin{\dot\cup}K_1,
\]

and suppose that `G` is seven-connected and `K_7`-minor-free.  Assume
that `G-S` has two connected components `D,H`, both full to `S`, and that
`D` is nonsingleton.  The exact two-piece contact atlas in
`hadwiger_c6_two_piece_locks.md` is part of the hypotheses below.

The point of this note is that the proposed arbitrary-SPQR extension of
the direct `R--R` face theorem is unnecessary if a nested exact
seven-cut is retained as an allowed outcome.  Every separation pair of
`D` already produces such a cut.  Thus, after excluding exact-seven
descent, the SPQR tree is trivial and there is no leaf face to propagate.

This also identifies the correct label-faithful operation.  One must
promote the separation pair and the five surviving old boundary
vertices to a new seven-boundary.  Contracting the pertinent subtree to
its poles is not a valid substitute: it deletes portal occurrences and
can lower the colourful transversal rank.

## 2. Every two-cut has a defect-two open side

For a component `C` of `D-{p,q}`, write

\[
                \Delta_C=S-N_S(C).
\]

### Theorem 2.1 (defect-two SPQR descent)

Let `{p,q}` be a two-cut of `D`.  Then one component `C` of
`D-{p,q}` satisfies

\[
                         |\Delta_C|=2.             \tag{2.1}
\]

Consequently

\[
                    S_C=N_S(C)\cup\{p,q\}          \tag{2.2}
\]

is an exact seven-cut of `G`, and `C` is a proper fragment contained in
the old shore `D`.  Moreover `G-S_C` has exactly two components, both
full to `S_C`.

### Proof

By Theorem 4.2 of `hadwiger_c6_two_piece_locks.md`, the graph
`D-{p,q}` has exactly two components; call them `A,B`.  Since `D` is
two-connected, each of `p,q` has a neighbour in each of `A,B`.

For `C` equal to `A` or `B`, the set

\[
                       N_S(C)\cup\{p,q\}
\]

separates `C` from the old opposite shore `H`.  Seven-connectivity gives

\[
                       |N_S(C)|+2\ge 7,
       \qquad\text{hence}\qquad |\Delta_C|\le2.    \tag{2.3}
\]

Apply the exact two-piece atlas to the connected bipartition

\[
                       A\mid (D-A).
\]

The second side is connected because it consists of `B`, the two poles,
and all incident pole edges.  Put

\[
 \Delta_A=S-N_S(A),\qquad
 E_A=S-N_S(D-A).
\]

As `B\subseteq D-A`, one has

\[
                         E_A\subseteq\Delta_B,      \tag{2.4}
\]

so both coordinates have order at most two by (2.3).  The split must be
a negative atlas split, since a positive quotient supplies a literal
`K_7` model after expanding the two connected sides and `H`.  The
low-defect lock, Lemma 4.1 of the cited file, therefore says in
particular that both coordinates are nonempty.

If `|\Delta_A|=2`, take `C=A`.  Otherwise
`\Delta_A={v}`.  In this singleton case the lock cannot be an
antipodal-pair state, nor can `\Delta_A` be its two-element
`N_{C_6}(u)` coordinate.  Hence it is the singleton coordinate and

\[
                         E_A=N_{C_6}(v),            \tag{2.5}
\]

so `|E_A|=2`; (2.4) and
`|\Delta_B|\le2` force `|\Delta_B|=2`, and we take `C=B`.  This proves
(2.1).

For this component `C`, two-connectivity makes both poles actual
neighbours of `C`, so its full external neighbourhood is exactly (2.2).
It has order

\[
                    (7-|\Delta_C|)+2=7.
\]

It separates the nonempty set `C` from `H`, and seven-connectivity says
that it is a minimum, hence exact, cut.  Since `C` is an open component
of a two-separation, it is a proper subset of `D`.

It remains to check that the far side is connected.  Return to the
notation in which `C=A`, so `|\Delta_A|=2`.  The low-defect lock also
says that

\[
                         E_A=S-N_S(D-A)
\]

is nonempty.  Choose `t\in E_A`.  Since `D` is full and neither `B` nor
either pole sees `t`, the component `A` sees `t`; hence
`t\notin\Delta_A`.  On the other hand `t\in\Delta_B`.  If `B` missed
both vertices of `\Delta_A`, then

\[
                    \Delta_A\cup\{t\}\subseteq\Delta_B,
\]

contrary to `|\Delta_B|\le2`.  Thus `B` sees at least one of the two
old boundary vertices in `\Delta_A`.

After deleting `S_C`, all vertices outside `A` therefore lie in the
single connected set

\[
                         B\cup\Delta_A\cup H:
\]

the old shore `H` sees both vertices of `\Delta_A`, and `B` sees at
least one of them.  Hence `G-S_C` has exactly two components.  Every
component behind a minimum cut in a seven-connected graph is full to
the cut (Lemma 3.1 below), so both new shores are full.  QED.

### Corollary 2.2 (the arbitrary SPQR disjunction)

If `D` has a nontrivial reduced SPQR tree, then `G` has a nested exact
seven-cut whose fragment is properly contained in `D`.  Equivalently,
if nested exact-seven descent is excluded, `D` is three-connected.

### Proof

A nontrivial SPQR tree represents a separation pair of the
two-connected graph `D`.  Apply Theorem 2.1.  QED.

### Theorem 2.3 (uniform two-gate descent criterion)

Let `G` be `k`-connected, let `S` be a `k`-cut, and suppose `G-S` has
exactly two connected full shores `D,H`.  Assume `D` is two-connected and
every two-cut of `D` has exactly two open components.  Call a connected
bipartition `X\mid Y` of `D` *negative* when its contracted two-piece
quotient does not contain the target clique minor, and assume
the following two boundary-lock properties:

1. no negative split has both boundary defects of order at most one;
2. whenever both defects have order at most two, neither is empty.

Then every two-cut of `D` exposes a proper component `C` for which

\[
                    (S-N_S(C))\text{ has order }2,
\]

and `N_S(C)\cup\{p,q\}` is a nested exact `k`-cut with exactly two full
shores.

### Proof

Let `A,B` be the two components of `D-{p,q}` and put
`\Delta_A=S-N_S(A)`, `\Delta_B=S-N_S(B)`.  The separators
`N_S(A)\cup\{p,q\}` and `N_S(B)\cup\{p,q\}` give

\[
                         |\Delta_A|,|\Delta_B|\le2. \tag{2.6}
\]

For the split `A\mid(D-A)`, its second defect `E_A` is contained in
`\Delta_B`.  If both open defects had order at most one, both split
defects would have order at most one, contradicting property 1.  Thus one
open defect has order two; rename that component `A`.

The split is negative in a target-minor-free graph.  Property 2 makes
`E_A` nonempty.  Choose `t\in E_A`.  Fullness gives
`t\notin\Delta_A`, while `E_A\subseteq\Delta_B`.  Therefore `B` cannot
miss both vertices of `\Delta_A`, for then its defect would contain the
three-element set `\Delta_A\cup\{t\}`.  The proof of Theorem 2.1 now
applies verbatim: the new cut has order `k`, the far side
`B\cup\Delta_A\cup H` is connected, and minimum-cut fullness gives the
last assertion.  QED.

This criterion is label-free.  The `C_6\dot\cup K_1` atlas is used only
to verify its two lock hypotheses.  It isolates the reusable principle:
once a full boundary forbids an empty defect and a one-defect/one-defect
split, every two-gate failure automatically descends to a new minimum
adhesion.

The conclusion is stronger than a leaf-by-leaf statement: it applies to
every SPQR edge, independent of whether its incident nodes are `R`, `S`
or `P` nodes.  In particular there is no separate `R--S`, `R--P`, or
multi-`R` peeling case once exact-seven descent is one of the target
outcomes.

## 3. Fullness of the descended fragments

The connectivity argument at the end of Theorem 2.1 proves that this
particular descended cut has exactly two complementary components.  The
following standard minimum-cut fact supplies their fullness.

### Lemma 3.1

Every component of `G-S_C` is full to `S_C`.

### Proof

If a component `K` of `G-S_C` missed a vertex `x\in S_C`, then
`S_C-\{x\}` would still separate `K` from every other component.  This
would be a cut of order six, contrary to seven-connectivity.  QED.

Thus the descent stays inside the two-full-shore category.  The proof of
outside connectivity is not a consequence of SPQR theory alone: it uses
the nonempty opposite defect supplied by the exact negative atlas.  This
is why the low-defect lock, rather than mere two-connectivity, is essential
to the recursive statement.

## 4. Why contraction to the poles is not label-faithful

Let `J` be the pertinent subgraph on the `C` side of `{p,q}`.  Replacing
`J` by the virtual edge `pq` is legitimate for testing an unlabelled
minor in the opposite torso.  It is not legitimate for propagating the
six portal classes.

Indeed, a label `s\in S` can satisfy

\[
                P_s\cap C\ne\varnothing,
        \qquad P_s\cap(D-C-\{p,q\})=\varnothing.   \tag{4.1}
\]

After contraction of `J` to `pq`, every occurrence in (4.1) disappears.
Assigning the label to `p` or `q` instead is also invalid: it can identify
two distinct representatives, manufacture a portal incidence not present
in `G`, and change which four-label transversals have rooted `K_4`
models.  The circular order of portal occurrences on a pole face is lost
as well.

The label-faithful replacement is exactly the cut transition (2.2):

* retain the five old boundary vertices in `N_S(C)`;
* promote the two literal poles `p,q` to boundary vertices; and
* move the two omitted old labels `\Delta_C` to the far side of the new
  cut.

This operation preserves every actual portal incidence on the fragment
`C`.  It changes the boundary graph, however.  Therefore the next state
needed for a recursive proof is not another SPQR face bit.  It is a
**boundary-transfer state** recording

1. the missing graph induced by `N_S(C)\cup\{p,q\}`;
2. the contacts (and noncontacts) of each pole with the five retained
   old labels;
3. which exact colour traces survive after the two omitted labels move
   to the opposite full component; and
4. the one-step deletion/contraction transitions across this new
   boundary.

The fixed-core computation in
`hadwiger_c6_rank22_nested_cut_exchange.md`, Section 4, is precisely the
canonical antipodal-pair instance of this boundary-transfer state.  The
multi-node obstruction is therefore not failure of a face to propagate
through an arbitrarily long SPQR tree.  It is failure, after the first
exact descent, to align the old colourful states with the new
seven-boundary operation states.

The selected defect `\Delta_C` is a two-subset of the seven old boundary
vertices.  It need not itself be one of the two-element base defects in
the atlas: a low-defect negative state may have the enlarged
singleton-side defect `\{v,w\}` opposite `N_{C_6}(v)`.  Thus no reduction
to only the neighbour-pair and antipodal-pair cores is valid.

There are nevertheless only three induced old-boundary core types.  To
see this, apply the low-defect lock once more to the split with
two-element coordinate `\Delta_C`.  This coordinate is either
`N_{C_6}(v)`, an antipodal pair, or an enlargement `\{v,w\}` of the
singleton coordinate opposite `N_{C_6}(v)`.  In the last case fullness
of the split makes its two defects disjoint, so

\[
                         w\notin N_{C_6}(v).        \tag{4.2}
\]

Thus two adjacent vertices of the missing cycle never form
`\Delta_C`; the extra vertex is `z`, is at cyclic distance two from
`v`, or is antipodal to `v`.

If
`z\in\Delta_C`, deleting the other vertex from the missing cycle and
deleting the isolated `z` leaves

\[
                              P_5.                 \tag{4.3}
\]

If both deleted vertices lie on the missing cycle, their cyclic distance
is two or three, and the respective remaining missing graphs are

\[
                P_3\dot\cup2K_1,\qquad
                2K_2\dot\cup K_1.                 \tag{4.4}
\]

The two promoted poles then have arbitrary, but literal, missing contacts
to the five-vertex core, together with the possible missing pole edge.
Thus a recursive closure needs pole-defect transition theorems over these
three cores, rather than an unbounded collection of SPQR-node types.
Section 4 of the rank-two note treats a canonical subfamily of the last
core in (4.4).

### Theorem 4.1 (defect pressure and a multiply-hit pole)

Assume now that `G` is a hypothetical minor-minimal `HC_7`
counterexample, so the exact five-defect full-adhesion theorem applies to
the descended cut `S_C`.  Let `F_C=\overline{G[S_C]}` and let

\[
 \lambda=|E(F_C)|-|E(F_C[N_S(C)])|                \tag{4.5}
\]

be the number of new missing edges incident with at least one promoted
pole (counting a missing `pq` once).  Then:

1. in the `P_5` old-core state, `\lambda\ge2`;
2. in the `P_3\dot\cup2K_1` and `2K_2\dot\cup K_1` old-core states,
   `\lambda\ge4`;
3. in either state of item 2, some promoted pole has at least two
   nonneighbours in `S_C`, and consequently has at least two distinct
   neighbours in one of the two open shores of `G-S_C`;
4. in the `P_5` state the same conclusion holds unless the sharp
   boundary pattern has `pq\in E(G)` and exactly one missing pole--core
   edge at each pole.

### Proof

The five-defect closure says that every full exact seven-boundary in a
non-six-colourable `K_7`-minor-free graph has at least six missing edges.
The old cores `P_5`, `P_3\dot\cup2K_1`, and
`2K_2\dot\cup K_1` have respectively four, two, and two edges.  Subtracting
from six proves items 1 and 2.

For a pole `x\in\{p,q\}`, let `m_x` be the number of its nonneighbours
among the other six vertices of `S_C`; a missing `pq` contributes to both
`m_p,m_q`.  If `\lambda\ge4`, then one of `m_p,m_q` is at least two.
Indeed

\[
             m_p+m_q=\lambda+\mathbf1_{pq\notin E(G)}.          \tag{4.6}
\]

The boundary degree of this pole is `6-m_x`.  Since a minimal
counterexample has minimum degree at least seven,

\[
                    |N_G(x)-S_C|\ge m_x+1.          \tag{4.7}
\]

Both open shores are full to `S_C`, so each contains a neighbour of `x`.
When `m_x\ge2`, equation (4.7) gives at least three exterior neighbours;
one of the two shores therefore contains at least two.  This proves item
3.

Finally suppose the `P_5` state has no multiply-hit conclusion.  Then
`m_p,m_q\le1`.  Equation (4.6) and `\lambda\ge2` force `pq` to be present,
`\lambda=2`, and `m_p=m_q=1`; the two missing edges are one pole--core
edge at each pole.  Conversely these counts are exactly the sharp pattern
not eliminated by the degree argument.  QED.

This is the first operation-relevant compression of the transfer family.
All distance-two and antipodal descents expose a literal repeated pole
portal in one new shore.  The only transfer without such a seed is a
balanced `P_5` frame with one defect at each pole.  Thus subsequent
rooted exchange need not analyze arbitrary pole rows: it needs a
split-from-a-repeated-pole lemma plus one balanced path-core web state.

### Theorem 4.2 (uniform boundary transfer to a covering bad split)

Under the hypotheses of Theorem 2.1, strengthen `G` to a hypothetical
minor-minimal `HC_7` counterexample.  If the old shore `D` has a
nontrivial SPQR tree, then, for the descended boundary `S_C`, at least one
of the following occurs:

1. `G` has a `K_7` minor;
2. `G` is six-colourable;
3. one of the two new full shores has a connected adjacent bipartition
   `X\dot\cup Y` whose contact rows cover `S_C`, whose three-helper
   quotient is `K_7`-minor-free, and which carries the strict one-step
   deletion/contraction boundary states of minor-criticality.

In outcome 3, either `N_{S_C}(X)\cup N_Y(X)` (or its symmetric mate) is
another nested exact seven-cut, or the corresponding interface has
strict surplus over order seven.

### Proof

Theorem 2.1 produces an exact seven-cut with exactly two full shores.
The exact-block/private-state theorem makes its missing graph nonsplit.
The cyclic-hull lemma and the closure of the sole exceptional
`2K_3\dot\cup K_1` boundary therefore give a cyclic hull.  If both shore
societies are crossless, the web-gluing half of the full-split theorem
six-colours `G`, which is outcome 2.  Hence one shore has a crossing.

Extend its two disjoint crossing carriers to a connected adjacent
partition `X\dot\cup Y` of the whole shore.  Their two contact rows cover
`S_C` by fullness.  If every compatible partition quotient has a
`K_7` minor, the quotient model expands to outcome 1.  Otherwise the
actual contact rows contain a bad partition quotient, giving outcome 3.
Every internal deletion or contraction produces a strict boundary state
accepted by the unchanged opposite full shore and rejected by the
original unoperated shore; this is the standard full-shore
minor-transition theorem.

Finally seven-connectivity gives

\[
                  |N_{S_C}(X)|+|N_Y(X)|\ge7.
\]

Equality is the nested exact-cut outcome, while strict inequality is the
surplus alternative.  This is Lemma 2.3 of
`hadwiger_full_split_cyclic_hull.md`.  QED.

The theorem is a label-faithful SPQR transfer principle.  It eliminates
the unbounded SPQR tree without contracting its portal labels: first
change the boundary by exact descent, then use a cyclic hull to extract
one actual covering split.  The unresolved object is consequently the
same operation-sensitive bad split already present in the general exact
adhesion programme, not a new family indexed by SPQR length or node type.

### Corollary 4.3 (doubled-pole versus balanced-path normal form)

Modulo a `K_7` minor, a six-colouring, or another nested exact seven-cut,
the first SPQR descent has one of the following two forms.

1. The new boundary core is `P_3\dot\cup2K_1` or
   `2K_2\dot\cup K_1`, and one new shore has a covering bad split whose
   two contact rows both contain the same promoted pole.
2. The core is `P_5`; either the same doubled-pole conclusion holds, or
   `pq` is present and the poles have exactly one core noncontact each.
   In that balanced case Theorem 4.2 still supplies a cyclic-hull
   covering bad split, but it need not double a pole label.

### Proof

In every non-balanced state, Theorem 4.1 gives a pole `x` with two
distinct neighbours in one open shore `R`.  Lemma 6.1 of
`hadwiger_root_multiplicity_split.md` partitions `R` into adjacent
connected sets `R_1,R_2` which both meet the `x`-portal class and whose
contact rows cover the new boundary.  Contract `R_1,R_2` and the opposite
full shore.  A positive quotient gives `K_7`; otherwise this is the
claimed doubled-pole bad split.  Its interface again gives an exact cut
at equality and strict surplus otherwise.  The only state in which the
degree count does not force such a repeated pole is exactly the balanced
`P_5` row of Theorem 4.1; apply Theorem 4.2 there.  QED.

The normal form retains one concrete label in both sides of the rich
split.  That is precisely the information lost by contracting an SPQR
subtree to its poles and is the appropriate root for a coupled two-edge
star/Kempe operation at the next exchange step.

### Lemma 4.4 (the balanced `P_5` state is not a six-defect survivor)

The exceptional balanced state in Corollary 4.3 cannot occur in a
hypothetical counterexample.

### Proof

In that state the new missing graph consists of the four edges of the
old-core `P_5` and exactly two pole--core edges, one incident with each
pole; the pole edge `pq` is present.  Hence it has exactly six edges, and
both promoted poles have missing-graph degree one.

The audited exact six-edge boundary theorem says that the only
counterexample-derived six-edge complement is

\[
                         C_6\dot\cup K_1.
\]

That graph has degree sequence `(2,2,2,2,2,2,0)` and in particular has
no degree-one vertex.  The balanced `P_5` graph has at least the two
degree-one promoted poles, so it is not isomorphic to the sole survivor.
All other six-edge types close by a `K_7` minor or a six-colouring.
QED.

### Corollary 4.5 (uniform repeated-pole transfer)

Every first SPQR descent in a hypothetical counterexample exposes a
promoted pole with two distinct neighbours in one of the two new full
shores.  Consequently, modulo another exact-cut descent, it produces a
covering negative split whose two rows contain that pole label and which
carries one of the two faithful states in Corollary 4.6 below.

### Proof

Theorem 4.1 forces a repeated pole in every state except the balanced
`P_5` state, and Lemma 4.4 eliminates that exception.  Apply the
root-multiplicity split and quotient argument in Corollary 4.3.  QED.

### Corollary 4.6 (the repeated pole carries one of two faithful states)

In the doubled-pole outcome, choose distinct neighbours `a,b` of the
repeated pole `x` in the same new shore.

* If `ab\notin E(G)`, contracting the star `x-a-b` and expanding a
  six-colouring gives the coupled two-edge Kempe lock of
  `hadwiger_two_edge_star_kempe_lock.md`.
* If `ab\in E(G)`, there is a connected covering split separating
  `a,b` for which `ab` is an interface edge.  Deleting `ab` gives the
  internal-ear-or-two-boundary-anchors state of
  `hadwiger_bad_split_interface_exchange.md`.

### Proof

The first item is exactly Theorem 1.1 of the cited star-lock note: `x`
is the centre and the two nonadjacent shore vertices are its leaves.

For the second, choose a spanning tree of the shore containing the edge
`ab` and delete that tree edge.  Its two vertex sets are connected,
adjacent through `ab`, contain `a,b` on opposite sides, both contact the
boundary label `x`, and together cover the boundary because they
partition a full shore.  Apply the edge-deletion interface theorem to
`ab`.  QED.

Thus the rich first-level transfer is not merely a repeated-contact
count.  It comes with either a coupled contraction state or an
interface-edge deletion state in the same labelled split geometry.  The
remaining proof obligation is to turn those states into a positive
rooted model or a common boundary colouring; no additional SPQR
classification is required.

## 5. Audit boundary

Theorem 2.1 uses only:

1. seven-connectivity;
2. two-connectivity of a nonsingleton full shore;
3. the proved assertion that a two-cut has exactly two open components;
4. the low-defect part of the exact `C_6\dot\cup K_1` two-piece atlas;
   and
5. the standard lifting of a positive connected quotient model.

It does not use a common web face, an SPQR reflection, or a contraction
of labelled portal subtrees.  It therefore bypasses the precise flaw in
the retracted one-web leaf argument.

What it does **not** prove is closure after recursively changing the
boundary.  A proof that refuses to stop at exact-seven descent must solve
the boundary-transfer problem in Section 4; the direct `R--R` rural
theorem alone cannot do that.
