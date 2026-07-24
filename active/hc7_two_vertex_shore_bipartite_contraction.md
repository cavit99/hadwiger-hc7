# A contraction obstruction for a two-vertex shore and a nearly bipartite boundary

**Status:** active written proof; separate internal audit GREEN in
[`hc7_two_vertex_shore_bipartite_contraction_audit.md`](hc7_two_vertex_shore_bipartite_contraction_audit.md).
The finite order-eight consequence in Section 4 is computer-assisted, has a
separately checked certificate package, and is not part of the written
theorem.  Neither result is promoted here, and nothing here proves `HC_7`.

## 1. Setting

Let `G` be a finite simple graph such that

\[
 \chi(G)=7,\qquad
 \chi(M)\le 6\quad\text{for every proper minor }M\text{ of }G. \tag{1.1}
\]

Let `(A,B)` be a separation of `G`, put `X=V(A\cap B)`, and suppose

\[
                         V(A-B)=\{v,a\},\qquad va\in E(G). \tag{1.2}
\]

Thus the open `A`-shore is the literal edge `va`; in particular, every
neighbour of `v` or `a` outside `{v,a}` lies in `X`.

## 2. Contraction lemma

### Theorem 2.1 (two-vertex-shore bipartite contraction)

Assume `|X|\ge3`.  There do not exist a set `Z subseteq X` with `|Z|\le2`
and a partition

\[
                         X-Z=P\mathbin{\dot\cup}Q                 \tag{2.1}
\]

such that

\[
 \begin{aligned}
   &P\text{ and }Q\text{ are independent in }G[X],\\
   &P\subseteq N_G(v),\qquad Q\subseteq N_G(a).
 \end{aligned}                                                   \tag{2.2}
\]

#### Proof

Contract a spanning tree of each of the two disjoint connected sets

\[
                         \{v\}\cup P,\qquad \{a\}\cup Q,           \tag{2.3}
\]

leaving their contraction images distinct.  At least one contraction is
nontrivial because `|X-Z|\ge1`, so the resulting graph `M` is a proper
minor of `G`.  By (1.1), fix a proper six-colouring `c` of `M`.

The edge `va` survives between the two contraction images, so those images
receive distinct colours.  Expand the first image only over `P` and the
second only over `Q`, and retain `c` on every other vertex of `B`.  This
gives a proper six-colouring `c_B` of `B`:

- no edge has both ends in `P` or both ends in `Q`, by their independence;
- every edge between `P` and `Q`, from `P union Q` to `Z`, or from
  `P union Q` to `B-X` is represented by an edge incident with the
  corresponding contraction image in `M`.

On the boundary, all of `P` has one colour, all of `Q` has a second colour,
and the vertices of `Z` contribute at most `|Z|` further colours.  Hence

\[
                         |c_B(X)|\le2+|Z|\le4.                    \tag{2.4}
\]

Choose two distinct colours from the six-colour palette that are absent
from `c_B(X)`, assign them to `v` and `a`, and leave `c_B` unchanged on
`B`.  The edge `va` is proper.  Every other edge incident with `v` or `a`
ends in `X`, where both new colours are absent.  This is a proper
six-colouring of `G`, contradicting `chi(G)=7`. \(\square\)

## 3. Full-endpoint consequence

### Corollary 3.1 (odd-cycle transversal of order at most two)

Under the hypotheses of Theorem 2.1, suppose both `v` and `a` are adjacent
to every vertex of `X`.  Then no set `Z subseteq X` of order at most two
makes `G[X-Z]` bipartite.

#### Proof

If `G[X-Z]` were bipartite, take its two bipartition classes as `P,Q`.
They are independent, and fullness of both endpoints gives
`P subseteq N_G(v)` and `Q subseteq N_G(a)`.  Theorem 2.1 applies.
\(\square\)

Equivalently, in this full-endpoint configuration the odd-cycle
transversal number of `G[X]` is at least three.

## 4. Separate finite order-eight input

The following finite statement is certified by exhaustive computation:

> **Finite OCT assertion.** Every `K_4`-minor-free graph on eight vertices
> has an odd-cycle transversal of order at most two.

Combining that assertion with Corollary 3.1 would exclude the case in which

\[
 |X|=8,\qquad
 G[X]\text{ is }K_4\text{-minor-free},\qquad
 N_G(v)\cap X=N_G(a)\cap X=X.                         \tag{4.1}
\]

This order-eight exclusion is therefore presently a **computer-assisted
consequence**, not an additional conclusion of the written proof above.
The deterministic
[certificate generator](hc7_order8_k4minor_oct_certificate.py), independent
[certificate checker](hc7_order8_k4minor_oct_check.py), and
[internal audit](hc7_order8_k4minor_oct_audit.md) record its exact finite
scope.  It should not be cited as a promoted repository result while this
package remains in `active/`.

## 5. Near-full endpoints and the exact limitation

If one or both endpoints miss vertices of `X`, a bipartition of `X-Z` need
not satisfy the orientation requirements in (2.2).  For example, suppose
`r` is the unique vertex of `X` missed by `v`, `s` is the distinct unique
vertex missed by `a`, and `r,s notin Z`.  Then `r` is adjacent to `a` but
cannot lie in `P`, while `s` is adjacent to `v` but cannot lie in `Q`.
The theorem therefore requires a bipartition orientation placing `r` in
`Q` and `s` in `P`.  In a connected bipartite component containing both
vertices, this is possible exactly when `r` and `s` lie in opposite
bipartition classes.

Thus an odd-cycle transversal of order at most two alone does not settle
the near-full case.  The surviving obstruction is an orientation, or
bipartite-parity, incompatibility.  The theorem does not show that the
named edge-deletion operation, seven- or eight-connectivity, or
`K_7`-minor exclusion resolves that incompatibility.

## 6. Trust boundary and dependencies

Theorem 2.1 is an unbounded written argument.  It uses only:

1. the explicit proper-minor six-colourability hypothesis (1.1);
2. the literal separation and two-vertex shore in (1.2); and
3. the independent-set and endpoint-neighbourhood conditions (2.1)--(2.2).

It does not use `K_7`-minor exclusion, connectivity, Kempe-chain geometry,
or any finite enumeration.  Conversely, it produces only a contradiction
for the displayed two-vertex shore; it does not produce a rooted
`K_4` model, a `K_7`-minor model, or a strict exact-seven response.

The finite OCT assertion in Section 4 is logically separate.  Any later
use of the full/full order-eight consequence must cite both this written
lemma and the independently checked finite assertion.

Context only:

- [bounded-interface bridge-composition frontier](hc7_bounded_interface_synchronization_frontier.md)
- [minimum degree-eight root-star response reduction](../results/hc7_degree8_minimal_root_star_response_reduction.md)
