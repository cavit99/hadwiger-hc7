# Independent audit: all-exact-block Kempe-distance barrier

**Verdict: GREEN.**

This audit checks the exact revisions

```text
barriers/hc7_simplicial_boundary_all_exact_blocks_distance_barrier.md
SHA-256 b2366c61be349ae398529896a65449f7c42db1e974efbb7a83255b292e3f4a2f

barriers/hc7_simplicial_boundary_all_exact_blocks_distance_barrier_verify.py
SHA-256 830cd896d155e973f96a09318cea5809e0ac6406a649a703d206fb49a891ce0f
```

The finite extension-language certificate, its realization by two connected
boundary-full open shores, and the stated trust boundary are correct.  This
is a barrier to a boundary-language inference, not a counterexample to
`HC_7`.

After the audit, promotion changed only the source's status line to link this
GREEN audit; no theorem, certificate, realization, or scope text changed.

## 1. Boundary graph

The boundary has two components.  One is `K_4` on `Y`.  The other consists
of `K_4` on `X` and the vertex `d`, whose neighbourhood is exactly the edge
`01`.  Hence `d` is simplicial.  Neither component has a `K_5` minor: the
first has four vertices, while the second has five vertices and is not
`K_5`; a five-branch-set model on five vertices would have five singleton
branch sets.  Thus the asserted `K_5`-minor exclusion is valid.

The independent-set count is also exact.  There are nine singletons,
sixteen `X`--`Y` pairs, six pairs containing `d`, and eight triples of the
form

```text
{d,x,y},  x in {2,3},  y in Y.
```

No larger independent set exists, giving `9+16+6+8=39`.

## 2. State enumeration and Kempe adjacency

The recursive enumeration assigns each boundary vertex either to an
existing independent block or to a new block, stopping at six blocks.
Canonicalization removes repeated presentations, so it enumerates exactly
the equality partitions into at most six nonempty independent blocks.

For two used colours, the verifier computes every connected component of
their induced two-colour graph and interchanges exactly that component.  If
one colour is unused, the used colour class is independent, so its vertices
are precisely the two-colour components; moving each vertex separately is
complete.  Swaps which only rename an entire colour class leave the equality
partition unchanged and are correctly omitted.  Symmetrizing the resulting
adjacency is legitimate.

The two listed certificate families map to distinct valid states.  The
verifier checks that they are disjoint, that no quotient Kempe edge crosses
between them, and that each of the 39 independent sets occurs as an exact
block in at least one state on each side.  Restricting the state graph to
partitions which retain a specified block gives quotient distance at least
two for every block.  A labelled Kempe path maps to a path in this quotient,
so this lower bound is also a valid lower bound for labelled exact-block
reconfiguration.  In particular, quotienting cannot create a false claim of
large labelled distance.

The verifier was rerun independently, including under a nondefault hash
seed, and produced exactly

```text
states=744 kempe_edges=6708 independent_blocks=39
left_states=16 right_states=17 cross_kempe_edges=0
exact_block_quotient_distances: 2=>33 3=>6
PASS: every independent exact block occurs on both sides at distance at least two
```

## 3. Realization and connected-full augmentation

For either certificate family, take all labelled six-colourings whose
equality partition belongs to that family.  The resulting relation is
closed under permutations of the six colours, so Theorem 3 of
Dvořák--Swart applies with `k=6` and realizes it by a finite boundaried
graph.

Adding a fresh open centre, a separate length-two path from every boundary
vertex to that centre, and a separate length-two path from each old open
component to the centre preserves the extension relation.  An old colouring
extends because every new subdivision vertex must avoid at most two colours;
conversely, every new colouring restricts to an old one.  The new open
interior is connected and has a neighbour at every literal boundary vertex.

Adding the prescribed boundary edges also preserves the relation.  Every
certificate state is proper on the stated boundary graph.  Conversely,
every prescribed boundary nonedge is an independent pair and hence occurs
as one exact block in each family; therefore neither original realizer can
already contain such a pair as an edge.  Gluing the two augmented realizers
along the boundary leaves their open interiors anticomplete and gives
exactly the two advertised extension languages.

Finally, if `Q` is either connected boundary-full open shore and `I` is a
nonempty independent boundary set, then `Q union I` is connected.  Choose
on the opposite closed shore a certificate colouring having `I` as an
exact block and contract `Q union I`.  The contraction image can receive
the colour of that block: it is adjacent to every boundary vertex outside
`I`, while any edge from `I` to the retained open shore was already proper
in the chosen colouring.  Thus every asserted shore-plus-block contraction
is indeed six-colourable.

## 4. Scope and unresolved hypotheses

The note does not assert that the realized host is `K_7`-minor-free,
seven-connected, seven-chromatic, or minor-minimal.  It expressly warns
that connectivity amplification creates a `K_7` minor.  Accordingly the
certificate refutes only the proposed inference from all exact-block
extension queries to distance one or a common trace.  A positive live-host
theorem may still use `K_7`-minor exclusion and operation-specific
contraction-critical responses.

The external realization input was checked against the primary preprint:
Theorem 3 states that for every `k>=3`, every finite boundary set and every
permutation-closed set of labelled `k`-colourings, a graph realizing exactly
that relation exists (with additional rooted-minor exclusions not needed
here).

No unresolved mathematical gap remains in the claim at its stated scope.
