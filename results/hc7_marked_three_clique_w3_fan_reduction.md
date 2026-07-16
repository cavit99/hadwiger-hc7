# The balanced `|W|=3` cell: a literal `K_6` and the reserved-hub gap

**Status:** proved local reduction, independently cold-audited in
[`hc7_marked_three_clique_w3_fan_reduction_audit.md`](hc7_marked_three_clique_w3_fan_reduction_audit.md).
The row--cell incidence lemma, three-fan construction, and literal `K_6`
decoder below are proved.  They reduce the abstract balanced `|W|=3` cell
to one standard local question about a three-fan with a connected reserved
hub.  That assertion is not proved here.  In the actual minimal-three-
contraction branch, the separate predecessor-splitting theorem closes the
cell without assuming it.

## 1. Standing equality cell

Let `H` be six-connected and `K_7`-minor-free.  Suppose that it contains
pairwise disjoint cliques

\[
                         L_1,L_2,L_3\cong K_5
\]

with prescribed vertices `z_i in L_i`, and assume

\[
 T\text{ a six-separator of }H
 \quad\Longrightarrow\quad
 \{z_1,z_2,z_3\}\subseteq T.                    \tag{1.1}
\]

Use the maximal Mader certificate and the notation from
[`hc7_marked_three_clique_cut_reduction.md`](../active/hc7_marked_three_clique_cut_reduction.md).
In the balanced equality cell with `|W|=3`, Section 4 of that note gives

\[
 W=\{z_1,z_2,z_3\},\qquad m=3,\qquad
 |X_1|=|X_2|=|X_3|=3,                            \tag{1.2}
\]

\[
 |B_1|=|B_2|=|B_3|=3,\qquad
 X_1\mathbin{\dot\cup}X_2\mathbin{\dot\cup}X_3
 =B_1\mathbin{\dot\cup}B_2\mathbin{\dot\cup}B_3, \tag{1.3}
\]

and every row has a nonempty tail `A_i-B_i`.

Put

\[
                         S_i=W\cup B_i.           \tag{1.4}
\]

The source separation says that `S_i` separates `A_i-B_i` from
`V(H)-A_i-W`.  Both sides are nonempty.  The binary-cut corollary in the
cut-reduction note therefore shows that `H-S_i` has exactly two
components.  Consequently

\[
                         P_i:=A_i-B_i              \tag{1.5}
\]

is one connected component and

\[
                         N_H(P_i)=S_i.             \tag{1.6}
\]

Indeed, more than one component in `A_i-B_i` would give at least three
components of `H-S_i`, and every vertex of a minimum separator has a
neighbour in each component.  The three `P_i` are pairwise disjoint and
pairwise anticomplete.  This also follows directly from the three source
separations.

## 2. Exact row--cell incidence

### Lemma 2.1

For every `i,j in {1,2,3}`,

\[
                            |B_i\cap X_j|=1.       \tag{2.1}
\]

Moreover, every large cell `H[Y_j]` is connected.

### Proof

Fix `i,j` and let `r=|B_i cap X_j|`.  If `r>=2`, put

\[
                      T=W\cup(B_i\mathbin\triangle X_j).        \tag{2.2}
\]

Put

\[
 Z=(B_i\cap X_j)\cup P_i\cup(Y_j-X_j).           \tag{2.3}
\]

Then

\[
                         N_H(Z)\subseteq T.         \tag{2.4}
\]

Here is the direct edge check.  By (1.6), after deleting
`W union (B_i-X_j)`, a vertex of
`P_i` can leave only through `B_i cap X_j`.  The Mader cell axiom gives

\[
              N_H(Y_j-X_j)\subseteq W\cup Y_j,    \tag{2.5}
\]

so after deleting `W union (X_j-B_i)` the cell interior can also leave
only through `B_i cap X_j`.  Finally, an edge from `B_i cap X_j` to a
different cell survives in the auxiliary graph used to define the
`A`-rows.  Its other endpoint therefore lies in the same `A_i`, hence in
`(B_i-X_j) union P_i`.

The set `Z` is nonempty.  A vertex survives outside `Z union T` because
`X_j-B_i` has at most one vertex when `r>=2`, whereas the other two rows
contain six vertices in total.  But

\[
 |T|=3+3+3-2r=9-2r\le5,                           \tag{2.6}
\]

contrary to six-connectivity.  Thus every intersection has order at most
one.  Each `B_i` has three vertices distributed over the three `X`-sets,
so every intersection has order exactly one.  Write

\[
                         B_i\cap X_j=\{x_{ij}\}.  \tag{2.7}
\]

For connectivity, suppose that `H[Y_j]` has at least two components and
split `Y_j` into those components, splitting `X_j` accordingly.  The
Mader boundary and terminal conditions remain valid, every cell-internal
edge witnessing a good path remains internal to one new cell, and

\[
 \sum_C\left\lfloor {|X_j\cap C|\over2}\right\rfloor
 \le \left\lfloor {|X_j|\over2}\right\rfloor=1.   \tag{2.8}
\]

The Mader boundary condition remains true componentwise.  A component
whose `X_j`-trace were empty would have all its neighbours in `W`, which
is impossible by six-connectivity; in any case all new `Y`-cells are
nonempty.  Thus the refinement preserves the budget and strictly
increases the number of nonempty cells, contrary to the secondary
maximality of the certificate.  Hence `H[Y_j]` is connected.  \(\square\)

## 3. A three-fan which terminalizes all columns

Put

\[
                         Q_i=L_i-z_i\cong K_4.     \tag{3.1}
\]

Since `L_i-W subseteq A_i`, equations (1.3) and (1.5) give

\[
                         Q_i\subseteq B_i\cup P_i. \tag{3.2}
\]

In particular `Q_i-B_i` is nonempty.

### Lemma 3.1 (terminalizing three-fan)

Fix a row `h`.  There are three pairwise vertex-disjoint paths
`R_1,R_2,R_3` in `H[P_h union B_h]` such that

* `R_j` has one end `x_{hj}`;
* the other ends are three distinct vertices of `Q_h`;
* `R_j-B_h subseteq P_h`; and
* there is a vertex

  \[
                              q_0\in Q_h\cap P_h   \tag{3.3}
  \]

  which lies on none of the three paths.

### Proof

The graph `J=H-W` is three-connected.  Put `I=Q_h cap B_h` and first use
the trivial one-vertex path at each member of `I`.  The graph `J-I` is
`(3-|I|)`-connected.  Set-Menger therefore gives `3-|I|` disjoint paths
from `Q_h-I` to `B_h-I`, with distinct starts and ends.  Orient each path
from `Q_h-I` and shorten it at its first vertex of `B_h`.  Since `P_h` is
a component of `J-B_h`, all its internal vertices then lie in `P_h`.

Choose the paths with minimum total length.  No nontrivial path contains
a second vertex of `Q_h`: otherwise it can be shortened from the last such
vertex before its `B_h`-end.  The three paths consequently use exactly
three vertices of the four-clique `Q_h`.  The unused vertex is not in
`B_h`, because every member of `I` was used as a trivial path.  Thus it is
the required `q_0 in Q_h cap P_h`.  Relabel the paths by their three
`B_h`-ends `x_{h1},x_{h2},x_{h3}`.  \(\square\)

For this fixed row, define

\[
                         E_j=H[Y_j\cup V(R_j)].    \tag{3.4}
\]

The path interior lies in `P_h subseteq A_h-B_h`, hence in the union of
the singleton `X`-cells, while `Y_j` is one of the three large cells.
Thus `P_h cap Y_j=emptyset`; the only overlap between `R_j` and `Y_j` is
its endpoint `x_{hj}`.

The three subgraphs `E_j` are pairwise vertex-disjoint and connected.
They are pairwise adjacent, because their three `Q_h` ends are distinct
vertices of the clique `Q_h`.  Each `E_j` is adjacent to `z_h`, again
through its `Q_h` end.  For `i ne h`, it is adjacent to `P_i`, since it
contains `x_{ij}` and `P_i` is `S_i`-full.

### Theorem 3.2 (unconditional literal `K_6`)

Every balanced `|W|=3` cell contains a literal `K_6` model.

### Proof

Let `{a,b,h}={1,2,3}` and use the fan from Lemma 3.1.  The six branch
sets

\[
 P_a\cup\{z_a\},\qquad P_b\cup\{z_b\},\qquad
 \{z_h\},\qquad V(E_1),\quad V(E_2),\quad V(E_3) \tag{3.5}
\]

are disjoint and connected.  The first three are pairwise adjacent:
`z_a` has a neighbour in `P_b`, while `z_h` has a neighbour in each of
`P_a,P_b`.  The last three are pairwise adjacent by the `Q_h` clique.
Every `E_j` contacts `P_a union {z_a}` through `x_{aj}`, contacts
`P_b union {z_b}` through `x_{bj}`, and contacts `{z_h}` through its
`Q_h` endpoint.  These are all fifteen adjacencies, so (3.5) is a literal
`K_6` model.
\(\square\)

## 4. Exact seventh-bag decoder

Let

\[
 F_h=P_h\cap\bigl(V(R_1)\cup V(R_2)\cup V(R_3)\bigr),           \tag{4.1}
\]

and let `C_h` be the component of `H[P_h-F_h]` containing the unused
vertex `q_0`.  This component exists by Lemma 3.1.  It is adjacent to all
three `E_j`, because `q_0` is adjacent to their three distinct `Q_h`
ends, and it is adjacent to `z_h` through the edge `q_0z_h`.

### Theorem 4.1 (reserved-hub decoder)

If, for some row `h` and some three-fan from Lemma 3.1,

\[
                  \{z_a,z_b\}\subseteq N_H(C_h),
                  \qquad \{a,b,h\}=\{1,2,3\},                  \tag{4.2}
\]

then `H` has a literal `K_7` minor.

### Proof

Add `C_h` to the six bags in (3.5).  It contacts `{z_h}` and all three
column bags as observed above.  It contacts `P_a union {z_a}` and
`P_b union {z_b}` through the two edges guaranteed by (4.2).  These seven
bags form a `K_7` model.  \(\square\)

### Corollary 4.2 (a row with three boundary terminals closes)

If

\[
                         |Q_h\cap B_h|=3            \tag{4.3}
\]

for some row `h`, then `H` has a `K_7` minor.  Consequently every live
`K_7`-minor-free cell satisfies

\[
                         |Q_i\cap B_i|\le2
                         \qquad(i=1,2,3).           \tag{4.4}
\]

### Proof

Under (4.3), the three paths in Lemma 3.1 are the three trivial paths at
`B_h cap Q_h`.  The unused fourth vertex `q_0` lies in `P_h`, and
`C_h=P_h`.  Equation (1.6) says that `P_h` has a neighbour at both marked
vertices in `W-z_h`, so Theorem 4.1 applies.  \(\square\)

Thus a `K_7`-minor-free balanced `|W|=3` cell must satisfy the following
precise obstruction in **every** row:

> For every terminalizing three-fan, the component containing the unused
> fourth vertex of `L_h-z_h` misses at least one of the other two marked
> vertices.

This is a local linkage statement in a three-connected graph behind a
literal three-cut.  It no longer mentions the Mader cell labels except for
the three boundary terminals.

## 5. A strict local gate shift

The failure of even a two-arm version of the required fan has a standard
and well-founded separator consequence.

### Lemma 5.1 (two-fan or inward three-cut)

Fix a row `i`, let `b in B_i-Q_i`, and put

\[
                         K=Q_i\cap P_i.             \tag{5.1}
\]

Thus `|K|>=2` by (4.4).  At least one of the following holds.

1. In `J-(B_i-\{b\})`, where `J=H-W`, there are two internally
   vertex-disjoint paths from `b` to two distinct vertices of `K`.
2. There is a vertex `p in P_i` such that

   \[
                   (B_i-\{b\})\cup\{p\}             \tag{5.2}
   \]

   is a three-separator of `J`.  The component on the `K-\{p\}` side is
   contained strictly in `P_i`.

In outcome 2,

\[
             W\cup(B_i-\{b\})\cup\{p\}             \tag{5.3}
\]

is a literal six-separator of `H`, and `H` minus this separator has exactly
two components.

### Proof

Write `B_i=\{b,c,d\}`.  The graph `J-\{c,d\}` is connected because `J`
is three-connected.  Apply the two-fan form of Menger's theorem from `b`
to the set `K`.  If the two-fan does not exist, a single vertex `p ne b`
separates `b` from `K-\{p\}` in `J-\{c,d\}`.  The set `K-\{p\}` is
nonempty because `|K|>=2`.

There is a `b`--`K` path contained in `H[P_i union \{b\}]`: the packet
`P_i` is connected, `b` has a neighbour in it by (1.6), and `K subseteq
P_i`.  Hence a vertex meeting every such path lies in `P_i`; in
particular `p in P_i`.  It follows directly that (5.2) separates `b`
from `K-\{p\}` in `J`.  The component containing `K-\{p\}` is contained
in `P_i-p`, and is therefore a strict subgraph of the old open packet.

Adding back the deleted set `W` proves that (5.3) is a six-separator of
`H`.  It contains all three marks, and the binary-cut corollary gives the
last assertion.  \(\square\)

Lemma 5.1 is a genuine order-decreasing rooted-packet handoff, with rank

\[
                  \rho(P_i,Q_i)=|V(P_i)|.           \tag{5.4}
\]

The new clique-side component has strictly smaller rank.  The handoff
retains the literal set `W`, the two named vertices `B_i-\{b\}`, and the
whole four-clique `Q_i` in the new closed shore: the vertices of
`Q_i cap B_i` lie among the two retained old gates, while `Q_i cap P_i`
lies in the new gate `p` or its clique-side component.  Since (5.3) is a
minimum cut, that new component is full to the new six-boundary.

What the handoff does **not** preserve is the full Mader row--cell state.
The new gate vertex `p` need not be a named clique vertex, the discarded
nonterminal `b` carried one old column identity, and the two retained
members of `B_i` do not by themselves carry all three old column duties.
It may therefore be iterated only in an argument whose state consists of
the closed-shore `K_4`, the two retained literal gates, and the strict rank
(5.4), rather than the original `3 by 3` incidence matrix.

## 6. Connectivity inside a tail

The marked-cut law gives more than mere fullness.  It prevents a component
behind one or two internal gates from losing too many of the three marked
contacts.

### Lemma 6.1 (marked tail torso)

Fix a row `i` and abbreviate `P=P_i`, `B=B_i`.  Then:

1. for every `p in P`, every component of `P-p` has a neighbour at each
   vertex of `W`;
2. for every two vertices `p,q in P`, every component of `P-\{p,q\}` has
   neighbours at at least two vertices of `W`;
3. `H[P union W]` is two-connected; and
4. the torso obtained from `H[P union W]` by completing `W` to a triangle
   is three-connected.

### Proof

Let `D` be a component of `P-p`.  If it misses some mark, then

\[
              B\cup\{p\}\cup N_W(D)               \tag{6.1}
\]

is a separator of order at most six: inside `P`, the component `D` can
leave only through `p`, and outside `P` it can leave only through
`W union B`.  If (6.1) has order at most five it contradicts
six-connectivity; if it has order six it omits a mark and contradicts
(1.1).  This proves assertion 1.

Similarly, if `D` is a component of `P-\{p,q\}` with at most one marked
neighbour, then

\[
              B\cup\{p,q\}\cup N_W(D)             \tag{6.2}
\]

has order at most six and gives the same contradiction.  This proves
assertion 2.

For assertion 3, deleting a vertex of `W` leaves the connected packet `P`
and the other two marks attached to it.  After deleting `p in P`, every
component of `P-p` sees both of any two remaining marks by assertion 1,
so all components and all three marks lie in one component.

For assertion 4, complete `W` to a triangle.  After deleting two vertices
of `P`, assertion 2 says that every remaining component of `P` attaches
to at least two vertices of the triangle, hence all are connected through
`W`.  After deleting one vertex of `P` and one of `W`, assertion 1 gives
the same conclusion.  After deleting two vertices of `W`, the remaining
mark attaches to the connected packet `P` by (1.6).  Thus deletion of any
two vertices leaves the torso connected.  \(\square\)

The triangle edges in this torso are virtual.  Lemma 6.1 must therefore
not be used as though `W` were a literal clique.  A rooted minor using a
virtual edge has to be lifted through disjoint material in the opposite
shore.  The lemma is nevertheless a standard three-connected setting for
attacking the reserved-hub fan by rooted-linkage or bridge methods.

## 7. The remaining local lemma and trust boundary

The exact sufficient statement left by Theorem 4.1 is the following.

### Reserved-hub three-fan lemma (open)

In the setting above, for at least one row `h`, there is a linkage of all
three vertices of `B_h` to three vertices of the four-clique `Q_h`, with
internal vertices in `P_h`, such that the component containing the unused
fourth clique vertex has neighbours at both marked vertices in `W-z_h`.

This formulation is strictly local and is suitable for a standard
linkage/bridge attack.  A bare version for an arbitrary three-connected
graph is not justified: three-connectivity gives the terminalizing fan,
but does not by itself preserve two prescribed external contacts in the
unused component.  Any proof must use the full six-connectivity and the
marked-six-cut law, or return a smaller separator when the two contacts
are trapped on the fan.

The companion note
[`hc7_marked_three_clique_w3_one_mark_decoder.md`](hc7_marked_three_clique_w3_one_mark_decoder.md)
shows that either one of the two marked contacts can always be reserved by
a four-linkage, closes tails of order at most two, and gives a local
three-vertex packet pattern showing that the two one-mark linkages need
not synchronize from local incidence alone.  Thus the remaining issue is
genuinely simultaneous: compose the two one-mark near-`K_7` models, or use
the marked tail torso and the opposite shore to reserve both contacts.

For the actual inclusion-minimal three-edge contraction branch, the split
predecessor supplies that composition by a different mechanism: expanding
one marked vertex repairs the sole missing adjacency of a one-mark
near-model.  That stronger predecessor-level closure is recorded in
[`hc7_marked_three_clique_w3_predecessor_closure.md`](hc7_marked_three_clique_w3_predecessor_closure.md).
Accordingly, the reserved-hub lemma remains open only for the abstract
marked theorem without literal split-predecessor data.

Proved here:

* exact `3 by 3` row--cell incidence;
* connectedness of the three large cells;
* a disjoint terminalizing three-fan in every row;
* an unconditional literal `K_6`; and
* a literal `K_7` whenever one fan has a two-mark reserved hub;
* immediate closure when some row has three clique vertices on its
  boundary; and
* a strict inward three-cut whenever a nonterminal gate has no two-fan to
  the tail clique; and
* a two-connected literal tail plus a three-connected completed-mark
  torso.

Not proved here:

* the reserved-hub three-fan lemma;
* exclusion of the balanced `|W|=3` cell in the abstract marked setting; or
* the marked three-clique theorem.
