# Internal audit of the connected attachment-tree counterexample

**Audit status:** GREEN.

**Audited source SHA-256:**
`2eb238f8c56f1294c22f865d1936c3421968764eafa8f500cecef84fb89ab3e5`

This is a separate internal audit, not external peer review.  It supersedes
the earlier audit of mathematical-content revision
`b46ed1f2b1fcbfa21b70642359493c4e3b7fdbbe0d9fa343a417697995fca4e3`.
The intervening source changes narrowed the claim to the connected-tree
interpretation and did not alter the displayed graph.

## Primary-source scope check

The statement checked is Theorem 5 of Kawarabayashi--Yu,
arXiv:2606.01586v2.  Its literal hypothesis excludes a strictly smaller
**forest** spanning the enlarged boundary.  It does not merely exclude a
smaller connected tree.  Theorem 4 is the strict reduction used by the
adjacent re-entry note; in its one-component case its threshold is two
above the boundary size.

The displayed graph has a smaller disconnected forest, so it is not a
counterexample to literal Theorem 5.  It is a counterexample exactly to
the attempted corollary obtained by replacing forest-minimality with
connected-tree minimality.  This distinction is stated in the title,
status paragraph, theorem discussion, and exact-scope paragraph of the
barrier note.

## Verification

In the graph displayed in the adjacent barrier note, the boundary vertex
`b` has only the neighbour `z_1`.  Every connected subgraph containing
`P union {w}` must therefore contain at least the six vertices
`P union {w,z_1}`.  The five displayed edges form a connected six-vertex
replacement tree, so the lower bound is sharp.  The original tree has
maximum degree three and cannot be a subdivision of `K_{1,4}`.

The construction does not satisfy the literal hypothesis if disconnected
replacement forests are allowed: a smaller disconnected forest exists.
The exact conclusion is therefore that the claimed connected-tree
corollary is false, while the strict `|P|+2` reduction remains intact.
