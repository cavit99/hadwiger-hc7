# A reserved path and two connected boundary-block subgraphs realize both root responses

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_three_block_linkage_reflection_audit.md`](hc7_order8_three_block_linkage_reflection_audit.md).
This is an unbounded colour-gluing theorem for the order-eight two-component
interface.  It does not prove `HC_7`.

## 1. Three-block and four-block contractions

### Theorem 1.1

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
 \qquad E_G(L,R)=\varnothing,
 \qquad L,R\ne\varnothing.                            \tag{1.1}
\]

Assume every proper minor of `G` is six-colourable.  Let `d,e` be
nonadjacent vertices of `S`, and let

\[
                         S-\{d,e\}=X\mathbin{\dot\cup}Y             \tag{1.2}
\]

be a bipartition of `G[S-\{d,e\}]`, with `X,Y` nonempty.  Assume that
each of `d,e` has a neighbour in each of `X,Y`, and that there is an edge
between `X` and `Y`.

Suppose that `R` contains three pairwise vertex-disjoint nonempty connected
subgraphs `D,C_X,C_Y` such that

1. `D` has a neighbour at both `d` and `e`;
2. `C_X` has a neighbour at every literal vertex of `X`; and
3. `C_Y` has a neighbour at every literal vertex of `Y`.

Then the closed shore `G[L\cup S]` has a proper six-colouring inducing the
exact boundary equality partition

\[
                              X\mid Y\mid\{d,e\}.       \tag{1.3}
\]

Suppose additionally that the vertex set of `D` is the disjoint union of
nonempty connected
subgraphs `D_d,D_e` such that `D_d,D_e` are adjacent, `D_d` has a neighbour
at `d`, and `D_e` has a neighbour at `e`.  Then the same closed shore also
has a proper six-colouring inducing

\[
                            X\mid Y\mid\{d\}\mid\{e\}. \tag{1.4}
\]

Consequently, if the opposite closed shore has a proper six-colouring
inducing either (1.3) or (1.4), then `G` is six-colourable.

#### Proof

For (1.3), contract spanning trees of the following three pairwise disjoint
connected sets:

\[
                         D\cup\{d,e\},\qquad
                         C_X\cup X,\qquad
                         C_Y\cup Y.                    \tag{1.5}
\]

Each set contains an edge, so the simultaneous contraction gives a proper
minor.  The three images form a triangle: the root image is adjacent to
both block images through the boundary neighbours of `d` in `X,Y`, and
the two block images are adjacent through the assumed `X`--`Y` edge.

Six-colour the minor and restrict to `G[L\cup S]`.  Expanding the three
images over the boundary produces (1.3).  Its blocks are independent, and
every edge from `L` to a contracted block was represented by an edge to its
image, so the expanded colouring is proper.

For (1.4), instead contract spanning trees of the four pairwise disjoint
connected sets

\[
 D_d\cup\{d\},\qquad D_e\cup\{e\},\qquad
 C_X\cup X,\qquad C_Y\cup Y.                          \tag{1.6}
\]

Their images form a `K_4`.  The two root images are adjacent through the
edge between `D_d,D_e`; each root image is adjacent to each block image
through the assumed boundary neighbours of `d,e` in both bipartition
classes; and the two block images are adjacent through the `X`--`Y` edge.
Every set in (1.6) contains an edge, so this too is a proper minor.

A six-colouring of this minor restricts and expands to (1.4) on the closed
`L`-shore, by the same edge-preservation argument.  Finally, whenever one
of (1.3), (1.4) also occurs on the opposite shore, permute the six colour
names there to align the displayed blocks.  The open shores are
anticomplete, so the colourings glue. \(\square\)

## 2. A reserved Two Paths instance

For a boundary vertex `s` and a connected subgraph `Q` disjoint from `S`,
write

\[
                            P_s(Q)=N_G(s)\cap V(Q).     \tag{2.1}
\]

### Corollary 2.1

Retain the boundary hypotheses of Theorem 1.1.  Suppose `R` contains two
vertex-disjoint connected subgraphs `Q_0,Q_1`, each adjacent to every
vertex of `S`, and let `X=\{x_0,x_1\}`.  If, for some `i in \{0,1\}`,
the graph `G[Q_i]` contains two vertex-disjoint paths such that

1. one is a nontrivial path joining a vertex of `P_d(Q_i)` to a distinct
   vertex of `P_e(Q_i)`; and
2. the other joins `P_{x_0}(Q_i)` to `P_{x_1}(Q_i)`,

then `G[L\cup S]` has proper six-colourings inducing both (1.3) and (1.4).

#### Proof

Let `D` be the first path and `C_X` the second, and take
`C_Y=Q_{1-i}`.  They are pairwise disjoint, connected, and have all
contacts required for (1.3).

Write the first path as

\[
                         q_0q_1\cdots q_k,\qquad k\ge1,             \tag{2.2}
\]

where `q_0` is adjacent to `d` and `q_k` is adjacent to `e`.  Split it at
any edge `q_tq_{t+1}`.  The prefix and suffix are nonempty adjacent
connected subgraphs satisfying the extra hypotheses for (1.4).  Apply
Theorem 1.1 twice. \(\square\)

The portal sets in Corollary 2.1 need not themselves be disjoint.  The two
selected paths, including their ends, must be vertex-disjoint, and the
root path must have distinct ends.

### Corollary 2.2

The conclusion of Corollary 2.1 remains valid for arbitrary nonempty `X`
if `G[Q_i]` contains a nontrivial path joining `P_d(Q_i)` to `P_e(Q_i)`
and, disjoint from that path, a connected subgraph meeting every portal set

\[
                              P_x(Q_i),\qquad x\in X.   \tag{2.3}
\]

#### Proof

Use the root path as `D`, the connected subgraph in (2.3) as `C_X`, and
the other boundary-full subgraph as `C_Y`; then split `D` at any path edge
for the four-block contraction. \(\square\)

## 3. Application to opposite responses

In the setting of the audited opposite-response theorem, assume in addition
the edge hypothesis `E_G(X,Y) nonempty` from Theorem 1.1.  The two physical
shore response sets are nonempty, regardless of which type belongs to the
shore containing `Q_0,Q_1`.  Corollary 2.1 or 2.2 would realize **both**
types on the opposite closed shore.  One of them therefore agrees with a
type on the `Q_0,Q_1` shore, and the two colourings glue.  Thus neither
reserved-linkage configuration can occur in a counterexample.

For a bipartition with a class of order two, each of the two named
boundary-full connected subgraphs is consequently a set-terminal instance
of the classical Two Paths obstruction: it has no pair of disjoint paths
joining the root portal sets and the two portals of that class, with a
nontrivial root path.  This is a literal host reduction.  It does not infer
a path from an abstract quotient edge or identify a colour with a
branch-set label.

## 4. Trust boundary

The theorem closes every positive reserved-linkage instance in either
orientation of the opposite responses.  It does not eliminate the
corresponding crossless web, prove that a web exposes an order-seven
separation, or handle a three-vertex bipartition class without the connected
subgraph in (2.3).  Those are the remaining host-level obligations in the
two-component residue.

No finite boundary census is used in the proof.  The exact quotient probe
shows only that 66 of its 124 static survivor pairs admit a bipartition
whose smaller class has order two; that finite count is motivation for
Corollary 2.1, not a hypothesis or an unbounded conclusion.

## 5. Dependencies

- proper-minor six-colourability from minor minimality;
- the [opposite-response theorem](hc7_order8_independent_oct_opposite_response.md),
  only for the application in Section 3;
- the classical Two Paths theorem only as a description of the remaining
  negative case, not as an input to Theorem 1.1 or its corollaries.
