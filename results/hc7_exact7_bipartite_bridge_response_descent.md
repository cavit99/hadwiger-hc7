# A bridge in the thin shore gives a strict exact-seven response descent

**Status:** written proof; separate internal audit GREEN in
[`hc7_exact7_bipartite_bridge_response_descent_audit.md`](hc7_exact7_bipartite_bridge_response_descent_audit.md).
This theorem converts a bridge in one connected open shore into two smaller
literal order-seven separations carrying operation-specific boundary
partitions.  It does not preserve the old boundary, its bipartition, or any
inherited clique-minor labels, and it does not prove `HC_7`.

## 1. Setting

Let `G` be seven-connected and `K_7`-minor-free, with

\[
 \chi(G)=7,
 \qquad\text{and every proper minor of }G\text{ six-colourable}.
\tag{1.1}
\]

Suppose

\[
 V(G)=L\mathbin{\dot\cup}Y\mathbin{\dot\cup}R,
 \qquad |Y|=7,
 \qquad E_G(L,R)=\varnothing,
\tag{1.2}
\]

where `L,R` are nonempty, `G[L]` is connected and adjacent to every
literal vertex of `Y`, and `R` contains two vertex-disjoint connected
subgraphs adjacent to every literal vertex of `Y`.  Assume that

\[
                              H:=G[Y]
\tag{1.3}
\]

is bipartite.

Let `uv` be a bridge of `G[L]`.  Write `C_1,C_2` for the components of
`G[L]-uv`, oriented so that `u\in C_1` and `v\in C_2`.

## 2. Exact contact and parity pattern

### Theorem 2.1

There are unique distinct vertices `x,y\in Y` such that

\[
 N_Y(C_1)=Y-\{y\},
 \qquad
 N_Y(C_2)=Y-\{x\}.
\tag{2.1}
\]

The vertex `x` has a neighbour in `C_1` but none in `C_2`, the vertex `y`
has a neighbour in `C_2` but none in `C_1`, and every other vertex of `Y`
has a neighbour in both bridge sides.  Moreover, `x,y` lie in the same
component of `H` and every `x`--`y` path in `H` has even length.

#### Proof

The bridge property and (1.2) give

\[
 N_G(C_1)=N_Y(C_1)\mathbin{\dot\cup}\{v\},
 \qquad
 N_G(C_2)=N_Y(C_2)\mathbin{\dot\cup}\{u\}.
\tag{2.2}
\]

Each displayed neighbourhood separates a nonempty bridge side from the
nonempty set `R`.  Seven-connectivity therefore gives

\[
                         |N_Y(C_i)|\ge6\qquad(i=1,2).
\tag{2.3}
\]

For `s\in Y`, define the nonempty contact list

\[
 \Lambda(s)=\{i\in\{1,2\}:N_G(s)\cap C_i\ne\varnothing\}.
\tag{2.4}
\]

The lists are nonempty because `L` is adjacent to every boundary vertex.
If `H` had a proper `\Lambda`-list-colouring, the audited nonspanning
two-connected-subgraph synchronization theorem, applied to the adjacent
subgraphs `C_1,C_2` and the two full connected subgraphs in `R`, would
six-colour `G`.  Hence the list instance is not colourable.

The graph `H` is bipartite.  The exact two-list parity theorem therefore
gives two forced vertices in one component which prescribe incompatible
bipartition orientations.  By (2.3), at most one boundary vertex has list
`{1}` and at most one has list `{2}`.  A parity conflict is consequently
possible only when both exist.  Call the vertex with list `{1}` `x` and
the vertex with list `{2}` `y`.  They are distinct, they lie in one
component of `H`, and the different singleton lists make their distance
even.  This is exactly (2.1) and the asserted contact pattern.
\(\square\)

## 3. Two smaller exact-seven separations

Put

\[
 \Omega_1=(Y-\{y\})\mathbin{\dot\cup}\{v\},
 \qquad
 \Omega_2=(Y-\{x\})\mathbin{\dot\cup}\{u\}.
\tag{3.1}
\]

### Theorem 3.1

For `i=1,2`, all of the following hold.

1. `\Omega_i=N_G(C_i)`, so `\Omega_i` is the boundary of an actual
   order-seven separation with connected open side `C_i`.
2. Every component of `G-\Omega_i` is adjacent to every literal vertex of
   `\Omega_i`.
3. The maximum number of pairwise disjoint `\Omega_i`-full connected
   subgraphs in `C_i` is one.  The corresponding maximum number `q_i` in
   the opposite open shore belongs to `{1,2}`.
4. Every proper six-colouring `c` of `G-uv` induces on `\Omega_i` an exact
   equality partition `\Pi_i` which is attainable on the opposite closed
   shore, is unattainable on the intact `C_i`-side, and satisfies

   \[
                       d_{G[\Omega_i]}(\Pi_i)>q_i.
   \tag{3.2}
   \]

In addition,

\[
                            |C_i|<|L|.
\tag{3.3}
\]

Thus each orientation is a strict connected-side reduction in the class of
operation-specific exact-seven interfaces.  It either remains in the
`(1,2)` full-subgraph packing case or enters the `(1,1)` case.

#### Proof

Equation (2.2) and Theorem 2.1 give item 1.  For any component `D` of
`G-\Omega_i`, its neighbourhood is contained in `\Omega_i`.  If `D`
missed one boundary vertex, at most six vertices would separate `D` from
the nonempty opposite side of the separation.  This contradicts
seven-connectivity and proves item 2.

Consider `C_1`.  It is `\Omega_1`-full by (2.1) and the bridge edge `uv`.
Every `\Omega_1`-full connected subgraph contained in `C_1` must contain
`u`, because `v` is a literal member of `\Omega_1` and `uv` is the only
edge from `C_1` to `v`.  Hence no two such subgraphs are disjoint, and the
near-side packing number is exactly one.  The same argument applies to
`C_2`.

The exact-seven full-subgraph packing theorem now leaves the vectors
`(1,1)`, `(1,2)` and `(1,3)`.  The adaptive `(1,3)` reflection theorem
excludes the last one in the present seven-chromatic `K_7`-minor-free host.
This proves item 3.

Let `c` be a six-colouring of `G-uv`.  Its endpoints have the same colour;
otherwise restoring `uv` would six-colour `G`.  On the separation with
near side `C_i`, the deleted edge crosses from that side to its boundary.
Consequently `c` restricts to a proper colouring of the opposite closed
shore and induces there the exact partition `\Pi_i`.

If `\Pi_i` were attainable by a proper colouring of the intact near
closed shore, a permutation of the six colours would align the two exact
boundary partitions and the colourings would glue to a six-colouring of
`G`.  Thus it is unattainable there.  If its demand were at most `q_i`,
the exact packet-reflection theorem, using `q_i` full connected subgraphs
on the opposite side, would either give a `K_7` minor or reproduce
`\Pi_i` on the near closed shore.  Both are impossible, so (3.2) follows.

Finally, both components of `G[L]-uv` are nonempty, which proves (3.3).
The proof for the two orientations is identical.
\(\square\)

## 4. Exact scope

The two new boundaries overlap in the five old boundary vertices
`Y-\{x,y\}`.  Replacing `v` by the equally coloured vertex `u`, their
operation-specific assignments agree on six named vertices.  This does not
make their complete equality partitions identical.

The old full connected subgraphs in `R` are not automatically full for a
new boundary: they have no edge to its new bridge endpoint.  The theorem
therefore recomputes the new packing vectors; it does not silently preserve
the old connected subgraphs.  It also does not preserve bipartiteness of
the boundary, the special five-plus-two labels, a selected old equality
partition, or any inherited minor-model labels.  An order-seven separation
with a one-sided legal response is not by itself a six-colouring or a
`K_7`-minor model.

## 5. Dependencies

- [exact two-connected-subgraph list obstruction](hc7_exact7_two_carrier_list_obstruction.md)
- [exact-seven full-subgraph packing](hc7_exact_seven_packet_packing.md)
- [adaptive `(1,3)` reflection](hc7_exact7_adaptive_packet_reflection.md)
