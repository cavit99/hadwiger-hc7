# Independent audit of the order-nine tight Gallai-block separator theorem

## Verdict and audited revision

**Verdict: GREEN.**

This audit checks the complete source file
[`hc7_order9_tight_gallai_block_separator.md`](hc7_order9_tight_gallai_block_separator.md)
at SHA-256

```text
8d5e5564b397365729c4ee693e01687ced8199bbbade6fe03aa779487eeae204
```

The degree identity, repeated-colour saturation, block-list reduction,
literal full-neighbourhood formula, separator calculation, and
proper-minor colouring response are all correct under the stated
hypotheses.  The result applies to every nontrivial block of the tight
Gallai forest, not only to leaf blocks.  The two-connected full-shore
corollary correctly rules out an all-tight spanning shore.

The audited revision contains two scope clarifications made before this
verdict.  It assigns `K_3`, which is both a clique and an odd cycle, to the
clique alternative.  It also states the attachment inequality (3.7) under
the explicit condition `|N_G(H)|>=9`; Corollary 3.2 is where
minor-criticality turns the separator into a response and licenses that
condition after order-seven and order-eight responses have been excluded.
The source hash above also includes the final status line linking this
audit; that status-only change does not alter the audited mathematics.

## 1. Degree accounting and literal saturation

For a shore vertex `v`, let `q(v)` be the number of colours appearing on
its boundary neighbours.  The definitions give

```text
|L(v)| = 6-q(v),
d_G[Z](v) = 6-q(v)+epsilon(v),
|N_G(v) cap B| = q(v)+rho(v).
```

There are no edges from `Z` to the opposite shore.  Adding the internal and
boundary degrees therefore gives exactly

```text
d_G(v)=6+epsilon(v)+rho(v).
```

Vertex-minimal non-list-colourability implies
`d_{G[Z]}(v)>=|L(v)|`: otherwise an `L`-colouring of `G[Z]-v` would leave an
available colour for `v`.  Hence `epsilon(v)>=0`.

Write the six nonempty boundary colour classes as `C_1,...,C_6`, and put
`n_i=|N_G(v) cap C_i|`.  Then

```text
rho(v) = sum_i (n_i-1 if n_i>0, else 0)
       = sum_i max(0,n_i-1).
```

Since `|B|=9` and all six colours occur,

```text
sum_i (|C_i|-1)=3,
```

so `rho(v)<=3`.  If `v` is tight, the assumed lower bound
`d_G(v)>=9` and the degree identity force `rho(v)>=3`.  Thus
`rho(v)=3` and every term attains its individual upper bound.  For a
nonsingleton class `C_i`, equality

```text
max(0,n_i-1)=|C_i|-1
```

forces `n_i=|C_i|`.  This proves the genuinely literal conclusion that
`v` is adjacent to every vertex in every nonsingleton colour class, not
merely to one vertex of each repeated colour.

Consequently a colour is absent from the boundary neighbourhood of a tight
vertex exactly when its class is a singleton and that unique boundary
vertex is missed.  Tightness then gives equation (2.2).  No branch-set
label is inferred from a palette colour.

## 2. Colouring the complement of a tight block

Let `H` be a nontrivial block of the tight-vertex induced subgraph.  Since
`V(H)` is nonempty, `G[Z]-V(H)` is a proper induced subgraph unless it is
empty; vertex-minimality supplies an `L`-colouring in either case (the empty
case is vacuous).

A block contains every edge of the ambient graph between its own vertices.
Because the tight-vertex graph is induced in `G[Z]`, the number of
neighbours of `v in H` outside `H` is

```text
d_G[Z](v)-d_H(v).
```

Deleting from `L(v)` the colours used by those outside neighbours removes
at most this many colours.  Tightness therefore gives

```text
|M_H(v)|
  >= |L(v)|-(d_G[Z](v)-d_H(v))
   = d_H(v).
```

If `H` admitted an `M_H`-colouring, it would combine with the fixed
colouring of its complement: by definition every colour used on an outside
neighbour was removed from the corresponding residual list.  This would
colour all of `G[Z]` from `L`, a contradiction.  Thus `H` is not
`M_H`-colourable.

The standard degree-choosability argument already makes each block of the
tight graph a clique or an odd cycle.  The stronger list descriptions used
here are also exact:

- If `H=K_r`, list-colouring is an SDR problem.  A set of at most `r-1`
  vertices automatically satisfies Hall because each individual list has
  at least `r-1` elements.  Failure can occur only on all `r` vertices;
  then their union has at most `r-1` elements while every list has at least
  `r-1`, so all lists equal one common `(r-1)`-set.
- A cycle with lists of order at least two is list-colourable unless it is
  odd and every list is the same two-element set.  Applied to the odd-cycle
  block, this gives the second alternative.  The source assigns the
  overlapping case `K_3` to the clique alternative, so the alternatives
  are unambiguous.

Every residual list is contained in the original list of its vertex.
Section 1 showed that an original list at a tight vertex contains only
colours carried by singleton boundary classes.  Hence every colour in the
common set `P` corresponds to one literal boundary vertex missed by every
vertex of `H`, proving `P_B subseteq Lambda_H`.

## 3. The full-neighbourhood separator

There are no edges from `H subseteq Z` to the opposite shore.  Every
neighbour of `H` is therefore either an internal shore vertex outside
`H`, belonging to `A_H`, or a boundary vertex met by `H`, belonging to
`B-Lambda_H`.  These two sets are disjoint and exhaust the open
neighbourhood, so

```text
N_G(H)=A_H disjoint-union (B-Lambda_H),
|N_G(H)|=|A_H|+9-|Lambda_H|.
```

Removing this open neighbourhood leaves the connected nonempty graph `H`
as one component.  The nonempty opposite shore contains no neighbour of
`H`, is disjoint from the removed set, and remains on another side.
Therefore `N_G(H)` is an actual vertex separator.  Seven-connectivity gives
`|N_G(H)|>=7`, which is equivalent to

```text
|A_H|>=|Lambda_H|-2.
```

Equality is equivalent to separator order seven.  Independently, the
explicit condition `|N_G(H)|>=9` is equivalent to
`|A_H|>=|Lambda_H|`; no response or colouring hypothesis is silently used
in Theorem 3.1 for this last implication.

## 4. Proper-minor response and gluing

Under Corollary 3.2, choose any edge `xy` leaving `H`.  Edge deletion is a
proper minor operation, so `G-xy` has a proper six-colouring `c`.  Its
restriction to `G-H` is proper because the deleted edge has its `x`
endpoint in `H`.  Its restriction to `G[H union N_G(H)]-xy` is also
proper.  These restrictions induce the same labelled colouring, and hence
the same equality partition, on `N_G(H)`.

If that equality partition extended through the intact inside, permute its
colour names to agree vertex-by-vertex with `c` on the boundary.  Such a
permutation exists because two colourings induce the same equality
partition; a bijection between the used boundary colours extends to a
permutation of the six-colour palette.  The intact inside then glues to
`c|G-H`.  No edge bypasses `N_G(H)`, so the result would be a proper
six-colouring of `G`, a contradiction.  Thus the intact side rejects the
partition.

The order calculation is exact:

- `|A_H|=|Lambda_H|-2` gives an order-seven response;
- `|A_H|=|Lambda_H|-1` gives an order-eight response;
- smaller attachment sets contradict seven-connectivity.

Accordingly, after order-seven and order-eight responses are terminal or
excluded, the only remaining block case has
`|A_H|>=|Lambda_H|`.  This is a one-step full-neighbourhood response; the
theorem does not claim that its boundary trace preserves the original
exact block or any minor-model labels.

## 5. A two-connected full shore is not all tight

Assume `G[Z]` is two-connected and every boundary vertex has a neighbour
in `Z`.  If all vertices of `Z` were tight, then the tight graph `T` would
equal `G[Z]`.  A two-connected graph is one nontrivial block, while the
Gallai-forest theorem says this block is a clique or an odd cycle.

Apply Theorem 3.1 to `H=G[Z]`.  The complement is empty, so the empty
colouring is the required complement colouring and `M_H(v)=L(v)`.  The
common set `P` is nonempty: it has order `r-1>=2` in the clique case (a
two-connected clique has `r>=3`) and order two in the odd-cycle case.
Every vertex of `Z` consequently misses every literal singleton boundary
vertex in the nonempty set `P_B`.  This contradicts boundary fullness.
Thus some vertex has `epsilon(v)>0`; since every excess is nonnegative,
their sum is positive, exactly as asserted in Corollary 3.3.

## 6. Trust boundary

The audited implication is exactly:

```text
order-nine boundary using all six colours
+ two nonempty anticomplete shores
+ a spanning vertex-minimal list obstruction for the fixed trace
+ shore degree at least nine
=> every tight vertex sees every literal repeated-colour boundary vertex;
   every nontrivial tight block has a common missed singleton set;
   its literal full neighbourhood has order
       |A_H|+9-|Lambda_H|;
   minor-criticality turns any crossing-edge deletion into a response;
   and a two-connected boundary-full shore has positive total excess.
```

This does not force a `K_7`-minor model, identify palette colours with named
minor-model branch sets, bound the attachment excess by zero, or prove
that the returned trace re-enters the paired-kernel setting.  It supplies
the exact residual inequality `|A_H|>=|Lambda_H|` after smaller response
boundaries have been removed.  The remaining allocation of those literal
attachments to named branch sets is outside the audited theorem.
