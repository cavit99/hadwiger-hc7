# Concentration of three lost branch-set adjacencies in one component

**Status:** written proof; separate internal audit GREEN in
[`hc7_three_owner_reserved_component_concentration_audit.md`](hc7_three_owner_reserved_component_concentration_audit.md).
This theorem
strengthens the three-label order-eight normal form by using the global
lexicographic choice of the labelled minor model.  It forces all three lost
branch-set adjacencies through one distinguished component and then returns
two disjoint, differently labelled critical contact edges.  It does not
convert their colour responses into a labelled linkage and does not prove
`HC_7`.

## 1. Setting

Use the hypotheses and notation of the audited
[reserved-component theorem](hc7_reserved_component_linkage_completion.md).
Thus `G` is seven-connected, seven-chromatic, `K_7`-minor-free, and every
proper minor is six-colourable.  There is a spanning labelled
`K_7`-minus-one-edge model

\[
                 X,Y,D,U,F_1,F_2,F_3,                 \tag{1.1}
\]

whose only possible missing branch-set adjacency is `X-Y`, with

\[
                    U=W\mathbin{\dot\cup}U'.           \tag{1.2}
\]

The fixed connected response subgraph lies in `D`, and a fixed edge joins it
to a vertex of `U'`.  The prescribed root of `U` also lies in `U'`.

Among every model compatible with these roots, the selected boundary
partition and the fixed response subgraph, first maximize the relaxed
literal first-hit rank `lambda` and then minimize `|U|`.

Assume that the complete owner set is an inclusion-minimal deficient family

\[
                 \Omega(W)=I=\{R_1,R_2,R_3\},          \tag{1.3}
\]

where the owner branch sets belong to `{X,Y,F_1,F_2,F_3}`.  Put

\[
 B=N_G(U')\cap W,
 \qquad A_R=N_G(R)\cap W\quad(R\in I).                \tag{1.4}
\]

Let `K={k_1,k_2}` be the minimum Rado--Menger transversal, so every
`B`--`A_I` path in `G[W]` meets `K`, while every two-owner subfamily has a
full labelled linkage.  Let `C` be a component of `G[W-K]` satisfying the
order-eight no-repeated-contact normal form:

\[
 E_G(C,U')=\varnothing,
 \quad N_{G[W]}(C)=K,
 \quad |N_G(C)|=8,                                   \tag{1.5}
\]

and `C` is adjacent to all six branch sets different from `U`.

An owner `R` will be called **`C`-exclusive** when

\[
                         A_R\subseteq C.               \tag{1.6}
\]

This term refers only to the literal location of the old `U-R` model
contacts.

## 2. Connected retained donor

### Lemma 2.1

The vertex set

\[
                  U_0=U'\cup(W-C)                     \tag{2.1}
\]

induces a connected subgraph and is adjacent to `C`.

#### Proof

Choose the full linkage for any two owners.  Its two paths start at distinct
vertices of `B`, are vertex-disjoint, and each must meet `K`.  Since
`|K|=2`, the two paths use the two vertices of `K` separately.  Before its
first vertex of `K`, neither path can enter `C`, because the whole
`G[W]`-neighbourhood of `C` is `K`.  Thus each `k_i` is joined inside
`W-C` to a vertex of `B`, and hence by one more edge to connected `U'`.

Every component of `G[W-K]` other than `C` has a neighbour in `K`, because
`G[W]` is connected.  It follows that every vertex of `W-C` lies in the
same component as `U'`, proving that `G[U_0]` is connected.  Finally `C` has
a neighbour in `K subseteq U_0`, proving the last assertion. \(\square\)

## 3. Complete concentration

### Theorem 3.1

Every owner is `C`-exclusive:

\[
                       A_{R_1}\cup A_{R_2}\cup A_{R_3}
                       \subseteq C.                    \tag{3.1}
\]

#### Proof

We show that zero, one or two `C`-exclusive owners would contradict the
lexicographic choice of the model (or immediately give a `K_7` minor).

Suppose first that no owner is `C`-exclusive.  Retain `U_0` as the new donor
and enlarge `D` to `D\cup C`.  The enlarged set is connected because `C`
meets `D`.  The new donor is adjacent to every owner through a portal in
`W-C`, to every nonowner through `U'`, and to `D\cup C` through the fixed
response edge from `D` to `U'`.

Suppose next that exactly one owner `R` is `C`-exclusive.  Retain `U_0` as
the donor and enlarge `R` to `R\cup C`.  This set is connected through an
`A_R` portal, and it is adjacent to `U_0` through an edge from `C` to `K`.
Every other owner has a portal in `W-C`.

In either case all other old branch-set adjacencies and all prescribed roots
remain.  If the reassignment repairs `X-Y`, the seven sets form an explicit
`K_7`-minor model.  Otherwise it gives another compatible spanning labelled
`K_7`-minus-one-edge model with donor `U_0`.

The relaxed first-hit rank does not decrease in that model.  A ranked path
whose label is not `U` avoided all of the old donor and hence avoids `C`.
A ranked `U`-path ending in `C` can be replaced inside the fixed connected
response subgraph by the fixed edge into `U'`, exactly as in the audited
rank-preserving transfer theorem.  Thus maximality of `lambda` and then
`|U_0|<|U|` give a contradiction.

It remains to exclude exactly two `C`-exclusive owners, say `R_1,R_2`.
Take their full two-owner linkage.  Each of its two paths uses one different
vertex of `K` and terminates in `C`.  After its unique vertex of `K`, a path
enters `C` and cannot leave it: leaving would require a second vertex of
`K`, already used by the other disjoint path.  Let `T_1,T_2` be the two
disjoint terminal tails inside `C`.

Every component of

\[
                         C-(T_1\cup T_2)               \tag{3.2}
\]

has an edge to at least one tail.  Assign each such component to one
adjacent tail.  This partitions `C` into connected sets

\[
                         C=L_1\mathbin{\dot\cup}L_2,   \tag{3.3}
\]

where `L_i` contains an `R_i` portal and has an edge to `U_0` through the
corresponding vertex of `K`.

Replace `R_i` by `R_i\cup L_i` and replace `U` by `U_0`.  The third owner
has a portal in `U_0` because it is not `C`-exclusive.  Hence every donor
adjacency is restored.  Connectedness, the old outside adjacencies and all
prescribed roots are retained.  As above, either `X-Y` is repaired, giving
a `K_7` model, or this is a compatible labelled model with the same maximum
rank and a strictly smaller donor.  Both outcomes are impossible.

All three owners are therefore `C`-exclusive, proving (3.1). \(\square\)

## 4. The exact two-edge response substrate

### Corollary 4.1

For any two distinct owners `R_i,R_j`, there are vertex-disjoint edges

\[
                         e=a_ir_i,\qquad f=a_jr_j,     \tag{4.1}
\]

where `a_i,a_j` are distinct vertices of `C` and `r_i in R_i`,
`r_j in R_j`.  Put `H=G-{e,f}`, where the operations are edge deletions.
Then `H` is connected, and its six-colourings have the exact signatures

\[
              ({\rm equal},{\rm equal}),
              \quad({\rm equal},{\rm proper}),
              \quad({\rm proper},{\rm equal}),        \tag{4.2}
\]

while `({\rm proper},{\rm proper})` is impossible.  Moreover, either the
four endpoints of `e,f` induce a `K_4` in `G`, or `H` is six-chromatic and
has a spanning `K_6`-minor model.

#### Proof

The proper two-owner subfamily has a full linkage.  By (3.1), its two
terminal vertices lie in `C`; vertex-disjointness makes them distinct.
Choose the two terminal contact edges into the two disjoint owner branch
sets.  This gives (4.1).

Seven-connectivity implies seven-edge-connectivity, so deleting two edges
does not disconnect `G`.  The double-contraction colouring of `G/e/f`
expands to the first signature in (4.2).  Colourings of `G/e` and `G/f`
give the two opposite one-proper signatures.  A six-colouring proper on both
deleted edges would extend to `G`, so the fourth signature is impossible.
The final alternative is the audited common edge-deletion `K_6` fork. \(\square\)

## 5. Exact remaining gap

The theorem reduces the three-owner order-eight obstruction to a single
component containing all three owner portal sets and to two literal critical
edges with different branch-set labels.  It still does not identify any
palette colour with a model label.  In particular:

- bichromatic lock paths for different colours may first enter the same
  branch set;
- those paths need not be mutually disjoint;
- the two one-proper colourings in (4.2) may induce different boundary
  partitions; and
- the spanning `K_6` model in `H` need not respect the six inherited model
  labels.

A proof-closing continuation must use this operation-specific package to
reroute a two-owner linkage away from `C`, preserve a connected residual of
`C` with all six outside contacts, or return an exact order-seven separator
with a partition-specific connected support system on the legally coloured
shore.

## 6. Dependencies

- [reserved-component linkage completion and order-eight normal form](hc7_reserved_component_linkage_completion.md)
- [rank preservation under branch-set transfer](hc7_first_hit_rank_preserving_branch_set_transfer.md)
- [multi-owner portal linkage transfer](hc7_multi_owner_portal_linkage_transfer.md)
- [common edge-deletion `K_6` fork](hc7_common_edge_deletion_k6_fork.md)
- [common-host double-contraction response](hc7_common_host_double_contraction_lock_allocation.md)
