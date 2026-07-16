# Label-preserving six-linkage classification beside a `K_6^-`

**Status:** computer-assisted finite theorem with a deterministic exact
verifier; independently audited in
[`hc7_disjoint_k6minus_support6_linkage_classifier_audit.md`](hc7_disjoint_k6minus_support6_linkage_classifier_audit.md).
This note does not prove the support-six transversal theorem or `HC_7`.

## 1. Configuration

Let `Q={0,1,2,3}` induce a `K_4`, let `45` be an edge, and assume that
each vertex of `Q` is adjacent to at least one of `4,5`.  The five branch
sets

\[
             \{0\},\{1\},\{2\},\{3\},\{4,5\}
\]

form a `K_5`-minor model on six vertices.  We impose the irredundancy
condition that neither `Q+4` nor `Q+5` is a `K_5`; equivalently, each of
`4,5` has a non-neighbour in `Q`.

Let `B={6,...,11}` induce `K_6^-`, with unique missing edge `10 11`.
Suppose the two displayed six-sets are joined by six pairwise
vertex-disjoint paths with distinct ends exhausting both six-sets.  After
contracting every such path to one edge, these edges form a perfect
matching.  The **bare matching quotient** retains exactly the edges of the
two displayed support graphs and these six matching edges; all other host
edges are deleted before contraction.  Let

\[
       \{r,s\}\subseteq Q\cup\{4,5\}
\]

be the two vertices matched to `10,11`.

The purpose of this note is to retain the labels discarded by the earlier
six-path quotient counterexample.

## 2. Bare matching quotient

### Theorem 2.1 (exact matching classification)

In the configuration above, the twelve-vertex bare matching quotient contains a
`K_7` minor if and only if `rs` is an edge of the six-vertex support graph
on `Q union {4,5}`.

Consequently, every quotient not already containing a `K_7` minor has the
following aligned form:

1. `r` is a singleton vertex in `Q`;
2. `s` is one endpoint of the two-vertex branch set;
3. `rs` is missing; and
4. the two missing edges `rs` and `10 11` are paired endpoint-for-endpoint
   by the linkage.

This is a much smaller residue than an arbitrary perfect matching.

### Minimal normal forms

Delete surplus singleton--edge-end contacts while retaining at least one
contact from each singleton and retaining irredundancy.  Up to interchanging
`4,5` and relabelling `Q`, there are two normal forms:

\[
\begin{array}{c|c|c}
\text{form}&N_Q(4)&N_Q(5)\\ \hline
3+1&\{0,1,2\}&\{3\}\\
2+2&\{0,1\}&\{2,3\}.
\end{array}
\]

For `3+1`, the bad preimages of `10 11` are

\[
 (0,5),(1,5),(2,5),(3,4),
\]

and for `2+2` they are

\[
 (0,5),(1,5),(2,4),(3,4).
\]

These lists are precisely the singleton--edge-end nonedges.  The verifier
also checks all irredundant contact patterns allowing a singleton to be
adjacent to both `4` and `5`, not only the two minimal forms.  The invariant
criterion remains exactly `rs in E(G)`.

## 3. One additional path between two linkage paths

For distinct `i,j in {0,...,5}`, subdivide the matching edges incident
with `i,j`, using new vertices `u_i,u_j`, and add the edge `u_i u_j`.
This is the canonical minor obtained from a path whose ends lie internally
on the two corresponding linkage paths and whose interior avoids all six
linkage paths and both endpoint supports.

The next table lists exactly when this fourteen-vertex one-bridge quotient
still has no `K_7` minor.  Only orbit representatives are shown.

| left normal form | preimage of `10 11` | residual bridge-pair orbits |
|---|---|---|
| `3+1` | `(0,5)` | `01, 03, 04, 12, 15, 35, 45` |
| `3+1` | `(3,4)` | `01, 03, 04, 35, 45` |
| `2+2` | `(0,5)` | `01, 02, 04, 15, 25, 45` |

The orbit conventions are:

- in the first row, `1,2` may be interchanged;
- in the second row, `0,1,2` may be permuted; and
- in the third row, `2,3` may be interchanged.

Every other bad matching is equivalent to one displayed row.  Thus a
single additional path with two internal attachments closes the
configuration unless its two linkage paths occur in the relevant finite
list.  Surplus contacts in the original support can only remove residual
pairs from the table.

### Oriented endpoint contraction forced by seven-connectivity

The connectivity argument in Section 5 gives an oriented connection from
`P_i-b_i` to `P_j-j`, where `j` is the left endpoint of `P_j`.  Even when
one or both attachments are endpoints,
contracting toward `i` on the first path and toward `b_j` on the second
always gives the extra edge `i b_j`.  The following table gives the exact
residual targets `j` for that guaranteed contraction.  Again only the three
orbit representatives are needed.

| normal form and missing preimage | source `i` | residual targets `j` |
|---|---:|---|
| `3+1`, `(0,5)` | `0` | `1,2,3,4` |
|  | `1` | `0,2,5` |
|  | `2` | `0,1,5` |
|  | `3` | `0,1,2,5` |
|  | `4` | `0,1,2,5` |
|  | `5` | `1,2,3,4` |
| `3+1`, `(3,4)` | `0` | `1,2,3,4` |
|  | `1` | `0,2,3,4` |
|  | `2` | `0,1,3,4` |
|  | `3` | `0,1,2,5` |
|  | `4` | `0,1,2,5` |
|  | `5` | `0,1,2,3,4` |
| `2+2`, `(0,5)` | `0` | `1,2,3,4` |
|  | `1` | `0,5` |
|  | `2` | `0,1,5` |
|  | `3` | `0,1,5` |
|  | `4` | `0,1,5` |
|  | `5` | `1,2,3,4` |

Every source has a residual target.  Therefore the Rolek--Song
one-connection argument, without attachment-order information, cannot by
itself escape the table.

## 4. Why the finite test is exact

The verifier uses two elementary completeness facts.

First, a seven-branch-set model on at most twelve vertices has at least two
singleton branch sets.  All singleton branch sets form a clique.  After
choosing the exact singleton clique, the verifier exhausts all remaining
pairwise disjoint connected branch sets of order at least two and checks
every required adjacency.

Second, if a vertex `v` has degree less than six, then `v` cannot be a
singleton branch set of a `K_7` model.  Hence

\[
 G\text{ has a }K_7\text{ minor}
 \quad\Longleftrightarrow\quad
 G-v\text{ has one, or }G/vw\text{ has one for some }w\in N(v). \tag{4.1}
\]

Indeed, if a model uses `v`, its branch set is non-singleton and contains
an edge `vw` that may be contracted.  Formula (4.1) removes the two
degree-three subdivision vertices of every one-bridge graph and reduces
the decision to the at-most-twelve-vertex exhaustive search.

Run the retained verifier from the repository root:

```text
uv run results/hc7_disjoint_k6minus_support6_linkage_classifier.py
```

It checks both minimal normal forms, all bad matching orbits, all fifteen
possible bridge pairs in each bad matching, and all irredundant contact
patterns with common contacts.

## 5. What seven-connectivity supplies

The path-forcing step in Rolek--Song's proof of their Lemma 1.9 has the
following label-preserving consequence here.  Write `P_i` for the path
from `i` to its matched vertex `b_i in B`.  Fix `i` and delete

\[
        \bigl((Q\cup\{4,5\})-\{i\}\bigr)\cup\{b_i\}. \tag{5.1}
\]

This is a set of six vertices.  Seven-connectivity leaves the graph
connected.  The surviving part of `P_i` on the left and the connected
graph consisting of `B-b_i` together with the surviving tails of the other
five linkage paths must therefore be joined by a path whose interior
avoids the six linkage paths.  Taking first and last intersections gives
an additional path between `P_i` and some `P_j`.

Thus seven-connectivity forces at least one such additional path from each
linkage path.  It does **not** prescribe its partner `j`, and every row of
the table admits residual partners for every required application of this
argument.  Moreover, paths obtained from different applications need not
be disjoint or have compatible attachment order.

The same argument can be applied to a subset of paths.  Let `T` be a
nonempty proper subset of `{0,...,5}`.  Delete `b_i` for `i in T` and
delete the left endpoint `j` for `j notin T`.  If the left support induced
by `T` and the right support induced by `{b_j:j notin T}` are both
connected, seven-connectivity forces an oriented additional path from
some `P_i` with `i in T` to some `P_j` with `j notin T`.

Even all these connected-bipartition requirements do not force a closing
orientation.  The verifier checks the following sets of residual arcs;
each set crosses every applicable bipartition:

\[
\begin{array}{c|c}
(3+1,(0,5))&03,15,20,31,42,54\\
(3+1,(3,4))&03,14,21,35,40,52\\
(2+2,(0,5))&02,03,15,25,31,40,54.
\end{array}                                                   \tag{5.2}
\]

Here `ij` denotes an oriented connection whose guaranteed endpoint
contraction adds `i b_j`.  Formula (5.2) is an abstract attachment pattern,
not a claim that the paths can be realized disjointly in a
`K_7`-minor-free seven-connected graph.  It proves that the endpoint-cut
logic alone is insufficient: the next step must exploit simultaneous
realizability and attachment order.

This identifies the exact remaining geometric issue:

> prove that several forced linkage bridges can be chosen with compatible
> attachment order so that their endpoint contractions compose, or show
> that failure produces a separator of order at most six.

Merely repeating the one-path connectivity argument cannot finish the
case.  The next theorem must use an extremal choice of the six-linkage and
the bridge-attachment order, rather than another unlabelled matching
argument.

## 6. Scope

The theorem is an exact finite classification of the quotient information
retained by one linkage bridge.  A residual table entry is not a
counterexample to the corresponding infinite seven-connected statement:
the host may have further bridges and edges.  Conversely, the theorem does
not prove that seven-connectivity forces a bridge outside the table.

Primary source for the path-forcing template: M. Rolek and Z.-X. Song,
*Coloring graphs with forbidden minors*, Journal of Combinatorial Theory,
Series B 127 (2017), Lemma 1.9 (arXiv:1606.05507).
