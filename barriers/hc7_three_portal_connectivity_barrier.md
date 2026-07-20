# Eight-connectivity does not force a reserved path and a three-portal tree

**Status:** explicit counterexample to an intermediate claim; deterministic
finite verification; separate internal audit GREEN in
[`hc7_three_portal_connectivity_barrier_audit.md`](hc7_three_portal_connectivity_barrier_audit.md).
The verifier is
[`hc7_three_portal_connectivity_barrier_verify.py`](hc7_three_portal_connectivity_barrier_verify.py).

## Refuted statement

The following connectivity-only assertion is false:

> Let `G` be seven-connected, let `S` be an eight-vertex set, and let `Q`
> be a connected component of `G-S` adjacent to every vertex of `S`.  For
> five distinct boundary vertices `d,e,x_1,x_2,x_3`, either `Q` contains a
> nontrivial `P_d(Q)`--`P_e(Q)` path disjoint from a connected subgraph
> meeting all three portal sets `P_{x_i}(Q)`, or `G` has an actual
> separation of order seven.

The counterexample is in fact eight-connected, `Q` is three-connected, and
`S` is an actual order-eight boundary with exactly two full components.

## Construction

Put

\[
 S=\{d,e,x_1,x_2,x_3,y_1,y_2,y_3\},
 \qquad X=\{x_1,x_2,x_3\},\quad Y=\{y_1,y_2,y_3\}.
\]

Let `G[S]` be the complete tripartite graph with parts `{d,e}`, `X`, and
`Y`.  In particular, `d,e` are nonadjacent, `X,Y` are independent, every
root is adjacent to every member of `X union Y`, and every `X`--`Y` edge
is present.

Let `Q` be the five-vertex wheel with rim

\[
                         q_0q_1q_2q_3q_0
\]

and hub `q_4`.  Its boundary portal sets are

\[
\begin{array}{c|c}
s&P_s(Q)\\ \hline
d&\{q_0\}\\
e&\{q_2\}\\
x_1&\{q_1\}\\
x_2&\{q_3\}\\
x_3,y_1,y_2,y_3&V(Q).
\end{array}                                                   \tag{1}
\]

Let the other component `R` be an edge `r_0r_1`, with both endpoints
adjacent to every vertex of `S`.  There are no `Q`--`R` edges.  This
completes the definition of `G`.

## Verification

The graph has 15 vertices and 70 edges.  Deleting `S` leaves exactly the
two connected `S`-full components `Q,R`.  Exhaustive enumeration of every
vertex set of order at most seven shows that its deletion leaves `G`
connected.  Since deleting `S` disconnects the graph, `G` has connectivity
exactly eight and has no actual order-seven separation.

There is no required packing in `Q`.  A connected subgraph meeting the
three `X`-portal sets must contain `q_1,q_3`.  If it is disjoint from a
`P_d`--`P_e` path, it avoids `q_0,q_2`; connecting `q_1,q_3` then forces
it to contain the hub `q_4`.  But deleting `q_1,q_3,q_4` leaves `q_0,q_2`
isolated and nonadjacent, so no `q_0`--`q_2` path remains.  This is a
contradiction.

The deterministic verifier independently enumerates all pairs of disjoint
connected supports in `Q` and all 16,384 vertex-deletion sets of order at
most seven.

Expected output:

```text
GREEN portal path/three-set-tree connectivity barrier
G: vertices=15 edges=70 connectivity=8 cuts_tested=16384
G-S: two connected S-full components of orders 5 and 2
Q: W5 connectivity=3; exhaustive packing witness: none
connected-support pairs checked=12
scope: no K7-minor-free or contraction-critical claim
```

Run from the repository root with

```text
PYTHONPATH=active/runtime/deps python3 barriers/hc7_three_portal_connectivity_barrier_verify.py
```

## Exact scope

The graph is not asserted to be `K_7`-minor-free, seven-chromatic, or
contraction-critical.  Thus it does not refute a theorem that genuinely
uses those hypotheses or operation-specific six-colouring responses.  It
does show that seven-connectivity, boundary fullness, three-connectivity of
the selected component, and the full opposite-response boundary adjacency
pattern are insufficient by themselves.

The example also proves that the small-component outcome in the adjacent
two--three-linkage reduction cannot be discarded by a connectivity-only
argument.
