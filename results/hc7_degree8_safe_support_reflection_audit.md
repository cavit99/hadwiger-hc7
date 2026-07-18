# Audit: safe boundary supports reflect the two paired traces

## Verdict

**GREEN** at the exact source revision

```text
1248eb14c14662052bcbcd59c98e9b9a37d2e04ca06c6061fecdf811e0bb4f24  results/hc7_degree8_safe_support_reflection.md
```

The simultaneous connected contractions are a proper minor operation, the
boundary pullback is a proper colouring of the unchanged far closed shore,
and the five-row reflection theorem applies with all of its literal
hypotheses.  The support assignments and Boolean blocker formulas for the
four stated contact patterns are exhaustive within those patterns.  No
unresolved mathematical assumption remains in the conditional theorem.

## 1. Setup and disjointness

The five subgraphs `C_0,...,C_4` are pairwise vertex-disjoint and lie in
`G[L union I union J]`.  Hence no vertex of
`B=T-(I union J)` belongs to any `C_r`.

For a safe support `p` of `I`, the two selected contact edges and paths in
`C_0` and `C_2` form a connected subgraph `X_I`.  The trace conditions give

```text
X_I intersect T = I union {p}.
```

The analogous construction gives a connected `X_J` with trace
`J union {q}`.  These two subgraphs are disjoint because they use four
different pairwise disjoint `C_r` subgraphs and the distinct vertices
`p,q`.  This remains true if one of `p,q` is the distinguished boundary
vertex `a`.

Each connected subgraph contains actual contact edges, so contracting a
spanning tree of each strictly reduces the number of vertices.  The two
disjoint contractions therefore produce a proper minor of `G`.

## 2. Pulling the minor colouring back to the far shore

Both contracted subgraphs lie in `L union T`; thus every vertex of `R`
remains literal in the minor.  Replacing the representative of `X_I` by
the literal vertices of `I union {p}`, and similarly for `X_J`, gives a
proper colouring of `G[R union T]`:

1. the vertices expanded from one representative are pairwise nonadjacent
   by the two safe-support independence hypotheses;
2. every edge from an expanded vertex to an unchanged vertex survives as
   an edge from the corresponding representative;
3. every edge with one end in each expanded set survives between the two
   representatives, so such an edge forces their colours to differ.

Consequently both `I` and `J` are monochromatic in the pulled-back
colouring.  The other three row traces have order at most one and hence are
monochromatic automatically.  At least one row is boundary-free, exactly
as required by the second alternative in the five-row reflection theorem.

The equality partition used for reflection is the exact global partition
induced by this proper far-shore colouring.  The sets `I union {p}` and
`J union {q}` are contained in equality blocks; they need not themselves
be distinct maximal blocks.  The source does not require or assert that
stronger statement.

The independently audited dependency is

```text
31adbe5d6255d2424c3fd9aeb9f1cef52068ea4d9bfe1150dea12cdb6c93fb06  results/hc7_five_row_separator_reflection.md
```

Its unchanged-shore hypothesis is satisfied here: the contractions occur
in `L union T`, all vertices of `R` remain unchanged, and only the
contracted literal boundary vertices are reconstructed.  Reflection gives
a proper colouring of `G[L union T]` with exactly the same boundary
partition.  A colour permutation aligns the two closed-shore colourings,
and the absence of `L`--`R` edges permits them to glue.

## 3. Independent check of the support assignments

Ignoring boundary independence temporarily, support for `I` requires both
`bC_0` and `bC_2` to be present, while support for `J` requires both
`bC_1` and `bC_3` to be present.  Direct enumeration gives:

| pattern | contact supports for `I` | contact supports for `J` | distinct assignments |
|---|---|---|---|
| A | `b_1,b_2` | `b_1,b_2` | `(b_1,b_2),(b_2,b_1)` |
| B | `b_1,b_2` | `b_2` | `(b_1,b_2)` |
| C | `b_2` | `b_0,b_1,b_2` | `(b_2,b_0),(b_2,b_1)` |
| D | `b_1,b_2` | `b_1,b_2` | `(b_1,b_2),(b_2,b_1)` |

This is exactly table (3.2).  It is exhaustive for each exact normalized
missing-contact set in (3.1); the theorem correctly does not claim that
the four contact patterns exhaust all possible degree-eight configurations.

## 4. Independent check of the blockers

For an assignment `(x,y)`, safety fails precisely when

```text
E_I(x) or E_J(y).
```

Conjoining this condition over all useful assignments gives:

- patterns A and D:
  `(E_I(b_1) or E_J(b_2)) and (E_I(b_2) or E_J(b_1))`;
- pattern B: `E_I(b_1) or E_J(b_2)`;
- pattern C:
  `(E_I(b_2) or E_J(b_0)) and (E_I(b_2) or E_J(b_1))`, which is equivalent
  to `E_I(b_2) or (E_J(b_0) and E_J(b_1))`.

These are exactly (4.2)--(4.4).  In A and D the two clauses contain four
different edge predicates, so at least two literal boundary edges are
needed.  The stated one- and two-edge minima in B and C are also correct.

## 5. Trust boundary

This audit establishes only the conditional reflection theorem and the
complete blocker classification for the four exact patterns in (3.1).
It does not establish:

- that patterns A--D exhaust all boundary-contact configurations;
- the existence of the five pairwise disjoint connected subgraphs
  `C_0,...,C_4` in an arbitrary degree-eight residue;
- elimination of any boundary-edge blocker in (4.2)--(4.4); or
- a `K_7` minor, compatible separation, or strict reduction after deleting
  one of those blocker edges.

Those are correctly retained as separate obligations in the source.
