# Exterior-component bounds at low-degree vertices

**Status:** written proof; two computer-assisted finite classifications;
separately audited GREEN.  This theorem does not prove `HC_7`.

## Theorem 1 (sharp current component bounds)

Let `G` be a finite simple graph such that:

1. `G` is seven-connected and `chi(G)=7`;
2. `G` has no `K_7` minor; and
3. every proper minor of `G` is six-colourable.

For a vertex `u`, let `m(u)` be the number of components of `G-N[u]`.
Then

\[
 d_G(u)=8\quad\Longrightarrow\quad m(u)\le2,
 \qquad
 d_G(u)=9\quad\Longrightarrow\quad m(u)\le3.          \tag{1.1}
\]

Together with the separately audited
[degree-seven connectivity theorem](../results/hc7_degree7_anti_neighbourhood_connectivity.md),
the possible numbers of exterior components at a degree-seven,
degree-eight, or degree-nine vertex are therefore at most one, two, and
three.

The finite proof appendices and retained verifiers keep their historical
filenames in `archive/` to preserve provenance.  They are incorporated
below only through their exact statements and the renewed adjacent audit.

## 1. Attachment and independence bounds

Put `X=N_G(u)` and let `D_1,...,D_m` be the components of `G-N[u]`.  Every
neighbour of `D_i` outside `D_i` belongs to `X`, and `N_G(D_i)` separates
`D_i` from `u`.  Seven-connectivity gives

\[
                         |N_G(D_i)|\ge7.                \tag{1.2}
\]

Thus a component misses at most one vertex of `X` in degree eight and at
most two in degree nine.  Proper-minor criticality also gives

\[
                         \alpha(G[X])\le d_G(u)-5.      \tag{1.3}
\]

Indeed, contract the star on `u` and a maximum independent set `I` of
`G[X]`.  In a six-colouring of the proper minor, the lifted colour on `I`
is absent from `X-I`.  If `|X-I|<=4`, at most five colours occur on `X`
and a sixth colour can be assigned to `u`, a contradiction.

## 2. Initial packing bounds

The analytic packing arguments are written in the retained
[degree-eight/nine appendix](../archive/hadwiger_degree8_degree9_exterior_bounds.md).
Their conclusions are

\[
 d_G(u)=8\Longrightarrow m(u)\le3,
 \qquad
 d_G(u)=9\Longrightarrow m(u)\le4.                    \tag{2.1}
\]

For degree eight, four components each miss at most one boundary vertex.
The appendix selects two adjacent boundary vertices missed by none of the
four components and four distinct representatives, one for each component,
with no reciprocal miss.  The two singleton representatives and the four
component-plus-representative sets form an `X`-meeting `K_6` model in
`G-u`; adding `{u}` gives a `K_7` model.

For degree nine, the two-vertex miss sets of five components are the edges
of a loopless multigraph on `X`.  The appendix proves by induction an
incidence-free representative theorem: for `r>=3` labelled two-sets on an
`(r+2)`-element set, there are distinct representatives outside their own
two-sets with no reciprocal incidence.  If the five miss sets have a common
unused vertex, this gives five component bags plus that singleton.  In the
only no-unused-vertex incidence form, `P_3 dotunion 3K_2`, the independence
bound (1.3) supplies one boundary edge and the same construction is repaired
explicitly.  Again an `X`-meeting `K_6` model joins `{u}` to give `K_7`.

Consequently it remains only to exclude exactly three components in degree
eight and exactly four in degree nine.

## 3. Certified boundary dichotomies

Contract every exterior component to one vertex, retain the boundary graph
`H=G[X]`, and delete any extra component-boundary edges beyond seven
contacts.  Each contracted component is nonadjacent to `u` and to every
other contracted component.

The retained degree-eight classification is stated and proved in the
[three-component appendix](../archive/hadwiger_degree8_three_component_closure.md).
Up to boundary and component permutations, the three one-vertex misses
have exactly three equality patterns.  For every eight-vertex graph `H`
with `alpha(H)<=3`, and every one of those patterns, at least one of the
following exists:

1. an `X`-meeting `K_6` model in the contracted quotient;
2. a partition of `X` into three nonempty independent blocks; or
3. a partition of `X` into three nonempty independent blocks and one
   singleton block,

where in outcomes 2 and 3 the following usability condition holds.  For
each component retained in the original graph, the other two components
can be assigned to two of the independent blocks so that their unions are
connected and, together with the star formed from `u` and the remaining
block, their contracted images are a clique; in outcome 3 the singleton
is adjacent to every image as well.

The retained degree-nine classification is stated and proved in the
[four-component appendix](../archive/hadwiger_degree9_four_component_closure.md).
The four two-vertex misses form one of exactly 23 loopless multigraph types.
For every nine-vertex `H` with `alpha(H)<=4`, the quotient has either an
`X`-meeting `K_6` model or a usable partition into four nonempty independent
blocks, optionally with a fifth singleton block.  For every retained
component, the other three components can be assigned to three blocks so
that their unions are connected and, together with the `u`-star block,
their contracted images form a clique; the optional singleton is adjacent
to every image.

The certificate verifiers reconstruct the independence clauses, every
usable block partition and assignment, and every listed quotient-model
template.  They impose the negation of every usable partition and every
listed model template; the resulting residual formula is unsatisfiable.
The degree-eight verifier checks three certificates with
141, 183, and 98 model templates.  The degree-nine verifier checks all 23
miss-multigraph types and 423 model templates in total.  The discovery
programs are not imported by either verifier.

## 4. Lifting and colour gluing

An `X`-meeting quotient `K_6` model lifts by replacing each contracted
component vertex with its original connected component.  Every lifted bag
still meets `X`, so `{u}` is adjacent to all six and completes an explicit
`K_7` model.

Suppose instead that a usable independent-block partition is returned.
Fix one retained component `D_i`.  Contract the connected star consisting
of `u` and its assigned independent block.  Contract each other exterior
component together with its assigned independent block.  The usability
conditions say exactly that the resulting three or four images form a
clique; when the optional singleton is present, it extends that clique by
one vertex.  This is a proper minor and has a six-colouring.

Delete the contracted exterior components other than `D_i`, delete `u`,
and expand each independent boundary block with the colour of its contracted
image.  This gives a proper colouring of `G[D_i union X]`: block
independence preserves internal edges, and every edge from a retained
vertex to an expanded block was represented at the contracted image.
The three or four degree-eight blocks, or the four or five degree-nine
blocks, receive distinct colours.

Repeat for every retained component and permute the six colours so that the
block colours agree on `X`.  Exterior components are pairwise anticomplete,
so these colourings glue over all of `G-u`.  At most four colours occur on
`X` in degree eight and at most five in degree nine.  Assign an absent sixth
colour to `u`, contradicting `chi(G)=7`.

The certified quotient alternative and the block-partition alternatives
are therefore all impossible.  This excludes exactly three components in
degree eight and exactly four in degree nine.  Combining with (2.1) proves
(1.1).  \(\square\)

## 5. Exact gain and limitation

This is an unbounded host-level theorem with a finite boundary
classification.  It leaves one or two exterior components in degree eight
and one, two, or three in degree nine.  It does not synchronize the
remaining component colouring languages, make a `K_6`-minor-free boundary
augmentation terminal, or address the connected-exterior tight pole
residue.
