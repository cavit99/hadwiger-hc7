# Maximum-contact pentagonal-bipyramid programme: finite evidence and transfer barriers

**Status:** active YELLOW programme.  The canonical lower bound and finite
experiments below are valid; no unbounded `c_*=10` or four-colourability
theorem is proved.

**Audit:**
[`hc7_pb_max_contact_nine_four_colour_audit.md`](hc7_pb_max_contact_nine_four_colour_audit.md)

**Verifiers:**
[`hc7_pb_max_contact_nine_verify.py`](hc7_pb_max_contact_nine_verify.py) and
[`hc7_pb_paired_rooted_adversarial_probe.py`](hc7_pb_paired_rooted_adversarial_probe.py)

## 1. Setup

Let `F` be simple and five-connected.  Its vertex set is partitioned into
nonempty connected columns

```text
C_a, C_b, C_0, C_1, C_2, C_3, C_4,
```

whose contact graph is exactly the pentagonal bipyramid
`C_5 join overline(K_2)`.  Let `A,B` be vertex sets such that every column
contains an `A`--`B` path.

A **five-part `A`--`B` pack** consists of five pairwise disjoint nonempty
connected subgraphs, each meeting both `A` and `B`.  Its contact count is the
number of adjacent pairs of parts.  Let `c_*` be the maximum contact count.
A pack with contact count ten is precisely the paired-rooted `K_5` outcome.

## 2. Canonical lower bound

### Proposition 2.1

One always has `c_*>=9`.

### Proof

The five sets

```text
C_a, C_b, C_0 union C_1, C_2, C_3 union C_4
```

form a spanning five-part `A`--`B` pack.  Each double column is connected by
one rim edge, and every part contains a whole column.  The only nonadjacent
pair is `C_a,C_b`: the pole columns are nonadjacent, while pole--rim contacts
and the three required rim contacts supply the other nine pairs.  Hence the
contact count is exactly nine.  \(\square\)

This normalization is useful, but raising nine contacts to ten is the entire
unbounded allocation problem; maximality alone supplies no improving move.

## 3. Two discarded inferences from the original Grok draft

The original isolated-laboratory draft proposed two shortcuts that are not
valid.  They are retained here as explicit proof barriers so they are not
reused.

### 3.1 A singleton rim column need not have degree at most four

The pentagonal-bipyramid quotient controls which **columns** may contact a
rim column, not how many vertex neighbours occur in each adjacent column.  A
singleton rim vertex may have arbitrarily many neighbours in either adjacent
rim column and in each pole column.  Thus `delta(F)>=5` does not imply that
every rim column has at least two vertices.

### 3.2 Two portal vertices in different off-path components are insufficient

Let `R` be a pole-to-pole path in `C_0`.  Knowing only that
`C_0-V(R)` contains a vertex adjacent to `C_1` and a vertex adjacent to `C_4`
does not make

```text
(C_0-V(R)) union C_1
```

connected: the two portal vertices may lie in different components, and
components not meeting `C_1` need not attach to the displayed part.

The valid component-aware theorem requires **one component** `H` of
`C_0-V(R)` to have both rim contacts.  It then uses

```text
B1 = C_a union V(R) union every other component of C_0-V(R)
B2 = C_b
B3 = H union C_1
B4 = C_2
B5 = C_3 union C_4.
```

Connectedness and all ten adjacencies are proved and separately audited in
[`hc7_pentagonal_bipyramid_off_path_bridge_draft.md`](hc7_pentagonal_bipyramid_off_path_bridge_draft.md).
The weaker aggregate-portal condition from the original Grok draft does not
imply this construction.

Consequently the old claims called “rim columns non-trivial,” “double-bag
transfer,” and their purported general reduction are not imported as proved
results.

## 4. Exact finite laboratories

The retained verifier considers 14-vertex hosts with two adjacent vertices in
each column and exhausts every spanning five-part `A`--`B` partition.  It has
no branch-set size cutoff.  Run:

```text
/usr/bin/python3 active/hc7_pb_max_contact_nine_verify.py
```

The deterministic run checks six named hosts and 38 seeded random
five-connected hosts.  Its summary is:

```text
five_conn_checked=43 all_cstar_10=True
low_cstar_hosts=1 (all four-colourable and not five-conn)
PASS finite maximum-contact laboratory checks
```

Thus every tested five-connected two-vertex host has `c_*=10`.  The sole
tested host with `c_*<=9` is the non-five-connected, four-colourable layer-zero
host.  This is computer-assisted finite evidence only.

The broader transfer probe can be reproduced with:

```text
/usr/bin/python3 active/hc7_pb_paired_rooted_adversarial_probe.py --host audited
```

For the two named 14-vertex hosts it exhausts respectively 17,644 and 28,281
spanning packs.  Both have `c_*=10`, with 2,902 and 5,150 complete maximum
packs.  The second host also has an incomplete contact-nine local maximum
under the tested connected-piece transfers.  Hence a greedy
contact-increasing exchange rule can stop before a complete pack even when a
complete pack exists elsewhere.

Neither experiment enumerates arbitrary column sizes or proves an unbounded
reduction.

## 5. Exact remaining inference

The surviving theorem-strength question is not the canonical lower bound.  It
is to use five-connectivity and literal column ownership to turn an arbitrary
contact-nine pack into one of:

1. the component-aware off-path transfer;
2. an alternating connected column split;
3. an adjacent-rim linkage;
4. a two-column or chained absorption model;
5. a whole-host four-colouring; or
6. a strict same-form reduction with an explicit lift and a declared
   decreasing host parameter.

The finite positive data do not establish that disjunction.  Formulating the
missing step as “some improving transfer exists” is also false in the tested
exchange system because the recorded incomplete local maximum has no
contact-increasing move.

Accordingly this file contributes one elementary lower bound, two retained
finite experiments, and two explicit warnings about invalid local arguments.
It does not prove Conjectural Theorem 3.1 or the max-contact-nine
four-colourability implication.
