# A boundary Kempe obstruction need not improve fixed-partition support coverage

**Status:** explicit finite barrier to an intermediate transition claim.  The
companion deterministic checker is
[`hc7_exact7_fixed_partition_coverage_transition_barrier_verify.py`](hc7_exact7_fixed_partition_coverage_transition_barrier_verify.py).

This note does not give a counterexample to `HC_7`.  It shows that maximizing
the number of blocks supported for one fixed boundary partition, and then
minimizing the total order of those supports, does not by itself turn a
boundary Kempe obstruction path into either an additional supported block or
a smaller support system.  A positive theorem must use further host-level
information to obtain an explicit `K_7`-minor model, a compatible separation,
or a labelled descent.

## 1. Boundary partition and its three required sets

Let `S={0,1,...,6}` induce the Moser spindle with edge set

```text
01 02 03 04 12 16 26 34 35 45 56.
```

Consider the proper boundary partition

\[
 \Pi=A\mid B\mid D\mid\{6\},\qquad
 A=\{2,3\},\quad B=\{1,4\},\quad D=\{0,5\}.
 \tag{1.1}
\]

Choose the singleton clique `U={6}`.  Each of `A,B,D` has a boundary edge
to `6`, respectively through `2,1,5`.  Consequently its required set in
the transported-partition reflection theorem is just the block itself:

\[
                   D_U(A)=A,\qquad D_U(B)=B,
                   \qquad D_U(D)=D.                  \tag{1.2}
\]

## 2. One boundary-full connected subgraph

Let the open-side graph `P` be the seven-cycle

\[
 u_0u_1u_2u_3u_4u_5s u_0.                            \tag{2.1}
\]

Give its vertices the following unique boundary contacts:

\[
 2u_0,\quad1u_1,\quad0u_2,\quad3u_3,
 \quad4u_4,\quad5u_5,\quad6u_0.                     \tag{2.2}
\]

Thus `P` is connected and adjacent to every literal boundary vertex.  The
six portals for the three required sets occur around the cycle as

\[
                         A\ B\ D\ A\ B\ D.           \tag{2.3}
\]

Call a nonempty connected subgraph of `P` a support for one of
`A,B,D` when it has a neighbour at every vertex of that block.  Because
the contacts in (2.2) are unique, such a support must contain both portals
of its block.  The portal pairs of every two blocks alternate on the
cycle.  Hence supports for two different blocks cannot be vertex-disjoint.
Conversely a shortest arc between either portal pair is a support of order
four.  It follows that

\[
 \kappa_P(\Pi)=1,
 \qquad
 \min\{|V(K)|:K\text{ supports a block of }\Pi\}=4.   \tag{2.4}
\]

Here `kappa_P(Pi)` is the maximum number of distinct blocks among
`A,B,D` having pairwise vertex-disjoint connected supports in `P`.  The
block unions are pairwise adjacent through the boundary edges, so no
additional adjacency condition changes (2.4).

## 3. The obstruction path changes the partition, not the rank

Give the four boundary blocks in (1.1) colours `1,2,3,4`, respectively,
and colour the open-side vertices by

\[
\begin{array}{c|ccccccc}
 &u_0&s&u_5&u_4&u_1&u_2&u_3\\ \hline
 c&2&1&2&1&5&6&5.
\end{array}                                           \tag{3.1}
\]

This is a proper six-colouring of `G[S union V(P)]`.  On the boundary, the
subgraph in colours `1,2` has precisely the two components

\[
                         \{1,2\},\qquad\{3,4\}.       \tag{3.2}
\]

The literal bichromatic path

\[
                 2u_0s u_5u_4 4                      \tag{3.3}
\]

joins those two components and has all internal vertices in `P`.  It is
therefore exactly the type of path supplied by the signature-change-path
argument when a boundary interchange is obstructed in a named shore.

Its open-side vertex set

\[
                         Z=\{u_0,s,u_5,u_4\}           \tag{3.4}
\]

contacts the boundary set `{2,4,5,6}`.  It therefore supports none of
`A,B,D`.  Moreover, the smallest connected superset of `Z` supporting
`A` or `B` has order five, and the smallest one supporting `D` has order
six.  Thus (3.3) neither increases the fixed-partition coverage in (2.4)
nor replaces a minimum support by a smaller one.

Interchanging colours `1,2` on the boundary component `{1,2}` changes the
complete equality partition to

\[
             \Pi'=\{1,3\}\mid\{2,4\}\mid D\mid\{6\}.
 \tag{3.5}
\]

The set `D` remains the same exact labelled colour class, but `Pi'` is not
`Pi`.  Any geometric improvement belonging to `Pi'` is therefore outside
an extremal comparison made only among support systems for `Pi`.

## 4. Minor exclusion and exact scope

The displayed graph has treewidth at most four.  One elimination order,
with at most four later filled neighbours at every step, is

```text
s u1 2 1 u3 u5 4 3 6 0 5 u0 u2 u4.
```

Since treewidth is minor-monotone and `tw(K7)=6`, this local graph has no
`K_7` minor.  Thus the failure of fixed-partition augmentation is not paid
for by a hidden clique minor inside the displayed page.

The construction refutes only the following intermediate inference:

> a literal bichromatic obstruction path, together with a maximum-coverage
> minimum-order support system for a fixed complete boundary partition,
> must add an uncovered required set for that same partition or shorten
> its support system.

It deliberately does **not** realize an entire hypothetical counterexample.
In particular, it is not seven-connected or contraction-critical, it has
no opposite closed shore with a proved extension-signature change, and it
has none of the five inherited branch-set labels used by the active
order-eight reduction.  It therefore does not refute a terminal theorem
which uses those omitted hypotheses to produce a compatible order-seven
separation, an explicit `K_7`-minor model elsewhere in the host, or the
audited labelled cyclic-contact conclusion.

The strongest general statement surviving this barrier is conditional and
essentially exact.  An obstruction-path interior augments a fixed
`Pi`-support system only when it is disjoint from the selected supports,
meets every literal vertex of one uncovered required set, and preserves the
needed adjacencies to the represented block unions.  Minimum support order
rules out a replacement only after that replacement is independently shown
to support the same block and preserve all those adjacencies.  A Kempe
transition supplies neither property merely from its two boundary ends.
