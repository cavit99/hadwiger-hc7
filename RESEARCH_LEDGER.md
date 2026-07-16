# $HC_7$ research ledger

**Last updated:** 16 July 2026
**Authoritative status:** $HC_7$ is not proved here.

This file records the current mathematical dependency chain.  The more
detailed claim-by-claim map is
[`active/hc7_support_six_coverage_checkpoint.md`](active/hc7_support_six_coverage_checkpoint.md),
and the concise list of live files is [`active/INDEX.md`](active/INDEX.md).
If an archived note conflicts with this ledger, this ledger governs the
current programme.

## 1. Counterexample framework

Suppose that $G$ is a minor-minimal counterexample to $HC_7$.  The programme
uses the following standard consequences:

- $\chi(G)=7$ and $G$ has no $K_7$ minor;
- every proper minor of $G$ is six-colourable; and
- $G$ is seven-connected.

A minor model's **support** is the union of its branch sets.  A
**six-vertex $K_5$ model** is necessarily a $K_5$-minor model with four
singleton branch sets and one two-vertex branch set; the latter is called
the model's two-vertex branch set below.

Let

$$
 \mathcal F_6(G)=\{V(M):M\text{ is a }K_5\text{-minor model using at most
 six vertices}\}.
$$

The first intermediate theorem sought is

$$
                         \tau(\mathcal F_6(G))\le2.       \tag{1}
$$

Even (1) is only the first extension step.  The final argument must produce
two vertices meeting the support of every $K_5$-minor model in $G$.  Deleting
such a pair leaves a $K_5$-minor-free graph; the known $t=5$ case then gives
a four-colouring, and two additional colours finish $G$.

## 2. Established dependency chain

The following statements have written proofs in the repository.  Many have
separate internal audit notes; those audits are not external peer review.
Items explicitly marked **computer-assisted** depend on a finite exhaustive
classification or computation as well as a written reduction.

1. **Bounded critical family (computer-assisted at the sharp bound).**  If
   (1) fails, there is an inclusion-minimal
   subfamily of at most twenty-seven supports with transversal number three.
   Each member has a private two-vertex transversal for the other members.
   The bound twenty-seven uses the verified nine-vertex support
   classification; the hand Bollobás set-pairs argument gives twenty-eight.

2. **Three-model extraction.**  Three supports can be selected with pairwise
   intersection at most three when both have order five, and at most four
   otherwise.  If all three are five-vertex $K_5$ subgraphs, existing
   clique-minor results give a $K_7$ minor.  Here
   $\tau(\mathcal F_6(G))>2$ first implies that $G$ is not two-apex,
   because an apex pair would meet every $K_5$-minor support; Theorem 1.10
   of Niu--Zhang then applies.  Thus every unresolved selection contains a
   six-vertex $K_5$ model.

3. **Label-preserving additional models.**  For each private pair
   $\{p,q\}$, the criticality argument produces one prescribed $K_5$
   model containing $p$ and another containing $q$.  The corrected
   dichotomy either separates three labelled models sufficiently, or
   produces two models sharing a prescribed vertex set $X$, together with
   specified replacement models.  Several maximal-intersection
   configurations are eliminated by explicit $K_7$-minor constructions.

4. **Rooted-minor compression.**  Prescribed terminals in a three-connected
   graph can be retained while contracting to a bounded three-connected
   rooted minor.  The five-terminal case has a hand classification; the
   six-, seven-, and eight-terminal interfaces used here have finite
   classifications and retained verification code.

5. **Eliminated shared-set configurations (partly computer-assisted).**
   In the shared-set outcome of item 3, $A\cap X$ must be empty if
   $|A|=5$; this is a restriction, not an elimination of the disjoint case.
   If $|A|=6$ and the two additional models have five vertices, every
   positive value of $|A\cap X|$ is eliminated. If all three models have
   six vertices, the cases $2\le |A\cap X|\le5$ are eliminated.
   The finite compositions have retained scripts and separate internal
   audits or replays.  This does not close the separated-labelled-triple
   outcome. The shared-set residue consists of every case with
   $A\cap X=\varnothing$, together with the all-six-vertex case
   $|A\cap X|=1$.

6. **Weighted separation function.** For three disjoint six-vertex $K_5$
   models, let $e_i=x_i y_i$ be the edge spanning the two-vertex branch set
   of model $i$, put $F=\{e_1,e_2,e_3\}$, and let $K=G-F$. The function

   $$
      \lambda_F(A,B)=|A\cap B|+
      |\{e\in F:e\text{ has endpoints in opposite open sides of }(A,B)\}|
   $$

   is submodular.  Seven-connectivity of $G$ implies
   $\lambda_F(A,B)\ge7$ for every separation of $K$ with both open sides
   nonempty.  For exact weighted order seven, after fixing two roots and the
   side assignment of every prescribed model, the cardinality of the
   anchored open side is a well-founded rank under uncrossing.

7. **Connectivity-four case.**  If $K$ has a separation of order four, the
   endpoint choices of the crossing matching edges lift to a separation of
   $G$ of order seven that preserves the prescribed models.  The anchored
   open-side cardinality above closes the connectivity-four case by a strict
   reduction.

8. **Common-deletion colouring patterns.**  If the connectivity-four
   reduction is unavailable, $K$ is at least five-connected and has
   chromatic number five or six. Every nonempty subset of $F$ occurs as
   exactly the set of matching edges whose endpoints receive the same colour
   in a six-colouring of $K$; no colouring makes all three edges bichromatic.

9. **Construction of each prescribed rooted model in the common graph.**
   Let $Q_i$ be the four singleton vertices of model $i$. For each $i$,
   $Q_i$ induces a prescribed $K_4$, and $K-Q_i$ contains an
   $x_i$--$y_i$ path. The singleton branch sets indexed by $Q_i$, together
   with this path, form a $K_5$-minor model in $K$, but the three paths may
   intersect.

10. **Kempe-component alternative.**  For any specified equality pattern
    and any monochromatic matching edge $e_i$, the colour missing from its
    prescribed $K_4$ yields either the required path or a two-colour component
    whose Kempe exchange produces another legal equality pattern arising
    from a proper minor.  The first move from the all-monochromatic pattern
    decreases the number of monochromatic matching edges, but later moves
    can branch or cycle.

11. **Three-edge contraction case.**  Contracting all three matching edges
    gives three disjoint $K_5$ subgraphs with specified contracted vertices.
    A Mader-type disjoint-path argument, followed by labelled separator
    constructions, excludes the entire case in which all three edges form an
    inclusion-minimal set whose simultaneous contraction destroys
    seven-connectivity.  This is an infinite-family result, not merely a
    finite enumeration.

12. **Global maximal-pair/private-pair bridge.** Under the contradictory
    assumption $\tau(\mathcal F_6(G))>2$, there is an inclusion-minimal family of at
    most twenty-seven exact six-vertex supports over the full family of
    literal $K_5$ subgraphs. Every support $A_i$ in this family has a
    private pair $P_i$ which meets every literal $K_5$, avoids $A_i$, and
    satisfies

    $$
          \mu_G(P_i)=6=\max_{|P|=2}\mu_G(P).
    $$

    Thus the global support-height normalization and labelled private-pair
    extraction can be imposed simultaneously. Equivalently,
    $\tau(\mathcal F_6(G))>2$ if and only if the maximum support height is six.
    Producing a pair of height at least seven is already the intermediate
    transversal theorem, not a smaller monotone step.

13. **Common representation for terminal-edge contractions.** If an edge
    joins two terminals in one part of a Mader network, contracting it is
    represented by replacing the two terminal columns of a skew matrix by
    one generic linear combination. Pairwise disjoint contractions admit
    one master representation whose legal principal restrictions give all
    predecessor endpoint delta-matroids. Ordinary symmetric exchange need
    not stay in those legal restrictions. More decisively, the endpoint
    system is invariant under every change to terminal--terminal edges
    within one part, so it cannot record the designated $K_4$, split edge,
    same-model paths, or deletion-colouring data.

14. **Canonical order-eight matching obstruction.** For an eight-vertex
    boundary $J$, put $F=\overline J$. If $I_2\vee J$ has no $K_7$ minor and
    $F$ has no perfect matching, the Gallai--Edmonds set $A(F)$ has order at
    most two and $F[D]$ has at most four factor-critical components. The
    possible pairs $(|A|,o(F-A))$ are $(0,2),(0,4),(1,3),(2,4)$. This
    canonicalizes the earlier Tutte witness but does not align the two
    shore colouring languages. An exact state-realization barrier shows
    that the canonical decomposition, two named edge transitions,
    independent-block responses, seven-connectivity, and the target-free
    quotient remain insufficient without global minor exclusion or further
    labelled branch-set data.

15. **Exact six-linkage alignment and a bridge/web dichotomy.** In the
    zero-intersection branch with a six-vertex $K_5$ model and a disjoint
    $K_6^-$, contract six disjoint linking paths to a perfect matching.
    A complete finite classification proves that the resulting
    twelve-vertex quotient has a $K_7$ minor unless the missing edge of
    the $K_6^-$ is matched to a missing singleton--split-end edge of the
    six-vertex model. Thus every surviving matching aligns two labelled
    nonedges; arbitrary endpoint permutations are no longer a residue.

    For the canonical $3+1$ contact form, a clean path from the remaining
    split-end linkage path to any of three specified linkage paths gives
    seven explicit branch sets. Seven-connectivity therefore forces either
    a $K_7$ minor or a separator relation through the two exceptional
    linkage paths after deleting six named vertices. A one-vertex minimum
    separator in that relation lifts to an actual order-seven separation.
    Two crossed bridges on either exceptional cycle transpose the aligned
    endpoints and again give an explicit $K_7$ model. Finally, the
    Generalised Two Paths Theorem gives a precise structural residue: in a
    $K_7$-minor-free host, two cleaned graphs have four-web completions with
    frames sharing the remaining linkage path.

    The two completion edge sets are not host edges and need not agree.
    Their compatibility or exclusion is the live unbounded problem on this
    branch. A separate exact quotient calculation also shows why attachment
    count alone cannot replace it: one connected contracted bridge with
    seven or eight quotient neighbours can remain nonrepairing in two
    labelled eight-vertex frames. This quotient statement does not lift
    through nontrivial linkage paths without preserving distinct first-hit
    vertices.

    Minor-criticality supplies two further constraints on this branch. If
    the private pair is nonadjacent, its deletion is exactly six-chromatic;
    each endpoint is colour-dominating in a separately attained
    six-colouring; a dominating $K_5$ model can be regenerated while
    avoiding any prescribed remaining vertex; and the deletion contains an
    unlabelled $K_6$ minor. Conversely, seven-connectivity and the disjoint
    $K_6^-$ and $K_5$ supports exclude any fixed pair whose deletion is
    $K_5$-minor-free. Neither statement preserves the linkage labels, so
    both are constraints on the two-web composition problem rather than a
    solution of it.

16. **One six-terminal test replaces the first two-web compatibility
    problem.**  In the canonical `3+1` form, apply the Generalised Two
    Paths Theorem to the ordered tuple

    $$
                         (a_3,y,x,q,r,p).
    $$

    Of the fifteen possible crossing types, twelve give explicit
    `K_7`-minor models.  The exact three survivors are

    $$
              (a_3x,yq),\qquad(a_3x,yr),\qquad(a_3x,yp).
    $$

    All three endpoint quotients, and the graphs obtained by subdividing
    both crossing edges once, are `K_7`-minor-free; thus these are genuine
    repaired-contact residues rather than omissions in the decoder.  If
    the six-terminal tuple is crossless, it has one same-vertex web
    completion.  The completion edges remain auxiliary, but the earlier
    pair of unrelated four-web completions is no longer the active
    obstruction.

    An endpoint-preserving stable rerouting of the six linkage paths makes
    every nontrivial bridge attach to at least two paths.  Every exterior
    bridge component then has at least seven skeleton attachments; exactly
    seven give an actual order-seven separation.  In a `K_7`-minor-free
    host no such component can attach both to the `y`--`r` path away from
    `y` and to one of the first three linkage paths away from its right
    endpoint.

    The distinct `2+2` contact form has also been advanced without
    identifying it with `3+1`: three clean augmenting-path classes and
    both crossed-linkage classes give explicit `K_7` models, the latter
    using a rooted-`K_4` cycle-linkage theorem.  Its remaining residue is
    two four-terminal web certificates sharing one linkage path.  A
    label-faithful six-terminal lift for this form is still open.

17. **A fixed support-exchange core.**  Delete one support `A` from a
    minimal exact-six critical family and let `H` be the remaining family
    together with all literal `K_5` subgraphs.  Then `tau(H)=2`.  If
    `T(H)` is the family of all two-vertex transversals of `H`, define

    $$
       Z_H=V(G)-\bigcup_{R\in T(H)}R.
    $$

    The support `A` lies in `Z_H`, and `G[Z_H]` contains no literal
    `K_5`.  Every exact six-vertex `K_5`-model support contained in `Z_H`
    may replace `A` while preserving **every** pair in `T(H)` as a private
    transversal.  Conversely, every vertex outside `Z_H` already belongs
    to a globally support-maximal private pair.  This is the first fixed
    global invariant for repeated one-vertex support replacements: private
    pairs can no longer drift arbitrarily.  It does not yet make the
    replacement graph acyclic or preserve a chosen six-linkage.

18. **Minor-critical repair and the exceptional intersection.**  A
    one-internal-vertex `a_3`--`x` repair replaces one vertex of the
    six-vertex support and admits two labelled `K_5` decompositions.
    Colourings after deleting its two edges force a second `a_3`--`x`
    path which avoids both edges and all other vertices of the original
    support.  This is a genuine palette-to-labelled-interface statement,
    although the new path may meet the linkage skeleton.

    If this simultaneous bypass meets the residual `y`--`p` or
    `y`--`q` path in one exterior component, an explicit `K_7` model
    results.  In the exceptional `y`--`r` case, all additional normalized
    endpoint contacts and all interior linkage-path contacts except those
    on the `y`--`r` path are likewise closed by explicit models.  The
    remaining component produces the actual order-seven boundary

    $$
                 X_7=\{a_3,x,y,r,b_0,b_1,b_2\}.
    $$

    Since `X_7` contains the clique
    `\{r,b_0,b_1,b_2\}`, the exact-seven packing theorem forces both open
    shores to have full-subgraph packing number exactly one.  Thus the
    unbounded attachment-order residue on the `y`--`r` path has been
    replaced by a normalized `(1,1)` exact-seven separation.  The still
    open cases are a bypass which meets the linkage skeleton before the
    residual path, a bypass disjoint from that path, or a sequence of
    support replacements inside `Z_H` with no strict rank.

    A sharp static barrier confirms that two web certificates and one
    bridge in each exceptional class do not suffice without high
    connectivity.  The examples have connectivity three.  Conversely, an
    exhaustive direct-link quotient search finds no `K_7`-free completion
    of minimum degree seven, supporting the use of seven-connectivity as
    the missing host-level input rather than further endpoint casework.

The most recent end-to-end composition theorem in item 11 is
[`hc7_three_split_marked_mader_branch_closure.md`](results/hc7_three_split_marked_mader_branch_closure.md),
with its adjacent audit.  The weighted separation and Kempe-component inputs
are recorded in
[`hc7_matching_deletion_separator_lift.md`](results/hc7_matching_deletion_separator_lift.md),
[`hc7_missing_colour_matching_transition.md`](results/hc7_missing_colour_matching_transition.md),
and [`hc7_kempe_component_odd_cycle.md`](results/hc7_kempe_component_odd_cycle.md).
The direct source for the common-deletion chromatic statement and all seven
nonempty matching-edge equality patterns is Sections 7--8 of
[`hc7_three_split_cross_star_ranked_exchange.md`](active/hc7_three_split_cross_star_ranked_exchange.md),
with its [separate internal audit](active/hc7_three_split_cross_star_ranked_exchange_audit.md).
The new global normalization is
[`hc7_maximal_support_pair_private_pair_bridge.md`](results/hc7_maximal_support_pair_private_pair_bridge.md).
The algebraic projection and canonical boundary obstruction are respectively
[`hc7_mader_terminal_contraction_projection.md`](results/hc7_mader_terminal_contraction_projection.md)
and
[`hc7_eight_boundary_gallai_edmonds.md`](results/hc7_eight_boundary_gallai_edmonds.md),
each with an adjacent audit.
The exact linkage classification and the constructive bridge/web theorem
are
[`hc7_disjoint_k6minus_support6_linkage_classifier.md`](results/hc7_disjoint_k6minus_support6_linkage_classifier.md)
and
[`hc7_disjoint_k6minus_support6_bridge_augmentation.md`](results/hc7_disjoint_k6minus_support6_bridge_augmentation.md),
again with adjacent audits.
The six-terminal compression, fixed support-exchange core, repaired-contact
colouring theorem, exceptional-intersection theorem, and the independent
`2+2` bridge theorem are respectively
[`hc7_disjoint_k6minus_six_terminal_crossing_decoder.md`](results/hc7_disjoint_k6minus_six_terminal_crossing_decoder.md),
[`hc7_one_vertex_support_exchange.md`](results/hc7_one_vertex_support_exchange.md),
[`hc7_repaired_contact_exchange.md`](results/hc7_repaired_contact_exchange.md),
[`hc7_repaired_contact_intersection.md`](results/hc7_repaired_contact_intersection.md),
and
[`hc7_disjoint_k6minus_support6_two_two_bridge_augmentation.md`](results/hc7_disjoint_k6minus_support6_two_two_bridge_augmentation.md).
The two secondary criticality constraints are
[`hc7_nonadjacent_pair_colouring_regeneration.md`](results/hc7_nonadjacent_pair_colouring_regeneration.md)
and
[`hc7_disjoint_k6minus_k5model_two_apex_exclusion.md`](results/hc7_disjoint_k6minus_k5model_two_apex_exclusion.md).

## 3. Exact open problems

### 3.1 Label-preserving extraction of compatible $K_5$ models

Starting with the bounded exact-six family and its globally maximal private
pairs from item 12, prove one of the following:

- an explicit $K_7$-minor model in $G$;
- two vertices meeting every member of $\mathcal F_6(G)$;
- three vertex-disjoint six-vertex $K_5$ models with their prescribed
  branch-set labels; or
- a separation of $G$ of order seven preserving all specified rooted models
  and colouring data, together with a strictly decreasing induction
  parameter.

In this normalization the avoided support $A$ always has order six. The
unresolved cases are a genuinely separated labelled triple and the
following shared-set configurations: $A\cap X=\varnothing$ (with the two
additional models both of order five or both of order six), and the case in
which all three models have six vertices and $|A\cap X|=1$. A complete
eight-terminal rooted-minor classification does not by itself resolve the
latter: one finite boundary pattern defeats every choice of four vertices
held outside the rooted reduction.  A successful proof must therefore use
several compatible models constructed after different contractions, or
retain additional information from the contraction sequence.

For one-vertex replacements there is now a canonical region `Z_H` in
which all replacements preserve the same complete family of private
transversal pairs.  The extraction problem should therefore be attacked
with the following fixed alternative: either a replacement remains in
`Z_H`, where a declared linkage/model rank must decrease, or its first
outside vertex already identifies another globally maximal private pair.
What is missing is a label-preserving regeneration theorem at that outside
pair, not another support-only extraction.

### 3.2 Simultaneous composition in the common edge-deletion graph

Let $K=G-\{e_1,e_2,e_3\}$ be as in item 6 and assume $K$ is five-connected.
Each prescribed $K_4$ can be extended individually by a path joining the
endpoints of its deleted edge, but the three paths may intersect.  The
remaining theorem must combine these paths and the Kempe-component
alternatives into one of:

- an explicit $K_7$-minor model;
- a global two-vertex transversal for all $K_5$ models; or
- a model-preserving order-seven separation with a strict induction
  parameter.

A complementary contraction analysis yields the following.  After the
three-edge contraction case has been excluded, it gives either an unranked
order-seven
separation or an inclusion-minimal two-edge set whose simultaneous
contraction is not seven-connected.  In the order-two case, expansion gives
a boundary of order eight; both open sides
contain a connected subgraph adjacent to every boundary vertex, and the
boundary graph is four-colourable.  The last fact is computer-assisted, with
retained verification code and an independent replay. Four-colourability
alone does not align the two boundary colourings. The canonical
Gallai--Edmonds decomposition removes arbitrary Tutte-witness choice but
still does not transfer a colouring state. Likewise, the common Mader
delta-matroid representation preserves endpoint feasibility across the two
contractions but is blind to the same-model branch adjacencies and paths
needed for composition.

An explicit quotient also shows that six arbitrary vertex-disjoint paths
between a disjoint six-vertex $K_5$ model and a $K_6^-$ need not yield a
$K_7$ minor: the quotient has a width-five tree decomposition. A positive
continuation must retain the bridges of an extremally chosen linkage and
prove an augmenting rerouting or an order-at-most-six separator; replacing
the linkage by its endpoint matching loses essential information.

The new alignment theorem identifies exactly what that retained information
must repair. In the canonical $3+1$ ownership form, clean augmentation and
crossed bridge order are closed by explicit models.  A six-terminal decoder
now closes twelve of all fifteen crossing types and turns the other three
into a repaired `a_3`--`x` contact paired with one of three labelled
`y`-paths.  For a one-vertex repair, minor-critical colourings give a second
contact path avoiding both repair edges.  An intersection with the `p`- or
`q`-path closes by an explicit model; the exceptional `r`-intersection
returns an actual exact-seven separation whose two full-subgraph packing
numbers are both one.  The remaining obligation is to control a bypass that
meets the linkage skeleton or avoids the second residual path, and to attach
a strict rank to support replacements inside the fixed exchange core.

The other minimal ownership form, `2+2`, now has its clean augmentations,
both crossed-linkage types, and two web certificates proved.  Its remaining
obligation is a label-faithful six-terminal compression; a quotient crossing
calculation alone does not lift through the three linkage paths involved.

The detailed formulations and all immediate dependencies are in
[`active/INDEX.md`](active/INDEX.md) and
[`active/hc7_support_six_frontier.md`](active/hc7_support_six_frontier.md).

## 4. Established obstructions to tempting shortcuts

The following approaches are known to be insufficient without additional
hypotheses:

- Seven-connectivity together with an unrooted $K_6$ model does not force a
  $K_7$ minor.  The join of $K_2$ with the icosahedron is the principal test
  example.
- A four-colourable boundary does not ensure that colourings of the two
  sides induce the same partition of the boundary.
- Regenerating an unrooted minor after a contraction does not preserve
  prescribed branch-set labels.
- Iterating only the endpoint-equality patterns of the three deleted edges
  has no well-founded rank; explicit highly connected examples branch and
  cycle.
- A single bounded rooted-minor classification does not compose the final
  one-vertex-intersection configuration.
- The Mader endpoint delta-matroid does not record terminal--terminal edges
  inside one model part, and its symmetric exchanges can leave every graph-
  realizable contraction slice.
- The canonical Gallai--Edmonds barrier and all static exact-block responses
  do not synchronize two shore colouring languages.
- Six arbitrary disjoint linking paths between the zero-overlap models do
  not suffice; an explicit quotient of treewidth five excludes $K_7$.
- One contracted external component with seven distinct quotient contacts
  also need not suffice. Seven host attachments may collapse under linkage
  contractions, so the quotient's two exceptional eight-frames cannot be
  promoted to a host separation without a first-hit argument.
- Two crossless four-terminal web certificates, with one external bridge
  in each exceptional class, can coexist without a `K_7` minor at
  connectivity three.  Their static compatibility is therefore false;
  seven-connectivity or minor-critical colouring must enter the composition.
- Replacing one vertex of an exact six-vertex support can preserve every
  private transversal pair and still cycle inside the fixed exchange core.
  The core prevents transversal drift but does not supply a descending rank.
- Finite neighbourhood or Moser-spindle enumeration cannot replace an
  unbounded structural theorem.

Concrete examples and verification scripts are stored in
[`barriers/`](barriers/). They refute intermediate lemmas, not $HC_7$.

## 5. Evidence and maintenance policy

- A theorem note in [`results/`](results/) is treated as a repository proof
  only when its hypotheses, conclusion, and proof are written explicitly.
- An adjacent audit records a separate internal check, not peer review.
- Finite computer classifications retain their encodings and verification
  scripts; they are never promoted to unbounded theorems without a written
  reduction.
- [`active/`](active/) contains only current proof work and supporting
  computations.  Superseded work moves to [`archive/`](archive/), while
  false intermediate claims and their counterexamples move to
  [`barriers/`](barriers/).

Historical filenames retain some old project shorthand so that citations
and audit hashes remain stable.  Current public documents and all new work
should use standard graph-theoretic descriptions; see [`AGENTS.md`](AGENTS.md).

## 6. Principal external inputs

- W. Mader, [*Über trennende Eckenmengen in homomorphiekritischen
  Graphen*](https://eudml.org/doc/161665), Math. Ann. 175 (1968), 243--252:
  seven-connectivity of the relevant contraction-critical graph.
- J. Niu and C.-Q. Zhang, [*Cliques, minors and apex
  graphs*](https://doi.org/10.1016/j.disc.2008.12.009), Discrete Math. 309
  (2009), 4095--4107, Theorem 1.10: the three-clique minor theorem used in
  item 2.
- A. Martinsson and R. Steiner, [*Strengthening Hadwiger's conjecture for
  4- and 5-chromatic
  graphs*](https://doi.org/10.1016/j.jctb.2023.08.009), J. Combin. Theory
  Ser. B 164 (2024), 1--16: Strong Hadwiger for four colours, used in the
  rooted argument described in the technical frontier.
- M. Wahlström, [*Representative set statements for delta-matroids and the
  Mader delta-matroid*](https://arxiv.org/abs/2306.03605), especially the
  linear representation of Mader endpoint systems. The terminal-edge
  projection in item 13 is a new deduction in this repository.
- S. Humeau and D. Pous, [*On the Two Paths Theorem and the Two Disjoint
  Paths Problem*](https://arxiv.org/abs/2505.16431), Theorem 1.5 and the
  equivalent web-completion formulation in Section 5: the structural input
  used in items 15--16.
- P. Wollan, [*Bridges in Highly Connected
  Graphs*](https://doi.org/10.1137/070710214), SIAM J. Discrete Math. 24
  (2010), 1731--1741, Theorem 1.1: endpoint-preserving stable rerouting of
  the six-path system in item 16.
- R. Fabila-Monroy and D. R. Wood, [*Rooted
  $K_4$-Minors*](https://doi.org/10.37236/3476), Electron. J. Combin. 20(2)
  (2013), P64, Lemma 7: the cycle-linkage rooted model used in the `2+2`
  branch of item 16.
- A. Girão et al., [*The Dominating 4-Colour
  Theorem*](https://arxiv.org/abs/2605.10112), Theorem 1.1: the regeneration
  input after deleting the nonadjacent private pair.
