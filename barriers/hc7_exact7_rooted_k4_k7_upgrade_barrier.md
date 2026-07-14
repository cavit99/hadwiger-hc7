# A rooted-`K_4` cross-lobe expansion need not contain `K_7`

**Status:** explicit solver-free barrier.  This graph proves that the
rooted-`K_4` handoff can force `K_7^vee` without forcing `K_7` from the same
static quotient.  It is not a hypothetical `HC_7` counterexample.

Use the thirteen vertices

```text
c,a1,t1,a2,t2,a3,t3,r,h1,h2,h3,p,q.
```

The four vertices `r,h1,h2,h3` induce `K_4`.  The three reversed trace
bags have edges

```text
h1-a1, h1-t3, h2-a2, h2-t2, h3-a3, h3-t1,
```

and `c-r` is present.  Each of `p,q` is complete to the seven boundary
vertices.  The retained boundary edges are

```text
a1-a2, a1-c, a1-t3, a2-c, a2-t3, a3-c.
```

Thus the original pairs `a_i t_i` are independent, `c` sees every pair,
every two original pairs have an edge between them, and the reversed traces
admit the required rooted `K_4` expansion.

The graph contains `K_7^vee`; one labelled model is

```text
{a3}, {a2,h2}, {h1}, {c,r}, {p,t2,t3}, {h3,t1}, {a1,q},
```

where the only omitted adjacencies are from `{a3}` to the next two bags.
But it has no `K_7` minor.  The following eight bags, joined by the seven
tree edges listed below, form a tree decomposition of width five:

```text
D1 = {h2,p,q,t2}
D2 = {h3,p,q,t1}
D3 = {a3,c,h3,p,q}
D4 = {c,h1,h2,h3,r}
D5 = {a1,a2,c,h1,p,q}
D6 = {a1,a2,h1,p,q,t3}
D7 = {a2,c,h1,h2,p,q}
D8 = {c,h1,h2,h3,p,q}

D5-D6, D7-D5, D7-D8, D7-D1, D8-D3, D8-D4, D8-D2.
```

Every graph edge lies in a displayed bag and the bags containing each
vertex form a connected subtree.  Their maximum order is six, so the graph
has treewidth at most five.  Since treewidth is minor-monotone and
`tw(K_7)=6`, the graph has no `K_7` minor.

The companion verifier checks the paired-state data, the literal
`K_7^vee` bags, and every tree-decomposition axiom without a solver.

## Exact lesson

The rooted expansion is a valid label-faithful near-`K_7` handoff, but a
claim that it directly produces `K_7` is false without additional dynamic
criticality or a model-composition argument.
