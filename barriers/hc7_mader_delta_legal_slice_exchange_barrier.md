# Barrier: symmetric exchange need not preserve graph-contraction slices

**Status:** hand-checkable counterexample to an intermediate algebraic
claim.  It does not satisfy the `HC_7` hypotheses and does not refute the
terminal-contraction projection theorem.

## 1. The false intermediate claim

The common representation in
[`../results/hc7_mader_terminal_contraction_projection.md`](../results/hc7_mader_terminal_contraction_projection.md)
contains both the split terminals `x,y` and their projected terminal `z`.
Two graph-realizable kinds of principal restriction are relevant:

- the split restriction retains `x,y` and omits `z`; and
- the contracted restriction retains `z` and omits `x,y`.

A tempting claim is that symmetric exchange between feasible endpoint
sets from these two restrictions can always be chosen to remain in one of
the graph-realizable restrictions.  The example below disproves this even
for one contracted edge.

## 2. Counterexample

Let the terminal partition have two parts

\[
                         \{x,y\},\qquad\{b_1,b_2\},
\]

and let the graph have exactly the edges

\[
                         xy,\quad xb_1,\quad yb_2.
\]

All four vertices are terminals.  In the split network,

\[
                         B=\{x,y,b_1,b_2\}
\]

is feasible, witnessed by the two disjoint Mader paths `xb_1` and
`yb_2`.

Contract `xy` to `z`.  The contracted network has edges `zb_1,zb_2` and
terminal parts `\{z\}` and `\{b_1,b_2\}`.  The set

\[
                         A=\{z,b_1\}
\]

is feasible.

Use the common skew-matrix representation with
`z=\alpha x+\beta y`.  The symmetric difference is

\[
                         A\mathbin\triangle B
                           =\{x,y,z,b_2\}.
\]

Apply symmetric exchange to `B` at the element `x`.  The possible second
elements give:

\[
\begin{array}{c|c|c}
v & B\mathbin\triangle\{x,v\} & \text{reason for infeasibility}\\
\hline
x & \{y,b_1,b_2\} & \text{odd order},\\
y & \{b_1,b_2\} & b_1,b_2\text{ lie in one terminal part},\\
b_2 & \{y,b_1\} & yb_1\notin E.
\end{array}
\]

The only feasible exchange uses `v=z` and returns

\[
                         \{y,z,b_1,b_2\}.
\]

This set is feasible in the common representation: because `y` is already
present, the projected element `z` must lift through `x`, recovering the
original feasible set `B`.  But it belongs to neither graph-realizable
restriction: it contains both the projected terminal `z` and the old
terminal `y`.

Thus the delta-matroid symmetric exchange axiom alone cannot keep an
exchange inside the split/contracted graph slices.  \(\square\)

## 3. Exact implication

The counterexample does not make mixed feasible sets meaningless.  In a
common projection representation, a feasible set containing `z` and
exactly one of `x,y` lifts through the other old endpoint to a feasible
set of the same order in the fully split network.  A set containing all
three of `x,y,z` is infeasible by linear dependence.

What fails is the stronger conclusion needed for graph induction: the
mixed set need not be the endpoint system of any member of the actual
contraction chain.  Therefore any successful continuation must use the
graph-specific connectivity, branch-set adjacency, or critical-colouring
data to normalize mixed exchanges.  No purely formal delta-matroid
exchange theorem can provide that normalization.

More precisely, suppose the projected column satisfies

\[
                         z=\alpha x+\beta y.
\]

If a feasible set contains `z` and `x` but not `y`, multilinearity of the
Pfaffian forces the set obtained by replacing `z` with `y` to be feasible
in the fully split restriction; the symmetric assertion holds with `x`
and `y` interchanged.  If it contains `z` but neither old endpoint, at
least one of the two old-endpoint lifts is feasible.  If it contains all
three elements, its principal Pfaffian vanishes because the `z` column is
in the span of the `x,y` columns.  Hence an endpoint-only normalization
does exist, but it is only the tautological lift back to the fully split
network.  It provides neither a feasible endpoint set in the contracted
network nor any of the labelled branch-set information needed by the
`HC_7` construction.

## 4. Terminal-part invariance

The following elementary observation is an independent obstruction to
recovering the missing labelled information from the Mader endpoint
system.

**Proposition (terminal-part invariance).**  Let
`(G,T,\mathcal T)` be a Mader network, where `\mathcal T` partitions the
terminal set `T`.  Toggle any collection of edges whose two endpoints are
terminals in the same part of `\mathcal T`.  The family of feasible
endpoint sets is unchanged.

**Proof.**  No Mader path can use such an edge `uv`.  If the path consists
only of `uv`, then its endpoints lie in the same terminal part, so it is
not a Mader path.  If `uv` occurs in a longer path, at least one of `u,v`
is an internal terminal, whereas a Mader path has no internal terminal.
Consequently no packing of vertex-disjoint Mader paths uses any toggled
edge.  The same path packings, and therefore the same endpoint sets, are
feasible before and after the toggles.  \(\square\)

In the intended near-`K_7` encoding, this means that the endpoint
delta-matroid is blind to all terminal--terminal edges internal to one
model part.  In particular, it cannot record:

- the edges of the designated `K_4` within that part;
- the edge joining the two split terminals;
- which of the two split terminals is adjacent to a particular designated
  vertex in the same part; or
- the existence of a path whose two designated endpoints lie in the same
  part as a feasible endpoint pair.

The last item says only that such a same-part linkage is not represented
as a Mader endpoint pair; it does not assert that arbitrary edges incident
with its internal vertices are irrelevant to every other path.

Thus two host graphs can have identical cross-part structure and identical
Mader feasible families while differing arbitrarily in these same-part
terminal edges.  For example, one may keep four designated vertices as a
`K_4`, keep two split vertices adjacent in the host graph, and redistribute
the contacts from the four `K_4` vertices between the split vertices
without changing the Mader endpoint family.  Those contacts nevertheless
determine whether the designated connected subgraphs have the adjacencies
required by the labelled `K_7`-minor construction.  The endpoint system
also cannot see
the deletion of the split edge, so it cannot encode the proper-minor
colouring or Kempe-chain consequences of that deletion.  These data must
enter through an additional labelled invariant rather than through the
Mader delta-matroid alone.

## 5. Retracted splice normalization

One might try to normalize a mixed feasible set by decoding its fully
split lift into two Mader paths ending at `x` and `y`, and then joining
those paths through the host edge `xy`.  This is not a valid Mader-path
normalization.  In the split network, the splice makes `x` and `y`
internal terminals of the joined path.  After contracting `xy`, it makes
`z` an internal terminal.  Either description violates the definition of
a Mader path.

The splice can sometimes be interpreted as one connected branch set in a
minor model, but it merges two prospective branch sets and so loses one
branch set.  It therefore neither supplies a feasible endpoint set in the
contracted Mader network nor gives the required seven-branch-set model.
Any earlier suggestion that this splice repaired the mixed exchange is
retracted.
