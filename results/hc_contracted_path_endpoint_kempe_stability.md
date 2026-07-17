# Kempe stability at a saturated path vertex

**Status:** written proof; adjacent internal audit.  This is a general
two-colour statement.  It does not assert that the same bichromatic
component works for two different path vertices.

## Theorem 1.1 (exact endpoint criterion)

Let `H` be a graph with a proper colouring `psi`, let `x` be a vertex
outside `H`, and let `a,b` be two colours.  Suppose that `x` has a
neighbour of each of colours `a` and `b` in `H`.  Call a component `C` of

\[
                         H[\psi^{-1}(\{a,b\})]
\]

**mixed at `x`** if `C` contains both an `a`-coloured neighbour and a
`b`-coloured neighbour of `x`.

The following are equivalent.

1. After every sequence of Kempe interchanges on components of the
   `a,b`-coloured subgraph, `x` still has a neighbour of each of colours
   `a` and `b`.
2. Some `a,b`-component is mixed at `x`.

If item 2 fails, a sequence of pairwise commuting Kempe interchanges can
be chosen so that colour `a` is absent from `N_H(x)`.

### Proof

If a component `C` is mixed at `x`, then before an interchange on `C`,
`x` has neighbours of both colours in `C`; after the interchange, the
same two neighbours have exchanged colours.  Interchanges on other
components do not affect them.  Thus item 2 implies item 1.

Conversely, suppose that no component is mixed at `x`.  Interchange
`a` and `b` on every component which contains an `a`-coloured neighbour
of `x`, and on no other component.  These interchanges commute because
their supports are distinct components.  Every former `a`-coloured
neighbour of `x` becomes `b`-coloured.  A component in this switched
family contains no `b`-coloured neighbour of `x`, by the assumption that
it is not mixed.  Every unswitched component contains no `a`-coloured
neighbour of `x`, by its selection.  Hence no neighbour of `x` has colour
`a` afterward.  Item 1 fails, and the final assertion is proved.
\(\square\)

## Corollary 1.2 (two vertices)

Let `x,y` both have neighbours of colours `a,b`.  Both vertices retain
both colours in their neighbourhoods under every sequence of `a,b` Kempe
interchanges if and only if there is a component mixed at `x` and there
is a component mixed at `y`.

The two components in this conclusion need not be the same.

### Proof

Apply Theorem 1.1 separately to `x` and `y`.  A sequence preserves both
vertices under every choice precisely when each of the two individual
universal statements holds.  Nothing in either statement identifies the
two witnessing components. \(\square\)

## Scope

For an endpoint of the locked subpath in the contracted-path list theorem,
being mixed for every pair of noncontracted colours is exactly the local
condition that makes saturation invariant under all pairwise Kempe
interchanges.  It is only a local condition.  It neither joins the two
locked endpoints through one component nor aligns colour components with
prescribed branch sets of a clique-minor model.
