# Internal audit of the exact order-eight star-boundary barrier

**Audit status:** GREEN — written proofs and finite verifier independently
checked.

**Audit date:** 2026-07-16

**Promoted theorem note:**
`hc7_star_order_eight_boundary_state_barrier.md`, SHA-256
`6d7f90e2df9963e0cbbb55674c9987394002687dec178a41684bfae68ab76580`.

**Original audited revision SHA-256:**
`6af933f7fffc13ee647aa117ce7ccf9807be2f7fa5a4217369e9d96d918fd96a`.

The promoted revision changes only the opening status paragraph to link
this audit and its deterministic verifier, and repairs one relative link
from a superseded `active/` location to the promoted theorem in `results/`.
No theorem statement, proof, finite encoding, result, or scope claim
changed, so the GREEN verdict rebinds to the promoted hash above.

**Audited verifier:**
`hc7_star_order_eight_boundary_state_barrier_verify.py`, SHA-256
`c4501face2d9de2e3027ca5fd65c3fedce557fe5ef291d3b1e8ee325ffd55884`.

This is a separate internal audit, not external peer review.

## Verdict

The proofs of Lemmas 2.1 and 3.1, Theorem 4.1, the reduction (5.3),
and the finite census in Section 5 are correct under the hypotheses stated
in Section 1.  The verifier reruns successfully and its search space and
tests match the mathematical claims.  No unresolved mathematical gap was
found inside the audited note.

This verdict does **not** audit the upstream derivation of the Section 1
boundary from the active five-support branch, and it does not promote the
barrier into a proof of that branch or of `HC_7`.

## Hand-proof audit

### Lemma 2.1

The seven proposed branch sets are pairwise disjoint and connected.  The
edge `uv=f` supplies the adjacency between the first two component-derived
sets.  Since each component is adjacent to every literal vertex of `S`,
the third component-derived set is adjacent to both of the first two and
all three are adjacent to `e` and to each singleton in `R`.  The remaining
adjacencies follow from the hypotheses that `R` is a clique and `e` is
collectively adjacent to each vertex of `R`.  Thus the displayed sets do
form a `K_7`-minor model.

### Lemma 3.1

With exactly two complementary components, the seven displayed branch
sets are disjoint, connected, and span `G`.  Full boundary adjacency gives
all component-to-boundary adjacencies, including the adjacency between
`D` and `C union {x}`.  The only branch-set pair not forced adjacent is
`e,f`, and the setup makes that pair anticomplete.  The claimed spanning
`K_7`-minus-one-edge model is therefore valid.

### Theorem 4.1

An independent set meets each of `R,e,f,{x}` at most once, so it has order
at most four.  If `|I|<=3` and `H-I` were complete, it would contain five
clique vertices; together with the two nonadjacent join vertices, the
sets consisting of those five singletons, `{a,s}`, and `{b}` are a valid
`K_7`-minor model.  In particular `{a,s}` is connected, is adjacent to
`{b}` through `bs`, and both new branch sets are adjacent to the five
clique singletons.  If `|I|=4`, the unused endpoints of `e` and `f` remain
nonadjacent, so `H-I` is again noncomplete.

Consequently an optimal colouring of `H-I` has a nonsingleton colour
class.  Splitting that class and then adjoining `I` produces partitions
with `q+1` and `q+2` blocks.  Since `q<=4`, both lie in `Omega_6(H)`, and
their block-count parities differ.  This proves the claimed bichromaticity
for every exact trace cylinder.

### Reduction (5.3)

The forward implication correctly separates the placements of the two
nonadjacent join vertices in a `K_7` model.  If they are absent from the
model, only one is used, or both lie in one branch set, six branch sets
give a `K_6` model in `H`.  If they lie in distinct branch sets, those two
sets cannot both be singleton join vertices; choosing an `H`-vertex `v`
from one leaves the other five branch sets as a `K_5` model in `H-v`.

Conversely, a `K_6` model in `H` extends using one join vertex.  A `K_5`
model in `H-v` extends using `{a,v}` and `{b}`: the former is connected,
the two new sets are adjacent through `bv`, and both see every old branch
set.  Thus (5.3) is exact.

## Verifier audit

The verifier was read in full.  The candidate space is complete:

- the three edges of `R` and the two specified edges are fixed;
- all four `e`--`f` edges are forbidden;
- each of the six root-to-specified-edge contact choices has three
  nonempty possibilities; and
- the seven incidences at `x` are free.

Hence there are `3^6 * 2^7 = 93,312` labelled candidates.  The implemented
contact group is exactly
`S_3 x (C_2 wr S_2)`, fixes `x`, and has order 48.  Ordinary graph
isomorphism is subsequently tested separately, so structural contact
orbits are not confused with unlabelled isomorphism classes.

The clique-minor recursion is exhaustive: until the target order remains,
it tries every vertex deletion and every existing-edge contraction; on
the target order it tests completeness.  Edge deletion need not be
explicitly searched for clique-minor existence.  The contraction routine,
the colouring backtracker, independent-block partition generation, clique
odd-cycle-transversal test, and complement matching recursion were also
checked against their stated meanings.  The partition count `4,111` is
correct: it is the number of partitions of eight vertices into at most six
blocks.

From the repository root, the command

```text
python3 barriers/hc7_star_order_eight_boundary_state_barrier_verify.py
```

completed with:

```text
GREEN: exact order-eight star-boundary census verified
labelled candidates 93312
contact orbits 2568
surviving contact orbits 899
surviving labelled candidates 35340
ordinary isomorphism types 710
cliqueOCT/perfect-matching counts {(False, False): 1, (False, True): 50, (True, False): 129, (True, True): 719}
trace cylinders checked 23750
unique neither code 119876351 graph6 G|uFKw
sparse portal code 33858967 graph6 G~F_G?
```

As independent encoding spot-checks, decoding code `119876351` gives
graph6 `G|uFKw` and exactly the 17 edges in (5.1).  Decoding code `33858967`
gives graph6 `G~F_G?` and exactly the eleven edges in (5.2), including an
isolated vertex `x=7` and the asserted concentrated contacts through
vertices 3 and 5.

## Scope retained

The audited contribution is a barrier plus the spanning near-clique model
in the exact two-component residue.  The census does not align shore
colour-extension languages, force distributed portals, or repair the
missing `e`--`f` branch-set adjacency.  Those limitations are stated
accurately in the theorem note.
