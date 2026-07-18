# Hamiltonian-cycle reduction for the four-root degree-eight disk

**Status:** written proof; separate internal audit.

This note replaces the unproved simultaneous bigon uncrossing in
`hc7_rooted_cyclic_sector_or_small_separator.md`.  It proves a stronger
cycle statement by using a published two-vertex-deletion theorem for
four-connected planar graphs.  What remains is a sharply stated root
allocation problem on that cycle; no claim is made that the allocation is
already solved.

## 1. Setup

Let `H` be a simple plane graph, let

\[
                         U=\{u_0,u_1,u_2,u_3\},
\]

and assume that every vertex of `U` is incident with the outer face while
every vertex of `H-U` is in the open disk bounded by that face.  Suppose:

1. `H` is three-connected;
2. the rooted pair `(H,U)` is internally four-connected, meaning that
   there is no separation `(A,B)` of `H` with

   \[
       U\subseteq A,\qquad B-A\ne\varnothing,
       \qquad |A\cap B|\le3;                         \tag{1.1}
   \]

3. `v` is a vertex of `H-U` with five distinct neighbours

   \[
                          C=N_H(v)=\{c_0,\ldots,c_4\}. \tag{1.2}
   \]

The application is the degree-eight equality in the two-pair disk: the
three other neighbours of `v` lie in the order-seven boundary.

## 2. Four-connected planar augmentation

### Theorem 2.1

Add a new vertex `r` in the outer face and join it to every member of `U`.
Call the resulting plane graph `J`.  Then `J` is four-connected.

#### Proof

The four new edges can be drawn in the outer face, so `J` is planar.
Suppose that a set `S` of at most three vertices disconnects `J`.

If `r in S`, then `S-{r}` has order at most two.  The graph
`H-(S-{r})` is connected because `H` is three-connected, and hence `J-S`
is connected, a contradiction.

Assume that `r notin S`.  The component of `J-S` containing `r` also
contains every member of `U-S`.  Any other component `K` contains no
member of `U-S`, and therefore `K subseteq V(H)-U`.  In `H`, the pair

\[
   \bigl(H-K,\;H[K\cup S]\bigr)                       \tag{2.1}
\]

(with edges assigned in the usual way) is a separation of order at most
three.  Its first closed side contains all of `U`: members of `U cap S`
belong to the separator, and every member of `U-S` lies outside `K`.
Its second open side contains the nonempty set `K`.  This contradicts
(1.1).  Thus no such `S` exists.  \(\square\)

### Corollary 2.2 (a spanning cycle avoiding `r` and `v`)

The graph `H-v` has a Hamiltonian cycle.  In particular, it has a cycle
containing all nine nominated vertices in `U union C` (with coincident
members counted only once).

#### Proof

Thomas and Yu proved that deleting at most two vertices from a
four-connected planar graph leaves a Hamiltonian graph.  Apply their
theorem to `J-{r,v}=H-v`.  \(\square\)

The exact published input is statement (3.4) in R. Thomas and X. Yu,
*4-connected projective-planar graphs are Hamiltonian*, Journal of
Combinatorial Theory, Series B **62** (1994), 114--132.  Their statement
(3.3) additionally permits one prescribed edge on either chosen facial
circuit exposed by deleting `r` and `v`.

## 3. Exact root-allocation residue

Fix a Hamiltonian cycle `W` in `H-v`.  List the five members of `C` in
their cyclic order on `W`.  Cutting `W` once in each of the five open
intervals between consecutive members of `C` gives five disjoint connected
path sets, one containing each `c_i`, with cyclic adjacencies.

The required four-root cyclic-sector conclusion follows whenever the cuts
can be chosen so that four different path sets contain the four different
members of `U`.  The following elementary criterion isolates exactly when
the cyclic order itself is sufficient.

### Lemma 3.1 (cyclic interval allocation)

For each root `u in U-C`, record the open `C`-interval of `W` containing
`u`.  Regard every root in \(U\cap C\) as already assigned to, and
occupying, that member of `C`.  Suppose the remaining roots can be assigned
to endpoints of their recorded intervals so that the combined assignment of
all four roots to members of `C` is injective, with roots occurring in one
interval assigned monotonically from its left endpoint to its right
endpoint.  Then `W` can be partitioned into five cyclic connected sets,
one containing each member of `C`, four of which contain the four distinct
roots in `U`.

#### Proof

In every open interval between consecutive members of `C`, choose one cut
edge after all roots assigned to its left endpoint and before all roots
assigned to its right endpoint.  (If one of those two classes is empty,
choose the cut at the corresponding end.)  The five resulting path sets
are disjoint and connected and retain the five cycle adjacencies.  The
injective assignment puts the four roots in four distinct sets.  \(\square\)

When `U` and `C` are disjoint, the only failures of the underlying Hall
condition are:

1. at least three roots lie in one `C`-interval; or
2. all four roots lie in two adjacent `C`-intervals, with two in each.

Indeed, each root has the two endpoints of its interval as possible
recipients.  Hall can fail for three roots only when they share one
interval, and can fail for all four only when the union of their interval
endpoints has order at most three, which is precisely the second pattern
after the first has been excluded.  With at most two roots in an interval,
the matching can be chosen monotone there.

Thus the old unbounded path-overlap problem has been reduced, without an
uncrossing assumption, to two explicit **root-clustering patterns on a
Hamiltonian cycle**.  A further proof must use chords or bridges forced by
four-connectivity to move one clustered root to another `C`-interval, or
show that failure exposes a useful host separation.  Thomas--Yu (3.3)
allows the Hamiltonian cycle to be reselected through a prescribed edge
of either exposed facial circuit and is the natural next mechanism to
test.

## 4. The omitted low-separator case in the old draft

In the original exact-seven host setup

\[
 V(G)=L\mathbin{\dot\cup}T\mathbin{\dot\cup}R,
 \qquad |T|=7,
 \qquad E_G(L,R)=\varnothing,
\]

if a separation of `H=G[L union U]` of order at most two has neither open
side meeting `L`, then `L` is contained in its separator.  This case was
omitted from the old proof.  It does not yield the proposed shifted
separator, but the original partition itself already gives the genuine
order-seven separation with boundary `T` and nonempty open sides `L,R`.

This observation repairs the coarse statement “an order-seven separation
exists”; it does **not** repair the trace-preserving descent for which a
new boundary was wanted.

## 5. Trust boundary

Theorem 2.1 and Corollary 2.2 are unbounded and use literal host vertices.
They do not prove the four-root allocation in the two clustering patterns,
do not synchronize colourings across an order-seven boundary, and do not
by themselves construct a `K_7` minor.  The failed orthogonal-fan lemma is
not used.
