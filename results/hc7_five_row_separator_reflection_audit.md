# Independent audit: five-row reflection across a separation

## Verdict

**GREEN** at the exact source revision

```text
31adbe5d6255d2424c3fd9aeb9f1cef52068ea4d9bfe1150dea12cdb6c93fb06  results/hc7_five_row_separator_reflection.md
```

Every boundary-meeting row is assigned to the unique equality block
containing its boundary trace.  The stated alternative supplies a row for
the block containing `a`; hence every block receives a row.  The resulting
sets `X_B` are pairwise disjoint, connected and pairwise adjacent.
Contracting their spanning trees is a proper minor operation because
`X_A` contains and contracts an actual edge from `a` to its assigned row.

Deleting original vertices of `R` outside the carriers preserves all
carrier representatives, all inter-representative edges and every edge
from `L` to a boundary representative.  Pulling the minor colouring back
only to `L union T` is valid: equality blocks are independent, distinct
representatives form a clique, and every `L`--`T` edge survives at the
corresponding representative.  Thus the recovered boundary partition is
exactly `Pi`; palette alignment with the unchanged far-shore colouring
gives a six-colouring of `G`.

The proof is valid for an arbitrary finite boundary `T`; neither
`|T|=7` nor an auxiliary deficient row is required.  A colouring used as
the far-shore input must genuinely be proper on that unchanged closed
shore.  No unresolved mathematical assumption remains.
