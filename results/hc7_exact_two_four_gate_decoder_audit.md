# Corrected cold re-audit of the exact-two four-gate decoder

**Audit status and provenance:** independently re-audited on 2026-07-16
against the three source hashes recorded below, after the earlier audit's
`4096`-lock claim was invalidated.  This document supersedes that earlier
auxiliary-count verdict; it does not inherit the old run as evidence.

**Verdict:** **GREEN for the branch-set theorem, with one corrected auxiliary
count.**  The abstract three-carrier lemma, its literal
four-gate specialization, its application to the audited exact-two gate,
the `4096`-case quantifier, and both model checks in the accompanying script
are correct.  The result closes that particular four-gate realization; it
does not close the general exact-two branch.

The original audit incorrectly reported that all `4096` minimal assignments
realize both Kempe locks.  The old test retained the deleted row edges
`aa'` and `bb'`, making row-end connectivity automatic.  The corrected test
runs in `K=G-{aa',bb'}` and gives `256`.  This does not affect the literal
`K_7` certificate, which remains valid for all `4096` assignments.

The re-audit reran the corrected verifier and separately compared its lock
predicate against the four endpoint-choice inequalities derived in Section
5.  Across all `4096` assignments there were zero mismatches.  The branch-set
theorem itself never assumes that all endpoint assignments are locked.

**Audited SHA-256 values:**

```text
b822c9fde19744d39b271423c451107f249800dabe0c18d4cecf262c561d68b8  results/hc7_exact_two_four_gate_decoder.md
64806b316f58da24d24f7844a15fde92daa92ba92f0497b882b116df2b03b67d  active/hc7_exact_two_gate_k7_probe.py
83551a1447d072dd3d7a82ec59c60ea8cc565245efac9bba54a89308e8e52418  active/hc7_five_colour_exact_two_row_linkage.md
```

## 1. Abstract branch-set lemma

Lemma 1.1 has exactly seven nonempty, pairwise disjoint connected bags:

* the three singleton vertices of `X-{x}`;
* `A union {x}`;
* `R_1`;
* `B union R_2`; and
* `R_3`.

The first four form a clique model because `X` is a four-clique and `A`
contacts `x`.  The last three are pairwise adjacent because the `R_i` are
pairwise adjacent; adjoining `B` to `R_2` loses no such contact.  Their
contacts to the first four are also complete:

* `R_1` contacts the three retained singleton vertices directly and
  contacts `A union {x}` through `A`;
* `B union R_2` contacts every vertex of `X` through `R_2`; and
* `R_3` contacts every vertex of `X`.

Finally `A-B` gives the additional adjacency between `A union {x}` and
`B union R_2`.  No hidden adjacency or label identification is used.

## 2. Four-gate specialization

The proposed carriers satisfy the abstract hypotheses literally:

\[
 R_1=\{y_2,z_3\},\qquad
 R_2=\{y_3,z_0\},\qquad
 R_3=\{y_4,z_1,z_2\}.
\]

The first two are connected by `y_2z_3` and `y_3z_0`; the third is
connected through the two edges from `y_4`.  They are pairwise adjacent
through the clique `Y`.  With `x=x_3`, the stated `z_3` edges give exactly
the three direct `X-{x_3}` contacts and the contact to `A`; `z_0` supplies
all four `X` contacts for `R_2`; and `z_2x_1` together with
`z_1x_2,z_1x_3,z_1x_4` supplies all four for `R_3`.  The hypotheses that
`B` contacts `y_3` and that `A` contacts `x_3` make the two enlarged bags
connected.  Thus the seven displayed bags in Corollary 2.1 are a literal
`K_7` model.  No edge `z_2z_3` is used.

## 3. Match with the audited gate

The vertex and colour correspondence in the script is

```text
QE = (x1,x2,x3,x4)       colours (1,2,3,4)
QF = (y0,y2,y3,y4)       colours (0,2,3,4)
Z  = (z0,z1,z2,z3)       colours (0,1,2,3).
```

Joining a gate to every core vertex of a different colour gives every
gate--core edge used in Corollary 2.1.  The support-six contacts give one
edge from each `QE` vertex to the first two-vertex row and from each `QF`
vertex to the second.  The declared common contacts give an edge from each
of `z_2,z_3` to each row.  The exact-two rigidity theorem supplies all six
edges on the four row endpoints, so the two row bags are connected and
adjacent.  Consequently every extension satisfying the source
description contains one of the minimal support graphs checked by the
script; additional contacts cannot destroy the displayed minor.

This application relies on the already cold-audited exact-two package.  It
does not assert that an arbitrary raw nonmonotone path has this gate
incidence matrix.

## 4. The `4096` assignments

The enumeration is exhaustive for minimal endpoint choices:

\[
 2^4\quad(Q_e\text{ to row }A),\qquad
 2^4\quad(Q_f\text{ to row }B),\qquad
 2^2\quad(z_2,z_3\text{ to }A),\qquad
 2^2\quad(z_2,z_3\text{ to }B).
\]

Their product is

\[
                             2^{12}=4096.
\]

Choosing exactly one endpoint for each required contact is sufficient:
every nonminimal support assignment contains one such minimal assignment
as a subgraph.  The script validates the same seven bags for every one of
the `4096` graphs.  Although the chosen endpoint changes, each enlarged row
bag contains both endpoints, so the fixed branch sets remain connected and
retain every required external adjacency.

## 5. Script and independent oracle

The fixed-model validator checks:

1. seven nonempty disjoint bags;
2. connectivity of every induced branch bag; and
3. a literal edge between every pair of bags.

The SMT replay is independently sound.  Each vertex belongs to at most one
bag; every bag has one root; strictly decreasing nonnegative depths connect
every assigned vertex to its root; and every pair of bags is constrained to
have a host edge.  Ordering the root names only breaks bag-label symmetry.
The run produced

```text
minimal_support_graphs 4096
two_lock_graphs 256
graphs_with_literal_uniform_K7 4096
uniform_K7_model ((0,), (1,), (2, 12, 13), (3,), (5, 11),
                  (6, 8, 14, 15), (7, 9, 10))
independent_exact_sample_K7 ((3, 13, 15), (4,), (5, 6), (10,), (11,),
                             (0, 2, 9, 12), (1, 7, 8, 14))
```

For colour `2` on row `A`, the relevant outside vertices form the chain

```text
x2-z0-y2-y0-z2.
```

After deleting `aa'`, its endpoints are connected precisely when the chosen
`A-x2` and `A-z2` contacts land on opposite row endpoints.  The colour-`3`
condition is the identical statement with `x3,z3`.  On row `B`, the
corresponding chains are

```text
y2-z1-x2-x1-z2,
y3-z1-x3-x1-z3.
```

Thus the two locks on both rows impose four independent inequalities on the
twelve endpoint-choice bits.  The other eight bits are free, giving exactly
`2^8=256` locked assignments.  The `has_two_locks` calculation now checks
these connections in the matching-deleted graph.  It is not needed for the
literal `K_7` certificate.

## 6. Trust boundary

Promoted here:

* the label-free three-carrier decoder;
* the exact literal four-gate corollary; and
* exclusion of all endpoint realizations of the Section 7 gate extension.

Not promoted here:

* augmentation of an arbitrary raw path to a four-linkage;
* extraction of the three carriers from every exact-two state; or
* the general support-six theorem or `HC_7`.
