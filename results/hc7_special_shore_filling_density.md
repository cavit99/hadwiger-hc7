# Density and block structure in the special shore-filling list-critical core

**Status:** written proof; separate internal audit GREEN in
[`hc7_special_shore_filling_density_audit.md`](hc7_special_shore_filling_density_audit.md).
This theorem sharpens the all-tight order bound in the special five-plus-two
exact-seven interface from eighteen vertices to eleven and describes its
block structure.  It does not bound total positive list-degree excess,
settle the bounded residue, or prove `HC_7`.

## 1. Setting and notation

Assume the complete shore-filling case `K=A` of the audited
[special exact-seven two-edge list-critical reduction](hc7_special_exact7_two_edge_list_core.md).
Thus

\[
 V(G)=A\mathbin{\dot\cup}Y\mathbin{\dot\cup}B,
 \qquad |Y|=7,
 \qquad E_G(A,B)=\varnothing,
\tag{1.1}
\]

`G` is seven-connected and `K_7`-minor-free, `A,B` are nonempty, and the
double-contraction colouring `\psi` defines lists

\[
 \mathcal L(v)=[6]\setminus
   \{\psi(y):y\in N_G(v)\cap Y\}
 \qquad(v\in A).
\tag{1.2}
\]

The graph `G[A]` is connected, is minimally non-`\mathcal L`-colourable,
and contains the two marked vertices of the simultaneous contraction.
Put

\[
\begin{aligned}
 c(v)&=|\{\psi(y):y\in N_G(v)\cap Y\}|,\\
 \rho(v)&=|N_G(v)\cap Y|-c(v),\\
 \varepsilon(v)&=d_{G[A]}(v)-|\mathcal L(v)|,\\
 C&=\sum_{v\in A}c(v),\qquad
 P=\sum_{v\in A}\rho(v),\qquad
 E=\sum_{v\in A}\varepsilon(v),\\
 \Delta&=\sum_{v\in A}(d_G(v)-9),\\
 r&=|A|,\qquad s=|E(G[Y])|,
 \qquad a=\operatorname{comp}(G[B]).
\end{aligned}
\tag{1.3}
\]

## 2. Palette-incidence density

### Theorem 2.1

Either some vertex of `A` has degree seven or eight, or `\Delta\ge0` and

\[
                         11r+9\Delta\le128+5E.
\tag{2.1}
\]

In particular, if `E=0`, then

\[
                              |A|\le11.
\tag{2.2}
\]

#### Proof

The low-degree alternative is an actual singleton-side separation, as in
the two-edge list-critical theorem.  Assume it does not occur.  Every
vertex of `A` then has degree at least nine and `\Delta\ge0`.

Let `\Pi` be the exact boundary partition induced by `\psi`.  The special
two-edge response theorem gives

\[
                         d_{G[Y]}(\Pi)>\nu_B\ge1.
\tag{2.3}
\]

No colour class of `\Pi` has order six or seven.  A seven-vertex block has
demand one, while a six-vertex block leaves one singleton and again has
demand `2-1=1`, contradicting (2.3).  Hence every boundary colour class
has order at most five.

For a fixed vertex `v\in A`, every boundary colour seen at `v` occurs on at
most five boundary neighbours.  Beyond the first such neighbour it can
therefore contribute at most four repetitions.  Summing first over the
seen colours and then over `A` gives

\[
                              P\le4C.
\tag{2.4}
\]

The exact degree identity in the shore-filling core gives

\[
                              P=3r+\Delta-E.
\tag{2.5}
\]

The boundary is four-colourable and, by the audited selected-response
preservation theorem, nonsplit.  In particular it has at least two edges,
so `s\ge2`; also `a\ge1`.  The audited surplus-sensitive Mader calculation
gives

\[
              2r+C-E+2s+2\Delta+4a\le40.
\tag{2.6}
\]

Equations (2.4)--(2.5) imply

\[
                         C\ge\frac{3r+\Delta-E}{4}.
\tag{2.7}
\]

Using `s\ge2` and `a\ge1` in (2.6), substituting (2.7), and multiplying by
four gives exactly

\[
                         11r+9\Delta-5E\le128.
\]

This is (2.1).  If `E=0`, then `\Delta\ge0` and
`r\le\lfloor128/11\rfloor=11`, proving (2.2).
\(\square\)

## 3. The all-tight Gallai-tree branch

### Theorem 3.1

Assume `E=0` and that no vertex of `A` has degree seven or eight.  Then
`G[A]` is a Gallai tree of order at most eleven.  Moreover, at least one of
the following holds.

1. An endblock lobe has a full neighbourhood of order exactly seven.
2. The block-cutvertex tree of `G[A]` is a path whose two endblock lobes are
   both `Y`-full.
3. `G[A]` consists of one block and is isomorphic to `K_4` or `K_5`.

Here outcome 2 is the multi-block case.  Thus the unbounded all-tight
residue has been reduced to a block path on at most eleven vertices.

#### Proof

Every `\varepsilon(v)` is nonnegative.  The equality `E=0` therefore gives
`\varepsilon(v)=0` at every vertex.  The audited degree-choosability
argument makes `G[A]` a Gallai tree.  Theorem 2.1 gives `|A|\le11`.

Suppose first that `G[A]` has more than one block.  Let `D` be an endblock,
let `w` be its unique cutvertex in `G[A]`, and put

\[
                              Q=V(D)-\{w\}.
\tag{3.1}
\]

The lobe `Q` is nonempty and connected, and

\[
                         N_G(Q)\subseteq\{w\}\cup Y.
\tag{3.2}
\]

It is separated from the nonempty opposite shore `B`, so
seven-connectivity gives `|N_G(Q)|\ge7`.  The cutvertex `w` has a neighbour
in `Q`; consequently `Q` has at least six boundary contacts.  Six contacts
give outcome 1.  Otherwise `Q` is adjacent to all seven vertices of `Y`.

Distinct endblock lobes are vertex-disjoint.  The special exact-seven
packing theorem gives `\nu_A\le2`, so absent outcome 1 the block-cutvertex
tree has exactly two leaves.  A finite tree with exactly two leaves is a
path, proving outcome 2.

It remains to consider the one-block case.  A Gallai block is a complete
graph or an odd cycle.  If `G[A]=K_n`, tightness gives lists of order
`n-1`.  An uncolourable degree-sized list assignment on `K_n` has all lists
equal: otherwise Hall's condition gives distinct representatives for the
vertices.  Both marked vertices `a_1,a_2` use their distinct `\psi`-colours
outside this common list, because

\[
 \psi(a_i)=\psi(z_i),
 \qquad z_i\in N_G(a_i)\cap Y.
\tag{3.3}
\]

The six-colour palette therefore contains the common `(n-1)`-set and two
further colours, so `n+1\le6` and `n\le5`.  The case `K_2` has whole degree
at most eight.  In `K_3`, degree at least nine forces every vertex to meet
all seven boundary vertices, producing three disjoint `Y`-full singleton
subgraphs, contrary to `\nu_A\le2`.  The two marked vertices already
exclude `K_1`.  Thus only `K_4,K_5` remain.

Finally, if the one block is an odd cycle, every vertex has internal degree
two.  Degree at least nine forces all seven boundary neighbours at every
vertex, and any three cycle vertices again give three disjoint `Y`-full
singletons.  This contradicts `\nu_A\le2`.  Hence the odd-cycle case is
impossible, and outcome 3 holds.
\(\square\)

## 4. Exact scope

The coefficient `E` in (2.1) is not bounded by the local two-root
list-critical data.  The audited odd-wheel barrier realizes arbitrarily
large list-degree excess under closely related local hypotheses; it exits
through a `K_7` minor and is not a counterexample, but it prevents a purely
local excess argument.

Outcome 1 of Theorem 3.1 is an actual order-seven separation, not a common
complete boundary colouring.  Outcome 2 is a finite block-path reduction,
not an elimination.  No conclusion here allocates palette colours to
inherited branch-set labels or proves `HC_7`.

## 5. Dependencies

- [special exact-seven two-edge list-critical reduction](hc7_special_exact7_two_edge_list_core.md)
- [surplus-sensitive density inequality](hc7_direct_entry_surplus_density.md)
- [selected-response nonsplit boundary](hc7_exact7_selected_response_preservation.md)
- [exact-seven full-subgraph packing](hc7_exact_seven_packet_packing.md)
- [unbounded list-excess barrier](../barriers/hc7_two_mark_list_excess_barrier.md)
