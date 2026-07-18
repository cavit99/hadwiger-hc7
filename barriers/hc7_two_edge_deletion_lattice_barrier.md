# The three responses of a two-edge star do not force the fourth boundary partition

**Status:** computer-assisted finite barrier; separate internal audit.  This is
not a counterexample to `HC_7`.  It shows that the three colourings obtained
from deleting one or both edges of a two-edge star have no abstract
compatibility consequence by themselves.

## Statement

There is a graph `H` with independent nominated vertices `b,i_0,i_1` whose
proper three-colourings induce exactly the following equality partitions on
those vertices:

\[
 \{b,i_0,i_1\},\qquad
 \{b,i_0\}\mid\{i_1\},\qquad
 \{b,i_1\}\mid\{i_0\}.                                  \tag{1.1}
\]

In particular, neither

\[
                 \{i_0,i_1\}\mid\{b\}                   \tag{1.2}
\]

nor the all-distinct partition occurs.  No such graph exists with fewer
than three internal vertices when the three nominated vertices are
independent.

## Construction

Add internal vertices `x,y,z` and the edges

\[
 \begin{aligned}
 E(H)=\{&bx,by,bz,
         i_0y,i_0z,
         i_1x,i_1z,
         xy\}.
 \end{aligned}                                             \tag{2.1}
\]

The vertex `z` is adjacent to all three nominated vertices.  Hence those
vertices cannot use three distinct colours.

If `i_0,i_1` have one colour and `b` has a second, both `x` and `y` are
forced to use the third colour, contrary to the edge `xy`.  This excludes
(1.2).

The three partitions in (1.1) extend as follows, with colours denoted
`0,1,2`:

\[
\begin{array}{c|ccc|ccc}
 &b&i_0&i_1&x&y&z\\ \hline
\text{all equal}&0&0&0&1&2&1\\
b=i_0\ne i_1&0&0&1&2&1&2\\
b=i_1\ne i_0&0&1&0&1&2&2.
\end{array}                                                \tag{2.2}
\]

Thus (1.1) is the complete extension relation.

## The deletion lattice

Put

\[
                         e_0=bi_0,\qquad e_1=bi_1.
\]

In `H+e_1`, only the partition \(b=i_0\ne i_1\) survives.  In `H+e_0`,
only \(b=i_1\ne i_0\) survives.  The graph `H` itself admits the all-equal
partition, while `H+e_0+e_1` is not three-colourable.  These are exactly the
three available partition types in the two-edge deletion lattice.  Deleting
both edges admits all three types in (1.1), including the all-equal response
constructed by the two connected supports in the application.

Joining every vertex of `H+e_0+e_1` to a disjoint `K_3` lifts the example to
six versus seven colours.  The two single-edge deletions realize the two
exclusive six-colour boundary partitions, and deleting both edges admits
the all-equal partition.

## Why this is not an `HC_7` counterexample

The graph `H+e_0+e_1` is four-chromatic.  It is not three-colourable by the
complete signature above, while the assignment

\[
 b=0,\qquad i_0=i_1=1,\qquad x=z=2,\qquad y=3
\]

is a proper four-colouring.  By the established `t=4` case of Hadwiger's
conjecture it has a `K_4` minor.  Joining the three vertices of the added
`K_3` produces a `K_7` minor.  The six-colour lift therefore deliberately
fails the `K_7`-minor exclusion required of a hypothetical counterexample.

The example also does not encode the five named pairwise-adjacent connected
subgraphs or the full seven-connected, contraction-critical host.  Its
exact consequence is narrower: the three boundary partitions alone do not
force a fourth
partition, a Kempe transition between the responses, or a common colouring
across a separation.  A positive theorem must use `K_7`-minor exclusion via
literal, label-preserving contacts with the named connected subgraphs; the
existence of the two connected supports merely constructs the all-equal
response and does not couple it to the two exclusive responses.

## Verification

Run

```text
python3 barriers/hc7_two_edge_deletion_lattice_barrier_verify.py
```

The script checks the complete boundary signature of (2.1), the effect of
adding either or both star edges, and exhaustive nonexistence with at most
two internal vertices.
