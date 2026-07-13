# Block rigidity of a lex-minimal labelled carrier

## Status and purpose

This audited note records a uniform consequence of label-preserving transfer
minimality.  It is stronger than choosing one favourable low-leaf spanning
tree: it bounds the total number of non-cutvertices of the carrier and hence
its entire block structure.  The result is intended for the three common
rows of the exact `K_3\vee C_4` residue.  It does not by itself finish that
residue; the active application is to turn its path/three-arm blocks into
either literal diagonal packets or a three-vertex deletion to a
four-colourable clique tree.

## 1. Labelled transfer minimality

Let `R,F_1,...,F_d` be pairwise disjoint nonempty connected sets.  Assume
that every pair `R,F_i` is adjacent.  Other branch bags and other required
model edges may be present, but they are held fixed.

For `x\in R`, say that `x` **owns duty `i`** when every actual edge between
`R` and `F_i` has its `R`-end equal to `x`.  Thus an owned duty is nonempty
and is concentrated at the single literal vertex `x`.

Assume the following permitted-transfer minimality.

* If `R-x` is nonempty and connected and `x` owns no duty, removing `x`
  from the displayed carrier contradicts the choice of `R`.
* If `R-x` is nonempty and connected and `x` owns exactly one duty `i`,
  moving `x` from `R` into `F_i` contradicts the choice of `R`.

The comparison may be lexicographic: a move is permitted whenever it
decreases the number of missing labelled pairs, or preserves that number
and decreases `|R|`.  No spanning-model assumption is made in this local
comparison.

### Lemma 1 (non-cutvertex ownership)

Every vertex `x` for which `R-x` is nonempty and connected owns at least
two duties.  Owner sets of two distinct such vertices are disjoint.
Consequently

\[
  |\{x\in R:G[R]-x\text{ is nonempty and connected}\}|
       \le \left\lfloor\frac d2\right\rfloor .          \tag{1.1}
\]

#### Proof

If `x` owns no duty, remove it.  All required `R-F_i` edges survive and
`R-x` remains a nonempty connected bag, contrary to minimality.

Suppose `x` owns exactly duty `i`.  Since that duty is required, `x` has
an actual neighbour in `F_i`, so `F_i\cup\{x\}` is connected.  An edge
from `x` to `R-x` exists because `G[R]` is connected; after the move it
restores the required adjacency between the enlarged `F_i` and the
residual row.  Every other `R-F_j` edge survives because `x` did not own
duty `j`, and all labelled pairs not incident with `R` survive unchanged.
This is the second forbidden transfer.  Hence `x` owns at least two
duties.

If distinct vertices `x,y` both owned duty `i`, every nonempty `R-F_i`
edge would have its `R`-end simultaneously equal to `x` and to `y`, an
impossibility.  The owner sets are therefore disjoint, and (1.1) follows
by counting duties. \(\square\)

The vertices counted in (1.1) are exactly the usual non-cutvertices when
`|R|\ge2`.  Equivalently, each can be made a leaf of some spanning tree of
`G[R]`; the statement is independent of a preselected tree.

## 2. The six-duty block theorem

### Theorem 2 (path/three-arm block rigidity)

Under Lemma 1 with `d=6` and `|R|\ge2`, put `H=G[R]`.  Then:

1. `H` has at most three non-cutvertices;
2. every block of `H` is an edge or a triangle;
3. at most one block is a triangle; and
4. the block-cutvertex tree has at most three leaf blocks and maximum
   degree at most three.

Thus, after suppressing degree-two edge blocks, `H` is a path or a
three-arm tree, with at most one triangle replacing one node of that
skeleton.  In particular deletion of any cutvertex leaves at most three
components.

#### Proof

Item 1 is Lemma 1.  We use the standard block-cutvertex tree `T_H`.
Every component of `T_H-B` hanging from a cutvertex of a block `B`
contains a leaf block, and that leaf block contains a non-cutvertex of
`H`.  Components hanging from different cutvertices of `B` are disjoint.
Each vertex of `B` which is not a cutvertex of `H` is itself a
non-cutvertex.  We may therefore assign to every vertex of `B` a distinct
global non-cutvertex: assign the vertex itself when it is not a
cutvertex, and otherwise choose a non-cutvertex in a leaf block in its
component of `T_H-B`.  Hence

\[
                         |V(B)|\le3.                     \tag{2.1}
\]

Every block of a simple graph is consequently `K_2` or `K_3`, proving
item 2.

If two distinct triangle blocks existed, consider the unique path between
their block nodes in `T_H`.  At each end triangle, the two vertices not
used toward the other triangle either are global non-cutvertices or lead
into two disjoint off-path branches containing global non-cutvertices.
The two end triangles would therefore supply four distinct
non-cutvertices, contradicting item 1.  This proves item 3.

Every leaf block contains a non-cutvertex, and different leaf blocks
contain different ones, so there are at most three leaf blocks.  Removing
any node of a finite tree, each resulting component contains an original
leaf unless the removed node itself was a leaf.  Therefore a node of
`T_H` cannot have degree more than the total number of leaves, namely
three.  This proves item 4 and the stated skeleton description.  For a
cutvertex `p`, the components of `H-p` correspond to the components of
`T_H-p`, so there are at most three. \(\square\)

### Corollary 3 (the exact three-owner cell)

If `H` has three non-cutvertices `x_1,x_2,x_3`, then each owns exactly two
of the six duties, the three owner pairs partition all six duties, and
every actual `R-F_i` edge has its `R`-end at the unique owner of duty `i`.
In particular no cutvertex or internal corridor vertex of `R` has an
edge to any of the six labelled neighbour bags.

#### Proof

Lemma 1 gives three pairwise disjoint owner sets, each of order at least
two, inside a six-element duty set.  All three therefore have order two
and exhaust the duty set.  The last assertion is the definition of
ownership. \(\square\)

### Corollary 4 (the two-owner cell)

If `H` has exactly two non-cutvertices, at least four of the six duties
are concentrated at those two vertices.  All portals for the remaining
at most two duties are the only labelled contacts which may occur in the
interior of the block path.

This isolates the constructive application.  A six-duty nonsingleton row
is not an arbitrary portal graph: it is a path/three-arm carrier with at
most two distributed duty classes.  The next exchange must use those one
or two distributed classes to produce an actual clique adhesion or a
proper-minor equality state; otherwise the concentrated endpoint pairs
are available for the lobe-median rotation.

## 3. Seven-connectivity removes every long three-arm carrier

Call a connected component outside the displayed seven bags **unused**.
Assume that the comparison class is closed under absorbing an unused
component into any foreign bag which it meets.  Such an absorption keeps
the foreign bag connected, loses no labelled adjacency, and can only
improve the primary defect measure.

### Corollary 5 (the three-root cell is a literal triangle)

In the three-owner cell of Corollary 3, if the host graph is
seven-connected and the comparison class has the absorption closure just
stated, then

\[
                              G[R]\cong K_3.             \tag{3.1}
\]

#### Proof

Put `Z={x_1,x_2,x_3}`.  Let an unused component `C` meet a foreign bag
`F_i`, and absorb `C` into `F_i`.  If this improves the primary defect
measure, it contradicts its minimality.  Otherwise the new model is
equally optimal and Lemma 1 applies to it.

If `C` had a neighbour in `R-Z`, the unique root which formerly owned
duty `i` would cease to own it.  It would retain exactly its other paired
duty and could acquire no third owned duty, since the other five original
portal sets have not changed.  The same vertex remains a non-cutvertex of
`G[R]`, so in the equally optimal model it would own exactly one duty,
contrary to Lemma 1.  Hence every absorbed component has all its
`R`-neighbours in `Z`.

After absorbing every unused component which meets a foreign bag, every
component still unused meets model bags only in `R`.  Let `E` be `R`
together with all these remaining components.  Corollary 3 says that
every edge from `R-Z` to a foreign bag is absent, and the preceding
paragraph says that no absorbed component has an edge to `R-Z`.
Distinct unused components have no edges between them.  Consequently
every component of `G[E-Z]` has all its neighbours in the three-vertex
set `Z`, while the six nonempty foreign bags lie outside `E-Z`.
Seven-connectivity makes `E-Z` empty.  Thus `R=Z`.  A connected graph on
three vertices in which all three vertices are non-cutvertices is the
triangle. \(\square\)

### Corollary 6 (a long path has a literal mobile portal packet)

In the two-owner path cell, perform the same absorptions.  Let `a,b` be
the path endpoints, let `M` be the at most two duties not owned by an
endpoint, and put

\[
                    P=\bigcup_{i\in M}N_R(F_i).          \tag{3.2}
\]

Then either the entire remaining `R`-private envelope is contained in
`P\cup\{a,b\}`, or

\[
                         |P\cup\{a,b\}|\ge7.             \tag{3.3}
\]

In particular, if `|R|\ge7`, at least five internal vertices of the path
are literal portals for the at most two mobile duties, and one mobile
duty has at least three distinct internal portal vertices.

#### Proof

Let `E` be `R` together with every component still unused.  All row edges
to endpoint-owned duties end at `a` or `b`; every other row edge to a
foreign bag ends in `P`; and the remaining unused components meet no
foreign bag.  Hence a nonempty component of

\[
                         G[E-(P\cup\{a,b\})]
\]

has no neighbour outside `P\cup\{a,b\}`.  If that set had order at most
six, seven-connectivity would exclude the component.  This proves the
dichotomy.  Since `R\subseteq E`, `|R|\ge7` forces
`|P\cup\{a,b\}|\ge7`; five members are internal path vertices.  The
pigeonhole principle over `|M|\le2` gives a mobile duty with at least
three of them. \(\square\)

## 4. Trust boundary

The proof uses only literal model edges and legal vertex transfer.  It does
not infer that a quotient separator is an actual clique, that the carrier
is spanning, or that its two residual distributed duties have compatible
colour states.  Those are precisely the remaining application steps.
