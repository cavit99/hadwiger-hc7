# A bridge criterion for one Kempe transition across two shores

**Status:** written proof; separate internal audit GREEN in
[`hc7_two_shore_kempe_incidence_cycle_audit.md`](hc7_two_shore_kempe_incidence_cycle_audit.md).

This note gives an exact composition law for the two literal obstruction
paths returned by a single boundary Kempe transition.  The relevant object
is a bipartite multigraph whose edges are the boundary two-colour
components and whose vertices record the full two-colour components on the
two closed shores.  A common labelled boundary colouring exists exactly
when the switched edge is a bridge.  Otherwise that edge lies on an
alternating cycle of shore-supported two-colour connections.

The cycle is a colouring certificate, not a clique-minor model.  In
particular, the theorem does not identify palette colours with inherited
branch-set labels and does not prove `HC_7`.

## 1. Setting

Let `q>=2`, and let

\[
             V(G)=A\mathbin{\dot\cup}X\mathbin{\dot\cup}D,
\tag{1.1}
\]

where `A,D` are nonempty and anticomplete.  Let `c_A` be a proper
`q`-colouring of `G[A union X]`, and let `c_D` be a proper `q`-colouring
of `G[D union X]`.  Write

\[
                    \gamma_A=c_A|_X,
        \qquad      \gamma_D=c_D|_X.                  \tag{1.2}
\]

Fix two colours `alpha,beta`.  Suppose that `K` is one connected component
of

\[
       G[X][\gamma_A^{-1}(\{\alpha,\beta\})],          \tag{1.3}
\]

and that `gamma_D` is obtained from `gamma_A` by interchanging
`alpha,beta` exactly on `K`.

The set of vertices receiving `alpha` or `beta`, and its induced graph in
`G[X]`, are unchanged by this interchange.  Let

\[
                         \mathcal C                   \tag{1.4}
\]

be the common set of connected components of that boundary two-colour
graph.  Thus `K in mathcal C`.

Define a partition `mathcal P_A` of `mathcal C` as follows.  Two boundary
components belong to the same block when they lie in the same connected
component of

\[
       G[A\cup X][c_A^{-1}(\{\alpha,\beta\})].         \tag{1.5}
\]

Define `mathcal P_D` analogously from `c_D` on `G[D union X]`.

The **two-shore incidence multigraph** `J` is bipartite with vertex classes
`mathcal P_A` and `mathcal P_D`.  For every `C in mathcal C`, put one edge
`e_C` between the unique blocks of `mathcal P_A` and `mathcal P_D`
containing `C`.  Parallel edges are retained.  The distinguished edge is
`e_K`.

## 2. Exact bridge criterion

### Theorem 2.1

There are Kempe interchanges on pairwise disjoint full
`alpha`--`beta` components of the two closed-shore colourings which make
their labelled boundary colourings identical if and only if `e_K` is a
bridge of `J`.

Consequently, if `G` is not `q`-colourable, then `e_K` is not a bridge and
therefore lies on a cycle of `J`.

### Proof

For each block `P in mathcal P_A`, introduce a variable

\[
                         x_P\in\mathbb F_2.             \tag{2.1}
\]

The value one means that the full two-colour component in (1.5) meeting
the boundary components in `P` is interchanged; zero means that it is left
unchanged.  Define variables `y_Q` for `Q in mathcal P_D` in the same way.
Full two-colour components belonging to different blocks are disjoint, so
every selection of these variables gives legitimate simultaneous Kempe
interchanges on the corresponding closed shore.

Let `C in mathcal C`, and let `P_C,Q_C` be its two endpoints in `J`.
Starting from `gamma_A`, the vertices of `C` are interchanged exactly when
`x_{P_C}=1`.  Starting from `gamma_D`, they are interchanged relative to
`gamma_A` exactly when

\[
                    {\bf 1}_{C=K}+y_{Q_C}=1
                    \quad\hbox{in }\mathbb F_2.        \tag{2.2}
\]

The two resulting labelled boundary colourings agree precisely when

\[
       x_{P_C}+y_{Q_C}={\bf 1}_{C=K}
       \qquad(C\in\mathcal C).                         \tag{2.3}
\]

For every edge of `J` other than `e_K`, equation (2.3) requires its two
endpoint variables to be equal.  Hence the variables are constant on each
connected component of `J-e_K`.  The equation at `e_K` requires its two
endpoint variables to be different.  Such an assignment exists if and
only if the endpoints of `e_K` lie in different components of `J-e_K`,
which is exactly the assertion that `e_K` is a bridge.

When the assignment exists, perform the indicated full-component
interchanges.  The resulting closed-shore colourings agree on the literal
vertex set `X`, so they glue to a proper `q`-colouring of `G`.  Therefore,
if `G` is not `q`-colourable, `e_K` cannot be a bridge.  Every nonbridge
edge of a multigraph lies on a cycle, including a two-edge cycle formed by
parallel edges. \(\square\)

## 3. Literal host realization of the nonbridge certificate

The incidence cycle has a direct host interpretation.  The formulation
below deliberately retains connected boundary components as the junctions;
it does not contract them to minor-model labels.

### Theorem 3.1

Suppose that `e_K` lies on a simple cycle `Z` of `J`.  List the edges of
`Z` cyclically as

\[
               e_{C_0},e_{C_1},\ldots,e_{C_{r-1}},
               \qquad C_0=K,                           \tag{3.1}
\]

where `r>=2`.  For every two consecutive edges of this cycle there is a
literal `alpha`--`beta` path joining the corresponding boundary components
in the closed shore represented by the intervening cycle vertex in `J`.
Equivalently, for every vertex of `Z`, use its two incident cycle edges;
this convention gives two paths, one in each shore, when `Z` is a
two-edge parallel cycle.
The shores of these paths alternate between `A` and `D` around the cycle.

Paths corresponding to distinct vertices of `Z` on the same shore lie in
different full two-colour components, and hence are vertex-disjoint.
Paths on opposite shores have disjoint open-shore interiors.  A selected
path may meet additional boundary two-colour components internally; no
stronger boundary-disjointness is asserted.

Each such path can be decomposed, at its successive visits to `X`, into
paths whose internal vertices lie wholly in the relevant open shore.
Thus `Z` yields a cyclic sequence of literal shore-supported two-colour
connections, based at the operated component `K`.

### Proof

At a specified cycle vertex, its two incident cycle edges correspond to
two boundary components.  Suppose first that this vertex is a block
`P in mathcal P_A`.  By the definition
of `mathcal P_A`, the corresponding boundary components lie in one
connected component of the full two-colour graph (1.5).  A shortest path
between their vertex sets in that component is the required literal
`alpha`--`beta` path in `G[A union X]`.  The same argument with (1.5)
replaced by its `D`-shore analogue applies at a vertex of
`mathcal P_D`.

The vertices of a bipartite cycle alternate between its two vertex
classes, so the supporting shores alternate.  A simple cycle does not
repeat a block vertex.  Distinct blocks of `mathcal P_A` are distinct full
two-colour components of (1.5), and are therefore disjoint; the analogous
statement holds on the `D` shore.  Finally `A` and `D` are disjoint, so
paths on opposite shores have disjoint open-shore interiors.

Cut any selected path immediately before and after each internal visit to
`X`.  Every resulting nontrivial segment has its internal vertices in one
open shore and joins two boundary two-colour components.  Reading these
segments cyclically gives the final assertion. \(\square\)

The same incidence cycle has a parity consequence which does not depend on
choosing the paths.

### Theorem 3.2 (the cycle is a literal odd-cycle certificate)

For every vertex `P` of `Z` in `mathcal P_A`, let `H_P` be the full
`alpha`--`beta` component of (1.5) which induces `P`; for every vertex
`Q` of `Z` in `mathcal P_D`, define `H_Q` analogously in the other closed
shore.  Then the literal host subgraph

\[
       \mathcal H_Z=\bigcup_{P\in V(Z)\cap\mathcal P_A}H_P
          \ \cup\!
       \bigcup_{Q\in V(Z)\cap\mathcal P_D}H_Q          \tag{3.2}
\]

is nonbipartite.  Moreover, `mathcal H_Z-V(K)` is bipartite, and the
intersection of `mathcal H_Z` with either one of the two closed shores is
bipartite.  Consequently every odd cycle in `mathcal H_Z` meets `K` and
uses vertices of both `A` and `D`.

### Proof

Suppose that `mathcal H_Z` were bipartite, and fix a proper two-colouring
of it.  Each `H_P` is connected and already has the proper two-colouring
induced by `c_A`.  The fixed two-colouring therefore agrees with `c_A` on
`H_P` either directly or after one global interchange; record that choice
by a bit `x_P`.  Similarly record by `y_Q` whether the fixed two-colouring
agrees with `c_D` or its interchange on each `H_Q`.

Let `e_C` be an edge of the incidence cycle, joining `P` to `Q`.  The two
full components both contain the nonempty connected boundary component
`C`.  If `C ne K`, the two original boundary colourings agree on `C`, so
consistency of the fixed two-colouring gives

\[
                            x_P+y_Q=0.                  \tag{3.3}
\]

On `K` the two original boundary colourings are interchanged, and the same
consistency gives

\[
                            x_P+y_Q=1.                  \tag{3.4}
\]

Adding these equations in `mathbb F_2` around `Z` makes every vertex bit
occur twice.  The left side is therefore zero, whereas the right side is
one because `e_K` is the unique operated edge on the cycle.  This is a
contradiction.  Hence `mathcal H_Z` is nonbipartite and contains a literal
odd cycle.

On `X-V(K)` the traces `gamma_A,gamma_D` agree.  Colour
`mathcal H_Z-V(K)` by `c_A` on `A union (X-V(K))` and by `c_D` on `D`.
These prescriptions agree on their common boundary vertices, and there is
no edge from `A` to `D`; hence they form a proper two-colouring.  Thus every
odd cycle in `mathcal H_Z` meets `K`.  Finally, the restriction of `c_A`
properly two-colours the intersection of `mathcal H_Z` with `A union X`,
and `c_D` does the same for `D union X`.  An odd cycle therefore cannot be
contained in either one closed shore and must use vertices of both open
shores. \(\square\)

## 4. Order-eight consequence and trust boundary

Assume additionally that `G` is seven-connected and `|X|=8`.  Every
component of `G-X` containing the interior of one of the boundary-clean
segments obtained in Theorem 3.1 has neighbourhood contained in `X`.
Hence it either has an actual order-seven full-neighbourhood separator or
is adjacent to every literal vertex of `X`.

It follows that a single opposite-shore Kempe transition has the exact
trichotomy:

1. the bridge equation is solvable and the closed-shore colourings glue;
2. an alternating-cycle support exposes an actual order-seven separator;
   or
3. every open-shore component used by the alternating cycle is
   `X`-full.

In the live two- and three-component order-eight residue, item 3 is the
remaining case by hypothesis.  Fullness means that the alternating paths
do not by themselves add a new unlabelled quotient adjacency.  The theorem
does not split a full component while retaining its boundary contacts,
allocate the cycle to inherited branch-set labels, or construct a
`K_7`-minor model.  Any continuation must use operation-specific colouring
data or a label-preserving component split; the existence of the two
initial obstruction paths alone is not terminal.

## 5. Dependencies

- [a single boundary Kempe transition between opposite-shore responses](../results/hc7_opposite_shore_single_kempe_transition.md)
- [Kempe transitions across boundary-full order-eight components](../results/hc7_order8_full_component_kempe_transition.md)
