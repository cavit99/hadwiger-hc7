# Independent audit of endpoint allocation in type-5 enlargements

**Verdict: GREEN** for theorem revision
`dc259a7b0833699cfb68c828e038e36c7fd5694ab1add8077b9201c1a94fdfd8`.

This audit checked the following exact files:

- theorem:
  `hc7_pentagonal_bipyramid_type5_endpoint_allocation.md`, SHA-256
  `dc259a7b0833699cfb68c828e038e36c7fd5694ab1add8077b9201c1a94fdfd8`;
- verifier:
  `hc7_pentagonal_bipyramid_type5_endpoint_allocation_verify.py`, SHA-256
  `cb5e609493dbe677f8692a86e7835a77dae04c07957775e2ba028238de4e2ed8`;
- imported generator and exact minor-model search:
  `../active/hc7_pentagonal_bipyramid_enlargement_probe.py`, SHA-256
  `d53e66678231eca6afc5d298a522f6cddd370b137feb974ee3cd756f7bbbadd3`.

The previous revision was RED because its verifier tested only singleton
endpoint choices while the theorem quantified over arbitrary nonempty
endpoint subsets, and because its host consequence overstated what happens
when both roots are confined.  Both defects are corrected in the revisions
identified above.

## 1. Reproduction

Running the pinned verifier produced exactly

```text
GREEN type-5 endpoint allocation: instances=50 tests=4050 failures=340 root-trap-mismatches=0
```

It exited with status zero.  The audit also checked that the verifier imports
the generator identified by the exact hash above rather than a separate or
embedded implementation.

## 2. Enumeration of labelled enlargements

The generator starts with the plane rotation system of
`C_5\vee\overline{K_2}`.  It ranges over every old edge, every conforming
split at each end, and the two possible facial orientations.  It orients each
split so that the retained old edge joins the two side-zero vertices, retains
exactly the compatible facial assignments in the definition, and adds the
side-one edge.  The resulting list has exactly 50 labelled type-5
enlargements.

This is an enumeration of the finite labelled objects in the theorem, not an
enumeration of arbitrary host graphs.  The theorem and its application state
that boundary correctly.

## 3. Exhaustive root-set and minor-model search

For each enlargement, the verifier first tests whether the five unsplit old
vertices root a `K_5` model.  Exactly 20 of the 50 enlargements fail that
test.

At each split pair, each nominated set may contain the side-zero endpoint,
the side-one endpoint, or both.  The verifier now ranges over

\[
 \bigl\{\{0\},\{1\},\{0,1\}\bigr\}^4,
\]

so it tests all `3^4=81` ordered choices for `(A,B)` in each labelled
enlargement, for `50*81=4050` tests.  This exactly matches the arbitrary
nonempty set-valued quantifiers in Theorem 2.1; no monotonicity reduction to
singleton choices is used.

For a fixed test, the imported search enumerates every nonempty connected
vertex set meeting both nominated sets.  It then enumerates five pairwise
disjoint candidates and accepts exactly when all ten pairwise branch-set
adjacencies are present.  Hence it searches all paired-rooted `K_5` minor
models, not only a prescribed family of paths, contractions, or whole-column
bags.

The search finds 340 failures.  In every test its result agrees with the
claimed predicate: failure occurs precisely in one of the 20 enlargements
without a five-unsplit-root model and when `A` or `B` consists only of the
side-zero endpoint in both split pairs.  The mismatch count is zero.  This
proves both directions of the finite classification.

## 4. Host lifting and corrected response consequence

Under the relative named-piece hypothesis, membership of a quotient vertex
in `A` or `B` means that the corresponding named connected piece is adjacent
to the respective root subgraph.  The preimages of the five quotient branch
sets are therefore connected, disjoint and pairwise adjacent, and each is
adjacent to both root subgraphs.  Together with the two disjoint adjacent
roots, they give seven branch sets of a `K_7` minor.  The lifting argument is
correct.

The revised final paragraph also distinguishes the two possible residuals:

- if exactly one root is confined, giving that root a side-one contact in
  either split column removes the finite obstruction;
- if both roots are confined, both must be freed unless another terminal
  construction is supplied.

Thus it no longer makes the false claim that freeing just one of two confined
roots is automatically terminal.

## 5. Trust boundary

The result is a computer-assisted finite theorem about labelled type-5
quotients.  It does not prove that an abstract Hegde--Thomas enlargement
preserves the named pieces or either root-contact set, nor does it force a
proper-minor colouring response that escapes confinement.  The theorem states
these limitations explicitly.  No unbounded conclusion beyond the
label-preserving relative application was used in this audit.

Within that stated scope, the theorem, verifier, finite encoding, and host
lift are GREEN.
