# Independent audit of boundary-anchor completion

## Verdict and audited revision

**GREEN.**  This audit checks the promoted source
[`results/hc7_boundary_anchored_model_completion.md`](hc7_boundary_anchored_model_completion.md)
at exact SHA-256

```text
cb88b01817071fde612db88aeca094c273242be615ca00f3b22ef3ddacb66e2f
```

The pre-promotion mathematical revision, now retained at the promoted source
linked above, had SHA-256

```text
5a7ead9ecec2ef99f6e464ac6ccccd72bcbc6edab166cf8c87e543f9ceb0e811
```

The promotion changed only the opening status paragraph.  Replacing the
promoted status paragraph by the exact pre-promotion paragraph reproduces
the pre-promotion hash above; all text from `## 1. Boundary-anchor
completion` onward is byte-for-byte unchanged.  The GREEN mathematical
audit therefore transfers exactly to the promoted path and final hash.

Theorem 1.1 and Corollary 2.1 are correct under their stated hypotheses.
There are no unresolved assumptions or proof gaps internal to those two
statements.  The audit does not independently re-audit the companion
Gallai--Edmonds reduction cited in Section 3, and neither result proves
`HC_7`.

## 1. Menger separator budget

Let `m` be the support order and let `h` be the number of branch sets
disjoint from the boundary.  One vertex is retained from each such branch
set, while every other model vertex and `s` is deleted.  Since the model
avoids `s`, the deleted set has exact order

```text
|Z| = m-h+1 <= 7-h.
```

Each boundary-disjoint branch set contributes at least one support vertex
outside `S`.  Thus, if `b` support vertices lie in `S`, then `b<=m-h` and

```text
|T| = 7-b >= 7-m+h >= h+1.
```

If the required `h` disjoint `A`--`T` paths did not exist, set-form Menger
would give an `A`--`T` separator `X` in `G-Z` with `|X|<=h-1`.  Because
`|A|=h` and `|T|>=h+1`, both `A-X` and `T-X` are nonempty.  Hence `Z union X`
disconnects `G`, but

```text
|Z union X| <= (7-h)+(h-1) = 6,
```

contradicting seven-connectivity.  This verifies the exact budget in
equations (1.4)--(1.6), including the possibility that a set separator uses
vertices of `A` or `T`.

## 2. Path truncation and model avoidance

The `h` disjoint paths use distinct vertices of `A`; because there are
exactly `h` paths and exactly `h` vertices in `A`, no path can contain a
second vertex of `A`.  Every other original model vertex and every boundary
vertex outside `T` belongs to `Z`.

Consequently, truncating each path at its first visit to `S` gives a path
from its assigned `a_i` to a distinct vertex `t_i` of `T`.  Before that
first boundary visit the path stays in `U`: it starts in `U`, and moving
from `U` to the other component of `G-S` requires first meeting `S`.  Its
internal vertices therefore lie in `U` and avoid the entire original model.

## 3. Branch-set integrity and the final `K_7` model

For every boundary-disjoint branch set, adjoining its truncated path
preserves connectivity and attaches exactly one new boundary endpoint.
Different enlarged branch sets remain disjoint because the paths are
pairwise disjoint and meet the old support only at their assigned vertices
`a_i`.  Every old pairwise branch-set adjacency is retained.

After the enlargement, each of the five branch sets contains a vertex of
`S-{s}`.  Boundary fullness supplies its adjacency to the connected branch
set `V`, while the boundary-universal vertex `s` supplies its adjacency to
the singleton branch set `{s}`.  Fullness also gives the `V`--`{s}`
adjacency.  Thus the seven displayed sets are pairwise disjoint, connected,
and pairwise adjacent.

## 4. Quotient contraction in Corollary 2.1

Fix an arbitrary minimum model in `G-{s,x}`.  Assumption 3 makes its support
order at most six.  If an open shore meets at most one branch set, then:

- when it meets one branch set, adjoining the whole connected shore to that
  branch set preserves connectivity and disjointness; and
- when it meets no branch set, its contraction vertex is simply unused by
  the model.

Contracting both shores therefore contracts inside at most one named branch
set per shore and never merges two branch-set labels.  It preserves all
model adjacencies and cannot increase support order.  Assumption 4 identifies
the resulting graph exactly as `I_2 vee G[B]`, so its small-model exclusion
forces one shore to meet at least two branch sets.

Assumption 2 makes both shores adjacent to every boundary vertex.  Therefore
the labels `U,V` may be interchanged before applying Theorem 1.1.  The
opposite shore cannot be avoided by the selected model, since that would
produce a `K_7` minor contrary to assumption 1.  The selected model genuinely
meets both open shores.

## 5. Support order and mixed-shore normal form

A support-five `K_5` model has five singleton branch sets.  Such a model
cannot meet both shores because there is no edge between distinct components
of `G-S`.  Hence the minimum support order is six, with one two-vertex edge
branch and four singleton branches.

Choose the shore meeting at least two branch sets and call it `U`.  One of
those branch sets is a singleton `{u}`.  Any branch set meeting `V` must be
adjacent to `{u}`; no singleton in `V` can do so.  It must therefore be the
unique edge branch, and connectivity plus the absence of `U`--`V` edges
forces its form to be `{v,t}` with `v in V` and `t in S`.  It is the only
branch set meeting `V`; all branch sets meeting `U` are singletons, and all
remaining singleton vertices lie in `B=S-{s,x}`.

If all four singleton vertices lay in `U`, then `t` would be adjacent to
all four and would form a literal `K_5` with them, contradicting minimum
support six.  Thus the number `h` of singleton branch sets in `U` is exactly
two or three.  The four singleton vertices form a clique, `t` meets every
`u_i`, and `t` must miss at least one boundary singleton `w_j`; otherwise
`t` and the four singleton vertices would again form a literal `K_5`.

## 6. Exhaustive defect-pattern check

For an endpoint `z` of the edge branch, `D_z` is its set of nonneighbours
among the four singleton vertices.  Model adjacency gives
`D_v cap D_t=empty`, while every `u_i` lies in `D_v` and no `u_i` lies in
`D_t`.

- If `h=3`, the unique `w_j` is missed by `t` and therefore met by `v`.
  The triple is `(3,1,0)`.
- If `h=2` and `t` misses both boundary singletons, `v` meets both and the
  triple is `(2,2,0)`.
- If `h=2` and `t` misses exactly one boundary singleton, `v` meets that
  vertex and may meet or miss the other.  The triples are respectively
  `(2,1,1)` and `(3,1,0)`.

These cases are exhaustive and give exactly the three patterns in (2.3).
The proof correctly allows `(3,1,0)` to arise from either value of `h`.

## 7. Final integrity check

The final source hash above and the metadata-only rebind to the
pre-promotion hash were recomputed before this audit was finalized.  No
finite enumeration or unbounded computational assumption is needed for the
GREEN verdict: the separator, contraction, and defect-pattern checks are
complete hand arguments.  Any mathematical alteration to the audited source
requires a new hash and a fresh audit.
