# Port-matching cycle exchange: compatible cylinder or rooted `K_4`

## Status and role

This is an **audited uniform rooted-model principle**.  It converts literal
port edges between two two-connected rural
shores into exactly the dichotomy needed by a labelled expansion:

* compatible cyclic port orders glue as a planar cylinder; or
* incompatible orders give a `K_4` minor whose four branch sets contain
  four specified port edges.

It is the uncontracted, label-preserving form of the audited two-shore
cycle-order exchange in `../results/hc7_rural_cycle_order_exchange.md`.

## Theorem 1 (port-matching cycle exchange)

Let `L,R` be vertex-disjoint graphs.  Let

\[
 M=\{\ell_i r_i:i\in I\}                                 \tag{1.1}
\]

be a matching of literal edges, where all `ell_i` are distinct vertices of
`L` and all `r_i` are distinct vertices of `R`, and `|I|>=4`.  Suppose
`L` has a cycle `C_L` containing every `ell_i`, and `R` has a cycle `C_R`
containing every `r_i`.

Then exactly one of the following two order cases holds.

1. The cyclic orders of the indices `I` on `C_L` and `C_R` agree up to
   reversal.  If `L` and `R` have disk embeddings exposing those two
   cycles, the embeddings and all edges of `M` glue to a plane embedding.
2. The two cyclic orders differ.  The graph

   \[
                            L\cup M\cup R                 \tag{1.2}
   \]

   contains a `K_4` minor with four branch sets, each of which contains a
   different literal matching edge `ell_i r_i`.

### Proof

Suppress on each of `C_L,C_R` every maximal subpath whose internal
vertices are not matching endpoints.  This records two abstract cycles on
the index set `I`.  If their orders differ, Lemma 1 of the audited
cycle-order exchange gives two independent edges `ab,cd` of the suppressed
`R`-cycle whose ends alternate on the suppressed `L`-cycle; say their
`L`-order is `a,c,b,d`.

Lift `ab,cd` to their two arcs of `C_R`.  Their interiors contain no
matching endpoint and are disjoint.  In `C_L`, take the four arcs between
consecutive members of `a,c,b,d`.  These arcs are internally disjoint.
For each `x in {a,b,c,d}`, use the literal matching edge
`ell_x r_x` as an initial rooted gadget.  The four `L`-arcs and two
`R`-arcs are six internally disjoint connections between the four gadgets
in the pattern of all six edges of `K_4`; disjointness of `L` and `R`
prevents cross-shore intersections.

Choose one cut edge on each connection and assign the two remaining path
segments to the rooted gadgets at its ends.  The four resulting branch
sets are connected, disjoint and pairwise adjacent, and each retains its
whole literal matching edge.  Unselected matching edges are omitted from
the minor subgraph, so extra port endpoints on an `L`-arc cause no
collision.  This proves outcome 2 without contracting any unselected port.

If the orders agree, reflect one disk if necessary.  Place the exposed
cycles on the two boundary circles of an annulus with matching labelled
points in the same cyclic order, and draw the matching edges as disjoint
radial arcs.  Fill the two complementary disks with the given embeddings
of `L` and `R`.  This gives the planar gluing in outcome 1. \(\square\)

## Corollary 2 (three fixed rows complete `K_7`)

Suppose additionally that `F_1,F_2,F_3` are pairwise disjoint connected
pairwise adjacent branch sets, disjoint from `L union M union R`, and that
for every `i in I` the port edge `ell_i r_i` has at least one endpoint
adjacent to each `F_j`.  If the two port orders differ, the host graph has
a literal `K_7` minor.

### Proof

The four branch sets from Theorem 1 each contain one selected port edge.
By hypothesis each is adjacent to every `F_j`.  Together with the three
pairwise adjacent fixed rows they form seven pairwise adjacent connected
branch sets. \(\square\)

It is enough to impose the three-row contact condition only on the four
port edges returned by the crossing, but the pointwise hypothesis makes
the conclusion independent of which four the order conflict selects.

## Corollary 3 (four contiguous label blocks)

Partition a subset of the matching edges into four nonempty labelled
classes `M_1,M_2,M_3,M_4`.  Suppose the occurrences of each class form one
contiguous block in each of the two cyclic port orders.  If the induced
cyclic orders of the four class labels differ up to reversal, choose one
matching edge from each class.  Their endpoint orders still differ, so
Theorem 1 gives a `K_4` minor rooted at one literal port edge of every
class.

This is the palette-to-labelled-carrier feature: a mismatch of four
label blocks returns four different labels, not merely four arbitrary
boundary vertices.

## Sharpness and trust boundary

Distinct port endpoints and closing cycles on both sides are essential.
With only two boundary paths, the orders `1234` and `1324` give `K_4-e`
after suppression and no `K_4` minor.  If several port edges share an
endpoint, contracting all of them collapses labels and the rooted conclusion
can fail; a common-portal absorption theorem is then required first.

The theorem does not prove that a near-`K_7` interface supplies the two
port cycles or the pointwise contacts to three fixed rows.  It says that
once those literal features are present, cyclic-order incompatibility is
terminal rather than a new case family.
