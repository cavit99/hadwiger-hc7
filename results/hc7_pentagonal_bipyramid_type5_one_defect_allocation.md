# One-defect allocation in type-5 pentagonal-bipyramid enlargements

**Status:** computer-assisted finite theorem; separately audited **GREEN**
in
[`hc7_pentagonal_bipyramid_type5_one_defect_allocation_audit.md`](hc7_pentagonal_bipyramid_type5_one_defect_allocation_audit.md).

The paired-rooted endpoint theorem leaves a simultaneous two-column
confinement.  This note determines exactly how much weaker root alignment
is still available there.  It is a finite statement about type-5
enlargements and does not align an abstract enlargement minor with a
previously selected model.

## 1. One-defect models

Use the notation of the
[endpoint-allocation theorem](hc7_pentagonal_bipyramid_type5_endpoint_allocation.md).
Thus `A,B` contain all five unsplit old vertices and meet both split
fibres.  A `K_5` model is **`A`-full and `B`-one-defect** when all five
branch sets meet `A` and at least four meet `B`.  Define the reverse
orientation symmetrically.

### Theorem 1.1 (exact one-defect classification)

For every type-5 enlargement and every admissible pair `(A,B)`, one of the
following holds.

1. There is a paired-rooted `K_5` model.
2. Exactly one of `A,B` is confined to the retained-edge sides of both
   split fibres.  There is a `K_5` model which is full at the unconfined
   set and one-defect at the confined set.
3. Both `A` and `B` are confined to the retained-edge sides.  In each of
   the 20 exceptional labelled enlargements, the bare enlargement has no
   `K_5` model which is one-defect in either orientation.

Across the complete finite census, outcome 1 fails in 340 cases.  Outcome
2 consists of 320 of them, while outcome 3 consists of the remaining 20.

### Proof

The exact enumeration is performed by
[`hc7_pentagonal_bipyramid_type5_one_defect_allocation_verify.py`](hc7_pentagonal_bipyramid_type5_one_defect_allocation_verify.py).
It uses the same 50 type-5 enlargements and all `3^4=81` nonempty
set-valued endpoint choices per enlargement as the audited endpoint
classification, for 4,050 cases in total.

For a fixed orientation, the verifier enumerates every nonempty connected
vertex set meeting the set which must be full.  It then enumerates every
five pairwise disjoint such sets, checks all ten clique-model adjacencies,
and counts how many meet the second nominated set.  Acceptance requires at
least four.  The reverse orientation is checked separately.  Hence the
search exhausts all one-defect `K_5` models.

The verifier first reproduces the 340 paired-rooted failures.  Among them,
exactly 20 have no one-defect model in either orientation.  Those 20 are
exactly the choices in which both nominated sets equal the side-zero
singleton in each split fibre.  In every other paired-rooted failure,
exactly one nominated set is confined and a model exists which is full at
the unconfined set and meets the confined set in at least four bags.  This
proves all three alternatives. \(\square\)

Running the verifier prints

```text
GREEN type-5 one-defect allocation: paired-failures=340 one-defect-failures=20 double-confined=20 mismatches=0
```

## 2. Host consequence and trust boundary

Suppose the host graph `G` is seven-connected, the type-5 enlargement is
relative to named connected pieces, and the two root subgraphs are
disjoint, connected, adjacent to one another and disjoint from those
pieces.  Suppose further that the confined nominated set is precisely the
neighbourhood in the core of a singleton root, and that the unconfined
nominated set consists of the named pieces adjacent to the other root
(equivalently, the two nominated sets are the two literal root-neighbourhood
sets under the quotient map).  In outcome 2, lift the one-defect `K_5`
model through the named pieces.  The separately audited
[one-defect two-root theorem](hc7_one_defect_two_root_k5_separator.md)
then gives either an explicit `K_7` minor or the full neighbourhood of a
nonempty proper connected set as an actual separation.

The returned separator has order at least seven, not necessarily exactly
seven, and the theorem does not synchronize boundary colourings.  If the
confined root is not the singleton root in the selected normalization, an
additional root-orientation argument is required before applying that
theorem.

The sole finite type-5 residue not covered even by this one-defect exit is
therefore **double confinement**: both roots meet only the side-zero piece
in both split columns.  Eliminating that unbounded host configuration, or
turning it into a compatible order-seven separation, remains the dynamic
contraction-critical problem.
