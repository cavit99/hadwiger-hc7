# Independent audit of the surplus-sensitive exact-seven density bound

**Verdict:** GREEN for Theorem 2.1 and the conditional residual-partition
specializations at the exact source revision below.

**Audited source:** `hc7_direct_entry_surplus_density.md`, SHA-256

```text
59b12bb3ee5b1215fa054e468553154e884c978e0cee8af6ce54a5e7f12cf3e9
```

This is a separate internal mathematical audit, not external peer review.
It checks every edge retained after contracting the opposite shore, the
total-excess and whole-degree-surplus identities, the multi-component
refinement, Mader's range, the boundary-colour incidence bound, and the
state-provenance warning for the two residual partitions.

## 1. Exact local identities

Put `m=|E(G[R])|` and `e_RS=|E_G(R,S)|`.  The definitions give

\[
 2m=6r-C+E,
 \qquad e_{RS}=C+P,
 \qquad d_G(v)=6+\varepsilon(v)+\rho(v).
\]

Once degrees seven and eight have been excluded, every shore vertex has
degree at least nine and

\[
 \Delta=\sum_{v\in R}(d_G(v)-9)\ge0,
 \qquad E+P=3r+\Delta.
\]

All equalities count literal edges; no inequality or average-degree
substitution is hidden here.

## 2. Opposite-shore contraction and Mader arithmetic

Every component of `G[L]` has neighbourhood contained in `S` and separates
itself from the nonempty set `R`.  Seven-connectivity and `|S|=7` therefore
make each of the `a=comp(G[L])` components adjacent to all seven boundary
vertices.  Contracting all components gives a simple minor `H` with

\[
 |V(H)|=r+7+a\ge9
\]

and exactly the following counted edges:

\[
\begin{aligned}
 |E(H)|
  &=m+e_{RS}+s+7a\\
  &=6r+\frac{C-E}{2}+\Delta+s+7a.
\end{aligned}
\]

The internal `R` edges, `R-S` edges, boundary edges, and the `7a` new
component-boundary edges are pairwise disjoint.  No parallel-edge
suppression removes an edge from any of these classes.

Mader's `K_7`-minor extremal inequality applies because `H` is simple,
`K_7`-minor-free, and has at least nine vertices.  Its upper bound is

\[
 5(r+7+a)-15=5r+20+5a.
\]

Comparison gives exactly

\[
 2r+C-E+2s+2\Delta+4a\le40,
\]

equivalently the claimed (2.1).  Since `E-C` is even by the internal-degree
identity, its right side is integral.  Taking `a>=1` and dropping the
nonnegative terms `C/2,Delta` gives the advertised weaker
`r<=18-s+E/2` conclusion.

## 3. Boundary-full subgraphs and residual partitions

For every colour used on `S`, each boundary-full connected subgraph contains
a vertex adjacent to a boundary vertex of that colour.  Vertex-disjointness
therefore makes these distinct `(vertex,colour)` incidences and proves
`C>=tb` for `t` such subgraphs.  The direct-entry `t=2` specializations are
valid.

If the list-defining assignment itself has partition `Pi_A`, it uses four
boundary colours; if it has partition `Pi_B`, it uses three.  Substitution
gives exactly the two bounds in (3.2).  The source correctly does not apply
them to the present proof spine: there the known `Pi_A/Pi_B` partition comes
from the old shore colouring, while the lists come from a different
simultaneous-contraction colouring.  Only inequality of the two partitions
is known.

In either residual partition, the three-set block, the two-set block, and
the displayed `x,y` pair contribute five distinct boundary nonedges, so
`s<=16`.  This is an upper bound and cannot improve a density inequality
whose right side decreases with `s`.  No positive lower bound for `s`
follows from these partitions alone.

## 4. Trust boundary

The theorem is an unbounded host-level order bound.  It does not bound `E`
from the two marked exceptions, synchronize boundary colourings, or preserve
the five named model branch sets.  The adjacent odd-wheel barrier correctly
shows that an excess bound needs more than local list-criticality and
seven-connectivity.
