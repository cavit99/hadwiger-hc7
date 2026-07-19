# Independent audit: ordered paths, rooted model, or series separation

**Verdict:** **GREEN** for Lemma 2.1, Theorem 3.1, Corollary 3.2,
Proposition 4.1, and the corrected trust boundary.  This is a separate
internal mathematical audit, not external peer review.  The result is
conditional and does not prove `HC_7`.

## Audited revision

This audit checks the complete source file
[`hc7_order8_ordered_paths_rooted_model_or_series_separation.md`](hc7_order8_ordered_paths_rooted_model_or_series_separation.md)
at SHA-256

```text
e674bc4f51601e133dd8f84f14a5cd49b242ea69a00bef66b8eff1d4f0aed0a3
```

The corrected mathematical revision was first audited at SHA-256
`b2906fefa4f017dca5d58d3bb16077a4123560f64300aab021440865db58c3aa`.
The final source hash above changes only the status paragraph to link this
audit; all hypotheses, constructions, proofs, conclusions, dependencies,
and trust-boundary text are identical.

The initial revision at SHA-256
`4bef0fce1ae95695d08b46073861ff7100618f30113d9446b0800277bb3a77c9`
was mathematically correct in its three main constructions but received an
AMBER trust-boundary verdict.  Its final paragraph treated a split of the
two cutvertex lobes as the only missing series-branch obligation.  In fact,
the omitted root is a one-vertex bottleneck which prevents the two original
`P_0,P_1` labels from descending disjointly; the new root `z` also need not
inherit the boundary-class contacts or the second rooted triangle.  The
audited revision states these losses explicitly.  It also makes the
path-pair quantifiers in Corollary 3.2 explicit, qualifies the ambient side
of the rooted model, orders the cutvertex-colour argument before its use,
and repairs one dependency link.  None of these repairs strengthens the
theorem.

## 1. Conditional rooted `K_5` and explicit `K_7` model

The two internally vertex-disjoint `d`--`e` paths meet only at their roots.
Because `A_d,A_e` lie in `L` and are disjoint, every trimmed passage
`W_i=a_iQ_ib_i` has an edge and all four endpoints belonging to different
paths or different deficient subgraphs are distinct as required.

For the five branch sets in (2.3), connectivity and disjointness are exact:

* `B_d` is the union of two prefixes meeting at `d`;
* `B_e` is the union of two suffixes meeting at `e`;
* `B_m` is the connected path `W_1` together with `x_e`, joined by
  `a_1x_e`; and
* deleting `a_1,b_1` from the two outer `Q_1` pieces and splitting `Q_2`
  across the edge `uv` leaves the three sets pairwise disjoint.

Every adjacency is supplied literally:

| Pair | Supplying edge or contact |
|---|---|
| `B_d,B_e` | `uv` |
| `B_d,B_m` | the edge of `Q_1` preceding `a_1` |
| `B_m,B_e` | the edge of `Q_1` following `b_1` |
| `B_d` to `x_d,y_d` | the two contacts at `a_2` |
| `B_e` to `x_d,y_d` | the two contacts at `b_2` |
| `B_m` to `x_d,y_d` | the two contacts at `a_1` |
| `x_d,y_d` | the first boundary triangle |

The five distinct roots are `d,e,x_e,x_d,y_d`.  Since all five branch sets
lie in `L union S`, they are disjoint from `P_0,P_1`.  Each `P_j` reaches
every rooted branch set through its literal boundary root, and the
stipulated `P_0`--`P_1` edge supplies the last adjacency.  Thus the seven
sets form an explicit `K_7`-minor model.  The pointwise condition (2.1) is
essential to this construction; aggregate contact (1.2) is not silently
promoted to endpoint contact.

## 2. Menger reduction and exact neighbourhood count

The three given Kempe paths ensure that `d,e` are connected in `H`, while
the extra hypothesis of Theorem 3.1 excludes two internally disjoint such
paths.  Since `de` is absent, the vertex form of Menger's theorem gives a
one-vertex internal separator `z in L`.

For every component `C` of `G[L]-z`, component maximality and the absence of
`L`--`R` edges give

```text
N_G(C) subseteq {z} union S.
```

No component can contact both `d,e`, or it would join the roots in `H-z`.
The candidate set has nine vertices and at least one root is absent, so
`|N_G(C)|<=8`.  Moreover `N_G(C)` is an actual separator: `C` remains on
one side and the nonempty set `R` remains on another.  If its order were at
most seven, outcome 2 would hold.  Excluding that outcome forces order
eight, hence exactly one of

```text
{z} union (S-{e}),    {z} union (S-{d}).
```

No hidden boundary contact is used in this count.

## 3. Repeated-component minor models

If two components have the first exact neighbourhood, the seven sets in
(3.5) are disjoint and connected.  The two enlarged components are adjacent
through `x_ey_e`; each reaches `d,x_d,y_d` through its exact neighbourhood;
and those last three vertices form the first triangle.  Each `P_j` reaches
all five other sets through their boundary roots, and `P_0,P_1` are
adjacent.  This checks every pair of branch sets.

For two components with the second exact neighbourhood, the symmetric model
enlarges them by `x_d,y_d`, uses `x_dy_d` between them, and uses the triangle
`e x_e y_e` as the last three sets.  Its adjacency table is identical after
interchanging the two rooted triangles.  Hence at most one component of
each exact type can survive without outcome 1.

## 4. The `alpha` cutvertex and six literal neighbours

Every `K_i` contains the Menger separator `z`.  As a common vertex of paths
with distinct private colours, `z` has colour `alpha`.  Properness then
excludes `zd,ze`, so both sides of every path contain a vertex of `L-z`.
The initial side lies in a component contacting `d` and the final side in a
component contacting `e`; these are the two different exact neighbourhood
types.  Since there is at most one component of each type, `G[L]-z` has
exactly the two components `C_d,C_e` and every path has order

```text
d, C_d, z, C_e, e.
```

On `K_i`, both neighbours of `z` have colour `beta_i`.  Neighbours from
different paths cannot coincide, because such a common vertex would have
to have colour `alpha`; the two neighbours on one path lie in the disjoint
components `C_d,C_e`.  Thus all six neighbours are literal and pairwise
distinct.

Corollary 3.2 is exhaustive with the corrected quantifier: if local
connectivity is at least two, either some path pair, trimming, and index
order satisfies (2.1), or every such choice fails it.  If local connectivity
is one, Theorem 3.1 applies.

## 5. Inherited opposite colourings

Write the three colours of `c_=` on `X,Y,{d,e,z}` as `a,b,r`, and the four
colours of `c_ne` on `X,Y,{d},{e}` as `A,B,D,E`.  Each displayed tuple has
distinct entries.  The partial map

```text
(a,b,r) -> (A,B,E)
```

extends to a permutation of the six-colour palette.  Use it on
`C_e union {z}` and use `c_ne` on `R union S`.  The exact two-component
structure means these domains cover `G-C_d`.  All cross-edges are safe:

* `C_e` has no neighbour at `d`, while its contacts to `X,Y,e` have aligned
  colours;
* `z` has no edge to `e`, receives colour `E`, and all its possible contacts
  to `X,Y` retain their aligned colours; its possible contact to `d` is safe
  because `D!=E`; and
* neither `C_e` nor `z` has an edge to `R`.

The boundary `S_d` therefore has exact colours `X:A,Y:B,d:D,z:E`.  The
restriction of `c_=` gives `X|Y|{d,z}` on the other closed side.  The map
`(a,b,r)->(A,B,D)` gives the symmetric splice on `G-C_e`, with exact boundary
colours `X:A,Y:B,e:E,z:D`.  Proposition 4.1 is GREEN.

## 6. Trust boundary

The source now distinguishes the two kinds of conclusion correctly.  The
pointwise locally two-connected branch is conditional and leaves aggregate
contact allocation open.  The one-vertex branch gives a strict decrease in
the order of the lobe carrying the merged colouring, but only at the level
of boundary responses.

It is not a recursive labelled instance.  For `S_d`, the complementary open
shore is `C_e dotcup {e} dotcup R`.  A connected subgraph there which meets
`R` and is adjacent to `z` must meet `C_e`; every `C_e`--`R` path inside that
open shore contains `e`.  Hence any such extension contains `e`, and two
disjoint extensions of `P_0,P_1` are impossible.  The symmetric bottleneck
is `d` for `S_e`.  In addition, no hypothesis gives `z` a contact to either
boundary bipartition class or a second rooted triangle, and the original
`A_d,A_e` labels need not survive in one lobe.  A split at the six
colour-indexed neighbours alone therefore does not restore the full
structural interface.

No `K_7` model, compatible order-seven separation, or label-preserving
recursive instance is claimed beyond the explicit outcomes above.  No
unresolved mathematical gap remains inside this corrected trust boundary.

## 7. Checked dependencies

The audit also checked the exact promoted inputs currently cited by the
source:

* ordered crossing, SHA-256
  `434efeab93a4f693d212b4ee434532e81647df775a69494384ffcb3349735dde`;
* three merged-root Kempe locks, SHA-256
  `2705b68b8452fd8642601ed48f93c84db98e313be46c12c3f4f7ba85cd94cd41`;
* opposite responses, SHA-256
  `fb6b2da07cfc90833f32bb887104816d0ecdcd3a16979f044cbfb0adc640025b`.

Their stated conclusions are used within their audited trust boundaries.
