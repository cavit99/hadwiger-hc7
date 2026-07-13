# Surplus-root transfer into unrooted clique bags

## Status

This is a parameter-uniform rooted-model exchange at the exact neutral
separator.  It converts two literal surplus boundary roots into the two
previously unrooted twin bags without losing the old clique model, or
exposes the exact residual-donor separator that prevents the simultaneous
move.  In the exchange branch, a full opposite shore supplies the next
clique branch set.

The theorem identifies the non-enumerative residual precisely: a
surviving exact-seven frame must lock every pair of surplus roots behind
multi-row monopoly sets, or all admissible transfers have one common
twin target.

## 1. One admissible transfer

Let `F_1,...,F_m` be pairwise disjoint connected pairwise adjacent bags.
Let `U=F_i`, let `T=F_j` with `i!=j`, and let `Z` be a nonempty proper
subset of `U`.  Call `Z` **transferable from `U` to `T`** when:

1. `G[Z]` and `G[U-Z]` are connected;
2. `Z` has an edge to `T`; and
3. for every `h notin {i,j}`, the residual `U-Z` still has an edge to
   `F_h`.

### Lemma 1 (root transfer)

If `Z` is transferable from `U` to `T`, then replacing

\[
                         U\mapsto U-Z,qquad
                         T\mapsto T\cup Z                 \tag{1.1}
\]

preserves a labelled `K_m` model.  Every marked root in `Z` moves to the
target bag, while every marked root in `U-Z` remains in the donor bag.

### Proof

The target is connected by item 2 and the residual donor by item 1.  An
edge across the connected split `Z|(U-Z)` restores the donor--target
adjacency.  Item 3 retains every other donor adjacency.  Enlarging the
target cannot destroy any of its old adjacencies, while all untouched
bags keep theirs.  Disjointness is preserved because all of `Z` is moved
once. \(\square\)

In portal-ownership language, item 3 is exactly

\[
                         \Omega_U(Z)\subseteq\{T\}.       \tag{1.2}

If the monopoly set is `{T}`, item 2 is automatic.  If it is empty, any
row actually met by `Z` is an admissible target.

## 2. Two surplus roots

Let `B,C,U_1,...,U_{m-2}` be a `K_m` model.  Let `S` be a set of marked
vertices lying in the `U_i`, with every `U_i` containing at least one
mark and `B,C` containing none.

### Theorem 2 (two-target surplus-root exchange or residual separation)

Suppose there are distinct donor bags `U_a,U_b` and disjoint marked
parts `Z_a subset U_a`, `Z_b subset U_b` such that:

* each `Z_h` and its donor complement are nonempty and connected;
* each `Z_h` contains a mark, and each donor complement contains a
  different mark; and
* after possibly interchanging `B,C`, `Z_a` is transferable to `B` and
  `Z_b` is transferable to `C`.

Put `W_a=U_a-Z_a` and `W_b=U_b-Z_b`.  If `W_a` and `W_b` are adjacent,
then the graph has an `S`-meeting `K_m` model: every one of its `m` bags
contains a distinct marked vertex of `S`.

If `W_a` and `W_b` are anticomplete, `N_G(W_a)` is an actual vertex
separator, with the connected nonempty set `W_b` on a far side.  In a
`k`-connected host this separator has order at least `k`; at order
exactly `k`, every separator vertex is full to every component of its
deletion.

In the first outcome, if in addition a connected set `X` is disjoint
from the model and has an edge to every vertex of `S`, then `X` together
with this rooted model is a `K_{m+1}` model.

### Proof

Suppose first that `W_a` and `W_b` are adjacent, and perform the two
transfers simultaneously.  They have disjoint donors and distinct
targets.  Lemma 1 verifies every adjacency incident with one changed
donor except that its retained edge to the old opposite donor could end
in the part simultaneously moved from that donor.  The explicit
`W_aW_b` edge is exactly the one additional adjacency needed after both
moves.  The two enlarged targets retain their old mutual edge, and each
residual donor retains its old edge to the opposite target.  Thus all
`m` bags remain connected, disjoint and pairwise adjacent.

The enlarged `B` and `C` contain the two moved marks.  The two donor
remainders retain their protected marks, and every other `U_i` retains
one.  These marks are distinct because the bags and moved parts were
disjoint.  This is an `S`-meeting `K_m` model.

For the final assertion, use `X` as one more branch set.  It is adjacent
to every rooted bag through that bag's selected member of `S`.

If instead `W_a` and `W_b` are anticomplete, then after deleting
`N_G(W_a)` the connected nonempty set `W_a` is separated from the
connected nonempty set `W_b`.  This is an actual separator.  The
connectivity lower bound follows immediately.  At equality, if one cut
vertex missed one component of the deletion, the other `k-1` cut
vertices would separate that component. \(\square\)

### Theorem 3 (one-donor two-piece exchange)

The `S`-meeting model conclusion also holds when both pieces lie in one
donor `U`, provided

\[
                 U=U_0\mathbin{\dot\cup}Z_B
                       \mathbin{\dot\cup}Z_C              \tag{2.1}

where all three sets are nonempty and connected, `U_0` is adjacent to
each of `Z_B,Z_C`, `Z_B` is adjacent to `B`, `Z_C` to `C`, and `U_0`
retains an edge to every bag other than `U,B,C`.  If each of the three
parts contains a distinct mark, transferring `Z_B,Z_C` to `B,C` gives an
`S`-meeting `K_m` model.

### Proof

The new donor is `U_0`; the two cut adjacencies in (2.1) restore its
edges to the enlarged `B,C`, so old `U_0-B,U_0-C` edges need not survive.
Its stipulated contacts retain all other rows.  Old target edges retain
every adjacency of the enlarged bags.
The mark count is literal. \(\square\)

### Theorem 4 (one-donor deficiency rotation)

Retain the exact-seven `HC_7` setting, so the four neutral bags are
`U,V_1,V_2,V_3`, the twins are `B,C`, and the connected full shore is
`X`.  Suppose

\[
                 U=U_0\mathbin{\dot\cup}Z_B
                       \mathbin{\dot\cup}Z_C              \tag{2.2}
\]

where all three parts are nonempty and connected, `U_0` is adjacent to
each moved part, `Z_B` meets `B`, `Z_C` meets `C`, and all three parts
contain distinct vertices of the full boundary `S`.  Put

\[
 \Lambda=\{i\in\{1,2,3\}:E(U_0,V_i)=\varnothing\}.       \tag{2.3}
\]

After transferring `Z_B,Z_C` to the twins:

* `Lambda=empty` gives an `S`-meeting `K_6` and hence a literal `K_7`;
* `|Lambda|=1` gives a labelled `K_7^-` model; and
* `|Lambda|=2` gives a labelled `K_7^vee` model,

with `U_0` as the new deficient centre.  Thus a partition of the form
(2.2) can avoid both the target and deficiency rotation only when

\[
                           \Lambda=\{1,2,3\}.             \tag{2.4}
\]

### Proof

Let `B'=B union Z_B` and `C'=C union Z_C`.  These bags are connected.
The cut edges from `U_0` to the two moved parts give literal
`U_0B',U_0C'` adjacencies.  The protected mark in `U_0` has a neighbour
in `X`, so `U_0X` is present.

The six bags

\[
                        X,B',C',V_1,V_2,V_3             \tag{2.5}
\]

form a clique model.  Indeed `X` meets `B',C'` through the marked roots
in the moved parts and meets each `V_i` through the old full neutral
contacts.  The two enlarged twins and the three untouched neutral bags
retain all old foreign-clique adjacencies.

Regard `U_0` as a new centre.  It meets `X,B',C'`; among the remaining
three foreign rows it misses exactly those indexed by `Lambda`.  The
four conclusions follow from `|Lambda|`. \(\square\)

Theorem 4 is useful even when neither moved piece is individually
monopoly-free.  What matters is only the number of untouched neutral rows
lost jointly after both roots move.

### Lemma 5 (three-root connected partition)

Let `U` be connected and contain at least three distinct marked vertices.
Then there is a partition

\[
                       U=U_0\mathbin{\dot\cup}Z_1
                            \mathbin{\dot\cup}Z_2         \tag{2.6}
\]

into nonempty connected sets such that `U_0` is adjacent to each `Z_i`
and all three parts contain distinct marks.

### Proof

Take a spanning tree of `G[U]` and let `T` be its minimal subtree
containing all marked vertices.  Every leaf of `T` is marked.  Choose two
leaves and delete their incident edges of `T` (the corresponding edges in
the spanning tree).  The two leaf-side components contain the chosen
marks.  The remaining component contains a third mark because at least
three marks occur and the two deleted leaf branches are distinct.  Add
each component of the spanning tree outside `T` to the unique part to
which it is attached.  Equivalently, take the three components of the
whole spanning tree after the two chosen edges are deleted.  They give
(2.6), and the deleted tree edges give both required adjacencies.
\(\square\)

### Corollary 6 (the one-donor exact-seven distribution)

Suppose all three surplus vertices of the exact-seven boundary lie with
the protected root in one neutral donor `U` (distribution
`4+1+1+1`).  Then at least one of the following holds:

1. `G` contains a `K_7` minor;
2. a labelled `K_7^-` or `K_7^vee` model is obtained by deficiency
   rotation; or
3. an actual separator of order at least seven is exposed, and it is full
   at exact order seven.

### Proof

Apply Lemma 5 to the four marked vertices of `U`, obtaining
`U_0,Z_1,Z_2`.  If one moved part misses either twin, its open
neighbourhood is an actual separator: the missed connected twin bag is a
nonempty far side.  Thus, outside outcome 3, both moved parts meet both
twins.  Assign `Z_1` to `B` and `Z_2` to `C` and apply Theorem 4.

If at most two untouched neutral rows are lost, Theorem 4 gives outcome
1 or 2.  In its sole remaining case, `U_0` is anticomplete to all three
other neutral bags.  Then `N_G(U_0)` is again an actual separator, with
any one of those connected neutral bags as a far side.  Seven-connectivity
gives its order, and exact-order fullness is the standard minimum-cut
conclusion. \(\square\)

Thus the concentrated four-root donor does not require a finite portal
catalogue.  Connected-tree partition plus deficiency rotation disposes of
the entire distribution, modulo the explicit actual-adhesion output.

## 3. Exact-seven `HC_7` consequence

Use the exact-seven separator `S` of
`hc7_near_k7_both_missing_neutral_separator.md`.  The old foreign bags

\[
                         B,C,U_1,U_2,U_3,U_4
\]

form a `K_6` model.  All seven vertices of `S` lie in the four neutral
bags and the connected path-side envelope `X` is adjacent to every one.

Choose one protected mark in each neutral bag.  There are three surplus
marks.  If two of them admit the distinct-donor transfer of Theorem 2,
or three marks in one donor admit Theorem 3, then an `S`-meeting `K_6`
model plus `X` is a literal `K_7` model.

Equivalently, form the bipartite transfer graph whose left vertices are
admissible surplus-root pieces and whose right vertices are `{B,C}`.
A matching of order two closes the exact-seven branch.  A target-free
frame must therefore satisfy one of the following structural failures:

1. surplus roots cannot be separated from a protected root while
   retaining all other row adjacencies;
2. every transferable surplus-root piece is confined to one donor bag
   without the three-part split of Theorem 3; or
3. every admissible piece has the same unique twin target.

These are portal-placement obstructions, not contact-count cases.  The
remaining rooted-model principle must turn one of them into a smaller
adhesion, a faithful proper-minor state splice, or one coherent two-apex
society.
