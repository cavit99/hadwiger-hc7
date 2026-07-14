# Audit: composition at the compulsory Hall portal

**Verdict:** GREEN at frozen source SHA-256
`59c35ba79fcc34b27331a77688fa49fde5f8c2b53059ec5dc9322fccea7eae11`.
The only changes from the composition source audited line by line were its
status line and the companion fan's promoted filename.

The three-carrier trace construction, the two near-model handoffs, the twin
exact-seven boundary, the Kempe and palette locks, and the sharpness example
are all correct under the inherited compulsory-Hall hypotheses.  Every
model below uses literal, disjoint branch sets and every separation is a
separation in `G`, not in a quotient.

The companion fan source was separately checked at SHA-256
`ad8e000c929e8cec02bb1093cbf3630addb0c85fda367386009b58f94d4fb6d5`.
Its only post-audit change was likewise the status line.
The promoted Hall-classification dependency has source SHA-256
`6adbb2ede7cdd0f54b6594eb1fe753d7ce08ffb2573a4453364718986e9b9279`;
its audit records that promotion changed only the status line of the
independently checked mathematical source.

## 1. Literal partition and bridge interface

The inherited sets satisfy

\[
 L=C\mathbin{\dot\cup}Y\mathbin{\dot\cup}\{z\},\qquad
 S=(S-U)\mathbin{\dot\cup}U,
\]

so

\[
 A=C\cup\{z\},\qquad W=(S-U)\cup Y,\qquad O=R\cup U
\]

are pairwise disjoint and partition `V(G)`.  The order computation is

\[
 |W|=7-|U|+(|U|-1)=6.
\]

There is no `C-R` edge by the old separation and no `C-U` edge because
`X=N_L(U)`.  There is no `z-R` edge, and the compulsory outcome says that
the sole `z-U` edge is the literal edge `zu_*`.  Hence `zu_*` is the only
`A-O` edge in `G-W`.

The set `A` is connected because connected `C` has a neighbour at `z` by
`Omega`-fullness.  Since `G` is seven-connected, deletion of the six-set
`W` leaves a connected graph.  The sole `A-O` edge then forces all of `O`
to lie in the component of `u_*`; in particular `O` is connected and
`zu_*` is a literal bridge of `G-W`.

The companion six-fan theorem is correct here.  Seven internally disjoint
`z-u_*` paths consist of the edge `zu_*` and six detours.  Every detour
must meet `W`; internal disjointness and `|W|=6` make it meet exactly one
distinct member of `W`.  Contracting the mutually internally disjoint
segments on the two bridge sides yields the rooted minor
`K_2 join G[W]` without identifying a literal member of `W`.

## 2. Lemma 2.1: the trace partition, including `|U|=1`

Put `k=|U|`.

* For `k=1`, `Y` is empty.  The partition `T_1=U`, `T_2=emptyset` is
  valid because the empty set vacuously dominates the empty set `Y`.
  This is the only place an empty trace is used.
* For `k=2`, `Y={y}`.  Applying Hall minimality to each proper singleton
  of `U` forces `y` to meet both vertices, so the two singleton parts both
  dominate `Y`.
* For `k=3`, write `Y={y_1,y_2}`.  If some `y_i` had only one neighbour
  `u`, then the two-set `U-{u}` would see at most the other member of `Y`,
  contradicting (1.2).  Thus both `y_i` have degree at least two into the
  three-set `U`, and their neighbourhoods intersect.  For a common
  neighbour `t`, both `{t}` and `U-{t}` dominate `Y`; the latter works
  because every `y_i` has a second neighbour.

Interchanging the two parts always puts `u_*` in `T_1`.  Thus the
construction is exhaustive and has no hidden nonemptiness assumption in
the atomic case.

## 3. Theorem 2.2: exact carrier path

The three sets

\[
 A=C\cup\{z\},\qquad B_1=P\cup T_1,\qquad B_2=Q\cup T_2
\]

are pairwise disjoint: `A` lies in the old `L` side, `P,Q` are disjoint in
`R`, and `T_1,T_2` partition the old boundary subset `U`.

Each `B_i` is connected.  Its old packet is connected and every literal
member of `T_i` has a neighbour in that `S`-full packet; for `T_2=emptyset`
this simply says `B_2=Q`.  The packet contacts `S-U`, and trace domination
contacts `Y`, so both sets are `W`-full.  The old literal `P-Q` edge gives
`B_1-B_2`.

The connected set `C` contacts every member of `W subseteq Omega`, hence
`A` is `W`-full.  The compulsory edge `zu_*`, with `u_* in T_1`, gives
`A-B_1`.  The edge exclusions in Section 1 rule out every possible
`A-B_2` edge: there is no `C-Q`, `C-T_2`, `z-Q`, or `z-T_2` edge.  Thus
the carrier adjacency graph is exactly the path

\[
                         A-B_1-B_2.
\]

## 4. Corollary 3.1: a boundary `K_4` gives seven literal bags

Let `D_1,...,D_4` be disjoint branch sets of a `K_4` model in `G[W]`.
They are disjoint from `A,B_1,B_2`, since the latter sets lie outside `W`.
Every carrier is `W`-full, so it has an edge to every nonempty `D_i`:
choose any literal `w in D_i` and use that carrier's neighbour at `w`.
The four `D_i` are pairwise adjacent, and the three carriers have exactly
the two path edges.  Therefore

\[
                    A,B_1,B_2,D_1,D_2,D_3,D_4
\]

are seven disjoint connected branch sets with sole possibly missing pair
`A-B_2`.  This is a literal `K_7^-` model.  Ignoring one additional edge
incident with the same deficient bag makes it a valid `K_7^vee` model.
Consequently an unresolved core is genuinely `K_4`-minor-free, hence has
treewidth at most two and is three-colourable.

## 5. Corollary 3.2: atomic rooted-triangle handoff

When `U={u_*}`, one has `Y=emptyset`, `W=S-{u_*}`,
`B_1=P union {u_*}`, and `B_2=Q`.  The six rim bags

\[
                    \{u_*\},P,Q,D_1,D_2,D_3
\]

are disjoint.  The first three form a triangle because the old packets
are adjacent and both meet the old boundary literal `u_*`.  Packet
fullness joins `P,Q` to every `D_i`; the rooted hypothesis joins
`{u_*}` to every `D_i`; and the `D_i` form a triangle.  Thus the rim is a
literal `K_6` model.

The seventh bag `A` meets `{u_*}` through `zu_*` and meets every `D_i` by
`W`-fullness.  It is anticomplete to `P,Q`, so its only two missing rim
spokes share the endpoint `A`.  These bags form exactly the claimed
labelled `K_7^vee` model.

## 6. Lemma 4.1: the twin boundary and strict descent

Every member of `W` has a neighbour in `C subseteq A`, and `u_*` meets
`z in A`.  The bridge exclusions show that `A` has no other outside
neighbour.  Therefore

\[
                         N_G(A)=W\cup\{u_*\}=\Sigma.
\]

Now let `K` be a component of `G[O-{u_*}]`.  It has no edge to `A`, and
no edge to another such component.  Hence `N_G(K) subseteq Sigma`.  The
nonempty set `A` remains outside `K union N_G(K)`, so `N_G(K)` is a literal
vertex cut.  Seven-connectivity and `|Sigma|=7` force
`N_G(K)=Sigma`.  Since `R` is nonempty, at least one such component exists.
Thus `Sigma` is an actual exact-seven separator, and all displayed
fullness claims follow from neighbourhood equality rather than from a
quotient convention.

Finally,

\[
 A=(L-X)\cup\{z\}=L-Y,
 \qquad |A|=|L|-(|U|-1).
\]

This is a strict `L`-shore decrease for `|U|=2,3`.  For `|U|=1`, `Y` is
empty and `Sigma=(S-{u_*}) union {u_*}=S`, so there is correctly no
shore-order decrease.

## 7. Lemma 5.1: exact Kempe locks

Edge deletion makes `G-e` a proper minor, so strong
seven-contraction-criticality gives it a six-colouring.  In every such
colouring the ends `z,u_*` have the same colour `alpha`; otherwise restoring
`e` would six-colour `G`.

For `beta ne alpha`, if the `alpha-beta` component of `z` omitted `u_*`,
swapping its two colours would give the ends of `e` distinct colours and
again six-colour `G`.  Hence the endpoints lie in one bichromatic
component.  Every resulting path is a path in `G-e`; the sole `A-O` edge
of `G-W` was `e`, so every such path meets the literal six-set `W`.

If `alpha` is absent from `W`, the `alpha-beta` path for each of the other
five palette colours must meet a `beta`-coloured boundary vertex.  Thus all
five other colours occur on `W`, making `alpha` the unique missing palette
colour.  If instead `beta` is absent, every crossing vertex of the
`alpha-beta` path in `W` has colour `alpha`.  These are exactly the claims
made; the lemma does not assert disjoint Kempe paths.

## 8. Lemma 5.2: exact palette compatibility

If two closed-shore colourings induce the same exact partition `Pi` on
`W`, agreement on each literal boundary vertex forces the colour of each
named block on one side to map to the colour of that same block on the
other.  This fixes a bijection on the `|Pi|` used boundary colours and
leaves an arbitrary bijection on the `6-|Pi|` spare colours.

After this alignment:

* endpoints of distinct named block types have distinct colours;
* a block-type endpoint and a spare endpoint have distinct colours; and
* two spare endpoints can be made distinct exactly when at least two spare
  colours are available.

The only unavoidable collisions are therefore the same named boundary
block, or two spare endpoints when `6-|Pi|=1`, equivalently `|Pi|=5`.
There is no spare endpoint when `|Pi|=6`.  Since `zu_*` is the sole
open-shore cross-edge, agreement on `W` plus inequality at its endpoints
is sufficient to glue the two colourings.  The two listed locks are exact.

## 9. The `K_2 join` icosahedron falsifier

The advertised NetworkX labelling was independently reconstructed.  In
the icosahedral graph `H`,

\[
 N_H(8)=\{0,1,2,7,9\},
\]

and deleting `W_0={0,1,2,7}` leaves a connected graph whose unique bridge
is `8-9`.  The edges `01,05,15` are present, so `0,1,5` form the claimed
triangle away from `8,9`.  NetworkX also returns vertex-connectivity five,
as expected for the icosahedron.

For `G=K_2 join H`, deletion of fewer than seven vertices leaves a join
vertex, which connects all survivors, or deletes both join vertices and at
most four vertices of the five-connected graph `H`.  Hence `G` is
seven-connected.

For every graph `F`,

\[
                         \eta(K_r\vee F)=r+\eta(F).
\]

The lower bound adjoins the `r` join singletons to a maximum model in
`F`.  For the upper bound, at most `r` bags of any clique model contain a
join vertex; deleting those bags leaves a clique-minor model wholly in
`F`.  Since planar `H` has no `K_5` minor, `eta(H)<=4`, and therefore this
`G` has no `K_7` minor.

On the other hand, `G-{8,9}` contains the literal `K_5` formed by the two
join vertices and the triangle `0,1,5`.  With
`W=V(K_2) union W_0`, deletion of `W` leaves the bridge `8-9`.  Thus the
example validates the precise warning: the bridge ends need not be the
desired fixed pair.  It does not contradict the near-model-or-some-pair
disjunction, and it is not asserted to be contraction-critical.

## 10. Exact trust boundary

The proved composition leaves exactly the stated atomic dynamic cell:
`|U|=1`, a `K_4`-minor-free six-core, no required rooted triangle, and the
Kempe/palette locks.  The note correctly does not claim that these facts
already produce a literal `K_7`, preserve an attained state through a
descent, or identify `{z,u_*}` as a coherent apex pair.
