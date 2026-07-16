# Endpoint-rigid order-eight frontier

**Status:** superseded frontier, archived after the terminal shifted
order-eight residue was eliminated by
[`../results/hc7_shifted_boundary_completion.md`](../results/hc7_shifted_boundary_completion.md).
Earlier order-seven-separation exits and the complementary
perfect-matching arm remain global obligations; this file is retained for
provenance only.

## 1. Global normalization

Let `G` be a hypothetical minor-minimal counterexample to `HC_7`.  For a
two-vertex set `P`, let `mu_G(P)` be the least support order of a
`K_5`-minor model in `G-P`.  The current branch begins with

\[
                      \max_{|P|=2}\mu_G(P)=6.          \tag{1.1}
\]

The labelled Mader/delta-matroid comparison does not preserve the legal
split-versus-contracted model data, so the proof instead follows the
canonical Gallai--Edmonds decomposition of the complement of an
eight-vertex boundary.

In the endpoint-rigid no-perfect-matching branch, the audited results give
an eight-vertex separator `S` with these properties.

1. `G-S` has exactly two connected components `U,V`, and every vertex of
   `S` has a neighbour in both.
2. There are distinct vertices `s,x\in S` such that `s` is adjacent to
   every vertex of `S-\{s\}`.
3. The six-vertex graph `G[S-\{s,x\}]` is a theta graph: an edge together
   with two internally disjoint paths of length three having the same ends.
4. Contracting `U` and `V` in `G-\{s,x\}` gives the join of this theta
   graph with two nonadjacent universal vertices, and that quotient has no
   `K_5`-minor model supported on at most six vertices.

These conclusions are local to this exact branch; they do not assert that
every maximal pair in `G` has an order-eight separator.

## 2. Proved model form

Every minimum `K_5` model in `G-\{s,x\}` genuinely uses both components.
After interchanging `U,V`, its branch sets have the form

\[
       \{u_1\},\ldots,\{u_h\},
       \quad\{w_1\},\ldots,\{w_{4-h}\},
       \quad\{v,t\},                                  \tag{2.1}
\]

where

\[
       h\in\{2,3\},\quad u_i\in U,\quad v\in V,
       \quad t,w_j\in S-\{s,x\}.                     \tag{2.2}
\]

The four singleton branch sets form a clique.  The vertex `t` is adjacent
to every `u_i` and misses at least one `w_j`.  The two endpoints `v,t` have
one of the three exact complementary nonadjacency patterns proved in the
boundary-anchor theorem.

The following further facts are proved and separately audited.

- `V` is not the singleton `\{v\}`.
- Every component of `V-v` either gives a `K_7` minor, gives an actual
  order-seven separation, or is adjacent to exactly seven vertices of `S`.
  In the last case its unique missed boundary vertex belongs to
  `\{s,t,w_1,\ldots,w_{4-h}\}`.
- A component missing only `t` gives an explicit `K_7`-minor model.
- If `h=3`, all components of `V-v` have the same missed boundary vertex,
  either `s` or `w_1`.
- If `h=2`, two components with different missed vertices among
  `s,w_1,w_2` also give an explicit `K_7`-minor model.  The proof uses a
  two-path boundary anchoring and a two-element Hall argument; it does not
  depend on finite theta enumeration.

Thus the surviving configurations have `|V|>=2`, and every component of
`V-v` misses the same boundary vertex

\[
                         y\in\{s,w_1,\ldots,w_{4-h}\}.
\]

Consequently

\[
                         N_G(V-v)=\{v\}\cup(S-\{y\}), \tag{2.3}
\]

an actual separator of order eight.  Every component on the `V-v` side is
adjacent to all eight vertices of this shifted boundary.  The original
support-six `K_5` model is contained wholly in the opposite closed side.

## 3. Immediate theorem

The contact-placement problem is closed.  The next theorem is a uniform
state-transfer statement across the shifted separator (2.3).

> **Shifted order-eight exchange.**  Under (1.1)--(2.3), assume `G` has no
> `K_7` minor and no actual order-seven separation.  Use a deletion or
> contraction internal to `V-v`, together with the resulting proper-minor
> six-colouring or regenerated `K_5` model, to obtain either a two-vertex
> set `P'` with `mu_G(P')>=7`, or a model-preserving separation with a
> strict decrease of a declared host parameter.

The intended move is now particularly constrained: `V-v` is disjoint from
all five branch sets in (2.1), every one of its components is complete to
the shifted boundary in the minor-model sense, and the opposite open side
contains the entire old model.  A valid outcome must be one of:

1. an explicit `K_7`-minor model;
2. a pair of support height at least seven;
3. an actual order-seven separation preserving the named branch sets and
   strictly reducing the chosen open-side order; or
4. a regenerated model with a strict decrease in a precisely stated
   intersection parameter.

The host parameter should begin with `|V-v|`, since (2.3) has already
removed the old vertex `v` from that open side.  However, order alone is not
a valid induction until the returned colouring partition and named model
are shown to survive the shift.  An outcome that merely renames the two
sides or cycles among the endpoint-nonadjacency patterns is not progress.

## 4. Guardrails

- The Gallai--Edmonds sets alone do not meet every regenerated model; a
  static counterexample is retained in `barriers/`.
- The legal split/contracted slices of the Mader representation do not obey
  ordinary symmetric exchange.  Reopen that route only with a genuinely
  label-sensitive invariant.
- Component contact counts and theta placements are now exhausted.  Further
  work must compose the named branch sets or use a proper-minor colouring
  transition across (2.3).
- Contracting the full side `V-v` is safe only if the exact boundary
  colouring partition or every named branch-set contact used later is
  retained.

## 5. Immediate dependencies

Read each result with its adjacent audit:

- [named-edge Gallai--Edmonds reduction](../results/hc7_eight_boundary_named_edge_gallai_reduction.md)
- [endpoint-contact rigidity](../results/hc7_star_order_eight_endpoint_contacts.md)
- [endpoint-rigid Gallai--Edmonds collapse](../results/hc7_endpoint_rigid_gallai_exchange.md)
- [boundary-anchor completion and mixed-model form](../results/hc7_boundary_anchored_model_completion.md)
- [uniform common-neighbour completion](../results/hc7_common_neighbour_model_completion.md)
- [component-contact trichotomy](../results/hc7_mixed_shore_component_contacts.md)
- [component exchange and `h=3` label alignment](../results/hc7_mixed_shore_two_component_exchange.md)
- [`h=2` two-defect exchange and shifted order-eight separator](../results/hc7_theta_two_defect_exchange.md)
