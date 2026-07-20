# A five-connected nonplanar nonsplit pentagonal-bipyramid expansion

**Status:** barrier/counterexample to a structural intermediate claim;
computer-checked by
[`hc7_pentagonal_bipyramid_nonplanar_nonsplit_expansion_verify.py`](hc7_pentagonal_bipyramid_nonplanar_nonsplit_expansion_verify.py).
It does not refute a theorem whose outcomes include a label-preserving
rooted `K_5` model: the example contains such a model explicitly.

## Claim refuted

The following two-outcome statement is false.

> Every four-connected nonplanar graph partitioned into seven connected
> columns with pentagonal-bipyramid contact graph either has a four-vertex
> cut or admits an alternating connected split of one column.

The counterexample is five-connected, so it has no four-vertex cut, and
none of its columns has an alternating connected split.

## Construction

Let `I` be the icosahedral graph and add its missing edge `1-7`; call the
result `F`.  Partition its vertices into

\[
\begin{array}{c|c}
A_0&\{2\}\\
A_1&\{4\}\\
R_0&\{6\}\\
R_1&\{3\}\\
R_2&\{9,10\}\\
R_3&\{7,8,11\}\\
R_4&\{0,1,5\}.
\end{array}
\]

The added edge runs from `R_4` to the adjacent rim column `R_3`, so the
column-contact graph remains exactly the pentagonal bipyramid.  The
icosahedron is five-connected, and adding an edge cannot lower
connectivity.  It is a maximal planar graph, so adding the missing edge
`1-7` makes `F` nonplanar.

The verifier enumerates all six unordered connected bipartitions of the
three nonsingleton columns and checks the cyclic incidence criterion.  No
split has alternating attachments.  The four singleton columns cannot be
split.

## Why the rooted-model outcome is indispensable

The example does contain a `K_5` minor whose five branch sets meet five
distinct selected column representatives.  One explicit model is

\[
 \{4\},\quad \{6\},\quad \{2,3,8\},\quad
 \{0,5,11\},\quad \{1,7,10\}.
\]

Each displayed set is connected, and the five sets are pairwise adjacent.
They collectively contain selected representatives from all seven columns;
in particular five distinct branch sets can be assigned five distinct
column labels.  A second distributed model is, for example,

\[
 \{3,9\},\quad \{2,6\},\quad \{4,5\},\quad
 \{0,8,11\},\quad \{1,7,10\}.
\]

This second display is only another model in the core; no claim is made
about arbitrary external root portals.  Thus the example isolates the
correct third outcome.  Nonplanarity and
five-connectivity do not force a geometric split or a cut; they can instead
manifest directly as a column-distributed `K_5` model.  Any viable host
theorem must retain that rooted-model alternative.

## Trust boundary

This is a twelve-vertex core, not a seven-chromatic host.  It refutes only
the split-or-cut inference.  It is positive evidence, not a proof, for the
stronger trichotomy

\[
 \text{column-distributed rooted }K_5
 \quad\text{or}\quad
 \text{alternating split}
 \quad\text{or}\quad
 \text{four-cut}.
\]
