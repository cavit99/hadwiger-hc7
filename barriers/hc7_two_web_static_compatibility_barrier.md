# Static barrier to composing the two four-terminal webs

**Status:** computer-assisted finite barrier, with a deterministic verifier.
This note refutes a compatibility principle based only on the two cleaned
four-terminal webs.  It does not refute a theorem that also uses
seven-connectivity, contraction-critical colouring transitions, or further
attachments outside the displayed configuration.

## 1. The canonical quotient

Let `Q` have vertex set `{0,...,11}`.  On `{0,...,5}` take

- a `K_4` on `{0,1,2,3}`;
- the edge `4-5`; and
- the edges `0-4,1-4,2-4,3-5`.

Thus the four singleton branch sets `{0},{1},{2},{3}`, together with
`{4,5}`, form a `K_5`-minor model.  On `{6,...,11}` take `K_6` minus the
edge `10-11`.  Finally add the six matching edges

\[
 0\!-6,\quad1\!-7,\quad2\!-8,\quad
 3\!-10,\quad4\!-11,\quad5\!-9.             \tag{1.1}
\]

The vertices correspond respectively to

\[
 (a_0,a_1,a_2,a_3,x,y,b_0,b_1,b_2,r,p,q).
\]

The missing edge `10-11` of the right-hand `K_6^-` is therefore aligned
with the nonedge `3-4` on the left.

## 2. One bridge to each exceptional rail is insufficient

Delete the three matching edges `5-9,3-10,4-11`.  Replace them with

\[
 P_5=5-12-13-9,\qquad P_3=3-14-10,\qquad P_4=4-15-11.       \tag{2.1}
\]

There are two possible relative orders for a bridge to `P_3` and a bridge
to `P_4` along the common path `P_5`:

\[
\begin{array}{c|cc}
 &P_5\text{--}P_3&P_5\text{--}P_4\\ \hline
G_{34}&12-14&13-15\\
G_{43}&13-14&12-15.
\end{array}                                                \tag{2.2}
\]

Both graphs have sixteen vertices and thirty-seven edges.  Neither has a
`K_7` minor.

For `h=3,4`, delete the other four linkage paths and all unused vertices of
the two displayed six-vertex supports, as in the cleaned graph `H_h` of the
bridge-augmentation theorem.  In either `G_34` or `G_43`, the resulting
graph is the frame cycle on

\[
                    (y,r,t_h,s_h)
\]

together with one chord joining an internal vertex of `P_5` to an internal
vertex of `P_h`.  It is planar with the four terminals in that cyclic order
on its outer face.  Hence it has no pair of vertex-disjoint paths joining
`y` to `t_h` and `r` to `s_h`.  The verifier also checks this directly by
enumerating the two path families.  Thus both four-terminal instances are
crossless (and already have explicit web embeddings) in both relative
orders.

The two graphs have vertex-connectivity three.  They are therefore static
quotient counterexamples only: they show that the two web certificates and
one bridge in each class do not compose by themselves.

## 3. Exact `K_7`-minor exclusion

The verifier uses the exact connected-branch-set detector from the adjacent
six-link classification.  For graphs of order at most twelve it enumerates
all possible seven-bag models.  For either sixteen-vertex graph above, it
uses the following exact recurrence.

If a vertex `v` has degree less than six, then `v` cannot be a singleton bag
of a `K_7`-minor model.  Every such model therefore either avoids `v`, or
contains an edge `vw` inside the branch set containing `v`.  Consequently

\[
 K_7\preccurlyeq G
 \quad\Longleftrightarrow\quad
 K_7\preccurlyeq G-v
 \ \text{or}\
 K_7\preccurlyeq G/vw\text{ for some }w\in N(v).           \tag{3.1}
\]

Repeated use of (3.1) reduces every branch to at most twelve vertices; at
the outset the four new subdivision vertices have degree three (as does
`y`).  The recursion then invokes the independently audited twelve-vertex
detector.  It returns `False` for both `G_34` and `G_43`.

## 4. Seven-connectivity cannot be added on the twelve vertices

There is a complementary finite positive result.  Keep the six linkage
paths as the six matching edges of `Q`, and add any subset of the thirty-five
missing edges.  Require both cleaned four-terminal instances to stay
crossless.  Since each cleaned graph then has only its four terminals, this
is exactly the pair of constraints

\[
 \neg(5\!-10\ \wedge\ 3\!-9),\qquad
 \neg(5\!-11\ \wedge\ 4\!-9).                  \tag{4.1}
\]

Among these edge-supergraphs, no `K_7`-minor-free graph has minimum degree
at least seven.  The exhaustive search visits 4,633 distinct partial
edge-sets (4,679 recursive calls before memoization) and applies the exact
twelve-vertex minor detector at every retained state.

The search is complete for the following reason.  At a partial graph choose
a vertex `v` with maximum positive degree deficit

\[
                         d=7-d(v).
\]

Every completion of minimum degree at least seven contains some `d`-subset
of the still-available edges incident with `v`.  The search branches over
all such subsets and may add further edges at later steps.  It prunes only
when (4.1) fails, a `K_7` minor has already appeared, or too few incident
edges remain.  These properties are monotone in precisely the direction
used by the pruning.

This census proves that the static direct-link quotient cannot itself be
completed to a seven-connected counterexample.  It says nothing about an
expanded linkage whose internal vertices receive additional attachments;
that is exactly where a valid host-level two-web theorem must use
seven-connectivity.

## 5. Reproduction

Run from the repository root:

```sh
uv run barriers/hc7_two_web_static_compatibility_barrier_verify.py
```

Expected final output:

```text
mixed_order_34 vertices 16 edges 37 connectivity 3 k7_minor False
mixed_order_43 vertices 16 edges 37 connectivity 3 k7_minor False
direct_link_states 4633
direct_link_recursive_calls 4679
direct_link_minimum_degree_seven_completion False
GREEN: static two-web barriers and direct-link census verified
```

## 6. Exact implication

The following statement is false:

> Two crossless cleaned four-terminal webs sharing `P_5`, with one genuine
> bridge from `P_5` to each exceptional path, always yield a `K_7` minor.

The relative order of the two bridges on `P_5` does not repair it.  A viable
composition theorem must use additional host information—most plausibly
seven-connectivity to force further attachments or contraction-criticality
to transfer a boundary-colouring pattern.  In the direct-link quotient,
seven-connectivity is not merely absent: minimum degree seven is already
impossible without creating a `K_7` minor.
