# Adjacent defect-one subgraphs do not complete the order-eight interface

**Status:** explicit barrier to an intermediate contact-only claim.  This is
not a counterexample to `HC_7`.

## Refuted claim

The following contact-only principle is false:

> Let `S` be an eight-vertex boundary containing two disjoint triangles.
> Let `A,B,Q_0,Q_1` be four disjoint connected subgraphs outside `S`.
> Suppose `Q_0,Q_1` are adjacent to every vertex of `S`, `A` and `B` each
> miss exactly one boundary vertex, their two missed vertices lie in
> different boundary triangles, and `A` is adjacent to `B`.  Then these
> contacts force a `K_7` minor.

This is the natural quotient-only completion claim suggested by the
audited two-cut triangle-transversal residue.  The example below refutes
it even when the two defect-one subgraphs are singletons joined by an edge.

## Construction

Let

\[
 S=\{0,1,2,3,4,5,6,7\}
\]

and let the only boundary edges be the two triangles on `{0,1,2}` and
`{3,4,5}`.  Thus `6,7` are isolated in the boundary graph.

Add four vertices `A,B,Q_0,Q_1` with the following neighbourhoods in `S`:

\[
\begin{aligned}
 N_S(A)&=S-\{0\},\\
 N_S(B)&=S-\{3\},\\
 N_S(Q_0)&=N_S(Q_1)=S.
\end{aligned}
\]

Add the edge `AB` and no other edge among these four vertices.  This graph
has order twelve and satisfies every hypothesis of the refuted claim.

## Width-five certificate

Number `A,B,Q_0,Q_1` as `8,9,10,11`.  Eliminate the vertices in the order

\[
 0,6,7,1,2,3,4,5,8,9,10,11.                           \tag{1}
\]

Adding fill edges among the later neighbours at each step, their later
neighbour sets are respectively

\[
\begin{array}{c|l}
0&1,2,9,10,11\\
6&8,9,10,11\\
7&8,9,10,11\\
1&2,8,9,10,11\\
2&8,9,10,11\\
3&4,5,8,10,11\\
4&5,8,9,10,11\\
5&8,9,10,11\\
8&9,10,11\\
9&10,11\\
10&11\\
11&\varnothing.
\end{array}                                             \tag{2}
\]

Every set in (2) has order at most five.  Therefore (1) gives a chordal
completion with clique number at most six, equivalently a tree
decomposition of width at most five.  Since treewidth is minor-monotone and
`tw(K_7)=6`, the graph has no `K_7` minor.

The adjacent deterministic verifier reconstructs the graph, checks the
claimed contact sets and the edge `AB`, performs the fill process in (1),
checks all sets in (2), and prints the width-five certificate.

Run

```text
python3 barriers/hc7_order8_adjacent_defect_one_carriers_barrier_verify.py
```

with exact output

```text
vertices=12
defects=A:{0} B:{3} full=Q0,Q1 edge=AB
elimination_order=0,6,7,1,2,3,4,5,8,9,10,11
elimination_width=5
K7_minor=no (treewidth at most 5)
```

## Exact scope

The example is more targeted than the earlier raw order-eight barrier with
three full vertices and one vertex missing two boundary contacts: here
there are only two full vertices, but the other two vertices each have
defect one and are adjacent to each other.  This is the adjacent-carrier
abstraction obtained by assigning the two cut vertices to opposite lobes;
the raw components behind the two-cut are themselves anticomplete.

It does not satisfy seven-connectivity, seven-chromaticity, contraction
criticality, or the operation-specific six-colouring responses of the host
problem.  It therefore shows only that the final two-lobe residue cannot be
closed from boundary contact incidence and lobe adjacency alone.
