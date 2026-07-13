# Exact-seven portal-rooted triangle exchanges

## 1. Frozen input and purpose

Use the audited setup and conclusions of
`../results/hc7_exact7_rooted_triangle_portal_rank.md`:

* `V(G)=L dotunion S dotunion R`, `|S|=7`, with no `LR` edges;
* `G` is seven-connected, `R` contains three disjoint connected
  `S`-full packets, and `G[L]` is three-connected;
* `T={t_1,t_2,t_3}` is a three-cut with exactly two lobes `K,J`;
* every nontrivial lobe has a literal `T`-rooted `K_3` model; and
* portal rank three on such a model gives a literal `K_7`.

This note does not reprove those GREEN results.  It gives two concrete
label-preserving augmentations of a low-rank rooted triangle:

1. peel a labelled sector from a rich triangle bag into a sparse bag; or
2. split the *other lobe* into a deficient-root leaf and a labelled core.

The second mechanism is stronger: it leaves the original rooted triangle
untouched and spends the other lobe as the fourth clique carrier.

## 2. Exact Hall normal form

Let `(B_1,B_2,B_3)` be a `T`-rooted triangle in `G[K union T]`, extended
to a spanning partition of `K union T`.  Put

\[
                         P_i=N_S(B_i).
\]

Since `N_S(K) subseteq P_1 union P_2 union P_3` and
`|N_S(K)|>=4`, failure of a three-set SDR has at least one of the
following forms (the two forms can overlap):

* `P_i=emptyset` for some `i`; or
* `|P_i union P_j|<=1` for some pair `i,j`.

Indeed Hall's deficient subfamily cannot be all three bags.  This is the
literal palette-to-carrier defect which the exchanges below address.

## 3. A branch-bag peel

### Lemma 3.1 (one-piece peel)

Fix distinct indices `i,j,k`.  Let `Z` be a nonempty proper subset of
`B_j` such that:

1. `t_j notin Z`;
2. `G[Z]`, `G[B_j-Z]`, and `G[B_i union Z]` are connected; and
3. `B_j-Z` remains adjacent to `B_k`.

Then

\[
 B_i'=B_i\cup Z,\qquad B_j'=B_j-Z,\qquad B_k'=B_k
\]

is another spanning `T`-rooted triangle.  If its three bags have three
distinct literal representatives in `S`, then `G` contains a literal
`K_7`.

#### Proof

The bags remain disjoint, spanning, connected, and retain their roots.
Since `B_j` was connected and `Z,B_j-Z` are nonempty, a literal edge
joins those two sets; it gives `B_i'B_j'`.  The old `B_iB_k` edge gives
`B_i'B_k'`, and hypothesis 3 gives `B_j'B_k'`.  Hence the new bags are a
rooted triangle.  Portal rank three closes by the frozen rank-three
triangle theorem. `square`

For example, in the defect `P_i=emptyset`, it is sufficient that `Z`
introduce one new representative while the donor remainder and the third
bag retain two distinct representatives.  In the defect
`P_i union P_k subseteq {q}`, it is sufficient to peel into a portal-free
one of those bags a label different from `q`, while the other sparse bag
retains `q` and the donor remainder retains a third label.

### Lemma 3.2 (two-piece peel)

Let `Z_1,Z_2` be disjoint nonempty subsets of `B_3`, and put
`B_3^0=B_3-(Z_1 union Z_2)`.  Suppose:

1. `t_3 in B_3^0`;
2. `B_1 union Z_1`, `B_2 union Z_2`, and `B_3^0` are connected; and
3. `B_3^0` is adjacent to each of `B_1 union Z_1` and
   `B_2 union Z_2`.

Then the three displayed sets are a spanning `T`-rooted triangle.  If
`Z_1,Z_2,B_3^0` contact three pairwise distinct literal labels, then `G`
contains a literal `K_7`.

#### Proof

The old `B_1B_2` edge remains, and hypothesis 3 gives the other two
model adjacencies.  All other branch-set conditions are explicit in the
hypotheses.  Apply the rank-three closure. `square`

This eliminates every Hall monopoly whose rich bag has two detachable
portal sectors and a labelled rooted remainder.  Its negative certificate
is literal: each proposed sector contains the donor root, disconnects the
donor remainder, owns the donor's last adjacency to the third bag, or
strands the remaining labels in one class.

## 4. Spend the other lobe instead

The peel is not the only way to raise rank.  Keep the rooted triangle in
`K` fixed and split `J`.

### Lemma 4.1 (other-lobe star split)

Suppose `J` has a partition

\[
                     V(J)=X_0\dot\cup X_1\dot\cup X_2\dot\cup X_3
                                                               \tag{4.1}
\]

where `X_0` is nonempty and connected, each nonempty `X_i` is connected,
and, for every `i in {1,2,3}`, either

* `X_i` is nonempty, has a neighbour at `t_i`, and is adjacent to `X_0`;
  or
* `X_i` is empty and `X_0` has a neighbour at `t_i`.

Then

\[
                         X_0,\qquad B_i\cup X_i\quad(1<=i<=3)  \tag{4.2}
\]

are four disjoint connected, pairwise adjacent literal carriers.  If
their four literal portal sets have an SDR in `S`, then `G` contains a
literal `K_7`.

#### Proof

Each `B_i union X_i` is connected: this is clear for empty `X_i`, and
otherwise follows from the literal `X_it_i` edge.  The three such bags
remain pairwise adjacent through the old rooted triangle.  The core
`X_0` is adjacent to each one either through an `X_0X_i` edge or directly
through its edge to `t_i in B_i`.  This proves (4.2) is a `K_4` model.
Four distinct literal representatives, followed by the three opposite
`S`-full packets anchored at the remaining labels, give the literal
`K_7`. `square`

An unlabelled partition of the form (4.1) always exists.  Choose one
neighbour `y_i in J` of each `t_i` and a minimal tree joining the three
chosen vertices.  Put its median vertex in `X_0` and the three open arms
in the corresponding `X_i` (an arm is empty when its terminal is the
median).  Absorb every component outside the tree into an incident part.
The obstruction is therefore solely whether the fresh portal labels can
be placed on the required arms and core.

The following two-block version is convenient when the rooted triangle
already supplies two labels.

### Lemma 4.2 (two-block star split)

Fix an index `i` and write `{i,j,k}={1,2,3}`.  Suppose `J` has a connected
partition

\[
                         V(J)=X\dot\cup Y
\]

such that:

1. `X` and `Y` are nonempty and there is an `XY` edge;
2. `X` has a neighbour at `t_i`; and
3. `Y` has neighbours at both `t_j` and `t_k`.

Then

\[
                         B_i\cup X,\qquad B_j,\qquad B_k,\qquad Y
                                                               \tag{4.3}
\]

are four disjoint connected, pairwise adjacent literal carriers.
Consequently, if their four literal portal sets have an SDR in `S`, then
`G` contains a literal `K_7`.

#### Proof

The first carrier is connected through an `Xt_i` edge.  The first three
carriers remain pairwise adjacent through the old rooted triangle.
The carrier `Y` is adjacent to `B_i union X` through the `XY` edge, to
`B_j` through a `Yt_j` edge, and to `B_k` through a `Yt_k` edge.  Thus
the four sets in (4.3) form a `K_4` model.  Adjoin four distinct literal
representatives and anchor the three opposite `S`-full packets at the
remaining boundary vertices.  Packet fullness supplies all remaining
adjacencies, giving a literal `K_7`. `square`

### Corollary 4.3 (rank-two repair by two fresh portals)

Suppose two triangle bags, say `B_j,B_k`, have distinct representatives
`p_j,p_k`, while `B_i` is the unmatched bag.  Put
`F={p_j,p_k}`.  The audited forbidden-label lobe matching theorem gives,
when `|J|>=2`, distinct vertices `x,y in J` with distinct labels

\[
             a,b in S-F,\qquad ax,by in E(G).             \tag{4.4}
\]

If, after possibly interchanging `(x,a)` and `(y,b)`, there is a connected
partition `J=X dotunion Y` satisfying Lemma 4.2 and

\[
                         x in X,\qquad y in Y,             \tag{4.5}
\]

then `G` contains a literal `K_7`.

#### Proof

Represent the four carriers in (4.3) by
`a,p_j,p_k,b`, respectively.  They are distinct by (4.4), so Lemma 4.2
applies. `square`

This closes an unbounded family at once: no portal has to be peeled from
the existing rooted triangle, and the two new labels are guaranteed by
seven-connectivity.  Only their **ordered placement** in `J` remains.

## 5. Exact negative object: a block-terminal web

For fixed `i,x,y`, call a connected lobe `J` an
`(x,y;i|jk)` **block-terminal web** if no connected bipartition
`J=X dotunion Y` satisfies

\[
 x in X,\quad y in Y,\quad
 X\cap N_J(t_i)neemptyset,\quad
 Y\cap N_J(t_j)neemptyset,\quad
 Y\cap N_J(t_k)neemptyset.                                \tag{5.1}
\]

Corollary 4.3 proves the following exact, non-enumerative dichotomy:

> A rank-two rooted triangle gives a literal `K_7`, unless every
> forbidden-label portal pair supplied by the opposite lobe is, in both
> orientations, a block-terminal web for the unmatched root.

The negative object already has an exact width-one order certificate.

### Lemma 5.1 (spanning-tree projection certificate)

Let `Q` be a spanning tree of `J`, and let

\[
                       x=v_0,v_1,\ldots,v_h=y
\]

be its `x`--`y` path.  For `z in V(J)`, let `pi_Q(z)` be the index of the
unique closest vertex of the `x`--`y` path to `z` in the tree `Q`
(equivalently, the unique vertex of that path lying on both the
`z`--`x` and `z`--`y` paths).  For a nonempty set `A`, put

\[
 ell_Q(A)=\min_{z\in A}pi_Q(z),\qquad
 r_Q(A)=\max_{z\in A}pi_Q(z).
\]

Write `A_l=N_J(t_l)`.  The tree `Q` has an edge whose two components
give a partition satisfying (5.1) if and only if

\[
 ell_Q(A_i)<\min\{r_Q(A_j),r_Q(A_k)\}.                  \tag{5.2}
\]

If neither orientation of `x,y` yields the required partition in `J`,
then **every** spanning tree `Q` satisfies the crossed projection
inequalities

\[
 \ell_Q(A_i)\ge\min\{r_Q(A_j),r_Q(A_k)\},\qquad
 r_Q(A_i)\le\max\{\ell_Q(A_j),\ell_Q(A_k)\}.            \tag{5.3}
\]

Conversely, violation of either inequality in (5.3) by one spanning tree
gives the star split and hence the literal `K_7` of Corollary 4.3.

#### Proof

Every edge separating `x` from `y` is `v_{r-1}v_r` for some
`1<=r<=h`.  Its `x`-side contains a member of `A_i` exactly when
`ell_Q(A_i)<r`.  Its `y`-side contains members of both `A_j,A_k` exactly
when

\[
                         r<=r_Q(A_j),r_Q(A_k).
\]

Such an integer `r` exists exactly under (5.2).  This proves the first
claim.  Applying the same formula after reversing the path exchanges
`ell` with `h-r`; failure in the reverse orientation is precisely the
second inequality in (5.3).

Finally, any connected bipartition of `J` together with one cross edge
and spanning trees of its two sides is a spanning tree of `J` for which
that cross edge is fundamental.  Hence a partition exists in `J` if and
only if some spanning tree displays it. `square`

Thus the negative output is not an unstructured failure of linkage.  It
is a literal crossed order which survives every change of spanning tree.
This is the exact point at which an additional chord must either reverse
the order (giving the split) or belong to the same two-terminal rural
page.  It is a suitable canonical input for a Two-Paths/web theorem.

### Corollary 5.2 (all tree lobes reduce to one crossed path order)

In a `K_7`-minor-free survivor, if the opposite lobe `J` is a tree, then
`J` is a path.  For a rank-two rooted triangle, every fresh portal pair
which violates the crossed inequalities (5.3) on that path gives a
literal `K_7`.  Hence the only surviving tree-lobe state is the single
path order (5.3), simultaneously for both orientations of every fresh
portal pair.

#### Proof

The audited nested-cutvertex exchange says that deletion of any vertex
of a surviving lobe leaves at most two components.  In a tree that number
is the degree of the deleted vertex.  Thus every vertex of `J` has degree
at most two, and connected `J` is a path.  It has only one spanning tree,
so Lemma 5.1 and Corollary 4.3 give the remaining assertions. `square`

This eliminates an unbounded family rather than a bounded order list:
every branching tree lobe and every non-crossed path lobe closes
literally.  The residue is one ordered path society, exactly the object
on which a proper-minor equality-state transfer can be attempted.

This negative alternative is stronger than a generic absence of a
rooted model: it fixes the literal unmatched root, the two fresh portal
vertices, and which two gate-contact classes must coexist on the core
side.  It is the direct block-terminal Two-Paths/web input requested by
the proof spine.

The alternative cannot be deleted using connectivity alone.  For
example, let `J` be the edge `uv`, with

\[
 N_J(t_i)=\{u,v\},\qquad N_J(t_j)=\{u\},\qquad
 N_J(t_k)=\{v\}.
\]

The crossed-arm condition from three-connectivity holds after deleting
either vertex, yet the portal pair `u,v` is a block-terminal web in both
orientations: the core side cannot meet both `t_j` and `t_k` without
using all of `J`.  Thus any unconditional star-split claim would be
false.  In the actual `HC_7` cell this tiny order is not itself a global
counterexample; it identifies the exact place where proper-minor state
transfer must enter.

## 6. Remaining constructive edge

The next theorem now has a narrower, literal input.  In a hypothetical
counterexample, contraction-criticality must exclude the simultaneous
coexistence of:

1. a maximum-rank rooted triangle with one of the two Hall monopolies in
   Section 2; and
2. the opposite lobe being a block-terminal web for every fresh portal
   pair promised by the forbidden-label matching theorem.

The required output is not another portal pattern.  It must show that the
negative web has a canonical adhesion whose proper-minor equality state
matches the opposite shore, or that its canonical median is one fixed
actual vertex and the corresponding median on the other lobe gives the
allowed coherent two-vertex endgame.
