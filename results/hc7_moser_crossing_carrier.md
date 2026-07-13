# The pure-Moser crossing: literal carrier completion and its rural blocker

## Status

This note proves the constructive part of the degree-seven, two-exterior-
component pure-Moser cell.  It does **not** claim to close the cell.  Its main
outputs are:

1. the guarded cyclic-shore theorem and the three-apex theorem force a literal
   rooted `K_4` in one exterior shore;
2. that rooted `K_4` lifts to a literal `K_7` as soon as the other shore has two
   disjoint connected carrier pieces satisfying the exact missing contacts;
3. each carrier has at most two repair duties, and a duty-free row closes
   unconditionally; and
4. when there is one duty on each row, failure of the carrier lift has an exact
   four-port disk/web certificate.  That one-shore disk is not by itself a
   three-apex certificate.

The last point identifies the remaining proof obligation without making an
unsafe palette-to-label inference.  The result is label-free up to Section 4;
the Moser labels enter only to bound the two duty sets.

## 1. Setup and the forced crossing

Let `G` be a hypothetical minor-minimal counterexample to `HC_7`, let `v` be a
degree-seven vertex, and put `N=N_G(v)`.  Assume that `G-N[v]` has exactly two
components `C_1,C_2`, each of which has neighbourhood exactly `N`.  In the
pure-Moser cell label `N={0,1,2,3,4,5,6}` so that

\[
 E(G[N])=\{01,02,03,04,12,16,26,34,35,45,56\}.       \tag{1.1}
\]

Choose the repeated nonedge `13` and set

\[
 U=N-\{1,3\}=\{0,2,4,5,6\}.
\]

The graph `G[U]` is the five-cycle

\[
                 0-2-6-5-4-0.                           \tag{1.2}
\]

Apply the audited guarded cyclic-shore theorem with

\[
 A=\{v,1,3\},\qquad R=U,\qquad D_i=C_i.                \tag{1.3}
\]

If neither portal tuple is crossed, that theorem says that `G-A` is planar.
The audited three-apex planar theorem then gives a `K_7` minor because
`chi(G)=7`.  Consequently, in a `K_7`-minor-free counterexample, one portal
tuple is crossed.  Relabel the two exterior components so that it is the tuple
of `C_1`.

Replacing the four artificial terminal ends by their actual roots and portal
edges, and adding the four intervening arcs of (1.2), gives a rooted
subdivision of `K_4` in `G[C_1\cup U]`.  Cut one edge on each of its six
subdivided edges and assign the two remaining path segments to their ends.
This produces four disjoint connected pairwise adjacent branch sets

\[
                         B_1,B_2,B_3,B_4.                \tag{1.4}
\]

Each `B_i` contains a distinct selected root of `U`.  The unselected fifth
root lies internally on one of the four frame arcs; assign it to either branch
set incident with that arc.  Thus every vertex of `U` belongs to one of the
four bags, and every bag contains at least one vertex of `U`.

## 2. The literal two-carrier completion theorem

The following statement is independent of the Moser graph.

### Theorem 2.1 (two-row carrier completion)

Let `v,a,b` be distinct vertices of a graph, with `v` adjacent to `a,b`.
Let `B_1,\ldots,B_4` be disjoint connected pairwise adjacent sets, disjoint
from `\{v,a,b\}`, such that `v` has a neighbour in every `B_i`.  Let `D` be a
connected set disjoint from `\{v,a,b\}` and from all four `B_i`.

Put

\[
 I_a=\{i:E(a,B_i)=\varnothing\},\qquad
 I_b=\{i:E(b,B_i)=\varnothing\}.                        \tag{2.1}
\]

For every `i\in I_a` choose `r_i\in B_i`, and for every `i\in I_b` choose
`s_i\in B_i`.  Suppose there are disjoint connected sets `X,Y\subseteq D`
such that

* `E(X,Y)\ne\varnothing`;
* `X` has a neighbour at `a` and a neighbour at every `r_i`, `i\in I_a`;
* `Y` has a neighbour at `b` and a neighbour at every `s_i`, `i\in I_b`.

Then the graph has a literal `K_7` model.

#### Proof

Take the seven bags

\[
 \{v\},\quad B_1,B_2,B_3,B_4,\quad \{a\}\cup X,
                                      \quad \{b\}\cup Y. \tag{2.2}
\]

They are pairwise disjoint.  The first five are connected, and the last two
are connected because `a` has a neighbour in `X` and `b` has a neighbour in
`Y`.  The four `B_i` are pairwise adjacent.  The singleton `\{v\}` is adjacent
to every `B_i` and to the last two bags.  The last two bags are adjacent by an
`X-Y` edge.  If `i\notin I_a`, the original edge from `a` to `B_i` gives the
required adjacency; if `i\in I_a`, the chosen `X-r_i` edge does.  The argument
for `\{b\}\cup Y` is identical.  Hence every two bags in (2.2) are adjacent.
\(\square\)

The theorem deliberately asks for literal portal contacts.  No colour class
is identified with a pre-existing bag.

### Lemma 2.2 (adjacent enlargement)

If a connected graph contains two disjoint nonempty connected sets `X_0,Y_0`,
then it contains disjoint connected supersets `X\supseteq X_0`,
`Y\supseteq Y_0` with an edge between `X` and `Y`.

#### Proof

Choose a shortest path `x_0\ldots x_k` with `x_0\in X_0` and `x_k\in Y_0`;
its internal vertices may be chosen outside `X_0\cup Y_0`.  Add
`x_1,\ldots,x_{k-1}` to `X_0`.  The resulting two sets remain disjoint and
connected, and the last edge of the path joins them. \(\square\)

Thus a disjoint two-Steiner packing already supplies the adjacency demanded
by Theorem 2.1.

## 3. Exact Moser duty bounds

Apply Theorem 2.1 with

\[
             a=1,\qquad b=3,\qquad D=C_2.               \tag{3.1}
\]

The relevant neighbourhoods on `U` are

\[
 N_U(1)=\{0,2,6\},\qquad N_U(3)=\{0,4,5\}.             \tag{3.2}
\]

### Lemma 3.1 (two duties per row)

For the four rooted bags in (1.4),

\[
                         |I_1|\le2,\qquad |I_3|\le2,     \tag{3.3}
\]

and `I_1\cap I_3=\varnothing`.

#### Proof

Every bag contains a selected root in `U`.  If `i\in I_1`, every `U`-vertex
of `B_i` must avoid `N_U(1)`, so its selected root lies in `\{4,5\}`.  Distinct
bags have distinct selected roots, proving `|I_1|\le2`.  Similarly, a bag in
`I_3` has selected root in `\{2,6\}`, proving the other bound.

A bag in both duty sets would contain a selected root lying in
`\{4,5\}\cap\{2,6\}`, which is empty. \(\square\)

For `i\in I_1`, choose any `U`-vertex `r_i\in B_i`; necessarily
`r_i\in\{4,5\}`.  For `i\in I_3`, choose `s_i\in B_i\cap U`; necessarily
`s_i\in\{2,6\}`.  Full attachment of `C_2` to `N` makes all corresponding
portal sets nonempty.

### Proposition 3.2 (a duty-free row closes)

If `I_1=\varnothing` or `I_3=\varnothing`, then `G` has a `K_7` minor.

#### Proof

Suppose `I_1=\varnothing`.  Since `C_2` is connected and is full to `N`, it
has a connected subgraph `Y` meeting the portal sets of `1`, `3`, and every
chosen `s_i`, `i\in I_3`: take the union of paths in `C_2` from one fixed
portal to all the others.  Use `\{1\}` as the first row bag and
`\{3\}\cup Y` as the second.  The first row contacts all four `B_i` by
`I_1=\varnothing`; it contacts the second row because `Y` meets a portal of
`1`.  The second row contacts all missing bags through the selected `s_i`.
Together with `\{v\},B_1,\ldots,B_4`, these are the seven bags in the proof of
Theorem 2.1.  The case `I_3=\varnothing` is symmetric. \(\square\)

Consequently the surviving crossing has one or two duties on **each** row.
This is the precise point at which a single connected shore must be split.

### Corollary 3.3 (the carrier shore is packet-thin)

Call a connected subgraph of `C_2` **`N`-full** when every literal vertex
of `N` has a neighbour in it.  In a surviving crossing, `C_2` does not
contain two vertex-disjoint `N`-full connected subgraphs.

#### Proof

Suppose `X_0,Y_0\subseteq C_2` were two such subgraphs.  They meet the
portal sets of `1`, `3`, and every selected duty root in (2.1).  Lemma 2.2
enlarges them inside connected `C_2` to disjoint adjacent connected sets
`X,Y`, without losing any of those contacts.  Assign `X` to row `1` and
`Y` to row `3`.  All hypotheses of Theorem 2.1 hold, so its seven bags
give a literal `K_7` model, a contradiction. \(\square\)

Thus the rural blocker below is automatically an actual packing-number-one
shore.  This is stronger than connectedness, but it does not assert a
one- or two-vertex transversal of all full packets.

## 4. The one-duty case: linkage or an exact rural disk

We first record a uniform four-port theorem.  It uses the generalized Two
Paths theorem in the same form already audited for the guarded cyclic-shore
theorem.

### Theorem 4.1 (seven-boundary four-port linkage or disk)

Let `G` be seven-connected, let `S` be a seven-vertex cut, and let `D` be a
nonempty component of `G-S`.  Assume `G-(D\cup S)` is nonempty.  Let
`p_0,p_1,p_2,p_3` be four distinct members of `S`, each with a neighbour in
`D`.

Then exactly one of the following conclusions is supplied by the proof.

1. There are vertex-disjoint paths with interiors in `D`, one joining
   `p_0` to `p_2` and one joining `p_1` to `p_3`.
2. `G[D\cup\{p_0,p_1,p_2,p_3\}]` has an embedding in a closed disk in which
   `p_0,p_1,p_2,p_3` occur on the boundary in that cyclic order.

#### Proof

Form `Q` from `G[D]` by adding four artificial terminals `t_i`, where `t_i`
is adjacent precisely to `N_D(p_i)`, and copy between terminals every edge
of `G[\{p_0,p_1,p_2,p_3\}]`.  Apply the generalized Two Paths theorem to the
ordered tuple `(t_0,t_1,t_2,t_3)`.

If the tuple is crossed, its two terminal-clean paths have the alternating
pairing `t_0-t_2,t_1-t_3`.  Replace each artificial end and its incident edge
by the corresponding actual root and portal edge.  A one-edge terminal path
is replaced by the corresponding actual boundary edge.  This gives outcome
1.

Otherwise `Q` has a same-vertex edge completion to a four-web.  Let `X` be
the set of original vertices of `D` in one clique inserted behind a facial
triangle of its planar rib.  All neighbours of `X` represented in `Q` lie in
that clique or among the at most three vertices of the facial triangle.
Replace each artificial terminal among those triangle vertices by its
corresponding actual root.  In the original graph the only additional possible neighbours of
`X` are the three unrepresented vertices of `S`.  Therefore

\[
                            |N_G(X)|\le3+3=6.             \tag{4.1}
\]

This set separates nonempty `X` from the nonempty far side
`G-(D\cup S)`, contrary to seven-connectivity.  Hence every original vertex
of `D` lies in the planar rib.

Delete every completion edge not belonging to `Q`.  Delete the artificial
terminals, replace retained terminal-shore edges by their literal root-shore
edges, and replace retained terminal-terminal edges by their copied literal
boundary edges.  The frame terminals lie on the disk boundary in the stated
order, so this gives outcome 2. \(\square\)

The disk conclusion is stronger than merely saying that the prescribed
linkage fails: it fixes the literal cyclic portal order and confines every
attachment of the four represented labels to one rural society.

### Corollary 4.2 (one duty on each row)

Suppose in the Moser setup that `I_1=\{i\}` and `I_3=\{j\}`.  Choose
`r\in B_i\cap U` and `s\in B_j\cap U`.  Then either `G` has a `K_7` minor,
or

\[
                    G[C_2\cup\{1,3,r,s\}]               \tag{4.2}
\]

has a disk embedding with boundary order

\[
                              1,3,r,s.                   \tag{4.3}
\]

#### Proof

Lemma 3.1 makes `i\ne j` and makes `1,3,r,s` distinct.  Apply Theorem 4.1
to the cut `S=N(v)`, the component `D=C_2`, and the ordered tuple
`(1,3,r,s)`.  In its first outcome let `X_0,Y_0` be the interiors in `C_2`
of the `1-r` and `3-s` paths.  Since `1r` and `3s` are absent by the
definitions of the duty sets, both interiors are nonempty.  Apply Lemma 2.2
inside connected `C_2` to make them adjacent.  Theorem 2.1 then gives a
literal `K_7` model.  The other outcome is exactly (4.2)--(4.3). \(\square\)

For the favorable Moser crossing obtained by omitting `6` and assigning it
to the bag rooted at `5`, the two duties are `r=4` for row `1` and `s=2` for
row `3`.  The residual disk order is therefore

\[
                              1,3,4,2.                   \tag{4.4}
\]

The symmetric favorable crossing omitting `5` gives the analogous fixed
four-port order.

### Proposition 4.3 (the residual order is genuinely compatible)

In the favorable normalization above, let `P_{05}` and `P_{24}` be the two
disjoint external paths in `C_1` returned by the crossing.  Then the crossed
closed shore contains the literal cycle

\[
 L=1-0-3-4-P_{42}-2-1,                                 \tag{4.5}
\]

and the four vertices `1,3,4,2` occur on `L` in exactly the rural order
`1,3,4,2` from (4.4).

#### Proof

The four boundary edges `10,03,34,21` belong to (1.1).  The path `P_{42}`
has its interior in `C_1`, hence avoids all boundary vertices.  Their union
is therefore the simple cycle (4.5), with the displayed order. \(\square\)

Thus the audited rural cycle-order exchange does not return an order-mismatch
`K_4` here: the forced order on the rural shore and a literal order on the
crossed shore agree.  The second crossing path `P_{05}` has only the vertex
`0` on (4.5) and its other boundary end is the fifth label `5`; it does not
by itself furnish a second four-port cycle of incompatible order.

This calculation also makes the topological residue precise.  The crossed
shore supplies one page with spine order (4.5), the rural shore supplies a
second page with the same four-port order, and the vertex `v`, adjacent to
all four spine labels, can supply a third page.  Compatibility of the first
two pages therefore does not make their union with `v` planar: the coarse
three-page incidence already contains the `K_{3,4}` obstruction.  To invoke
the three-apex theorem one must prove that one page can be absorbed or that
all three pages admit a single planar embedding; order agreement alone does
neither.

## 5. Why the rural outcome is not yet three-apex

The disk in Corollary 4.2 belongs only to `C_2` and four boundary labels.
The opposite component `C_1` still contains the rooted `K_4` crossing that
created the bags `B_1,\ldots,B_4`.  Consequently (4.2) does not imply that
deleting the other three boundary labels makes the whole graph planar.
Attaching one further vertex to four boundary vertices of a disk can create
the familiar third-page obstruction (the coarse incidence graph is of
`K_{3,4}` type).  Thus the audited three-apex theorem cannot be applied at
this point.

Nor does one proper-minor colouring remove this obstruction.  The audited
dynamic locked-gate theorem gives the exact safe state.  With

\[
 C=G[C_2\cup N],\qquad O=G-C_2,                          \tag{5.1}
\]

write `Ext(J,N)` for the labelled equality partitions of `N` induced by
six-colourings of `J`.  In a minor-minimal non-six-colourable graph,

\[
                 Ext(C,N)\cap Ext(O,N)=\varnothing,       \tag{5.2}
\]

whereas every internal deletion or contraction `\mu` in `C_2` produces a
partition in

\[
                 Ext(C/\mu,N)\cap Ext(O,N).              \tag{5.3}
\]

A single rural carrier can preserve the alternating order (4.3) while an
internal deletion/contraction creates a locked palette state; the audited
square-antiprism construction in
`../results/hc7_near_k7_dynamic_locked_gate.md` is an explicit example.
It is not a full `HC_7` counterexample, but it proves that one cannot infer a
labelled rerouting from a single transition colour by itself.

The exact dynamic contradiction still available is this: if an operation
inside `C_1` and an operation inside `C_2` produce the same labelled equality
partition of `N`, the unchanged closed sides splice and six-colour `G`.
Therefore a residual rural configuration must keep **all** operation states
from the two shores disjoint.  Establishing a collision of those labelled
partitions, or proving that the two rural societies have compatible global
orders yielding an actual three-apex embedding, is the remaining exchange
step.  Merely comparing colour names is insufficient.

## 6. The remaining carrier problem

After the closures above, each of `I_1,I_3` has order one or two.  The
unresolved constructive demand is:

> find disjoint connected adjacent `X,Y\subseteq C_2` such that `X` meets
> the portal sets of `1` and at most two roots in `\{4,5\}`, while `Y` meets
> the portal sets of `3` and at most two roots in `\{2,6\}`.

This is a two-versus-at-most-three set-linkage problem.  When both duty sets
have order one, Corollary 4.2 identifies its exact rural obstruction.  When a
duty set has order two, the generic abstraction is a `(2,3)`-linkage problem;
it is not a routine consequence of seven-connectivity.  A valid completion
must exploit the actual seven-boundary equality states or the already-crossed
opposite shore, not assert an unproved set-root version of Two Paths.

## Dependency chain

1. `../results/hc7_guarded_cycle_web_exchange.md` and its GREEN audit.
2. `../results/hc7_three_apex_planar_endgame.md` and its GREEN audit.
3. The generalized Two Paths/web completion theorem in the same form audited
   in item 1.
4. For Section 5 only,
   `../results/hc7_near_k7_dynamic_locked_gate.md` and its GREEN audit.

No computational enumeration is used in this note.
