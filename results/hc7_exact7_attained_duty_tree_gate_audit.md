# Independent hostile audit: attained-duty tree split or gate

Audited file: `results/hc7_exact7_attained_duty_tree_gate.md`.

## Verdict

**GREEN.**  Theorem 3.1 and Corollary 3.2 are correct with the current
duty-specific portal convention.  The result is a local exchange theorem:
for every selected witness system and packet tree, nonreflection forces a
literal common vertex of the three selected duty hulls.  It does not make
that vertex canonical, a separator, or an apex.

The duty-specific sharpening is material and correctly implemented.  If a
literal retained singleton occurs in two duties, its witnesses in those
duties may be different packet vertices.  Nothing in the proof identifies
them.

## 1. State count and duty identity

Let `C` be a maximum clique among singleton blocks of the exact boundary
partition `Pi`.  Since

\[
                         |\Pi|-|C|=3,
\]

exactly three blocks of `Pi` are not represented by the retained literal
singletons in `C`.  This remains true when one or more of those three blocks
is itself a singleton outside `C`.

For such a block `B_i`, the displayed duty

\[
 D_i=B_i\cup\{c\in C:N_H(c)\cap B_i=\varnothing\}
\]

is exactly the contact requirement used by the labelled carrier-reflection
lemma:

* contact with every member of `B_i` makes `X union B_i` connected, because
  `X` is connected and every boundary member has an edge to `X`; and
* for `c in C`, the funded representative sees `c` through a literal
  `c-B_i` edge when one exists, and otherwise through the required
  `c-X` contact.

No unconditional support-size or defect assertion is substituted for this
partition-dependent duty.

## 2. Witnesses, tree hulls, and quantifiers

For each ordered pair `(i,s)` with `s in D_i`, the proof selects a witness
`p_i(s)`.  Thus two duties containing the same boundary label need not use
the same portal.  A tree in the connected packet contains the finite union
of all selected witnesses, and the minimal subtree spanning the witnesses
of a nonempty duty is well-defined and nonempty.

The theorem is valid for **every** such selected witness system and every
tree containing it.  Consequently, if reflection is impossible, every
selection has a common hull vertex.  The vertex may change after changing
the witnesses or the tree.  Corollary 3.2 makes only the safe existential
selection in each of the two disjoint packets and does not assert a common
choice across them.

## 3. The tree split

Assume `K_i` and `K_j` are disjoint.  Their unique joining path in the tree
has endpoints `u in K_i` and `v in K_j`.  Deleting any oriented edge `xy`
of that path separates

\[
 X=K_i\cup uTx,
 \qquad
 Y=K_j\cup yTv
\]

into nonempty, connected, vertex-disjoint sets joined by the literal edge
`xy`.  They retain every selected witness for `D_i` and `D_j`, respectively.
There is no requirement that they avoid the third selected hull, because
the third duty is funded in the other full packet.

Let `Q` be that other packet.  The three branch sets

\[
 X\cup B_i,\qquad Y\cup B_j,\qquad Q\cup B_k
\]

are connected and pairwise disjoint.  The first two are adjacent through
`xy`.  Fullness of `Q` supplies an edge from `Q` to a literal member of each
nonempty block `B_i,B_j`, so the third set is adjacent to the first two.
The duty identity verifies adjacency from the first two representatives to
every `c in C`, and fullness verifies it for the third.  Finally `C` is a
literal clique.  Hence these representatives and `C` form a clique indexed
by all blocks of `Pi`.

## 4. Proper contraction and exact pullback

The contracted sets are disjoint connected sets and contain nonempty
rich-shore vertices, so the resulting graph is a proper minor.  Strong
contraction-criticality supplies a six-colouring.

On expanding only the untouched thin closed shore:

* all vertices in each `B_i` inherit the colour of its representative;
* different blocks inherit different colours because all block
  representatives form a clique; and
* expansion is proper because every equality block of the returned state is
  independent and there are no edges between the two open shores.

The induced equality partition on literal `S` is therefore exactly `Pi`,
not merely a coarsening.  Its palette can be permuted to match the original
thin-operation colouring on the rich closed shore, and the two colourings
glue across `S`.

## 5. Helly gate

If reflection is impossible, no pair of hulls is disjoint.  For three
pairwise-intersecting subtrees of a tree, choose

\[
 x\in K_1\cap K_2,
 \quad y\in K_1\cap K_3,
 \quad z\in K_2\cap K_3.
\]

Their tree median lies on `xTy`, `xTz`, and `yTz`.  These paths lie in
`K_1`, `K_2`, and `K_3`, respectively, so the median is a literal common
vertex.  Applying this independently in the two disjoint packets gives two
distinct literal gates.

## Trust boundary

The audit does **not** promote the proposed bypass-or-coherence target.
A bridge avoiding a selected gate need not respect the cyclic order of the
three labelled duties, and neither the theorem nor Helly supplies a
label-compatible rerouting.  That obstruction is realized concretely in
`barriers/hc7_exact7_gate_bypass_falsifier.md` and audited separately.
