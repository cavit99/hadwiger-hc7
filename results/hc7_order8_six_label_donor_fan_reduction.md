# A six-label fan reduces a donor-contained order-eight component to a singleton

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_six_label_donor_fan_reduction_audit.md`](hc7_order8_six_label_donor_fan_reduction_audit.md).

This note gives a label-preserving reduction for the special boundary-full
order-eight case in which one open component is contained wholly in one
branch set of the selected spanning `K_7`-minus-one-edge model and deleting
that component leaves the branch set connected.  The proof treats two and
three complementary components uniformly.  It produces an actual
order-seven separation or reduces the component to a degree-eight singleton.

The order-seven separation does not yet carry a common equality partition,
and the singleton case is not eliminated.  Thus this theorem does not close
the general boundary-full order-eight interface or prove `HC_7`.

## 1. Labelled and extremal setting

Let `G` be a seven-connected graph with no `K_7` minor.  Suppose that its
vertex set is partitioned into seven nonempty connected branch sets

\[
                  X,Y,D,U,F_1,F_2,F_3,                 \tag{1.1}
\]

and that every two are adjacent except possibly `X,Y`.  Fix one prescribed
root in every branch set.  Fix also:

1. a connected response subgraph `Z_0 subseteq D`;
2. a set of permitted source ports in `Z_0`;
3. a selected literal boundary partition; and
4. an edge

   \[
                         z_0u_0,
              \qquad z_0\in Z_0,\quad u_0\in U.       \tag{1.2}
   \]

Rank some of the labels in

\[
                     \{X,Y,U,F_1,F_2,F_3\},           \tag{1.3}
\]

including `U`.  For a compatible labelled model, let `lambda` be the
maximum number of paths which have distinct designated ports in `Z_0`, are
pairwise vertex-disjoint outside `Z_0`, and first meet the union of the
ranked branch sets in branch sets having distinct ranked labels.  Every path
is trimmed at that first ranked hit.  Paths may overlap inside `Z_0`.  This
is the relaxed literal first-hit rank used in the rank-preserving branch-set
transfer theorem.

Among all spanning labelled `K_7`-minus-one-edge models compatible with
the fixed roots, response subgraph, ports and boundary partition, choose
one which first maximizes `lambda` and, subject to that, minimizes `|U|`.

Let `S` be an eight-vertex set and let `C` be a component of `G-S` such
that another component of `G-S` exists and

\[
                         N_G(C)=S.                     \tag{1.4}
\]

Assume

\[
              C\subseteq U,
       \qquad U_0:=U-C\text{ is nonempty and connected},           \tag{1.5}
\]

that the prescribed root of `U` and the vertex `u_0` in (1.2) lie in
`U_0`, and that the boundary labels are

\[
 S=\{k_1,k_2\}\mathbin{\dot\cup}
   \{s_X,s_Y,s_D,s_{F_1},s_{F_2},s_{F_3}\},           \tag{1.6}
\]

where `k_1,k_2 in U_0` and `s_R in R` for every
`R in {X,Y,D,F_1,F_2,F_3}`.

These hypotheses are literal.  In particular, `C` is not merely assigned
the label `U` in a quotient: every vertex of `C` belongs to the old branch
set `U`, and the six vertices `s_R` belong to the six displayed old branch
sets.

## 2. Uniform reduction

### Theorem 2.1 (six-label donor-fan reduction)

In the setting of Section 1, at least one of the following holds.

1. There is a nonempty connected proper set `A subsetneq C` such that

   \[
                              |N_G(A)|=7,              \tag{2.1}
   \]

   and its full neighbourhood is the boundary of an actual separation
   with two nonempty open sides.
2. The component `C` is a singleton, say `C={v}`.  Consequently

   \[
                              N_G(v)=S,
              \qquad          d_G(v)=8.               \tag{2.2}
   \]

Thus every non-singleton donor-contained component in this order-eight
normal form returns an actual order-seven separation.

#### Proof

The vertex `k_1` has a neighbour in `C` by (1.4).  Choose

\[
                          v\in C,\qquad vk_1\in E(G),  \tag{2.3}
\]

and put

\[
                         T=\{s_X,s_Y,s_D,
                              s_{F_1},s_{F_2},s_{F_3}\}.            \tag{2.4}
\]

Apply the fan form of Menger's theorem from `v` to `T` in the graph

\[
                              H=G[C\cup T].             \tag{2.5}
\]

Suppose first that there is no six-fan.  There is a set

\[
                    Z\subseteq V(H)-\{v\},\qquad |Z|\le5,          \tag{2.6}
\]

which separates `v` from `T-Z`.  Let `A` be the component of `H-Z`
containing `v`.  Since `C` is a component of `G-S`, every host neighbour
of `A` lies either in `Z` or in the two omitted boundary vertices.  Hence

\[
                         N_G(A)\subseteq Z\cup\{k_1,k_2\}.          \tag{2.7}
\]

The set `T-Z` is nonempty.  Choose `s in T-Z`.  It lies outside `A` and
outside the right side of (2.7).  Moreover, (1.4) gives an edge from `s`
to `C`; its end in `C` cannot lie in `A`, by (2.7).  Thus `A` is a proper
subset of `C`.  The other component of `G-S` supplies a further nonempty
opposite side.  Consequently `N_G(A)` is a genuine host separator.  By
seven-connectivity and (2.6)--(2.7),

\[
              7\le |N_G(A)|\le |Z|+2\le7.             \tag{2.8}
\]

This proves outcome 1.

It remains to suppose that there is a six-fan.  Write its paths as

\[
                         P_R\quad
             (R\in\{X,Y,D,F_1,F_2,F_3\}),             \tag{2.9}
\]

where `P_R` joins `v` to `s_R`, and the paths meet pairwise only at `v`.
No path uses another member of `T` internally, because the six distinct
members of `T` are already the six terminal vertices.  Put

\[
                         L_R^0=V(P_R)-\{v,s_R\}.       \tag{2.10}
\]

Every nonempty `L_R^0` is connected, and the nonempty sets in (2.10) are
pairwise disjoint.  Remove `v` and all the nonempty sets `L_R^0` from
`C`.  Each remaining component has a neighbour in at least one of these
sets or at `v`, because `G[C]` is connected.  Assign each remaining
component to one adjacent member, and enlarge that member by the assigned
components.  This gives a partition

\[
                 C=C_0\mathbin{\dot\cup}
                    \mathop{\mathbin{\dot\bigcup}}_{L_R^0\ne\varnothing}
                    L_R,                               \tag{2.11}
\]

where `v in C_0`, every displayed set is connected, and
`L_R^0 subseteq L_R`.

Replace the old branch sets by

\[
                    U^*=U_0\cup C_0,
       \qquad       R^*=R\cup L_R
          \quad\text{when }L_R^0\ne\varnothing,       \tag{2.12}
\]

leaving `R` unchanged when `L_R^0` is empty.  The set `U^*` is connected
through the edge `vk_1`.  Every enlarged `R^*` is connected through the
last edge of `P_R`.  Its adjacency to `U^*` is supplied by the first edge
of `P_R`; when `L_R^0` is empty the direct edge `vs_R` supplies the same
adjacency.  Enlarging an outside branch set destroys no old adjacency.
All branch sets in (2.12) remain disjoint and, together with the unchanged
sets, partition `V(G)`.  They therefore form either an explicit `K_7`
minor model, if the possible missing `X-Y` adjacency has been repaired,
or another compatible spanning labelled `K_7`-minus-one-edge model.

The second model retains every prescribed root, the selected boundary
partition and `Z_0`.  Its relaxed first-hit rank does not decrease.  Indeed,
an old ranked path ending at a label other than `U` avoided the whole old
branch set `U`, and hence avoids every transferred subset of `C`.  An old
path ending in `U_0` also survives.  If the old path for label `U` ended
in a transferred subset of `C`, retain its designated port, join that port
to `z_0` inside connected `Z_0`, and append the fixed edge `z_0u_0`.
The replacement may overlap the other paths inside `Z_0`, which is allowed,
and outside `Z_0` it has only the new terminal `u_0`.  Every other ranked
path avoided the old `U`, so it avoids `u_0`.  This is a valid family of
the same order.

If some `L_R^0` is nonempty, (2.12) removes a nonempty set from `U`.
The `K_7` outcome contradicts the hypothesis on `G`; the compatible-model
outcome contradicts the maximum-rank, minimum-`|U|` choice.  Hence

\[
                           L_R^0=\varnothing
              \quad\text{for all }R,                  \tag{2.13}
\]

and therefore

\[
                           vs_R\in E(G)
              \quad\text{for all }R.                  \tag{2.14}
\]

Suppose that `C-v` is nonempty, and let `Q` be any component of
`G[C-v]`.  If `Q` had no neighbour in `T`, then componenthood of `C` in
`G-S` and componenthood of `Q` in `G[C-v]` would give

\[
                           N_G(Q)\subseteq\{v,k_1,k_2\},           \tag{2.15}
\]

contrary to seven-connectivity.  Thus every component `Q` has a neighbour
at some `s_R`.  Assign `Q` to one such `R`, and enlarge that outside branch
set by all components assigned to it.  Put

\[
                              U^{**}=U_0\cup\{v\}.      \tag{2.16}
\]

The set in (2.16) is connected through `vk_1`; every enlarged outside
branch set is connected through its boundary vertex `s_R`; and the six
direct edges in (2.14) retain every adjacency from `U^{**}` to an outside
branch set.  As before, this is an explicit `K_7` model or a compatible
spanning labelled `K_7`-minus-one-edge model.  The preceding first-hit
argument again preserves `lambda`.

If `C-v` were nonempty, (2.16) would strictly reduce `|U|`, contradicting
the extremal choice.  Therefore `C={v}`.  Equation (1.4) now gives (2.2),
and the proof is complete. \(\square\)

## 3. Preservation of incident operation responses

### Corollary 3.1

In addition to the hypotheses above, suppose that `v` supports prescribed
edges

\[
                         e=vs_R,\qquad f=vs_{R'},      \tag{3.1}
\]

with `R ne R'`, and that their one-edge and simultaneous-contraction
six-colourings are part of the fixed response data.  The six-fan in the
proof may be chosen to use `e,f` as its two corresponding paths.

In outcome 1 of Theorem 2.1, both `s_R,s_{R'}` belong to the literal
boundary `N_G(A)`, both edges in (3.1) cross from `A` to that boundary,
and each selected **one-edge** response restricts to the corresponding
edge-operated closed `A`-shore and to the unchanged opposite closed shore.
Thus the order-seven return retains the two one-edge responses and their
literal branch-set labels.  The simultaneous-contraction response has the
same conclusion when `s_Rs_{R'}` is not an edge.  If that boundary edge is
present, expanding the simultaneous contraction makes its ends equal, so
the response is only an identified-boundary trace and is not a proper
colouring of the literal opposite closed shore.  No assertion is made that
an equality partition extends through both intact closed shores.

#### Proof

In the fan outcome, replace the two fan paths by the direct edges, exactly
as in the fan form of Menger's theorem.  In the separator outcome, the
edge from `v in A` to a terminal `s_R` shows that `s_R` must belong to
the separating set `Z`; otherwise it would lie in the `v`-component.
The same holds for `s_{R'}`.  Equality in (2.8) gives

\[
                         N_G(A)=Z\mathbin{\dot\cup}\{k_1,k_2\}.  \tag{3.2}
\]

Hence both edges cross the new boundary.  Restrict either one-edge response
to the two closed shores.  Its operated edge is absent on the `A`-shore,
and the edge's interior end does not occur on the opposite shore, so both
restrictions are proper and the literal boundary assignment is unchanged.

For the simultaneous response, the only additional issue on the opposite
shore is the edge `s_Rs_{R'}`: its ends are identified by the two
contractions and hence receive one colour after expansion.  The restriction
is proper when this edge is absent, and need not be proper when it is
present.  This proves exactly the stated claim. \(\square\)

## 4. Exact trust boundary

The theorem is uniform in the number of other components of `G-S`; in
particular it applies to either the two- or three-component order-eight
residue whenever the donor-containment hypotheses (1.5)--(1.6) hold.

It does **not** apply to an arbitrary boundary-full component whose vertices
belong to several old branch sets, or when deleting `C` disconnects `U`.
Those are precisely the cases in which assigning the six fan arms to their
literal labels is not automatically a spanning-model transfer.

Outcome 1 is a bare actual order-seven separation.  Corollary 3.1 preserves
the two selected one-edge responses when their edges have a common end `v`;
the simultaneous response also survives literally only under the stated
boundary-nonadjacency condition.  The corollary does not furnish a common
equality partition on the intact closed shores.  For
two independent response edges one must instead use a connected source
containing both inner ends; the equality case then leaves a rooted
path/Steiner-tree allocation obstruction rather than the singleton proved
here.

Outcome 2 is an exact degree-eight local obstruction, not a contradiction.
Eliminating it requires the degree-eight colouring/minor machinery or a
separate compatible-separator theorem.

## 5. Dependencies

- the fan form of Menger's theorem;
- the extremal relaxed first-hit rank and its replacement path from
  [first-hit rank under a label-preserving branch-set transfer](../results/hc7_first_hit_rank_preserving_branch_set_transfer.md);
- the spanning labelled order-eight normal form from
  [reserved-component completion](../results/hc7_reserved_component_linkage_completion.md),
  when this theorem is invoked in that branch.
