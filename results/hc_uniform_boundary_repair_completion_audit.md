# Internal audit of uniform boundary-repair completion

**Verdict:** **GREEN** for the exact source revision identified below.

## Audited revision and scope

- source: `results/hc_uniform_boundary_repair_completion.md`
- promoted source SHA-256:
  `34c3061f1ee8ed3026b6a168e58cf2ebdbb0e3aea86c6858b4b18a05b49a6b86`
- independently audited mathematical revision SHA-256:
  `77539e353e77eabc962accad99be5e89f96c9901db9d5a0f207da9ed78a0f4ef`

Promotion made two header-only changes before `## Theorem 1.1`: it replaced
the pending-audit status by a link to this GREEN audit and rewrapped the
sentence describing the theorem as the principle behind the shifted-boundary
construction.  I compared the promoted source from `## Theorem 1.1` onward
against the audited revision: the theorem statement, all six hypotheses,
proof, displayed formulae, and final remark are unchanged.  The mathematical
audit therefore applies without modification.

This is a separate internal mathematical audit, not external peer review.  It
checks the theorem as a self-contained conditional statement.  It does not
assert that its hypotheses arise in every hypothetical counterexample to
Hadwiger's conjecture.

## 1. Position of the selected roots and of `v`

Let `I` index the `q` branch sets missing `W=S-{s}`.  Hypothesis 5 puts
each entire branch set indexed by `I` inside the component `U`, so every
selected root `a_i` lies in `U` and outside `W`.

The unique model-support vertex in `V` is `v`.  Its branch set cannot be
indexed by `I`: if it missed `W`, hypothesis 5 would put that branch set
inside `U`, contradicting `v in V`.  Thus its branch set meets `W`, `v` is
not selected into `A_0`, and

\[
                         v\in Z.
\]

The old model lies in `G-s`, so `s` is not already in its support and its
addition to `Z` is disjoint.

## 2. Boundary and deletion counts

At least `q` support vertices lie outside `W`, namely the selected roots.
Since the full support has order at most `k-1`, at most `k-1-q` vertices
of `W` occur in it.  Therefore

\[
 |Z|\le (k-1-q)+1=k-q,
 \qquad
 |T|\ge k-(k-1-q)=q+1.
\]

The sets `A_0`, `T`, and `Z` are pairwise disjoint.  These estimates remain
valid if an anchored branch set meets several vertices of `W` or an
unanchored branch set contains more than its one selected root.

## 3. Menger's theorem and terminal conventions

Assume `q>0`.  If there are not `q` disjoint `A_0`--`T` paths in `G-Z`,
the vertex-set form of Menger's theorem gives a separating set `X` of order
at most `q-1`.  This is an actual separator of the host even when `X` is
allowed to contain terminal vertices:

- `|A_0|=q`, so `A_0-X` is nonempty;
- `|T|>=q+1`, so `T-X` is nonempty; and
- the two surviving terminal sets have no joining path in
  `G-(Z union X)`.

Its order is at most

\[
                  (k-q)+(q-1)=k-1,
\]

contradicting `k`-connectivity.  The required linkage therefore exists.

The `q=0` case is correctly separated from this argument.  Every branch set
already meets `W`; no empty-terminal application of Menger's theorem is
made.

## 4. First-hit paths and avoidance of the reserved component

There are `q` vertex-disjoint paths from a `q`-vertex set, so they use the
selected roots as distinct starts and no path can contain another selected
root.  Every other old model vertex belongs to `Z`.  Hence a path in
`G-Z` meets the old model only at its own start.

Stop each path at its first visit to `W`.  The first-hit vertex lies in
`T`, because every old support vertex in `W` is in `Z`.  The stopped paths
remain pairwise disjoint and have distinct first-hit vertices.

Before that hit, a path starting in `U` cannot reach `V-v`:

- distinct components `U,V` of `G-S` are anticomplete;
- `v` is in `Z`;
- `s` is in `Z`; and
- every other possible passage through the boundary meets `W`, where the
  path has already stopped.

Thus every stopped path avoids the specified component `C` of `V-v`.
The original model also avoids `C`, because its support meets `V` exactly
in `v`.  Enlarging the indexed rows consequently preserves connectivity,
pairwise disjointness, all old clique-model adjacencies, and disjointness
from both `C` and `{s}`.

## 5. The unused boundary vertex and the case `q=0`

The old support uses at most `k-1-q` vertices of `W`, and the stopped
linkage adds `q` distinct vertices from the previously unused set `T`.
Thus the enlarged model uses at most `k-1` of the `k` vertices of `W`, so
an unused vertex `z` exists.

When `q=0`, every old branch set already meets `W`, the support bound alone
shows that at most `k-1` vertices of `W` are used, and the same choice of
`z` is available.  The original model is disjoint from `C` and `{s}` by
hypotheses 3 and 4.  Therefore the final construction is equally valid in
this edge case.

## 6. Connectivity, disjointness, and all `K_k` adjacencies

The proposed sets

\[
       M'_1,\ldots,M'_{k-2},\quad C\mathbin\cup\{z\},\quad\{s\}
\]

are pairwise disjoint: the enlarged rows avoid `C` and `s`, while `z` was
chosen outside all of them.  They are connected because the old rows were
only enlarged by paths, `C` is connected and has a neighbour at `z`, and
the last set is a singleton.

Every required pair is witnessed as follows:

1. the `binom(k-2,2)` pairs among old rows retain the original
   `K_{k-2}`-model adjacencies;
2. for each of the `k-2` rows, choose a vertex of that row in `W`; boundary
   fullness of `C` gives the row--`C union {z}` adjacency;
3. the same boundary vertex is adjacent to `s`, giving the row--`{s}`
   adjacency; and
4. the edge `sz` joins the final two branch sets.

This accounts for

\[
 \binom{k-2}{2}+2(k-2)+1=\binom{k}{2}
\]

adjacencies.  No edge between `U` and `V`, and no adjacency from `v` to
`C`, is assumed.  The displayed sets therefore form a valid `K_k`-minor
model.

## 7. Falsification attempts and trust boundary

I tested the proof against the natural failure modes:

- `q=0` and `q=1`;
- maximum support order `k-1`;
- an unanchored branch set with several vertices;
- an anchored branch set meeting several boundary vertices;
- a Menger separator containing terminal vertices;
- a path attempting to enter `V-v` before its boundary hit; and
- the smallest parameter `k=3`.

The counts, the placement of `s,v` in `Z`, and the first-hit argument close
all of them.  I found no graph satisfying the six hypotheses while avoiding
the constructed `K_k` minor.  The theorem is a genuine all-`k` completion
principle, but its compact-support, one-support-vertex-in-`V`, and
unanchored-row placement hypotheses remain substantive.
