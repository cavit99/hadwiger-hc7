# Internal audit: opposite responses at an independent odd-cycle transversal

**Verdict:** **GREEN** for Theorems 3.1 and 4.1 and their displayed
corollaries, within the trust boundary in the source.  This is a separate
internal mathematical audit, not external peer review.  It does not prove
`HC_7`.

## Audited revision

This audit checks the complete promoted source file
[`results/hc7_order8_independent_oct_opposite_response.md`](hc7_order8_independent_oct_opposite_response.md)
at SHA-256

```text
fb6b2da07cfc90833f32bb887104816d0ecdcd3a16979f044cbfb0adc640025b
```

The file was promoted from `active/` to `results/` with only status and
navigation metadata changed.  The hypotheses, theorem statements, proofs,
corollaries, dependencies, and trust boundary are mathematically unchanged
from the previously GREEN-audited revision.  The complete promoted file was
also rechecked line by line against the argument recorded below.

## 1. The contraction constructions

The sets `A_d union X` and `A_e union Y` are disjoint, connected, and
nontrivial.  Exact one-defect boundary contact makes their images adjacent
and makes each of `d,e` adjacent to both images.  Their simultaneous
contraction therefore produces a `K_4` minus the absent edge `de` in a
proper minor.  Pulling a six-colouring back to the opposite closed shore
makes `X,Y` distinct monochromatic blocks and makes `d,e` avoid both block
colours.

The same verification applies to `Q_1 union X` and `Q_2 union Y` because
the two connected subgraphs are disjoint and adjacent to every boundary
vertex.  Thus both response sets are nonempty subsets of the two-element
set consisting of the equality and inequality types.

## 2. Gluing and the Kempe argument

For a common response type, the two boundary restrictions have exactly the
same three-block or four-block equality partition.  A bijection between
the used block colours extends to a permutation of the six-colour palette,
so the two closed-shore colourings glue.

If the response sets are disjoint, nonemptiness forces them to be opposite
singletons.  On the shore with the inequality response, let `alpha,beta`
be the root colours.  Each root sees each of the monochromatic blocks
`X,Y`, so neither block colour is `alpha` or `beta`.  If the roots belonged
to different `alpha,beta` components, a Kempe interchange on one component
would preserve the defining boundary conditions and create an equality
response.  Hence a two-colour root-to-root path exists, and no internal
vertex of that path lies in the boundary.

## 3. Localization at the two full connected subgraphs

Suppose a root-to-root path avoids `Q_1 union Q_2` internally.  Since `de`
is absent, contract at least one edge of the path while retaining distinct
endpoint images, until its image is the edge `de`.  Simultaneously contract
`Q_1 union X` and `Q_2 union Y`.  The three contracted vertex sets are
disjoint.  The resulting four images form a `K_4` in a proper minor.

A six-colouring of that minor pulls back to the opposite closed shore with
`X,Y` as two distinct monochromatic blocks and with `d,e` assigned distinct
colours avoiding both block colours.  This is the forbidden inequality
response on a shore whose response set is the equality singleton.  Thus
every such path must meet one of the two named full connected subgraphs.

## 4. Trust boundary

The audit does not claim that the unavoidable path splits either full
connected subgraph, produces an explicit `K_7`-minor model, or exposes an
order-seven separation.  It checks no finite classification of the
eight-vertex boundary.  Theorems 3.1 and 4.1 are unbounded two-shore
colouring statements under their explicit hypotheses.
