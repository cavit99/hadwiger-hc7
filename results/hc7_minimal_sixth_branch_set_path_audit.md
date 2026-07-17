# Audit of the minimal sixth-branch-set path normalization

**Verdict:** **GREEN** for the exact source revision identified below.

This is a separate internal mathematical audit.  It verifies the local
`K_6`-minor-model normalization, the conditional raw-separator consequence,
and the stated trust boundary.  It is not external peer review, does not
promote the note beyond its stated conditional scope, and does not prove
`HC_7`.

## Audited revision

The audited file is
`results/hc7_minimal_sixth_branch_set_path.md`.

**Current source SHA-256:**
`655b7a40b56ce39709753499715b2dfda5a0715f404e34adfe80f939c0746ee1`.

The mathematical revision originally audited had SHA-256
`e3577232d1406a75eef1230fd581461996191e44b95684843d8e849aa72f9dab`.
The current file differs from that revision only in two nonmathematical
edits: its status now records this GREEN audit, and the TeX spacing command
in the displayed path in Section 4 was corrected from `,qquad` to
`,\qquad`.  Reversing exactly those two edits reproduces the originally
audited SHA-256.  No theorem statement, hypothesis, or proof step changed.

## 1. Definitions and elementary re-selections

At every stage the five contact sets

\[
                         S_i=N_G(B_i)\cap L
\]

are nonempty, because the current distinguished branch set is adjacent to
every named branch set.  The definition

\[
                 P_L(x)=\{i:S_i=\{x\}\}
\]

therefore records exactly the names whose sole *contact vertex in the
current `L`* is `x`.  It does not assert uniqueness of a contact edge or of
a neighbour inside `B_i`.  The source recomputes these sets after each move;
no invariant incorrectly freezes the original contacts.

If `|L|>=2` and `x` is a non-cutvertex of `G[L]`, then `L-{x}` is nonempty
and connected.  Connectedness of `G[L]` also gives an edge from `x` to
`L-{x}`.  These two facts supply exactly the connectivity and adjacency
needed by both elementary operations.

In the deletion case, `P_L(x)=emptyset` implies that every nonempty `S_i`
contains a vertex other than `x`; hence every named branch set retains a
contact with `L-{x}`.  In the absorption case, `P_L(x)={i}` gives a contact
edge from `x` to `B_i`, so `B_i union {x}` is connected.  The edge from `x`
to `L-{x}` makes the enlarged set adjacent to the new `L`.  For each
`j!=i`, nonmembership in `P_L(x)`, together with nonempty `S_j`, leaves a
contact vertex different from `x`.

Moving `x` from `L` into `B_i` preserves pairwise disjointness: `x` was in
none of the old `B_j`, it is removed from `L`, and the old six sets were
disjoint.  Enlarging one named branch set cannot destroy any old adjacency
among the five named sets.  Thus Lemma 1.1 checks all four branch-set
requirements: nonemptiness, connectivity, disjointness, and every required
pairwise adjacency.

Each move replaces a positive `|L|>=2` by `|L|-1`.  The process can never
delete the final vertex and therefore terminates after at most the original
`|L|-1` moves.  No fairness or choice assumption is needed: every maximal
sequence is finite and ends at a tuple to which neither permitted move
applies.

## 2. Reduced tuples and the path conclusion

Let a reduced tuple have `|L|>=2`.  Every non-cutvertex `x` must satisfy
`|P_L(x)|>=2`; otherwise its private-label count is zero or one and the
corresponding elementary move applies.  For distinct `x,y`, the sets
`P_L(x)` and `P_L(y)` are disjoint, since a fixed `S_i` cannot equal both
distinct singletons.  Five labels can therefore support at most two
non-cutvertices.

The graph-theoretic sublemma used next is correct under the repository's
standing finite-simple-graph convention.  Every connected graph of order at
least two has at least two non-cutvertices: leaves of a spanning tree remain
non-cutvertices in the ambient graph.  If a spanning tree has only two
leaves, it is a spanning path.  Any extra ambient edge joining
nonconsecutive vertices of that path makes every path vertex strictly
between its ends a further non-cutvertex.  Hence a connected graph with
exactly two non-cutvertices is a path, and its two non-cutvertices are its
endpoints.

It follows that a nonsingleton reduced `G[L]` is a path.  Each endpoint has
at least two private labels; their private-label sets are disjoint; and their
union has order at least four, leaving at most one of the five names unused.
The theorem's private-label counting is therefore exact.  Since each new
`L` is a vertex subset of the preceding one, an initially bipartite induced
subgraph stays bipartite, and `G[L]` is automatically the induced subgraph
on the retained vertex set.

## 3. Fixed-support counterexample and direct splitting

In the chordless `C_4` example, adjacency to `b_1,b_2,b_3` respectively
forces `x_1,x_2,x_3`, while adjacency to either `b_4` or `b_5` forces `x_4`.
Thus every subset of `L` adjacent to all five fixed singleton branch sets
contains all four cycle vertices.  In particular, no connected proper
subset works, while `G[L]` is a bipartite cycle and not a path.  The example
correctly refutes fixed-support deletion-only normalization and does not
refute Theorem 2.1, which permits absorption into a named branch set.

For a reduced path `v_0...v_r`, every right shore after an edge split omits
`v_0` and is therefore anticomplete to each `B_i` with
`i in P_L(v_0)`.  Symmetrically, every left shore is anticomplete to each
`B_i` with `i in P_L(v_r)`.  Each missed family has at least two names.
Consequently the two path shores together with the five unchanged named
sets do not themselves give the missing seven-branch-set model.  The source
correctly presents this as an obstruction to the direct fixed-name split,
not as a general exclusion of every other `K_7` construction.

## 4. Raw full-neighbourhood separation

The conditional defect-one premise used in Section 5 is sufficient.  Four
represented protected labels give at least four vertices in the selected
component-contact graph.  A simplicial degree-two vertex representing
`L_0`, together with its two neighbours, accounts for only three of them;
there is therefore another selected vertex.  Its represented connected
subgraph `W` is disjoint from `L_0` and anticomplete to it, because quotient
adjacency is defined exactly by adjacency of the represented subgraphs.

For nonempty connected `Y subseteq L_0`, put

\[
                       A=Y\cup N_G(Y),\qquad B=V(G)-Y.
\]

Then `A union B=V(G)`, `A intersection B=N_G(Y)`, and there is no edge from
`A-B=Y` to `B-A=V(G)-(Y union N_G(Y))` by the definition of the external
open neighbourhood.  The first open side contains the nonempty set `Y`.
The nonempty subgraph `W` lies in the second open side because it is
disjoint from and anticomplete to all of `L_0`, hence to `Y`.  Thus (5.1) is
an actual separation with two nonempty open sides.

Seven-connectivity consequently yields only `|N_G(Y)|>=7`.  It gives no
upper bound.  Prefixes and suffixes of the final path qualify because every
move only removes vertices from the current `L`, so the final path remains
a subset of the original `L_0`, and each such prefix or suffix is nonempty
and connected.  The source correctly requires an independent upper bound
before calling any of these separations order seven and claims neither
shore colourings nor a common separator equality partition.

The defect-one background identification was cross-checked against
`results/hc7_defect_one_simplicial_normalization.md` at SHA-256
`a6c954234ec2121b0150959f4ce9cff18e78045932a4d331343094db2bf88b05`;
its exact-file internal audit is GREEN.  Proposition 5.1 itself needs only
the explicit two-tree, four-label, contact-graph, and seven-connectivity
premises restated above.

## 5. Trust boundary

The final limitations are accurate and load-bearing.

1. The local deletion `L-{x}` changes a displayed branch set but does not
   delete `x` from the fixed host or from the fixed residual induced graph.
   It therefore need not yield another residual component.
2. Absorbing `x` into `B_i` preserves the six local branch sets but can
   destroy any path-side, pole, protected-label, valid-cut, or selected-
   component role imposed on `B_i` by the full defect-one configuration.
3. Hence minimality of `|L|` over full valid configurations does not imply
   reducedness under operations that may leave that class of configurations.
4. The raw separator argument supplies only its connectivity lower bound.
   Proper-minor six-colourings do not canonically identify their exposed
   colour classes with these five named branch sets, so they do not by
   themselves restore private endpoint contacts or synchronize two closed-
   shore colourings.

Accordingly, the note proves no strict host-level descent, no compatible
order-seven separation, and no `K_7`-minor construction.  Its stated need
for an operation-specific reconstruction theorem is the correct remaining
trust boundary.
