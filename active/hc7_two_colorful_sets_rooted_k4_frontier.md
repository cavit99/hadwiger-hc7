# Technical frontier: a `K_4` minor rooted at two colourful sets

**Status:** active reduction and conjectural target.  The reduction below
uses the GREEN-audited star-Kempe compression theorem.  The paired-root
theorem in Section 3 is open.  Nothing here proves `HC_7`.

## 1. Compressed setup

Let `G` be a hypothetical minor-minimal counterexample to `HC_7`.  In the
star-Kempe branch of the adjacent-pair construction, the vertex set has a
partition

\[
                    V(G)=X\mathbin{\dot\cup}V(Q),
\]

with the following properties.

1. `X` is a connected induced bipartite subgraph and dominates `Q`.
2. The graph `Q` is five-chromatic and has no `K_6` minor.
3. There are adjacent vertices `z,u in V(Q)` such that, on putting

   \[
                         R=Q-\{z,u\},                  \tag{1.1}
   \]

   one has

   \[
      \chi(R)=4,qquad \chi(R+z)=\chi(R+u)=5.          \tag{1.2}
   \]

4. Both `z` and `u` have a neighbour in `X`.

Write

\[
                 S=N_R(z),\qquad T=N_R(u).             \tag{1.3}
\]

## 2. Exact reduction to two colourful sets

### Lemma 2.1

Both `S` and `T` are colourful in the four-chromatic graph `R`: every
proper four-colouring of `R` uses all four colours on each of `S,T`.

#### Proof

Let `c` be a proper four-colouring of `R`.  If some colour were absent
from `S`, assigning that colour to `z` would four-colour `R+z`, contrary
to (1.2).  Thus `S` contains all four colours under `c`.  The proof for
`T` is symmetric. \(\square\)

### Lemma 2.2

If `R` has a `K_4`-minor model `(D_1,D_2,D_3,D_4)` such that

\[
       D_i\cap S\ne\varnothing
       \quad\hbox{and}\quad
       D_i\cap T\ne\varnothing
       \qquad(i=1,2,3,4),                              \tag{2.1}
\]

then `G` contains a `K_7` minor.

#### Proof

The seven branch sets

\[
                 \{z\},\ \{u\},\ X,\ D_1,D_2,D_3,D_4
\]

are pairwise disjoint and connected.  The first two are adjacent because
`zu` is an edge.  Both are adjacent to `X`, and domination makes `X`
adjacent to every `D_i`.  Condition (2.1) makes both singletons adjacent
to every `D_i`, while the four `D_i` are pairwise adjacent by definition.
These are the branch sets of a `K_7` minor. \(\square\)

Martinsson--Steiner's Strong Hadwiger theorem for four colours, applied
separately to `S` and `T`, produces an `S`-rooted `K_4` model and a
`T`-rooted `K_4` model.  The missing operation is to synchronize those two
models so that every branch set satisfies both conditions in (2.1).

## 3. Primary open theorem

### Paired colourful-set alternative

Under the complete setup of Section 1, prove at least one of the
following.

1. `R` has a `K_4` model satisfying (2.1), and Lemma 2.2 gives a `K_7`
   minor.
2. `G` has an actual order-seven separation whose boundary colouring is
   induced by proper-minor six-colourings on both sides.

The former two-vertex `K_5`-model-transversal outcome feeds into item 2 only
at the level of raw separation existence: in the present host it
forces a degree-seven vertex and an actual order-seven separation, but it
does not supply compatible shore colourings and therefore does not close
item 2.

The statement is intentionally tied to the lifted host `G`.  It is false
for arbitrary four-chromatic `R` with two colourful sets, even when `R` is
five-connected; see the
[explicit join-of-two-paths barrier](../barriers/hc7_two_colorful_sets_paired_k4_barrier.md).
That example contains a `K_6` minor and therefore cannot occur as the
present core.  The connected dominating subgraph `X`, the `K_6`-minor
exclusion, seven-connectivity, and the proper-minor colouring responses
must all remain available in a proof.

## 4. The deficient component and its expanded boundary

Fix an `S`-rooted `K_4` model `(D_1,...,D_4)`.  The six branch sets

\[
                         X,\ \{z\},\ D_1,\ldots,D_4    \tag{4.1}
\]

form a `K_6` model.  The remaining pole `u` is adjacent to `X` and `z`,
and it is adjacent to `D_i` exactly when that branch set contains a member
of `T`.  Contracting the sets in (4.1) therefore gives a proper minor
containing a named `K_6` plus one vertex whose missing adjacencies are
precisely the `T`-deficient branch sets.

Because every proper minor of `G` is six-colourable, the six clique
vertices receive distinct colours and `u` must repeat the colour of one
of the branch sets it misses.  This makes the paired-root failure visible
as an exact proper-minor colouring response, rather than merely as an
unlabelled failure of two rooted models to coincide.

The repeated colour is not itself a rerouting certificate.  Even with a
`K_6`-minor-free five-chromatic core and a unique missed branch set, the
quotient response may be forced while no improving rooted model exists;
see the explicit barrier linked below.

There is, however, a host-level separator attached to every missed branch
set.  Choose the `S`-rooted model to maximize the number of branch sets
meeting `T`.  For a missed branch set `D_j`, delete the other three branch
sets from `R`, and let `C_j` be the component containing `D_j`.  The
promoted deficient-component theorem proves

\[
 C_j\cap T=\varnothing,
 \qquad
 N_G(C_j)=N_R(C_j)\mathbin{\dot\cup}N_X(C_j)
              \mathbin{\dot\cup}\{z\},               \tag{4.2}
\]

with `N_R(C_j)` contained in the other three branch sets.  This is the
boundary of an actual separation and has order at least seven.  Contraction
collapses its possibly many vertices to at most five labels, which explains
why the quotient colouring gives no upper bound.

The constructive programme is therefore:

1. choose an `S`-rooted model maximizing the number of branch sets meeting
   `T`;
2. work with the literal boundary (4.2), not only its contracted labels;
3. use distributed attachments in `X` and the other three branch sets to
   reroute the deficient branch set or construct `K_7`; and
4. if this is impossible, reduce (4.2) to an order-seven boundary carrying
   compatible proper-minor colourings; if a global two-vertex transversal
   is obtained, invoke the promoted theorem to obtain that separation.

In the unique-deficiency case, `C_j,u,z,X` and the other three branch sets
already form a `K_7`-minus-one-edge model, missing only the adjacency
between `C_j` and `u`.  The immediate host theorem is therefore a
label-preserving split-or-separator theorem for this actual near-complete
model.

The promoted colour-matched-path theorem supplies a path from `C_j` to a
neighbour of `u`.  Removing that path from the four protected branch sets
has an exhaustive consequence: either residual components give an explicit
`K_7` model, or the full neighbourhood of one connected residual component
is an actual separator.  Varying the cut edge along the path gives an exact
valid-cut interval for every residual component.

This exchange has a scalar formulation.  For seven disjoint candidate sets
`B_i`, put

\[
 \delta(\mathcal B)=
 \sum_{i<j}\bigl(c(B_i\cup B_j)-1\bigr)
 -\sum_i\bigl(c(B_i)-1\bigr),                       \tag{4.3}
\]

where `c` counts connected components.  A component-contraction density
argument gives `K_7` whenever \(\delta\le0\); the initial
`K_7`-minus-one-edge model has \(\delta=1\).  At one path cut, any `K_4` minor
in the contact graph of residual components adjacent to `z` and both path
sides lifts to `K_7`.  In the unique-deficiency branch, for a fixed
admissible cut and a selection representing all four protected classes,
every selected residual component is also required to lie in its valid-cut
interval—so it is adjacent to both path-side anchor sets—and to be adjacent
to `z`.  A
`K_4`-minor-free contact graph then has defect one exactly when it is a
two-tree.  Those hypotheses are not known to be exhaustive.  The next
theorem in this conditional branch must use the proper-minor six-colourings
at a lifted simplicial degree-two component to destroy that last unit of
defect, expose a colour-compatible order-seven boundary, or produce a new
valid instance of the same eligible defect-one setup with a lifted
simplicial component `L'` satisfying `|V(L')|<|V(L)|`.  Choose `L` with
minimum order over all eligible simplicial lifted components in every valid
configuration in the fixed host `G`.  This is the sole proposed rank;
noncanonical path length and the selected contact-graph order are excluded.

A **valid defect-one configuration** comprises the complete adjacent-pair
connected-dominating frame, the uniquely deficient rooted model, the
colour-matched path `P` and admissible cut `q`, four nonempty labelled
selections of residual components, eligibility of every selected component
at `q`, and a `K_4`-minor-free component-contact graph `J` of defect one.
The subgraph `L` is the literal component represented by a simplicial
degree-two vertex of `J`.  A smaller `L'` must occur in another full valid
configuration in the original `G`, not only as an image in a proper minor.

Adjacent maximal triangles of the two-tree determine local `K_6` models
sharing five named branch sets, but their colour patterns can be globally
coherent without a `K_7` minor.  A transition must therefore preserve the
label of each component by its protected branch-set class, the orientation
of `P` and interval endpoints, and chosen host edges and endpoints witnessing
every required contact.  A transition must retain those witnesses or give
explicit replacements, identify the bipartition-side or pole source of each
colour response, preserve named root traces, and carry the exact boundary
equality partition.  Failure returns `N_G(Y)` for a named connected residual
piece `Y` with both shores nonempty.  A proper-minor operation inside `L` is
only a probe; its conclusion must lift back to `G`.

An elementary minor operation in the five-chromatic core leaves a four- or
five-chromatic core.  In the four-chromatic branch, the common attachment
set for the two bipartition classes of `X` is colourful and roots a `K_4`
model meeting both sets.  These are not the pole sets `S,T`, and the two
bipartition classes need not be connected branch sets, so this is not yet
the required paired-root model.  The five-chromatic branch obeys only the
exact common-hole law.  Merely alternating between independently generated
models, rereading the repeated quotient colour, or optimizing a shortest
locked subpath gives no descent.

## 5. Immediate dependencies and barrier

- [deficient-component separator theorem](../results/hc7_maximal_rooted_k4_deficient_component_separator.md)
- [colour-matched repair path](../results/hc7_colour_matched_repair_path.md)
- [component exchange criterion](../results/hc7_colour_matched_path_component_exchange.md)
- [fixed-path exchange or separation](../results/hc7_colour_matched_path_exchange_or_separator.md)
- [all-cut interval and component-defect criterion](../results/hc7_colour_matched_path_all_cut_interval_exchange.md)
- [component-contact defect theorem and two-tree equality structure](../results/hc7_component_contact_defect_theorem.md)
- [one-step minor dynamics and the exact common-hole law](../results/hc7_star_core_one_step_minor_dynamics.md)
- [contracted-path list obstruction](../results/hc_contracted_path_list_lock.md)
- [two-vertex transversal implies an order-seven separation](../results/hc7_k5_transversal_order7_separator.md)
- [repeated quotient colour does not force an exchange](../barriers/hc7_repeated_colour_rooted_k4_exchange_barrier.md)
- [planar four-connected paired-root barrier](../barriers/hc7_paired_colourful_planar_core_barrier.md)
- [connectivity-only near-`K_7` augmentation hardness](../barriers/hc7_eight_connected_near_k7_augmentation_hardness.md)
- [shortest-lock orbit barrier](../barriers/hc7_contracted_path_shortest_lock_orbit_barrier.md)

## 6. Established external input

A. Martinsson and R. Steiner,
[*Strengthening Hadwiger's conjecture for 4- and 5-chromatic graphs*](https://doi.org/10.1016/j.jctb.2023.08.009),
Journal of Combinatorial Theory, Series B 164 (2024), 1--16, Theorem 1.3
and Corollary 1.4.

Theorem 1.3 says that a colourful set in a four-chromatic graph roots a
`K_4` minor.  It is applied separately to `S` and `T`; the paired version
in Section 3 is not claimed by that paper.
