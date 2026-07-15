# What model minimality really forces in a same-row obstruction

**Status:** proved local structural lemma.  It is not the same-row split
theorem and does not create a ranked receiver.

## 1. Setup

Let

\[
                         \mathcal M=(F,F_1,\ldots,F_5)
\]

be a labelled `K_6` model in `G-{z,u}`.  Suppose that distinct vertices
`x,y in F` are adjacent to `z,u`, respectively.  Among all labelled
models which preserve these two literal vertices in the first row and
preserve all six clique-model adjacencies, first maximize any monotone
two-pole contact potential and then minimize `|F|`.  The only property of
the potential used below is this: adding a pole contact to a foreign row
does not make the potential worse.

For a nonempty proper set `X subset F`, call `X` **root-free detachable**
when

* `G[X]` and `G[F-X]` are connected; and
* `x,y notin X`.

Put

\[
 \Omega_F(X)=\{i\in[5]:
       \text{every literal `F-F_i` model edge has its `F`-end in `X`}\}.
\tag{1.1}
\]

## Theorem 2.1 (two-owner rule away from the poles)

Every root-free detachable `X` satisfies

\[
                              |\Omega_F(X)|\ge2.        \tag{2.1}
\]

### Proof

If `Omega_F(X)` is empty, replace `F` by `F-X` and omit `X`.  The
residual row is connected, contains `x,y`, and retains every foreign-row
edge.  It therefore still contacts both poles and gives the same labelled
model with smaller first row.

Suppose `Omega_F(X)={i}`.  Replace

\[
                    F\longmapsto F-X,
       \qquad       F_i\longmapsto F_i\cup X.           \tag{2.2}
\]

The enlarged row is connected through an old `X-F_i` edge.  The residual
row retains every foreign adjacency except possibly `FF_i`, and an edge
across the connected split `X | (F-X)` restores that adjacency after
(2.2).  Every old adjacency of `F_i` to another foreign row survives.

The residual first row still contains `x,y`, so it still contacts both
poles.  Moving `X` can only add pole contacts to `F_i`; it cannot remove a
contact required by the comparison class.  Hence the contact potential
does not decrease.  If it increases, maximality is contradicted.  If it
does not, (2.2) contradicts the minimum choice of `|F|`.  Both cases are
impossible, proving (2.1).  \(\square\)

## Corollary 2.2 (at most two root-free lobes)

There are at most two pairwise disjoint root-free detachable subsets of
`F`.

### Proof

The monopoly sets of disjoint detachable subsets are disjoint: the
nonempty set of all `F`-ends of the edges to one row cannot be wholly
contained in two disjoint sets.  Each monopoly set has order at least two
by Theorem 2.1, and only five labels are available.  \(\square\)

## Corollary 2.3 (four-leaf block frame)

The block-cutvertex tree of `G[F]` has at most four leaf blocks: at most
two whose interiors contain `x` or `y`, and at most two further leaf
blocks.

### Proof

The interior of a leaf block is connected, and deleting it leaves the
rest of the block tree connected.  Leaf-block interiors are pairwise
disjoint.  Any one which contains neither `x` nor `y` is therefore a
root-free detachable set.  Corollary 2.2 permits at most two of these;
only two other leaf interiors can contain the two named roots.  \(\square\)

## 3. Exact trust boundary

The theorem is sharp in the way relevant to the active decoder.  It does
not constrain lobes containing `x` or `y`.  Those two protected lobes can
own complementary bundles of foreign rows and prevent both sides from
retaining all five duties.  The two-apex icosahedron barrier realizes
exactly this endpoint-bundle obstruction with a two-vertex row.

Thus minimal portal-tree surgery gives a bounded four-leaf frame, but it
does not yield the split in Lemma 5.3.  In the endpoint-bundle residue the
next legitimate operation must use a proper-minor state attached to an
owned portal edge, or prove that the two protected bundles extend to one
coherent fixed-pair terminal.  Calling the endpoint bundles a graph
separator or an exact-seven receiver without that operation would be an
unranked handoff.

