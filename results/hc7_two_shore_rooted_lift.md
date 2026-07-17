# A two-shore rooted-model lift

**Status:** written proof with a separate GREEN internal audit in
[`hc7_two_shore_rooted_lift_audit.md`](hc7_two_shore_rooted_lift_audit.md).
This is a general branch-set lemma; it uses neither colouring nor
contraction-criticality.

## 1. The lift

### Theorem 1.1 (two full shores add two clique bags)

Let

\[
                         V(G)=A\mathbin{\dot\cup}S
                                  \mathbin{\dot\cup}B
\]

where `G[A]` and `G[B]` are nonempty and connected, there is no `A-B`
edge, and every vertex of `S` has a neighbour in each of `A` and `B`.
If `G[S]` contains a `K_r` model with support `W proper subset S`, then
`G` contains a `K_{r+2}` minor.

### Proof

Let `D_1,...,D_r` be the branch bags of the model and choose
`u in S-W`.  Retain the first `r` bags and add

\[
                              A\cup\{u\},\qquad B.       \tag{1.1}
\]

The first new bag is connected because `u` has a neighbour in `A`; the
second is connected by hypothesis.  They are adjacent because `u` has a
neighbour in `B`.  Each `D_i` contains a boundary vertex, and every
boundary vertex has a neighbour in each open shore.  Thus both new bags
are adjacent to every `D_i`.  All bags are disjoint, so they form a
`K_{r+2}` model.  \(\square\)

The unused boundary vertex is essential only for joining the two
anticomplete shores.  No edge between two packets or shores is assumed.

## 2. Application to a minimal bad split contraction

Use the notation of
[`hc7_three_split_minimal_bad_contraction.md`](hc7_three_split_minimal_bad_contraction.md).
In its exact two-component residue, write the components of `H-T` after
literal expansion as `A,B` and write the expanded boundary as `S=T^+`.
The minimal-bad-contraction theorem gives

\[
 |S|\in\{8,9\},\qquad
 N_G(s)\cap A\ne\varnothing\ne N_G(s)\cap B
                    \quad(s\in S).                    \tag{2.1}
\]

### Corollary 2.1 (boundary exclusion)

If `G` has no `K_7` minor, then `G[S]` has no `K_5` model supported on a
proper subset of `S`.  Equivalently:

* at expanded order eight, every support-at-most-seven `K_5` model is
  forbidden in `G[S]`; and
* at expanded order nine, every support-at-most-eight `K_5` model is
  forbidden in `G[S]`.

### Proof

Apply Theorem 1.1 with `r=5`.  \(\square\)

### Corollary 2.2 (named footprint bound)

For every contracted named model

\[
                     M_i=Q_i\mathbin{\dot\cup}\{x_i,y_i\},
\]

one has

\[
                              |Q_i\cap T|\le3.          \tag{2.2}
\]

### Proof

If `Q_i subseteq T`, then inside the literal expanded boundary the four
singleton bags `Q_i` and the edge-bag `{x_i,y_i}` form a `K_5` model on
six vertices.  Since `|S|>=8`, its support is proper in `S`, contradicting
Corollary 2.1.  \(\square\)

## 3. Exact scope

This lemma removes every two-shore residue whose boundary already carries
a nonspanning `K_5` model.  It does not turn a `K_5` model using vertices
of one open shore into a boundary model: the occupied shore cannot then be
reused as one of the two added bags.  That is precisely why the remaining
two-component problem still asks for a reserved connected carrier or a
label-faithful component split.
