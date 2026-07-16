# Independent audit: regeneration after deleting a nonadjacent pair

**Verdict:** **GREEN.**  The five conclusions of Theorem 1.1, the final
four-clique refinement, and the stated application to the order-five
common-core branch are correct.  The result regenerates unlabelled minor
models and two separately attained colourings; it does not align either
object with the branch sets of a preselected model.

**Audited source:**
[`hc7_nonadjacent_pair_colouring_regeneration.md`](hc7_nonadjacent_pair_colouring_regeneration.md).

**Source SHA-256:**
`573541210c72abf297a1699cc022d08b02447013f543394671426c90dd020809`.

**External source checked:** António Girão, Freddie Illingworth, Bojan
Mohar, Sergey Norin, Raphael Steiner, Youri Tamitegama, Jane Tan, David R.
Wood and Jung Hon Yip, *The Dominating 4-Colour Theorem*, Theorem 1.1,
arXiv:2605.10112 (2026), <https://arxiv.org/abs/2605.10112>.

## 1. Exact chromatic number after deleting the pair

Let `P={p,q}` be nonadjacent and put `H=G-P`.  Vertex deletion is a minor
operation, so the proper-minor hypothesis gives `chi(H)<=6`.  If `H` had
a colouring with at most five colours, assigning the same fresh sixth
colour to `p` and `q` would be proper: the roots are nonadjacent, and every
edge from a root into `H` has differently coloured ends.  This contradicts
`chi(G)=7`.  Hence `chi(H)=6`.

No `K_7`-minor exclusion or connectivity hypothesis is hidden in this
step.

## 2. Palette domination and separate attainability

Fix any six-colouring of `H`.  If `p` misses a colour on its neighbourhood
and `q` also misses a colour, assign each root one colour it misses.  The
chosen colours may coincide because `pq` is absent.  This extends the
colouring to `G`, a contradiction.  Thus at least one root has a neighbour
in every one of the six colour classes.  This proves item 2 for **every**
six-colouring of `H`, not merely for a selected colouring.

The two orientations in item 3 are also valid, but generally occur in
different colourings.  A six-colouring of the proper minor `G-p` must use
every colour on `N_G(p)`: if one colour were absent there, assigning it to
`p` would six-colour `G`.  Since `pq` is not an edge, deleting `q` removes
no neighbour of `p`, so restricting this colouring to `H` preserves all
six witnessed colours.  This is `c_p`.  The argument with `p,q`
interchanged gives `c_q`.

This reasoning remains valid if a “six-colouring” is initially understood
as a map into a six-colour palette rather than a surjective map.  A globally
unused colour would in particular be absent from the relevant
neighbourhood and would yield the same forbidden extension.

## 3. Regenerated minor models

For any `v in V(H)`, a four-colouring of `H-v` would extend to a
six-colouring of `G`: give `v` a fresh fifth colour and give both
nonadjacent roots the fresh sixth colour.  All restored edges are proper.
Therefore `chi(H-v)>=5`.

The cited Dominating 4-Colour Theorem defines a dominating `K_t` model as
an ordered sequence of disjoint connected subgraphs in which every vertex
of each later member has a neighbour in every earlier member.  Its Theorem
1.1 states that every graph without a dominating `K_5` model is
four-colourable.  The contrapositive applies to every `H-v`, giving the
claimed dominating `K_5` model.  This exact external statement was checked
against the primary preprint and agrees with the already audited use in
[`../results/hc7_common_deletion_dominating_five_substrate.md`](../results/hc7_common_deletion_dominating_five_substrate.md).

Since `chi(H)=6`, the proved `t=6` case of Hadwiger's Conjecture gives a
`K_6` minor in `H`.  This is the exact contrapositive of the established
statement that every `K_6`-minor-free graph is five-colourable.

## 4. Four-clique refinement

In either selected colouring, the four vertices of the clique `X` have
four distinct colours.  In `c_p`, the root `p` has a neighbour of every
colour and is adjacent to all of `X`.  The two colours absent from `X`
must therefore occur on neighbours of `p` outside `X`.  They are distinct
because they are two different colour classes.  The same argument proves
the assertion for `q` in `c_q`.

The theorem does not assert that the two outside neighbours are adjacent,
that they belong to prescribed branch sets, or that `c_p` and `c_q` agree
away from the roots.

## 5. Audit of the live application

The application imports three already audited facts rather than deriving
them from Theorem 1.1 alone.

1. In the order-five common-core outcome, the two five-vertex model
   supports `X union {p}` and `X union {q}` are literal `K_5` subgraphs.
   Hence `X` is a four-clique and both roots are complete to it.
2. Corollary 2.1 of
   [`../results/hc7_rigid_cross_arm_double_root_cover.md`](../results/hc7_rigid_cross_arm_double_root_cover.md)
   proves `pq` is absent in this literal-arm case; otherwise these six
   vertices form a `K_6` that seven-connectivity lifts to a `K_7` minor.
3. The globally maximal private-pair theorem chooses the avoided support
   with order exactly six and disjoint from `P`.  In the named
   zero-intersection subcase it is also disjoint from the common core `X`
   by definition of that subcase.

These facts put the live configuration within Theorem 1.1.  The three
listed consequences in Section 2 of the source then follow literally.

## 6. Exact trust boundary

The theorem proves:

- exact six-chromaticity of the common deletion `G-P`;
- palette domination by at least one root in every six-colouring;
- separate attainability of both root orientations;
- a dominating `K_5` model avoiding any one chosen vertex; and
- an unlabelled `K_6` minor.

It does not preserve a selected six-vertex `K_5` model, make the two
colourings compatible, locate regenerated branch sets relative to `X`, or
compose the disjoint supports into a `K_7` minor.  The source states these
limitations accurately.
