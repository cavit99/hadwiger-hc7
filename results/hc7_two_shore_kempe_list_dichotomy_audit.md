# Internal audit: two-shore Kempe/list-critical dichotomy

**Verdict:** GREEN.

**Audited source:** `results/hc7_two_shore_kempe_list_dichotomy.md`

**SHA-256:**

```text
0882a91fbb18c51fcec93ee8980f6c67d0a99a289e3f5bd264b1c8c27f13e4ec
```

This is a separate internal mathematical audit, not external peer review.

## 1. Boundary graph and extension sets

The vertices of the boundary reconfiguration graph are literal labelled
colourings, and every edge is one interchange on one connected component
of a boundary two-colour graph.  The extension sets are nonempty by
hypothesis and disjoint: anticompleteness of the two open shores lets
extensions with one common labelled trace glue.

## 2. Shortest-distance logic

Distance is minimized over both endpoint sets.  If an interior or later
path vertex still extended through the first shore, the suffix would be a
shorter path; if an earlier vertex extended through the second shore, the
prefix would be shorter.  Thus a distance-at-least-two path has an internal
trace rejected by both shores.

## 3. Distance-one paths

In an extension through the first shore, failure to lift the operated
boundary component forces its full two-colour component to meet another
boundary component.  A shortest connection has nonempty interior entirely
in that shore.  Reversing the same move in an extension through the other
shore gives the second path.  Interchanging the two names preserves the
underlying boundary two-colour components, and the two interiors are
disjoint because the shores are disjoint.  The theorem correctly does not
claim that the other boundary components agree.

## 4. List-critical kernels

For a trace rejected by a shore, extension is equivalent to colouring the
open shore from lists obtained by deleting the colours on literal boundary
neighbours.  A minimum-order induced uncolourable subgraph is connected and
vertex-minimal.  Colouring it after deleting `u` proves

\[
d_K(u)\ge |L(u)|=q-|c(N_X(u))|,
\]

since otherwise a listed colour absent from the coloured neighbours extends
the colouring.  Empty lists and singleton kernels cause no exception.  The
two kernels are disjoint because the shores are disjoint.

## 5. Small-boundary corollary and scope

For `q=6` and `|X|<=8`, the induced boundary graph is `K_7`-minor-free and
the audited small-boundary lemma gives exactly the required connectivity of
labelled six-colourings.  In a minor-minimal counterexample, deleting either
nonempty shore provides the opposite closed-side colouring.

Neither kernel is proved boundary-full, a component of `G-X`, or bounded by
an order-seven/eight neighbourhood.  The distance-one outcome synchronizes
the colour pair and operated boundary component only.  No clique minor or
common trace is overclaimed.

No mathematical defect was found.
