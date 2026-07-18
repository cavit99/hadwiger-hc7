# Audit: the two-edge deletion lattice barrier

## Verdict

**GREEN** at the exact revisions

```text
3d931f5f356c28a101dc279bd3ad0b598435ed386df7094d7b8c04d01b8c0a37  barriers/hc7_two_edge_deletion_lattice_barrier.md
6f6c6145c42e09d192007e5c15f488655870a0365af724ec7fa58a32034e8bd2  barriers/hc7_two_edge_deletion_lattice_barrier_verify.py
```

The verifier runs successfully with output

```text
GREEN: exact three-state deletion lattice verified
GREEN: no realization with at most two internal vertices
```

The five possible equality partitions of the three independent nominated
vertices reduce exactly as claimed: the common neighbour `z` excludes the
all-distinct partition, and the edge `xy` excludes
\(i_0=i_1\ne b\); the three remaining partitions have the displayed proper
colourings.  Adding `e_0`, `e_1`, or both gives the stated deletion-lattice
signatures.  The exhaustive search checks every labelled simple graph with
independent terminals and zero, one, or two internal vertices.

The added four-colouring

```text
b=0, i_0=i_1=1, x=z=2, y=3
```

is proper, while the empty three-colour signature proves that
`H+e_0+e_1` is exactly four-chromatic.  Joining a disjoint `K_3` therefore
lifts the single- and double-deletion graphs to six colours and the full
graph to seven colours.  The established `t=4` case supplies a `K_4` minor
in `H+e_0+e_1`; together with the three singleton join vertices this is a
`K_7` minor.  The source consequently states its trust boundary correctly:
the gadget refutes only an abstract boundary-partition inference and is not
a counterexample to `HC_7` or to a theorem using the full labelled host
structure.
