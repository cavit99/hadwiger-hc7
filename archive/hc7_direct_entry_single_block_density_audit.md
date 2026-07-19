# Independent audit of the tight single-block density closure

**Verdict:** GREEN for Theorem 1 at the exact source revision identified
below.

**Audited source:** `hc7_direct_entry_single_block_density.md`, SHA-256

```text
900300e5b99931c1cd872749a5354969309af7d2bcb51278e446be52363b766c
```

This is a separate internal mathematical audit, not external peer review.
It checks the one-block classification, the `K_1` and `K_2` exclusions, the
singleton-side separation, fullness of the contracted opposite-shore
component, the minor construction and edge count, and the exact use of
Mader's `K_7`-minor extremal inequality.

## 1. Classification and the small complete blocks

The hypotheses give a connected graph `G[R]` with a fixed uncolourable list
assignment satisfying

\[
                         |A(v)|=d_{G[R]}(v)
\]

at every vertex.  The degree-choosability theorem therefore makes `G[R]` a
Gallai tree.  Since it consists of one block, it is a complete graph or an
odd cycle.

If `G[R]=K_1`, tightness gives an empty list at its sole vertex.  By the
definition of `A`, its neighbours in `S` then use all six colours, contrary
to the four-colour boundary hypothesis.  If `G[R]=K_2`, either vertex has
internal degree one and hence a singleton list; its boundary neighbours use
five distinct colours, giving the same contradiction.  Thus a complete
single block has order at least three.  It has order at most six because a
`K_7` subgraph would itself be a `K_7` minor.  This proves the complete-block
outcome exactly as stated.

## 2. Degrees on an odd-cycle shore

Let `G[R]` be an odd cycle of order `n`.  Every vertex has internal degree
two, so tightness gives `|A(v)|=2`.  Since the palette has six colours, the
boundary neighbours of every cycle vertex use exactly four distinct
colours.

No vertex of `R` has a neighbour in `L`.  Seven-connectivity therefore gives

\[
 7\le d_G(v)=2+|N_G(v)\cap S|,
\]

and each cycle vertex has at least five neighbours in `S`.  If one has
exactly five, its whole-graph degree is seven.  Its full neighbourhood
separates the singleton `{v}` from the nonempty set `L`; hence this is an
actual order-seven separation, not merely a degree observation.

If no vertex has exactly five boundary neighbours, integrality gives at
least six boundary neighbours at every cycle vertex.  This is the only case
passed to the density argument.

## 3. The opposite-shore contraction

Choose a component `D` of the nonempty graph `G[L]`.  By component
maximality it has no neighbour in another component of `G[L]`, and
`E_G(L,R)=emptyset`; therefore `N_G(D) subseteq S`.  The set `N_G(D)`
separates `D` from the nonempty shore `R`.  Seven-connectivity gives
`|N_G(D)|>=7`, while `|S|=7`, so

\[
                              N_G(D)=S.
\]

Contracting the connected set `D` to a vertex `ell`, deleting all other
vertices of `L`, and suppressing loops or parallel edges produces a simple
minor `H` of `G`.  It has exactly `n+8` vertices: the `n` cycle vertices,
the seven vertices of `S`, and `ell`.  Because `H` is a minor of the
`K_7`-minor-free graph `G`, it too has no `K_7` minor.

The following counted edge sets are pairwise disjoint and survive in the
simple minor:

- the `n` cycle edges inside `R`;
- seven distinct edges from `ell` to the seven vertices of `S`; and
- at least `6n` distinct edges between `R` and `S`.

Thus `|E(H)|>=7n+7`.  No uncounted edge inside `S` is needed.

## 4. Mader's bound and the arithmetic

Mader's sharp small-clique-minor inequality says that a simple
`K_7`-minor-free graph on `N>=7` vertices has at most `5N-15` edges.  Here
`N=n+8>=11`, so there is no small-order exception.  Applying the inequality
to `H` gives

\[
 7n+7\le |E(H)|\le 5(n+8)-15=5n+25.
\]

Consequently `2n<=18` and `n<=9`.  Since the cycle is odd, the remaining
orders are `3,5,7,9`; the triangle also belongs to the already listed
complete-block outcome.

## 5. Trust boundary

The result is an unbounded density closure only for the **single-block**
outcome of the tight Gallai-shore theorem.  It proves that this outcome is
either a complete graph of order three through six, an odd cycle of order
at most nine, or has an order-seven singleton-side separation.

It does not eliminate any of those bounded shores, provide compatible
proper colourings on the returned order-seven separation, address a path of
Gallai blocks, preserve an older five-label branch-set system, or construct
a `K_7`-minor model.  It therefore does not prove `HC_7`.
