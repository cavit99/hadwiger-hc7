# Audit: terminal-cycle contraction and synchronized parity locks

**Verdict:** GREEN.  The three available states and one forbidden state are
valid, whole-component switching handles components meeting arbitrarily
many same-parity cycle vertices, shortest paths have no internal cycle
vertex, and deleting `e` loses at most the single palette indexed by the
other colour on `e` when `k` occurs there.  The `HC_7` sink application is
valid for an even induced terminal cycle, but supplies no terminal sink
classification.

**Audited source:**
`results/hc7_terminal_cycle_contraction_parity_locks.md`.

**Source SHA-256:**
`4835aea5b65987d21566fc47d5ff82c63bddc9a8ec70c89747cf70e56238da9d`.

## 1. Hosts and induced-cycle expansion

The edge `e=xy` is vertex-disjoint from `C`.  Thus contracting `C`, or
contracting both `e` and `C`, gives a proper minor and leaves the two
contracted vertex classes distinct.

Let a colouring of `G/C` assign colour `k` to the contracted cycle vertex.
Expanding it assigns `k` to every vertex of `C`.  Every edge from `C` to an
outside vertex maps to an incident edge of the contracted vertex, so its
outside endpoint already has colour different from `k`.  Parallel edges
created by common neighbours cause no problem.  The only internal edges
made monochromatic are edges with both ends in `C`.  Because `C` is
induced, these are exactly `E(C)`, all deleted in `X` and `J`.

For the simultaneous contraction `G/e/C`, the same argument applies to
both disjoint classes.  The edge `e` and all cycle edges are absent from
`J`.  Any edge between an endpoint of `e` and a cycle vertex becomes an
edge between the two contracted images and forces their colours to differ;
expanding it is therefore proper.  Common outside neighbours and merged
parallel edges remain harmless.  This validates both expansion steps.

The induced-cycle hypothesis is genuinely needed for this formulation.  A
chord would be removed as a loop by contracting `C` but would remain in
`X`, where the equal-colour expansion would make it monochromatic.

## 2. Three available states and the forbidden state

The edge-deletion minor `G-e` has a \(q\)-colouring.  Every such colouring
makes `x,y` equal, since otherwise restoring `e` would \(q\)-colour `G`.
All edges of `C` remain present and proper.  Restriction to `J` therefore
gives state `(e equal, C proper)`.

A colouring of `G/C` expands to `X` as audited above.  Since `e` is
disjoint from `C`, it remains a literal edge and is proper.  Restriction to
`J` gives `(e proper, C collapsed)`.

A colouring of the proper minor `G/e/C` expands to `J` with both `e` and
`C` collapsed, giving the third state.  Finally, if a colouring of `J`
made `e` proper and every cycle edge proper, restoring exactly
`{e}\cup E(C)` would recover a \(q\)-colouring of `G`.  This is forbidden
by \(\chi(G)=q+1\).

No compatibility among the three witness colourings is asserted or
needed.  The third witness is one whole-cycle state and is not obtained by
combining independently selected edge contractions.

## 3. Whole-component parity switch

Let `C=C_0 dotunion C_1` be the cyclic bipartition of an even cycle, and
fix \(j\ne k\).  Suppose no `k-j` component in `X` meets both parity
classes.  Switch `k,j` on **every** component meeting `C_0`.

This remains valid even when one component meets several vertices of
`C_0`: that component is switched once, and all of those vertices change
from `k` to `j`.  By the supposition it meets no vertex of `C_1`, so every
vertex there stays `k`.  Distinct selected components are disjoint, and a
whole-component Kempe switch preserves every edge of `X`, including `e`,
regardless of whether it switches zero, one, or both endpoints of `e`.

Every restored cycle edge has one endpoint in each parity class and hence
colours `j,k`.  Since `C` is induced, there is no unaccounted chord inside
one parity class.  All other edges were already present and remain proper
in `X`.  The result would therefore \(q\)-colour `G`, a contradiction.
Thus a component meeting both parity classes exists for every alternate
colour.

## 4. External shortest path

Inside such a component choose a shortest path from the set `C_0` to the
set `C_1`.  If an internal path vertex lay in `C_0`, its suffix to the
`C_1` endpoint would be a shorter path between the two sets.  If it lay in
`C_1`, the corresponding prefix would be shorter.  Since every cycle
vertex belongs to exactly one parity class, no internal vertex lies in
`C`.

The resulting path is literal in `X`, is bichromatic in `{k,j}`, and has
one endpoint in each fixed parity class.  Multiple same-parity contacts of
the ambient component do not affect this shortest-path argument.

## 5. Exact loss on deleting `e`

Let the proper edge `e` have distinct endpoint colours `r,s`.  Its edge is
present in the induced `k-j` graph exactly when both endpoint colours lie
in `{k,j}`.  Because `r` and `s` are distinct, this is equivalent to

\[
                         \{r,s\}=\{k,j\}.
\]

If \(k\in\{r,s\}\), there is exactly one such alternate colour `j`,
namely the other endpoint colour.  If \(k\notin\{r,s\}\), there is none:
even when one endpoint happens to have colour `j`, the other endpoint lies
outside `{k,j}`, so `e` is not an edge of that induced subgraph.

For every nonexceptional `j`, passing from `X` to `J=X-e` changes no edge
at all in the `k-j` induced subgraph.  Its parity-crossing component and
shortest external path therefore remain.  This proves the exact guaranteed
lower bound

\[
               q-1-\mathbf 1_{\{k\in\{r,s\}\}},
\]

which is at least \(q-2\).  The exceptional palette may also survive if a
different parity-crossing route avoids `e`; the theorem correctly claims
only the lower bound.

## 6. `HC_7` sink applicability

In the sink programme, the terminal cycle lies in `G-V(e)`, so it is
vertex-disjoint from the sink edge.  Inducedness in `G-V(e)` is the same as
inducedness on its vertex set in `G`, because deleting outside vertices
does not alter edges between cycle vertices.  A hypothetical minimal
`HC_7` counterexample supplies (1.1) with \(q=6\).

Hence an **even** terminal cycle satisfies every hypothesis and one
whole-cycle contraction yields at least four external parity-lock paths in
the common host `J`, synchronized in one colouring and between the same
literal parity classes.

This does not apply to an odd cycle: alternating two colours around it
cannot make all cycle edges proper, so the parity-switch contradiction is
unavailable.  It also does not establish internal disjointness among the
four paths; paths for different palettes may meet at vertices of colour
`k`.

## 7. Exact scope

The theorem proves a graph-global common colouring and a family of
same-parity-targeted literal locks.  It does **not** package those paths
with the two dominating bags, identify palette colours with model rows,
produce a rooted \(K_5\), expose a fixed pair, increase a verified sink
rank, classify a sink component, or prove `HC_7`.  Section 4 of the source
states these remaining alternatives at the correct open strength.
