# Connectivity does not pull support six back through a contraction

**Status:** explicit counterexample with an exact checker.  It does not
satisfy strong seven-contraction-criticality and has a coherent fixed pair;
therefore it is a guardrail, not a counterexample to the active `HC_7`
target.

The checker is
[`hc7_global_contraction_pullback_probe.py`](hc7_global_contraction_pullback_probe.py).

## 1. The false rule

Let `xy` be an edge of a seven-connected `K_7`-minor-free graph, let
`H=G/xy`, and let `z` be the contracted image.  The following tempting
support pullback is false.

1. If `z notin R` and `mu_H(R)>=6`, then `mu_G(R)>=7`.
2. If `R={z,r}` and `mu_H(R)>=6`, then one of
   `mu_G({x,r}),mu_G({y,r})` is at least seven.

## 2. Counterexample

Let `P` be the 32-vertex planar dual of the truncated icosahedron and put

\[
                         G=\overline{K_2}\vee P,
\]

where the two new universal vertices are nonadjacent.  The graph `P` is
five-connected.  Hence `G` is seven-connected: deleting fewer than seven
vertices either leaves an apex, or deletes both apices and fewer than five
vertices of `P`.

The graph has no `K_7` minor.  At most two bags of a clique model can contain
the two apices.  Removing those bags from a putative `K_7` model leaves at
least five pairwise adjacent base-only bags, a `K_5` minor in the planar
graph `P`.

For the displayed base edge `xy=(0,16)`, direct exact connectivity
calculation gives

\[
                     \kappa(G/xy)=7.
\]

Write `z=0`.  The exhaustive support census gives

\[
 \begin{array}{c|c|c}
 R&\mu_{G/xy}(R)&\text{pullback value in }G\\ \hline
 \{1,2\}&6&\mu_G(\{1,2\})=6,\\
 \{z,1\}&6&\mu_G(\{0,1\})=\mu_G(\{16,1\})=6.
 \end{array}
\]

The checker prints explicit order-six models for all five values.  It also
exhausts all five-bag size patterns of total order at most seven, so the
reported values are exact.  There is a short lower-bound check: neither
`G` nor `G/xy` has a literal `K_5`.  The apices are nonadjacent, so such a
clique could use at most one apex and would require a literal `K_4` in the
five-connected planar base (or its displayed five-connected planar edge
contraction).  A nontrivial five-connected planar graph has no `K_4`, since
an embedded `K_4` exposes a separating triangle.

For comparison, the older adjacent-apex guardrail `K_2 vee I`, with `I`
the icosahedron, has no eligible contraction edge: all 55 edge contractions
have connectivity six.

## 3. Exact lesson

The counterexample has a coherent terminal pair, namely its two universal
vertices, and is not seven-contraction-critical.  Accordingly it proves
only the following boundary.

* Seven-connectivity and `K_7`-minor-freeness do not turn a support-six pair
  of the contraction into a support-seven pair of the original graph.
* A correct theorem must retain the exact split-row alternative: a small
  model can place `x,y` in distinct branch sets and disappear when `xy` is
  contracted.
* Eliminating that alternative must use the proper-minor colouring response
  or return the coherent fixed pair.  Pure support arithmetic is
  insufficient.

This is precisely the obstruction isolated abstractly by Lemma 2.1 of
[`../active/hc7_global_support_six_stateful_pullback.md`](../active/hc7_global_support_six_stateful_pullback.md).
