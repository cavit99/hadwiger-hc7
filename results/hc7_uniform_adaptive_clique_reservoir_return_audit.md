# Independent audit: adaptive clique-reservoir carrier return

Audited file:
`results/hc7_uniform_adaptive_clique_reservoir_return.md`.

Audited SHA-256:
`7889a9d9ca826016674a4c11dc3cd4287dd5e86864949d66d3941b6fd94462cb`.

## Verdict

**GREEN.**  The uniform Theorem 1.1 is valid for every `k>=2` and
`1<=q<=k-1`.  The first proper minor returns a completely counted exact
boundary partition of packet demand at most `q`.  A maximum clique of
singleton blocks leaves exactly that many blocks to be represented by
distinct full packets.  The resulting second minor is proper and returns
the same exact partition.  The zero-demand case is correctly handled by
deleting the nonempty open packet shore.  Palette alignment is valid for
the full `(k-1)`-colour palette, including `(k,q)=(2,1)`.

Corollaries 1.2 and 2.1, and the support-only obstruction in Section 3,
remain GREEN.  No mathematical repair is required.

## 1. Parameters and the first proper minor

For every `i`, put

\[
                         A_i=C_i\cup I_i.
\]

Each `A_i` is connected because `C_i` is connected and every literal
member of `I_i` has a neighbour in it.  The sets are pairwise disjoint.
They are all nontrivial because both `C_i` and the nonempty `I_i` occur in
different parts of the separation.  Simultaneously contracting spanning
trees in the `A_i` therefore strictly lowers the vertex count and gives a
proper minor.

The images `a_1,...,a_q` form a clique through the pairwise literal carrier
adjacencies.  The hypothesis

\[
                         q\le k-1
\]

is exactly compatible with assigning them distinct colours from the
proper-minor palette.  Strong contraction-criticality supplies a
`(k-1)`-colouring of the minor.

Restricting that colouring to `R union S` and expanding `I_i` with the
colour of `a_i` is in the correct direction: every internal carrier vertex
lies in the discarded `L` side.  The expansion is proper edge by edge:

* each `I_i` is independent;
* distinct seed blocks get distinct image colours;
* every edge from `I_i` to `U` or `R` became incident with `a_i`; and
* `U` and `R` remain literal vertices of the minor.

Thus the first closed-shore colouring and its equality partition `Pi` are
legitimate.  Since `Pi` is induced by a `(k-1)`-colouring,

\[
                         |\Pi|\le k-1.                 \tag{A.1}
\]

This bound will make the clique of block representatives in the second
minor compatible with the same palette.

## 2. Exact block count and demand

Let `B_i` be the equality block containing `I_i`.  The `B_i` are pairwise
distinct because the images `a_i` form a clique.  Every boundary vertex
outside their seed sets belongs to the clique reservoir `U`.

An equality block is independent, so at most one vertex of `U` can join
each `B_i`.  If `u in U` joins none of them, its colour is different from
every image colour.  It cannot share a colour with another such reservoir
vertex because `U` is a clique.  Hence it is a singleton block.

There are no other boundary vertices.  Consequently, if

\[
                    r=\left|U-\bigcup_{i=1}^qB_i\right|,
\]

then the complete equality partition consists exactly of

\[
                         B_1,\ldots,B_q
\]

and those `r` singleton reservoir vertices.  Therefore

\[
                         |\Pi|=q+r.                    \tag{A.2}
\]

The displayed singleton vertices induce a clique, giving

\[
 \omega\bigl(G[S][\operatorname{sing}(\Pi)]\bigr)\ge r.
\]

This remains true at `r=0`.  A seed block `B_i` may itself be a singleton,
but such extra singleton blocks can only increase the maximum clique term.
Thus

\[
 d_{G[S]}(\Pi)
 =|\Pi|-\omega\bigl(G[S][\operatorname{sing}(\Pi)]\bigr)
 \le q.                                                \tag{A.3}
\]

No reservoir vertices can form an omitted nonsingleton block: two of them
are adjacent, and every non-reservoir boundary vertex already belongs to
one of the named seed blocks.

## 3. Maximum singleton clique and packet assignment

Choose a maximum clique `K` in the graph induced by the singleton-block
vertices of `Pi`.  Every member of `K` represents exactly one block of
`Pi`, and

\[
 |K|=\omega\bigl(G[S][\operatorname{sing}(\Pi)]\bigr).
\]

Hence the number of blocks of `Pi` not represented by `K` is exactly

\[
 |\Pi|-|K|=d_{G[S]}(\Pi)\le q.                        \tag{A.4}
\]

There are therefore enough pairwise disjoint full packets to assign a
different packet `P_B` to every such block `B`.

Assume first that at least one block lies outside `K`.  Every

\[
                         P_B\cup B
\]

is connected: the packet is connected and has a literal neighbour at
every member of the nonempty block `B`.  These sets are pairwise disjoint
and nontrivial, so contracting all of them gives a proper minor.

Their images, together with the retained singleton vertices in `K`, form a
clique with one representative for every block of `Pi`:

* `P_B` contacts every literal member of every other block `B'`, giving
  all image-image adjacencies;
* every packet contacts every retained singleton in `K`; and
* `K` is a literal clique by choice.

By (A.1), this clique has order at most `k-1`.  A `(k-1)`-colouring of the
proper minor assigns all block representatives distinct colours.

Restrict this colouring to `L union S`, retain the literal vertices of
`K`, and expand every contracted block `B` with its representative colour.
The result is proper:

* every `B` is independent because `Pi` came from a proper colouring;
* a `BL` edge became an image-`L` edge;
* distinct blocks have differently coloured clique representatives; and
* retained singleton incidences are represented by the same clique.

It induces exactly `Pi` on literal `S`.  Unused packet vertices and all
other vertices of `R` are discarded only when restricting to the opposite
closed shore; no packet is expanded back onto its own shore.

## 4. The zero-demand deletion branch

Suppose no block lies outside `K`.  Then

\[
 |\Pi|=|K|
   =\omega\bigl(G[S][\operatorname{sing}(\Pi)]\bigr).
\]

Since the singleton-block graph has at most one vertex for each block,
equality forces every block of `Pi` to be a singleton and every boundary
vertex to belong to `K`.  Thus `K=S`, `G[S]` is a clique, and `Pi` is the
discrete partition of `S`.

The open shore `R` is nonempty by hypothesis.  Deleting all of `R` gives a
proper minor on `L union S`, so it has a `(k-1)`-colouring.  Since `S` is a
clique, that colouring assigns all its vertices distinct colours and hence
induces exactly the discrete partition `Pi`.  The same assumption also
forces `|S|<=k-1`, consistently with the available palette.

This covers `d_{G[S]}(Pi)=0` without making an empty family of contractions
and without appealing to an exceptional exact-seven reflection lemma.

## 5. Palette alignment for general `k`

The first colouring of `G[R union S]` and the second colouring of
`G[L union S]` induce the same exact partition `Pi`.  Each side uses
pairwise distinct colours on its `|Pi|<=k-1` boundary blocks.  Mapping the
colour of every block on one side to the colour of the same block on the
other gives a bijection between two `|Pi|`-element subsets of the
`(k-1)`-colour palette.  It extends to a permutation of the entire palette.

After applying that permutation to one closed-shore colouring, the two
colourings agree vertexwise on `S`.  There is no `LR` edge, so they glue to
a proper `(k-1)`-colouring of `G`.

Nothing in the proof assumes `q>=2` or `k>=3`.  At `(k,q)=(2,1)`, the
palette has one colour.  The first proper-minor colouring forces `|Pi|=1`;
the direct packet contraction or the zero-demand deletion branch returns
the same one block, and the unique palette permutation aligns it.

The direct uniform proof therefore supports the stronger conclusion
`chi(G)<=k-1`; no literal-minor exceptional outcome is needed.

## 6. Exact-seven corollaries

At `(k,q)=(7,2)`, Theorem 1.1 specializes directly to Corollary 1.2.
For any allocation `T_D subseteq T` in Corollary 2.1, the sets

\[
 X=D\cup T_D,
 \qquad
 Y=E\cup(T-T_D)
\]

are disjoint.  They are connected because each lobe meets every gate
vertex assigned to it.  They are adjacent as well: if one set receives all
of `T`, the other lobe has an edge to that gate side; if the allocation is
split, a lobe has an edge to a gate vertex assigned to the other set.

A bipartition `I dotunion J` of `G[S]-U` covers `S-U` and makes both sets
independent.  The nonemptiness and contact inclusions in (2.2), together
with the clique property of `U`, are precisely the remaining hypotheses of
the uniform theorem.  Interchanging the two classes only interchanges the
carrier names.  Corollary 2.1 is therefore valid.

Its explanation is also accurate: the returned partition need not be the
prescribed `I|J|U`.  Reservoir vertices may be absorbed into the seed
blocks, but the exact partition still has demand at most two.

## 7. Support-only obstruction

The boundary graph in (3.2) is a tree.  The three pairs in (3.3) are
independent; `z` has a neighbour in every pair (`a_2,b_1,b_3`); and every
two paired blocks have a literal joining edge (`b_1b_2`, `a_1a_3`, and
`a_2a_3`).  It is therefore a valid paired width-two boundary at the stated
support-only level.

Since `A cap C={z}`, every `a_i` outside `U` is forced into the
`A`-carrier block and every `b_i` outside `U` is forced into the
`C`-carrier block.  If `a_3 notin U`, then `a_3` lies in the former block.
The edges `a_3a_1,a_3a_2` force both `a_1,a_2` into `U`, but they are
nonadjacent.  Thus `a_3 in U`.  The edge `b_1b_2` then forces at least one
of `b_1,b_2` into `U`, and neither is adjacent to `a_3`.  This is again
impossible for a clique `U`.

The two independent blocks are unordered, so reversing the carrier
assignment is already covered by renaming them.  The example is correctly
claimed only as a boundary/support certificate; it does not assert an
internal lobe realization, seven-connectivity, minor-criticality, or an
`HC_7` counterexample.
