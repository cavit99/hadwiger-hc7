# Boundary-forced Kempe locks in the paired exact-seven response

**Status:** written proof; separate internal audit GREEN in
[`hc7_paired_boundary_forced_kempe_locks_audit.md`](hc7_paired_boundary_forced_kempe_locks_audit.md).
This note is a
corollary of the fixed-trace two-edge analysis.  It converts a literal
boundary adjacency into a forced bichromatic lock at a monochromatic deleted
edge.  It does not identify colours with minor-model branch sets, produce a
`K_7`-minor model, or synchronize two shore colourings.

## 1. Fixed-trace setting

Let `q>=2`, let `G` be a graph which is not `q`-colourable, and let

\[
             V(G)=A\mathbin{\dot\cup}X\mathbin{\dot\cup}D,
             \qquad E_G(A,D)=\varnothing .                       \tag{1.1}
\]

Fix a proper `q`-colouring `c` of `G[A union X]`.  Let `e=ab` and `f=cd`
be vertex-disjoint edges of `G[D]`.  Assume that neither `G-e` nor `G-f`
has a `q`-colouring inducing on `X` the equality partition of `c`, but that
`G-{e,f}` has such a colouring `psi`.  After a global permutation of the
palette, assume

\[
                         \psi|_X=c|_X.                            \tag{1.2}
\]

The ends of both deleted edges are monochromatic under `psi`.  For a colour
`r`, put

\[
                         B_r=X\cap\psi^{-1}(r).                   \tag{1.3}
\]

If `psi(a)=psi(b)=i` and `j!=i`, say that `e` is **`i-j` locked** when
`a,b` belong to one component of the subgraph of `G-{e,f}` induced by the
two colours `i,j`.

## 2. The boundary-component criterion

### Lemma 2.1

If `e` is not `i-j` locked, then the boundary graph

\[
                       G[X][B_i\cup B_j]                           \tag{2.1}
\]

has at least two nonempty connected components.  Consequently, if (2.1)
is connected whenever it is nonempty, then `e` is `i-j` locked.

#### Proof

Let `Q_a,Q_b` be the distinct `i-j` components containing `a,b`.  The
fixed-trace endpoint-switch argument applies to either component: switching
its two colours makes `e` proper, so if that component avoided `X`, the
other deleted edge could be restored while retaining (1.2), contrary to
the hypothesis on `f`.  Thus both `Q_a` and `Q_b` meet `X`.

Every vertex of `Q_a\cap X` and `Q_b\cap X` lies in `B_i\cup B_j`.  If a
path in (2.1) joined the two intersections, it would also be an `i-j` path
in the full host joining `Q_a` to `Q_b`, contrary to their being distinct
components.  Therefore the two intersections lie in distinct nonempty
components of (2.1).  The contrapositive is the final assertion. \(\square\)

### Corollary 2.2 (block rules)

The following are sufficient to force an `i-j` lock.

1. `B_i` is empty and `B_j` is a singleton, or conversely.
2. `B_i={x}`, `B_j={y}`, and `xy` is an edge.
3. One block is a singleton `{x}`, the other is an independent set `M`,
   and `x` is adjacent to every vertex of `M`.

#### Proof

In each case the nonempty graph in (2.1) is connected: respectively a
single vertex, one edge, or a star containing every vertex of `M`.
Lemma 2.1 applies. \(\square\)

The third condition deliberately requires adjacency to every literal
vertex of `M`.  A palette colour does not name a minor-model branch set,
and one contact with `M` is insufficient.

## 3. Exact counts for the paired boundary partition

Assume now that `q=6`, that `|X|=7`, and that the equality partition induced by `psi`
has the form

\[
 \Pi=M\mid\{x\}\mid\{y\}\mid\{k\}\ (k\in K),
 \qquad
 X=M\mathbin{\dot\cup}\{x,y\}\mathbin{\dot\cup}K,               \tag{3.1}
\]

where `M` is independent, `K` is a clique, `xy` is a nonedge, and

\[
                       (|M|,|K|)\in\{(2,3),(3,2)\}.                \tag{3.2}
\]

The notation in (3.1) means that every vertex of `K` is its own singleton
block.  There are six used colours in the `(2,3)` case and five used
colours in the `(3,2)` case.

### Corollary 3.1 (`(|M|,|K|)=(2,3)`)

Suppose `psi(a)=psi(b)=i`.

1. If `B_i={k}` for `k in K`, then `e` is locked against the colours of
   the other two vertices of `K`.
2. If `B_i={v}` is any singleton block, then `e` is locked against every
   singleton-block colour whose literal vertex is adjacent to `v`, and
   also against the colour of `M` when `v` is complete to `M`.
3. If `B_i=M`, then `e` is locked against the colour of every singleton
   vertex complete to `M`.

In particular, a `K`-singleton equality colour has at least two
boundary-forced locks.  No positive universal count follows from the
boundary alone when the equality colour is `x`, `y`, or `M`.

#### Proof

The clique property of `K` and Corollary 2.2(2) give item 1.  Items 2 and
3 are exactly Corollary 2.2(2)--(3).  The hypotheses impose no edge from
`x` or `y` to another singleton other than those explicitly present, and
they impose no vertex complete to `M`; hence the final sentence makes no
unstated adjacency assumption. \(\square\)

### Corollary 3.2 (`(|M|,|K|)=(3,2)`)

Let `o` be the unique palette colour absent from `X`, and suppose again
that `psi(a)=psi(b)=i`.

1. If `i=o`, then `e` is locked against each of the four singleton-block
   colours (those of `x`, `y`, and the two vertices of `K`).
2. If `B_i={x}` or `B_i={y}`, then `e` is locked against `o`; hence it has
   at least one boundary-forced lock.
3. If `B_i={k}` for `k in K`, then `e` is locked against `o` and against
   the colour of the other vertex of `K`; hence it has at least two
   boundary-forced locks.
4. If `B_i=M`, then `e` is locked against every singleton-block colour
   whose vertex is complete to `M`, but the absent colour `o` need not be
   locked by this criterion.

#### Proof

For item 1, pair the empty block `B_o` with each singleton block and use
Corollary 2.2(1).  The same rule proves the absent-colour locks in items 2
and 3; the clique edge inside `K` supplies the other lock in item 3.
Item 4 is Corollary 2.2(3).  When `B_i=M` and `B_o` is empty, the graph in
(2.1) is the independent graph on the three vertices of `M`, so Lemma 2.1
does not force a lock. \(\square\)

All statements are symmetric for the other deleted edge `f`.

## 4. Exact gain and remaining obstruction

In the stronger minor-critical application where `chi(G)=7` and every
proper minor of `G` is six-colourable, the common-host lock-allocation
theorem says that, in a double-contraction six-colouring, one of two
vertex-disjoint deleted edges has at least three locks, and at least four
when their equality colours are distinct.  Corollaries 3.1--3.2 add
literal boundary information: they
identify locks which are forced before any model-label allocation is
attempted, and show that every unlocked alternate colour must split the
corresponding two boundary colour blocks into at least two components.

This still does not solve the repeated-exposure exchange.  A lock is a
path indexed by palette colours, not by one of the five named common
minor-model branch sets.  The remaining theorem must use the literal
first model-bag hit of such a path, together with `K_7`-minor exclusion,
to obtain a new named label, a proper response-preserving subkernel, an
explicit `K_7`-minor model, or an exact seven-separation carrying the
partition-specific connected-subgraph system needed for colour gluing.

## 5. Dependencies

- [fixed-trace alternatives for two repeated-exposure edges](hc7_repeated_exposure_fixed_trace_fork.md)
- [common-host double-contraction lock allocation](../results/hc7_common_host_double_contraction_lock_allocation.md)
- [exact selected-response preservation criterion](hc7_exact7_selected_response_preservation.md)
