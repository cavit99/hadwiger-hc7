# The balanced `|W|=3` cell: one-mark decoder and the first packet closures

**Status:** proved local lemmas, independently cold-audited in
[`hc7_marked_three_clique_w3_one_mark_decoder_audit.md`](hc7_marked_three_clique_w3_one_mark_decoder_audit.md).
These lemmas do not close the generic marked cell.  Their exact residual
is the simultaneous two-mark compatibility problem in Section 5.  In the
actual minimal-three-contraction branch, the separate predecessor-
splitting theorem closes this residual.

## 1. Standing interface

Let `H` be six-connected and `K_7`-minor-free.  Let

\[
                 W=\{z_1,z_2,z_3\}
\]

be the three marked vertices in the balanced `|W|=3` equality cell of the
marked Mader certificate.  Use the following consequences of that cell.

* There are three disjoint connected large-cell bags `Y_1,Y_2,Y_3`.
* There are disjoint rows `B_i=\{b_{i1},b_{i2},b_{i3}\}` with
  `b_{ij} in Y_j`.
* For every `i`, the set `S_i=W union B_i` is a six-cut.  Its row-tail
  `P_i=A_i-B_i` is one component of `H-S_i`, and
  `N_H(P_i)=S_i`.
* The three `P_i` are pairwise disjoint and anticomplete.
* Each `P_i` is disjoint from `Y_1 union Y_2 union Y_3`: the source
  inclusion `A_i subseteq union_j X_j` and the definition of `B_i` put
  `A_i-B_i` entirely in the residual singleton `X`-cells.
* If `Q_i=L_i-z_i`, then `Q_i` is a literal `K_4` contained in
  `P_i union B_i`.

The connectedness of the `Y_j` follows from the secondary maximality of
the Mader certificate: a disconnected `Y_j` can be split into its
components without increasing the floor budget.  The one-vertex
row--cell incidences follow from the usual symmetric-difference cut.

Fix a row `i`, and write the other two indices as `a,b`.  Put

\[
                        Q=Q_i,\qquad B=B_i,\qquad P=P_i.
\]

For `k in {a,b}` put `D_k=P_k union {z_k}`.  Each `D_k` is connected.
Moreover, `D_a,D_b` are adjacent to one another, to `{z_i}`, and to every
large cell: use the fullness of `P_a,P_b` at the appropriate literal
vertices of `W` and `B_a,B_b`.

## 2. A one-mark linkage always exists

### Lemma 2.1 (one-mark terminalization)

For either `c in {a,b}`, there are four mutually disjoint paths, with
distinct initial vertices equal to the four vertices of `Q` and distinct
final vertices equal to

\[
                              B union \{z_c\},
\]

such that every nontrivial path has all internal vertices in `P`.

### Proof

Let `d` be the other member of `{a,b}`.  The graph

\[
                              H-\{z_i,z_d\}
\]

is four-connected.  Take the trivial path at every vertex of
`I=Q cap B`.  After deleting `I`, set-Menger supplies
`4-|I|` disjoint paths between `Q-I` and
`(B union {z_c})-I`, with distinct ends.  Shorten each path at its first
vertex in the target set.

Every nontrivial initial vertex lies in `Q-B subseteq P`.  The only
neighbours of `P` outside `P` lie in `W union B`; after `z_i,z_d` have
been deleted, the first possible exit is therefore a member of
`B union {z_c}`.  The shortened path consequently has all internal
vertices in `P`.  \(\square\)

The three paths ending in `B` can be absorbed into the corresponding
large-cell bags.  Call the resulting bags `C_1,C_2,C_3`.  They are
connected and pairwise adjacent, because their three initial vertices
are distinct members of the clique `Q`.  The fourth path, with its final
vertex `z_c` omitted, is a connected bag `R_c`.  Its initial vertex is the
unused member of `Q`, so `R_c` is adjacent to all three `C_j` and to
`{z_i}`.

### Corollary 2.2 (a labelled near-`K_7` model)

The seven bags

\[
                 C_1,C_2,C_3,\ R_c,\ \{z_i\},\ D_a,D_b
\]

have every pairwise adjacency except possibly

\[
                              R_cD_d,
\]

where `d={a,b}-{c}`.  In particular, every live `|W|=3` cell has two
literal labelled `K_7^-` models, one for each choice of the supported
outside mark.

### Proof

The observations preceding Lemma 2.1 give all adjacencies involving
`D_a,D_b` except the displayed possible one.  The endpoint edge of the
fourth path joins `R_c` to `z_c in D_c`.  The clique `Q` supplies all
adjacencies among `R_c,C_1,C_2,C_3`, and `z_i` is complete to `Q` in the
literal clique `L_i`.  \(\square\)

Thus ordinary fan existence is not the open issue.  The exact issue is to
make the unused `Q`-root component contact **both** other marked packets in
one terminalization, or to compose the two labelled near-models.

## 3. A terminal row closes immediately

### Lemma 3.1

If `|Q cap B|=3`, then the balanced cell contains a literal `K_7` model.

### Proof

Let `q` be the unique member of `Q-B`.  Use the three original connected
large-cell bags `Y_1,Y_2,Y_3`.  They are pairwise adjacent through the
three vertices of `Q cap B`, which form a triangle.  Use `P` as a fourth
bag.  It is connected, it contacts both `z_a,z_b` by `S_i`-fullness, and
it contacts every `Y_j` through the edge from `q` to the member of
`Q cap B` in that cell.  The remaining three bags are

\[
                            \{z_i\},D_a,D_b.
\]

The literal clique `L_i` and the fullness observations in Section 1 give
all remaining adjacencies.  These seven bags form a `K_7` model.  \(\square\)

## 4. Tails of order at most two close

### Lemma 4.1

If `|P|<=2`, then the balanced cell contains a literal `K_7` model.

### Proof

Since `Q` has four vertices and `B` has three, `|P|=1` forces
`|Q cap B|=3`, and Lemma 3.1 applies.  The same is true when `|P|=2` and
`|Q cap B|=3`.

It remains to consider `|P|=2` and `|Q cap B|=2`.  Write

\[
 Q cap P=\{q,q'\},\qquad Q cap B=\{u_1,u_2\},
 \qquad B-(Q cap B)=\{u_3\}.
\]

The two vertices `q,q'` are adjacent.  Each has the four fixed neighbours

\[
                  q'\text{ (or }q\text{)},\ z_i,\ u_1,\ u_2.
\]

It has no neighbour outside `P union S_i`.  Six-connectivity gives
minimum degree at least six.  If, say, `q` missed `z_a`, it would have to
see at least two of `z_b,u_3`; hence it would see both, have degree exactly
six, and `N_H(q)` would be a six-cut omitting the marked vertex `z_a`.
This contradicts the marked-cut law.  Thus both `q` and `q'` see both
`z_a,z_b`.

Since `P` is `S_i`-full, at least one of `q,q'`, say `q`, sees `u_3`.
Use the trivial paths at `u_1,u_2` and the edge `qu_3` as the three
terminalizing paths.  Absorb `q` into the large-cell bag containing
`u_3`; the three augmented cell bags are pairwise adjacent through the
clique `\{u_1,u_2,q\}`.  Use `{q'}` as the reserved hub.  It contacts both
`D_a,D_b`, all three augmented cells, and `{z_i}`.  Together with
`{z_i},D_a,D_b`, these are seven pairwise adjacent connected bags.
\(\square\)

Consequently every surviving tail has order at least three and every row
satisfies `|Q_i cap B_i|<=2`.

## 5. Exact residual and a local guardrail

Corollary 2.2 reduces the live packet question to synchronizing the two
one-mark terminalizations.  This synchronization is not a consequence of
the local packet incidence and marked minimum-degree facts alone.

For example, take

\[
 Q=\{u_1,q_1,q_2,q_3\}\cong K_4,
 \qquad B=\{u_1,u_2,u_3\},
 \qquad P=\{q_1,q_2,q_3\}\cong K_3.
\]

Make every `q_t` adjacent to `z_i,u_2,u_3`.  Let `z_a` see `q_1,q_2` and
let `z_b` see `q_3`, with no `q_t` seeing both outside marks.  The packet
is full to `W union B`, every `q_t` has seven neighbours in this local
interface, and each one-mark terminalization exists.  But every root-clean
terminalization of all three `B`-vertices (one shortened at its first
target and last `Q`-root) uses two of `q_1,q_2,q_3` as column roots and
leaves the third as the reserved root; that root contacts only one outside
mark.  Hence no common two-mark reserved root exists within this minimal
linkage language.

This is an interface guardrail, not a six-connected `K_7`-minor-free host
and not a counterexample to the marked theorem.  It proves that the next
lemma must use at least one genuinely global input: the opposite shore,
the other two row packets, `K_7`-minor exclusion, or a state/model
composition between the two near-`K_7` models.  Repeating one-mark Menger
alone cannot close the cell.
