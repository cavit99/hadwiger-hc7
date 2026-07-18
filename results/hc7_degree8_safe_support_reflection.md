# Safe boundary supports reflect the two paired traces

**Status:** written proof; separate internal audit.  This is a conditional
closure lemma for the degree-eight disk configuration.  It does not prove
that the four contact patterns below are exhaustive, and it does not
eliminate the boundary-edge obstructions identified in Section 4.

## 1. Setup

Let `G` be a graph which is not six-colourable and every proper minor of
which is six-colourable.  Let

\[
       V(G)=L\mathbin{\dot\cup}T\mathbin{\dot\cup}R,
       \qquad E_G(L,R)=\varnothing,                         \tag{1.1}
\]

where both open sides are nonempty.  Fix `a in T`.  Suppose that
`G[R union T]-a` contains five pairwise vertex-disjoint connected
subgraphs

\[
                         Q_I,Q_J,Q_1,Q_2,Q_3                \tag{1.2}
\]

which are pairwise adjacent, each is adjacent to `a`, and which cover
`T-{a}`.  Assume that

\[
       Q_I\cap T=I=\{i_0,i_1\},\qquad
       Q_J\cap T=J=\{j_0,j_1\},                            \tag{1.3}
\]

that `I` and `J` are independent, that every other row intersection has
order at most one, and that at least one of `Q_1,Q_2,Q_3` misses `T`.
Put

\[
                         B=T-(I\cup J),\qquad |B|=3.        \tag{1.4}
\]

On the other closed side suppose there are five pairwise vertex-disjoint
connected subgraphs

\[
                         C_0,C_1,C_2,C_3,C_4               \tag{1.5}
\]

of `G[L union I union J]` such that

\[
 \begin{array}{c|ccccc}
 r&0&1&2&3&4\\ \hline
 C_r\cap T&\{i_0\}&\{j_0\}&\{i_1\}&\{j_1\}&\varnothing.
 \end{array}                                               \tag{1.6}
\]

In the degree-eight application these sets occur in cyclic order, but the
reflection lemma below needs only their connectedness, disjointness, and
the traces in (1.6).

For `b in B`, say that `b` **safely supports `I`** if

\[
 E_G(b,C_0)\ne\varnothing,\qquad
 E_G(b,C_2)\ne\varnothing,
 \qquad I\cup\{b\}\text{ is independent}.                \tag{1.7}
\]

Define safe support of `J` analogously using `C_1,C_3` and
`J union {b}`.

## 2. Safe-support reflection theorem

### Theorem 2.1

If distinct vertices `p,q in B` safely support `I` and `J`, respectively,
then `G` is six-colourable.

### Proof

Choose an edge from `p` to `C_0`.  Inside the connected graph `C_0`, take
a path from `i_0` to its endpoint.  Do the same in `C_2`, starting at
`i_1`, and adjoin `p`.  The union is a connected subgraph `X_I` satisfying

\[
                         X_I\cap T=I\cup\{p\}.           \tag{2.1}
\]

Similarly, the two contacts from `q` to `C_1,C_3` give a connected
subgraph `X_J` with

\[
                         X_J\cap T=J\cup\{q\}.           \tag{2.2}
\]

The two connected subgraphs are vertex-disjoint: their four sector
subgraphs are pairwise disjoint, and `p ne q`.  Contract a spanning tree
of each of `X_I,X_J`.  This is a proper minor, because both contracted
sets contain an edge.  Give the minor a proper six-colouring.

Pull the colouring back only on the unchanged far closed shore
`G[R union T]`: give every literal vertex of `I union {p}` the colour of
the representative of `X_I`, give every vertex of `J union {q}` the
colour of the representative of `X_J`, and retain every other colour.
This is proper.  The two displayed boundary sets are independent by safe
support.  Every edge from either set to an unchanged vertex survived at
the corresponding representative, and every edge between the two sets
survived between the two representatives.

In this far-shore colouring the traces `I` and `J` are monochromatic.
Each of the other three row traces has order at most one and is therefore
monochromatic automatically.  One row misses `T`, so the five-row
reflection theorem reflects the resulting literal equality partition
through `G[L union T]`.  After a permutation of the six colours, the two
closed-shore colourings agree on `T` and glue, contrary to the hypothesis
on `G`.  \(\square\)

The conclusion uses one simultaneous proper-minor operation.  No colour
class is identified with a branch-set label without the two literal
connected subgraphs `X_I,X_J`.

## 3. Four concentrated contact patterns

Assume now that adjacency from `B={b_0,b_1,b_2}` to the five connected
sets is complete except for one of the following normalized sets of
nonadjacent pairs:

\[
\begin{array}{c|l}
A& b_0C_0,\ b_0C_1,\ b_0C_2,\\
B& b_0C_0,\ b_0C_1,\ b_1C_3,\\
C& b_0C_0,\ b_1C_0,\\
D& b_0C_2,\ b_0C_3.
\end{array}                                               \tag{3.1}
\]

Here `bC_r` means `E_G(b,C_r)=varnothing`.  Before checking independence,
the possible distinct support assignments are:

\[
\begin{array}{c|c|c|c}
 &\text{vertices supporting }I&\text{vertices supporting }J
 &\text{useful assignments }(I,J)\\ \hline
A&\{b_1,b_2\}&\{b_1,b_2\}&(b_1,b_2),(b_2,b_1)\\
B&\{b_1,b_2\}&\{b_2\}&(b_1,b_2)\\
C&\{b_2\}&\{b_0,b_1,b_2\}&(b_2,b_0),(b_2,b_1)\\
D&\{b_1,b_2\}&\{b_1,b_2\}&(b_1,b_2),(b_2,b_1).
\end{array}                                               \tag{3.2}
\]

Thus contact placement alone supplies a system of distinct
representatives for the two paired traces in every pattern.  By Theorem
2.1, a survivor must destroy every assignment in the last column by a
literal edge inside the boundary.

## 4. Exact boundary-edge obstruction

For `b in B`, write

\[
 \begin{aligned}
 E_I(b)&:\Longleftrightarrow
       E_G(\{b\},I)\ne\varnothing,\\
 E_J(b)&:\Longleftrightarrow
       E_G(\{b\},J)\ne\varnothing.
 \end{aligned}                                             \tag{4.1}
\]

These assertions refer to literal boundary edges, not merely to a contact
with the connected set containing the corresponding root.  The support
assignments in (3.2) and Theorem 2.1 give the following necessary
conditions for a non-six-colourable survivor.

### Pattern A or D

Both assignments must fail, so

\[
 \bigl(E_I(b_1)\lor E_J(b_2)\bigr)
 \ \land\
 \bigl(E_I(b_2)\lor E_J(b_1)\bigr).                    \tag{4.2}
\]

In particular, at least two literal boundary edges are required.  A
minimal blocker consists of one edge witnessing each parenthesis in
(4.2).  The two edges can be incident with one `b` vertex or with two
different `B` vertices.

### Pattern B

There is only one useful assignment, and it is blocked precisely when

\[
                         E_I(b_1)\lor E_J(b_2).          \tag{4.3}
\]

Thus one edge from `b_1` to an `I` root, or one edge from `b_2` to a `J`
root, is already the minimal obstruction.

### Pattern C

The vertex `b_2` is the only contact support for `I`.  Either it is unsafe,
or both possible supports for `J` are unsafe:

\[
                 E_I(b_2)
       \ \lor\
                 \bigl(E_J(b_0)\land E_J(b_1)\bigr).   \tag{4.4}
\]

The first alternative is a one-edge blocker; the second needs at least two
literal boundary edges.

Equations (4.2)--(4.4) are the complete obstruction to this simultaneous
contraction mechanism for the four normalized contact patterns.  They do
not assert that such blockers occur in a hypothetical counterexample.

## 5. Remaining step and trust boundary

The theorem converts the four contact-allocation residues into a smaller,
literal problem: apply the proper edge-deletion response at one of the
boundary edges in (4.2)--(4.4), while retaining a safe connected carrier
for the opposite paired trace.  A six-colouring after deleting the blocker
edge makes its ends equal and supplies the usual bichromatic Kempe paths,
but that colouring is not proper on the unchanged far shore when the edge
is restored.  A further label-preserving composition is therefore still
needed to obtain

1. an explicit `K_7`-minor model;
2. one boundary equality partition extending through both closed shores;
   or
3. a strict host-level reduction preserving the two paired traces and the
   five named far-side connected subgraphs.

The theorem does not handle additional missing `B`--`C_r` contacts beyond
the four exact patterns in (3.1).  Nor does it prove the existence of the
five cycle-disjoint connected sector subgraphs.  Those are separate
reserved-cycle and contact-compression obligations.

The local graph obtained from a `5`-cycle, the three vertices of `B`, a
degree-eight centre, and one exterior vertex complete to the eight
neighbour labels realizes the boundary-edge obstruction when the four
root sectors are singletons.  It is six-colourable and is not
seven-connected.  It therefore does not have the non-six-colourability,
seven-connectivity, or proper-minor transition structure of the active
host, and is not a counterexample to this theorem or to `HC_7`.

## 6. Dependency

- [five-row reflection across a separation](hc7_five_row_separator_reflection.md)
