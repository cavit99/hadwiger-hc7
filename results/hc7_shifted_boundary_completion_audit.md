# Internal audit of shifted-boundary clique-model completion

**Verdict:** **GREEN** for the exact source revision identified below.

## Audited revision and scope

- source: `results/hc7_shifted_boundary_completion.md`
- promoted source SHA-256:
  `48c64a946f48a9a2f838b152efd4a108f25a28c62341f0310155b1ba7eab6ad1`
- independently audited mathematical revision SHA-256:
  `a6be042ca80c7de65901eb39a007fc4991c78bdbe259b0ddb9aa46b724efac8e`

The promoted source differs from the independently audited revision only in
its status paragraph: the pending-audit wording was replaced by a link to
this GREEN audit, and the description of the closed branch was made explicitly
conditional.  Replacing the promoted status paragraph by the pre-promotion
paragraph reproduces the audited mathematical hash exactly.  The theorem
statements, hypotheses, proofs, and corollary are byte-for-byte unchanged.

After promotion, the setup link in Section 2 was retargeted from the former
active frontier to its archived closed-branch copy.  Replacing that one link
in the current source reproduces the preceding promoted source hash
`16957a20d72a20759d721e3b3c339fb203f884d378fff47f618d47a5200dbc22`
exactly.  This navigation-only update changes no mathematical text.

This is a separate internal mathematical audit, not external peer review.  It
checks the uniform theorem and all three `HC_7` consequences, including the
new completion when the common missed boundary vertex is `s`.  It treats the
endpoint-rigid mixed-shore configuration quoted in Section 2 as an input; it
does not reaudit the earlier results that produce that configuration.

## 1. Uniform theorem: counting and Menger's theorem

Let `q` be the number of old branch sets that avoid the boundary `S`, and
retain one selected vertex from each of them.  The selected vertices lie
outside `S`.  Deleting every other model vertex therefore gives

\[
 |Z|\le k-1-q.
\]

At least `q` support vertices lie outside `S`, one in each unanchored branch
set.  Hence at most `k-1-q` vertices of `S` lie in the old support, and the
unused boundary set has order at least

\[
 (k+1)-(k-1-q)=q+2.
\]

The sets `A_0`, `T`, and `Z` are pairwise disjoint.  If fewer than `q`
disjoint `A_0`--`T` paths exist in `G-Z`, set-Menger gives an
`A_0`--`T` separator `X` of order at most `q-1`.  This remains valid when
the separator is permitted to contain terminals: `|A_0|=q` and
`|T|>=q+2`, so both terminal sets retain a vertex.  The two surviving
terminal vertices lie in different components of

\[
 G-(Z\mathbin\cup X),\qquad
 |Z\mathbin\cup X|\le(k-1-q)+(q-1)=k-2,
\]

contradicting `k`-connectivity.  Thus the linkage exists.  The case `q=0`
correctly bypasses this argument.

## 2. Uniform theorem: stopping and enlarging the branch sets

The `q` disjoint paths use all `q` members of `A_0` as distinct starts.
Consequently no path can contain another selected vertex belonging to a
different path.  Every other old model vertex is in `Z`, so a path in
`G-Z` meets the old model only at its own start.

Stopping a path at its first visit to `S` preserves pairwise disjointness.
That first boundary vertex belongs to `T`, since every old support vertex
in `S` was put in `Z`.  Before this visit the path stays in the component
of `G-S` containing its selected start.  An unanchored branch set is
connected and avoids `S`, so it lies wholly in that component.  Because
the original model avoids the two reserved components `C_1,C_2`, the
stopped path avoids them as well.

Adjoining each stopped path to its corresponding branch set therefore
preserves connectivity, disjointness, all old model adjacencies, and every
branch-set label.  The new boundary endpoints are distinct.  The old
support used at most `k-1-q` boundary vertices and the linkage adds `q`, so
at most `k-1` vertices of the `(k+1)`-set `S` are used.  Two unused vertices
`z_1,z_2` exist.

For completeness, all new adjacencies in the claimed `K_k` model are
valid:

- each `C_j union {z_j}` is connected by boundary fullness;
- it is adjacent to every old branch set through a boundary vertex in that
  branch set; and
- the last two branch sets are adjacent because `C_1` has a neighbour at
  `z_2` (equivalently, `C_2` has a neighbour at `z_1`).

Thus Theorem 1.1 is valid.  No hidden assumption that the old branch sets
meet `S` in exactly one vertex is used.

## 3. Theorem 2.1: two components on the shifted side

The shifted boundary

\[
 T=\{v\}\mathbin\cup(S-\{y\})
\]

has order eight.  A component of `V-v` has no edge to `U`, to another
component of `V-v`, or to `y`; all its other possible external neighbours
belong to `T`.  Hence distinct components of `V-v` are indeed distinct
components of `G-T`, not merely relative pieces of a shore.  Each is
adjacent to every vertex of `T` by the input contact equality.

The old five-branch-set model avoids every component of `V-v`, has support
order six, and is a `K_5` model in the graph obtained after deleting any
two selected components.  These are exactly Theorem 1.1's hypotheses with
`k=7`.  The conclusion that two such components give a `K_7` minor is
therefore valid, so the minor-free residue has `V-v` connected.

## 4. Theorem 2.2: anchoring on `W=S-{s,y}`

When `y!=s`, the established list of possible missed vertices makes `y`
one of the singleton branch vertices `w_j`.  The six-set

\[
 W=S-\{s,y\}
\]

is the correct safe anchoring set.  In the exact support-six model, the
unanchored branch sets are the `h` singleton sets in `U` and `{y}`, so
`q=h+1`.  The branch set `{v,t}` is anchored because `t` is distinct from
`s,y` and belongs to `W`.

For the proof's more invariant notation, retaining one vertex from every
unanchored branch set gives

\[
 |Z|=|M-A_0|+1=7-q.
\]

Every old model vertex in `W` lies in `M-A_0`, and hence

\[
 |T_0|=|W-M|\ge 6-(6-q)=q.
\]

Failure of `q` disjoint `A_0`--`T_0` paths in `G-Z` would give a separator
of order at most `q-1`.  Since both terminal sets have order at least `q`,
both retain a vertex, while the total deleted set has order at most

\[
 (7-q)+(q-1)=6,
\]

contradicting seven-connectivity.  The endpoint count is therefore sharp
and correct.

The stopped paths cannot enter `V-v`.  They start in `U` or at `y`;
there is no `U`--`V` edge, every component of `V-v` misses `y`, and the
only remaining ways to cross into that side use `v` or a boundary vertex.
Here `v,s` are in `Z`, and every other boundary vertex is in `W`, where the
path has already stopped.  The stopped paths also avoid every other old
model vertex because those vertices are in `Z`.

After the enlargements, all five branch sets contain distinct vertices of
`W`, remain disjoint from the chosen component `C` and from `{s}`, and
retain the old `K_5` adjacencies.  The remaining eleven adjacencies needed
for the seven displayed branch sets are all forced:

- `C` is adjacent to each of the five old branch sets through its respective
  vertex of `W`, since `C` misses only `y` on `S`;
- `{s}` is adjacent to each old branch set through the same vertices,
  because `s` is complete to `S-{s}`; and
- `C` is adjacent to `{s}` because `s!=y`.

This accounts for all `10+5+5+1=21` pairs.  Theorem 2.2 is valid.

## 5. Theorem 2.3: the case `y=s`

Here the target boundary set

\[
                         B_0=S-\{s\}
\]

has order seven.  The old support has the six distinct vertices
`u_1,...,u_h,w_1,...,w_{4-h},v,t`.  After retaining the `h` vertices
`u_i` and deleting every other support vertex together with `s`, the proof
has

\[
 |Z|=(6-h)+1=7-h.
\]

The old support meets `B_0` in exactly the `4-h` vertices `w_j` and `t`.
Neither `v` nor any `u_i` lies in the original boundary.  Therefore

\[
 |T_0|=7-((4-h)+1)=h+2.
\]

If there were fewer than `h` disjoint `A_0`--`T_0` paths in `G-Z`,
set-Menger would give a separator `X` of order at most `h-1`.  Even if `X`
contains terminal vertices, both terminal sets retain a vertex because
`|A_0|=h` and `|T_0|=h+2`.  The resulting actual separator has order at
most

\[
                     (7-h)+(h-1)=6,
\]

contradicting seven-connectivity.  Thus the required linkage exists.

Every other old model vertex belongs to `Z`, so a linkage path meets the old
model only in its own selected start.  Since there are `h` disjoint paths
from an `h`-set, no path can consume another selected start.  Stop each path
at its first visit to `B_0`.  The first-hit vertices lie in `T_0`: every
old model vertex of `B_0` was deleted into `Z`.  They are distinct because
the paths are vertex-disjoint.

No stopped path enters `V-v`.  It starts in the component `U`; there is no
edge from `U` to the distinct component `V` of `G-S`; `v` is in `Z`; and
the only boundary vertex not in `B_0` is `s`, also in `Z`.  Any possible
passage from `U` toward `V-v` therefore reaches `B_0` first and has already
been stopped.  In particular, the enlarged rows avoid the later chosen
component `C` of `V-v`.

The five enlarged branch sets contain exactly five distinct, named vertices
of `B_0`: the `h` new first-hit vertices, the `4-h` old singleton vertices
`w_j`, and `t`.  As `|B_0|=7`, there are in fact two unused boundary
vertices; choosing one of them as `z` guarantees that `z` lies in none of
the enlarged branch sets.  The vertex `s` was deleted throughout the
linkage construction.  Consequently

\[
 M'_1,\ldots,M'_5,\quad C\mathbin\cup\{z\},\quad\{s\}
\]

are pairwise disjoint, and all are connected: the first five by enlargement,
the sixth because `C` is adjacent to `z`, and the last trivially.

All 21 adjacencies are accounted for without an implicit edge:

- the ten pairs among the five `M'_i` retain the old `K_5`-model
  adjacencies;
- the five pairs from `C union {z}` to the model rows are witnessed by the
  five selected boundary vertices, every one of which is adjacent to `C`
  because `y=s`;
- the five pairs from `{s}` to the model rows use the same boundary
  vertices and the fact that `s` is complete to `S-{s}`; and
- the final pair is witnessed by the edge `sz`.

The count is `10+5+5+1=21`.  Thus Theorem 2.3 gives an explicit valid
`K_7`-minor model.

## 6. Corollary 2.4 and closure of the shifted branch

The frontier input lists the common missed vertex as

\[
                    y\in\{s,w_1,\ldots,w_{4-h}\}.
\]

If `y!=s`, Theorem 2.2 applies; if `y=s`, Theorem 2.3 applies.  The two
cases are exhaustive and each gives a `K_7` minor.  Thus the full shifted
order-eight configuration described by (2.1)--(2.3) is eliminated under
precisely the quoted frontier hypotheses.  Theorem 2.1 is separately valid
and gives the stronger early conclusion when `V-v` has two components, but
it is not needed for the final two-case exhaustion.

This is closure of that conditional proof branch, not closure of every
order-eight separation and not a proof of `HC_7`; the upstream reduction to
the endpoint-rigid mixed-shore configuration remains an external dependency.

## 7. Falsification attempts and trust boundary

I tested the proof against the failure modes most likely to invalidate a
completion lemma:

1. a Menger separator containing terminal vertices;
2. unanchored branch sets of more than one vertex;
3. an old branch set meeting several boundary vertices;
4. a linkage path attempting to traverse one reserved component before its
   first boundary hit;
5. the sharp support bound `k-1` and the smallest cases `q=0,1`; and
6. a stopped path using the future vertex `z` or entering `V-v`; and
7. a missing adjacency involving `C union {z}`.

The explicit terminal counts, deletion budgets, first-hit argument, two
unused vertices of `B_0`, and the 21-pair accounting respectively rule these
out.  I found no graph satisfying a theorem's hypotheses while avoiding its
conclusion.

The audit does not establish the upstream endpoint-rigid normalization,
and does not prove `HC_7`.  It certifies exactly the uniform two-component
completion and the elimination of the shifted order-eight branch described
by (2.1)--(2.3).
