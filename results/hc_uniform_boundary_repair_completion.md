# Completing a compact clique model with one full component and one universal boundary vertex

**Status:** written proof with a separate GREEN internal audit in
[`hc_uniform_boundary_repair_completion_audit.md`](hc_uniform_boundary_repair_completion_audit.md).
This theorem is the uniform principle behind the final shifted-boundary
construction in
[`hc7_shifted_boundary_completion.md`](hc7_shifted_boundary_completion.md).
It is stated independently of `HC_7` and of the special eight-vertex
boundary graph.

## Theorem 1.1

Let `k>=3`, let `G` be a `k`-connected graph, and let `S` be a set of
`k+1` vertices.  Suppose:

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

Put

\[
                             W=S-\{s\}.
\]

Thus `|W|=k`.  Write the branch sets of `M` as

\[
                         M_1,\ldots,M_{k-2},
\]

let

\[
        I=\{i:M_i\cap W=\varnothing\},\qquad q=|I|,
\]

and choose one vertex `a_i in M_i` for each `i in I`.  Hypothesis 5 says
that every such selected vertex lies in `U`.  Put

\[
 A_0=\{a_i:i\in I\},\qquad
 Z=\left(\bigcup_{i=1}^{k-2}M_i-A_0\right)\cup\{s\},
 \qquad
 T=W-\bigcup_{i=1}^{k-2}M_i.                         \tag{1.1}
\]

The model branch set containing `v` meets `W`: otherwise it would be a
branch set disjoint from `W` but not contained in `U`, contrary to
hypothesis 5.  Hence `v` belongs to `Z`.

The support bound gives

\[
                              |Z|\le k-q.              \tag{1.2}
\]

At most `k-1-q` boundary vertices of `W` belong to the model support, so

\[
                              |T|\ge q+1.              \tag{1.3}
\]

Assume first that `q>0`.  There are `q` pairwise vertex-disjoint
`A_0`--`T` paths in `G-Z`.  Otherwise Menger's theorem gives an
`A_0`--`T` separator `X` in `G-Z` with `|X|<=q-1`.  Since
`|A_0|=q` and `|T|>=q+1`, both terminal sets retain a vertex after deleting
`X`, while

\[
                              |Z\cup X|\le k-1,
\]

contrary to `k`-connectivity.

Choose such a linkage, shorten its paths so that each contains exactly one
vertex of `A_0`, and stop every path on its first visit to `W`.  Its first
boundary vertex lies in `T`, since every vertex of `W` already in the
model belongs to `Z`.

No stopped path meets `V-v`.  It starts in `U`; distinct components of
`G-S` have no edge between them; the vertices `s` and `v` belong to `Z`;
and every possible remaining passage from `U` into `V` first visits a
vertex of `W`, where the path has already stopped.

Enlarge each `M_i`, for `i in I`, along its corresponding stopped path.
The resulting `K_{k-2}` model is disjoint from `C` and from `s`, and every
branch set now contains a vertex of `W`.  The number of used boundary
vertices is at most

\[
     |W\cap\bigcup_iM_i|+q\le(k-1-q)+q=k-1.
\]

Choose an unused vertex

\[
                              z\in W.                  \tag{1.4}
\]

If `q=0`, all branch sets already meet `W`, and the support bound again
leaves an unused vertex `z`; no linkage is needed.

Denote the resulting branch sets by `M'_1,...,M'_{k-2}`.  The following
`k` sets are connected and pairwise disjoint:

\[
      M'_1,\ldots,M'_{k-2},\qquad C\cup\{z\},\qquad\{s\}.
                                                               \tag{1.5}
\]

They are pairwise adjacent for the following reasons.

- The first `k-2` sets retain all adjacencies of the original clique-minor
  model.
- The component `C` has a neighbour at every vertex of `W`; hence it is
  adjacent to each `M'_i` through a boundary vertex in that branch set, and
  `C\cup\{z\}` is connected.
- The vertex `s` is adjacent to each `M'_i` through the same boundary
  vertices, because `s` is adjacent to every vertex of `W`.
- The edge `sz` joins the last two sets.

Thus (1.5) is a `K_k`-minor model. \(\square\)

## Remark 1.2 (why the hypotheses have this form)

The only purpose of hypotheses 2, 4, and 5 is to keep the anchoring paths
out of `C`: the sole model vertex in `V` is deleted in `Z`, the universal
vertex `s` is also deleted, and an anchoring path is stopped when it first
reaches `W`.  A formally weaker version may replace those three hypotheses
by the direct assertion that the required disjoint anchoring paths can be
chosen outside `C`, but that formulation hides the connectivity argument
which makes the theorem useful.

The support bound `k-1` and boundary order `k` are sharp for this proof:
after anchoring the `k-2` old branch sets, one unused boundary vertex is
needed to join `C` to the singleton branch set `\{s\}`.
