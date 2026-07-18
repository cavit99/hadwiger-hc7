# Lexicographic packet minimality does not peel a direct first entry

**Status:** explicit finite barrier with a deterministic verifier; separate
internal audit GREEN.  The graph is six-connected and `K_7`-minor-free,
but it is five-colourable and is not a hypothetical `HC_7` counterexample.

The accompanying checker is
[`hc7_first_entry_packet_minimality_barrier_verify.py`](hc7_first_entry_packet_minimality_barrier_verify.py).

## 1. Refuted geometric inference

The following inference is false one connectivity unit below the active
host hypotheses:

> If two disjoint adjacent boundary-full connected subgraphs and a
> bichromatic boundary-to-boundary path are chosen lexicographically to
> minimize the total order of the two subgraphs and then the path
> intersection, the first path vertex in their union can be peeled to give
> a strictly smaller such pair.

The example does **not** refute a theorem whose alternatives include an
arbitrary common boundary colouring: its displayed partition extends over
both shores.  Its purpose is narrower and exact.  It shows that
lexicographic geometry alone cannot supply the claimed smaller pair, even
with six-connectivity and `K_7`-minor exclusion.

## 2. Construction

Let

\[
 S=\{0,1,2,3,4,5,6\},\quad
 A=\{a_1,a_2,c_1,c_2\},\quad B=\{b\}.
\]

The boundary contains the cycle

\[
 01,12,23,34,45,56,60
\]

and the two additional edges `02,13`.  The open side `A` has the path

\[
                         a_1a_2c_1c_2.                 \tag{2.1}
\]

There are no `A-B` edges, and `b` is adjacent to every member of `S`.
The boundary neighbourhoods of the four vertices in `A` are

\[
\begin{array}{c|c}
a_1&\{0,1,4,5,6\},\\
a_2&\{2,3,4,5\},\\
c_1&\{0,2,5,6\},\\
c_2&\{1,2,3,4,5,6\}.
\end{array}                                            \tag{2.2}
\]

These rules define the graph completely.

## 3. The exact first-entry data

The boundary equality partition

\[
                 \{1,4,6\}\mid\{2,5\}\mid\{0\}\mid\{3\} \tag{3.1}
\]

is proper.  Give its four blocks four distinct colours, give
`a_1,c_1` the colour of `3`, give `a_2,c_2` the colour of `0`, and give
`b` a fifth colour.  This is a proper colouring of the whole graph.

Put

\[
             P_1=G[\{a_1,a_2\}],\qquad
             P_2=G[\{c_1,c_2\}].                      \tag{3.2}
\]

Both are connected and adjacent, and (2.2) shows that each is adjacent to
all seven vertices of `S`.  No singleton vertex of `A` is boundary-full.
Thus every pair of disjoint boundary-full connected subgraphs in `A` has
total order at least four, and the pair in (3.2) is minimum.

The path

\[
                         0a_1a_2 3                    \tag{3.3}
\]

is bichromatic.  The two-colour subgraph on the colours of `0,3` has no
other boundary vertices, and `03` is a nonedge.  Hence every `0-3` path in
that two-colour subgraph meets `P_1 union P_2`.  The displayed path enters
the minimum pair directly at `a_1` and has only two internal vertices, the
minimum possible intersection with the selected union.  There are other
bichromatic paths, but none avoids the union; uniqueness is not claimed.
No strictly smaller pair exists to be obtained by peeling `a_1`.

## 4. Connectivity and minor exclusion

The graph is six-connected.  Exhaustive deletion of at most five vertices
leaves it connected, while

\[
                       \{0,2,5,6,a_2,c_2\}             \tag{4.1}
\]

is a six-vertex cut isolating `c_1`.

The verifier also exhausts all spanning partitions into seven nonempty
connected parts and finds no pairwise adjacent partition.  This is a
complete `K_7`-minor test for a connected graph: any unused component of a
minor model can be absorbed, along a path to the model, into an adjacent
branch set.  Thus every `K_7` model can be extended to one whose seven
branch sets partition the whole vertex set.

## 5. Trust boundary

The example is not seven-connected: the cut (4.1) is exactly the missing
unit.  It is five-colourable, not seven-chromatic, and does not have the
proper-minor response system of a minimal counterexample.  The partition
(3.1) also extends over both closed shores, so synchronization is already
available.

The boundary graph is not one of the ten absolute-demand-three hard
boundaries used in the active `(1,2)` theorem.  For example, `{1,2}` is a
clique odd-cycle transversal: deleting it leaves the path
`3-4-5-6-0`.  Thus a low-demand partition exists even though the displayed
four-block partition itself has demand three.

Accordingly, the graph does not refute a host-level first-entry theorem
using seven-connectivity and contraction-critical colouring.  It refutes
only the proposed automatic **geometric peel** from packet/path
lexicographic minimality.  A positive theorem must spend one of the missing
host hypotheses at the direct entry.
