# Locked two-row carrier: linkage, one rural face, or a sharp gate path

## Status

This note isolates the exact residue left by rooted-triangle promotion.
A carrier is simultaneously needed to give a private row `H` to the
left shore and a blocked row `Q` to the right shore.  A protected fixed
linkage closes the carrier.  In a four-connected carrier, failure puts
all usable portals on one coherent rural face.  Without that internal
connectivity, the final section gives an arbitrary-boundary path
obstruction, so a generic protected portal-peel recursion is false.

The rural outcome is not by itself a global two-apex conclusion.

## 1. Protected fixed linkage

Use a path cut `L|R`.  Let `K` be an old exterior carrier, disjoint from
the path and every foreign row.  Let

\[
 A_L=N_K(L),\quad A_R=N_K(R),\quad
 P_H=N_K(H),\quad P_Q=N_K(Q),                              \tag{1.1}
\]

where `H,Q` are two distinct connected foreign rows.  Assume the four
portal families admit a system of distinct representatives.

### Lemma 1 (literal linkage completion)

If `K` contains disjoint paths, one joining `A_L` to `P_H` and the
other joining `A_R` to `P_Q`, then the left shore can be enlarged to see
`H` and the right shore can be enlarged to see `Q`, without using a
vertex of any foreign row or any other old exterior carrier.

Thus any two mutually disjoint helper families outside `K`, with every
helper piece already attached to its assigned path side, can be adjoined
to the corresponding enlarged shores; connectedness and all remaining
literal row contacts survive.  When those helpers supply the other rows
in the one-missing capacity state, the literal shore-completion theorem
gives a `K_7` minor.

#### Proof

Adjoin the first path to `L` and the second to `R`.  Each enlarged shore
is connected through its first portal edge.  The shores are disjoint,
remain adjacent through the old path-cut edge, and see their named rows
through the last portal edges.  Both paths lie in `K`, which is disjoint
from every protected helper and foreign bag.  All old contacts therefore
survive, and adjoining helpers already attached to the old path sides
preserves shore connectedness. \(\square\)

## 2. Four-connected carriers have one coherent face

### Theorem 2 (fixed linkage or portal-cofaciality)

Suppose `K` is four-connected.  Then either

1. the protected fixed linkage of Lemma 1 exists; or
2. `K` is planar and one face contains every vertex of
   `A_L union A_R union P_H union P_Q` which occurs in a full system of
   distinct representatives of the four portal families.

For every representative quadruple in outcome 2, the cyclic order is
alternating for the prescribed pairs `(A_L,P_H)` and `(A_R,P_Q)`;
otherwise the two boundary arcs already give the fixed linkage.

#### Proof

Let `(l,r,h,q)` be any system of distinct representatives.  An
`{l,r,h,q}`-rooted `K_4` model contains the required linkage: use the
two rooted branch sets and their joining edge for the `l-h` path, and
the other two branch sets and their joining edge for the `r-q` path.
The paths are disjoint because the four rooted branch sets are disjoint.

Hence, if outcome 1 fails, no representative quadruple has a rooted
`K_4` model.  Apply the SDR facial-coherence theorem
(`../results/hc7_near_k7_active_root_face_exchange.md`, Theorem 2.3) to
the four portal families in the four-connected graph `K`.  It gives one
plane embedding and one face containing every portal vertex occurring
in a full SDR, proving outcome 2.

In a plane graph, four cofacial terminals whose prescribed pairs do not
alternate can be joined by disjoint subarcs of the facial boundary
(shortening repeated boundary walks if necessary).  Such arcs would be
outcome 1.  Therefore every surviving SDR has alternating order.
\(\square\)

The theorem is label-faithful: the linkage paths avoid the foreign rows,
and the rural face contains the literal portal vertices.  But expanding
this one disk does not delete literal apex vertices from the rest of the
host; different carriers must still be shown to use compatible rotations
and the same global exceptional pair.

## 3. A sharp path obstruction to unconditional peeling

Let

\[
                        K=k_Lk_Qk_Rk_H                       \tag{1.2}
\]

be a four-vertex path.  Give `k_L` neighbours only on the path side `L`,
`k_R` neighbours only on the path side `R`, `k_H` foreign contacts only
in row `H`, and `k_Q` foreign contacts only in row `Q`.  These four
contact sets may contain arbitrarily many distinct boundary vertices.
In particular choose at least six neighbours for each end vertex and at
least five for each internal vertex.  Then every vertex of `K` has
degree at least seven in the displayed local graph and

\[
                         |N_G(K)|\ge 22.                      \tag{1.3}
\]

The carrier is crossing, is the unique `H`-support for the left state
and the unique `Q`-support for the right state, and is anticomplete to
any prescribed missed twin `D`.  Nevertheless the fixed linkage is
impossible: the unique `k_L-k_H` path contains the edge `k_Qk_R`, which
is the unique `k_R-k_Q` path.

Rooted-triangle promotion does not fix this example.  In the promotion
of `L,R,Q`, the articulation `k_R` belongs to the right promoted shore,
while the sole `H` portal `k_H` lies behind `k_R`.  Connecting that
portal to the left shore would therefore meet the right shore.  The
protected `H` duty cannot simultaneously be assigned to the left by a
disjoint carrier.

The large boundary in (1.3) shows that seven-connectivity's numerical
adhesion lower bound alone does not remove the obstruction.  The
foreign rows and path sides can have rich connections outside `K`, so
the cutvertices of (1.2) need not be cutvertices of the whole host.
Subdividing the three path edges and retaining the same ordered portal
classes gives an unbounded family with the same linkage obstruction.
Raw subdivision vertices have degree two, so this last amplification is
not claimed to preserve the preceding local minimum-degree bound.

This is a local carrier counterarchitecture, not a claimed
seven-contraction-critical `K_7`-minor-free graph.  It proves the exact
negative statement needed here: protected ownership, arbitrarily large
boundary, and local minimum degree do not force the fixed linkage or a
strict portal peel.  A valid continuation must use the proper-minor
state transition to splice across this ordered gate, or prove that all
such gates compose into the same global rural society.
