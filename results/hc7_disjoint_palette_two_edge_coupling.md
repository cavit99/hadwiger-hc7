# Disjoint-palette coupling for two critical edges

**Status:** written proof, independently audited in
[`hc7_disjoint_palette_two_edge_coupling_audit.md`](hc7_disjoint_palette_two_edge_coupling_audit.md).
The theorem is uniform for two disjoint three-colour supports.  It couples the two
generalized Kempe forks and forces one edge to have replacement paths in
both cyclic orders.  It does not by itself construct a `K_7` minor; a
ten-vertex sharpness example is recorded in
[`../barriers/hc7_disjoint_palette_two_edge_decoder_barrier.md`](../barriers/hc7_disjoint_palette_two_edge_decoder_barrier.md).

## 1. Coupled forks

Let `G` be a graph which is not `q`-colourable, let

\[
                         e=ab,\qquad f=cd
\]

be vertex-disjoint edges, and put `H=G-{e,f}`.  Let `phi` be a proper
`q`-colouring of `H` with

\[
                 \phi(a)=\phi(b),\qquad \phi(c)=\phi(d). \tag{1.1}
\]

Let `Omega_e,Omega_f` be disjoint three-element colour sets containing the
common colours of `e,f`, respectively.  Choose cyclic permutations
`sigma_e,sigma_f` of these sets.  Orient each edge of
`H[phi^{-1}(Omega_e)]` from `u` to `v` when

\[
                         \phi(v)=\sigma_e(\phi(u)),     \tag{1.2}
\]

and define the analogous orientation on `Omega_f`.  Let `F_e` be the set
reachable from `a` in the first orientation, and let `F_f` be the set
reachable from `c` in the second.

### Theorem 1.1 (disjoint-palette coupling)

The following statements hold.

1. It is impossible that both `b notin F_e` and `d notin F_f`.
2. If `b in F_e` and `d in F_f`, there are vertex-disjoint directed paths
   from `a` to `b` and from `c` to `d` in their prescribed cyclic orders.
3. If, for example, `b notin F_e` and `d in F_f`, rotating
   `sigma_e` on `F_e` gives a proper `q`-colouring of `G-f`, while the
   directed `c-d` path remains present unchanged.  The symmetric statement
   holds after interchanging the two edges.

#### Proof

The reachable-set recolouring for `e` rotates by `sigma_e` every vertex of
`F_e`.  If `b notin F_e`, it makes `e` proper.  The result is a proper
colouring of `H`; because `G` is not `q`-colourable, the ends of `f` must
remain equal.  This is the first response alternative of the generalized
two-edge Kempe fork.  The corresponding statement holds for `f`.

Suppose both opposite endpoints were unreachable.  The two rotated vertex
sets are disjoint because every vertex of `F_e` has a colour in `Omega_e`,
every vertex of `F_f` has a colour in `Omega_f`, and the two colour sets
are disjoint.  The rotations commute.  Moreover, neither rotation changes
an endpoint or a path edge belonging to the other palette.  Performing
both rotations therefore gives a proper colouring of `H` in which both
`e` and `f` are proper.  Restoring the two edges would `q`-colour `G`, a
contradiction.  This proves assertion 1.

If both opposite endpoints are reachable, choose a simple directed path
inside each reachable set.  Their vertex sets are disjoint because their
colour supports are disjoint, proving assertion 2.

Finally suppose only `b` is unreachable.  Its reachable-set rotation gives
the proper colouring of `G-f` just described.  It changes no vertex whose
colour lies in `Omega_f`, so the selected directed `c-d` path and all its
colours remain unchanged.  This proves assertion 3. \(\square\)

### Corollary 1.2 (one edge is locked in both cyclic orders)

For each of `Omega_e,Omega_f`, consider both cyclic orientations.  Then at
least one of the two edges has its opposite endpoint reachable in both
orientations.  Equivalently, one edge has two fixed-end replacement paths,
one in each cyclic order.

#### Proof

If neither edge had the asserted property, some orientation of `Omega_e`
would leave `b` unreachable and some orientation of `Omega_f` would leave
`d` unreachable.  Apply Theorem 1.1 to that pair of orientations, contrary
to assertion 1. \(\square\)

## 2. Two five-cliques

Suppose `q=6`, and suppose `e` belongs to a five-clique

\[
                         L_e=\{a,b,r_1,r_2,r_3\},
\]

while `f` belongs to a vertex-disjoint five-clique

\[
                         L_f=\{c,d,t_1,t_2,t_3\}.
\]

In the colouring (1.1), the three vertices `r_i` have distinct colours and
the two colours absent from `L_e-e`, together with the common colour on
`a,b`, form the natural support `Omega_e`.  Define `Omega_f` analogously.

If these natural supports are disjoint, they partition the six colours.
The three `r_i` use the colours of `Omega_f`, and the three `t_i` use the
colours of `Omega_e`.  Consequently:

1. every replacement path for `e` avoids `r_1,r_2,r_3`;
2. every replacement path for `f` avoids `t_1,t_2,t_3`; and
3. every selected `e`-path is vertex-disjoint from every selected `f`-path.

Corollary 1.2 therefore supplies a label-preserving replacement of one
clique edge in both cyclic orders.  If the other edge is locked in either
orientation, its path is automatically disjoint from both paths on the
first edge.  If it is unlocked, Theorem 1.1 instead supplies the opposite
one-edge-restoration colouring while preserving the locked path.

The cross-intersections are not controlled: an `e`-path may use vertices
among `t_1,t_2,t_3`, and an `f`-path may use vertices among
`r_1,r_2,r_3`.  This is precisely why the conclusion is not yet a pair of
disjoint labelled `K_5` models.

## 3. Application boundary

In the balanced order-eight configuration, the natural support for
`g=ell_e ell_f` is the complement of the three colours on the reserved
triangle `R`.  If the natural support for the opposite clique edge `h` is
disjoint from it, Theorem 1.1 and Corollary 1.2 apply without identifying
palette colours with branch-set labels.

The theorem is a real coupling unavailable from two independent fork
applications: two response rotations on disjoint palettes are forbidden,
and one named edge is simultaneously locked in both cyclic directions.
The barrier cited at the start shows that even the stronger outcome in
which both edges are locked in both directions does not force a `K_7`
minor from the two clique/path systems alone.  A successful completion must
also use seven-connectivity, the literal two-endpoint defect edges at the
order-eight boundary, or the incompatibility of the two proper-minor
boundary traces.
