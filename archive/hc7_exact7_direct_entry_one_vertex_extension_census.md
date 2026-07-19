# One-vertex critical-triangle extensions of the direct-entry barrier

**Status:** computer-assisted finite experiment; written and unaudited.  This
is not an unbounded theorem and does not prove `HC_7`.

The audited
[six-connected direct-entry barrier](../barriers/hc7_exact7_bichromatic_path_full_subgraphs_barrier.md)
cannot be upgraded to a seven-connected `K_7`-minor-free example by adding
one role-labelled critical-triangle vertex while keeping its old graph,
boundary colouring, separation, path, and two selected boundary-full
connected subgraphs fixed.  Every seven-connected extension in this exact
finite class has the same explicit spanning `K_7`-minor model.

The deterministic census is
[`hc7_exact7_direct_entry_one_vertex_extension_census.py`](hc7_exact7_direct_entry_one_vertex_extension_census.py).

## 1. Extension class

Retain all vertices, edges, colours, and names of the base barrier.  Its
seven-boundary is `S={0,...,6}`, its four-vertex open shore is

```text
A={a1,a2,c1,c2},
```

and its other open shore is `{b}`.  The distinguished boundary vertex is
`v=1`, of colour zero.

Add one new vertex `w`, also of colour zero, to one open shore.  Choose an
old outer endpoint `y` in that shore such that `vy` is already an edge.
There are exactly three role-labelled possibilities:

```text
(A,a1),  (A,c2),  ({b},b).
```

Require the triangle edges `vw,vy,wy`.  Treat `vw,vy` as the two operation
edges.  All other edges incident with `w` are arbitrary subject to the
following requirements.

1. The original separation is retained: an `A`-side `w` is nonadjacent to
   `b`, while a `{b}`-side `w` is nonadjacent to every vertex of `A`.
2. The fixed colouring is proper after deleting `vw`.
3. In the common deletion of `vw,vy`, the two-colour component containing
   `w` is exactly `{w,y}`.  Switching that component gives a proper
   colouring after deleting `vy`.
4. Both operation-edge colourings have exact contraction trace: no other
   neighbour of the contracted pair has its common colour.

These conditions enumerate every possible neighbourhood of `w` in this
fixed role-labelled class.  The old bichromatic path

```text
4-a2-c1-6
```

and the two selected boundary-full connected subgraphs

```text
{a1,a2},  {c1,c2}
```

remain unchanged.

Call an extension **strictly same-shore** when `{w}` is not itself
boundary-full.  Since the two old selected subgraphs cover all old vertices
of `A`, this is exactly the condition that adding `w` has not supplied a
third disjoint boundary-full connected subgraph in that shore.

## 2. Exhaustive census

The role-labelled counts are

| shore / old endpoint | candidate neighbourhoods | exact response pairs | seven-connected | strictly same-shore |
|---|---:|---:|---:|---:|
| `A / a1` | 512 | 256 | 4 | 4 |
| `A / c2` | 512 | 512 | 4 | 3 |
| `{b} / b` | 64 | 64 | 0 | 0 |

Thus there are eight seven-connected role-labelled extensions, representing
six distinct host graphs.  Seven of the eight retain the strict same-shore
obstruction.

Every one of the eight contains the following fixed spanning `K_7`-minor
model:

```text
{0,6,c1,w}, {1,a1}, {2,b}, {3,c2}, {4}, {5}, {a2}.
```

The script checks disjointness, connectedness, spanning, and all twenty-one
branch-set adjacencies for every extension, rather than inferring the model
from a minor oracle.

There is also no seven-chromatic survivor.  Every seven-connected extension
places `w` in the `A`-shore, and the following one fixed five-colouring is
proper in all of them:

```text
{w,b} | {0,a2,c2} | {2,5} | {3,a1,c1} | {1,4,6}.
```

The `{b}`-shore role never reaches seven-connectivity.

## 3. Consequence and exact scope

This closes the one-added-vertex version of the fixed-skeleton test:

> A role-labelled one-vertex extension retaining the exact separation,
> two operation-edge responses, old direct path, and selected full connected
> subgraphs is either not seven-connected or contains the displayed
> `K_7`-minor model.

It does not prove the proposed label-preserving first-hit principle in an
arbitrary host.  It does not allow changes among the old vertices, a larger
critical component, two new private-path vertices, or a different exact
boundary interface.  Those would require separately stated extension
classes rather than extrapolation from this census.

Run from the repository root with

```text
python3 archive/hc7_exact7_direct_entry_one_vertex_extension_census.py
```

Expected output:

```text
role=A/a1: candidates=512 responses=256 seven_connected=4 strict_same_shore=4
role=A/c2: candidates=512 responses=512 seven_connected=4 strict_same_shore=3
role=B/b: candidates=64 responses=64 seven_connected=0 strict_same_shore=0
seven-connected role-labelled extensions=8 distinct_hosts=6
strict direct-entry extensions=7
all seven-connected extensions: fixed spanning K7 model=yes
all A-shore extensions: fixed five-colouring=yes
ALL CHECKS PASSED
```
