# Independent audit of type-5 one-defect endpoint allocation

**Verdict: GREEN** for theorem revision
`f7a7baa24c4dceb0d0a1f2a16feb606c37096d932f84eea24eb09ff303e3c653`.

The mathematical source revision audited before publication had SHA-256
`dbc1d140018c6f54361d09516c00eb08045d28be80c4f59cef4d13d38c79d8fd`.
The only subsequent source change replaced the pending-audit status line
with a link to this GREEN audit.  No theorem statement, hypothesis, proof,
application, or trust-boundary text changed.

This audit checked the following exact files:

- theorem:
  `hc7_pentagonal_bipyramid_type5_one_defect_allocation.md`, SHA-256
  `f7a7baa24c4dceb0d0a1f2a16feb606c37096d932f84eea24eb09ff303e3c653`;
- verifier:
  `hc7_pentagonal_bipyramid_type5_one_defect_allocation_verify.py`, SHA-256
  `a414c11b8402c79fd8960dedcb939f9b9c4a8eb881f026d55d41ce862583d22a`;
- imported enlargement generator and exact minor-model search:
  `../active/hc7_pentagonal_bipyramid_enlargement_probe.py`, SHA-256
  `d53e66678231eca6afc5d298a522f6cddd370b137feb974ee3cd756f7bbbadd3`;
- one-defect two-root completion-or-separation theorem:
  `hc7_one_defect_two_root_k5_separator.md`, SHA-256
  `87e08e0a151f0aca4c168995a906b60b0a95d9023e8076d4fa92b8982a002179`;
- its adjacent GREEN audit:
  `hc7_one_defect_two_root_k5_separator_audit.md`, SHA-256
  `557f63c2dc4a90e93819ad2e8861d527ed3835c4039fba5667c92cac6f934c67`.

## 1. Reproduction

Running the pinned verifier exited with status zero and printed exactly

```text
GREEN type-5 one-defect allocation: paired-failures=340 one-defect-failures=20 double-confined=20 mismatches=0
```

The verifier imports the same enlargement generator and minor-model routines
used by the separately audited endpoint-allocation classification; the exact
imported revision is pinned above.

## 2. Coverage of all endpoint sets

The generator produces the 50 labelled type-5 enlargements.  For each one,
the verifier ranges independently over the three nonempty subsets
`{0}`, `{1}`, and `{0,1}` in each of the two split fibres for each of the two
nominated sets.  It therefore covers exactly

\[
                   50\cdot3^4=4050
\]

ordered admissible pairs `(A,B)`.  This is the full set-valued quantifier in
Theorem 1.1, not the earlier singleton-only subcensus.

The verifier first invokes the exhaustive paired-rooted `K_5` search and
continues to the one-defect search precisely on its 340 negative cases.  By
the audited endpoint classification, every such case has at least one
confined nominated set, so the three alternatives in Theorem 1.1 exhaust the
domain.

## 3. Exhaustiveness of the one-defect search

For a fixed orientation, the search enumerates every nonempty vertex subset
of the enlargement, retains exactly the connected subsets meeting the set
that must be full, and records whether each also meets the second nominated
set.  Its recursive search chooses five candidates in increasing order,
checks vertex-disjointness by bit masks, and checks every new candidate
against every previously chosen bag for a literal graph edge.  Thus all ten
branch-set adjacencies hold.  The pruning condition

```text
defect_hits + remaining < 4
```

removes only partial choices that cannot possibly reach four contacts.  At a
five-bag leaf it accepts exactly when at least four bags meet the second set.
The reverse orientation is searched separately.  Consequently, failure
means that no one-defect `K_5` model exists in either orientation; it is not
failure of a prescribed contraction or path family.

## 4. Exact 340/320/20 classification

The verifier reproduces 340 paired-rooted failures.  It then checks the
following exact orientation predicate in every one of them:

- when only `A` is confined, the `B`-full/`A`-one-defect orientation exists
  and the reverse orientation does not;
- when only `B` is confined, the `A`-full/`B`-one-defect orientation exists
  and the reverse orientation does not;
- when both are confined, neither orientation exists.

There are 160 cases of each singly confined orientation and 20
double-confined cases, giving 320 cases in outcome 2 and 20 in outcome 3.
The mismatch count is zero.  Together with the 3,710 paired-rooted positive
cases, these counts exhaust all 4,050 assignments.

## 5. Conditional host consequence

The source now states every hypothesis needed for the host lift: `G` is
seven-connected; the two root subgraphs are connected, disjoint and adjacent;
the named pieces are disjoint from them; and the two nominated sets are the
literal root-neighbourhood sets under the quotient map.  Therefore each
lifted model bag that meets a nominated set is adjacent to the corresponding
root.

Outcome 2 consequently gives five bags adjacent to one root and at least
four adjacent to the other.  The pinned, separately audited one-defect
two-root theorem applies without identifying palette colours with quotient
labels.  It returns either an explicit `K_7`-minor model or the full
neighbourhood of a nonempty proper connected set as an actual separation.

The source correctly does **not** claim that this separation is terminal:
its order is at least seven but need not equal seven, and the two closed-shore
colourings need not induce a common boundary partition.  It also correctly
leaves the 20 double-confined quotient cases unresolved.

## 6. Trust boundary

This is a computer-assisted finite classification of labelled type-5
enlargements.  It does not prove that an abstract enlargement theorem
preserves the two nominated root-neighbourhood sets, does not produce the
operation-specific response required to free a confined root, and does not
close the returned separation.  Within its exact finite and conditional
host-lifting scope, the theorem and verifier are GREEN.
