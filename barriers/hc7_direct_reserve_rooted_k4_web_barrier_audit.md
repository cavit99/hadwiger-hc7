# Independent audit: direct-reserve rooted-`K_4` web barrier

**Verdict:** GREEN.

**Barrier SHA-256:**
`980d68148e5d890c84ce9b6f949f840f524e69262b19896600f4edd7fd62446d`

**Verifier SHA-256:**
`d3043d85ad8e156f8f80d64c1b819b9d507e6d8ddee551b5a1e251d13a9b1afb`

The solver-free verifier was rerun independently.  The following claims
were checked.

1. The displayed four bags are connected and pairwise disjoint, and their
   only missing adjacency is the `y-r` pair.
2. Assigning each of the three nonroots to one of four root bags or to the
   unused state exhausts all possible rooted models.  None is a rooted
   `K_4`.
3. For every set `Z` of fewer than four deleted vertices, every component
   of `J-Z` contains a surviving root.  This is equivalent here to the
   asymmetric rooted internal-four condition used by the programme.
4. In the seven-boundary extension, `zu` is the unique `A-u` edge,
   `A-z` is connected and `W`-full, and every connected nonempty subset of
   `A` satisfies the stated relative seven-cut inequality.
5. The paths `xy` and `r-a-u` are the required disjoint parity-bad paths.
   The reserved component `{a,u}` has the two stated contacts.
6. The displayed adaptive carriers are disjoint, connected and adjacent;
   their two seed sets are independent and partition `H-r`; and every seed
   has its required literal carrier contact.

Thus the example really refutes the unconditional rooted-`K_4` upgrade,
while exiting through an allowed adaptive-carrier outcome.  It is not an
`HC_7` counterexample and is not claimed to satisfy global
minor-criticality or the rich-shore hypotheses.
