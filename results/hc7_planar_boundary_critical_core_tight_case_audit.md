# Independent audit: tight vertices in the planar boundary-critical core

**Audited file:** `results/hc7_planar_boundary_critical_core_tight_case.md`
**SHA-256:** `a35476782ad79bf513a756f05bdae972bbee4b18022a49a6d2721352cf960df1`
**Verdict:** **GREEN.** The general tight-vertex Gallai-forest theorem, the
exact planar slack calculation, the exclusion of the zero-slack four-clique,
and the three residual alternatives are correct as stated. No mathematical
change to the audited source is required.

This is an independent internal mathematical audit, not external peer
review. The balanced-order-eight deductions are conditional on the exact
hypotheses and promoted inputs cited by the theorem.

## Promotion recheck

The promoted source differs from the audited draft only in its status,
adjacent-audit link, and the relative link to the active balanced
order-eight frontier. Reversing those navigation and metadata edits
reproduces the original audited SHA-256
`e8e78e223af97a2f0969aea2d33aca2caebea70f2fc2da1cdb0b3f051a4747f3`.
No theorem hypothesis, conclusion, proof step, or dependency changed, so
the GREEN verdict transfers to the promoted hash above.

## 1. Tight-vertex Gallai forest

Let `B` be a block of `K[T]` which is neither complete nor an odd cycle.
The proof correctly colours the proper induced subgraph `K-V(B)` by
vertex-minimality. For every `w in V(B)`, deleting colours used by its
already coloured outside neighbours removes at most
`d_K(w)-d_B(w)` colours. Tightness gives

\[
 |L_B(w)|\ge |L(w)|-(d_K(w)-d_B(w))=d_B(w).
\]

A block contains every graph edge whose ends both belong to its vertex set,
so `d_B` is the degree relevant to colouring the induced block. Since this
connected block is not a clique or an odd cycle, the
Borodin--Erdos--Rubin--Taylor degree-choosability characterization supplies
an `L_B`-colouring. It combines with the outside colouring because every
outside-neighbour colour was removed from the corresponding list. This
contradicts non-`L`-colourability of `K` and proves Theorem 2.1.

The argument is correctly confined to `K[T]`; it makes no unsupported
Gallai-tree claim about vertices with positive list-degree excess.

## 2. Exact planar slack and equality

From

\[
 \varepsilon(w)=d_K(w)-|L(w)|,
 \qquad c(w)=6-|L(w)|,
\]

summing degrees gives the exact identity

\[
 \sum_w c(w)=6|K|-2|E(K)|+\sum_w\varepsilon(w).
\]

For a simple planar graph of order at least three,
`|E(K)|<=3|K|-6`; every excess is a nonnegative integer and every vertex of
the excess set contributes at least one. Thus both inequalities in (2.2)
are valid.

If the incidence sum is twelve, all excesses vanish and
`|E(K)|=3|K|-6`. For order at least four this is a maximal planar graph and
hence one block; the order-three exception is `K_3`. The tight-vertex
theorem then permits only a planar complete graph or an odd cycle. Comparing
edge counts leaves exactly `K_3,K_4`.

For `K_t`, list-colourability is an SDR problem. Each remaining list has
order `t-1`. A Hall obstruction cannot use fewer than all `t` vertices,
because the union of any nonempty subfamily already has order at least
`t-1`. Hence the union of all lists has order exactly `t-1`, and every list
is that same set. The final equality conclusion is therefore correct.

## 3. Host lemmas

If a seven-connected graph contains a six-clique `J`, then `G-J` is
nonempty. It is connected, since otherwise the neighbourhood of one of its
components is a cut contained in the six-set `J`. Minimum degree at least
seven gives every vertex of `J` a neighbour outside `J`. Thus `G-J` and the
six singleton clique vertices form seven pairwise adjacent connected branch
sets. Lemma 3.1 is valid.

For Lemma 3.2, if (for example) `x ell_f` is an edge, connectedness of
`A=C-{ell_e,ell_f}`, its contact with `V(e)`, and its neighbour at
`ell_e` give a connected subgraph containing `ell_e` and contacting
`V(e)`. This is disjoint from `{ell_f}`, which contacts `x`. These are
exactly the two open-side subgraphs required by the promoted split-edge
completion. The symmetric argument is identical. Hence both displayed
leaf--`x` edges are correctly excluded.

## 4. The zero-slack four-clique

For a zero-slack `K_4` core on
`{ell_e,ell_f,p,q}`, the common three-element list is the complement of
the three colours on `R`: the leaves are adjacent to all of `R`, and their
lists have order three. Therefore each of `p,q` sees on the boundary
exactly the three colours occurring on `R`.

Neither `p` nor `q` can be adjacent to all of `R`, since that vertex, the
two leaves, and `R` would induce a six-clique. Whenever such a vertex misses
a member of `R`, it must see that member's distinct colour at a boundary
neighbour in one of the three literal groups

\[
                         V(e),\quad V(f),\quad\{x\}.
\]

### Group-concentration check

Suppose `p,q` have contacts in two different groups. Because both are
adjacent to both leaves inside the core, the two contacts produce
vertex-disjoint connected subgraphs with the following labelled ends:

- `V(e),V(f)`: `ell_e` to `V(e)` and `ell_f` to `V(f)`;
- `V(e),{x}`: `ell_e` to `V(e)` and `ell_f` to `x`;
- `V(f),{x}`: `ell_f` to `V(f)` and `ell_e` to `x`.

In the first case, after contracting the two boundary edges these are the
missing same-index linkage in the promoted canonical four-root graph. Its
other two pair-linkages and the rooted-`K_4` characterization give four
rooted branch sets; expanding the contractions and adjoining the three
singletons of `R` gives the stated `K_7` model. The second case exactly
matches the promoted split-edge completion, and the third matches its
label-swapped form.

This also handles the possibility that one of `p,q` contacts several
groups: choose one of its contacts in a group different from a contact of
the other vertex. Consequently the union of the group-contact sets of
`p,q` must be one singleton group in the `K_7`-minor-free branch. The
group-concentration conclusion is valid.

The union of the sets of vertices of `R` missed by `p,q` has order at
least two. Otherwise two vertices of `R`, together with the four-clique
core, induce a six-clique. The common contact group cannot be `{x}`: the
two missed vertices have distinct colours, while the one literal vertex
`x` supplies only one colour. Hence the common group is `V(e)` or `V(f)`.

Assume it is `V(e)`. Both `p,q` contact `V(e)` and neither contacts `x`.
In connected `A`, choose a shortest path from `{p,q}` to a vertex adjacent
to `x`. Its first vertex is one of `p,q`, its last is not, and it avoids
the other member of `{p,q}`; otherwise the suffix beginning at that other
member is shorter. Adjoining `ell_f` gives the `ell_f`--`x` connected
subgraph. The other core vertex with `ell_e` gives a disjoint
`ell_e`--`V(e)` connected subgraph. The split-edge completion applies.
The `V(f)` case is symmetric. This proves Theorem 4.1 with all labels
preserved.

## 5. Residual edge and triangle cases

If the critical core is only `ell_e ell_f`, minimal non-list-colourability
forces both lists to be the same singleton, namely the common endpoint
colour in the displayed edge-deleted colouring. Each leaf therefore sees
all five other boundary colours. Lemma 3.2 removes `x`, while the leaf is
anticomplete to its same-index defect edge. The two colours absent from the
original five-clique must consequently occur on the two endpoints of the
opposite defect edge, both adjacent to that leaf. Since those endpoints are
adjacent and properly coloured, they indeed carry the two distinct missing
colours. Outcome 1 is correct.

For a zero-slack triangle, Corollary 2.2 gives one common two-element list.
The edge-deleted colouring puts the common leaf colour and the colour of the
third vertex `w` in that list. The latter is one of the two colours absent
from the original five-clique. Thus the common list and the fourth excluded
boundary colour are exactly as stated in (5.1). Anticompleteness to the
same-index defect edge and Lemma 3.2 force the other absent colour to occur
at the two asserted cross-index contacts.

### Corrected facial-triangle lift

The promoted boundary-criticality theorem places the entire leaf-side
component in the planar skeleton of the canonical web. Hence `w` is a
skeleton vertex and `ell_e ell_f w` is a skeleton triangle containing the
outer edge `ell_e ell_f`.

If deleting this triangle separated the web completion, then deleting

\[
                  R\mathbin{\dot\cup}\{\ell_e,\ell_f,w\}
\]

would separate `G`. This lift is sound: a path in the expanded host avoiding
that six-set would project, after deleting `R` and contracting `e,f`, to a
walk in the quotient avoiding the triangle. Expanding the two undeleted
defect vertices therefore cannot reconnect two quotient components. The
resulting separator has order six, contradicting seven-connectivity.

Thus the triangle is nonseparating. In the embedded web skeleton, the outer
edge `ell_e ell_f` is incident with one bounded face, every bounded face is
a triangle, and a nonfacial triangle through that outer edge would separate
vertices on its two sides. Therefore `w` is precisely the third vertex of
the unique bounded facial triangle incident with `ell_e ell_f`. The final
localization statement is correct and does not treat a completion edge as
a host edge.

## 6. Trust boundary

The audit verifies the tight-vertex structure and eliminates only the
zero-slack four-clique under the full balanced-order-eight hypotheses. It
does not eliminate the two-vertex core, the facial-triangle core, the
positive-slack case, the balanced order-eight configuration, `HC_7`, or
Hadwiger's Conjecture.
