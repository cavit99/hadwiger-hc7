# Predecessor closure of the balanced `|W|=3` cell

**Status:** proved and independently cold-audited in
[`hc7_marked_three_clique_w3_predecessor_closure_audit.md`](hc7_marked_three_clique_w3_predecessor_closure_audit.md).
This closes the balanced `|W|=3` Mader cell when the three marked vertices
are images of an inclusion-minimal three-edge contraction from
seven-connected predecessors.  It does not prove the generic marked
three-clique theorem and does not address the balanced cells `|W|=4,5`.

## 1. Predecessor setting

Let `G` be a graph and let

\[
                    F=\{e_1,e_2,e_3\}              \tag{1.1}
\]

be three pairwise vertex-disjoint edges.  Contract all three edges and
write

\[
                    H=G/F,                          \tag{1.2}
\]

where `z_i` is the image of `e_i`.  For each `a in {1,2,3}`, put

\[
                    H_a=G/(F-\{e_a\}).              \tag{1.3}
\]

Thus `H_a` is obtained from `H` by splitting `z_a` back into the two
ends of the literal edge `e_a`.  Assume that every `H_a` is
seven-connected.

Suppose that `H` satisfies the standing hypotheses of the marked
three-clique problem and that its maximal Mader certificate lies in the
balanced `|W|=3` cell.  In the notation of
[`hc7_marked_three_clique_w3_fan_reduction.md`](hc7_marked_three_clique_w3_fan_reduction.md),

\[
 W=\{z_1,z_2,z_3\},\qquad
 S_i=W\cup B_i                                      \tag{1.4}
\]

is a six-separator, and `H-S_i` has exactly two components.  One of them
is the connected `S_i`-full row packet `P_i`.

The one-mark decoder in
[`hc7_marked_three_clique_w3_one_mark_decoder.md`](hc7_marked_three_clique_w3_one_mark_decoder.md)
gives, for any choice of row `h` and either `a ne h`, a labelled
`K_7^-` model.  If `{a,b,h}={1,2,3}`, its seven bags are

\[
 C_1,C_2,C_3,quad R_a,quad \{z_h\},quad
 D_a=P_a\cup\{z_a\},quad D_b=P_b\cup\{z_b\},       \tag{1.5}
\]

and its only undecided adjacency is

\[
                              R_aD_b.               \tag{1.6}
\]

There is a literal edge from `R_a` to `z_a`: it is the last edge of the
fourth terminalizing path before its endpoint `z_a` was omitted from the
bag `R_a`.

## 2. Expanding a row cut

Write

\[
                              e_a=x_ay_a.           \tag{2.1}
\]

For every row `i`, define

\[
              S_i^a=(S_i-\{z_a\})\cup\{x_a,y_a\}. \tag{2.2}
\]

### Lemma 2.1 (literal expanded-cut fullness)

For every `i`, the set `S_i^a` is a seven-separator of `H_a`, and
`H_a-S_i^a` has the same two open components as `H-S_i`.  Every vertex of
`S_i^a` has a neighbour in each of those two components.  In particular,

\[
 x_a,y_a\in N_{H_a}(P_i)                           \tag{2.3}
\]

for every row `i`.

### Proof

Deleting both ends `x_a,y_a` in `H_a` has exactly the same effect outside
the deleted set as deleting their contracted image `z_a` in `H`.
Consequently `H_a-S_i^a` is naturally identical to `H-S_i`, including its
two component sides.  Thus `S_i^a` is a literal separator of order seven.

The graph `H_a` is seven-connected, so `S_i^a` is a minimum separator.
If a member `s` of `S_i^a` had no neighbour in one open component, then
`S_i^a-\{s\}` would still separate that component, contradicting
seven-connectivity.  This proves fullness at every boundary vertex and,
in particular, (2.3).  \(\square\)

The point of applying Lemma 2.1 to **different** rows is that both split
vertices meet both packets needed below:

\[
 x_a,y_a\in N(P_a)\cap N(P_b).                    \tag{2.4}
\]

The first pair of contacts comes from the expanded cut `S_a^a`, and the
second from `S_b^a`.  Fullness of one expanded cut alone would only put a
neighbour somewhere in its opposite component; it would not identify the
specific packet `P_b`.

## 3. Literal `K_7` after one split

### Theorem 3.1 (balanced-three predecessor closure)

Under the hypotheses in Section 1, `H_a`, and hence `G`, contains a
`K_7` minor.  Therefore the balanced `|W|=3` cell cannot occur in a
`K_7`-minor-free graph arising from the stated minimal-three-contraction
predecessor setting.

### Proof

Choose the name `x_a` in (2.1) so that the last edge from `R_a` to the
contracted vertex `z_a` in `H` lifts to an edge from `R_a` to `x_a` in
`H_a`.  Replace the two bags `R_a,D_a` in (1.5) by

\[
                  \widehat R_a=R_a\cup\{x_a\},
                  \qquad
                  \widehat D_a=P_a\cup\{y_a\}.     \tag{3.1}
\]

Keep the other five bags

\[
                  C_1,C_2,C_3,\quad\{z_h\},\quad D_b.           \tag{3.2}
\]

All seven bags are pairwise disjoint.  The bag `\widehat R_a` is connected
by the chosen lifted last edge.  The bag `\widehat D_a` is connected by
the contact `y_aP_a` from the expanded row cut `S_a^a`.

Every adjacency not involving one of the two changed bags is inherited
from the labelled `K_7^-` model (1.5).  The adjacencies of
`\widehat R_a` are as follows.

* Its adjacencies to `C_1,C_2,C_3` and `{z_h}` are inherited from `R_a`.
* It is adjacent to `\widehat D_a` through the literal split edge
  `x_ay_a`.
* It is adjacent to `D_b` through an edge from `x_a` to `P_b`, supplied
  by the expanded row cut `S_b^a`.

Thus the single missing pair (1.6) has been repaired.  Finally,
`\widehat D_a` retains all old duties of `D_a` without using `x_a`:

* it meets every `C_j` through the `B_a` vertex in `C_j` and the
  `S_a`-full packet `P_a`;
* it meets `{z_h}` because `P_a` has a neighbour at `z_h`;
* it meets `D_b` because `P_a` has a neighbour at `z_b` in `D_b`; and
* it meets `\widehat R_a` through `x_ay_a`.

These account for all twenty-one pairs.  Hence (3.1)--(3.2) are seven
literal connected branch sets forming a `K_7` model in `H_a`.  Since
`H_a` is a minor of `G`, the same is true in `G`.  \(\square\)

## 4. Exact consequence and trust boundary

The proof uses the predecessor information at one precise point: splitting
`z_a` produces a seven-connected graph in which **both** ends of `e_a`
are full at every expanded row cut.  The generic marked quotient does not
provide two literal vertices with those simultaneous packet contacts.

Proved here:

* every balanced `|W|=3` cell in the stated three-edge predecessor setting
  expands to a literal `K_7` model after splitting one mark.

Not proved here:

* the generic six-connected marked three-clique theorem;
* the balanced cells `|W|=4,5`;
* that every occurrence of three marked `K_5` cliques in an arbitrary
  quotient comes from the predecessor setting in Section 1; or
* the global support-six theorem or `HC_7`.
