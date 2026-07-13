# Barrier: a dutyless three-gate does not supply the pullback matching

**Status:** adversarial finite certificate.  This graph is six-colourable
and is not a hypothetical `HC_7` counterexample.  It does not refute a
lemma whose conclusion also permits reflection, a `K_7`, or a fixed-pair
terminal outcome.

It does show that the local data currently proved by the binary-duty
three-gate descent do **not** imply the literal prerequisite for the proposed
descendant state

\[
 \Pi_X=\bigl\{\{b_i,z_{\sigma(i)}\}:1\le i\le3\bigr\}
          \cup\{\{c\}\}.
\]

Even with seven-connectivity, an actual `(1,2)` seven-separation, a legally
attained old paired-triangle state, a three-connected full packet, and the
exact dutyless-lobe trace, every `b_i z_j` may be an edge.  Then no
permutation `sigma` makes the displayed pairs independent, so `Pi_X` is not
even a proper equality partition.

The dependency-free verifier is
[`hc7_exact7_three_gate_pullback_matching_barrier_verify.py`](hc7_exact7_three_gate_pullback_matching_barrier_verify.py).

## 1. The fourteen-vertex graph

Let

\[
 S=\{c,b_1,a_1,b_2,a_2,b_3,a_3\},\qquad
 B_i=\{b_i,a_i\},
\]

and put

\[
 Z=\{z_1,z_2,z_3\},\qquad
 P=Z\cup\{x,y\},\qquad Q=\{q\},\qquad L=\{\ell\}.
\]

The old boundary graph has the following edges:

* both `a_1a_2a_3` and `b_1b_2b_3` are triangles;
* `ca_i` is an edge for every `i`; and
* `b_1a_2,b_2a_3,b_3a_1` are edges.

There is no edge `a_i b_i`.  Thus

\[
                    \Pi=\{B_1,B_2,B_3,\{c\}\}             \tag{1.1}
\]

is a proper paired-triangle partition: the three nonsingleton blocks are
pairwise adjacent, and `c` has a neighbour in every block.

Inside `P`, make both `x` and `y` adjacent to every member of `Z`, and add
the path `z_1z_2z_3`.  Add the boundary contacts

\[
\begin{aligned}
 N_S(x)&=\{c,b_1,b_2,b_3\},\\
 N_S(y)&=\{c,a_1,a_2,a_3\},\\
 N_S(z_j)&=\{b_1,b_2,b_3,a_j\}\quad(1\le j\le3).
\end{aligned}                                               \tag{1.2}
\]

Finally, both `q` and `ell` are adjacent to every vertex of `S`, and there
are no other edges.  Take the old separation to be

\[
             (L,S,R),\qquad R=P\mathbin{\dot\cup}Q.          \tag{1.3}
\]

The verifier exhausts all deletions of at most six vertices and confirms
that the graph is seven-connected.  Since deleting `S` disconnects it, its
connectivity is exactly seven.

It also enumerates every connected `S`-full vertex set in each open shore
and every disjoint packing of those sets.  The maximum packing numbers are

\[
                         (\nu_L,\nu_R)=(1,2).                \tag{1.4}
\]

The witnesses on the rich side are `P` and `Q`.  Within `P`, all full
packets intersect, so `P` contributes only one member to a packing.

## 2. Literal old-state attainment

Contract the connected set

\[
                         L\cup B_1=\{\ell,b_1,a_1\}          \tag{2.1}
\]

to a vertex `t`.  This is a proper minor operation supported in the thin
shore together with the independent boundary block `B_1`.

The resulting minor has the following proper six-colouring:

\[
\begin{array}{c|c}
\text{vertices}&\text{colour}\\ \hline
t&1\\
b_2,a_2&2\\
b_3,a_3&3\\
c,z_1,z_3&4\\
q,x,y&5\\
z_2&6.
\end{array}                                                  \tag{2.2}
\]

Expanding only the literal boundary block `B_1` on the untouched rich
closed shore gives exactly (1.1), with colours `1,2,3,4` on
`B_1,B_2,B_3,{c}`, respectively.  Thus the old paired-triangle state is
legally attained; it has not merely been declared as an abstract proper
partition.

## 3. Exact gate and failed pullback

The graph `P` is three-connected.  Deleting the three-vertex gate `Z`
leaves the two lobes `{x}` and `{y}`.  For the lobe `X={x}`,

\[
 N_P(X)=Z,
 \qquad
 N_S(X)=\{c,b_1,b_2,b_3\}.                                  \tag{3.1}
\]

It contains no complete old duty `B_i`, so this is exactly the audited
`c`-plus-rainbow dutyless trace.  Moreover

\[
 S_X=N_G(X)=Z\cup\{c,b_1,b_2,b_3\}                          \tag{3.2}
\]

has order seven.  Removing `S_X` leaves the lobe `{x}` and one nonempty
opposite component, and both are full to `S_X`; hence (3.2) is an actual
strictly smaller exact-seven adhesion.

Nevertheless (1.2) gives

\[
                         b_i z_j\in E(G)
                 \quad\text{for all }1\le i,j\le3.          \tag{3.3}
\]

The bipartite compatibility graph in which `b_i z_j` is available when it
is a boundary **nonedge** is therefore empty.  There is no permutation
`sigma` for which even one displayed block
`{b_i,z_{sigma(i)}}` is independent, much less all three.

For scope control, the verifier also checks an explicit six-colouring of
the original graph.  The certificate therefore does not defeat the full
terminal disjunction: in this graph the old state can reflect.  Its exact
lesson is narrower and literal:

> A state-preserving pullback theorem must derive a compatibility matching
> from a nonreflection or terminal-exclusion argument.  The gate trace,
> fullness, packet vector, old state attainment, and seven-connectivity do
> not provide that matching on their own.

Even a compatibility matching would establish only that the proposed
blocks are independent.  A complete positive lemma must separately prove
the new inter-block adjacencies, the `c`-to-block incidences, and legal exact
attainment of all three blocks.  The existing full-shore private-block
transition prescribes one independent block, not an entire four-block
partition.
