# Internal audit of three-column chained absorption

**Verdict:** **GREEN** for Theorem 2.1 and its sixteen-vertex application.

**Audited source:**
[`hc7_pentagonal_bipyramid_three_column_chained_absorption.md`](hc7_pentagonal_bipyramid_three_column_chained_absorption.md)

**Audited source SHA-256:**
`8626c51e077675b90bdbb24330b58a28fd89f43d1d3f1dc7d0affeb1abb4ee31`

**Audit type:** separate internal mathematical cold audit, followed by an
exact-diff review of the audit-link status edit.  This is not external peer
review.

## Theorem audit

The five proposed bags are pairwise disjoint.  The pieces taken from each of
`C_b`, `C_{i+1}`, and `C_{i+2}` are disjoint by (2.1), and all remaining
pieces lie in different columns.  The bags `C_a,C_i` are connected columns;
connectedness of `D_1,D_2,D_3` is an explicit hypothesis.

The seven contacts in (2.3) supply exactly the seven nonautomatic
adjacencies.  The remaining three are literal quotient contacts:

- `C_a C_i` and `C_a C_{i+3}` are pole--rim contacts;
- `C_i C_{i+4}` is a rim-cycle contact.

Thus the table in the proof covers all ten unordered pairs, without using a
completion edge or an inferred contact.  The first two bags meet both root
sets because they are whole columns.  The sets `D_1,D_2` meet both by
hypothesis, and `D_3` contains the two whole columns
`C_{i+3},C_{i+4}`.  The conclusion is therefore a paired-rooted `K_5` model.
The cyclic, rim-reversal, and pole-interchange symmetries preserve every
hypothesis after relabelling.

## Application audit

For the displayed sixteen-vertex graph, the five bags are disjoint and their
induced subgraphs are connected.  Each of the ten edges in (3.4) joins the
corresponding pair in the theorem's adjacency table.  The root sets in (3.5)
are disjoint, contain one vertex of every column, and meet every displayed
bag.  The assignment

```text
P_b={2}, Q_b={3}, P_1={7}, Q_1={15}, Q_2={8}, Z_2={9}
```

satisfies all three connectedness conditions and all seven contacts in
(2.3).  The insertion-time notation for vertex `14` was checked in the final
revision: `N_{F-15}(14)={2,3,6,7,8}`, while the final graph also has edge
`14 15`.

The construction was independently reconstructed from the prose without
importing the retained verifier.  That reconstruction confirmed all ten edge
witnesses and all literal root intersections.

## Scope

The theorem is a sufficient, root-sensitive allocation mechanism.  It does
not assert that every pentagonal-bipyramid expansion admits these pieces, and
it does not prove Conjectural Theorem 3.1.  In particular, `D_1,D_2` must meet
the actual root sets; the construction is not uniform over arbitrary choices
of one endpoint per column.  There are no unresolved assumptions in the
stated theorem or its displayed application.
