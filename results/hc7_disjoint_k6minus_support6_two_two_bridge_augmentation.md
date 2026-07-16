# Bridge augmentation for the minimal `2+2` contact form

**Status:** written proof; independently audited in
[`hc7_disjoint_k6minus_support6_two_two_bridge_augmentation_audit.md`](hc7_disjoint_k6minus_support6_two_two_bridge_augmentation_audit.md).
This note treats
the second minimal irredundant six-vertex support from the exact finite
linkage classification.  It proves a clean augmenting-path decoder, an
exact two-path separator relation, two crossed-linkage decoders, and two
four-terminal web certificates.  A previous revision incorrectly described
the second crossed linkage as a reversible endpoint transposition.  In fact,
the crossing produces a rooted `K_4` minor and hence a `K_7` minor in the
present configuration.  The two web certificates have not yet been
compressed into one six-terminal theorem.  This note does not prove the
support-six transversal theorem or `HC_7`.

## 1. Canonical configuration

Let `G` be a seven-connected graph.  Suppose that it contains two disjoint
six-vertex subgraphs on

\[
 A=\{a_0,a_1,a_2,a_3,x,y\},\qquad
 B=\{b_0,b_1,b_2,r,p,q\}.
\]

Assume the following edges.

- The set `Q={a_0,a_1,a_2,a_3}` is a clique, `xy` is an edge,
  \[
       N_Q(x)=\{a_0,a_1\},\qquad N_Q(y)=\{a_2,a_3\}.
                                                               \tag{1.1}
  \]
- Every pair of vertices of `B` is adjacent except possibly `p,q`.

Suppose there are six pairwise vertex-disjoint paths, internally disjoint
from `A\cup B`, with ends

\[
\begin{array}{lll}
 P_0:a_0\mathbin{-}p,&
 P_1:a_1\mathbin{-}b_0,&
 P_2:a_2\mathbin{-}b_1,\\
 P_3:a_3\mathbin{-}b_2,&
 P_4:x\mathbin{-}r,&
 P_5:y\mathbin{-}q.
\end{array}                                                   \tag{1.2}
\]

The paths are oriented from their first displayed end to their second.
Put

\[
 (s_2,t_2)=(a_2,b_1),\quad
 (s_3,t_3)=(a_3,b_2),\quad
 (s_4,t_4)=(x,r).                                      \tag{1.3}
\]

The missing right edge `pq` is aligned with the left nonedge `a_0y`.
This is the canonical `2+2` quotient survivor.  It is not a relabelling of
the `3+1` contact form: the unordered pair

\[
                    \{|N_Q(x)|,|N_Q(y)|\}
\]

is `{2,2}` here and `{3,1}` there, and is invariant under interchanging
`x,y` and relabelling the clique `Q`.

## 2. Three clean augmenting-path classes give a `K_7` minor

### Theorem 2.1 (oriented clean augmenting path)

Fix \(j\in\{2,3,4\}\).  Suppose that a path `R` has one end

\[
                    u\in V(P_1-b_0)
\]

and the other end

\[
                    v\in V(P_j-s_j),
\]

and that its interior is disjoint from `A`, `B`, and all six paths in
(1.2).  Then `G` has a `K_7` minor.

#### Proof

Let `u^+` be the neighbour of `u` on `P_1` toward `b_0`, and let `v^-`
be the neighbour of `v` on `P_j` toward `s_j`.  They exist because
`u\ne b_0` and `v\ne s_j`.  Define

\[
\begin{aligned}
 S_L&=P_1[a_1,u]\cup(R-v),&
 S_R&=P_1[u^+,b_0]\cup\{q\},\\
 T_L&=P_j[s_j,v^-]\cup(P_5-q),&
 T_R&=P_j[v,t_j].
\end{aligned}                                                \tag{2.1}
\]

The set `S_L` is connected through `u`; `S_R` is connected by the edge
`b_0q`; and `T_L` is connected because `s_jy` is an edge for each
\(j\in\{2,3,4\}\).  Let `k,l` be the other two members of `{2,3,4}`.  The
seven branch sets are

\[
 \boxed{P_0,\quad S_L,\quad P_k,\quad P_l,\quad
        T_L,\quad S_R,\quad T_R.}                       \tag{2.2}
\]

They are pairwise disjoint and connected.  The following edges give the
adjacencies involving `S_L`:

\[
\begin{array}{c|cccccc}
 &P_0&P_k&P_l&T_L&S_R&T_R\\ \hline
S_L&a_1a_0&a_1s_k&a_1s_l&a_1s_j&uu^+&
      \text{the last edge of }R\text{ at }v.
\end{array}                                                  \tag{2.3}
\]

Here `a_1s_h` means a clique edge when `h=2,3` and the edge `a_1x`
when `h=4`.  The branch set `P_0` is adjacent to `P_k,P_l,T_R` through
the right-side edges incident with `p`, to `T_L` through `a_0s_j`, and
to `S_R` through `pb_0`.

All adjacencies among `P_k,P_l,T_R,S_R` are supplied by the clique
`B-\{p,q\}` together with the edges from `q` to `b_0,b_1,b_2,r`.  The
sets `T_L,S_R` are adjacent along the final edge of `P_5`, and `T_L,T_R`
are adjacent along `v^-v`.  Finally, `T_L` is adjacent to `P_k,P_l` as
follows:

\[
\begin{array}{c|cc}
j&\text{edge to }P_k&\text{edge to }P_l\\ \hline
2&a_2a_3&yx\\
3&a_3a_2&yx\\
4&ya_2&ya_3.
\end{array}                                                  \tag{2.4}
\]

Thus every pair in (2.2) is adjacent, so (2.2) is an explicit
`K_7`-minor model.  \(\square\)

## 3. Seven-connectivity leaves exactly two exceptional paths

Put

\[
 Z=(A-\{a_1\})\cup\{b_0\},\qquad H=G-Z,                 \tag{3.1}
\]

and in `H` define

\[
\begin{aligned}
 U&=V(P_1-b_0),\\
 T&=\bigcup_{j=2}^{4}V(P_j-s_j),\\
 X&=V(P_0-a_0)\cup V(P_5-y).
\end{aligned}                                                \tag{3.2}
\]

### Theorem 3.1 (forced return and separator)

At least one of the following holds:

1. `G` has a `K_7` minor; or
2. `X` separates `U` from `T` in `H`.

More precisely, seven-connectivity supplies a path with one end in `U`
and the other in one of the five paths comprising `T\cup X`, whose
interior avoids `A`, `B`, and all paths in (1.2).  In a
`K_7`-minor-free graph its second end must lie in `X`.

#### Proof

The set `Z` has order six, so `H` is connected.  The set `U` is nonempty
and connected.  The set `T\cup X` is connected: it contains all vertices
of `B-b_0`, which induces a connected `K_5^-`, and every truncated path
in its definition ends in `B-b_0`.  Choose a shortest `U`--`(T\cup X)`
path in `H`.  Its interior avoids these two sets.  All vertices of the
six displayed paths and of `A\cup B` lie in `U\cup T\cup X\cup Z`, so
the path has the asserted cleanliness.  If its second end lies in `T`,
Theorem 2.1 gives a `K_7` minor.  Thus a `K_7`-minor-free graph forces the
second end into `X`.

If `H-X` contained a `U`--`T` path, shorten it at its first and last
contacts.  Its interior would avoid `U\cup T\cup X`, hence all the
displayed paths and support vertices.  Theorem 2.1 would again give a
`K_7` minor.  Therefore `X` separates `U` from `T`.  \(\square\)

As in the `3+1` form, this is a separator by two named paths, not a
bounded-order separator.  A minimum `U`--`T` separator in `H` either has
order one, yielding an actual order-seven separation after restoring `Z`,
or Menger's theorem gives at least two disjoint `U`--`T` paths through
`X`.

## 4. Both crossed augmentations close

### Theorem 4.1 (transposing `P_1` and `P_5`)

Suppose there are two vertex-disjoint paths `Q_1,Q_5`, internally
disjoint from the other four paths in (1.2) and from `A\cup B`, except
for their four prescribed ends, such that

\[
                  Q_1:a_1\mathbin{-}q,\qquad
                  Q_5:y\mathbin{-}b_0.                 \tag{4.1}
\]

Then `G` has a `K_7` minor.

#### Proof

The seven branch sets

\[
 \boxed{
 P_0,\quad Q_1,\quad
 (P_2-b_1)\cup(Q_5-b_0),\quad
 P_3,\quad P_4,\quad\{b_0\},\quad\{b_1\}}
                                                               \tag{4.2}
\]

are pairwise disjoint and connected; the third is connected by `a_2y`.
It is adjacent to the last two singleton sets along the final edges of
`Q_5` and `P_2`.  The only missing adjacency among the right ends of the
first five sets is `pq`, between `P_0` and `Q_1`, and it is supplied by
the clique edge `a_0a_1`.  The third branch set is adjacent to
`P_0,Q_1,P_3,P_4` through `a_2a_0,a_2a_1,a_2a_3,yx`, respectively.  Finally
`b_0,b_1` are adjacent to each other and to all four relevant right ends.
Thus (4.2) is a `K_7`-minor model.  \(\square\)

### Corollary 4.2 (crossed `P_1`--`P_5` bridges)

Suppose two pairwise vertex-disjoint paths `R_1,R_2` join `P_1` to
`P_5`, have four distinct ends, and have interiors disjoint from `A`,
`B`, and all six paths in (1.2).  Write \(u_i\in V(P_1)\) and
\(v_i\in V(P_5)\) for the ends of `R_i`.  If `u_1,u_2` occur in this order
from `a_1` to `b_0`, while `v_2,v_1` occur in this order from `y` to `q`,
then `G` has a `K_7` minor.

#### Proof

The paths

\[
\begin{aligned}
 Q_1&=P_1[a_1,u_1]\cup R_1\cup P_5[v_1,q],\\
 Q_5&=P_5[y,v_2]\cup R_2\cup P_1[u_2,b_0]
\end{aligned}
\]

are vertex-disjoint and meet the hypotheses of Theorem 4.1.  \(\square\)

### Corollary 4.3 (one web certificate)

Let

\[
 D_5=\left((A\cup B)\cup
       \bigcup_{\ell\notin\{1,5\}}V(P_\ell)\right)
       \setminus\bigl(V(P_1)\cup V(P_5)\bigr),
 \qquad H_5=G-D_5.                                      \tag{4.3}
\]

If `G` is `K_7`-minor-free, then `H_5` embeds as a spanning subgraph of a
`4`-web with frame

\[
                         (a_1,b_0,q,y).                 \tag{4.4}
\]

#### Proof

A crossing of the ordered tuple in (4.4) consists of disjoint paths
`a_1`--`q` and `b_0`--`y`.  The definition of `H_5` makes them eligible
as `Q_1,Q_5` in Theorem 4.1, which would give a `K_7` minor.  The tuple is
therefore crossless.  The Generalised Two Paths Theorem supplies a web
completion with the specified frame.  \(\square\)

### Theorem 4.4 (transposing `P_0` and `P_1`)

Suppose there are two vertex-disjoint paths `Q_0,Q_1`, internally
disjoint from `P_2,P_3,P_4,P_5` and from
`(A\cup B)-\{a_0,a_1,b_0,p\}`, such that

\[
                  Q_0:a_0\mathbin{-}b_0,\qquad
                  Q_1:a_1\mathbin{-}p.                 \tag{4.5}
\]

Then `G` has a `K_7` minor.

#### Proof

The paths `P_0,P_1` together with the edges `a_0a_1` and `pb_0` form a
cycle `C` on which

\[
                         a_0,a_1,b_0,p                 \tag{4.6}
\]

occur in this cyclic order.  The paths `Q_0,Q_1` form an
`(a_0b_0,a_1p)`-linkage.  Apply Fabila-Monroy and Wood's rooted-`K_4`
cycle-linkage lemma to the subgraph `C\cup Q_0\cup Q_1`.  It gives four
pairwise disjoint, pairwise adjacent connected branch sets
`L_0,L_1,R_0,R_p`, containing `a_0,a_1,b_0,p`, respectively.  By the
disjointness hypothesis, these branch sets avoid `P_2,P_3,P_4,P_5`.

Add the three connected branch sets

\[
                         P_2\cup P_5,\qquad P_3,\qquad P_4.       \tag{4.7}
\]

The first is connected by the edge `a_2y`.  The three sets in (4.7) are
pairwise adjacent: use `a_2a_3`, `b_1r`, and `b_2r`.  Each of the four
rooted branch sets is adjacent to each set in (4.7).  For `L_0,L_1`, use
the left-side edges from `a_0,a_1` to `a_2,a_3,x`; for `R_0,R_p`, use the
right-side edges from `b_0,p` to `b_1,b_2,r`.  Thus the four rooted branch
sets and the three sets in (4.7) form a `K_7`-minor model.  \(\square\)

### Corollary 4.5 (crossed `P_0`--`P_1` bridges)

Suppose two pairwise vertex-disjoint paths `R_1,R_2` join `P_1` to
`P_0`, have four distinct ends, and have interiors disjoint from `A`,
`B`, and all six paths in (1.2).  Orient the paths as in (1.2), and write
the ends so that

\[
 a_1,u_1,u_2,b_0\quad\hbox{occur in this order on }P_1,
\]

\[
 a_0,v_2,v_1,p\quad\hbox{occur in this order on }P_0,
\]

with `R_i` joining `u_i` to `v_i`.  Then `G` has a `K_7` minor.

#### Proof

The paths

\[
\begin{aligned}
 Q_0&=P_0[a_0,v_2]\cup R_2\cup P_1[u_2,b_0],\\
 Q_1&=P_1[a_1,u_1]\cup R_1\cup P_0[v_1,p]
\end{aligned}
\]

are vertex-disjoint and satisfy Theorem 4.4.  \(\square\)

### Corollary 4.6 (second web certificate)

Let

\[
 D_0=\left((A\cup B)\cup
       \bigcup_{\ell\notin\{0,1\}}V(P_\ell)\right)
       \setminus\bigl(V(P_0)\cup V(P_1)\bigr),
 \qquad H_0=G-D_0.                                      \tag{4.8}
\]

If `G` is `K_7`-minor-free, then `H_0` embeds as a spanning subgraph of a
`4`-web with frame

\[
                         (a_0,a_1,b_0,p).               \tag{4.9}
\]

#### Proof

A crossing of the ordered tuple in (4.9) consists of disjoint paths
`a_0`--`b_0` and `a_1`--`p`.  The definition of `H_0` makes them eligible
as `Q_0,Q_1` in Theorem 4.4, which would give a `K_7` minor.  The tuple is
therefore crossless, and the Generalised Two Paths Theorem supplies the
claimed web completion.  \(\square\)

### 4.7 Why the two certificates are not yet one six-terminal theorem

The natural common cyclic order is

\[
                  (a_0,a_1,y,q,b_0,p).                 \tag{4.10}
\]

It restricts to the frames in (4.4) and (4.9), up to cyclic reversal.  An
exploratory, unpromoted computation on the contracted twelve-vertex
quotient found that adding the two edges of any one of the fifteen
crossings of (4.10) creates a `K_7` minor.  This finite evidence is not
used in any proved claim here: an arbitrary crossing linkage may meet the
interiors of `P_0,P_1,P_5`, and a quotient certificate using two added
edges need not lift label-faithfully through those intersections.

Accordingly, the proved residual is the simultaneous existence of the two
web certificates (4.4) and (4.9), sharing the path `P_1`.  A genuine
six-terminal compression requires a decoder for all fifteen arbitrary
crossing-linkage types in (4.10), not only the two types handled by
Theorems 4.1 and 4.4.

## 5. Source and trust boundary

The finite normal forms are recorded
in
[`hc7_disjoint_k6minus_support6_linkage_classifier.md`](../results/hc7_disjoint_k6minus_support6_linkage_classifier.md).
The proofs of Theorems 2.1, 3.1, 4.1, and 4.4 are independent of that
computation once the canonical form (1.2) has been selected.

The external structural inputs in Corollaries 4.3 and 4.6 and
Theorem 4.4 are:

- S. Humeau and D. Pous, *On the Two Paths Theorem and the Two Disjoint
  Paths Problem*, [arXiv:2505.16431](https://arxiv.org/abs/2505.16431),
  Theorem 1.3 and the web-completion equivalence in Section 5.
- R. Fabila-Monroy and D. R. Wood, *Rooted `K_4`-Minors*,
  *Electronic Journal of Combinatorics* 20(2) (2013), P64,
  [doi:10.37236/3476](https://doi.org/10.37236/3476), Lemma 7.

The completion edges of the resulting web are not host edges.  The exact
next problem is to combine the two overlapping four-terminal web
certificates without treating completion edges as host edges.  The finite
six-terminal quotient check in Section 4.7 does not discharge this
label-preserving composition problem.
