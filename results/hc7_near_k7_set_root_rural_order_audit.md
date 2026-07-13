# Independent audit: set-rooted rural order

## Verdict: **GREEN**

All three stated results are correct in their stated pairwise-disjoint-set
scope.  The four-set theorem has the right cyclic order, its alternatives are
exclusive, and the connected comparison graph in Theorem 2 really does put
all portal sets on one common root-to-root facial arc.  The HC7 corollary is
valid only under the explicitly stated disjointness hypothesis; that
hypothesis is not automatic for rotation portal sets.

I found no counterexample.  The supplied falsifier completes successfully,
although its atlas portion contains no no-linkage instance and is therefore
only a sanity check; the two explicit eight-vertex sharp cases are the
nonvacuous computational tests.

## Theorem 1 (four-set rural block theorem): **GREEN**

### Exact Two Paths use

Failure of an `A-P`/`B-Q` set linkage implies failure for every selected
quadruple

\[
 a\in A,\quad b\in B,\quad p\in P,\quad q\in Q.
\]

The terminals are distinct because the four sets are pairwise disjoint.
The standard 4-connected Two Paths Theorem therefore applies to the pairs
`(a,p)` and `(b,q)`.  Its rural cyclic order is alternating between those
two pairs.  Up to reflection this is exactly

\[
                         A,Q,P,B,
\]

not `A,P,Q,B`.

### Face-sharing argument

The face propagation is valid.  Replacing one selected terminal leaves the
other three distinct terminals fixed.  In the unique embedding of a
3-connected planar graph, two different facial cycles cannot share three
distinct vertices.  Hence every replacement uses the original face.  Varying
one set at a time with the other three original representatives fixed puts
every member of all four sets on that face.

### Four-block order

On the open `a_0-b_0` arc containing `q_0,p_0`, alternation with fixed
`q_0` puts every `P` vertex after `q_0`; alternation with fixed `p_0` puts
every `Q` vertex before `p_0`; applying alternation to arbitrary `p,q`
forces every `Q` occurrence before every `P` occurrence.

The symmetric argument on the complementary `p_0-q_0` arc forces every
`B` occurrence before every `A` occurrence.  Thus none of the four labelled
sets can split another labelled block, and the cyclic filtered order is
precisely `A,Q,P,B`.

### Exclusivity

Outcome 2 preserves the roles of `P` and `Q`, unlike the previously audited
unoriented two-block statement.  Any selected `a,q,p,b` occur alternately
for the pairs `a-p` and `b-q`.  Planar Jordan separation therefore forbids
two vertex-disjoint prescribed paths.  Hence outcomes 1 and 2 are genuinely
exclusive.

The statement “one facial cycle” is also justified: the union contains at
least four distinct vertices, and a second face containing it would share at
least three boundary vertices with the first.

## Theorem 2 (set-rooted rural holonomy is flat): **GREEN**

The graph assumptions repair exactly the vacuous cases present in the
earlier fixed-single-root formulation: `I` has at least two labels, the arc
set is nonempty, and `Q_0` is loopless with connected underlying graph.

Apply Theorem 1 on one arc.  During a spanning-tree traversal, a new edge
shares with the already established face:

* every vertex of nonempty `A`;
* every vertex of nonempty `B`; and
* every vertex of the nonempty already placed portal set.

These supply at least three distinct common vertices, so the new face is the
same face.  The already placed portal set also determines which of the two
`A-B` gaps is the portal-containing gap; the new portal set must occupy that
same gap.  Connectedness of the underlying comparison graph propagates this
choice to every label.  Because every label is incident with a tree edge,
the corresponding application of Theorem 1 also prevents that portal set
from splitting either root block.

For an arc `i -> j`, Theorem 1 gives, up to reflection,

\[
                         A,P_j,P_i,B.
\]

Reading the common portal-containing arc from the `B` block towards the
`A` block gives

\[
                         B,P_i,P_j,A,
\]

so the asserted comparison `P_i<P_j` has the correct direction.  All arcs
are therefore strict comparisons on one line, and a directed cycle is
impossible.  Opposite arcs between two labels are correctly rejected as a
directed 2-cycle.

## Corollary 3 (HC7 discharge): **GREEN in the stated scope**

When

\[
 N_Z(X),\ N_Z(W),\ N_Z(F_i),\ N_Z(F_j)
\]

are nonempty and pairwise disjoint, a set linkage consists of two disjoint
connected carriers meeting the required attachment and private portal sets.
Lemma 2 of the common-row note adds the nonempty common portal occurrence,
and the robust rotation theorem then gives a `K_7^-` model.  If the linkage
does not exist, Theorem 1 places **all** possible literal attachment roots in
the same four-block facial order.  Thus changing the selected roots within
this one connector cannot change the sign.

This corollary must not be used when any attachment set overlaps a portal
set, when two row portal sets overlap, or across different connector torsos.
In a raw rotation datum such overlaps can occur; they require the separate
common-portal absorption/promotion argument exactly as the trust boundary
states.

## Computational check

Running

```text
PYTHONPATH=active/runtime/deps python3 active/hc7_set_root_rural_order_verify.py
```

returned

```text
GREEN: 30 4-connected atlas graphs; 643800 terminal assignments; 0 no-linkage instances
GREEN: sharp square-antiprism and double-book rural orders
```

The `0 no-linkage instances` means the atlas enumeration does not itself
exercise the rural conclusion.  The two named eight-vertex cases do exercise
it and pass.  The proof, not this computation, establishes the theorem.

## Trust boundary

This theorem completely removes **choice of roots inside a fixed
4-connected connector with disjoint terminal sets** as a source of signed
holonomy.  It does not align orders across different torsos, cross a
cutvertex/2-adhesion, or handle overlapping portal classes.  Those remain
the genuine composition problem.
