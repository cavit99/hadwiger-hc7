# An exposed six-block boundary colouring at the canonical exact-seven separation

**Status:** written proof; separate internal audit GREEN.  This is a
conditional theorem about the canonical exact order-seven separation in a
hypothetical minor-minimal counterexample.  It does not prove `HC_7`.

## 1. Setup and notation

Let `G` satisfy

\[
 \chi(G)=7,
 \qquad
 \text{every proper minor of }G\text{ is six-colourable}.
 \tag{1.1}
\]

Suppose

\[
 V(G)=X\mathbin{\dot\cup}S\mathbin{\dot\cup}Y,
 \tag{1.2}
\]

where `X` and `Y` are nonempty, connected, and anticomplete, and every
vertex of `S` has a neighbour in each of `X` and `Y`.  Assume

\[
 G[S]=G[\{p,q\}]\vee G[C],
 \qquad pq\in E(G),
 \qquad G[C]\cong C_5.
 \tag{1.3}
\]

Thus `p,q` are the two adjacent universal vertices of the boundary.  Let

\[
 D=\overline{G[C]}\cong C_5.
 \tag{1.4}
\]

For an edge `e` of `D`, let `sigma_e` be the partition of `S` into six
blocks whose only nonsingleton block is the pair of ends of `e`.  For a
maximum matching `M` of `D`, let `pi_M` be the partition into five blocks
whose two nonsingleton blocks are the two edges of `M`.

For `Z in {X,Y}`, let `Ext_Z(S)` denote the equality partitions of the
literal boundary `S` induced by proper colourings of `G[Z union S]` with
at most six colours.

## 2. The exposed-partition theorem

### Theorem 2.1

The following statements hold.

1. The only possible members of either closed-shore extension language are
   the five partitions `sigma_e` and the five partitions `pi_M`.
2. The two languages are disjoint:

   \[
   \operatorname{Ext}_X(S)\cap\operatorname{Ext}_Y(S)=\varnothing.
   \tag{2.1}
   \]

3. Each language covers every edge of `D`: for every `e in E(D)` and each
   `Z in {X,Y}`, the language `Ext_Z(S)` contains either `sigma_e` or a
   partition `pi_M` with `e in M`.
4. For one shore `Z` there is an edge `e in E(D)` such that

   \[
   \sigma_e\in\operatorname{Ext}_Z(S),
   \tag{2.2}
   \]

   while neither of the two maximum matchings of `D` containing `e`
   defines a member of `Ext_Z(S)`.
5. Label

   \[
   D=x_0x_1x_2x_3x_4x_0
   \tag{2.3}
   \]

   so that the exposed partition in item 4 is
   `sigma_{x_0x_1}`.  In every colouring of the selected closed shore
   inducing this partition, there are

   - an `x_2`--`x_3` bichromatic path, and
   - an `x_3`--`x_4` bichromatic path,

   and all internal vertices of each path lie in the same selected open
   shore `Z`.

The two paths coexist in one colouring, but the theorem does not assert
that they are internally disjoint.

### Proof

The vertices `p,q` are adjacent and universal in `G[S]`, so each is a
singleton block in every proper boundary partition and their blocks are
distinct.  A nonsingleton block on `C` is an edge of the complementary
cycle `D`, and the nonsingleton blocks form a matching in `D`.  The graph
`G[C]` needs three or four colours in a colouring of `S` with at most six
colours.  Thus the matching has order two or one, respectively.  These are
exactly the five `pi_M` and five `sigma_e`, proving item 1.

If the two closed shores induced the same boundary equality partition,
permute the six colour names on one shore so that the boundary colours
agree.  The colourings then glue across the anticomplete open shores and
six-colour `G`, contrary to (1.1).  This proves item 2.

Fix an edge `e=uv` of `D`.  Contract the connected subgraph

\[
                         Y\cup\{u,v\}
\tag{2.4}
\]

to one vertex.  The result is a proper minor, so it has a six-colouring.
Expand `u,v` with the colour of the contracted vertex and restrict the
colouring to `G[X union S]`.  Every vertex of `S-e` is adjacent to `Y`,
and hence was adjacent to the contracted vertex, so no such boundary
vertex receives the colour of `u,v`.  The pair `e` is therefore an exact
boundary colour class.  Item 1 says that the returned partition is
`sigma_e` or a `pi_M` containing `e`.  Interchanging `X,Y` proves item 3
for both languages.

Suppose item 4 were false.  In either language, whenever an edge `e` was
covered only by `sigma_e`, one of the two `pi_M` containing `e` would also
belong to that language.  Consequently the `pi`-subfamily of each language
would itself cover all five edges of `D`.  At least three two-edge
matchings are needed to cover five edges.  The disjoint languages would
therefore contain at least six distinct `pi` partitions, although `D` has
only five maximum matchings.  This contradiction proves item 4.

Choose a colouring `c` of the selected closed shore inducing the exposed
partition `sigma_{x_0x_1}`.  The colours on `x_2,x_3,x_4` are distinct and
occur nowhere else on `S`.  If `x_2,x_3` belonged to different components
of the subgraph induced by their two colours, interchange those colours on
the component containing `x_2`.  The resulting proper colouring would
induce the partition with nonsingleton blocks

\[
                    \{x_0,x_1\},\qquad\{x_2,x_3\},
\tag{2.5}
\]

one of the two forbidden `pi` refinements in item 4.  Hence `x_2,x_3`
belong to one bichromatic component.  The same argument applied to
`x_3,x_4` gives the other component.  Since no other boundary vertex has
either relevant pair of colours, the internal vertices of the two paths
lie in `Z`.  This proves item 5.  QED.

## 3. Immediate model consequence

Assume additionally that `G` has no `K_7` minor.  The two paths in
Theorem 2.1 and the rooted-path case of the Kriesell--Mohr construction
give three disjoint connected branch sets rooted at `x_2,x_3,x_4` and
pairwise adjacent: the missing adjacencies `x_2x_3,x_3x_4` come from the
two bichromatic connections, while `x_2x_4` is an edge of `G[C]`.

Together with

\[
 \{p\},\quad \{q\},\quad Y\cup\{x_0\},\quad \{x_1\},
\tag{3.1}
\]

these form a labelled `K_7`-minus-one-edge minor model.  Its sole possibly
missing adjacency is between the branch set rooted at `x_1` and the branch
set rooted at `x_2`.

This strengthens the four-colour branch of the
[universal-edge Kempe normalization theorem](hc7_exact7_universal_edge_kempe_normalization.md): the two
consecutive missing-chord connections can always be selected in one fixed
open shore.  It still does not repair the last labelled adjacency.

## 4. Scope and dependency notes

The ten-partition classification and trace-completeness of the two
languages already appear in
`barriers/hc7_exact7_pentagonal_dynamic_language_barrier.md`.  The
singleton Kempe exchange is proved separately in
`results/hc7_exact7_singleton_block_kempe_exchange.md`.  The new step here
is the exposed-partition pigeonhole argument and its synthesis with those
ingredients to place two consecutive bichromatic connections in one fixed
shore and one fixed colouring.

The theorem does not force a third missing-chord connection, a rooted
`K_5` model, a common boundary partition, or a `K_7` minor.
