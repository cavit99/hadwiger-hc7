# Independent audit of the full-trace tight-cycle completion

## Verdict and audited revision

**Verdict: GREEN.**

This audit checks the complete source file
[`hc7_order9_full_trace_tight_cycle_completion.md`](hc7_order9_full_trace_tight_cycle_completion.md)
at SHA-256

```text
b697f94c6cb1b78968c41d4e3a4d87ab4f4baab21c4b230f31000b4a4f36e029
```

The final revision changes only the source status line to link this audit;
the audited mathematics is unchanged.  The six-colour boundary arithmetic, the equality characterization for a
tight shore vertex, the explicit seven-branch-set construction, and the
two-connected corollary are correct under the stated hypotheses.  In
particular, the construction does not assume that vertices belonging to
one repeated boundary colour are adjacent.

## 1. Boundary-colour arithmetic

The hypothesis says that the nine boundary vertices use **exactly** six
colours.  Thus the six colour classes `C_1,...,C_6` are all nonempty and

\[
              \sum_{i=1}^6 (|C_i|-1)=9-6=3.
\]

The possible unordered size patterns are

```text
4+1+1+1+1+1,
3+2+1+1+1+1,
2+2+2+1+1+1.
```

Their nonsingleton unions have orders four, five and six respectively.
Consequently the source's lower bound `|M|>=4` is sharp.  The explicit
exclusion of unused colours is essential here: with fewer than six used
colours, the total excess would not be three.  The source both assumes
exactly six colours and records the fewer-colour case outside its trust
boundary.

For a shore vertex `v`, put

\[
                   n_i=|N_G(v)\cap C_i|.
\]

Since `q(v)` counts exactly the indices with `n_i>0`, the identity

\[
 \rho(v)=|N_G(v)\cap B|-q(v)
        =\sum_{i:n_i>0}(n_i-1)
\]

is exact.  Term by term,

\[
 \sum_{i:n_i>0}(n_i-1)
       \le \sum_{i=1}^6(|C_i|-1)=3.
\]

If `v` is tight, the left internal-surplus term in (1.4) is zero, so
`rho(v)>=3`.  Hence equality holds in the displayed termwise bound.  For
every nonsingleton class `C_i`, omitting the class gives contribution zero
instead of `|C_i|-1>0`, and meeting it incompletely gives at most
`|C_i|-2`.  Either event would make the total strictly below three.
Therefore every tight vertex is adjacent to every literal vertex of every
nonsingleton class, exactly as Lemma 2.1 claims.

As an independent finite check of this equality case, all 56 ordered
compositions of nine into six positive class sizes were enumerated, along
with every possible vector `(n_1,...,n_6)` satisfying
`0<=n_i<=|C_i|`.  Every vector with `rho=3` contains each nonsingleton
class completely.

## 2. Extracting the two shore triangles

A cycle has a `K_3` minor: divide the cycle into three nonempty connected
arcs, retaining one cycle edge between each consecutive pair of arcs.
Thus cycles in `G[T_A]` and `G[T_D]` supply three pairwise disjoint
connected sets

\[
 A_1,A_2,A_3\subseteq T_A,
 \qquad
 D_1,D_2,D_3\subseteq T_D,
\]

with each triple pairwise adjacent.  Because the cycles lie in the induced
tight-vertex subgraphs, every vertex in each of these six sets satisfies
Lemma 2.1 and is adjacent to every vertex of `M`.

Lemma 2.1 gives four distinct literal vertices
`m_1,m_2,m_3,m_4 in M`.  They need not have distinct colours, and no edge
between two of them is required.  The sharp pattern
`4+1+1+1+1+1`, in which all four can belong to one independent colour
class, is therefore a valid adversarial test of the construction.

## 3. The seven branch sets

The seven proposed sets are

\[
 A_1,A_2,A_3,
 D_1\cup\{m_1\},D_2\cup\{m_2\},D_3\cup\{m_3\},
 \{m_4\}.
\]

They are disjoint because `A`, `B` and `D` are disjoint, the two shore
minor models have disjoint branch sets, and the four `m_i` are distinct.
Each enlarged `D_i` is connected because every vertex of `D_i` is tight
and hence adjacent to `m_i`.

Every required adjacency has a licensed literal edge:

- the `A_i` are pairwise adjacent through their `K_3` model;
- the enlarged `D_i` are pairwise adjacent through the original
  `D_i`--`D_j` model edges;
- `A_i` is adjacent to `D_j union {m_j}` through an edge from a tight
  vertex of `A_i` to `m_j`;
- `{m_4}` is adjacent to each `A_i` and each enlarged `D_j` through the
  corresponding tight shore vertices.

The standing anticompleteness of `A` and `D` causes no gap: all cross-shore
adjacencies are deliberately supplied by the boundary vertices `m_j`.
Likewise, no adjacency among the `m_i` is used.  These seven connected,
pairwise disjoint and pairwise adjacent sets are therefore an explicit
`K_7`-minor model.

## 4. Corollary and scope

The first conclusion of Corollary 3.2 is exactly the contrapositive of
Theorem 3.1.  Under the standard graph-theoretic convention, a
two-connected graph has at least three vertices and contains a cycle.  If
every vertex of both shore graphs is tight, then `T_A=A` and `T_D=D`, so
both required tight cycles exist and Theorem 3.1 applies.

The proof does not show that either tight-vertex subgraph contains a cycle
in every live order-nine endpoint.  It leaves precisely the cases stated
in the source: one tight subgraph may be a forest, or the cycles of a shore
may require non-tight vertices.  It also does not treat a boundary trace
using fewer than six colours and makes no identification between a colour
class and an inherited minor-model label.  Hence the result closes an
unbounded subfamily of the endpoint, not the entire order-nine branch or
`HC_7`.
