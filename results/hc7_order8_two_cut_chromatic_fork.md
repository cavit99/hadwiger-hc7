# Chromatic localization at the order-eight two-cut residue

**Status:** written proof; separate internal audit GREEN in
[`hc7_order8_two_cut_chromatic_fork_audit.md`](hc7_order8_two_cut_chromatic_fork_audit.md).
This theorem does not prove `HC_7`.

## 1. Setting

Assume the hypotheses and notation of the written
[two-cut response-orientation theorem](../results/hc7_order8_two_cut_response_orientation.md).
Thus `S` has order eight, the components of `G-S` are the three
`S`-full connected graphs `C,Q_0,Q_1`, and

\[
 C=L_d\mathbin{\dot\cup}L_e\mathbin{\dot\cup}\{x,y\}.
\tag{1.1}
\]

The sets `L_d,L_e` are the components of `G[C]-{x,y}`.  They miss
exactly `d,e` from `S`, respectively, while `x,y` are adjacent to neither
`d` nor `e`.  Moreover,

\[
 S-\{d,e\}=P\mathbin{\dot\cup}R
\tag{1.2}
\]

is a bipartition, `de` is absent, and the closed `C`-side admits the
boundary partition

\[
 \Pi_{\ne}=P\mid R\mid\{d\}\mid\{e\}
\tag{1.3}
\]

but not

\[
 \Pi_=P\mid R\mid\{d,e\}.
\tag{1.4}
\]

Each closed component-side `G[Q_i union S]` admits (1.4).

## 2. The chromatic fork

### Theorem 2.1

At least one of the following alternatives holds.

1. One of `G[L_d]`, `G[L_e]` is not three-colourable.  Consequently that
   open lobe contains an induced four-critical subgraph.
2. The edge `xy` is present and `G-xy` has a proper six-colouring `phi`
   with all of the following properties:

   a. `phi` induces `Pi_=` on `S`;
   b. for some colour `alpha`,

      \[
      \phi(x)=\phi(y)=\phi(d)=\phi(e)=\alpha;
      \tag{2.1}
      \]

   c. all vertices of `L_d union L_e` use three colours disjoint from the
      three colours on the blocks of `Pi_=`;
   d. for every colour `beta != alpha`, the vertices `x,y` belong to one
      `alpha`--`beta` component of `G-xy`;
   e. paths for distinct choices of `beta` can be chosen edge-disjoint,
      and two such paths can meet only at vertices coloured `alpha`; and
   f. for either of the two boundary-block colours, every corresponding
      `x`--`y` path meets `S` internally.  For each of the three colours
      used on `L_d union L_e`, every corresponding path either meets
      `S` internally, first at `d` or `e`, or is a two-edge path through
      one common neighbour of `x,y` in a single lobe.

Thus the two-cut residue cannot remain merely an ordinary pair of
three-colourable lobes.  It contains either a literal four-critical core
inside one open lobe or one globally aligned, operation-specific five-path
response at the cut edge.

### Proof

Suppose first that both open lobes are three-colourable.

If `xy` is absent, colour `G[L_d]` and `G[L_e]` independently with three
new colours, give `x,y,d,e` a fourth colour, and give `P,R` two further
colours.  The colouring is proper: `x,y` have no edge between them and no
edge to `d,e`; the lobe colours are disjoint from all three boundary
colours; and (1.2) is a bipartition.  Its restriction to the closed
`C`-side induces (1.4), contrary to the response orientation.  Hence

\[
                         xy\in E(G).
\tag{2.2}
\]

Choose arbitrary proper three-colourings of the two open lobes, using the
same three colour names on both.  Delete `xy`, give all four vertices
`x,y,d,e` a new colour `alpha`, and give the two independent sets `P,R`
two further colours.  This is a proper six-colouring of
`G[C union S]-xy` inducing (1.4).  Assertion 1 of the response-orientation
theorem supplies a colouring of each `G[Q_i union S]` inducing the same
partition.  Permute colour names so that all three colourings agree on
the three literal blocks of (1.4), and glue them.  The components of
`G-S` are pairwise anticomplete, so the result is a proper six-colouring
`phi` of `G-xy`.  It has properties a--c.

Fix a colour `beta != alpha`.  If `x,y` belonged to different components
of the subgraph of `G-xy` induced by `alpha,beta`, interchange those two
colours on the component containing `x`.  This would give `x,y` different
colours, after which the edge `xy` could be restored.  The result would be
a proper six-colouring of `G`, a contradiction.  Hence `x,y` lie in one
such component, proving d.

For every `beta`, choose a simple `alpha`--`beta` path between `x,y`.
For distinct colours `beta,gamma`, the two paths can intersect only at
vertices whose colour belongs to

\[
 \{\alpha,\beta\}\cap\{\alpha,\gamma\}=\{\alpha\}.
\tag{2.3}
\]

They cannot share an edge, because adjacent vertices have different
colours.  This proves e.

Let `beta` be one of the two colours on `P,R`.  No vertex of
`L_d union L_e` has colour `alpha` or `beta`.  An `x`--`y` path whose
internal vertices avoided `S` would be contained in `C`: leaving `C`
for either `Q_i` requires passing through `S`.  After deleting its ends,
such a path lies in one component of `G[C]-{x,y}`, but that component has
no vertex of either required colour.  This is impossible.  Hence the path
meets `S` internally.

Now let `beta` be one of the three lobe colours.  If the path avoids `S`
internally, it is again contained in one lobe after deleting its ends.
No lobe vertex has colour `alpha`.  An alternating path from the
`alpha`-coloured vertex `x` to the `alpha`-coloured vertex `y` can then
have only one internal vertex.  It is therefore a two-edge path through a
common `beta`-coloured neighbour of `x,y`.  Otherwise the path meets `S`.
The only `alpha`-coloured boundary vertices are `d,e`, and no boundary
vertex has one of the three lobe colours.  Its first boundary vertex is
therefore `d` or `e`.  This proves f and alternative 2.

We have shown that, if alternative 1 fails, alternative 2 holds.  If
alternative 1 holds, a vertex-minimal induced non-three-colourable subgraph
of the corresponding lobe is four-critical: deleting any vertex makes it
three-colourable, and its chromatic number is exactly four because a
minimal non-three-colourable graph is four-colourable after colouring a
deleted-vertex graph with three colours and assigning the deleted vertex
a fourth.  This completes the proof. \(\square\)

## 3. A stronger closed-side observation

### Lemma 3.1

At least one of

\[
 G[L_d\cup\{x,y\}],\qquad G[L_e\cup\{x,y\}]
\tag{3.1}
\]

is not three-colourable.

Moreover, if the first graph is three-colourable, then deleting either
`x` or `y` from the second graph leaves a non-three-colourable graph; the
same statement holds with the lobes interchanged.

### Proof

Suppose first that both graphs in (3.1) are three-colourable.  Choose one
three-colouring of each.  If the two restrictions to `{x,y}` have the same
equality relation, permute the three colour names so that they agree on
both vertices and glue them to a three-colouring of `G[C]`.  Using three
new colours on `C` and the three colours of (1.4) on `S` gives the forbidden
closed-side equality response.

If the two equality relations differ, normalize the colour of `x` in both
colourings and recolour only `y` in each graph with the colour assigned to
the block `{d,e}`.  That colour was not used in either three-colouring, so
the recolouring is proper; and `y` is adjacent to neither `d` nor `e`.
The two colourings now agree on `x,y` and glue.  All other vertices of `C`
use the three colours disjoint from the boundary palette, so this again
gives (1.4), a contradiction.  This proves the first assertion.

Suppose, say, `G[L_d union {x,y}]` is three-colourable and
`G[L_e union {x,y}]-y` is also three-colourable.  Normalize the two
colourings to agree at `x`, assign the boundary colour of `{d,e}` only to
`y`, and otherwise use three colours absent from `S`.  Recolouring or
adding `y` with this fresh colour is proper on both sides, even when `xy`
is an edge.  The colourings glue and once more extend (1.4), a
contradiction.  Interchanging `x,y` and the two lobes proves all remaining
claims. \(\square\)

## 4. Exact gain and remaining host-level gap

The theorem is unbounded: the two lobes may have arbitrary order.  It
turns the coarse inequality `chi(G[C])>=4` into two literal alternatives.
The first contains an ordinary four-critical graph wholly inside one open
lobe.  The second is a selected edge-deletion response whose five Kempe
paths have controlled first boundary hits; it is not merely a colouring of
a further contracted minor.

Neither alternative is terminal under the present inputs.  In the
four-critical alternative, `HC_4` gives an unrooted `K_4` model but does
not make its four branch sets meet prescribed boundary portals or bound
the full neighbourhood of the critical subgraph by eight.  In the
five-path alternative, paths of different colour pairs can share
`alpha`-coloured vertices, and a two-edge path can use a common neighbour
inside one lobe.  Thus the paths are not yet two vertex-disjoint connected
subgraphs with the required boundary-block contacts.

Consequently the exact remaining statement in this branch is a
label-preserving allocation theorem for one of these two alternatives:
either root the four-critical lobe model at the required literal contacts,
or turn the first-hit five-path family into the reserved path and
portal-spanning connected subgraph of the audited three-block linkage
reflection theorem.  Failure must expose an actual order-seven separator
carrying the equality partition; ordinary criticality alone supplies no
such upper bound.

## 5. Dependencies

- the two-cut response-orientation theorem;
- proper-minor six-colourability and non-six-colourability of `G`; and
- elementary Kempe interchange at the deleted edge `xy`.
