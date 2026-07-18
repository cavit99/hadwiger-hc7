# A local barrier to degree-eight contact allocation

**Status:** computer-assisted finite barrier to an intermediate claim.

The following nine-vertex local graph shows that

\[
 |S|=7,
 \qquad \alpha(H)\le3,
\]

even together with all but one of the edges between a three-set and a
five-set, does not force the six local branch sets used in the
degree-eight contact-allocation argument.  The missing literal edges
inside the five-set matter.

The deterministic verifier is
[`hc7_degree8_contact_allocation_barrier_verify.py`](hc7_degree8_contact_allocation_barrier_verify.py).

## Construction

Let

\[
 B=\{b_0,b_1,b_2\},\qquad
 C=\{c_0,c_1,c_2,c_3,c_4\}.
\]

Define a graph `H` on `B union C` as follows.

- `B` is independent.
- Every `B`--`C` edge is present except `b_2c_0`.
- The only edges inside `C` are `c_0c_1` and `c_2c_3`.

Add a vertex `v` adjacent to every vertex of `H`; call the resulting graph
`J`.  Put

\[
                     S=V(H)-\{c_2\}.                    \tag{1.1}
\]

The set `S` has order seven.  Moreover,

\[
                              \alpha(H)=3.               \tag{1.2}
\]

Indeed, `B` itself is an independent set of order three.  An independent
set meeting `b_0` or `b_1` contains no vertex of `C`; an independent set
containing `b_2` can contain only `c_0` from `C`; and `H[C]` has
independence number three.

Nevertheless, `J` has no six pairwise vertex-disjoint, connected,
pairwise adjacent subgraphs each meeting `S`.  The verifier enumerates
every nonempty connected vertex set meeting `S`, constructs the exact
compatibility relation (disjointness and adjacency), and exhaustively
searches for a compatible family of order six.

In the notation of Theorem 3.1 of the adjacent result, the sole absent
`B`--`C` edge is `b_2c_0`, but

\[
          (C\cap S)-\{c_0\}=\{c_1,c_3,c_4\}
\]

is independent.  Thus the contacted-edge condition in that theorem cannot
be deleted on the strength of the displayed local hypotheses alone.

## Exact scope

This is not a counterexample to `HC_7` and is not asserted to occur as the
neighbourhood of a vertex in a seven-connected, seven-contraction-critical
graph.  It refutes only the local implication from contact-set size,
neighbourhood independence number, and one missing `B`--`C` edge to the
specified `S`-meeting `K_6` minor model in `J`.  A host-level theorem may
still exclude the construction by using contraction-critical colourings,
the plane component outside the neighbourhood, or an exact separation.
