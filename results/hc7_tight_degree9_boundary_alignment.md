# Boundary alignment at a tight degree-nine vertex

**Status:** written proof; separate internal audit GREEN in
[`hc7_tight_degree9_boundary_alignment_audit.md`](hc7_tight_degree9_boundary_alignment_audit.md).

This note couples the order-nine tight-vertex response to the audited
low-degree adjacent-pair and exterior-component machinery.  Its main gain
is an exact dichotomy: either the order-nine boundary strictly drops, or a
full exterior component yields a sparse, rooted two-apex-type local minor.
The latter alternative lies strictly below the density range of the
degree-nine pole verifier, so this note also identifies why that verifier
does not close the new response.

## 1. Setting

Let `G` be a seven-connected, seven-chromatic graph with no `K_7` minor,
and suppose every proper minor of `G` is six-colourable.  Let `v` have
degree nine and suppose `G-N_G[v]` is nonempty.  We use the established
cases `HC_5` and `HC_6`.

The live application is a tight vertex in one of the two anticomplete
shores of the full-six-colour order-nine paired list obstruction.  The
tight-vertex theorem supplies exactly the two hypotheses used here:

1. `d_G(v)=9`; and
2. an opposite old shore is disjoint from `N_G[v]`, so the exterior is
   nonempty.

Put

\[
                         H=G[N_G(v)].                 \tag{1.1}
\]

## 2. A boundary-aligned non-double-critical edge

### Theorem 2.1

There are a neighbour `x` of `v` and a component `C` of `G-N_G[v]` such
that, with

\[
                         S=N_G(C),                    \tag{2.1}
\]

the following hold.

1. `x in S`, `7<=|S|<=9`, and

   \[
                         \chi(G-\{v,x\})=6.            \tag{2.2}
   \]

2. Both `C` and the singleton `{v}` are adjacent to every literal vertex
   of `S`.
3. Every proper six-colouring `c` of `G-vx` makes `{x}` an exact colour
   block on `S`.  Its boundary partition extends through
   `G[C union S]` and through the edge-deleted opposite closed side, but is
   rejected by the intact opposite closed side.
4. `G[S-\{x\}]` has no `K_5` minor and is therefore four-colourable.

Consequently, if `|S|<=8`, the tight order-nine response has produced a
strictly smaller, operation-aligned full-neighbourhood response.  If
`|S|=9`, then

\[
                         S=N_G(v),                    \tag{2.3}
\]

`C` is adjacent to all nine neighbours of `v`, and every colouring in
item 3 uses all six colours on `S`.

### Proof

Let `T` be the set of neighbours of `v` having a neighbour outside
`N_G[v]`.  Its complement in `N_G(v)` has no exterior neighbour, so `T`
separates the nonempty exterior from `v` together with that complement.
Seven-connectivity gives `|T|>=7`.

Suppose every `y in T` satisfied `chi(G-{v,y})=5`.  The standard
double-critical-edge recolouring argument would give
`d_H(y)>=5` for every `y in T`.  If `y in N_G(v)-T`, then all neighbours
of `y` lie in `N_G[v]`; seven-connectivity and the edge `vy` give
`d_H(y)=d_G(y)-1>=6`.  Hence `delta(H)>=5`.

Contract any component of `G-N_G[v]` to a vertex `c`.  It has at least
seven neighbours in `H`.  The audited degree-nine pole completion now
applies: Mader's bound gives a `K_7` minor directly outside its three
equality regimes, while the finite verifier gives an `H`-meeting
`K_6`-minor model in those regimes and `{v}` supplies the seventh bag.
This contradiction proves that some `x in T` satisfies (2.2).  Choose a component `C` of
`G-N_G[v]` adjacent to `x` and put `S=N_G(C)`.  Componenthood gives
`S subseteq N_G(v)`, while seven-connectivity gives `|S|>=7`.
The singleton `{v}` and `C` are both full to `S`.  This establishes items
1 and 2 without changing the selected pole.

For completeness, the exact singleton assertion is elementary.  In a
six-colouring of `G-vx`, the two endpoints have one common colour
`alpha`, or the edge could be restored.  Every vertex of `S-{x}` is still
adjacent to `v`, so no such vertex has colour `alpha`.  Thus `{x}` is an
exact boundary block.  The side containing `C` does not contain `v`, so
the colouring is proper there before or after the edge is restored.  If
the same partition extended through the intact side containing `v`, the
two shore colourings could be aligned on their equality blocks and glued,
contrary to `chi(G)=7`.

Suppose `G[S-{x}]` had a `K_5`-minor model with branch sets
`M_1,...,M_5`.  The seven sets

\[
              M_1,\ldots,M_5,\qquad C,\qquad \{v,x\}  \tag{2.4}
\]

would form a `K_7`-minor model.  Indeed, `C` is adjacent to every literal
vertex of `S` and hence to every `M_i`; the connected set `{v,x}` is
adjacent to every `M_i` through `v` and to `C` through an `x`--`C` edge.
This contradiction proves the minor exclusion in item 4.  The established
case `HC_5` then gives four-colourability.

Finally, `S subseteq N_G(v)` and both sets have order nine in the equality
case, proving (2.3).  For a degree-nine vertex, the standard edge-deletion
recolouring argument forces every one of the other five colours to occur
on `N_G(v)-{x}`; together with the colour on `x`, all six occur.  \(\square\)

## 3. The full-component alternative is sparse

### Theorem 3.1

Suppose some component `C` of `G-N_G[v]` is adjacent to every vertex of
`N_G(v)`.  Then there is a neighbour `x` of `v` for which

\[
 d_H(x)\le4,
 \qquad \chi(G-\{v,x\})=6,                            \tag{3.1}
\]

and all conclusions of Theorem 2.1 hold with `S=N_G(v)` and this same
component `C`.  In addition:

1. `|E(H)|<=22`;
2. `x` has at least two neighbours outside `N_G[v]`;
3. `H-x` is `K_5`-minor-free;
4. the audited adjacent-pair palette-permutation linkage applies to the
   edge `vx`.

If `C` is the unique exterior component, both exterior neighbours forced
in item 2 lie in `C`.

### Proof

Contract `C` to one vertex `c`, delete every other exterior vertex, and
retain `v` and all nine vertices of `H`.  The resulting simple minor `Q`
has eleven vertices.  The vertices `v,c` are nonadjacent and are each
complete to `H`, so

\[
                      |E(Q)|=18+|E(H)|.               \tag{3.2}
\]

Mader's exact bound for a `K_7`-minor-free graph on eleven vertices is
forty edges.  Hence `|E(H)|<=22`.  The average degree in the nine-vertex
graph `H` is at most `44/9<5`; choose `x` with `d_H(x)<=4`.

If `chi(G-{v,x})=5`, the standard double-critical-edge recolouring
argument would give five common neighbours of `v` and `x`.  All such
vertices lie in `H`, contradicting `d_H(x)<=4`.  Deleting two vertices
from a seven-chromatic graph leaves chromatic number at least five, while
proper-minor minimality gives at most six.  Therefore (3.1) holds.

Since `C` is full to `N_G(v)`, the chosen `x` is exterior-contacting and
Theorem 2.1 applies with `S=N_G(v)`.  The vertex set decomposition gives

\[
 d_G(x)=1+d_H(x)+
       |N_G(x)\cap (V(G)-N_G[v])|.
\]

Together with seven-connectivity, this shows that `x` has at least
`6-d_H(x)>=2` exterior neighbours.  The assertion about `H-x` is item 4
of Theorem 2.1.

Finally, `chi(G-{v,x})=6` is precisely the hypothesis needed by the adjacent-pair
palette-permutation theorem: `HC_6` gives a `K_6`-minor model in
`G-{v,x}`, and connectivity lets it be enlarged to a spanning model;
and five pairwise vertex-disjoint paths join complete five-colour palettes
at the two poles.  \(\square\)

## 4. Exact relation to the old fixed boundary trace

In the live order-nine paired list obstruction, tightness gives a
colour-preserving bijection between the old singleton boundary vertices
missed by `v` and its internal neighbours in the old shore.  If the
aligned vertex `x` in Theorem 2.1 happens to be one of those internal
neighbours, deleting `vx` also gives the audited fixed-trace rainbow
replacement on the operated old shore.

There is no theorem forcing the aligned `x` to be internal.  Every old
boundary neighbour of `v` is exterior-contacting through the opposite old
shore, so the low-degree alignment may select such a boundary vertex.
Even when `x` is internal, the fixed-trace colouring need not extend
through the opposite old shore and therefore need not be the global
six-colouring of `G-vx`.

## 5. Why the existing degree-nine tools stop here

The full-component calculation identifies an exact disjointness between
the new residue and the pole verifier.

- The pole verifier assumes `delta(H)>=5`, hence `|E(H)|>=23`, and treats
  the three remaining density cases after Mader's bound.
- A full exterior component in the present residue forces
  `|E(H)|<=22` by (3.2).

Thus the verifier has already done all it can: it is the mechanism that
finds a non-double-critical aligned edge before the full-component residue,
whereas the surviving full-component case lies strictly below its input
density.

The legacy exterior-component analysis eliminates four or more components
at a degree-nine vertex; it does not eliminate the remaining one-, two-,
or three-component cases.  That result is not used as an input here: its
legacy audit has not yet been repinned to the current hash standard.  The
archived degree-nine three-shore and cutvertex completions additionally
assume special Moser-labelled or exact miss-set geometries not inherited by
`N_G(v)`.

Finally, (2.4) shows that the full-component residue contains the rooted
minor

\[
                         K_2\vee(H-x),                \tag{5.1}
\]

where the two joined branch sets are `C` and `{v,x}`.  Its base `H-x` is
`K_5`-minor-free, exactly as `K_7`-minor exclusion requires.  This is a
coherent two-apex-type local obstruction, not a contradiction.  Closing
it requires a host-level theorem forcing a `K_5` model outside this local
base, a compatible order-seven colouring, or a label-preserving use of
the palette linkage.  Neither density, exterior-component counting, nor
the old fixed-trace replacement supplies that missing implication.

## 6. Dependencies

- [tight vertices give exact order-nine singleton responses](../results/hc7_order9_tight_vertex_singleton_response.md)
- [low-degree boundary-edge alignment](../results/hc7_low_degree_boundary_edge_alignment.md)
- [degree-nine pole verifier](../results/hc7_degree9_pole_verifier.md)
- [adjacent-pair palette-permutation linkage](../results/hc7_adjacent_pair_palette_linkage.md)
- Mader's exact `K_7` extremal bound and the established cases `HC_5` and
  `HC_6`
