# A distinct-boundary prescribed-spoke fan and three-owner transfer

**Status:** written proof; separate internal audit GREEN in
[`hc7_distinct_boundary_spoke_owner_transfer_audit.md`](hc7_distinct_boundary_spoke_owner_transfer_audit.md).
The theorem
turns the five prescribed first edges of one operation-specific response
into five paths with distinct literal ends at a boundary-full order-eight
interface.  In one exact endpoint pattern it gives a strict,
label-preserving transfer of the distinguished component among its three
owner branch sets, or a common literal portal for all three owner labels.
It does not force that endpoint pattern and does not prove `HC_7`.

## 1. Setting

Use the spanning labelled `K_7`-minus-one-edge model

\[
                 X,Y,D,U,F_1,F_2,F_3                       \tag{1.1}
\]

and the globally extremal choice in the audited
[three-owner concentration theorem](hc7_three_owner_reserved_component_concentration.md):
the relaxed literal first-hit rank is maximum and, subject to that, the
order of `U` is minimum.  Write

\[
                 U=C\mathbin{\dot\cup}U_0,                 \tag{1.2}
\]

where `C` and `U_0` are nonempty and connected, `C` is adjacent to `U_0`,
and the three owner branch sets are

\[
                 I=\{R_1,R_2,R_3\}\subseteq
                    \{X,Y,F_1,F_2,F_3\}.                   \tag{1.3}
\]

All old `U-R_i` contacts lie in `C`.  The full neighbourhood of `C` is

\[
 S=K\mathbin{\dot\cup}
   \{s_D,s_X,s_Y,s_{F_1},s_{F_2},s_{F_3}\},
 \qquad K=\{k_1,k_2\},                                    \tag{1.4}
\]

where `s_Q` is the unique literal vertex of the branch set `Q` in
`N_G(C)`.  In particular, the representative of owner `R_i` in (1.4) will
be denoted by `s_i`.

Fix a vertex `v in C` and five distinct edges at `v`, denoted

\[
                         vv_1,\ldots,vv_5.                \tag{1.5}
\]

In the application these are the five colour-indexed first edges supplied
by a six-colouring after deleting one critical edge from `v` to `S`.  The
proof below uses their literal identities, but not their palette colours.

## 2. The boundary-first fan

### Theorem 2.1

There are five paths from `v` to `S` which

1. start with the five prescribed edges in (1.5), one per path;
2. have five distinct ends in `S`;
3. share no vertex other than `v`; and
4. have all internal vertices in `C`.

Consequently their five ends belong to at least four distinct branch-set
labels of (1.1).  Equality can occur only when both `k_1` and `k_2` are
ends; in that case the other three ends lie in three distinct branch sets
different from `U`.

#### Proof

Apply Theorem 1.1 of the audited
[prescribed-spoke reduction](hc7_order8_prescribed_spoke_reduction.md)
with `k=5` and target set `Y=S`.  Seven-connectivity is stronger than the
required six-connectivity, and `|S|=8>=5`.  It gives five paths with the
prescribed first edges, distinct ends in `S`, and no common vertex outside
`v`.

Choose the paths in the first-target form used in the proof of that
theorem, or equivalently truncate each one at its first vertex of `S`.
Truncation preserves its first edge and preserves distinctness of the ends,
because the paths are disjoint outside `v`.  Since `C` is a component of
`G-S`, every vertex before that first boundary hit lies in `C`.  This proves
items 1--4.

The vertices `k_1,k_2` have the same inherited label `U`, whereas the other
six vertices of `S` lie one each in six different branch sets.  Five
distinct boundary ends therefore have at least four inherited labels, and
four labels occur only when both members of `K` are used. \(\square\)

## 3. The all-owner endpoint pattern

### Theorem 3.1

Assume the endpoint set of the five paths in Theorem 2.1 is

\[
                         \{k_1,k_2,s_1,s_2,s_3\}.       \tag{3.1}
\]

Then one of the following holds.

1. `G` contains a `K_7` minor.
2. There is another spanning labelled `K_7`-minus-one-edge model with the
   same possible missing pair, prescribed roots, selected boundary
   partition and fixed response subgraph, whose relaxed literal first-hit
   rank is not smaller and whose `U` branch set has smaller order.
3. All three owner representatives are adjacent to the same literal vertex
   `v in C`:

   \[
                            vs_i\in E(G)
                            \qquad(1\le i\le3).          \tag{3.2}
   \]

In particular, outcome 3 supplies incident owner-contact edges carrying
three distinct inherited branch-set labels.  It does not assert that these
are the only contacts from `C` to the owners.

#### Proof

Name the two paths ending at `k_1,k_2` by `Q_1,Q_2`, and name the path
ending at `s_i` by `P_i`.  All five paths share only `v`.  Put

\[
 D_0=\bigl(V(Q_1)\cup V(Q_2)\bigr)\cap C,
 \qquad
 L_i=\bigl(V(P_i)\cap C\bigr)-\{v\}.                   \tag{3.3}
\]

The set `D_0` is connected and contains `v`; it is adjacent to `U_0`
through both endpoint edges into `k_1,k_2`.  Every nonempty `L_i` is a
connected path, is adjacent to `D_0` through the first edge of `P_i`, and
is adjacent to `R_i` through the last edge of `P_i`.  The four sets
`D_0,L_1,L_2,L_3`, after empty `L_i` are omitted, are pairwise disjoint.

Every component of

\[
 C-\left(D_0\cup L_1\cup L_2\cup L_3\right)            \tag{3.4}
\]

has a neighbour in at least one nonempty displayed set, because `G[C]` is
connected.  Assign each such component to one adjacent set.  After the
assignment, write the resulting connected partition as

\[
                         C=D_0'\mathbin{\dot\cup}
                           L_1'\mathbin{\dot\cup}
                           L_2'\mathbin{\dot\cup}L_3',  \tag{3.5}
\]

where `L_i'` is empty exactly when `L_i` was empty.  (A component is never
assigned to an empty seed.)

Replace the old branch sets by

\[
                         U^*=U_0\cup D_0',
 \qquad                  R_i^*=R_i\cup L_i'
                         \quad(1\le i\le3),             \tag{3.6}
\]

leaving the other three branch sets unchanged.  These seven sets are
connected, disjoint and span `G`.  If `L_i'` is nonempty, its first and
last path edges give the adjacencies `U^*-R_i^*`; if it is empty, `P_i` is
the direct edge `vs_i`, which gives the same adjacency.  Every nonowner of
`C` is adjacent to `U_0`, and the fixed edge from the response subgraph in
`D` to `U_0` preserves the `D-U^*` adjacency.  Enlarging an owner preserves
all of its old outside adjacencies.  Hence the only branch-set pair which
can still be nonadjacent is the old possible pair `X,Y`.  If it becomes
adjacent, the displayed sets form a `K_7`-minor model, giving outcome 1.

Otherwise (3.6) is a compatible spanning labelled near-complete model.
All prescribed roots remain in their old branch sets, because the root of
`U` lies in `U_0` and no owner is reduced.  The relaxed first-hit rank does
not decrease.  A ranked path with a label different from `U` avoided all
of old `U`, and therefore avoids every transferred set `L_i'`.  A ranked
`U`-path ending outside `U^*` is replaced, with the same designated port,
by a path inside the fixed connected response subgraph followed by the
fixed edge into `U_0`; this is exactly the rank-preservation argument in
the audited multi-owner transfer theorem.

If some `L_i` is nonempty, then the corresponding nonempty seed remains in
`L_i'`, so

\[
                              |U^*|<|U|.                \tag{3.7}
\]

This is outcome 2 (and contradicts the global extremal choice in the
application).

It remains that every `L_i` is empty.  By definition, each `P_i` then has
no vertex of `C` other than `v`, and its end is `s_i`; hence it is exactly
the edge `vs_i`.  This proves (3.2) and outcome 3.  Thus directness of all
three owner arms is the only obstruction to strict decrease in this fan
transfer. \(\square\)

## 4. Exact contribution and trust boundary

Theorem 2.1 removes endpoint collision from the operation-specific
five-spoke response without losing its prescribed first edges.  It is
stronger for literal first-hit ownership than the component-internal fan in
the operation-coupled response theorem, but it no longer remembers the
bichromatic colour assigned to each path.

Theorem 3.1 closes the exact endpoint pattern consisting of both internal
separator vertices and all three owner representatives, except for the
finite common-portal geometry (3.2).  It does **not** force the five fan
ends to have this pattern.  In particular, when the three non-`K` ends use
one or more nonowner representatives, a further label-allocation or
proper-minor response argument remains necessary.

## 5. Dependencies

- [prescribed first edges and an arbitrary target set](hc7_order8_prescribed_spoke_reduction.md)
- [concentration of the three owner portal sets in one component](hc7_three_owner_reserved_component_concentration.md)
- [rank preservation under multi-owner transfer](hc7_multi_owner_portal_linkage_transfer.md)
