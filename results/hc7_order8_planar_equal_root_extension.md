# A cofacial planar side realizes the equal-root boundary partition

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_planar_equal_root_extension_audit.md`](hc7_order8_planar_equal_root_extension_audit.md).
This is an unbounded colour-extension theorem.  It does not prove `HC_7`.

## Theorem 1 (cofacial equal-root extension)

Let

\[
 V(F)=C\mathbin{\dot\cup}S,
 \qquad
 S-\{d,e\}=P\mathbin{\dot\cup}R,
 \tag{1.1}
\]

where `P` and `R` are nonempty independent sets, `de` is not an edge, and
`C` is disjoint from `S`.  Suppose that the graph

\[
                         F[C\cup\{d,e\}]              \tag{1.2}
\]

is planar in an embedding in which `d` and `e` lie on a common face.
Then `F` has a proper six-colouring whose equality partition on `S` is

\[
                         P\mid R\mid\{d,e\}.           \tag{1.3}
\]

### Proof

In the common face, draw an auxiliary edge `de`, and contract that edge.
The resulting graph is planar.  By the Four Colour Theorem it has a proper
colouring with at most four colours.  Expand the contracted vertex over the
two nonadjacent vertices `d,e`.  This gives a proper colouring of
`F[C\cup\{d,e\}]` with at most four colours in which `d` and `e` have one
common colour, say `alpha`.

Use two further colours, neither occurring on `C\cup\{d,e\}`: give every
vertex of `P` the first and every vertex of `R` the second.  The two classes
are independent and their colours are distinct, so this respects all edges
inside `S-\{d,e\}`.  Their colours also differ from `alpha`, so all boundary
edges incident with `d` or `e` are proper.  Finally, neither new colour
occurs in `C`, so every edge from `C` to `P\cup R` is proper.  The resulting
six-colouring has exactly the boundary partition (1.3). \(\square\)

The proof permits fewer than four colours in (1.2): unused colours may be
added to the palette before assigning the two fresh block colours.

## Corollary 2 (closure of the attachment-free two-paths web)

Assume the hypotheses and notation of the audited
[two-cut response-orientation theorem](hc7_order8_two_cut_response_orientation.md),
and suppose one bipartition class has order two, say `P={p,q}`.  If

\[
                         G[C\cup\{d,e,p,q\}]           \tag{2.1}
\]

is a spanning subgraph of an attachment-free planar `(d,p,e,q)`-web, then
`G` is six-colourable.

### Proof

The planar web skeleton gives an embedding of (2.1) in which
`d,p,e,q` occur in this cyclic order on the outer face.  Delete `p,q` from
that embedding.  The vertices `d,e` remain incident with the outer face, so
Theorem 1 applies to the closed `C`-side and gives a six-colouring inducing

\[
                         P\mid R\mid\{d,e\}.           \tag{2.2}
\]

The response-orientation theorem gives a six-colouring of each individual
closed `Q_i`-side inducing the same labelled partition.  Permute colour
names so that the three colourings agree on the three blocks in (2.2).
The components `C,Q_0,Q_1` of `G-S` are pairwise anticomplete, so the
colourings glue to a proper six-colouring of `G`. \(\square\)

## Corollary 3 (the two-vertex class closes)

In the setting of the audited two-cut response-orientation theorem, if one
class of `S-{d,e}` has order two, then at least one of the following holds:

1. `G` is six-colourable; or
2. `G` has an actual separation of order seven whose connected shore lies
   in `C`.

### Proof

Apply the audited unbalanced-bipartition reduction.  Its positive linkage
outcome gives item 1, and a nonempty web attachment gives item 2.  Its only
remaining outcome is the attachment-free web, which Corollary 2 makes
six-colourable. \(\square\)

## Exact gain and trust boundary

Corollary 3 eliminates the planar-web residue for arbitrarily large lobes
and web skeletons; it is not a finite enumeration.  The returned
order-seven separation is not proved here to carry the same complete
equality partition on both closed shores.  The theorem does not treat the
balanced `3+3` bipartition, whose reserved connected-subgraph problem has
three terminals rather than two.

## Dependencies

- the Four Colour Theorem;
- the audited two-cut response-orientation theorem; and
- the audited unbalanced-bipartition web reduction.
