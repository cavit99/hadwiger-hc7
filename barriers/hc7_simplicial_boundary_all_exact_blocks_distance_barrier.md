# All exact independent blocks need not yield a one-move shore transition

**Status:** computer-assisted finite extension-language barrier; deterministic
verifier in
[`hc7_simplicial_boundary_all_exact_blocks_distance_barrier_verify.py`](hc7_simplicial_boundary_all_exact_blocks_distance_barrier_verify.py);
separate internal audit GREEN in
[`hc7_simplicial_boundary_all_exact_blocks_distance_barrier_audit.md`](hc7_simplicial_boundary_all_exact_blocks_distance_barrier_audit.md).

This barrier shows that using several exact independent boundary blocks does
not, by itself, force two shore-extension languages to be one Kempe move
apart.  It includes a simplicial triangle vertex and tests every independent
block, including all legal sets containing that vertex.  It does not satisfy
the global `K_7`-minor exclusion and proper-minor criticality of the live
`HC_7` setting.

## 1. Boundary

Let

\[
 X=\{0,1,2,3\},\qquad Y=\{4,5,6,7\},\qquad d=8,
\]

and let the boundary graph `B` consist of the two disjoint cliques `X,Y`
together with the two edges `d0,d1`.  Thus `d` has precisely the adjacent
neighbours `0,1`.  The boundary is `K_5`-minor-free: its two components are
`K_4` and a five-vertex graph obtained from `K_4` by adding one degree-two
simplicial vertex, and the latter is not `K_5`.

The nonempty independent sets of `B` are:

- the nine singletons;
- cross-pairs using one vertex of `X` and one of `Y`;
- pairs containing `d` and one vertex outside `{0,1}`; and
- the eight triples `{d,x,y}` with `x in {2,3}` and `y in Y`.

There are 39 such sets.

## 2. Boundary states and the certificate

A **state** is an equality partition of `B` into at most six nonempty
independent blocks.  A boundary Kempe move interchanges two named colours on
one connected component of their two-colour graph.  Forgetting the colour
names gives an edge between the corresponding equality partitions.

The verifier contains two explicit families

\[
                         \mathcal L,\mathcal R          \tag{2.1}
\]

of respectively 16 and 17 states.  It checks all of the following.

1. Every member of either family is a proper state with at most six blocks.
2. For every nonempty independent set `I subseteq B`, each family contains
   a state having `I` as one exact block.
3. No member of `mathcal L` is Kempe-adjacent to a member of `mathcal R`.
4. In the state graph induced by states retaining a fixed exact block `I`,
   the distance between the two families is at least two for every `I`.

For completeness, the exhaustive state graph has 744 vertices and 6,708
edges.  The quotient distance is two for 33 independent blocks and three
for the other six.  In particular this includes `I={d}`, every legal pair
`{d,w}`, and every legal independent triple containing `d`.

The adjacency enumeration is exact.  If both colours are used, the checker
interchanges each connected component of their induced two-colour graph.
If one colour is unused, every vertex of the used independent colour class
is a component and is tested separately.  These exhaust all possible Kempe
moves on a labelled representative, so absence of an equality-partition
edge implies absence of a labelled one-move transition.

Running

```text
python3 barriers/hc7_simplicial_boundary_all_exact_blocks_distance_barrier_verify.py
```

prints

```text
states=744 kempe_edges=6708 independent_blocks=39
left_states=16 right_states=17 cross_kempe_edges=0
exact_block_quotient_distances: 2=>33 3=>6
PASS: every independent exact block occurs on both sides at distance at least two
```

## 3. Realization by two connected full shores

Take all labelled six-colourings whose equality partitions belong to
`mathcal L` or `mathcal R`.  Each relation is closed under permutation of
the six colour names.  The exact colouring-relation realization theorem of
Dvorak and Swart therefore gives two finite `B`-boundaried graphs having
these exact extension relations.

The standard connected-full augmentation preserves either relation: add a
new open centre, join every boundary vertex to it by a fresh length-two
path, and similarly join the centre by a length-two path to one selected
vertex of every old open component.  Every old colouring extends because
each new internal vertex has to avoid at most two colours; every new
colouring restricts to an old one.  The open interior becomes connected and
adjacent to every boundary vertex.

Glue one augmented realizer of each relation along `B`, leaving their open
interiors anticomplete, and add exactly the boundary edges defined in
Section 1.  The exact relations remain `mathcal L` and `mathcal R`: every
state in the certificate is proper on `B`, while every boundary nonedge
occurs together in some exact block in each relation and therefore cannot
already be an edge of either realizer.

The resulting two closed shores answer every exact independent-block query,
but have no common six-colouring and have exact-`I` Kempe distance at least
two for every `I`.  Moreover, for either open shore `Q` and every nonempty
independent `I`, the contraction of the connected set `Q union I` is
six-colourable: choose on the retained shore a certificate state having `I`
as an exact block and give the contraction image that block's colour.

## 4. Exact scope

The construction proves that the family of all exact-block cylinders—even
with a `K_5`-minor-free boundary, a simplicial triangle vertex, connected
full shores and actual shore-plus-block contraction colourings—does not
force a distance-one move or a common boundary trace.

It is not asserted to be `K_7`-minor-free, seven-connected, or
minor-minimal.  The usual false-twin amplification can make the realization
seven-connected while preserving its extension languages, but it also
creates an explicit `K_7` minor inside an amplified shore.  Thus the barrier
does not refute a theorem whose alternative conclusion is a `K_7`-minor
model.  Rather, it shows that such a positive theorem must visibly use
global `K_7`-minor exclusion or responses to operations internal to the
open shores; no invariant of the collection of exact-block distances alone
can supply the missing conclusion.

## 5. External input

- Z. Dvorak and J. M. Swart, *A note on extendable sets of colorings and
  rooted minors*, arXiv:2504.07764, Theorem 3: realization of every
  permutation-closed finite boundary-colouring relation with the stated
  rooted-minor exclusions.
