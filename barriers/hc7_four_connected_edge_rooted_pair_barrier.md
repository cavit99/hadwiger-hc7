# A four-connected barrier to connectivity-only paired edge repair

**Status:** barrier/counterexample to an intermediate claim; deterministic
exhaustive checker in
[`hc7_four_connected_edge_rooted_pair_barrier_verify.py`](hc7_four_connected_edge_rooted_pair_barrier_verify.py).
This graph is not asserted to be contraction-critical or a counterexample
to Hadwiger's conjecture.

## Refuted claim

The following tempting strengthening of rooted-`K_4` theory is false:

> Let `K` be a four-connected nonplanar graph containing a literal `K_5`.
> For any distinct vertices `u,v` and vertex-disjoint edges `ab,cd`, if
> `u` is anticomplete to `{a,b}` and `v` is anticomplete to `{c,d}`, then
> `K` has vertex-disjoint connected subgraphs containing `{u,a,b}` and
> `{v,c,d}`, respectively.

## Counterexample

Take the graph with graph6 string

```text
Ffznw
```

and edge set

\[
\begin{aligned}
\{&01,03,04,05,06,
   13,14,15,16,
   23,24,25,26,\\
  &36,45,46,56\}.
\end{aligned}
\]

Set

\[
u=2,\qquad v=3,\qquad ab=01,\qquad cd=45.
\]

The graph is four-connected.  It is nonplanar because
`{0,1,4,5,6}` induces a literal `K_5`.  The vertex `2` is anticomplete
to `{0,1}`, and `3` is anticomplete to `{4,5}`.

Nevertheless there are no vertex-disjoint connected subgraphs containing
`{2,0,1}` and `{3,4,5}`.  The checker enumerates every connected vertex
set containing each prescribed triple and tests every disjoint pair.
Structurally, each prescribed triple induces an edge plus an isolated
root.  A connected enlargement of the first triple which avoids the
second prescribed triple must contain the only remaining vertex `6`, and
the symmetric statement holds for the second triple.  Thus two disjoint
enlargements would both have to contain `6`.

## Scope

This refutes the use of four-connectivity, nonplanarity, and even a
literal `K_5` as a standalone paired-repair theorem.  It does not refute
the contracted rooted-four dichotomy in the active star-kernel draft,
which retains the full seven-connected host and lifts small cuts back to
the original graph.
