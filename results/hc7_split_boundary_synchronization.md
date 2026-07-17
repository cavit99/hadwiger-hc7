# Split-boundary colour synchronization

**Status:** written proof; separate internal audit GREEN.  The application below closes the
split-boundary branch of the bounded `HC_7` interface.  The parity
construction is an abstract sharpness result; it does not realize either
language as the colouring-extension language of a contraction-critical
graph.  Nothing in this note proves `HC_7`.

## 1. Exact-block cylinders

Let `H` be a nonempty graph and let `r` be a positive integer.  Write
`P_r(H)` for the set of partitions of `V(H)` into at most `r` nonempty
independent sets.  These are exactly the equality partitions induced by
proper `r`-colourings of `H`, with unused colours discarded.

For every nonempty independent set `I` of `H`, define its **exact-block
cylinder** by

\[
        \mathcal C_I
        =\{\Pi\in\mathcal P_r(H): I\text{ is a block of }\Pi\}.
\]

The exact-block cylinder hypergraph `X_r(H)` has vertex set `P_r(H)` and
one hyperedge `C_I` for every nonempty independent set `I`.

A hypergraph has **Property B** when its vertices admit a two-colouring
such that every hyperedge contains both colours.  Equivalently here,
`X_r(H)` has Property B when `P_r(H)` contains two disjoint sets, each of
which meets every exact-block cylinder.

Recall that `H` is a **split graph** when

\[
                         V(H)=K\mathbin{\dot\cup}J
\]

for a clique `K` and an independent set `J`.

## 2. Property-B characterization

### Theorem 2.1 (split graphs are exactly the static obstruction)

Let `H` be a nonempty graph satisfying

\[
                              \chi(H)\le r-2.       \tag{2.1}
\]

Then the exact-block cylinder hypergraph `X_r(H)` has Property B if and
only if `H` is not a split graph.

Moreover, when `H` is not split, colouring a partition according to the
parity of its number of blocks is a Property-B colouring.

#### Proof

First suppose that `H` is split.  Choose
`V(H)=K dotunion J`, where `K` is a clique and `J` is independent.  We may
assume `J` is nonempty: if `J` is empty, then `H` is complete and we move
one vertex of `K` into `J`.

Consider a partition in which `J` is an exact block.  Every vertex of
`K=V(H)-J` must be a singleton block because `K` is a clique.  Hence the
cylinder `C_J` consists of the unique partition

\[
                         \{J\}\cup\{\{x\}:x\in K\}.       \tag{2.2}
\]

This is a member of `P_r(H)`: since `K` is a clique,
`|K|<=chi(H)<=r-2`, so (2.2) has at most `r-1` blocks.  Thus `X_r(H)` has
a singleton hyperedge and cannot have Property B.

Conversely, suppose that `H` is not split.  Fix a nonempty independent
set `I` and put `F=H-I`.  The graph `F` is not a clique, since otherwise
`V(H)=V(F) dotunion I` would be a split partition of `H`.

Let `q=chi(F)` and take an optimal colouring of `F`, viewed as a partition
into `q` nonempty independent sets.  Because `F` is not a clique,
`q<|V(F)|`; consequently at least one colour class contains two vertices.
Splitting that class into two nonempty independent sets gives a proper
partition of `F` into `q+1` blocks.  After adjoining `I` as one exact
block, these two partitions of `H` have respectively

\[
                              q+1\quad\hbox{and}\quad q+2              \tag{2.3}
\]

blocks.  Both belong to `P_r(H)`, because
`q<=chi(H)<=r-2`.  Their block counts have opposite parity.  Therefore
every cylinder `C_I` contains both an even-block and an odd-block
partition.  Parity of the block count is a Property-B colouring of
`X_r(H)`.  This proves both assertions.  \(\square\)

## 3. Consequence for the bounded `HC_7` interface

Use the audited bounded-interface reduction.  Thus `G` is a hypothetical
minor-minimal counterexample to `HC_7`, `C` is a component of
`G-N[u]`,

\[
              S=N_G(C),\qquad A=G[C\cup S],\qquad B=G-C,
\]

and

\[
                   7\le |S|\le9,\qquad \chi(G[S])\le4.                \tag{3.1}
\]

For `Y` equal to `A` or `B`, let `E(Y,S)` be the equality partitions of
`S` induced by proper six-colourings of `Y`.  The reduction proves that,
for every nonempty independent set `I` of `G[S]`, each of `E(A,S)` and
`E(B,S)` meets the exact-block cylinder `C_I`.

### Corollary 3.1 (split boundaries glue)

If `G[S]` is a split graph, then

\[
                          E(A,S)\cap E(B,S)\ne\varnothing.             \tag{3.2}
\]

Consequently the two shore colourings can be aligned on `S` and glued to
a proper six-colouring of `G`, a contradiction.

#### Proof

Suppose instead that the two extension languages are disjoint.  Colour
every member of `E(A,S)` red and every member of `E(B,S)` blue; colour all
remaining members of `P_6(G[S])` arbitrarily.  Each exact-block cylinder
contains a red member and a blue member, so this is a Property-B colouring
of `X_6(G[S])`.

But (3.1) gives `chi(G[S])<=6-2`, and Theorem 2.1 says that a split
boundary has no such colouring.  This proves (3.2).  Two proper
six-colourings inducing the same equality partition on `S` differ there
only by a permutation of their used colour names.  After applying that
permutation on one shore, the colourings agree on `S` and glue.  \(\square\)

Thus every unresolved bounded interface in a hypothetical counterexample
has a **nonsplit** boundary graph.

## 4. Exact abstract sharpness on nonsplit boundaries

When `H` is nonsplit and `chi(H)<=r-2`, define

\[
\begin{aligned}
  \mathcal E_{\mathrm{even}}
     &=\{\Pi\in\mathcal P_r(H):|\Pi|\text{ is even}\},\\
  \mathcal E_{\mathrm{odd}}
     &=\{\Pi\in\mathcal P_r(H):|\Pi|\text{ is odd}\}.
\end{aligned}                                                        \tag{4.1}
\]

The proof of Theorem 2.1 shows that these two languages are disjoint and
that each meets every exact-block cylinder.  Hence, for **every**
nonsplit boundary satisfying the chromatic slack in (2.1), independent-
block completeness alone admits two incompatible abstract shore
languages.

This is sharp only at the static language level.  The parity classes in
(4.1) are not asserted to be realizable by the two shores of one graph,
let alone by a seven-connected, seven-contraction-critical,
`K_7`-minor-free host.  Closing the remaining nonsplit branch must use
host-level deletion/contraction transitions, labelled routing, or the
minor exclusion; no further conclusion follows from exact-block probes
alone.
