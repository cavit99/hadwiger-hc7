# Operation-coupled colouring responses at a boundary-full eight-separation

**Status:** written proof; separate internal audit GREEN in
[`hc7_operation_coupled_order8_response_audit.md`](hc7_operation_coupled_order8_response_audit.md).
This theorem combines the boundary Kempe-transition, prescribed-first-edge
fan, and transported-partition Hall criteria for the two remaining component
counts at an eight-vertex separation.  It treats the two- and
three-component interfaces uniformly.  It does not align palette colours
with inherited minor-model branch-set labels and does not prove `HC_7`.

## 1. Setting

Let `G` be a seven-connected graph such that

\[
 \chi(G)=7,\qquad K_7\not\preccurlyeq G,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G.
 \tag{1.1}
\]

Let `X` be an eight-vertex set.  Suppose the components of `G-X` are

\[
                       C_0,C_1,\ldots,C_{m-1},
                       \qquad m\in\{2,3\},             \tag{1.2}
\]

and every component is adjacent to every literal vertex of `X`.  Let

\[
                         e=pv,\qquad p\in X,\quad v\in C_0,      \tag{1.3}
\]

and let `d` be a proper six-colouring of `G-e`.  Put

\[
                         \rho=d|_X.                               \tag{1.4}
\]

The ends of `e` have one common colour, say

\[
                         d(p)=d(v)=\alpha.                        \tag{1.5}
\]

For a proper boundary colouring `phi`, let

\[
 \operatorname{Ext}(\phi)=
 \{i: \phi\text{ extends to a proper six-colouring of }
                    G[C_i\cup X]\}.                              \tag{1.6}
\]

## 2. The asymmetric response and its Hall obstruction

### Theorem 2.1

The selected partition satisfies

\[
                  \operatorname{Ext}(\rho)=\{1,\ldots,m-1\}.
                                                                    \tag{2.1}
\]

In particular, let `Sigma` be the equality partition of `rho`, choose a
maximum clique `U` among its singleton blocks, and put

\[
        d_X(\Sigma)=|\Sigma|-|U|.                                  \tag{2.2}
\]

Then

\[
                         d_X(\Sigma)\ge m.                          \tag{2.3}
\]

More precisely, consider any family in the union of the far components
`C_1\cup\cdots\cup C_{m-1}` consisting of

1. `r` pairwise disjoint connected subgraphs adjacent to every vertex of
   `X`; and
2. pairwise disjoint, pairwise adjacent named connected subgraphs `W_k`,
   all disjoint from the first family.

For every block `B` outside `U`, including a singleton block not represented
in the chosen clique `U`, call `W_k` eligible for `B` when it has a
neighbour at every vertex of

\[
 D_U(B)=B\cup\{u\in U:E_G(u,B)=\varnothing\}.                       \tag{2.4}
\]

The corresponding incidence graph has no matching saturating all the
blocks outside `U`.  Thus some nonempty block family `\mathcal F` obeys

\[
             r+|N_{\{W_k\}}(\mathcal F)|<|\mathcal F|.             \tag{2.5}
\]

#### Proof

The colouring `d` is proper on every unchanged closed component-side, so
`rho` extends through each `C_i` with `i>0`.  If it also extended through
the intact `C_0`-side, choose one extension on every component-side and
glue them on their common labelled colouring of `X`.  The resulting
colouring would contain the edge `e` and would six-colour `G`.  This proves
(2.1).

Use each of the `m-1` far components as a boundary-full connected support.
If `d_X(Sigma)<=m-1`, the transported-partition reflection theorem
contracts one support for every block outside `U` and produces a colouring
of the intact `C_0`-side with equality partition `Sigma`.  After a palette
permutation this glues to `d` on the far sides, contradicting (1.1).  This
proves (2.3).

The same theorem applies to every displayed mixed support family.  A
saturating matching would again reproduce `Sigma` on the intact side and
six-colour `G`.  Hence no such matching exists, and Hall's theorem gives
(2.5). \(\square\)

## 3. One connected Kempe space records both orientations

### Theorem 3.1

Let `I` be any nonempty block of `Sigma`.  After normalizing the palette,
all proper labelled boundary colourings having `I` as the exact class of
one fixed named colour lie in one Kempe class under moves avoiding that
colour.  In this one class the following hold.

1. If `m=2`, there is a path from `rho` to a colouring extending through
   `C_0`.  Some edge of the path changes the `C_1` extension bit and has a
   literal bichromatic obstruction path with interior in `C_1`; some edge
   changes the `C_0` extension bit and has such a path with interior in
   `C_0`.
2. If `m=3`, the colouring `rho` is the anchor whose extension signature is
   `{1,2}`.  Together with two further anchors it lies in a finite
   transition tree in which every one of the three extension bits changes
   on some edge.  The edge changing the `C_i` bit has a literal
   bichromatic obstruction path with interior in `C_i`.

The two relevant changes in item 1, and the three changes in item 2, need
not occur on the same boundary Kempe move.

#### Proof

For every nonempty independent `I\subseteq X`, the graph `G[X]-I` is
four-degenerate.  The Las Vergnas--Meyniel theorem therefore makes the
exact-`I` five-colour reconfiguration graph connected.

For `m=2`, contract `C_1\cup I`, colour the proper minor, and restrict the
colouring to the untouched `C_0`-side.  Its boundary colouring has `I` as
the same exact block, extends through `C_0`, and cannot extend through
`C_1`.  Thus the two extension bits both change along a path from `rho` to
this colouring.  At the first edge on which a bit changes, the
signature-change path lemma supplies the stated literal path in the named
component.

For `m=3`, use `rho` as the anchor with signature `\{1,2\}`.  For
`i\in\{1,2\}`, contract `C_i\cup I`; restriction to the other two
component-sides gives an exact-`I` colouring with signature
`\{0,1,2\}-\{i\}`.  Connect these three anchors by a finite tree in the
exact-`I` Kempe graph.  Each bit is zero at one anchor and one at the other
two, so it changes on the tree.  Apply the same signature-change path
lemma. \(\square\)

## 4. A clean response fan or a coloured order-seven separation

### Theorem 4.1

For every colour `beta\ne alpha`, there is an `alpha`--`beta` path from
`v` to `X`, stopped at its first boundary vertex, whose internal vertices
lie in `C_0`.  The five paths may be chosen edge-disjoint; paths belonging
to different alternate colours meet only at `alpha`-coloured vertices.

From their five distinct first edges, one obtains one of the following.

1. **Clean fan.**  There are five paths preserving those first edges and
   pairwise vertex-disjoint outside `{v}\cup X`.  Their boundary ends may
   coincide, and their first inherited branch-set labels need not be
   distinct.
2. **Exact seven-boundary.**  For some `ell\in\{2,3,4,5\}` there are sets

   \[
      I\subseteq X,\quad |I|=\ell+1,\quad p\in I,
      \qquad Z\subseteq C_0-\{v\},\quad |Z|=\ell-1,       \tag{4.1}
   \]

   and a nonempty connected set
   `A\subseteq C_0-(\{v\}\cup Z)`, with

   \[
          Y=N_G(A)=(X-I)\mathbin{\dot\cup}\{v\}
                     \mathbin{\dot\cup}Z,\qquad |Y|=7,            \tag{4.2}
   \]

   such that `sigma=d|_Y` is a proper boundary colouring on the closed
   `A`-side.  Its exact `alpha`-block

   \[
                         J=\sigma^{-1}(\alpha)                       \tag{4.3}
   \]

   contains `v` and at least one vertex of `Z`.

#### Proof

If the full `alpha`--`beta` component containing `v` did not contain `p`,
interchanging the two colours on that component would make the ends of the
deleted edge different and allow `e` to be restored.  Hence it contains
`p`.  Stop a `v`--`p` path at its first vertex of `X`.  Distinct colour
pairs share only `alpha`-coloured vertices and no edge, which gives the
first assertion.

Apply the prescribed-first-edge fan-or-separation theorem to these five
paths.  Its packing outcome is item 1.  In its cut outcome that theorem
returns exactly the sets `I,Z,A` displayed above.  Seven-connectivity makes
its upper bound on the full neighbourhood tight, yielding (4.2).  The same
theorem shows that `d` is proper on the original closed `A`-side and that
some vertex of `Z`, as well as `v`, has colour `alpha`, proving (4.3).
\(\square\)

## 5. The exact-seven outcome has two dynamic orientations

### Theorem 5.1

Assume outcome 2 of Theorem 4.1.  Then the opposite closed shore has a
proper six-colouring `tau` in which `J` is the same exact labelled colour
class.  Exactly one of the following holds.

1. `sigma` and `tau` induce the same equality partition on `Y`, in which
   case the two shore colourings align and six-colour `G`.
2. They induce two distinct exact-`J` partitions in one connected
   exact-`J` boundary Kempe class.  Along every path between them:

   - some transition loses extendability through `A` and supplies a
     literal bichromatic obstruction path with interior in `A`; and
   - for at least one opposite component through which `sigma` does not
     extend, some transition gains extendability and supplies such a path
     in that component.

   These transitions need not coincide.

In the second outcome, orient the boundary once from each of the two legal
closed shores, and let `Pi` be the complete equality partition legal on the
chosen shore.  Choose a maximum clique `U` among the singleton blocks of
`Pi`.  For every block `B` not represented by `U`, define `D_U(B)` as in
(2.4).  The full-connected-subgraph packing number of the chosen shore is
`r\in\{1,2\}`.  Fix `r` pairwise disjoint boundary-full connected supports
realizing this maximum, and any further pairwise disjoint, pairwise adjacent
named connected supports `W_k` which are disjoint from the full supports.
Join `W_k` to `B` in the incidence graph exactly when `W_k` has a neighbour
at every vertex of `D_U(B)`.  There is a nonempty block family `\mathcal F`
outside `U` satisfying

\[
                        r+|N(\mathcal F)|<|\mathcal F|.             \tag{5.1}
\]

#### Proof

Contract a spanning tree of the connected set `A\cup J`, colour the proper
minor, and restrict to the opposite closed shore.  The contraction image
is adjacent to every vertex of `Y-J`; pulling its colour back only over the
independent set `J` gives the colouring `tau` with `J` exact.

If the two equality partitions coincide, permute the six colour names on
one shore and glue.  Otherwise, `G[Y-J]` has at most five vertices and is
four-degenerate.  Thus all labelled five-colourings of it are Kempe
equivalent while the sixth colour is held fixed exactly on `J`.

The colouring `sigma` extends through `A`, whereas `tau` cannot, or it
would glue to its opposite-shore extension.  Hence the `A` extension bit
changes along a boundary Kempe path.  Conversely, `tau` extends through
every opposite component.  The colouring `sigma` fails on at least one of
them, since otherwise its `A`-side extension would glue across `Y` and
colour `G`.  The proof of the signature-change path lemma is independent of
the boundary order: a Kempe switch would extend across the named component
unless a full two-colour component joins the switched boundary component to
another one.  Applying that same argument supplies the two asserted literal
obstruction paths.

Every component behind an exact seven-boundary is adjacent to every
boundary vertex.  The exact-seven packing and adaptive-reflection theorems
leave packing number one or two on either orientation.  If the displayed
supports had a saturating matching for the legal partition, transported
partition reflection would reproduce that partition on the rejected shore
and the two colourings would glue.  Hall's theorem therefore gives (5.1).
\(\square\)

## 6. Exact contribution and remaining gap

The theorem replaces both remaining order-eight component counts by one
operation-decorated alternative:

1. a clean five-path fan whose unresolved datum is the literal first-hit
   map into the inherited minor-model branch sets; or
2. an exact order-seven separation carrying two different exact-`J`
   partitions, bilateral Hall-deficiency certificates, and literal
   operation-specific transition paths in both orientations.

Neither output is terminal.  A proof-closing theorem must use the inherited
branch-set labels and the selected proper-minor response to do at least one
of the following:

- allocate the clean fan to the five required labels while preserving a
  connected residual subgraph;
- make one transition meet a complete Hall duty; or
- preserve one complete equality partition through both shores.

The first-hit rank alone cannot supply these conclusions: its strict
gammoid form requires globally disjoint unit-capacity source paths, while
the relaxed connected-kernel rank permits overlaps inside the response
subgraph.  A rank defect also gives an order-seven boundary only after the
unused-label exposure satisfies the separate literal counting bound.

## 7. Dependencies

- [Kempe transitions across a boundary-full order-eight separation](hc7_order8_full_component_kempe_transition.md)
- [prescribed spokes at a boundary-full order-eight interface](hc7_order8_prescribed_spoke_reduction.md)
- [transported-partition Hall reflection](hc7_transported_partition_hall_reflection.md)
- [exact-seven full-connected-subgraph packing](hc7_exact_seven_packet_packing.md)
- [adaptive reflection at an exact seven-boundary](hc7_exact7_adaptive_packet_reflection.md)
