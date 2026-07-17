# A colour-matched path gives a `K_7` model or an actual separation

**Status:** written proof; separate internal audit GREEN.  This theorem
compresses every branch-set-preservation failure for one fixed repair path
to a genuine vertex separation.  It does not bound the separator above
and does not prove `HC_7`.

## 1. Setup

Assume the complete setup of the audited colour-matched path theorem and
the unique-deficiency case.  Thus

\[
                 C,\ \{u\},\ \{z\},\ X,\ D_1,D_2,D_3               \tag{1.1}
\]

form a `K_7`-minus-one-edge model, whose only missing adjacency is
`C`--`{u}`.  Let `P` be any colour-matched `C`--`T` path supplied by that
theorem, and put

\[
 Y=\{u\}\cup(V(P)-C),
 \qquad
 \mathcal K=\{X,D_1,D_2,D_3\},
 \qquad
 I_K=V(P)\cap K.                                      \tag{1.2}
\]

The set `Y` is connected, disjoint from `C`, and adjacent to `C`.  Every
`I_K` is independent.  The graph `G` is seven-connected,
seven-chromatic, and `K_7`-minor-free, and every proper minor is
six-colourable.

## 2. Exchange-or-separator theorem

### Theorem 2.1

For every path `P` in the setup above, at least one of the following
holds.

1. `G` contains a `K_7` minor.
2. There is a nonempty connected set `L` such that `N_G(L)` is the
   boundary of an actual separation with nonempty open sides.  Moreover,
   either
   - `L` is a component of `G[K-I_K]` for some `K in mathcal K`; or
   - `L={v}=K` for a singleton protected branch set consumed by `P`.

Every separator returned in item 2 has order at least seven.  If `G` has
no separation of order seven, each has order at least eight.

#### Proof

Suppose first that `K-I_K` is nonempty for every `K in mathcal K`.  For
each `K`, consider the components of `G[K-I_K]`.

If, for some `K`, no component is adjacent to both `C` and `z`, choose a
component `L` which misses one of these two anchors.  The missed anchor is
disjoint from `L union N_G(L)`.  Hence

\[
       (L\cup N_G(L),\ V(G)-L)
\]

is an actual separation with `L` on one open side and the missed anchor
on the other.

We may therefore assume that, for every `K`, some component `L_K` of
`G[K-I_K]` is adjacent to both `C` and `z`.  Choose one such component for
each `K`.  If the four selected components are pairwise adjacent, the
audited component-exchange criterion gives an explicit `K_7`-minor model.

Otherwise, two selected components `L_K,L_{K'}` are nonadjacent.  The
second component is disjoint from `L_K union N_G(L_K)`, so

\[
       (L_K\cup N_G(L_K),\ V(G)-L_K)
\]

is an actual separation with `L_K` and `L_{K'}` in its two open sides.
This proves the theorem when every protected branch set has a residual
vertex.

It remains to consider `K-I_K=emptyset`.  Since `I_K` is independent and
`G[K]` is connected, `K` consists of one vertex `v`.  This cannot occur
for `K=X`: both colour classes forming the connected bipartite graph `X`
are nonempty, while `P cap X` lies wholly in only one of them.  Thus
`K=D_i={v}` for some `i`.

The vertex `v` is not universal in `G`.  Indeed, if it were universal,
then `G-v` would be six-chromatic: it is six-colourable as a proper minor,
and a five-colouring would extend to a six-colouring of `G`.  The proved
case `HC_6` would give a `K_6` minor in `G-v`, and the universal singleton
`{v}` would extend it to a `K_7` minor in `G`, a contradiction.  Choose a
non-neighbour `w` of `v`.  Then

\[
       (\{v\}\cup N_G(v),\ V(G)-\{v\})
\]

is an actual separation with open sides containing `v` and `w`.

Finally, seven-connectivity makes every displayed separator have order at
least seven.  Excluding order seven strengthens the lower bound to eight.
\(\square\)

## 3. Consequence for the proof programme

For a fixed colour-matched path there is no residual purely combinatorial
compatibility case: failure to retain four mutually adjacent protected
components always exposes the full neighbourhood of one connected set.
The remaining problem is quantitative and chromatic.  One must either
force one such boundary to have order seven, or transfer compatible
proper-minor six-colourings across a boundary of order at least eight.

This theorem does not provide that upper bound or state transfer.  The
connectivity-only claim that an eight-connected graph with a
`K_7`-minus-one-edge minor has a `K_7` minor is deliberately not invoked;
it is open-problem strength.

## 4. Dependencies

- [colour-matched repair path](../results/hc7_colour_matched_repair_path.md)
- [component-transversal exchange criterion](../results/hc7_colour_matched_path_component_exchange.md)
- [hardness of connectivity-only near-`K_7` augmentation](../barriers/hc7_eight_connected_near_k7_augmentation_hardness.md)
