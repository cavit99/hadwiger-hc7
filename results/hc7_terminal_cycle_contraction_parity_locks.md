# Terminal-cycle contraction and synchronized parity locks

**Status:** proved and independently audited.  This is a graph-global
whole-cycle consequence of strong minor-criticality.  It does not classify
the dominating-edge sink or prove `HC_7`.

## 1. Setup

Let `q>=2`, and let `G` satisfy

\[
 \chi(G)=q+1,
 \qquad\text{every proper minor of }G\text{ is }q\text{-colourable}.
                                                               \tag{1.1}
\]

Let `e=xy` be an edge and let `C` be a vertex-disjoint induced cycle.
Put

\[
 X=G-E(C),
 \qquad
 J=G-\bigl(\{e\}\cup E(C)\bigr),                     \tag{1.2}
\]

where (1.2) uses edge deletion.  Say that `C` is **collapsed** in a
colouring of `J` when all its vertices have one colour, and **proper** when
the ends of every edge of `C` have different colours.

The induced-cycle hypothesis is essential for the expansion from `G/C`:
every edge with both ends in `C` must be among the edges deleted in (1.2).

## 2. Exact cycle-level state theorem

### Theorem 2.1

The common host `J` has the following three available states.

1. `e` is equal and `C` is proper.
2. `e` is proper and `C` is collapsed.
3. `e` is equal and `C` is collapsed.

No `q`-colouring of `J` makes `e` proper and `C` proper simultaneously.
More precisely, the first three states are supplied by `G-e`, `G/C`, and
`G/e/C`, respectively.

### Proof

The edge deletion `G-e` is a proper minor and hence has a `q`-colouring.
The ends of `e` are equal in every such colouring, since otherwise the
same assignment would colour `G`.  Restricting it to `J` leaves every edge
of `C` proper and gives state 1.

Contract the connected cycle `C` to one vertex.  The proper minor `G/C`
has a `q`-colouring, and the disjoint edge `e` remains proper.  Expand the
contracted vertex by giving every vertex of `C` its colour.  Because `C`
is induced, the only edges made monochromatic by this expansion are the
cycle edges deleted in `X`.  Thus the expansion is a proper colouring of
`X`, and its restriction to `J` has state 2.

Contract both `e` and `C`.  A `q`-colouring of the proper minor `G/e/C`
expands in the same way to a proper colouring of `J` with state 3.  Edges
between the two contracted sets cause no problem: they become edges between
the two contracted images and force their colours to differ.

Finally, a `q`-colouring of `J` in which `e` and all cycle edges are proper
would remain proper after restoring precisely those edges.  It would colour
`G`, contrary to (1.1).  \(\square\)

This is one state system for the whole cycle.  It is stronger than choosing
unrelated double-contraction colourings for the individual edges of `C`.

## 3. Synchronized locks on an even cycle

Assume now that `C` is even, and write its cyclic bipartition as

\[
                         V(C)=C_0\mathbin{\dot\cup}C_1. \tag{3.1}
\]

Fix any `q`-colouring `kappa` of `G/C`, expanded to `X` as in state 2 of
Theorem 2.1.  Let `k` be the common colour on `C`, and let `r,s` be the two
distinct colours on the proper edge `e=xy`.

### Theorem 3.1 (whole-cycle parity locks)

For every colour `j` different from `k`, some component of

\[
                         X[\kappa^{-1}(\{k,j\})]       \tag{3.2}
\]

meets both `C_0` and `C_1`.  Consequently it contains a path with one end
in each parity class and with all internal vertices outside `C`.

After deleting `e`, this conclusion remains true in the one common
colouring of `J` for at least

\[
             q-1-\mathbf 1_{\{k\in\{r,s\}\}}          \tag{3.3}
\]

alternate colours, and therefore for at least `q-2` alternate colours.  In
the `HC_7` case `q=6`, at least four synchronized parity-lock paths lie
wholly in `J`.

### Proof

Fix `j` different from `k`.  Suppose no component in (3.2) meets both
parity classes.  Simultaneously interchange `k` and `j` on every component
which meets `C_0`.  Whole-component Kempe switches preserve properness in
`X`, including on the present edge `e`.  Every vertex in `C_0` changes from
`k` to `j`, while every vertex in `C_1` remains `k`, because no selected
component meets `C_1`.  Restoring the edges of the even cycle therefore
gives a proper `q`-colouring of `G`, a contradiction.  Hence a component
meeting both parity classes exists.

Choose a shortest path in that component from `C_0` to `C_1`.  Its interior
avoids `C`: an internal cycle vertex belongs to one of the two parity
classes and would give a shorter prefix or suffix between the same two
sets.  The path is therefore a literal external parity lock.

Passing from `X` to `J` deletes only `e`.  That edge belongs to the
`k-j` subgraph only when its endpoint-colour set satisfies
`{r,s}={k,j}`.  This can occur for at most the one alternate colour paired
with `k` on `e`; if `k` is absent from `{r,s}`, it occurs for none.  For
every other `j`, the entire induced subgraph (3.2), and hence its
parity-crossing component, is unchanged in `J`.  This proves (3.3).
\(\square\)

All paths in Theorem 3.1 are synchronized in one colouring and join the
same two literal parity classes.  Paths belonging to different alternate
colours may still intersect at vertices of colour `k`; no disjointness is
claimed.

## 4. `HC_7` sink-cycle application

In the dominating-edge sink programme, let `e` be a sink edge and let `C`
be the induced terminal cycle of a normalized dominating `K_5` frame in
`G-V(e)`.  Then `e` and `C` satisfy the hypotheses above.  If `C` is even,
one contraction of the whole cycle supplies four synchronized external
parity locks in the common host `J`.

This discharges a genuine composition substep: the four paths no longer
come from four independently selected cycle-edge responses.  The remaining
theorem is label-faithful and topological.  It must show that these paths
either:

1. package with the two early dominating bags into a literal `K_7`;
2. have a common obstruction exposing one fixed `K_5`-transversal pair; or
3. produce a verified strict successor in the global sink rank.

No one of these outcomes follows merely from Theorem 3.1.

For an odd terminal cycle, the two-colour alternating target used in the
proof is impossible for parity reasons even when all bichromatic components
are singletons.  Thus the theorem gives no odd-cycle conclusion.  Resolving
that branch requires a three-colour exchange, a contraction of a selected
cycle interval with a label-preserving lift, or a separate terminal
argument; treating the parity failure itself as a separator would be
invalid.

## 5. Exact scope

The theorem is uniform in `q` and uses no Moser labels, portal order,
selected adhesion, or pre-existing clique model.  It proves a common
whole-cycle colouring and synchronized literal paths.  It does not prove
path disjointness, a rooted `K_5`, a row split, a fixed pair, a strict
height increase, sink termination, or `HC_7`.
