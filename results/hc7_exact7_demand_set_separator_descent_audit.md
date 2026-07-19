# Independent audit of exact-seven demand-set reflection and descent

**Verdict:** GREEN for Theorems 2.1 and 3.1 and Corollary 3.2 at the exact
source revision identified below.  The accompanying geometry barrier and
its deterministic certificate also verify at the exact revisions pinned
below.

**Audited theorem:** `hc7_exact7_demand_set_separator_descent.md`, SHA-256

```text
9729a02a822c16f7cc90de1a7fa3ba6728173f37f84623e134a53719f5e8b713
```

The GREEN audit was performed on source revision
`5fcd84228401520be7b3f95dd0744f578f62d36ef115f112716cd271b2a3b707`.
The source was then moved from `active/` to `results/` and only its status
line was changed to link this audit.  The theorem statement and proof are
unchanged; the displayed hash pins the promoted source.

**Audited barrier:** `../barriers/hc7_exact7_clean_path_geometry_barrier.md`,
SHA-256

```text
6373b14c9f7a7b5d59a80d2e1d154d98dcf794b6e07b09c7aa47de7cbc2191c9
```

**Audited verifier:**
`../barriers/hc7_exact7_clean_path_geometry_barrier_verify.py`, SHA-256

```text
abfa8caba1a3bd1f39a939daf92fde102c5026bb6df23b4408b67d7c76744893
```

This is a separate internal mathematical audit, not external peer review.
It reconstructs the contraction-and-gluing argument, checks every
demand-set adjacency, verifies all path-component and full-neighbourhood
claims, checks strictness and the final counting bounds, and independently
reruns the barrier certificate.

## 1. Setup and combinatorial bookkeeping

The boundary partition is

\[
             \Pi=M\mid\{x\}\mid\{y\}\mid\{k\}\ (k\in K),
\]

where `M` is independent, `K` is a clique, `xy` is absent, and
`(|M|,|K|)` is `(2,3)` or `(3,2)`.  Thus there are respectively six or
five blocks.  All three members of

\[
                         \{M,\{x\},\{y\}\}
\]

are nonempty independent sets.  The two fixed subgraphs `P_1,P_2` are
nonempty, connected, disjoint, contained in the open side `R`, and each is
adjacent to every literal vertex of `S`.

For a block `B` among these three, the demand set

\[
        D_K(B)=B\cup\{k\in K:E_G(k,B)=\varnothing\}
\]

records exactly the boundary vertices needed for a connected third
subgraph to represent `B` in a clique minor: if `k` already has an edge to
some member of `B`, the boundary edge supplies the branch-set adjacency;
if it has none, a contact from the third connected subgraph to `k` is
necessary and sufficient.  The definition does not incorrectly require
`k` to be complete to `B`.

## 2. Exact reflection minor

Fix a block `B` and a connected subgraph `Z` disjoint from `P_1 union P_2`
which contacts every member of `D_K(B)`.  Let `B_1,B_2` be the other two
blocks.  The three sets

\[
             Z\cup B,\qquad P_1\cup B_1,\qquad P_2\cup B_2
\]

are pairwise disjoint.  Each is connected:

- `Z` is connected and has a neighbour at every vertex of the nonempty
  block `B`; and
- each `P_i` is connected and boundary-full, so it joins all vertices of
  its assigned independent block.

Contract a spanning tree in each set.  At least one edge is contracted in
each set, because it contains a nonempty open-side subgraph and a nonempty
boundary block joined by an edge.  The resulting graph is therefore a
proper minor, regardless of whether any unused vertices of `R` are also
deleted.

### 2.1 Every clique adjacency

The three contraction vertices and the literal singleton vertices of `K`
form a clique.

1. The representatives using `P_1` and `P_2` are adjacent because `P_1`
   has a neighbour at every vertex of `B_2` (and symmetrically).
2. The representative using `Z union B` is adjacent to either `P_i`
   representative because `P_i` has a neighbour at every vertex of `B`.
3. Each `P_i` representative is adjacent to every `k in K` through a
   boundary-full contact from `P_i` to `k`.
4. For the `Z union B` representative and `k in K`, either `k` has an edge
   to `B`, or `k in D_K(B)` and `Z` has a required contact to `k`.
5. The literal vertices of `K` are pairwise adjacent by hypothesis.

There is consequently one clique vertex for each block of `Pi`.  A proper
six-colouring of the proper minor assigns pairwise distinct colours to
those representatives.  In the five-block case one palette colour may be
absent from the boundary; this does not affect exactness.

### 2.2 Expansion and gluing

Restrict the minor colouring to the unchanged vertices of `L union S`, and
give every vertex of each contracted boundary block the colour of its
representative.  This is a proper colouring of `G[L union S]`:

- each expanded block is independent;
- every edge from a block vertex to `L` or to another boundary block became
  an edge incident with its contraction representative; and
- contracted edges leading into `R` are irrelevant after restricting to
  `L union S`.

Different blocks receive different colours, so the equality partition on
literal `S` is exactly `Pi`, not merely a coarsening.  The given colouring
of `G[S union R]` has the same exact partition.  A bijection between the
colours used by corresponding blocks extends to a permutation of all six
colour names, including the possible unused colour in the five-block case.
After that permutation the colourings agree vertex by vertex on `S`.
There are no `L-R` edges, so they glue to a six-colouring of `G`.

This proves the general reflection statement and, under `chi(G)=7`, rules
out `Z` exactly as claimed.  The explanatory phrase “before assuming that
`G` is not six-colourable” is read as dropping that contradiction only;
the proper-minor six-colourability used to colour the contracted graph
remains an explicit hypothesis.

## 3. A path avoiding both boundary-full subgraphs

Let `P` be an `x`--`y` path with nonempty interior in `R`.  Nonemptiness
follows from the boundary nonedge `xy`.

Suppose its interior avoids `P_1 union P_2`.  The internal path is connected,
so all of it lies in one component `X` of
`R-(V(P_1) union V(P_2))`.  Its first and last edges show that `X` has a
neighbour at both `x` and `y`; hence `x,y in T_X`.

If every `k in K` nonadjacent to `x` also belonged to `T_X`, then the
connected subgraph `X` would contact every vertex of `D_K({x})`, contrary
to Theorem 2.1.  This implication also handles the case in which no member
of `K` is nonadjacent to `x`: the universal statement would then be
vacuously true and still produce the contradiction, so at least one such
`k_x` must exist.  Thus

\[
                  k_x\in K-T_X,\qquad xk_x\notin E(G).
\]

The identical argument at `y` supplies `k_y`; the two witnesses may be the
same, as the theorem states.

## 4. A nondirect first meeting

Orient `P` from `x`, and suppose its first internal vertex in
`P_1 union P_2` is not the first vertex after `x`.  The vertices strictly
between `x` and that first meeting form a nonempty connected subpath in the
complement of `P_1 union P_2`; it lies in one component `X` and its first
edge gives `x in T_X`.  Applying Theorem 2.1 to `X` and the block `{x}`
gives a vertex `k_x in K-T_X` nonadjacent to `x`, by the same demand-set
argument.  Reversing the orientation proves the symmetric statement at
the `y` end.  No disjointness between the two possible returned components
is asserted or needed.

## 5. Full-neighbourhood equality and strict descent

For every component `X` returned above, its external neighbours inside `R`
are exactly vertices of `P_1 union P_2`: this is the defining component
property after deleting those two vertex sets.  There are no edges from
`R` to `L`, and all remaining external neighbours lie on `S`.  Therefore

\[
  N_G(X)=\bigl(N_G(X)\cap S\bigr)\mathbin{\dot\cup}
         \bigl(N_G(X)\cap(V(P_1)\cup V(P_2))\bigr)
        =T_X\mathbin{\dot\cup}A_X.
\]

The union is disjoint because `S` and `R` are disjoint.  The nonempty set
`L` lies outside `X union N_G(X)`, while connected nonempty `X` survives on
the other side.  Hence this is the full boundary of an actual separation.
Seven-connectivity gives

\[
                         |T_X|+|A_X|\ge7.
\]

Both nonempty subgraphs `P_1,P_2` are disjoint from `X`, so `X` omits at
least two vertices of `R`; in particular `|X|<|R|`.  This is a strict
host-vertex decrease and does not depend on a quotient or completion.

In the path-avoidance case, two distinct witnesses `k_x,k_y` exclude two
of the seven boundary vertices from `T_X`, so `|T_X|<=5` and the preceding
inequality gives `|A_X|>=2`.  If they coincide, one boundary vertex is
excluded, giving `|T_X|<=6` and `|A_X|>=1`.  These counts remain valid for
both allowed values of `|K|`.

## 6. Exhaustion of path-end geometries

If the path interior avoids `P_1 union P_2`, Theorem 3.1(1) applies.
Otherwise inspect the path from both ends.  If the first meeting from at
least one end occurs after that end's first internal vertex, Theorem 3.1(2)
applies.  If neither orientation has such a nondirect first meeting, the
first internal vertex after `x` and the first internal vertex before `y`
both belong to `P_1 union P_2`.  These alternatives are exhaustive, so
Corollary 3.2 accurately isolates only the two-ended direct-intersection
geometry.

## 7. Barrier and verifier

The barrier graph has boundary
`S={m_1,m_2,x,y,k_1,k_2,k_3}`, with only the triangle on `K` inside `S`.
The vertices `d,p_1,p_2` are each adjacent to every member of `S`, while
`w` has precisely the displayed contacts to `x,y,p_1,p_2`.  Thus:

- `L={d}` and `R={p_1,p_2,w}` are anticomplete open sides;
- `d`, `p_1`, and `p_2` are boundary-full;
- `R` is connected and `x-w-y` is the required clean path; and
- its internal component `{w}` misses all of `K`, hence both endpoint
  demand sets.

The displayed five bags cover every graph edge and satisfy the
running-intersection property.  Their decomposition tree has four edges on
five bags, and the largest bag has six vertices.  Therefore the graph has
treewidth at most five and cannot contain the treewidth-six graph `K_7` as
a minor.

The verifier was rerun at its pinned hash with command

```text
python3 barriers/hc7_exact7_clean_path_geometry_barrier_verify.py
```

and returned exactly

```text
PASS: clean-path geometry; tree decomposition width 5; no K7 minor
```

The example is not seven-connected and does not satisfy the proper-minor
colouring setup.  Indeed, a boundary-full singleton sees all six colours of
the displayed six-block partition, so that partition cannot extend through
either shore.  It therefore refutes only the geometry-only shortcut stated
in the barrier, not the audited theorem or `HC_7`.

## 8. Trust boundary

The descent can return a boundary larger than seven and does not preserve
the old boundary partition or the two named boundary-full subgraphs through
that new separation.  It does not close the two-ended direct-intersection
path geometry.  The theorem consequently supplies a strict connected-side
parameter and exact missing-corner information, but not a recursive
state-preserving exact-seven induction.  The audit found no stronger
conclusion hidden in the proof.
