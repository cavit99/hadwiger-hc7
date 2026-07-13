# Opposite crossings force a rooted-prism obstruction in the `C6+K1` core

> **Retraction notice (two-cut section).**  Lemma 4.1 below is false as
> stated.  The current verifier produces the opposite-frame support
> words `001001`, `010010`, and `100100`.  For example, boundary contact
> masks `(a,b,p,q)=(109,118,0,0)` with no `pq` edge pass all four coarse
> allocation tests and visibly support frames 0 and 3.  The program's
> final assertion therefore fails.  Sections 1--3 and 5 remain separate;
> no conclusion may be drawn from Section 4 until row locks, Hall data,
> or another missing full-graph hypothesis is added.  The exact output is
> recorded in `hadwiger_c6_twocut_counterstate.md`.

## 1. Setting and six frames

Let `S={z,c_0,...,c_5}`.  The vertex `z` is complete to the other six
boundary vertices, and the only missing boundary edges are

\[
 e_i=c_ic_{i+1}\qquad(i\in\mathbb Z/6\mathbb Z).       \tag{1.1}
\]

Let `D_1,D_2` be the two connected full shores.  For frame `i`, an
**`i`-crossing in a shore** consists of disjoint connected sets `X_i,Y_i`
which are adjacent and satisfy

\[
\begin{aligned}
 X_i&\text{ touches }c_{i-2},c_{i-1},\\
 Y_i&\text{ touches }c_{i+2},c_{i+3}.
\end{aligned}                                           \tag{1.2}
\]

These are exactly the two pieces obtained from an alternating crossing
of the relaxed four-frame which omits `c_i,c_{i+1},z`.  The web-gluing
theorem proves that, in a seven-chromatic survivor, every one of the six
frames is crossed in at least one shore.

Throughout Sections 4--5 we also use the counterexample-derived
inequality `delta(G)>=7` and global seven-connectivity.

Frames `i` and `i+3` will be called **opposite**.

This terminology refers to the six *four-terminal frames*.  It should not
be confused with the three antipodal pairs of individual missing edges
`e_i|e_{i+3}`.  A two-linkage for one of those antipodal edge pairs
already has a positive elementary quotient; the difficult frame
crossings join two edges of the same alternating matching.

## 2. The opposite-crossing model

### Lemma 2.1 (compatible opposite crossings)

Suppose an `i`-crossing and an `(i+3)`-crossing can be chosen so that
their four pieces are pairwise disjoint.  The crossings may lie in the
same shore or in different shores.  Then `G` contains a `K_7` minor.

### Proof

Rotate indices so that `i=0`.  Use the seven bags

\[
\begin{array}{c}
 \{c_2\},\quad \{c_5\},\quad \{z\},\\[2mm]
 X_0\cup\{c_4\},\quad Y_0\cup\{c_3\},\quad
 X_3\cup\{c_1\},\quad Y_3\cup\{c_0\}.              \tag{2.1}
\end{array}
\]

Each composite bag is connected by its displayed contact.  The first
two composite bags are adjacent through the `X_0-Y_0` edge, and the last
two through the `X_3-Y_3` edge.  Every cross-pair between those two
groups has boundary anchors at cyclic distance two or three, and hence
is a boundary edge.

The singleton `c_2` has only the two missing boundary adjacencies to
`c_1,c_3`; they are repaired because `X_3` and `Y_0`, respectively,
touch `c_2`.  Similarly, the two missing adjacencies from `c_5` to
`c_4,c_0` are repaired by the contacts of `X_0,Y_3`.  The vertices
`c_2,c_5` are adjacent, and `z` sees every boundary-anchored bag.  Thus
all seven bags are pairwise adjacent.  They are disjoint by hypothesis,
so (2.1) is a `K_7` model.  \(\square\)

The proof uses no internal edge between the two opposite crossings.
Consequently crossings in different shores are automatically compatible.

### Corollary 2.2 (exact frame ownership)

In a `K_7`-minor-free, non-six-colourable realization:

1. no frame is crossed in both shores;
2. each opposite pair `{i,i+3}` is crossed entirely in one shore; and
3. one shore owns at least two opposite pairs, hence at least four of the
   six frames.

### Proof

Every frame is crossed somewhere.  If frame `i` is crossed in `D_1` and
frame `i+3` in `D_2`, Lemma 2.1 applies.  Thus the two members of an
opposite pair cannot be split between the shores.  If a frame were
crossed in both shores, whichever shore contains its opposite frame
would again give a cross-shore application of Lemma 2.1.  Hence every
frame has a unique owner, and each opposite pair has one owner.  There
are three opposite pairs and two shores, proving item 3.  \(\square\)

This is substantially stronger than six unrelated applications of the
Two Paths Theorem.  The residual is now concentrated in one shore: that
shore carries two pairs of opposite linkages, but every opposite pair of
linkages is forced to intersect in every choice.

### Corollary 2.3 (pairwise-but-not-triple linkage form)

The six missing cycle edges split into the two alternating perfect
matchings

\[
 \{e_0,e_2,e_4\},\qquad \{e_1,e_3,e_5\}.            \tag{2.2}
\]

The three frames of each parity are exactly the three pairwise
two-linkage demands on the corresponding matching.  Thus all six edges
of these two auxiliary triangles are supplied by the shores, subject to
the ownership rule in Corollary 2.2.  On the other hand, Theorem 2.1 of
`hadwiger_c6_three_linkage_exclusion.md` proves that neither shore can
supply all three paths of either matching simultaneously: a minimal tree
joining the three path interiors gives an explicit `K_7` model in every
tree case.

Accordingly the surviving shore is a **pairwise-but-not-triple linkage
obstruction** for two prescribed three-pair systems.  This is the exact
place where a rooted-prism/rope theorem applies; it is stronger than
mere pairwise portal connectivity.

No coherent choice of portal representatives is being asserted here.
Different frame crossings may meet different vertices of the same portal
class.  In particular, formal cyclic inequalities between portal *labels*
do not prove that two same-shore separators cross.  Lemma 2.1 uses actual
pairwise-disjoint branch pieces; Corollary 2.2 uses it automatically only
across the two anticomplete shores.  The intersecting same-shore system is
left explicitly as the rope obstruction in Section 6.

## 3. A label-free formulation

The preceding argument is an instance of a reusable principle.  Let a
boundary graph be the complement of a cyclic frame, with any vertices
complete to that frame placed outside it.  A **repair linkage** is a
two-path linkage for two independent frame edges.  Call two repair
linkages *complementary* when their four anchored pieces, together with
the untouched boundary vertices, give a clique model by the finite
boundary quotient.

> **Complementary-linkage ownership principle.**  If complementary
> repair linkages have a positive disjoint quotient, then in a
> target-minor-free two-shore realization the two linkages cannot lie in
> different shores.  If every frame obstruction must occur in some shore,
> the complementary-linkage graph on the frame obstructions is therefore
> monochromatic on each connected component under the shore assignment.

This statement is simply the lifting argument of Lemma 2.1, but it
separates the finite boundary calculation from the unbounded shore
geometry.  In the present `C_6` cell the complementary-linkage graph is
the perfect matching `i--(i+3)`, and Corollary 2.2 is its exact
two-colour consequence.

## 4. Exact interaction with a shore two-cut

Let `{p,q}` be a two-cut of a shore.  The theorem in
`hadwiger_c6_two_piece_locks.md` says that there are exactly two
components `A,B`, each having at least five boundary contacts.  Contract
`A,B,p,q` but retain their four distinct vertices.  Each component is
adjacent to both cut vertices.  A frame crossing is called **visible at
the two-cut** if its two paths project to vertex-disjoint paths in this
four-vertex quotient.

### Lemma 4.1 (coarse two-cut signatures; finite certificate)

Assume all four connected allocations of `p,q` to the two component
sides, and the two singleton cut-vertex splits, have bad two-piece
quotients.  Then the set of frames visibly
crossed by the four-vertex quotient is contained in three cyclically
consecutive frames.  In particular it contains no opposite pair.

### Certificate

There are only `3^7` full contact covers for a connected bipartition.
The exact bad family has 762 ordered contact pairs, of which 760 have
both contact rows nonempty.  Enumerate component
contact rows of order at least five and the two cut-vertex rows, retaining
the state only when each of

\[
\begin{array}{c}
 A\mid Bpq,\quad Ap\mid Bq,\quad Aq\mid Bp,\quad Apq\mid B
\end{array}                                           \tag{4.1}
\]

is in that exact bad family.  There are 6,240 contact-row states.  For
each state and each choice of the edge `pq`, enumerate the two disjoint
paths in the four-node quotient.  The inclusion-maximal support words are

\[
 000111,001110,011100,111000,110001,100011,           \tag{4.2}
\]

the six rotations of a three-edge interval.  All other support words are
subwords of these.  None contains positions `i,i+3`.

The dependency-free program `c6_twocut_support_probe.py` performs the
enumeration, derives the bad pairs from the replayed `K_7` branch
partitions, and prints all 21 support signatures.  This is a finite
statement about the cut quotient; it makes no assertion that an arbitrary
crossing inside a large component projects injectively through the cut.

Combining Lemma 4.1 with Corollary 2.2 shows exactly what remains at a
two-cut: some owned opposite crossing must be **nonvisible**, so two
disjoint strands traverse the same component of the two-sum.  Mutual
portal separation then turns that component into a rope bridge.  Thus the
two-cut residual is no longer an arbitrary contact distribution; it is a
nonprojectable rope-linkage.

## 5. Cyclic shores and degree-two vertices

The exact low-defect atlas also excludes the most obvious rope/web
exception.

### Lemma 5.1 (no cyclic full shore)

No nonsingleton full shore is a cycle.

### Proof

Suppose `D=x_1...x_nx_1`, `n>=4`.  For each `i`, put

\[
 d_i=S-N_S(x_i).
\]

Minimum degree seven and the two shore neighbours of `x_i` give
`|d_i|<=2`.  Since `D-x_i` is connected, the defect of the other side of
the split is

\[
 e_i=\bigcap_{j\ne i}d_j.                            \tag{5.1}
\]

The low-defect part of the exact `C_6+K_1` split atlas says that both
coordinates of every bad split with defects of order at most two are
nonempty.  Hence every `d_i` and every `e_i` is nonempty.  Fullness says
`\bigcap_i d_i=emptyset`.

Choose `a_i in e_i`.  Then `a_i notin d_i` but `a_i in d_j` for every
`j ne i`.  The `a_i` are distinct, and `d_j` contains the `n-1` elements
`a_i`, `i ne j`.  Since `|d_j|<=2`, this forces `n<=3`, a contradiction.
\(\square\)

The same argument gives an exact local lock which is useful in any
rope decomposition.

### Lemma 5.2 (degree-two portal lock)

If a vertex `x` of a nonsingleton shore has exactly two neighbours in
the shore, then for a unique rim vertex `v`

\[
 S-N_S(x)=N_{C_6}(v),\qquad
 S-N_S(D-x)=\{v\}.                                  \tag{5.2}
\]

In particular, `x` is the unique shore portal of `v`, has exactly five
boundary neighbours, and has degree exactly seven in `G`.

### Proof

Two-connectivity of the shore makes `D-x` connected.  Degree seven gives
at least five boundary contacts at `x`, while global seven-connectivity
applied to `D-x` gives at least six contacts there.  Thus the two split
defects have orders at most two and one, respectively.  They are
nonempty.  In the exact low-defect atlas, the only row with one coordinate
a singleton and the other of order at most two is
`N_{C_6}(v)|{v}` (up to reversal).  The size bounds fix the displayed
orientation.  The degree assertion follows.  \(\square\)

## 6. Exact remaining structural gap

Corollary 2.2 and Lemma 5.1 leave neither independent frame choices nor
a simple cyclic shore.  A survivor has a shore with at least four frame
crossings arranged as two opposite pairs, but every two opposite
crossings are incompatible: any choices intersect.

If the other shore is a singleton, it cannot contain a crossing (two
disjoint terminal paths cannot both use its sole internal vertex), so the
nonsingleton shore owns all six frames.  It is then pairwise linkable on
both alternating three-pair systems, while
`hadwiger_c6_three_linkage_exclusion.md` forbids a simultaneous
three-linkage on either system.  Thus the singleton cell is also absorbed
into the same pairwise-but-not-triple rope obstruction; its separate
edge-deletion colouring witnesses provide additional reserved paths but
are not needed for the ownership reduction.

Equivalently, after adding the relevant boundary chords, the shore has
two prescribed cycle systems which cannot be made vertex-disjoint.  This
is a rooted-prism/rope-bridge obstruction, not another finite contact
case.  A complete closure now needs the following structural implication:

> **Rooted prism-or-web lemma for the shore.**  Two incompatible opposite
> frame pairs either produce a boundary-rooted `C_6` model, or induce a
> laminar rope/web decomposition whose adhesion is colour-gluable.

A boundary-rooted `C_6` model immediately gives `K_7`: the six cycle
adjacencies come from the rooted model, all nonconsecutive adjacencies
come from the complement-cycle boundary, and `{z}` is the seventh bag.
The pure cycle case has been removed, and every degree-two rope vertex
has the exact portal lock (5.2).  What remains is the genuinely
3-connected prism core or a nontrivial two-sum chain.  This is the precise unbounded gap; it is much
narrower than the original six-frame portal lock.
