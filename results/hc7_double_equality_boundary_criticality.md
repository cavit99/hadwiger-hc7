# Boundary-preserving criticality in the simultaneous-equality colouring

**Status:** written proof, independently audited in
[`hc7_double_equality_boundary_criticality_audit.md`](hc7_double_equality_boundary_criticality_audit.md).
The general lemmas below identify exactly what a six-colouring obtained after contracting
two opposite-shore edges forces when its boundary colouring cannot be
preserved while either edge is restored.  The final section applies the
lemmas to the balanced order-eight configuration.  It does not eliminate
that configuration or prove `HC_7`.

## 1. Boundary traces and one-sided repairs

Let

\[
 V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}B
\]

with no edge between `A` and `B`.  Let

\[
                  e=uv\in E(G[A]),\qquad f=yz\in E(G[B])
\]

be vertex-disjoint edges, put `H=G-{e,f}`, and suppose that `kappa` is a
proper `q`-colouring of `H` satisfying

\[
                  \kappa(u)=\kappa(v),\qquad
                  \kappa(y)=\kappa(z).                 \tag{1.1}
\]

Write `tau=kappa|_S`.  The edge `e` is **repairable with trace `tau`** if
`G[A union S]` has a proper `q`-colouring whose restriction to `S` is
literally `tau`.  Define trace-preserving repairability of `f`
symmetrically.  Requiring the same equality partition on `S` is equivalent:
a permutation of the colour names aligns such a colouring literally with
`tau`.

### Lemma 1.1 (orientation of a simultaneous-equality trace)

If `G` is not `q`-colourable, then `e` and `f` are not both repairable with
trace `tau`.

More precisely:

1. `e` is repairable with trace `tau` if and only if the boundary
   partition of `kappa` is induced by a `q`-colouring of `G-f`; every
   resulting common-host colouring has signature `(proper,equal)`;
2. `f` is repairable with trace `tau` if and only if the boundary
   partition of `kappa` is induced by a `q`-colouring of `G-e`; every
   resulting common-host colouring has signature `(equal,proper)`; and
3. if neither repair exists, the boundary partition of `kappa` belongs to
   neither one-edge-restoration response family.

#### Proof

A repair of `e` is proper on the original closed side `G[A union S]`.
The restriction of `kappa` to `G[B union S]-f` is proper and has the same
literal boundary colours.  The two colourings therefore glue to a proper
colouring of `G-f`.  This proves the forward direction of assertion 1,
including its signature: `e` is proper, and the ends of `f` must remain
equal-coloured, since otherwise the same colouring would colour `G`.
Conversely, rename any `q`-colouring of `G-f`
with the displayed boundary partition so that it agrees with `tau` on
`S`, and restrict it to `A union S`; this is a trace-preserving repair of
`e`.  Assertion 2 is symmetric.

If both repairs existed, they would agree on `S` and would glue to a proper
`q`-colouring of all of `G`, a contradiction.  Assertion 3 follows from
the two equivalences.  \(\square\)

The lemma deliberately allows the possibility that neither edge is
repairable with the displayed trace.  Ruling out that possibility would be
a new boundary-state synchronization theorem; it does not follow merely
from the existence of colourings after deleting or contracting each edge.

## 2. The exact fixed-boundary Kempe certificate

The next lemma is local to one closed side.  Let `X` be a graph, let
`S subseteq V(X)`, and let `uv` be an edge whose ends lie outside `S`.
Suppose `kappa` is a proper `q`-colouring of `X-uv` with

\[
                           \kappa(u)=\kappa(v)=\alpha. \tag{2.1}
\]

### Lemma 2.1 (locked pair or literal boundary paths)

Assume that no proper `q`-colouring of `X` agrees with `kappa` at every
vertex of `S`.  For each colour `beta!=alpha`, let `K_u,K_v` be the
components containing `u,v` in

\[
                 (X-uv)[\kappa^{-1}(\{\alpha,\beta\})]. \tag{2.2}
\]

Then exactly one of the following two component alternatives holds.

1. `K_u=K_v`, so (2.2) contains a literal `u-v` path.
2. `K_u!=K_v`, both components meet `S`, and there are vertex-disjoint
   paths from `u` and `v` to two distinct vertices of `S`, respectively,
   whose internal vertices avoid `S`.

In particular, each of `u,v` has a neighbour of every colour different
from `alpha`.  No interchange of `alpha,beta` on a union of components of
(2.2) which is disjoint from `S` can make `uv` proper.

#### Proof

Suppose first that `K_u` and `K_v` are distinct.  If, say, `K_u` avoided
`S`, interchange `alpha,beta` on all of `K_u`.  This preserves properness
of `X-uv`, changes no boundary colour, and changes exactly one end of
`uv`.  Restoring `uv` would give the excluded colouring of `X`.  Thus both
components meet `S`.

In each component choose a shortest path from its named endpoint to `S`
and stop at the first boundary vertex.  The two paths are disjoint because
their components are distinct; their boundary ends are distinct for the
same reason; and minimality makes both interiors avoid `S`.  This proves
alternative 2.  If the components are equal, their connectedness gives
alternative 1.

If an endpoint had no neighbour of colour `beta`, its bichromatic component
could not also contain the other endpoint, and the singleton endpoint
could be recoloured `beta` without changing `S`; this would repair `uv`.
Thus both endpoints see every alternate colour.  Finally, switching any
collection of components disjoint from `S` preserves the boundary.  If it
made `uv` proper it would again give the excluded colouring of `X`.
\(\square\)

When alternative 1 occurs, a shortest `u-v` path gives the following more
geometric trichotomy: it either has all internal vertices outside `S`, or
its two initial segments from `u,v` end at distinct boundary vertices and
are disjoint, or they end at one common boundary vertex and are internally
disjoint.  This refinement uses no connectivity assumption on `X`.

### Lemma 2.2 (list-critical core)

Under the hypotheses of Lemma 2.1, put

\[
 L(w)=[q]-\{\kappa(s):s\in N_X(w)\cap S\}
                    \qquad(w\in V(X)-S).              \tag{2.3}
\]

There is a connected induced subgraph `K` of `X-S` such that:

1. `K` contains `u,v` and the edge `uv`;
2. `K` is not `L`-colourable, but every proper induced subgraph of `K` is
   `L`-colourable;
3. `K-uv` is `L`-colourable; and
4. for every `w in V(K)`,

   \[
       d_K(w)\ge |L(w)|
       =q-|\kappa(N_X(w)\cap S)|.                     \tag{2.4}
   \]

Here the last term counts distinct boundary colours, not boundary
vertices.

#### Proof

A colouring of `X-S` from the lists (2.3) is exactly a colouring which
extends the fixed colouring `kappa|_S`.  Hence `X-S` with the edge `uv`
restored is not `L`-colourable, while `kappa|_{X-S}` is an `L`-colouring
after deleting `uv`.

Choose an induced non-`L`-colourable subgraph `K` minimal by vertex
inclusion.  It must contain both ends of `uv`; otherwise it is an induced
subgraph of the `L`-colourable graph `(X-S)-uv`.  Thus it contains `uv`,
and assertion 3 follows by restricting `kappa`.  Minimality gives assertion
2 and also forces connectedness, since an uncolourable component would be
a smaller choice.

For `w in V(K)`, colour `K-w` from its lists.  If
`d_K(w)<|L(w)|`, some colour in `L(w)` is absent from its coloured
neighbours, so the colouring extends to `w`, a contradiction.  This proves
(2.4).  \(\square\)

This critical core is a genuine fixed-boundary obstruction.  It need not
be separated from the rest of the open side by a small vertex set, and
(2.4) alone does not identify any colour with a prescribed branch set.
No Gallai-tree conclusion follows from (2.4) in general: the
degree-choosability theorem assumes that list orders are at least the
corresponding degrees, whereas (2.4) gives the reverse inequality.  It
could be invoked only after separately proving equality at every vertex.

## 3. Consequence for the balanced order-eight configuration

Use the notation and all hypotheses of
[`hc7_balanced_order8_frontier.md`](../active/hc7_balanced_order8_frontier.md).  Thus

\[
 S=R\mathbin{\dot\cup}V(e)\mathbin{\dot\cup}V(f)
       \mathbin{\dot\cup}\{x\},
\]

the open sides are `C,D`, the five-clique
`L=R union {ell_e,ell_f}` lies on the `C` side, and the second five-clique
`Y` has an edge `h` internal to `D`.  Put

\[
                         g=\ell_e\ell_f,
 \qquad                  H=G-\{g,h\}.
\]

Let `kappa` be a six-colouring of `H` obtained by expanding a colouring of
`G/g/h`; it has signature `(equal,equal)`.  Write `tau=kappa|_S`.

### Corollary 3.1 (one locked closed side)

At least one of the following holds.

1. `g` is not repairable in `G[C union S]` with trace `tau`.
2. `h` is not repairable in `G[D union S]` with trace `tau`.

For every nonrepairable edge and every colour different from its common
endpoint colour, Lemmas 2.1 and 2.2 apply inside that closed side.

If `g` is nonrepairable, let `gamma,delta` be the two colours absent from
the five vertices of `L` in `kappa`.  For each
`theta in {gamma,delta}`, the `kappa`-bichromatic subgraph on the colours
of `g` and `theta` contains either

1. an `ell_e-ell_f` path in `G[C union S]-g`; or
2. two vertex-disjoint paths from `ell_e,ell_f` to distinct literal
   vertices of `S`, with both interiors in `C`.

The analogous assertion holds for the two colours absent from `Y` when
`h` is nonrepairable.

#### Proof

Lemma 1.1 says that at least one of the displayed alternatives holds.
Apply Lemma 2.1 to the
corresponding closed side.  The three colours on `R` already join
`ell_e,ell_f` through the three length-two paths in the clique `L`, so the
two colours absent from `L` are the two nontrivial applications on the
`C` side.  The same argument uses the three other vertices of `Y` in the
closed `D`-side graph.  \(\square\)

### Lemma 3.2 (no web-attachment vertex lies on the leaf side)

Let `Q` be the contracted graph and let `W^+` be the web completion in the
canonical rooted-web theorem.  Let

\[
                         T=\{z_e,z_f,x\}
\]

be the facial triangle localized by the second five-clique.  Every vertex
of the component of `Q-T` containing `ell_e,ell_f` is a vertex of the
planar skeleton `W`.  Equivalently, every vertex belonging to one of the
web attachment sets `X_U` lies in the other component of `Q-T`.

#### Proof

Because `Q` is a spanning subgraph of `W^+`, it has the same vertex set as
the web completion.  Suppose `X_U` is nonempty for a facial triangle `U`
of `W`.  In `W^+`, and hence in `Q`, every neighbour of a vertex of `X_U`
belongs to `U union X_U`.  Thus deleting `U` separates the nonempty set
`X_U` from an outer root not in the three-set `U`.  Consequently `U` is a
three-vertex cut of `Q`.

The exact rooted-web hypotheses say that every three-vertex cut of `Q`
contains both `z_e,z_f`.  The virtual edge `z_ez_f` lies on the
four-vertex outer face of the planar skeleton and is incident with only
one bounded facial triangle.  Therefore `U=T`.  This proves that every
web-attachment vertex belongs to `X_T`.

After deleting `T`, no vertex of `X_T` has an edge to a skeleton vertex.
The rooted-web theorem also says that `Q-T` has exactly two components:
one contains `ell_e,ell_f`, while the other contains a vertex of the image
of the second five-clique lying in `X_T`.  If any vertex of `X_T` lay in a
different component from that clique vertex, `Q-T` would have at least
three components.  Hence all of `X_T` lies in the second component, and
the leaf component contains only skeleton vertices.  \(\square\)

This is a deduction from the hypotheses of the promoted rooted-web theorem,
not an additional property supplied by the abstract Two Paths theorem.

### Corollary 3.3 (a planar fixed-boundary critical core)

If `g` is not repairable with trace `tau`, the critical core `K` supplied
by Lemma 2.2 is a planar graph contained in `C`, where `C` is the component
of `Q-T` containing `ell_e,ell_f` after lifting the two contractions.  Put

\[
 c(w)=|\kappa(N_G(w)\cap S)|\qquad(w\in V(K)),         \tag{3.1}
\]

again counting distinct colours.  If `|K|>=3`, then

\[
                         \sum_{w\in V(K)}c(w)\ge12.   \tag{3.2}
\]

If `K` consists only of the two ends of `g`, each end sees all five other
boundary colours.

#### Proof

Lemma 3.2 puts `C` in the planar web skeleton.  Deleting `R` and
contracting `e,f`, which are disjoint from `C`, changes no edge with both
ends in `C`.  Hence `G[C]=Q[C]` is planar, and so is its subgraph `K`.

By (2.4), `c(w)>=6-d_K(w)`.  For a simple planar graph of order at least
three,

\[
 \sum_w c(w)\ge6|K|-2|E(K)|\ge12,
\]

which proves (3.2).  If `K` is the single edge `g`, nonempty lists at its
two ends have no system of distinct representatives, while each one-vertex
proper induced subgraph is list-colourable.  Both lists are consequently
the same singleton, namely the common endpoint colour in `kappa`.  Each
endpoint therefore sees all other five colours on `S`.  \(\square\)

This is a global incidence bound on a planar obstruction, not a labelled
linkage: one boundary colour may occur on several literal boundary
vertices, and (3.2) does not prescribe which defect edge or which vertex
of `R` receives a contact.

### Corollary 3.4 (the labelled first-hit patterns which already close)

Suppose `g` is nonrepairable and, for one of the two colours absent from
`L`, Lemma 2.1 gives two first-hit paths.  Each of the following placements
of their boundary ends gives a `K_7` minor.

1. The path from `ell_e` ends in `V(e)` and the path from `ell_f` ends in
   `V(f)`.
2. The path from `ell_f` ends at `x` and the path from `ell_e` ends in
   `V(e)`.
3. The path from `ell_e` ends at `x` and the path from `ell_f` ends in
   `V(f)`.

#### Proof

In outcome 1, contract `e,f` and delete `R`.  The two first-hit paths have
internal vertices in `C`, so they give the missing
`ell_e-z_e,ell_f-z_f` linkage in the four-root graph from the
[canonical rooted-web theorem](../results/hc7_star_order_eight_rooted_web.md).
Together with the other two pair-linkages proved there, this gives a
`K_4` minor rooted at `ell_e,ell_f,z_e,z_f`.  Lift the four rooted branch
sets, replacing `z_e,z_f` by the literal edges `e,f`, and add the three
singleton branch sets from `R`.  The leaf roots are adjacent to every
member of `R`, and each defect edge is collectively adjacent to every
member of `R`; hence these seven sets are pairwise adjacent and form the
required `K_7`-minor model.

In outcome 2, delete the terminal boundary vertex from each first-hit
path.  The remaining two paths are disjoint connected subgraphs of `C`:
one contains `ell_f` and has a neighbour at `x`, while the other contains
`ell_e` and has a neighbour in `V(e)`.  The promoted
[split-edge completion](../results/hc7_star_order_eight_split_edge_completion.md)
gives a `K_7` minor.  Outcome 3 is its symmetric application.  \(\square\)

## 4. Exact remaining failure of the double-equality route

The preceding argument does not force the nonrepairable edge to be `g`.
Even when it is `g`, Lemma 2.1 does not prescribe the two first boundary
hits; they may avoid all three placements in Corollary 3.4, or the relevant
bichromatic component may contain the two leaves without yielding either
of the promoted disjoint path patterns.  The existing
[two-path counterexample](../barriers/hc7_balanced_order8_two_missing_colour_paths.md)
shows that even complete Kempe locking of the leaf edge, together with the
canonical web and the localized second five-clique at quotient level, does
not repair the rooted model.

Thus the missing implication can now be stated sharply:

> use `K_7`-freeness and global minor-minimality to force a
> trace-preserving repair on the localized-clique side, or to force one of
> the three labelled first-hit patterns in Corollary 3.4; otherwise turn
> the two fixed-boundary list-critical cores from Lemma 2.2 into an actual
> order-seven separation or a two-vertex transversal of the relevant
> `K_5`-minor models.

Neither the canonical web theorem nor fixed-boundary Kempe switching alone
supplies this implication.  Completion edges of the web are not host
edges, and the critical core in Lemma 2.2 need not have a small external
neighbourhood.
