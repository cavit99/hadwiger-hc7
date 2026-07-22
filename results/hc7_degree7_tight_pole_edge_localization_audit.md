# Independent audit: degree-seven tight-pole edge localization

**Verdict:** **GREEN** for the exact source revision

```text
df9c3b32584ee46379993e2a94ad677b14088e7c56545e4542d91b4dc456e171  results/hc7_degree7_tight_pole_edge_localization.md
```

This is a separate internal mathematical audit, not external peer review.
The displayed revision was checked line by line, including the new
articulation-side localization theorem and the strengthened
internally-vertex-disjoint-path residual.  Any mathematical change requires
a fresh audit.

## 1. Setup and matching choice

The audited degree-seven anti-neighbourhood theorem makes
`C=G-N[u]` nonempty and connected, so `A=G-u=G[C union S]`.  The exact
matching-language theorem then gives

```text
M(A) = the one-edge matchings of F,
M(G[N[u]]) = the matchings of F of order at least two.
```

Dirac's neighbourhood inequality gives `alpha(G[S])<=2`, and the audited
bounded-interface input gives `chi(G[S])<=4`.  A proper colouring of the
seven-vertex graph `G[S]` has colour classes of order at most two.  It
therefore uses exactly four classes of sizes `2,2,2,1`, so their three
doubletons are an order-three matching in `F`.  The exact-language theorem
supplies the fixed `A`-colouring whose sole repeated boundary pair is
`e_0`.

## 2. Proposition 2.1: automatic tight-pole transition

Outside `e_0`, the five boundary vertices have five distinct colours.  For
`e_i=x_i y_i`, the roots are separate singleton components of the boundary
two-colour graph.  If they were in different full two-colour components of
`A`, swapping the component containing `x_i` would give the forbidden
`A`-matching `{e_0,e_i}`.  Hence both roots lie in one component `K_i`, and
no other boundary vertex lies there.

Swapping the singleton boundary component `{x_i}` merges `x_i,y_i`, keeps
`e_0`, and removes the old colour of `x_i` from `S`.  That colour can be
assigned to `u`, so the final trace extends through `G[N[u]]`.  The two
extension languages are disjoint by matching order, making the minimum
transition length exactly one.

The opposite open shore is empty after `u` is removed.  In the final trace
the two roots are nonadjacent vertices of the same colour, while the old
colour is absent from `S`; the route through `u` is therefore exactly the
tight-pole case of the audited pole-move normal form.  The palettes of
`K_1,K_2` are disjoint, so those full bichromatic components are
vertex-disjoint.

## 3. Theorem 3.1: prescribed edge response

An `x_i-y_i` separating edge is a bridge of the connected graph `K_i`.
Deleting it leaves two components `X,Y` containing the roots on opposite
sides.  Swapping the two colours on `X` is a Kempe interchange in `A-h`:
`h` is the only two-colour edge between the sides, and `K_i` is a full
two-colour component.  Only `x_i` changes on `S`, so the boundary matching
is exactly `{e_0,e_i}`.  Giving `u` the disappeared colour produces a
proper six-colouring of `G-h`.

Exactly one endpoint of `h` is swapped.  The endpoints consequently become
monochromatic, and the colouring descends to `G/h`.  If those endpoints
were in different common-colour/`theta` components for any alternate
colour, a swap at one endpoint would make `h` proper and six-colour `G`.
This proves all five component connections.  Paths inside `X,Y`, joined
through `x_i-u-y_i`, give the asserted literal old-palette route.  No
unstated shore-locality follows from that route.

## 4. Theorem 4.1: rank-smaller bridge side

The singleton case `C={v}` is correctly impossible.  Seven-connectivity
makes `v` adjacent to every vertex of `S`; in a six-colouring of `G-v`, the
colour of `u` is absent from `S` and can also be assigned to the nonadjacent
vertex `v`.

For `n=|C|>=2`, one has `|K_i|<=n+2`.  If `n>=3`, the smaller component of
`K_i-h` has order at most `floor((n+2)/2)<n`.  For `n=2`, only a `2+2`
split needs separate treatment.  Then `K_i` has four vertices; its bridge
cut, bipartition, and nonadjacent opposite-colour roots force the alternating
four-vertex path with the roots at its ends.  An end edge has a singleton
root side.  Thus a selected bridge side `W` always has `|W|<|C|`.

If the other bridge component has a vertex beyond the endpoint of `h`,
that vertex has no neighbour in `W`, since such an edge would reconnect the
two sides in the full induced two-colour graph.  If the other component is
a singleton, it is the other root; selecting that singleton instead leaves
the first root outside its closed neighbourhood because `e_i` is a
boundary nonedge.  Hence a nonempty far side exists.  The full neighbourhood
`N_G(W)` is an actual separator and has order at least seven.

When its order is seven, `W`, `N_G(W)`, and the far side satisfy the exact
partition and anticompleteness clauses of a generic response interface.
The selected bridge edge crosses from `W` to its boundary, and the colouring
from Theorem 3.1 is intact on the opposite closed shore.  Extension of its
complete boundary equality partition through the intact `W`-shore would
glue to a six-colouring of `G`.  Thus the response is rejected, and
`|W|<|C|` is a strict comparison on literal vertices of the unchanged host.
No upper bound is asserted when the boundary has order at least eight.

## 5. Theorem 4.2: articulation-side localization

The roots `x_i,y_i` are nonadjacent, so the vertex form of Menger's theorem
applies without an adjacent-root exception.  If there are not two
internally vertex-disjoint root-to-root paths, a vertex
`v notin {x_i,y_i}` separates them in `K_i`.  For their components `X,Y`
in `K_i-v`,

```text
min(|X|,|Y|) <= floor((|K_i|-1)/2)
              <= floor((|C|+1)/2) < |C|.
```

The last inequality is valid also for `|C|=2`; the setup itself excludes
`|C|=1` by the argument recorded in Theorem 4.1.  Choosing the smaller root
component therefore gives the claimed strict rank decrease.

The other root component is anticomplete to `W` in the full host.  Both
sets lie in the induced two-colour graph, so any host edge between them
would remain in `K_i-v` and join its two components.  It supplies a nonempty
far side, making `N_G(W)` an actual separator of order at least seven.

For any crossing edge `at`, every six-colouring of the proper minor
`G-at` restricts to the unchanged opposite closed shore.  If its complete
equality partition on `T=N_G(W)` extended through the intact closed
`W`-shore, a palette permutation and gluing would six-colour `G`.  This
argument is uniform over all such colourings, not merely one selected
colouring.  When `|T|=7`, all clauses of the generic exact-seven response
interface definition hold: `W` is connected, both open shores are
nonempty, `T=N_G(W)`, the selected edge crosses `W-T`, and the opposite
shore carries the proper-minor response.  The result need not preserve the
old matching or palette, exactly as the source warns.  For `|T|>=8`, only
the stated positive-excess response is proved.

Consequently the exhaustive residual is legitimately strengthened from
two edge-disjoint routes to two internally vertex-disjoint routes in every
layer that yields no smaller response-bearing separator.

## 6. Corollary 5.1 and the residual

The two full bichromatic components use disjoint palettes and are
vertex-disjoint.  Edges may join the components, but swapping colours
within either disjoint palette preserves every such edge, so the swaps
commute.  Each single swap gives its prescribed deletion response.  The
double swap gives boundary matching `{e_0,e_1,e_2}`; either disappeared
colour can be assigned to `u`, and exactly one endpoint of each deleted
edge was swapped.  Both deleted endpoint pairs are therefore
monochromatic.  The source correctly makes no five-lock claim for the
double-deletion colouring.

After excluding order-seven descent, the remaining alternatives are
exactly those stated: each of the two vertex-disjoint layers either has two
internally vertex-disjoint literal root paths or exposes a smaller connected
side with boundary order at least eight.  This does not create the missing
contacts to a rooted clique-minor model, tighten positive separator excess,
or prove `HC_7`.

## 7. Dependency revisions checked

The following named inputs were read at their current hash-pinned GREEN
revisions:

| dependency | checked SHA-256 |
|---|---|
| degree-seven anti-neighbourhood connectivity | `a73429c60377546d55f9578a7795eb45634a98fdc87d84604ee62865880a90f3` |
| exact matching languages and disjoint Kempe bridges | `7fda58a909aabf5a49c32be513ebc598695c448855a4a8bede3ae1efdc63314a` |
| degree-seven off-pole edge responses | `61ed79428d43a82043ea024e5c804f12d59f74c1082be726865d588338039d37` |
| bounded-interface pole-move normal form | `01fa19f3a58a232a92a7479877b786d55341990cd3dd81af92a384231d99794f` |
| generic exact-seven selected-response restart | `e689c96686a936c27e58c2cba22d699c62ad649092eebfcdfc9c5db95a8e7b5a` |
| atomic bichromatic-bridge localization | `88070e23ca1b0d8d51e8ba34c177a29c6779bd218c77aea71e649cc0128984de` |

The atomic localization theorem is contextual rather than logically needed
for the elementary articulation argument.  Menger's theorem is used only
in its standard vertex form.

## 8. Novelty and unresolved dependencies

The exact revision proves a genuine specialization: the degree-seven pole
transition is automatic; a root-separating articulation exposes a strictly
smaller literal connected side; a separating edge retains the prescribed
matching `{e_0,e_i}`; and two such edges retain the triple matching under
double deletion.

It does **not** prove that a boundary of order at least eight can be reduced
to order seven, that the two internally vertex-disjoint routes meet the
named rooted branch sets needed for a clique-minor construction, or that an
arbitrary articulation response preserves the original operation labels.
Those are genuine unresolved dependencies.  No omitted case, invalid
Kempe swap, false rank decrease, dependency mismatch, or terminal overclaim
was found.
