# A label-preserving split for the repeated packet leaf

## 1. The multiplicity cell

Use the notation of `hadwiger_full_shore_packet_fan_cut.md`.  Suppose a
five-path fan has final vertices in four of the five pairwise adjacent
leaf bags.  Write the distribution as

\[
        L,L,N_1,N_2,N_3,
\]

and let `M` be the missed leaf.  Let the two distinct final vertices in
`L` be `u,v`, and let `b` be the boundary root of `L`.  For
`j=1,2,3` and for the missed leaf put

\[
 Q_j=N_L(N_j),\qquad Q_M=N_L(M).
\tag{1.1}
\]

All four portal sets are nonempty because the old leaf bags are
pairwise adjacent.

Choose any spanning tree `T` of `G[L]`.  The result below is purely
label-preserving: it uses the two named fan ends, the root, and the four
actual portal classes, and does not identify a contracted leaf with an
unlabelled helper.

## 2. A split which immediately repairs the fan

### Lemma 2.1 (missed-leaf absorption split)

Suppose an edge of `T` gives a bipartition

\[
                         L=A\mathbin{\dot\cup}B
\tag{2.1}
\]

such that, after possibly interchanging `u,v`,

\[
 \begin{aligned}
 &u\in A,\qquad v,b\in B,\qquad A\cap Q_M\ne\varnothing,\\
 &B\cap Q_j\ne\varnothing\quad(j=1,2,3).
 \end{aligned}                                                \tag{2.2}
\]

Then the multiplicity obstruction gives a literal `K_7` model.

### Proof

Both `A` and `B` are connected and an edge joins them.  Since `A`
contains a portal to `M`, the enlarged bag

\[
                              M'=M\cup A
\tag{2.3}
\]

is connected.  The fan path formerly ending at `u` now ends in `M'`;
the other repeated path still ends at `v in B`.  The three remaining
paths end in `N_1,N_2,N_3`.  Thus the same source bag is adjacent to all
five new leaf bags

\[
                              B,M',N_1,N_2,N_3.                \tag{2.4}
\]

These bags are pairwise adjacent.  The three `B-N_j` adjacencies are
retained by (2.2), while `B-M'` is the tree edge across (2.1).  Every
pair among `M,N_1,N_2,N_3` was already adjacent before `A` was absorbed.
The root `b` remains in `B`, and the root of `M` remains in `M'`.
Consequently the opposite full shore still sees all five leaf bags.

Writing `P^+` for the connected source bag formed from `P` and the fan
paths before their final vertices, the seven branch bags are

\[
                     R,\quad P^+,\quad B,\quad M',\quad
                     N_1,\quad N_2,\quad N_3.                 \tag{2.5}
\]

They are disjoint, connected and pairwise adjacent.  This is a `K_7`
model.  QED.

The absorption in (2.3) is useful: the residual bag need not retain a
second direct `L-M` portal.  The split edge itself becomes its adjacency
to the enlarged missed leaf.  This avoids an unjustified portal-
multiplicity assumption.

### Corollary 2.2 (path-extension version)

If, in addition to (2.2), `B cap Q_M` is nonempty, one may leave `M`
unchanged.  Extend the path ending at `u` through `T[A]` to an
`A-M` edge, absorb `A` into the source bag, and use

\[
                       R,P^+\cup A,B,M,N_1,N_2,N_3.
\]

The retained `B-Q_M` portal supplies the `B-M` adjacency.  Thus this is
the stronger literal “extend one repeated path through the peel” form.

## 3. Exact capacity-state criterion on the portal tree

The existence of the split in Lemma 2.1 has an exact one-dimensional
test.  It turns the unbounded tree into a bounded portal-order state.

Fix `e in {u,v}` and write `f` for the other repeated end.  Let `K_e`
be the `b-f` path in `T`, and let

\[
             e=x_0,x_1,\ldots,x_k
\tag{3.1}
\]

be the path from `e` to its first vertex `x_k` in `K_e`.  If `e` already
belongs to `K_e`, take `k=0`.  Every vertex `y of T` has a projection
index

\[
 \pi_e(y)=\max\{i:x_i\text{ lies on the }e\text{-}y\text{ path}\}.
\tag{3.2}
\]

Vertices beyond `x_k`, including `b` and `f`, have index `k`.  For
`0<=i<k`, the component `W_i` of
`T-x_ix_{i+1}` containing `e` is exactly

\[
                              W_i=\{y:\pi_e(y)\le i\}.         \tag{3.3}
\]

Put

\[
 \alpha_e=\min_{q\in Q_M}\pi_e(q),\qquad
 \beta_e=\min_{j=1,2,3}\ \max_{q\in Q_j}\pi_e(q).            \tag{3.4}
\]

### Theorem 3.1 (leaf capacity-state exchange)

For the fixed tree `T`, a split satisfying Lemma 2.1 exists if and only
if

\[
                         \alpha_e<\beta_e                 \tag{3.5}
\]

for at least one `e in {u,v}`.

If (3.5) fails at both ends, then for each `e` there is a blocking
already-hit leaf `N_{j_e}` such that

\[
 \max_{q\in Q_{j_e}}\pi_e(q)
       =\beta_e\le\alpha_e
       =\min_{q\in Q_M}\pi_e(q).                            \tag{3.6}
\]

Thus all portals from `L` to one already-hit leaf are exhausted no
deeper along the `e`-arm than the first portal to the missed leaf.  This
ordered blocker, at both repeated ends, is the exact exceptional
skeleton; arbitrary leaf-tree geometry does not survive.

### Proof

For `i<k`, the edge `x_ix_{i+1}` separates `e` from `b` and `f`.
The `e`-side `W_i` contains a missed-leaf portal exactly when

\[
                              \alpha_e\le i.                  \tag{3.7}
\]

Its complement contains a portal of every `Q_j`, `j=1,2,3`, exactly
when

\[
                  i<\max_{q\in Q_j}\pi_e(q)quad(j=1,2,3),
\]

or equivalently `i<beta_e`.  Hence an admissible edge exists precisely
when there is an integer `i` with

\[
                              \alpha_e\le i<\beta_e,
\]

which is (3.5).  Taking `A=W_i`, `B=L-W_i` gives Lemma 2.1.

If (3.5) fails, choose a class attaining the outer minimum in the
definition of `beta_e`.  This is (3.6).  QED.

## 4. The obstruction is a bounded labelled skeleton

The inequalities (3.6) have a certificate of bounded topological size.
For each `e in {u,v}`, choose

* one `m_e in Q_M` attaining `alpha_e`; and
* one `q_{e,j} in Q_j` attaining the maximum in (3.4), for each
  `j=1,2,3`.

Together with `u,v,b`, these give at most eleven marked vertices of `T`.
Let `T_0` be their minimal spanning subtree and suppress every unmarked
degree-two vertex.  Every leaf of the resulting tree is marked, so it
has at most

\[
                              2(11)-2=20                      \tag{4.1}
\]

vertices.  The projections of the eight portal witnesses onto the
three-arm Steiner tree of `u,v,b` retain all comparisons in (3.5)--
(3.6).  Therefore failure of the label-preserving split is certified by
a labelled tree on at most twenty vertices, two blocker labels
`j_u,j_v in {1,2,3}`, and the weak/strict order at the two threshold
positions.

Equivalently, the unbounded multiplicity obstruction has only

\[
                         3^2\cdot2^2=36                       \tag{4.2}
\]

coarse blocker states before coincidences and symmetries are identified.
The number (4.2) is not asserted to be a complete graph-isomorphism
count; it is the exact capacity/order data relevant to the split.

If the original leaf bag is chosen inclusion-minimal for its root and
four adjacency roles, its spanning tree has the familiar Steiner form:
each tree leaf is charged to the root or to a unique adjacency role.
Theorem 3.1 shows what the two fan ends add to that normal form.  Either
one arm opens and (2.5) is an explicit `K_7`, or both arms terminate in
the bounded ordered blocker skeleton (3.6).  No general small ambient
cut follows from tree minimality alone, since vertices on a corridor may
have arbitrarily many neighbours outside the bag.  Any cut conclusion
must additionally use the actual portal/interface surplus of the
ambient seven-connected graph.

## 5. Consequence for the packet-fan trichotomy

Outcome 3 of `hadwiger_full_shore_packet_fan_cut.md` can therefore be
replaced by the sharper alternative:

1. the repeated leaf has an absorption peel, giving the seven bags
   (2.5); or
2. for every selected repeated fan and spanning portal tree, both fan
   ends satisfy the ordered blocker inequality (3.6), certified by the
   bounded twenty-vertex labelled skeleton.

This is a uniform leaf-splitting theorem.  It does not by itself exclude
the 36 blocker states; the next operation-level exchange needs only
those states, rather than an arbitrary five-portal tree.
