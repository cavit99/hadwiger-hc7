# Complete elimination of tricyclic sole exteriors behind a Moser boundary

## Theorem

Let (G) be seven-connected, let (d(v)=7), suppose (G[N(v)]) is the
pure Moser spindle, and let (C=G-N[v]) be the sole exterior component.
If (C) is tricyclic, then (G) contains a (K_7)-minor.

## Previously closed contraction branch

The safe-contraction theorem in `hadwiger_moser_tricyclic_exteriors.md`
proves that every connected tricyclic graph of order at least six can be
contracted, using only nontriangle edges, to either:

1. a simple connected six-vertex tricyclic graph; or
2. one of two seven-vertex all-triangle cacti: three triangles sharing a
   common cutvertex, or a chain of three triangle blocks.

The first outcome is already eliminated by the certified six-shore
tricyclic theorem covering all twenty-two simple six-vertex types.  It
remains to close the two cacti.

## Seven-shore cactus lemma

Let (Q) be either of the following graphs on vertices (0,ldots,6):

\[
\begin{aligned}
E(Q_F)&=\{01,02,03,04,05,06,12,34,56\},\\
E(Q_C)&=\{01,02,12,23,24,34,45,46,56\}.
\end{aligned}
\]

Let (A_0,ldots,A_6) be disjoint connected shores representing every
edge of (Q), with at most one original cross-edge between each pair of
shores.  Suppose the shores collectively meet every vertex of the Moser
boundary (N), and for every nonempty proper (I\subset V(Q)),

\[
\left|N_N\left(\bigcup_{i\in I}A_i\right)\right|
 +|\delta_Q(I)|\ge7.                                  \tag{1}
\]

Then the graph on the shores and (N) contains an (N)-meeting
(K_6)-model.

### Certified proof

Contract the seven shores to helpers and retain the fixed Moser boundary.
The forty-nine helper-boundary incidences are Boolean variables.  For each
nonempty proper (I\), constraint (1) is encoded by counting the boundary
columns hit by a helper in (I); full column coverage is also imposed.

For a satisfying assignment, an exact search enumerates connected vertex
subsets of the fourteen-vertex quotient and finds six disjoint pairwise
adjacent bags, each meeting (N).  Only the optional incidences needed for
bag trees and cross-adjacencies are recorded.  Excluding each recorded
monotone model eventually gives `UNSAT` in both cases:

\[
\begin{array}{c|c}
Q_F&2635\text{ model clauses},\\
Q_C&3792\text{ model clauses}.
\end{array}
\]

The independent verifier `moser_cactus7_shore_verify.py` does not import
the discovery code.  It reconstructs both explicit cactus graphs, all
shore-union cut inequalities, full boundary coverage, every recorded bag
and all fifteen bag adjacencies, and both final Z3 unsatisfiability
checks.  A replay reports

```text
friendship verified 2635 K6 model clauses
chain verified 3792 K6 model clauses
```

The remaining trust boundary is the Z3 kernel.  This proves the
seven-shore cactus lemma.

## Application

Take inverse images of the seven cactus vertices under the safe
contractions.  Nontriangle contractions preserve simplicity, so there is
at most one edge between any two inverse-image shores.  For a nonempty
proper union (A_I), the vertices at the far ends of quotient cut edges,
together with (N_N(A_I)), contain its entire external neighbourhood.
This set separates (A_I) from (v).  Seven-connectivity therefore gives
(1), and (N_G(C)=N) gives full boundary coverage.

The cactus lemma supplies an (N)-meeting (K_6)-model in (G-v).
Adding the singleton bag ({v}) gives a (K_7)-minor.  Together with
the previous six-shore theorem, this eliminates every tricyclic
exterior. (square)

## Updated pure-Moser residual

Combining the tree, unicyclic, bicyclic, and now complete tricyclic
closures, every surviving pure-Moser sole exterior satisfies

\[
\rho(C)\ge4,
\qquad |E(C)|\ge |V(C)|+3.
\]

This is an infinite-family advance, but it does not solve the general
reserved-connector problem for exteriors of unbounded cyclomatic number.
