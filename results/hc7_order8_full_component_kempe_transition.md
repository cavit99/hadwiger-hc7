# Kempe transitions across a boundary-full order-eight separation

**Status:** written proof; separate internal audit in
[`hc7_order8_full_component_kempe_transition_audit.md`](hc7_order8_full_component_kempe_transition_audit.md).

This theorem is an unbounded host-level reduction for the two remaining
component counts at the order-eight boundary.  It replaces arbitrary,
unrelated boundary extension languages by one connected Kempe-reconfiguration
space.  Every change of shore extendability along that space has a literal
bichromatic path through the named complementary component.

The final section applies the transition to every one of the 82 boundary
graphs in the three-component finite normal form.  It produces a compulsory
edge-deletion response and five colour-indexed paths in one literal component.
It does not yet allocate those paths to the inherited clique-minor branch
sets, and therefore does not prove `HC_7`.

## 1. Boundary and extension notation

Let `G` be a graph satisfying

1. `G` has no `K_7` minor;
2. `G` is not six-colourable; and
3. every proper minor of `G` is six-colourable.

Let `X` be a set of eight vertices.  Suppose that the components of `G-X`
are

\[
                         C_1,\ldots,C_m,
             \qquad m\in\{2,3\},                         \tag{1.1}
\]

and every `C_i` is **`X`-full**: it is nonempty and connected and every
literal vertex of `X` has a neighbour in `C_i`.  Put

\[
                              H=G[X].                    \tag{1.2}
\]

A labelled proper boundary colouring
`phi:X -> {1,...,6}` **extends through** `C_i` if it is the restriction of
a proper six-colouring of `G[C_i union X]`.  Define its extension signature
by

\[
 \lambda(\phi)=\{i:\phi\text{ extends through }C_i\}.    \tag{1.3}
\]

The components in (1.1) are pairwise anticomplete.  Consequently, a labelled
boundary colouring extends through a union of component-sides exactly when
it extends through each component separately.  In particular,

\[
                        \lambda(\phi)\ne[m]              \tag{1.4}
\]

for every `phi`, since otherwise the component-side colourings glue to a
six-colouring of `G`.

## 2. Boundary degeneracy and connected Kempe spaces

### Theorem 2.1 (full boundary and exact-block Kempe connectivity)

The graph `H` is five-degenerate.  More strongly, for every nonempty
independent set `I subseteq X`, the graph `H-I` is four-degenerate.

It follows that:

1. all labelled proper six-colourings of `H` belong to one Kempe class; and
2. after fixing colour six exactly on `I`, all labelled boundary colourings
   `phi` satisfying

   \[
                         \phi^{-1}(6)=I                 \tag{2.1}
   \]

   belong to one Kempe class under interchanges using only colours
   `1,...,5`.

Every component-side admits a colouring satisfying (2.1).  When `m=3`,
every individual component-side also admits any two prescribed disjoint,
nonempty independent sets `I,J subseteq X` as two exact boundary colour
classes with distinct colours.

#### Proof

Suppose first that a subgraph `F` of `H` has minimum degree at least six,
and put `h=|V(F)|`.  Then `7<=h<=8`.  Contract two distinct full components
to two vertices.  The two contraction images are nonadjacent and each is
complete to `F`, so the resulting minor contains

\[
                         \overline K_2\vee F.            \tag{2.2}
\]

This graph has `h+2` vertices and at least

\[
                         2h+3h=5h                       \tag{2.3}
\]

edges.  Mader's exact extremal bound for a `K_7`-minor-free graph gives at
most

\[
                         5(h+2)-15=5h-5                 \tag{2.4}
\]

edges, a contradiction.  Thus `H` is five-degenerate.

Now fix a nonempty independent `I`.  If a subgraph `F` of `H-I` has
minimum degree at least five, then `6<=h<=7`.  The same two contractions
give the minor (2.2), now with at least

\[
                     2h+\left\lceil\frac{5h}{2}\right\rceil
\]

edges.  This is `27` when `h=6` and `32` when `h=7`, whereas (2.4) is
respectively `25` and `30`.  Hence `H-I` is four-degenerate.

The theorem of Las Vergnas and Meyniel that all `k`-colourings of a
`(k-1)`-degenerate graph are Kempe equivalent now applies with `k=6` to
`H`, and with `k=5` to `H-I`.  In the latter application colour six is
fixed on `I`, and every Kempe interchange avoids that colour.  This proves
the two connectivity assertions.  Unused palette colours cause no problem:
a proper colouring with fewer colours is still a labelled `k`-colouring.

For the exact-block assertion, choose `j ne i` and contract a spanning tree
of the connected set

\[
                            C_j\cup I.                  \tag{2.5}
\]

Six-colour the proper minor and pull the colouring back only to
`G[C_i union X]`, expanding the colour of the contraction image over the
literal independent set `I`.  Fullness makes that image adjacent to every
vertex of `X-I`; hence (2.1) holds exactly.

Finally suppose `m=3`, and let `I,J` be disjoint nonempty independent
sets.  To colour the side containing `C_k`, contract separately

\[
                         C_i\cup I,\qquad C_j\cup J,     \tag{2.6}
\]

where `{i,j,k}={1,2,3}`.  The two images are adjacent, and each image is
adjacent to every boundary vertex outside its own block.  Pullback to the
untouched `C_k`-side therefore makes `I,J` exact boundary classes with
distinct colours.  \(\square\)

### Corollary 2.2 (connected exact-pair cylinder)

Assume `m=3`.  Let `I,J` be disjoint nonempty independent subsets of `X`
with

\[
                              |I\cup J|\ge4.             \tag{2.7}
\]

After fixing two distinct colours exactly on `I,J`, all such labelled
boundary colourings lie in one Kempe class under moves avoiding both fixed
colours.

#### Proof

The graph `H-(I union J)` has at most four vertices and is therefore
three-degenerate.  Apply the Las Vergnas--Meyniel theorem with the four
remaining colours.  \(\square\)

## 3. A change of extension signature gives a literal path

Let `Gamma` be either the full six-colour boundary Kempe graph from
Theorem 2.1 or one of its exact-block subgraphs.  Suppose adjacent
colourings `phi,phi'` interchange colours `alpha,beta` on one component
`W` of `H[alpha,beta]`.

### Lemma 3.1 (signature-change path)

If

\[
                        i\in\lambda(\phi)-\lambda(\phi'), \tag{3.1}
\]

then every extension of `phi` through `C_i` contains an
`alpha`--`beta` path joining `W` to a different boundary component of
`H[alpha,beta]`, with every internal vertex in the literal component
`C_i`.  The reverse statement holds when the membership change is from
`phi'` to `phi`.

#### Proof

Take an extension of `phi` to `G[C_i union X]`.  Consider the full
`alpha`--`beta` components that meet `W`.  If none meets another boundary
component, interchange the two colours on their union.  This gives an
extension of `phi'`, contrary to (3.1).

Thus one full two-colour component meets `W` and a different boundary
two-colour component.  A shortest path between the two boundary components
has no internal vertex in `X`; all its internal vertices therefore lie in
`C_i`.  \(\square\)

This lemma retains the labelled boundary colouring, the operated boundary
component, the colour pair, and the literal complementary component.  It
does not identify palette colours with clique-minor branch-set labels.

## 4. Consequences for two and three full components

### Theorem 4.1 (two-component transition)

Assume `m=2`, and fix a nonempty independent `I subseteq X`.  There is a
shortest path

\[
                       \phi_0,\ldots,\phi_k             \tag{4.1}
\]

in the connected exact-`I` boundary Kempe graph such that:

1. `phi_0` extends through `C_1` and `phi_k` extends through `C_2`;
2. the first Kempe move in (4.1) has a signature-change path with interior
   in `C_1`;
3. the last move, read backwards, has such a path with interior in `C_2`;
4. every colouring in (4.1) retains `I` as the same exact labelled colour
   class.

If `k=1`, the same boundary interchange is obstructed by literal
bichromatic paths in the two opposite components.

#### Proof

The two extension sets in the exact-`I` Kempe graph are nonempty by
Theorem 2.1.  They are disjoint: a common labelled boundary colouring
would glue across the two anticomplete components.  Choose (4.1) with
minimum length over all endpoint choices.

No `phi_t` with `t>0` extends through `C_1`, and no `phi_t` with `t<k`
extends through `C_2`, since either occurrence would shorten (4.1).  Apply
Lemma 3.1 to the first and last edges.  \(\square\)

### Theorem 4.2 (three-component transition tree)

Assume `m=3`.  For every nonempty independent `I subseteq X`, there are
three exact-`I` boundary colourings `psi_1,psi_2,psi_3` satisfying

\[
                       \lambda(\psi_i)=[3]-\{i\}.        \tag{4.2}
\]

One finite tree in the exact-`I` boundary Kempe graph contains all three
colourings.  For each `i`, some edge of that tree changes membership in
the `C_i` extension set, and therefore Lemma 3.1 supplies a literal
bichromatic path with interior in `C_i`.

The same assertion holds without fixing `I`, in the full boundary
six-colour Kempe graph.

#### Proof

Contract `C_i union I`, six-colour the proper minor, and restrict to the
unchanged union of the other two closed component-sides.  After normalizing
the colour of `I`, the resulting boundary colouring `psi_i` extends through
the other two components.  It cannot extend through `C_i`, by (1.4).  This
proves (4.2).

Join the three `psi_i` by finitely many paths in the connected exact-`I`
Kempe graph and take a spanning tree of their union.  For fixed `i`, the
`i`-th signature bit is zero at `psi_i` and one at either other anchor.
It changes along their tree path, so Lemma 3.1 applies.  If no exact block
is fixed, delete `C_i` instead of contracting `C_i union I`, and use the
full boundary Kempe graph from Theorem 2.1.  \(\square\)

The three paths in Theorem 4.2 can come from different boundary moves and
different colour pairs.  The theorem asserts neither their simultaneous
existence in one colouring nor their mutual disjointness.

## 5. The high-demand edge-deletion fan in the 82-type residue

Assume `m=3` and that `H` is one of the 82 graphs in the audited
three-component boundary classification.  Thus `H` is three-colourable
and has no clique odd-cycle transversal.  In particular, every proper
boundary equality partition has packet demand at least three.

Choose a proper three-colouring

\[
                         X=A\mathbin{\dot\cup}B
                              \mathbin{\dot\cup}\{p,q\}. \tag{5.1}
\]

Such a colouring exists: no colour class can be a singleton, since deleting
that singleton clique would leave a bipartite graph; hence a three-colouring
of eight vertices has a colour class of order two.  In particular,
`pq notin E(H)`.  The local names `p,q` need not be the inherited old
boundary labels used before the order-eight descent; identifying them with
minor-model labels is part of the remaining allocation problem.

For each `i`, fix an ordering `(j,k)` of the other two components and form
the proper minor obtained by contracting separately

\[
                         C_j\cup A,\qquad C_k\cup B.     \tag{5.2}
\]

Every six-colouring of this fixed minor induces on `X` one of the two
partitions

\[
 \Theta=A\mid B\mid\{p,q\},\qquad
 \Omega=A\mid B\mid\{p\}\mid\{q\}.                    \tag{5.3}
\]

### Theorem 5.1 (gluing or a locked path and critical fan)

Exactly one of the following outcomes is forced.

1. Every component-side admits the partition `Theta`; the three
   component-side colourings align and six-colour `G`.
2. For some fixed `i` and the fixed orientation (5.2), every colouring of
   that minor induces `Omega`.  In this case:

   a. `G[C_i union X]` contains a bichromatic `p`--`q` path with all
      internal vertices in `C_i`;
   b. if `e=pv` is the first edge of such a path and `d` is any
      six-colouring of `G-e`, then its boundary partition `rho` is different
      from `Omega`, does not extend through the intact `C_i`-side, and has
      packet demand at least three;
   c. writing `alpha=d(p)=d(v)`, for every colour `beta ne alpha` there is
      an `alpha`--`beta` path from `v` to `X` with all internal vertices in
      `C_i`;
   d. the five paths in item c can be selected pairwise edge-disjoint, and
      paths belonging to different `beta` can meet only at
      `alpha`-coloured vertices.  If two paths have the same boundary
      endpoint, that endpoint has colour `alpha`.

#### Proof

The contraction images in (5.2) are adjacent to one another and to both
`p,q`.  Hence (5.3) lists all possible boundary partitions.  If, for every
`i`, the fixed minor has some colouring inducing `Theta`, restrict those
three colourings to the respective intact component-sides, align their
palettes on the common equality partition, and glue.

Otherwise fix `i` for which no such colouring exists.  Every colouring of
that fixed minor induces `Omega`.  In one such colouring, consider the
two-colour graph determined by the colours on `p,q`.  If they lie in
different components, a Kempe interchange on the component containing
`p` merges them, producing `Theta`.  They therefore lie in the same
component.  The two contraction images and all vertices of `A union B`
use the other two boundary colours, so a shortest `p`--`q` path has all
internal vertices in `C_i`.  Since `pq` is not an edge, its first edge is
`e=pv` with `v in C_i`.  This proves item a.

Every colouring `d` of `G-e` gives `d(p)=d(v)`: otherwise restoring `e`
would six-colour `G`.  Its restriction to `X` extends through both
components other than `C_i`.  It cannot extend through intact `C_i`, since
the three extensions would glue.  On the other hand `Omega` does extend
through `C_i` by the preceding locked colouring.  If `rho=Omega`, these
extensions again glue, so `rho ne Omega`.  The no-clique-odd-cycle-
transversal property says exactly that every proper partition of `H` has
packet demand at least three.  This proves item b.

Put `alpha=d(p)=d(v)`.  Fix `beta ne alpha`.  If the full
`alpha`--`beta` component containing `v` did not contain `p`, interchange
the two colours on that component.  The result would still colour `G-e`,
but `p,v` would then have different colours and `e` could be restored.
Thus `v,p` lie in the same two-colour component.  Take a `v`--`p` path in
that component and stop it at its first vertex of `X`; its internal vertices
lie in `C_i`.  This proves item c.

For two different colours `beta,gamma`, the two selected paths can share
only vertices whose colour lies in

\[
                  \{\alpha,\beta\}\cap\{\alpha,\gamma\}
                         =\{\alpha\}.                   \tag{5.4}
\]

They cannot share an edge, since a proper-colouring edge cannot have two
`alpha`-coloured ends.  The same intersection calculation shows that a
repeated boundary endpoint is `alpha`-coloured.  This proves item d.
\(\square\)

The paths in Theorem 5.1 all contain `v` and may share further
`alpha`-coloured vertices.  Their first boundary endpoint may be `p`.
Accordingly, they are not five disjoint branch-set extensions and do not
simultaneously add five boundary edges.  The remaining theorem must use
the inherited named branch sets and proper-minor responses to diversify
their first hits, or show that their concentration exposes an actual
order-seven separation carrying a compatible boundary partition.

## 6. Exact scope

The results above make three advances over the former static interface.

1. The two closed-shore languages at `m=2` lie in one exact-block Kempe
   cylinder with literal obstruction paths at both ends.
2. At `m=3`, three pairwise-extension responses lie in one connected
   boundary reconfiguration space, and every component occurs as a literal
   signature-change obstruction.
3. Every one of the 82 finite boundary types has the locked-path or
   edge-deletion-fan output of Theorem 5.1.

They do **not** prove a common partition, an order-seven separator, or a
`K_7` minor.  A shortest transition can have more than one edge; bridges
in different components need not correspond to the same boundary move;
and palette colours do not identify the five inherited clique-minor branch
sets.

The next positive theorem must convert the high-demand fan or one of the
signature-change paths into either

- two disjoint connected subgraphs with the required literal branch-set
  contacts;
- an attained partition reproduced on every closed component-side; or
- a strict full-neighbourhood-separator descent preserving the inherited
  labels and boundary equality data.

## 7. External inputs

- W. Mader, *Homomorphiesätze für Graphen*, Math. Ann. 178 (1968),
  154--168: the exact edge bound `5n-15` for `K_7`-minor-free graphs.
- M. Las Vergnas and H. Meyniel, *Kempe classes and the Hadwiger
  Conjecture*, J. Combin. Theory Ser. B 31 (1981), 95--104: all
  `k`-colourings of a `(k-1)`-degenerate graph are Kempe equivalent.
- [three-component order-eight boundary classification](hc7_order8_three_component_boundary_classification.md)
  for the 82-type normal form and the packet-demand identity used in
  Section 5.
