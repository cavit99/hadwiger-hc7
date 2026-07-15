# Two full shores force a four-colour boundary or one cyclic exception

**Status:** proved and independently audited.  The order-eight conclusion
also has an earlier independent proof in
`../archive/hadwiger_exact8_critical_core_elimination.md`; the order-nine
classification is the new part of this note.

This is a component-absorption theorem for the exact two-component residue.
It does not use Moser labels or portal orders.  Contracting the two open
shores turns the question into a literal join-minor test on the boundary.

## 1. Statement

Let `G` be a `K_7`-minor-free graph.  Let `A,B,S` be pairwise disjoint
vertex sets such that

1. `A` and `B` are nonempty and connected;
2. there is no edge between `A` and `B`; and
3. every vertex of `S` has a neighbour in `A` and a neighbour in `B`.

Put `J=G[S]`.

### Theorem 1 (boundary absorption)

If `|S|=8`, then `J` is four-colourable.  If `|S|=9`, then either `J` is
four-colourable or

\[
                         J\cong K_2\vee C_7.           \tag{1.1}
\]

Here `vee` denotes the graph join.

Consequently, in the two-component residue of
`hc7_three_split_minimal_bad_contraction.md`, an excess-eight boundary is
necessarily four-colourable.  An excess-nine boundary is necessarily
four-colourable unless it has the unique coherent two-apex boundary core
`K_2 vee C_7`.

## 2. Reduction to a finite join test

Contract `A` and `B` separately to vertices `a,b`.  The resulting graph is
a minor of `G`, and its subgraph on `S union {a,b}` is exactly

\[
                         I_2\vee J,                    \tag{2.1}
\]

where `a,b` are the two nonadjacent vertices of `I_2`.  Individual
fullness in hypothesis 3 is exactly what supplies all join edges.
Therefore

\[
                         I_2\vee J\not\succcurlyeq K_7. \tag{2.2}
\]

If `chi(J)>=6`, the known case `HC_6` gives a `K_6` model in `J`.
The connected set `A`, which has an edge to every boundary branch set,
would be a seventh bag.  Hence `chi(J)<=5`.

Suppose `chi(J)=5`.  Choose an induced vertex-minimal five-chromatic
subgraph `J_0` of `J`.  By the known case `HC_5`, `J_0` has a `K_5`
minor.  If `J_0` is a proper induced vertex-subgraph of `J`, choose
`s in V(J)-V(J_0)`.  The five branch sets in `J_0`, together with

\[
                            A\cup\{s\},\qquad B,       \tag{2.3}
\]

form a `K_7` model in `G`: `A union {s}` is connected, it is adjacent to
`B` through an edge from `s` to `B`, and both last bags are adjacent to
every boundary branch set by fullness.  This contradicts the hypothesis.

Thus `J_0=J`; in particular, `J` is a vertex-five-critical graph on
exactly eight or nine vertices.  It remains only to classify which such
graphs satisfy (2.2).

## 3. Exact finite census

The dependency-free checker

```text
active/hc7_boundary_join_probe.py
```

does four exact operations.

1. It decodes graph6 input.
2. A DSATUR backtracking routine tests four-colourability and
   vertex-five-criticality.
3. It forms the literal graph `I_2 vee J`.
4. It tests for a `K_7` minor by exhaustive vertex deletion and edge
   contraction until seven vertices remain, accepting exactly a complete
   graph.

Every vertex-five-critical graph is connected and has minimum degree at
least four.  Hence the following nauty commands cover every candidate:

```text
geng -q -c -d4 8 | python3 active/hc7_boundary_join_probe.py
geng -q -c -d4 9 | python3 active/hc7_boundary_join_probe.py
```

The exact outputs are

```text
# total=424 critical5=7 join_survivors=0
# total=15471 critical5=236 join_survivors=1
HCp`f~~
```

The unique nine-vertex survivor has edge set

```text
03 04 07 08 14 15 17 18 25 26 27 28 36 37 38
47 48 57 58 67 68 78
```

Vertices `7,8` form a `K_2` complete to the seven-cycle

```text
0-3-6-2-5-1-4-0,
```

so it is exactly `K_2 vee C_7`.  This proves Theorem 1.

## 4. Why this changes the live residue

The theorem removes an entire state-free branch of the excess cut.  No
eight-atom two-shore obstruction can have a five-chromatic boundary.  At
nine atoms, every five-chromatic obstruction has the same two literal
vertices complete to a cyclic seven-vertex remainder.  Thus any continuing
proof may use a four-colouring of the boundary, except in one explicitly
coherent apex-pair geometry.

The theorem does **not** say that the two vertices in (1.1) are a global
two-vertex transversal.  Interior structure in `A` or `B` can support a
`K_5` model after they are deleted.  Nor does a four-colouring of `S`
automatically extend to compatible six-colourings of both closed shores.
Those are the exact remaining state-transfer obligations.

## 5. Trust boundary

The mathematical reduction in Section 2 is independent of computation.
The census in Section 3 is exhaustive but computer-assisted.  Promotion to
fully audited status requires an independent rerun and code audit, or a
short hand classification of vertex-five-critical graphs of orders eight
and nine under the join-minor exclusion.
