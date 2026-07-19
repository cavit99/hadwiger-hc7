# Internal audit of the aligned two-edge bypass and separator theorem

**Verdict:** GREEN for Theorems 2.1 and 3.1, Proposition 4.1,
Corollaries 5.1 and 5.2, and the fixed-trace locked-edge conclusion in
Section 6, under the exact hypotheses and application scope stated in the
source.

**Audited source:** `hc7_aligned_two_edge_bypass_separator.md`, SHA-256

```text
de9e974aa71a2372933a65b01835d2543664ebe63ca637591b50b63cfb50efae
```

After the GREEN audit, only the source status line was changed to link this
audit.  The mathematical statement and proof are unchanged; this audit is
repinned to the resulting source hash above.

This is a separate internal mathematical audit, not external peer review.
Every proposed branch set and pairwise adjacency was checked explicitly.
The two deletion-colouring arguments were reconstructed independently, as
were the full-neighbourhood separator, both response-language inclusions,
the shared/disjoint lock allocation, and the locked-edge first-hit claim.

## 1. Aligned setting

The seven sets in (1.1) are disjoint connected branch sets which cover the
host.  Their only missing model adjacency is `{x}`--`B`.  The three named
edges have the placements required later:

```text
g=xv with v in Z,
f=vu with u in B,
e=rs with r in Z and s in B.
```

The condition `v ne r` guarantees that `e` and `f` are distinct even when
`u=s`.  Thus deleting `f` leaves `e` as a genuine `B`--`Z` edge.  No proof
step requires `u` and `s` to be distinct.

Since `G` is not six-colourable, the ends of a deleted edge have one common
colour in every six-colouring of its deletion.  This elementary critical-edge
fact applies separately to the given colourings of `G-g` and `G-f`; no
minor-minimality assumption beyond existence of those two colourings is used.

## 2. The simultaneous bypass

Theorem 2.1 is correct.

In the colouring `d` of `G-g`, the ends `x,v` of `g` have common colour
`alpha`.  The edge `f=vu` is present, so `d(u)=beta ne alpha`.  If `x` and
`v` lay in distinct `alpha`--`beta` components, switching the component
containing one endpoint would make `g` proper and six-colour `G` after its
restoration.  They therefore lie in one component, and the edge `vu` places
`u` in that component as well.  A simple `x`--`v` path `P` in it avoids
`g` because it lies in `G-g`.

Likewise, in the colouring `psi` of `G-f`, the endpoints `v,u` have common
colour `lambda`.  Equality (1.4) gives `psi(x)=alpha`, and the present edge
`xv` forces `alpha ne lambda`.  Critical-edge switching for `f` places
`v,u` in one `lambda`--`alpha` component; `xv` also places `x` there.  A
simple `v`--`u` path `Q` in that component avoids `f`.

The three path-placement cases cover all possibilities:

1. If `u` lies on `P`, its `x`--`u` subpath avoids `f`.  A simple path ending
   at `v` can use `uv` only as its final edge, which is not in that subpath.
2. If `x` lies on `Q`, its `x`--`u` subpath avoids `g`.  A simple path
   starting at `v` can use `vx` only as its first edge, which is not in that
   subpath.
3. Otherwise `P` avoids `f` because it avoids `u`, while `Q` avoids `g`
   because it avoids `x`.  Both contain `v`, so their union is connected in
   `G-{g,f}` and contains `x,u`.

Thus a simple `x`--`u` path avoiding both named edges exists.  The argument
does not claim that the two differently coloured paths themselves form one
properly coloured object.

## 3. The donor branch-set split and both minor models

Let `W` be the component of `G[Z-v]` containing `r`.  Every component of
`G[Z-v]` has a neighbour at `v`, since otherwise connectedness of `G[Z]`
would fail.  Therefore `L=Z-W` consists of `v` together with the other
components, is connected, and is adjacent to `W`.

If `W` is adjacent to every `H_i`, the seven proposed branch sets in (3.5)
are disjoint and connected.  Their non-inherited adjacencies are all present:

```text
({x} union L)--B       via f=vu,
({x} union L)--W       via a W--L edge,
({x} union L)--H_i     via the old {x}--H_i adjacency,
W--B                   via e=rs,
W--H_i                 by the case assumption.
```

Every other pair is adjacent in the original labelled model.  Hence these
sets form an explicit `K_7`-minor model.

If `W` instead misses `H_j`, then `H_j` is disjoint from both `W` and
`N_G(W)`.  The full neighbourhood `N_G(W)` separates the nonempty connected
set `W` from a nonempty component containing `H_j`.  It is consequently a
genuine vertex cut, and seven-connectivity proves `|N_G(W)|>=7`.

Now assume additionally that `x in N_G(W)`.  If `L` is adjacent to every
`H_i`, the seven sets in (3.6) again give an explicit model.  The complete
check of the non-inherited adjacencies is:

```text
({x} union W)--B       via e=rs,
({x} union W)--L       via a W--L edge,
({x} union W)--H_i     via {x}--H_i,
L--B                   via f=vu,
L--H_i                 by the case assumption.
```

The first set is connected because `x in N_G(W)`.  Thus, outside the
`K_7` outcome, some `H_k` is anticomplete to `L`.  The index satisfies
`k ne j`: the original `Z` branch set is adjacent to `H_j`, and since
`W` misses `H_j`, an old `Z`--`H_j` edge must have its `Z` endpoint in
`L`.  This verifies the complementary label split exactly as stated.

## 4. Endpoint placement on the returned full neighbourhood

Put `S=N_G(W)`.  The component `W` has a neighbour at `v`, so `v in S`.
The singleton `x` and the branch-set vertex `u in B` both lie outside `W`.

The colouring `d` is proper on every host edge except possibly `g=xv`, and
its two ends have equal colour.  Both ends lie in `W union S` exactly when
`x in S`, because `v in S` and `x notin W`.  Therefore its restriction is
proper exactly when `x notin S`; in the other case `g` is its unique failed
edge.  The identical argument for `psi` and `f=vu` proves the second claim,
with `u in S` as the exact placement condition.

If the two deletion colourings have the same labelled trace on an old
boundary `X`, they agree vertex-by-vertex on `X intersect S`; this is a
labelled-colour assertion, not merely equality of the induced partitions.
The proposition correctly refrains from claiming agreement on all of `S`.

When `|S|=7`, the separator is an actual order-seven interface.  Neither
seven-connectivity nor the endpoint-placement facts synchronize the two
complete boundary partitions, and the source does not assert otherwise.

## 5. Opposite response languages and lock allocation

### Corollary 5.1

The application of the audited opposite-boundary-response theorem is exact.
Map its deficient branch set to the present `B`, its singleton branch set to
`{x}`, and its donor branch set to `Z`.  The required five-set `K_6` model is
`{x},Z,H_1,...,H_4`; `B` is anticomplete to `{x}`, adjacent to the other
five sets, and has no neighbours outside them because the model is spanning.

The two selected `B`-attachment vertices in the donor are the distinct
vertices `r,v`.  With the cut vertex of the response theorem equal to `v`,
its component containing `r` is exactly the present `W`, and its
complementary connected set is the present `L`.  The required
`L`--`{x}` contact is `g=xv`.  Since `W` is anticomplete to `H_j` while the
old donor `Z` is adjacent to `H_j`, every donor endpoint of a `Z`--`H_j`
edge lies in `L`; hence `H_j` belongs to the theorem's lost-contact family.

The response theorem also gives the exact donor-internal attachment

```text
N_Z(W)={v}.
```

Thus an edge `vw_0` with `w_0 in W` and an edge `t_jh_j` from `L` to
`H_j` are precisely its two oppositely situated response edges.  For
`S=N_G(W)`, `C=G[W union S]`, and `O=G-W`, a colouring of `G-vw_0`
restricts properly to the unchanged shore `O`, while a colouring of
`G-t_jh_j` restricts properly to the unchanged shore `C`.  If either
induced equality partition extended through the opposite shore, a
permutation of the six colour names would align the two literal boundary
colourings and glue them to a six-colouring of `G`.  Consequently

```text
Resp(vw_0,S)       is contained in Ext(O,S)-Ext(C,S),
Resp(t_jh_j,S)     is contained in Ext(C,S)-Ext(O,S).
```

Both response languages are nonempty because the relevant edge deletions
are proper minors under the additional hypothesis in Section 5.  The two
set differences are disjoint, proving (5.5).  This is an equality-partition
statement: it does not assert that the two response languages intersect or
that their labelled colour names already agree.

### Corollary 5.2, shared endpoint

The two geometric cases are exhaustive.  If `v` has a neighbour `h_j` in
`H_j`, choose the lost-contact edge as `vh_j`.  The named edges
`vw_0,vh_j` are distinct incident edges, and their leaves `w_0,h_j` are
nonadjacent by (3.2).  Contracting the two-edge path is a proper minor, so
the audited incident-edge bichromatic-bypass theorem applies with six
colours.

It gives exactly the stated alternative in one expanded simultaneous-
contraction colouring: one named pair is linked for all five alternate
colours, or `G-{vw_0,vh_j}-v` has a `w_0`--`h_j` path contained in two named
bichromatic components and at most one joining edge.  In the latter case,
the first vertex after the path leaves `W` belongs to `S=N_G(W)` and is not
`v`, because the path avoids `v`.  Since `N_Z(W)={v}`, that first exit is
outside the old donor `Z`.  No stronger assertion about which old branch
set it first meets is made.

### Corollary 5.2, disjoint endpoints

If `v` has no neighbour in `H_j`, every chosen `L`--`H_j` edge
`t_jh_j` has `t_j ne v`.  The edges `vw_0` and `t_jh_j` are then
vertex-disjoint: their four endpoints lie respectively in `L`, `W`,
`L-{v}`, and `H_j`, with these relevant sets disjoint.

The audited double-contraction allocation theorem applies because the
additional hypothesis that every proper minor is six-colourable, together
with non-six-colourability, implies `chi(G)=7`.  A double-contraction
colouring expands to the common host

```text
G-{vw_0,t_jh_j}
```

with both endpoint pairs monochromatic.  If their common colours coincide,
one pair has bichromatic paths for at least three of the five alternate
colours.  If the colours differ, one pair has at least four.  Hence the
unconditional lower bound three is correct.

The cross-edge sharpening is also exact.  Between the endpoint pairs the
four possible cross-edges are:

```text
w_0t_j   absent because N_Z(W)={v},
w_0h_j   absent by (3.2),
vh_j     absent in the present case,
vt_j     the only remaining possibility.
```

If `vt_j` exists, the two contracted images are adjacent and must receive
distinct colours.  The four-path branch of the allocation theorem therefore
applies.  Every lock path lies in the common two-edge-deletion host and
avoids both named edges.  Neither the three-path nor four-path conclusion
asserts path disjointness or identifies palette colours with old branch-set
labels.

## 6. Fixed-trace locked-edge first hit

Section 6 is valid in its explicitly additional fixed-trace application.
Its “old boundary `X`” and list assignment `L_c` are imported from the
persistent-edge fixed-trace alignment: in that application `x in X`, the
edge `f=vu` belongs to the edge-minimal non-`L_c`-colourable subgraph `F`,
and `g=xv` is among the `F`--`X` edges of the local graph.  This paragraph is
not a consequence of the bare model hypotheses (1.1)--(1.4) without those
additional data.

The restriction of `psi` colours `F-f` from `L_c`, and the ends `v,u` have
common colour `lambda`.  The edge `xv` is present in `G-f`, so
`alpha=psi(x)` differs from `lambda`; it places `x` in the local
`lambda`--`alpha` component containing `v`.

Apply the locked-edge alternative to `f` with the second colour `alpha`.
If the endpoint components coincide, that component contains `u,v,x`.
Otherwise both endpoint components meet the old boundary.  A shortest first
hit from the component containing `u` ends at some `y in X` and has internal
vertices in the fixed-trace critical subgraph.  It cannot end at `x`, since
`x` lies in the distinct component containing `v`.  Hence
`y in X-{x}` exactly as claimed.

The source correctly records two limitations.  The first-hit vertex is not
assigned to any named `H_i`, and the local fixed-trace graph need not contain
all host edges.  Consequently its path cannot be combined with Theorem 2.1
as if both paths came from one common colouring.

## 7. Trust boundary

The audited note proves:

1. an `x`--`u` bypass avoiding both aligned critical edges;
2. an explicit `K_7`-minor model or a full-neighbourhood donor separator;
3. a complementary two-label contact split when `x` lies on that separator;
4. exact placement of the two single failed edges in the closed
   `W`-shore; and
5. two nonempty oppositely oriented response languages attached to the
   unique donor interface and the named lost contact;
6. a shared-endpoint saturation/bypass alternative or a disjoint-edge
   three-lock allocation, sharpened to four locks by the sole possible
   cross-edge; and
7. in the additional fixed-trace setting, a local connection through
   `u,v,x` or a second literal boundary first hit.

It does not upper-bound the returned separator, synchronize a complete
boundary colouring, assign palette colours or first hits to the four named
branch sets, or reconstruct a smaller aligned tuple.  No such unproved
conclusion is used in the source.  Within this scope, no unresolved
mathematical gap was found.
