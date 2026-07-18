# Audit of the missing-five-row three-path barrier

**Verdict:** **GREEN** for the finite, computer-assisted barrier exactly as
stated.  This is a separate internal audit, not external peer review, and
not a counterexample to `HC_7`.

## Audited revision

- barrier: `barriers/hc7_three_path_missing_five_row_barrier.md`
- barrier SHA-256:
  `687e29c27fdcb2e2af4634de061064dce5ac3ef97286594d35faf7da94334a57`
- checker: `barriers/hc7_three_path_missing_five_row_barrier_verify.py`
- checker SHA-256:
  `c67fd2feb75dbddd326bcd47ae076c8b73fd1a6c9a0316ac8b314fadc26d3991`

## Verdict

The displayed eighteen-vertex graph has the asserted cycle, colouring,
three-path, cyclic-set, and far-side wheel geometry.  It is three-connected
and has no `K_7` minor.  Adding any colouring-compatible edge from `b_0` to
the far-side wheel creates a `K_7` minor.  Hence it refutes the stated local
inference when the fifth labelled far-side contact is omitted.

The barrier hash above differs from the line-by-line audited revision
`68c5e51c6a21ae4932c3152d89cfba70e9b3562e6af28a34dd4fd1eb52670302`
only because its status line was updated to record this GREEN audit; the
construction and mathematical claim are unchanged.

## Construction and connectivity

The checker constructs exactly the edges in Section 2 and no others.  Direct
enumeration of all vertex sets of order at most two found no separator.  The
set

\[
 \{y_0,y_1,y_3\}
\]

is a three-vertex cut: after its deletion `y_4` is isolated.  Thus the host
has vertex-connectivity exactly three.  The induced graph on
`y_0,\ldots,y_4` is the wheel with a four-cycle rim and has connectivity
three.

The far-side wheel is adjacent to `u_0` through `y_1,y_2,y_3`, to
`u_1,u_2,u_3,b_2` through `y_1`, and to `b_1` through `y_1,y_2,y_3`.  It has
no edge to `b_0`.  It therefore meets exactly the six claimed vertices of
`U\cup B`.

## Colouring and path geometry

After deleting `b_1u_0`, every listed edge has endpoints of different
colours in (2.2).  In particular,

- `I\cup\{b_1\}` has colour 0;
- `J\cup\{b_2\}` has colour 1; and
- the internal vertices `y_1,y_2,y_3` of the three displayed
  `b_1`--`u_0` paths have colours 2, 3, and 4, respectively, none of which
  occurs on `U\cup B`.

The five sets in (2.4) are disjoint and connected.  Consecutive sets are
adjacent through the four-cycle or five-cycle edges, including `x_3x_4`
and `x_4x_0` at the end.  They contain `u_0,u_1,u_2,u_3` separately and
partition the five vertices of `X`.

The barrier graph itself is not seven-chromatic: recolouring `b_1` from 0
to 1 in (2.2) gives a proper six-colouring of the undeleted graph.  This is
an additional explicit reason that the example is outside the hypothetical
counterexample class.

## Exact `K_7`-minor check

For each of seven branch-set labels, the SMT encoding selects one root and a
possibly larger assigned vertex set.  Each assigned nonroot vertex must have
a same-label neighbour of strictly smaller integer depth.  Following these
strictly decreasing depths reaches the unique root, so each nonempty branch
set is connected.  A vertex is assigned to at most one branch set, and each
pair of labels is constrained to have an edge between its selected sets.

Conversely, any `K_7`-minor model satisfies the encoding: order the seven
branch sets by chosen root index, assign each vertex its branch label, and
use distances from the root as depths.  Thus `UNSAT` is exactly equivalent
to `K_7`-minor exclusion; it is not a bounded-depth heuristic.  The solver
returned `UNSAT` for the base graph.  A timeout or any result other than
`SAT`/`UNSAT` now raises an explicit error.

For reproducibility, the augmented instances returned the following
checkable `K_7` models (one line per added edge):

```text
b0-y1:
{b0,x4} | {b2} | {u1,v,x1} | {u2,u3,x3} |
{u0,x0,y0,y3} | {b1,x2,y2} | {y1,y4}

b0-y2:
{b2,x4} | {u0,x0} | {u1,u2,x1} | {u3,x3} | {y1} |
{b0,v,y2} | {b1,x2,y0,y3,y4}

b0-y3:
{b2,x4} | {u0,u2,u3,x0} | {v} | {u1,x1,y1} | {x2,x3} |
{b0,y0,y3,y4} | {b1,y2}

b0-y4:
{b0,v} | {b1,y2} | {b2,x4} | {u1,x1} | {x2} |
{u2,y0,y1,y4} | {u0,u3,x0,x3,y3}
```

The checker independently validates nonemptiness, disjointness,
connectedness, and all pairwise adjacencies of each extracted model.

## Checker replay

All correctness checks use an explicit `require` function and remain active
under optimized Python.  Both normal and optimized runs completed
successfully with the same output:

```text
python3 barriers/hc7_three_path_missing_five_row_barrier_verify.py
python3 -O barriers/hc7_three_path_missing_five_row_barrier_verify.py

base: exact K7-minor exclusion verified
b0-y1: K7 model verified
b0-y2: K7 model verified
b0-y3: K7 model verified
b0-y4: K7 model verified
GREEN: the one-missing-contact barrier is verified
```

## Exact scope not refuted

The example has connectivity three, is six-colourable, and is not asserted
to be contraction-critical.  Its far-side subgraph misses `b_0` and does not
realize five pairwise adjacent labelled connected subgraphs.  It therefore
does not refute a theorem that uses seven-connectivity, seven-chromaticity,
contraction-critical proper-minor colourings, or the complete five-subgraph
geometry.  Its role is only to show that three paths, local
three-connectivity, and six of seven far-side contacts do not suffice.
