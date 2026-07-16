# Cold audit of the marked three-clique `|W|=2` closure

**Verdict: GREEN.** The proof in
[`hc7_marked_three_clique_w2_closure.md`](hc7_marked_three_clique_w2_closure.md)
is valid under its stated standing cell. Every use of the Mader certificate
matches the definitions and claims in
[`hc7_marked_three_clique_cut_reduction.md`](hc7_marked_three_clique_cut_reduction.md)
and Niu's dissertation, Chapter 3, claims 3.2.4--3.2.18. The proof does not
use the claw-free conclusions later in Niu's argument.

This audit checks the standing equality data, singleton residue, cell
equality, symmetric-difference separator, degree envelope, marked
neighbourhood cuts, binary shore, and all seven branch-set adjacencies.

## 1. Source dictionary and equality cell

The source certificate supplies:

1. a partition `Y_1,...,Y_n` of `V(H)-W`, with `X_j subseteq Y_j`;
2. the budget
   \[
        |W|+\sum_j\left\lfloor |X_j|/2\right\rfloor\le6;
   \]
3. no edge from `Y_j-X_j` to
   `V(H)-(W union Y_j)`;
4. the auxiliary graph obtained from `H-W` by deleting every edge with
   both ends in one `Y_j`; and
5. disjoint sets `A_i`, each a union of auxiliary components and containing
   `L_i-W`, with `A_i subseteq union_j X_j`.

The balanced `|W|=2` equality branch has `m=4`, four sets `X_j` of order
three, and three disjoint sets `B_i` of order four contained in their
union. The four cells have total order twelve and the three rows have total
order twelve. Therefore

\[
 X_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}X_4
 =B_1\mathbin{\dot\cup}B_2\mathbin{\dot\cup}B_3.
\]

The budget is already tight:

\[
 2+4\left\lfloor3/2\right\rfloor=6.
\]

Every other nonempty `X_j` has odd order by source claim 3.2.12 and
contributes zero to the remaining budget, so it is a singleton. This
verifies (1.5) and the singleton assertion.

The cut-reduction note correctly derives that exactly one row has a tail.
After relabelling it is row one. Its six-cut `W union B_1` contains all
three marks; disjointness of the `A_i` forces the other two marks into `W`.
Thus

\[
 W=\{z_2,z_3\},\qquad z_1\in B_1.
\]

The two tail-free rows satisfy `A_i=B_i`. Since `L_i-W subseteq A_i` and
both sets have order four, this gives

\[
 A_2=B_2=L_2-z_2,\qquad A_3=B_3=L_3-z_3.
\]

Hence all data in (1.2)--(1.5) are justified by the prior reduction.

## 2. Cell equality and the symmetric-difference cut

For each of the four large cells,

\[
                         |W union X_j|=2+3=5<6.
\]

If `Y_j-X_j` were nonempty, source claim 3.2.10 would make
`W union X_j` a separator. Six-connectivity therefore gives `Y_j=X_j`,
exactly as claimed.

Fix a row `B_i`, a large cell `X_j`, and put
`R=B_i cap X_j`. If `|R|>=2`, set

\[
                         T=W\cup(B_i\mathbin\triangle X_j).
\]

After deleting `T`, no edge leaves

\[
                         R\cup(A_i-B_i).             \tag{2.1}
\]

Indeed:

* an edge from `R` to outside `X_j` is not cell-internal, so it remains in
  the auxiliary graph; its non-`W` end lies in the same auxiliary
  component and hence in `A_i`;
* the vertices of `B_i-X_j` have been deleted;
* every vertex of `A_i-B_i` lies in a residual singleton `X`-cell;
  that cell equals its `Y`-cell because its union with `W` has order three;
  hence every non-`W` edge at that vertex survives in the auxiliary graph
  and remains inside `A_i`; and
* the only undeleted vertices of `A_i` are precisely (2.1).

The set (2.1) is nonempty. A different row `B_k` has order four, whereas
`X_j` has order three, so a vertex of `B_k-X_j` survives on the other side.
Thus `T` is a genuine separator. Its order is

\[
 |T|=2+4+3-2|R|\le5,
\]

contrary to six-connectivity. Consequently every intersection has order
at most one. Each row has four vertices distributed over four cells, so
all twelve intersections have order exactly one. Lemma 2.1 is GREEN.

## 3. Neighbour envelopes and marked six-cuts

Fix `x=x_{2j}`. Because `Y_j=X_j`, every edge from `x` to outside `X_j`
survives in the auxiliary graph. Its non-`W` endpoint is in the same
auxiliary component as `x`, hence in `A_2=B_2`. Inside `X_j`, Lemma 2.1
leaves only `x_{1j}` and `x_{3j}`. Therefore

\[
 N_H(x)\subseteq
 (B_2-\{x\})\cup\{z_2,z_3\}\cup\{x_{1j},x_{3j}\}.  \tag{3.1}
\]

The seven displayed vertices are distinct. The clique `L_2` gives the
four neighbours `(B_2-{x}) union {z_2}`. Six-connectivity gives
`d_H(x)>=6`.

If `d_H(x)=7`, equality holds in (3.1) and every displayed contact exists.
If `d_H(x)=6`, then `N_H(x)` is a six-separator: its deletion isolates
`x`, while at least one vertex remains outside `N_H[x]` because the three
disjoint five-cliques give at least fifteen vertices. The marked-cut law
therefore puts `z_1,z_2,z_3` in `N_H(x)`.

This has the exact consequences used in the proof:

* `xz_3` always exists;
* when `j=j_0`, the degree-six case forces `xz_1`, while degree seven also
  gives it; and
* when `j!=j_0`, `z_1` is absent from the seven-vertex envelope, so degree
  six is impossible and `x` sees the entire envelope, including
  `x_{3j}`.

Repeating the same argument with rows two and three exchanged gives
`z_2` complete to `B_3`, the two `z_1` contacts in cell `j_0`, and all
cross-row edges `x_{2j}x_{3j}` for `j!=j_0`. It also confirms that both
vertices of `W` are complete to both `B_2` and `B_3`. Lemma 3.1 is GREEN.

## 4. Binary shore and the split path

The set

\[
                           S=W\cup B_1
\]

has order six and is a separator by source claim 3.2.16, because
`A_1-B_1` is nonempty. It contains all three marks. The binary minimum-cut
corollary in the reduction note therefore applies and says that `H-S` has
exactly two components.

All of `A_1-B_1` lies in one component `P`: source claim 3.2.16 puts every
such vertex opposite the nonempty set `V(H)-A_1-W`, and two tail components
would produce at least three components of `H-S`. Disjointness of the
`A_i` puts `B_2 union B_3` in the opposite shore, so `P` contains neither
row.

The component `P` is `S`-full. Its open neighbourhood is contained in
`S`; if it omitted one member of `S`, that neighbourhood would have order
at most five and separate `P` from the other component. Thus both `z_2`
and `z_3` have neighbours in the connected graph `P`. Joining those two
neighbours inside `P` yields a `z_2-z_3` path whose internal vertices lie
in `P`. Splitting this path across an edge produces disjoint connected
bags `D_2,D_3`, containing `z_2,z_3` respectively, with an edge between
them.

## 5. Complete branch-set audit

The seven proposed bags are

\[
 K_j=\{x_{2j}\}\quad(1\le j\le4),\qquad
 D_2,\quad D_3,\quad C=B_3\cup\{z_1\}.
\]

### Disjointness and connectedness

* The four `K_j` are distinct singleton vertices of `B_2`.
* The path bags `D_2,D_3` are disjoint connected subpaths, use only
  `z_2,z_3` and vertices of `P`, and are adjacent across the split edge.
* The bag `C` is disjoint from the preceding bags because
  `B_1,B_2,B_3,W,P` are pairwise disjoint in the required combinations.
* The clique `B_3` is connected, and `z_1x_{3j_0}` joins `z_1` to it, so
  `C` is connected.

### All pairwise adjacencies

There are exactly the following types.

1. `K_j-K_k` for `j!=k`: the four vertices form the clique
   `B_2=L_2-z_2`.
2. `D_2-K_j`: use `z_2x_{2j}`, an edge of `L_2`.
3. `D_3-K_j`: use `z_3x_{2j}`, supplied by Lemma 3.1.
4. `C-K_j` for `j!=j_0`: use `x_{3j}x_{2j}`.
5. `C-K_{j_0}`: use `z_1x_{2j_0}`.
6. `D_2-D_3`: use the selected split edge of the path.
7. `D_2-C`: use any edge `z_2x_{3j}`, since `z_2` is complete to `B_3`.
8. `D_3-C`: use any edge `z_3x_{3j}` of the clique `L_3`.

These account for all twenty-one unordered pairs of seven bags. Hence the
bags form a literal `K_7` model, contradicting the standing exclusion.
Theorem 4.1 is GREEN.

## 6. Trust boundary

This audit proves only the balanced equality branch with `|W|=2`. It does
not establish the analogous closure for `3<=|W|<=5`, the complete marked
three-clique theorem, or the global support-six theorem. Its only
source-level inputs are the certificate axioms and arithmetic through
Niu's claims 3.2.4--3.2.18, plus the independently proved marked-cut and
binary-cut adaptations in the reduction note.
