# Cycle completion from two connected shores

**Status:** written proof; separate internal audit GREEN in
[`hc7_adjacent_full_pair_cycle_completion_audit.md`](hc7_adjacent_full_pair_cycle_completion_audit.md).
This is a reusable branch-set construction.  It does not prove `HC_7`.

The previous audited revision assumed that two connected subgraphs on one
shore were already adjacent and had exact one-vertex boundary defects.  The
argument below removes both restrictions: connectedness of that shore makes
the two subgraphs adjacent after absorbing a shortest path, and only lower
bounds on their boundary contacts are used.  This is a material revision, so
the adjacent audit applies only to the previous revision until this statement
is re-audited.

## 1. Setting

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
 \qquad |S|=8,
\]

where `G[L]` and `G[R]` are connected.  Let `d,e` be distinct vertices of
`S`.

Suppose that `G[L]` contains vertex-disjoint connected subgraphs `A_d,A_e`
such that

\[
 S-\{d\}\subseteq N_G(A_d)\cap S,
 \qquad
 S-\{e\}\subseteq N_G(A_e)\cap S.                    \tag{1.1}
\]

No restriction is imposed on whether `A_d` is adjacent to `d` or `A_e` is
adjacent to `e`.

Suppose also that `G[R]` contains vertex-disjoint nonempty connected
subgraphs `Q_0,Q_1`, each adjacent to every literal vertex of `S`.

## 2. Adjacent connected normal form

### Lemma 2.1

There is a partition

\[
                         R=P_0\mathbin{\dot\cup}P_1                  \tag{2.1}
\]

such that each `G[P_i]` is connected and adjacent to every vertex of `S`,
and there is a `P_0`--`P_1` edge.

There are also vertex-disjoint connected subgraphs
`\widehat A_d,\widehat A_e` of `G[L]` satisfying (1.1) in place of
`A_d,A_e` and having an edge between them.

#### Proof

Apply Lemma 1.1 of the audited connected-rich width-two frontier to
`G[R]` and the two subgraphs `Q_0,Q_1`.  It gives (2.1), with each part
containing one of the original boundary-full connected subgraphs, and a
cross-edge.  Hence both parts remain adjacent to every boundary vertex.

For the second assertion, choose a shortest path

\[
                         v_0v_1\ldots v_k
\]

in `G[L]` from `V(A_d)` to `V(A_e)`.  Its internal vertices lie outside
both original subgraphs.  Absorb all of them into `A_d`: let
`\widehat A_d` be the connected subgraph consisting of `A_d`, the internal
vertices of the path, and the corresponding path edges, and put
`\widehat A_e=A_e`.  The two resulting subgraphs are vertex-disjoint and
connected.  The last edge of the path joins them.  Enlarging `A_d` cannot
destroy any boundary contact in (1.1), while `A_e` is unchanged. \(\square\)

## 3. Cycle completion

### Theorem 3.1

If `G[S-{d,e}]` contains a cycle, then `G` contains a `K_7` minor.

#### Proof

Use Lemma 2.1 to fix `P_0,P_1,\widehat A_d,\widehat A_e`.  Let `C` be a
cycle in `G[S-{d,e}]`.  Partition its cyclic order into three nonempty
consecutive arcs, and denote their vertex sets by `M_1,M_2,M_3`.  Each
`G[M_i]` is connected, and the three sets are pairwise adjacent through
the three transition edges of the cycle.

Consider the following seven vertex sets:

\[
 P_0,\quad P_1,\quad
 V(\widehat A_d)\cup\{e\},\quad
 V(\widehat A_e)\cup\{d\},\quad
 M_1,\quad M_2,\quad M_3.                            \tag{3.1}
\]

They are pairwise disjoint.  They are connected because `P_0,P_1` and the
three arcs are connected, while (1.1) supplies an edge from `e` to
`\widehat A_d` and an edge from `d` to `\widehat A_e`.

We check every required adjacency.

- `P_0` and `P_1` are adjacent by Lemma 2.1.
- Each `P_j` is adjacent to the third set in (3.1) through its contact at
  `e`, and to the fourth through its contact at `d`.
- Boundary fullness makes each `P_j` adjacent to each nonempty `M_i`.
- The third and fourth sets are adjacent through the edge between
  `\widehat A_d` and `\widehat A_e`.
- Every cycle vertex lies in `S-{d,e}`.  Thus (1.1) makes each of
  `\widehat A_d,\widehat A_e` adjacent to every `M_i`.
- The three arc sets are pairwise adjacent through the transition edges of
  `C`.

Thus (3.1) is an explicit `K_7`-minor model in `G`. \(\square\)

### Corollary 3.2 (forest normalization)

If `G` has no `K_7` minor, then `G[S-{d,e}]` is a forest.

In particular, this applies to the live connected two-component
opposite-response interface: the merged-response component supplies
`A_d,A_e`, and the connected split-response component contains two
disjoint boundary-full connected subgraphs.  The response orientation is
not used in the proof.

### Lemma 3.3 (the `(3,5)` boundary type)

If `G[S]` contains two vertex-disjoint odd cycles, one of order three and
one of order five, then `G` contains a `K_7` minor.

#### Proof

Otherwise Corollary 3.2 implies that the two cycles contain `d,e`, one
root each.  By symmetry let the five-cycle `C` contain `d`, and let the
triangle contain `e`.  Choose a non-root vertex `t` of that triangle.
Partition `C` into three nonempty consecutive arcs `M_1,M_2,M_3`, choosing
the partition so that `d in M_1` and `|M_1|>=2`.

Use the seven branch sets

\[
 P_0,\quad P_1,\quad
 V(\widehat A_d)\cup\{e\},\quad
 V(\widehat A_e)\cup\{t\},\quad
 M_1,\quad M_2,\quad M_3.                            \tag{3.2}
\]

They are disjoint and connected.  The boundary vertices `e,t` make both
of the third and fourth branch sets adjacent to both `P_0,P_1`, while the
edge between `\widehat A_d,\widehat A_e` makes those two branch sets
adjacent.  Boundary fullness makes each `P_j` adjacent to every cycle arc.
The subgraph `\widehat A_e` is adjacent to every cycle vertex because `C`
avoids `e`.  The subgraph `\widehat A_d` is adjacent to every arc not
containing `d`, and it is adjacent to `M_1` through its second vertex.
Finally the three arc sets are pairwise adjacent through the transition
edges of `C`.  Thus (3.2) is a `K_7`-minor model. \(\square\)

### Lemma 3.4 (an extra neighbour of a rooted triangle)

Suppose `dxy` is a triangle in `G[S]`, with `e` outside that triangle.  If
`d` has a neighbour `w in S-{d,x,y}`, then `G` contains a `K_7` minor.
The same holds with `d,e` interchanged.

#### Proof

First suppose \(w\ne e\).  Choose
\(t\in S-\{d,e,w,x,y\}\).  The seven branch sets are

\[
 P_0,\quad P_1,\quad
 V(\widehat A_d)\cup\{e\},\quad
 V(\widehat A_e)\cup\{t\},\quad
 \{d,w\},\quad\{x\},\quad\{y\}.                    \tag{3.3}
\]

They are disjoint and connected.  The three boundary sets are pairwise
adjacent through `dx,dy,xy`.  The subgraph `\widehat A_d` sees the first
boundary set through `w`, and sees `x,y`; `\widehat A_e` sees the first
boundary set through `d`, and also sees `x,y`.  The two enlarged subgraphs
are adjacent through the edge between their off-boundary parts.  Each
`P_j` sees them through `e,t`, respectively, and sees all three boundary
sets by boundary fullness.  Thus (3.3) is a `K_7`-minor model.

It remains to consider \(w=e\), so `de` is an edge.  Choose distinct
\(a,b\in S-\{d,e,x,y\}\) and instead use

\[
 P_0,\quad P_1,\quad
 V(\widehat A_d)\cup\{a\},\quad
 V(\widehat A_e)\cup\{b\},\quad
 \{d,e\},\quad\{x\},\quad\{y\}.                    \tag{3.4}
\]

The same check applies: `a,b` fund the adjacencies from the first two
off-boundary branch sets to `P_0,P_1`; each off-boundary subgraph sees all
three boundary sets; and `de,dx,dy,xy` give all adjacencies among the last
three sets.  Hence (3.4) is a `K_7`-minor model. \(\square\)

### Corollary 3.5 (two rooted odd cycles)

Assume additionally that `G[S]` contains two vertex-disjoint odd cycles and
that `G` has no `K_7` minor.  Then the two cycles are triangles, one
containing `d` and the other containing `e`.  Moreover,

\[
                         d_{G[S]}(d)=d_{G[S]}(e)=2.                 \tag{3.5}
\]

Consequently the `(3,5)` odd-cycle boundary type is eliminated.

#### Proof

By Corollary 3.2, each odd cycle must meet `{d,e}`.  Vertex disjointness
forces the roots to occur one per cycle.  The only possible orders for two
disjoint odd cycles on eight vertices are `(3,3)` and `(3,5)`.  Lemma 3.3
excludes the latter, so both are triangles.  Each root has its two triangle
neighbours.  Any further boundary neighbour contradicts Lemma 3.4, proving
(3.5). \(\square\)

Equivalently, the remaining `(3,3)` boundary consists of two disjoint
rooted triangles whose roots have no other boundary neighbours, together
with a forest on the six non-root boundary vertices containing the two
opposite triangle edges.

## 4. Exact gain and trust boundary

The theorem eliminates every cycle in `G[S-{d,e}]` in the connected
two-component opposite-response interface, for arbitrary shore sizes and
without using a colouring or finite boundary classification.  Rooted
triangles in `G[S]` may remain.  Exact
one-vertex defects are unnecessary: additional boundary contacts acquired
when the shortest path is absorbed only strengthen the minor construction.

The result does not eliminate the normalized two-triangle forest case.  In
particular, two root triangles may leave two independent edges in
`G[S-{d,e}]`, with two further boundary vertices unused.  The theorem also
does not produce a common boundary equality partition, an order-seven
separation, or a label-preserving strict descent.  Those remain separate
obligations in the live branch.

Connectedness of both shores is used essentially by the proof: it supplies
the adjacent boundary-full cover on `R` and the path joining `A_d` to
`A_e` on `L`.

## 5. Dependency

- [Lemma 1.1 of the connected-rich width-two frontier](hc7_exact7_connected_rich_width2_frontier.md),
  for the adjacent connected cover of `R`.
