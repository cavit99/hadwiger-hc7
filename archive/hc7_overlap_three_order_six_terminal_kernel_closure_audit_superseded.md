# Superseded audit: six-terminal kernel closure at overlap three

**Archived:** superseded by the canonical independent audit at
[`../results/hc7_overlap_three_six_terminal_kernel_closure_audit.md`](../results/hc7_overlap_three_six_terminal_kernel_closure_audit.md).
This earlier draft is retained because it documents the caught 300-versus-780
labelled-kernel enumeration defect.

## Verdict

**GREEN.**  The theorem and its exhaustive verifier close all 140
noncommon category orbits, of total weight 7,878, in the normalized
irredundant arm-order-six, overlap-three cell.  Together with the separately
audited common-state composition, this closes that entire normalized cell.

This is not a proof of the support-six transversal theorem or of `HC_7`.
It does not address the other arm overlaps or the separated-triple branch.

Audited files:

* [`../results/hc7_overlap_three_six_terminal_kernel_closure.md`](../results/hc7_overlap_three_six_terminal_kernel_closure.md);
* [`../active/hc7_overlap_three_six_terminal_kernel_verify.py`](../active/hc7_overlap_three_six_terminal_kernel_verify.py);
* the local relation and generic branch-partition detector in
  [`../active/hc7_cross_arm_overlap_three_kernel_decoder.py`](../active/hc7_cross_arm_overlap_three_kernel_decoder.py).

## 1. Structural reduction

The connectivity calculation is correct.  With `I={0,1,2}`, a cut of order
at most three in `H=G-I` would give a cut of order at most six in `G`.
Thus `H` is four-connected.  After reserving any `r in T`, deleting at most
two more vertices from `H-r` still deletes at most six vertices from `G`,
so `H-r` is three-connected.

The terminal-legal kernel theorem therefore applies to the other six
literal terminals and gives a rooted irreducible kernel of order six or
seven.  Terminal labels remain distinct throughout.

For order six, every three-connected carrier contains a spanning
edge-minimal three-connected subgraph.  Exhausting all 142 labelled minimal
subgraphs is therefore sufficient by edge monotonicity; it does not assume
that a bare `C_6` is enough.

For order seven, the sole nonterminal is incident only with terminal-legal
edges.  Hence terminal irreducibility is exactly the condition that every
such incident contraction fails to remain three-connected.  The direct
`2^21` enumeration checks this condition, simplicity, minimum degree, and
three-connectivity.  Wu's four-charge condition is used only as a necessary
filter and cannot discard a legal kernel.

The resulting 780 labelled kernels agree exactly with the independently
proved hand classification:

* 60 labelled six-wheels;
* an oppositely chorded `C_6`, with the hub missing both chord ends
  (180 labelled kernels), one chord end (360), or neither chord end (180).

Their degree profile matches the one asserted in the theorem.  Absorbing
the nonterminal into any adjacent terminal bag is legitimate: the two
preimage bags are adjacent and connected, the union retains the terminal,
and all transferred contacts are actual bag adjacencies.  The proof may
choose the absorbing neighbour after seeing the returned kernel.

## 2. Boundary-state coverage

The local six-vertex relation is exact.  A spanning `K_5` model on six
vertices has one two-vertex connected bag and four singleton bags.  The
four singletons form a clique and each contacts the edge-bag.  Excluding a
literal `K_5` gives exactly the 375 local patterns used by the join.

The verifier independently asserts:

```text
60,162 joined states;
7,878 noncommon states;
140 noncommon orbits under a group of order 144.
```

It also reconstructs every representative's full orbit, checks containment
in the noncommon state set, and checks its exact weight.  The complement,
52,284 states, is precisely the common class handled by the separately
audited three-rooted small-`K_4` composition theorem.

Passing to one representative per orbit is sound.  The automorphism group
preserves the four label categories and the normalized hypotheses, while
the conclusion permits the reserved terminal and absorbing owner to be
transported by the same automorphism.

The final search uses only the forced-one mask and the carrier edges.  It
does not complete any of the seven unknown literal edges.  A carrier edge
may join two bags whose literal roots are a forced nonedge; this is valid
because it records an actual adjacency elsewhere between the two rooted
preimage bags and is introduced only after the local relations have been
joined.

## 3. Exact `K_7` detector

The specialized detector's case split is exhaustive.  Seven nonempty
branch sets supported on at most ten quotient objects have at least four
singleton bags.  According to the number of singleton bags, the remaining
sizes are:

```text
7 singletons;
6 singletons and one connected bag;
5 singletons and two connected adjacent bags;
4 singletons and three two-vertex bags using all six remaining objects.
```

The code tests the singleton clique, connectivity of every nonsingleton
bag, contact with each singleton, and every inter-bag contact.  It permits
unused quotient objects in the first three cases.  The four-singleton case
enumerates every perfect matching of the remaining six objects.

As a separate algorithmic cross-check, the generic set-partition detector
was run on 8,204 carrier compositions drawn from both kernel orders and two
reserved labels.  It agreed with the specialized detector in every case.

## 4. Reproduction

Run:

```text
python3 active/hc7_overlap_three_six_terminal_kernel_verify.py --crosscheck
```

The audited output is:

```text
minimal order6 carriers 142
labelled irreducible order7 kernels 780
catalogue_sha256 02672ee56c859e9f45d3ab7b5a8bf82562fac14bf844f524101a1834954c43fe
noncommon_state_sha256 6017357f84a3ebfd812d7e282d865ba6eab4cad2f6d33d4103f08dd6678560c1
closed_orbits 140
closed_weight 7878
failure_orbits 0
failure_weight 0
generic_crosscheck 8204 sha256 b831df578ec60a78b49328ae7b0a8e9fa806b05b8e0210bd93325b3a692845ca
```

The distribution of the number of valid reserved roots, weighted over the
7,878 original states, is

```text
1:153, 2:180, 3:513, 4:513, 5:3798, 6:1416, 7:1305.
```

## 5. Caught enumeration defect

During the audit, an auxiliary classification generator initially reported
only 300 labelled order-seven kernels.  It fixed one cycle label and also
forced that label to be a chord end, thereby omitting the other two choices
of opposite chord pair.  That auxiliary generator was not the basis of the
780-kernel verifier.  It has been corrected to iterate all three opposite
pairs and now also reports 780.

This correction is important: the 300-mask run was not exhaustive and must
not be cited.  The promoted result uses the direct 780-kernel enumeration
and the digest above.

## 6. Lift and exact limitation

For the certified reserved root, every possible returned order-six kernel
closes; for every returned order-seven kernel, at least one legitimate
absorbing owner closes.  The quotient model lifts because all kernel
vertices have pairwise disjoint connected preimages, the members of `I`
and the reserved root remain literal singleton objects, original edges are
literal root adjacencies, and carrier edges are actual preimage-bag
adjacencies.

Accordingly the claimed normalized cell is closed.  No stronger global
conclusion is licensed by this audit.
