# Independent audit: universal boundary-contact vertex split

**Verdict:** **GREEN.**  The nonseparating-path input, the two endpoint
degeneracies, the singleton-path case, and the exact order-seven separation
are valid under the stated hypotheses.  The result is conditional and does
not preserve a previously selected minor model or boundary colouring.

**Audited source:**
`results/hc7_boundary_full_universal_vertex_split.md`.

**Source SHA-256:**
`3390c21c45c2541ea4e4aba19776aa578e44ac9f9ac6739816aae4994148266e`.

## 1. External nonseparating-path input

The quoted theorem agrees exactly with Theorem 1.2.1 of Yingjie Qian's
2022 dissertation: if `D` is three-connected and `x,y,w` are distinct,
then `D-w` contains an `x-y` path `P` for which `D-V(P)` is connected.
Qian attributes this result to Tutte's 1963 paper *How to Draw a Graph*.
Thus the source uses neither a stronger connectivity assumption nor an
extra avoidance conclusion.

In the distinct-representative case, `x` and `y` are distinct by choice and
both differ from `w` by the definitions of `X` and `Y`, so all hypotheses
of the cited theorem are met.  The endpoint edges `bx` and `iy` for some
`i in I` make the path a repair support.  Since the path avoids `w`, the
connected residual contains the universal boundary-contact vertex `w` and
is adjacent to every member of `T`.

## 2. Boundary and unique-contact cases

Because `D` is a component of `G-T`, its external neighbourhood is contained
in `T`.  The nonempty opposite side makes that neighbourhood a genuine
vertex cut.  Seven-connectivity and `|T|=7` therefore give `N_G(D)=T`.

If `X` is empty, `b` has no neighbour in `D-w`, whence

\[
       N_G(D-w)\subseteq \{w\}\cup(T-\{b\}).
\]

Three-connectivity makes `D-w` connected and nonempty.  The opposite side
from the setup remains separated from it, so seven-connectivity gives the
reverse cardinality bound.  Since the displayed right-hand side has order
seven, containment and the cardinality bound force the asserted exact
equality.  Hence this is an actual order-seven separation, not merely an
upper bound on a neighbourhood.

If `Y` is empty, both vertices of `I` have no neighbour in `D-w`, and

\[
       N_G(D-w)\subseteq \{w\}\cup(T-I),
\]

whose right-hand side has order six.  The same two nonempty sides make this
a genuine separation, contradicting seven-connectivity.  This corrected
branch is exhaustive and does not incorrectly infer an order-seven equality
after omitting both members of `I`.

## 3. Common-contact singleton path

For nonempty `X,Y`, failure to choose distinct representatives forces
`X=Y={z}`.  The vertex `z` differs from `w`, is adjacent to `b`, and is
adjacent to at least one member of `I`.  Treating the one-vertex graph on
`z` as a path is explicitly allowed by the theorem.  Three-connectivity
makes `D-z` connected; it contains `w`, so it is nonempty and adjacent to
all seven boundary vertices.  The repair support and residual are disjoint
as required.

## 4. Trust boundary

The proof gives no control over how the selected path intersects previously
chosen branch sets inside `D`, and it transfers no boundary-colouring data.
It also assumes an already identified three-connected component containing
one vertex adjacent to all seven boundary vertices.  The GREEN verdict does
not infer any of those additional properties or `HC_7`.
