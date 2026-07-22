# Audit: concentrated exclusive reserve responses

**Audit type:** separate internal cold audit

**Verdict:** **GREEN**

Audited theorem:
[`hc7_common_root_exclusive_reserve_response.md`](hc7_common_root_exclusive_reserve_response.md)

Audited source SHA-256:

```text
5d7e6a8520744fc6e4458a74fce2a41fe5fa04567b009b0860ccd30d1e230f19
```

## Matching-swap closure

For `rs in D`, only `r,s` have the two selected colours on the boundary.
If the bichromatic component through `r` in `G[F union X]` met `s`, a
shortest joining path would have nonempty open interior in `F`, since `rs`
is a boundary nonedge.  This contradicts `E`-exclusivity, so the component
meets `X` only at `r`.  Its Kempe interchange therefore creates exactly the
boundary pair `{r,s}`.

For a matching, distinct demands use disjoint pairs of colours.  Their
bichromatic components are vertex-disjoint, each interchange leaves every
other relevant two-colour subgraph unchanged, and the colour palettes on
different swapped sets remain disjoint.  The swaps consequently commute
and cannot create a monochromatic edge between swapped sets.  Theorem 2.1
has the stated exact boundary partition.

## Proper-minor response and exceptional set

The set `F union I` is connected because `F` is connected and `X`-full.
After its contraction to `z`, the vertices `u,z` are adjacent and both are
adjacent to all five vertices of `R`.  Proper-minor six-colourability thus
forces `u,z` to receive two distinct colours absent from `R`; hence `R`
uses at most four colours.  Restricting away the contracted copy of `F` and
expanding `z` over the independent set `I` preserves every retained edge
and gives the asserted colouring of `G[E union X union {u}]`.  Since `z`
was adjacent to every vertex of `R`, `I` is an exact boundary colour class.

If this response has no block of order at least three, all nonsingleton
`R`-classes form a matching.  If every such pair belongs to `D`, Theorem
2.1 supplies the identical boundary equality partition on the other shore;
a colour permutation then glues the two colourings to a six-colouring of
`G`.  Therefore either a large block occurs or some pair block lies in
`N`, exactly as claimed.

Because `D` is defined as the set of *all* `E`-exclusive reserve nonedges,
the reserve nonedges split disjointly as `D union N`, so

```text
|N| = q-|D|.
```

The bounds `q<=8` in degree eight and `q<=9` in degree nine, checked below,
give `|N|<=1` and `|N|<=2` from `|D|>=7`; the preliminary `|N|<=3` follows
from `q<=10`.  The independence bound `alpha(G[X])<=d_G(u)-5` makes a large
block have order exactly three in degree eight and order three or four in
degree nine.  These are exact implications, not heuristic counts.

## Six-demand rooted model

Let `Gamma` be the whole `gamma`-class and `Q=(G-u)-Gamma`.  The audited
five-reserve packet gives a proper five-colouring of `Q` with `R` as a
transversal.  Every demand in `D_0` has an `E`-interior bichromatic path;
the path avoids `Gamma`, so the two roots lie in one corresponding
bichromatic component of `Q[E union R]`.

Kriesell--Mohr, *Kempe Chains and Rooted Minors*, Theorem 7 applies exactly:
the demand graph has five vertices and six edges, and it is a spanning
subgraph of the routing graph of the five-coloured graph `Q[E union R]`.
It yields five pairwise disjoint connected rooted bags, adjacent on every
edge of `D_0`.  A literal edge of `G[R]` supplies every additional
adjacency claimed in Theorem 4.1.

The five bags lie in `Q[E union R]`, and hence are disjoint from `{u}` and
`F union I`.  The latter set is connected.  It is adjacent to every rooted
bag through the bag's root because `F` is `X`-full, while `{u}` is adjacent
to each root and to `F union I` through the nonempty set `I`.  All seven
branch sets are therefore pairwise disjoint and have every asserted
adjacency.  No unproved adjacency across a reserve nonedge outside `D_0` is
used.

For the numerical bound, the reserve-nonedge graph in degree eight has no
`K_4`, since `alpha(G[R])<=3`.  A graph on five vertices with at least nine
edges is `K_5` or `K_5` minus one edge and contains a `K_4`; hence `q<=8`.
In degree nine, `alpha(G[R])<=4`, so `G[R]` is not edgeless and `q<=9`.
Subtracting the six chosen demands gives the possible-missing-edge bounds
two and three.

## Separator corollary and abstract barrier

If rooted bags `B_r,B_s` are nonadjacent, the connected set `B_s` is
disjoint from `B_r union N_G(B_r)`.  Thus deleting `N_G(B_r)` leaves the
nonempty connected set `B_r` separated from `B_s`, so it is the boundary of
an actual separation.  Seven-connectivity gives only the lower bound
`|N_G(B_r)|>=7`; the corollary correctly claims no upper bound.

In the Section 5 example, `G[R]` has exactly the three displayed edges and
the other seven pairs form `D`.  Every guaranteed matching-swap partition
has blocks of order at most two, whereas `{1,2,3}|{4}|{5}` is a proper
boundary partition with a block of order three.  This refutes only the
set-theoretic sufficiency of the matching-swap response language.  The text
explicitly does not assert realization by a host satisfying the graph-
theoretic setup, so it does not overstate the barrier.

## Dependencies and unresolved limits

No proof gap was found.  The theorem depends on the audited short-trace
classification, full proper-minor six-colourability, seven-connectivity,
both exterior components being `X`-full, the audited five-reserve packet,
and the cited Kriesell--Mohr theorem.

The result does not complete the near-`K_7` model: up to two or three
reserve-bag adjacencies may remain absent.  The separator returned by a
missing adjacency has no proved upper bound, and the proper-minor response
need not preserve a selected matching partition.  Accordingly, the source
correctly presents a trace-preserving/confluence statement or a
dirty-path completion statement as new work rather than as a consequence
already proved.
