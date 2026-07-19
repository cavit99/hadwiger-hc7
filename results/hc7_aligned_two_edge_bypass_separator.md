# Two aligned critical edges give a bypass or a labelled donor separation

**Status:** written proof; separate internal audit GREEN in
[`hc7_aligned_two_edge_bypass_separator_audit.md`](hc7_aligned_two_edge_bypass_separator_audit.md).

This note works in the exact-trace branch of the persistent-edge alignment
programme.  Two incident critical edges give a path avoiding both edges.
Independently, the second edge which preserves the spanning
`K_7`-minus-one-edge model either completes a `K_7` minor or exposes a
connected part of the donor branch set behind an actual full-neighbourhood
separator.  The placement of the two deleted-edge endpoints relative to
that separator is recorded exactly.

The theorem does not synchronize the complete boundary partitions on the
returned separator and does not prove `HC_7`.

## 1. Aligned setting

Let `G` be a seven-connected graph which is not six-colourable.  Suppose

\[
                 \{x\},\ B,\ Z,\ H_1,H_2,H_3,H_4                 \tag{1.1}
\]

are pairwise disjoint nonempty connected sets which partition `V(G)`, and
every two sets in (1.1) are adjacent except that `x` has no neighbour in
`B`.  Thus (1.1) is a spanning labelled `K_7`-minus-one-edge model.

Choose vertices

\[
  v,r\in Z,\qquad v\ne r,\qquad u,s\in B                         \tag{1.2}
\]

such that

\[
                    g=xv,\qquad f=vu,\qquad e=rs                 \tag{1.3}
\]

are edges.  The edge `e` is the second `B`--`Z` model edge which retains
that model adjacency after `f` is deleted.  The vertices `u,s` are not
required to be distinct.

Assume that `d` is a proper six-colouring of `G-g`, that `psi` is a proper
six-colouring of `G-f`, and that

\[
                              d(x)=\psi(x).                       \tag{1.4}
\]

In the fixed-trace application, (1.4) follows from the stronger equality
of the two labelled traces on the old boundary `X`.

## 2. The simultaneous bypass

### Theorem 2.1

Under (1.1)--(1.4), there is an `x`--`u` path in

\[
                              G-\{g,f\}.                          \tag{2.1}
\]

#### Proof

Since `G` is not six-colourable, the ends of a deleted edge receive the
same colour in every six-colouring of its deletion.  Put

\[
             d(x)=d(v)=\alpha,\qquad d(u)=\beta.                 \tag{2.2}
\]

The edge `f=vu` is present in `G-g`, so `beta` is different from `alpha`.
The usual critical-edge Kempe argument says that `x` and `v` lie in one
`alpha`--`beta` component of `G-g`; otherwise interchanging the two
colours in the component containing one endpoint would allow `g` to be
restored.  The edge `vu` puts `u` in that same component.  Choose a simple
`x`--`v` path `P` in it which avoids `g`.

Similarly, write

\[
                  \psi(v)=\psi(u)=\lambda.                       \tag{2.3}
\]

By (1.4), `psi(x)=alpha`, and the edge `g=xv` is present in `G-f`, so
`lambda` is different from `alpha`.  Critical-edge Kempe connectivity for
`f` gives a simple `v`--`u` path `Q` in the
`lambda`--`alpha` subgraph of `G-f`.  The edge `xv` puts `x` in the same
component.

If `u` lies on `P`, the `x`--`u` subpath of `P` avoids both `g` and `f`.
Indeed, any use of `f` on the simple `x`--`v` path would be its final edge.
If `x` lies on `Q`, the `x`--`u` subpath of `Q` likewise avoids both
deleted edges.  In the remaining case `P` avoids `f`, because it avoids
`u`, and `Q` avoids `g`, because it avoids `x`.  Hence `P union Q` is a
connected subgraph of `G-{g,f}` containing `x,u`, and contains the desired
path.  \(\square\)

## 3. The donor-side separator

### Theorem 3.1

Let `W` be the component of `G[Z-v]` containing `r`, and put

\[
                              L=Z-W.                              \tag{3.1}
\]

Then `L` is connected, contains `v`, and is adjacent to `W`.  Moreover,
one of the following holds.

1. `G` contains a `K_7` minor, with seven branch sets explicitly obtained
   from (1.1); or
2. for some `j in {1,2,3,4}`,

   \[
                              E_G(W,H_j)=\varnothing.             \tag{3.2}
   \]

   Consequently `N_G(W)` is an actual separator with two nonempty open
   sides, and

   \[
                              |N_G(W)|\ge 7.                      \tag{3.3}
   \]

If outcome 2 holds and `x in N_G(W)`, then either outcome 1 also holds or
there is a `k ne j` such that

\[
                              E_G(L,H_k)=\varnothing.             \tag{3.4}
\]

Thus the boundary placement `x in N_G(W)` forces a complementary
two-label split of the old `Z` contacts in every `K_7`-minor-free host.

#### Proof

Every component of `Z-v` has a neighbour at `v`, since `Z` is connected.
It follows that `L`, which consists of `v` and all components other than
`W`, is connected and adjacent to `W`.

Suppose first that `W` is adjacent to every `H_i`.  Then

\[
              \{x\}\cup L,\quad B,\quad W,\quad H_1,H_2,H_3,H_4 \tag{3.5}
\]

are seven branch sets of a `K_7` minor.  The first set is connected by
`xv`; it meets `B` through `f=vu`, meets `W` through a `W`--`L` edge,
and meets every `H_i` through the old singleton branch set `x`.  The set
`W` meets `B` through `e=rs` and, by assumption, meets every `H_i`.
All remaining adjacencies are inherited from (1.1).  This proves outcome
1 unless (3.2) holds.

Assume (3.2).  The nonempty set `H_j` is disjoint from `W union N_G(W)`,
so the full neighbourhood `N_G(W)` separates the connected set `W` from
a nonempty part containing `H_j`.  Seven-connectivity proves (3.3).

Now suppose also that `x in N_G(W)`.  If `L` were adjacent to every
`H_i`, the seven sets

\[
              \{x\}\cup W,\quad B,\quad L,\quad H_1,H_2,H_3,H_4 \tag{3.6}
\]

would form a `K_7`-minor model: `x` connects the first set to every
`H_i`, `e=rs` connects it to `B`, a `W`--`L` edge connects it to `L`,
and `f=vu` connects `L` to `B`.  Hence, outside outcome 1, (3.4) holds
for some `k`.  The indices are distinct because the original branch set
`Z` is adjacent to `H_j`, while (3.2) forces every `Z`--`H_j` edge to
have its `Z`-end in `L`.  \(\square\)

## 4. Exact colouring behaviour on the returned separator

Put

\[
                              S=N_G(W).                           \tag{4.1}
\]

The connectedness of `Z` implies `v in S`.  The restrictions of the two
deletion colourings to the closed `W`-shore have the following exact
behaviour.

### Proposition 4.1

1. The restriction of `d` to `G[W union S]` is proper if and only if
   `x notin S`.  If `x in S`, it is proper after deleting the single
   boundary edge `g=xv`, and `d(x)=d(v)` is its only failed edge.
2. The restriction of `psi` to `G[W union S]` is proper if and only if
   `u notin S`.  If `u in S`, it is proper after deleting the single
   boundary edge `f=vu`, and `psi(v)=psi(u)` is its only failed edge.
3. If the two colourings attain the same labelled trace on an old boundary
   `X`, then their restrictions agree on `X intersect S`.

In particular, if `|S|=7`, this is an actual exact order-seven interface.
When `x,u notin S`, both displayed colourings extend through its closed
`W`-shore, but their complete equality partitions on `S` need not agree.
When one or both vertices lie in `S`, the corresponding response is a
single-edge boundary pinch rather than a proper colouring of the original
closed shore.

#### Proof

The colouring `d` is proper on every edge except `g`, whose ends have the
same colour.  The vertex `v` lies in `S`, while `x` does not lie in `W`.
Thus both ends of `g` belong to `W union S` exactly when `x in S`.  This
proves assertion 1.  The same argument with `psi,f,u` proves assertion 2.
Assertion 3 is immediate from equality of the labelled traces.  \(\square\)

## 5. Oppositely oriented responses at the lost labelled contact

Assume now, as in the minor-minimal `HC_7` application, that every proper
minor of `G` is six-colourable and that outcome 2 of Theorem 3.1 holds.
Choose an edge

\[
                              vw_0,qquad w_0\in W,                \tag{5.1}
\]

which exists because `W` is a component of `Z-v`.  Since the old branch
set `Z` is adjacent to `H_j` while `W` is anticomplete to `H_j`, choose

\[
                 t_jh_j\in E_G(L,H_j),qquad
                 t_j\in L,\quad h_j\in H_j.                       \tag{5.2}
\]

For an edge `a` and a labelled vertex set `S`, let `Resp(a,S)` denote the
equality partitions of `S` induced by proper six-colourings of `G-a`.
Let `Ext(Q,S)` denote the partitions induced by proper six-colourings of a
closed shore `Q` with boundary `S`.  Put

\[
                  C=G[W\cup S],\qquad O=G-W.                     \tag{5.3}
\]

### Corollary 5.1

The two named response languages have opposite orientations:

\[
\begin{aligned}
 Resp(vw_0,S)&\subseteq Ext(O,S)\setminus Ext(C,S),\\
 Resp(t_jh_j,S)&\subseteq Ext(C,S)\setminus Ext(O,S).
\end{aligned}                                                     \tag{5.4}
\]

In particular,

\[
                 Resp(vw_0,S)\cap Resp(t_jh_j,S)=\varnothing.    \tag{5.5}
\]

Thus the separator carries one response based at its unique donor-side
attachment and an opposite response based at the precise old branch-set
label whose contact was lost.

#### Proof

Apply the audited opposite-boundary-response theorem with its deficient
branch set `A` equal to the present `B`, its singleton branch set `R`
equal to `{x}`, and its donor `U` equal to `Z`.  The two selected
`B`-attachments in `Z` are `r,v`.  Its component `W` and complementary
set `U-W` are exactly the present `W,L`.  The set `L` is adjacent to
`{x}` through `g=xv`, while (3.2) says that the named branch set `H_j`
belongs to the theorem's lost-contact family.  Equations (5.1)--(5.2) are
therefore precisely its donor-interface edge and its oppositely situated
lost-contact edge.  Formulae (5.4)--(5.5) follow.  \(\square\)

The point of (5.4) is not that the two languages already intersect: in a
seven-chromatic graph they cannot.  It identifies the exact
label-preserving collision which a fixed-trace, fan, or proper-minor
argument would have to force.

There is one further exact split according to the location of the lost
contact in `L`.

### Corollary 5.2 (shared portal or disjoint response edges)

For the label `H_j` in (3.2), exactly one of the following geometric cases
holds.

1. The edge in (5.2) can be chosen as `vh_j`.  Then the donor-interface
   edge `vw_0` and the lost-contact edge `vh_j` share the literal portal
   `v`.  In one six-colouring obtained by contracting both edges, either
   one of these two named pairs is bichromatically connected for all five
   alternate colours, or
   \(G-\{vw_0,vh_j\}-v\) contains a `w_0`--`h_j` path.  This path is the
   union of two named bichromatic components and at most one edge between
   them.  Its first vertex after leaving `W` belongs to `S-{v}` and lies
   outside the old donor `Z`.
2. No vertex of `H_j` is adjacent to `v`.  Then every edge in
   `E_G(L,H_j)` has its `L`-end in `L-{v}`, and the two response edges
   `vw_0` and `t_jh_j` are vertex-disjoint.  In one six-colouring of
   their common two-edge deletion, one of the two named endpoint pairs is
   joined by bichromatic paths for at least three alternate colours.  If
   `vt_j` is an edge, one named pair has at least four such paths.

#### Proof

If `v` has a neighbour `h_j` in `H_j`, apply the audited shared-interface
bichromatic-bypass theorem to the induced two-edge path
`w_0-v-h_j`.  Its leaves are nonadjacent by (3.2), and contracting the
path gives a proper minor, so all its hypotheses hold.  The theorem gives
the stated saturation-or-bypass alternative.  Since
`N_Z(W)={v}`, the first exit of a bypass avoiding `v` lies outside `Z`.

If no such neighbour exists, (5.2) still supplies a lost-contact edge,
but its `L`-end is different from `v`.  Its other end lies in `H_j`, while
`w_0` lies in `W`; hence it is vertex-disjoint from `vw_0`.

For completeness, the final common-colouring assertion in case 2 is the
audited double-contraction lock-allocation theorem applied to the two
vertex-disjoint edges.  The possible cross-edges between their endpoint
pairs are especially constrained here: `w_0t_j` is absent because
`N_Z(W)={v}`, `w_0h_j` is absent by (3.2), and `vh_j` is absent by case 2.
Thus `vt_j` is the only possible cross-edge.  The general allocation gives
three colour-restricted paths for one pair; when `vt_j` exists, the
cross-edge sharpening gives four.  Every asserted path avoids both named
edges.  These palette-indexed paths still need not meet distinct old
branch sets.  \(\square\)

## 6. The fixed-trace locked-edge information

Assume additionally that `f` lies in an edge-minimal non-`L_c`-colourable
subgraph `F` of the fixed-trace shore, and that `psi|_F` is the
`L_c`-colouring of `F-f` supplied by the attained trace.  Put

\[
                 \lambda=\psi(v)=\psi(u),\qquad
                 \alpha=\psi(x).                                 \tag{6.1}
\]

In the local properly coloured graph consisting of `F-f`, the old boundary
`X`, and all critical-subgraph--boundary edges, the
`lambda`--`alpha` component containing `v` also contains `x`, through
`g=xv`.  The locked-edge alternative therefore says exactly one of:

1. that component also contains `u`, and hence contains a local connected
   subgraph through `u,v,x`; or
2. the component containing `u` is distinct and has a first-hit path to a
   boundary vertex `y in X-{x}`, internally contained in the fixed-trace
   critical subgraph.

This is a literal second boundary contact, but it does not identify `y`
with any of the four named branch-set labels `H_i`.  Also, the local graph
need not contain every edge of the host graph, so this alternative cannot
by itself be combined with Theorem 2.1 as though both paths belonged to
one common properly coloured graph.

## 7. Exact remaining gap

The aligned trace-attaining branch now supplies simultaneously:

- an `x`--`u` path avoiding both critical edges;
- either an explicit `K_7`-minor model or an actual donor-side
  full-neighbourhood separator;
- exact endpoint-placement information for the two deletion responses;
- oppositely oriented proper-minor responses attached to the unique donor
  interface and the specific lost branch-set label;
- and a local fixed-trace connection or a second literal boundary first
  hit.

What is still missing is a label-preserving allocation theorem.  It must
either identify the bypass or the local first hit with the missing contact
`H_j`, synchronize one complete equality partition on an order-seven
separator, or reconstruct the entire aligned tuple in a strictly smaller
open component.  Palette colours alone do not identify these branch-set
labels, and Theorem 3.1 provides no upper bound on `|N_G(W)|`.

## 8. Dependencies

- [persistent-edge fixed-trace alignment](hc7_persistent_edge_fixed_trace_alignment.md)
- [single-portal amplification](hc7_single_portal_amplification.md)
- [boundary list-criticality and locked-edge alternatives](hc7_boundary_list_critical_transfer.md)
- [oppositely oriented boundary responses at a connected-subgraph rotation](hc7_rotation_opposite_boundary_responses.md)
- [bichromatic saturation or a bypass at incident critical edges](hc7_shared_interface_bichromatic_bypass.md)
- [common-host double-contraction lock allocation](hc7_common_host_double_contraction_lock_allocation.md)
