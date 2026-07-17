# Audit of the labelled near-`K_7` internal-edge fork

**Verdict:** GREEN for the exact source revision identified below.

This is an independent internal mathematical audit.  It verifies the
conditional statements in the source file; it is not external peer review
and does not prove that every hypothetical `HC_7` counterexample reaches the
conditional defect-one configuration.

## Audited revision

The audited file is
`active/hc7_defect_one_near_k7_edge_fork.md`.

**Source SHA-256:**
`41682f92a0bbab28652e439e472e48ba61b59012d46f5d808db59c0dd20435d1`.

After the mathematical audit, the source status was changed from
"written proof draft awaiting a separate exact-file audit" to "written
proof; separate internal audit GREEN."  Replacing that one status line by
its prior text reproduces the initially audited SHA-256
`0aaaf97cc24c7f4a1dc4183c4be9c14bc5d742447b2c6ab46771db09faa02aca`
exactly.  No mathematical statement or proof text changed.

The relevant audited dependencies are:

- `results/hc7_component_contact_defect_theorem.md`, SHA-256
  `247de0124f0fadf2000aa2984e77c709fece88d2daf9515fae9cd8ed4e1b44a5`;
- `results/hc7_defect_one_simplicial_normalization.md`, SHA-256
  `a6c954234ec2121b0150959f4ce9cff18e78045932a4d331343094db2bf88b05`.

## 1. Setup and the two-tree triangle

All four parts of the component-contact graph are nonempty, so the two-tree
`J` has at least four vertices.  If the chosen simplicial degree-two vertex
`l` was added on `mn`, the edge `mn` already lay in a triangle before that
addition.  If instead `l` is a vertex of the initial triangle and still has
degree two in the final two-tree, no later vertex was added on either edge
incident with `l`.  The first later addition must therefore have been on the
opposite edge `mn`, and supplies a triangle through `mn` avoiding `l`.
This includes the order-four initial-triangle case.  Thus there is indeed a
vertex `r` in `J-l` adjacent to both `m,n`.

The represented subgraphs `L,M,N,R` are pairwise disjoint and disjoint from
the three anchors.  The triangle `mnr` supplies all adjacencies among
`M,N,R`, and every selected component is adjacent to all three anchors.
Consequently the six displayed sets in (2.1) form a `K_6`-minor model
disjoint from `L`.  Adding `L` gives all required adjacencies except
`LR`, because `l` is adjacent to `m,n` and every anchor.  Hence (2.2) is a
labelled `K_7^-` model.  If the remaining adjacency happened to exist in
the host, the same seven disjoint connected sets would be an explicit
`K_7` model.

Because the model (2.1) uses no vertex of `L`, deleting vertices or
contracting edges wholly inside `L` leaves that displayed model intact.
The source correctly warns that this model-survival statement gives no
chromatic lower bound after the operation.

## 2. Chromatic five-or-six fork

Both `G/xy` and `H=G-{x,y}` are proper minors, so they are six-colourable.
A five-colouring of `G/xy` would expand by giving one endpoint the
contracted colour and the other a new sixth colour, contradicting
`chi(G)=7`.  A four-colouring of `H` would similarly extend by two distinct
new colours.  Therefore

\[
             \chi(G/xy)=6,\qquad 5\le\chi(H)\le6.
\]

These two values of `chi(H)` are mutually exclusive and exhaustive.

### Five-colour branch

For a five-colouring of `H`, giving both ends of the deleted edge the new
colour `6` properly colours `G-xy`.  For
`pi=(6,j_1,...,j_s)`, orient a colour-relevant edge from colour `c` to
colour `pi(c)` and take the set reachable from `x`.  Rotating by `pi` on
that set remains proper: any newly monochromatic crossing edge would have
its outside endpoint in the next colour and hence would be a directed
reachability step.  If `y` were outside the set, the rotation would
separate the colours of `x,y`, allowing `xy` to be restored, a
contradiction.

A shortest directed `x`--`y` path is simple.  Its colours follow the
displayed cycle, and the only vertices having colour `6` are `x,y`.
Therefore it reaches `y` at its first return to colour `6`; its internal
colours are exactly `j_1,...,j_s` in order.  Taking `s=1` gives a common
neighbour of `x,y` in each of the five colour classes.  The argument is
edge-local: no double-critical hypothesis is imposed on any other edge.

### Six-colour branch

For any six-colouring `phi` of `H`, assigning distinct representatives from
`M_x(phi)` and `M_y(phi)` to `x,y` would colour `G`.  Two finite sets have no
distinct representatives precisely when at least one is empty, or both are
the same singleton.  This is exactly the three-alternative statement
(3.4); importantly, it permits asymmetric one-sided-hole colourings.

Restricting a six-colouring of `G/xy` to `H` produces a colour `alpha`
missing from both endpoint neighbourhoods.  If an additional colour were
missing at either endpoint, that colour and `alpha` could be assigned in
the appropriate order to `x,y`.  Thus this particular colouring has
`M_x=M_y={alpha}`, proving the asserted existence of a common-hole
colouring.  It does not assert that every six-colouring has a common hole.

## 3. Explicit repair and its corollary

The five sets `B_1,...,B_5` are disjoint connected branch sets and are
pairwise adjacent: the anchors form a triangle, `M,N` are adjacent, and
both meet all anchors.  Cutting a spanning tree of `G[L]` at `xy` gives two
nonempty, disjoint, connected vertex sets `L_x,L_y`, adjacent through
`xy`.  A common neighbour `w_i` in `B_i` makes both `L_x` and `L_y`
adjacent to `B_i`.  The five witnesses are distinct because the five
branch sets are disjoint.  Hence

\[
                  L_x,L_y,B_1,B_2,B_3,B_4,B_5
\]

are seven pairwise disjoint connected pairwise adjacent branch sets.  This
checks the literal `K_7` lift in Theorem 4.1.

In the five-colour branch every colour has a common-neighbour witness, but
if every named branch set contained some such witness then Theorem 4.1
would apply.  The `K_7`-minor exclusion therefore forces at least one named
branch set to contain none, exactly as Corollary 4.2 states.

## 4. Exact trust boundary

The audited result proves only the following conditional advances:

1. a simplicial vertex of the conditional defect-one two-tree lies in a
   labelled `K_7^-` model with one missing adjacency;
2. every internal edge of its represented component has the exact
   five-versus-six chromatic fork of Theorem 3.1; and
3. common-neighbour alignment with the five named branch sets gives an
   explicit `K_7` model.

It does **not** prove any of the following:

- that the conditional defect-one component selection is globally
  exhaustive;
- that a simplicial represented component has an internal edge (it may be
  a singleton);
- that colour classes or common-neighbour witnesses align with the five
  named branch sets;
- that a common-hole colouring is available in every six-colouring;
- that the surviving `K_6` model imposes a chromatic lower bound;
- that a failed repair yields a separator of order at most seven or
  compatible closed-shore colourings; or
- that an internal operation preserves the valid path cut and component
  labels or yields a strictly smaller valid configuration in the original
  host.

Within this trust boundary, the exact audited source revision is GREEN.
