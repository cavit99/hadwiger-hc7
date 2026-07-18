# Five prescribed vertices remain cyclable after three deletions

**Status:** written proof; separate internal audit.  This theorem is a
consequence of the exact order-seven full-packet bound and the classical
Watkins--Mesner cyclability theorem.  It does not prove `HC_7`.

## Theorem

Let `G` be a seven-connected, `K_7`-minor-free graph such that

\[
   \chi(G)=7
   \quad\text{and every proper minor of }G\text{ is six-colourable}.
                                                               \tag{1.1}
\]

For every set `X subseteq V(G)` of order at most three and every set
`W subseteq V(G)-X` of order five, the graph `G-X` has a cycle containing
all five vertices of `W`.

Equivalently, deleting any three vertices of `G` leaves a five-cyclable
graph.

## Proof

Put

\[
                              H=G-X.                        \tag{2.1}
\]

Deleting fewer than three vertices leaves a graph of connectivity at least
five.  Dirac's prescribed-vertex cycle theorem says that any five vertices
of a five-connected graph lie on one cycle, so the result is immediate when
`|X|<=2`.

Assume now that `|X|=3`.  Then `H` is four-connected.  If `H` is
five-connected, Dirac's theorem again applies.  It remains to suppose that

\[
                              \kappa(H)=4.                  \tag{2.2}
\]

Suppose for a contradiction that no cycle of `H` contains `W`.  The
Watkins--Mesner theorem for a graph of connectivity `lambda>3`, applied
with `lambda=4`, gives a four-vertex set `S` such that the five specified
vertices of `W` lie in five distinct components of `H-S`.  More precisely,
this is the necessity direction of their Theorem 1: its proof starts from
the specified noncyclable `(lambda+1)`-set and produces one `lambda`-set
separating its members into distinct components.

The set

\[
                              T=X\mathbin{\dot\cup}S        \tag{2.3}
\]

has order seven.  The components of `G-T` are exactly the components of
`H-S`, so there are at least five of them.  Every such component `C` is
adjacent to every vertex of `T`.  Indeed,

\[
                              N_G(C)\subseteq T,            \tag{2.4}
\]

and `N_G(C)` separates `C` from at least one other nonempty component of
`G-T`.  Seven-connectivity gives `|N_G(C)|>=7`, and hence

\[
                              N_G(C)=T.                     \tag{2.5}
\]

Choose one component as the first open shore and put every other component
in the second open shore.  This is an actual order-seven separation.  The
first shore contains one `T`-full connected subgraph, while the second
contains at least four pairwise vertex-disjoint `T`-full connected
subgraphs.  Thus the two packet numbers have sum at least five.

This contradicts the audited exact-seven full-packet theorem, which gives

\[
                              \nu_1+\nu_2\le4               \tag{2.6}
\]

for every actual order-seven separation in a graph satisfying (1.1).
Therefore `H` has a cycle through `W`, as required. \(\square\)

## Degree-eight application

Let `v` be a degree-eight vertex arising from the alternating four-root
disk, write its three neighbours outside that disk as

\[
                              B=\{b_0,b_1,b_2\},
\]

and let `C` be its five neighbours in the disk.  For each `i`, apply the
theorem with

\[
                  X=\{v\}\cup(B-\{b_i\}),\qquad W=C.       \tag{3.1}
\]

It follows that `G-X` has a cycle through all five members of `C`.  Hence
there are three such cycles, each avoiding `v` and two prescribed members
of `B`.  This is a fault-tolerant host-level replacement for relying on the
single facial boundary exposed by deleting `v`.

The theorem does **not** yet produce one cycle avoiding all of
`\{v\}\cup B`, nor a cycle disjoint from the connected seventh branch set.
Combining the three cycles while preserving the five branch-set labels is
the remaining exchange problem.

## Dependencies and citation boundary

The repository input is the
[exact-seven full-packet theorem](hc7_exact_seven_packet_packing.md).

The external input is Theorem 1, together with its necessity proof and
concluding uniqueness observation, of M. E. Watkins and D. M. Mesner,
*Cycles and Connectivity in Graphs*, Canadian Journal of Mathematics 19
(1967), 1319--1328,
<https://doi.org/10.4153/CJM-1967-121-2>.  In the notation of that paper,
when the connectivity and guaranteed cyclability are both `lambda>3`, a
specified noncyclable set of order `lambda+1` is split among distinct
components by a separator of order `lambda`.

Dirac's prescribed-vertex cycle theorem is used only in its classical
form: any `k` prescribed vertices of a `k`-connected graph lie on one
cycle.
