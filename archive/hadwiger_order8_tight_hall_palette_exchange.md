# The defect-one order-eight gate is an exact Two Paths web

## 1. Setting and scope

Let

\[
 S=\{c_0,\ldots,c_5,z\},
\]

where the missing-edge graph on the `c_i` is the cycle
`c_0c_1...c_5c_0`, and `z` is adjacent to all six cycle vertices.
Let `H` be a connected old shore full to `S`.

Consider the defect-one tight-Hall outcome of Corollary 4.4 in
`hadwiger_colorful_rk4_spqr_exchange.md`.  After rotating the cycle, write

\[
 i=c_0,\qquad k=c_1,
\]

so that `x` is a common portal of `c_0,c_1` and the `c_1`-portal in the
open side is unique.  Let the open-side defect be `alpha`, and let `K` be
a component behind the exact order-eight separator.  In the absence of
the order-seven alternative, every displayed gate vertex is necessary,
so

\[
 N_S(K)=S-\{c_1,\alpha\},\qquad x\in N(K).          \tag{1.1}
\]

For a gate vertex `r`, put `P_r=N_K(r)`.  Thus all portal sets occurring
below are nonempty.

The purpose of this note is to identify the exact graph-theoretic content
of the remaining order-eight state.  It does not eliminate the final web.

## 2. Three defect positions close in the bare quotient

### Lemma 2.1 (easy defect rows)

If

\[
             \alpha\in\{c_2,c_5,z\},               \tag{2.1}
\]

then `G` contains a `K_7` minor.

### Proof

Contract `K` to one connected bag, still denoted `K`.  For
`alpha=c_2`, use

\[
 \{c_0\},\ \{c_3\},\ \{z\},\ K,\
 \{c_2,c_5\},\ \{c_1,x\},\ H\cup\{c_4\}.          \tag{2.2}
\]

For `alpha=c_5`, use

\[
 \{c_0\},\ \{c_2\},\ \{c_4\},\ \{z\},\ K,\
 H\cup\{c_3\},\ \{c_1,c_5,x\}.                   \tag{2.3}
\]

For `alpha=z`, use

\[
 \{c_0\},\ \{c_2\},\ \{c_4\},\ \{z\},\ H,\
 K\cup\{c_3\},\ \{c_1,c_5,x\}.                   \tag{2.4}
\]

Every displayed set is connected.  Pairwise adjacency follows directly
from the complement-of-cycle boundary, fullness of `H`, (1.1), and the
two literal edges `xc_0,xc_1`.  These are seven branch bags.  QED.

The two bare quotient survivors are therefore

\[
                         \alpha=c_3,c_4.            \tag{2.5}
\]

The exact verifier `order8_tight_hall_quotient_probe.py` checks all
connected branch-set partitions of the ten-vertex quotient.  It confirms
that neither quotient in (2.5) itself has a `K_7` minor.  This negative
calculation is not used in any positive proof below; it records that a
static quotient contraction cannot close the two rows.

## 3. The hard rows are two prescribed linkages

### Lemma 3.1 (two-path completion)

In the row `alpha=c_3`, suppose `K` contains vertex-disjoint connected
subgraphs `L_1,L_2` with

\[
 L_1\cap P_x\ne\varnothing,\quad L_1\cap P_{c_2}\ne\varnothing,
 \qquad
 L_2\cap P_{c_4}\ne\varnothing,\quad L_2\cap P_{c_5}\ne\varnothing.
                                                               \tag{3.1}
\]

Then `G` has a `K_7` minor.

In the row `alpha=c_4`, the same conclusion holds if there are disjoint
connected `L_1,L_2` with

\[
 L_1\cap P_x\ne\varnothing,\quad L_1\cap P_{c_5}\ne\varnothing,
 \qquad
 L_2\cap P_{c_2}\ne\varnothing,\quad L_2\cap P_{c_3}\ne\varnothing.
                                                               \tag{3.2}
\]

### Proof

Extend `L_1,L_2` to a connected bipartition

\[
                         K=A\mathbin{\dot\cup}B     \tag{3.3}
\]

with `L_1` in `A`, `L_2` in `B`, and an `A-B` edge.  This is the standard
two-core extension: contract the cores in a spanning tree and cut one
edge on the path between them.

For `alpha=c_3`, the seven bags are

\[
 \{c_0\},\ \{c_2\},\ \{c_4\},\ \{z\},\ H,\
 A\cup\{x,c_1\},\ B\cup\{c_3,c_5\}.               \tag{3.4}
\]

The last bag is connected because `B` meets `P_{c_5}` and `c_3c_5` is
an edge.  It sees `{c_4}` through the `c_4` portal.  Its other required
adjacencies are inherited from `c_3,c_5`, fullness of `H`, and the
`A-B` edge.  The penultimate bag is connected through an `x` portal and
sees `{c_2}` through the `c_2` portal; all its other boundary
adjacencies are inherited from `c_1,x`.

For `alpha=c_4`, use

\[
 \{c_0\},\ \{c_2\},\ \{z\},\ H,\ \{c_1,c_4\},\
 B\cup\{c_3\},\ A\cup\{x,c_5\}.                   \tag{3.5}
\]

Here `B` meets `P_{c_3}` for connectivity and `P_{c_2}` for the only
boundary adjacency not inherited from `c_3`; the other checks are
literal.  Thus (3.4) and (3.5) are `K_7` models.  QED.

The hypotheses can equivalently be phrased as two vertex-disjoint paths
between portal sets.  Add four artificial terminals adjacent to the four
sets in (3.1), or in (3.2), and delete the artificial first and last
edges after obtaining the linkage.

### Corollary 3.2 (exact Two Paths web alternative)

In a `K_7`-minor-free hard row, the corresponding augmented graph has no
two disjoint paths joining the two prescribed terminal pairs.  Hence the
Two Paths Theorem places every edge-maximal nonlinkable completion in a
web with the four terminals in alternating outer order (with the usual
clique insertions in facial triangles).

Thus the order-eight tight-Hall outcome is not a generic eight-separator.
After the three easy defect rows are removed, it is exactly one of the
two labelled web states

\[
 (P_x,P_{c_2})\mid(P_{c_4},P_{c_5}),
 \qquad
 (P_x,P_{c_5})\mid(P_{c_2},P_{c_3}).               \tag{3.6}
\]

### Proof

If the prescribed linkage existed, Lemma 3.1 would give `K_7`.  Apply
the standard Two Paths Theorem to an edge-maximal nonlinkable completion,
exactly as in Theorem 3.1 of
`hadwiger_atomic_portal_order_operation_states.md`.  QED.

The word *completion* is essential: it does not imply that every added
web edge is present or realizable in `K`.  Bridge confinement is valid
only after saturation, as explained in Example 3.3 of that note.

## 4. What the palette-star theorem supplies

Theorem 1.1 of `hadwiger_palette_anchor_rooted_star.md` is valid and
useful here.  A family of differently coloured Kempe anchors gives one
protected connected centre bag, because an `alpha/beta` path cannot pass
through an anchor of a third colour.

### Lemma 4.1 (protected-column terminal)

In either hard row, suppose two applications of the palette-anchor
theorem yield disjoint connected centre bags contained in `K`, the first
meeting the two portal classes in the first pair of (3.6), and the second
meeting the two portal classes in the second pair.  Then `G` has a `K_7`
minor.

### Proof

The two centre bags are the two subgraphs `L_1,L_2` in Lemma 3.1.  QED.

This is the exact point where palette labels must be aligned with portal
labels.  One palette star is insufficient, even when its common-alpha
warehouse has order one.

### Example 4.2 (the warehouse bound alone does not split the web)

Take an alpha-coloured hub `t` and four leaves of four distinct non-alpha
colours.  Join each leaf only to `t`.  The palette-anchor theorem gives
the rooted star, and the alpha warehouse is the singleton `{t}`.  But
two paths joining two alternating pairs of leaves must both contain `t`,
so they cannot be disjoint.

The same example realizes the full cross-interaction clause of the
coupled-star lock.  Take alpha-coloured vertices `p,a,b,t`.  For each
colour `beta` in a nonempty set `E_B`, add a beta vertex adjacent to
`p,b` and another beta vertex adjacent to `a,t`.  For each colour `gamma`
in a nonempty set `E_A`, add a gamma vertex adjacent to `p,a` and another
gamma vertex adjacent to `b,t`.  Every unsupported beta component at
`a` and unsupported gamma component at `b` meets in the alpha vertex
`t`; all conclusions of the coupled lock and the warehouse bound hold.
In particular, the entire cross-interaction conclusion can be discharged
by one alpha vertex: it contains no hidden assertion that two protected
centre bags are disjoint.

This is a local coloured counterarchitecture, not a hypothetical
seven-connected counterexample.  It proves the precise logical point:
the coupled-star conclusions plus `|Z_alpha|<=3` do not by themselves
imply the two disjoint protected columns of Lemma 4.1.  Seven-connectivity,
the opposite pole orientation, or the one-step minor-transition states
must be used to break the web bottleneck.

## 5. Exact remaining theorem

The order-eight alternative in Corollary 7.4 of
`hadwiger_colorful_rk4_spqr_exchange.md` can now be replaced by the
following narrower statement.

> In one of the two webs (3.6), the exact minor-transition state and the
> opposite exclusive palette family either realize the second protected
> column of Lemma 4.1, or induce the same marked equality state on the two
> sides of a web gate and hence colour-glue.

The second alternative cannot mean preservation of an arbitrary honest
`G-v` boundary partition on the whole order-eight gate.  Lemma 2.1 of
`hadwiger_order8_exact_trace_marked_state.md` proves the uniform stronger
fact that every operation supported in a neighbourhood-free open shore
changes every such partition.  The required common state, if it exists,
must therefore be a genuinely new transition state synchronized across
two operated sides.

This is a genuine two-shore capacity--state web exchange.  It no longer
contains an arbitrary defect label, an arbitrary four-class assignment,
or an arbitrary order-eight separator.  The remaining difficulty is
dynamic: proving compatibility of the protected palette column with the
literal portal column.  Static Hall counting and the alpha-warehouse
bound cannot prove it, by Example 4.2.
