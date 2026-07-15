# Audit of the dominating-edge sink programme

## Verdict

**GREEN for the literal transition digraph, terminal-cycle closure,
inclusive common-host fork, simultaneous state/lock refinement, and even
whole-cycle parity synchronization; AMBER for the proposed
chromatic-stratum closure; OPEN for sink
classification.**  Section 3.1 states the common edge-deletion fork
correctly: it gives *at least one* of the endpoint-`K_4` and six-chromatic
common-host substrates.  Independently of that fork, double contraction
supplies the simultaneous `(equal,equal)` state and the audited
three-/four-lock allocation.  Whole-cycle contraction synchronizes at
least four external parity locks when the terminal cycle is even.  The
construction remains graph-global and finite, but is not yet a
well-founded invariant.

This audit is independent of the proof attempt in
[`hc7_global_dominating_edge_sink_goal.md`](hc7_global_dominating_edge_sink_goal.md).

**Audited source SHA-256:**
`3b17b039b23ae78c3f378efd9fa4d494a3691a577b328922642c3b739a5ebeac`.

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

## 5. Audit update: common host on every terminal-cycle arc

Let the sink state be the literal edge `e=xy`, and let `f=uv` be an edge
of a normalized terminal cycle for `e`.  The frame lives in
`G-{x,y}`, with vertex deletion understood, so `u,v` are distinct from
`x,y`.  Hence the literal edges `e,f` are vertex-disjoint.  Terminal-cycle
closure puts every such `f` in the same sink as `e`.

Now put

\[
                         H_f=G-\{e,f\},
\]

with edge deletion understood.  Seven-connectivity implies
`lambda(G)>=7`, so deleting two edges leaves `H_f` connected.  The audited
common edge-deletion fork applies and gives

\[
 \boxed{
   G[\{x,y,u,v\}]\cong K_4
   \quad\text{or}\quad
   \chi(H_f)=6.}
\tag{5.1}
\]

The disjunction in (5.1) is inclusive.  A literal endpoint `K_4` may
coexist with `chi(H_f)=6`; the underlying fork explicitly does not claim
exclusivity.  Section 3.1 now states this correctly as “at least one.”
Equivalently, the constructive proof may choose the endpoint `K_4`
whenever it is present and invoke the six-chromatic branch when it is
absent.

In the second branch, known `HC_6` gives a `K_6` minor, and connectedness
allows absorption to a spanning `K_6` model in `H_f`.  Strong
contraction-criticality also gives

\[
 \chi(H_f)=\chi(H_f+e)=\chi(H_f+f)=6,
 \qquad \chi(H_f+e+f)=7.
\tag{5.2}
\]

Thus every six-colouring of `G-f=H_f+e` has edge signature
`(e proper,f equal)`, every six-colouring of `G-e=H_f+f` has signature
`(e equal,f proper)`, and no six-colouring of `H_f` has signature
`(proper,proper)`.  Identifying the equal endpoints gives the named `G/f`
and `G/e` contraction responses.

Independently of which branch of (5.1) occurs, `G/e/f` is a proper minor
and hence has a six-colouring.  Expanding its two contracted vertices gives
an `(equal,equal)` colouring of `H_f`.  In that one colouring, the audited
whole-component switching theorem gives one named pair at least three
bichromatic lock incidences, or at least four if the two equality colours
differ.  In each one-edge restoration response the still-equal pair is
locked in all five alternate palettes; deleting the restored edge can
destroy at most one of those locks.  Thus each named pair separately has
four literal common-host locks in its own response colouring.

These are exact palette counts, not disjoint-linkage or row-allocation
statements.  The two one-restoration four-lock systems may use unrelated
colourings, and different lock paths may share vertices.

Consequently terminal-cycle closure supplies a cyclic **mixed family**:
for every cycle edge `f`, the simultaneous state/lock certificate is
available, and at least one of an endpoint `K_4` certificate or a spanning
common six-row host with opposite edge signatures is available; sometimes
both fork certificates are available.  Calling every member a six-row
host would be too strong unless the endpoint `K_4` branch were first shown
to imply `chi(H_f)=6`.

## 6. Audit update: whole-cycle synchronization

For an even induced terminal cycle `C`, the independently audited
whole-cycle theorem applies to the vertex-disjoint sink edge `e` and `C`.
A colouring of `G/C`, expanded after deleting `E(C)`, makes `C`
monochromatic while keeping `e` proper.  Whole-component Kempe switching
then forces, for every other colour, a component meeting both cyclic parity
classes.  Deleting `e` can destroy this property in at most one palette, so
at least four literal parity-crossing paths remain in one common colouring.

This is stronger than collecting independently coloured certificates for
the edges of `C`.  It is not a sink classification: paths of different
palettes may share vertices of the common cycle colour, no model-row labels
are supplied, and the proof gives no odd-cycle conclusion.

Source: [terminal-cycle contraction and synchronized parity
locks](../results/hc7_terminal_cycle_contraction_parity_locks.md), with its
[audit](../results/hc7_terminal_cycle_contraction_parity_locks_audit.md).

The revised constructive paragraph in Section 4 is sound as an open
programme under this inclusive reading.  Its three requested operations
are not asserted consequences:

1. endpoint `K_4` plus the dominating frame must still be decoded into
   `K_7` or a fixed pair;
2. a spanning common `K_6` must still be split or reselected in a
   label-faithful way under the two signatures; or
3. a whole cyclic family of failed splits must still produce a
   six-residual successor with a verified strict near-Hajos height
   increase.

The common-host fork and lock-allocation theorem prove none of these
labelled allocations or the claimed height increase.  The source correctly
labels them as the required composition theorem and correctly rejects two
consecutive uncomposed models or an unranked row rotation as outputs.
