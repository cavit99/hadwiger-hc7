# Fixed-trace alternatives for two repeated-exposure edges

**Status:** written proof; separate internal audit GREEN in
[`hc7_repeated_exposure_fixed_trace_fork_audit.md`](hc7_repeated_exposure_fixed_trace_fork_audit.md).
This note couples the
two persistent critical edges returned by labelled first-hit exposure to one
selected boundary colouring.  It proves an exact fixed-trace trichotomy and
shows that, in the common double-equality branch, every Kempe recolouring
which repairs one edge must meet the literal boundary.  It does not allocate
those boundary hits to five distinct model branch sets, construct a
`K_7`-minor model, or prove `HC_7`.

## 1. Fixed boundary colouring and notation

Let `q>=2`, let `G` be a graph which is not `q`-colourable, and suppose

\[
             V(G)=A\mathbin{\dot\cup}X\mathbin{\dot\cup}D,
             \qquad E_G(A,D)=\varnothing .                     \tag{1.1}
\]

Let `c` be a proper `q`-colouring of `G[A\cup X]`.  For `v\in D` put

\[
             L(v)=[q]-c(N_G(v)\cap X).                         \tag{1.2}
\]

Then `G[D]` is not `L`-colourable, since an `L`-colouring would glue to
`c` and colour `G`.

Let `e` and `f` be two distinct edges of `G[D]`.  They may be
vertex-disjoint or incident.  Say that an edge `g\in\{e,f\}` **attains the
fixed trace** when `G[D]-g` is `L`-colourable.  Equivalently, `G-g` has a
proper `q`-colouring agreeing with `c` on the labelled boundary `X`.

### Lemma 1.1 (trace attainment depends only on the equality partition)

An edge `g` attains the fixed trace if and only if some proper
`q`-colouring of `G-g` induces on `X` the same equality partition as `c`.

#### Proof

Only the reverse implication needs proof.  The two boundary colourings use
one distinct palette colour for each block of their common equality
partition.  The bijection which sends the colour of every block in the
new colouring to its colour under `c` extends to a permutation of `[q]`.
Apply that permutation to the whole colouring of `G-g`.  The resulting
proper colouring agrees with `c` at every literal vertex of `X`, and hence
attains the fixed trace. \(\square\)

## 2. Exact fixed-trace fork

### Theorem 2.1 (single attainment, common equality, or common rejection)

Exactly one of the following alternatives holds.

1. **Single-edge attainment.**  At least one of `e,f` attains the fixed
   trace.  Every attained edge belongs to every induced non-`L`-colourable
   subgraph of `G[D]`.
2. **Common fixed-trace equality.**  Neither single edge attains the fixed
   trace, but `G[D]-\{e,f\}` is `L`-colourable.  Every `L`-colouring of
   `G[D]-\{e,f\}` makes the two ends of `e` equal and the two ends of `f`
   equal.  Gluing to `c` therefore gives a proper `q`-colouring `psi` of
   `G-\{e,f\}` with both endpoint equalities and with

   \[
                              \psi|_X=c|_X.             \tag{2.1}
   \]

   This colouring descends to a proper colouring of the minor obtained by
   contracting both edges.
3. **Common fixed-trace rejection.**  The graph
   `G[D]-\{e,f\}` is not `L`-colourable.  It has a connected induced
   vertex-minimal non-`L`-colourable subgraph `K` satisfying

   \[
                              d_K(v)\ge |L(v)|
                              \quad(v\in V(K)).          \tag{2.2}
   \]

   The subgraph induced by the vertices for which equality holds in
   (2.2) is a Gallai forest.  If `K` is a proper induced subgraph of
   `G[D]`, it is a strictly smaller connected kernel rejecting the **same**
   fixed trace `c|X`.

   If `K` spans `D`, there is instead a spanning edge-minimal
   non-`L`-colourable subgraph

   \[
                         F\subseteq G[D]-\{e,f\}         \tag{2.3}
   \]

   such that, for every `v\in D`,

   \[
      d_F(v)\ge |L(v)|,
      \qquad
      d_{G[D]}(v)\ge |L(v)|+m(v),                       \tag{2.4}
   \]

   where `m(v)` is the number of edges in `{e,f}` incident with `v`.

#### Proof

Colourability is monotone under edge deletion.  Thus the following three
possibilities are exhaustive and disjoint: one of the two single-edge
deletions is `L`-colourable; neither is `L`-colourable but their common
deletion is; or the common deletion is not `L`-colourable.

In the first possibility, the fixed-trace alignment theorem applies.  If,
say, `G[D]-e` is `L`-colourable, every induced non-`L`-colourable subgraph
of `G[D]` must contain `e`; otherwise it would be a subgraph of the
`L`-colourable graph `G[D]-e`.  This proves alternative 1.

Suppose the second possibility holds, and let `phi` be an `L`-colouring of
`G[D]-{e,f}`.  If the ends of `e` had different colours, restoring `e`
would give an `L`-colouring of `G[D]-f`, contrary to the failure of
single-edge attainment.  Hence the ends of `e` have one colour.
Symmetrically the ends of `f` have one colour.  Gluing `phi` to `c` gives
`psi` and proves (2.1).

Identifying the equal-coloured ends of the two edges preserves properness.
For vertex-disjoint edges this is immediate.  If the edges are incident,
their two outer ends cannot be adjacent: such an edge is present in
`G-{e,f}` and its ends have the same colour under `psi`.  Thus the
three-vertex tree may also be contracted and `psi` descends to the
resulting proper minor.  This proves alternative 2.

Finally suppose the common deletion is not `L`-colourable.  Choose an
induced vertex-minimal non-`L`-colourable subgraph `K`.  It is connected:
otherwise one of its components is already a proper non-`L`-colourable
induced subgraph.  Colouring `K-v` and then extending to `v` proves
(2.2).  The standard degree-choosability argument applied to every block
of the tight-vertex subgraph proves that its blocks are complete graphs or
odd cycles.

If `K` is proper, it rejects precisely the lists (1.2), so both the
labelled boundary colouring and the failure to extend it are unchanged
while the kernel order strictly decreases.

If `K` spans `D`, delete edges while retaining non-`L`-colourability to
obtain `F` as in (2.3).  The same one-vertex extension argument gives
`d_F(v)>=|L(v)|`.  None of the `m(v)` selected incident edges belongs to
`F`, and all of them belong to `G[D]`; hence (2.4).  This proves
alternative 3. \(\square\)

## 3. What the common-equality branch adds dynamically

Assume now the hypotheses of alternative 2 and, as in the minor-minimal
application, assume also that every proper minor of `G` is `q`-colourable.
In particular `psi` is a double-contraction colouring which retains the
selected labelled trace.

### Proposition 3.1 (paired fixed-trace critical subgraphs)

There are connected subgraphs, vertex-induced in their respective
edge-deleted hosts,

\[
 K_e\subseteq G[D]-f,
 \qquad
 K_f\subseteq G[D]-e,                                  \tag{3.1}
\]

which are non-`L`-colourable and minimal by vertex inclusion, such that
`K_e` contains the edge `e` and `K_f` contains the edge `f`.  They need
not be vertex-induced subgraphs of `G[D]`, because restoring the companion
edge may add an edge on the same vertex set.  If either has fewer vertices
than `D`, that vertex set induces in `G[D]` a strict connected kernel
rejecting the same fixed trace.  This strict kernel need not retain the
companion edge or the five model labels.

Each `K_g`, for `g\in\{e,f\}`, has an edge-minimal non-`L`-colourable
spanning subgraph `F_g` containing `g`.  Let `phi` be any `L`-colouring of
the common deletion.  For every colour `beta` different from the common
`phi`-colour `alpha` on the ends of `g`, exactly one of the following
holds in the graph consisting of `F_g-g`, the fixed boundary `X`, and all
`K_g`--`X` edges.

1. The two ends of `g` lie in one `alpha`--`beta` component, giving a
   literal path between them in `G-{e,f}`.
2. Their two `alpha`--`beta` components are distinct and both meet `X`,
   giving two vertex-disjoint first-hit paths to two distinct literal
   boundary vertices.

If no strict kernel occurs, both `K_e` and `K_f` span `D`.  Thus the
common-equality branch has two spanning, oppositely deleted,
fixed-trace-critical subgraphs; it is not merely an unstructured colouring
of the common deletion.  In that spanning case, every endpoint `v` of
`e\cup f` satisfies

\[
                         d_{G[D]}(v)\ge |L(v)|+1.       \tag{3.2}
\]

#### Proof

The graph `G[D]-f` is not `L`-colourable, since alternative 2 assumes that
`f` does not attain the trace.  Choose a vertex-minimal induced
non-`L`-colourable subgraph `K_e` of it.  The graph obtained by deleting
`e` from `G[D]-f` is the `L`-colourable common deletion.  Hence `K_e`
must contain the edge `e`; otherwise it would be a subgraph of that common
deletion.  The same argument with the edges interchanged gives `K_f`.

Edge-minimize each `K_g` while preserving non-`L`-colourability.  The
result `F_g` contains `g`, again because `F_g-g` is a subgraph of the
`L`-colourable common deletion.  The restriction of `phi` is an
`L`-colouring of `F_g-g`.  The fixed-trace locked-edge theorem now gives
exactly the two displayed component alternatives, including disjointness
and distinct literal first hits in the second one.  All its internal path
vertices lie in `K_g`, so every path is a path of the common edge-deletion
host.

If both critical subgraphs span, an endpoint of `e` has degree at least
`|L(v)|` in `F_f\subseteq G[D]-e`, and restoring its incident edge `e`
proves (3.2).  The symmetric argument treats endpoints belonging only to
`f`; a common endpoint may use either inequality.  The remaining
assertions follow from the vertex orders of `K_e,K_f`. \(\square\)

### Proposition 3.2 (an unlocked pair forces literal boundary exposure)

Suppose first that `e=ab` and `f=cd` are vertex-disjoint.  Fix distinct
colours `i,j`, and suppose the ends of `e` have common colour `i` in
`psi`.  If the ends of `e` lie in different `i`--`j` components, then
**each** of the two components containing an end of `e` meets `X`.  The
symmetric statement holds for `f`.  Switching either endpoint component
changes the equality partition induced on `X`, not merely the literal
colour names.

Consequently the common-host lock-allocation theorem applies in the same
fixed-trace colouring `psi`, with its exact same-colour or distinct-colour
allocation.  Every pair which is unlocked for one of the palettes under
consideration has two literal boundary-reaching components.  In the
six-colour application one pair has at least three locks, and at least
four when the two equality colours are distinct.

#### Proof

Let `Q` be either of the two `i`--`j` components containing one end of
`e`.  Interchange `i,j` on `Q`.  This makes `e` proper.  The result remains
a proper colouring of `G-{e,f}`.  Its ends on `f` must remain equal, since
otherwise both edges could be restored and `G` would be `q`-colourable.
It is therefore a proper colouring of `G-f`.

If `Q` avoided `X`, the interchange would leave (2.1) unchanged, so `f`
would attain the fixed trace.  That contradicts alternative 2.  Thus
`Q` meets `X`.  If the switched colouring induced the same equality
partition as `c` on `X`, one global permutation of the palette would make
its labelled trace equal to `c|X`; this would again make `f` attain the
fixed trace.  Hence the partition changes.  Either endpoint component can
be used as `Q`, proving the first assertion.  The lock counts are exactly
the audited common-host double-contraction allocation theorem applied to
`psi`. \(\square\)

### Proposition 3.3 (incident saturation or two boundary-reaching moves)

Suppose instead that

\[
                              e=sw,\qquad f=st.          \tag{3.3}
\]

Apply the incident-edge saturation-or-bypass theorem to `psi`.  Then
either one of the pairs `sw,st` is locked for every alternate colour, or
there are distinct alternate colours `i,j` and components `Q_w,Q_t` such
that

* `Q_w` contains `w` but not `s,t` and meets `X`;
* `Q_t` contains `t` but not `s,w` and meets `X`;
* `Q_w\cup Q_t` contains a `w`--`t` path avoiding `s`, using at most one
  edge between the two components; and
* switching `Q_w` or `Q_t` gives the two opposite one-edge responses,
  but changes the selected boundary equality partition.

#### Proof

The common-equality colouring descends to the simultaneous contraction,
so the incident-edge theorem applies.  Its saturated outcome is the first
outcome here.  In its other outcome, let `Q_w,Q_t` be the two components
called `A,B` in that theorem.  Their path and switching properties are
exactly its conclusion.

If `Q_w` avoided `X`, its switch would produce a proper colouring of
`G-f` which still agreed with `c` on `X`, making `f` attain the fixed
trace.  Alternative 2 excludes this.  Therefore `Q_w` meets `X`.
The same argument with `Q_t` proves that it meets `X`.  Since a switch
changes only the two colours on its component, the resulting labelled
trace differs from `c|X`.  If its equality partition were unchanged, a
global palette permutation would align that trace with `c|X` and would
make the corresponding single edge attain the fixed trace.  This is
excluded by alternative 2, so the equality partition changes. \(\square\)

### Corollary 3.4 (every response move has a partial boundary footprint)

Let `Q` be any endpoint component switched in Proposition 3.2 or 3.3, and
let its two colours be `i,j`.  Put

\[
 X_i=X\cap\psi^{-1}(i),\qquad X_j=X\cap\psi^{-1}(j).
\]

Then

\[
 \varnothing\ne Q\cap(X_i\cup X_j)
              \ne X_i\cup X_j.                         \tag{3.4}
\]

Moreover no edge of the `i`--`j` subgraph joins
`Q\cap X` to `(X_i\cup X_j)-Q`.

#### Proof

The first inequality follows from the boundary-reaching conclusions.  If
`Q` contained all of `X_i\cup X_j`, switching it would merely interchange
the names of the two complete boundary colour blocks.  The equality
partition would be unchanged, contrary to Propositions 3.2--3.3.  This
proves (3.4).  The last assertion holds because `Q` is a full connected
component of the corresponding bichromatic subgraph. \(\square\)

## 4. Repeated-exposure application and exact residual

In the repeated-exposure compression theorem, the two displayed edges
join the same two named branch sets and deleting either preserves the
spanning labelled `K_7`-minus-one-edge model.  Whenever this pair lies in
the open shore on which the selected boundary trace is being tested,
apply Theorem 2.1 to that trace.

* Alternative 1 supplies a deletion-persistent model edge in every
  fixed-trace critical obstruction; the companion edge retains the old
  model adjacency.
* A proper kernel in alternative 3 is an actual trace-preserving strict
  descent, but not yet a label-preserving one.  The only no-descent subcase
  there is a shore-filling common rejection kernel with the marked endpoint
  excess (2.4).
* Alternative 2 spends the common double-contraction response **without
  losing the selected trace**.  Proposition 3.1 gives paired
  fixed-trace-critical subgraphs and a strict kernel whenever either is
  proper.  Propositions 3.2--3.3 show that failure of lock saturation is
  paid for by literal boundary-reaching response components.

This reduces the dynamic exchange to two explicit obligations.

1. Convert a locked endpoint path or a boundary first hit into a new named
   first-hit label (or a proper subkernel), rather than merely a palette
   change.
2. In the shore-filling common-rejection subcase, use the simultaneous
   endpoint excess in (2.4) to produce an explicit `K_7`-minor model or an
   order-seven separation carrying both a proper trace and the
   partition-specific connected-subgraph system required for response
   reflection.

The existing response-reflection theorem then makes the latter separator
terminal.  A bare order-seven separator is not sufficient.

## 5. Sharpness and trust boundary

The [two-edge deletion-lattice
barrier](../barriers/hc7_two_edge_deletion_lattice_barrier.md) realizes
alternative 2 sharply.  For its all-equal fixed boundary response, neither
single-edge restoration retains that response even though the common
deletion does.  Thus a common fixed-trace equality does **not** force a
single-edge fixed-trace response.  The barrier has a `K_7` minor after its
six-colour lift and is not a hypothetical counterexample.

The propositions above retain literal boundary colours, but they still do
not identify a palette colour or boundary vertex with one of the five
named common branch sets.  A proper critical subgraph may also lose the
companion edge and the original first-hit source set.  The joint-pair
first-hit Hall barrier shows that even high connectivity, exact response
transitions and joint model persistence do not supply that identification
before global `K_7`-minor exclusion and the remaining proper-minor
responses are used.

## 6. Dependencies

- [persistent-edge fixed-trace alignment](../results/hc7_persistent_edge_fixed_trace_alignment.md)
- [common-host double-contraction lock allocation](../results/hc7_common_host_double_contraction_lock_allocation.md)
- [incident-edge saturation or bypass](../results/hc7_shared_interface_bichromatic_bypass.md)
- [total rejection of a fixed boundary trace](../results/hc7_total_trace_rejection_kernel.md)
- [exact response-preservation criterion](hc7_exact7_selected_response_preservation.md)
- [repeated first-hit exposure compression](hc7_labelled_first_hit_exposure_compression.md)
