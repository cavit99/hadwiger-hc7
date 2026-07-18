# Superseded draft: rooted cyclic sectors or a small host separator

**Status:** **not proved; independent audit RED.**  This file is retained
only to record the failed route.  Lemma 2.1 has not been established: the
inclusion-minimal-bigon argument does not justify that the cycle side of a
bigon avoids the other paths.  Consequently Theorem 3.1 and Corollary 3.2
must not be cited.  A rigorous replacement reduction is developed in
[`the audited Hamiltonian-cycle reduction`](../results/hc7_rooted_hamiltonian_cycle_reduction.md).

This note isolates the overlap issue in the degree-eight branch of the
two-pair disk configuration.  Its main point is that the connected set used
as the seventh branch set need not be a component of `G-N[v]`.  In the
three-connected disk branch one may instead use a component of the old far
shore, which is automatically disjoint from the disk.  Failure of ordinary
three-connectivity returns an actual host separation of order seven or
eight.

The theorem does **not** prove that the three omitted boundary vertices
have the contact pattern required by the degree-eight contact-allocation
theorem.  It settles only cycle reservation and the seven-label contact of
the reserved connected set.

## 1. Host setup

Let `G` be seven-connected and let

\[
 V(G)=L\mathbin{\dot\cup}T\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
 \qquad |T|=7,                                           \tag{1.1}
\]

where `L,R` are nonempty.  Write

\[
             T=U\mathbin{\dot\cup}B,
             \qquad |U|=4,
             \qquad |B|=3,                              \tag{1.2}
\]

and put

\[
                         H=G[L\cup U].                   \tag{1.3}
\]

Assume that `H` has a plane drawing in a disk, with the four vertices of
`U` on the boundary and every vertex of `H-U` in the open disk, and that
the rooted pair `(H,U)` is internally four-connected: there is no
separation `(X,Y)` of `H` with

\[
 U\subseteq X,
 \qquad Y-X\ne\varnothing,
 \qquad |X\cap Y|\le3.                                  \tag{1.4}
\]

Let `v in L` have degree five in `H`, and write its five neighbours in
their rotation at `v` as

\[
                         c_0,c_1,c_2,c_3,c_4.            \tag{1.5}
\]

In the active degree-eight application, `v` is also adjacent to every
vertex of `B`, and these are all its remaining host neighbours.

## 2. A plane orthogonal-fan lemma

We first record the planar uncrossing used below.

### Failed Lemma 2.1 (orthogonal fan; unproved)

Let `K` be a plane graph, let `r,v` be distinct vertices, and let `F` be a
cycle separating `r` from `v`.  Suppose that

1. there are `k` internally vertex-disjoint `r`--`v` paths; and
2. every neighbour of `v` lies on `F`.

Then the paths may be chosen so that, for every selected path `P`,

\[
                         P\cap F                           \tag{2.1}
\]

is a nonempty connected subpath of `F`.  Subject to that choice, if the
total length of the paths is minimum, then `P \cap F` contains exactly one
neighbour of `v`, namely the penultimate vertex of `P`.

#### Proof

Choose the paths to minimize first

\[
        \sum_P c(P\cap F),                               \tag{2.2}
\]

where `c` denotes the number of connected components, and then their total
number of edges.

We use the standard plane bigon reduction, included here for clarity.
Perturb the drawing in pairwise disjoint small neighbourhoods of vertices
of `F` so that a path which enters and leaves `F` is represented by a
simple arc meeting the Jordan curve `F` transversely; a shared subpath of
`F` is retained as one intersection interval.  If some selected path has
two intersection intervals, an extra excursion between two consecutive
intervals and one subarc of `F` bound a bigon not containing `r` or `v`.
Choose such a bigon inclusion-minimal over the whole path family.  Its
interior contains no selected path.  Indeed, a selected path entering the
bigon must leave it, and an innermost portion between its first and last
crossings would give a strictly smaller bigon.  Its `F`-side also contains
no vertex of another selected path, by the same argument.  Replacing the
excursion by that `F`-subarc, and suppressing any resulting repeated
initial or terminal segment, preserves `k` internally disjoint
`r`--`v` paths and decreases (2.2).

For completeness, if the first bigon displayed by an excursion contains
one endpoint, use the other consecutive excursion of that same path.  If
all excursions of that path are nested around the endpoint, take an
innermost one.  Every other selected path from `r` to `v` which leaves that
innermost region has a first and last crossing of its boundary; switching
the two path tails at those crossings gives an endpoint-free smaller
bigon.  This is the usual two-path tail switch, and again preserves the
set of first edges at `r` and last edges at `v` up to permutation.  Thus an
endpoint-free inclusion-minimal bigon always exists whenever (2.2) is
larger than `k`.

This contradicts the choice in (2.2).  Hence every `P \cap F` is connected.
It is nonempty because `F` separates the two ends.

The last edge of `P` is `cv` for some `c in N_K(v) subseteq V(F)`.  If
`P \cap F` contained an earlier vertex `c' in N_K(v)`, replace the suffix of
`P` beginning at the first such `c'` by the edge `c'v`.  The vertex `c'`
lies on no other selected path, by internal disjointness; the replacement
therefore preserves the path family, does not increase (2.2), and strictly
decreases total length.  This contradicts the secondary choice.  Thus
`P \cap F` contains exactly its penultimate vertex among the neighbours of
`v`.  \(\square\)

The perturbation in this proof is only a way to identify the two boundary
arcs of a bigon.  Every rerouting uses a literal subpath of the graph cycle
`F`; no topological arc is treated as a host edge.

## 3. Four rooted cyclic sectors

### Conjectural statement 3.1 (not proved)

Under the setup of Section 1, assume additionally that `H` is
three-connected.  Then there are five pairwise vertex-disjoint connected
subgraphs

\[
                         C_0,C_1,C_2,C_3,C_4             \tag{3.1}
\]

such that, after cyclic reindexing,

1. `c_i in C_i` for every `i`;
2. `C_i` is adjacent to `C_{i+1}` for every index modulo five; and
3. four of the five sets contain the four distinct vertices of `U`, one
   root in each set.

All five sets lie in `H-v`.

#### Proof

Because `H` is three-connected, `H-v` is two-connected.  The face created
by deleting `v` therefore has a boundary cycle `F`, and `F` contains the
five neighbours in their rotation at `v`.

Add one auxiliary vertex `r` in the outer face and join it to the four
vertices of `U`.  These four edges can be drawn in the outer face and do
not cross.  There is no set of at most three vertices, disjoint from
`{r,v}`, separating `r` from `v`.  Otherwise all roots outside the
separator lie in the `r`-component, while roots in the separator may be
put on that same closed side.  Restricting the resulting separation to
`H` contradicts (1.4).  Menger's theorem consequently supplies four
internally vertex-disjoint `r`--`v` paths.

Since `r` has exactly four neighbours, the paths use the four different
vertices of `U`.  Their penultimate vertices at `v` are four different
members of (1.5).  Apply Lemma 2.1 to `F`.  For the four paths
`P_0,...,P_3`, the sets

\[
                         A_i=P_i\cap F                   \tag{3.2}
\]

are pairwise disjoint subpaths of `F`, each containing exactly one of the
five vertices in (1.5).  Let `c_*` be the unused fifth neighbour.  It lies
in none of the four paths.

Delete `r,v` from every `P_i`.  The four remaining path sets are connected,
pairwise disjoint, and each contains one root of `U` and one selected
neighbour of `v`.  Read their four intersection arcs `A_i` around `F`.
Between every two consecutive arcs is a path segment of `F`.  If such a
segment does not contain `c_*`, add all its internal vertices to the path
set preceding it.  The last edge of the segment then supplies adjacency
to the following path set.

There is a unique intervening segment containing `c_*`.  Along that
segment, add the vertices strictly before `c_*` to the preceding path set,
add the vertices strictly after `c_*` to the following path set, and use
`{c_*}` as the fifth set.  The two edges incident with `c_*` on this
segment supply its adjacencies to those two sets.  These assignments are
disjoint, preserve connectedness, and give a cyclic sequence of five
connected sets.  Relabel that sequence as (3.1).  \(\square\)

### Corollary 3.2 (a disjoint connected set with seven contacts)

Let `R_0` be any component of `G[R]`.  Under the hypotheses of Theorem
3.1, the sets in (3.1) may be chosen together with `R_0` so that

\[
 R_0\cap\left(\{v\}\cup B\cup\bigcup_iV(C_i)\right)=\varnothing          \tag{3.3}
\]

and `R_0` is adjacent to every vertex of `B` and to four distinct sets
among the `C_i`.  Thus it contacts at least seven of the eight labels

\[
                  B\mathbin{\dot\cup}\{C_0,\ldots,C_4\}.                \tag{3.4}
\]

#### Proof

The component `R_0` has no neighbour in `L` and no neighbour in another
component of `G[R]`, so `N_G(R_0) subseteq T`.  If it missed a vertex of
`T`, its neighbourhood would have order at most six and would separate
`R_0` from the nonempty set `L`, contrary to seven-connectivity.  Hence

\[
                              N_G(R_0)=T.                \tag{3.5}
\]

The five sets lie in `H-v=G[L union U]-v`, so (3.3) holds.  Equation
(3.5) gives adjacency to the three singleton labels in `B`, while the four
root-containing sets from Theorem 3.1 give four further distinct contacts.
\(\square\)

This replaces, rather than trims, a component of `G-N[v]` which may meet
the facial cycle.  The old far-shore component is disjoint from the entire
disk from the outset.

## 4. Failure of ordinary three-connectivity

### Theorem 4.1

Under the setup of Section 1, suppose that `H` has a proper separation
`(X,Y)` with

\[
                         Z=X\cap Y,
                         \qquad |Z|\le2.                 \tag{4.1}
\]

Then `G` has an actual nontrivial separation whose boundary has order
seven or eight.  More precisely:

1. if both `X-Y` and `Y-X` contain a vertex of `L`, there is an order-seven
   separation; and
2. otherwise one open side consists only of boundary roots, and the
   construction below gives a separation of order at most eight.

#### Proof

Let `A` be one of the open sides and assume first that

\[
                              A_L=A\cap L\ne\varnothing. \tag{4.2}
\]

Put

\[
                    S_A=B\cup Z\cup(U\cap A).           \tag{4.3}
\]

In `G-S_A`, no vertex of `A_L` has a neighbour outside `A_L` through the
other open side of the separation, through `R`, or through `T`.  The first
assertion is the separation property in `H`, the second is (1.1), and the
third follows because every root of `U` on the `A`-side and every vertex
of `B` has been removed; roots on the other open side cannot have an edge
to `A_L` across the separation.  Thus a component `K_A` of `G-S_A`
contained in `A_L` is separated from the nonempty set `R`.  Consequently

\[
 \bigl(G[V(K_A)\cup N_G(K_A)],\,G-V(K_A)\bigr)          \tag{4.4}
\]

is a genuine nontrivial host separation, with literal boundary
`N_G(K_A) subseteq S_A`.  Seven-connectivity implies

\[
                  7\le |N_G(K_A)|\le |S_A|.             \tag{4.5}
\]

Suppose both open sides meet `L`.  Choose one having at most two of the
roots outside `Z`.  Then

\[
                         |S_A|\le3+2+2=7.                \tag{4.6}
\]

Together with (4.5), this gives an actual order-seven separation.  The
only equality pattern with two roots on each open side has `|Z|=2` and no
root in `Z`; any smaller count would contradict (4.5).

It remains that only one open side meets `L`.  The other open side is a
nonempty subset of the four roots `U`.  Hence the `L`-containing side has
at most three roots outside `Z`.  Applying (4.3) to that side gives

\[
                         7\le |S_A|\le3+2+3=8.           \tag{4.7}
\]

This is the claimed order-seven or order-eight host separation.  In the
order-eight equality, the opposite open side is a root-only lobe, `Z` has
order two, and the `L`-side contains the other three roots outside `Z`.
\(\square\)

### Combined consequence

In the degree-eight two-pair disk setup, at least one of the following
holds.

1. There are five cyclic connected sets containing the five disk
   neighbours of `v`, four of them contain the four distinct roots, and a
   connected old far-shore component is disjoint from them and contacts
   the three omitted boundary vertices plus those four sets.
2. `G` has an actual separation of order seven or eight.

The first outcome removes the facial-cycle/seventh-set overlap completely.
The second is a bounded host interface.  An order-seven interface still
needs a common equality partition on its two closed shores, and an
order-eight interface still needs the separate balanced-boundary
synchronization machinery.

Neither outcome proves that the missing adjacencies between `B` and the
five cyclic sets form a matching of order at most two.  That contact-
distribution condition remains the exact input needed to invoke the
degree-eight cyclic contact-allocation theorem.

## 5. Dependencies

- [closed-shore rooted connectivity](../results/hc7_closed_shore_rooted_connectivity.md)
- [two-pair disk structure](../results/hc7_two_pair_disk_structure.md)
- [degree-eight cyclic contact allocation](../results/hc7_degree8_contact_allocation.md)
