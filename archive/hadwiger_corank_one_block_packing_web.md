# Co-rank-one Hall circuits: block packing and the two-active-label web

## 1. Scope and verdict

This note strengthens the split theorem in
`hadwiger_corank_one_portal_basis_descent.md`.  The old proof used one
far Hall bag for each retained deficient label.  That is unnecessarily
rigid: because the deficient bags are the bags of a clique model, several
of them may be joined into one far branch set.  The resulting **block
packing theorem** is uniform in the clique order.

For the co-rank-one `HC_7` cell it has two concrete consequences.

1. A two-piece split closes exactly when its five deficient labels can be
   packed into four two-sided blocks.  Thus every surviving connected
   split has at most two labels whose attachment sets cross the split,
   except for one oriented three-crossing state.
2. If the old contacted root and the two clean portal roots give three
   rooted pieces of the accessible bag, then merely having three label
   contacts at every piece already gives a `K_7` minor.  Omitted
   deficient bags repair the two exceptional incidence patterns.

Sweeping a 2-connected accessible bag by an `st`-ordering therefore gives
a genuine width-two label web: whenever at least one label is wholly in
the past and another is wholly in the future, at most two labels can be
active across the cut.  This eliminates, in one theorem, every
co-rank-one configuration having four crossing label classes at some
connected two-shore split.  It does not yet turn the width-two **label**
gate into a small ambient vertex adhesion; the deficient bags may have
arbitrarily many vertices.  That is the exact remaining dynamic step.

The final example shows that this residue is real statically, even when
the accessible bag is 2-connected.  Proper-minor transition states are
therefore still indispensable.

## 2. Setup

Use the co-rank-one setup with a labelled `K_r` model

\[
                 (B,B_1,\ldots,B_{r-1})
\]

in `G-v`.  The deficient-label set is

\[
                         I=[r-1],
\]

and it is a Hall circuit with exact interface `X`, where
`|X|=r-2`.  The old accessible bag `B` contains a root
`a\in N_G(v)`.  The clean portal-basis theorem supplies clean mutually
disjoint root paths to individual vertices of `B`, simultaneously
disjoint from the root-to-`X` linkage.

For a connected set `C\subseteq B`, define its label support

\[
                 \Lambda(C)=\{i\in I:E(C,B_i)\ne\varnothing\}.
                                                        \tag{2.1}
\]

All model bags below are the original labelled bags; in particular they
are pairwise adjacent.

## 3. The Hall block-packing theorem

### Theorem 3.1 (rooted block packing)

Let `2\le s\le r-1`.  Suppose there are pairwise disjoint, pairwise
adjacent connected sets

\[
                         C_1,\ldots,C_s\subseteq B       \tag{3.1}
\]

such that `C_1` contains the old root `a` and, for
`2\le t\le s`, the set `C_t` contains a distinct clean portal endpoint.
Absorb the corresponding clean portal paths into `C_2,\ldots,C_s`.

Suppose the deficient labels admit a partition into `r-s` nonempty
blocks

\[
                         I=J_1\dot\cup\cdots\dot\cup J_{r-s} \tag{3.2}
\]

such that

\[
                         J_u\cap\Lambda(C_t)\ne\varnothing
       \quad(1\le u\le r-s,\ 1\le t\le s).             \tag{3.3}
\]

Then `G` contains a `K_{r+1}` minor.

#### Proof

Choose one representative `j_u\in J_u` from every block and put
`J=\{j_1,\ldots,j_{r-s}\}`.  Since

\[
                         |J|=r-s\le r-2<|I|,
\]

the Hall-circuit property makes `J` linkable.  We need the slightly
stronger fact that this linkage may be joined to the already fixed clean
root-to-`X` paths.  Choose an index `i\in I-J`.  The exact Hall
certificate omitting `i` has one path through each vertex of `X` and
ends in all bags `B_j`, `j\ne i`.  Retain only the paths ending in the
representatives in `J`.  Factor each retained path at its unique vertex
of `X`, and concatenate its far suffix with the corresponding member of
the fixed root-to-`X` linkage.  This gives `r-s` disjoint rooted far
branch sets, one containing each `B_{j_u}`.  They are disjoint from the
clean portal paths.

For every `u`, enlarge the far branch containing `B_{j_u}` by all old
bags `B_i` with `i\in J_u-j_u`.  The enlarged set is connected because
the old deficient bags are pairwise adjacent.  Enlarged far sets for
different blocks are disjoint and pairwise adjacent.  Condition (3.3)
makes every `C_t` adjacent to every enlarged far set.  The sets `C_t`
are pairwise adjacent by assumption.

We have constructed `s+(r-s)=r` pairwise disjoint, pairwise adjacent
connected sets in `G-v`.  The first contains `a`, the next `s-1`
contain the roots of their clean portal paths, and the remaining `r-s`
contain the distinct roots of the retained `X` paths.  Hence every set
meets `N_G(v)`.  Adding the singleton `{v}` gives the required
`K_{r+1}` model.  \(\square\)

### Remark 3.2 (why arbitrary proper Hall subsets are legitimate)

The proof does not assume an unproved compatibility between two gammoid
bases.  It takes the exact `I-i` certificate, whose paths use the
vertices of `X` once each, and merely discards unwanted paths.  The fixed
root-side linkage already reaches every vertex of `X` and the selected
portal endpoints simultaneously.

### Theorem 3.3 (assisted block packing)

The conclusion of Theorem 3.1 remains valid under the following more
general allocation.  Partition `I` into `r-s` nonempty **far blocks**

\[
                         J_1,\ldots,J_{r-s}
\]

and pairwise disjoint **helper blocks** `H_t`, indexed by a set
`T\subseteq[s]`; helper blocks are nonempty and all these blocks together
partition `I`.  Assume

1. for every `t\in T`, some label in `H_t` belongs to
   `\Lambda(C_t)`; and
2. for every `t\notin T` and every far block `J_u`,
   `J_u\cap\Lambda(C_t)\ne\varnothing`.

Then `G` contains a `K_{r+1}` minor.

#### Proof

Choose and link one representative from each far block exactly as in
Theorem 3.1, and enlarge its far branch by the other bags in that far
block.  For `t\in T`, enlarge `C_t` by all bags with labels in `H_t`.
This is connected: one helper bag has an edge to `C_t`, and all helper
bags are pairwise adjacent.  It is adjacent to every far branch through
the old clique adjacencies among deficient bags.  If `t\notin T`,
condition 2 supplies a direct `C_t`-to-bag edge in every far block.
The accessible sets remain mutually adjacent through their original
edges, and all disjointness and root assertions are unchanged.  These are
again `r` rooted clique bags in `G-v`; add `{v}`. \(\square\)

This theorem is a uniform rooted-model allocation principle.  An omitted
deficient bag can be spent in either of two ways: it can enlarge a far
branch so that the branch sees more accessible pieces, or it can enlarge
one accessible piece and make that piece see every far branch.

## 4. Exact two-piece capacity for `HC_7`

Now put `r=6`, so `|I|=5`.  Let

\[
                         B=Y_p\dot\cup Y_q              \tag{4.1}
\]

be a connected adjacent split containing the two clean portal endpoints.
For every label `i`, record its nonempty support mask

\[
 \mu(i)=\{p:E(Y_p,B_i)\ne\varnothing\}
       \cup\{q:E(Y_q,B_i)\ne\varnothing\}.             \tag{4.2}
\]

Call a label **crossing** when `\mu(i)=\{p,q\}`.

### Corollary 4.1 (exact four-block criterion)

The split (4.1) gives a `K_7` minor whenever either

1. at least four labels are crossing; or
2. exactly three labels are crossing and the other two labels are owned
   by opposite sides.

Consequently, in a `K_7`-minor-free co-rank-one cell, every connected
two-portal split has at most two crossing labels, except possibly for an
oriented state in which exactly three labels cross and both remaining
labels are owned by the same side.

#### Proof

Theorem 3.1 with `s=2` asks for a partition of five labels into four
blocks, each meeting both sides.  Its block sizes are necessarily
`2,1,1,1`.  Hence the three singleton blocks must be crossing labels.
The remaining two labels form the double block and need only cover the
two sides collectively.

Four crossing labels permit three crossing singleton blocks and leave a
crossing label in the double block, which covers both sides with any
fifth label.  With exactly three crossing labels, they must be the three
singletons, and the remaining pair covers both sides exactly when its
members are owned by opposite sides.  Apply Theorem 3.1.  The converse
description is simply the negation of these two sufficient conditions.
\(\square\)

This contains Theorem 4.1 of `hadwiger_B_gated_capacity_state.md` as the
case of three crossing labels and one exclusive label on each side, but
also closes every split having four or five crossing labels.

## 5. A three-root upgrade

Assume that the old root `a` and two clean portal endpoints `p,q` are
distinct.

### Lemma 5.0 (rooted triangle in a 2-connected graph)

Every three distinct vertices `x,y,z` of a 2-connected graph lie in
three disjoint pairwise adjacent connected sets rooted respectively at
`x,y,z`.

#### Proof

Take a `y`--`z` path `P` in the graph with `x` deleted.  The fan lemma
gives two internally disjoint `x`--`P` paths with distinct ends `u,v` on
`P`, and with no other vertices on `P`.  Order them so that `u` precedes
`v` from `y` to `z`, and cut `P` at any edge between `u` and `v`.
The prefix and suffix of `P` are connected rooted sets containing `y`
and `z` and are adjacent through the cut edge.  The union of the two fan
paths after deleting their ends `u,v` is a connected set containing `x`;
it is disjoint from, and adjacent to, both path pieces. \(\square\)

Apply the lemma in `B`.  Thus it has disjoint
pairwise adjacent connected sets

\[
                         C_a,C_p,C_q                    \tag{5.1}
\]

containing `a,p,q`, respectively.  The sets need not cover `B`.

### Lemma 5.0 (rooted triangle in a 2-connected graph)

If `J` is 2-connected and `a,p,q` are distinct vertices, then `J`
contains three pairwise disjoint, pairwise adjacent connected sets rooted
at `a,p,q`, respectively.

#### Proof

Choose a cycle `C` through `p,q`.  If `a\in V(C)`, cut the cyclic order
at three edges, one between each consecutive pair of roots.  The three
root-containing arcs are the required sets.

Suppose `a\notin V(C)`.  By the fan lemma there are internally disjoint
paths from `a` to distinct vertices `u,w\in V(C)`, meeting `C` only at
their ends.  Delete `u,w` from the union of the two paths; the remaining
set is connected and contains `a`.  If `u,w,p,q` are distinct, one of
the two pairings of `{u,w}` with `{p,q}` is noncrossing on the cycle.
For that pairing, cut `C` at two edges to obtain disjoint connected arcs,
one containing `p` and its paired fan end, the other containing `q` and
the other fan end.  If a fan end is itself `p` or `q`, the same arcs are
obtained by cutting the two `p`--`q` arcs immediately on the appropriate
sides of the other fan end; this is the degenerate instance of the same
noncrossing pairing.  The two arcs are adjacent along the cut edges, and
the first set is adjacent to both arcs through the last edges of the fan.
These are the desired three branch sets. \(\square\)

### Lemma 5.1 (five labels into three common transversals)

Let five nonempty subsets of `{1,2,3}` be given.  They can be partitioned
into three nonempty blocks whose union in each block is `{1,2,3}` if and
only if

1. every coordinate belongs to at least three of the five subsets; and
2. at least one of the five subsets is `{1,2,3}`.

#### Proof

Necessity is immediate.  Each coordinate must occur in a different label
of every one of the three disjoint blocks.  Moreover five objects in
three nonempty blocks leave a singleton block, and its sole subset must
be `{1,2,3}`.

For sufficiency, choose a universal subset `U` and consider the remaining
four subsets.  Every coordinate occurs in at least two of them.  If they
can be paired so that both pairs cover `{1,2,3}`, use those pairs and
`{U}`.

Suppose no such pairing exists.  Call a pair bad if its union misses a
coordinate.  For each coordinate, at most two of the four subsets miss
it, so that coordinate certifies at most one bad pair.  Thus there are at
most three bad pairs.  Failure of all three perfect matchings of four
objects requires exactly three bad pairs, one in each perfect matching.
Those three edges form either a star or a triangle.  In the star case the
central subset misses the three distinct certifying coordinates and is
empty, impossible.  In the triangle case its three subsets are, after a
permutation of coordinates, contained respectively in `{1}`, `{2}` and
`{3}`; nonemptiness makes them exactly these singletons.  The fourth
subset must then be universal in order that every coordinate occur twice.
Use the two universal subsets as singleton blocks and the three singleton
subsets as the third block.  This proves sufficiency. \(\square\)

### Theorem 5.2 (distributed rooted triangle closes)

In the `HC_7` co-rank-one setup, suppose (5.1) can be chosen so that

\[
                 |\Lambda(C_t)|\ge3
                    \quad(t\in\{a,p,q\}),              \tag{5.2}
\]

and some deficient label `i` belongs to all three support sets.  Then
`G` contains a `K_7` minor.

#### Proof

Replace each deficient label by its support mask on the three sets in
(5.1).  Conditions (5.2) and the common label are precisely the two
conditions in Lemma 5.1.  Its three blocks satisfy (3.3).  Apply Theorem
3.1 with `s=3`. \(\square\)

The theorem closes an infinite family: the orders and internal geometry
of `B` and of all five deficient bags are unrestricted.  Only the
three-piece portal incidence is used.

### Theorem 5.3 (assisted rooted-triangle closure)

Suppose a rooted triangle (5.1) is chosen and every one of its three
pieces meets at least three deficient labels.  Then `G` contains a
`K_7` minor.

#### Proof

If one label meets all three pieces, apply Theorem 5.2.  Otherwise every
support mask has order at most two.  The sum of the three piece-degrees is
at least nine and at most ten.

If the sum is nine, exactly four masks have order two and one has order
one, while all three piece-degrees equal three.  Put the singleton at
piece 1.  If `x_{ij}` is the multiplicity of mask `ij`, the degree
equations give

\[
 x_{12}+x_{13}=2,\quad x_{12}+x_{23}=3,\quad
 x_{13}+x_{23}=3,
\]

whose solution is `(x_{12},x_{13},x_{23})=(1,1,2)`.  Thus the masks are

\[
 \{1,12,13,23,23\},                                    \tag{5.3}
\]

after relabelling the deficient bags.  Link the three labels with masks
`1,12,13` through three members of `X`, obtaining three rooted far
branch sets.  Absorb one omitted `23` bag into `C_2` and the other into
`C_3`.  These absorptions are connected.  Each enlarged accessible set
is adjacent to all three far sets because the old deficient bags are
pairwise adjacent, while `C_1` is adjacent to all three far sets by the
displayed masks.  The three accessible sets remain pairwise adjacent.
Together they and the three far sets give six rooted clique bags, hence a
`K_7` with `{v}`.

If the incidence sum is ten, all five masks have order two.  The degree
sequence is `(4,3,3)` up to permutation, and the analogous equations give

\[
 \{12,12,13,13,23\}.                                   \tag{5.4}
\]

Link three labels with masks `12,12,13` to the three far roots.  Absorb
the omitted `23` bag into `C_2` and the omitted second `13` bag into
`C_3`.  Again `C_1` sees all three far bags directly, while the two
helper-augmented pieces see all three through their helper bags.  The same
six rooted branch sets give `K_7`. \(\square\)

The proof uses omitted deficient bags as **accessible helpers**, in
addition to Theorem 3.1's merging of omitted bags into far branches.  It
closes both exact support patterns which ordinary three-block packing
cannot close.

### Corollary 5.4 (sparse-piece obstruction)

In a `K_7`-minor-free co-rank-one cell, every rooted `K_3` model in `B`
at the three distinct roots `a,p,q` has a branch set adjacent to at most
two of the five deficient bags.

This is a genuine rooted-model principle: the branch set may have
arbitrary order, and the other two branch sets and all deficient bags may
be arbitrarily complicated.

### Corollary 5.5 (a sparse root is forced)

If `a,p,q` are distinct and each of these three vertices is adjacent to
at least three deficient bags, then `G` contains a `K_7` minor.
Consequently a target-free co-rank-one cell satisfies

\[
 \min\bigl\{|\Lambda(\{a\})|,
             |\Lambda(\{p\})|,
             |\Lambda(\{q\})|\bigr\}\le2.             \tag{5.5}
\]

#### Proof

Take any rooted triangle at `a,p,q`, which exists because `B` is
2-connected.  Each rooted branch set contains its named vertex, so each
has support at least three.  Apply Theorem 5.3. \(\square\)

Thus high portal multiplicity now means multiplicity in **model labels**,
not merely many root-shore neighbours: two clean basis portals which each
see three deficient bags close the cell as soon as the protected root has
the same label capacity.

### Theorem 5.6 (one-helper sparse-piece closure)

Let `C_1,C_2,C_3` be a rooted triangle as in (5.1), and suppose
`h\in\Lambda(C_1)`.  Among the other four deficient labels, call a label
crossing when it belongs to both `\Lambda(C_2)` and `\Lambda(C_3)`.
Then `G` contains a `K_7` minor if either

1. at least three of those four labels are crossing; or
2. exactly two are crossing and the remaining two are owned by opposite
   pieces among `C_2,C_3`.

#### Proof

In Theorem 3.3 use `B_h` as a helper for `C_1`.  The other four labels
must be put into three far blocks which meet both `C_2` and `C_3`; their
block sizes are `2,1,1`.  Two crossing labels give the singleton blocks.
The double block covers both pieces if it contains a third crossing label,
or if its two exclusive labels are owned by opposite pieces.  Theorem 3.3
now gives the target. \(\square\)

Hence a supported sparse piece leaves a still narrower pole lock: after
spending any one of its supported labels as a helper, the other two rooted
pieces have at most one crossing label, or have exactly two crossing
labels with both remaining labels owned by the same piece.

## 6. The two-active-label web

Let `B` be 2-connected and fix distinct clean endpoints `p,q`.  Add the
edge `pq` if necessary and take an `st`-ordering

\[
                         z_1=p,z_2,\ldots,z_n=q          \tag{6.1}
\]

of `B+pq`.  Deleting the added edge does not affect the standard
conclusion: for every `1\le t<n`, both

\[
 P_t=B[\{z_1,\ldots,z_t\}],\qquad
 Q_t=B[\{z_{t+1},\ldots,z_n\}]                         \tag{6.2}
\]

are connected in `B`, and an edge joins them.  Equivalently one may use
the usual bipolar ordering theorem directly for prescribed poles.

For a label `i`, let

\[
 \ell_i=\min\{j:z_j\in A_i\},\qquad
 r_i=\max\{j:z_j\in A_i\},\qquad
 A_i=N_B(B_i).                                         \tag{6.3}
\]

At cut `t`, call `i` past if `r_i\le t`, future if
`\ell_i>t`, and active if `\ell_i\le t<r_i`.

### Theorem 6.1 (two-active-label web)

If the co-rank-one cell has no `K_7` minor, then for every `t`:

1. at most three deficient labels are active at cut `t`; and
2. if both a past and a future label exist, at most two deficient labels
   are active.

Equivalently, the sole possible three-active state is oriented: the two
inactive labels are both wholly in the past or both wholly in the future.

#### Proof

The connected split `P_t\dot\cup Q_t` is a two-portal split after
absorbing the clean `p`- and `q`-paths.  A label is crossing this split
exactly when it is active in (6.3).  Four active labels give outcome 1 of
Corollary 4.1.  Three active labels together with a past and a future
label give outcome 2.  Both would produce a `K_7` minor. \(\square\)

This is the promised capacity-state web.  It is not a bound on the order
of `B`; it controls every cut of every bipolar sweep.  In a mixed
past/future region, all five labelled attachment intervals communicate
through at most two active labels.

### Corollary 6.2 (exact structural residue)

If some bipolar cut has four active attachment classes, the model admits
a label-preserving block split and `G` has a `K_7` minor.  Otherwise every
unbounded 2-connected residue is a width-two interval web, apart from a
one-sided three-active prefix or suffix.

The phrase “width two” is label-theoretic.  It does **not** assert that
the actual ambient separator has two vertices: one deficient label may be
a large bag, and edges of `B` may cross the bipolar cut at many vertices.

## 7. Sparse-piece exchange and the connectivity count

Choose, among all rooted triangles at `a,p,q`, one which maximizes the
nondecreasing triple

\[
 (|\Lambda(C_{(1)})|,|\Lambda(C_{(2)})|,
   |\Lambda(C_{(3)})|)                                \tag{7.1}
\]

lexicographically.  Theorem 5.3 says its first coordinate is at most two
in a target-free graph.

### Lemma 7.1 (safe sparse-lobe exchange)

Let `C_1` be a sparse piece and let `D\subsetneq C_2` be nonempty.  If

1. `D` and `C_2-D` are connected;
2. the root of `C_2` lies in `C_2-D`;
3. `D` is adjacent to `C_1`;
4. `C_2-D` remains adjacent to `C_3`; and
5. `C_2-D` remains adjacent to every deficient bag in
   `\Lambda(C_2)`; and
6. `D` is adjacent to a deficient bag not in `\Lambda(C_1)`,

then replacing

\[
                  C_1\longmapsto C_1\cup D,qquad
                  C_2\longmapsto C_2-D                 \tag{7.2}
\]

gives another rooted triangle in which the support of `C_1` strictly
increases and neither other support decreases.  In particular, (7.2) is
impossible at a frame maximizing (7.1).

#### Proof

The new sets are connected by conditions 1 and 3.  Since `C_2` was
connected, an edge joins `D` to `C_2-D`, so the first two new pieces are
adjacent.  Condition 4 retains the second--third adjacency, while the old
`C_1`--`C_3` edge retains the first--third adjacency.  All three roots
remain in their named pieces by condition 2.  Condition 5 prevents a
support loss at the second piece, and condition 6 adds a new support label
to the first.  The third support is unchanged. \(\square\)

Thus a first-hit route from a sparse piece into another rooted piece has
only five genuine blockers: it contains the other root, is a cut-lobe,
owns the sole adjacency to the third piece, wholly owns a current support
label of its source piece, or carries no new deficient label.  This is the
rooted-triangle analogue of the safe-peel theorem.

The direct use of 7-connectivity is the following exact count.  It is
stated separately so that no label set is silently treated as a set of
vertices.

### Lemma 7.2 (sparse-shore fan count)

Let `C` be a nonempty connected vertex set in the 7-connected ambient
graph `G`, assume `|V(G)-C|\ge7`, let `L=\Lambda(C)` with
`|L|\le2`, and put

\[
 W=N_G(C)-\bigcup_{i\in L}V(B_i).                      \tag{7.3}
\]

Then

\[
             \sum_{i\in L}|N_G(C)\cap V(B_i)|
                         \ge 7-|W|.                    \tag{7.4}
\]

In particular, if `|W|\le2` and `|L|\le2`, some supported deficient bag
contains at least three distinct first-hit neighbour vertices of `C`.
If `L=\varnothing`, then necessarily `|W|\ge7`.

#### Proof

If `N_G(C)=V(G)-C`, its order is at least seven by hypothesis.  Otherwise
deleting `N_G(C)` separates `C` from the nonempty set
`V(G)-(C\cup N_G(C))`, so 7-connectivity again gives
`|N_G(C)|\ge7`.  The sets in (7.3)--(7.4) are disjoint and partition
`N_G(C)`, proving the inequality.  With at most two summands and right
side at least five, one summand is at least three. \(\square\)

Lemma 7.2 identifies the exact optimization required for the proposed
7-fan argument.  If unused `B`-components and root-side pieces can be
absorbed until the nonlabel gate `W` has order at most two, triple
first-hit capacity is forced in one of the at most two supported foreign
bags.  If this absorption fails, the failed lobe is one of the five named
blockers in Lemma 7.1 or contributes an actual third vertex to `W`.

Triple first-hit capacity alone is not yet a label-preserving split of
that foreign bag: its four adjacencies to the other deficient bags may all
be concentrated behind one internal cut.  The next operation-state lemma
must either distribute those label portals, or use the resulting internal
cut as a faithful adhesion.  This qualification is necessary and avoids
the false inference “three attachment vertices imply a splittable clique
bag.”

### Theorem 7.3 (exact two-paths exchange or a four-frame web)

Let `C_1,C_2,C_3` be a rooted triangle and let `r_2` be the root in
`C_2`.  Choose four distinct vertices of `C_2` as follows:

* `s` has a neighbour in `C_1`;
* `t` has a neighbour in a deficient bag whose label is not in
  `\Lambda(C_1)`;
* `u` has a neighbour in `C_3`; and
* `r_2` is the protected root of `C_2`.

Then at least one of the following holds.

1. There is a safe sparse-lobe exchange as in Lemma 7.1.
2. There is a connected bipartition `C_2=D\dot\cup E` with
   `s,t\in D`, `r_2,u\in E`, and some current support label of `C_2`
   is wholly owned by `D` relative to `C_2`.
3. The graph `C_2` embeds in a 4-web whose frame, in cyclic order, is
   `(s,r_2,t,u)`.

#### Proof

Apply the generalized Two Paths Theorem of Humeau--Pous (Theorem 1.5 in
arXiv:2505.16431) to the ordered tuple `(s,r_2,t,u)` in `C_2`.  If the
tuple is crossless, that theorem says that `C_2` is a subgraph of a web
with this frame, which is outcome 3.

Otherwise there are disjoint paths `P,Q` with `P` joining `s` to `t`
and `Q` joining `r_2` to `u`.  Any two disjoint connected subgraphs of a
connected graph extend to a connected bipartition: contract `P,Q`, take a
spanning tree of the contracted graph, delete an edge of the unique
`P`--`Q` tree path, and expand the two resulting tree components.  Thus
obtain `D,E` containing `P,Q`, respectively.

The set `D` is adjacent to `C_1` and to the new deficient label.  The set
`E` retains the root `r_2` and the adjacency to `C_3`.  If `E` also
retains every deficient label in `\Lambda(C_2)`, all hypotheses of Lemma
7.1 hold and outcome 1 follows.  Otherwise a label supported by `C_2`
has all its `C_2`-attachment vertices in `D`, which is outcome 2.
\(\square\)

This is the exact conversion of the sparse-piece problem to a web.  It
does not identify the label-width-two sweep of Theorem 6.1 with a
vertex-width-two decomposition.  The web conclusion arises only after a
specific four-terminal exchange fails.

### Lemma 7.4 (terminal-coincidence audit)

In the setup of Theorem 7.3, first replace a role vertex by another vertex
with the same role whenever this makes the four terminals more distinct.
If no such replacement is available, every remaining coincidence has one
of the following exact outcomes.

1. If `s=t` and this vertex is distinct from `r_2,u`, then either the
   singleton transfer `D={s}` is a safe exchange, or `s` is a cutvertex
   of `C_2`, owns the sole `C_2`--`C_3` adjacency, or wholly owns a
   current support label of `C_2`.
2. If `r_2=u` and `s,t` are otherwise distinct, then either there is a
   safe exchange, there is a current support-owner blocker, or `r_2`
   separates `s` from `t` in `C_2`.
3. If `s=r_2` or `t=r_2`, the protected root is respectively the sole
   available `C_1`-facing portal or the sole available portal of the new
   label.  This is a named root-protected blocker.
4. If `s=u` or `t=u`, that common vertex is the sole available
   `C_2`--`C_3` portal for the proposed transfer.  This is the named
   third-adjacency-owner blocker.

Coincidences involving three or four roles satisfy at least one of items
1--4.  Thus failure of four-terminal distinctness creates no untyped
case.

#### Proof

For item 1, use `D={s}` and `E=C_2-s`.  The two sets give Lemma 7.1
unless `E` is disconnected, misses the protected root (excluded by the
stated distinctness), misses every `C_3` portal, or misses a current
support label.  These are exactly the listed blockers.

For item 2, look for an `s`--`t` path in `C_2-r_2`.  If none exists,
`r_2` is the displayed separator.  If one exists, take it as `P` and
take the length-zero connected subgraph `{r_2}` as `Q`.  Extend `P,Q` to
a connected bipartition by the spanning-tree argument in Theorem 7.3.
The `Q`-side contains both the protected root and the `C_3` portal.  It
therefore gives Lemma 7.1 unless it loses a current support label, which
is the owner blocker.

For item 3, the preliminary replacement rule says there is no alternative
vertex for the coincident transferable role.  Any lobe realizing that
role contains `r_2`, so moving it loses the protected root.  For item 4,
there is no alternative `C_3` portal; moving a lobe containing the common
vertex loses the sole second--third adjacency.  Multiple coincidences
inherit one of these obstructions. \(\square\)

Nor may a facial triangle of this web immediately be called an ambient
three-vertex adhesion: its vertices can have edges from `C_2` to root
shores or deficient bags outside the web instance.  To use proper-minor
states on a facial clique, one must first prove that all such external
attachments are carried by the at most two active label classes, or add
their actual portal vertices to the adhesion.  This is the precise
interface between the Two Paths Theorem and the still-missing dynamic
state argument.

### Corollary 7.5 (seven-connectivity loads every filled web triangle)

In outcome 3, fix a facial rib triangle `T` of the web completion and let
`K_T` be its set of clique vertices.  Let `Z` be a nonempty component of
the original graph `C_2[K_T]`, and assume `|V(G)-Z|\ge7`.  Put

\[
                 R_Z=N_G(Z)-V(T).                       \tag{7.5}
\]

Then `|R_Z|\ge4`.  In particular, if every external neighbour of `Z`
outside the frame triangle lies in two deficient bags, one of those bags
contains at least two distinct neighbours of `Z`.

#### Proof

In the web completion, clique vertices belonging to `T` have no rib
neighbours outside `T`, and no neighbours in clique fillers of other
triangles.  Since `Z` is a component in the **original** subgraph on
`K_T`, its neighbours in `C_2-Z` which lie in the web instance are all in
`T`.  Hence

\[
                         N_G(Z)\subseteq T\cup R_Z.
\]

As in Lemma 7.2, 7-connectivity and the order hypothesis give
`|N_G(Z)|\ge7`.  Since `|T|=3`, (7.5) has order at least four.  The last
claim is pigeonhole. \(\square\)

Thus a crossless frame has only two possibilities: external attachment
loads every filled triangle, or an actual separator of order at most six
appears.  The former is the portal-distribution input required by an
operation-state exchange; it cannot be discarded as harmless web
decoration.

## 8. Sharp static counterarchitecture

Let `B` be any 2-connected graph with three distinct vertices `p,q,a`.
Take five deficient clique bags whose attachment sets in `B` are

\[
             A_1=A_2=\{p\},\qquad
             A_3=A_4=\{q\},\qquad
             A_5=\{a\}.                               \tag{7.1}
\]

For every connected `p`-`q` split, the `q`-side misses labels `1,2`
and the `p`-side misses labels `3,4`; label 5 is owned by one side as
well.  Thus every split has a two-owner lock on each side.  No conclusion
based only on 2-connectivity, the two clean portal vertices, and the five
attachment sets can remove it.  The triangle `B=pqa p` is the smallest
instance.

This construction is only a labelled branch-bag architecture; it is not
claimed to be 7-connected or minor-critical.  It falsifies the tempting
static assertion that a 2-connected accessible bag always has a
label-preserving two-foot split.  It also pinpoints what the full
proper-minor transition family must exclude: two duplicated owner classes
at each pole with one protected/mobile class between them.

## 9. Exact remaining dynamic step

Theorems 3.1 and 6.1 reduce the 2-connected co-rank-one obstruction to a
uniform object, not a list of graph orders:

* every bipolar sweep is a two-active-label web in its mixed region;
* every rooted triangle whose three pieces each see three labels closes;
  and
* duplicated owner classes of the form illustrated by (7.1), possibly
  with the fifth class mobile, remain a sharp static obstruction.

The missing theorem is now the following operation-sensitive statement.

> **Width-two transition exchange.**  In a proper-minor-minimal
> non-6-colourable graph, the two active deficient bags of a mixed bipolar
> cut either support a faithful label-block rotation, expose a smaller
> Hall circuit, or induce the same marked state as a faithful operation on
> the opposite shore.

The last outcome 6-colours `G` by crossed splicing.  The label web alone
cannot prove it, because (7.1) realizes the web statically.  Conversely,
any proof of this transition exchange may work with only two active labels
rather than five arbitrary portal classes.  This is the narrowest verified
form of the co-rank-one dynamic obstruction.
