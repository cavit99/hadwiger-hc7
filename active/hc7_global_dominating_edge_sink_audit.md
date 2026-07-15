# Audit of the dominating-edge sink programme

## Verdict

**GREEN for the literal transition digraph and terminal-cycle closure;
AMBER for the proposed chromatic-stratum closure; OPEN for sink
classification.**  The construction is graph-global and finite, but it is
not yet a well-founded invariant.  Strong connectivity explicitly permits
neutral transition cycles.

This audit is independent of the proof attempt in
[`hc7_global_dominating_edge_sink_goal.md`](hc7_global_dominating_edge_sink_goal.md).

## 1. Positive out-degree and literal edge heads

In a seven-critical graph, deleting a two-set lowers chromatic number by at
most two, so `chi(G-P)>=5`.  The Dominating 4-Colour Theorem therefore gives
a dominating `K_5` model in `G-P`, and its normalized last two singleton bags
form an edge disjoint from `P`.  Hence every state has positive out-degree,
every transition head is a literal edge, and the finite transition digraph
has a sink strongly connected component.

Every vertex of a sink component is itself an edge.  Indeed, a sink state
has an out-neighbour inside the same component, and every such head is an
edge; strong connectivity then gives an incoming transition to every state.
A singleton nonedge component cannot be a sink because loops are impossible:
the transition head is disjoint from its tail.

## 2. Terminal-cycle rotation

For a normalized frame

```text
(T1,T2,T3,{v},{w})
```

let `C=G[T3 union {v,w}]` be its induced terminal cycle.  For each edge
`ab` of `C`, deleting `a,b` from the cycle leaves a connected path.  The
two endpoints each meet that path through their other cycle edge, and
`T1,T2` retain all required later-bag adjacencies.  Thus

```text
(T1,T2,C-{a,b},{a},{b})
```

is another normalized dominating model in the same graph `G-P`.  Therefore
all edges of every such cycle are successors of `P`.

If `P` belongs to a sink `Sigma`, closure puts all those cycle edges in
`Sigma`.  Since the terminal cycle lies in `G-P`, none of its edges uses an
endpoint of the edge-state `P`; it contributes at least three other states.
Consequently `|Sigma|>=4`, and every sink edge has a vertex-disjoint induced
cycle whose edges all lie in the same sink.

## 3. Chromatic strata

For an edge `e=xy`, vertex-criticality gives

```text
5 <= chi(G-{x,y}) <= 6.
```

The lower value is exactly the double-critical case; call the upper value
six-residual.  At least one six-residual edge exists, because if every edge
of `G` were double-critical, the Kawarabayashi--Pedersen--Toft theorem would
give a `K_7` minor.

Two tempting upgrades are invalid.

1. If every edge of one sink is double-critical, `G` need not be a
   double-critical graph.  The published theorem requires the property for
   every edge of `G`, not merely a closed subfamily.
2. If `e` is six-residual, a transition `e -> f` supplies a dominating model
   in `G-V(e)`.  It does not exclude a small near-Hajos carrier in
   `G-V(f)`, so it proves no increase of pair height.

Thus neither chromatic stratum is presently closed under the transition.

## 4. Exact missing theorem

The programme becomes a proof engine only after a **closed-family exchange
theorem** proves one of the following for every sink:

1. its double-critical Kempe systems compose into literal `K_7` branch
   sets;
2. a six-residual transition strictly raises the graph-global near-Hajos
   pair height; or
3. the whole sink identifies one fixed pair meeting every `K_5` model.

No result in the current notes proves any of these conclusions.  Until one
is established, sink existence is a useful global normalization, not a
termination argument.
