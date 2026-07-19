# Independent audit of the bipartite-boundary bridge response descent

**Verdict:** GREEN for Theorems 2.1 and 3.1 in
[`hc7_exact7_bipartite_bridge_response_descent.md`](hc7_exact7_bipartite_bridge_response_descent.md)
at source SHA-256

```text
638adad4e58de96f59918d8ebf13d224f1cff9b61889ef7f9a0ee6a44f7f94e1
```

This is a separate internal mathematical audit, not external peer review.

## 1. Exact setting

The source assumes an actual order-seven separation, seven-connectivity,
seven-chromatic proper-minor criticality, `K_7`-minor exclusion, a connected
boundary-full shore `L`, two disjoint boundary-full connected subgraphs in
the opposite shore, a bipartite boundary graph, and a literal bridge `uv`
of `G[L]`.  Every dependency used below has precisely these hypotheses or
weaker ones.

## 2. Bridge-side neighbourhoods

For the components `C_1,C_2` of `G[L]-uv`, oriented with `u\in C_1` and
`v\in C_2`, the bridge and separation hypotheses give

\[
 N_G(C_1)=N_Y(C_1)\mathbin{\dot\cup}\{v\},
 \qquad
 N_G(C_2)=N_Y(C_2)\mathbin{\dot\cup}\{u\}.
\]

Each set separates its nonempty bridge side from the nonempty opposite
shore.  Seven-connectivity therefore gives `|N_Y(C_i)|\ge6`.  This is a
literal host-neighbourhood calculation; no quotient contact is substituted
for a host edge.

## 3. Exact two-list invocation

Every carrier list is nonempty because `L` is boundary-full.  The subgraphs
`C_1,C_2` are connected, disjoint and adjacent through `uv`; the opposite
shore supplies the two required disjoint full connected subgraphs.  Thus
Theorem 2.1 of the audited nonspanning two-connected-subgraph theorem
applies.  A proper list-colouring would six-colour `G`, so the list instance
is uncolourable.

The boundary is bipartite.  Each forced-label set has order at most one by
the neighbourhood bounds.  The exact parity theorem therefore forces
exactly one vertex of each singleton list.  Calling them `x,y` gives

\[
 N_Y(C_1)=Y-\{y\},
 \qquad
 N_Y(C_2)=Y-\{x\}.
\]

They are distinct, lie in one boundary component, and their different
singleton lists force even distance.  The proof does not identify palette
colours with minor-model labels.

## 4. Literal order-seven boundaries

The sets

\[
 \Omega_1=(Y-\{y\})\cup\{v\},
 \qquad
 \Omega_2=(Y-\{x\})\cup\{u\}
\]

are exactly `N_G(C_1),N_G(C_2)`, not merely supersets.  They have order
seven and separate nonempty open sides.  If a component of either new
separation missed a boundary vertex, at most six vertices would separate it
from the opposite open side.  Thus every new off-boundary component is full.

## 5. New packing vectors

Every `\Omega_1`-full connected subgraph in `C_1` contains `u`, because
`uv` is the unique edge from `C_1` to the literal boundary vertex `v`.
Hence the near packing number is exactly one; the argument for `C_2` is
symmetric.  Exact-seven packing and adaptive `(1,3)` exclusion make the
opposite packing number one or two.  The proof correctly recomputes these
numbers: the old opposite-shore full subgraphs need not meet the new bridge
endpoint and are not silently reused.

## 6. Operation-specific response

Every six-colouring of `G-uv` makes `u,v` equal, since otherwise restoring
the edge colours `G`.  On either new separation the colouring is proper on
the opposite closed shore.  If its exact boundary partition extended to
the intact near side, palette permutation and gluing would six-colour `G`.
Exact packet reflection therefore makes its demand strictly larger than the
opposite full-subgraph packing number; otherwise reflection would give the
forbidden near-side extension or a `K_7` minor.

## 7. Strictness and trust boundary

Both `C_1,C_2` are nonempty proper subsets of `L`, so the connected-side
order strictly decreases.  This gives a well-founded move in the broad
class of operation-specific exact-seven interfaces.  It does not preserve
the old complete boundary partition, bipartiteness, special five-plus-two
labels, old full-subgraph identities, or inherited minor-model labels.
The theorem therefore supplies a response-carrying descent, not a terminal
six-colouring or `K_7`-minor model, and does not prove `HC_7`.
