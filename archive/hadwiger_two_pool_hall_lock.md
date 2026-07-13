# Two-pool completion and the exact Hall lock

## 1. Status

The rooted Hall condition in Theorem 5.1 of
`hadwiger_atomic_three_packet_core_completion.md` is much stronger than
necessary.  A full shore can pool all boundary owners into one branch
set.  Repeated owners are therefore harmless: the only static obstruction
is a protected frame bag with no portal in the second pool.

This note proves that statement for arbitrary target order, records the
exact alternating structure of an abstract Hall failure, and identifies
the geometry still needed after the Hall obstruction has collapsed.  No
colouring or minor-criticality hypothesis is used in the completion
theorem.

All pieces called bags below are pairwise vertex-disjoint.  A protected
`m`-frame is a family of `m` nonempty connected, pairwise adjacent sets.
For a set `U` disjoint from `S`, write

\[
                 P_S(U)=N_G(U)\cap S.                 \tag{1.1}
\]

A connected set `R` disjoint from `S` is **full to** `S` if every vertex
of `S` has a neighbour in `R`.

## 2. The uniform two-pool theorem

### Theorem 2.1 (two-pool frame completion)

Let `U_1,...,U_m` be a protected `m`-frame disjoint from `S\cup R`.  Let

\[
                         S=B\mathbin{\dot\cup}T       \tag{2.1}
\]

where `B,T` are nonempty, `G[B]` is connected, and `R` is connected and
full to `S`.  If

\[
          P_S(U_i)\cap B\ne\varnothing
          \quad\hbox{and}\quad
          P_S(U_i)\cap T\ne\varnothing
          \qquad(1\le i\le m),                       \tag{2.2}
\]

then `G` contains a `K_{m+2}` minor.

#### Proof

Use the following `m+2` bags:

\[
                 U_1,\ldots,U_m,\qquad B,\qquad R\cup T. \tag{2.3}
\]

The first `m` bags are connected and pairwise adjacent by the frame
hypothesis.  The bag `B` is connected.  The bag `R\cup T` is connected:
`R` is connected and every vertex of `T` has a neighbour in `R`.

Condition (2.2) makes every `U_i` adjacent to each of the last two bags.
Finally, fullness gives an edge from every vertex of the nonempty set `B`
to `R`, so the last two bags are adjacent.  The bags in (2.3) are
pairwise disjoint, and hence form a `K_{m+2}` model.  \(\square\)

The proof does not choose distinct representatives in `T`.  All labels
in `T` are donated to the one full-shore bag, so an arbitrary number of
frame pieces may use the same owner.

### Corollary 2.2 (one-root pooling)

Let `|S|\ge2`, let `s\in S`, let `R` be connected and full to `S`, and
let `U_1,...,U_m` be a protected frame outside `S\cup R`.  Suppose every
`U_i` has an `s`-portal.  Then either

1. `G` contains a `K_{m+2}` minor; or
2. some frame bag has the exact portal lock
   \[
                         P_S(U_i)=\{s\}.              \tag{2.4}
   \]

#### Proof

Apply Theorem 2.1 with `B={s}` and `T=S-{s}`.  Every frame bag sees `B`.
If (2.4) fails, every frame bag also sees `T`, and outcome 1 follows.
\(\square\)

For `m=t-2`, outcome 1 is a `K_t` minor.  This strictly strengthens the
rooted Hall completion theorem: a system of distinct representatives is
unnecessary, and every nontrivial Hall circuit is absorbed at once.

### Corollary 2.3 (apex/contact form)

Let `v` be a vertex, put `S=N_G(v)`, and let
`U_1,...,U_{t-2}` be a protected `(t-2)`-frame in `G-v`, disjoint from
`S`.  If there is a nonempty proper set `B\subset S` such that `G[B]` is
connected and every frame bag has both a `B`-portal and an
`S-B`-portal, then `G` has a `K_t` minor.

Indeed, apply Theorem 2.1 with `R={v}`.  The literal model is

\[
             U_1,\ldots,U_{t-2},\qquad B,
             \qquad \{v\}\cup(S-B).                  \tag{2.5}
\]

Consequently, failure has the exact certificate

\[
 \boxed{\text{for every nonempty proper connected }B\subset S,
 \text{ some }U_i\text{ is dark to }B\text{ or to }S-B.} \tag{2.6}
\]

In particular, if all frame bags contact a common root `s`, then a
`K_t`-minor-free graph has a bag satisfying (2.4).

The conclusion (2.6) is a label-free contact obstruction.  It is not a
matching obstruction: it says that every connected boundary bipartition
is witnessed by a monochromatic-side frame bag.

### Proposition 2.4 (the singleton lock is statically sharp)

For every `m\ge2` there is a graph satisfying all hypotheses of
Corollary 2.2, having exactly one locked row, and containing no
`K_{m+2}` minor.

#### Construction and proof

Let `U={u_0,...,u_{m-1}}` induce `K_m`, put `S={s,q}`, and let
`R={h}`.  Add the edges

\[
 su_i\ (0\le i<m),\qquad qu_i\ (1\le i<m),
 \qquad hs,hq,                                    \tag{2.7}
\]

and no others outside `K_m`.  The singleton `U_i={u_i}` form the
protected frame, `R` is full to `S`, every frame bag sees `s`, and
`P_S(U_0)={s}`.

The three bags

\[
 U\cup\{s\},\qquad (U-\{u_0\})\cup\{s,q\},
 \qquad\{s,q,h\}                                  \tag{2.8}
\]

in the displayed path order form a tree decomposition.  Every bag has
order at most `m+1`, so the graph has treewidth at most `m`.  Since
treewidth is minor-monotone and `K_{m+2}` has treewidth `m+1`, the graph
has no `K_{m+2}` minor.  Thus no static strengthening can delete outcome
(2.4) without adding connectivity, minimality, or operation-state data.

### Theorem 2.5 (owned-root two-pool completion)

The frame need not be wholly outside the boundary.  Let
`U_1,...,U_m` be a protected frame disjoint from a connected full shore
`R`, and put

\[
                     W=S\cap\bigcup_{i=1}^mU_i.       \tag{2.9}
\]

Choose a nonempty connected set `B\subseteq S-W` and put
`T=S-(B\cup W)`.  Suppose every `U_i` is adjacent to `B`, and, for every
`i`, either

\[
                   U_i\cap S\ne\varnothing
          \quad\hbox{or}\quad P_S(U_i)\cap T\ne\varnothing.       \tag{2.10}
\]

Then `G` has a `K_{m+2}` minor.

#### Proof

Use again

\[
                       U_1,\ldots,U_m,\quad B,\quad R\cup T.    \tag{2.11}
\]

These bags are disjoint because all boundary vertices already owned by
the frame were removed into `W`, rather than being put in either pool.
The last bag is connected by fullness.  Every frame bag sees `B` by
hypothesis.  A frame bag meeting `S` sees `R` through any one of its owned
boundary vertices; a frame bag missing `S` sees `T` by (2.10).  Thus every
frame bag sees `R\cup T`.  Finally `B` sees `R`, and (2.11) is the desired
clique model.  \(\square\)

### Corollary 2.6 (four rooted bags plus one free bag, `HC_7` form)

Let `S=N(v)`.  Suppose a protected five-frame in `G-v` consists of four bags which
each contain a vertex of `S` and a fifth bag `U_0` disjoint from `S`.
If there is an unowned vertex `s\in S` adjacent to all five bags and
`U_0` has a portal in

\[
                 S-\left(\{s\}\cup\bigcup_{i=1}^5U_i\right),      \tag{2.12}
\]

then `G` contains a `K_7` minor.

Apply Theorem 2.5 with `R={v}` and `B={s}`.  This is the overlap-safe
form for composing a rooted `K_4` model with a fifth protected bag.  If
the fifth bag has no portal in (2.12), it is the exact unowned singleton
lock; no boundary root is counted in two branch sets.

## 3. Exact anatomy of the obsolete Hall obstruction

The following facts remain useful when a later argument protects some
boundary labels from being pooled.

Let `\mathcal P` be a bipartite graph with left side `I`, right side `T`,
and `|I|=|T|=n`.  Think of `iT` as the portal row of `U_i`.

### Lemma 3.1 (minimal critical owner block)

Suppose `X\subseteq I` is inclusion-minimal subject to

\[
                         |N(X)|<|X|.                  \tag{3.1}
\]

Put `Y=N(X)`.  Then:

1. `|Y|=|X|-1`;
2. for every `x\in X`, the graph `\mathcal P[X-{x},Y]` has a perfect
   matching;
3. `\mathcal P[X,Y]` is connected; and
4. fix `x_0\in X` and a matching `M` from `X-{x_0}` onto `Y`.  Every
   vertex of `X\cup Y` is reachable from `x_0` by an `M`-alternating
   path.  Flipping such a path ending at `x\in X` produces a matching
   from `X-{x}` onto `Y`.

#### Proof

Every proper subset `Z` of `X` satisfies `|N(Z)|\ge|Z|`.  Taking
`Z=X-{x}` gives

\[
                   |Y|\ge |N(X-{x})|\ge|X|-1,
\]

while (3.1) gives the reverse inequality.  This proves item 1.  Hall's
condition on every subset of `X-{x}` proves item 2.

If `\mathcal P[X,Y]` had at least two components, the left side of each
component would be a proper subset of `X` and would have at least as many
neighbours as vertices.  Summing over the components would give
`|Y|\ge|X|`, contrary to item 1.  This proves item 3.

For item 4, start the usual alternating search at the unmatched vertex
`x_0`: traverse nonmatching edges from left to right and matching edges
from right to left.  Let `A` and `C` be the reached left and right sets.
Every neighbour of `A` is in `C`, every vertex of `C` is matched to a
reached vertex of `A-{x_0}`, and hence

\[
                         N(A)=C,qquad |C|=|A|-1.      \tag{3.2}
\]

If `A` were proper in `X`, it would contradict the minimality of `X`.
Thus `A=X` and then `C=Y`.  Flipping an alternating path from `x_0` to
`x` exchanges the unique unmatched left vertex from `x_0` to `x`.
\(\square\)

Thus a critical owner block is a connected near-perfect alternating
circuit, not an arbitrary Hall-deficient family.  A new portal edge
`xq`, with `x\in X` and `q\notin Y`, matches all of `X`: leave `x`
unmatched in item 2 and use `xq`.  If `q` is exposed by a maximum matching
on the complementary rows, this edge increases the global portal-matching
number.  This is the exact label-preserving rerouting target.

### Theorem 3.2 (ordered atomic Hall decomposition)

If `\mathcal P` has no perfect matching, there are disjoint nonempty left
blocks `X_1,...,X_d`, pairwise disjoint (possibly empty) right blocks
`Y_1,...,Y_d`, and remainders
`I_*`, `T_*` such that

\[
 I=X_1\dot\cup\cdots\dot\cup X_d\dot\cup I_*,\qquad
 T=Y_1\dot\cup\cdots\dot\cup Y_d\dot\cup T_*,        \tag{3.3}
\]

and:

1. `|X_j|=|Y_j|+1`;
2. after deleting the earlier blocks, `X_j` is a minimal critical owner
   block with neighbourhood exactly `Y_j`;
3. in the original graph,
   \[
              N(X_j)\subseteq Y_1\cup\cdots\cup Y_j; \tag{3.4}
   \]
4. `\mathcal P[I_*,T_*]` has a matching saturating `I_*`;
5. the maximum matching number of `\mathcal P` is `n-d`, and there is a
   maximum matching which leaves one arbitrarily prescribed member of
   each `X_j` unmatched and leaves exactly `d` labels of `T_*` unmatched.

#### Proof

In the current residual bipartite graph, choose an inclusion-minimal
deficient left set, call it `X_j`, put `Y_j=N(X_j)`, and delete both.
Repeat until the remaining left side is matchable.  Lemma 3.1 proves
items 1 and 2.  At the moment `X_j` is chosen it has no neighbour among
the labels which remain later; this is (3.4).  The stopping condition is
item 4.

For every prefix `A_j=X_1\cup\cdots\cup X_j`, (3.4) gives

\[
 |N(A_j)|\le\sum_{h\le j}|Y_h|
             =\sum_{h\le j}|X_h|-j=|A_j|-j.          \tag{3.5}
\]

In particular every matching misses at least `d` left vertices.  On the
other hand, use Lemma 3.1 to match `X_j-{x_j}` onto `Y_j`, independently
for every `j`, and use the saturating matching on the remainder.  This
matches `n-d` left vertices.  Since initially the two sides have the same
order, after deleting the `d` co-rank-one blocks the remainder has
`|T_*|=|I_*|+d`; its saturating matching exposes exactly `d` right
labels.  Item 5 follows.  \(\square\)

### Corollary 3.3 (Hall circuits collapse to zero rows)

In the graph-theoretic setup of Corollary 2.2, if the portal incidence
into `S-{s}` has no matching saturating all frame rows but has no zero
row, the graph already contains a `K_{m+2}` minor.  Hence, in the presence of a full shore, the
only Hall obstruction needed to certify static failure is the singleton
block

\[
                         X=\{i\},\qquad Y=\varnothing,\qquad
                         P_S(U_i)=\{s\}.              \tag{3.6}
\]

If no such singleton block occurs, all critical blocks of order at least
two are eliminated simultaneously by owner pooling, irrespective of their
alternating geometry.  When a zero row does occur, other abstract Hall
blocks may coexist, but they add no further static obstruction.

## 4. Rerouting versus the atomic singleton lock

Assume the hypotheses of Corollary 2.2 and suppose `U_0` is the locked
bag in (2.4).  Let

\[
 F=G-\bigl(S\cup R\cup\!\bigcup_{i\ne0}U_i\bigr).   \tag{4.1}
\]

and permit paths whose first vertex lies in `U_0`.  If there is a path
`P` contained in `F` from `U_0` to a vertex having a neighbour in
`S-{s}`, then absorb `P` into `U_0`.  The enlarged bag remains connected,
disjoint from the other bags, adjacent to every other frame bag through the old frame edges, and
still has an `s`-portal.  It now has a second-pool portal, so Corollary 2.2
gives a `K_{m+2}` minor.

Thus failure of every label-preserving rerouting has the exact relative
form

\[
 \boxed{\text{the free-space component containing }U_0
 \text{ has no }(S-{s})\text{-portal}.}              \tag{4.2}
\]

Its frontier is contained in `S\cup R` and the other protected bags.
This is a model-relative adhesion, not automatically a small vertex
separator: an entire protected bag may contain arbitrarily many frontier
vertices.  Any claim that (4.2) itself is a colour-gluable adhesion would
silently replace connected branch sets by single vertices and would be
false.  One still needs either

* a bounded transversal of the frontier whose two side-colouring state
  families intersect; or
* shore-free protected cores which permit the clean donor/owner exchange
  of `hadwiger_full_adhesion_owner_exchange.md`.

This is the exact geometry not supplied by Hall theory.

### Lemma 4.1 (the exact colour-gluing exit)

Let `G` be non-`r`-colourable while every proper subgraph is
`r`-colourable.  Let `(A,B)` be a separation with both `G[A]` and `G[B]`
proper, and put `X=A\cap B`.  For `Z\in\{A,B\}`, let
`\mathcal E_Z` be the labelled equality partitions of `X` induced by
proper `r`-colourings of `G[Z]`.  Then

\[
                         \mathcal E_A\cap\mathcal E_B=\varnothing. \tag{4.3}
\]

In particular, `X` cannot be a clique of order at most `r`.

#### Proof

If colourings on the two sides induce the same labelled equality
partition, a permutation of the palette makes them agree pointwise on
`X`; they then glue because there is no edge between `A-B` and `B-A`.
This would `r`-colour `G`.  If `X` is a clique of order at most `r`, every
proper colouring induces the all-singleton partition, so the two nonempty
state families intersect.  \(\square\)

### Theorem 4.2 (uniform Hall-lock dichotomy)

Put `m=t-2` in Corollary 2.2 and suppose in addition that `G` is
minor-minimal non-`(t-1)`-colourable.  Then at least one of the following
objects is present.

1. A `K_t` model supplied by Theorem 2.1.
2. A label-preserving free-space path which enlarges a singleton-locked
   frame bag and hence supplies the model in item 1.
3. A separation at the frontier of the free-space component whose two
   proper sides accept a common labelled `(t-1)`-colour state (and hence
   colour-glue, contradicting the counterexample hypothesis, by Lemma
   4.1).
4. An **atomic Hall lock**: a frame bag `U_0` satisfies
   `P_S(U_0)={s}`; its free-space component has no second-pool portal; and
   the labelled extension-state families on every proper frontier
   separation are disjoint.  In particular, no such frontier is a clique
   of order at most `t-1`.

#### Proof

If every row has a second-pool portal, Corollary 2.2 gives item 1.
Otherwise choose `U_0` with exact row `{s}`.  A free-space path as in the
paragraph preceding (4.2) gives item 2 and then item 1.  If there is no
such path, (4.2) holds.  For each actual vertex separation obtained from
its frontier, Lemma 4.1 gives item 3 when the state families meet; if none
meet, the data are exactly item 4.  \(\square\)

Outcome 4 is sharply specified but not yet eliminated.  Its last clause
is operation-sensitive: unlike a quotient contraction, it retains the
full labelled colouring states of every frontier vertex.
Item 3 is a contradiction exit in the proof search, not a configuration
which can persist in the assumed minor-minimal counterexample.

## 5. Minimum-fragment collision and the two-shore lock

The singleton lock becomes highly nonlocal inside a minimum fragment.

### Proposition 5.1 (minimum-fragment contact collision)

Let `G` be `k`-connected, let `S` be a `k`-cut, and let `D` be a
globally minimum fragment behind `S`.  Suppose

\[
                    D=U_0\dot\cup U_1\dot\cup\cdots\dot\cup U_{m-1}, \tag{5.1}
\]

where `m\ge2` and the `m` sets form a protected frame, and suppose

\[
                         P_S(U_0)=\{s\}.              \tag{5.2}
\]

Then at least `k` distinct vertices of `D-U_0` have a neighbour in
`U_0`.  Consequently some `U_j`, `1\le j<m`, contains at least

\[
                         \left\lceil\frac{k}{m-1}\right\rceil       \tag{5.3}
\]

such vertices.  In particular, for `k=7,m=5`, one owner contains at
least two.

#### Proof

The set `D-U_0` is connected: it is the union of `m-1` pairwise adjacent
connected frame bags.  It is adjacent to `U_0`.  Apply the atomic-surplus
Theorem 2.1 of `hadwiger_exact_cut_atomic_kernel.md` to the connected
split `D=U_0\dot\cup(D-U_0)`.  It gives

\[
 |N_S(U_0)|+|N_{D-U_0}(U_0)|\ge k+1.
\]

Equation (5.2) makes the first term one, so the second is at least `k`.
The other `m-1` bags cover these distinct vertices, and the pigeonhole
principle gives (5.3).  \(\square\)

### Corollary 5.2 (conditional lift to the audited two-shore lock)

Retain the `k=7,m=5` case of Proposition 5.1, and let `p,q` be two distinct `U_0`-neighbours
in the same owner `U_j`.  Suppose, in addition, that these two vertices
are terminals of the repeated trace of a labelled clique model across two
full shores `A,B`, and that every retained label has a connected
shore-free protected core meeting the adhesion, exactly as in Corollary
3.3 of `hadwiger_full_adhesion_owner_exchange.md`.  Then either

1. `G` contains a `K_7` minor; or
2. every connected `p`-`q` trace in that repeated owner uses `A\cup B`.

#### Proof

Under the stated core hypotheses, any connected `p`-`q` trace avoiding
`A\cup B` is the transverse connector in Theorem 4.1 of
`hadwiger_full_adhesion_owner_exchange.md`, and gives a `K_7` minor.
The displayed alternative is its literal negation.  \(\square\)

The extra alignment in Corollary 5.2 is essential.  If either the
repeated-trace alignment or one of the asserted protected cores does not
exist, Corollary 5.2 is simply inapplicable; this is not a third outcome
under its hypotheses.  Proposition 5.1 only
places `p,q` in the same frame bag; it does not make them adhesion
terminals and does not manufacture shore-free protected cores.  Therefore
the rigorously remaining uniform problem is now narrow:

\[
 \boxed{\text{promote the seven-contact collision to a transverse trace,
 or expose a bounded state-compatible frontier.}}     \tag{5.4}
\]

## 6. Adversarial scope audit

1. **Boundary labels are used once.**  In Theorem 2.1 all of `T` belongs
   to the single bag `R\cup T`; none is also adjoined to a frame bag.
2. **No boundary adjacency is assumed inside `T`.**  Fullness of `R`
   connects every vertex of `T` to the same connected shore.
3. **The pools are adjacent.**  Because `B` is nonempty and `R` is full,
   there is an edge from `B` to `R`.
4. **The frame must avoid both pools.**  If a purported protected bag
   already contains a boundary label or invades `R`, (2.3) may overlap;
   the theorem explicitly excludes this.
5. **A zero row is genuinely static.**  Neither connectivity nor Hall's
   theorem alone gives an `(S-{s})`-portal to `U_0`.  Connectivity may
   route paths through other protected bags, which is precisely the
   frontier in (4.2).
6. **Connected branch sets are not colour-gluable vertices.**  Contracting
   a protected bag can create a proper-minor colouring which does not
   expand to a colouring of the original bag.  A genuine gluing outcome
   needs a vertex adhesion or a fully recorded labelled boundary state.
7. **The minimum-fragment collision is conditional on coverage.**  The
   equality `D=U_0\dot\cup\cdots\dot\cup U_4` is what makes `D-U_0`
   connected and lets atomic surplus apply.  A frame merely contained in
   `D` does not suffice.

Theorem 2.1 and Corollaries 2.2--2.3 are the reusable result.  They replace
the Hall-matching target by a strictly sharper singleton-portal target;
Sections 4--5 identify, without suppressing any quantifier, the geometry
which a proper-minor state exchange must still eliminate.
