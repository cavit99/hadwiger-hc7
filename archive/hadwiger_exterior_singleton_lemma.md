# A general singleton-exterior exclusion

## Lemma

Let (G) be a proper-minor-minimal counterexample to
(mathrm{HC}_t), let (vin V(G)), and put (N=N_G(v)).  No component
of (G-N[v]) consists of a single vertex.

## Proof

Suppose ({x}) is such a component.  The proper minor (G-x) has a
proper ((t-1))-colouring (c).  Since (v) is adjacent to every
vertex of (N), the colour (c(v)) occurs nowhere on (N).

The vertex (x) has no neighbour outside (N): it is not adjacent to
(v), it has no neighbour in another component of (G-N[v]), and its
own exterior component is a singleton.  Hence assigning

\[
c(x):=c(v)
\]

creates no monochromatic edge.  This extends (c) to a proper
((t-1))-colouring of (G), a contradiction. \(square\)

## Consequences for the current (t=7) cells

This argument is independent of the degree of (v), the graph induced
by (N), and the number of other exterior components.  In particular,
every exterior component in the remaining degree-seven pure-Moser
two-component cell has order at least two.  Combined with the global
cutvertex and two-cut closures, each such component is either (K_2),
(K_3), or has order at least four and is 3-connected.
