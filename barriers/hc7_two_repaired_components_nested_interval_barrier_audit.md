# Independent audit: nested-interval attachment-count barrier

**Verdict:** GREEN for the exact barrier and verifier revisions identified
below.

## Audited revisions

- barrier SHA-256:
  `0aff965cc225c89ac97189e431408aa873ef5da4f9e65bb7678ffee13175aedf`
- verifier SHA-256:
  `6580e489fbc22635611468abcd00fc959d7ee759b2637dfc34e0861763da2bb3`

The audited files are
`barriers/hc7_two_repaired_components_nested_interval_barrier.md` and
`barriers/hc7_two_repaired_components_nested_interval_barrier.py`.

## 1. Verifier replay

Running the documented command under Python 3 returned exactly:

```text
vertices 26
edges 59
component_attachment_counts 8 8
treewidth_upper_bound 5
vertex_connectivity 3
GREEN: nested-interval attachment-count barrier verified
```

The verifier uses only the Python standard library.

## 2. Graph construction and attachment data

The generated graph has the twelve normalized endpoint vertices, twelve
internal vertices on `P5`, and the two exterior vertices `c,d`.  The edge
set consists exactly of:

- the specified left support;
- `K6-pq` on the right support;
- five one-edge linkage paths and the subdivided `y`--`r` path;
- the eight edges from `c` to `a3,x,s0,...,s5`; and
- the eight edges from `d` to `y,r,s6,...,s11`.

The script checks that `c,d` are nonadjacent and that their neighbourhoods
are exactly these two eight-element sets.  Hence they are distinct
components outside the linkage union and have the two advertised compulsory
pairs.  Along the oriented `y`--`r` path, the first and last contacts of `d`
are `y,r`, while all six contacts of `c` lie at `s0,...,s5`; this is the
claimed nested, noncrossing first--last order.

## 3. Treewidth certificate

The verifier stores 21 bags and 20 distinct tree edges.  It checks that the
bag graph is connected; the edge count therefore makes it a tree.  It then
checks all three tree-decomposition axioms directly:

1. the union of the bags is the full 26-vertex set;
2. every one of the 59 graph edges has both ends in some bag; and
3. for each graph vertex, the bags containing it induce a connected subtree.

The maximum bag size is six, so this is a valid width-five tree
decomposition.  Since treewidth is minor-monotone and `tw(K7)=6`, the graph
has no `K7` minor.  This is a complete negative certificate, not a failed
minor search.

## 4. Exact connectivity

For every vertex subset of order zero, one, or two, the verifier constructs
the remaining graph and checks it is connected.  It separately checks that
deleting `{a3,x,r}` disconnects the graph.  Thus its vertex-connectivity is
at least three and at most three, hence exactly three.  As a cross-check, the
two resulting components after this deletion are the endpoint-side set
`{a0,a1,a2,b0,b1,b2,p,q}` and the set containing the subdivided path and
both exterior vertices.

## 5. Exact scope

The example disproves only the local claim that two repaired components,
eight attachment vertices each, and nested first--last intervals force a
`K7` minor from that attachment information alone.  It is deliberately not
seven-connected.  It does not refute a theorem that also uses
seven-connectivity to obtain a path across the nested intervals or an actual
order-seven separation, and it is not a counterexample to `HC7`.

## Unresolved assumptions or gaps

None for the stated finite barrier and its exact scope.
