# Independent audit: splitting a distance-one obstruction path

**Verdict:** **GREEN** for the exact source revision identified below.

This is a separate internal mathematical audit, not external peer review.
It checks the full-neighbourhood identity and response orientation in Lemma
1.1, and every connectivity, disjointness, and adjacency assertion in the
seven-branch-set construction of Theorem 2.1.  The result is conditional and
does not prove `HC_7`.

## Audited revision

The audited source is
`results/hc7_distance_one_path_split_response.md` at SHA-256

```text
c8061bd6e2ae9fc2184a450321ce6be41aac585ec891e69b0156e5dec9cd8e50
```

The final revision changes only the source status line to link this audit;
the audited mathematics is unchanged.

## 1. Full-neighbourhood identity

Let `H` be a component of `G[E-V(P^circ)]`.  Any neighbour of `H` in
`E-H` must lie in `P^circ`; otherwise that neighbour belongs to the same
component of `G[E-V(P^circ)]`.  There are no `E`--`C` edges.  Consequently

\[
 N_G(H)=(N_G(H)\cap B)\mathbin{\dot\cup}
        (N_G(H)\cap V(P^\circ)).
\]

The first set has order `9-m(H)` and the second has order `h(H)`, proving

\[
 |N_G(H)|=9-m(H)+h(H).
\]

The path ends cause no double counting: they lie in `B`, while its interior
lies in `E`.  The nonempty shore `C` is anticomplete to `H`, so it survives
outside `H union N_G(H)`.  Thus `N_G(H)` is the boundary of an actual
nontrivial separation.  Seven-connectivity gives `|N_G(H)|>=7`; when
`h(H)<m(H)`, the displayed identity gives `|N_G(H)|<=8`.

## 2. Operation-specific response

For a crossing edge `xy` with `x in H`, its other endpoint belongs to
`N_G(H)`.  Edge deletion is a proper minor, so `G-xy` has a proper
six-colouring.  Its endpoints must have one colour, since otherwise the
edge can be restored.  Restriction gives a colouring of the intact outside
graph `G-H` and of the edge-deleted inside graph
`G[H union N_G(H)]-xy`.

If the resulting equality partition on `N_G(H)` extended through the
intact inside graph, the two boundary assignments could be aligned by a
permutation of the six colour names: equality classes correspond
bijectively to the colours used on the boundary, and unused colours can be
mapped arbitrarily.  The aligned colourings would glue to a six-colouring
of `G`, a contradiction.  Hence the response orientation and rejection
claim in Lemma 1.1 are correct.

## 3. The three cycle branch sets

In the distance-one outcome, the endpoints `u,v` belong to distinct
components of the operated boundary two-colour graph.  Both carry one of
the two operated colours, so a boundary edge `uv` would join those
components.  Therefore `uv` is not an edge.

Under Theorem 2.1's hypothesis, `u,v` lie in one component of the forest
`G[F]`.  Its unique `u`--`v` path

\[
 u=t_0,t_1,\ldots,t_k=v
\]

therefore has `k>=2`.  It meets the obstruction path only at `u,v`, because
the latter has all internal vertices in `E`, whereas the forest path lies
in `F`.  The three sets

\[
 \{u\},\qquad \{t_1,\ldots,t_{k-1}\},\qquad
 \{v\}\cup V(P^\circ)
\]

are nonempty, connected, and pairwise disjoint.  The first two are adjacent
through `ut_1`, the last two through `t_{k-1}v`, and the first and last
through the first edge of `P`.  Each contains a literal vertex of `F`.

## 4. The four external branch sets

The inherited normalized setting supplies pairwise disjoint, connected,
pairwise adjacent sets

\[
 R_0,\quad R_1,\quad E\cup\{d\},\quad D\cup\{e\},
\]

each adjacent to every vertex of `F`.  Replacing `E union {d}` by
`H union {d}` preserves all required properties:

- it is connected because `H` is full to `B` and `d in B`;
- it is adjacent to `R_0,R_1` through the boundary vertex `d`, since each
  rooted part contains an `S`-full connected subgraph;
- it is adjacent to `D union {e}` through any `w in W`, because
  `W subseteq D cap B` and boundary-fullness gives an `H`--`w` edge; and
- it is adjacent to every vertex of `F`, since `F subseteq B` and `H` is
  full to `B`.

The other three external sets retain their inherited adjacencies.  The four
sets are pairwise disjoint: `R_0,R_1` lie in `R`, `H` lies in `E`, `D` is
disjoint from both, and the adjoined vertices `d,e` are distinct boundary
vertices.

They are also disjoint from the three cycle sets.  The only cycle vertices
outside `F` lie in `P^circ`; these are disjoint from `H` by its definition
and from `R union D`.  The cycle's boundary vertices lie in
`F=S-{d,e}`, hence are distinct from the adjoined `d,e` and from all open-
shore vertices.

Finally, every external set is adjacent to every literal vertex of `F`.
Since each cycle set contains such a vertex, each external set is adjacent
to each cycle set.  Together with the already checked internal adjacencies,
the seven sets form a valid `K_7`-minor model.

## 5. Trust boundary

The theorem requires both additional hypotheses in Theorem 2.1: the two
obstruction-path endpoints must lie in one component of `G[F]`, and a
component of `G[E-V(P^circ)]` must be full to all nine vertices of `B`.
It does not prove either hypothesis from the distance-one Kempe transition.

If those hypotheses fail, the note proves only the alternatives recorded in
Section 3: separated endpoint locations, a path interior spanning `E`, or
the component-attachment inequality `h(H)>=m(H)`.  The second obstruction
path is not shown to split or replace the branch sets that it meets.  The
order-seven/eight response supplied by Lemma 1.1 is operation-specific; it
does not by itself give a common intact-shore boundary colouring.  Within
these stated limits, no mathematical error or unresolved assumption was
found.
