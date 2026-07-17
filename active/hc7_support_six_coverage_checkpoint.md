# Coverage map: a two-vertex transversal for small $K_5$-minor models

**Document role:** detailed dependency and coverage map. The authoritative
current research record is
[`../RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md). Neither $HC_7$ nor the
intermediate theorem below has been proved.

Unless a paragraph says otherwise, a result described here as proved has a
written proof and a separate internal audit beside the theorem note. An
internal audit is not external peer review. Results that depend on exhaustive
finite computation are marked **computer-assisted**.

## 1. Setup and intermediate theorem

Let $G$ be a seven-connected graph such that

$$
 \chi(G)=7,\qquad G\text{ has no }K_7\text{ minor},
$$

and every proper minor of $G$ is six-colourable. For a $K_5$-minor model
$M$, let $V(M)$ be the union of its branch sets, and put

$$
 \mathcal F_6(G)=\{V(M):M\text{ is a }K_5\text{-minor model and }
 |V(M)|\le 6\}.
$$

The active intermediate target is

$$
                         \tau(\mathcal F_6(G))\le 2.       \tag{1.1}
$$

Every irredundant six-vertex $K_5$-minor model consists of four singleton
branch sets inducing a $K_4$, together with one two-vertex branch set. The
edge in that two-vertex branch set will be called its **matching edge**.

The rest of this document records what is known under the contradictory
assumption $\tau(\mathcal F_6(G))>2$. A reduction through a separation is
not considered complete unless it preserves the specified branch sets and
boundary colouring partition and strictly decreases a named induction
parameter.

## 2. Proved initial extraction

The following facts are proved and internally audited.

1. There are three supports $A_1,A_2,A_3\in\mathcal F_6(G)$ satisfying

   $$
   |A_i\cap A_j|\le
   \begin{cases}
   3,& |A_i|=|A_j|=5,\\
   4,& \text{otherwise}.
   \end{cases}                                           \tag{2.1}
   $$

2. **Computer-assisted at the sharp bound:** there is an inclusion-minimal
   subfamily of $\mathcal F_6(G)$ with
   transversal number three and at most twenty-seven members. For every
   member $A$ of this subfamily there is a pair $\{p,q\}$, disjoint from
   $A$, that meets every other member.

3. If all three supports in (2.1) have order five, they are $K_5$
   subgraphs. Moreover, $\tau(\mathcal F_6(G))>2$ implies that $G$ is
   not two-apex, since an apex pair would meet every $K_5$-minor support.
   Theorem 1.10 of Niu--Zhang then gives a $K_7$ minor. Hence every
   unresolved triple contains at least one six-vertex model.

The private-pair and global support-height normalizations can now be made
simultaneously.  More precisely, one may choose a nonempty inclusion-minimal
family $\mathcal C\subseteq\mathcal F_6(G)-\mathcal F_5(G)$ whose addition
to the full family of $K_5$ subgraphs raises the transversal number above
two.  Every member of $\mathcal C$ has order six and has a private pair
$P$ which meets every $K_5$ subgraph and satisfies

$$
             \mu_G(P)=6=\max_{|R|=2}\mu_G(R),
$$

where $\mu_G(R)$ is the least support order of a $K_5$ model in $G-R$.
The elementary set-pairs argument bounds $|\mathcal C|$ by twenty-eight;
the audited nine-vertex finite closure sharpens this to twenty-seven.  Thus
the avoided support in the live private-pair branch may always be taken to
have order six.  This does not make the associated matching edges or
additional models compatible.

For a fixed deleted-family hypergraph, the graph whose edges are all
two-vertex transversals gives a sharper canonical alternative. It either
contains two disjoint edges, or it is a star or triangle whose vertex set
has order at most seven. In the first branch the two edges are globally
support-maximal private pairs for every support in the fixed exchange core.
In the second branch, seven-connectivity controls the graph after deletion
of the fixed locus; if an order-seven locus disconnects the graph, it is an
actual full order-seven boundary. Across the whole minimal critical family,
choosing one private pair per support gives the analogous
matching-or-small-kernel alternative, with at most six supports in the
nonmatching branch.

The five- and six-member star alternatives now have an explicit graph
normal form.  In the five-member case with a literal clique avoiding the
centre, the five critical supports produce five distinct distinguished
edges outside the leaf clique, including a disjoint pair; there is also a
second literal `K_5` disjoint from the leaf clique, and the complement of
the leaf clique is three-connected.  Contracting a disjoint pair and using
the rooted-`K_4` theorem turns failure of the paired repair into a small
separator or a planar cofacial quotient.  A simultaneous argument over all
five edges eliminates the planar alternative.  What remains is either an
actual order-seven separation, or an eight-vertex boundary with exactly two
full complementary components, a four-colourable induced boundary, and two
anticomplete distinguished edge branch sets.  In the six-member case,
compatible clique witnesses would invoke the existing one-split/two-clique
composition theorem.

There is also a parallel normalization. Every seven-connected graph either
has a $K_7$ minor or has a two-vertex set meeting every $K_5$ subgraph.
If the smallest $K_5$-minor model avoiding such a pair has order six, its
matching-edge contraction either remains seven-connected or expands a
six-vertex cut in the quotient to an order-seven separation of $G$. This
normalization supplies inputs to later composition arguments, but it does
not show that the pair meets every member of $\mathcal F_6(G)$.

No proved theorem allows the triple in (2.1) to be chosen with compatible
matching edges, with simultaneous contractions preserving
seven-connectivity, or with pairwise disjoint supports.

Sources:

- [three-support extraction](../results/hc7_support_at_most_six_separated_triple_extraction.md)
- [bounded critical support family](../results/hc7_support_six_bounded_critical_kernel.md)
- [private-pair extraction](../results/hc7_support_six_private_pair_v_extraction.md)
- [global maximal-pair/private-pair bridge](../results/hc7_maximal_support_pair_private_pair_bridge.md)
- [minimum-transversal graph of the fixed exchange core](../results/hc7_exchange_core_transversal_graph.md)
- [matching-or-small-kernel theorem for chosen private pairs](../results/hc7_private_transversal_graph_kernel.md)
- [five- and six-support star-kernel structure](../results/hc7_star_private_transversal_large_kernel.md)
- [rooted-four contraction and separator theorem](../results/hc7_star_kernel_rooted_four_contraction.md)
- [three-connectivity barrier for paired repair linkage](../barriers/hc7_five_defect_edges_three_connected_linkage_barrier.md)
- [single-pair planar obstruction](../barriers/hc7_star_kernel_contracted_root_planar_barrier.md)
- [four-connectivity-only paired-repair barrier](../barriers/hc7_four_connected_edge_rooted_pair_barrier.md)
- [the all-$K_5$-subgraph case](../results/hc7_one_split_two_clique_composition.md)
- [two-vertex transversal for $K_5$ subgraphs](../results/hc7_global_literal_k5_transversal.md)
- [normalization after contracting one matching edge](../results/hc7_global_support_six_contraction_dichotomy.md)

## 3. Proved composition cases

The following branches have complete conclusions under their stated extra
hypotheses.

1. Let $e$ be the matching edge of one six-vertex model. If $G/e$ is
   seven-connected and two-apex, the contraction can be expanded to obtain
   two vertices meeting every member of $\mathcal F_6(G)$. The proof uses
   the exclusion of a $K_4$-minor model on at most five vertices in a
   five-connected planar graph.

2. Suppose one six-vertex model and two $K_5$ subgraphs have compatible
   prescribed branch sets, and the three resulting $K_5$ subgraphs after
   contraction meet pairwise in at most three vertices. Then one obtains an
   explicit $K_7$-minor model, a two-vertex transversal of
   $\mathcal F_6(G)$, or an order-seven separation preserving the named
   model and boundary data. The last alternative still needs a strict
   induction parameter before it can be used recursively.

3. Three pairwise disjoint two-vertex branch sets attached to the same four
   singleton branch sets yield a $K_7$-minor model by a rooted-triangle
   construction.

4. Simultaneously contract the matching edges of three specified models.
   If the quotient is seven-connected, the three resulting $K_5$
   subgraphs give a $K_7$ minor whenever their union has at least twelve
   vertices, or whenever the quotient is non-two-apex and their pairwise
   intersections have order at most three.

5. **Computer-assisted:** if the family of exact six-vertex $K_5$-minor
   supports contained in one nine-vertex set has transversal number greater
   than two, then $G$ has a $K_7$ minor. The unique finite exception is
   $\overline{C_9}$, and seven-connectivity eliminates it. The theorem does
   not include five-vertex $K_5$ subgraphs. The computation has an
   independent replay.

6. Two disjoint small $K_5$-minor models yield five pairwise disjoint
   connected subgraphs with prescribed adjacencies. Separately, if the
   quotient obtained by contracting the three matching edges has a
   separator $T$ satisfying $|T|+\rho(T)=7$, expanding $T$ gives an
   order-seven separation preserving the three prescribed six-vertex
   models. These are useful composition inputs, but neither result supplies
   a compatible boundary colouring partition or a strict induction
   parameter.

Sources:

- [planar exclusion used in contraction expansion](../results/hc7_five_connected_planar_support_five_exclusion.md)
- [one six-vertex model and two $K_5$ subgraphs](../results/hc7_one_split_two_clique_composition.md)
- [simultaneous composition of specified models](../results/hc7_global_split_model_composition.md)
- [nine-vertex finite closure](../results/hc7_nine_vertex_support_six_closure.md)
- [five connected subgraphs from two models](../results/hc7_two_model_five_cluster.md)
- [order-seven separation preserving three models](../results/hc7_three_split_exact_separator_handoff.md)

These cases do not exhaust the triple produced by Section 2.

## 4. Three pairwise disjoint six-vertex models

Assume now that three specified supports are pairwise vertex-disjoint. Let
$F=\{e_1,e_2,e_3\}$ be their matching edges. Contract all three edges. If
the quotient remains seven-connected, the three resulting disjoint
$K_5$ subgraphs have union of order fifteen, so the published
three-clique theorem gives a $K_7$ minor.

Otherwise choose a nonempty inclusion-minimal set

$$
                         E\subseteq F
$$

such that $G/E$ is not seven-connected. Minimality is with respect to
loss of seven-connectivity; it is **not** a chromatic minimality condition.
The following conclusions are proved and internally audited.

- The case $|E|=3$ is eliminated by a marked Mader-type disjoint-path
  argument and explicit constructions preserving the three specified
  models.
- If $|E|=1$, expanding a minimum cut gives an order-seven separation of
  $G$ preserving the contracted model. No current theorem equips this
  separation with compatible colourings on both sides or a strict global
  induction parameter.
- If $|E|=2$, then $G/E$ is six-connected and every separation of
  order six contains both contracted vertices in its boundary. Expanding
  the two edges gives a boundary of order eight. Every component on either
  side has a neighbour at every boundary vertex, and the boundary graph is
  four-colourable. The four-colourability assertion is computer-assisted,
  with retained verification code and an independent replay.
- Three or more components in the quotient yield an explicit
  $K_7$-minor model. Thus the unresolved $|E|=2$ case has exactly two
  components.

Consequently this contraction analysis leaves exactly

$$
 \boxed{
 \begin{array}{l}
 \text{an order-seven separation without a strict induction parameter, or}\\
 \text{an inclusion-minimal two-edge contraction whose expansion has an}\\
 \text{eight-vertex, four-colourable boundary and a connected subgraph}\\
 \text{adjacent to every boundary vertex on each side.}
 \end{array}}
                                                               \tag{4.1}
$$

Four-colourability of the boundary does not imply that six-colourings of
the two sides induce the same boundary partition. For example,
$K_{3,5}$ has no proper four-colouring with four classes of size two.

A second proved construction contracts an inclusion-minimal forest inside
the two open sides until the quotient becomes five-colourable. Each
one-edge predecessor is exactly six-chromatic, and in every terminal
colouring each endpoint-side of a forest edge has a neighbour in every
nonassigned colour class. If deleting a contraction image lowers the
terminal graph to four colours, the rooted four-colour theorem gives a
$K_6$-minor model with the two forest sides as prescribed branch sets.
This does not yet supply a seventh branch set.

Two barriers delimit the conclusion:

- weighted cut size alone does not preserve the three labelled models; a
  fifteen-vertex counterexample has the required marked $K_5$ subgraphs,
  weighted cut order seven, and no $K_7$ minor;
- an unrooted $K_5$-minor model reconstructed after contraction does not
  preserve the branch
  sets needed for composition.

Sources:

- [minimal contraction alternatives](../results/hc7_three_split_minimal_bad_contraction.md)
- [closure of the three-edge contraction case](../results/hc7_three_split_marked_mader_branch_closure.md)
- [the eight-vertex boundary theorem](../results/hc7_two_full_shore_boundary_absorption.md)
- [forest-contraction colouring constraints](../results/hc7_minimal_contraction_forest_saturation.md)
- [weighted-cut counterexample](../barriers/hc7_decorated_hwege_genuine_cell_falsifier.md)

## 5. Proved bounded rooted-minor reductions

Fix a support $A$ in the minimal subfamily from Section 2 and a private
pair $\{p,q\}$. The extraction theorems produce one additional model
containing $p$ and another containing $q$. Either they give a
sufficiently separated triple, or the two additional supports share a
prescribed vertex set $X$, and further models are forced by replacing
vertices of $A\cap X$ with $p$ or $q$.

The following positive-intersection configurations have complete
conclusions. Each gives an explicit $K_7$-minor model. The finite interface
classifications used in several cases are computer-assisted and have
separate internal audits.

- $|A|=5$, for every possible nonempty intersection $A\cap X$.
- $|A|=6$, additional supports of order five with
  $|A\cap X|=4$.
- $|A|=6$, additional supports of order six with
  $|A\cap X|=5$.
- additional supports of order six with $|A\cap X|=4$, using a rooted
  five-terminal theorem and a hand classification of its residues.
- additional supports of order five with $|A\cap X|=3$, using a
  four-connected rooted clique-or-fan theorem.
- additional supports of order six with $|A\cap X|=3$, using the complete
  catalogue of rooted reductions on six terminals.
- additional supports of order five with $|A\cap X|=2$, using the same
  six-terminal catalogue.
- additional supports of order six with $|A\cap X|=2$, and additional
  supports of order five with $|A\cap X|=1$, using the complete catalogue
  of rooted reductions on seven terminals.

No theorem in this list eliminates $A\cap X=\varnothing$.  In the raw
catalogue those cases occur for either order of $A$.  In the globally
maximal private-pair normalization of Section 2, however, the avoided
support $A$ always has order six.  The live zero-intersection cases have
both additional models of order five or both of order six.  Among positive
intersections, the sole residue has all three models of order six and
$|A\cap X|=1$.

The six-terminal catalogue consists of 142 labelled minimal graphs on six
vertices and 780 irreducible graphs on seven vertices. The seven-terminal
catalogue consists of 5,495 labelled minimal graphs on seven vertices and
30,600 labelled order-eight templates. These are classifications of fixed
rooted interfaces, not bounds on the order of the ambient graph.

The analogous eight-terminal theorem is also proved: eight prescribed
vertices in a simple three-connected graph root one of three explicit
minor types. It does not close the remaining positive-intersection
configuration. **Computer-assisted barrier:** when all three models have
order six and $|A\cap X|=1$, one verified boundary pattern defeats every
choice of four vertices reserved outside a single rooted reduction. Independent explicit
branch-set enumeration and SMT verification agree. This refutes only the
single-interface composition strategy, not the desired transversal theorem.

Before applying these reductions, six-vertex supports containing a retained
five-vertex support must be deleted from the critical subfamily. This
pruning preserves its transversal number and ensures that every later
additional model belongs to the same irredundant family.

The extraction also forces a family of additional supports not visible in
the initial triple: for every two-set $R\subseteq A$ meeting
$A\cap X$, there is a support containing both $p$ and $q$ and avoiding
$R$. When the two original additional models have five vertices,
$pq\notin E(G)$, and each such
support is a six-vertex model in which exactly one of $p,q$ lies in the
two-vertex branch set. A proof must compose these two labelled orientations;
another reduction of intersection size is not a complete conclusion.

Principal sources:

- [dichotomy for models through a private pair](../results/hc7_private_pair_cross_arm_dichotomy.md)
- [replacement models sharing a prescribed vertex set](../results/hc7_rigid_cross_arm_double_root_cover.md)
- [exclusion of nonempty $A\cap X$ when $|A|=5$](../results/hc7_literal_cross_arm_overlap_elimination.md)
- [five-vertex additional models with $|A\cap X|=4$](../results/hc7_k4_two_vertices_one_edge_cycle_composition.md)
- [maximal intersection for six-vertex additional models](../results/hc7_cross_arm_maximal_order_six_overlap_elimination.md)
- [five-terminal rooted theorem](../results/hc7_five_terminal_rooted_fan.md)
- [six-vertex additional models with $|A\cap X|=4$](../results/hc7_cross_arm_overlap_four_cycle_decoder.md)
- [four-connected rooted clique-or-fan theorem](../results/hc7_four_connected_terminal_fan_or_k4.md)
- [five-vertex additional models with $|A\cap X|=3$](../results/hc7_overlap_three_five_good_decoder.md)
- [six-vertex additional models with $|A\cap X|=3$](../results/hc7_overlap_three_six_terminal_kernel_closure.md)
- [five-vertex additional models with $|A\cap X|=2$](../results/hc7_overlap_two_order_five_six_terminal_kernel_closure.md)
- [seven-terminal rooted classification](../results/hc7_seven_terminal_irreducible_kernel_classification.md)
- [six-vertex additional models with $|A\cap X|=2$](../results/hc7_overlap_two_order_six_seven_terminal_kernel_closure.md)
- [five-vertex additional models with $|A\cap X|=1$](../results/hc7_overlap_one_order_five_seven_terminal_kernel_closure.md)
- [eight-terminal rooted theorem](../results/hc7_eight_terminal_rooted_carrier_trichotomy.md)
- [barrier to one eight-terminal reduction](../barriers/hc7_overlap_one_exact_eight_kernel_bundle_barrier.md)

## 6. The two exact open problems

The intermediate theorem (1.1) has not been reduced solely to the
contraction alternatives in (4.1). Two independent obligations remain.

### 6.1 Label-preserving extraction and composition

Starting with the bounded exact-six family and its globally maximal private
pairs from Section 2, prove one of the following:

1. an explicit $K_7$-minor model in $G$;
2. two vertices meeting every member of $\mathcal F_6(G)$;
3. three pairwise vertex-disjoint six-vertex $K_5$-minor models with all
   prescribed branch sets retained; or
4. an order-seven separation preserving the specified models and boundary
   colouring partition and strictly decreasing a named induction parameter.

The unresolved shared-set configurations have $|A|=6$ and
$A\cap X=\varnothing$, with both additional models of order five or both
of order six, together with the all-six-vertex case $|A\cap X|=1$. The
separated triple from Section 2 is also unresolved. The
next argument must use several additional models simultaneously, their actual
branch sets, or proper-minor colouring transitions. The verified
eight-terminal barrier shows that one isolated rooted-minor classification
cannot suffice.

One-vertex replacements now preserve a canonical invariant.  After deleting
the chosen support `A`, let `H` consist of the remaining critical supports
and all literal `K_5` subgraphs.  The complement `Z_H` of the union of all
two-vertex transversals of `H` contains `A`, contains no literal `K_5`, and
contains every support onto which `A` may be rebased while preserving the
same complete family of private pairs.  Every first vertex outside `Z_H`
already belongs to a globally support-maximal private pair.  The missing
step is therefore label-preserving regeneration or a strict rank, not
another unnormalized one-vertex exchange.

The graph of all such pairs resolves that drift into two exact branches.
Either it gives two disjoint globally maximal pairs, in which case the
missing theorem is their label-preserving model composition, or all exits
from the exchange core lie in one fixed set of order at most seven. In the
latter branch, residual connectivity is known and an order-seven
disconnecting locus is already an actual full boundary. Across the full
critical family, failure of the disjoint-pair branch leaves only a star or
triangle kernel with at most six supports. Any further extraction must use
one of these two structures rather than enlarge the family of supports.

Source:

- [canonical one-vertex exchange core](../results/hc7_one_vertex_support_exchange.md)
- [minimum-transversal graph of the exchange core](../results/hc7_exchange_core_transversal_graph.md)
- [private-pair matching-or-small-kernel theorem](../results/hc7_private_transversal_graph_kernel.md)
- [five- and six-support star-kernel structure](../results/hc7_star_private_transversal_large_kernel.md)
- [rooted-four contraction and separator theorem](../results/hc7_star_kernel_rooted_four_contraction.md)
- [three-connectivity barrier for paired repair linkage](../barriers/hc7_five_defect_edges_three_connected_linkage_barrier.md)

### 6.2 Simultaneous composition after deleting three matching edges

Suppose three pairwise disjoint six-vertex models have been obtained. Let
$Q_i$ be the set of four singleton vertices of the $i$th model, let
$e_i=x_i y_i$ be its matching edge, and define

$$
                      F=\{e_1,e_2,e_3\},\qquad K=G-F.
$$

For a separation $(C,D)$ of $K$, put

$$
 \lambda_F(C,D)=|C\cap D|+
 |\{e\in F:e\text{ has one endpoint in each open side}\}|.       \tag{6.1}
$$

The following facts are proved and internally audited.

1. $\lambda_F$ is submodular, and seven-connectivity of $G$ gives
   $\lambda_F(C,D)\ge 7$ whenever both open sides are nonempty.
2. If $\kappa(K)=4$, the matching-edge endpoints lift a minimum
   separation to an order-seven separation of $G$ preserving all three
   models. At exact weighted order seven, after fixing two roots and the
   side assignment of every prescribed model, the cardinality of the
   anchored open side is a strict uncrossing parameter. This recursively
   eliminates the case.
3. Otherwise $\kappa(K)\ge 5$ and $\chi(K)\in\{5,6\}$.
4. For every nonempty $D\subseteq F$, some six-colouring $c$ of $K$
   satisfies

   $$
        D=\{x_i y_i\in F:c(x_i)=c(y_i)\}.                \tag{6.2}
   $$

   No six-colouring makes all three matching edges bichromatic.
5. For each $i$, there is an $x_i$-$y_i$ path in $K-Q_i$. The singleton
   branch sets indexed by $Q_i$, together with this path, form the
   prescribed $K_5$-minor model in $K$. The three paths need not be
   disjoint.
6. A missing-colour Kempe argument applied to a monochromatic matching edge
   gives either the required path or a two-colour component whose exchange
   produces another boundary equality pattern arising from a proper minor.
   The first exchange from the pattern in which all three edges are
   monochromatic decreases their number, but later exchanges may branch or
   cycle.

The missing theorem must combine these three paths and the two-colour
components to produce an explicit $K_7$-minor model, a global two-vertex
transversal, or an order-seven separation preserving the specified models
and boundary colouring partition with a strict named induction parameter.
A complementary contraction approach would instead resolve the two
alternatives in (4.1) without losing the prescribed branch sets or the
boundary colouring partition.

In the five-colour case, a colouring with exactly two monochromatic
matching edges has additional proved structure: the four endpoints induce
a $K_4$, every edge between the two pairs is locally double-critical, and
Menger's theorem gives either an order-seven separation preserving the two
named models or four disjoint paths between prescribed endpoint sets. A
specific four-connected test graph arising here is closed by a
**computer-assisted** finite construction over 4,096 minimal attachment
patterns. This verifies that test graph only; connectivity and the local
double-critical conditions do not settle the arbitrary residue.

Two common descriptions of the order-two residue have also been audited.
Terminal-edge contractions are principal restrictions of one represented
Mader delta-matroid, but ordinary symmetric exchange can leave every
restriction corresponding to an actual graph, and the endpoint system is
blind to same-model terminal edges.  Independently, Gallai--Edmonds theory
canonically reduces a deficient eight-vertex boundary complement to a set
of order at most two and at most four factor-critical components.  A static
state-realization example shows that this canonical matching data still
does not synchronize the two shore colourings.

Finally, a width-five quotient contains a disjoint six-vertex $K_5$ model,
a $K_6^-$, and six independent linking edges.  Hence the endpoint matching
of an arbitrary six-path linkage is insufficient.  Any positive linkage
theorem for the zero-intersection branch must choose the linkage extremally
and retain its bridges, producing either a label-preserving augmentation or
a separator of order at most six.

The endpoint labels are now classified exactly. The bare matching quotient
contains a $K_7$ minor unless the missing edge of the $K_6^-$ is paired with
a missing singleton--split-end edge of the six-vertex model. In the
canonical `3+1` form, clean augmentation and crossed attachment order both
give written explicit $K_7$ models. A single six-terminal test now replaces
the earlier pair of web certificates: twelve of its fifteen crossings give
explicit models, and the other three are exactly an `a3`--`x` repaired
contact paired with a `y`--`p`, `y`--`q`, or `y`--`r` path. A crossless
tuple has one auxiliary same-vertex web completion.

For a one-internal-vertex repaired contact, two proper-edge-deletion
colourings force a second `a3`--`x` path avoiding both repair edges and all
other original support vertices. If its off-skeleton interior meets the
`p`- or `q`-path, an explicit $K_7$ model results. The exceptional
`r`-intersection yields the actual boundary

$$
                  \{a_3,x,y,r,b_0,b_1,b_2\}.
$$

Both shores of this order-seven separation have full-subgraph packing number
one, because its boundary contains a literal `K_4`. Thus arbitrary return
order along the `y`--`r` path is no longer open. What remains is a bypass
which meets the linkage skeleton or avoids the second residual path, and
possible cycling of support replacements inside the canonical exchange
core.

The distinct `2+2` form has three clean augmenting classes and both crossed
linkage classes closed, together with two four-terminal web certificates.
A further unbounded class is closed: a path between the two unmatched
linkage paths whose interior avoids all six named paths produces an explicit
seven-branch-set `K_7` model. A corrected counterexample shows that these
three clean path patterns do not extract from every abstract terminal
crossing, so the remaining theorem must retain the full six-path bridge
structure.
A label-faithful six-terminal compression is still missing. Static
composition of two web certificates is false at connectivity three; a
direct-link quotient census finds no minimum-degree-seven counterexample,
so the next theorem must use host seven-connectivity rather than more
endpoint matching data.

In the canonical `3+1` form, broad attachment is no longer open.
**Computer-assisted finite interface:** a
connected subgraph outside the six named paths that is adjacent to the two
repaired-contact ends and five further normalized endpoints yields an
explicit `K_7` model. The same is true when its five further contacts lie
in five distinct linkage paths. Exact six-contact and once-subdivided
catalogues show that every surviving attachment pattern is concentrated on
only a few named paths. The residual problem is therefore ordered
first/last contact or a block-cutvertex separation, not another endpoint
count.

The concentration is exact for a component adjacent to `a3,x`: it cannot
meet the interiors of `P3` or `P4`, and all remaining contacts lie in one
of two displayed sectors, on `P5` or on `P0 union P1 union P2`. At eight
or more contacts, one named path has a nontrivial first--last interval.

The equality cases of that block--cutvertex analysis are proved without
finite enumeration. Every leaf-block interior of an off-linkage component
has at least six linkage neighbours; equality gives an actual order-seven
separation preserving all six paths. A cutvertex-free component has at
least seven linkage neighbours, again with the corresponding separation at
equality. Only strict excess remains in this branch.

An infinite two-fan barrier shows why strict excess is not itself a
descent parameter. Two distinct repaired-contact components can have
arbitrarily many first hits, and in six families both meet several linkage
paths, while the extracted graph is still `K_7`-minor-free. These graphs
are not seven-connected or contraction-critical. A positive theorem must
therefore use the additional host edges or proper-minor colouring
transitions, rather than only attachment count or first/last order.

The corresponding atomic calculation is complete. The local degree bound
and Dirac's inequality reduce the fan vertex to two degree-eight
neighbourhoods, but every Rolek--Song equality-case path pair for those
neighbourhoods already exists inside the same quotient. Thus these standard
local criticality inputs cannot replace the missing global composition.

A separate width-five example realizes two eight-contact components in
nested `P5` intervals and has connectivity exactly three. This fixes the
next unbounded target: use seven-connectivity to force a crossing of those
intervals, or return an actual order-seven separation preserving all six
named paths.

After deleting the nonadjacent private pair, criticality also gives exact
six-chromaticity, separately attained colour-dominating modes for the two
endpoints, a dominating $K_5$ model avoiding any prescribed remaining
vertex, and an unlabelled $K_6$ minor. A separate theorem excludes a fixed
pair whose deletion is $K_5$-minor-free when the disjoint $K_6^-$ and
$K_5$ supports are present. These facts constrain the branch but do not
align a regenerated model with the six linkage labels.

Sources:

- [weighted separation after deleting three edges](../results/hc7_matching_deletion_separator_lift.md)
- [Kempe transition for a missing colour](../results/hc7_missing_colour_matching_transition.md)
- [two-colour component alternative](../results/hc7_kempe_component_odd_cycle.md)
- [matching-edge equality patterns and the proved ranked-exchange sections](hc7_three_split_cross_star_ranked_exchange.md)
- [audit of the proved ranked-exchange sections](hc7_three_split_cross_star_ranked_exchange_audit.md)
- [two monochromatic matching edges](hc7_five_colour_exact_two_row_linkage.md)
- [finite construction for the four-connected test graph](../results/hc7_exact_two_four_gate_decoder.md)
- [barrier to composition from adjacency data alone](../barriers/hc7_four_edge_double_critical_packaging_barrier.md)
- [terminal-edge contraction projection](../results/hc7_mader_terminal_contraction_projection.md)
- [canonical Gallai--Edmonds boundary obstruction](../results/hc7_eight_boundary_gallai_edmonds.md)
- [barrier to arbitrary six-path composition](../barriers/hc7_disjoint_k6minus_support6_six_link_barrier.md)
- [exact label-preserving linkage classification](../results/hc7_disjoint_k6minus_support6_linkage_classifier.md)
- [clean augmentation and the two-web residue](../results/hc7_disjoint_k6minus_support6_bridge_augmentation.md)
- [six-terminal crossing decoder](../results/hc7_disjoint_k6minus_six_terminal_crossing_decoder.md)
- [minor-critical repaired-contact exchange](../results/hc7_repaired_contact_exchange.md)
- [exceptional intersection and normalized exact-seven separation](../results/hc7_repaired_contact_intersection.md)
- [seven-attachment and five-path-spread construction](../results/hc7_disjoint_k6minus_seven_attachment_decoder.md)
- [two-sector attachment concentration](../results/hc7_repaired_component_attachment_concentration.md)
- [leaf-block threshold and exact order-seven separation](../results/hc7_linkage_bridge_leaf_block_separation.md)
- [two-fan barrier to attachment-count descent](../barriers/hc7_repaired_contact_two_fan_barrier.md)
- [atomic Dirac/Rolek--Song escape barrier](../barriers/hc7_atomic_fan_dirac_rolek_barrier.md)
- [nested-interval barrier without seven-connectivity](../barriers/hc7_two_repaired_components_nested_interval_barrier.md)
- [`2+2` bridge augmentation and web certificates](../results/hc7_disjoint_k6minus_support6_two_two_bridge_augmentation.md)
- [`2+2` connector between the unmatched paths](../results/hc7_disjoint_k6minus_support6_two_two_connector.md)
- [barrier to extracting the three clean path patterns from every crossing](../barriers/hc7_two_two_three_pattern_extraction_barrier.md)
- [static two-web compatibility barrier](../barriers/hc7_two_web_static_compatibility_barrier.md)
- [colouring and minor regeneration after deleting the private pair](../results/hc7_nonadjacent_pair_colouring_regeneration.md)
- [fixed-pair exclusion for the disjoint models](../results/hc7_disjoint_k6minus_k5model_two_apex_exclusion.md)
- [single-bridge quotient barrier](../barriers/hc7_disjoint_k6minus_external_bridge_barrier.md)

## 7. What is and is not established

Established work closes several infinite configurations because fixed
rooted-minor theorems reduce arbitrary ambient graphs to finite interfaces.
It also eliminates the inclusion-minimal three-edge contraction case.

The following remain conjectural targets:

- the two-vertex transversal theorem (1.1);
- the label-preserving extraction theorem in Section 6.1; and
- the core-preserving repaired-contact exchange in Section 6.2;
- a label-faithful six-terminal compression of the `2+2` form; and
- the rest of the simultaneous-composition theorem in Section 6.2.

Finite catalogues do not prove any of these unbounded statements. A new
result should either eliminate an infinite family in Section 6, construct
an explicit $K_7$-minor model or global two-vertex transversal, or return
an order-seven separation preserving all named data and strictly decreasing
a declared induction parameter.
