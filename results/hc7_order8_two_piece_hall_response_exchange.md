# Demand-two Hall responses force a cross-edge matching or a smaller response side

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_two_piece_hall_response_exchange_audit.md`](hc7_order8_two_piece_hall_response_exchange_audit.md).
This is a
conditional theorem inside outcome 3 of the audited
[positive boundary-excess theorem](../results/hc7_order8_positive_excess_frozen_outer_shore.md).
It does not prove `HC_7`.

## 1. Setting

Use the notation of that theorem.  Thus

\[
 V(G)=E\mathbin{\dot\cup}B\mathbin{\dot\cup}C,
 \qquad E_G(E,C)=\varnothing,
 \qquad C=Q_0\mathbin{\dot\cup}Q_1,
\tag{1.1}
\]

where `E,C,Q_0,Q_1` are connected, an edge joins `Q_0,Q_1`,

\[
 B=(S-\{e\})\mathbin{\dot\cup}W,
\tag{1.2}
\]

and each `Q_i` is adjacent to every vertex of `S`.  The whole set `C` is
adjacent to every vertex of `B`.

A **response side** is a nonempty connected set `A` with full neighbourhood
`N_G(A)` separating it from a nonempty opposite side, together with a
crossing edge whose deletion produces a six-colouring legal on the opposite
closed side and rejected by the intact `A`-side.  Order response sides
lexicographically by

\[
                         (|N_G(A)|,|A|).
\tag{1.3}
\]

No minimality in (1.3) is assumed unless stated explicitly; the theorem
will instead return a smaller response side as one possible conclusion.

For `i in {0,1}`, put

\[
 m_i=|W-N_G(Q_i)|,
 \qquad
 h_i=|N_G(Q_i)\cap Q_{1-i}|.
\tag{1.4}
\]

## 2. Every operation-specific response has demand at least two

### Lemma 2.1

Every equality partition induced by deleting a crossing edge between `B`
and either `E` or `C` has full-subgraph demand at least two, when oriented
from the unchanged closed shore toward the intact rejected shore.

#### Proof

Delete an `E`--`B` edge.  The resulting colouring is proper on
`G[C\cup B]`, and its boundary partition is rejected by the intact
`E`-shore; otherwise the two closed-shore colourings would align and glue.
The connected set `C` is adjacent to every vertex of `B`, so it is one
universal support in the transported-partition theorem.  A partition of
demand at most one would therefore reflect through the intact `E`-shore,
a contradiction.

The argument is symmetric for a `C`--`B` edge, using the boundary-full
connected set `E`.  The demand cannot be zero in either orientation; this
also follows from `|B|>=9` and the use of at most six colours. \(\square\)

In particular, both one-edge partitions in the bypass outcome of
Proposition 3.1 of the cited theorem have demand at least two.

## 3. Exact demand-two incidence

Let `Sigma` be the partition induced by an `E`--`B` response and suppose
its demand is exactly two.  Choose a maximum clique `U` among its singleton
blocks and call the other two blocks `C_1,C_2`.  Join `Q_i` to `C_j` when
`Q_i` has a neighbour at every vertex of

\[
 R_U(C_j)=C_j\cup\{u\in U:E_G(u,C_j)=\varnothing\}.
\tag{3.1}
\]

### Lemma 3.1 (the two exact Hall forms)

Exactly one of the following incidence forms occurs.

1. At least one of `C_1,C_2` has no incident support.  For such a block
   there are distinct vertices `w_0,w_1 in W` such that `Q_i` misses
   `w_i` and `Q_{1-i}` meets it.
2. After possibly exchanging the indices, `Q_0` is incident with both
   blocks and `Q_1` with neither.  For each `j` there is a vertex

   \[
                   w_j\in R_U(C_j)\cap W
   \tag{3.2}
   \]

   missed by `Q_1` and met by `Q_0`.  If `w_1=w_2`, this common vertex
   belongs to `U` and has no boundary neighbour in either `C_1` or `C_2`.

#### Proof

The transported-partition theorem says that the two-by-two incidence graph
has no matching saturating `C_1,C_2`.  If one right vertex has degree zero,
item 1 holds.  Otherwise both have positive degree, and Hall failure for
the two-vertex right side says their combined neighbourhood is one support,
which is item 2.

Every failed incidence is witnessed in `W`, because each `Q_i` is adjacent
to every vertex of `S-\{e\}`.  In item 1, the two witnesses are distinct:
`C=Q_0\dot\cup Q_1` is boundary-full, so no literal boundary vertex is
missed by both subgraphs.  Hence the other subgraph meets each witness.
The same boundary-fullness proves the meeting assertion in item 2.

If `w_1=w_2`, then this vertex belongs to the intersection of the two
required sets.  The blocks are disjoint, so the intersection consists
only of vertices of `U` having no boundary edge to either block.  This
proves the last assertion. \(\square\)

## 4. Literal response rank of the two pieces

### Lemma 4.1

For `i in {0,1}`,

\[
                         |N_G(Q_i)|=|B|+h_i-m_i.
\tag{4.1}
\]

Consequently at least one of the following holds.

1. `Q_i` is a response side strictly smaller than `C` in the rank (1.3).
2. `h_i>=m_i+1`.

#### Proof

There are no `E`--`C` edges.  Every `Q_i` meets all seven vertices of
`S-\{e\}`.  Its remaining external neighbours are precisely its neighbours
in `W` and in `Q_{1-i}`.  These sets are disjoint, and therefore

\[
\begin{split}
 |N_G(Q_i)|
  &=7+(|W|-m_i)+h_i\\
  &=|B|+h_i-m_i.
\end{split}
\]

For every edge from `Q_i` to its full neighbourhood, a six-colouring after
deleting that edge is legal on the opposite closed side and is rejected by
the intact `Q_i`-side; otherwise it would glue and six-colour `G`.  Hence
`Q_i` is a response side.

If `h_i<m_i`, equation (4.1) lowers boundary order.  If `h_i=m_i`, it has
the same boundary order as `C` but `|Q_i|<|C|`.  Both cases give item 1.
Outside item 1, integrality gives `h_i>=m_i+1`. \(\square\)

## 5. A two-edge matching unless the nonowner is a singleton

Let `J` be the bipartite graph of edges between `Q_0` and `Q_1`.

### Theorem 5.1

For a demand-two response, at least one of the following holds.

1. There is a response side strictly smaller than `C` in the rank (1.3).
2. The graph `J` contains a matching of order two.
3. The Hall incidence has form 2 of Lemma 3.1 and its unique nonincident
   support consists of one vertex.

In particular, form 1 of Lemma 3.1 always gives outcome 1 or 2.

#### Proof

Assume outcome 1 does not hold.  Lemma 4.1 gives

\[
                         h_i\ge m_i+1
\tag{5.1}
\]

for both indices.

In Hall form 1, each support misses a literal witness, so `m_0,m_1>=1`.
Thus at least two vertices of each side of `J` are incident with an edge.
A bipartite graph of matching number at most one is a star and has only one
incident vertex on at least one side.  Therefore `J` has a matching of
order two.

In Hall form 2, orient the indices so that `Q_1` is the nonincident
support.  It misses at least one witness, so `m_1>=1`; (5.1) gives
`h_1>=2`.  Suppose `J` has no two-edge matching.  It is a star.  Since at
least two vertices of `Q_0` are incident with `J`, the centre of this star
is one vertex `v in Q_1`.

If `Q_1-{v}` is nonempty, let `A` be any component of that graph.  Every
edge from `A` to `Q_0` would be an edge of `J` not incident with `v`, so
there is none, and

\[
 N_G(A)\subseteq (N_G(Q_1)\cap B)\cup\{v\},
 \qquad
 |N_G(A)|\le |B|-m_1+1\le |B|.
\tag{5.2}
\]

More explicitly, the boundary part of `N_G(A)` is contained in the
`|B|-m_1` vertices met by `Q_1`, and every internal neighbour lies in the
single vertex `v`.  Deleting a crossing edge makes `A` a response side.
If the last inequality in (5.2) is strict, its boundary order decreases;
if equality holds, its side is a proper subset of `C`.  Both contradict
the assumed failure of outcome 1.  Therefore `Q_1={v}`, which is outcome
3. \(\square\)

## 6. Application to the coupled incident-edge response

In the bypass outcome of Proposition 3.1, let `Sigma_C` be the boundary
partition induced by the colouring of `G-wu`, which is legal on the
`C`-side and rejected by the intact `E`-side.  Lemma 2.1 gives

\[
                         d_B(\Sigma_C)\ge2.
\tag{6.1}
\]

If equality holds, Theorem 5.1 applies.  Thus the exact demand-two coupled
response returns a strict response-side descent, two vertex-disjoint
`Q_0`--`Q_1` edges, or a singleton nonowner adjacent to every vertex of
the old eight-set `S`.

The other one-edge partition, legal on `E` and rejected by `C`, also has
demand at least two.  The fact that the two partitions arise from one
simultaneous-contraction colouring does not by itself identify a Hall
witness with either switched bichromatic component.  The adjacent
[minimum tableau barrier](../barriers/hc7_order8_coupled_response_hall_tableau_barrier.md)
shows this failure already at boundary order nine and demand two.

The remaining host theorem must allocate the two disjoint cross edges, or
the singleton nonowner, into an additional connected subgraph meeting one
complete required boundary set; alternatively its failure must expose an
exact order-seven response side.  No colour has been identified with a
branch-set label in this proof.
