# The balanced response residue has a three-attachment bridge system

**Archive note:** unaudited frozen order-eight draft retained for provenance;
it is not part of the current proof spine.

**Status:** written proof; independent audit pending.  This is an unbounded
necessary condition in the balanced order-eight two-cut response case.  It
does not prove `HC_7`.

## 1. Setting

Assume the hypotheses and notation of the audited
[two-cut response-orientation theorem](../results/hc7_order8_two_cut_response_orientation.md),
and assume that the boundary bipartition is balanced:

\[
                 S-\{d,e\}=P\mathbin{\dot\cup}R,
                 \qquad |P|=|R|=3.                   \tag{1.1}
\]

Assume additionally that none of the following has occurred:

1. a proper six-colouring of `G`;
2. an actual order-seven separation; or
3. a strict boundary-full order-eight descent supplied by the audited
   small-boundary lobe theorem.

Fix a forced `d`--`e` path from the selected split-response colouring and
write its internal path as

\[
                         D=v_0v_1\cdots v_k.          \tag{1.2}
\]

For a component `A` of `G[C]-V(D)`, its **attachments** are

\[
                         N_{G[C]}(A)\subseteq V(D).   \tag{1.3}
\]

## 2. Every off-path component has three attachments

### Theorem 2.1

Every component `A` of `G[C]-V(D)` satisfies all of the following.

1. `A` misses the portal set of at least one literal vertex of `P` and at
   least one literal vertex of `R`.
2. `A` has at least three distinct attachments on `D`.
3. Let `v_i,v_j` be two attachments, `i<j`, and let `W` be a
   `v_i`--`v_j` path whose internal vertices lie in `A`.  Put

   \[
   I=\{v_{i+1},\ldots,v_{j-1}\}                       \tag{2.1}
   \]

   and define the augmented open span

   \[
   H(A;i,j)=I\ \cup
      \bigcup\left\{V(B):
       \begin{array}{l}
       B\ne A\text{ is a component of }G[C]-V(D),\\[-2pt]
       N_{G[C]}(B)\cap I\ne\varnothing
       \end{array}\right\}.                          \tag{2.2}
   \]

   If `I` is nonempty, then the connected subgraph induced by
   `H(A;i,j)` misses the portal set of at least one vertex of `P` and at
   least one vertex of `R`.

The same conclusion as item 3 holds for a chord `v_iv_j` of `D`, with no
excluded component `A` in (2.2).

### Proof

If `A` met the portal set of every vertex of `P`, retain `D` as the root
path and use `A` as the connected `P`-subgraph.  The audited forced-path
detour exchange then gives a proper six-colouring of `G`, contrary to the
standing assumption.  The same argument applies to `R`, proving item 1.

The components of `G[C]-V(D)` are pairwise anticomplete, so every internal
neighbour of `A` lies on `D`.  Item 1 says that `A` misses at least two
vertices of the eight-set `S`.  Consequently

\[
 |N_G(A)|
  =|N_{G[C]}(A)|+|N_G(A)\cap S|
  \le |N_{G[C]}(A)|+6.                               \tag{2.3}
\]

If `A` had at most two attachments, (2.3) would give
`|N_G(A)|<=8`.  The set `A` is nonempty, connected, and proper in `C`, so
the small-boundary lobe theorem would return outcome 2 or 3 from Section
1.  Both are excluded.  Hence `A` has at least three attachments, proving
item 2.

Now fix `A,i,j,W` as in item 3.  Every component `B` included in (2.2) is
connected and has an edge to `I`.  Therefore `G[H(A;i,j)]` is connected.
It is disjoint from

\[
 D'=D[v_0,v_i]\cup W\cup D[v_j,v_k].                 \tag{2.4}
\]

Indeed, `I` omits the two ends of the detour, the interior of `W` lies in
`A`, and every component included in (2.2) is different from `A`.

If `H(A;i,j)` met every portal set indexed by `P` or every one indexed by
`R`, use it as the connected boundary-block subgraph and use (2.4) as the
root path in the audited reserved-path boundary-response theorem.  The
other full component supplies the complementary boundary class.  The
theorem realizes both root responses on each opposite component-side, and
the split one aligns with the selected colouring on the closed `C`-side.
The resulting three colourings glue to a proper six-colouring.  Thus the
augmented span misses a portal label from each class.  This proves item 3.

For a chord, use the chord itself in place of `W`.  No off-path component
is consumed by the rerouted root path, so the union in (2.2) ranges over
all components meeting `I`.  The same disjointness and gluing argument
applies. \(\square\)

## 3. Exact gain

The theorem replaces a bridge-by-bridge obstruction by a condition on the
whole connected subgraph available behind each detour.  In particular,
two or more off-path components may cooperate through the open path span;
the theorem tests that cooperation simultaneously.

Thus every surviving balanced instance consists of off-path components
with at least three attachments, and every augmented detour span omits a
literal portal label from each three-element boundary class.  This is a
host-level interval constraint and is independent of the orders of the
lobes and bridges.

The theorem does not yet show that these missed labels occur in a cyclic
order, preserve the five inherited minor-model branch sets, or yield a
common equality partition on a smaller boundary.  Those are the remaining
allocation and response-transfer obligations.

## 4. Dependencies

- the audited forced-path detour exchange and its reserved-path
  boundary-response dependency;
- the audited small-boundary lobe descent; and
- the audited two-cut response orientation, which supplies the selected
  forced `d`--`e` path and literal boundary bipartition.
