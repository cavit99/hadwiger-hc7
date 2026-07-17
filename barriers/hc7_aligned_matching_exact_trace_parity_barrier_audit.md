# Independent audit: aligned exact-trace parity barrier

**Verdict:** **GREEN** as a barrier to arguments using only the data listed
in Section 5 of the source note.

This is an internal mathematical audit, not external peer review.  It does
not promote the construction to a counterexample to `HC_7`.

## 1. Audited revision

- theorem note:
  `barriers/hc7_aligned_matching_exact_trace_parity_barrier.md`
- audited SHA-256:
  `137a06460e9b448ee661222b3d84c185b1200884a307b65558524f69457ea26a`
- independently audited mathematical revision SHA-256:
  `91c0017c01e2bef0adff30189c8020df02b50c02ad451f81d56a287b14f732ed`
- finite checker:
  `barriers/hc7_aligned_matching_exact_trace_parity_barrier_verify.py`
- checker SHA-256:
  `3c28a43e8c83d4935f8939e2c69850cc8b4307dbc79f89bfe77657f45cc45319`
- realization theorem used by the construction:
  `barriers/hc7_state_realization_barrier.md`
- realization-note SHA-256:
  `e4891b54ba77daaa15fcae759a9d2dae1d51678bdeba58265bbca1a27f32ece0`

The promoted source differs from the independently audited mathematical
revision only in its opening status paragraph, which now records this
GREEN audit.  No statement, construction, or proof step changed.

The checker was run with Python 3 and returned:

```text
aligned perfect matching verified
endpoint-contact rigidity verified
width-five join decomposition verified
legal boundary partitions: 343
nonempty independent sets: 41
every exact-trace cylinder has both block-count parities
```

The checker is useful finite corroboration.  The existence of the two
unbounded colouring-relation realizers is supplied by the cited theorem,
not by this checker.

## 2. Boundary graph and minor calculation

The edge list (2.1) has all the asserted properties.

- `R={0,1,2}` is a triangle.
- `34` and `56` are edges, and there is no edge between `{3,4}` and
  `{5,6}`.
- In `R`, vertices `3,5` each miss exactly `0`, while vertices `4,6`
  each miss exactly `1,2`.  Thus the two nonneighbour sets belonging to
  either matching edge are nonempty and disjoint.
- `03,16,27,45` are four pairwise disjoint nonedges and cover the eight
  boundary vertices.  Hence they form the claimed aligned perfect
  matching of the complement.
- `{0,3,5,7}` is independent, so the warning that the hypotheses do not
  imply boundary independence number at most two is correct.

The displayed bags form a tree decomposition of `J`: every edge is in a
bag and the bags containing each vertex form a connected subtree.  Adding
the two independent universal vertices to every bag gives bags of order at
most six, hence a tree decomposition of width at most five for
`I_2 vee J`.  Since treewidth is minor-monotone and `tw(K_7)=6`, this join
has no `K_7` minor.

## 3. Parity-cylinder argument

For every nonempty independent `I` of `J`, one has `|I|<=4`, since `I`
meets each of the cliques `R`, `A`, `B`, and `{x}` at most once.

The claim that `J-I` is not complete is valid.  If `|I|<=3` and `J-I`
were complete, it would contain a five-clique.  Choose `i in I`, and let
`u,v` be the two independent universal vertices of `I_2 vee J`.  Then

```text
{u,i}, {v}, and the five singleton vertices of that K_5
```

are seven branch sets of a `K_7`-minor model, contradicting the preceding
treewidth calculation.  If `|I|=4`, then `I` contains one vertex from each
of `R,A,B,{x}`; the unused endpoint of `A` and the unused endpoint of `B`
are nonadjacent, so again `J-I` is not complete.

The complement matching gives a four-colouring of `J`, so
`q=chi(J-I)<=4`.  Since `J-I` is noncomplete, an optimal `q`-colouring has
a nonsingleton colour class.  Splitting that class gives proper partitions
of `J-I` with `q` and `q+1` blocks.  After adjoining `I` as one exact
block, the two boundary partitions have `q+1` and `q+2` blocks.  Both are
at most six, and their block counts have opposite parity.  This proves
(3.2), including the block-count bound that is needed to invoke the
six-colouring realization theorem.

The checker independently enumerates all 343 legal partitions and all 41
nonempty independent sets and confirms both parities in every exact-block
cylinder.

## 4. Realization, connectivity, and chromatic number

`Pi_0` is a proper six-block partition of `J-01`: the only restored
boundary edge internal to one of its blocks is `01`.  The two families in
(3.4), interpreted as all labelled six-colourings with the indicated
equality partitions, are closed under permutations of the six colours.
They therefore satisfy exactly the hypothesis of Dvořák--Swart,
Theorem 3, *A note on extendable sets of colorings and rooted minors*,
arXiv:2504.07764.  That theorem permits an arbitrary permutation-closed
set of labelled `k`-colourings of a finite boundary, so it realizes both
families used here.

The connected-full augmentation in the cited realization note preserves
the extension relation: every new middle vertex on a length-two path has
to avoid at most two colours, and six colours are available.  The
false-twin amplification also preserves the relation in both directions:
colour each twin class uniformly to extend an old colouring, and select
one representative of each class to recover an old colouring from an
amplified one.

For amplification order seven, deletion of fewer than seven vertices
leaves a representative in every false-twin class and at least one of the
eight boundary vertices.  Each amplified open shore therefore remains
connected, every surviving boundary vertex joins both shores, and the
remaining graph is connected.  Thus the glued graph is seven-connected.
Adding boundary edges cannot decrease connectivity.

Adding all edges of `J` filters the two extension relations to exactly the
even and odd legal partitions: `Pi_0` is excluded by `01`, while every
partition in `E` or `O` is proper on `J`.  No nonedge of `J` can already
be an edge of either realizer, because both parity families contain an
extension in which the two ends of that nonedge form one exact block.
Consequently the induced boundary is exactly `J`.

The two filtered relations are disjoint, so the glued graph is not
six-colourable.  After deleting `01`, `Pi_0` extends on both sides; a
colour permutation aligns the two shore colourings because they induce
the same equality partition.  Hence `G-01` is six-colourable.  Recolouring
one end of `01` with a seventh colour proves `chi(G)<=7`, while the
disjoint relations prove `chi(G)>6`.  Therefore `chi(G)=7`.

## 5. Actual proper-minor traces

The contraction argument in Section 4 is correct.

Fix an independent `I`, retain the left open shore `L`, and choose a
left-closed-shore colouring in which `I` is exactly one colour class.
The set `D union I` is connected: `D` is connected and boundary fullness
gives every vertex of `I` a neighbour in `D`.  Contract it to `z`.

- Every vertex of `S-I` is adjacent to `D`, hence to `z`, and exactness
  gives it a colour different from the common colour of `I`.
- There is no `L`--`D` edge.  Thus every new edge from `z` to a vertex of
  `L` comes from an old edge between that vertex and a member of `I`, and
  the old proper colouring gives different colours at its ends.
- All edges not incident with `z` were already checked by the retained
  closed-shore colouring.

Assigning the common colour of `I` to `z` is therefore a proper
six-colouring of the contracted graph.  This is an actual proper minor:
`D` and `I` are both nonempty, so contracting their connected union
strictly reduces the number of vertices.  The same proof works with the
two shores interchanged.  Strictly speaking, `I` no longer consists of
literal vertices in the quotient; “`I` is exactly one boundary colour
class” correctly refers to the labelled trace obtained by expanding the
contracted vertex.

## 6. Simultaneous two-pair contractions

For disjoint independent boundary pairs `I,K`, the sets `L union I` and
`D union K` are connected and vertex-disjoint.  Contracting both leaves
the two contracted vertices and the four untouched boundary vertices, so
the quotient has exactly six vertices.  Giving those six vertices
different colours is always proper and induces the labelled trace

```text
I | K | four singleton blocks.
```

This does not give a colouring of either uncontracted closed shore, and
the source note does not claim that it does.  The stated corollary and its
scope are therefore correct.

## 7. Trust boundary

The construction is not asserted to be `K_7`-minor-free or
seven-contraction-critical, and the realization/amplification procedure
does not establish either property.  It also permits an actual
order-seven separation.  The source explicitly preserves all three
limitations.

Accordingly, this barrier refutes only a positive implication based on
the aligned boundary, seven-connectivity, exact chromatic number seven,
two connected boundary-full shores, and all of the specified shore-
contraction traces.  It does not refute a theorem that uses global
`K_7`-minor exclusion, the response to every proper minor, the additional
labelled clique models of the active host, or a conclusion allowing an
order-seven separation.  The final sentence about what a successful proof
must use should be read in this explicitly stated methodological scope.
