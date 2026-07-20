# Prescribed omission and paired columns at a boundary of order eight

**Status:** written proof; independently audited **GREEN** in
[`hc7_order8_prescribed_omission_paired_column_decoder_audit.md`](hc7_order8_prescribed_omission_paired_column_decoder_audit.md).
This note proves two unbounded host-level reductions for the remaining
two-component boundary of order eight. It does not couple the complete
proper-minor colouring responses, produce a common boundary partition, or
prove `HC_7`.

## 1. Setting and terminology

Let `G` be a seven-connected graph, let `S` be an eight-vertex set, and
suppose that `G-S` has exactly two components `C,D`. Assume that both are
adjacent to every literal vertex of `S`.

A **crossing-edge response side** consists of a nonempty connected set `A`,
its full neighbourhood `N_G(A)`, and an edge `xy` with

\[
                     x\in A,\qquad y\in N_G(A).        \tag{1.1}
\]

When `G` is not six-colourable and every proper minor of `G` is
six-colourable, deleting `xy` gives a six-colouring in which `x,y` have one
colour. Its equality partition on `N_G(A)` is legal on the edge-deleted
closed `A`-side and on the opposite closed shore, but is rejected by the
intact closed `A`-side. Otherwise the two intact shore colourings could be
aligned and glued to six-colour `G`.

## 2. Prescribing the omitted boundary vertex

### Theorem 2.1 (prescribed omission or a smaller response side)

Fix `v in C` and seven distinct incident edges

\[
                         vv_1,\ldots,vv_7.             \tag{2.1}
\]

Put

\[
 D_0=\{v_i:v_i\in S\},\qquad
 U_0=\{v_i:v_i\in C-v\}.                              \tag{2.2}
\]

For every `r in S-D_0`, at least one of the following holds.

1. There are seven paths which begin respectively with the edges in
   (2.1), are pairwise vertex-disjoint outside `v`, meet `S` only at their
   other ends, and end at the seven distinct vertices of `S-{r}`.
2. There is a nonempty connected proper set `A subsetneq C` such that

   \[
                         7\le |N_G(A)|\le8,             \tag{2.3}
   \]

   and one of the prescribed edges in (2.1) crosses between `A` and
   `N_G(A)`. The full neighbourhood is the boundary of an actual separation
   with two nonempty open sides.

#### Proof

Write `d=|D_0|` and `k=|U_0|=7-d`. Since `r notin D_0`, the set

\[
                         T=S-(D_0\cup\{r\})             \tag{2.4}
\]

has order `k`. In the graph

\[
                         H=G[(C-\{v\})\cup T]           \tag{2.5}
\]

apply the vertex-set form of Menger's theorem between `U_0` and `T`.

If `k=0`, the seven prescribed edges are the direct paths to
`D_0=S-\{r\}`, so outcome 1 holds. Assume henceforth that `k\ge1`.

If there are `k` pairwise vertex-disjoint `U_0`--`T` paths, every member of
`U_0` and every member of `T` is an end of exactly one path. Truncate each
path at its first member of `T`, prepend its prescribed edge from `v`, and
add the direct edges `vv_i` for `v_i in D_0`. The resulting seven paths
have precisely the properties in outcome 1.

Otherwise Menger's theorem gives a set `Z subseteq V(H)` with

\[
                              |Z|\le k-1                \tag{2.6}
\]

separating `U_0` from `T`; terminals are allowed to belong to `Z`. Choose
`u in U_0-Z`, and let `A` be the component of `H-Z` containing `u`. No
surviving member of `T` belongs to `A`. Since `C` is a component of
`G-S`, componenthood gives

\[
              N_G(A)\subseteq\{v\}\cup D_0\cup\{r\}\cup Z.       \tag{2.7}
\]

Consequently

\[
 |N_G(A)|\le 1+d+1+(k-1)=8.                            \tag{2.8}
\]

The set `A` is nonempty, connected and excludes `v`. The opposite
component `D` lies outside `A union N_G(A)`, so this is a genuine
separation. Seven-connectivity gives the lower bound in (2.3). Finally,
`u` is one of the first neighbours in (2.1), and hence the edge `vu`
crosses the displayed full neighbourhood. This proves outcome 2.
\(\square\)

### Corollary 2.2 (response interpretation)

Assume additionally that `G` is not six-colourable and every proper minor
of `G` is six-colourable. In outcome 2, deleting the crossing prescribed
edge makes `A,N_G(A)` a crossing-edge response side in the sense of
Section 1. When `|N_G(A)|=7` it is an exact order-seven response. When
`|N_G(A)|=8`, it is a strict response-side descent because `A subsetneq C`.

#### Proof

Let the crossing edge be `vu`, with `u in A` and `v in N_G(A)`. Every
six-colouring of `G-vu` gives `u,v` one colour, or the deleted edge could be
restored. Restrict such a colouring to the two edge-deleted closed shores.
If its equality partition on `N_G(A)` extended through the intact closed
`A`-side, a palette permutation would align that extension with the
unchanged opposite-shore restriction and six-colour `G`. This is
impossible. Strictness in the order-eight case follows from
`A subsetneq C`. \(\square\)

### Corollary 2.3 (synchronizing two response fans)

Let `p in S`, let `v in C,w in D` be neighbours of `p`, and choose seven
prescribed edges at each centre, including `vp` and `wp`. Let `D_C,D_D`
be their respective sets of direct boundary ends.

Unless Theorem 2.1 returns an order-seven response or a strict order-eight
response descent, the following hold.

1. Each fan may be made to omit any prescribed member of `S-D_C`,
   respectively `S-D_D`.
2. If `D_C union D_D ne S`, the two fans may omit the same vertex and have
   six common non-`p` boundary ends.
3. In general, choosing omissions `r_C,r_D` gives five common non-`p`
   boundary ends when `r_C ne r_D`, and six when they agree.

Thus endpoint availability is completely controlled. The exceptional case
for a common omission is the direct-saturation condition

\[
                              D_C\cup D_D=S.            \tag{2.9}
\]

No assertion is made that a colour indexing a prescribed edge identifies
the branch-set label at the other end of its rerouted path.

## 3. A paired all-boundary column decoder

### Theorem 3.1

Let `p in S` and choose

\[
                    v\in N_G(p)\cap C,\qquad
                    w\in N_G(p)\cap D.                 \tag{3.1}
\]

Then at least one of the following holds.

1. A nonempty connected proper subset of `C` or `D` has an actual full
   neighbourhood of order seven.
2. There are seven pairwise vertex-disjoint connected subgraphs

   \[
                              L_s\quad(s\in S-\{p\})    \tag{3.2}
   \]

   disjoint from the two connected root sets

   \[
                              R_C=\{v,p\},\qquad R_D=\{w\},       \tag{3.3}
   \]

   such that `s in L_s`, the two roots are adjacent, and each root is
   adjacent to every `L_s`.

Define the **column-contact graph** `J` on `S-{p}` by

\[
 st\in E(J)\quad\Longleftrightarrow\quad
 E_G(L_s,L_t)\ne\varnothing.                            \tag{3.4}
\]

The nine branch sets in (3.2)--(3.3) give a `K_2 join J` minor in `G`.
If `J` contains a `K_5` minor, they lift it to an explicit `K_7` minor in
`G`. Consequently, in a `K_7`-minor-free host, every paired all-boundary
column system has a seven-vertex `K_5`-minor-free contact graph.

#### Proof

Apply the fan form of Menger's theorem from `v` to `S` in `G[C union S]`.
If no eight-fan exists, a separator `Z` of order at most seven separates
`v` from some surviving member of `S`. The component of
`G[C union S]-Z` containing `v` is a nonempty connected proper subset of
`C` whose full neighbourhood has order at most seven. The component `D`
makes the separation genuine, and seven-connectivity makes its boundary
have order exactly seven. To see properness explicitly, choose
`s in S-Z`. Boundary-fullness gives an edge from `s` to `C`, and its end
cannot lie in the `v`-component without contradicting the separation.
This is outcome 1.

Otherwise there are eight paths from `v` to the eight distinct members of
`S`, pairwise disjoint outside `v` and meeting `S` only at their ends.
Replace the path ending at `p` by the direct edge `vp`. Perform the same
construction from `w` in `G[D union S]`, retaining `wp`.

For `s in S-{p}`, let `P_s^C,P_s^D` be the two fan paths ending at `s` and
put

\[
                    L_s=(P_s^C-v)\cup(P_s^D-w).         \tag{3.5}
\]

The set `L_s` is connected through `s`, including when one of the two fan
paths is a direct edge. The seven columns are pairwise disjoint, because
the two fan systems are separately disjoint outside their centres and the
two open components are disjoint. They avoid `p` and the two roots.

The edge `pw` joins the roots. The first edge of each fan path makes its
root adjacent to the corresponding column. Hence contracting the nine
connected sets gives `K_2 join J`. A `K_5` model in `J`, together with the
two root bags, gives seven pairwise adjacent connected branch sets in `G`.
\(\square\)

## 4. Sharpness of the static information

The paired-column decoder and the existence of the three positive two-edge
colouring signatures do not by themselves force a `K_7` minor.

Let `I` be the icosahedral graph with vertices

\[
 t,d,u_0,\ldots,u_4,w_0,\ldots,w_4
\]

and its standard capped-antiprism edges

\[
 tu_i,\quad dw_i,\quad u_iu_{i+1},\quad w_iw_{i+1},\quad
 u_iw_i,\quad u_iw_{i-1},                              \tag{4.1}
\]

with indices modulo five. Add adjacent universal vertices `p,q`, forming

\[
                              G_0=K_2\mathbin{\vee}I.   \tag{4.2}
\]

Put

\[
\begin{aligned}
 S&=\{p,q,t,d,u_0,w_0,u_2,w_2\},\\
 C&=\{u_3,u_4,w_3,w_4\},\\
 D&=\{u_1,w_1\},\\
 v&=u_3,\qquad w=u_1.
\end{aligned}                                           \tag{4.3}
\]

Then `C,D` are the two components of `G_0-S`, both are `S`-full,
`C-v` is connected, and `D-w` is the connected singleton `{w_1}`.
The graph `G_0` is seven-connected: retaining either universal vertex
keeps the graph connected, while after deleting both, five-connectivity of
the icosahedron handles four further deletions. It is `K_7`-minor-free.
Indeed, a `K_7` model using the two universal vertices in separate branch
sets would leave a `K_5` minor in the planar graph `I`; using fewer than two
separate universal bags would leave an even larger clique minor in `I`.

For the incident crossing edges

\[
                              e=pv,\qquad f=pw,          \tag{4.4}
\]

the common deletion has colourings with signatures

\[
            ({\rm equal},{\rm equal}),\qquad
            ({\rm equal},{\rm proper}),\qquad
            ({\rm proper},{\rm equal}).                \tag{4.5}
\]

For example, contract both edges, only `e`, or only `f`, respectively,
six-colour the resulting join minor, and expand the contraction images.
But `G_0` itself is six-colourable, so the fourth signature

\[
                              ({\rm proper},{\rm proper})          \tag{4.6}
\]

also occurs. Moreover every vertex of `I` has degree seven in `G_0`, so
its neighbourhood gives an actual order-seven separation. Thus this is
not a counterexample to a theorem retaining criticality or a compatible
separator outcome.

The example proves the precise sharpness statement needed here: the
two-centre connected geometry, the paired fan/column systems and the three
positive signatures cannot be converted into a `K_7` model without using
the universal exclusion of (4.6), or equivalent operation-specific
nonextendability, together with literal information inside the column
bags.

## 5. Exact remaining gap

Theorem 2.1 removes endpoint availability as an obstruction: away from a
strict response descent, the omitted boundary vertex can be prescribed.
Theorem 3.1 converts paired all-boundary fans into seven literal columns
dominated by two adjacent root bags. In a `K_7`-minor-free survivor their
contact graph has no `K_5` minor.

The columns need not cover `C-v` or `D-w`, and neither operation records
where the five colour-indexed critical first edges enter the columns.
Contracting a whole column erases its internal first-hit and
equality-partition data, while retaining only the column contact graph
permits the sharpness example above. The remaining theorem must therefore
turn the universal absence of the `(proper,proper)` signature into one of:

1. a `K_5` minor in a literal contact refinement of `J`, hence a `K_7`
   minor in `G`;
2. an actual order-seven separation on whose two closed shores one complete
   equality partition is realized; or
3. a strict response-preserving descent.

This is a colouring-to-labelled-column coupling problem. It is not another
unlabelled fan or endpoint-packing problem.

## 6. Trust boundary

- Theorem 2.1 and Theorem 3.1 are unbounded literal-host statements.
- Outcome 2 of Theorem 2.1 becomes a response descent only under the
  explicit minor-colourability hypotheses of Corollary 2.2.
- A `K_5` minor in the column-contact graph is sufficient for a `K_7`
  minor, but the converse is not asserted.
- The columns need not cover either open component, and no connectivity is
  asserted for a shore-specific subgraph of the column-contact graph.
- The sharpness graph is six-colourable and has order-seven separators. It
  refutes only geometry-plus-positive-signatures shortcuts, not the live
  critical-host disjunction.
- No palette colour is identified with a column, a boundary vertex, or an
  inherited minor-model branch-set label.
