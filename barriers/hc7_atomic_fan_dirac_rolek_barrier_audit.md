# Independent audit of the atomic fan Dirac/Rolek--Song barrier

**Verdict:** GREEN for the exact revisions listed below.

## Audited revisions

- statement: `hc7_atomic_fan_dirac_rolek_barrier.md`
- statement SHA-256:
  `d246309c35bcf8cdf720ad4be4ff75d73431abdf8a46de7bbe9fd281260ea38a`
- checker: `hc7_atomic_fan_dirac_rolek_barrier.py`
- checker SHA-256:
  `cb651474bd11eaca1a15c46ea2f372c3b99bbd93408b131e989ebb4514a53742`

## Replay

Running

```sh
python3 barriers/hc7_atomic_fan_dirac_rolek_barrier.py
```

returned exactly

```text
rows 7
degree_seven_negative_counts (11, 11, 11, 11, 11, 11, 11)
degree_eight_negative_counts (2, 2, 2, 2, 2, 2, 2)
rolek_core_path_pairs 28
certificate_digest 0bfc8eb21a675c644c86a639df2bcf699e4f373bc9bd9abc40dc50e51d51d86c
GREEN: atomic Dirac residues and internal Rolek path pairs verified
```

The first row was also replayed separately.  It returns the two stated
degree-eight neighbourhoods and four explicit disjoint path pairs.

## Mathematical checks

The atomic graph is obtained literally by deleting the artificial edge
`a0-b0`, inserting the path `a0-w-b0`, and retaining the two edges from
the first fan centre to the ends together with `cw`.  Thus the three base
neighbours of `w` in the statement agree with the checker.

There are eleven eligible additional core vertices.  The checker tests all
`binom(11,4)` degree-seven choices in each of the seven second-fan rows with
the exact deletion/contraction minor detector already retained for the
audited six-terminal decoder.  Every negative choice has neighbourhood
independence number three.  Monotonicity of minor containment justifies
forming the degree-eight candidates from five-sets all of whose four-sets
are negative; the exact search leaves precisely the two displayed
five-sets.  Every six-set contains a positive four-set, so the
degree-at-least-nine conclusion is valid without a further host-order
assumption.

For a noncomplete seven-contraction-critical graph, Dirac's neighbourhood
bound is

\[
                 \alpha(N(w))\le d(w)-7+2.
\]

It therefore excludes every negative degree-seven completion, while the
finite minor calculation excludes degree at least nine under the explicit
assumption that `w` has no neighbours outside the displayed core.  The two
degree-eight patterns attain equality with independence number three.

For each of the two independent triples in the statement, the two named
terminal pairs are disjoint missing edges among the five remaining
neighbours.  The Rolek--Song equality-case lemma therefore supplies the
corresponding two disjoint external paths.  The checker searches paths
whose internal vertices avoid `N[w]`, verifies vertex-disjointness, and
finds all twenty-eight required pairs inside the atomic graph itself.

## Scope

The finite cores are not seven-connected or contraction-critical.  The
result does not refute an escape theorem using global seven-connectivity,
additional proper-minor colouring transitions, or a ranked separation.
It refutes only the proposed inference from the local degree bound,
Dirac equality, and the standard equality-case external paths to a path
leaving the concentrated fan.
