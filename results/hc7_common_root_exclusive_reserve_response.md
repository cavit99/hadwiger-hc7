# Concentrated exclusive reserve responses

**Status:** written proof; separate internal audit: GREEN.
This theorem does not prove `HC_7`.

## 1. Setup

Assume either tight atomic outcome of the audited
[short-trace classification](../results/hc7_common_root_short_trace_classification.md).
Thus `G` is seven-connected and seven-chromatic, has no `K_7` minor, every
proper minor of `G` is six-colourable, `u` has degree eight or nine, and

\[
                         X=N_G(u),\qquad H=G[X].       \tag{1.1}
\]

The graph `G-N[u]` has exactly two components `E,F`, each adjacent to every
vertex of `X`.  Let `I` be the independent trace transversal from Theorem 5
of the short-trace classification and put `R=X-I`.  In the fixed colouring
`c` of `G-u`, the set `I` is the complete boundary colour class of one
colour `gamma`, while the five vertices of `R` have the other five colours,
one each.  Moreover,

\[
             |R|=5,\qquad \alpha(H)\le d_G(u)-5.      \tag{1.2}
\]

Let `D` be the set of all nonedges `rs` of `H[R]` such that the fixed
colouring has a `c(r)`--`c(s)` path whose open interior lies in `E`, but has
no such path whose open interior lies in `F`, and assume `|D|>=7`.  Thus `D`
is the set of `E`-exclusive reserve demands.  Write

\[
 q=\binom52-|E(H[R])|,
 \qquad
 N=\bigl(\tbinom R2-E(H[R])\bigr)-D.                 \tag{1.3}
\]

The set `N` consists of the nonexclusive reserve nonedges.

## 2. Matching swaps on the opposite shore

### Theorem 2.1 (matching-swap closure)

For every matching `M subseteq D`, the closed subgraph `G[F union X]` has a
proper six-colouring whose equality partition on `X` is

\[
 I\ \mid\ \{r,s\}\ (rs\in M)\ \mid\
 \{t\}\quad\bigl(t\in R-V(M)\bigr).                 \tag{2.1}
\]

#### Proof

Fix `rs in D`.  In the restriction of `c` to `G[F union X]`, let `K_rs` be
the component containing `r` in the subgraph induced by the two colours
`c(r),c(s)`.  The only boundary vertices with those colours are `r,s`.
Because `rs` is a nonedge, a path from `r` to `s` in this closed subgraph
would have nonempty open interior in `F`, contrary to exclusivity.  Hence

\[
                         K_{rs}\cap X=\{r\}.          \tag{2.2}
\]

Interchanging the two colours on `K_rs` is therefore a proper Kempe
interchange which changes the boundary only at `r`; it gives `r` the colour
of `s` and creates the pair block `{r,s}`.

If `rs,tu` are distinct edges of the matching, their two colour sets are
disjoint.  Consequently `K_rs` and `K_tu` are vertex-disjoint, either swap
leaves the other two-colour subgraph unchanged, and no edge between the two
swapped sets can become monochromatic.  All the swaps for `M` therefore
commute.  They fix `I` and every unmatched reserve vertex, and their boundary
partition is exactly (2.1).  \(\square\)

## 3. What proper-minor criticality forces

### Theorem 3.1 (critical-response normal form)

The pole-containing closed shore `G[E union X union {u}]` has a proper
six-colouring in which `I` is an exact boundary colour class and `R` has at
most four colour classes.  Every colouring obtained by the contraction in
the proof below satisfies at least one of the following:

1. one colour class contained in `R` has order at least three; or
2. some two-vertex colour class contained in `R` is a member of `N`.

In particular,

\[
 |N|\le3,
 \qquad
 |N|\le1\text{ in degree eight},
 \qquad
 |N|\le2\text{ in degree nine}.                      \tag{3.1}
\]

In degree eight the large block in outcome 1 has order exactly three.  In
degree nine it has order three or four.

#### Proof

The set `F union I` is connected: `F` is connected and is adjacent to every
vertex of `I`.  Contract it to one vertex `z`.  This is a proper minor, so it
has a proper six-colouring.  The vertices `u,z` are adjacent, and both are
adjacent to all five vertices of `R`.  They consequently receive distinct
colours, neither of which occurs on `R`.  Thus `R` uses at most four colours.

Discard the contracted copy of `F`, expand `z` only over the independent set
`I`, and give every member of `I` the colour of `z`.  Every retained edge
incident with `I` was represented by an edge at `z`, so this gives a proper
colouring of `G[E union X union {u}]`.  Since `z` was adjacent to every
member of `R`, the set `I` is an exact boundary colour class.

Suppose that all nonsingleton colour classes in `R` have order two and that
every such pair belongs to `D`.  These pair blocks form a matching `M`.
Theorem 2.1 gives a colouring of `G[F union X]` with exactly the same
boundary equality partition.  After permuting colour names, the two closed
shore colourings agree on `X` and glue to a proper six-colouring of `G`, a
contradiction.  Hence a response with no block of order at least three must
contain a pair in `N`.

There are ten reserve pairs and `|D|>=7`, so `|N|<=3`.  The sharper bounds
follow from Section 4 below: `q<=8` in degree eight and `q<=9` in degree
nine, whence `|N|=q-|D|` is at most one or two, respectively.  Finally,
every colour class is independent.  Formula (1.2) bounds its order by three
in degree eight and by four in degree nine.  \(\square\)

## 4. Six demands give a near-`K_7` model

### Theorem 4.1 (shore-confined six-demand model)

Choose any six-edge set `D_0 subseteq D`.  There are seven pairwise disjoint
connected branch sets

\[
                    B_r\ (r\in R),\qquad \{u\},
                    \qquad F\cup I                    \tag{4.1}
\]

such that every pair is adjacent except possibly pairs `B_r,B_s` for which

\[
             rs\in\bigl(\tbinom R2-E(H[R])\bigr)-D_0. \tag{4.2}
\]

Thus the branch-set contact graph is `K_7` with at most `q-6` possible
missing edges, all between reserve-rooted bags.  More precisely,

\[
 q-6\le
 \begin{cases}
 2,&d_G(u)=8,\\
 3,&d_G(u)=9.
 \end{cases}                                           \tag{4.3}
\]

The word *possible* is essential: additional contacts between the rooted
bags may remove some of the pairs in (4.2).

#### Proof

Let `Gamma` be the `gamma`-colour class of `c` in `G-u`, and put

\[
                         Q=(G-u)-\Gamma .              \tag{4.4}
\]

The audited five-reserve packet proves that `Q` is five-colourable with
`R` as a transversal and that every demand in `D_0` has its two roots in
one bichromatic component of `Q[E union R]`.  Kriesell--Mohr, Theorem 7,
applied to the six-edge demand graph `(R,D_0)`, gives five pairwise disjoint
connected rooted bags `B_r subseteq Q[E union R]`, adjacent for every edge
of `D_0`.

If `rs` is an edge of `H[R]`, the literal root edge joins `B_r` to `B_s`.
Hence only the reserve nonedges outside `D_0` can remain missing among the
five bags.

The set `F union I` is connected and disjoint from the five bags.  It is
adjacent to every `B_r` through a neighbour in `F` of the root `r`.  The
singleton `{u}` is adjacent to every `B_r` through `ur`, and it is adjacent
to `F union I` through any member of the nonempty set `I`.  This proves
(4.1)--(4.2).

It remains to bound `q`.  In degree eight, (1.2) gives
`alpha(H[R])<=3`, so the nonedge graph of `H[R]` contains no `K_4`.  Every
graph on five vertices with at least nine edges contains a `K_4`; hence a
`K_4`-free graph on five vertices has at most eight edges.  Thus `q<=8`.
In degree nine, `alpha(H[R])<=4`, so `R` is not independent
and `H[R]` has at least one edge; hence `q<=9`.  Subtracting the six demands
in `D_0` proves (4.3).  \(\square\)

### Corollary 4.2 (what the near model returns)

If the model in Theorem 4.1 is not already a `K_7` model, the full
neighbourhood of either branch set in a missing pair is the boundary of an
actual separation and has order at least seven.  No upper bound on this
separator follows from the theorem.

#### Proof

Let `B_r,B_s` be nonadjacent branch sets.  The connected set `B_s` lies
outside `B_r union N_G(B_r)`, so `N_G(B_r)` separates two nonempty vertex
sets.  Seven-connectivity gives `|N_G(B_r)|>=7`.  \(\square\)

## 5. Smallest abstract response-language obstruction

The matching-swap conclusion does not set-theoretically force a common
nonrainbow partition.  Let

\[
 R=\{1,2,3,4,5\},\qquad E(H[R])=\{14,25,45\}.          \tag{5.1}
\]

The seven remaining pairs are nonedges; call their set `D`.  The guaranteed
matching family from Theorem 2.1 contains the rainbow partition and every
partition obtained by merging the edges of a matching in `D`.  The
proper partition

\[
                         \{1,2,3\}\mid\{4\}\mid\{5\}  \tag{5.2}
\]

is not in that language, because it has a block of order three.  Thus a
critical pole response of the form (5.2) avoids every conclusion obtainable
from commuting disjoint pair swaps.

This is only an abstract response-language obstruction.  No claim is made
here that these two exact extension languages are realized simultaneously
inside a seven-connected, minor-minimal, `K_7`-minor-free host.

## 6. Exact remaining hypothesis

The concentrated residue is therefore reduced, but not closed.  A positive
continuation needs at least one genuinely new host-level statement:

1. a **trace-preserving or confluence theorem** which either retains one of
   the matching partitions under a proper-minor response or composes the
   pair swaps into the large block returned by Theorem 3.1; or
2. a **dirty-path completion theorem** which uses the at most two or three
   missing adjacencies in Theorem 4.1 to give an explicit `K_7` model, a
   separator of order at most nine with the required colouring response, or
   an actual smaller component of `G-N[u]` preserving that response.

Ordinary proper-minor criticality supplies an arbitrary colouring of the
contracted minor, not a selected boundary trace.  Seven-connectivity gives
only the lower bound in Corollary 4.2.  Neither fact supplies the missing
upper bound or trace alignment.

## Inputs

- [low-degree common-root short-trace classification](../results/hc7_common_root_short_trace_classification.md)
- [five-reserve Kempe packet](../results/hc7_common_root_five_reserve_kempe_packet.md)
- Matthias Kriesell and Samuel Mohr,
  [*Kempe Chains and Rooted Minors*](https://arxiv.org/abs/1911.09998),
  Theorem 7
