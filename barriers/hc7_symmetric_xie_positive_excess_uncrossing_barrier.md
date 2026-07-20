# Symmetric positive-excess cuts do not uncross by neighbourhood submodularity

**Status:** explicit counterexample to an intermediate claim, with a
deterministic finite verifier; separate internal audit **GREEN** in
[`hc7_symmetric_xie_positive_excess_uncrossing_barrier_audit.md`](hc7_symmetric_xie_positive_excess_uncrossing_barrier_audit.md).
The verifier is
[`hc7_symmetric_xie_positive_excess_uncrossing_barrier_verify.py`](hc7_symmetric_xie_positive_excess_uncrossing_barrier_verify.py).
This graph is not a counterexample to `HC_7`.

## 1. The refuted intermediate principle

The positive-excess outcome in Lemma 5.1 and Corollary 5.2 of the ordered
two--three allocation theorem can occur on both sides of a connected
order-eight interface.  A tempting next step is to apply full-neighbourhood
submodularity to the two selected connected sides.

The following principle is false, even after retaining seven-connectivity
and `K_7`-minor exclusion.

> **Symmetric-cut uncrossing principle (false).**  Let `G` be a
> seven-connected `K_7`-minor-free graph with an actual order-eight
> separation `(L,S,R)`, where `R` is nonempty, connected, and adjacent to
> every vertex of `S`.  Suppose `L=E dotcup D`, where `E,D` are adjacent
> connected subgraphs, and selected Xie completions on both `E` and `D`
> have terminal-free nonempty connected sides `C_E,C_D` behind separators
> of order at most five.  If both full neighbourhoods have order at least
> nine, then neighbourhood submodularity forces a `K_7` minor or makes one
> of `C_E`, `C_D`, or `C_E union C_D` have boundary of order at most eight.

The construction below has

\[
 |N_G(C_E)|=|N_G(C_D)|=9,
 \qquad |N_G(C_E\cup C_D)|=16.                 \tag{1.1}
\]

Thus the empty meet corner absorbs all of the submodular slack.

## 2. Construction

Start with the 32-vertex planar triangulation obtained from the icosahedron
as follows.  Retain its twelve vertices, introduce one vertex for each of
its twenty triangular faces, join a face vertex to its three incident old
vertices, and join two face vertices when their faces share an edge.  On
the deterministic NetworkX labelling used by the verifier, make these five
planar diagonal flips, in order:

\[
\begin{array}{c|c}
\text{deleted edge}&\text{added edge}\\ \hline
17\,18&1\,2\\
13\,15&0\,8\\
27\,28&11\,4\\
23\,26&4\,6\\
12\,14&0\,5.
\end{array}                                      \tag{2.1}
\]

Call the resulting planar graph `H`.  It has 32 vertices, 90 edges, and
vertex-connectivity five.  Vertices `0` and `4` are nonadjacent, each has
degree seven, and their open neighbourhoods in `H` are disjoint.

Let

\[
                           G=K_2\mathbin\vee H,   \tag{2.2}
\]

and call the two universal adjacent vertices `p,q`.  Then `G` is
seven-connected.  It is `K_7`-minor-free: at most two branch sets of a
`K_7` model can meet `{p,q}`, so at least five branch sets would lie in
the planar graph `H`, producing a `K_5` minor in `H`.

Put

\[
 S=\{p,q,2,12,13,17,18,19\}.                    \tag{2.3}
\]

The components of `G-S` are the singleton `R={1}` and a connected
25-vertex set `L`.  Moreover, `N_G(1)=S`, so `R` is adjacent to every
literal boundary vertex.  Partition `L` into

\[
\begin{aligned}
 E={}&\{0,5,6,7,8,9,14,15,21,22,25,26,27,28,31\},\\
 D={}&\{3,4,10,11,16,20,23,24,29,30\}.
\end{aligned}                                    \tag{2.4}
\]

Both induced subgraphs are connected and an edge joins them.

## 3. Two simultaneous terminal-free completion cuts

For the `E`-side completion, use the nominated triple

\[
                       (6,7,12)
\]

and nominated pair `(9,21)`, adding the virtual pair edge and all six
triple-to-pair edges.  The five-set

\[
                         K_E=\{5,8,12,14,15\}     \tag{3.1}
\]

separates the terminal-free singleton `C_E={0}` from another nonempty
side.  Its internal neighbourhood is

\[
                         N_E(0)=\{5,8,14,15\}.    \tag{3.2}
\]

Symmetrically, on `D union {2}` use the nominated triple `(3,10,2)` and
pair `(16,20)`.  The three-set

\[
                         K_D=\{11,23,24\}         \tag{3.3}
\]

separates the terminal-free singleton `C_D={4}` from another nonempty
side, with

\[
                         N_D(4)=\{11,23,24\}.     \tag{3.4}
\]

Their full neighbourhoods are

\[
\begin{aligned}
 N_G(0)&=\{p,q,5,8,12,13,14,15,16\},\\
 N_G(4)&=\{p,q,6,11,23,24,26,27,28\}.
\end{aligned}                                    \tag{3.5}
\]

They intersect exactly in `{p,q}`.  Since `0,4` are nonadjacent,

\[
 |N_G(\{0,4\})|=16.                              \tag{3.6}
\]

Each singleton neighbourhood is an actual separation boundary.  Full
neighbourhood submodularity therefore gives only

\[
                 9+9\ \ge\ 16+|N_G(\varnothing)|=16,  \tag{3.7}
\]

and supplies no order-seven or order-eight selected side.

## 4. Exact scope

This example retains more than an abstract set system:

- `G` is seven-connected and `K_7`-minor-free;
- `(L,S,R)` is an actual order-eight separation, with `R` connected and
  adjacent to every vertex of `S`;
- `L` is the union of two adjacent connected subgraphs; and
- both selected Xie completions have a terminal-free side behind a cut of
  order at most five, while both corresponding full boundaries have
  positive excess over seven.

It does **not** realize the full live `HC_7` configuration.  In particular:

- `G` is six-colourable, because deleting `p,q` leaves the planar graph
  `H`; it is neither seven-chromatic nor contraction-critical;
- `R` has only one connected subgraph adjacent to every boundary vertex,
  rather than two vertex-disjoint such subgraphs;
- the boundary does not carry the two labelled rooted triangles and the
  opposite proper-minor colouring responses of the live branch; and
- no operation-specific equality partition or named branch-set data are
  asserted.

The graph also has unrelated order-seven separators, obtained from
five-vertex separators of `H` together with `{p,q}`.  Consequently it does
not refute a theorem allowed to return an arbitrary order-seven separator.
It refutes only the proposed inference that the **two selected symmetric
Xie cuts**, together with ordinary full-neighbourhood submodularity, must
themselves yield a `K_7` minor or a selected boundary of order at most
eight.

The missing input must therefore use information absent here: two disjoint
boundary-full subgraphs on the opposite shore, contraction-critical
proper-minor colouring responses, or label-preserving branch-set geometry.
