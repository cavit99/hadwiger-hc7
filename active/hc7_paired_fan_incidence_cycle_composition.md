# What a paired five-label fan needs from a Kempe incidence cycle

**Status:** active draft; written conditional composition theorem and exact
non-composition statement.  No separate internal audit.  This note does not
close the boundary-full order-eight interface or prove `HC_7`.

The paired fan and the two-shore Kempe incidence cycle solve different
parts of the live problem.  The fan reaches five literal boundary vertices
with five distinct inherited branch-set labels.  The incidence cycle gives
a literal odd cycle assembled from one pair of palette colours.  This note
records the exact extra conditions under which those outputs compose, and
shows why the incidence cycle itself cannot supply them in the two-component
case.

## 1. A terminal cyclic completion of the paired fan

Let `S=B dotcup T`, where

\[
 B=\{b_0,b_1,b_2\},\qquad
 T=\{t_0,t_1,t_2,t_3,t_4\}.
\tag{1.1}
\]

Let `C,Q` be distinct components of `G-S`, each adjacent to every literal
vertex of `S`.  Suppose that `F` is a connected subgraph of `C` with an edge
to every `t_i`.  In the intended application, `F` is the union of the source
path and the interiors of the paired five-label fan.

### Theorem 1.1 (rooted cyclic completion)

Suppose there are pairwise disjoint connected subgraphs

\[
                         A,Z_0,Z_1,Z_2,Z_3,Z_4,Q
\tag{1.2}
\]

with all of the following properties.

1. `F subseteq A subseteq C`, and `A` is adjacent to every `b_j`.
2. `t_i in Z_i` for every `i`, and `A` is adjacent to `Z_i` through the
   fixed `F-t_i` contact.
3. The five sets are cyclically adjacent:

   \[
                        E_G(Z_i,Z_{i+1})\ne\varnothing
                        \qquad(i\bmod 5).
   \tag{1.3}
   \]

4. The bipartite nonadjacency graph between
   `\{\{b_0\},\{b_1\},\{b_2\}\}` and `\{Z_0,...,Z_4\}` is a matching of
   order at most two.

Then `G` contains a `K_7` minor.

#### Proof

Contract a spanning tree of `A` to a vertex `v`.  The images of

\[
       \{v\},\ \{b_0\},\ \{b_1\},\ \{b_2\},\
       Z_0,Z_1,Z_2,Z_3,Z_4,\ Q
\tag{1.4}
\]

are pairwise disjoint.  The vertex `v` is adjacent to every singleton
`b_j` by item 1 and to every `Z_i` by item 2.  The five `Z_i` are cyclically
adjacent by item 3, and item 4 is exactly the matching-defect hypothesis of
the cyclic connected-set contact theorem.

Finally, `Q` is adjacent to each singleton `b_j` and to each `Z_i`: it is
adjacent to every vertex of `S`, and `b_j in S`, `t_i in Z_i cap S`.
Thus `Q` meets all eight root labels in that theorem.  Its explicit
allocation table gives six branch sets in the contracted graph; appending
`Q` gives a `K_7`-minor model.  Lifting the contraction replaces the branch
set containing `v` by the connected set `A`, and therefore gives a literal
minor model in `G`. \(\square\)

The theorem requires only a `T`-rooted five-cycle model, not a rooted
`K_5` model.  It is consequently weaker than the clean rooted-model decoder
for the paired fan.  Its two genuinely new requirements are that the cyclic
sets avoid both the fan source and the reserved component, and that they
retain the five literal roots.

## 2. Exact information carried by one incidence cycle

Use the notation of the audited two-shore Kempe incidence-cycle theorem.
Thus the boundary is `S`, the two open shores are anticomplete, the active
palette pair is `alpha,beta`, and `K` is the operated boundary two-colour
component.  Let `mathcal H_Z` be the union of the full two-colour components
belonging to an incidence cycle through `e_K`.

### Proposition 2.1 (support and reserved-component obstruction)

Every vertex of `mathcal H_Z cap S` has colour `alpha` or `beta`.  Every odd
cycle `O` in `mathcal H_Z` has all of the following properties.

1. `O` meets `K`.
2. `O` has a vertex in each open shore.
3. `|V(O)|>=5`.

Consequently, if the order-eight separation has exactly two complementary
components `C,Q`, and `Q` is retained whole as the seventh connected set in
Theorem 1.1, then no partition of `O` into five nonempty cyclically adjacent
connected sets can be used for `Z_0,...,Z_4`: its union meets `Q`.

#### Proof

The subgraph `mathcal H_Z` is a union of full `alpha`--`beta` components,
so its boundary vertices have one of those two colours.  Items 1 and 2 are
the literal odd-cycle conclusion of the incidence-cycle theorem.  A
triangle meeting both anticomplete open shores would need an edge between
those shores, so no such triangle exists.  Hence an odd cycle satisfying
item 2 has length at least five.

In the two-component case the two open shores are precisely `C` and `Q`.
Item 2 gives `V(O) cap Q ne empty`.  Five connected sets obtained by
partitioning `O` have union `V(O)`, and therefore cannot all be disjoint
from the reserved set `Q`. \(\square\)

There are only two possible ways around this obstruction.  One must either

* find in `Q-V(O)` a connected subgraph retaining the required seven or
  eight literal boundary contacts; or
* construct the five cyclic sets somewhere other than the incidence odd
  cycle.

Neither conclusion is part of the incidence-cycle theorem.

### Proposition 2.2 (the label-coverage obstruction)

If some `t_i` has a colour outside `\{alpha,beta\}` in the two boundary
colourings defining the incidence cycle, then no connected subgraph of
`mathcal H_Z` contains `t_i`.  Even when all five `t_i` use the active two
colours, the incidence-cycle theorem does not assert that one odd cycle, or
five disjoint cyclic pieces, contains all five vertices.

#### Proof

The first assertion follows from the definition of `mathcal H_Z` as a union
of `alpha`--`beta` components.  The second is exactly the distinction
between membership in the union of selected full components and membership
on one selected odd cycle: the parity proof only forces an odd cycle through
`K`, and imposes no other prescribed boundary vertex on that cycle.
\(\square\)

## 3. Why operation provenance does not yet bridge the two outputs

The operation-specific datum retained by the incidence construction is the
operated boundary component `K` and its active palette pair.  The equations
defining the incidence multigraph record which boundary two-colour
components lie in one full two-colour component on each shore.  They contain
no inherited branch-set label and no information about the paired fan's
five terminal vertices unless one of those vertices happens to lie in a
selected boundary component.

Conversely, the paired fan records the five literal labels

\[
                           U,D,F_1,F_2,F_3,
\tag{3.1}
\]

but its paths are not required to be bichromatic for one common palette
pair and are not required to lie in `mathcal H_Z`.  Thus the two audited
outputs do not by themselves imply the hypotheses of Theorem 1.1.

For three complementary components there is a possible genuine route: an
incidence cycle supported by exactly two components could leave the third
component as the reserved connected set.  To finish that route one still
has to prove both

1. a five-label `T`-rooted cyclic decomposition of the incidence support,
   disjoint from the paired-fan source; and
2. the matching bound on the three-by-five cross-nonadjacency graph.

For two complementary components, one additionally has to peel a
boundary-full residual from a component used by the incidence cycle.
These are literal host obligations.  They cannot be replaced by identifying
the two active palette colours with any of the five inherited model labels.

## 4. Dependencies and trust boundary

- [common-label paired paths at an order-eight boundary](../results/hc7_order8_common_label_paired_fan.md)
- [the two-shore Kempe incidence-cycle theorem](../results/hc7_two_shore_kempe_incidence_cycle.md)
- [cyclic connected-set contact allocation](../results/hc7_degree8_contact_allocation.md),
  Theorem 4.2

Theorem 1.1 is a terminal explicit minor-model construction once its
literal disjointness and incidence hypotheses are met.  Propositions 2.1
and 2.2 show that simply partitioning the incidence odd cycle cannot meet
those hypotheses in the two-component case and need not cover the five
labels in either component count.  The note does not prove that no more
elaborate operation-specific use of the incidence cycle can succeed.
