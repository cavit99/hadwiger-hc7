# Independent audit: paired-colourful planar-core barrier

**Audited source:** `hc7_paired_colourful_planar_core_barrier.md`
**Source SHA-256:**
`25d436688ed47f624fafc465249165ac889c43839e1c3a83d4930a90f1118630`
**Verifier:** `hc7_paired_colourful_planar_core_barrier_verify.py`
**Verifier SHA-256:**
`5266dd8700ee72ec3105df39104a9a4b1a772eb729153bf8155af7ba694543bc`
**Verdict:** **GREEN.**

The construction refutes exactly the static paired-root implication stated
in Section 1 of the source.  It does not construct, and does not claim to
construct, a seven-chromatic minor-critical host.

## 1. Core graph and four-connectivity

The graph6 string `HEhutxm` decodes to the displayed nine-vertex,
twenty-one-edge graph.  The fourteen oriented faces in the source use each
directed edge exactly once.  Euler's identity gives

\[
                            9-21+14=2,
\]

so they certify a plane triangulation.  Exhausting its triples gives
exactly the fourteen facial triangles and hence no separating triangle.
A maximal planar graph on at least four vertices is three-connected, and
its three-vertex cuts are precisely its separating triangles.  Therefore
`R` is four-connected.  NetworkX's independent planarity and
vertex-connectivity implementations return `True` and `4`, respectively.

## 2. Colouring and colourfulness

The complement has the unique triangle `012`, so `012` is the unique
independent triple of `R`.  On `3,...,8`, the complement is the cycle
`3456783`.  Four independent sets of order at most two cannot cover nine
vertices, so every four-colouring contains `012` as a colour class.  The
other three classes are a perfect matching of that complementary cycle.
Its two perfect matchings give exactly

\[
                 \{012,34,56,78\},\qquad
                 \{012,38,45,67\}.
\]

Both `S={0,3,5,7}` and `T={0,4,6,8}` meet every class in both
partitions.  This proves colourfulness.  The verifier independently finds
exactly `48=2*4!` labelled four-colourings and those two unlabelled
partitions.

The source's non-three-colourability count is conservative but valid: one
class has order at most three and, after using the unique independent
triple, each remaining class has order at most two.  The displayed
partitions prove four-colourability without invoking the Four Colour
Theorem.

## 3. Absence of a paired `K_4` model

Four disjoint branch sets meeting each of the order-four sets `S,T` use
each member of either root set exactly once.  Since their intersection is
`{0}`, the branch set containing `0` has no other root.  Vertices `1,2`
are the only nonroots and are each nonadjacent to `0`, as well as to one
another, so that branch set is the singleton `{0}`.

For the other three branch sets, direct inspection gives exactly the six
root pairs that can be connected and made adjacent to `{0}`:

\[
                         36,38,54,56,74,78.
\]

The pairs `36,74` need no internal vertex; `38,56` each require vertex
`1`; and `54,78` each require vertex `2`.  The two perfect matchings are

\[
                    \{36,54,78\},\qquad\{38,56,74\}.
\]

The first demands vertex `2` in two disjoint branch sets and the second
demands vertex `1` in two disjoint branch sets.  This is impossible.  The
argument already fails before the three remaining branch sets' mutual
adjacencies need to be checked, so it certainly excludes the requested
`K_4` model.  The verifier separately searches every connected subset
meeting both root sets and finds no four-set model.

## 4. Five-chromatic extension

The neighbourhood definitions in `Q` are exact.  A four-colouring of
`R+z` would restrict to a four-colouring of `R`, but colourfulness of `S`
leaves no colour for `z`; hence `chi(R+z)=5`.  The same argument applies
to `u`.  Since `Q` contains either graph, `chi(Q)>=5`, while the five
independent sets displayed in the source colour `Q`.  Therefore all three
chromatic equalities in (3.3) hold.

## 5. Complete-minor computation

The verifier was run under NetworkX 3.6.1 and returned the four stated
`PASS` lines.  Its two `K_6`-minor encodings are exhaustive for different
reasons.

1. Every branch set of a minor model is a nonempty connected vertex
   subset.  The first search enumerates all such subsets, and its
   compatibility graph joins precisely the disjoint adjacent pairs.  A
   six-clique is therefore equivalent to a `K_6`-minor model.
2. The second search assigns every vertex either to an unused set or to
   one of six branch sets.  New branch labels are introduced only in
   first-occurrence order, removing label symmetry but no set partition.
   At a leaf it checks that all six sets are nonempty, connected, and
   pairwise adjacent.  Connectivity and adjacency are recomputed by an
   independent bit-mask implementation rather than by the first search's
   NetworkX subset primitives.  Thus every possible six-branch-set model
   is tested.

Both encodings first find the singleton model in `K_6` as a positive
control.  Both return no model in `Q`.  No branch-set order, path length,
or graph order beyond the literal eleven-vertex input is assumed.

The conclusion for `K_1 vee Q` is also valid.  A `K_7` model has at most
one branch set containing the universal vertex.  Removing that branch set,
or selecting any six branch sets if the universal vertex is unused, would
leave a `K_6` model in `Q`, contradicting the exhaustive result.

## 6. Trust boundary

- The complete-minor exclusion is a finite computer-assisted result, not
  an unbounded theorem inferred from enumeration.
- The verifier is deterministic, checks positive controls, and includes
  two exhaustive encodings of the only substantive computational claim.
- The construction has no actual connected bipartite expansion `X`, is
  not seven-connected or seven-chromatic, and is not strongly
  contraction-critical.
- It therefore does not refute a theorem that uses proper-minor
  six-colourings to produce a `K_7` model, an actual order-seven
  separation, or a fixed two-vertex `K_5`-model transversal.
- It does prove that no theorem based only on the compressed graphs
  `R,Q`, their chromatic numbers, planarity/four-connectivity, the two
  colourful neighbourhoods, and `K_6`-minor exclusion can force the
  paired rooted `K_4` model.

No unresolved gap remains in the stated barrier scope.
