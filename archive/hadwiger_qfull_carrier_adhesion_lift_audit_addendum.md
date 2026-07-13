# Audit addendum: arbitrary one/two-carrier adhesion lift

## Verdict

**GREEN AS STRENGTHENED** for Theorems 3.3 and 3.4.

For Theorem 3.3, the two-gate shore theorem supplies a gate set of order
at most two.  If no component after deleting it meets both quotient
incidence sets, every incidence-to-incidence path uses the gate, so the
faithful lift is exactly `Q union S_0 union Z`, of order at most six.
If a component straddles, the new Corollary 2.3 in the shore/gate note
shows that it meets at most one neutral portal class, stronger than the
original claimed darkness.

For Theorem 3.4, the carriers are disjoint, so their gate sets are
automatically disjoint.  If their union separates the combined network,
the faithful separator has order at most seven.  Seven-connectivity
forces equality, hence both individual gate sets have order two.  If the
union does not separate, one component of the combined network after gate
deletion meets both quotient shores.  No carrier-by-carrier darkness is
claimed for that combined component, correctly.

Theorems 3.3--3.4 close the following genuine infinite family:

* every one-carrier quotient cut whose carrier either has the typed split
  or whose gate has no straddling lobe;
* every two-carrier quotient cut whose combined gate union separates and
  has fewer than four vertices.

The exact residues are a portal-monochromatic straddling lobe in the
one-carrier case, and either a combined straddler or four distinct gates
on an exact order-seven cut in the two-carrier case.

The local counterarchitecture in
`hadwiger_gate_a_combined_network_round.md` verifies that individual gate
lobes can combine through cross-edges into nonplanar systems with
different missing labels.  Its verifier reports:

```text
typed shore pairs: none in either star
combined lobe profiles: [(1, [1]), (1, [3]),
                         (6, [1, 2]), (6, [2, 3])]
combined L-R separator order: 6
nonplanar straddling systems: 2
```

Thus the exact missing hypothesis is state-forcing cross-lobe expansion:
a non-rural interaction between differently deficient lobes must produce
a full-row shore split or a labelled target minor.  Gate size and linkage
capacity alone do not prove this.

