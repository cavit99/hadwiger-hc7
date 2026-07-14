# Independent audit: cross-lobe rooted-`K_4` handoff

Audited file: `hc7_exact7_cross_lobe_rooted_k4_handoff.md`.

## Verdict

**GREEN**, subject only to the stated scope.  A reversed rooted-`K_4`
expansion, two disjoint boundary-full packets, and the legally attained
paired-triangle boundary data force a literal labelled `K_7^vee` model.
They do not force `K_7` and do not close the no-expansion planar-strip
branch.

## 1. Literal quotient reduction

Contracting `R,H_1,H_2,H_3,P,Q` is legitimate because the six sets are
connected, pairwise disjoint, and disjoint from the literal boundary.  The
four rooted sets give a literal `K_4`; the three named traces give

```text
h1-a1, h1-t3, h2-a2, h2-t2, h3-a3, h3-t1;
```

the two packet vertices are complete to the seven boundary vertices; and
`c` has one of four possible core contacts.

For the attained boundary partition, one witness edge must be retained
between `c` and each paired block and between each two distinct paired
blocks.  These six independent choices have respectively sizes

```text
2,2,2,4,4,4,
```

so there are `2^3 4^3=512` minimal boundary graphs for each `c` contact,
and `4*512=2048` quotients in total.  Any omitted host edge can only help a
minor model, so checking these minimal graphs is sufficient.

## 2. Frozen certificate replay

The Z3 discovery script produced 293 monotone certificates in a
deterministic run.  Every certificate was then checked on the graph
containing only its advertised boundary edges.  The frozen JSON catalogue
is replayed by a separate solver-free implementation which:

1. reconstructs the four fixed quotient bases and all 512 boundary choices;
2. checks seven nonempty, pairwise disjoint bags using only named quotient
   vertices;
3. checks each bag by an independent connectivity search;
4. checks all nineteen required adjacencies of `K_7` except the two edges
   incident with the designated deficient branch; and
5. verifies that every one of the 2,048 minimal quotients contains at least
   one advertised certificate.

The replay was also run under `python -O`; proof checks are explicit and do
not disappear with assertions.  An earlier active verifier did use
assertions and could print a false success message under optimization.  That
implementation defect was reproduced, repaired, and is not present in the
frozen replay.

## 3. Literal expansion

Each quotient bag expands by replacing a quotient vertex with its original
connected set.  Trace contacts, packet contacts, and core adjacencies are
literal host edges, so expansion preserves connectedness, disjointness, and
all advertised bag adjacencies.  The deficient row and its two possible
nonneighbours remain explicitly named.  Hence the output is a
label-faithful `K_7^vee` model suitable for the S1 interface.

## 4. Sharp scope

The companion width-five graph in
`../barriers/hc7_exact7_rooted_k4_k7_upgrade_barrier.md` satisfies every
static hypothesis and has the asserted `K_7^vee` model but no `K_7` minor.
Thus no direct `K_7` conclusion follows from this quotient theorem.  A
well-founded near-model composition theorem or additional dynamic
criticality is still required.
