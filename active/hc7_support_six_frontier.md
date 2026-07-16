# Technical frontier: a two-vertex transversal for small $K_5$ models

**Status:** active technical proof spine. Neither $HC_7$ nor the
intermediate transversal theorem below is proved.  See
[`../RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md) for the authoritative
status and
[`hc7_support_six_coverage_checkpoint.md`](hc7_support_six_coverage_checkpoint.md)
for the full dependency record.

## 1. Setup and intermediate target

Let $G$ be a seven-connected graph with $\chi(G)=7$, no $K_7$ minor, and
every proper minor six-colourable. For a minor model $M$, write $V(M)$ for
the union of its branch sets, and define

$$
 \mathcal F_6(G)=\{V(M):M\text{ is a }K_5\text{-minor model and }
 |V(M)|\le6\}.
$$

The current intermediate target is

$$
                            \tau(\mathcal F_6(G))\le2.       \tag{1.1}
$$

A six-vertex $K_5$ model has four singleton branch sets forming a $K_4$
and one two-vertex branch set. We write that branch set as $\{x_i,y_i\}$
and its edge as $e_i=x_i y_i$.

A successful recursive reduction must return a separation of the original
graph $G$ of order seven, preserve every specified branch set and boundary
colouring partition, and strictly decrease an explicitly named induction
parameter.  Merely finding another order-seven separator is not sufficient.

Two problems remain.

## 2. Label-preserving extraction of compatible $K_5$ models

Assume for contradiction that $\tau(\mathcal F_6(G))>2$.  The proved extraction
theorems give:

- an inclusion-minimal family $\mathcal C$ of at most twenty-seven
  **exactly six-vertex** supports such that adjoining $\mathcal C$ to the
  full family of literal $K_5$ subgraphs raises the transversal number
  above two;
- for each $A_i\in\mathcal C$, a **private pair** $P_i=\{p_i,q_i\}$ which
  avoids $A_i$, meets every other member of $\mathcal C$, and meets every
  literal $K_5$ in $G$;
- the global normalization

  $$
             \mu_G(P_i)=6=\max_{|P|=2}\mu_G(P),
  $$

  where $\mu_G(P)$ is the minimum support order of a $K_5$ model in
  $G-P$;
- for each fixed $i$, one prescribed $K_5$ model containing exactly
  $p_i$ from $P_i$ and another containing exactly $q_i$, both meeting
  $A_i$ in at most four vertices; and
- independently, three supports $A_1,A_2,A_3$ satisfying

  $$
  |A_i\cap A_j|\le
  \begin{cases}
  3,&|A_i|=|A_j|=5,\\
  4,&\text{otherwise}.
  \end{cases}                                           \tag{2.1}
  $$

If all three supports have order five, they are $K_5$ subgraphs.  Moreover,
$\tau(\mathcal F_6(G))>2$ implies that $G$ is not two-apex, since an
apex pair would meet every $K_5$-minor support.  Theorem 1.10 of
Niu--Zhang then gives a $K_7$ minor.  Thus an unresolved triple contains
at least one six-vertex model.

The additional-model dichotomy has two outcomes:

1. three labelled models are sufficiently separated; or
2. the models containing $p$ and $q$ share a prescribed vertex set
   $X$,
   and criticality forces further replacement models obtained by replacing
   a vertex of $A\cap X$ with $p$ or $q$.

In the shared-set outcome, $A\cap X$ must be empty if $|A|=5$; this does
not eliminate the disjoint case. If $|A|=6$ and the two additional models
have five vertices, explicit minor constructions and bounded rooted-minor
reductions eliminate every positive value of $|A\cap X|$. If all three
models have six vertices, they eliminate $2\le |A\cap X|\le5$. The
globally normalized kernel always has $|A|=6$. Its unresolved
configurations are:

- the separated labelled triple;
- every shared-set outcome with $A\cap X=\varnothing$ and both additional
  models of the same order, five or six; and
- the shared-set outcome in which all three models have six vertices and
  $|A\cap X|=1$.

For either configuration, the required conclusion is one of:

- an explicit $K_7$-minor model in $G$;
- two vertices meeting every support in $\mathcal F_6(G)$;
- three vertex-disjoint six-vertex $K_5$ models with all prescribed branch
  sets retained; or
- a model-preserving order-seven separation with a strict induction
  parameter.

A complete classification of one eight-terminal rooted-minor interface is
not enough: a verified finite boundary pattern defeats every choice of four
vertices held outside that reduction.  The next proof must therefore retain
information shared by models constructed after several different
contractions, or by the ambient contraction sequence.

Principal inputs:

- [global maximal-pair/private-pair bridge](../results/hc7_maximal_support_pair_private_pair_bridge.md)
- [bounded critical support family](../results/hc7_support_six_bounded_critical_kernel.md)
- [private-pair extraction](../results/hc7_support_six_private_pair_v_extraction.md)
- [dichotomy for models through a private pair](../results/hc7_private_pair_cross_arm_dichotomy.md)
- [replacement models sharing a prescribed vertex set](../results/hc7_rigid_cross_arm_double_root_cover.md)
- [exclusion of nonempty $A\cap X$ when $|A|=5$](../results/hc7_literal_cross_arm_overlap_elimination.md)
- [closure for five-vertex additional models with $|A\cap X|=4$](../results/hc7_k4_two_vertices_one_edge_cycle_composition.md)
- [maximal intersection for six-vertex additional models](../results/hc7_cross_arm_maximal_order_six_overlap_elimination.md)
- [rooted five-terminal theorem](../results/hc7_five_terminal_rooted_fan.md)
- [rooted eight-terminal theorem](../results/hc7_eight_terminal_rooted_carrier_trichotomy.md)
- [barrier to a single eight-terminal reduction](../barriers/hc7_overlap_one_exact_eight_kernel_bundle_barrier.md)

## 3. Simultaneous composition after deleting three branch-set edges

Suppose the extraction problem yields three vertex-disjoint six-vertex
$K_5$ models.  For $i=1,2,3$, let $Q_i$ be the set of four singleton
vertices inducing the model's $K_4$, let $e_i=x_i y_i$ be the edge in the
two-vertex branch set, and put

$$
                         F=\{e_1,e_2,e_3\},\qquad K=G-F.
$$

For a separation $(A,B)$ of $K$, define

$$
 \lambda_F(A,B)=|A\cap B|+
 |\{e\in F:e\text{ has endpoints in opposite open sides of }(A,B)\}|.
                                                               \tag{3.1}
$$

The following are proved.

1. $\lambda_F$ is submodular, and seven-connectivity of $G$ gives
   $\lambda_F(A,B)\ge7$ whenever both open sides are nonempty.
2. If $K$ has connectivity four, endpoint choices for the matching edges
   lift to a separation of $G$ of order seven preserving all three named
   models.  At exact weighted order seven, after fixing two roots and the
   side assignment of every prescribed model, the cardinality of the
   anchored open side is a strict uncrossing parameter; this eliminates the
   case recursively.
3. Otherwise $K$ is at least five-connected and $\chi(K)$ is five or six.
4. For every nonempty $D\subseteq F$, there is a six-colouring $c$ of $K$
   such that

   $$
                 D=\{x_i y_i\in F:c(x_i)=c(y_i)\}.       \tag{3.2}
   $$

   No six-colouring makes all three matching edges bichromatic.
5. For each $i$, connectivity gives an $x_i$-$y_i$ path in
   $K-Q_i$.  The singleton branch sets $\{q\}$ for $q\in Q_i$, together
   with this path as the fifth branch set, form the prescribed $K_5$ model
   in $K$.  The three paths may intersect.
6. From a colouring satisfying (3.2) and a monochromatic edge $e_i$, the
   colour missing from $Q_i$ gives either the required $x_i$--$y_i$ path or a
   two-colour component whose Kempe exchange produces another equality set
   arising from a proper minor. The first such move from $D=F$ decreases
   $|D|$, but later moves may branch or cycle.

The open theorem must combine the three paths constructing the prescribed
models and the
two-colour components into one of:

- an explicit $K_7$-minor model;
- two vertices meeting every $K_5$-model support in $G$; or
- a model-preserving order-seven separation with a strict induction
  parameter.

Colouring patterns alone cannot prove this: their transition graph need not
be acyclic, and reconstructing an unrooted minor after contraction does not
preserve the four specified singleton branch sets.

There is a complementary contraction formulation.  A nonempty
inclusion-minimal subset of the three edges whose simultaneous contraction
is not seven-connected cannot have order three; that entire case is
eliminated by a Mader-type disjoint-path argument and labelled separator
constructions.  What remains is either:

- an order-seven separation not yet equipped with a strict parameter; or
- an inclusion-minimal two-edge set whose simultaneous contraction is not
  seven-connected and whose expansion has an eight-vertex boundary.  On
  each side of that boundary is a connected
  subgraph adjacent to every boundary vertex, and the boundary graph is
  four-colourable. The four-colourability assertion is a computer-assisted
  finite result with retained verification code and an independent replay.

Four-colourability does not ensure that colourings of the two sides induce
the same boundary partition.  This compatibility problem is part of the
same simultaneous-composition theorem.

Two additional common descriptions are now proved, with sharp limitations.

1. The Mader endpoint delta-matroids before and after contracting either
   named edge are principal restrictions of one represented delta-matroid.
   Generic exchange can leave every graph-realizable restriction, and the
   endpoint system is invariant under changes to the same-model terminal
   edges that carry the labelled `K_5` data.
2. If the complement of the eight-vertex boundary has no perfect matching,
   its Gallai--Edmonds decomposition has a canonical barrier of order at
   most two and at most four factor-critical deficient components. A
   seven-connected exact-state realization shows that this canonical
   matching structure and the two named boundary-edge transitions still do
   not align the shore colourings without additional global or labelled
   input.

There is also an explicit width-five quotient consisting of a disjoint
six-vertex `K_5` model and a `K_6^-` joined by a perfect matching. Thus six
arbitrary disjoint linking paths do not close the zero-overlap rigid case.
An exact finite classification now proves that the quotient contains a
`K_7` minor unless the missing edge of the `K_6^-` is matched to a missing
singleton--split-end edge of the six-vertex model. Hence the remaining
linkages have a prescribed label alignment rather than an arbitrary
endpoint permutation.

For the canonical `3+1` contact form, a clean external path to any of the
three nonexceptional linkage paths produces an explicit `K_7` model. Two
external paths with crossed attachment order on either exceptional linkage
path do the same. If neither construction occurs, two cleaned host graphs
have Humeau--Pous four-web completions whose frames share the remaining
linkage path. The completion edges are auxiliary and need not agree between
the two webs.

The immediate constructive target is therefore a **two-web composition
theorem**: prove that the two certificates either force a genuine crossing
in one host graph or expose an order-seven separation preserving the named
models and decreasing a strict parameter. The `2+2` contact form must be
reduced to this theorem or supplied with an analogous bridge construction.
Counting attachments or contracting an external component is insufficient;
the retained first-hit vertices and their order along the linkage paths are
essential.

Criticality supplies additional, deliberately secondary data. For the
nonadjacent private pair `P={p,q}`, the graph `G-P` is exactly
six-chromatic; each endpoint is colour-dominating in a separately attained
six-colouring; `G-P-v` has a dominating `K_5` model for every `v`; and
`G-P` has a `K_6` minor. These models are unlabelled. Moreover, in the
present disjoint-support configuration no pair can leave a
`K_5`-minor-free remainder. Thus the usual fixed-pair terminal would close
this branch only by contradiction, not by providing its missing model
alignment.

Principal inputs:

- [weighted separation theorem](../results/hc7_matching_deletion_separator_lift.md)
- [Kempe transition theorem](../results/hc7_missing_colour_matching_transition.md)
- [two-colour component alternative](../results/hc7_kempe_component_odd_cycle.md)
- [matching-edge equality patterns and proved ranked-exchange sections](hc7_three_split_cross_star_ranked_exchange.md)
- [audit of the proved ranked-exchange sections](hc7_three_split_cross_star_ranked_exchange_audit.md)
- [minimal contraction alternatives](../results/hc7_three_split_minimal_bad_contraction.md)
- [closure of the three-edge contraction case](../results/hc7_three_split_marked_mader_branch_closure.md)
- [eight-vertex boundary absorption](../results/hc7_two_full_shore_boundary_absorption.md)
- [terminal-edge projection in the Mader delta-matroid](../results/hc7_mader_terminal_contraction_projection.md)
- [canonical Gallai--Edmonds boundary barrier](../results/hc7_eight_boundary_gallai_edmonds.md)
- [barrier to endpoint-only delta-matroid exchange](../barriers/hc7_mader_delta_legal_slice_exchange_barrier.md)
- [barrier to static Gallai--Edmonds state transfer](../barriers/hc7_eight_boundary_gallai_state_transfer_barrier.md)
- [barrier to arbitrary six-path composition](../barriers/hc7_disjoint_k6minus_support6_six_link_barrier.md)
- [exact label-preserving linkage classification](../results/hc7_disjoint_k6minus_support6_linkage_classifier.md)
- [bridge augmentation and two-web residue](../results/hc7_disjoint_k6minus_support6_bridge_augmentation.md)
- [colouring and minor regeneration](../results/hc7_nonadjacent_pair_colouring_regeneration.md)
- [fixed-pair exclusion in the disjoint-model configuration](../results/hc7_disjoint_k6minus_k5model_two_apex_exclusion.md)
- [barrier to a single contracted external bridge](../barriers/hc7_disjoint_k6minus_external_bridge_barrier.md)

## 4. Strong Hadwiger for four colours in the order-two case

Let $J$ be a graph with an edge $uv$ such that

$$
               \chi(J)=k+2,\qquad \chi(J-\{u,v\})\le k.
$$

Set $H=J-\{u,v\}$ and $X=N_J(u)\cap N_J(v)$. Then $\chi(H)=k$, and every
proper $k$-colouring of $H$ uses all $k$ colours on $X$. Strong Hadwiger's
Conjecture says that if $\chi(H)=k$ and $X$ receives all $k$ colours in
every proper $k$-colouring of $H$, then $H$ has a $K_k$-minor model in
which every branch set meets $X$. Martinsson--Steiner prove this statement
for $k=4$. Applying it here gives a $K_6$-minor model with singleton branch
sets $\{u\}$ and $\{v\}$ in the relevant contracted graph, but it does not
by itself produce a seventh branch set in $G$.

## 5. Admission rule for new work

Do not add another finite neighbourhood classification, attachment
catalogue, or unranked separator to the active spine.  A new result should
either:

- eliminate an infinite family in one of Sections 2 or 3;
- construct an explicit $K_7$-minor model or global two-vertex transversal;
  or
- produce a model-preserving order-seven separation with a named strict
  parameter.

On the current zero-overlap branch, a linkage theorem is admissible only if
it retains the actual bridge attachments of an extremal linkage. A theorem
about its endpoint matching alone is false. The declared live measure for a
two-web reduction must count a host object—such as the interior of a named
linkage interval or a model-preserving side of an actual separation—not
auxiliary web-completion edges.

Historical theorem filenames retain some former project shorthand for
provenance.  New statements and link descriptions should follow the
standard-language policy in [`../AGENTS.md`](../AGENTS.md).
