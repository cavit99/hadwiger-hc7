# Internal audit: five-contact reserved completion

**Verdict:** GREEN for the exact source revision

```text
4b691b627cac8102663a3f32a5d9dfc37cacbdcedd3dfa58ad480f7cdcc77baa
```

This is a separate internal audit, not external peer review.

## 1. Scope checked

The audit checked:

1. every branch-set merger in Theorem 1.1;
2. disjointness, connectedness, branch-set counts and every required
   adjacency;
3. exhaustiveness of the two exceptional quotient geometries;
4. the eight-vertex sharpness proof in Proposition 1.2; and
5. the transfer of hypotheses from the reserved-component theorem to
   Corollaries 2.1--2.2.

The mathematical source revision checked line by line had SHA-256

```text
29e75a24e2c2f002f62b5eda027ab1568380ccc7d19f51884e1711f7b2ed4f62
```

The pinned source revision changes only its opening status line to link this
audit.  Its mathematical content is identical to the revision checked line
by line.

## 2. Findings

### The completion constructions are correct

When the possible missed labels agree, either deleting one of `X,Y` leaves
five outside clique bags, or merging the common ordinary missed bag with
`X` repairs the unique `X-Y` defect.  When the missed labels are distinct
and exactly one belongs to `\{X,Y\}`, their union is connected, both new
connected subgraphs meet it through opposite members, and its ordinary
member supplies adjacency to the other end of the old `X-Y` defect.

All displayed branch sets are pairwise disjoint and connected, and the
proof lists exactly seven of them.

### The two quotient exceptions are exhaustive and sharp

If both connected subgraphs have unique, distinct missed labels, the
completion above fails only when the two labels are `X,Y` in opposite
orientations or when both are distinct members of
`\{D,F_1,F_2,F_3\}`.  At the eight-bag quotient level the absent pairs are,
respectively, a four-vertex path or a three-edge matching.

On eight vertices a seven-branch-set minor model can only delete one vertex
or use one connected two-vertex branch set.  The complement-cover argument
in Proposition 1.2 correctly excludes both possibilities for each quotient.
Thus the exceptions cannot be removed from the stated adjacency data.

### The reserved-component corollaries retain their hypotheses

The cited reserved-component construction makes its linkage union connected,
adjacent to the residual connected subgraph, and adjacent to every outside
branch set except possibly the omitted owner.  Its audited source revision
is

```text
9710607f41d2c5120f5a24daa0f909a0e5e5fbf119f9e0d7198ebcea98c0b2ff
```

Choosing the omitted owner away from `X,Y` removes the crossed exception.
The theorem correctly retains the distinct-ordinary-label exception rather
than claiming an unconditional `K_7` minor.

## 3. Trust boundary

The theorem classifies exactly when five outside contacts complete the
displayed near-clique model.  It does not construct a residual connected
subgraph, preserve five contacts after a linkage, repair either exceptional
quotient, or synchronize a boundary colouring.  No unresolved assumption
remains inside its stated conclusions.
