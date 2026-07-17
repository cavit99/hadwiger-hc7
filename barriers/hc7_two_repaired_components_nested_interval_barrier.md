# Attachment count does not compose two repaired components locally

**Status:** explicit finite barrier with a deterministic, dependency-free
tree-decomposition checker; independently audited GREEN in the adjacent
audit.  This graph is not seven-connected and is not a counterexample to the
host theorem under investigation.

## 1. Construction

Start with the canonical `3+1` endpoint graph on

\[
 A=\{a_0,a_1,a_2,a_3,x,y\},\qquad
 B=\{b_0,b_1,b_2,r,p,q\}.
\]

Thus `a0,a1,a2,a3` induce a clique, the edges

\[
 xy,\ a_3y,\ xa_0,\ xa_1,\ xa_2
\]

are present, and `B` induces $K_6-pq$.  Take the first five named paths to
be the edges

\[
 a_ib_i\ (0\le i\le2),\qquad a_3p,\qquad xq.
\]

Subdivide the `y`--`r` path with twelve vertices, in order,

\[
             y,s_0,s_1,\ldots,s_{11},r.                \tag{1.1}
\]

Add two nonadjacent vertices `c,d`.  Let

\[
\begin{aligned}
 N(c)&=\{a_3,x,s_0,s_1,s_2,s_3,s_4,s_5\},\\
 N(d)&=\{y,r,s_6,s_7,s_8,s_9,s_{10},s_{11}\}.
                                                               \tag{1.2}
\end{aligned}
\]

There are no other edges.  Relative to the union $\Sigma$ of the six
named paths, `{c}` and `{d}` are distinct components of $G-V(\Sigma)$.
Each has eight distinct linkage neighbours.  The first has the compulsory
pair `{a3,x}`, and the second has `{y,r}`.  Their first--last intervals on
the `y`--`r` path are in the most concentrated noncrossing order: the
six contacts of `c` lie inside the outer `y`--`r` interval belonging to
`d`.

## 2. Exact negative certificate

The graph has a tree decomposition of width five.  The adjacent verifier
stores the twenty-one bags and the twenty edges of the decomposition tree
and checks all three defining properties:

1. every graph vertex occurs in a bag;
2. both ends of every graph edge occur together in a bag; and
3. the bags containing any fixed graph vertex induce a connected subtree.

Every bag has order at most six.  Hence the graph has treewidth at most
five.  Since treewidth is minor-monotone and $\operatorname{tw}(K_7)=6$,
the graph has no $K_7$ minor.

The verifier also checks that the graph has vertex-connectivity exactly
three: deleting any set of order at most two leaves it connected, while
`{a3,x,r}` is a three-vertex cut.

Run from the repository root:

```text
python3 barriers/hc7_two_repaired_components_nested_interval_barrier.py
```

Expected output:

```text
vertices 26
edges 59
component_attachment_counts 8 8
treewidth_upper_bound 5
vertex_connectivity 3
GREEN: nested-interval attachment-count barrier verified
```

## 3. Exact implication

The following local implication is false:

> In the canonical six-linkage, two distinct exterior components with the
> compulsory pairs `{a3,x}` and `{y,r}`, and with at least eight linkage
> neighbours each, force a $K_7$ minor merely from their attachment counts
> and first--last order.

The example does **not** refute the intended seven-connected
`K7`-minor-or-order-seven-separation theorem.  Its deliberate three-cut
shows what that theorem must add: seven-connectivity has to force a third
component or path across the two nested intervals, or turn the relevant
leaf-block side into an actual order-seven separation.  No argument that
only contracts the two displayed components and reads their attachment
sets can supply that missing step.
