# Exact reversibility and capacity of a single-gate deficiency rotation

## Status

This identifies one exact composition object after the rooted exchange
theorems.  A **single connected-gate** deficiency rotation is not a
descent: it is an exact involution.  Consequently no model potential can
be strictly decreasing on every such legal rotation.  Its residue is a single
connector carrying the old and new missing-row demands.  Splitting that
connector into two demand carriers gives `K_7` immediately.

The concentrated `4+1+1+1` exchange moves two disjoint pieces from one
donor into the old centre.  Their union need not be connected inside the
donor, so that two-piece rotation is not covered by the involution theorem
and may still admit a directed capacity potential.

This separates the two global cases cleanly.

* If the host has no `K_7^-` minor, every nonterminal **single-gate**
  rotation edge is a two-pair versus two-pair capacity
  obstruction--precisely the proposed web-exchange cell.
* If a `K_7^-` minor exists, one-pair edges remain rooted Two-Paths
  problems of lower demand.  Their unrooted capacity shadows have simple
  cutvertex descriptions, but alternating attachment order is an
  additional genuine obstruction.

The remaining theorem must compose those pinches/webs into a common
two-apex society or match proper-minor states.  Re-optimizing bag sizes
alone cannot do so.

## 1. Rotation datum

Let `F_1,...,F_5` be pairwise disjoint connected pairwise adjacent
sets.  Let `X,U` be disjoint connected sets, disjoint from the `F_i`,
such that

\[
             XU\ne\varnothing,
             \qquad E(X,F_i)\ne\varnothing\quad(i\notin D),
             \qquad E(X,F_i)=\varnothing\quad(i\in D),    \tag{1.1}
\]

where `D` is a nonempty set of at most two labels.  Assume

\[
                         E(U,F_i)\ne\varnothing
                         \qquad(i\in[5]),                \tag{1.1a}
\]

so that `U,F_1,...,F_5` are the old foreign `K_6` model, and assume

\[
             U=Z\mathbin{\dot\cup}W                       \tag{1.2}
\]

with `Z,W` nonempty and connected, `E(Z,W) nonempty`, and:

1. `Z` meets `X` and every `F_i` with `i in D`;
2. `W` meets `X`; and
3. for a nonempty set `E` of at most two labels,

   \[
       E(W,F_i)=\varnothing\ (i\in E),\qquad
       E(W,F_i)\ne\varnothing\ (i\notin E).              \tag{1.3}
   \]

The old seven bags are

\[
                         X,U,F_1,\ldots,F_5,              \tag{1.4}
\]

with missing centre spokes `D`.  Put

\[
                         X'=X\cup Z.                      \tag{1.5}
\]

The rotated seven bags are

\[
                         W,X',F_1,\ldots,F_5,             \tag{1.6}
\]

with missing centre spokes `E`.  This is the literal form of every
non-target **single-gate** rotation produced by the row-core theorem.  In
that application, `E=Omega_U(Z)`.  It does not encode the two-piece
concentrated rotation.

For `i in[5]`, write

\[
                         P_i=N_Z(F_i).                    \tag{1.7}
\]

Every `P_i` with `i in D union E` is nonempty: old missing rows are met
by `Z` in order to repair `X'`, and new missing rows are monopolized by
`Z` in the old donor.

## Theorem 1 (a rotation is an exact involution)

The passage (1.4) to (1.6) has a label-preserving inverse using the same
piece `Z`.  More exactly, regard `X'=X union Z` as the donor in the
rotated model and split it as `Z dotcup X`.  Then:

* `Z` meets every new missing row in `E`;
* `X` is connected and retains exactly the rows outside `D`; and
* the monopoly set of `Z` in the donor `X'`, relative to the five fixed
  rows, is exactly `D`.

Moving `Z` into the current centre `W` restores the old donor
`W union Z=U`, makes `X` the centre, and restores precisely the old
missing set `D`.

### Proof

For `i in D`, the old centre `X` is anticomplete to `F_i`, while `X'`
meets `F_i` through `Z`; hence every `X'F_i` portal lies in `Z`.  Thus
`D` is contained in the inverse monopoly set.

For `i notin D`, (1.1) supplies an old `XF_i` edge.  Its endpoint in
`X` survives after `Z` is removed, so `i` is not monopolized by `Z`.
The inverse monopoly set is therefore exactly `D`.  The nonempty sets
`P_i`, `i in E`, show that `Z` meets every current missing row.  Finally
`X,Z,W` are connected in the required pairs: `XZ` and `ZW` are literal
edges.  The inverse gate-to-centre operation gives

\[
             X' - Z=X,\qquad W\cup Z=U,
\]

and the preceding monopoly calculation gives missing set `D`.  Every
other fixed-row edge is unchanged. \(\square\)

### Corollary 1.1 (no universally monotone model potential)

On any class of near-`K_7` models closed under the gate rotations above,
there is no function of the current labelled model which strictly
decreases under every nontrivial legal rotation.

### Proof

Every rotation is nontrivial because `Z` is nonempty, and Theorem 1 says
that its inverse is another legal rotation.  Strict decrease in both
directions is impossible. \(\square\)

Thus a valid termination proof must orient rotations by extra global
data and prove that terminal equal-potential cycles are coherent.  Bag
size, centre size, or a lexicographic combination cannot be asserted to
decrease merely because the new centre is a proper part of the old
donor.

## 2. The exact connector split

Fix attachment vertices

\[
                  alpha in N_Z(X),\qquad beta in N_Z(W). \tag{2.0}
\]

For a nonempty label set `Q subseteq[5]`, call a connected subgraph of
`G[Z]` a **`Q`-carrier** if it meets every `P_i`, `i in Q`.  It is
`X`-rooted if it contains `alpha`, and `W`-rooted if it contains `beta`.

### Theorem 2 (two-carrier completion)

If `G[Z]` contains a vertex-disjoint `X`-rooted `D`-carrier and
`W`-rooted `E`-carrier, then `G` contains a `K_7` minor.

### Proof

Let `L,R` be disjoint rooted carriers of the two respective types.  If they are
not adjacent, take a shortest `L-R` path in connected `G[Z]` and add its
internal vertices to `L`.  The two sets remain disjoint and connected
and become adjacent.

Contract `L,R`, extend an edge between their images to a spanning tree
of `G[Z]`, and delete that tree edge.  Lifting its two components gives
a partition

\[
                         Z=Z_X\mathbin{\dot\cup}Z_W       \tag{2.1}
\]

into nonempty connected adjacent sets with `L subseteq Z_X` and
`R subseteq Z_W`.

Now use the seven branch sets

\[
             X\cup Z_X,\quad W\cup Z_W,\quad
             F_1,\ldots,F_5.                              \tag{2.2}
\]

The first is connected through the old `X-alpha` edge because
`alpha in L subseteq Z_X`; symmetrically the second is connected through
the `W-beta` edge.

The first enlarged centre meets every row outside `D` through `X` and
every row in `D` through the `D`-carrier.  The second enlarged centre
meets every row outside `E` through `W` and every row in `E` through the
`E`-carrier.  They are adjacent through (2.1), and the five fixed rows
are a clique model.  Thus (2.2) is a `K_7` model. \(\square\)

The roots are essential.  Without them, mere disjoint demand carriers
need not lie on the correct sides of a connected bipartition.

## 3. Exact one-hole consequences and the rooting warning

### Theorem 3 (one versus one is a rooted Two-Paths instance)

Suppose `D={d}` and `E={e}`.  If there are distinct vertices

\[
                    x in P_d,\qquad y in P_e,             \tag{3.1}
\]

which can be joined respectively to the fixed `X`- and `W`-attachment
sides by vertex-disjoint connected subgraphs of `Z`, then `G` has a
`K_7` minor.

For singleton portal sets `P_d={x}`, `P_e={y}`, the surviving obstruction
is exactly the absence of disjoint paths joining the terminal pairs
`(alpha,x)` and `(beta,y)` (with a zero-length path allowed when a root
is already its required portal).  Even a 2-connected connector can have
this obstruction: a cycle with the four terminals in alternating order
is the basic example.  Thus no unique-common-portal or cutvertex
conclusion is valid without a rooted Two Paths/web theorem.

### Proof

The first assertion is Theorem 2 with singleton-demand carriers.  When
the portal sets are singletons, deleting inessential branches from the
two rooted carriers leaves the stated two disjoint paths, and conversely
those paths are the two rooted carriers required by Theorem 2.  The
alternating cycle verifies that 2-connectivity alone does not remove the
rooting obstruction. \(\square\)

### Theorem 4 (unrooted one-versus-two capacity shadow)

Suppose `D={d}` and `E={e,f}`.  Ignore the two fixed attachment roots for
the moment.  There are disjoint unrooted `D`- and `E`-carriers if and
only if some `x in P_d` has the property that one component of `Z-x`
meets both `P_e` and `P_f` (where a portal occurrence at `x` itself is
deleted).

Consequently, if even this unrooted split fails, every `x in P_d` separates the
two new portal classes in the exact sense that no component of `Z-x`
meets both.  If `Z` is 2-connected, this forces every `x in P_d` to be
the unique vertex of `P_e` or the unique vertex of `P_f`; in particular

\[
                              |P_d|\le2.                  \tag{3.3}
\]

### Proof

If a component `K` of `Z-x` meets both new portal classes, a connected
subgraph of `K` meeting both is an `E`-carrier, while `{x}` is a disjoint
`D`-carrier.

Conversely, given disjoint carriers `L,R`, choose `x in L cap P_d`.
The connected `E`-carrier `R` lies in one component of `Z-x` and meets
both `P_e,P_f` there.  This proves the equivalence.

If `Z` is 2-connected, `Z-x` is connected.  It fails to meet both portal
classes only if one of them has no vertex after deleting `x`, namely if
`P_e={x}` or `P_f={x}`.  Distinct vertices of `P_d` cannot both be the
unique vertex of the same nonempty portal set, so at most two occur.
\(\square\)

Theorem 4 deliberately forgets `alpha,beta`.  To obtain a `K_7`, the two
carriers must additionally be rooted as in Theorem 2.  Failure to root
them need not give a cutvertex: it can again be an alternating Two-Paths
web.  Hence (3.3) follows only from failure of *unrooted* capacity, not
from target-freeness by itself.

## 4. The no-`K_7^-` single-gate branch is a two-pair web edge

Assume `G` has no `K_7^-` minor.  A target-free rotation cannot have
`|D|=1` or `|E|=1`; either would itself display a `K_7^-` model.  Hence
every single-gate rotation edge left by the rooted trichotomies has

\[
                          |D|=|E|=2.                      \tag{4.1}
\]

The absence of `K_7^-` gives more than failure of the full split.

### Theorem 5 (robust four-demand exclusion)

For subsets `D_0 subseteq D` and `E_0 subseteq E`, suppose `Z` has
vertex-disjoint carriers `L,R` such that:

* `L` is `X`-rooted and meets every `P_i`, `i in D_0`; and
* `R` is `W`-rooted and meets every `P_i`, `i in E_0`.

Then `G` contains a seven-bag model in which the only possibly absent
bag adjacencies are

\[
                    \{(X\cup Z_X,F_i):i in D-D_0\}
             \mathbin{\cup}
                    \{(W\cup Z_W,F_i):i in E-E_0\}.       \tag{4.2}
\]

Consequently:

* if `|D-D_0|+|E-E_0|=0`, there is a `K_7` minor; and
* if `|D-D_0|+|E-E_0|=1`, there is a `K_7^-` minor.

In a graph with neither minor, **no two disjoint rooted carriers can
cover three of the four occurrences in the demand multiset `D dotcup E`**.

#### Proof

Extend the two disjoint rooted carriers to an adjacent connected
partition `Z=Z_X dotcup Z_W` exactly as in Theorem 2.  Use the seven
bags (2.2).  The first enlarged centre retains every old row outside
`D` through `X` and gains the rows in `D_0` through `L`; therefore only
the first family in (4.2) may be absent.  The symmetric statement holds
for the second enlarged centre.  Every other adjacency is a fixed-row
clique edge or the edge between the two connected sides of `Z`.

With no absent pair the model is `K_7`.  With exactly one absent pair it
contains `K_7^-` (and it is harmless if that last pair also happens to
be present). \(\square\)

For `D={d_1,d_2}` and `E={e_1,e_2}`, the target-free connector therefore
simultaneously forbids all four rooted capacity patterns

\[
 \begin{array}{ll}
  D\text{-carrier against an }\{e_1\}\text{-carrier},&
  D\text{-carrier against an }\{e_2\}\text{-carrier},\\
  \{d_1\}\text{-carrier against an }E\text{-carrier},&
  \{d_2\}\text{-carrier against an }E\text{-carrier}.
 \end{array}                                               \tag{4.3}
\]

This is a **robust** rooted web obstruction: deleting any one of the
four row demands still does not permit the two rooted sides.  It is
strictly narrower than an arbitrary failure of two prescribed disjoint
paths.

By Theorem 2, its connector `Z` has no pair of disjoint rooted carriers,
one meeting the two old missing-row portal classes and the other meeting
the two new classes.  This is precisely a port-set version of the Two
Paths obstruction.  After localizing attachment cutvertices and 2-cuts,
the 3-connected torso is the web/rural alternative of the Two Paths
Theorem.

Thus the remaining no-`K_7^-` single-gate composition lemma can be stated without
Moser labels or model history:

> **Rotation-web composition target.**  A cycle of involutive two-pair
> rotation edges either has one connector with the rooted two-carrier
> split of Theorem 2, has two opposite proper-minor operations producing
> the same actual-adhesion equality state, or all connector webs compose
> with one common pair of literal apex vertices.

This is the genuine global target for the single-gate exchange component.
The two-piece concentrated exchange remains a separate possible source of
directed progress.  A proof which merely chooses a smaller centre on each
single-gate edge is invalid by Theorem 1.
