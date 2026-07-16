# Kempe transitions between opposite critical-edge responses

**Status:** written proof with a separate GREEN internal audit in
[`hc7_opposite_critical_edge_transition_audit.md`](hc7_opposite_critical_edge_transition_audit.md).
The direct transition theorem below is uniform in the number of colours.
It identifies the exact structure produced by one Kempe interchange between
the two one-edge-deletion responses.  It does not prove that such an
interchange, or even a Kempe sequence between the responses, exists.

## 1. Direct transition theorem

Let `q>=2`, let `G` be a graph which is not `q`-colourable, and let

\[
                         e=ab,\qquad f=cd
\]

be vertex-disjoint edges.  Put `H=G-{e,f}`, where both operations are edge
deletions.

### Theorem 1.1

Suppose `phi` is a proper `q`-colouring of `H` with signature

\[
             (e,f)=(\mathop{\rm equal},\mathop{\rm proper}),
\]

and one Kempe interchange on a component `K` of `H` changes `phi` to a
colouring `psi` with signature

\[
             (e,f)=(\mathop{\rm proper},\mathop{\rm equal}).
\]

Then there are two colours `alpha,beta` and two distinct components `K,K'`
of `H[phi^{-1}({alpha,beta})]` such that each of `K,K'` contains exactly
one endpoint of `e` and exactly one endpoint of `f`.

Consequently `H` contains two vertex-disjoint paths joining the endpoint
set of `e` to the endpoint set of `f`, with distinct ends at both edges.
The two deleted edges both join `K` to `K'` in `G`.
The two paths together with `e` and `f` contain a cycle through all four
endpoints in which `e` and `f` are the two distinguished cross-edges.

### Proof

Write `phi(a)=phi(b)=alpha`.  The interchange makes the ends of `e`
different, so its two colours are `alpha` and some `beta!=alpha`, and `K`
contains exactly one of `a,b`.  Relabel the ends so that

\[
                             a\in K,\qquad b\notin K.       \tag{1.1}
\]

The same interchange changes the ends of `f` from different colours to
one colour.  Hence exactly one of `c,d` belongs to `K`, both ends have
colours in `{alpha,beta}` under `phi`, and their colours are different.
Relabel them so that

\[
                             c\in K,\qquad d\notin K.       \tag{1.2}
\]

The colouring `phi` is a proper colouring of `G-e=H+f`.  Since `G` is not
`q`-colourable, the equal ends `a,b` lie in the same
`alpha`--`beta` component of `G-e`: otherwise interchanging the component
containing just one of them would make `e` proper while preserving every
edge of `G-e`, and would therefore colour `G`.

In `H`, however, `a` lies in `K` and `b` lies in a different
`alpha`--`beta` component.  The only edge of `(G-e)-H` is `f`.  It follows
that `f` joins `K` to the component `K'` of `H[alpha,beta]` containing
`b`.  By (1.2), its endpoint outside `K` is `d`, so `d\in K'`.

Thus `K` contains `a,c`, while `K'` contains `b,d`.  Connected paths
inside these two distinct components give the asserted vertex-disjoint
cross paths.  Finally `e` has one endpoint in each component by (1.1),
and the same is true of `f`.  If `P` is an `a`--`c` path in `K` and `Q`
is a `b`--`d` path in `K'`, then

\[
                         aPc\,dQb\,a
\]

is the asserted cycle, where `cd=f` and `ba=e` (the paths lie in disjoint
components and are chosen simple).  This proves every assertion.  \(\square\)

The proof is symmetric if the endpoint pairing is `a-d,b-c`.

## 2. Opposite-shore consequence

Suppose additionally that `(A,S,B)` is a separation of `G`, that `e` is
internal to `A`, that `f` is internal to `B`, and that every proper minor
of `G` is `q`-colourable.  Let

\[
\begin{aligned}
 X&=\{\text{`q`-colourings of `H` with signature `(equal,proper)`}\},\\
 Y&=\{\text{`q`-colourings of `H` with signature `(proper,equal)`}\},\\
 Z&=\{\text{`q`-colourings of `H` with signature `(equal,equal)`}\}.
\end{aligned}
\]

All three sets are nonempty: one-edge deletion gives `X,Y`, and colouring
`G/e/f` gives `Z`.  The fourth signature `(proper,proper)` is empty,
because it would colour `G`.

The opposite-shore incompatibility theorem shows that no member of `X`
and member of `Y` induce the same partition of the literal boundary `S`.
In particular, every direct Kempe interchange from `X` to `Y` changes the
boundary partition as well as producing the two paths in Theorem 1.1.

### Corollary 2.1 (three-chamber alternative)

If a component of the Kempe reconfiguration graph of `H` meets both `X`
and `Y`, then every Kempe path in that component from `X` to `Y` either

1. has a consecutive `X`--`Y` pair, to which Theorem 1.1 applies; or
2. contains a colouring in `Z`.

### Proof

Read the four possible signatures along the path.  The
`(proper,proper)` signature never occurs.  If no consecutive vertices lie
in `X` and `Y`, the first change from one of these sets toward the other
must pass through `Z`.  \(\square\)

## 3. Application and exact obstruction at the balanced boundary

At the balanced order-eight boundary, take `e` to be the edge between the
two vertices of the original five-clique lying in one open shore, and take
`f` to be an edge between two vertices of the second five-clique lying in
the opposite shore.  Theorem 1.1 would give two disjoint paths joining the
two endpoint sets, with distinct ends at each edge for one of the two
endpoint pairings, whenever the opposite one-edge responses differ by one
Kempe interchange.

There are two unresolved steps, and they are logically separate.

1. The common edge-deletion theorem gives a spanning `K_6` model in `H`,
   but that model is uncoloured.  It does not place the two opposite
   response colourings in one Kempe class.  Six-colourable,
   `K_7`-minor-free graphs with a spanning clique model can have several
   Kempe classes.  The common host in the `K_2`-join-icosahedron
   construction has a spanning `K_6` model by `HC_6` and absorption, and is
   the repository's warning mechanism:
   [`../barriers/hc7_two_root_kempe_class_icosahedron_barrier.md`](../barriers/hc7_two_root_kempe_class_icosahedron_barrier.md)
   That construction is not a counterexample under the full current
   hypotheses, because its ambient graph has both a `K_7` minor and an
   order-seven separation.
2. Even a direct transition gives only the two cross paths of Theorem 1.1.
   Their interiors can use vertices of the two five-cliques and both
   shores.  No proved theorem converts them, without additional avoidance
   or branch-set data, into a `K_7` model or an order-seven separation.

Therefore the proposed composition cannot use the common spanning `K_6`
model as an implicit recolouring bridge.  A valid continuation needs one
new host-level input of one of the following precise forms:

- a theorem putting suitable opposite critical-edge responses in one
  Kempe class under the terminal exclusions; or
- a label-preserving construction which uses the double-equality chamber
  `Z` or the two paths from Theorem 1.1 to produce a `K_7` model or a strict
  order-seven separation.

The first alternative is a genuine new recolouring theorem, not a
consequence of the existing common-deletion `K_6` model.
