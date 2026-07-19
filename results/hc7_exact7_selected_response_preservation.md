# Exact preservation criterion for a selected response at a seven-vertex separator

**Status:** written theorem and strategic application; separate internal audit
GREEN in
[`hc7_exact7_selected_response_preservation_audit.md`](hc7_exact7_selected_response_preservation_audit.md).
This note isolates a checkable host-level certificate which turns a
one-sided boundary response into a common boundary colouring.  It also
records why contraction-criticality and the existence of an order-seven
separator do not supply that information automatically.  Nothing here
proves `HC_7`.

## 1. A partition-specific rooted carrier system

Let

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}B,
 \qquad E_G(A,B)=\varnothing,
 \qquad A,B\ne\varnothing.                              \tag{1.1}
\]

Let `Pi` be a partition of `S` into independent sets, using at most `q`
blocks.  Choose a clique `U` in `G[S]` such that every member of `U` is a
singleton block of `Pi`.  List all remaining blocks of `Pi` as

\[
                         B_1,\ldots,B_m.                 \tag{1.2}
\]

Assume `m>=1`.

A **`Pi`-carrier system in `A` relative to `U`** consists of pairwise
vertex-disjoint nonempty connected subgraphs

\[
                         P_1,\ldots,P_m\subseteq G[A]    \tag{1.3}
\]

such that, on putting `Z_i=V(P_i) union B_i`,

1. every `Z_i` is connected;
2. the sets `Z_1,...,Z_m` are pairwise adjacent in `G`; and
3. every `Z_i` is adjacent to every vertex of `U`.

This definition is partition-specific.  It neither requires any `P_i` to
be adjacent to every boundary vertex nor identifies a palette colour with
a minor-model label.

### Theorem 1.1 (exact response reflection)

Assume that every proper minor of `G` is `q`-colourable.  Suppose that
`G[A union S]` has a proper `q`-colouring whose equality partition on the
literal boundary is exactly `Pi`, and that `A` contains a `Pi`-carrier
system relative to `U`.

Then `G[B union S]` also has a proper `q`-colouring whose equality
partition on `S` is exactly `Pi`.  Consequently `G` is `q`-colourable.

Independently of the colouring assumption, if a partition and connected
sets satisfy the three carrier conditions with `m+|U|=q+1` (dropping the
at-most-`q` restriction), the `Z_i` and the singleton vertices of `U` are
the branch sets of a `K_{q+1}` minor.

#### Proof

For every `i`, contract a spanning tree of the connected set `Z_i`.  At
least one boundary--open-side edge is contracted, so the resulting minor
`M` is proper.  Let `z_i` denote the image of `Z_i`.

The vertices

\[
                         z_1,\ldots,z_m,\quad U          \tag{1.4}
\]

form a clique in `M`.  The three requirements in the definition supply,
respectively, valid branch sets, the adjacencies between their images, and
the adjacencies to the literal singleton vertices in `U`; the vertices of
`U` are mutually adjacent by choice.  There is one vertex in (1.4) for
every block of `Pi`.

Since `Pi` has at most `q` blocks, take a proper `q`-colouring of `M`.
The clique (1.4) gives different colours to different blocks.  The
independent `q+1`-block assertion follows directly from the same connected
sets before contraction.

Keep this minor colouring on the untouched open side `B` and on `U`.  For
each literal vertex `s in B_i`, give `s` the colour of `z_i`.  This is
proper on `G[B union S]`: `B_i` is independent, and every edge from a
vertex of `B_i` to an untouched vertex is represented by an edge incident
with `z_i` in the minor.  The clique (1.4) makes the induced equality
partition exactly `Pi`, rather than a coarsening.

The given colouring of `G[A union S]` has the same exact partition.
Permute its used colour names to agree with the new colouring on every
block of `Pi`, and extend this partial bijection arbitrarily to the whole
palette.  The two colourings now agree literally on `S` and glue because
there are no `A`--`B` edges.  This proves the theorem. \(\square\)

## 2. The paired direct-entry specialization

The direct-entry residue has a proper boundary partition of the form

\[
 \Pi=M\mid\{x\}\mid\{y\}\mid\{k\}\ (k\in K),
 \qquad
 S=M\mathbin{\dot\cup}\{x,y\}\mathbin{\dot\cup}K,     \tag{2.1}
\]

where `M` is independent, `K` is a clique, `xy` is a nonedge, and

\[
                         (|M|,|K|)\in\{(2,3),(3,2)\}.    \tag{2.2}
\]

For a block `D in {M,{x},{y}}`, define its literal duty relative to `K` by

\[
 D_K(D)=D\cup\{k\in K:E_G(k,D)=\varnothing\}.          \tag{2.3}
\]

### Corollary 2.1 (two full subgraphs and one duty carrier preserve `Pi`)

In the setting of Theorem 1.1, suppose `A` contains two disjoint connected
subgraphs `P_1,P_2`, each adjacent to every vertex of `S`.  If, for some
`D in {M,{x},{y}}`, there is a connected subgraph

\[
       Z\subseteq G[A-(V(P_1)\cup V(P_2))]              \tag{2.4}
\]

adjacent to every literal vertex of `D_K(D)`, then the partition `Pi`
extends through both closed shores and `G` is `q`-colourable.

#### Proof

Assign `Z` to the block `D`, and assign `P_1,P_2` to the other two members
of `{M,{x},{y}}`.  Each block union is connected.  The two boundary-full
subgraphs supply every adjacency between different block unions and every
adjacency from their own block unions to `K`.  For `Z union D`, an
adjacency to `k in K` is supplied either by a boundary edge from `D` to
`k`, or by the stipulated contact of `Z` with `k` when no such edge exists.
Thus these three subgraphs form a `Pi`-carrier system relative to `K`, and
Theorem 1.1 applies. \(\square\)

This is the exact state-preservation condition already implicit in the
demand-set reflection theorem.  A generic connected subgraph of small
boundary defect is not enough: the connected subgraph must meet one
specific duty set, and the two boundary-full subgraphs must survive on the
same side of the returned separator.

## 3. What the selected two-edge colouring does and does not preserve

Let `e,f` be the two direct-entry edges and let `psi` be the expansion of a
`q`-colouring after contracting both.  It is a proper colouring of
`G-{e,f}`.  For a new separator `T`, the assignment `psi|T` is useful only
when it is the boundary trace of a proper colouring of at least one
**original** closed shore.  This requires that every failed edge which is
present in that closed shore be repaired while retaining `psi|T`; merely
having the same assignment on both restrictions is not enough.

### Lemma 3.1 (failed-edge placement)

Assume both ends of each of `e,f` have one colour under `psi`, as they do
after expanding the two contractions.  For a closed shore `G[A union S]`,
the raw restriction of `psi` is proper if and only if neither failed edge
belongs to `E(G[A union S])`.  In particular:

1. a failed edge contained in `S` makes both raw closed-shore restrictions
   improper;
2. if one failed edge belongs exclusively to each of the two closed shores,
   both restrictions are improper; and
3. if both failed edges belong only to one closed shore, the opposite
   restriction is proper and supplies the oriented one-sided trace needed
   by Theorem 1.1.

#### Proof

Every edge other than `e,f` is proper under `psi`.  Each failed edge is
monochromatic.  The assertion therefore follows by checking which of the
two induced closed shores contains each failed edge. \(\square\)

There are therefore two logically separate requirements for this
contraction-and-reflection mechanism.

1. **Trace legality.**  One original closed shore must have a proper
   colouring with the selected boundary partition.  If a failed edge lies
   inside the boundary, the selected assignment is not even a proper
   boundary colouring.  If one failed edge lies in each closed shore, both
   displayed restrictions may be improper.
2. **Partition-specific geometry.**  On a shore which has that proper
   trace, a carrier system for the complete partition is a sufficient
   geometric certificate.  In the paired residue, it is enough to retain
   the two boundary-full subgraphs and one disjoint connected subgraph
   meeting a duty set (2.3).

Contraction-criticality guarantees colourings after each proper minor
operation.  It does not guarantee that any of those colourings retains a
previously selected trace.  Indeed, for operations internal to opposite
open shores, the proper-minor boundary response languages are necessarily
disjoint: equality would glue the two unchanged closed-shore restrictions
and colour `G`.

Consequently, in a hypothetical counterexample, any one-sided proper
partition `Pi` satisfies the following obstruction law.  If the same
coloured shore contains `nu` disjoint boundary-full connected subgraphs,
then

\[
                         d_{G[S]}(\Pi)>\nu,              \tag{3.1}
\]

Here

\[
 d_{G[S]}(\Pi)
   =|\Pi|-\omega\bigl(G[S][\operatorname{sing}(\Pi)]\bigr)
                                                               \tag{3.2}
\]

is the exact full-subgraph demand.  The reverse inequality is precisely
the boundary-full special case of Theorem 1.1.

## 4. Why criticality plus an order-seven separator is insufficient

The audited boundary-operation parity construction gives a
seven-connected, seven-chromatic graph with an actual seven-vertex
separator, connected boundary-full open shores, and disjoint six-colouring
extension languages.  A concrete one-sided partition still fails on the
opposite closed shore even though

- deletion or contraction of every boundary edge is six-colourable;
- deletion of either selected separator vertex is six-colourable; and
- every contraction of an open shore together with a prescribed
  independent boundary block is six-colourable.

The construction deliberately contains a `K_7` minor and is not globally
minor-minimal.  It therefore does not refute the intended `HC_7` theorem.
It proves that boundary queries, boundary fullness and exact separator
order do not by themselves force the selected partition on both shores.

The separate two-edge deletion-lattice barrier gives the complementary
warning:
the three natural single- and double-deletion responses need not generate
the fourth boundary partition even abstractly.  Thus state preservation
cannot be obtained from the response lattice alone.  No one construction
cited here simultaneously realizes the complete direct-entry geometry,
global minor-criticality, seven-connectivity and `K_7`-minor exclusion;
that conjunction remains the live positive setting.

The remaining positive theorem must spend information absent from these
barriers.  In the first-hit formulation, one sufficient assertion matching
the live mechanism is:

> a deficient labelled first-hit certificate which lifts to an order-seven
> separator either preserves a proper one-sided trace together with the
> two boundary-full subgraphs and produces a connected subgraph meeting one
> exact duty set, or it gives an explicit `K_7`-minor model or a strict
> response-preserving descent.

The phrase “preserves a response” must include trace legality and either an
actual opposite-shore extension or a sufficient literal certificate such
as the duty-carrier geometry above.  Preserving only the equality partition
as an assignment, only one exact block, or only the five palette colours is
insufficient.

## 5. The live exact-seven normal form

The orientation of the two direct-entry responses matters.  In the old
exact-seven separation, the original partition `Pi` properly colours the
closed rich shore, and its two boundary-full connected subgraphs also lie
in that rich shore.  The simultaneous-contraction partition `Omega` is
different from `Pi` and properly colours the opposite closed shore.  The
old two boundary-full subgraphs therefore cannot be used to reflect
`Omega`: Theorem 1.1 requires the proper one-sided trace and its carrier
system on the same shore.

Consequently, a first-hit separator can close in either of two genuinely
different ways.

1. It retains a proper `Pi`-colouring and, on that same shore, retains the
   two boundary-full connected subgraphs and creates a third connected
   subgraph meeting one exact duty set.  Corollary 2.1 then reflects `Pi`.
2. It retains a proper `Omega`-colouring and creates an `Omega`-carrier
   system on the `Omega`-coloured shore.  The old rich-shore subgraphs do
   not supply this conclusion merely because they survive elsewhere in
   the graph.

If the two failed direct-entry edges lie on opposite closed shores of the
new separation, the displayed simultaneous-contraction assignment may be
improper on both.  A trace-preserving repair of one failed edge is then a
prerequisite to either outcome.

The following packages the resulting normal form precisely.

### Corollary 5.1 (oriented exact-seven obstruction)

Suppose `G` is seven-connected, `chi(G)=7`, and every proper minor of `G`
is six-colourable.  Let (1.1) be an actual separation with `|S|=7`, and
suppose `G[A union S]` has a proper six-colouring with exact boundary
partition `Pi`.  Let `nu_A` be the maximum number of pairwise disjoint
boundary-full connected subgraphs in `A`.  Then:

1. `d_{G[S]}(Pi)>nu_A`;
2. if `chi(G[S])<=4`, then `G[S]` is nonsplit; and
3. if `Pi` has the paired form (2.1) and `A` contains two fixed disjoint
   boundary-full connected subgraphs, every connected subgraph in `A`
   disjoint from them misses at least one literal vertex of every duty set
   (2.3).

#### Proof

For item 1, choose a maximum clique among the singleton blocks of `Pi`.
The number of remaining blocks is `d_{G[S]}(Pi)`.  If it were at most
`nu_A`, assign distinct boundary-full connected subgraphs to the remaining
blocks.  They form the carrier system of Theorem 1.1, contradicting
`chi(G)=7`.

For item 2, every component of either open shore is boundary-full: if a
component missed one literal boundary vertex, its neighbourhood would
have order at most six, contrary to seven-connectivity.  Given any nonempty
independent set `I` of `G[S]`, contract one such component together with
`I`.  A six-colouring of the proper minor, restricted to the opposite
closed shore and expanded over `I`, has `I` as an exact boundary block.
The same argument in the opposite orientation shows that both shore
extension languages meet every exact-block cylinder.  The audited
split-boundary synchronization theorem, with `chi(G[S])<=4`, now excludes
a split `G[S]`.

Item 3 is the contrapositive of Corollary 2.1. \(\square\)

Thus a tight first-hit certificate does not merely return an order-seven
separator.  To be terminal, it must also return a proper oriented trace
and the partition-specific connected-subgraph certificate on the shore
carrying that trace.  Otherwise it is only another separator normal form.

## 6. Dependencies and trust boundary

- [adaptive exact-seven connected-subgraph reflection](../results/hc7_exact7_adaptive_packet_reflection.md)
- [demand-set reflection at the paired residue](../results/hc7_exact7_demand_set_separator_descent.md)
- [opposite-shore incompatibility of proper-minor responses](../results/hc_opposite_shore_minor_response_incompatibility.md)
- [two-edge list-critical direct-entry descent](../results/hc7_direct_entry_two_edge_list_core.md)
- [boundary-operation parity barrier](../barriers/hc7_exact7_separator_boundary_operation_parity_barrier.md)
- [two-edge deletion-lattice barrier](../barriers/hc7_two_edge_deletion_lattice_barrier.md)
- [split-boundary synchronization](../results/hc7_split_boundary_synchronization.md)

Theorem 1.1 is parameter-uniform and host-level, but its hypotheses already
contain the rooted connected-subgraph geometry needed for the contraction.
It does not prove that a deficient first-hit gammoid certificate supplies
that geometry.  Corollary 2.1 does not preserve the two full subgraphs after
an arbitrary new separator is chosen.  Those are exactly the remaining
first-hit/exposure obligations.
