# Completing a compact clique model across an order-`k` boundary

**Status:** written proof with a separate GREEN internal audit in
[`hc_uniform_boundary_repair_completion_audit.md`](hc_uniform_boundary_repair_completion_audit.md).
This theorem is the uniform principle behind the final shifted-boundary
construction in
[`hc7_shifted_boundary_completion.md`](hc7_shifted_boundary_completion.md).
It is stated independently of `HC_7` and of the special eight-vertex
boundary graph.

## Theorem 1.1

Let `k>=3`, let `G` be a `k`-connected graph, and let `S` be a set of `k`
vertices.  Suppose:

1. `s in S` is adjacent to every vertex of `S-{s}`;
2. `G-S` has distinct components `U,V`;
3. `M` is a `K_{k-2}`-minor model in `G-s`, supported on at most `k-1`
   vertices;
4. for some vertex `v in V`, the model support meets `V` exactly in `v`;
5. every branch set of `M` which is disjoint from `S-{s}` is contained in
   `U`; and
6. some component `C` of `V-v` has a neighbour at every vertex of
   `S-{s}`.

Then `G` contains a `K_k` minor.

## Proof

Put `W=S-{s}`, so `|W|=k-1`.  Write the branch sets of `M` as

\[
                         M_1,\ldots,M_{k-2}.
\]

Let

\[
 I=\{i:M_i\cap W=\varnothing\},\qquad q=|I|,
\]

and choose one vertex `a_i in M_i` for every `i in I`.  Hypothesis 5 puts
all these vertices in `U`.  Define

\[
 A_0=\{a_i:i\in I\},\qquad
 Z=\left(\bigcup_{i=1}^{k-2}M_i-A_0\right)\cup\{s\},
 \qquad
 T=W-\bigcup_{i=1}^{k-2}M_i.                         \tag{1.1}
\]

The branch set containing `v` meets `W`: otherwise it would be disjoint
from `W` but would not lie in `U`, contrary to hypothesis 5.  In particular,
`v` is not one of the selected vertices in `A_0`, and `v in Z`.

The `q` selected vertices and `v` are `q+1` distinct support vertices
outside `W`.  Since the support has order at most `k-1`,

\[
 \left|W\cap\bigcup_iM_i\right|\le k-2-q,
 \qquad |T|\ge q+1.                                  \tag{1.2}
\]

The support bound also gives

\[
                              |Z|\le k-q.             \tag{1.3}
\]

Suppose first that `q>0`.  There are `q` pairwise vertex-disjoint
`A_0`--`T` paths in `G-Z`.  Otherwise the vertex form of Menger's theorem
gives an `A_0`--`T` separator `X` in `G-Z` with `|X|<=q-1`.  Both terminal
sets retain a vertex after deleting `X`, by `|A_0|=q` and (1.2), whereas

\[
                              |Z\cup X|\le k-1.
\]

This contradicts `k`-connectivity.

Shorten the paths so that each starts at its unique vertex of `A_0`, and
stop each path at its first visit to `W`.  That first boundary vertex lies
in `T`, since every vertex of the old model in `W` belongs to `Z`.  No
stopped path meets `V-v`: it starts in `U`; the distinct components `U,V`
of `G-S` are anticomplete; both `s` and `v` lie in `Z`; and every remaining
passage through `S` first meets `W`, where the path has already stopped.

For each `i in I`, enlarge `M_i` along its corresponding stopped path.  The
result is still a `K_{k-2}`-minor model, is disjoint from `C` and from `s`,
and every branch set now meets `W`.  By (1.2), its branch sets use at most

\[
                              (k-2-q)+q=k-2
\]

vertices of `W`.  Thus some vertex `z in W` remains unused.

If `q=0`, every branch set already meets `W`.  The vertex `v` is a support
vertex outside `W`, so the support bound shows directly that the model uses
at most `k-2` vertices of `W`; again choose an unused `z in W`.  The model
is disjoint from `C` by hypothesis 4.

In either case, denote the resulting branch sets by
`M'_1,...,M'_{k-2}`.  The following `k` sets are pairwise disjoint and
connected:

\[
      M'_1,\ldots,M'_{k-2},\qquad C\cup\{z\},\qquad\{s\}.       \tag{1.4}
\]

The first `k-2` sets retain the clique-model adjacencies.  Each `M'_i`
contains a vertex of `W`; the fullness of `C` and the universality of `s`
therefore make both of the last two sets adjacent to every `M'_i`.  Finally,
`C` has a neighbour at `z`, so `C\cup\{z\}` is connected, and the edge
`sz` joins the last two sets.  Hence (1.4) is a `K_k`-minor model.
\(\square\)

## Remark 1.2 (the spare boundary vertex)

The count uses more than the support-order bound alone.  In addition to
the `q` selected roots in `U`, the unique model vertex `v in V` lies outside
`W`.  These are `q+1` distinct support vertices outside `W`.  Consequently
the old model uses at most `k-2-q` vertices of `W`; after the `q` anchoring
paths are added, one vertex of the order-`k-1` set `W` remains available.

The edge cases are included in the proof.  For `q=0`, the vertex `v`
supplies the spare count without a linkage.  For `q=1`, `|T|>=2` and a
failed single path makes `Z` a cut of order at most `k-1`.  For `k=3`, the
sole branch set contains `v` and therefore cannot be `W`-disjoint under
hypothesis 5, so `q=0`.

The order-`k` boundary is the smallest one for which this particular
construction is guaranteed to leave a boundary vertex joining `C` to the
singleton branch set `{s}`.
