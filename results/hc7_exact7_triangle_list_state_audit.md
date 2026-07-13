# Independent audit: exact-seven spanning-triangle list-state theorem

## Verdict

**GREEN.**  Theorem 1.1 is a valid proper-minor state-synchronization
argument.  Both contractions are literal, both expanded colourings are
proper, the equality partition on the seven boundary vertices is exact,
and a partial bijection between the used block colours extends to a
permutation of the six-colour palette.  The entry construction (5.1) is
also valid.  Two explanatory sentences in Section 5 were tightened, but
no hypothesis or conclusion changed.

## 1. Carrier-side contraction

Put `I_i=phi^{-1}(i)`.  Properness of `phi` says exactly that every `I_i`
is independent.  The list condition says that every vertex of `I_i` has
a literal neighbour in the nonempty connected carrier `C_i`; hence

\[
                         A_i=C_i\cup I_i
\]

is connected, including when `I_i` is empty.  The three sets are disjoint
and cover `L\cup S`.  Because `S` is nonempty, at least one `I_i` is
nonempty and its `A_i` contains at least two vertices.  Contracting the
three connected sets therefore strictly lowers the vertex count and
produces a proper minor.

The images `a_1,a_2,a_3` form a literal clique: each pair of original
carriers is adjacent.  Consequently the images corresponding to distinct
nonempty blocks have distinct colours.  On restricting the minor
colouring to `R` and assigning every `s\in I_i` the colour of `a_i`, all
edge types are safe:

* `I_i` has no internal edge;
* boundary edges between distinct blocks have differently coloured ends;
* every original `sR` edge became an `a_iR` edge in the minor.

Thus this expansion properly colours `G[R\cup S]`.  Two boundary vertices
have the same colour exactly when they belong to the same nonempty `I_i`,
so the induced equality partition is exact.  Empty `I_i` contribute no
boundary block and cause no issue.

## 2. Packet-side contraction

There are at most three nonempty blocks, so they can be assigned injectively
to the three disjoint `S`-full packets.  For each such block,

\[
                         D_i=P_i\cup I_i
\]

is connected because every literal member of `I_i` has a neighbour in
`P_i`.  It is nontrivial because both terms are nonempty.  The `D_i` are
disjoint, so contracting them produces a proper minor.

For distinct nonempty blocks `I_i,I_j`, fullness of `P_i` at every member
of `I_j` gives a literal edge from `D_i` to `D_j`.  Hence all contracted
vertices `d_i` form a clique and receive distinct colours.  Restricting
the minor colouring to `L` and expanding `I_i` with the colour of `d_i`
is proper: independence handles edges inside a block, the clique handles
edges between blocks, and every `sL` edge was represented by a `d_iL`
edge.  The resulting colouring of `G[L\cup S]` therefore induces the
same exact boundary equality partition.

No packet is allocated to an empty block.  In particular, the proof never
needs two unused packets to be adjacent.

## 3. Palette alignment and gluing

Each side uses one distinct colour per nonempty boundary block.  The map
from the block colours on one side to those on the other is an injection
between two equally sized subsets of the six-colour palette and extends
to a permutation of all six colours.  After applying it, the two
colourings agree at every literal vertex of `S`.  The open shores are
anticomplete, so their union is a proper six-colouring of `G`.

This verifies that the proof does not identify pre-existing colour names
with model bags.  Both matching equality states are manufactured by
proper-minor contractions and aligned only afterward.

## 4. Entry construction and boundary clique number

Let `(B_1,B_2,B_3)` be a `T`-rooted triangle in one lobe `K`, extended
to a spanning partition of `K\cup T`.  Such an extension is legitimate:
successively absorb each component outside the current model into any
adjacent bag; connectedness is preserved and the old pairwise
adjacencies remain.

The other lobe `J` is connected and meets every literal gate vertex.
Since `t_1\in B_1`, a literal `Jt_1` edge makes

\[
 C_1=B_1\cup J,\qquad C_2=B_2,\qquad C_3=B_3
\]

a spanning partition of `L` into three nonempty connected pairwise
adjacent carriers.  The more flexible star split is also compatible with
Theorem 1.1 after its core is absorbed into any adjacent one of the three
rooted carriers.

Finally, seven-connectivity forces connected `L` to be `S`-full: if a
literal `s\in S` had no neighbour in `L`, then at most the other six
boundary vertices would separate nonempty `L` from nonempty `R`.  Thus
all lists are nonempty.  Since `L` contains one full packet and `R`
contains three, the audited exact-seven packet theorem forces packing
vector `(1,3)` and

\[
                         \omega(G[S])\le6-(1+3)=2.
\]

Hence the boundary is triangle-free.  The final stated residue--an
uncolourable nonempty three-palette list assignment for every legal
spanning triangle-carrier choice--follows exactly, without claiming that
such a list assignment is itself impossible.

## 5. Scope

The theorem is a reusable sufficient condition, not yet a closure of the
two-lobe cell.  The remaining task is to use legal arm/core or branch-bag
exchanges to force a proper list-colouring, or to extract a compatible
minor state or fixed two-vertex endgame.  This audit assumes none of those
unproved steps.
