# Independent audit: shortest-transition pole barrier

**Verdict:** **GREEN** for the exact source revision

```text
afc736d98452dc260354a35b3a3db5cdcb90b2332a4516fc7ddf5a8d6f7d15f0  barriers/hc7_opposite_shore_shortest_transition_pole_barrier.md
```

This is a separate internal mathematical cold audit, not external peer
review.  Any change to the construction, realized languages, transition
claim, or exact scope requires renewed audit.

## 1. Boundary languages and realization

For `H=K_3 dotunion K_3 dotunion K_2`, one has
`chi(H)=alpha(H)=3`, and `H` is nonsplit.  The six-block language and the
union of the five- and six-block languages are palette-invariant exact
relations.  Each contains a six-block partition equating the ends of every
boundary nonedge, so the realization theorem permits boundary induced
graph exactly `H`.

Adding a disjoint internal `K_6` preserves the first relation.  The
connected-full augmentation attaches it without changing the relation.
False-twin classes of possibly different orders preserve both relations;
orders at least seven give seven-connectivity, while larger classes on the
second side make its component no smaller than `C`.  One representative
from each amplified clique class retains a literal `K_6`.

## 2. Host properties and responses

Adding `u` complete exactly to the eight boundary vertices filters the
second open-side relation from five-or-six blocks to exactly five blocks;
the first closed shore accepts exactly six.  Hence the host is not
six-colourable.  The explicit colouring of every `G-E_I`, followed by a
fresh colour on `u` when restoring one pole edge, proves seven-colourability.
The retained internal `K_6` verifies both
`chi(G-uz)=6` and `chi(G-{u,z})=6`.

The case constructions for independent sets of orders one, two and three
correctly give an exact five-block partition with another nonsingleton
independent block, and splitting one vertex gives an adjacent exact
six-block partition.  They also prove every pole-star deletion response.
The two amplified open interiors are exactly the components of `G-N[u]`;
both have `z` in their neighbourhoods, and the chosen size inequality excludes a strict smaller
component.  Deleting the unused interior and contracting `C` gives
`overline K_2 join H`, with the displayed width-four decomposition.

## 3. Every shortest transition

The explicit adjacent exact-`I` five- and six-block states make the minimum
shore-language distance one.  In a disjoint union of cliques, a nontrivial
two-colour boundary component is either a singleton or one edge inside a
clique.  Switching an edge retains both colours, so any six-to-five-block
move operates a singleton whose old colour disappears and which joins an
existing colour block.  The final trace has one missing colour, forced on
the universal vertex `u`; therefore every shortest transition has the
canonical last pole move.

The proof does not infer a Kempe lift merely because the second realizer
accepts both adjacent states.  It claims only the boundary transition and
canonical pole classification.

## 4. Trust boundary

The construction is not asserted to be `K_7`-minor-free or fully
contraction-critical.  Its target-free contracted quotient does not imply
minor exclusion in the uncontracted realizers.  The note therefore refutes
only a proof from the listed local, pole-star, and shortest-transition data;
it is neither a counterexample to the full opposite-shore lemma nor to
`HC_7`.
