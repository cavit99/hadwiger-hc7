# A maximal pair of boundary-full connected subgraphs covers a connected shore

**Status:** superseded draft.  Lemma 1.1 of
[`hc7_exact7_connected_rich_width2_frontier.md`](../results/hc7_exact7_connected_rich_width2_frontier.md)
proves the same normalization in stronger form and has a separate GREEN
audit.  This duplicate is retained only for provenance and does not prove
`HC_7`.

## Theorem 1 (maximal-pair cover)

Let `G` be a finite graph, let `R` be a connected induced subgraph of `G`,
and let `S\subseteq V(G)-V(R)`.  Suppose `R` contains two vertex-disjoint
nonempty connected subgraphs `Q_0,Q_1`, each adjacent in `G` to every
literal vertex of `S`.  Choose such a pair maximizing

\[
                          |V(Q_0)\cup V(Q_1)|.          \tag{1.1}
\]

Then

\[
                          V(Q_0)\mathbin{\dot\cup}V(Q_1)=V(R).     \tag{1.2}
\]

In particular, after adding to each `Q_i` every edge of `R` with both ends
in its vertex set, the open shore has a partition into two nonempty
connected boundary-full induced subgraphs.  At least one edge of `R` joins
the two parts.

### Proof

Suppose that a vertex of `R` lies outside `Q_0\cup Q_1`, and let `C` be a
component of

\[
                         R-(V(Q_0)\cup V(Q_1)).        \tag{1.3}
\]

Because `R` is connected, an edge joins `C` to one of the two subgraphs,
say to `Q_i`.  The union of `Q_i`, that edge, and a spanning tree of `C` is
a connected subgraph.  It remains disjoint from `Q_{1-i}` and remains
adjacent to every vertex of `S`, because it contains `Q_i`.  Replacing
`Q_i` by this larger connected subgraph strictly increases (1.1), a
contradiction.  This proves (1.2).

Adding internal edges does not change either vertex set, connectedness, or
boundary fullness.  Finally, connectedness of `R` and the nonempty
partition (1.2) force an edge between the two parts. \(\square\)

## Corollary 2 (shore-filling form of the three-duty obstruction)

In the connected order-eight opposite-response interface, the two named
disjoint boundary-full connected subgraphs may always be selected so that
they partition the entire open shore.  Therefore components outside the
two selected subgraphs are not part of the normalized obstruction.

The remaining problem is a refinement problem inside one connected
two-part shore: either repartition its vertices into three disjoint sets
whose unions with the boundary groups `\{d,e\}`, `X`, and `Y` are connected,
or use `K_7`-minor exclusion and the selected proper-minor response to
obtain a compatible order-seven separation or a strict descent.

### Proof

Apply Theorem 1 to the two boundary-full connected subgraphs already
present in that interface.  The final sentence only restates the exact
remaining alternative and is not asserted as a proved implication. \(\square\)

## Exact gain and trust boundary

The normalization is independent of the orders and internal structures of
the two subgraphs.  It removes every argument based on components outside a
maximal pair from the live branch.

It does not split either part into two rooted connected sets, preserve a
selected colouring response under a repartition, or use `K_7`-minor
exclusion.  The two parts may have arbitrarily complicated internal
structure, and maximality of their union gives no vertex-minimality inside
either part.
