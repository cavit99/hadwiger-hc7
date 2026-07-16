# One-split predecessor closure of the balanced `|W|=4,5` cells

**Status:** proved and independently cold-audited in
[`hc7_marked_three_clique_w45_predecessor_closure_audit.md`](hc7_marked_three_clique_w45_predecessor_closure_audit.md).

This note continues the balanced marked-three-clique reduction in the
actual minimal-three-contraction setting.  It eliminates both remaining
balanced cells, `|W|=4` and `|W|=5`, by a uniform construction.  A clean
row clique supplies five of seven branch sets, with every extra vertex of
`W` retained as a literal packet-contact carrier.  The resulting model has
only one undecided adjacency, which is repaired by splitting one marked
edge in a seven-connected predecessor.

The same decoder specializes at `|W|=3` to the previously audited
predecessor closure.  It does not close the unbalanced branches of the
marked three-clique argument, the two-edge minimal-contraction branch, the
global support-six theorem, or `HC_7`.

## 1. Standing balanced cell

Let `G` be a graph containing three pairwise vertex-disjoint edges

\[
                         e_i=x_i y_i\qquad(i=1,2,3),             \tag{1.1}
\]

put

\[
 H=G/\{e_1,e_2,e_3\},\qquad
 H_i=G/\{e_j:j\ne i\},                                         \tag{1.2}
\]

and write `z_i` for the image of `e_i` in `H`.  Assume every `H_i` is
seven-connected.  Suppose `H` is six-connected and `K_7`-minor-free,
contains three pairwise disjoint literal cliques

\[
                         L_i=Q_i\cup\{z_i\}\cong K_5,            \tag{1.3}
\]

and every six-separator of `H` contains `z_1,z_2,z_3`.

Assume a maximal Mader certificate lies in the balanced equality cell with

\[
                         w:=|W|\in\{4,5\},\qquad m=6-w.          \tag{1.4}
\]

Thus `W` contains all three marks, there are `m` large cells
`(Y_j,X_j)` with `|X_j|=3`, and there are three disjoint rows `B_i` of
order `m` which partition the `X_j`.  Every row has a nonempty tail.  Put

\[
                         S_i=W\cup B_i.                           \tag{1.5}
\]

As in the audited `|W|=3` reduction, `H-S_i` has exactly two components.
The component on the row side is

\[
                         P_i=A_i-B_i,                             \tag{1.6}
\]

and

\[
                         N_H(P_i)=S_i.                            \tag{1.7}
\]

The three `P_i` are pairwise disjoint and anticomplete.

### Lemma 1.1 (row--cell incidence and connected cells)

For every `i` and `j`,

\[
                         |B_i\cap X_j|=1,                         \tag{1.8}
\]

and every `H[Y_j]` is connected.  Moreover,

\[
                         P_i\cap Y_j=\varnothing.                 \tag{1.9}
\]

### Proof

For `w=5`, both `m` and every `|B_i|` equal one, so (1.8) is immediate.
For `w=4`, fix `i,j` and suppose `r=|B_i\cap X_j|\ge2`.  Then

\[
 T=W\cup(B_i\mathbin\triangle X_j)
\]

has order

\[
 |T|=w+|B_i|+|X_j|-2r=9-2r\le5.                                 \tag{1.10}
\]

The standard symmetric-difference shore

\[
 (B_i\cap X_j)\cup P_i\cup(Y_j-X_j)
\]

has neighbourhood contained in `T`: the row packet can leave only through
`W\cup B_i`, the cell interior can leave only through `W\cup Y_j`, and
an edge from `B_i\cap X_j` to another cell remains in the auxiliary graph
defining `A_i`, hence stays in `(B_i-X_j)\cup P_i`.  A vertex of another
row in the other large cell survives outside this shore and `T`.  This
contradicts six-connectivity.  Thus every intersection has order at most
one.  Each row has `m` vertices distributed among `m` three-sets, so all
intersections have order one.

If `H[Y_j]` were disconnected, refine `Y_j` into its graph components and
split `X_j` accordingly.  The Mader boundary and terminal conditions are
preserved componentwise, every old cell-internal witness edge remains
inside one new component, and

\[
 \sum_C\left\lfloor {|X_j\cap C|\over2}\right\rfloor
 \le \left\lfloor {|X_j|\over2}\right\rfloor=1.
\]

The refinement preserves the budget and strictly increases the secondary
cell count, contrary to maximality.  (A component with empty `X_j`-trace
would in addition have neighbourhood contained in `W`, impossible in a
six-connected graph when `w\le5`.)  Hence every cell is connected.

Finally, in the auxiliary graph defining `A_i`, every edge internal to a
cell is deleted.  A vertex of `Y_j-X_j` has no edge outside `W\cup Y_j`
and is therefore isolated after `W` and the cell-internal edges are
deleted.  It cannot lie in an auxiliary component meeting `L_i-W`; all
clique vertices in `Y_j` belong to `X_j`.  The only vertices of `A_i` in
the large cells are therefore the members of `B_i`, proving (1.9).
\(\square\)

## 2. A uniform four-path decoder

Put

\[
                         E=W-\{z_1,z_2,z_3\},\qquad k=|E|=w-3.  \tag{2.1}
\]

Since `k\le2` and the three cliques `L_i` are disjoint, some index `h`
satisfies

\[
                         E\cap L_h=\varnothing.                  \tag{2.2}
\]

Consequently `W\cap L_h=\{z_h\}` and the whole four-clique
`Q_h=L_h-z_h` lies in `P_h\cup B_h`.  Write
`\{a,b,h\}=\{1,2,3\}` and define

\[
                         T_h=B_h\cup E\cup\{z_a\}.              \tag{2.3}
\]

Its order is

\[
                         |T_h|=(6-w)+(w-3)+1=4.                 \tag{2.4}
\]

### Lemma 2.1 (localized four-path linkage)

There are four pairwise vertex-disjoint paths with distinct initial
vertices equal to the four vertices of `Q_h` and distinct final vertices
equal to the four vertices of `T_h`.  Every nontrivial path has all
internal vertices in `P_h`.

### Proof

Work in

\[
                         H-\{z_h,z_b\},                          \tag{2.5}
\]

which is four-connected.  Take the trivial path at every vertex of
`I=Q_h\cap B_h`.  After deleting `I`, set-Menger gives `4-|I|`
disjoint paths from `Q_h-I` to `T_h-I`, with distinct starts and ends.
Shorten every path at its first vertex in `T_h`.

A nontrivial initial vertex lies in `Q_h-B_h\subseteq P_h`.  The only
neighbours of `P_h` outside `P_h` lie in
`S_h=W\cup B_h`.  After deleting `z_h,z_b`, that boundary is exactly
`B_h\cup E\cup\{z_a\}=T_h`.  The shortened path consequently has all
internal vertices in `P_h`.  The four disjoint ends exhaust the four-set
`T_h`.  \(\square\)

For each large cell `Y_j`, let `b_{hj}` be its unique member of `B_h`.
Absorb the path ending at `b_{hj}` into `Y_j`, and call the resulting
connected bag `C_j`.  By (1.9), its only intersection with `Y_j` is its
final vertex.  For each `e\in E`, keep the final vertex `e` in its path
bag and call the bag `R_e`.  From the path ending at `z_a`, omit only its
final vertex and call the remaining connected bag `R_a`.

These

\[
                         C_1,\ldots,C_m,\quad
                         (R_e:e\in E),\quad R_a                 \tag{2.6}
\]

are four pairwise disjoint connected bags.  They contain the four distinct
initial vertices of the clique `Q_h`, so they are pairwise adjacent.  Each
is adjacent to the singleton bag `\{z_h\}` through its initial vertex.
Thus (2.6) together with `\{z_h\}` is a literal `K_5` model.

Put

\[
                         D_c=P_c\cup\{z_c\}\qquad(c=a,b).       \tag{2.7}
\]

### Lemma 2.2 (the sole-defect model)

The seven bags

\[
 C_1,\ldots,C_m,\quad (R_e:e\in E),\quad R_a,\quad
 \{z_h\},\quad D_a,D_b                                      \tag{2.8}
\]

have every pairwise adjacency except possibly

\[
                              R_aD_b.                            \tag{2.9}
\]

### Proof

The five bags consisting of (2.6) and `\{z_h\}` form a clique model as
just observed.  The two packet bags are connected.  They are adjacent to
one another because `P_a` has a neighbour at `z_b`, and each is adjacent
to `\{z_h\}` by fullness at `z_h`.

For every large cell `j` and `c\in\{a,b\}`, the row vertex
`b_{cj}\in B_c\cap X_j` lies in `C_j`, and fullness of `P_c` at
`b_{cj}` supplies the edge `D_cC_j`.  For every `e\in E`, the bag `R_e`
contains the literal vertex `e`; fullness of both `P_a` and `P_b` at `e`
supplies `D_aR_e` and `D_bR_e`.  Finally, the last edge of the path ending
at `z_a` supplies `R_aD_a`.  This lists all pairs other than (2.9).
\(\square\)

The key point is that an extra member of `W` is not discarded as a fan
endpoint.  Retaining it in its path bag makes it a simultaneous literal
contact to both outside row packets.

## 3. Splitting one mark repairs the sole defect

Write `e_a=x_ay_a`, naming `x_a` so that the last edge from `R_a` to the
contracted vertex `z_a` lifts in `H_a` to an edge from `R_a` to `x_a`.
For every row `i`, put

\[
             S_i^a=(S_i-\{z_a\})\cup\{x_a,y_a\}.                \tag{3.1}
\]

Exactly as in the audited `|W|=3` predecessor closure, `S_i^a` is an
order-seven separator in `H_a`, with the same two open components as
`H-S_i`.  Since `H_a` is seven-connected, every boundary vertex has a
neighbour in both open components.  In particular,

\[
                         x_a,y_a\in N_{H_a}(P_i)                 \tag{3.2}
\]

for every row `i`.

### Theorem 3.1 (balanced-four/five predecessor closure)

Under the hypotheses in Section 1, `H_a`, and hence `G`, contains a
`K_7` minor.

### Proof

In (2.8), replace

\[
                         R_a\longmapsto
                         \widehat R_a=R_a\cup\{x_a\},
 \qquad
                         D_a\longmapsto
                         \widehat D_a=P_a\cup\{y_a\}.           \tag{3.3}
\]

Keep every other bag, including `D_b=P_b\cup\{z_b\}`.  The seven bags
remain pairwise disjoint.  The lifted last edge makes `\widehat R_a`
connected, and `y_aP_a` from (3.2) makes `\widehat D_a` connected.

Here is the complete adjacency check.

* The five core bags in (2.6) together with `\{z_h\}` retain all ten
  mutual adjacencies from the clique `Q_h` and the edges `z_hQ_h`.
* `D_b` retains its adjacency to every core bag, to `\{z_h\}`, and to
  `\widehat D_a`, all through `P_b` or the retained vertex `z_b`.
* `\widehat D_a` retains every old duty of `D_a` without using `x_a`:
  it meets `C_j` through `P_a b_{aj}`, meets every `R_e` through
  `P_a e`, meets `\{z_h\}` through `P_a z_h`, and meets `D_b` through
  `P_a z_b`.
* `\widehat R_a` retains its adjacencies to every other core bag and to
  `\{z_h\}` from `R_a`.  The split edge `x_ay_a` gives its adjacency to
  `\widehat D_a`, while the contact `x_aP_b` from (3.2), applied to row
  `b`, repairs the sole missing pair `R_aD_b`.

These account for all twenty-one pairs.  Hence the seven sets are a
literal `K_7` model in `H_a`.  Since `H_a` is a minor of `G`, the same is
true in `G`.  \(\square\)

## 4. Consequence and trust boundary

Together with the independently audited `|W|=3` predecessor closure, this
eliminates every balanced equality cell `3\le|W|\le5` in the actual
inclusion-minimal three-edge contraction branch.  In fact the proof is one
uniform decoder: in all three cases, the row boundary other than
`z_h,z_b` has four vertices, and every non-cell endpoint retained from
`W-\{z_1,z_2,z_3\}` is automatically a two-packet carrier.  Only one
marked endpoint transfer is needed.

This does **not** prove that the full marked three-clique argument always
reaches a balanced equality cell.  It also does not treat an abstract
six-connected marked quotient lacking seven-connected split predecessors,
or a minimal bad contraction set of order two.
