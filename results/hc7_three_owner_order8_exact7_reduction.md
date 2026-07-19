# A concentrated three-owner order-eight interface has an order-seven separation

**Status:** written proof; separate internal audit GREEN in
[`hc7_three_owner_order8_exact7_reduction_audit.md`](hc7_three_owner_order8_exact7_reduction_audit.md).
This theorem
eliminates the boundary-full order-eight outcome of the concentrated
three-owner branch by a three-fan argument and the existing extremal choice
of the labelled minor model.  Its conclusion is an actual order-seven
separation, not yet a pair of closed-shore colourings with the same boundary
partition.  It does not prove `HC_7`.

## 1. Setting

Use the hypotheses and notation of the audited
[three-owner concentration theorem](hc7_three_owner_reserved_component_concentration.md).
Thus `G` is seven-connected, seven-chromatic and `K_7`-minor-free, every
proper minor of `G` is six-colourable, and `G` has a spanning labelled
`K_7`-minus-one-edge model

\[
                 X,Y,D,U,F_1,F_2,F_3,
\]

whose only possible missing branch-set adjacency is `X-Y`.  Write

\[
                 U=W\mathbin{\dot\cup}U'
\]

as in that theorem.  The model is chosen, among all models compatible with
the fixed roots, boundary partition and response subgraph, first to maximize
the relaxed literal first-hit rank and then to minimize `|U|`.

The complete owner set is the inclusion-minimal deficient family

\[
                         I=\{R_1,R_2,R_3\}
       \subseteq\{X,Y,F_1,F_2,F_3\}.
\]

There is a two-vertex internal transversal `K={k_1,k_2}` and a component
`C` of `G[W-K]` for which

\[
 E_G(C,U')=\varnothing,
 \qquad N_{G[W]}(C)=K,
 \qquad |N_G(C)|=8.
\tag{1.1}
\]

Each of the six branch sets different from `U` contains exactly one vertex
of `N_G(C)`.  Denote these vertices by

\[
                  s_D,s_X,s_Y,s_{F_1},s_{F_2},s_{F_3}.
\]

Put

\[
 S=N_G(C)=\{k_1,k_2\}\mathbin{\dot\cup}
   \{s_D,s_X,s_Y,s_{F_1},s_{F_2},s_{F_3}\},
\tag{1.2}
\]

and

\[
                         U_0=U'\cup(W-C).
\tag{1.3}
\]

The cited theorem proves that `G[U_0]` is connected.  It also proves the
complete concentration of the owner portals:

\[
                  N_G(R_i)\cap W\subseteq C
                  \qquad(1\le i\le3).
\tag{1.4}
\]

Because `C` has only the one boundary vertex `s_{R_i}` in the branch set
`R_i`, every edge from `C` to `R_i` ends at `s_{R_i}`.

## 2. The reduction

### Theorem 2.1

In the setting above, `G` has an actual separation of order seven.

#### Proof

By (1.1), `C` has a neighbour in `K`; choose

\[
                         v\in C,qquad vk_1\in E(G).
\tag{2.1}
\]

Consider the graph

\[
             H=G[C\cup\{s_{R_1},s_{R_2},s_{R_3}\}].
\tag{2.2}
\]

Apply the fan form of Menger's theorem from `v` to the three displayed
owner representatives.

Suppose first that there is no three-fan.  Then there is a set

\[
 Z\subseteq V(H)-\{v\},\qquad |Z|\le2,
\tag{2.3}
\]

meeting every path in `H` from `v` to
`{s_{R_1},s_{R_2},s_{R_3}}`.  The set `Z` is allowed to contain owner
representatives.  Let `A` be the component of `H-Z` containing `v`.  No
owner representative outside `Z` belongs to `A`, and componenthood gives

\[
 N_G(A)\subseteq
       \bigl(S-\{s_{R_1},s_{R_2},s_{R_3}\}\bigr)\cup Z.
\tag{2.4}
\]

The right-hand side has order at most `5+2=7`.  At least one owner
representative is outside `Z`, and it lies outside both `A` and the
right-hand side of (2.4).  Thus (2.4) is a nontrivial host separation.
Seven-connectivity forces equality throughout: `|N_G(A)|=7`, and
`N_G(A)` is the boundary of an actual order-seven separation.  This is the
desired conclusion.

It remains to show that the three-fan outcome is impossible.  Let

\[
                         P_1,P_2,P_3
\tag{2.5}
\]

be paths which meet pairwise only in `v`, where `P_i` ends at `s_{R_i}`
and otherwise lies in `C`.  Put

\[
                         T_i=V(P_i)-\{v,s_{R_i}\}.
\tag{2.6}
\]

The sets `T_i` are pairwise disjoint; each is either empty or connected,
as witnessed by the corresponding internal subpath of `P_i`.  Remove `v`
and the three `T_i` from `C`.  Every component of the
remaining graph has an edge to `\{v\}\cup T_1\cup T_2\cup T_3`, because
`G[C]` is connected.  Assign each such component to one adjacent nonempty
member among `\{v\},T_1,T_2,T_3`.  After adjoining the assigned components,
write the resulting partition as

\[
                         C=C_0\mathbin{\dot\cup}L_1
                              \mathbin{\dot\cup}L_2
                              \mathbin{\dot\cup}L_3,
\tag{2.7}
\]

where `v\in C_0`, every nonempty `L_i` contains `T_i`, and all four
nonempty sets in (2.7) are connected.  When `T_i` is empty, take `L_i`
empty and assign no component to it.

Replace the old donor and owner branch sets by

\[
              U^*=U_0\cup C_0,
              \qquad R_i^*=R_i\cup L_i
              \quad(1\le i\le3),
\tag{2.8}
\]

with the convention `R_i^*=R_i` when `L_i` is empty.  The set `U^*` is
connected through the edge `vk_1`.  If `L_i` is nonempty, the last edge of
`P_i` makes `R_i^*` connected and the first edge of `P_i` gives the
`U^*-R_i^*` adjacency.  If `L_i` is empty, the path `P_i` is the edge
`vs_{R_i}`, which gives that adjacency directly.

The retained set `U_0` preserves every donor adjacency to a nonowner, and
the fixed edge from the response subgraph in `D` to `U'\subseteq U_0`
preserves the `D-U^*` adjacency.  Enlarging an owner cannot destroy any
other old model adjacency.  Hence (2.8), together with the three unchanged
branch sets, gives either an explicit `K_7`-minor model (if `X-Y` has been
repaired) or another compatible spanning labelled
`K_7`-minus-one-edge model.

The relaxed first-hit rank does not decrease.  Every ranked path whose
terminal label is not `U` avoided all of the old branch set `U` and hence
avoids every transferred part of `C`.  A ranked path which ended in a
transferred part of `U` is replaced, inside the fixed connected response
subgraph, by the fixed edge into `U'`, exactly as in the audited
rank-preserving transfer theorem.  All roots and the selected colouring
data remain fixed.

If some `T_i` is nonempty, then `U^*` is a proper subset of `U`.  The first
outcome above contradicts `K_7`-minor exclusion, and the second contradicts
the maximum-rank, minimum-`|U|` choice.  Therefore

\[
                         T_1=T_2=T_3=\varnothing.
\tag{2.9}
\]

In particular, `v` is adjacent to all three owner representatives.

Suppose that `C-\{v\}` is nonempty, and let `Q` be any of its components.
If `Q` had no neighbour in any of the six branch sets different from `U`,
then, using (1.1) and componenthood in `C-v`,

\[
                         N_G(Q)\subseteq\{v,k_1,k_2\},
\]

contrary to seven-connectivity.  Choose for every component `Q` one
outside branch set to which it is adjacent, and absorb all of `Q` into
that branch set.  Several components may be assigned to the same branch
set; their union with that old connected branch set remains connected.

Now replace `U` by `U_0\cup\{v\}`.  This is connected by (2.1), and the
three edges `vs_{R_i}` preserve all owner adjacencies.  The set `U_0`
preserves the nonowner and `D` adjacencies.  The same rank-preservation
argument applies.  Thus, if `|C|>1`, the reassignment again gives either a
`K_7` model or a compatible model of the same maximum rank with a strictly
smaller donor.  Both are impossible.  Consequently

\[
                              C=\{v\}.
\tag{2.10}
\]

Finally, the exact two-edge response corollary of the concentration theorem
gives, for any two distinct owners, two owner-contact edges with distinct
ends in `C`.  This is impossible when (2.10) holds.  The three-fan outcome
is therefore impossible, so the fan failure already gave the asserted
order-seven separation.  \(\square\)

## 3. Exact contribution and trust boundary

The proof eliminates the complete concentrated three-owner
boundary-full order-eight geometry.  It uses the order-eight boundary only
through its literal five-versus-three split: deleting the three owner
representatives leaves five boundary vertices, so a failed three-fan has a
host neighbourhood of order at most seven.  In the fan outcome, the
maximum first-hit rank and minimum donor order make the common fan centre a
valid well-founded branch-set exchange.

The returned order-seven separation is not yet a colouring-gluing
conclusion.  In particular, this theorem does not prove that its two closed
shores have six-colourings inducing the same equality partition.  The next
operation must apply contraction-critical colouring to an edge crossing
the returned boundary and either synchronize a complete boundary
partition, construct a `K_7` model, or make a strict state-preserving
descent.

## 4. Dependencies

- [three-owner portal concentration and its two-edge response](hc7_three_owner_reserved_component_concentration.md)
- [connected retained donor and the order-eight boundary normal form](hc7_reserved_component_linkage_completion.md)
- [first-hit rank under a label-preserving branch-set transfer](hc7_first_hit_rank_preserving_branch_set_transfer.md)
- the fan form of Menger's theorem.
