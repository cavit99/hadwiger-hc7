# Exact boundary-state transfer across two exterior sides

> **Portalized extension.**  The multi-piece version with a genuine
> adhesion \(X\supseteq N(v)\), explicit portal blocks, and one-step
> minor-transition states is proved in
> `hadwiger_portal_exact_boundary_transfer.md`.  The theorem below is its
> two-piece, portal-free special case.

## Theorem

Let $G$ be a proper-minor-minimal counterexample to $\mathrm{HC}_t$.
Fix a vertex $v$, put $N=N_G(v)$, and suppose

$$
G-N[v]=C_1\mathbin{\dot\cup}C_2
$$

with no edge between $C_1$ and $C_2$. Let

$$
\Pi=\{P_1,\ldots,P_q\}
$$

be a partition of $N$ into nonempty independent sets.

Say that side $s$ **realizes** $\Pi$ if there are pairwise disjoint
connected sets

$$
X_1,\ldots,X_q\subseteq N\cup C_s\cup\{v\}
$$

such that

1. $X_i\cap N=P_i$ for every $i$; and
2. $X_i$ and $X_j$ are adjacent for every $i\ne j$.

Then:

1. if side $s$ realizes $\Pi$, the exact boundary state $\Pi$ extends
   to the opposite boundaried graph $G[N\cup C_{3-s}]$;
2. if both sides realize $\Pi$ and $q\le t-2$, then $G$ is
   $(t-1)$-colourable, a contradiction.

Thus a minor-minimal counterexample cannot contain bilateral
realizations with at most $t-2$ blocks.

## Proof

Assume side $s$ realizes $\Pi$. Contract every $X_i$ to a vertex
$x_i$, and delete all unused vertices of $C_s\cup\{v\}$. This is a
proper minor of $G$. The vertices $x_1,\ldots,x_q$ form a clique, so
in every $(t-1)$-colouring of the minor they receive pairwise distinct
colours.

Keep the colouring on $C_{3-s}$ and give every original boundary vertex
in $P_i$ the colour of $x_i$. This expansion is proper:

- each $P_i$ is independent;
- every edge between two different blocks has differently coloured
  ends because the corresponding images lie in the clique; and
- all edges from the boundary to $C_{3-s}$ were retained in the minor.

The colour classes induced on $N$ are exactly
$P_1,\ldots,P_q$, because the clique images have distinct colours and
the blocks cover $N$. This proves the transfer assertion.

Now suppose both sides realize $\Pi$. Applying the first assertion in
the two directions gives:

- a $(t-1)$-colouring of $G[N\cup C_1]$ inducing exactly $\Pi$ on
  $N$; and
- a $(t-1)$-colouring of $G[N\cup C_2]$ inducing exactly $\Pi$ on
  $N$.

Permute the palette on one side so that the colours of corresponding
blocks agree. The two colourings then glue, because the sides have no
edge between them. Exactly $q$ colours occur on $N$. If $q\le t-2$,
one of the $t-1$ colours is absent from $N$; assign it to $v$.
Since $v$ has no neighbours outside $N$, the result is a
$(t-1)$-colouring of $G$, the required contradiction. $\square$

## Remarks on use

The sets $X_i$ need not cover $C_s\cup\{v\}$; unused vertices are
deleted.  No prescribed tree or path structure inside a block is needed:
only connectivity of each set in $G$ and pairwise adjacency are used.
The hypotheses explicitly guarantee that branch sets are disjoint and
that no boundary vertex occurs in the wrong block.

The supported-pair transfer in the pure-Moser cell is the case
$t=7$, $q=4$: the four blocks are the repeated-pair star, two disjoint
path blocks joined by a connector edge, and the remaining singleton
root. The theorem isolates the reusable mechanism from that local
geometry.
