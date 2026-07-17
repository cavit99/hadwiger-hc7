# Two concentrated bridge fans defeat attachment-count descent

**Status:** written infinite barrier with a deterministic finite-core
checker.  This is not a counterexample to `HC_7`: the displayed graphs are
not seven-connected or contraction-critical.  It refutes the proposed
local implication after seven-connectivity has been used only to obtain
seven or more first-hit vertices.

## 1. Normalized linkage

Use the normalized `3+1` configuration and the six disjoint paths

\[
 P_i:a_i-b_i\ (0\le i\le2),\qquad
 P_3:a_3-p,\quad P_4:x-q,\quad P_5:y-r
\]

from the
[six-terminal crossing decoder](../results/hc7_disjoint_k6minus_six_terminal_crossing_decoder.md).
The vertices `a0,a1,a2,a3` induce a clique, `xy,a3y` are edges, `x` is
adjacent to `a0,a1,a2`, and the six right endpoints induce `K6-pq`.

Fix an integer `k>=1`.  On each of two selected linkage paths, replace its
edge by a path with `k` internal vertices.  Add two nonadjacent vertices
`c,d` as follows.

- `c` is adjacent to `a3`, `x`, and every internal vertex of the first
  selected path;
- `d` is adjacent to `y`, a vertex `z in {p,q,r}`, and every internal
  vertex of the second selected path.

Thus `a3-c-x` and `y-d-z` are the two clean repaired-contact paths.  The
vertices `c,d` represent two distinct components outside the linkage
skeleton.  Each has exactly `k+2` distinct skeleton neighbours, so for
`k>=5` both meet the seven-attachment threshold forced by
seven-connectivity.  In the robust cases below each component attaches to
at least two of the six linkage paths, so endpoint-preserving stable
rerouting does not discard it as a one-path bridge.

Up to permuting `P0,P1,P2`, take the first selected path to be `P0`.  The
following seven choices are `K7`-minor-free for every `k`:

| `z` | permitted second selected path |
|---|---|
| `p` | `P3` or `P5` |
| `q` | `P4` or `P5` |
| `r` | `P3`, `P4`, or `P5` |

The choices `P3` and `P4` in the last row also satisfy the two-path
stability condition; `P5` is retained to display the full symmetry of the
finite core.

## 2. Uniform exclusion of a `K7` minor

For one row of the table, form a fourteen-vertex **completed core** as
follows.  Restore the two direct linkage edges.  Keep `c,d`, and make `c`
adjacent to both ends of its selected linkage edge and `d` adjacent to both
ends of its selected linkage edge.  The other four compulsory neighbours
`a3,x,y,z` are retained.  The adjacent exact checker verifies that each of
the seven completed cores has no `K7` minor.

Now add back the first subdivided path together with its fan centre `c`,
temporarily retaining the three filling edges on the vertices

\[
        \{c,\text{the two ends of the selected linkage path}\}.
\]

This added graph is a wheel and meets the completed core in a triangle.
Do the same with the `d`-fan.  The resulting supergraph is obtained from
three `K7`-minor-free graphs by two clique-sums of order three.

A `K7` model cannot straddle such a clique-sum.  Indeed, after deleting the
at most three model branch sets which meet the adhesion clique, all
remaining branch sets must lie on one side: branch sets in opposite open
sides have no edge between them.  The portions of the at most three
adhesion-meeting branch sets on the other side can be replaced inside the
adhesion clique, so a `K7` model would already occur in one summand.  This
is impossible because the completed core is `K7`-minor-free and each wheel
is planar.

The graph in Section 1 is a subgraph of this clique-sum supergraph (delete
the filling triangle edges).  It is therefore `K7`-minor-free for every
`k>=1`.

## 3. What the barrier rules out

The following proposed extracted-subgraph principle is false:

> Two distinct off-skeleton components, one containing an `a3`--`x`
> connector and one containing a `y`--`z` connector, force a `K7` minor as
> soon as each has at least seven distinct first hits on the six-linkage.

The failure persists with arbitrarily many first hits and, in the robust
rows, with each component attached to several linkage paths.  The first
hits can all be concentrated along one additional path on each side; that
ordered fan is separated from the fixed quotient by a triangle and hence
cannot be defeated by attachment count, first/last hit selection, or
stable-bridge incidence alone.

This does **not** refute a theorem using the full hypotheses of a minimal
`HC_7` counterexample.  The fan vertices have low degree and the examples
are not seven-connected.  A successful repaired-contact exchange must use
the additional edges forced at those fan vertices, a proper-minor colouring
transition, or a global fixed-pair conclusion.  Merely increasing the
number of first hits cannot supply a strict host-defined rank.

## 4. Verification

Run from the repository root:

```sh
python3 barriers/hc7_repaired_contact_two_fan_barrier.py
```

Expected output:

```text
completed_cores 7
finite_family_replay 49
GREEN: all two-fan cores and replay members are K7-minor-free
```

The checker imports the independently audited exact `K7` detector from the
six-terminal decoder.  It checks all seven completed cores and replays the
first seven members of every infinite family.  The unbounded conclusion
comes from the written clique-sum argument, not from extrapolating the
finite replay.

Verification hashes for this revision:

```text
barrier checker  a0e32dedc4d1b48a618966464f1204990a6dd0b3032c1d7fcbdfcee28c65c11a
imported decoder 02a37655bb2c3e4ef2a5b125deecaac41431530e7cfe5a921616406e45095b81
```
