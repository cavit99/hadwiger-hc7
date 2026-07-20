# Independent audit of the two-column absorption theorem

**Verdict:** **GREEN** for the exact source revision identified below.

**Audited source:**
[`hc7_pentagonal_bipyramid_two_column_absorption.md`](hc7_pentagonal_bipyramid_two_column_absorption.md)

**Audited SHA-256:**
`2759a37d6d3e6b93022c5fb58744dffbcd2e1d32b7263fdac201c77f07a39cff`

The mathematical source was audited at the preceding revision; its only
subsequent change replaces the pending-audit status line with a link to this
GREEN audit.

**Verifier SHA-256:**
`1f7bd1de6e67225522a646c4b88c96d543ed4a77279badc9421e0af766744dba`

The verifier changed only by removal of one trailing blank line after the
mathematical audit; its executable content is unchanged.

This is an internal mathematical audit, not external peer review.  The
generic five-bag construction and the fourteen-vertex certificate are
correct at the displayed revisions.  The theorem is only a sufficient
completion criterion; it does not force its two absorbable pieces from a
Kempe response.

## 1. Generic branch sets

The sets `D_1,D_2` are disjoint because `X_1,X_2` are vertex-disjoint and
lie in the two columns omitted from the four rim anchors.  Their
connectedness is assumed.  The other three displayed branch sets are
whole connected columns.

Among the four rim-derived sets, the inherited quotient edges

```text
C_1-C_2, C_2-C_3, C_3-C_4
```

and the three stipulated contacts

```text
D_1-C_3, D_1-C_4, D_2-C_4
```

give all six pairwise adjacencies.  The pole column `C_b` is adjacent to
all four rim anchors, so the five sets form a `K_5` model.

Each set retains a distinct whole old column.  Therefore both fixed root
subgraphs are adjacent to all five sets, and their mutual edge completes
the explicit `K_7` model.  No palette colour is identified with a column
label.

## 2. Finite certificate

The verifier constructs exactly the displayed fourteen-vertex graph and
checks:

- order fourteen and size thirty-seven;
- connectivity five and nonplanarity;
- connectedness and disjointness of the five displayed bags;
- coverage of all fourteen vertices; and
- all ten pairwise bag adjacencies.

It outputs:

```text
GREEN combined-negative PB core: distributed K5 certificate
```

Thus the finite combined-negative example is terminal after adjoining the
two universal root branch sets.

## 3. Trust boundary

The proof does not show that operation-selected paths can be chosen
vertex-disjoint, that their first column contacts have the required labels,
or that a failure returns a colour-compatible order-seven separator.  It
therefore does not establish the proposed dynamic three-outcome theorem or
`HC_7`.

All generic branch-set steps and finite checks are valid at the audited
hashes.  **GREEN.**
