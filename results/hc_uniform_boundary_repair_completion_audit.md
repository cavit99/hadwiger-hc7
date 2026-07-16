# Internal audit of compact-model completion across an order-`k` boundary

**Verdict:** **GREEN** for the exact source revision identified below.

## Audited revision and scope

- source: `results/hc_uniform_boundary_repair_completion.md`
- source SHA-256:
  `1e653c1d36a603b22e89a2b3bc0cbcbd523de3eb14ce8b53d4765e8cdd68eade`
- independently audited draft SHA-256:
  `5b400c268f7687c7464f032f5707b59cf7b4a977e658b87116dad6ef67b5f40a`

The independently audited draft was promoted with editorial changes only:
the title and status material were revised, theorem and equation numbers were
added, and the already audited edge-case discussion was collected into
Remark 1.2.  The six hypotheses, counting inequalities, Menger argument,
first-hit construction, component-avoidance argument, edge cases, and final
minor model are mathematically unchanged.  The auditor compared the promoted
source with the draft and rebound this verdict to the exact promoted hash.

This is a separate internal mathematical audit, not external peer review.
It checks the theorem as a self-contained conditional statement.  It does
not assert that its hypotheses arise in every hypothetical counterexample to
Hadwiger's conjecture.

## 1. Boundary count

Let `q` be the number of model branch sets missing
`W=S-{s}`.  Hypothesis 5 puts one selected vertex from each such branch set
in `U`.  The unique support vertex `v in V` is distinct from those `q`
vertices.  Its branch set must meet `W`, since a `W`-disjoint branch set
would lie in `U` by hypothesis 5.  Hence `v in Z`, and there are `q+1`
distinct support vertices outside `W`.

The support-order bound therefore gives

\[
 \left|W\cap\bigcup_iM_i\right|\le k-2-q,
 \qquad |T|\ge q+1,
 \qquad |Z|\le k-q.                                  \tag{A.1}
\]

This is the extra count which permits the boundary to have order `k`
rather than `k+1`.

## 2. Menger linkage and first hits

For `q>0`, failure of `q` disjoint `A_0`--`T` paths in `G-Z` gives a
separator `X` of order at most `q-1`.  Both terminal sets retain a vertex,
whereas

\[
                         |Z\cup X|\le k-1,
\]

contradicting `k`-connectivity.  Thus the linkage exists.

The paths may be shortened to start at their distinct selected roots and
stopped at their first visits to `W`.  Every other old model vertex is in
`Z`, so each path meets the model only at its own root and its first boundary
vertex lies in `T`.  Before that first hit a path starting in `U` cannot
enter `V-v`: the components `U,V` of `G-S` are anticomplete, while `s,v`
belong to `Z`.  Hence all stopped paths avoid the reserved component `C`.

## 3. Spare boundary vertex and edge cases

After the `q` paths are added, the model uses at most

\[
                         (k-2-q)+q=k-2
\]

vertices of the order-`k-1` set `W`, leaving an unused vertex `z`.

- For `q=0`, the support vertex `v` outside `W` gives the spare count
  directly; no empty-terminal application of Menger's theorem is made.
- For `q=1`, (A.1) gives `|T|>=2`, and a failed single path would make `Z`
  a cut of order at most `k-1`.
- For `k=3`, the sole branch set contains `v` and cannot be `W`-disjoint
  under hypothesis 5, so `q=0`.

## 4. Final branch-set audit

The sets

\[
       M'_1,\ldots,M'_{k-2},\quad C\cup\{z\},\quad\{s\}
\]

are pairwise disjoint and connected.  The first `k-2` retain their old
clique-model adjacencies.  Every old row now contains a vertex of `W`, so
the fullness of `C` and universality of `s` give both required adjacencies
from that row.  The set `C\cup\{z\}` is connected through a `C-z` edge,
and `sz` joins the last two branch sets.  This accounts for every edge of
the claimed `K_k` minor model.

No hidden intersection with `C`, empty-terminal case, or missing adjacency
was found.  The theorem is a genuine all-`k` strengthening; its compact
support and one-support-vertex placement hypotheses remain substantive.
