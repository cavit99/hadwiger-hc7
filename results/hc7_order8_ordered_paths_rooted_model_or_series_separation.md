# Ordered paths: a rooted model or an exact series separation

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_ordered_paths_rooted_model_or_series_separation_audit.md`](hc7_order8_ordered_paths_rooted_model_or_series_separation_audit.md).
This is an unbounded conditional theorem in the connected order-eight
interface.  It does not prove `HC_7`.

## 1. Setting

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
\]

where

\[
 S=\{d,e,x_d,y_d,x_e,y_e,x_0,y_0\}.
\]

Assume that `G[L]` and `G[R]` are connected and that `d,e` are
nonadjacent.  Suppose that `G[S]` contains the two vertex-disjoint
triangles

\[
                   d x_d y_d d,
             \qquad e x_e y_e e.                    \tag{1.1}
\]

Suppose that `G[R]` contains disjoint connected subgraphs `P_0,P_1`,
each adjacent to every vertex of `S`, with an edge between them.  Suppose
that `G[L]` contains disjoint connected subgraphs `A_d,A_e` such that

\[
 S-\{d\}\subseteq N_G(A_d)\cap S,
 \qquad
 S-\{e\}\subseteq N_G(A_e)\cap S,                  \tag{1.2}
\]

with an edge between `A_d` and `A_e`.

Finally, fix a proper colouring of `G[L\cup S]`.  Suppose that `d,e` have
one common colour `alpha`, and that there are three `d`--`e` paths

\[
                         K_1,K_2,K_3                 \tag{1.3}
\]

whose internal vertices lie in `L`, where `K_i` uses exactly the two colours
`alpha,beta_i` and the three `beta_i` are distinct.  Thus every common
vertex of two different paths has colour `alpha`.  This is the fixed
merged-root six-colouring in the intended application.  Assume the
ordered-crossing conclusion already proved for this setting:
every `d`--`e` path with interior in `L` first meets `A_e` and last meets
`A_d`.

Put

\[
                         H=G[L\cup\{d,e\}].          \tag{1.4}
\]

An **`S`-rooted `K_5` model on the `L`-side** means five pairwise disjoint,
connected, pairwise adjacent subgraphs of `G[L\cup S]`, each containing a
distinct vertex of `S`.  Together with `P_0,P_1`, such a model is an
explicit `K_7`-minor model.

## 2. A pointwise boundary-compatible path pair gives a rooted `K_5`

### Lemma 2.1

Suppose `H` contains two internally vertex-disjoint `d`--`e` paths
`Q_1,Q_2`.  For each path choose a trimmed subpath

\[
                         W_i=a_iQ_i b_i
\]

from `A_e` to `A_d`, with no internal vertex in either deficient
subgraph.  Assume, after possibly interchanging the two paths, that

\[
 \begin{split}
 &a_1x_e\in E(G),\\
 &a_1x_d,a_1y_d,a_2x_d,a_2y_d,b_2x_d,b_2y_d\in E(G). \tag{2.1}
 \end{split}
\]

Then `G[L\cup S]` contains an `S`-rooted `K_5` model.  Consequently `G`
contains a `K_7` minor.

#### Proof

Such trimmed subpaths exist because the first encounter with
`A_d\cup A_e` lies in `A_e` and the last encounter lies in `A_d`: take a
last `A_e`-vertex immediately before a subsequent first `A_d`-vertex.
Internal disjointness gives

\[
                         a_1\ne a_2,
                  \qquad b_1\ne b_2.                \tag{2.2}
\]

Choose an edge `uv` of `W_2`, with `u` preceding `v` from `a_2` toward
`b_2`.  Define three vertex sets as follows.

* `B_d` is the union of the `d`--`a_1` prefix of `Q_1` with `a_1`
  deleted and the `d`--`u` prefix of `Q_2`.
* `B_e` is the union of the `b_1`--`e` suffix of `Q_1` with `b_1`
  deleted and the `v`--`e` suffix of `Q_2`.
* `B_m=V(W_1)\cup\{x_e\}`.

The first two sets are connected because their two constituent paths meet
at `d` and `e`, respectively.  The third is connected by the first edge
listed in (2.1).  The three sets
are pairwise disjoint: the two paths meet only at `d,e`, while the displayed
prefixes and suffixes exclude the endpoints of `W_1` assigned to `B_m`.

There is a `B_d`--`B_e` edge, namely `uv`.  The edge of `Q_1` immediately
preceding `a_1` joins `B_d` to `B_m`, and the edge immediately following
`b_1` joins `B_m` to `B_e`.  Thus the three sets are pairwise adjacent.

Moreover, `B_d` contains `a_2` (because every edge of `W_2` occurs at or
after `a_2`), `B_e` contains `b_2`, and `B_m` contains `a_1`.  The remaining
edges in (2.1) make each of these three sets adjacent to both `x_d` and
`y_d`.
Therefore

\[
                    B_d,\quad B_e,\quad B_m,
                    \quad\{x_d\},\quad\{y_d\}       \tag{2.3}
\]

are five pairwise disjoint connected pairwise adjacent sets.  They contain
the five distinct boundary vertices `d,e,x_e,x_d,y_d`, respectively, so
they form the required rooted `K_5` model.

Finally append `P_0,P_1`.  They are adjacent to each other and, through the
distinct boundary root in every set in (2.3), to every rooted branch set.
This gives an explicit `K_7`-minor model. \(\square\)

The pointwise boundary-contact condition (2.1) is stronger than the aggregate
neighbourhood condition (1.2).  It is stated explicitly because aggregate
contact does not identify the vertices carrying those contacts.  Removing
this extra condition is the unresolved rooted-allocation problem.

Call a pair `Q_1,Q_2` **pointwise boundary-compatible** if some choice of
trimmed subpaths and one of the two index orders satisfies (2.1).

## 3. The exact one-vertex series obstruction

### Theorem 3.1

Assume, in addition to the hypotheses of Section 1, that `H` has no two
internally vertex-disjoint `d`--`e` paths.  Then at least one of the
following holds.

1. `G` contains an explicit `K_7`-minor model.
2. There is a nonempty connected subgraph `C` contained in `L` such that
   `N_G(C)` is an actual separator of order at most seven.
3. There is a vertex `z in L` and exactly two components `C_d,C_e` of
   `G[L]-z`, satisfying

   \[
   N_G(C_d)=\{z\}\mathbin{\dot\cup}(S-\{e\}),
   \qquad
   N_G(C_e)=\{z\}\mathbin{\dot\cup}(S-\{d\}).       \tag{3.1}
   \]

   Every `K_i` passes in the order

   \[
                         d,\ C_d,\ z,\ C_e,\ e.     \tag{3.2}
   \]

   The vertex `z` has colour `alpha`.  For each `i`, its neighbour on the
   `d`-side of `K_i` lies in `C_d` and has colour `beta_i`, while its
   neighbour on the `e`-side lies in `C_e` and has colour `beta_i`.  These
   six neighbours are pairwise distinct.

Thus the only survivor not already returning a separator of order at most
seven is an exact one-vertex series composition of two connected components,
with all six colour-indexed neighbours retained literally.

#### Proof

Suppose outcomes 1 and 2 fail.  Menger's theorem, the additional hypothesis of
the theorem, and the existence of the paths (1.3) give a vertex `z in L`
separating `d` from `e` in `H`.

Let `C` be any component of `G[L]-z`.  Since there are no `L`--`R` edges,

\[
                         N_G(C)\subseteq \{z\}\cup S.              \tag{3.3}
\]

The component cannot have neighbours at both `d` and `e`, since it would
then join them in `H-z`.  Hence `|N_G(C)|<=8`.  The set `N_G(C)` is an
actual separator: `C` is one nonempty side, while the nonempty set `R`
survives outside `C\cup N_G(C)` and has no edge to `C`.  Outcome 2 being
excluded, every component therefore has one of the two exact neighbourhoods

\[
 \{z\}\cup(S-\{e\}),
 \qquad
 \{z\}\cup(S-\{d\}).                               \tag{3.4}
\]

There cannot be two components `D_1,D_2` with the first neighbourhood in
(3.4).  If there were, the following seven sets would be an explicit
`K_7`-minor model:

\[
 P_0,\quad P_1,\quad
 V(D_1)\cup\{x_e\},\quad
 V(D_2)\cup\{y_e\},\quad
 \{d\},\quad\{x_d\},\quad\{y_d\}.                 \tag{3.5}
\]

The first two are adjacent and boundary-full.  The next two are connected,
are adjacent through the edge `x_e y_e`, and each is adjacent to the last
three sets by (3.4).  The last three form the first triangle in (1.1).
Boundary-fullness supplies every remaining adjacency.  This is outcome 1.
Symmetrically, two components
with the second neighbourhood in (3.4) give a `K_7` model using `x_d,y_d`
to enlarge the two components and the triangle `e x_e y_e` as the last
three branch sets.

Every path `K_i` meets `z`.  Since `z` lies on all three paths, the pairwise
intersection rule gives it colour `alpha`.  Properness therefore gives
that neither `zd` nor `ze` is an edge, so each path has a nonempty internal
segment on both sides of `z`.  Its initial segment supplies a component of
the first type in (3.4), and its final segment supplies one of the second
type.  Hence at least one component of each type exists.  The preceding
paragraph shows that there is exactly one of each; call them `C_d,C_e`.
There can be no third component, which proves (3.1) and (3.2).

Along `K_i`, each neighbour of `z` has colour `beta_i`.  Neighbours
belonging to different paths are distinct: a common neighbour would be a
common vertex of two paths with a colour different from `alpha`, contrary
to the intersection rule.  The two sides lie in the disjoint components
`C_d,C_e`, so all six neighbours are distinct. \(\square\)

### Corollary 3.2 (complete local alternative)

Without the extra local-connectivity hypothesis in Theorem 3.1, one of the
following holds:

1. `G` contains an explicit `K_7` model, either from the pointwise
   boundary-compatible pair in Lemma 2.1 or from repeated exact components
   in Theorem 3.1;
2. `H` has two internally vertex-disjoint `d`--`e` paths, but no such pair
   is pointwise boundary-compatible (equivalently, every eligible choice
   of trimmed subpaths in both index orders fails (2.1));
3. an actual separator of order at most seven occurs; or
4. the exact one-vertex series structure (3.1)--(3.2) occurs.

Outcome 2 is precisely the palette-to-literal boundary-contact gap.  The
aggregate contacts in (1.2) do not by themselves place the contacts on the
trimmed path endpoints.

## 4. The inherited boundary colourings

Now assume the full opposite-response data, and let the fixed colouring in
Section 1 be a six-colouring `c_=` of `G[L\cup S]` inducing

\[
                         X\mid Y\mid\{d,e\},         \tag{4.1}
\]

where `S-{d,e}=X dotcup Y`, and let `c_ne` be a six-colouring of
`G[R\cup S]` inducing

\[
                         X\mid Y\mid\{d\}\mid\{e\}.\tag{4.2}
\]

Assume outcome 3 of Theorem 3.1, and put

\[
 S_d=\{z\}\cup(S-\{e\}),
 \qquad
 S_e=\{z\}\cup(S-\{d\}).                           \tag{4.3}
\]

### Proposition 4.1

Each of the two exact order-eight separations inherits the same opposite
response pattern:

* on `G[C_d\cup S_d]`, the restriction of `c_=` induces
  `X|Y|{d,z}`;
* on `G-C_d`, there is a six-colouring inducing
  `X|Y|{d}|{z}` on `S_d`;
* on `G[C_e\cup S_e]`, the restriction of `c_=` induces
  `X|Y|{e,z}`;
* on `G-C_e`, there is a six-colouring inducing
  `X|Y|{e}|{z}` on `S_e`.

#### Proof

The vertex `z` has the common root colour `alpha` in `c_=`.  Restriction
therefore gives the two merged partitions immediately.

For the opposite colouring at `S_d`, permute the colours of `c_=` so that
its colours on the three blocks `X,Y,{e}` agree with the colours of
`c_ne` on those blocks.  Use the permuted colouring on `C_e\cup\{z\}` and
use `c_ne` on `R\cup S`.  These assignments are compatible on every edge:

* `C_e` has no neighbour at `d`, by (3.1), and its colours agree with the
  colours of all its other boundary neighbours;
* `z` receives the `c_ne`-colour of `e`, while `d` has a distinct colour;
* properness of `c_=` shows that `z` is not adjacent to `e`, and its other
  boundary neighbours have the aligned `X`- or `Y`-colour; and
* there are no edges from `C_e\cup\{z\}` to `R`.

This is a proper colouring of `G-C_d`.  On `S_d`, the vertices `d,z` have
the two distinct colours used by `d,e` in (4.2), so the induced partition
is exactly `X|Y|{d}|{z}`.

The construction for `G-C_e` is symmetric: align the `c_=` colours on
`X,Y,{d}` with `c_ne`, use the permuted colouring on `C_d\cup\{z\}`, and
use `c_ne` on `R\cup S`.  Now `C_d` has no neighbour at `e`, and `z` gets
the `c_ne`-colour of `d`, distinct from the colour on `e`. \(\square\)

## 5. Exact gain and missing response geometry

In the one-vertex series branch, Theorem 3.1 and Proposition 4.1 produce a
strict descent in **open-shore order** at the level of exact boundary
colourings: both `C_d` and `C_e` are proper subsets of `L`, and each new
exact order-eight separation retains a
merged response on the smaller lobe and a split response on the opposite
closed shore.

This is not yet a recursive instance of the full selected-response
interface.  In particular:

* the original connected subgraphs `P_0,P_1` have no neighbours at `z`,
  because `z in L` and there are no `L`--`R` edges, so they are not
  boundary-full for either new boundary;
* more strongly, the original two labels cannot both be extended
  disjointly.  Relative to `S_d`, the complementary open shore is
  `C_e dotcup {e} dotcup R`.  Every connected subgraph there which meets
  `R` and is adjacent to `z` must contain `e`: it must meet `C_e`, because
  `z` has no neighbour in `R union {e}`, and `e` is the only vertex of this
  open shore through which `C_e` can reach `R`.  Thus two disjoint
  boundary-full extensions of `P_0,P_1` are impossible.  Symmetrically,
  every such extension relative to `S_e` contains `d`;
* the hypotheses do not give the new root `z` a neighbour in either of the
  boundary classes `X,Y`, and neither new boundary is known to contain a
  second rooted triangle through `z`; and
* the original labelled subgraphs `A_d,A_e` may meet `z` or lie on either
  side of it, so the required pair of one-defect connected subgraphs is not
  automatically inherited by either smaller lobe.

Thus the colour responses descend strictly, and the six colour-indexed
neighbours survive literally, but the named branch-set geometry does not
descend.  In the locally two-connected branch, removing the pointwise
portal hypothesis from Lemma 2.1 remains open.  In the series branch, any
recursive continuation must replace the lost labels and boundary
incidences; neither such a continuation nor an order-seven separation is
proved here.  Splitting only at the three `beta_i` neighbours cannot restore
both original `P_0,P_1` labels across the omitted-root bottleneck.

## 6. Dependencies

- [ordered crossings of the two deficient connected
  subgraphs](../results/hc7_order8_ordered_defect_crossing.md);
- [three colour-indexed Kempe paths on the merged-response
  shore](../results/hc7_merged_root_three_kempe_locks.md);
- [opposite colouring responses at the independent two-vertex
  transversal](../results/hc7_order8_independent_oct_opposite_response.md).
